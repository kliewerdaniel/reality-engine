# Requirements

**Reality Engine — Requirements Document**
**Version:** 0.1.0
**Date:** November 1, 2026
**Status:** Review draft

This document defines the functional and non-functional requirements for Reality Engine.

---

## 1. Requirements Identification

**REQUIREMENT CATALOG**
All requirements are assigned stable identifiers:

| Prefix | Meaning |
|---|---|
| REQ-001 | Project-level requirement |
| REQ-002 | Architecture requirement |
| REQ-003 | Data model requirement |
| REQ-004 | Temporal requirement |
| REQ-005 | Revision requirement |
| REQ-006 | Evidence requirement |
| REQ-007 | Provenance requirement |
| REQ-008 | Agent requirement |
| REQ-009 | Observation requirement |
| REQ-010 | Intelligence requirement |
| REQ-011 | Security requirement |
| REQ-012 | API requirement |
| REQ-013 | Evaluation requirement |
| REQ-014 | Operational requirement |

---

## 2. Functional Requirements

### 2.1 Core Object Requirements

| ID | Requirement | Priority |
|---|---|---|
| REQ-001 | The system must represent the five core object types: Observation, Claim, Evidence, Hypothesis, Conclusion | MUST |
| REQ-002 | The system must distinguish Observation from Claim, Evidence, Hypothesis, and Conclusion | MUST |
| REQ-003 | The system must distinguish the three conceptual layers: external reality, observation, understanding | MUST |
| REQ-004 | The system must maintain immutable evidence records | MUST |
| REQ-005 | The system must maintain versioned interpretations | MUST |

### 2.2 Temporal Requirements

| ID | Requirement | Priority |
|---|---|---|
| REQ-006 | The system must distinguish valid time (when something happened) from transaction time (when it became known) | MUST |
| REQ-007 | The system must support historical reconstruction queries | MUST |
| REQ-008 | The system must answer: "What did the system understand at a historical date?" | MUST |
| REQ-009 | The system must answer: "What does the system currently understand about what was true at a historical date?" | MUST |
| REQ-010 | The system must preserve all historical versions intact | MUST |
| REQ-011 | The system must enforce interval semantics using proper timestamp types | MUST |

### 2.3 Revision Requirements

| ID | Requirement | Priority |
|---|---|---|
| REQ-012 | The system must identify affected claims when new evidence arrives | MUST |
| REQ-013 | The system must traverse dependency graphs to find downstream impacts | MUST |
| REQ-014 | The system must not automatically reverse all downstream conclusions | MUST |
| REQ-015 | The system must preserve unaffected claims | MUST |
| REQ-016 | The system must record every revision as an audit event | MUST |
| REQ-017 | The system must support reversible revisions where applicable | MUST |
| REQ-018 | The system must support correction of temporal scope | MUST |
| REQ-019 | The system must support entity reassignment | MUST |
| REQ-020 | The system must support hypothesis invalidation | MUST |

### 2.4 Evidence Requirements

| ID | Requirement | Priority |
|---|---|---|
| REQ-021 | The system must preserve original documents and observations | MUST |
| REQ-022 | The system must extract claims from documents | MUST |
| REQ-023 | The system must connect claims to source passages | MUST |
| REQ-024 | The system must support SUPPORTS, CONTRADICTS, QUALIFIES, DERIVED_FROM, REPEATS, ATTRIBUTED_TO, SUPERSEDES, CORROBORATES relationships | MUST |
| REQ-025 | The system must track source lineage | MUST |
| REQ-026 | The system must distinguish publication diversity from evidentiary independence | MUST |
| REQ-027 | The system must assess evidence quality as multidimensional | MUST |
| REQ-028 | The system must not silently rewrite evidence | MUST |

### 2.5 Intelligence Requirements

| ID | Requirement | Priority |
|---|---|---|
| REQ-029 | The system must include an Analyst agent that proposes interpretations and hypotheses | MUST |
| REQ-030 | The system must include a Skeptic agent that challenges interpretations | MUST |
| REQ-031 | The system must include a Historian agent that retrieves historical context | MUST |
| REQ-032 | The system must include a Forecaster agent that generates testable predictions | MUST |
| REQ-033 | The system must include a Verifier agent that checks provenance and consistency | MUST |
| REQ-034 | The system must include a Systems Integrator agent that coordinates revisions | MUST |
| REQ-035 | The system must not allow agents to vote on what is true | MUST |
| REQ-036 | The system must validate all agent proposals before they affect world state | MUST |

### 2.6 Observation Requirements

| ID | Requirement | Priority |
|---|---|---|
| REQ-037 | The system must support source adapters for multiple source types | MUST |
| REQ-038 | The system must deduplicate identical content from multiple URLs | MUST |
| REQ-039 | The system must maintain collection checkpoints | MUST |
| REQ-040 | The system must support incremental collection | MUST |
| REQ-041 | The system must support scheduled collection | MUST |
| REQ-042 | The system must detect and report adapter failures | MUST |

### 2.7 Evaluation Requirements

| ID | Requirement | Priority |
|---|---|---|
| REQ-043 | The system must support extraction accuracy benchmarks | MUST |
| REQ-044 | The system must support provenance accuracy benchmarks | MUST |
| REQ-045 | The system must support temporal integrity benchmarks | MUST |
| REQ-046 | The system must support revision accuracy benchmarks | MUST |
| REQ-047 | The system must support source independence benchmarks | MUST |
| REQ-048 | The system must support contradiction detection benchmarks | MUST |
| REQ-049 | The system must support forecast calibration benchmarks | MUST |
| REQ-050 | The system must support hindsight contamination tests | MUST |

---

## 3. Non-Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| NFR-001 | The system must run on a modern Apple Silicon workstation with approximately 48 GB unified memory | MUST |
| NFR-002 | The system must be local-first (local inference, local storage, replaceable model providers) | MUST |
| NFR-003 | The system must not depend on a particular commercial LLM or inference provider | MUST |
| NFR-004 | The core domain model must not depend on the frontend | MUST |
| NFR-005 | The revision engine must not depend on a particular agent implementation | MUST |
| NFR-006 | The world model must not depend on the availability of an external cloud API | MUST |
| NFR-007 | All significant state transitions must produce audit events | MUST |
| NFR-008 | Audit events must be append-only | MUST |
| NFR-009 | The system must support historical reconstruction within acceptable latency | SHOULD |
| NFR-010 | The system must support idempotent processing | MUST |
| NFR-011 | The system must support reproducibility with documented model and prompt versions | MUST |
| NFR-012 | The system must be deployable as a modular monolith initially | MUST |
| NFR-013 | The system must support separation into services after measured bottlenecks | MUST |

---

## 4. Acceptance Test Mapping

| Requirement | Test |
|---|---|
| REQ-001 to REQ-005 | docs/IMPLEMENTATION_PLAN.md — Milestone 0 |
| REQ-006 to REQ-011 | docs/IMPLEMENTATION_PLAN.md — Milestone 2 |
| REQ-012 to REQ-020 | docs/IMPLEMENTATION_PLAN.md — Milestone 3 |
| REQ-021 to REQ-028 | docs/IMPLEMENTATION_PLAN.md — Milestone 1 |
| REQ-029 to REQ-036 | docs/IMPLEMENTATION_PLAN.md — Milestone 4 |
| REQ-037 to REQ-042 | docs/IMPLEMENTATION_PLAN.md — Milestone 1 |
| REQ-043 to REQ-050 | docs/Evaluation |

---

## 5. Usage Scenarios

### Scenario 1: Tracking a Policy Decision

1. The system ingests a government announcement.
2. It extracts the claim "Policy X will reduce unemployment."
3. It connects the claim to the source passage and documents the publication time.
4. Six months later, it ingests employment data.
5. It creates a new observation and evaluates whether the original claim is supported.
6. It generates a revision proposal, which is validated and committed or rejected.
7. The user can reconstruct what the system believed at any point in time.

### Scenario 2: Conflicting Reports

1. Two sources report different values for the same economic indicator.
2. The system records both observations with their source provenance.
3. It creates a contradictory-evidence relationship.
4. It marks the claim as CONTESTED.
5. It triggers reassessment of dependent hypotheses.
6. The user can inspect both evidence streams and the resulting assessment.

---

## 6. Out of Scope (Deferred)

| Item | Deferral Reason |
|---|---|
| Mobile applications | Initial focus is the core data model and API |
| Real-time streaming ingestion | Initial sources are batch (RSS, APIs) |
| Commercial deployment | Initial implementation is a research platform |
| Distributed execution | Only after measured bottlenecks justify it |
| Graph database migration | Relational tables are sufficient initially |
