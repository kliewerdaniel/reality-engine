import pytest

@pytest.mark.xfail(strict=True, reason="F-03")
def test_f03_fabricates_canonical_url():
    import tempfile, pathlib
    from reality_engine.database import Database
    db = Database(pathlib.Path(tempfile.mkdtemp())/"t.db")
    dom = db.register_domain("Econ","d")
    src = db.register_source("Src","NEWS","econ")
    doc = db.ingest_document(src, "Inflation reached 3.2 percent.", "article", "en", "2026-10-01T00:00:00Z")
    row = db.conn.execute("SELECT canonical_url FROM documents WHERE id=?", (doc,)).fetchone()
    assert row["canonical_url"] is None

@pytest.mark.xfail(strict=True, reason="F-04")
def test_f04_deduplication():
    import tempfile, pathlib
    from reality_engine.database import Database
    db = Database(pathlib.Path(tempfile.mkdtemp())/"t.db")
    dom = db.register_domain("Econ","d")
    src = db.register_source("Src","NEWS","econ")
    d1 = db.ingest_document(src, "same", "article", "en", "2026-10-01T00:00:00Z")
    d2 = db.ingest_document(src, "same", "article", "en", "2026-10-01T00:00:00Z")
    assert d1 == d2

@pytest.mark.xfail(strict=True, reason="F-08")
def test_f08_transaction_rollback():
    import tempfile, pathlib
    from reality_engine.database import Database
    db = Database(pathlib.Path(tempfile.mkdtemp())/"t.db")
    try:
        with db.transaction():
            db.register_domain("ShouldRollBack","x")
            raise RuntimeError("boom")
    except Exception:
        pass
    n = db.conn.execute("SELECT COUNT(*) c FROM domains WHERE name='ShouldRollBack'").fetchone()["c"]
    assert n == 0

@pytest.mark.xfail(strict=True, reason="F-10")
def test_f10_asof_status():
    import tempfile, pathlib
    from reality_engine.database import Database
    from reality_engine.revision import RevisionEngine
    from reality_engine.core.temporal import reconstruct_claims_at
    tmp = tempfile.mkdtemp()
    db = Database(pathlib.Path(tmp)/"t.db")
    dom = db.register_domain("Econ","d")
    src = db.register_source("Src","NEWS","econ")
    ent = db.register_entity("Inflation","ECONOMIC_MEASUREMENT",dom,["cpi"])
    doc = db.ingest_document(src, "Inflation reached 3.2 percent in October.", "article", "en", "2026-10-01T00:00:00Z")
    span = db.extract_source_span(doc, "Inflation reached 3.2 percent", 1, 0, 29)
    clm = db.submit_claim(ent, "has_rate", "3.2", "QUANTITATIVE", dom, doc, span, recorded_at="2026-10-02T00:00:00Z")
    obs = db.register_observation(doc, src, ent, "challenge", "2026-10-06T00:00:00Z")
    eng = RevisionEngine(db)
    prop = {"proposal_id":"rp","affected_records":[clm],"entity_id":ent,
            "trigger_observation_id":obs,"challenge_evidence_id":span,
            "proposed_status":"CONTESTED","current_state":{"status":"SUPPORTED","revision_number":1}}
    eng.commit_revision(prop, eng.validate_proposal(prop))
    past = reconstruct_claims_at(db.conn, ent, "2026-10-15T00:00:00Z")
    assert past and past[0]["status"] == "SUPPORTED"

@pytest.mark.xfail(strict=True, reason="F-11")
def test_f11_relationships_filter():
    import tempfile, pathlib
    from reality_engine.database import Database
    from reality_engine.core.temporal import materialize_world_state_at
    tmp = tempfile.mkdtemp()
    db = Database(pathlib.Path(tmp)/"t.db")
    dom = db.register_domain("Econ","d")
    src = db.register_source("Src","NEWS","econ")
    ent = db.register_entity("Inflation","ECONOMIC_MEASUREMENT",dom,["cpi"])
    e_b = db.register_entity("Other","X",dom)
    db.register_relationship("MEASURED_BY", ent, e_b, recorded_at="2026-10-02T00:00:00Z")
    db.register_relationship("MEASURED_BY", ent, e_b, recorded_at="2026-12-15T00:00:00Z")
    snap = materialize_world_state_at(db.conn, "2026-12-01T00:00:00Z")
    recs = sorted(r["recorded_at"] for r in snap["relationships"])
    assert recs == ["2026-10-02T00:00:00Z"]

@pytest.mark.xfail(strict=True, reason="F-12")
def test_f12_hindsight_events():
    import tempfile, pathlib
    from reality_engine.database import Database
    from reality_engine.core.temporal import materialize_world_state_at
    tmp = tempfile.mkdtemp()
    db = Database(pathlib.Path(tmp)/"t.db")
    dom = db.register_domain("Econ","d")
    src = db.register_source("Src","NEWS","econ")
    ent = db.register_entity("Inflation","ECONOMIC_MEASUREMENT",dom,["cpi"])
    db.register_event("DEBATE", "late-recorded event", occurred_at="2026-10-01T00:00:00Z",
                      recorded_at="2026-11-20T00:00:00Z")
    snap = materialize_world_state_at(db.conn, "2026-10-05T00:00:00Z")
    leaked = [e for e in snap["events"] if e["recorded_at"] > "2026-10-05T00:00:00Z"]
    assert len(leaked) == 0
