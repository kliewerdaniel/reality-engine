# HERMES NEXT

## Summary of this run

Reality Engine cleanup and continued development — M1 (finish properly), M2 (bitememporal), M3 (revision engine).

### What was verified

- **All 20 pytest tests pass** — D1–D12 fixes confirmed
- **Demo runs with exit code 0** — assertion-driven proof of the revision behavior
- **Package install works** — `pip install -e .` succeeds on Python 3.11–3.13
- **Audit chain verified** — `previous_hash` chaining works correctly
- **Temporal as-of reconstruction verified** — claim versions and as-of reads work correctly
- **Entity resolution with aliases verified** — ranked candidates, case-insensitive

### What is verified

| Item | Status |
|------|--------|
| 20 pytest tests pass | ✅ |
| Demo runs with exit code 0 | ✅ |
| Package installs | ✅ |
| Audit chain verifies and detects tampering | ✅ |
| As-of reconstruction correct | ✅ |
| Document content preserved | ✅ |
| Entity aliases resolved to stable identities | ✅ |
| Entity resolution ranked candidates | ✅ |
| WAL mode, busy_timeout, transaction() | ✅ |
| Transaction rollback on failure | ✅ |

### What is blocked / not verified

| Item | Status | Notes |
|------|--------|-------|
| CI (GitHub Actions) | Blocked | Workflow not yet configured |
| CLI (reality-engine) | Blocked | Not implemented |
| M2 (Bitemporal) | Blocked | Not started |
| M3 (Revision engine) | Blocked | Approvals not yet in code |
| Docs reorganization (INDEX.md, per-folder docs) | Blocked | Not done |

## Next three slices with definitions of done

### Slice 1: CI and remaining doc setup (definition of done)

1. GitHub Actions workflow green on Python 3.11, 3.12, 3.13
2. ruff check and mypy strict pass
3. pytest -v all pass
4. Doc link checker and lint pass
5. Docs reorganization complete with INDEX.md
6. docs/STATUS.md, docs/BLOCKERS.md, docs/HERMES_NEXT.md current

### Slice 2: M2 (Bitemporal World Model) (definition of done)

1. Bitemporal read API: `as_of(transaction_time)`, `valid_at(valid_time)`, combined
2. Temporal validation rules
3. World-state snapshots
4. Hindsight contamination and temporal tests written
5. All tests pass (pytest -v)

### Slice 3: M3 (Revision Engine) (definition of done)

1. Contradiction detection
2. Dependency-graph propagation
3. Proposal → validate → commit with source-independence checks
4. Stale-proposal refusal
5. Transactional commit
6. Human-readable explanation output
7. Integration test (GETTING_STARTED_FIRST_PROOF) passes

## Stop conditions

- Suite red and cannot fix
- Change would violate an invariant (P1–P11)
- ADR needed and choice genuinely the author's
- M3 acceptance test green and report written
