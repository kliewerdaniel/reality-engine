# Bitemporal Data

**Reality Engine — Bitemporal Data Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines bitemporal data in Reality Engine. It covers the four temporal fields, interval semantics, and correction handling.

---

## 1. Bitemporal Principles

Bitemporal data distinguishes two temporal dimensions:

| Dimension | Field | Meaning |
|---|---|---|
| World time | valid_from | When the information applies to the external world |
| World time | valid_to | When the information ceased to apply |
| Knowledge time | recorded_at | When the system recorded the information |
| Knowledge time | superseded_at | When the system replaced the information |

---

## 2. Bitemporal Fields

| Field | Type | Required | Description |
|---|---|---|---|
| valid_from | timestamp | Yes | When the information applies to the external world |
| valid_to | timestamp or null | No | When the information ceased to apply |
| recorded_at | timestamp | Yes | When the system recorded it |
| superseded_at | timestamp or null | No | When the system replaced the information |

---

## 3. Interval Semantics

Intervals are enforced at the database level using proper timestamp types.

**Rules:**

1. `valid_from` must be less than or equal to `valid_to` (if `valid_to` is set).
2. `recorded_at` must be greater than or equal to `valid_from`.
3. All timestamps are in UTC.
4. Unknown or approximate dates are represented explicitly, not invented.

---

## 4. Correction Handling

**Rule:** Corrections are recorded as new records, not by modifying old records.

**Example:**

| Item | Original | Corrected |
|---|---|---|
| valid_from | 2026-10-10 | 2026-10-11 |
| valid_to | null | null |
| recorded_at | 2026-10-13 | 2026-10-20 |

The corrected record is linked to the original record.

---

## 5. Temporal Queries

### 5.1 Reconstructing Historical Knowledge

Query: "What did the system understand about the world at a particular historical knowledge time?"

- Returns the system's understanding at that knowledge time.
- Uses only information available at that time.

### 5.2 Current Understanding of the Past

Query: "What does the system currently understand about what was true at a historical date?"

- Returns the system's current interpretation of what was true at the historical date.
- Uses all available current information.

**These queries must not produce interchangeable results.**

---

## 6. Event Log

The event log is append-only:

1. Events are recorded as they occur.
2. Events are never deleted.
3. Corrections require new events.
4. A previous event must not be silently rewritten.

---

## 7. Summary

- Bitemporal data distinguishes world time from knowledge time.
- The four fields are valid_from, valid_to, recorded_at, superseded_at.
- Corrections are recorded as new records.
- Temporal consistency is enforced at the database level.
- Historical queries are distinct from current understanding queries.
