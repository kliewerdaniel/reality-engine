import pathlib
import tempfile
from datetime import UTC, datetime, timedelta

from reality_engine.core.temporal import reconstruct_claims_at
from reality_engine.database import Database


def test_hindsight_oracle():
    tmp = tempfile.mkdtemp()
    db = Database(pathlib.Path(tmp)/"o.db")
    dom = db.register_domain("Econ","d")
    src = db.register_source("Src","NEWS","econ")
    ent = db.register_entity("Inflation","ECONOMIC_MEASUREMENT",dom,["cpi"])
    base = datetime(2026,1,1,tzinfo=UTC)
    for i in range(200):
        t = base + timedelta(days=i)
        doc = db.ingest_document(src, f"claim {i}", "article", "en", t.isoformat())
        span = db.extract_source_span(doc, f"claim {i}", 1, 0, len(f"claim {i}"))
        db.submit_claim(ent, "has_rate", str(i), "QUANTITATIVE", dom, doc, span, recorded_at=t.isoformat())
    cutoff = (base + timedelta(days=99)).isoformat()
    rows = reconstruct_claims_at(db.conn, ent, cutoff)
    assert len(rows) == 100
    for r in rows:
        assert r["recorded_at"] <= cutoff
