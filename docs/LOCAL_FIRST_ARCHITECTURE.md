# Local-First Architecture

**Reality Engine — Local-First Architecture Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document describes the local-first architecture of Reality Engine. It explains what runs locally, what can be optional, and where future distributed execution might be justified.

---

## 1. Design Philosophy

Reality Engine is designed to run locally-first, with cloud services as optional integrations, not architectural dependencies.

### 1.1 Core Principles

| Principle | Meaning |
|---|---|
| **Local storage** | Data is stored locally first. The world model is stored in SQLite. |
| **Local inference** | The system uses local inference (Ollama, llama.cpp) by default. |
| **Replaceable model providers** | Models are accessed through a common model interface. Any provider can be plugged in. |
| **User-controlled infrastructure** | The user controls the infrastructure. Cloud services are optional. |
| **Privacy by default** | The initial application should prioritize public information. Private data integrations must require explicit authorization. |

---

## 2. Technology Stack

| Component | Technology | Reason |
|---|---|---|
| Core application | Python | Fast development, extensive ecosystem |
| Database | SQLite | Local, zero-configuration, ACID |
| Database mode | WAL (Write-Ahead Logging) | Concurrency, crash recovery |
| Full-text search | FTS5 | Integrated, no external dependencies |
| Data validation | Pydantic | Schema validation |
| API | FastAPI | Modern, fast, standard |
| Background processing | Python task workers | Simple, local, reliable |
| Interface | React and TypeScript | Rich UI, type safety |
| Visualization | D3.js or equivalent | Interactive visualization |
| Local inference | Ollama | Easy local model management |
| Alternative inference | llama.cpp | Lightweight, portable |
| Embeddings | Local embedding models | No cloud dependency |
| Optional performance components | Rust | Hot-path optimization |
| Testing | pytest | Standard testing framework |

---

## 3. Inference Architecture

### 3.1 Model Abstraction

All inference must pass through a common model interface:

```python
class ModelProvider:
    def generate(self, request):
        ...

    def embed(self, request):
        ...

    def health(self):
        ...

    def capabilities(self):
        ...
```

The application must not depend directly on a single provider's proprietary request format.

### 3.2 Model Selection by Task

| Task | Preferred Model Capability |
|---|---|
| Entity extraction | Small instruction model |
| Claim extraction | Structured-output model |
| Classification | Small local model |
| Relationship discovery | Reasoning-capable model |
| Contradiction analysis | Independent reasoning model |
| Historical synthesis | Long-context model |
| Final explanation | Instruction-following model |

### 3.3 Model Independence

The system must be capable of:

- Replacing any model without changing the underlying data model.
- Running several models against the same evidence and comparing their interpretations.
- Interfacing with a smaller model for routine extraction and a larger model for difficult contradictions.
- Changing the underlying model without destroying the knowledge infrastructure.

### 3.4 Hardware Requirements

The initial system should be capable of running on a modern Apple Silicon workstation with approximately 48 GB unified memory.

Resource-intensive tasks should be queued. Large global ingestion workloads should not require all documents to remain in model context.

### 3.5 Mandatory Optimization Techniques

The following are mandatory:

- Batch processing
- Caching
- Incremental indexing
- Compact intermediate representations

---

## 4. Storage Architecture

### 4.1 Primary Storage

- **SQLite** — primary transactional storage, in local storage.
- **FTS5** — full-text search, integrated with SQLite.

### 4.2 Document Storage

- Large source documents are stored outside frequently queried relational records when appropriate.
- The database retains content references, hashes, and metadata.

### 4.3 Document Archive

- Original documents are preserved in an accessible archive.
- The archive supports content hashing for deduplication.

### 4.4 Derived Indexes

- Derived intelligence indexes are built from the database.
- The indexes can be deleted and rebuilt without losing historical evidence or revision history.

---

## 5. Infrastructure Boundaries

| Component | Local | Optional Cloud |
|---|---|---|
| Database | SQLite (local) | — |
| Full-text search | FTS5 (local) | — |
| Document archive | Local storage | — |
| Inference | Ollama, llama.cpp (local) | Optional cloud providers |
| Embeddings | Local (local) | Optional cloud providers |
| RSS and API ingestion | Local collection | — |
| Source adapters | Local | — |
| Background processing | Local task workers | — |
| API server | Local | — |
| Frontend | Local browser | — |
| Evaluation | Local | Optional benchmark services |
| Image/audio/video rendering | Local | — |
| External source APIs | — | GDELT, FRED, etc. (these are source APIs, not system infrastructure) |

---

## 6. Distributed Execution

### 6.1 Deferral

Distributed execution is **not** justified in the initial implementation. The specification explicitly recommends:

- A modular monolith.
- Embedded task processing.
- No microservices from the start.

### 6.2 When to Justify Distribution

Distributed execution is justified only when measured requirements demand it:

| Decision | Requirement |
|---|---|
| **OD-007** | Distributed execution is justified only after measured bottlenecks |
| **OD-007** | Initial recommendation: Only after measured bottlenecks |

### 6.3 Future Targets (If Needed)

If the project outgrows SQLite, potential additions include:

- PostgreSQL for concurrent transactional workloads.
- Dedicated graph storage.
- DuckDB for analytical processing.
- Specialized vector storage.
- Message queues.
- Distributed ingestion workers.
- Object storage.

---

## 7. Operational Considerations

### 7.1 Installation

The application should support local installation with documented prerequisites. A single development command should start the core services where practical.

### 7.2 Configuration

Configuration should support:

- Database location.
- Document storage location.
- Enabled source adapters.
- Collection intervals.
- Model providers.
- Model selection.
- Processing limits.
- Domain settings.
- Governance policies.

### 7.3 Secrets

Secrets must be stored outside source control. Use `.env.example` to document required environment variables.

### 7.4 Logging

Logs should distinguish:

- Logging levels.
- Collection operations.
- Extraction operations.
- Inference operations.
- Revision proposals.
- Accepted revisions.
- Rejected revisions.
- Validation failures.
- Database errors.

### 7.5 Recovery

The system must support:

- Database backups.
- Document archive recovery.
- Failed task retries.
- Processing checkpoint recovery.
- Event replay.
- Projection rebuilding.

---

## 8. Privacy and Data Boundaries

### 8.1 Initial Application

The initial application should prioritize public information.

### 8.2 Private Data

Private data integrations must require explicit authorization and appropriate access controls.

### 8.3 Access Boundaries

Public and private information should have separate access boundaries.

### 8.4 Provenance

Every factual assertion must have traceable provenance. The system must never allow a confident interpretation to overwrite the underlying evidence without preserving the evidence.

---

## 9. Observability

The system must represent the limitations of its own information environment.

### 9.1 Observability Model

| Category | Meaning |
|---|---|
| OBSERVABLE | Fully covered by available data |
| PARTIALLY_OBSERVABLE | Some data exists, gaps remain |
| NOT_DIRECTLY_OBSERVABLE | Cannot be directly observed |
| NOT_YET_COLLECTED | Data may exist but has not been gathered |
| UNKNOWN_LIMITATIONS | Limitations are not yet characterized |

### 9.2 Observability Metrics

Track:

- Source coverage
- Geographic coverage
- Temporal coverage
- Update frequency
- Missing data
- Data quality
- Known reporting delays
- Entity resolution completeness

### 9.3 Domain Observability

Each domain should have an observability profile. Example:

```yaml
domain: international_trade
observable:
  - published_trade_statistics
  - customs_data_where_available
  - shipping_movements
  - official_trade_announcements
partially_observable:
  - informal_trade
  - private_commercial_agreements
  - unreported_transactions
not_directly_observable:
  - undisclosed_negotiations
  - private_decision_making
known_limitations:
  - reporting_delays
  - missing_datasets
  - geographic_coverage_gaps
  - measurement_differences
```

### 9.4 Active World Observation

The system should eventually identify gaps in its understanding and determine which additional observations would most improve its understanding.

Observation priority heuristic:

```text
Observation Priority =
    Potential Information Value
  × Uncertainty Reduction
  × Domain Relevance
  × Time Sensitivity
  / Collection Cost
```

---

## 10. Summary

Reality Engine is a local-first system:

- **Storage:** SQLite, FTS5, local document archive.
- **Inference:** Ollama, llama.cpp, local embedding models.
- **API:** FastAPI, served locally.
- **Interface:** React and TypeScript in the browser.
- **Background processing:** Python task workers.
- **Distribution:** Deferred until measured bottlenecks justify it.
- **Cloud services:** Optional integrations, not architectural dependencies.

The architecture preserves the distinction between local operation and optional cloud services. The knowledge infrastructure is designed to work without any cloud API.
