"""Bitemporal data model for Reality Engine.

Two independent time dimensions:
- valid_time: When the information applies to the external world.
- transaction_time: When Reality Engine learned or recorded the information.

Example:
- A regulation takes effect October 10 (valid_from).
- It is reported October 12 (transaction_time).
- Reality Engine collects it October 13 (recorded_at).
- A correction arrives October 20, establishing the effective date was actually October 11.
"""

import sqlite3
from datetime import datetime
from typing import Any

# ── Bitemporal helpers ──────────────────────────────────────────────────────────

def parse_iso8601(value: str | None) -> datetime | None:
    """Parse ISO 8601 timestamp, returning None for 'None' or empty."""
    if value is None or value == "None" or value == "":
        return None
    try:
        return datetime.fromisoformat(value)
    except (ValueError, AttributeError):
        return None


def format_iso8601(dt: datetime) -> str:
    """Format datetime as ISO 8601 UTC."""
    return dt.isoformat().replace("+00:00", "Z")


def bitemporal_key(recorded_at: str, valid_from: str | None = None,
                   valid_to: str | None = None) -> tuple[str, str, str]:
    """Compute a deterministic bitemporal sort key."""
    return (recorded_at or "", valid_from or "", valid_to or "")


# ── Bitemporal query helpers ────────────────────────────────────────────────────

def get_observations_in_interval(conn: sqlite3.Connection, valid_from_min: str, valid_from_max: str) -> list[dict[str, Any]]:
    """Get observations whose valid_from falls within the interval."""
    rows = conn.execute(
        "SELECT * FROM observations WHERE valid_from IS NOT NULL"
        " AND valid_from >= ? AND valid_from <= ?"
        " ORDER BY valid_from", (valid_from_min, valid_from_max)
    ).fetchall()
    return [dict(r) for r in rows]


def get_observations_since(conn: sqlite3.Connection, since: str) -> list[dict[str, Any]]:
    """Get observations recorded at or after the given timestamp."""
    rows = conn.execute(
        "SELECT * FROM observations WHERE recorded_at >= ? ORDER BY recorded_at", (since,)
    ).fetchall()
    return [dict(r) for r in rows]


def get_relationships_in_interval(conn: sqlite3.Connection, valid_from_min: str, valid_from_max: str) -> list[dict[str, Any]]:
    """Get relationships whose valid_from falls within the interval."""
    rows = conn.execute(
        "SELECT * FROM relationships WHERE valid_from IS NOT NULL"
        " AND valid_from >= ? AND valid_from <= ?"
        " ORDER BY valid_from", (valid_from_min, valid_from_max)
    ).fetchall()
    return [dict(r) for r in rows]


def get_relationships_since(conn: sqlite3.Connection, since: str) -> list[dict[str, Any]]:
    """Get relationships recorded at or after the given timestamp."""
    rows = conn.execute(
        "SELECT * FROM relationships WHERE recorded_at >= ? ORDER BY recorded_at", (since,)
    ).fetchall()
    return [dict(r) for r in rows]


# ── Historical reconstruction helpers ───────────────────────────────────────────

def reconstruct_observations_at(
    conn: sqlite3.Connection,
    entity_id: str | None = None,
    timestamp: str | None = None
) -> list[dict[str, Any]]:
    """Reconstruct what the system understood about an entity at a given point in time.

    Uses recorded_at (transaction time) as the cutoff: only observations recorded
    before or at `timestamp` are included in the reconstruction.

    If entity_id is None, all observations up to the timestamp are returned.

    Args:
        conn: SQLite connection.
        entity_id: The entity ID. If None, returns all observations.
        timestamp: The time of reconstruction (ISO 8601).

    Returns:
        List of observations recorded at or before the timestamp.
    """
    if entity_id:
        query = (
            "SELECT * FROM observations"
            " WHERE subject_id = ? AND recorded_at <= ?"
            " ORDER BY recorded_at"
        )
        params: tuple[Any, ...] = (entity_id, timestamp)
    else:
        query = (
            "SELECT * FROM observations"
            " WHERE recorded_at <= ?"
            " ORDER BY recorded_at"
        )
        params = (timestamp,)
    rows = conn.execute(query, params).fetchall()
    return [dict(r) for r in rows]


def reconstruct_claims_at(
    conn: sqlite3.Connection,
    entity_id: str | None = None,
    timestamp: str | None = None
) -> list[dict[str, Any]]:
    """Reconstruct what the system's understanding of a claim at a given time.

    Returns claim versions recorded before or at the timestamp.

    If entity_id is None, all claims up to the timestamp are returned.

    Args:
        conn: SQLite connection.
        entity_id: The entity ID. If None, returns all claims.
        timestamp: The time of reconstruction (ISO 8601).

    Returns:
        List of claims recorded at or before the timestamp.
    """
    if entity_id:
        query = (
            "SELECT cv.claim_id AS id, cv.* FROM claim_versions cv "
            "WHERE cv.subject_id = ? AND cv.recorded_at <= ? "
            "AND cv.recorded_at = (SELECT MAX(cv2.recorded_at) FROM claim_versions cv2 "
            "WHERE cv2.claim_id = cv.claim_id AND cv2.recorded_at <= ?) "
            "ORDER BY cv.recorded_at"
        )
        params: tuple[Any, ...] = (entity_id, timestamp, timestamp)
    else:
        query = (
            "SELECT cv.claim_id AS id, cv.* FROM claim_versions cv "
            "WHERE cv.recorded_at <= ? "
            "AND cv.recorded_at = (SELECT MAX(cv2.recorded_at) FROM claim_versions cv2 "
            "WHERE cv2.claim_id = cv.claim_id AND cv2.recorded_at <= ?) "
            "ORDER BY cv.recorded_at"
        )
        params = (timestamp, timestamp)
    rows = conn.execute(query, params).fetchall()
    return [dict(r) for r in rows]


def reconstruct_events_at(
    conn: sqlite3.Connection,
    start_date: str | None = None,
    end_date: str | None = None
) -> list[dict[str, Any]]:
    """Reconstruct events up to a given point in time."""
    query = "SELECT * FROM events WHERE 1=1"
    params: list[Any] = []
    if start_date:
        query += " AND occurred_at >= ?"
        params.append(start_date)
    if end_date:
        query += " AND occurred_at <= ?"
        params.append(end_date)
    query += " ORDER BY occurred_at"
    rows = conn.execute(query, params).fetchall()
    return [dict(r) for r in rows]


# ── Bitemporal state materialization ────────────────────────────────────────────

def _canon_ts(ts: str | None) -> str | None:
    from reality_engine.core.clock import canonical_utc
    dt = parse_iso8601(ts)
    return canonical_utc(dt) if dt is not None else ts

def materialize_world_state_at(
    conn: sqlite3.Connection,
    timestamp: str
 ) -> dict[str, Any]:
    timestamp = _canon_ts(timestamp) or timestamp
    """Materialize a snapshot of the world state at a given transaction time.

    Returns a dictionary with:
    - entities: all entities known at the time
    - claims: claims with recorded_at <= timestamp
    - observations: observations with recorded_at <= timestamp
    - relationships: relationships with recorded_at <= timestamp
    - events: events with recorded_at <= timestamp
    - revision_count: number of revisions committed before timestamp
    """
    claims = reconstruct_claims_at(conn, None, timestamp)
    observations = reconstruct_observations_at(conn, None, timestamp)
    entities: list[dict[str, Any]] = []
    for row in conn.execute(
        "SELECT DISTINCT e.* FROM entities e "
        "WHERE e.created_at <= ? "
        "OR e.id IN (SELECT subject_id FROM observations WHERE recorded_at <= ?) "
        "OR e.id IN (SELECT subject_id FROM claim_versions WHERE recorded_at <= ?) "
        "ORDER BY e.canonical_name",
        (timestamp, timestamp, timestamp),
    ).fetchall():
        entities.append(dict(row))
    rows = conn.execute("SELECT * FROM relationships WHERE recorded_at <= ? ORDER BY recorded_at", (timestamp,)).fetchall()
    relationships = [dict(r) for r in rows]
    ev_rows = conn.execute("SELECT * FROM events WHERE recorded_at <= ? ORDER BY recorded_at", (timestamp,)).fetchall()
    events = [dict(r) for r in ev_rows]
    revision_count = conn.execute(
        "SELECT COUNT(*) as c FROM revisions WHERE created_at <= ?", (timestamp,)
    ).fetchone()[0]

    return {
        "entities": [dict(r) for r in entities],
        "claims": claims,
        "observations": observations,
        "relationships": relationships,
        "events": events,
        "revision_count": revision_count,
    }
