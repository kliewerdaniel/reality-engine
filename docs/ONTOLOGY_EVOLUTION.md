# Ontology Evolution

**Reality Engine — Ontology Evolution Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines how the shared ontology can evolve without invalidating existing records.

---

## 1. Ontological Primitives

The common ontology defines the following primitives:

| Primitive | Type | Description |
|---|---|---|
| Entity | Object | An identifiable object in the world |
| Event | Object | An occurrence in the world |
| Observation | Object | A directly measured or recorded observation |
| Claim | Object | An assertion about the world |
| Evidence | Relationship | Information supporting or challenging a claim |
| Relationship | Object | A connection between entities, events, claims, or hypotheses |
| Condition | Object | A state or observable condition |
| Hypothesis | Object | An explanatory model |
| Forecast | Object | A formal prediction |
| Conclusion | Object | An assessment derived from evidence |
| Domain | Object | A logical division of the world model |
| Revision | Object | A controlled change to the world model |
| Audit Event | Object | A record of a significant operation |
| World-State Snapshot | Object | A versioned snapshot of the world state |

---

## 2. Evolution Requirements

The ontology must be able to:

1. Introduce new object types without invalidating existing records.
2. Introduce new relationship types without invalidating existing records.
3. Deprecate relationship types without destroying historical data.
4. Change field definitions without invalidating existing records.
5. Add new constraints without breaking historical data.

---

## 3. Versioned Ontology Schemas

**Ontology version:** 0.1.0

Each version of the ontology is recorded:

| Field | Description |
|---|---|
| version | The ontology version |
| schema_hash | Hash of the schema |
| created_at | When the version was created |
| description | Description of the changes |

---

## 4. Migration Events

When the ontology changes, a migration event is recorded:

| Field | Description |
|---|---|
| migration_id | Unique identifier |
| from_version | The previous ontology version |
| to_version | The new ontology version |
| type | The type of migration |
| affected_objects | Objects affected by the migration |
| executed_at | When the migration was executed |
| status | Status of the migration |

**Migration types:**

| Type | Description |
|---|---|
| ADD_OBJECT_TYPE | Add a new object type |
| ADD_RELATIONSHIP_TYPE | Add a new relationship type |
| DEPRECATE_OBJECT_TYPE | Deprecate an object type |
| DEPRECATE_RELATIONSHIP_TYPE | Deprecate a relationship type |
| CHANGE_FIELD_DEFINITION | Change a field definition |
| ADD_CONSTRAINT | Add a new constraint |
| REMOVE_CONSTRAINT | Remove a constraint |

---

## 5. Evolution Rules

### 5.1 Adding Object Types

Adding a new object type does not invalidate existing records.

**Example:**

- Add a new object type `LINK` to represent connections between entities.
- Existing records are unaffected.

### 5.2 Adding Relationship Types

Adding a new relationship type does not invalidate existing records.

**Example:**

- Add `COORDINATED_WITH` to represent coordination between entities.
- Existing relationships are unaffected.

### 5.3 Deprecating Relationship Types

Deprecating a relationship type does not destroy historical data. Deprecated relationships are marked as deprecated.

**Example:**

- Deprecate `RELATED_TO` after a more specific type is introduced.
- Existing relationships are marked as `DEPRECATED`.
- Historical data is preserved.

### 5.4 Changing Field Definitions

Changing a field definition must not invalidate existing records. Historical records retain their values.

**Example:**

- Change the `unit` field from `TEXT` to `TEXT` with a new constraint.
- Existing records retain their values.
- New records must satisfy the new constraint.

### 5.5 Adding Constraints

Adding a constraint may require migration. Historical records that violate the constraint are marked with a `CONSTRAINT_VIOLATION` status.

**Example:**

- Add a constraint that `probability` must be between 0.0 and 1.0.
- Historical records with `probability` > 1.0 are marked as `CONSTRAINT_VIOLATION`.
- New records must satisfy the constraint.

### 5.6 Removing Constraints

Removing a constraint does not invalidate historical records. The constraint removal is recorded as a migration event.

---

## 6. Ontology Versioning

The ontology version is stored in the `ontology_versions` table:

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Version identifier |
| schema_hash | TEXT NOT NULL | Hash of the schema |
| created_at | TEXT NOT NULL | Creation timestamp |
| description | TEXT | Description of changes |

The current ontology version is the most recent row in `ontology_versions`.

---

## 7. Backward Compatibility

The ontology must maintain backward compatibility:

1. **Records:** Existing records must remain readable across versions.
2. **Queries:** Queries written for one version must be accurate for later versions.
3. **Interfaces:** The API must remain stable across versions.

---

## 8. Forward Compatibility

The ontology must be forward-compatible:

1. **New types:** New types must be recognizable by consumers that only know older versions.
2. **New fields:** New fields must be optional.
3. **Conflicts:** Conflicting fields must be explicitly marked as `UNKNOWN`.

---

## 9. Constraints

1. **Immutability:** Historical records must remain immutable.
2. **Versioning:** All ontology changes are recorded as versioned migrations.
3. **Backward compatibility:** Existing records must remain readable.
4. **Forward compatibility:** New types and fields must be optional.
5. **Provenance:** Ontology changes do not affect the provenance of existing records.

---

## 10. Summary

The ontology evolves through versioned migrations. Each change is recorded as a migration event. Existing records are preserved. The system maintains backward and forward compatibility.

---

## 11. References

- ONTOLOGY.md — common ontology definitions
- OBJECT_MODEL.md — object model
- TEMPORAL_MODEL.md — bitemporal semantics
- REVISION_MODEL.md — revision definitions
- REVISION_STATE_MACHINE.md — how revisions interact with the ontology
