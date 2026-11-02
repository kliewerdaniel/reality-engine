"""Audit repro: each check prints REPRODUCED (defect exists) or ok (behaves correctly).

Uses only the public package API in a throwaway temp DB. Nothing here touches the repo.
"""
import sqlite3
import tempfile
import pathlib
import sys

from reality_engine.database import Database
from reality_engine.revision import RevisionEngine
from reality_engine.core.temporal import (
    materialize_world_state_at,
    reconstruct_claims_at,
)

results = []

# Maps a substring of a check name to the finding ID used in the audit / Hermes prompt.
FID = {
    "fabricates canonical_url": "F-03",
    "deduplication": "F-04",
    "extract_source_span accepts": "F-05",
    "different document": "F-05",
    "audit_events rows are mutable": "F-06",
    "documents.content mutable": "F-06",
    "valid_from = recorded_at": "F-07",
    "transaction():": "F-08",
    "delete_entity": "F-09",
    "as-of 2026-10-15": "F-10",
    "relationships filtered with >=": "F-11",
    "events recorded AFTER cutoff": "F-12",
    "snapshot at year 2000": "F-12",
    "proposal_not_stale": "F-13",
    "unconditional placeholders": "F-13",
    "span_verified passes for fabricated": "F-13",
    "hardcodes CONTESTED": "F-14",
    "previous_hash is NULL": "F-15",
    "verify_audit_chain": "F-15",
    "mixed 'Z'": "F-01",
    "0.5s AFTER": "F-01",
}


def check(name, defect_present, detail=""):
    tag = "REPRODUCED" if defect_present else "ok"
    fid = next((v for k, v in FID.items() if k in name), "    ")
    results.append((name, defect_present))
    print(f"[{tag:10}] {fid} {name}" + (f"  -- {detail}" if detail else ""))


def fresh():
    tmp = tempfile.mkdtemp()
    db = Database(pathlib.Path(tmp) / "t.db")
    dom = db.register_domain("Econ", "d")
    src = db.register_source("Src", "NEWS", "econ")
    ent = db.register_entity("Inflation", "ECONOMIC_MEASUREMENT", dom, ["cpi"])
    return db, dom, src, ent


# ---- 1. canonical_url is fabricated ---------------------------------------
db, dom, src, ent = fresh()
doc = db.ingest_document(src, "Inflation reached 3.2 percent.", "article", "en", "2026-10-01T00:00:00Z")
row = db.conn.execute("SELECT canonical_url, source_native_id, processing_status FROM documents WHERE id=?", (doc,)).fetchone()
check("ingest_document fabricates canonical_url/native_id/status",
      row["canonical_url"] == "https://example.com/doc",
      f"url={row['canonical_url']} native_id={row['source_native_id'][:14]}.. status={row['processing_status']}")

# ---- 2. identical content ingested twice -> two documents ------------------
doc_b = db.ingest_document(src, "Inflation reached 3.2 percent.", "article", "en", "2026-10-01T00:00:00Z")
n = db.conn.execute("SELECT COUNT(*) c FROM documents WHERE content_hash=(SELECT content_hash FROM documents WHERE id=?)", (doc,)).fetchone()["c"]
check("no content-hash deduplication", n == 2, f"{n} rows share one content_hash")

# ---- 3. span not validated against document --------------------------------
try:
    bad = db.extract_source_span(doc, "THIS TEXT IS NOT IN THE DOCUMENT", 1, 9000, 9100)
    check("extract_source_span accepts quote not in doc / offsets out of range", True, "accepted")
except Exception as e:  # noqa
    check("extract_source_span accepts quote not in doc / offsets out of range", False, str(e))

# ---- 4. span from a DIFFERENT document accepted for a claim ----------------
doc2 = db.ingest_document(src, "Unrelated text.", "article", "en", "2026-10-02T00:00:00Z")
span2 = db.extract_source_span(doc2, "Unrelated text", 1, 0, 14)
try:
    db.submit_claim(ent, "has_rate", "3.2", "QUANTITATIVE", dom, doc, span2)
    check("submit_claim accepts span belonging to a different document", True, "accepted")
except Exception as e:  # noqa
    check("submit_claim accepts span belonging to a different document", False, str(e))

# ---- 5. valid_from conflated with recorded_at ------------------------------
db, dom, src, ent = fresh()
doc = db.ingest_document(src, "Inflation reached 3.2 percent in October.", "article", "en", "2026-10-01T00:00:00Z")
span = db.extract_source_span(doc, "Inflation reached 3.2 percent", 1, 0, 29)
clm = db.submit_claim(ent, "has_rate", "3.2", "QUANTITATIVE", dom, doc, span, recorded_at="2026-10-02T00:00:00Z")
c = db.get_claim_by_id(clm)
check("submit_claim sets valid_from = recorded_at (bitemporal conflation)",
      c["valid_from"] == c["recorded_at"], f"valid_from={c['valid_from']} recorded_at={c['recorded_at']}")

# ---- 6. validator: stale / fake-span / placeholder rules -------------------
eng = RevisionEngine(db)
obs2 = db.register_observation(doc, src, ent, "challenge", "2026-10-06T00:00:00Z")
proposal = {
    "proposal_id": "revp_x", "affected_records": [clm], "entity_id": ent,
    "trigger_observation_id": obs2, "challenge_evidence_id": span,
    "proposed_status": "SUPERSEDED",
    "current_state": {"status": "SUPPORTED", "revision_number": 99},  # deliberately wrong revision
}
v = eng.validate_proposal(proposal)
stale_rule = next(r for r in v["rules"] if r["name"] == "proposal_not_stale")
check("validator: proposal_not_stale passes with wrong revision_number",
      stale_rule["passed"] and v["result"] == "ACCEPT", stale_rule["detail"])

ph = [r["name"] for r in v["rules"] if "placeholder" in r["detail"]]
check("validator: rules that are unconditional placeholders", len(ph) > 0, f"{ph}")

# span_verified with a span whose quoted_text is NOT in the document
fake_span = db.extract_source_span(doc, "FABRICATED QUOTE NOT IN DOC", 1, 0, 27)
db.add_evidence_link(clm, fake_span, "SUPPORTS", "SUPPORTED")
db.conn.execute("DELETE FROM evidence_links WHERE claim_id=? AND source_span_id=?", (clm, span))
db.conn.commit()
v2 = eng.validate_proposal(proposal)
sv = next(r for r in v2["rules"] if r["name"] == "span_verified")
check("validator: span_verified passes for fabricated quote",
      sv["passed"], sv["detail"])
# restore original link
db.add_evidence_link(clm, span, "SUPPORTS", "SUPPORTED")

# ---- 7. commit ignores proposed_status; hardcodes CONTESTED ----------------
db, dom, src, ent = fresh()
doc = db.ingest_document(src, "Inflation reached 3.2 percent in October.", "article", "en", "2026-10-01T00:00:00Z")
span = db.extract_source_span(doc, "Inflation reached 3.2 percent", 1, 0, 29)
clm = db.submit_claim(ent, "has_rate", "3.2", "QUANTITATIVE", dom, doc, span, recorded_at="2026-10-02T00:00:00Z")
obs2 = db.register_observation(doc, src, ent, "challenge", "2026-10-06T00:00:00Z")
eng = RevisionEngine(db)
prop = {
    "proposal_id": "revp_1", "affected_records": [clm], "entity_id": ent,
    "trigger_observation_id": obs2, "challenge_evidence_id": span,
    "proposed_status": "SUPERSEDED",
    "current_state": {"status": "SUPPORTED", "revision_number": 1},
}
val = eng.validate_proposal(prop)
out = eng.commit_revision(prop, val)
check("commit_revision hardcodes CONTESTED (ignores proposed_status=SUPERSEDED)",
      out.get("new_status") == "CONTESTED", f"new_status={out.get('new_status')}")

# ---- 8. audit chain: previous_hash always NULL; no verifier ----------------
db2, dom2, src2, ent2 = fresh()
d = db2.ingest_document(src2, "A claim here.", "article", "en", "2026-10-01T00:00:00Z")
s = db2.extract_source_span(d, "A claim", 1, 0, 7)
claims = []
for i in range(2):
    claims.append(db2.submit_claim(ent2, f"p{i}", "v", "QUALITATIVE", dom2, d, s, recorded_at="2026-10-02T00:00:00Z"))
o = db2.register_observation(d, src2, ent2, "x", "2026-10-03T00:00:00Z")
e2 = RevisionEngine(db2)
for c_id in claims:
    p = {"proposal_id": f"rp_{c_id}", "affected_records": [c_id], "entity_id": ent2,
         "trigger_observation_id": o, "challenge_evidence_id": s,
         "proposed_status": "CONTESTED", "current_state": {"status": "SUPPORTED", "revision_number": 1}}
    e2.commit_revision(p, e2.validate_proposal(p))
rows = db2.conn.execute("SELECT previous_hash FROM audit_events ORDER BY created_at").fetchall()
check("audit chain: previous_hash is NULL on every event (not chained)",
      len(rows) == 2 and all(r["previous_hash"] is None for r in rows), f"{len(rows)} events, prev_hashes={[r['previous_hash'] for r in rows]}")
check("no verify_audit_chain() exists", not hasattr(RevisionEngine, "verify_audit_chain") and not hasattr(Database, "verify_audit_chain"))
# tamper test: rewrite an audit row silently
db2.conn.execute("UPDATE audit_events SET object_id='tampered'")
db2.conn.commit()
check("audit_events rows are mutable (no trigger / no tamper detection)", True, "UPDATE succeeded silently")
db2.conn.execute("UPDATE documents SET content='REWRITTEN EVIDENCE'")
db2.conn.commit()
chk = db2.conn.execute("SELECT content, content_hash FROM documents LIMIT 1").fetchone()
check("documents.content mutable; content_hash no longer matches and nothing notices", True, "UPDATE succeeded silently")

# ---- 9. as-of reconstruction after a revision ------------------------------
db, dom, src, ent = fresh()
doc = db.ingest_document(src, "Inflation reached 3.2 percent in October.", "article", "en", "2026-10-01T00:00:00Z")
span = db.extract_source_span(doc, "Inflation reached 3.2 percent", 1, 0, 29)
clm = db.submit_claim(ent, "has_rate", "3.2", "QUANTITATIVE", dom, doc, span, recorded_at="2026-10-02T00:00:00Z")
obs = db.register_observation(doc, src, ent, "challenge", "2026-10-06T00:00:00Z")
eng = RevisionEngine(db)
prop = {"proposal_id": "rp", "affected_records": [clm], "entity_id": ent,
        "trigger_observation_id": obs, "challenge_evidence_id": span,
        "proposed_status": "CONTESTED", "current_state": {"status": "SUPPORTED", "revision_number": 1}}
eng.commit_revision(prop, eng.validate_proposal(prop))   # revision recorded at real 'now' (2026-11)
past = reconstruct_claims_at(db.conn, ent, "2026-10-15T00:00:00Z")
status_then = past[0]["status"] if past else None
check("as-of 2026-10-15 reports CURRENT status, not the status believed then",
      status_then != "SUPPORTED", f"as-of status={status_then} (should be SUPPORTED)")

# ---- 10. relationships snapshot uses >= (future leak, past omission) -------
db, dom, src, ent = fresh()
e_b = db.register_entity("Other", "X", dom)
db.register_relationship("MEASURED_BY", ent, e_b, recorded_at="2026-10-02T00:00:00Z")
db.register_relationship("MEASURED_BY", ent, e_b, recorded_at="2026-12-15T00:00:00Z")
snap = materialize_world_state_at(db.conn, "2026-12-01T00:00:00Z")
recs = sorted(r["recorded_at"] for r in snap["relationships"])
check("materialize_world_state_at: relationships filtered with >= (leaks future, drops past)",
      recs == ["2026-12-15T00:00:00Z"], f"snapshot@2026-12-01 contains relationships recorded {recs}")

# ---- 11. events filtered by occurred_at, not recorded_at -------------------
db.register_event("DEBATE", "late-recorded event", occurred_at="2026-10-01T00:00:00Z",
                  recorded_at="2026-11-20T00:00:00Z")
snap = materialize_world_state_at(db.conn, "2026-10-05T00:00:00Z")
leaked = [e for e in snap["events"] if e["recorded_at"] > "2026-10-05T00:00:00Z"]
check("materialize_world_state_at: events recorded AFTER cutoff leak into snapshot (hindsight)",
      len(leaked) == 1, f"{len(leaked)} event(s) known only after cutoff appear in the 2026-10-05 snapshot")

# ---- 12. entities in snapshot ignore time ----------------------------------
snap = materialize_world_state_at(db.conn, "2000-01-01T00:00:00Z")
check("snapshot at year 2000 still lists all entities", len(snap["entities"]) > 0, f"{len(snap['entities'])} entities")

# ---- 13. transaction() does not make Database methods atomic ---------------
db, dom, src, ent = fresh()
try:
    with db.transaction():
        db.register_domain("ShouldRollBack", "x")
        raise RuntimeError("boom")
except Exception:
    pass
n = db.conn.execute("SELECT COUNT(*) c FROM domains WHERE name='ShouldRollBack'").fetchone()["c"]
check("transaction(): Database methods self-commit, so rollback does not undo them", n == 1, f"{n} row survived the rollback")

# ---- 14. delete_entity vs FK + history -------------------------------------
db, dom, src, ent = fresh()
doc = db.ingest_document(src, "Inflation reached 3.2 percent.", "article", "en", "2026-10-01T00:00:00Z")
span = db.extract_source_span(doc, "Inflation reached 3.2 percent", 1, 0, 29)
clm = db.submit_claim(ent, "has_rate", "3.2", "QUANTITATIVE", dom, doc, span)
try:
    db.delete_entity(ent)
    check("delete_entity on entity with claims", False, "succeeded (history erased)")
except sqlite3.IntegrityError as e:
    check("delete_entity crashes on entity with claims (FK) / violates P4 by design", True, f"IntegrityError: {e}")

# ---- 15. timestamp string-compare hazards ----------------------------------
db, dom, src, ent = fresh()
db.register_observation(doc if False else db.ingest_document(src, "x", "a", "en", "2026-10-01T00:00:00Z"), src, ent, "v", "2026-10-05T12:00:00+00:00")
same_instant_z = materialize_world_state_at(db.conn, "2026-10-05T12:00:00Z")
n_obs = len(same_instant_z["observations"])
check("mixed 'Z' vs '+00:00' timestamps: observation recorded exactly at cutoff instant",
      n_obs != 1, f"found {n_obs} (1 is correct for this case)")
db.register_observation(db.ingest_document(src, "y", "a", "en", "2026-10-01T00:00:00Z"), src, ent, "v", "2026-10-05T12:00:00.500000+00:00")
snap = materialize_world_state_at(db.conn, "2026-10-05T12:00:00Z")
check("timestamp compare: obs recorded 0.5s AFTER cutoff is included",
      len(snap["observations"]) == 2, f"{len(snap['observations'])} observations (expected 1)")

# ---- 16. compute_state_hash ordering --------------------------------------
import inspect
src_txt = inspect.getsource(Database.list_claims_for_entity)
print(f"[latent    ] compute_state_hash input query has ORDER BY: {'ORDER BY' in src_txt} "
      "(code inspection only; not counted as a reproduced defect)")

print()
n_def = sum(1 for _, d in results if d)
print(f"{n_def} of {len(results)} checks reproduced a defect")
# Baseline tool: exits 1 while any defect reproduces. It targets the baseline (e95f42d) API and is
# expected to be ported into pytest regression tests and then archived, not kept as a CI gate.
sys.exit(1 if n_def else 0)
