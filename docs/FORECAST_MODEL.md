# Forecast Model

**Reality Engine — Forecast Model Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the forecast model of Reality Engine. It defines all forecasts, their fields, constraints, evaluation, and calibration.

---

## 1. Forecast Definition

A forecast is a formal prediction with an explicitly defined hypothesis, predicted outcome, probability, time horizon, and resolution criteria. Forecasts are a secondary capability built on top of the world model.

---

## 2. Forecast Fields

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | Yes | Forecast identifier |
| hypothesis_id | string | Yes | Foreign key to Hypothesis |
| predicted_outcome | string | Yes | Predicted outcome |
| probability | float | Yes | Predicted probability (0.0 to 1.0) |
| evaluation_horizon | string | Yes | Evaluation horizon |
| resolution_criteria | string | Yes | Resolution criteria |
| created_at | timestamp | Yes | Creation timestamp |
| evaluated_at | timestamp or null | No | When evaluated |
| observed_outcome | string | No | Actual outcome |
| score | float | No | Scoring result |
| status | string | Yes | Forecast status |

**Constraints:**

- `probability` must be between 0.0 and 1.0.
- `hypothesis_id` must reference an existing Hypothesis.

---

## 3. Forecast Status

| Status | Meaning |
|---|---|
| OPEN | The forecast is open |
| EVALUATED | The forecast has been evaluated |
| RESOLVED | The forecast has been resolved |
| WITHDRAWN | The forecast has been withdrawn |

---

## 4. Forecast Types

### 4.1 Binary Forecast

A binary forecast predicts one of two outcomes:

| Outcome | Probability |
|---|---|
| Y | 0.7 |
| N | 0.3 |

**Brier score:**

$$BS = \frac{1}{N}\sum_{i=1}^{N}(p_i - o_i)^2$$

Where:

- $p_i$ is the predicted probability.
- $o_i$ is the observed outcome, either 0 or 1.

### 4.2 Continuous Forecast

A continuous forecast predicts a value in a range. For continuous forecasts, use appropriate proper scoring rules.

---

## 5. Forecast Evaluation

Forecasts are evaluated against actual outcomes:

| Step | Action |
|---|---|
| 1 | The forecast is created with a hypothesis |
| 2 | The forecast is recorded in the `forecasts` table |
| 3 | The forecast's evaluation horizon is set |
| 4 | The horizon expires |
| 5 | The observed outcome is recorded |
| 6 | The forecast is scored |
| 7 | The forecast status is updated to EVALUATED or RESOLVED |

---

## 6. Forecast Examples

**Binary Forecast:**

```json
{
  "id": "forecast_000001",
  "hypothesis_id": "hypothesis_000001",
  "predicted_outcome": "Global oil prices exceed $100/barrel",
  "probability": 0.35,
  "evaluation_horizon": "2026-12-31",
  "resolution_criteria": "Oil price > $100/barrel",
  "created_at": "2026-10-15T00:00:00Z",
  "evaluated_at": null,
  "observed_outcome": null,
  "score": null,
  "status": "OPEN"
}
```

**Evaluated Forecast:**

```json
{
  "id": "forecast_000001",
  "hypothesis_id": "hypothesis_000001",
  "predicted_outcome": "Global oil prices exceed $100/barrel",
  "probability": 0.35,
  "evaluation_horizon": "2026-12-31",
  "resolution_criteria": "Oil price > $100/barrel",
  "created_at": "2026-10-15T00:00:00Z",
  "evaluated_at": "2026-12-31T00:00:00Z",
  "observed_outcome": "Oil price at $95/barrel",
  "score": 0.42,
  "status": "RESOLVED"
}
```

---

## 7. Forecast Calibration

Forecast calibration measures whether predictions assigned a particular probability occur at approximately that frequency over a large sample.

**Example:**

A model repeatedly predicting 80% probability should not be considered calibrated if such events occur only 40% of the time.

**Calibration metric:**

| Probability Bin | Predicted | Observed | Calibration |
|---|---|---|---|
| 0.0–0.2 | 100 events | 20 events | Well calibrated |
| 0.2–0.4 | 80 events | 30 events | Poor calibration |
| 0.4–0.6 | 50 events | 25 events | Well calibrated |
| 0.6–0.8 | 30 events | 10 events | Poor calibration |
| 0.8–1.0 | 20 events | 15 events | Poor calibration |

---

## 8. Constraints

1. **Probability:** Forecast probability must be between 0.0 and 1.0.
2. **Hypothesis:** A forecast must reference an existing Hypothesis.
3. **Evaluation:** A forecast cannot be evaluated before its evaluation horizon.
4. **Resolution:** A forecast must have resolution criteria.
5. **Immutability:** A published forecast cannot be changed. Corrections require separate records.

---

## 8. References

- ONTOLOGY.md — common ontology definitions
- HYPOTHESIS_MODEL.md — hypothesis definitions
- TEMPORAL_MODEL.md — bitemporal semantics
- REVISION_MODEL.md — revision definitions
- REVISION_STATE_MACHINE.md — how forecasts are revised
