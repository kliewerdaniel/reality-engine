# Information Reliability

**Reality Engine — Information Reliability Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines information reliability in Reality Engine. It covers how the system assesses the reliability of information and how reliability is recorded.

---

## 1. Information Reliability Definition

Information reliability is the assessment of the reliability of information. It is distinct from evidence quality. Information reliability focuses on the reliability of the information itself, not the quality of the evidence.

---

## 2. Reliability Dimensions

| Dimension | Question |
|---|---|
| Source reliability | How dependable is the source for this type of information? |
| Directness | Is the information direct or secondhand? |
| Corroboration | Are there genuinely independent sources? |
| Temporal validity | Is the information current? |
| Measurement quality | How reliable is the underlying measurement? |
| Interpretation | How much inference is required? |
| Contradiction | What evidence challenges the claim? |
| Completeness | What important information is missing? |

**Constraint:** These dimensions must remain independently inspectable. The system may optionally calculate confidence estimates, but the methodology must be explicit and domain-specific.

---

## 3. Constraints

1. **Identity:** Each information reliability record must have a stable unique identifier.
2. **Temporal:** Information reliability has valid times.
3. **Provenance:** Each information reliability record must have provenance.
4. **Versioning:** Information reliability has versions.
5. **Consistency:** Information reliability records must be consistent.
