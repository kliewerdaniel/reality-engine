# System Components

**Reality Engine — System Components Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document describes the system components, their responsibilities, dependencies, interfaces, data ownership, and failure behavior.

---

## 1. Component Overview

| Subsystem | Components | Primary Responsibility |
|---|---|---|
| **Core** | World State, Revision, Temporal, Ontology, Events | Authoritative data model, revision logic, temporal semantics, event ledger |
| **Observation** | Adapters, Collectors, Scheduler, Normalization, Deduplication | Collect and normalize information from external sources |
| **Evidence** | Extraction, Claims, Provenance, Lineage, Contradiction, Verification | Transform documents into structured evidence; maintain provenance |
| **Intelligence** | Analyst, Skeptic, Historian, Forecaster, Verifier, Integrator | Analyze the world model; propose revisions; verify consistency |
| **Domains** | Geopolitical, Economic, Financial, Scientific, Technological, Environmental, Social, Security, Legal, Infrastructure | Domain-specific models and schemas |
| **Governance** | Policies, Permissions, Frozen Spine, Audit | Deterministic authorization and audit |
| **Storage** | SQLite, Documents, Indexes, Migrations, Projections | Persistent storage and retrieval |
| **API** | Routes, Schemas, Services | External interfaces |
| **Frontend** | Components, Pages, Explorer, Timeline, Evidence, Intelligence, Observatory | User interface |
| **Evaluation** | Datasets, Tests, Benchmarks | Evaluation and evaluation infrastructure |

---

## 2. Core Subsystem

### 2.1 World State

**Purpose:** Maintain the current accepted world state.

**Responsibilities:**

- Maintain entities, conditions, relationships, claims, and hypotheses.
- Maintain world-state snapshots (versions).
- Provide historical state queries.

**Public interfaces:**

- `get_world_state(version=None)` — returns the current or a specific version.
- `query_world(query)` — structured query interface.
- `get_entity_timeline(entity_id)` — returns the entity's history.
- `get_entity_state(entity_id)` — returns the entity's current state.

**Dependencies:**

- Core domain models (entities, events, relationships, temporal)
- Storage

**Data ownership:**

- All accepted world state is owned by this component.

**Tests:**

- World-state query correctness
- Version management
- Historical reconstruction

**What it must not do:**

- It must not accept uncommitted drafts.
- It must not bypass the revision engine.

---

### 2.2 Revision Engine

**Purpose:** Determine how new evidence affects existing understanding.

**Responsibilities:**

- Identify affected claims when new evidence arrives.
- Traverse dependency graphs.
- Generate revision proposals.
- Validate proposals (temporal consistency, provenance, governance).
- Commit or reject proposals atomically.
- Record revision events.
- Preserve historical versions.

**Public interfaces:**

- `propose_revision(observation, context)` — generates a proposal.
- `validate_revision(proposal)` — validates a proposal.
- `commit_revision(proposal)` — atomically commits.
- `get_revision_history(entity_id)` — returns the revision history.

**Dependencies:**

- Core domain models
- Storage
- Governance (Frozen Spine)

**Data ownership:**

- Revision events, dependencies, world-state snapshots.

**Tests:**

- Revision transaction atomicity
- Dependency traversal correctness
- Temporal consistency validation
- Rollback behavior

**What it must not do:**

- It must not allow LLM-generated proposals to bypass validation.
- It must not silently overwrite historical records.

---

### 2.3 Temporal

**Purpose:** Handle temporal semantics.

**Responsibilities:**

- Maintain bitemporal records (valid time + transaction time).
- Support historical reconstruction queries.
- Enforce interval semantics.

**Public interfaces:**

- `record_with_valid_time(entity, valid_from, valid_to, recorded_at)`
- `get_history(entity_id, knowledge_time)` — historical reconstruction
- `get_current_valid(entity_id)` — current state

**Dependencies:**

- Storage

**Data ownership:**

- All time-sensitive fields on entities, events, claims, observations, relationships.

**Tests:**

- Historical reconstruction correctness
- Bitemporal query correctness
- Interval semantics

**What it must not do:**

- It must not allow string-based timestamp comparisons.
- It must not permit silent overwriting of historical records.

---

### 2.4 Ontology

**Purpose:** Define the shared ontology.

**Responsibilities:**

- Define object types, relationship types, and constraints.
- Define domain schemas.
- Manage ontology evolution.

**Public interfaces:**

- `get_object_type(type_name)` — returns object type definition.
- `get_relationship_type(type_name)` — returns relationship type definition.
- `validate_object(instance)` — validates an object against the ontology.

**Dependencies:**

- Domains (they extend the common ontology)

**Data ownership:**

- Ontology definitions, domain schemas.

**Tests:**

- Ontology consistency
- Domain schema compatibility

**What it must not do:**

- It must not allow a domain to replace the common ontology.

---

### 2.5 Events

**Purpose:** Manage the event ledger.

**Responsibilities:**

- Record all significant events.
- Support replay and reproducibility.
- Preserve event immutability.

**Public interfaces:**

- `record_event(event_type, actor, resource, payload, previous_hash, created_at)`
- `get_event_history(resource_type, resource_id)` — returns the event history
- `rebuild_projection(projection_type)` — rebuilds derived projections

**Dependencies:**

- Storage

**Data ownership:**

- All audit events, revision events, and significant system events.

**Tests:**

- Event immutability
- Replay correctness
- Audit trail completeness

**What it must not do:**

- It must not allow events to be deleted.
- It must not allow events to be silently modified.

---

## 3. Observation Subsystem

### 3.1 Source Adapter

**Purpose:** Collect information from a specific source type.

**Responsibilities:**

- Identify the source.
- Collect items.
- Normalize items.
- Persist checkpoints.
- Report health.

**Public interface:**

```python
class SourceAdapter:
    def identify(self) -> SourceIdentity:
        ...

    def collect(self, cursor=None) -> CollectionBatch:
        ...

    def normalize(self, raw_item) -> NormalizedDocument:
        ...

    def checkpoint(self) -> CollectionCheckpoint:
        ...

    def health(self) -> AdapterHealth:
        ...
```

**Dependencies:**

- Storage (for checkpoints and document archive)

**Data ownership:**

- Source-specific data. Each adapter is responsible for its own data.

**Tests:**

- Collection idempotency
- Checkpoint persistence
- Health reporting

**What it must not do:**

- It must not bypass the normalization step.
- It must not collect data without a documented collection policy.

---

### 3.2 Collector

**Purpose:** Orchestrate collection from multiple adapters.

**Responsibilities:**

- Schedule collection runs.
- Manage collection budget across sources.
- Apply collection policies.

**Public interfaces:**

- `schedule_collection(source_ids, interval)` — adds a scheduled collection
- `run_collection(source_id, cursor=None)` — runs a collection
- `get_checkpoint(source_id)` — returns the current checkpoint

**Dependencies:**

- Source adapters
- Storage

**Tests:**

- Scheduling correctness
- Budget allocation

**What it must not do:**

- It must not allow one high-volume source to consume the entire processing budget.

---

### 3.3 Normalization

**Purpose:** Normalize documents into a standard format.

**Responsibilities:**

- Convert source-specific formats into normalized documents.
- Extract metadata.
- Apply content hashing.

**Public interface:**

```python
class Normalizer:
    def normalize(self, raw_item, source_id) -> NormalizedDocument:
        ...
```

**Dependencies:**

- Source adapters

**Tests:**

- Normalization correctness

**What it must not do:**

- It must not lose metadata during normalization.

---

### 3.4 Deduplication

**Purpose:** Detect and handle duplicate content.

**Responsibilities:**

- Detect identical content across multiple URLs.
- Mark duplicates without discarding source records.

**Tests:**

- Deduplication correctness
- Multi-URL recognition

**What it must not do:**

- It must not discard identical content from individual source records.

---

## 4. Evidence Subsystem

### 4.1 Extraction

**Purpose:** Extract observations and claims from documents.

**Responsibilities:**

- Extract candidate claims from documents.
- Classify claims by type.
- Resolve entities against the registry.
- Link claims to source passages.

**Public interface:**

```python
class Extractor:
    def extract(self, document_id) -> ExtractionResult:
        ...
```

**Dependencies:**

- Model providers (for extraction)
- Core domain models
- Entity registry

**Data ownership:**

- Extracted observations, claims, and entity references.

**Tests:**

- Extraction accuracy
- Claim type classification
- Entity resolution correctness

**What it must not do:**

- It must not overwrite the original document.
- It must not generate claims without a source reference.

---

### 4.2 Claims

**Purpose:** Manage claim objects.

**Responsibilities:**

- Store and retrieve claims.
- Link claims to evidence.
- Track claim status and revision history.

**Public interface:**

```python
class ClaimStore:
    def create_claim(claim) -> ClaimID:
        ...
    def get_claim(claim_id) -> Claim:
        ...
    def add_evidence(claim_id, evidence_id, relationship_type, provenance) -> None:
        ...
```

**Dependencies:**

- Storage

**Tests:**

- Claim retrieval
- Evidence linking

---

### 4.3 Provenance

**Purpose:** Track the provenance of all claims and observations.

**Responsibilities:**

- Record source → document → claim chains.
- Preserve provenance through revisions.

**Public interface:**

```python
class ProvenanceStore:
    def record_provenance(claim_id, source_id, document_id, passage) -> None:
        ...
    def get_provenance(claim_id) -> Provenance:
        ...
```

**Dependencies:**

- Storage

**Tests:**

- Provenance completeness
- Provenance preservation through revisions

---

### 4.4 Lineage

**Purpose:** Track source lineage.

**Responsibilities:**

- Build the source lineage graph.
- Identify shared origins and information propagation.

**Public interface:**

```python
class LineageStore:
    def record_lineage(source_a, source_b, relationship_type, confidence) -> None:
        ...
    def get_lineage(source_id) -> LineageGraph:
        ...
```

**Dependencies:**

- Storage

**Tests:**

- Lineage graph correctness

---

### 4.5 Contradiction Detection

**Purpose:** Detect contradictions in the evidence.

**Responsibilities:**

- Detect genuine contradictions.
- Distinguish apparent contradictions from different time periods, units, or definitions.

**Public interface:**

```python
class ContradictionDetector:
    def detect(self, claim_id) -> ContradictionList:
        ...
```

**Dependencies:**

- Evidence store
- Temporal storage

**Tests:**

- Contradiction detection accuracy
- False-positive rate

---

### 4.6 Verification

**Purpose:** Verify the integrity of the system.

**Responsibilities:**

- Verify source attribution.
- Validate evidence relationships.
- Check temporal consistency.
- Check schema validity.

**Public interface:**

```python
class Verifier:
    def verify(self, claim_id) -> VerificationResult:
        ...
```

**Dependencies:**

- Storage
- Evidence store

**Tests:**

- Verification correctness

---

## 5. Intelligence Subsystem

### 5.1 Analyst

**Purpose:** Extract meaning, identify relationships, construct interpretations, propose hypotheses.

**Responsibilities:**

- Interpret observations.
- Extract candidate claims.
- Identify possible relationships.
- Generate hypotheses.
- Explain developments.

**Public interface:**

```python
class Analyst:
    def analyze(self, observations, context) -> AnalystResponse:
        ...
```

**Dependencies:**

- Model providers
- Core domain models

**Data ownership:**

- Analyst-proposed claims, hypotheses, and interpretations.

**Tests:**

- Analyst output quality
- Evidence reference correctness

**What it must not do:**

- It must not write authoritative world-state records directly.

---

### 5.2 Skeptic

**Purpose:** Search for contradictions, missing evidence, alternative explanations, unsupported assumptions.

**Responsibilities:**

- Find contradictory evidence.
- Identify unsupported assumptions.
- Detect alternative explanations.
- Challenge weak inferences.
- Identify missing information.

**Public interface:**

```python
class Skeptic:
    def critique(self, hypothesis_id, context) -> SkepticResponse:
        ...
```

**Dependencies:**

- Model providers
- Evidence store
- Temporal storage

**Tests:**

- Skeptic sensitivity to contradictions

**What it must not do:**

- Its agreement with another model does not constitute verification.

---

### 5.3 Historian

**Purpose:** Connect current events to historical precedents and track how previous interpretations changed.

**Responsibilities:**

- Retrieve historical context.
- Compare previous events.
- Identify recurring patterns.
- Track previous interpretations.
- Identify historical differences.

**Public interface:**

```python
class Historian:
    def research(self, topic, time_range) -> HistoricalAnalysis:
        ...
```

**Dependencies:**

- World model
- Temporal storage

**Tests:**

- Historical reconstruction accuracy

---

### 5.4 Forecaster

**Purpose:** Generate testable predictions and evaluate forecasts.

**Responsibilities:**

- Generate testable predictions based on hypotheses.
- Record probabilities.
- Define outcome conditions.
- Specify evaluation horizons.
- Track forecast performance.

**Public interface:**

```python
class Forecaster:
    def create_forecast(self, hypothesis_id, probability, horizon, criteria) -> ForecastID:
        ...
    def evaluate_forecast(self, forecast_id) -> EvaluationResult:
        ...
```

**Dependencies:**

- World model
- Temporal storage

**Tests:**

- Forecast calibration

---

### 5.5 Verifier

**Purpose:** Check source attribution, evidence relationships, temporal consistency, and schema validity.

**Responsibilities:**

- Check provenance.
- Validate schema compliance.
- Verify source references.
- Check temporal consistency.
- Detect unsupported assertions.
- Validate revision requirements.

**Public interface:**

```python
class Verifier:
    def verify(self, proposal) -> VerificationResult:
        ...
```

**Dependencies:**

- Storage
- Evidence store
- Temporal storage
- Governance

**Tests:**

- Verification checklist coverage

---

### 5.6 Systems Integrator

**Purpose:** Coordinate analytical tasks, collect agent outputs, generate revision proposals, resolve conflicts, submit proposals to the revision engine.

**Responsibilities:**

- Coordinate analytical tasks.
- Collect agent outputs.
- Generate revision proposals.
- Resolve schema and dependency conflicts.
- Submit proposals to the deterministic revision engine.

**Public interface:**

```python
class SystemsIntegrator:
    def process(self, observation) -> RevisionProposal:
        ...
```

**Dependencies:**

- Intelligence agents
- Revision engine

**Tests:**

- Proposal coordination

---

## 6. Domains

Each domain provides a specialized schema extending the common ontology.

| Domain | Key Objects |
|---|---|
| Geopolitical | States, governments, alliances, treaties, diplomatic relationships, territorial changes, conflicts, sanctions, political institutions |
| Economic | GDP, inflation, employment, interest rates, trade, production, debt, consumption, monetary policy, fiscal policy |
| Financial | Markets, instruments, central banking, capital flows, publications |
| Scientific | Publications, researchers, institutions, hypotheses, experimental results, replications, retractions, research domains |
| Technological | Companies, software projects, hardware, patents, technical capabilities, standards, research developments, releases |
| Environmental | Climate indicators, weather observations, ecosystems, natural resources, emissions, environmental events |
| Social | Demographics, population changes, education, public opinion |
| Security | Military developments, conflicts, treaties, sanctions, arms control |
| Legal | Courts, legislation, regulatory actions, treaty disputes, institutional changes |
| Infrastructure | Grids, transport, supply chains, energy production, industrial facilities |

Each domain:

- Retains its own specialized objects and relationships.
- Shares the common ontology.
- Is extensible without replacing existing models.

---

## 7. Governance Subsystem

### 7.1 Policies

**Purpose:** Define governance policies.

**Responsibilities:**

- Define rules for what can be modified.
- Define rules for revision proposals.

**Tests:**

- Policy enforcement

---

### 7.2 Permissions

**Purpose:** Enforce least-privilege permissions.

**Responsibilities:**

- Define permissions.
- Enforce access controls.

**Tests:**

- Permission enforcement

---

### 7.3 Frozen Spine

**Purpose:** Provide the authorization and execution boundary.

**Responsibilities:**

- Validate that the actor is authorized.
- Validate that the operation is permitted.
- Enforce least-privilege permissions.
- Execute approved operations or reject them.

**Public interface:**

```python
class FrozenSpine:
    def authorize(self, actor, operation, resource) -> AuthorizationDecision:
        ...
    def execute(self, operation, resource) -> ExecutionResult:
        ...
```

**Tests:**

- Authorization correctness
- Reject unauthorized operations

---

### 7.4 Audit

**Purpose:** Record all significant operations.

**Responsibilities:**

- Record audit events.
- Preserve audit history (append-only).
- Support replay.

**Tests:**

- Audit completeness
- Event immutability

---

## 8. Storage Subsystem

### 8.1 SQLite

**Purpose:** Primary storage.

**Responsibilities:**

- Store core tables.
- Enforce foreign keys, constraints, and indexes.
- Support FTS5 full-text search.

**Tests:**

- Schema validation
- Query correctness

---

### 8.2 Documents

**Purpose:** Store document archives.

**Responsibilities:**

- Store original documents.
- Preserve content hashes and metadata.

**Tests:**

- Document retrieval

---

### 8.3 Indexes

**Purpose:** Maintain search indexes and derived indexes.

**Responsibilities:**

- Maintain FTS5 indexes.
- Maintain derived indexes.

**Tests:**

- Index accuracy

---

### 8.4 Migrations

**Purpose:** Apply schema migrations.

**Responsibilities:**

- Apply versioned schema migrations.
- Record migration versions.

**Tests:**

- Migration correctness

---

### 8.5 Projections

**Purpose:** Maintain derived world-state projections.

**Responsibilities:**

- Rebuild projections from recorded events.
- Support query performance.

**Tests:**

- Projection accuracy

---

## 9. API Subsystem

### 9.1 Routes

**Purpose:** Expose API endpoints.

**Responsibilities:**

- Route requests to services.
- Handle errors.
- Version the API.

**Tests:**

- Endpoint correctness

---

### 9.2 Schemas

**Purpose:** Validate API payloads.

**Responsibilities:**

- Validate request payloads.
- Serialize responses.

**Tests:**

- Schema validation

---

### 9.3 Services

**Purpose:** Implement API services.

**Responsibilities:**

- Implement business logic for API endpoints.
- Coordinate with internal services.

**Tests:**

- Service correctness

---

## 10. Frontend Subsystem

### 10.1 Components

**Purpose:** Provide reusable UI components.

**Responsibilities:**

- World state visualization.
- Search and filter.
- Revision history display.

**Tests:**

- Component correctness

---

### 10.2 Pages

**Purpose:** Provide page-level UI.

**Responsibilities:**

- World Overview
- World Explorer
- Reality Timeline
- Change Intelligence
- Evidence Explorer
- Ask Reality
- Forecast Observatory
- System Observatory
- Administration

**Tests:**

- Page correctness

---

### 10.3 Explorer, Timeline, Evidence, Intelligence, Observatory

**Purpose:** Provide specialized views.

**Responsibilities:**

- World Explorer: interactive map and graph.
- Reality Timeline: historical reconstruction.
- Evidence Explorer: inspect evidence.
- Intelligence: agent analysis results.
- Observatory: operational health.

**Tests:**

- View correctness

---

## 11. Evaluation Subsystem

### 11.1 Datasets

**Purpose:** Provide test datasets.

**Responsibilities:**

- Provide extraction datasets.
- Provide provenance datasets.
- Provide temporal datasets.
- Provide revision datasets.
- Provide forecasting datasets.
- Provide adversarial datasets.

**Tests:**

- Dataset correctness

---

### 11.2 Tests

**Purpose:** Run evaluation tests.

**Responsibilities:**

- Run extraction tests.
- Run provenance tests.
- Run temporal tests.
- Run revision tests.
- Run forecasting tests.
- Run adversarial tests.

**Tests:**

- Test correctness

---

### 11.3 Benchmarks

**Purpose:** Measure performance.

**Responsibilities:**

- Run benchmarks.
- Report results.

**Tests:**

- Benchmark correctness

---

## 12. Failure Behavior Summary

| Component | Failure | Response |
|---|---|---|
| Source adapter | Network failure | Retry with backoff; report health |
| Source adapter | Rate limiting | Wait and resume; report failure |
| Extraction pipeline | Extraction failure | Log, preserve original, do not fabricate |
| Revision validation | Temporal inconsistency | Reject proposal; record reason |
| Revision validation | Provenance violation | Reject proposal; record reason |
| Storage | Database error | Fail-closed; prevent data loss |
| API | Unauthorized request | Return 403; log |
| Intelligence agent | Model failure | Fall back or retry; do not block |
| Infrastructure | Disk full | Fail-closed; alert |

---

## 13. Public Interfaces Summary

| Subsystem | Public Interface |
|---|---|
| Core | Core domain interfaces |
| Observation | SourceAdapter interface, scheduler interface |
| Evidence | Extraction pipeline, evidence linking, contradiction detection |
| Intelligence | Agent contracts, agent interfaces |
| Domains | Domain-specific schemas and services |
| Governance | Authorization boundary, audit event publishing |
| Storage | Storage interfaces |
| API | REST API (FastAPI) |
| Frontend | Web interface (React/TypeScript) |
| Evaluation | Test suite, benchmark runner |

---

## 14. Data Ownership Summary

| Data | Owner |
|---|---|
| Entities, relationships, claims, observations, evidence | Core (World State) |
| Revision events, dependencies, world-state snapshots | Core (Revision) |
| Temporal records | Core (Temporal) |
| Event ledger, audit events | Core (Events) |
| Source records, documents, checkpoints | Observation |
| Provenance, lineage, contradictions | Evidence |
| Agent outputs, proposals | Intelligence |
| Domain-specific data | Domains |
| Audit trails | Governance |
| Storage metadata | Storage |
| API payloads | API |
| UI state | Frontend |
| Evaluation datasets, test results | Evaluation |

---

## 15. Summary

The system has eleven major subsystems:

1. Core (World State, Revision, Temporal, Ontology, Events)
2. Observation (Adapters, Collectors, Scheduler, Normalization, Deduplication)
3. Evidence (Extraction, Claims, Provenance, Lineage, Contradiction, Verification)
4. Intelligence (Analyst, Skeptic, Historian, Forecaster, Verifier, Integrator)
5. Domains (Geopolitical, Economic, Financial, Scientific, Technological, Environmental, Social, Security, Legal, Infrastructure)
6. Governance (Policies, Permissions, Frozen Spine, Audit)
7. Storage (SQLite, Documents, Indexes, Migrations, Projections)
8. API (Routes, Schemas, Services)
9. Frontend (Components, Pages, Explorer, Timeline, Evidence, Intelligence, Observatory)
10. Evaluation (Datasets, Tests, Benchmarks)
11. Scripts, Migrations

Each component has a clearly defined responsibility, dependency, data ownership, test strategy, and failure behavior. The system is organized as a modular monolith with explicit subsystem boundaries so that components can be separated later if necessary.
