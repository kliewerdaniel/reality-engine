# Storage Architecture

**Reality Engine — Storage Architecture Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document describes the storage architecture of Reality Engine. It covers the initial technology, the required tables, database integrity, and future scaling paths.

---

## 1. Storage Philosophy

The system separates three fundamentally different storage responsibilities:

| Storage Type | Properties | Contents |
|---|---|---|
| **Evidence store** | Append-only, immutable | Original documents, observations, source metadata, extracted claims, immutable provenance records |
| **World-state database** | Versioned | Entities, current conditions, relationships, hypotheses, accepted interpretations |
| **Derived intelligence** | Recomputable | Summaries, embeddings, dashboards, forecasts, dependency maps, analytical reports |

This separation matters because you should be able to delete and rebuild a derived intelligence index without losing the historical evidence or the world-state revision history.

---

## 2. Initial Technology

| Component | Technology | Purpose |
|---|---|---|
| Primary storage | SQLite | Transactional world-state storage |
| Database mode | WAL (Write-Ahead Logging) | Concurrency, crash recovery |
| Foreign-key enforcement | Enabled | Referential integrity |
| Full-text search | FTS5 | Document and claim search |
| Data validation | Pydantic | Schema validation on input |
| API | FastAPI | REST API |
| Background processing | Python task workers | Asynchronous operations |
| Testing | pytest | Unit and integration tests |
| Optional performance components | Rust | Hot-path optimization |

The first version should avoid unnecessary infrastructure. The system must be capable of running on a modern Apple Silicon workstation with approximately 48 GB unified memory.

---

## 3. Core Tables

### 3.1 sources

Source identities and characteristics.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Unique source identifier |
| name | TEXT NOT NULL | Source name |
| source_type | TEXT NOT NULL | Type of source (news, economic, scientific, etc.) |
| canonical_domain | TEXT | Canonical domain classification |
| authority_metadata | TEXT | Source authority metadata |
| collection_policy | TEXT | Rules for collecting from this source |
| created_at | TEXT NOT NULL | When the source was registered |
| updated_at | TEXT | When the record was last updated |

### 3.2 documents

Original collected material.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Document identifier |
| source_id | TEXT NOT NULL | Foreign key to sources |
| source_native_id | TEXT | Source-native identifier |
| canonical_url | TEXT | Canonical URL |
| content_hash | TEXT | Cryptographic hash of the content |
| content_type | TEXT | Document type |
| language | TEXT | Original language |
| published_at | TEXT | Publication timestamp |
| collected_at | TEXT | Collection timestamp |
| content_reference | TEXT | Reference to the original content |
| processing_status | TEXT | Processing state |
| updated_at | TEXT | Last update timestamp |

### 3.3 observations

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
| extraction_version | TEXT | Extraction model and version |
| created_at | TEXT | Creation timestamp |
| updated_at | TEXT | Update timestamp |

### 3.4 claims

Normalized assertions.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Claim identifier |
| subject_id | TEXT | Foreign key to entities |
| predicate | TEXT | Predicate (relationship type) |
| object_value | TEXT | The claim's object |
| claim_type | TEXT | Claim type (Factual, Reported, etc.) |
| domain_id | TEXT | Foreign key to domain |
| valid_from | TEXT | Valid time start |
| valid_to | TEXT | Valid time end |
| recorded_at | TEXT | When the system recorded it |
| status | TEXT | Evidence status |
| revision_number | INTEGER | Revision counter |
| created_at | TEXT | Creation timestamp |
| updated_at | TEXT | Update timestamp |

### 3.5 evidence_links

Support and contradiction relationships.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Link identifier |
| claim_id | TEXT | Foreign key to claims |
| observation_id | TEXT | Foreign key to observations |
| relationship_type | TEXT | SUPPORTS, CONTRADICTS, etc. |
| explanation | TEXT | Explanation of the inference |
| assessment_status | TEXT | Assessment status |
| created_at | TEXT | Creation timestamp |

### 3.6 entities

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

### 3.7 entity_aliases

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

### 3.8 events

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

### 3.9 relationships

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

### 3.10 hypotheses

Explanatory models.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Hypothesis identifier |
| statement | TEXT | The hypothesis statement |
| domain_id | TEXT | Foreign key to domain |
| status | TEXT | Hypothesis status |
| prior_assumptions | TEXT | Prior assumptions |
| methodology | TEXT | Methodology |
| created_at | TEXT | Creation timestamp |
| revised_at | TEXT | Last revision timestamp |

### 3.11 forecasts

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

### 3.12 world_states

Versioned state snapshots.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | State identifier |
| domain_id | TEXT | Foreign key to domain |
| version | INTEGER | State version |
| parent_version | TEXT | Parent state version |
| state_hash | TEXT | Hash of the state |
| created_at | TEXT | Creation timestamp |

### 3.13 revision_events

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

### 3.14 dependencies

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

### 3.15 source_lineage

Shared origins and information propagation.

| Column | Type | Purpose |
|---|---|---|
| id | TEXT PRIMARY KEY | Lineage identifier |
| source_id_a | TEXT | First source |
| source_id_b | TEXT | Second source |
| relationship_type | TEXT | Relationship type |
| confidence | REAL | Confidence |
| created_at | TEXT | Creation timestamp |

### 3.16 audit_events

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

## 4. Database Integrity

### 4.1 Required Controls

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

### 4.2 Hash Chain

A hash chain may be used to detect alteration of audit history. A hash chain alone does not guarantee tamper resistance if an attacker controls the database and all associated keys. External checkpoints or independently stored signatures may be introduced later.

---

## 5. FTS5 Full-Text Search

FTS5 is used for full-text search on:

- Source names
- Document content
- Claim text
- Entity names
- Hypothesis statements

FTS5 provides the initial full-text search capability. If performance requirements dictate, a dedicated search engine may be introduced later.

---

## 6. Idempotency Keys

The system must support idempotent processing. Each processing operation must use an idempotency key so that reprocessing the same document does not create duplicate observations or artificially increase confidence.

---

## 7. Future Scaling

If the project outgrows SQLite, introduce components based on measured requirements. Potential additions:

| Component | Purpose |
|---|---|
| PostgreSQL | Concurrent transactional workloads |
| Dedicated graph storage | Relationship traversal at scale |
| DuckDB | Analytical processing |
| Specialized vector storage | Semantic retrieval |
| Message queues | Distributed ingestion workers |
| Object storage | Large documents |

No migration should be performed simply because a technology is fashionable.

---

## 8. Database Growth

- Large source documents should be stored outside frequently queried relational records when appropriate.
- The database should retain content references, hashes, and metadata.
- Free space should be periodically checked and reclaimed.

---

## 9. Storage and the Revision Engine

The revision engine must preserve the state before and after each revision. The `world_states` table records the state hash of every committed revision. The `revision_events` table records the mapping from previous state to resulting state.

This separation ensures that:

- Historical versions remain recoverable.
- A revision never changes the historical transaction record of an earlier accepted revision.
- Every accepted state transition has a recorded trigger.
- Historical queries cannot silently incorporate future observations.

---

## 10. Summary

- Primary storage: SQLite with WAL mode.
- Foreign-key enforcement is enabled.
- Full-text search via FTS5.
- Three storage responsibilities: evidence store, world-state database, derived intelligence.
- Core tables: sources, documents, observations, claims, evidence_links, entities, entity_aliases, events, relationships, hypotheses, forecasts, world_states, revision_events, dependencies, source_lineage, audit_events.
- Database integrity is enforced through foreign keys, unique constraints, transactional commits, and immutable evidence.
- The audit ledger is append-only with a hash chain.
- Future scaling is driven by measured requirements, not fashion.
