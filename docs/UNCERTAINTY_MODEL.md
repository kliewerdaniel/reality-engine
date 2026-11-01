# Uncertainty Model

**Reality Engine — Uncertainty Model Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the uncertainty model of Reality Engine. It covers the epistemic dimensions and the Bayesian analysis.

---

## 1. Uncertainty Model Overview

The uncertainty model represents uncertainty explicitly. The system must distinguish what is known, what is reported, what is inferred, and what remains unknown. No single confidence score is sufficient to represent all uncertainty.

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

## 3. Bayesian Analysis

Bayesian updating may be used for suitable probabilistic hypotheses.

**Constraint:** Bayesian updating requires defensible likelihood assumptions. The system must document:

- Prior assumptions
- Likelihood model
- Evidence dependencies
- Conditional independence assumptions
- Update calculations
- Model version

**Constraint:** Bayesian calculations must not be applied to arbitrary claims without defensible probability models.

---

## 4. Constraints

1. **No single confidence score is sufficient to represent all uncertainty.**
2. **These dimensions must remain independently inspectable.**
3. **Confidence estimates must be optional.**
4. **The methodology must be explicit and domain-specific.**
