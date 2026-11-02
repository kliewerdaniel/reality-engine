"""Database layer for Reality Engine.

Single source of truth for the SQLite schema and connection management.
All database operations are transactional.
"""

import hashlib
from typing import Optional, Type, Any, Literal
from uuid import uuid4
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

# ── SQL Schema ──────────────────────────────────────────────────────────────────

SCHEMA = """
-- Core tables
CREATE TABLE IF NOT EXISTS domains (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    canonical_name TEXT,
    description TEXT,
    parent_domain_id TEXT,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sources (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    source_type TEXT NOT NULL,
    canonical_domain TEXT,
    authority_metadata TEXT,
    collection_policy TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT
);

CREATE TABLE IF NOT EXISTS documents (
    id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL,
    source_native_id TEXT,
    canonical_url TEXT,
    content_hash TEXT,
    content_type TEXT,
    content TEXT NOT NULL,
    language TEXT,
    published_at TEXT,
    collected_at TEXT NOT NULL,
    processing_status TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    FOREIGN KEY (source_id) REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS entities (
    id TEXT PRIMARY KEY,
    canonical_name TEXT,
    entity_type TEXT,
    domain_id TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    status TEXT,
    FOREIGN KEY (domain_id) REFERENCES domains(id)
);

CREATE TABLE IF NOT EXISTS entity_aliases (
    id TEXT PRIMARY KEY,
    entity_id TEXT NOT NULL,
    alias TEXT NOT NULL,
    source_hint TEXT,
    normalized TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (entity_id) REFERENCES entities(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS observations (
    id TEXT PRIMARY KEY,
    observation_type TEXT,
    subject_id TEXT,
    observed_value TEXT,
    unit TEXT,
    valid_from TEXT,
    valid_to TEXT,
    recorded_at TEXT NOT NULL,
    source_id TEXT,
    document_id TEXT,
    provenance_reference TEXT,
    extraction_version TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    FOREIGN KEY (source_id) REFERENCES sources(id),
    FOREIGN KEY (document_id) REFERENCES documents(id),
    FOREIGN KEY (subject_id) REFERENCES entities(id)
);

CREATE TABLE IF NOT EXISTS events (
    id TEXT PRIMARY KEY,
    event_type TEXT NOT NULL,
    event_description TEXT,
    occurred_at TEXT,
    occurred_on TEXT,
    valid_from TEXT,
    valid_to TEXT,
    recorded_at TEXT NOT NULL,
    source_id TEXT,
    document_id TEXT,
    observation_ids TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (source_id) REFERENCES sources(id),
    FOREIGN KEY (document_id) REFERENCES documents(id)
);

CREATE TABLE IF NOT EXISTS claims (
    id TEXT PRIMARY KEY,
    subject_id TEXT NOT NULL,
    predicate TEXT NOT NULL,
    object_value TEXT NOT NULL,
    claim_type TEXT NOT NULL,
    domain_id TEXT NOT NULL,
    document_id TEXT NOT NULL,
    valid_from TEXT,
    valid_to TEXT,
    recorded_at TEXT NOT NULL,
    status TEXT NOT NULL,
    revision_number INTEGER DEFAULT 1,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    FOREIGN KEY (subject_id) REFERENCES entities(id),
    FOREIGN KEY (document_id) REFERENCES documents(id),
    FOREIGN KEY (domain_id) REFERENCES domains(id)
);

CREATE TABLE IF NOT EXISTS claim_versions (
    id TEXT PRIMARY KEY,
    claim_id TEXT NOT NULL,
    subject_id TEXT NOT NULL,
    predicate TEXT NOT NULL,
    object_value TEXT NOT NULL,
    claim_type TEXT NOT NULL,
    domain_id TEXT NOT NULL,
    document_id TEXT NOT NULL,
    valid_from TEXT,
    valid_to TEXT,
    recorded_at TEXT NOT NULL,
    status TEXT NOT NULL,
    revision_number INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (claim_id) REFERENCES claims(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS evidence_links (
    id TEXT PRIMARY KEY,
    claim_id TEXT NOT NULL,
    observation_id TEXT,
    source_span_id TEXT,
    relationship_type TEXT NOT NULL,
    explanation TEXT,
    assessment_status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (claim_id) REFERENCES claims(id),
    FOREIGN KEY (observation_id) REFERENCES observations(id),
    FOREIGN KEY (source_span_id) REFERENCES source_spans(id)
);

CREATE TABLE IF NOT EXISTS source_spans (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL,
    start_offset INTEGER NOT NULL,
    end_offset INTEGER NOT NULL,
    page INTEGER,
    paragraph TEXT,
    quoted_text TEXT NOT NULL,
    language TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (document_id) REFERENCES documents(id)
);

CREATE TABLE IF NOT EXISTS dependencies (
    id TEXT PRIMARY KEY,
    dependent_type TEXT NOT NULL,
    dependent_id TEXT NOT NULL,
    prerequisite_type TEXT NOT NULL,
    prerequisite_id TEXT NOT NULL,
    dependency_type TEXT NOT NULL,
    created_at TEXT NOT NULL,
    CHECK (
        (dependent_type = 'claim' AND prerequisite_type = 'claim') OR
        (dependent_type = 'claim' AND prerequisite_type = 'hypothesis') OR
        (dependent_type = 'hypothesis' AND prerequisite_type = 'claim') OR
        (dependent_type = 'hypothesis' AND prerequisite_type = 'hypothesis') OR
        (dependent_type = 'conclusion' AND prerequisite_type = 'claim') OR
        (dependent_type = 'conclusion' AND prerequisite_type = 'hypothesis') OR
        (dependent_type = 'conclusion' AND prerequisite_type = 'conclusion') OR
        (dependent_type = 'relationship' AND prerequisite_type = 'claim') OR
        (dependent_type = 'relationship' AND prerequisite_type = 'hypothesis') OR
        (dependent_type = 'relationship' AND prerequisite_type = 'conclusion')
    )
);

CREATE TABLE IF NOT EXISTS relationships (
    id TEXT PRIMARY KEY,
    type TEXT NOT NULL,
    subject_id TEXT NOT NULL,
    object_id TEXT NOT NULL,
    predicate TEXT,
    valid_from TEXT,
    valid_to TEXT,
    recorded_at TEXT NOT NULL,
    source_id TEXT,
    document_id TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES entities(id),
    FOREIGN KEY (object_id) REFERENCES entities(id),
    FOREIGN KEY (source_id) REFERENCES sources(id),
    FOREIGN KEY (document_id) REFERENCES documents(id)
);

CREATE TABLE IF NOT EXISTS revisions (
    id TEXT PRIMARY KEY,
    revision_type TEXT NOT NULL,
    trigger_observation_id TEXT,
    proposal_reference TEXT,
    validation_result TEXT NOT NULL,
    object_id TEXT NOT NULL,
    transaction_id TEXT,
    previous_claim_version_id TEXT,
    resulting_claim_version_id TEXT,
    previous_state_id TEXT,
    resulting_state_id TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (object_id) REFERENCES entities(id),
    FOREIGN KEY (previous_claim_version_id) REFERENCES claim_versions(id),
    FOREIGN KEY (resulting_claim_version_id) REFERENCES claim_versions(id)
);

CREATE TABLE IF NOT EXISTS source_lineage (
    id TEXT PRIMARY KEY,
    source_id_a TEXT NOT NULL,
    source_id_b TEXT NOT NULL,
    relationship_type TEXT NOT NULL,
    confidence REAL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS audit_events (
    id TEXT PRIMARY KEY,
    event_type TEXT NOT NULL,
    actor_type TEXT NOT NULL,
    actor_id TEXT NOT NULL,
    object_type TEXT NOT NULL,
    object_id TEXT NOT NULL,
    previous_hash TEXT,
    event_hash TEXT NOT NULL UNIQUE,
    payload_reference TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (previous_hash) REFERENCES audit_events(event_hash)
);

CREATE INDEX IF NOT EXISTS idx_sources_name ON sources(name);
CREATE INDEX IF NOT EXISTS idx_documents_source_id ON documents(source_id);
CREATE INDEX IF NOT EXISTS idx_documents_content_hash ON documents(content_hash);
CREATE INDEX IF NOT EXISTS idx_observations_source ON observations(source_id);
CREATE INDEX IF NOT EXISTS idx_observations_document ON observations(document_id);
CREATE INDEX IF NOT EXISTS idx_observations_subject ON observations(subject_id);
CREATE INDEX IF NOT EXISTS idx_claims_subject ON claims(subject_id);
CREATE INDEX IF NOT EXISTS idx_claims_document ON claims(document_id);
CREATE INDEX IF NOT EXISTS idx_claims_domain ON claims(domain_id);
CREATE INDEX IF NOT EXISTS idx_entities_canonical_name ON entities(canonical_name);
CREATE INDEX IF NOT EXISTS idx_entities_type ON entities(entity_type);
CREATE INDEX IF NOT EXISTS idx_entity_aliases_entity ON entity_aliases(entity_id);
CREATE INDEX IF NOT EXISTS idx_entity_aliases_alias ON entity_aliases(alias);
CREATE INDEX IF NOT EXISTS idx_source_spans_doc ON source_spans(document_id);
CREATE INDEX IF NOT EXISTS idx_revisions_state ON revisions(resulting_state_id);
CREATE INDEX IF NOT EXISTS idx_events_recorded ON events(recorded_at);
CREATE INDEX IF NOT EXISTS idx_events_source ON events(source_id);
CREATE INDEX IF NOT EXISTS idx_relationships_subject ON relationships(subject_id);
CREATE INDEX IF NOT EXISTS idx_relationships_object ON relationships(object_id);

-- Event → observation linkage (explicit, multi-valued via JSON)
CREATE INDEX IF NOT EXISTS idx_events_observation_ids ON events(observation_ids);

-- Bitemporal index: observations valid_from/valid_to
CREATE INDEX IF NOT EXISTS idx_observations_valid_time ON observations(valid_from, valid_to);

-- Bitemporal index: relationships valid_from/valid_to
CREATE INDEX IF NOT EXISTS idx_relationships_valid_time ON relationships(valid_from, valid_to);

-- Bitemporal index: events occurred_at
CREATE INDEX IF NOT EXISTS idx_events_occurred_at ON events(occurred_at);
"""

# ── Helpers ─────────────────────────────────────────────────────────────────────

def _uid(prefix: str) -> str:
    """Generate a unique identifier using uuid4 (collision-free)."""
    return f"{prefix}__{uuid4().hex}"


class _Transaction:
    """Context manager for atomic database transactions."""

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.conn.execute("PRAGMA busy_timeout = 5000")
        self._closed = False

    def __enter__(self) -> "_Transaction":
        self.conn.execute("BEGIN")
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Any, exc_tb: Any) -> Literal[False]:
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()
        return False


# ── Database class ─────────────────────────────────────────────────────────────

class Database:
    """SQLite database wrapper with transactional operations."""

    def __init__(self, path: Path):
        self.path = path
        self.conn = self._connect(path)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.conn.execute("PRAGMA journal_mode = WAL")
        self.conn.execute("PRAGMA busy_timeout = 5000")
        self.conn.executescript(SCHEMA)
        self.conn.commit()
        self.conn.row_factory = sqlite3.Row

    def _connect(self, path: Path) -> sqlite3.Connection:
        """Connect to the database.

        Accepts either a path-like object (str/Path) or a sqlite3.Connection.
        When a connection is provided, it is used directly; otherwise a new
        connection is opened at the given path.
        """
        if isinstance(path, sqlite3.Connection):
            return path
        return sqlite3.connect(str(path))

    def _now(self) -> str:
        return datetime.now(timezone.utc).isoformat()

    def transaction(self) -> "_Transaction":
        """Context manager for atomic database transactions.

        All database operations within the with block succeed or fail together.
        """
        return _Transaction(self.conn)

    # ── Domains ────────────────────────────────────────────────────────────────

    def register_domain(self, name: str, description: str) -> str:
        dom_id = _uid("dom")
        self.conn.execute(
            "INSERT INTO domains (id, name, canonical_name, description, created_at)"
            " VALUES (?, ?, ?, ?, ?)",
            (dom_id, name, name.lower(), description, self._now()),
        )
        self.conn.commit()
        return dom_id

    # ── Sources ────────────────────────────────────────────────────────────────

    def register_source(self, name: str, source_type: str, canonical_domain: str) -> str:
        src_id = _uid("src")
        self.conn.execute(
            "INSERT INTO sources (id, name, source_type, canonical_domain, created_at, updated_at)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (src_id, name, source_type, canonical_domain, self._now(), self._now()),
        )
        self.conn.commit()
        return src_id

    # ── Documents ───────────────────────────────────────────────────────────────

    def ingest_document(self, source_id: str, content: str, content_type: str,
                        language: str, published_at: str) -> str:
        doc_id = _uid("doc")
        content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        self.conn.execute(
            "INSERT INTO documents (id, source_id, source_native_id, canonical_url, content_hash,"
            " content_type, content, language, published_at, collected_at, processing_status, created_at, updated_at)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (doc_id, source_id, f"native_{doc_id}", "https://example.com/doc",
             content_hash, content_type, content, language, published_at,
             self._now(), "PROCESSED", self._now(), self._now()),
        )
        self.conn.commit()
        return doc_id

    # ── Source Spans ───────────────────────────────────────────────────────────

    def extract_source_span(self, document_id: str, quoted_text: str,
                             page: int, start_offset: int, end_offset: int) -> str:
        span_id = _uid("span")
        self.conn.execute(
            "INSERT INTO source_spans (id, document_id, start_offset, end_offset, page, quoted_text, created_at)"
            " VALUES (?, ?, ?, ?, ?, ?, ?)",
            (span_id, document_id, start_offset, end_offset, page, quoted_text, self._now()),
        )
        self.conn.commit()
        return span_id

    # ── Entities ───────────────────────────────────────────────────────────────

    def register_entity(self, canonical_name: str, entity_type: str,
                        domain_id: Optional[str] = None, aliases: Optional[list] = None) -> str:
        """Register an entity with optional aliases.

        Args:
            canonical_name: The canonical name of the entity.
            entity_type: The type of entity (e.g., 'COUNTRY', 'ORGANIZATION').
            domain_id: Optional domain classification.
            aliases: Optional list of alternate names (strings).

        Returns:
            The entity ID.
        """
        ent_id = _uid("ent")
        self.conn.execute(
            "INSERT INTO entities (id, canonical_name, entity_type, domain_id, created_at, status)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (ent_id, canonical_name, entity_type, domain_id, self._now(), "ACTIVE"),
        )
        if aliases:
            for i, alias in enumerate(aliases):
                ali_id = _uid(f"ali_{i}")
                normalized = alias.lower().strip()
                self.conn.execute(
                    "INSERT INTO entity_aliases (id, entity_id, alias, source_hint, normalized, created_at)"
                    " VALUES (?, ?, ?, ?, ?, ?)",
                    (ali_id, ent_id, alias, alias, normalized, self._now()),
                )
        self.conn.commit()
        return ent_id

    def resolve_entity(self, name: str, limit: int = 3) -> list[dict[str, Any]]:
        """Resolve an entity by canonical name or alias (case-insensitive).

        Args:
            name: The name to resolve (canonical or alias).
            limit: Maximum number of candidates to return.

        Returns:
            List of candidate entity dicts, ranked by match quality.
            Empty list if no match found.
        """
        normalized = name.lower().strip()
        if not normalized:
            return []

        # Query for exact match on canonical name (case-insensitive)
        canonical_matches = self.conn.execute(
            "SELECT e.id, e.canonical_name, e.entity_type, e.domain_id, e.created_at, e.status, 1 as rank"
            " FROM entities e"
            " WHERE lower(e.canonical_name) = ?"
            " ORDER BY e.created_at", (normalized,)
        ).fetchall()

        # Query for alias match (case-insensitive)
        alias_matches = self.conn.execute(
            "SELECT e.id, e.canonical_name, e.entity_type, e.domain_id, e.created_at, e.status, 2 as rank"
            " FROM entities e JOIN entity_aliases a ON a.entity_id = e.id"
            " WHERE lower(a.alias) = ?"
            " ORDER BY e.created_at", (normalized,)
        ).fetchall()

        # Combine and rank
        candidates = []
        for row in canonical_matches:
            c = dict(row)
            c["type"] = "canonical"
            candidates.append(c)
        for row in alias_matches:
            c = dict(row)
            c["type"] = "alias"
            candidates.append(c)

        # Sort by rank
        candidates.sort(key=lambda x: x["rank"])
        return [c for c in candidates[:limit]]

    def get_entity_by_id(self, entity_id: str) -> Optional[dict[str, Any]]:
        row = self.conn.execute("SELECT * FROM entities WHERE id = ?", (entity_id,)).fetchone()
        return dict(row) if row else None

    def get_entities_by_type(self, entity_type: str) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT * FROM entities WHERE entity_type = ? ORDER BY canonical_name", (entity_type,)
        ).fetchall()
        return [dict(r) for r in rows]

    def get_all_entities(self) -> list[dict[str, Any]]:
        rows = self.conn.execute("SELECT * FROM entities ORDER BY canonical_name").fetchall()
        return [dict(r) for r in rows]

    # ── Observations ───────────────────────────────────────────────────────────

    def register_observation(self, document_id: str, source_id: str,
                             subject_id: str, observed_value: str,
                             recorded_at: str, observation_type: str = "REPORT") -> str:
        obs_id = _uid("obs")
        self.conn.execute(
            "INSERT INTO observations (id, observation_type, subject_id, observed_value, recorded_at,"
            " source_id, document_id, created_at, updated_at)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (obs_id, observation_type, subject_id, observed_value, recorded_at,
             source_id, document_id, recorded_at, recorded_at),
        )
        self.conn.commit()
        return obs_id

    def get_observations_for_entity(self, entity_id: str) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT * FROM observations WHERE subject_id = ? ORDER BY recorded_at", (entity_id,)
        ).fetchall()
        return [dict(r) for r in rows]

    def get_source_span(self, span_id: str) -> dict:
        """Retrieve a source span by ID."""
        row = self.conn.execute(
            "SELECT * FROM source_spans WHERE id = ?", (span_id,)
        ).fetchone()
        return dict(row) if row else None

    def get_observations_by_source_span(self, source_span_id: str) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT o.* FROM observations o JOIN evidence_links el ON el.observation_id = o.id"
            " WHERE el.source_span_id = ? ORDER BY o.recorded_at", (source_span_id,)
        ).fetchall()
        return [dict(r) for r in rows]

    # ── Events ─────────────────────────────────────────────────────────────────

    def register_event(self, event_type: str, event_description: str,
                       occurred_at: str, occurred_on: str = None,
                       recorded_at: str = None, source_id: str = None,
                       document_id: str = None, observation_ids: str = None) -> str:
        """Register an event.

        Args:
            event_type: Type of event (e.g., 'DEBATE', 'SUPERSONIC_TEST', 'CORRECTION').
            event_description: Human-readable description.
            occurred_at: When the event occurred (ISO 8601).
            occurred_on: Short date (e.g., '2026-10-10').
            recorded_at: When the system recorded it (defaults to now).
            source_id: Optional source identifier.
            document_id: Optional document identifier.
            observation_ids: Comma-separated list of observation IDs.

        Returns:
            The event ID.
        """
        if recorded_at is None:
            recorded_at = self._now()
        evt_id = _uid("evt")
        self.conn.execute(
            "INSERT INTO events (id, event_type, event_description, occurred_at, occurred_on,"
            " recorded_at, source_id, document_id, observation_ids, created_at)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (evt_id, event_type, event_description, occurred_at, occurred_on,
             recorded_at, source_id, document_id, observation_ids, recorded_at),
        )
        self.conn.commit()
        return evt_id

    def get_events(self, event_type: Optional[str] = None, start_date: Optional[str] = None,
                   end_date: Optional[str] = None) -> list[dict[str, Any]]:
        """Query events by type and/or date range.

        Returns a list of event dictionaries.
        """
        query = "SELECT * FROM events WHERE 1=1"
        params = []
        if event_type:
            query += " AND event_type = ?"
            params.append(event_type)
        if start_date:
            query += " AND occurred_at >= ?"
            params.append(start_date)
        if end_date:
            query += " AND occurred_at <= ?"
            params.append(end_date)
        query += " ORDER BY recorded_at"
        rows = self.conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]

    # ── Relationships ──────────────────────────────────────────────────────────

    def register_relationship(self, relationship_type: str,
                              subject_id: str, object_id: str,
                              predicate: Optional[str] = None,
                              valid_from: Optional[str] = None, valid_to: Optional[str] = None,
                              recorded_at: Optional[str] = None,
                              source_id: Optional[str] = None, document_id: Optional[str] = None) -> str:
        """Register a typed relationship between entities.

        Args:
            relationship_type: The type of relationship (e.g., 'SUPPORTS', 'CONTRADICTS',
                             'CORRELATES_WITH', 'MEASURED_BY').
            subject_id: The subject entity ID.
            object_id: The object entity ID.
            predicate: Optional detailed predicate.
            valid_from: Valid time interval start (bitemporal).
            valid_to: Valid time interval end (bitemporal).
            recorded_at: When the system recorded it.
            source_id: Optional source identifier.
            document_id: Optional document identifier.

        Returns:
            The relationship ID.
        """
        if recorded_at is None:
            recorded_at = self._now()
        rel_id = _uid("rel")
        self.conn.execute(
            "INSERT INTO relationships (id, type, subject_id, object_id, predicate,"
            " valid_from, valid_to, recorded_at, source_id, document_id, created_at)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (rel_id, relationship_type, subject_id, object_id, predicate,
             valid_from, valid_to, recorded_at, source_id, document_id, recorded_at),
        )
        self.conn.commit()
        return rel_id

    def get_relationships_for_entity(self, entity_id: str, direction: str = "outgoing") -> list[dict[str, Any]]:
        """Get relationships for an entity (outgoing or incoming).

        direction: 'outgoing' (the entity is subject), 'incoming' (the entity is object).
        """
        if direction == "incoming":
            query = "SELECT * FROM relationships WHERE object_id = ? ORDER BY recorded_at"
            params = (entity_id,)
        else:
            query = "SELECT * FROM relationships WHERE subject_id = ? ORDER BY recorded_at"
            params = (entity_id,)
        rows = self.conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]

    # ── Claims ─────────────────────────────────────────────────────────────────

    def submit_claim(self, subject_id: str, predicate: str, object_value: str,
                     claim_type: str, domain_id: str, document_id: str,
                     source_span_id: str, status: str = "SUPPORTED",
                     recorded_at: Optional[str] = None) -> str:
        """Submit a new claim version and link it to its source span.

        Args:
            subject_id: The entity being described.
            predicate: The predicate (e.g., 'has_rate', 'governs').
            object_value: The value or object of the claim.
            claim_type: The type of claim (e.g., 'QUANTITATIVE', 'QUALITATIVE').
            domain_id: The domain classification.
            document_id: The source document ID.
            source_span_id: The source span ID (exact passage).
            status: The claim status.
            recorded_at: When the claim was recorded.

        Returns:
            The claim ID.
        """
        if recorded_at is None:
            recorded_at = self._now()
        claim_id = _uid("clm")
        self.conn.execute(
            "INSERT INTO claims (id, subject_id, predicate, object_value, claim_type, domain_id,"
            " document_id, valid_from, recorded_at, status, revision_number, created_at, updated_at)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?, ?)",
            (claim_id, subject_id, predicate, object_value, claim_type, domain_id,
             document_id, recorded_at, recorded_at, status, recorded_at, recorded_at),
        )
        # Insert a claim version (no time conflation: valid_to stays NULL)
        # Version ID is distinct from claim ID
        result_version_id = _uid("clmv")
        self.conn.execute(
            "INSERT INTO claim_versions (id, claim_id, subject_id, predicate, object_value,"
            " claim_type, domain_id, document_id, valid_from, valid_to, recorded_at, status, revision_number, created_at)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)",
            (result_version_id, claim_id, subject_id, predicate, object_value, claim_type, domain_id,
             document_id, recorded_at, None, recorded_at, status, recorded_at),
        )
        # Link the claim to the source passage
        evl_id = _uid("evl")
        self.conn.execute(
            "INSERT INTO evidence_links (id, claim_id, source_span_id, relationship_type, assessment_status, created_at)"
            " VALUES (?, ?, ?, 'DERIVED_FROM', 'SUPPORTED', ?)",
            (evl_id, claim_id, source_span_id, recorded_at),
        )
        self.conn.commit()
        return claim_id

    def get_claim_by_id(self, claim_id: str) -> dict:
        row = self.conn.execute("SELECT * FROM claims WHERE id = ?", (claim_id,)).fetchone()
        return dict(row) if row else None

    def get_claims_by_subject(self, subject_id: str) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT * FROM claims WHERE subject_id = ? ORDER BY recorded_at", (subject_id,)
        ).fetchall()
        return [dict(r) for r in rows]

    def list_claims_for_entity(self, entity_id: str) -> list[dict[str, Any]]:
        return [dict(r) for r in self.conn.execute(
            "SELECT c.* FROM claims c JOIN entities e ON c.subject_id = e.id WHERE e.id = ?", (entity_id,)
        ).fetchall()]

    def get_evidence_links_for_claim(self, claim_id: str) -> list[dict[str, Any]]:
        return [dict(r) for r in self.conn.execute(
            "SELECT * FROM evidence_links WHERE claim_id = ?", (claim_id,)
        ).fetchall()]

    def get_claims_with_provenance(self, entity_id: str) -> list[dict[str, Any]]:
        """Get claims for an entity with source-span provenance.

        FIX: Join through evidence_links.source_span_id.
        """
        rows = self.conn.execute("""
            SELECT c.*, s.id as span_id, s.quoted_text, s.page, s.start_offset, s.end_offset
            FROM claims c
            JOIN evidence_links el ON el.claim_id = c.id
            JOIN source_spans s ON s.id = el.source_span_id
            WHERE c.subject_id = ?
            ORDER BY c.recorded_at
        """, (entity_id,)).fetchall()
        return [dict(r) for r in rows]

    def get_claim_versions(self, claim_id: str) -> list[dict[str, Any]]:
        return [dict(r) for r in self.conn.execute(
            "SELECT * FROM claim_versions WHERE claim_id = ? ORDER BY created_at", (claim_id,)
        ).fetchall()]

    def get_claim_version(self, claim_id: str, revision_number: int) -> Optional[dict[str, Any]]:
        row = self.conn.execute(
            "SELECT * FROM claim_versions WHERE claim_id = ? AND revision_number = ?",
            (claim_id, revision_number)
        ).fetchone()
        return dict(row) if row else None

    def add_evidence_link(self, claim_id: str, source_span_id: str,
                          relationship_type: str, assessment_status: str) -> str:
        """Link a claim to a source span with a relationship type and assessment.

        Args:
            claim_id: The claim ID.
            source_span_id: The source span ID (exact passage).
            relationship_type: Type of link (e.g., 'SUPPORTS', 'CONTRADICTS',
                             'DERIVED_FROM').
            assessment_status: Assessment result.

        Returns:
            The evidence link ID.
        """
        evl_id = _uid("evl")
        self.conn.execute(
            "INSERT INTO evidence_links (id, claim_id, source_span_id, relationship_type, assessment_status, created_at)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (evl_id, claim_id, source_span_id, relationship_type, assessment_status, self._now()),
        )
        self.conn.commit()
        return evl_id

    def delete_entity(self, entity_id: str) -> None:
        """Delete an entity and all related records (transactional).

        NOTE: This is destructive — use only in test/seed scripts.
        """
        self.conn.execute("DELETE FROM entity_aliases WHERE entity_id = ?", (entity_id,))
        self.conn.execute("DELETE FROM claims WHERE subject_id = ?", (entity_id,))
        self.conn.execute("DELETE FROM relationships WHERE subject_id = ? OR object_id = ?",
                          (entity_id, entity_id))
        self.conn.execute("DELETE FROM observations WHERE subject_id = ?", (entity_id,))
        self.conn.execute("DELETE FROM entities WHERE id = ?", (entity_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
