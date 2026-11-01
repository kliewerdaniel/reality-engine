# Database Schema

**Reality Engine — Database Schema Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the database schema of Reality Engine. It defines the tables, foreign keys, indexes, constraints, migrations, and example queries.

---

## 1. Initial Technology

| Component | Technology |
|---|---|
| Primary storage | SQLite |
| Database mode | WAL (Write-Ahead Logging) |
| Foreign-key enforcement | Enabled |
| Full-text search | FTS5 |
| Data validation | Pydantic |
| API | FastAPI |
| Background processing | Python task workers |
| Testing | pytest |

---

## 2. Core Tables

### 2.1 sources

Source identities and characteristics.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Unique source identifier |
| name | TEXT NOT NULL | Source name |
| source_type | TEXT NOT NULL | Type of source |
| canonical_domain | TEXT | Canonical domain classification |
| authority_metadata | TEXT | Authority metadata |
| collection_policy | TEXT | Collection policy rules |
| created_at | TEXT NOT NULL | When the source was registered |
| updated_at | TEXT | When the record was last updated |

### 2.2 documents

Original collected material.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Document identifier |
| source_id | TEXT NOT NULL | Foreign key to sources |
| source_native_id | TEXT | Source-native identifier |
| canonical_url | TEXT | Canonical URL |
| content_hash | TEXT | Cryptographic hash |
| content_type | TEXT | Document type |
| language | TEXT | Original language |
| published_at | TEXT | Publication timestamp |
| collected_at | TEXT | Collection timestamp |
| content_reference | TEXT | Reference to original content |
| processing_status | TEXT | Processing state |
| updated_at | TEXT | Last update timestamp |

### 2.3 observations

Extracted or measured observations.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Observation identifier |
| observation_type | TEXT | Type of observation |
| subject_id | TEXT | Foreign key to entities |
| observed_value | TEXT | The observed value |
| unit | TEXT | Measurement unit |
| valid_from | TEXT | Valid time start |
| valid_to | TEXT | Valid time end |
| recorded_at | TEXT | When the system recorded it |
| source_id | TEXT | Foreign key to sources |
| document_id | TEXT | Foreign key to documents |
| provenance_reference | TEXT | Provenance reference |
| extraction_version | TEXT | Extraction version |
| created_at | TEXT | Creation timestamp |
| updated_at | TEXT | Update timestamp |

### 2.4 claims

Normalized assertions.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Claim identifier |
| subject_id | TEXT | Foreign key to entities |
| predicate | TEXT | Predicate |
| object_value | TEXT | The claim's object |
| claim_type | TEXT | Claim type |
| domain_id | TEXT | Foreign key to domain |
| valid_from | TEXT | Valid time start |
| valid_to | TEXT | Valid time end |
| recorded_at | TEXT | When the system recorded it |
| status | TEXT | Evidence status |
| revision_number | INTEGER | Revision counter |
| created_at | TEXT | Creation timestamp |
| updated_at | TEXT | Update timestamp |

### 2.5 evidence_links

Support and contradiction relationships.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Link identifier |
| claim_id | TEXT | Foreign key to claims |
| observation_id | TEXT | Foreign key to observations |
| relationship_type | TEXT | Relationship type |
| explanation | TEXT | Explanation of the inference |
| assessment_status | TEXT | Assessment status |
| created_at | TEXT | Creation timestamp |

### 2.6 entities

Countries, organizations, people, systems.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Entity identifier |
| canonical_name | TEXT | Canonical name |
| entity_type | TEXT | Type of entity |
| domain_id | TEXT | Foreign key to domain |
| created_at | TEXT | Creation timestamp |
| updated_at | TEXT | Update timestamp |
| status | TEXT | Entity status |

### 2.7 entity_aliases

Alternate names for entities.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Alias identifier |
| entity_id | TEXT | Foreign key to entities |
| alias | TEXT | The alias |
| language | TEXT | Language |
| source_id | TEXT | Foreign key to sources |
| valid_from | TEXT | Valid time start |
| valid_to | TEXT | Valid time end |
| created_at | TEXT | Creation timestamp |

### 2.8 events

Occurrences in the world.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Event identifier |
| event_type | TEXT | Type of event |
| description | TEXT | Event description |
| location_id | TEXT | Foreign key to entities |
| valid_from | TEXT | Valid time start |
| valid_to | TEXT | Valid time end |
| recorded_at | TEXT | When the system recorded it |
| status | TEXT | Event status |
| created_at | TEXT | Creation timestamp |
| updated_at | TEXT | Update timestamp |

### 2.9 relationships

Connections between entities.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Relationship identifier |
| source_entity_id | TEXT | Foreign key to source entity |
| target_entity_id | TEXT | Foreign key to target entity |
| relationship_type | TEXT | Type of relationship |
| valid_from | TEXT | Valid time start |
| valid_to | TEXT | Valid time end |
| recorded_at | TEXT | When the system recorded it |
| evidence_status | TEXT | Evidence status |
| created_at | TEXT | Creation timestamp |
| updated_at | TEXT | Update timestamp |

### 2.10 hypotheses

Explanatory models.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Hypothesis identifier |
| statement | TEXT | Hypothesis statement |
| domain_id | TEXT | Foreign key to domain |
| status | TEXT | Hypothesis status |
| prior_assumptions | TEXT | Prior assumptions |
| methodology | TEXT | Methodology |
| created_at | TEXT | Creation timestamp |
| revised_at | TEXT | Last revision timestamp |

### 2.11 forecasts

Predictions and evaluation conditions.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Forecast identifier |
| hypothesis_id | TEXT | Foreign key to hypotheses |
| predicted_outcome | TEXT | Predicted outcome |
| probability | REAL | Predicted probability |
| evaluation_horizon | TEXT | Evaluation horizon |
| resolution_criteria | TEXT | Resolution criteria |
| created_at | TEXT | Creation timestamp |
| evaluated_at | TEXT | When evaluated |
| observed_outcome | TEXT | Actual outcome |
| score | REAL | Scoring result |
| status | TEXT | Forecast status |

### 2.12 world_states

Versioned state snapshots.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | State identifier |
| domain_id | TEXT | Foreign key to domain |
| version | INTEGER | State version |
| parent_version | TEXT | Parent state version |
| state_hash | TEXT | Hash of the state |
| created_at | TEXT | Creation timestamp |

### 2.13 revision_events

Every proposed and accepted revision.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Revision event identifier |
| trigger_observation_id | TEXT | Triggering observation |
| previous_state_id | TEXT | Previous state |
| resulting_state_id | TEXT | Resulting state |
| revision_type | TEXT | Outcome type |
| proposal_reference | TEXT | Proposal reference |
| validation_result | TEXT | Validation result |
| created_at | TEXT | Creation timestamp |

### 2.14 dependencies

Relationships between conclusions.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Dependency identifier |
| dependent_type | TEXT | Dependent type |
| dependent_id | TEXT | Dependent identifier |
| prerequisite_type | TEXT | Prerequisite type |
| prerequisite_id | TEXT | Prerequisite identifier |
| dependency_type | TEXT | Type of dependency |
| created_at | TEXT | Creation timestamp |

### 2.15 source_lineage

Shared origins and information propagation.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Lineage identifier |
| source_id_a | TEXT | First source |
| source_id_b | TEXT | Second source |
| relationship_type | TEXT | Relationship type |
| confidence | REAL | Confidence |
| created_at | TEXT | Creation timestamp |

### 2.16 audit_events

Audit trail of significant operations.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Audit event identifier |
| event_type | TEXT | Event type |
| actor_type | TEXT | Actor type |
| actor_id | TEXT | Actor identifier |
| object_type | TEXT | Object type |
| object_id | TEXT | Object identifier |
| previous_hash | TEXT | Hash of state before change |
| event_hash | TEXT | Hash of the event |
| payload_reference | TEXT | Reference to payload |
| created_at | TEXT | When recorded |
| CONSTRAINT fk_previous_state FOREIGN KEY (previous_hash) REFERENCES audit_events(event_hash) | | |

---

## 3. Indexes

Indexes must be maintained on:

- sources.name
- documents.source_id
- documents.canonical_url
- documents.content_hash
- observations.source_id
- observations.document_id
- observations.subject_id
- claims.subject_id
- claims.predicate
- entities.canonical_name
- entities.entity_type
- events.event_type
- relationships.source_entity_id
- relationships.target_entity_id
- hypotheses.statement
- forecasts.status
- world_states.domain_id

---

## 4. Foreign Keys

Foreign keys must be enforced:

- documents.source_id → sources.id
- observations.source_id → sources.id
- observations.document_id → documents.id
- observations.subject_id → entities.id
- claims.subject_id → entities.id
- claims.domain_id → domains.id
- entities.domain_id → domains.id
- entity_aliases.entity_id → entities.id
- entity_aliases.source_id → sources.id
- events.location_id → entities.id
- relationships.source_entity_id → entities.id
- relationships.target_entity_id → entities.id
- hypotheses.domain_id → domains.id
- forecasts.hypothesis_id → hypotheses.id
- dependencies.dependent_id → ...
- dependencies.prerequisite_id → ...

---

## 5. Constraints

| Constraint | Description |
|---|---|
| NOT_NULL | Fields must not be null |
| UNIQUE | Fields must be unique |
| FOREIGN_KEY | Fields must reference an existing object |
| CHECK | Fields must satisfy a condition |
| ENUM | Fields must be one of a set of values |

---

## 6. Example Queries

### 6.1 Find all claims for a document

```sql
SELECT c.* FROM claims c
JOIN documents d ON d.id = c.document_id
WHERE d.id = 'doc_000001';
```

### 6.2 Find all observations for an entity

```sql
SELECT o.* FROM observations o
WHERE o.subject_id = 'entity_000001';
```

### 6.3 Find all revisions for an entity

```sql
SELECT r.* FROM world_states w
JOIN revision_events r ON r.resulting_state_id = w.id
WHERE w.domain_id = 'geopolitical';
```

### 6.4 Find all evidence for a claim

```sql
SELECT e.* FROM evidence_links e
WHERE e.claim_id = 'claim_000001';
```

---

## 7. Database Integrity

| Control | Description |
|---|---|
| Foreign-key constraints | Enforce referential integrity |
| Unique identity constraints | Prevent duplicate identifiers |
| Transactional revision commits | Ensure atomicity |
| Immutable evidence records | Prevent silent modification of evidence |
| Explicit correction records | Record corrections as new events |
| Schema migrations | Apply changes in a controlled manner |
| Consistent timestamps | All timestamps in UTC |
| Idempotency keys | Prevent duplicate processing |
| Database backup and recovery | Support recovery |

---

## 8. Constraints

1. **Foreign-key constraints must be enforced.**
2. **Unique identity constraints must be enforced.**
3. **Transactional revision commits must be enforced.**
4. **Immutable evidence records must be enforced.**
5. **Explicit correction records must be enforced.**
6. **Schema migrations must be enforced.**
7. **Consistent timestamps must be enforced.**
8. **Idempotency keys must be enforced.**
9. **Database backup and recovery must be enforced.**
