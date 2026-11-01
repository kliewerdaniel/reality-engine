# Skeptic Specification

**Reality Engine — Skeptic Specification Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the Skeptic specification. It defines the structured input, output, permissions, error handling, model selection, and evaluation requirements.

---

## 1. Skeptic Role

The Skeptic searches for contradictions, missing evidence, alternative explanations, and unsupported assumptions.

---

## 2. Input

**Context:**

- Hypothesis or claim
- Evidence (all evidence)

**Prompt:**

- Context
- Task: find contradictions, alternative explanations, unsupported assumptions, missing information

**Expected output format:**

```json
{
  "contradictions": [
    {
      "claim_id": "claim_000001",
      "evidence": "contradictory evidence",
      "severity": "low|medium|high"
    }
  ],
  "alternative_explanations": [
    {
      "statement": "alternative explanation",
      "evidence": "evidence supporting the explanation"
    }
  ],
  "unsupported_assumptions": [
    "assumption 1",
    "assumption 2"
  ],
  "missing_information": [
    "information 1",
    "information 2"
  ],
  "timestamp": "2026-11-01T12:00:00Z"
}
```

---

## 3. Output

The Skeptic must produce:

- A list of contradictions.
- A list of alternative explanations.
- A list of unsupported assumptions.
- A list of missing information.

---

## 4. Permissions

The Skeptic has these permissions:

- Read authorized information.
- Generate candidate observations.
- Propose claims.
- Suggest relationships.
- Generate hypotheses.
- Propose revisions.

The Skeptic may not:

- Modify immutable evidence.
- Delete audit records.
- Override validation.
- Grant themselves permissions.
- Directly change accepted world state.
- Execute arbitrary external actions.

---

## 5. Model Selection

The Skeptic should use:

- Reasoning-capable model: for contradiction analysis.
- Long-context model: for historical synthesis.

---

## 6. Error Handling

| Error | Handling |
|---|---|
| Extraction failure | Log, preserve original, do not fabricate |
| Model failure | Fall back to a backup model or retry |
| Schema validation failure | Reject the output and log |

---

## 7. Evaluation

The Skeptic is evaluated by:

- Contradiction detection accuracy.
- False-positive rate.

---

## 8. Constraints

1. **The Skeptic agreement with another model does not constitute verification.**
2. **The Skeptic should be independently prompted and evaluated.**
