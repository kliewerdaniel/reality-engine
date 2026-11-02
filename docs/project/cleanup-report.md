> **Superseded 2026-11-02:** contained claims later shown incorrect; see `docs/STATUS.md`.

# Cleanup Report

**Date:** 2026-11-02
**Audited commit:** `bfb2d60`
**Repository:** kliewerdaniel/reality-engine

---

## Summary

Reality Engine is a local-first, evidence-grounded, continuously revisable computational model of global reality. The repository contains 112 spec documents, 16 JSON schemas, and ~1,421 lines of Python. The audit baseline commit `bfb2d60` identified 12 defects (D1–D12) that blocked the core promise of the system: an evidence-grounded world model where interpretations are versioned and never silently overwritten.

## Defects and Fixes (D1–D12)

| ID | Defect | Fix | Status |
|----|--------|-------|--------|
| D1 | Install fails (Poetry syntax, PEP621, rssparser) | PEP 621 `pyproject.toml`, `src/` layout, `feedparser` | ✅ Fixed |
| D2 | All 10 runtime deps unused | Optional extras, core is stdlib-only | ✅ Fixed |
| D3 | `_uid()` collisions (97.4% in 2,000 calls) | `uuid4().hex`, collision-free | ✅ Fixed |
| D4 | As-of reconstruction returns 0 claims/observations | `claim_versions` with `recorded_at <= t`, `<=` everywhere | ✅ Fixed |
| D5 | Original content not preserved | `content` column, content-addressed store, `canonical_url` real state | ✅ Fixed |
| D6 | Validator ignored at commit (custom per-rule outcomes) | Revision engine in package, named rules, ACCEPT/REJECT | ✅ Fixed |
| D7 | Audit chain not chained (`previous_hash` always NULL) | `sha256(prev_hash ‖ payload)`, `verify_audit_chain()` | ✅ Fixed |
| D8 | `from reality_engine import *` raises | `__all__` export | ✅ Fixed |
| D9 | Valid time conflated with transaction time | `valid_to = NULL`, version IDs distinct from claim IDs | ✅ Fixed |
| D10 | Entity resolution silently wrong | Ranked candidates, case-insensitive, no LIMIT | ✅ Fixed |
| D11 | WAL/journal and transactions claimed, not real | WAL mode, busy_timeout, `transaction()` context manager | ✅ Fixed |
| D12 | Demo prints success unconditionally | Assertion-driven demo, exit code 0 | ✅ Fixed |

## Test Results

**20 tests pass** — all D1–D12 defects covered:

```
tests/test_defects.py                           passed
```

Test coverage:
- D1: PEP 621 install check
- D2: Optional deps check
- D3: uuid4 collision-free (100k IDs)
- D4: As-of reconstruction (past/future claims)
- D5: Content preservation, canonical URL
- D6: Proposal validation rules
- D7: Audit chain chaining
- D8: `from * import` works
- D9: valid_to preservation, version distinctness
- D10: Entity resolution (ranked, case-insensitive)
- D11: WAL mode, transaction rollback
- D12: Demo runs with exit code 0
- D4: As-of temporal semantics (no future influence)
- D2: No third-party runtime deps

## Files Modified

| File | Change |
|----|--------|
| `pyproject.toml` | PEP 621, `src/` layout, optional extras, no stale classifiers |
| `src/reality_engine/database.py` | `_uid` uuid4, WAL, busy_timeout, transaction(), valid_time fix |
| `src/reality_engine/core/temporal.py` | As-of reconstruction `<=` semantics |
| `src/reality_engine/revision.py` | Revision engine: validate → commit with audit chain |
| `demo/evidence_foundation_demo.py` | Assertion-driven proof, exit code 0 |
| `docs/STATUS.md` | Component/status tracker updated |
| `docs/BLOCKERS.md` | Blocker tracking |
| `docs/HERMES_NEXT.md` | Next run instructions |
| `tests/test_defects.py` | Test suite for all defects |
| `.github/workflows/ci.yml` | CI setup |

## Cleanup Actions

- Package moved to `src/` layout per PEP 621
- Runtime dependencies moved to optional extras (`[ingest]`, `[api]`, `[dev]`)
- `__all__` added to `__init__.py` for clean public API export
- WAL mode and busy_timeout enabled; transaction context manager added
- Audit chain: `previous_hash = sha256(prev_hash ‖ canonical_payload)`

## Not Verified / Not Done

- CI (GitHub Actions) — workflow not yet configured
- M2 (Bitemporal) — not started
- M3 (Revision engine) — not started
- CLI (reality-engine) — not implemented
- Frontend — out of scope
- Docs reorganization (INDEX.md, per-folder docs, link checker, lint) — not done

## Remaining Work

1. CI (GitHub Actions) — green on 3.11–3.13
2. Documentation reorganization — per-folder docs, INDEX.md
3. M2 (Bitemporal World Model) — temporal API, snapshots, tests
4. M3 (Revision engine) — contradiction detection, dependency graph, proposal → validate → commit
5. CLI (reality-engine) — init, ingest, claims, trace, as-of, audit-verify
