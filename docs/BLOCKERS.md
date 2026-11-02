# BLOCKERS

## Current Blockers

| Blocker | Status | How to resolve |
|---------|--------|----------------|
| CI (GitHub Actions) not configured | Blocked | Create `.github/workflows/ci.yml`, verify green on 3.11–3.13 |
| M2 (Bitemporal) not started | Blocked | Proceed to M2 slice after CI is green |
| M3 (Revision engine) not started | Blocked | Proceed after M2 acceptance test passes |
| CLI (reality-engine) not implemented | Blocked | Not urgent this run; defer to later |
| Frontend | Blocked | Out of scope for this run |

## Infrastructure Notes

- **No API keys, tokens, passwords, or secrets** are present in the source material or repository. None were needed during the audit or fixes.
- **No network access required** in the test suite. All tests use fixtures and in-memory SQLite.
- **Local inference** (Ollama, llama.cpp) is out of scope for this run. Model selection is a future extension.

## Dependency Graph for Future Work

```
M1 (finish properly) → CI green → M2 (bitemporal) → M3 (revision engine) → CLI → Frontend
```

## Past Blockers (resolved)

| Blocker | Status | Resolution |
|---------|--------|------------|
| Install fails | ✅ Resolved | pyproject.toml rewritten in PEP 621, package installs |
| _uid() collisions | ✅ Resolved | uuid4().hex, 2000 unique IDs verified |
| from * import raises | ✅ Resolved | __all__ added to __init__.py |
| Valid time conflated | ✅ Resolved | valid_to = NULL for open claims, version IDs distinct |
| Entity resolution silently wrong | ✅ Resolved | Ranked candidates, case-insensitive |
| Transactions and WAL claimed, not real | ✅ Resolved | WAL mode, busy_timeout, transaction() context manager |
| Demo lies (prints success unconditionally) | ✅ Resolved | Demo assertion-driven, exit code 0 |
