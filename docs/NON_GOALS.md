# Non-Goals

**Reality Engine — Non-Goals Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document specifies what Reality Engine is explicitly **not** intended to be in its initial versions.

---

## 1. Purpose of This Document

The non-goals document defines boundaries for the initial implementation. It prevents scope creep and ensures that the team focuses on the core innovation: a continuously revisable, evidence-grounded world model with deterministic governance.

These non-goals are **deferred**, not permanently rejected. They may become goals in later milestones.

---

## 2. Non-Goals for Version 0.1 (Evidence Foundation)

### 2.1 No Microservices

**Non-goal:** Do not build a microservices architecture from the start.

**Rationale:** The specification explicitly recommends a modular monolith initially. Microservices introduce distributed-system complexity (network latency, consistency, failure modes, deployment overhead) before the computational model is proven.

**Alternative:** Develop as a modular monolith with clear internal subsystem boundaries. Services can be introduced after measured bottlenecks justify them.

---

### 2.2 No Graph Database

**Non-goal:** Do not use a dedicated graph database as the authoritative store in Version 0.1.

**Rationale:** The specification explicitly recommends SQLite relational tables with graph projections initially. No measured performance requirement justifies a graph database yet.

**Alternative:** SQLite relational tables with graph projections. A graph database can be introduced if measured requirements dictate.

---

### 2.3 No LLM-Dependent World State

**Non-goal:** Do not make the LLM the world model.

**Rationale:** The world model must be a deterministic, versioned computational system that LLM-generated proposals interact with. Making the LLM the world model would destroy the knowledge infrastructure when models change.

**Alternative:** The world model is deterministic and versioned. LLMs propose changes; deterministic systems control accepted state transitions.

---

### 2.4 No Autonomous Multi-Agent Orchestration

**Non-goal:** Do not build six continuously running autonomous agents.

**Rationale:** The specification recommends a task-driven architecture where agents are invoked when necessary. Running all six agents continuously would be inefficient and unnecessary.

**Alternative:** A deterministic scheduler decides which operation is necessary. Small models perform routine extraction; more capable models are invoked for ambiguous interpretation.

---

### 2.5 No Complex Dashboard

**Non-goal:** Do not build an elaborate dashboard in Version 0.1.

**Rationale:** The interface is important, but the first engineering proof must be the evidence and revision foundations. A dashboard without the underlying model is a demo, not a system.

**Alternative:** A minimal interface that supports the end-to-end workflow: ingest, extract, trace, revise, reconstruct.

---

### 2.6 No Six Autonomous Agents

**Non-goal:** Do not implement all six autonomous agents initially.

**Rationale:** The specification recommends starting with the evidence foundation. The agents are introduced in Milestone 4.

**Alternative:** The evidence foundation (Milestone 1-3) does not require agents. Agents are introduced in Milestone 4.

---

### 2.7 No Large Ingestion Pipeline

**Non-goal:** Do not build a large ingestion pipeline for all candidate sources.

**Rationale:** The system must be incremental. The first sources should be RSS and a single API source.

**Alternative:** Start with a small set of sources (GDELT, RSS, FRED, one government source). Expand as adapters are validated.

---

### 2.8 No Distributed Execution

**Non-goal:** Do not introduce distributed services, message brokers, or distributed workers.

**Rationale:** The specification recommends embedded task processing initially. Distributed execution is deferred until measured bottlenecks justify it.

**Alternative:** Embedded task processing. Distributed execution only after measured bottlenecks.

---

## 3. Non-Goals for Version 0.2 (Temporal World Model)

### 3.1 No Real-Time Streaming

**Non-goal:** Do not build a real-time streaming ingestion pipeline.

**Rationale:** The initial sources are batch (RSS, APIs). Real-time streaming is a later enhancement.

**Alternative:** Incremental collection with configurable intervals.

---

### 3.2 No Full Global Coverage

**Non-goal:** Do not attempt to model the entire world with complete coverage.

**Rationale:** Global coverage is a long-term goal. The initial implementation covers a limited set of sources and domains.

**Alternative:** Domain-specific observability metrics. Start with geopolitical, economic, and scientific sources.

---

## 4. Non-Goals for Version 0.3 (Revision Engine)

### 4.1 No Bayesian Updating for All Claims

**Non-goal:** Do not apply Bayesian updating to every claim.

**Rationale:** Bayesian updating requires defensible likelihood assumptions. The specification explicitly states that the method must be explicit and domain-specific.

**Alternative:** Use Bayesian updating only for suitable probabilistic hypotheses. Document priors, likelihoods, and conditional independence assumptions.

---

### 4.2 No Universal Confidence Score

**Non-goal:** Do not assign a single confidence score to every claim.

**Rationale:** A single confidence score conceals important uncertainty. The specification recommends multidimensional epistemic representation.

**Alternative:** Multidimensional epistemic representation with independent dimensions.

---

## 5. Non-Goals for Version 0.4 (Global Intelligence)

### 5.1 No Predictive-Centric Design

**Non-goal:** Do not make forecasting the primary objective in Version 0.4.

**Rationale:** Forecasting is a secondary capability built on top of the world model.

**Alternative:** World model first, forecasting on top. Formal forecasts, but evaluation is secondary.

---

### 5.2 No Graph Database Integration

**Non-goal:** Do not integrate a dedicated graph database in Version 0.4.

**Rationale:** Relational tables are sufficient. A graph database is a future enhancement after measured requirements.

**Alternative:** Graph projections from relational data.

---

## 6. Non-Goals for Version 1.0 (Global Reality Interface)

### 6.1 No Autonomous Political Decisions

**Non-goal:** Do not build Reality Engine to make autonomous political decisions.

**Rationale:** The system provides an evidence-grounded model and analytical representations, not authoritative determinations of reality. It does not make decisions.

**Alternative:** Evidence and analysis; the system does not decide.

---

### 6.2 No Execution of Financial Transactions

**Non-goal:** Do not build Reality Engine to execute financial transactions.

**Rationale:** The system is an information and intelligence infrastructure project. Its outputs are analytical representations.

**Alternative:** Read-only model of the world.

---

### 6.3 No Control of External Infrastructure

**Non-goal:** Do not build Reality Engine to control external infrastructure.

**Rationale:** The system models the world; it does not act on it.

**Alternative:** Observational and analytical infrastructure only.

---

## 7. Non-Goals (Permanently Deferred)

| Item | Deferral Reason |
|---|---|
| Mobile applications | Initial focus is the core data model and API |
| Real-time streaming ingestion | Initial sources are batch (RSS, APIs) |
| Commercial deployment | Initial implementation is a research platform |
| Distributed execution | Only after measured bottlenecks justify it |
| Graph database migration | Relational tables are sufficient initially |
| Mobile and tablet interface variants | Desktop browser interface is sufficient initially |
| Voice interaction | Text-based querying is the primary interface |
| Automated trading | Out of scope for the research platform |
| Autonomous decision-making | The system provides evidence and analysis, not decisions |

---

## 8. Summary

The non-goals are essential for keeping the initial implementation focused. The central innovation — a continuously revisable, evidence-grounded world model with deterministic governance — is the priority. All other features are either deferred or explicitly out of scope for the initial versions.

The system should not be confused with:

- A news aggregator.
- A chatbot.
- A search engine.
- A fact-checking service.
- A research assistant.
- An intelligence dashboard.
- A predictive market.
- A decision support system.

Reality Engine is a **continuously revised computational model of global reality**, preserving the distinction between external reality, observation, and understanding.
