# Time Semantics

**Reality Engine — Time Semantics Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the time semantics of Reality Engine. It covers how time is represented, how different kinds of time are distinguished, and how time is used in queries.

---

## 1. Kinds of Time

The system distinguishes at least two kinds of time:

| Kind | Field | Meaning |
|---|---|---|
| World time | valid_from | When something happened in the external world |
| World time | valid_to | When something ceased to apply |
| Knowledge time | recorded_at | When the system learned about it |
| Knowledge time | superseded_at | When the system replaced it |

---

## 2. Examples

### 2.1 Economic Policy Change

| Item | World time | Knowledge time |
|---|---|---|
| Policy change | October 10 | — |
| Report published | — | October 12 |
| System records | — | October 13 |
| Correction | October 11 (actually) | October 20 |

### 2.2 News Report

| Item | World time | Knowledge time |
|---|---|---|
| Event | October 15 | — |
| News report | — | October 16 |
| System records | — | October 16 |
| Correction | October 15 | October 17 |

---

## 3. Query Semantics

### 3.1 Historical Knowledge

**Question:** "What did the system understand about the world on October 15, based only on information available at that time?"

**Answer:** The system's state as of October 15, using only information available by that time.

### 3.2 Current Understanding of the Past

**Question:** "What does the system currently understand about what was true on October 15?"

**Answer:** The system's current state, using all available current information.

---

## 4. Timestamp Format

All timestamps are in ISO 8601 UTC format:

```
2026-10-15T00:00:00Z
```

---

## 5. Temporal Constraints

1. **Immutability:** Historical records must not be silently modified.
2. **Corrections:** Corrections are recorded as new records.
3. **Versioning:** All accepted world-state changes create new versions.
4. **Query:** Historical queries must not silently incorporate future observations.
5. **Consistency:** All timestamps are in UTC.

---

## 6. Summary

- The system distinguishes world time from knowledge time.
- Historical knowledge queries use only information available at the historical knowledge time.
- Current understanding of the past queries use all available current information.
- All timestamps are in UTC.
- Historical records are immutable.
