import subprocess, sys, tempfile, pathlib
from reality_engine.database import Database

def test_e2e_first_proof():
    tmp = tempfile.mkdtemp()
    dbpath = pathlib.Path(tmp)/"e2e.db"
    db = Database(dbpath)
    dom = db.register_domain("Econ","d")
    src = db.register_source("Src","NEWS","econ")
    ent = db.register_entity("Inflation","ECONOMIC_MEASUREMENT",dom,["cpi"])
    doc = db.ingest_document(src, "Inflation reached 3.2 percent.", "article", "en", "2026-10-01T00:00:00Z")
    span = db.extract_source_span(doc, "Inflation reached 3.2 percent.", 1, 0, 30)
    clm = db.submit_claim(ent, "has_rate", "3.2", "QUANTITATIVE", dom, doc, span, recorded_at="2026-10-02T00:00:00Z")
    assert clm
    # demo smoke with temp db
    demo = pathlib.Path(__file__).resolve().parents[2]/"demo"/"evidence_foundation_demo.py"
    r = subprocess.run([sys.executable, str(demo), "--db", str(pathlib.Path(tmp)/"demo.db")], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
