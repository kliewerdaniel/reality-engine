# Evidence Assessment

**Reality Engine — Evidence Assessment Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines evidence assessment in Reality Engine. It covers how evidence is assessed and how evidentiary assessments are recorded.

---

## 1. Evidence Assessment Definition

Evidence assessment is the process of assessing the quality and weight of evidence supporting or challenging a claim.

---

## 2. Assessment Dimensions

| Dimension | Question |
|---|---|
| Source reliability | How dependable is the source for this type of information? |
| Directness | Is the evidence direct or secondhand? |
| Corroboration | Are there genuinely independent sources? |
| Temporal validity | Is the information current? |
| Measurement quality | How reliable is the underlying measurement? |
| Interpretation | How much inference is required? |
| Contradiction | What evidence challenges the claim? |
| Completeness | What important information is missing? |

**Constraint:** These dimensions must remain independently inspectable. The system may optionally calculate confidence estimates, but the methodology must be explicit and domain-specific.

---

## 3. Constraints

1. **Identity:** Each evidence assessment record must have a stable unique identifier.
2. **Temporal:** Evidence assessment has valid times.
3. **Provenance:** Each evidence assessment record must have provenance.
4. **Versioning:** Evidence assessment has versions.
5. **Consistency:** Evidence assessment records must be consistent.
