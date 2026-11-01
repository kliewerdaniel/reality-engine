# Project Roadmap

**Reality Engine — Development Roadmap**
**Version:** 0.1.0
**Date:** November 1, 2026
**Status:** Documentation phase

This roadmap is organized around proving increasingly ambitious capabilities, rather than building every subsystem simultaneously.

---

## 0. Architecture and Ontology (Milestone 0)

**Goal:** Establish the foundational data model and governance rules before any information enters the system.

### Deliverables

- [ ] Final ontology specification (common ontology + domain schemas)
- [ ] Core object definitions (Entity, Event, Observation, Claim, Evidence, Relationship, Hypothesis, Forecast, Conclusion)
- [ ] Database schema (SQLite DDL with foreign keys, indexes, constraints)
- [ ] Temporal model (bitemporal records, interval semantics)
- [ ] Event model (event registry, event types)
- [ ] Source adapter interface specification
- [ ] Revision state machine specification
- [ ] Initial architecture decision records
- [ ] Research references (W3C PROV, event sourcing, bitemporal modeling)
- [ ] Verification of object representation without LLM dependency

### Acceptance Criteria

- All core objects can be represented without depending on an LLM.
- The ontology is stable enough to define a database schema.
- The temporal model distinguishes valid time from transaction time.
- The revision state machine is defined with explicit states and transitions.
- Source adapter interfaces are documented and testable.
- Architecture decision records exist for the foundational decisions.

### Complexity

- High (foundational)
- Est. effort: 3-4 weeks

---

## 1. Reality Engine 0.1 — Evidence Foundation

**Goal:** A user can ingest a document, inspect extracted claims, and trace every accepted claim to the original document.

### Deliverables

- [ ] SQLite database
- [ ] Source registry
- [ ] RSS ingestion (initial source adapter)
- [ ] Initial API ingestion (one additional source type)
- [ ] Document archive (content hashing, storage)
- [ ] Claim extraction (structured-output extraction pipeline)
- [ ] Entity extraction (entity resolution against registry)
- [ ] Provenance records (source → document → claim)
- [ ] Basic search (FTS5)
- [ ] Core API endpoints (sources, documents, observations, claims)
- [ ] Unit tests (extraction accuracy, provenance coverage)

### Acceptance Criteria

- A user can ingest a document through the system.
- The system extracts claims from the document.
- Every accepted claim can be traced back to the original document.
- The user can inspect the full provenance chain.
- The system is idempotent — reprocessing the same document does not create duplicates.
- The API returns claims with source references and timestamps.

### Complexity

- Medium
- Est. effort: 4-6 weeks

---

## 2. Reality Engine 0.2 — Temporal World Model

**Goal:** The system can reconstruct both historical knowledge and current understanding of historical conditions.

### Deliverables

- [ ] Bitemporal storage design (valid time + transaction time)
- [ ] Historical state snapshots
- [ ] Historical query interface
- [ ] Temporal validation rules
- [ ] Time-sematics documentation
- [ ] Historical reconstruction tests
- [ ] World-state version management

### Acceptance Criteria

- The system can answer: "What did the system understand about the world at a particular historical date?"
- The system can answer: "What does the system currently understand about what was true at that historical date?"
- These two queries produce distinct, non-interchangeable results.
- Bitemporal records are enforced at the database level.

### Complexity

- Medium
- Est. effort: 3-4 weeks

---

## 3. Reality Engine 0.3 — Revision Engine

**Goal:** A new observation can trigger a controlled revision of affected claims while preserving unaffected state and previous interpretations.

### Deliverables

- [ ] Contradiction detection
- [ ] Source lineage tracking
- [ ] Dependency graph
- [ ] Revision proposals
- [ ] Deterministic validation
- [ ] Transactional state updates
- [ ] Audit history
- [ ] Revision benchmarks
- [ ] Revision state machine tests

### Acceptance Criteria

- A new observation correctly identifies which previous conclusions need reconsideration.
- Affected claims are identified through dependency traversal.
- Unaffected claims are not modified merely because they are connected.
- A revision is atomic (all changes committed or none).
- The revision event is recorded in the audit log.
- Historical versions remain accessible and unchanged.

### Complexity

- High (central subsystem)
- Est. effort: 5-7 weeks

---

## 4. Reality Engine 0.4 — Global Intelligence

**Goal:** Users can investigate a development across multiple domains and inspect the evidence behind each conclusion.

### Deliverables

- [ ] Cross-domain relationship discovery
- [ ] Analyst agent (structured interpretation proposals)
- [ ] Skeptic agent (contradiction, alternative explanation, missing evidence)
- [ ] Historian agent (historical context, precedent)
- [ ] Verifier agent (schema, provenance, temporal consistency checks)
- [ ] Change reports
- [ ] Natural-language querying
- [ ] Agent orchestration specification

### Acceptance Criteria

- Users can investigate a global development and follow the evidence chain.
- The Analyst produces structured proposals with evidence references.
- The Skeptic surfaces contradictions and alternative explanations.
- The Historian retrieves relevant historical context.
- The Verifier checks the internal consistency of proposals.
- The Systems Integrator coordinates and submits validated proposals to the revision engine.

### Complexity

- High
- Est. effort: 6-8 weeks

---

## 5. Reality Engine 0.5 — Predictive Intelligence

**Goal:** Forecasts can be evaluated against actual outcomes without changing their original published probabilities.

### Deliverables

- [ ] Forecast objects and evaluation criteria
- [ ] Outcome collection interface
- [ ] Forecast evaluation pipeline
- [ ] Brier score and proper scoring rule implementation
- [ ] Calibration reporting
- [ ] Historical forecast comparison
- [ ] Forecast benchmarks

### Acceptance Criteria

- A forecast is immutable after publication.
- Corrections require separate records.
- Evaluation results remain historically accessible.
- Forecast performance is measurable against baselines.
- The system distinguishes forecast from outcome.

### Complexity

- Medium
- Est. effort: 3-4 weeks

---

## 6. Reality Engine 1.0 — Global Reality Interface

**Goal:** An independent user can investigate a global development from observation through evidence, interpretation, revision, and outcome.

### Deliverables

- [ ] Interactive global world model
- [ ] Historical timeline interface
- [ ] Evidence explorer
- [ ] Change intelligence interface
- [ ] Forecast explorer
- [ ] Public API
- [ ] World Overview dashboard
- [ ] Ask Reality interface
- [ ] System Observatory

### Acceptance Criteria

- An independent user can follow a global development from original observations through claim extraction, evidence relationships, revision, and final world-state assessment.
- Every change in the model is attributable to a specific revision event.
- Historical reconstruction is possible.
- The system distinguishes current understanding from historical understanding.

### Complexity

- High (full interface)
- Est. effort: 8-12 weeks

---

## 7. Long-Term Research Directions (Milestone 6+)

### Active World Observation

The system identifies gaps in its understanding and determines which additional observations would most improve its understanding.

### Forecasting and Calibration

The system generates predictions and measures whether its probability estimates are calibrated.

### Cross-Domain Relationship Discovery

The system identifies meaningful relationships across different domains without manufacturing causal connections.

---

## 8. Development Phases

| Phase | Focus | Duration |
|---|---|---|
| **Phase A** | Understand (read PDF, extract decisions) | Completed |
| **Phase B** | Challenge (architectural review) | Completed |
| **Phase C** | Establish foundations (architecture decisions) | 3-4 weeks |
| **Phase D** | Formalize (ontology, schemas, DB, API, security) | 6-8 weeks |
| **Phase E** | Document (full repository) | 4-6 weeks |
| **Phase F** | Validate (consistency audit) | 2-3 weeks |
| **Phase G** | Implementation readiness report | 1-2 weeks |

---

## 9. Key Decision Gates

| Gate | Decision Required | Delivered By |
|---|---|---|
| Gate 0 | Architecture and ontology maturity | Milestone 0 |
| Gate 1 | Can the evidence foundation work? | Milestone 1 |
| Gate 2 | Can historical knowledge be reconstructed? | Milestone 2 |
| Gate 3 | Can the revision engine work correctly? | Milestone 3 |
| Gate 4 | Can cross-domain intelligence work? | Milestone 4 |
| Gate 5 | Can forecasts be calibrated? | Milestone 5 |
| Gate 6 | Can the interface support independent investigation? | Milestone 6 |

---

## 10. Release Strategy

Releases are tagged on GitHub. The release pipeline is defined in docs/RELEASE.md and docs/DEPLOYMENT.md.

The recommended approach is a **modular monolith** initially, with separate services introduced only after measured bottlenecks justify them.

### Repository Structure

```
reality-engine/
├── README.md
├── docs/
├── schemas/
├── core/
├── observation/
├── evidence/
├── intelligence/
├── domains/
├── governance/
├── storage/
├── api/
├── frontend/
├── evaluation/
├── scripts/
├── migrations/
└── tests/
```

---

## 11. Success Metrics

| Metric | Target | Measurement |
|---|---|---|
| Evidence foundation | Claims traceable to source | Provenance benchmark |
| Temporal integrity | Historical reconstruction accuracy | Temporal benchmark |
| Revision accuracy | Correctly identified affected claims | Revision benchmark |
| Source independence | No spurious corroboration from replicas | Source-lineage benchmark |
| Forecast calibration | Brier score vs. baseline | Forecast evaluation |
| Hindsight contamination | Zero in controlled tests | Hindsight contamination test |
| Revision auditability | 100% of accepted revisions | Audit benchmark |

---

## 12. References

- docs/PROJECT_SPECIFICATION.md — complete project specification
- docs/ARCHITECTURE.md — system architecture
- docs/DECISIONS/ — architecture decision records
- docs/Evaluation — benchmarks and evaluation methodology
