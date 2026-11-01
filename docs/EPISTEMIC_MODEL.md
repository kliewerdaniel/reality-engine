# Epistemic Model

**Reality Engine — Epistemic Model Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the epistemic model of Reality Engine. It covers the epistemic dimensions and the structured epistemic representation.

---

## 1. Epistemic Model Overview

The epistemic model represents uncertainty explicitly. The system must distinguish what is known, what is reported, what is inferred, and what remains unknown. No single confidence score is sufficient to represent all uncertainty.

---

## 2. Epistemic Dimensions

Each significant claim may carry these dimensions:

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

## 3. Structured Epistemic Representation

The system must introduce a structured epistemic representation.

**Example:**

```json
{
  "claim_id": "claim_000001",
  "epistemic_dimensions": {
    "source_reliability": 0.9,
    "directness": "direct",
    "corroboration": 2,
    "temporal_validity": 0.8,
    "measurement_quality": 0.95,
    "interpretation": 0.6,
    "contradiction": 0,
    "completeness": 0.7
  }
}
```

---

## 4. Constraints

1. **No single confidence score is sufficient to represent all uncertainty.**
2. **These dimensions must remain independently inspectable.**
3. **Confidence estimates must be optional.**
4. **The methodology must be explicit and domain-specific.**
