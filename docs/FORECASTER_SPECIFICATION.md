# Forecaster Specification

**Reality Engine — Forecaster Specification Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the Forecaster specification. It defines the structured input, output, permissions, error handling, model selection, and evaluation requirements.

---

## 1. Forecaster Role

The Forecaster generates testable predictions and records the conditions under which they should be evaluated.

---

## 2. Input

**Context:**

- Hypothesis
- Context

**Prompt:**

- Context
- Task: generate testable predictions based on the hypothesis

**Expected output format:**

```json
{
  "predictions": [
    {
      "predicted_outcome": "predicted outcome",
      "probability": 0.7,
      "time_horizon": "2026-12-31",
      "outcome_conditions": "conditions under which the prediction resolves"
    }
  ],
  "model_config": "model configuration",
  "timestamp": "2026-11-01T12:00:00Z"
}
```

---

## 3. Output

The Forecaster must produce:

- Testable predictions.
- Probabilities.
- Outcome conditions.
- Evaluation horizons.

**Important:** Every forecast must be immutable after publication except through an explicit correction record.

---

## 4. Permissions

The Forecaster has these permissions:

- Read authorized information.
- Generate candidate observations.
- Propose claims.
- Suggest relationships.
- Generate hypotheses.
- Propose revisions.

The Forecaster may not:

- Modify immutable evidence.
- Delete audit records.
- Override validation.
- Grant themselves permissions.
- Directly change accepted world state.
- Execute arbitrary external actions.

---

## 5. Model Selection

The Forecaster should use:

- Reasoning-capable model: for prediction generation.
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

The Forecaster is evaluated by:

- Forecast calibration.
- Forecast evaluation.

---

## 8. Constraints

1. **Every forecast must be immutable after publication except through an explicit correction record.**
2. **Forecasts must not be silently rewritten.**
3. **Corrections require separate records.**
