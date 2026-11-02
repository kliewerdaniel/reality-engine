# Architecture Decision Records

**Reality Engine — Architecture Decision Records (ADRs)**
**Version:** 0.1.1
**Date:** November 1, 2026

This document records the key architecture decisions for Reality Engine. Each decision record contains context, decision, rationale, and consequences.

---

## Decision Classification

Each ADR carries a classification that indicates its maturity and evidentiary basis:

| Classification | Meaning |
|---|---|
| **Established** | Required by the project's fundamental principles. Not materially disputable. |
| **Provisional** | Selected as the initial engineering approach. Sensible and reasoned, but must be demonstrated through implementation. |
| **Experimental** | Needs a prototype and evaluation. The approach may not be adopted. |
| **Deferred** | Intentionally outside the current milestone. Implemented later or not at all. |

**Constraint:** Do not treat a provisional decision as a settled engineering necessity. Mark provisional decisions as such in all dependent documentation.

---

## ADR-001: The Fundamental Object

**Status:** Established

**Classification:** Required by project fundamental principles. The fundamental object is fixed by the project's definition.

**Context:** The system needed a fundamental object to represent the world. Options included: a document, a conversation, an embedding, or a claim about reality supported by evidence, situated in time, and connected to other claims.

**Decision:** The fundamental object is **a claim about reality, supported by evidence, situated in time, and connected to other claims**.

**Rationale:** The project's purpose is not to collect documents or answer questions. It is to construct, maintain, evaluate, and revise a global representation of the world. A claim captures the assertion; evidence supports or challenges it; time situates it; and relationships connect it to other claims.

**Consequences:**

- The data model is built around claims, not documents.
- The system extracts claims from documents.
- Evidence, rather than documents, is the unit of verification.
- The data flow prioritizes claim extraction over document collection.

---

## ADR-002: Five Core Object Types

**Status:** Established

**Classification:** Required by project fundamental principles. Five distinct object types are the core ontology.

**Context:** The system needed to represent different kinds of information. Options included a single generic knowledge object, or distinct objects.

**Decision:** The system uses five distinct object types:

1. Observation — something directly measured or recorded.
2. Claim — an assertion about the world.
3. Evidence — information supporting or challenging a claim.
4. Hypothesis — an explanation for observed events.
5. Conclusion — an assessment derived from available evidence.

**Rationale:** These objects are never interchangeable. A government announcement is an observation; the government's prediction about unemployment is a claim; an economic model's projection is a hypothesis; the assessment of the prediction is a conclusion.

**Consequences:**

- The ontology enforces distinct types.
- Operations treat each type differently.
- Claim type determines how claims are evaluated.

---

## ADR-003: The Seven-Layer Architecture

**Status:** Provisional

**Classification:** Initial organizational choice. Must be demonstrated through implementation.

**Context:** The system needed an organizational structure for its components.

**Decision:** The system is organized into seven logical layers:

| Layer | Name | Responsibility |
|---|---|---|
| 1 | External Reality | Environment being modeled |
| 2 | Observation Engine | Collect information |
| 3 | Evidence Engine | Transform documents into observations and claims |
| 4 | World Model | Maintain the structured representation |
| 5 | Revision Engine | Determine how new evidence affects existing understanding |
| 6 | Intelligence Engine | Provide analytical capabilities |
| 7 | World Interface | Expose the system to users |

**Rationale:** The layers separate concerns: collection, extraction, modeling, revision, analysis, and interface. This separation allows independent development and testing.

**Consequences:**

- New layers can be added.
- Components can be developed and tested independently.
- The interface is distinct from the model.

---

## ADR-004: Modular Monolith

**Status:** Provisional

**Classification:** Initial engineering approach. Microservices deferred until measured requirements justify them.

**Context:** The system required an initial implementation architecture.

**Decision:** The initial architecture is a **modular monolith**.

**Rationale:** Microservices introduce distributed-system complexity (network latency, consistency, failure modes, deployment overhead) before the computational model is proven. A modular monolith keeps the system simple while maintaining explicit subsystem boundaries.

**Consequences:**

- The codebase is a single deployable unit.
- Subsystem boundaries are explicit.
- Components can be separated later if necessary.

---

## ADR-005: SQLite WAL

**Status:** Provisional

**Classification:** Sensible initial choice. Prototype evidence needed before broader adoption.

**Context:** The system needed a primary database.

**Decision:** Use SQLite with WAL (Write-Ahead Logging) mode.

**Rationale:** SQLite is a zero-configuration, local-first database with ACID transactions. WAL mode provides concurrency and crash recovery. Using SQLite avoids the operational complexity of a client-server database.

**Consequences:**

- The system is local-first by default.
- No database server is required.
- The system runs on a modern Apple Silicon workstation with approximately 48 GB unified memory.

---

## ADR-006: Bitemporal Data Model

**Status:** Established

**Classification:** Required by the temporal model. Bitemporal fields are fundamental to the system.

**Context:** The system needed to model time correctly.

**Decision:** Use bitemporal data throughout the system:

| Field | Meaning |
|---|---|
| valid_from | When the information applies to the external world |
| valid_to | When the information ceased to apply |
| recorded_at | When the system recorded the information |
| superseded_at | When the system replaced the information |

**Rationale:** The system must distinguish when something happened from when it became known. Historical reconstruction requires querying the system's understanding at a specific historical knowledge time using only information available at that time.

**Consequences:**

- All time-sensitive objects have bitemporal fields.
- Historical reconstruction is possible but distinct from current understanding of the past.
- The database uses proper timestamp types and interval semantics.

---

## ADR-007: Evidence-Centric Revision Engine

**Status:** Provisional

**Classification:** Central subsystem. Must be demonstrated through the evidence foundation.

**Context:** The system needed a way to revise its understanding.

**Decision:** Implement a revision engine that is evidence-centric, dependency-aware, and governed by deterministic validation.

**Rationale:** Most knowledge systems are optimized for ingestion and retrieval. Reality Engine should be optimized for maintaining a coherent understanding despite changing evidence. The revision engine must:

- Identify affected claims.
- Traverse dependency graphs.
- Generate and validate proposals.
- Commit atomically.
- Preserve historical versions.

**Consequences:**

- The revision engine is the central subsystem.
- All changes require validation.
- Historical versions are preserved.
- Revisions are recorded as events.

---

## ADR-008: Six Specialized Agents

**Status:** Experimental

**Classification:** Needs prototype and evaluation. The six-agent architecture is not yet proven.

**Context:** The system needed intelligence agents.

**Decision:** Implement six specialized, task-driven agents:

| Agent | Role |
|---|---|
| Analyst | Interpret observations, extract relationships, propose hypotheses |
| Skeptic | Search for contradictions, missing evidence, alternative explanations |
| Historian | Connect current events to historical precedents |
| Forecaster | Generate explicitly testable predictions |
| Verifier | Check provenance, evidence relationships, temporal consistency, schema validity |
| Systems Integrator | Coordinate revision proposals, update affected projections |

**Rationale:** Specialized agents are more effective than a single general agent. Each agent has a specific computational responsibility. The agents do not vote on what is true; the evidence model and verification mechanisms determine what can be concluded.

**Consequences:**

- Agents are invoked when tasks require them, not continuously.
- Routine extraction uses inexpensive local models.
- More capable models are reserved for difficult interpretation and revision.
- Agents never write authoritative world-state records directly.

---

## ADR-009: Evidence Preservation

**Status:** Established

**Classification:** Required by the evidence-preservation principle.

**Context:** The system needed to preserve evidence.

**Decision:** The system must preserve original observations and source material immutably. Evidence is never overwritten. Interpretations are versioned. Revisions are recorded as events.

**Rationale:** The system must never confuse its understanding of reality with reality itself. If an article is corrected, both the original and corrected versions are preserved. If an interpretation changes, the earlier interpretation is preserved and explained.

**Consequences:**

- The evidence store is append-only.
- The audit ledger is append-only.
- Historical versions are recoverable.
- Revisions are recorded as events.

---

## ADR-010: Source Independence Tracking

**Status:** Established

**Classification:** Required by the source-independence principle. Distinguishes publication diversity from evidentiary independence.

**Context:** The system needed to measure the independence of sources.

**Decision:** The system must track source lineage and distinguish publication diversity from evidentiary independence.

**Rationale:** Without source independence tracking, the system could mistake five repetitions of a claim from one press release for five independent confirmations. The system must preserve publication diversity separately from evidentiary independence.

**Consequences:**

- A source lineage graph is maintained.
- Source independence classifications are stored (Independent, Shared Origin, Partially Dependent, Unknown, Not Applicable).
- Evidence assessment accounts for source independence.

---

## ADR-011: Multidimensional Epistemic Model

**Status:** Established

**Classification:** Required by the dimensional uncertainty principle. No universal confidence score.

**Context:** The system needed to represent uncertainty.

**Decision:** Do not assign one confidence score to every claim. Instead, use a multidimensional epistemic representation:

- Source reliability
- Directness
- Corroboration
- Temporal validity
- Measurement quality
- Interpretation
- Contradiction
- Completeness

**Rationale:** A single confidence score conceals important uncertainty. A claim about military spending has different uncertainty dimensions than a measurement of inflation. Each dimension must be stored independently.

**Consequences:**

- Claims carry multiple epistemic dimensions.
- Confidence estimates are optional and methodology must be explicit.
- Bayesian updating is used only where defensible.

---

## ADR-012: Local-First Technology Stack

**Status:** Provisional

**Classification:** Initial technology stack. Local-first by default; cloud deferred.

**Context:** The system needed a technology stack.

**Decision:** Use:

| Component | Technology |
|---|---|
| Core application | Python |
| Database | SQLite (WAL) |
| Full-text search | FTS5 |
| Data validation | Pydantic |
| API | FastAPI |
| Background processing | Python task workers |
| Interface | React and TypeScript |
| Visualization | D3.js or equivalent |
| Local inference | Ollama / llama.cpp |
| Embeddings | Local embedding models |
| Optional performance components | Rust |
| Testing | pytest |

**Rationale:** The stack matches the local-first philosophy. SQLite provides local, ACID storage. Ollama and llama.cpp provide local inference. Pydantic provides schema validation. FastAPI provides the API. React and TypeScript provide the interface.

**Consequences:**

- The system is local-first.
- The system does not depend on a cloud API.
- The system is model-independent through a common model interface.

---

## ADR-013: No LLM as World Model

**Status:** Established

**Classification:** Required by the deterministic governance principle. LLMs propose; deterministic systems control.

**Context:** The system needed a clear boundary between the world model and model-generated proposals.

**Decision:** Make the world model a deterministic, versioned computational system that LLM-generated proposals interact with. The LLM does not control authoritative state transitions.

**Rationale:** If the LLM is the world model, changing the model destroys the knowledge infrastructure. The world model must remain stable. LLMs can propose changes; deterministic systems control accepted state transitions.

**Consequences:**

- The world model is versioned and deterministic.
- All state transitions are validated.
- LLMs propose, but the Frozen Spine controls.
- The system is replaceable.

---

## ADR-014: Domain-Specific World Models

**Status:** Provisional

**Classification:** Initial architectural choice. Domains should be demonstrated through implementation.

**Context:** The system needed a model of the world.

**Decision:** Create a collection of domain models connected through a common world ontology.

**Rationale:** A single enormous undifferentiated knowledge graph is not appropriate. The system should have specialized world models for each domain, sharing a common ontology. Each domain maintains its own specialized observations and relationships.

**Consequences:**

- The ontology defines common object types.
- Domains extend the common ontology.
- Cross-domain dependencies are traversable.

---

## ADR-015: Task-Driven Agent Execution

**Status:** Provisional

**Classification:** Initial execution approach. Task scheduling must be demonstrated.

**Context:** The system needed to execute intelligence agents.

**Decision:** Execute agents when tasks require them. Do not run every agent continuously.

**Rationale:** Running all agents continuously would be inefficient. The scheduler should use task complexity, uncertainty, novelty, and resource cost to determine which agents are needed.

**Consequences:**

- A deterministic scheduler decides which operation is necessary.
- Routine extraction uses inexpensive local models.
- More capable reasoning models are reserved for difficult tasks.

---

## ADR-016: Event Sourcing and Append-Only Audit

**Status:** Provisional

**Classification:** Initial audit approach. Event sourcing is the chosen implementation pattern.

**Context:** The system needed audit and history.

**Decision:** Implement event sourcing with an append-only audit ledger.

**Rationale:** The system must preserve history and be auditable. Events must be append-only. Corrections require new events. A hash chain may detect alteration of the audit history. External checkpoints or independently stored signatures may be introduced later.

**Consequences:**

- All significant state transitions produce audit events.
- Events are append-only.
- Replay is supported.
- Reproducibility is preserved.

---

## ADR-017: Deeply Layered Time

**Status:** Established

**Classification:** Required by the temporal model. Historical reconstruction requires multiple time dimensions.

**Context:** The system needed to distinguish when something happened from when it became known.

**Decision:** Differentiate at least two kinds of time: world time (valid time) and knowledge time (transaction time). The system must query historical knowledge and current understanding of the past as distinct operations.

**Rationale:** The system must answer:

- "What did Reality Engine believe about the economy on October 15, based only on information available at that time?"
- "What does the system currently understand about what was true at that historical date?"

These are different questions.

**Consequences:**

- All time-sensitive objects have bitemporal fields.
- Historical reconstruction is a distinct capability.

---

## ADR-018: Active World Observation

**Status:** DEFERRED

**Classification:** Deferred. Intentionally outside current milestone.

**Context:** The system should identify gaps in its understanding and determine which additional observations would most improve its understanding.

**Decision:** Implement a preliminary version of an observation priority heuristic, but treat it as an initial heuristic, not a statistically validated formula.

**Rationale:** The observation priority heuristic is a starting point:

```text
Observation Priority =
    Potential Information Value
  × Uncertainty Reduction
  × Domain Relevance
  × Time Sensitivity
  / Collection Cost
```

The system should eventually measure whether acquiring the suggested information actually improves its world model.

**Consequences:**

- The system can identify knowledge gaps.
- Observation priority is initially a heuristic.
- Active collection is bounded by approved public sources.

---

## ADR-019: Initial Source Set

**Status:** Provisional

**Classification:** Initial source set. Must be validated through the collection pipeline.

**Context:** The system needed initial sources.

**Decision:** Start with a small set of sources:

| Domain | Initial Sources |
|---|---|
| News and global events | GDELT, RSS, official news organization feeds, government press releases |
| Economics | FRED, World Bank, IMF, OECD |
| Science | Crossref, OpenAlex, arXiv |
| Environment | NASA, NOAA, Copernicus |
| Technology | GitHub API, public software release feeds, patent databases |
| Geopolitical and institutional information | United Nations, World Trade Organization, government publications |

**Rationale:** Starting with a small set of sources allows the team to validate the source adapters, the extraction pipeline, and the revision engine without being overwhelmed by volume.

**Consequences:**

- The first milestone covers RSS and a few API sources.
- Additional sources are added as adapters are validated.
- Source-specific metadata is recorded.

---

## ADR-020: Benchmarks Before Implementation

**Status:** Provisional

**Classification:** Benchmarks guide implementation. Validation is a work in progress.

**Context:** The system needed a way to measure success.

**Decision:** Establish benchmarks before building too much intelligence into the system.

**Rationale:** The system must be evaluated on the correctness of its knowledge operations, not the fluency of its generated explanations. A convincing answer is not necessarily a correct answer.

**Consequences:**

- Extraction benchmarks exist.
- Provenance benchmarks exist.
- Temporal benchmarks exist.
- Revision benchmarks exist.
- Source independence benchmarks exist.
- Forecast calibration benchmarks exist.
- Hindsight contamination tests exist.

---

## ADR-021: Observability Model

**Status:** Provisional

**Classification:** Initial observability model. Should be demonstrated through system operation.

**Context:** The system needed to represent the limitations of its own information environment.

**Decision:** Implement an observability model that represents the limitations of the system's information environment.

**Rationale:** The system must know what it cannot observe. The system must distinguish between confirmed observations, current interpretations, potential consequences, unresolved questions, and unknown states. Without this model, the system would confuse lack of evidence with evidence of absence.

**Consequences:**

- Each domain has an observability profile.
- The system tracks source coverage, geographic coverage, temporal coverage, update frequency, missing data, and data quality.
- The system can identify knowledge gaps.

---

## ADR-022: Modular Deployment

**Status:** Provisional

**Classification:** Initial deployment pattern. Microservices deferred until measured requirements justify them.

**Context:** The system needed a deployment strategy.

**Decision:** Deploy as a modular monolith initially. There is no reason to introduce distributed services, message brokers, and operational complexity before the actual computational model is proven.

**Rationale:** The modular monolith provides explicit subsystem boundaries without distributed-system complexity. Components can be separated later if measured requirements justify it.

**Consequences:**

- The system is a single deployable unit.
- Subsystem boundaries are explicit.
- Services are introduced only when necessary.

---

## ADR-023: Model Abstraction Layer

**Status:** Established

**Classification:** Required by the model-independence principle. Models are pluggable, not hardcoded.

**Context:** The system needed to integrate models.

**Decision:** All inference passes through a common model abstraction layer. The system must not depend directly on a single provider's proprietary request format.

**Rationale:** Model independence ensures that the knowledge infrastructure does not depend on a particular commercial LLM or inference provider. The system can swap models without changing the data model.

**Consequences:**

- The `ModelProvider` interface is the only dependency on models.
- Tasks are mapped to model capabilities.
- The system can run several models against the same evidence.

---

## ADR-024: Versioned Ontology

**Status:** DEFERRED

**Classification:** Deferred. Versioned ontology evolution intentionally outside current milestone.

**Context:** The system needed to evolve the ontology.

**Decision:** Use versioned ontology schemas and explicit migration events. Ontology evolution must not invalidate existing records.

**Rationale:** Domains evolve. New entity types and relationships are introduced. The ontology must evolve without invalidating historical records.

**Consequences:**

- Ontology versions are tracked.
- Migration events are recorded.
- Historical records remain valid.

---

## ADR-025: No Universal Confidence Score

**Status:** Established

**Classification:** Required by the dimensional uncertainty principle. No universal score.

**Context:** The system needed to represent uncertainty.

**Decision:** Do not collapse evidence quality into one universal reliability score. Domain-specific scoring may be introduced later, with explicit methodology.

**Rationale:** A single universal score conceals the multidimensional nature of evidence quality. Each dimension (source reliability, directness, corroboration, temporal validity, measurement quality, interpretation, contradiction, completeness) must be stored independently.

**Consequences:**

- Evidence quality is multidimensional.
- Domain-specific scoring is deferred.

---

## ADR-026: Initial Implementation

**Status:** Provisional

**Classification:** Implementation sequence. The first proof is the evidence foundation, not orchestration.

**Context:** The system needed an initial implementation plan.

**Decision:** For the first coding session, implement only:

1. Repository foundation.
2. Core ontology.
3. SQLite database.
4. Source registry.
5. Document ingestion.
6. Content hashing.
7. Observation and claim schemas.
8. Provenance storage.
9. Basic API.
10. Unit tests.

**Rationale:** The first meaningful demonstration should be: ingest one document, extract several claims, connect them to their source passages, and retrieve those claims with complete provenance. Then ingest a second document that challenges one of the claims. Demonstrate that the system preserves both documents and produces an explicit revision proposal without silently changing its previous understanding.

**Consequences:**

- The first milestone is the evidence foundation.
- The system does not start with an elaborate dashboard.
- The system does not start with multi-agent orchestration or a large ingestion pipeline.

---

## ADR-027: Deferred Distributed Execution

**Status:** DEFERRED

**Classification:** Deferred. Distributed execution intentionally outside current milestone. Embedded task processing only.

**Context:** The system needed to decide when to introduce distributed execution.

**Decision:** Defer distributed execution until measured bottlenecks justify it. Initial recommendation: embedded task processing.

**Rationale:** Distributed systems introduce operational complexity. The specification explicitly recommends a modular monolith initially. Distributed execution is justified only when measured requirements demand it.

**Consequences:**

- The system remains a modular monolith.
- Services are introduced when bottlenecks are measured.
