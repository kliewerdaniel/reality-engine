# Revision Model

**Reality Engine — Revision Model Document**
**Version:** 0.1.1
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

## 2. Claim Identity vs. Versioning vs. Assessment

A claim is an enduring assertion about the world. It must not disappear when new evidence arrives. Instead, the system administers a claim's lifecycle through distinct mechanisms:

### 2.1 Claim Identity

A claim is identified by its `id`. The claim persists across revisions. Its identity, subject, predicate, and object description remain stable.

- The claim "Inflation is increasing" has one identity even if the system's assessment changes.
- Retraction is not removal; the claim remains in the model with a new status.

### 2.2 Claim Versions

A claim may have successive versions that represent changes in formulation, temporal scope, or supporting evidence.

- A claim's `object_value` may change over time, with each change creating a new version.
- The current version is the one the system would present as its current understanding.
- Historical versions are preserved in `revision_events` and `world_states`.

### 2.3 Evidence Assessments

Each piece of evidence is assessed separately against the claim via evidence links.

- SUPPORTS, CONTRADICTS, QUALIFIES, CORROBORATES relationships are attached to specific observations.
- The assessment status of each evidence link is independent and versioned.
- The claim's overall status is the aggregation of its evidence links.

### 2.4 Current Epistemic Status

The claim's current assessment reflects the system's latest understanding, given all available evidence:

| Status | Meaning |
|---|---|
| UNASSESSED | No assessment yet |
| SUPPORTED | Evidence predominantly supports |
| PARTIALLY_SUPPORTED | Mix of support and challenge |
| CONTESTED | Competing evidence exists |
| CONTRADICTED | Evidence predominantly contradicts |
| UNSUPPORTED | Insufficient evidence; not the same as contradicted |
| WITHDRAWN | Source has withdrawn the claim |
| SUPERSEDED | Replaced by a newer claim version |

### 2.5 Historical Assessment

A claim's historical assessment is what the system believed at a specific knowledge time, given only information available at that time. This is distinct from the current assessment.

- Historical querying must use `recorded_at` ≤ the requested knowledge time.
- Historical assessments are reconstructed from the audit trail.

---

## 3. Revision Operations

The revision engine supports the following operations. None of these removes a claim from the model; they all preserve the claim's identity and record the change explicitly.

| Operation | Meaning |
|---|---|
| **CREATE** | Create a new entity, claim, or hypothesis. The claim acquires a new identity. |
| **SUPPORT** | Add supporting evidence to an existing claim. |
| **QUALIFY** | Add qualifying conditions to an existing claim. |
| **CHALLENGE** | Add contradictory evidence to an existing claim. |
| **RETRACT** | Change a claim's status to WITHDRAWN, preserving the claim record and its history. The claim no longer reflects current understanding but is not removed. |
| **REPLACE** | Create a new claim version that supersedes the old one. The old version is marked SUPERSEDED. |
| **SUPERSEDE** | Mark an older claim version as replaced. Both versions remain. |
| **CORRECT_TEMPORAL_SCOPE** | Fix or refine the valid time range of a claim. The claim record is preserved with a new version. |
| **REASSIGN_ENTITY** | Change the subject entity of a claim. The claim record and its history are preserved. |
| **INVALIDATE_DEPENDENCY** | Remove a dependency edge. The dependency is marked INVALID. |
| **REASSESS_HYPOTHESIS** | Recalculate the hypothesis status. |

**Constraint:** Any operation that would remove a claim must instead change the claim's status to a lifecycle state (WITHDRAWN, SUPERSEDED, or REJECTED) and preserve the claim record, its evidence links, and its history.

---

## 4. Dependency Semantics

The revision engine maintains explicit dependencies between conclusions.

### 4.1 Dependency Types

| Type | Meaning |
|---|---|
| DIRECT | The claim directly depends on the prerequisite. |
| TRANSITIVE | The claim indirectly depends on the prerequisite. |
| INDEPENDENT_SUPPORT | Multiple independent pieces of evidence support the same claim. |
| ALTERNATIVE_SUPPORT | Multiple pieces of evidence provide alternative support. |
| CIRCULAR | A circular dependency exists. |
| INVALID | The dependency is invalid. |
| CROSS_DOMAIN | The dependency spans domains. |

### 4.2 Dependency Traversal

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

## 5. Revision Transaction

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

## 6. Revision Invariants

The revision engine enforces the following invariants:

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

## 7. Revision Outcomes

| Outcome | Meaning |
|---|---|
| NEW_INFORMATION | New evidence requiring review |
| SUPPORTED | Existing claim is supported |
| PARTIALLY_SUPPORTED | Some evidence supports, some challenges |
| CHALLENGED | Existing claim is challenged |
| CONTRADICTED | Existing claim is contradicted |
| SUPERSEDED | Replaced by a newer version |
| WITHDRAWN | Explicitly withdrawn; claim record preserved |
| UNRESOLVED | Cannot be resolved |
| NO_CHANGE | No effect on current understanding |

---

## 8. Revision States

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

## 9. Revision Pseudocode

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

## 10. Revision Examples

### 10.1 New Information

A new observation arrives. The revision engine identifies affected claims and generates a proposal.

### 10.2 Correction

A correction to the temporal scope of a claim is recorded as a new event. The original record is preserved.

### 10.3 Claim Retraction

A source withdraws a claim. The system changes the claim's status to WITHDRAWN. The claim record, its evidence links, and its history are preserved. The claim is no longer part of the current understanding.

### 10.4 Hypothesis Invalidation

A new observation invalidates a hypothesis. The system flags downstream hypotheses for reassessment.

---

## 11. Summary

- The revision engine manages seven state categories.
- It supports eleven primary revision operations.
- It maintains explicit dependencies between conclusions.
- It enforces seven revision invariants.
- It manages nine revision outcomes.
- It supports seven revision states.

---

## 12. References

- ONTOLOGY.md — common ontology definitions
- TEMPORAL_MODEL.md — bitemporal semantics
- HYPOTHESIS_MODEL.md — hypothesis definitions
- FORECAST_MODEL.md — forecast definitions
- BELIEF_REVISION.md — belief revision
- REVISION_STATE_MACHINE.md — revision state machine
- DEPENDENCY_GRAPH.md — dependency graph
- REVISION_VALIDATION.md — revision validation
- REVISION_TRANSACTION_MODEL.md — revision transaction model
