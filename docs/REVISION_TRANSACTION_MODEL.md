# Revision Transaction Model

**Reality Engine — Revision Transaction Model Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the revision transaction model of Reality Engine. It covers transaction boundaries, idempotency, cycle detection, revision ordering, conflict handling, failure recovery, and dependency version checks.

---

## 1. Revision Transaction

A revision transaction is a transaction containing all changes from a revision proposal. The transaction is committed atomically.

---

## 2. Transaction Boundaries

The transaction boundaries are:

1. **Proposal generation:** The proposal is generated.
2. **Validation:** The proposal is validated.
3. **Commit:** The proposal is committed.
4. **Audit:** The audit events are recorded.

**Constraint:** If any stage fails, the transaction is rolled back.

---

## 3. Idempotency

The system must support idempotent processing. Each processing operation must use an idempotency key so that reprocessing the same document does not create duplicate observations or artificially increase confidence.

| Field | Description |
|---|---|
| idempotency_key | Unique idempotency key |
| operation | The operation |
| result | The result |
| created_at | Creation timestamp |

---

## 4. Cycle Detection

The system must detect cyclic dependencies. If a cycle is found, the system must flag it and not proceed with the revision.

---

## 5. Revision Ordering

| Order | Description |
|---|---|
| Temporal order | Revisions are ordered by time |
| Dependency order | Revisions are ordered by dependencies |

---

## 6. Conflict Handling

| Conflict Type | Resolution |
|---|---|
| Temporal | Use bitemporal records to determine the correct valid time |
| Provenance | Resolve by evaluating domain- and claim-specific authority dimensions; do not use a single universal authority score |
| Evidence | Evaluate remaining evidence independently |
| Dependency | Flag for reassessment without automatic reversal |

---

## 7. Failure Recovery

| Failure | Recovery |
|---|---|
| Proposal generation | Retry or abort |
| Validation failure | Record the rejection |
| Commit failure | Record the failure and retry |
| Audit recording failure | Record the failure and retry |

---

## 8. Dependency Version Checks

Each dependency must record its version. When a dependency changes, the dependent conclusion must be flagged.

| Field | Description |
|---|---|
| dependency_id | Unique identifier |
| dependent_id | Dependent conclusion |
| prerequisite_id | Prerequisite conclusion |
| dependency_type | Type of dependency |
| version | Dependency version |
| status | Status of the dependency |

---

## 9. Audit Requirements

All significant state transitions must produce audit events:

| Event | Description |
|---|---|
| REVISION_PROPOSED | A revision proposal has been generated |
| REVISION_VALIDATED | A revision proposal has been validated |
| REVISION_REJECTED | A revision proposal has been rejected |
| REVISION_COMMITTED | A revision proposal has been committed |
| REVISION_ROLLED_BACK | A revision has been rolled back |

**Constraint:** The audit ledger is append-only.

---

## 10. Summary

- Revision transactions are committed atomically.
- The system supports idempotent processing.
- The system detects cyclic dependencies.
- The system orders revisions by time and dependency.
- The system handles conflicts in four ways.
- The system recovers from failures.
- The system checks dependency versions.
- The audit ledger is append-only.
