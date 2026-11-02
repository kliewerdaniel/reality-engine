# Reality Engine

**Reality Engine** is a continuously operating computational system that constructs, maintains, evaluates, and revises a global representation of the world using observations collected from heterogeneous information sources.

**Status:** Architecture specification v0.1.0 — documentation phase (November 2026)
**Author:** Daniel Kliewer
**Classification:** Open research and software architecture
**Implementation philosophy:** Local-first, evidence-grounded, temporally consistent, continuously revisable intelligence infrastructure.

---

## 0. First End-to-End Proof

The defining capability of Reality Engine is not a dashboard or a multi-agent system. It is the ability to **change its understanding of the world without losing the history of how it got there**.

The first executable proof is in the `demo/` directory:

**`demo/evidence_foundation_demo.py`**

This script executes the full eight-step workflow defined in the acceptance criteria:

1. Register a source and ingest an original document.
2. Preserve its content, hash, collection time, and provenance.
3. Extract a claim and link it to an exact passage in the document.
4. Ingest a second document that challenges the claim.
5. Generate a revision proposal without changing accepted state.
6. Validate the proposal through deterministic rules.
7. Commit the accepted revision while preserving the previous state.
8. Query both what the system believed before and what it believes now.

```bash
cd /Users/danielkliewer/Projects/reality-engine
python demo/evidence_foundation_demo.py
```

The script creates an in-memory SQLite database at `demo/demo_evidence_foundation.db` and prints each step with its results. A successful run ends with the claim status transitioning from `SUPPORTED` to `CONTESTED`, the previous state hash preserved in the `revisions` table, and both the before/after world states queryable.

---

## 1. Project Definition

Reality Engine is a continuously operating computational system designed to construct, maintain, evaluate, and revise a global representation of the world using observations collected from heterogeneous information sources.

Its purpose is to create an evolving model of global reality that:

- Preserves the distinction between immutable evidence and versioned interpretations.
- Represents temporal knowledge explicitly (valid time vs. transaction time).
- Performs dependency-aware revision rather than simple information accumulation.
- Uses specialized intelligence agents as proposers, not as authorities.
- Governs all state transitions with deterministic validation and verification.
- Executes locally-first with replaceable, provider-neutral inference backends.

Reality Engine does not assume that available information represents reality completely or accurately. Instead, it:

- Maintains a versioned understanding derived from available observations.
- Records the provenance of every significant assertion.
- Identifies contradictory evidence.
- Tracks uncertainty explicitly.
- Revises previous interpretations when new information becomes available.

**Primary innovation:** The construction of a continuously revisable global world model with explicit evidence provenance, temporal consistency, and independently verifiable state transitions.

---

## 2. Central Research Question

**How can an artificial intelligence system maintain a historically traceable, continuously updated computational representation of a complex external world despite incomplete observations, contradictory information, changing conditions, and uncertainty?**

Answer: By separating three independent representations — **external reality**, **observation**, and **understanding** — with explicit transformations between them, and by enforcing deterministic governance over all changes to the understanding.

---

## 3. Intended Users

- Independent researchers — studying global developments over time
- Intelligence analysts — tracking events, hypotheses, and contradictions
- Economists — monitoring policy decisions, indicators, and outcomes
- Journalists — verifying claims against evidence and identifying omitted context
- Scientific researchers — tracking claims, replication, and consensus change
- Policy analysts — connecting decisions to measurable outcomes
- AI developers — building systems on an evidence-grounded, temporally consistent world model
- Organizations requiring evidence-based situational awareness

The initial implementation is a research and development platform. Commercial applications may emerge from its underlying infrastructure.

---

## 4. Scope

### 4.1 Global Scope

Reality Engine models interconnected global systems. The initial domain taxonomy:

| Domain | Initial Coverage |
|---|---|
| Geopolitical systems | States, governments, alliances, conflicts, diplomacy |
| Economic systems | Production, trade, employment, prices, debt |
| Financial systems | Markets, instruments, central banking, capital flows |
| Scientific systems | Research, discoveries, theories, replication, retractions |
| Technological systems | Companies, patents, infrastructure, capabilities |
| Environmental systems | Climate, weather, ecosystems, emissions |
| Social & demographic systems | Populations, movements, education, public opinion |
| Military & security systems | Forces, deployments, arms, conflicts, treaties |
| Legal & institutional systems | Courts, legislation, regulatory actions |
| Infrastructure & energy systems | Grids, transport, supply chains, energy production |

### 4.2 Initial Scope

Version 0.1 (Evidence Foundation) focuses on the evidence foundation and a limited set of global information sources.

### 4.3 Non-Goals

See [docs/NON_GOALS.md](docs/NON_GOALS.md) for the complete non-goals document.

---

## 5. Foundational Principles

| ID | Principle | Meaning |
|---|---|---|
| P1 | Evidence preservation | Original observations and source material must remain recoverable. |
| P2 | Provenance | Every factual assertion must have traceable provenance. |
| P3 | Temporal integrity | The system must distinguish when something happened from when it became known. |
| P4 | Revision rather than replacement | New information must revise previous understanding without silently erasing historical interpretations. |
| P5 | Explicit uncertainty | Unknown, disputed, unsupported, and contradicted information must remain distinguishable. |
| P6 | Source independence | Repeated reporting derived from a common origin must not be counted as independent corroboration. |
| P7 | Domain separation | Specialized world models must retain their own schemas while sharing a common ontology. |
| P8 | Deterministic governance | Language models may propose changes but must not directly control authoritative world-state transitions. |
| P9 | Reproducibility | Significant conclusions and revisions must be reconstructable from recorded inputs, model configurations, and processing versions. |
| P10 | Model independence | The knowledge infrastructure must not depend on a particular commercial LLM or inference provider. |
| P11 | Historical accountability | Previous interpretations, predictions, and errors must remain available for evaluation. |
| P12 | Observability awareness | The system must represent the limitations of its information environment. |

---

## 6. System Architecture (Seven Layers)

| Layer | Name | Responsibility |
|---|---|---|
| 1 | External Reality | Environment being modeled |
| 2 | Observation Engine | Collect information |
| 3 | Evidence Engine | Transform documents into observations and claims |
| 4 | World Model | Maintain the structured representation |
| 5 | Revision Engine | Determine how new evidence affects existing understanding |
| 6 | Intelligence Engine | Analytical capabilities (six specialized agents) |
| 7 | World Interface | Expose the system to users |

---

## 7. Primary Data Objects

The system uses five distinct object types that are never interchangeable:

| Object | Meaning | Example |
|---|---|---|
| **Observation** | Something directly measured or recorded | A CPI reading of 3.2% released this week |
| **Claim** | An assertion about the world | "Inflation is increasing" |
| **Evidence** | Information supporting or challenging a claim | Government data, a research paper, a contradictory report |
| **Hypothesis** | An explanation for observed events | "Inflation will remain elevated because energy prices rose" |
| **Conclusion** | An assessment derived from available evidence | "The policy is not yet supported as effective" |

---

## 8. Core Technology Stack

| Component | Technology |
|---|---|
| Core application | Python |
| Database | SQLite (WAL mode) |
| Full-text search | FTS5 |
| Data validation | Pydantic |
| API | FastAPI |
| Background processing | Python task workers |
| Interface | React and TypeScript |
| Visualization | D3.js or equivalent |
| Local inference | Ollama / llama.cpp |
| Embeddings | Local embedding models |
| Testing | pytest |
| Schema migrations | Versioned migration framework |

---

## 9. Repository Structure

```
reality-engine/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── pyproject.toml
├── package.json
├── .env.example
├── .gitignore
│
├── docs/           # Comprehensive documentation (see docs/README.md)
├── schemas/        # Versioned JSON Schemas
├── core/           # World model, revision, temporal, ontology, events
├── observation/    # Source adapters, collectors, scheduler, normalization
├── evidence/       # Extraction, claims, provenance, lineage, contradiction
├── intelligence/   # Analyst, skeptic, historian, forecaster, verifier, integrator
├── domains/        # Geopolitical, economic, financial, scientific, etc.
├── governance/     # Policies, permissions, frozen spine, audit
├── storage/        # SQLite, documents, indexes, migrations, projections
├── api/            # Routes, schemas, services
├── frontend/       # React/TypeScript UI
├── evaluation/     # Datasets, tests, benchmarks
├── scripts/        # Utility scripts
├── migrations/     # Database migrations
└── tests/          # Unit and integration tests
```

---

## 10. Documentation

This repository contains comprehensive documentation organized into:

| Category | Documents |
|---|---|
| **Project foundation** | README.md, PROJECT_SPECIFICATION.md, PROJECT_CONTEXT_AND_DECISIONS.md, PROJECT_ROADMAP.md, REQUIREMENTS.md, DEFINITIONS_AND_TERMINOLOGY.md, NON_GOALS.md |
| **Architecture** | ARCHITECTURE.md, SYSTEM_COMPONENTS.md, DATA_FLOW.md, EVENT_ARCHITECTURE.md, STORAGE_ARCHITECTURE.md, LOCAL_FIRST_ARCHITECTURE.md, MODEL_ABSTRACTION.md, ARCHITECTURE_DECISIONS.md |
| **Ontology and knowledge representation** | ONTOLOGY.md, ENTITY_MODEL.md, EVENT_MODEL.md, RELATIONSHIP_MODEL.md, OBSERVATION_MODEL.md, CLAIM_MODEL.md, EVIDENCE_MODEL.md, HYPOTHESIS_MODEL.md, FORECAST_MODEL.md, DOMAIN_MODELS.md, ONTOLOGY_EVOLUTION.md |
| **Temporal architecture** | TEMPORAL_MODEL.md, BITEMPORAL_DATA.md, HISTORICAL_RECONSTRUCTION.md, TIME_SEMANTICS.md |
| **Revision engine** | REVISION_MODEL.md, REVISION_STATE_MACHINE.md, DEPENDENCY_GRAPH.md, CONTRADICTION_DETECTION.md, BELIEF_REVISION.md, REVISION_VALIDATION.md, REVISION_TRANSACTION_MODEL.md |
| **Evidence and provenance** | PROVENANCE_MODEL.md, SOURCE_LINEAGE.md, SOURCE_INDEPENDENCE.md, SOURCE_QUALITY.md, EVIDENCE_ASSESSMENT.md, INFORMATION_RELIABILITY.md |
| **Intelligence architecture** | INTELLIGENCE_ARCHITECTURE.md, AGENT_ROLES.md, AGENT_CONTRACTS.md, ANALYST_SPECIFICATION.md, SKEPTIC_SPECIFICATION.md, HISTORIAN_SPECIFICATION.md, FORECASTER_SPECIFICATION.md, VERIFIER_SPECIFICATION.md, SYSTEMS_INTEGRATOR_SPECIFICATION.md, AGENT_ORCHESTRATION.md |
| **Observation and ingestion** | OBSERVATION_ENGINE.md, SOURCE_ADAPTER_SPECIFICATION.md, INGESTION_PIPELINE.md, DOCUMENT_PROCESSING.md, ENTITY_RESOLUTION.md, DEDUPLICATION.md, COLLECTION_SCHEDULER.md, INITIAL_DATA_SOURCES.md |
| **Active observation and uncertainty** | EPISTEMIC_MODEL.md, UNCERTAINTY_MODEL.md, OBSERVABILITY_MODEL.md, KNOWLEDGE_GAPS.md, ACTIVE_OBSERVATION.md, VALUE_OF_INFORMATION.md |
| **Security and governance** | SECURITY_MODEL.md, THREAT_MODEL.md, FROZEN_SPINE_INTEGRATION.md, PERMISSION_MODEL.md, AUDIT_MODEL.md, PROMPT_INJECTION_DEFENSE.md, DATA_PRIVACY.md |
| **Database and APIs** | DATABASE_SCHEMA.md, DATABASE_MIGRATIONS.md, DATABASE_INDEXING.md, API_SPECIFICATION.md, API_VERSIONING.md, API_ERROR_MODEL.md |
| **Interface** | USER_INTERFACE.md, WORLD_OVERVIEW.md, WORLD_EXPLORER.md, REALITY_TIMELINE.md, CHANGE_INTELLIGENCE.md, EVIDENCE_EXPLORER.md, ASK_REALITY.md, SYSTEM_OBSERVATORY.md |
| **Evaluation** | EVALUATION_FRAMEWORK.md, BENCHMARKS.md, REVISION_BENCHMARKS.md, TEMPORAL_BENCHMARKS.md, PROVENANCE_BENCHMARKS.md, SOURCE_LINEAGE_BENCHMARKS.md, FORECAST_EVALUATION.md, HINDSIGHT_CONTAMINATION_TESTS.md, ADVERSARIAL_TESTING.md |
| **Development and operations** | DEVELOPMENT_GUIDE.md, REPOSITORY_STRUCTURE.md, CODING_STANDARDS.md, TESTING_STRATEGY.md, OBSERVABILITY_AND_MONITORING.md, DEPLOYMENT.md, BACKUP_AND_RECOVERY.md, OPERATIONS_MANUAL.md, CONTRIBUTING.md |
| **Implementation readiness** | IMPLEMENTATION_PLAN.md, MILESTONES.md, ACCEPTANCE_CRITERIA.md, INITIAL_BACKLOG.md, RESEARCH_REFERENCES.md |

---

## 11. How to Use This Repository

This documentation system is designed so that an independent coding agent can be given the repository and instructed: *"Implement Reality Engine according to these specifications."* The agent should be able to determine:

- What the system is and why it exists.
- How it is structured.
- What each component does.
- What data it stores.
- How data moves through the system.
- How evidence is represented.
- How time is handled.
- How revision works.
- How state transitions are validated.
- How agents interact with the system.
- What permissions they have.
- How the application is tested.
- What constitutes successful implementation.
- What must be implemented first.

The documentation minimizes architectural guesswork during implementation.

---

## 12. License

This document and the accompanying specification are licensed for open research and software architecture. See LICENSE file.
