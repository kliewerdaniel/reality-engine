# Source Lineage

**Reality Engine — Source Lineage Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines source lineage in Reality Engine. It defines how the system tracks the propagation of information from one source to another.

---

## 1. Source Lineage Definition

Source lineage is the graph of relationships showing how information propagated from one source to another.

**Example:**

```text
ORIGINAL STATEMENT → NEWS SOURCE A
ORIGINAL STATEMENT → NEWS SOURCE B
ORIGINAL STATEMENT → NEWS SOURCE C
ORIGINAL STATEMENT → NEWS SOURCE D
ORIGINAL STATEMENT → NEWS SOURCE E
```

The five media reports do not represent five independent observations. They share a common origin.

---

## 2. Source Lineage Fields

| Field | Description |
|---|---|
| id | Unique identifier |
| source_id_a | First source |
| source_id_b | Second source |
| relationship_type | Relationship type |
| confidence | Confidence |
| created_at | Creation timestamp |

**relationship_type values:**

| Type | Meaning |
|---|---|
| ORIGINAL | The original source |
| REPUBLISHING | A republishing source |
| QUOTED | A quoted source |
| SYNDICATED | Syndicated reporting |
| COMMON | A common source |
| INDEPENDENT | An independent source |

---

## 3. Source Independence

Source independence is the assessment of whether information from different sources is genuinely independent or derived from a common origin.

| Classification | Meaning |
|---|---|
| INDEPENDENT | Genuinely separate observations |
| SHARED_ORIGIN | Common source or dataset |
| PARTIALLY_DEPENDENT | Partially shared origin |
| UNKNOWN | Dependence cannot be determined |
| NOT_APPLICABLE | No relationship exists |

**Constraint:** An unknown relationship must not be interpreted as independence.

---

## 4. Constraints

1. **Identity:** Each source lineage record must have a stable unique identifier.
2. **Temporal:** Source lineage has valid times.
3. **Provenance:** Each source lineage record must have provenance.
4. **Versioning:** Source lineage has versions.
5. **Consistency:** Source lineage records must be consistent.
