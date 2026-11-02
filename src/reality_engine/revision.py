"""Revision engine: proposal validation, transactional commit, and audit chain.

This module implements the deterministic governance layer for Reality Engine.
Proposals flow in from language models (and other sources); the revision engine
validates them against named rules and commits accepted transitions.

All writes are transactional (BEGIN/COMMIT/ROLLBACK). The audit chain is hashed
and chains each event to the previous one.
"""
import hashlib
import sqlite3
from datetime import datetime, timezone
from typing import Any
import uuid


class RevisionEngine:
    """Deterministic revision engine.

    Validates proposals through per-rule outcomes and commits accepted transitions
    atomically. The audit chain is hashed and chains each event to the previous one.

    Attributes:
        db: The database instance.
    """

    def __init__(self, db: Any):
        self.db = db

    def validate_proposal(self, proposal: dict[str, Any]) -> dict[str, Any]:
        """Validate a proposal deterministically via registered rule callables."""
        claim_id = proposal["affected_records"][0]
        claim = self.db.get_claim_by_id(claim_id)
        if claim is None:
            return {
                "result": "REJECT",
                "rules": [{"name": "claim_exists", "passed": False, "detail": "Claim not found"}],
                "validated_status": "REJECTED",
            }

        links = self.db.get_evidence_links_for_claim(claim_id)

        def rule_provenance_present(db, proposal, claim, links):
            return (len(links) > 0, f"{len(links)} evidence link(s) found")

        def rule_span_verified(db, proposal, claim, links):
            if not links:
                return (False, "no evidence links on claim")
            for lk in links:
                src_span = lk.get("source_span_id")
                if not src_span:
                    return (False, "no source_span_id on evidence link")
                span = db.get_source_span(src_span)
                if not span:
                    return (False, f"span {src_span} not found")
                doc_row = db.conn.execute("SELECT content FROM documents WHERE id=?", (span["document_id"],)).fetchone()
                content = doc_row["content"] if hasattr(doc_row,"keys") else doc_row[0]
                start = span["start_offset"]; end = span["end_offset"]
                if start < 0 or end > len(content) or content[start:end] != span["quoted_text"] or span["quoted_text"] not in content:
                    return (False, f"fabricated quote not in document for span {src_span}")
            return (True, "all spans verified")

        def rule_temporal_consistency(db, proposal, claim, links):
            # valid time must not exceed collection time (recorded_at)
            vf = claim.get("valid_from")
            ra = claim.get("recorded_at")
            if vf and ra and vf > ra:
                return (False, "valid_from exceeds recorded_at")
            return (True, "temporal consistency ok")

        def rule_source_independence(db, proposal, claim, links):
            # challenge evidence source must differ from claim source
            challenge_span_id = None
            # challenge_evidence_id may be span id
            ce = proposal.get("challenge_evidence_id")
            if ce:
                cspan = db.get_source_span(ce)
                if cspan:
                    cdoc = db.conn.execute("SELECT source_id FROM documents WHERE id=?", (cspan["document_id"],)).fetchone()
                    csrc = cdoc["source_id"] if hasattr(cdoc,"keys") else cdoc[0]
                    claim_doc = db.conn.execute("SELECT source_id FROM documents WHERE id=?", (claim["document_id"],)).fetchone()
                    csrc2 = claim_doc["source_id"] if hasattr(claim_doc,"keys") else claim_doc[0]
                    claim_span_id = links[0].get("source_span_id") if links else None
                    if csrc == csrc2 and ce != claim_span_id:
                        return (False, "challenge source not independent")
            return (True, "source independence ok")

        def rule_proposal_not_stale(db, proposal, claim, links):
            cur = claim.get("revision_number")
            ref = proposal.get("current_state", {}).get("revision_number")
            if ref is not None and ref != cur:
                return (False, f"proposal stale: {ref} != {cur}")
            return (True, f"claim revision {cur} matches proposal reference")

        rules_registry = [
            ("provenance_present", rule_provenance_present),
            ("span_verified", rule_span_verified),
            ("temporal_consistency", rule_temporal_consistency),
            ("source_independence", rule_source_independence),
            ("proposal_not_stale", rule_proposal_not_stale),
        ]

        rules = []
        for name, fn in rules_registry:
            passed, detail = fn(self.db, proposal, claim, links)
            rules.append({"name": name, "passed": bool(passed), "detail": detail})

        all_passed = all(r["passed"] for r in rules)
        return {
            "result": "ACCEPT" if all_passed else "REJECT",
            "rules": rules,
            "validated_status": "ACCEPTED" if all_passed else "REJECTED",
        }

    def commit_revision(self, proposal: dict[str, Any], validation: dict[str, Any]) -> dict[str, Any]:
        """Commit a revision as a SINGLE atomic transaction.

        All operations succeed or fail together.
        """
        claim_id = proposal["affected_records"][0]
        claim = self.db.get_claim_by_id(claim_id)
        current_status = claim["status"]

        # Verify the proposal is still current
        if current_status != proposal["current_state"]["status"]:
            return {
                "revision_id": None, "claim_id": claim_id,
                "previous_status": current_status, "new_status": None,
                "previous_hash": None, "error": "Proposal is stale",
            }

        # Verify validation passed
        if validation.get("result") != "ACCEPT":
            return {
                "revision_id": None, "claim_id": claim_id,
                "previous_status": current_status, "new_status": None,
                "previous_hash": None, "error": f"Validation failed: {validation.get('result')}",
            }

        # Capture previous state hash
        previous_hash = self.compute_state_hash(claim["subject_id"])

        # Capture the previous claim version for preservation
        previous_version = self.db.get_claim_version(claim_id, claim["revision_number"])
        if previous_version is None:
            return {
                "revision_id": None, "claim_id": claim_id,
                "previous_status": current_status, "new_status": None,
                "previous_hash": None, "error": "Previous claim version not found",
            }

        # Verify triggering evidence exists
        if not proposal.get("challenge_evidence_id"):
            return {
                "revision_id": None, "claim_id": claim_id,
                "previous_status": current_status, "new_status": None,
                "previous_hash": None, "error": "Challenge evidence reference missing",
            }

        # Capture the transaction ID
        tx_id = self._uid("tx")

        # Start the transaction and perform all operations atomically
        db_conn = self.db.conn
        now = self._now()
        try:
            db_conn.execute("BEGIN")

            # Create the resulting claim version (preserving the full history)
            result_version_id = self._uid("clmv")
            db_conn.execute(
                "INSERT INTO claim_versions (id, claim_id, subject_id, predicate, object_value, "
                " claim_type, domain_id, document_id, valid_from, valid_to, recorded_at, status, "
                "revision_number, created_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (result_version_id, claim_id, claim["subject_id"], claim["predicate"],
                 claim["object_value"], claim["claim_type"], claim["domain_id"], claim["document_id"],
                 claim["valid_from"], claim["valid_to"], now, "CONTESTED",
                 claim["revision_number"] + 1, now),
            )

            # Update current-state projection (current claims table)
            db_conn.execute(
                "UPDATE claims SET status = ?, revision_number = ?, updated_at = ? WHERE id = ?",
                (proposal.get("proposed_status","CONTESTED"), claim["revision_number"] + 1, now, claim_id),
            )

            # Compute resulting state hash AFTER the update
            resulting_hash = self.compute_state_hash(claim["subject_id"])

            # Record the revision event
            rev_event_id = self._uid("rev")
            db_conn.execute(
                "INSERT INTO revisions (id, revision_type, trigger_observation_id, proposal_reference, "
                "validation_result, object_id, transaction_id, previous_claim_version_id, "
                "resulting_claim_version_id, previous_state_id, resulting_state_id, created_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (rev_event_id, proposal.get("proposed_status","CONTESTED"), proposal["trigger_observation_id"],
                 proposal["proposal_id"], "PASS", claim["subject_id"],
                 tx_id, previous_version["id"], result_version_id,
                 previous_hash, resulting_hash, now),
            )

            # Record the audit event
            audit_id = self._uid("aud")
            prev_row = db_conn.execute(
                "SELECT event_hash FROM audit_events ORDER BY created_at DESC, id DESC LIMIT 1"
            ).fetchone()
            prev_audit_hash = prev_row[0] if prev_row else None
            payload = {"revision_id": rev_event_id, "claim_id": claim_id,
                       "new_status": proposal.get("proposed_status","CONTESTED"), "created_at": now}
            import json as _json
            event_hash = hashlib.sha256(
                ((prev_audit_hash or "") + _json.dumps(payload, sort_keys=True)).encode("utf-8")
            ).hexdigest()
            db_conn.execute(
                "INSERT INTO audit_events (id, event_type, actor_type, actor_id, object_type, object_id, "
                "previous_hash, event_hash, payload_reference, created_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (audit_id, "REVISION_COMMITTED", "Systems Integrator", "auto",
                 "claim", claim_id,
                 prev_audit_hash, event_hash,
                 f"claim:{claim_id}:to:CONTESTED", now),
            )

            db_conn.commit()
        except Exception:
            db_conn.rollback()
            raise

        return {
            "revision_id": rev_event_id,
            "claim_id": claim_id,
            "previous_status": current_status,
            "new_status": proposal.get("proposed_status","CONTESTED"),
            "previous_hash": previous_hash,
            "resulting_hash": resulting_hash,
            "transaction_id": tx_id,
            "previous_claim_version_id": previous_version["id"],
            "resulting_claim_version_id": result_version_id,
        }

    def verify_audit_chain(self) -> object:
        """Return 'OK' if chain intact, else index of first broken event."""
        rows = self.db.conn.execute(
            "SELECT previous_hash, event_hash, payload_reference, created_at, id FROM audit_events ORDER BY created_at, id"
        ).fetchall()
        prev = None
        for i, r in enumerate(rows):
            if (r[0] if not hasattr(r, "keys") else r["previous_hash"]) != prev:
                return i
            prev = r[1] if not hasattr(r, "keys") else r["event_hash"]
        return "OK"

    def compute_state_hash(self, entity_id: str) -> str:
        """Compute a hash of the current world state for this entity.

        Args:
            entity_id: The entity ID.

        Returns:
            SHA-256 hex digest of the entity's current claims.
        """
        claims = self.db.list_claims_for_entity(entity_id)
        state = "".join(
            f"{c['id']}:{c['status']}:{c['recorded_at']}"
            for c in claims
        )
        return hashlib.sha256(state.encode("utf-8")).hexdigest()

    def _uid(self, prefix: str) -> str:
        """Generate a unique ID.

        Args:
            prefix: A string prefix for the ID.

        Returns:
            A unique ID string.
        """
        import uuid
        return f"{prefix}_{uuid.uuid4().hex[:12]}"

    def _now(self) -> str:
        """Get the current UTC timestamp.

        Returns:
            A UTC timestamp string.
        """
        from datetime import datetime, timezone
        return datetime.now(timezone.utc).isoformat()
