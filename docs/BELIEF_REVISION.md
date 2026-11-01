# Belief Revision

**Reality Engine — Belief Revision Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines belief revision in Reality Engine. It covers how the system revises its understanding when new evidence arrives, how it preserves history, and how it reconstructs previous states.

---

## 1. Belief Revision Definition

Belief revision is the process by which the system updates its understanding when new evidence arrives. The system must revise its understanding without silently erasing history.

**Example:**

1. October 1: Initial hypothesis (inflation is increasing).
2. October 15: New observations (inflation increases).
3. November 1: Additional evidence (energy prices increase).
4. December 1: New economic data (core inflation declines).
5. December 15: Revised assessment (the original hypothesis is neither simply accepted nor rejected).

---

## 2. Revision Principles

| Principle | Description |
|---|---|
| **No silent erasure** | The system must not silently rewrite its historical understanding. |
| **Evidence grounding** | Revisions must be evidence-grounded. |
| **Auditability** | Every revision must be auditable. |
| **Dependency awareness** | Revisions must account for dependencies. |
| **Temporal consistency** | Revisions must be temporally consistent. |
| **Preservation** | The system must preserve previous interpretations. |

---

## 3. Revision Operations

| Operation | Meaning |
|---|---|
| CREATE | Create a new entity, claim, or hypothesis |
| SUPPORT | Add supporting evidence |
| QUALIFY | Add qualifying conditions |
| CHALLENGE | Add contradictory evidence |
| RETRACT | Remove a claim |
| REPLACE | Swap a claim for a corrected one |
| SUPERSEDE | Mark an older version as replaced |
| CORRECT_TEMPORAL_SCOPE | Fix the valid time range |
| REASSIGN_ENTITY | Change the subject entity |
| INVALIDATE_DEPENDENCY | Remove a dependency edge |
| REASSESS_HYPOTHESIS | Recalculate hypothesis status |

---

## 4. Belief Revision Examples

### 4.1 New Information

A new observation arrives. The system identifies affected claims and generates a revision proposal.

### 4.2 Correction

A correction to the temporal scope of a claim is recorded. The original claim is preserved.

### 4.3 Hypothesis Invalidation

A new observation invalidates a hypothesis. The system flags downstream hypotheses for reassessment.

---

## 5. Constraints

1. **Evidence preservation:** Evidence is never silently destroyed.
2. **Historical immutability:** A revision never changes the historical transaction record of an earlier accepted revision.
3. **Trigger recording:** Every accepted state transition has a recorded trigger.
4. **Evidence path:** Every factual state has a traceable evidence path or an explicitly documented exception.
5. **Unaffected claims preserved:** Unaffected claims are not modified merely because they are connected to a changed claim.
6. **Rejected proposals:** A rejected proposal cannot change accepted state.
7. **Historical queries:** Historical queries cannot silently incorporate future observations.

---

## 6. Summary

- Belief revision is the process by which the system updates its understanding.
- The system must preserve history.
- Revisions are auditable.
- The system supports eleven revision operations.
- The system enforces seven belief revision invariants.
