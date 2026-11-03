#!/usr/bin/env python3
import argparse, sys
from pathlib import Path
BASE_DIR = Path(__file__).parent.parent
SRC_DIR = BASE_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from reality_engine.database import Database
from reality_engine.revision import RevisionEngine
from reality_engine.core.temporal import materialize_world_state_at

def span(db, doc_id, text):
    row = db.conn.execute("SELECT content FROM documents WHERE id=?", (doc_id,)).fetchone()
    content = row["content"] if hasattr(row, "keys") else row[0]
    i = content.find(text)
    assert i >= 0
    return db.extract_source_span(doc_id, text, 1, i, i + len(text))

def run(db_path):
    db = Database(db_path)
    src1 = db.register_source("Economic Times", "NEWS", "economic")
    src2 = db.register_source("Reuters", "NEWS", "reuters")
    src3 = db.register_source("Syndicated Wire", "NEWS", "economic")
    c1 = "Inflation reached 3.2 percent in October 2026."
    doc1 = db.ingest_document(src1, c1, "article", "en", "2026-10-01T00:00:00Z")
    s1 = span(db, doc1, "Inflation reached 3.2 percent")
    domain = db.register_domain("Economic Indicators", "Measures")
    ent = db.register_entity("Inflation", "ECONOMIC_MEASUREMENT", domain_id=domain, aliases=["CPI"])
    obs = db.register_observation(doc1, src1, ent, "3.2 percent", "2026-10-02T00:00:00Z")
    claim = db.submit_claim(ent, "has_rate", "3.2", "QUANTITATIVE", domain, doc1, source_span_id=s1, status="SUPPORTED")
    c2 = "Independent data confirms inflation at 3.2 percent."
    doc2 = db.ingest_document(src2, c2, "article", "en", "2026-10-03T00:00:00Z")
    s2 = span(db, doc2, "Independent data confirms inflation at 3.2 percent.")
    db.add_evidence_link(claim, s2, "SUPPORTS", "SUPPORTED")
    c3 = "Inflation reached 3.2 percent in October 2026."
    doc3 = db.ingest_document(src3, c3, "article", "en", "2026-10-04T00:00:00Z")
    s3 = span(db, doc3, "Inflation reached 3.2 percent")
    db.add_evidence_link(claim, s3, "SUPPORTS", "SUPPORTED")
    c4 = "Economists question whether the 3.2 percent figure is overstated."
    doc4 = db.ingest_document(src2, c4, "article", "en", "2026-10-05T00:00:00Z")
    s4 = span(db, doc4, "Economists question whether the 3.2 percent figure is overstated.")
    obs2 = db.register_observation(doc4, src2, ent, "question", "2026-10-06T00:00:00Z")
    db.add_evidence_link(claim, s4, "CONTRADICTS", "CONTRADICTED")
    assert db.get_claim_by_id(claim)["status"] == "SUPPORTED"
    engine = RevisionEngine(db)
    proposal = {
        "proposal_id": "p1",
        "affected_records": [claim],
        "entity_id": ent,
        "trigger_observation_id": obs2,
        "challenge_evidence_id": s4,
        "proposed_status": "CONTESTED",
        "current_state": {"status": "SUPPORTED", "revision_number": db.get_claim_by_id(claim)["revision_number"]},
        "status": "PROPOSED",
    }
    validation = engine.validate_proposal(proposal)
    banner = "ACCEPTED" if validation["result"] == "ACCEPT" else "REJECTED"
    assert validation["result"] in ("ACCEPT", "REJECT")
    commit = engine.commit_revision(proposal, validation)
    assert commit.get("revision_id") is not None
    print("VALIDATION:", validation["result"])
    print("BANNER:", banner)
    print("COMMIT:", commit.get("revision_id"))
    db.close()
    return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=None)
    args = ap.parse_args()
    if args.db:
        db_path = Path(args.db)
    else:
        db_path = BASE_DIR / "demo" / "demo_evidence_foundation.db"
    if db_path.exists():
        db_path.unlink()
    return run(db_path)

if __name__ == "__main__":
    sys.exit(main())
