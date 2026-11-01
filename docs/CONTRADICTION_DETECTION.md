# Contradiction Detection

**Reality Engine — Contradiction Detection Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines contradiction detection in Reality Engine. It covers how the system detects genuine contradictions, distinguishes apparent contradictions from different time periods, units, or definitions, and handles conflicting sources.

---

## 1. Contradiction Detection Overview

Contradiction detection is the process of identifying genuine conflicts in the evidence.

**Examples:**

- Two sources report conflicting values for the same economic indicator.
- A government announces a policy; a later report says the policy was never enacted.
- A scientific paper reports a result; a later paper reports that the result was retracted.

---

## 2. Contradiction Types

| Type | Description |
|---|---|
| Genuine contradiction | Two sources contradict each other on the same subject |
| Apparent contradiction | Two sources appear contradictory but differ in time, units, or definition |
| Delayed reporting | A report arrived late |
| Corrected publication | A publication was corrected |
| Retracted publication | A publication was retracted |

---

## 3. Distinguishing Genuine from Apparent

The system must distinguish genuine contradictions from apparent contradictions.

**Apparent contradiction factors:**

| Factor | Description |
|---|---|
| Different time periods | The two sources refer to different times |
| Different units | The two sources use different units |
| Different definitions | The two sources use different definitions |
| Different geographic scopes | The two sources refer to different geographic scopes |
| Incomplete reporting | One source has incomplete information |

**Constraint:** The system must identify whether the contradiction is genuine or apparent.

---

## 4. Contradiction Detection Process

| Step | Action |
|---|---|
| 1 | Identify claims that could conflict. |
| 2 | Retrieve evidence for each claim. |
| 3 | Compare the claims. |
| 4 | Determine whether the conflict is genuine or apparent. |
| 5 | Flag the contradiction. |
| 6 | Update the claim status. |
| 7 | Flag downstream hypotheses for reassessment. |

---

## 5. Contradiction Resolution

| Resolution | Description |
|---|---|
| Retract | One claim is retracted due to the contradiction. |
| Qualify | One claim is qualified due to the contradiction. |
| Flag | The contradiction is flagged for human review. |
| Revise | The claims are revised based on the contradiction. |

---

## 6. Contradiction Constraints

1. **Identity:** Each contradiction must have a unique identifier.
2. **Temporal:** Contradictions have valid times.
3. **Provenance:** Each contradiction must have provenance.
4. **Versioning:** Contradictions have versions.
5. **Consistency:** The contradiction detection must be consistent.

---

## 7. Summary

- Contradiction detection identifies genuine conflicts in the evidence.
- It distinguishes genuine from apparent contradictions.
- It flags contradictions and updates claim status.
- It flags downstream hypotheses for reassessment.
- It handles delayed reporting, corrected publications, and retracted publications.
