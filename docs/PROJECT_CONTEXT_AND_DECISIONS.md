# Project Context and Architecture Decisions

**Reality Engine — Project Context and Decisions Document**
**Version:** 0.1.0
**Date:** November 1, 2026
**Status:** Architecture exploration → documentation phase

This document distinguishes, for every element of the project:

- **DECIDED** — an established requirement.
- **PROPOSED** — a recommended architecture decision.
- **ASSUMPTION** — an assumption that should be validated.
- **OPEN QUESTION** — a decision that requires further investigation.
- **DEFERRED** — deliberately postponed.
- **REJECTED** — evaluated and rejected, with rationale.

---

## 1. Project Context Extracted from the Source PDF

### 1.1 The Core Idea

Reality Engine is not a chatbot, a search engine, or a news summarizer. It is a **computational system that maintains an evolving representation of what is happening, what is known, what is believed, what is disputed, and what is changing**.

The fundamental object is not a document, a conversation, or an embedding. It is a **claim about reality, supported by evidence, situated in time, and connected to other claims**.

Key distinction (from PDF p.2):

> The system doesn't need to decide that one source is universally trustworthy. It needs to understand what each source actually establishes.

---

### 1.2 The Five Core Object Types

**DECIDED** — these five object types are foundational and must never be interchangeable:

| Object | Meaning |
|---|---|
| **Observation** | Something directly measured or recorded |
| **Claim** | An assertion about the world |
| **Evidence** | Information supporting or challenging a claim |
| **Hypothesis** | An explanation for observed events |
| **Conclusion** | An assessment derived from available evidence |

Example temporal chain from PDF (p.2-3):

- A government announces a new economic policy → **observation**
- The government says the policy will reduce unemployment → **claim**
- An economic model predicts employment growth → **hypothesis**
- Six months later, employment data becomes available → **observation**
- The engine determines whether the original prediction was supported → **conclusion**

---

### 1.3 The Temporal Dimension

**DECIDED** — the system must distinguish at least two kinds of time:

| Type | Meaning | Example |
|---|---|---|
| **World time** (valid time) | When something happened | The policy took effect October 10 |
| **Knowledge time** (transaction time) | When the system learned about it | The system collected the report on October 13 |

Example from PDF (p.4):

> You could ask: "What did Reality Engine believe about the economy on October 15, based only on information available at that time?"

---

### 1.4 The Architecture

**PROPOSED** — seven-layer architecture:

| Layer | Name | Responsibility |
|---|---|---|
| 1 | External Reality | The environment being modeled (conceptual) |
| 2 | Observation Engine | Collects information |
| 3 | Evidence Engine | Transforms documents into observations and claims |
| 4 | World Model | Maintains the structured representation |
| 5 | Revision Engine | Determines how new evidence affects understanding |
| 6 | Intelligence Engine | Analytical capabilities (agents) |
| 7 | World Interface | Exposes the system to users |

---

### 1.5 The Intelligence Architecture

**PROPOSED** — six specialized, task-driven agents:

| Agent | Role |
|---|---|
| **Analyst** | Extracts meaning, identifies relationships, constructs interpretations, proposes hypotheses |
| **Skeptic** | Searches for contradictions, missing evidence, alternative explanations, unsupported assumptions |
| **Historian** | Connects current events to historical precedents, tracks how previous interpretations changed |
| **Forecaster** | Generates explicitly testable predictions, records conditions for evaluation |
| **Verifier** | Checks source attribution, evidence relationships, temporal consistency, and schema validity |
| **Systems Integrator** | Coordinates revision proposals and updates affected world-state projections |

**DECIDED** — agents do not vote on what is true:

> One important architectural principle: the agents should not vote on what is true. Three LLMs agreeing with each other does not constitute independent evidence.

The underlying evidence model and verification mechanisms determine what can legitimately be concluded.

---

### 1.6 The Revision Engine (The Central Innovation)

**DECIDED** — the revision engine is the primary differentiating subsystem:

> Most knowledge systems are optimized for ingestion and retrieval. Reality Engine should be optimized for maintaining a coherent understanding despite changing evidence.

The revision engine answers five questions when new information arrives:

1. What does this information establish?
2. Which existing claims does it support or challenge?
3. Which relationships or conclusions depend on those claims?
4. What parts of the world model need to change?
5. What should remain unchanged?

**DECIDED** — immutable observations, mutable understanding:

| Layer | Property |
|---|---|
| **Immutable evidence ledger** | What the system received, where it came from, when it received it |
| **Versioned interpretation layer** | What the system currently believes the observations establish |
| **World-state projection** | The current best-supported representation of the world |

---

### 1.7 The Two-Dimensional Time Model

**DECIDED** — bitemporal data throughout the system:

| Field | Meaning |
|---|---|
| **valid_from** | When the information applies to the external world |
| **valid_to** | When the information ceased to apply |
| **recorded_at** | When the system recorded the information |
| **superseded_at** | When the system replaced the information |

Example from PDF (p.18):

> A government changes a regulation on October 10. The change is reported on October 12. Reality Engine collects the report on October 13. Later, on October 20, the government publishes a correction establishing that the regulation actually took effect October 11. The engine should be able to answer both:
> - "What was the regulation on October 15?"
> - "What did Reality Engine know on October 15?"

---

### 1.8 The Epistemic Model

**PROPOSED** — structured epistemic representation. Do not assign one confidence score to every claim.

| Dimension | Question |
|---|---|
| Source reliability | How dependable is the source for this type of information? |
| Directness | Is the evidence direct or secondhand? |
| Corroboration | Are there genuinely independent sources? |
| Temporal validity | Is the information current? |
| Measurement quality | How reliable is the underlying measurement? |
| Interpretation | How much inference is required? |
| Contradiction | What evidence challenges the claim? |
| Completeness | What important information is missing? |

**DECIDED** — evidence statuses (do not collapse into binary):

| Status | Meaning |
|---|---|
| UNASSESSED | Not yet evaluated |
| SUPPORTED | Evidence supports the claim |
| PARTIALLY_SUPPORTED | Some evidence supports, some contradicts |
| CONTESTED | Competing claims exist |
| CONTRADICTED | Evidence directly challenges the claim |
| UNRESOLVED | Insufficient evidence to decide |
| SUPERSEDED | Replaced by a newer version |
| WITHDRAWN | Explicitly withdrawn |

---

### 1.9 Source Independence and Lineage

**DECIDED** — the system must track source lineage:

> Suppose five news organizations report the same event. But all five obtained their information from one government press release. Reality Engine should identify the common origin. Otherwise, it could mistake five repetitions for five independent confirmations.

**PROPOSED** — source independence classifications:

| Classification | Meaning |
|---|---|
| Independent | Genuinely separate observations |
| Shared origin | Common source or dataset |
| Partially dependent | Partially shared origin |
| Unknown | Dependence cannot be determined |
| Not applicable | No relationship exists |

---

### 1.10 The World Model

**DECIDED** — a collection of domain models connected through a common world ontology:

| Model | What it represents |
|---|---|
| Geopolitical | States, governments, alliances, conflicts, diplomacy |
| Economic | Production, trade, employment, prices, debt |
| Scientific | Research, discoveries, theories, replication |
| Technological | Companies, inventions, infrastructure, capabilities |
| Environmental | Climate, ecosystems, weather, resources |
| Social | Demographics, populations, movements, institutions |

**DECIDED** — ultimate ambition:

> An AI system that doesn't merely tell you what it thinks is happening in the world, but can show you how it arrived at that understanding, what could prove it wrong, what changed since yesterday, and what we still don't know.

---

## 2. Architectural Review

### 2.1 Graph vs. State Machines

**DECIDED** — the authoritative relationship model should remain relational initially, with graph projections later:

> The initial recommendation is: SQLite relational tables with graph projections.

Rationale: A well-designed relational representation supports the first implementation and allows the introduction of specialized graph infrastructure when measured requirements justify it.

---

### 2.2 World-State Representation

**PROPOSED** — a world state is:

> [W_t = {E_t, S_t, R_t, C_t, H_t, U_t}]

Where:

| Symbol | Component |
|---|---|
| E | Entities |
| S | State (current observable conditions) |
| R | Relationships |
| C | Claims |
| H | History (events and previous states) |
| U | Uncertainty (unknowns, conflicting evidence, limitations) |

**DECIDED** — the revision function must not merely append information:

> [W{t+1} = F(W_t, O{t+1}, K_t)]

The important part is that F should not simply append information. It must determine what the new information changes.

---

### 2.3 Revision Semantics

**DECIDED** — supported revision outcomes:

| Outcome | Meaning |
|---|---|
| NEW_INFORMATION | New evidence requiring review |
| SUPPORTED | Existing claim is supported |
| PARTIALLY_SUPPORTED | Some evidence supports, some challenges |
| CHALLENGED | Existing claim is challenged |
| CONTRADICTED | Existing claim is contradicted |
| SUPERSEDED | Replaced by a newer version |
| WITHDRAWN | Explicitly withdrawn |
| UNRESOLVED | Cannot be resolved |
| NO_CHANGE | No effect on current understanding |

**PROPOSED** — revision operations:

| Operation | Meaning |
|---|---|
| CREATE | New entity, claim, or hypothesis |
| SUPPORT | Add supporting evidence |
| QUALIFY | Add qualifying conditions |
| CHALLENGE | Add contradictory evidence |
| RETRACT | Remove a claim |
| REPLACE | Swap a claim for a corrected one |
| SUPERSEDE | Mark an older version as replaced |
| CORRECT_TEMPORAL_SCOPE | Fix the valid time range |
| REASSIGN_ENTITY | Change the subject entity |
| INVALIDATE_DEPENDENCY | Remove a dependency edge |
| REASSESS_HYPOTHESIS | Recalculate hypothesis status |

---

### 2.4 Evidence Model

**DECIDED** — the system must distinguish:

| Object | Meaning |
|---|---|
| Source | The origin of information |
| Document | The collected material |
| Observation | What was measured or recorded |
| Claim | What was asserted |
| Evidence | Information supporting or challenging a claim |
| Interpretation | What the system believes the evidence establishes |
| Hypothesis | An explanation for observed events |
| Conclusion | An assessment derived from evidence |
| Forecast | A testable prediction about the future |

**DECIDED** — do not collapse these into a single generic knowledge object.

---

### 2.5 Source Independence

**DECIDED** — the system must represent source dependence explicitly:

| Relationship | Meaning |
|---|---|
| INDEPENDENT | Genuinely separate observations |
| SHARED_ORIGIN | Common source or dataset |
| PARTIALLY_DEPENDENT | Partially shared origin |
| UNKNOWN | Dependence cannot be determined |
| NOT_APPLICABLE | No relationship exists |

---

### 2.6 Causal Reasoning

**DECIDED** — the system must distinguish:

| Relationship Type | Meaning |
|---|---|
| **TEMPORAL** | A happened before B |
| **CORRELATIONAL** | A and B change together |
| **MECHANISTIC** | There is a plausible mechanism connecting them |
| **CAUSAL_HYPOTHESIS** | A may have contributed to B |
| **EXPERIMENTALLY_SUPPORTED** | Evidence from a suitable experiment supports causation |

**DECIDED** — causal relationships require stronger evidence and explicit methodological justification than ordinary associations.

---

### 2.7 Ontology Evolution

**DEFERRED** — the system must be designed to accommodate ontology evolution. Specific strategies (versioned ontology schemas, migration events) are documented in ONTOLOGY_EVOLUTION.md.

---

### 2.8 Knowledge Completeness and Observability

**DECIDED** — each domain should have an observability profile:

| Observability Level | Meaning |
|---|---|
| OBSERVABLE | Fully covered by available data |
| PARTIALLY_OBSERVABLE | Some data exists, gaps remain |
| NOT_DIRECTLY_OBSERVABLE | Cannot be directly observed |
| NOT_YET_COLLECTED | Data may exist but has not been gathered |
| UNKNOWN_LIMITATIONS | Limitations are not yet characterized |

**PROPOSED** — observability metrics:

| Metric | Meaning |
|---|---|
| Source coverage | Which sources are active and how frequently |
| Geographic coverage | Which regions are represented |
| Temporal coverage | Which time periods are represented |
| Update frequency | How often data is refreshed |
| Missing data | What is absent |
| Data quality | How reliable the data is |
| Known reporting delays | Documented latency |
| Entity resolution completeness | How well entities are identified |

---

### 2.9 Active Information Acquisition

**PROPOSED** — an initial heuristic for observation priority:

```text
Observation Priority =
    Potential Information Value
  × Uncertainty Reduction
  × Domain Relevance
  × Time Sensitivity
  / Collection Cost
```

This is an initial heuristic, not a statistically validated formula.

---

### 2.10 Local-First Operation

**DECIDED** — technology stack:

| Component | Technology |
|---|---|
| Core application | Python |
| Database | SQLite (WAL mode) |
| Full-text search | FTS5 |
| Data validation | Pydantic |
| API | FastAPI |
| Background processing | Python task workers |
| Interface | React and TypeScript |
| Localization | Ollama / llama.cpp |
| Alternative inference | llama.cpp |
| Embeddings | Local embedding models |
| Optional performance components | Rust (for hot paths) |
| Testing | pytest |

**DECIDED** — the system must be capable of running on a modern Apple Silicon workstation with approximately 48 GB unified memory.

---

## 3. Unresolved Decisions

The following decisions remain to be resolved through prototypes and benchmarks:

| ID | Decision | Initial Recommendation |
|---|---|---|
| OD-001 | Graph representation | SQLite relational tables with graph projections |
| OD-002 | Event processing | Embedded task processing |
| OD-003 | Belief revision methodology | Hybrid architecture with explicit evidence relationships and deterministic revision rules |
| OD-004 | Ontology evolution | Versioned ontology schemas and explicit migration events |
| OD-005 | Source evaluation | Domain-specific, multidimensional source assessment |
| OD-006 | Model independence | Provider-neutral structured request and response contracts |
| OD-007 | Distributed execution | Only after measured bottlenecks |
| OD-008 | Global coverage | Domain-specific observability metrics rather than a single global completeness score |

---

## 4. Assumptions

| Assumption | Validation Required |
|---|---|
| SQLite WAL mode is sufficient for Version 0.1 workloads | Performance benchmarking during Milestone 1 |
| FTS5 provides adequate full-text search | Functional testing |
| Pydantic provides adequate data validation | Code review |
| Local inference (Ollama/llama.cpp) meets extraction quality needs | Quality evaluation during Milestone 1 |
| The modular monolith architecture is sufficient for Version 0.1 | Architecture review |
| A deterministic revision state machine is implementable | Implementation in Milestone 3 |
| Bitemporal data models are implementable in SQLite | Schema design review |
| Source adapters can be implemented against candidate sources (GDELT, RSS, FRED, etc.) | Integration testing |

---

## 5. Rejected Alternatives

| Alternative | Reason for Rejection |
|---|---|
| Microservices from the start | Premature distributed-system complexity; the specification explicitly recommends a modular monolith initially |
| Graph database as authoritative | No measured performance requirement; relational tables are sufficient initially |
| A single undifferentiated knowledge graph | The specification recommends domain-specific models connected through a common ontology |
| One universal confidence score for every claim | Conceals important uncertainty; multidimensional epistemic representation is required |
| Treating LLM agreement as evidence | Three LLMs agreeing does not constitute independent evidence |
| Bayesian updating applied indiscriminately | Requires defensible likelihood assumptions; repeating the same information ten times does not create ten independent pieces of evidence |
| Embedding as the fundamental object | The fundamental object is a claim about reality, supported by evidence, situated in time, connected to other claims |

---

## 6. Research References

The following external technical resources informed the architecture:

| Source | What was learned | How it affects the architecture |
|---|---|---|
| W3C PROV Model Primer | Provenance model concepts | Source-lineage graph design |
| Event sourcing literature | Event-sourced database concepts | The evidence store as an append-only event ledger |
| Bitemporal modeling literature | Temporal database patterns | Valid time vs. transaction time in all time-sensitive objects |
| Belief revision theory | Principles of belief revision | The revision engine and its dependency-aware operations |

Full details are documented in docs/RESEARCH_REFERENCES.md.

---

## 7. Summary of Key Design Decisions

| Decision | Value |
|---|---|
| **Fundamental object** | Claim about reality, supported by evidence, situated in time, connected to other claims |
| **Architecture** | Seven logical layers, modular monolith |
| **Time model** | Bitemporal (valid time + transaction time) |
| **Revision engine** | Dependency-aware, immutable evidence, versioned interpretations |
| **Intelligence** | Six specialized, task-driven agents (no voting on truth) |
| **Epistemic model** | Multidimensional (not a single confidence score) |
| **Storage** | SQLite WAL, FTS5, Pydantic, FastAPI |
| **Inheritance** | Local-first, replaceable model providers |
| **Governance** | Deterministic validation of all state transitions |
