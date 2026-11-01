# Evaluation Framework

**Reality Engine — Evaluation Framework Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the evaluation framework of Reality Engine. It covers the core benchmark categories, the evaluation philosophy, and the evaluation procedures.

---

## 1. Evaluation Philosophy

Reality Engine must be evaluated on the correctness of its knowledge operations, not the fluency of its generated explanations. A convincing answer is not necessarily a correct answer.

---

## 2. Core Benchmark Categories

| Benchmark | Measurement |
|---|---|
| Extraction Accuracy | Claim extraction precision, recall, entity extraction accuracy, event extraction accuracy, temporal extraction accuracy |
| Provenance Accuracy | Percentage of claims traceable to correct original source passages |
| Temporal Integrity | Delayed reporting, corrected publication dates, retroactive policy changes |
| Revision Accuracy | Correctly affected claims, incorrectly affected claims, missed dependencies, invalid revision acceptance, unnecessary revision frequency |
| Source Independence | Syndicated articles, repeated press releases, independent measurements, shared research sources, quoted secondary sources |
| Contradiction Detection | Genuine contradictions, apparent contradictions caused by different time periods, different units, different definitions, different geographic scopes, incomplete reporting |
| Forecast Calibration | Accuracy against proper scoring rules and baseline models |

---

## 3. Evaluation Procedures

| Benchmark | Procedure |
|---|---|
| Extraction Accuracy | Measure claim extraction precision, recall, entity extraction accuracy, event extraction accuracy, temporal extraction accuracy |
| Provenance Accuracy | Measure the percentage of claims that can be traced to correct original source passages |
| Temporal Integrity | Test delayed reporting, corrected publication dates, retroactive policy changes |
| Revision Accuracy | Measure correctly affected claims, incorrectly affected claims, missed dependencies, invalid revision acceptance, unnecessary revision frequency |
| Source Independence | Test syndicated articles, repeated press releases, independent measurements, shared research sources, quoted secondary sources |
| Contradiction Detection | Test genuine contradictions, apparent contradictions, delayed reporting, corrected publications, retracted publications |
| Forecast Calibration | Measure forecast accuracy against proper scoring rules and baseline models |

---

## 4. Constraints

1. **Reality Engine must be evaluated on the correctness of its knowledge operations, not the fluency of its generated explanations.**
2. **A convincing answer is not necessarily a correct answer.**
