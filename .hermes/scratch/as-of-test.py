import sys
sys.path.insert(0, "/Users/danielkliewer/Projects/reality-engine")
from reality_engine.core.temporal import materialize_world_state_at
import sqlite3
import tempfile
import pathlib

with tempfile.TemporaryDirectory() as tmp:
    db_path = pathlib.Path(tmp) / "test.db"
    
    import importlib
    db_module = importlib.import_module("reality_engine.database")
    
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.executescript(db_module.SCHEMA)
    conn.commit()
    
    # Register a domain
    dom_id = "dom_test"
    conn.execute("INSERT INTO domains (id, name, canonical_name, description, created_at) VALUES (?, ?, ?, ?, ?)",
        (dom_id, "Test", "test", "Test domain", "2026-11-01T00:00:00Z"))
    conn.commit()
    
    # Register an entity
    ent_id = "ent_test"
    conn.execute("INSERT INTO entities (id, canonical_name, entity_type, domain_id, created_at, status) VALUES (?, ?, ?, ?, ?, ?)",
        (ent_id, "Test", "TEST", dom_id, "2026-11-01T00:00:00Z", "ACTIVE"))
    conn.commit()
    
    # Register a source
    src_id = "src_test"
    conn.execute("INSERT INTO sources (id, name, source_type, canonical_domain, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
        (src_id, "Test Source", "NEWS", "test", "2026-11-01T00:00:00Z", "2026-11-01T00:00:00Z"))
    conn.commit()
    
    # Register a document
    doc_id = "doc_test"
    conn.execute("INSERT INTO documents (id, source_id, source_native_id, canonical_url, content_hash, content_type, language, published_at, collected_at, processing_status, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (doc_id, src_id, f"native_{doc_id}", "https://example.com/doc", "hash", "article", "en", "2026-10-01T00:00:00Z", "2026-11-01T00:00:00Z", "PROCESSED", "2026-11-01T00:00:00Z", "2026-11-01T00:00:00Z"))
    conn.commit()
    
    # Observation recorded_at = 2026-10-01 (BEFORE as-of 2026-10-05) - should appear
    obs_id = "obs_test"
    conn.execute("INSERT INTO observations (id, observation_type, subject_id, observed_value, recorded_at, source_id, document_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (obs_id, "REPORT", ent_id, "Test observation", "2026-10-01T00:00:00Z", src_id, doc_id, "2026-11-01T00:00:00Z", "2026-11-01T00:00:00Z"))
    conn.commit()
    
    # Claim recorded_at = 2026-11-01 (AFTER as-of 2026-10-05) - should NOT appear
    claim_id = "clm_test"
    conn.execute("INSERT INTO claims (id, subject_id, predicate, object_value, claim_type, domain_id, document_id, recorded_at, status, revision_number, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (claim_id, ent_id, "has_test", "test", "QUALITATIVE", dom_id, doc_id, "2026-11-01T00:00:00Z", "SUPPORTED", 1, "2026-11-01T00:00:00Z", "2026-11-01T00:00:00Z"))
    conn.commit()
    
    # Create claim version
    conn.execute("INSERT INTO claim_versions (id, claim_id, subject_id, predicate, object_value, claim_type, domain_id, document_id, recorded_at, status, revision_number, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (f"clmv_test", claim_id, ent_id, "has_test", "test", "QUALITATIVE", dom_id, doc_id, "2026-11-01T00:00:00Z", "SUPPORTED", 1, "2026-11-01T00:00:00Z"))
    conn.commit()
    
    # As-of reconstruction at 2026-10-05 (should see: entity, observation made on 2026-10-01, NOT claim)
    result = materialize_world_state_at(conn, "2026-10-05T00:00:00Z")
    
    print(f"=== As-of Reconstruction at 2026-10-05 ===")
    print(f"Entities: {len(result['entities'])} (expected 1)")
    print(f"Claims: {len(result['claims'])} (expected 0)")
    print(f"Observations: {len(result['observations'])} (expected 1)")
    
    obs_ids = [o['id'] for o in result['observations']]
    print(f"Observation IDs: {obs_ids}")
    
    clm_ids = [c['id'] for c in result['claims']]
    print(f"Claim IDs: {clm_ids}")
    
    # Verify correctness
    obs_present = obs_id in obs_ids
    clm_present = claim_id in clm_ids
    print(f"Observation present: {obs_present} (expected True)")
    print(f"Claim present: {clm_present} (expected False)")
    
    # D4 defect: was returning 0 for everything
    print(f"D4 defect reproduced: {len(result['claims']) == 0 and len(result['observations']) == 0} (should be False)")
    print(f"Before fix: D4 was 0 entities, 0 claims, 0 observations, 0 relationships, 0 events")
    print(f"After fix: {'BETTER' if obs_present else 'STILL BROKEN'}")
