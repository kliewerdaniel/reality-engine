# Historical Reconstruction

**Reality Engine — Historical Reconstruction Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines historical reconstruction in Reality Engine. It covers how the system reconstructs the system's understanding at a specific historical point in time.

---

## 1. Definition

Historical reconstruction is the process of reconstructing the system's understanding at a specific historical point in time, using only information that was available at that time.

---

## 2. Two Distinct Queries

The system supports two distinct historical reconstruction queries:

| Query | Meaning |
|---|---|
| **Historical knowledge** | What did the system understand about the world at a particular historical date? |
| **Current understanding of the past** | What does the system currently understand about what was true at a historical date? |

These queries are distinct and must not produce interchangeable results.

---

## 3. Historical Knowledge Query

**Question:** "What did the system understand about the world on October 15, based only on information available at that time?"

**Method:**

1. Identify all information available by October 15.
2. Reconstruct the system's understanding at that time.
3. Return the system's state as it was understood at that time.

---

## 4. Current Understanding of the Past Query

**Question:** "What does the system currently understand about what was true on October 15?"

**Method:**

1. Identify the state of the world on October 15.
2. Use all current information to determine the current understanding.
3. Return the current understanding of the past.

---

## 5. Historical Reconstruction Components

| Component | Responsibility |
|---|---|
| Temporal query | Find information available at the historical knowledge time |
| State reconstruction | Reconstruct the state at that time |
| State version | Store the reconstructed state |
| Audit log | Record the reconstruction |

---

## 6. Historical Reconstruction Examples

**Example:** What did Reality Engine believe about the economy on October 15, based only on information available at that time?

```json
{
  "date": "2026-10-15",
  "knowledge_time": "2026-10-15",
  "state": {
    "entities": [
      { "id": "country_x", "name": "Country X", "status": "ACTIVE" }
    ],
    "claims": [
      { "id": "claim_000184", "status": "SUPPORTED", "statement": "Inflation is increasing" }
    ],
    "observations": [
      { "id": "obs_000018", "value": "3.2", "unit": "percent" }
    ]
  }
}
```

---

## 7. Historical Reconstruction Accuracy

Historical reconstruction accuracy is measured by the temporal benchmark:

| Metric | Target |
|---|---|
| Historical reconstruction | Accurate for deterministic recorded events |
| Time-series consistency | Past states are reconstructed correctly |
| Knowledge time | The system knows what it knew at the time |

---

## 8. Constraints

1. **Immutability:** Historical records must not be silently modified.
2. **Corrections:** Corrections are recorded as new records.
3. **Versioning:** All accepted world-state changes create new versions.
4. **Historical knowledge:** Historical knowledge must be reconstructed from information available at that time.
5. **Current knowledge:** Current understanding must not be conflated with historical knowledge.

---

## 9. Summary

- Historical reconstruction is the process of reconstructing the system's understanding at a specific historical point in time.
- The system supports two distinct historical queries.
- Historical reconstruction accuracy is measured by the temporal benchmark.
- Corrections are recorded as new records.
- Historical records are immutable.
