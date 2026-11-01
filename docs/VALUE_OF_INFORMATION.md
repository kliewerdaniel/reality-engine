# Value of Information

**Reality Engine — Value of Information Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the value of information of Reality Engine. It covers the observation priority metric.

---

## 1. Value of Information Overview

The value of information is an estimate of how much a specific additional observation would improve the world model.

---

## 2. Observation Priority

The observation priority is an initial heuristic, not a statistically validated formula:

```text
Observation Priority =
    Potential Information Value
  × Uncertainty Reduction
  × Domain Relevance
  × Time Sensitivity
  / Collection Cost
```

**Constraint:** This is an initial heuristic, not a statistically validated formula. The system should eventually measure whether acquiring the suggested information actually improves its world model.

---

## 3. Constraints

1. **The observation engine may autonomously collect from approved public sources within defined limits.**
2. **The observation engine must not bypass access controls.**
3. **The observation engine must not circumvent paywalls.**
4. **The observation engine must not violate source terms.**
