# Audit Model

**Reality Engine — Audit Model Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the audit model of Reality Engine. It covers the audit events and the audit history.

---

## 1. Audit Model Overview

The audit model defines how the system records and preserves audit events.

---

## 2. Audit Events

| Event | Description |
|---|---|
| SOURCE_REGISTERED | A source has been registered |
| DOCUMENT_COLLECTED | A document has been collected |
| DOCUMENT_UPDATED | A document has been updated |
| OBSERVATION_EXTRACTED | An observation has been extracted |
| CLAIM_CREATED | A claim has been created |
| CLAIM_SUPPORTED | A claim has been supported |
| CLAIM_CHALLENGED | A claim has been challenged |
| ENTITY_CREATED | An entity has been created |
| ENTITY_RESOLVED | An entity has been resolved |
| RELATIONSHIP_CREATED | A relationship has been created |
| HYPOTHESIS_CREATED | A hypothesis has been created |
| REVISION_PROPOSED | A revision proposal has been generated |
| REVISION_VALIDATED | A revision proposal has been validated |
| REVISION_REJECTED | A revision proposal has been rejected |
| WORLD_STATE_UPDATED | The world state has been updated |
| FORECAST_CREATED | A forecast has been created |
| FORECAST_EVALUATED | A forecast has been evaluated |
| SCHEMA_MIGRATED | The database schema has been migrated |

---

## 3. Audit Event Fields

| Field | Description |
|---|---|
| id | Unique event identifier |
| event_type | The event type |
| actor_type | The actor type |
| actor_id | The actor identifier |
| object_type | The object type |
| object_id | The object identifier |
| previous_hash | The hash of the state before the change |
| event_hash | The hash of the event |
| payload_reference | The payload reference |
| created_at | When the event was recorded |

---

## 4. Constraints

1. **Events must be append-only.**
2. **Corrections require new events.**
3. **A previous event must not be silently rewritten.**
