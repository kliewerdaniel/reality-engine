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

### 2.1 domains

Domain divisions of the world model. Domains share a common ontology and do not replace it.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Domain identifier |
| name | TEXT NOT NULL | Domain name |
| canonical_name | TEXT | Canonical domain name |
| description | TEXT | Domain description |
| parent_domain_id | TEXT | Parent domain for hierarchical domains |
| created_at | TEXT NOT NULL | Creation timestamp |

### 2.2 sources

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

### 2.3 documents

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

### 2.4 observations

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

### 2.5 claims

Normalized assertions. Every claim is traceable to a source document via `document_id`.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Claim identifier |
| subject_id | TEXT | Foreign key to entities |
| predicate | TEXT | Predicate |
| object_value | TEXT | The claim's object |
| claim_type | TEXT | Claim type |
| domain_id | TEXT | Foreign key to domains |
| document_id | TEXT | Foreign key to documents |
| valid_from | TEXT | Valid time start |
| valid_to | TEXT | Valid time end |
| recorded_at | TEXT | When the system recorded it |
| status | TEXT | Evidence status |
| revision_number | INTEGER | Revision counter |
| created_at | TEXT | Creation timestamp |
| updated_at | TEXT | Update timestamp |

### 2.6 evidence_links

Support and contradiction relationships. Every evidence link is traceable to a source span via `source_span_id`.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Link identifier |
| claim_id | TEXT | Foreign key to claims |
| observation_id | TEXT | Foreign key to observations |
| source_span_id | TEXT | Foreign key to source_spans |
| relationship_type | TEXT | Relationship type |
| explanation | TEXT | Explanation of the inference |
| assessment_status | TEXT | Assessment status |
| created_at | TEXT | Creation timestamp |

### 2.7 entities

Countries, organizations, people, systems.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Entity identifier |
| canonical_name | TEXT | Canonical name |
| entity_type | TEXT | Type of entity |
| domain_id | TEXT | Foreign key to domains |
| created_at | TEXT | Creation timestamp |
| updated_at | TEXT | Update timestamp |
| status | TEXT | Entity status |

### 2.8 entity_aliases

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

### 2.9 events

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

### 2.10 relationships

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

### 2.11 hypotheses

Explanatory models.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Hypothesis identifier |
| statement | TEXT | Hypothesis statement |
| domain_id | TEXT | Foreign key to domains |
| status | TEXT | Hypothesis status |
| prior_assumptions | TEXT | Prior assumptions |
| methodology | TEXT | Methodology |
| created_at | TEXT | Creation timestamp |
| revised_at | TEXT | Last revision timestamp |

### 2.12 forecasts

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

### 2.13 world_states

Versioned state snapshots.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | State identifier |
| domain_id | TEXT | Foreign key to domains |
| version | INTEGER | State version |
| parent_version | TEXT | Parent state version |
| state_hash | TEXT | Hash of the state |
| created_at | TEXT | Creation timestamp |

### 2.14 revision_events

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

### 2.15 dependencies

Relationships between conclusions. Polymorphic references are validated by CHECK constraints and enforced by triggers; every polymorphic pair must have a corresponding referenced row.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Dependency identifier |
| dependent_type | TEXT | Dependent type (claim, hypothesis, conclusion, relationship) |
| dependent_id | TEXT | Dependent identifier |
| prerequisite_type | TEXT | Prerequisite type |
| prerequisite_id | TEXT | Prerequisite identifier |
| dependency_type | TEXT | Type of dependency |
| created_at | TEXT | Creation timestamp |
| CONSTRAINT chk_dependent_type CHECK (dependent_type IN ('claim','hypothesis','conclusion','relationship')) |
| CONSTRAINT chk_prerequisite_type CHECK (prerequisite_type IN ('claim','hypothesis','conclusion','relationship')) |
| FOREIGN KEY (dependent_id) REFERENCES claims(id), -- resolved by trigger for claim dependencies |
| FOREIGN KEY (prerequisite_id) REFERENCES claims(id), -- resolved by trigger for claim dependencies |
| FOREIGN KEY (dependent_id) REFERENCES hypotheses(id), -- resolved by trigger for hypothesis dependencies |
| FOREIGN KEY (prerequisite_id) REFERENCES hypotheses(id), -- resolved by trigger for hypothesis dependencies |
| FOREIGN KEY (dependent_id) REFERENCES conclusions(id), -- resolved by trigger for conclusion dependencies |
| FOREIGN KEY (prerequisite_id) REFERENCES conclusions(id) -- resolved by trigger for conclusion dependencies |
|

### 2.16 source_lineage

Shared origins and information propagation.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Lineage identifier |
| source_id_a | TEXT | First source |
| source_id_b | TEXT | Second source |
| relationship_type | TEXT | Relationship type |
| confidence | REAL | Confidence |
| created_at | TEXT | Creation timestamp |

### 2.17 source_spans

First-class passage-level provenance. Every factual assertion must cite the exact source span: document, character offsets, page, and quoted text.

| Column | Type | Purpose |
|---|---|
| id | TEXT PRIMARY KEY | Span identifier |
| document_id | TEXT NOT NULL | Foreign key to documents |
| start_offset | INTEGER | Character offset start |
| end_offset | INTEGER | Character offset end |
| page | INTEGER | Page number |
| paragraph | TEXT | Paragraph marker |
| quoted_text | TEXT | Exact quoted text |
| language | TEXT | Language |
| created_at | TEXT NOT NULL | Creation timestamp |
| FOREIGN KEY (document_id) REFERENCES documents(id) |

### 2.18 audit_events

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
| CONSTRAINT fk_previous_state FOREIGN KEY (previous_hash) REFERENCES audit_events(event_hash) |

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
- claims.document_id
- claims.domain_id
- entities.canonical_name
- entities.entity_type
- events.event_type
- relationships.source_entity_id
- relationships.target_entity_id
- hypotheses.statement
- forecasts.status
- world_states.domain_id
- source_spans.document_id
- source_spans.start_offset

---

## 4. Foreign Keys

Foreign keys must be enforced:

- documents.source_id → sources.id
- observations.source_id → sources.id
- observations.document_id → documents.id
- observations.subject_id → entities.id
- claims.subject_id → entities.id
- claims.document_id → documents.id
- claims.domain_id → domains.id
- entities.domain_id → domains.id
- entity_aliases.entity_id → entities.id
- entity_aliases.source_id → sources.id
- events.location_id → entities.id
- relationships.source_entity_id → entities.id
- relationships.target_entity_id → entities.id
- hypotheses.domain_id → domains.id
- forecasts.hypothesis_id → hypotheses.id
- dependencies.dependent_id → (resolved by trigger: depends on dependent_type)
- dependencies.prerequisite_id → (resolved by trigger: depends on prerequisite_type)
- source_spans.document_id → documents.id
- audit_events.previous_hash → audit_events.event_hash
- revision_events.previous_state_id → world_states.id
- revision_events.resulting_state_id → world_states.id

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
JOIN source_spans s ON s.id = e.source_span_id
WHERE e.claim_id = 'claim_000001';
```

### 6.5 Find the exact source span for a claim

```sql
SELECT s.quoted_text, s.page, s.start_offset, s.end_offset
FROM source_spans s
JOIN evidence_links e ON e.source_span_id = s.id
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
| Source-span provenance | Every factual claim cites the exact document passage |

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
10. **Source-span provenance: every factual claim must cite the exact document passage it is derived from.**

---

## 9. Source-Span Provenance

The `source_spans` table is a first-class data structure, not an optional text field. Every claim extracted from a source document must reference one or more source spans that cite the exact quoted text, page, and character offsets.

A claim may be supported by multiple evidence links, each tied to a source span. This allows the system to distinguish:

- Whether a claim was supported by one direct quote or many indirect mentions.
- Whether two claims derive from the same passage (shared origin) or different passages.
- Whether a revision that changes a claim's assessment also changes the underlying quotes.

The source-span model is mandatory for all evidence links that trace to documents. For unverified hypotheses, the source_span_id is null, but the claim must still cite its source document and passage conceptually in the `metadata` field.

---

## 10. Polymorphic Dependency Enforcement

The `dependencies` table uses polymorphic identifiers (`dependent_type`/`dependent_id` pairs). Referential integrity is enforced by triggers rather than by a flat set of FOREIGN KEY constraints, because no single flat column set covers all type combinations.

The following triggers enforce referential integrity at the database level:

- Trigger `enforce_dependencies_claim_refs`: When `dependent_type = 'claim'` or `prerequisite_type = 'claim'`, enforces the corresponding foreign key into `claims`.
- Trigger `enforce_dependencies_hypothesis_refs`: When `dependent_type = 'hypothesis'` or `prerequisite_type = 'hypothesis'`, enforces the corresponding foreign key into `hypotheses`.
- Trigger `enforce_dependencies_conclusion_refs`: When `dependent_type = 'conclusion'` or `prerequisite_type = 'conclusion'`, enforces the corresponding foreign key into `conclusions`.

The triggers also enforce the CHECK constraints on `dependent_type` and `prerequisite_type`.

---

## 11. Migration Notes

This schema revision (v0.1.1) introduces changes from v0.1.0:

| Change | Migration Action |
|---|---|
| Added `domains` table | Create `domains` table; populate from existing domain constants |
| Added `document_id` to `claims` | Add column (nullable), backfill from `source_spans`, set NOT NULL with default |
| Added `source_spans` table | Create `source_spans` table with FTS5 index |
| Changed `evidence_links` to reference `source_span_id` | Add `source_span_id` column, backfill from existing passage data |
| Changed `claims.domain_id` FK | Points to `domains.id` (was missing in v0.1.0) |
| Added polymorphic dependency constraints | Add triggers and CHECK constraints |

All existing data must be migrated through the versioned migration framework before the new schema is activated.
