# Systems Integrator Specification

**Reality Engine — Systems Integrator Specification Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the Systems Integrator specification. It defines the structured input, output, permissions, error handling, model selection, and evaluation requirements.

---

## 1. Systems Integrator Role

The Systems Integrator coordinates revision proposals and updates affected world-state projections.

---

## 2. Input

**Context:**

- Observations
- Context

**Prompt:**

- Context
- Task: coordinate the agents and generate revision proposals

**Expected output format:**

```json
{
  "revision_proposal": {
    "proposal_id": "proposal_000001",
    "trigger_observation_id": "obs_000001",
    "affected_records": ["record_1"],
    "changes": ["change 1"],
    "dependencies": ["dependency 1"],
    "status": "PROPOSED"
  },
  "timestamp": "2026-11-01T12:00:00Z"
}
```

---

## 3. Output

The Systems Integrator must produce:

- Revision proposals.
- Coordination of the agents.
- Resolution of schema and dependency conflicts.

---

## 4. Permissions

The Systems Integrator has these permissions:

- Read authorized information.
- Generate candidate observations.
- Propose claims.
- Suggest relationships.
- Generate hypotheses.
- Propose revisions.

The Systems Integrator may not:

- Modify immutable evidence.
- Delete audit records.
- Override validation.
- Grant themselves permissions.
- Directly change accepted world state.
- Execute arbitrary external actions.

---

## 5. Model Selection

The Systems Integrator should use:

- Reasoning-capable model: for coordination and proposal generation.
- Instruction-following model: for final explanation.

---

## 6. Error Handling

| Error | Handling |
|---|---|
| Extraction failure | Log, preserve original, do not fabricate |
| Model failure | Fall back to a backup model or retry |
| Schema validation failure | Reject the output and log |

---

## 7. Evaluation

The Systems Integrator is evaluated by:

- Proposal coordination.
- Cross-domain relationship discovery.
- Revison accuracy benchmarks.

---

## 8. Constraints

1. **The Systems Integrator must not directly write authoritative world-state records.**
