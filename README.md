# Reality Engine

**Reality Engine** is a continuously operating, local-first computational system that constructs, maintains, evaluates, and revises a global representation of the world from heterogeneous observations. Evidence is immutable; interpretations are versioned; every state transition is deterministic and auditable.

**Status:** Remediation complete on `main` (merged from `hermes/remediate-and-m1`). Phases 0–7 M1 slice complete. 61 tests passing, ruff + mypy strict clean, coverage 85%, `gen_status --check` OK.
**Author:** Daniel Kliewer
**Classification:** Open research and software architecture
**Implementation philosophy:** Local-first, evidence-grounded, temporally consistent, continuously revisable intelligence infrastructure.

---

## 0. First End-to-End Proof

The defining capability is changing understanding of the world without losing the history of how it got there.

**`demo/evidence_foundation_demo.py`** runs the full eight-step evidence workflow:

1. Register a source and ingest an original document.
2. Preserve content, hash, collection time, provenance.
3. Extract a claim linked to an exact passage.
4. Ingest a second document challenging the claim.
5. Generate a revision proposal without changing accepted state.
6. Validate via deterministic rules.
7. Commit the accepted revision, preserving prior state.
8. Query both before and after world states.

```bash
cd /Users/danielkliewer/Projects/reality-engine
python demo/evidence_foundation_demo.py
```

---

## 1. Project Definition

Reality Engine separates three representations — **external reality**, **observation**, and **understanding** — with explicit transformations between them and deterministic governance over all changes to understanding. It preserves provenance, distinguishes valid time from transaction time, detects contradiction, tracks uncertainty, and revises interpretations without erasing history.

## 2. Foundational Principles

P1 evidence preservation · P2 provenance · P3 temporal integrity · P4 revision over replacement · P5 explicit uncertainty · P6 source independence · P7 domain separation · P8 deterministic governance (LLMs propose, never authorize) · P9 reproducibility · P10 model independence · P11 historical accountability · P12 observability awareness.

## 3. Repository Layout (actual)

```
reality-engine/
├── README.md
├── pyproject.toml
├── src/reality_engine/        # package (importable)
│   ├── database.py            # SQLite world model, transactions, entities, claims, spans
│   ├── revision.py            # RevisionEngine: proposals, validation rules, commit
│   ├── core/
│   │   ├── clock.py           # injectable clock (F-01)
│   │   └── temporal.py        # bitemporal reconstruction, as-of queries
│   ├── adapters/              # DirectoryAdapter, RssAdapter
│   ├── proposal/              # Proposal, ClaimProposer, RuleBasedProposer
│   ├── intelligence/          # ModelProvider, OllamaProvider (off-by-default)
│   ├── cli/                   # stdlib CLI: init/ingest/claims/trace/as-of/audit-verify/revise
│   └── tests/
├── tests/
│   ├── test_defects.py
│   ├── test_coverage_boost.py
│   ├── test_m1_modules.py
│   ├── e2e/test_first_proof.py
│   └── regression/            # test_findings.py, test_hindsight_oracle.py
├── demo/evidence_foundation_demo.py
├── docs/                      # comprehensive specs (see docs/README.md)
├── schemas/                   # versioned JSON Schemas
└── scripts/
    ├── gen_status.py          # regenerate docs/STATUS.md / docs/status.json
    ├── lint_docs.py
    └── check_links.py
```

## 4. Tech Stack

Python 3.12 (pyenv), stdlib core, SQLite (WAL), pytest, ruff, mypy (strict), jsonschema. No third-party runtime deps in core. Optional: Ollama for local inference (off-by-default).

## 5. Setup & Verification

```bash
cd /Users/danielkliewer/Projects/reality-engine
export PATH="/opt/homebrew/bin:$PATH"
PYENV_VERSION=3.12.3 pyenv exec python -m pytest -q          # 61 passed
PYENV_VERSION=3.12.3 pyenv exec python -m ruff check src tests
PYENV_VERSION=3.12.3 pyenv exec python -m mypy src --strict
PYENV_VERSION=3.12.3 pyenv exec python scripts/gen_status.py --check
```

## 6. CLI Usage

```bash
python -m reality_engine.cli init --db path.db
python -m reality_engine.cli ingest --db path.db --source Src --file doc.txt
python -m reality_engine.cli claims --db path.db
python -m reality_engine.cli trace --db path.db --claim <id>   # claim->span->document(hash)->source
python -m reality_engine.cli as-of --db path.db --at 2026-10-01T00:00:00Z
python -m reality_engine.cli audit-verify --db path.db
python -m reality_engine.cli revise --db path.db --proposal p.json
```

## 7. Development Guide for Agents

- Branch: work on `hermes/*` branches; never commit to `main` directly unless directed. Merge locally only.
- Python: `/Users/danielkliewer/.pyenv/versions/3.12.3/bin/python` (PYENV_VERSION=3.12.3).
- Run `python scripts/gen_status.py --check` at each boundary; regenerate docs/STATUS.md via `gen_status.py`.
- Tests before claims: real verification (pytest). Highlight pass counts.
- Fail closed: validators reject on any unverified rule; no placeholders.
- stdlib core: no non-stdlib imports in core modules.
- Mark unverified items open in `docs/status.json`.
- Do not start M3.
- Key pitfalls: span quoted_text must be checked against document content; source independence compares document source_id; temporal reconstruction filters recorded_at <= t and joins claim_versions; extract_source_span raises on mismatch.

### Navigation for continuation
- Core world model: `src/reality_engine/database.py`
- Revision governance: `src/reality_engine/revision.py`
- Temporal/bitemporal: `src/reality_engine/core/temporal.py`
- Adapters: `src/reality_engine/adapters/__init__.py`
- Proposals: `src/reality_engine/proposal/__init__.py`
- Inference (off-by-default): `src/reality_engine/intelligence/__init__.py`
- CLI: `src/reality_engine/cli/__init__.py`
- Findings tracker: `docs/status.json`; status: `docs/STATUS.md`
- Full spec index: `docs/README.md`

## 8. License

Open research and software architecture. See LICENSE.