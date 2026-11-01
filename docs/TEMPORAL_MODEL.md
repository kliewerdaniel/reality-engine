# Temporal Model

**Reality Engine — Temporal Model Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the temporal model of Reality Engine. It defines temporal validity, transaction time, corrections, historical queries, and reconstruction behavior.

---

## 1. Temporal Foundations

The temporal model is built on the premise that the system must distinguish:

1. When something happened (world time).
2. When the system learned about it (knowledge time).

These are the two dimensions of bitemporal data.

---

## 2. Bitemporal Data Model

Every time-sensitive object has:

| Field | Meaning |
|---|---|
| valid_from | When the information applies to the external world |
| valid_to | When the information ceased to apply |
| recorded_at | When the system recorded the information |
| superseded_at | When the system replaced the information |

**Constraints:**

- All timestamps are in UTC.
- Unknown or approximate dates are represented explicitly, not invented.
- `valid_from` must be less than or equal to `valid_to` (if `valid_to` is set).
- `recorded_at` must be greater than or equal to `valid_from`.

---

## 3. Temporal Queries

### 3.1 Reconstructing Historical Knowledge

Query: "What did the system understand about the world at a particular historical date?"

- Uses only information available at that date.
- Returns the system's understanding at that knowledge time.
- Historical state snapshots are reconstructed from recorded events.

### 3.2 Current Understanding of the Past

Query: "What does the system currently understand about what was true at a historical date?"

- Uses all current information.
- Returns the system's current interpretation of what was true at the historical date.
- Current state snapshots are used.

**These queries must not produce interchangeable results.**

---

## 4. Correction Handling

A correction is a new record, not a modification of the original record.

**Example:**

| Item | Original | Corrected |
|---|---|---|
| valid_from | 2026-10-10 | 2026-10-11 |
| valid_to | null | null |
| recorded_at | 2026-10-13 | 2026-10-20 |

**Correction rules:**

1. Corrections are recorded as new records.
2. The original record is preserved.
3. The correction is linked to the original record.
4. The correction includes an explanation.

---

## 5. Temporal Consistency

Temporal consistency is enforced at three levels:

| Level | Enforcement |
|---|---|
| Database | Proper timestamp types, interval semantics |
| Application | Validation rules |
| Governance | Validated revisions |

---

## 6. Timestamp Format

All timestamps are in ISO 8601 UTC format:

```
2026-10-15T00:00:00Z
```

---

## 7. Historical Reconstruction

Historical reconstruction is the process of reconstructing the system's understanding at a specific historical point.

### 7.1 Historical Reconstruction Query

The system answers two distinct queries:

| Query | Meaning |
|---|---|
| What did the system understand about the world at a particular historical date? | Uses only information available at that date. |
| What does the system currently understand about what was true at that historical date? | Uses all current information. |

### 7.2 Reconstruction Accuracy

Historical reconstruction accuracy is measured by the temporal benchmark:

| Metric | Target |
|---|---|
| Historical reconstruction | Accurate for deterministic recorded events |
| Time-series consistency | Past states are reconstructed correctly |

---

## 8. Event Processing

Events are processed in order:

1. The event is received.
2. The event is validated.
3. The event is recorded.
4. The state is updated.
5. The event is recorded in the audit ledger.

---

## 9. Temporal Constraints

1. **Immutability:** Historical records must not be silently modified.
2. **Corrections:** Corrections are recorded as new records.
3. **Versioning:** All accepted world-state changes create new versions.
4. **Query:** Historical queries must not silently incorporate future observations.
5. **Consistency:** All timestamps are in UTC.

---

## 10. Summary

- The system uses bitemporal data (valid time + transaction time).
- Historical reconstruction queries are distinct from current understanding queries.
- Corrections are recorded as new records.
- Temporal consistency is enforced at database, application, and governance levels.
- All timestamps are in UTC.

---

## 11. References

- ONTOLOGY.md — common ontology definitions
- ENTITY_MODEL.md — entity definitions
- EVENT_MODEL.md — event definitions
- CLAIM_MODEL.md — claim definitions
- OBSERVATION_MODEL.md — observation definitions
- REVISION_MODEL.md — revision definitions
- HISTORICAL_RECONSTRUCTION.md — historical reconstruction
