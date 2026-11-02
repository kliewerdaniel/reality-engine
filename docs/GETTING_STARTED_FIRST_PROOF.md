# Getting Started: First End-to-End Proof

**Reality Engine — First End-to-End Proof Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document explains how to run the first end-to-end proof of Reality Engine.

---

## 1. Overview

The defining capability of Reality Engine is not a dashboard, a multi-agent system, or a global ingestion network. It is the ability to **change its understanding of the world without losing the history of how it got there**.

The first executable proof is in the `demo/` directory.

---

## 2. The Demo Script

**File:** `demo/evidence_foundation_demo.py`

The script executes the eight-step workflow defined in the acceptance criteria:

| Step | Action | Result |
|---|---|---|
| 1 | Register a source and ingest an original document | Source `src_*`, document `doc_*` created |
| 2 | Preserve content, hash, collection time, and provenance | Document content hash stored; source_span recorded |
| 3 | Extract a claim and link it to an exact passage | Claim `clm_*` with source_span `span_*` |
| 4 | Ingest a second document that challenges the claim | Second document `doc_*` with CONTRADICTS link |
| 5 | Generate a revision proposal without changing accepted state | Proposal `revp_*`; state unchanged |
| 6 | Validate the proposal through deterministic rules | Validation: CHALLENGED; PASS |
| 7 | Commit the accepted revision while preserving previous state | Revision `rev_*`; previous hash preserved |
| 8 | Query both what the system believed before and what it believes now | Previous and current states both available |

---

## 3. How to Run

```bash
cd /Users/danielkliewer/Projects/reality-engine
python demo/evidence_foundation_demo.py
```

The script creates a SQLite database at `demo/demo_evidence_foundation.db`.

---

## 4. Expected Output

A successful run prints:

```
[0] Initializing database...
[1] Registering source and ingesting original document...
[2] Extracting claim with source-span provenance...
[3] Ingesting second document that challenges the claim...
[4] Generating revision proposal (no state change yet)...
[5] Validating proposal through deterministic rules...
[6] Committing accepted revision while preserving previous state...
[7] Querying both states...

End-to-End Proof Complete
```

---

## 5. What the Proof Demonstrates

The proof demonstrates that the system can:

1. **Register a source** — creates a source registry entry.
2. **Preserve content** — stores the document, its hash, collection time, and processing status.
3. **Extract a claim with provenance** — the claim is linked to the exact source passage (character offsets, page, quoted text).
4. **Detect a challenge** — the second document contains contradictory evidence, linked via `CONTRADICTS`.
5. **Generate a proposal without changing state** — the revision proposal is created with status `PROPOSED`; the claim remains `SUPPORTED`.
6. **Validate deterministically** — validation checks schema, provenance, temporal consistency, and source independence.
7. **Commit with history preserved** — the claim status changes to `CONTESTED`; the previous state hash is recorded in the `revisions` table.
8. **Query both states** — the current claim status is `CONTESTED`; the previous state hash is queryable from the revision history.

---

## 6. Acceptance Test

**The system must be able to explain exactly what changed, why it changed, which evidence caused the change, and what it previously understood.**

From the demo output:

```
[7] Querying both states...
     Current claim status: CONTESTED
     Revisions on record: 1
       - CONTESTED: ACCEPT
```

The claim changed from `SUPPORTED` to `CONTESTED` because of the contradictory evidence from the second document. The previous state hash is preserved in the `revisions` table. The system can explain:

- **What changed:** Claim status from SUPPORTED to CONTESTED.
- **Why:** Second document (economist question) contradicted the original claim.
- **Which evidence caused the change:** `evl_...ee915a7c` (CONTRADICTS relationship).
- **What it previously understood:** The claim was SUPPORTED (status before revision).

---

## 7. Files

| File | Purpose |
|---|---|
| `demo/evidence_foundation_demo.py` | The first end-to-end proof |
| `demo/demo_evidence_foundation.db` | SQLite database created by the proof |
| `docs/README.md` | Full documentation index (with proof reference) |

---

## 8. Next Steps

After this proof succeeds:

1. Review the database schema in `docs/DATABASE_SCHEMA.md`.
2. Review the revision model in `docs/REVISION_MODEL.md`.
3. Review the architecture decisions in `docs/ARCHITECTURE_DECISIONS.md`.
4. Build the next milestone: extend the proof to handle domain-specific claims.
