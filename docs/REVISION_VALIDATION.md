# Revision Validation

**Reality Engine — Revision Validation Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the validation of revision proposals in Reality Engine. It covers schema validation, provenance validation, temporal consistency validation, source independence, source quality, and governance.

---

## 1. Validation Overview

Validation ensures that a revision proposal is correct before it is committed. Validation occurs in the revision engine and is enforced by the Frozen Spine.

---

## 2. Validation Layers

| Layer | Description |
|---|---|
| Database | Proper timestamp types, interval semantics |
| Application | Validation rules |
| Governance | Validated revisions |

---

## 3. Schema Validation

Schema validation checks:

| Check | Description |
|---|---|
| Required fields | Required fields are present |
| Types | Field types are correct |
| Constraints | Field constraints are satisfied |
| References | Foreign keys reference existing objects |

---

## 4. Provenance Validation

Provenance validation checks:

| Check | Description |
|---|---|
| Source reference | The claim is traceable to a source |
| Document reference | The claim is traceable to a document |
| Passage reference | The claim is traceable to a passage |
| Extraction model | The extraction model and version are recorded |
| Validation | The claim passed validation |

**Constraint:** A claim without provenance may exist as an explicitly unverified hypothesis, but it must not enter the verified factual state.

---

## 5. Temporal Consistency Validation

Temporal consistency validation checks:

| Check | Description |
|---|---|
| valid_from ≤ valid_to | If valid_to is set, valid_from must be less than or equal to valid_to |
| recorded_at ≥ valid_from | recorded_at must be greater than or equal to valid_from |
| UTC | All timestamps are in UTC |
| No future | Historical queries cannot silently incorporate future observations |

---

## 6. Source Independence Validation

Source independence validation checks:

| Check | Description |
|---|---|
| Source independence | Reported independence must be genuine |
| Shared origin | Shared origins are flagged |
| Syndicated reporting | Syndicated reporting is distinguished from independent confirmation |

**Constraint:** An unknown relationship must not be interpreted as independence.

---

## 7. Source Quality Validation

Source quality validation checks:

| Check | Description |
|---|---|
| Source reliability | The source is reliable for this type of information |
| Directness | The evidence is direct or secondhand |
| Measurement quality | The underlying measurement is reliable |
| Corroboration | Independent sources corroborate |

**Constraint:** Do not collapse evidence quality into one universal reliability score.

---

## 8. Governance Validation

Governance validation checks:

| Check | Description |
|---|---|
| Authorized actor | The actor is authorized |
| Permitted operation | The operation is permitted |
| Least privilege | The actor has the least privilege necessary |
| Sandboxed document processing | Untrusted documents are processed in a sandbox |

---

## 9. Validation Results

| Result | Meaning |
|---|---|
| ACCEPT | The proposal is accepted. |
| REJECT | The proposal is rejected. |
| NEEDS_REVIEW | The proposal requires further review. |

---

## 10. Validation Constraints

1. **Identity:** Each validation has a unique identifier.
2. **Temporal:** Validation has valid times.
3. **Provenance:** Validation has provenance.
4. **Versioning:** Validation has versions.
5. **Consistency:** Validation must be consistent.

---

## 11. Summary

- Validation has three layers.
- Schema validation checks structure.
- Provenance validation checks traceability.
- Temporal consistency validation checks temporal rules.
- Source independence validation checks independence.
- Source quality validation checks quality.
- Governance validation checks authorization.
- Validation results are ACCEPT, REJECT, or NEEDS_REVIEW.
