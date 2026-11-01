# Revision Model

**Reality Engine — Revision Model Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the formal revision model of Reality Engine. It defines the state categories, revision operations, dependency semantics, and the revision transaction.

---

## 1. State Categories

The revision engine manages the following state categories:

| State Category | Meaning |
|---|---|
| **ACCEPTED** | The state has been accepted and is part of the world model. |
| **PROPOSED** | The state has been proposed but not yet validated or accepted. |
| **HISTORICAL** | The state is part of the historical record. Preserved and recoverable. |
| **SUPERSEDED** | The state has been replaced by a newer version. |
| **REJECTED** | A proposal was rejected. The rejection is recorded. |
| **UNRESOLVED_ASSESSMENT** | An assessment that remains unresolved. |

---

## 2. Revision Operations

### 2.1 Primary Operations

| Operation | Meaning |
|---|---|
| **CREATE** | Create a new entity, claim, or hypothesis. |
| **SUPPORT** | Add supporting evidence to an existing claim. |
| **QUALIFY** | Add qualifying conditions to an existing claim. |
| **CHALLENGE** | Add contradictory evidence to an existing claim. |
| **RETRACT** | Remove a claim. |
| **REPLACE** | Swap a claim for a corrected claim. |
| **SUPERSEDE** | Mark an older version as replaced. |
| **CORRECT_TEMPORAL_SCOPE** | Fix the valid time range. |
| **REASSIGN_ENTITY** | Change the subject entity. |
| **INVALIDATE_DEPENDENCY** | Remove a dependency edge. |
| **REASSESS_HYPOTHESIS** | Recalculate the hypothesis status. |

**Constraint:** Additional operations may be necessary. The revision state machine must support any operation that is needed.

---

## 3. Dependency Semantics

The revision engine maintains explicit dependencies between conclusions.

### 3.1 Dependency Types

| Type | Meaning |
|---|---|
| DIRECT | The claim directly depends on the prerequisite. |
| TRANSITIVE | The claim indirectly depends on the prerequisite. |
| INDEPENDENT_SUPPORT | Multiple independent pieces of evidence support the same claim. |
| ALTERNATIVE_SUPPORT | Multiple pieces of evidence provide alternative support. |
| CIRCULAR | A circular dependency exists. |
| INVALID | The dependency is invalid. |
| CROSS_DOMAIN | The dependency spans domains. |

### 3.2 Dependency Traversal

| Step | Action |
|---|---|
| 1 | Identify the directly affected claims. |
| 2 | Traverse the dependency graph to find downstream hypotheses. |
| 3 | Evaluate whether the supporting evidence remains valid. |
| 4 | Recalculate affected assessments. |
| 5 | Preserve unaffected assessments. |
| 6 | Record the revision. |

**Constraint:** Correlation must never silently become a causal relationship.

---

## 4. Revision Transaction

A revision transaction must:

1. Capture the triggering observation.
2. Identify affected records.
3. Capture relevant prior versions.
4. Generate proposed changes.
5. Validate dependencies.
6. Validate evidence.
7. Validate temporal consistency.
8. Apply authorization rules.
9. Commit changes atomically.
10. Record the resulting audit events.

**Constraint:** If any stage fails, the transaction is rolled back.

---

## 5. Revision Invariants

| Invariant | Description |
|---|---|
| **Evidence preservation** | Evidence is never silently destroyed. |
| **Historical immutability** | A revision never changes the historical transaction record of an earlier accepted revision. |
| **Trigger recording** | Every accepted state transition has a recorded trigger. |
| **Evidence path** | Every factual state has a traceable evidence path or an explicitly documented exception. |
| **Unaffected claims preserved** | Unaffected claims are not modified merely because they are connected to a changed claim. |
| **Rejected proposals** | A rejected proposal cannot change accepted state. |
| **Historical queries** | Historical queries cannot silently incorporate future observations. |

**Constraint:** Additional invariants may be necessary. Every invariant must have executable test scenarios.

---

## 6. Revision Outcomes

| Outcome | Meaning |
|---|---|
| NEW_INFORMATION | New evidence requiring review |
| SUPPORTED | Existing claim is supported |
| PARTIALLY_SUPPORTED | Some evidence supports, some challenges |
| CHALLENGED | Existing claim is challenged |
| CONTRADICTED | Existing claim is contradicted |
| SUPERSEDED | Replaced by a newer version |
| WITHDRAWN | Explicitly withdrawn |
| UNRESOLVED | Cannot be resolved |
| NO_CHANGE | No effect on current understanding |

---

## 7. Revision States

| State | Meaning |
|---|---|
| PROPOSED | The revision proposal has been generated. |
| VALIDATED | The proposal has been validated. |
| COMMITTED | The revision has been committed. |
| REJECTED | The proposal has been rejected. |
| ROLLING_BACK | The revision is being rolled back. |
| ROLLED_BACK | The revision has been rolled back. |
| AWAITING_REVIEW | Awaiting review. |

---

## 8. Revision Pseudocode

```python
def process_revision(observation):
    affected = identify_directly_affected_claims(observation)
    dependency_set = traverse_dependencies(affected)
    proposals = []
    for item in dependency_set:
        proposal = generate_revision_proposal(
            item=item,
            new_observation=observation,
            evidence=load_related_evidence(item),
            dependencies=load_dependencies(item)
        )
        proposals.append(proposal)
    validated = validate_revision_proposals(proposals)
    return commit_revision_transaction(validated)
```

---

## 9. Revision Examples

### 8.1 New Information

A new observation arrives. The revision engine identifies affected claims and generates a proposal.

### 8.2 Correction

A correction to the temporal scope of a claim is recorded as a new event. The original record is preserved.

### 8.3 Hypothesis Invalidation

A new observation invalidates a hypothesis. The system flags downstream hypotheses for reassessment.

---

## 10. Summary

- The revision engine manages six state categories.
- It supports eleven primary revision operations.
- It maintains explicit dependencies between conclusions.
- It enforces five revision invariants.
- It manages nine revision outcomes.
- It supports seven revision states.

---

## 11. References

- ONTOLOGY.md — common ontology definitions
- TEMPORAL_MODEL.md — bitemporal semantics
- HYPOTHESIS_MODEL.md — hypothesis definitions
- FORECAST_MODEL.md — forecast definitions
- BELIEF_REVISION.md — belief revision
- REVISION_STATE_MACHINE.md — revision state machine
- DEPENDENCY_GRAPH.md — dependency graph
- REVISION_VALIDATION.md — revision validation
- REVISION_TRANSACTION_MODEL.md — revision transaction model
