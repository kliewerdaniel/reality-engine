# Milestones

**Reality Engine — Milestones Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the milestones for Reality Engine. It covers the milestones and the acceptance criteria.

---

## 1. Milestones Overview

| Milestone | Deliverable | Success Criterion |
|---|---|---|
| Milestone 0: Architecture and Ontology | All core objects can be represented without depending on an LLM | All core objects can be represented without depending on an LLM |
| Milestone 1: Reality Engine 0.1 (Evidence Foundation) | SQLite database, source registry, RSS ingestion, initial API ingestion, document archive, content hashing, claim extraction, entity extraction, provenance records, basic search, entity registry, event registry, relationship model, bitemporal storage, historical state snapshots, historical query interface | A user can ingest a document, inspect extracted claims, and trace every accepted claim to the original document |
| Milestone 2: Reality Engine 0.2 (Temporal World Model) | Bitemporal storage design, historical state snapshots, historical query interface, temporal validation rules, time-semantics documentation, historical reconstruction tests, world-state version management | The system can reconstruct both historical knowledge and current understanding of historical conditions |
| Milestone 3: Reality Engine 0.3 (Revision Engine) | Contradiction detection, evidence lineage, dependency graph, revision proposals, deterministic validation, transactional state updates, audit history | A new observation can trigger a controlled revision of affected claims while preserving unaffected state and previous interpretations |
| Milestone 4: Reality Engine 0.4 (Global Intelligence) | Contradiction detection, evidence lineage, dependency graph, revision proposals, deterministic validation, transactional state updates, audit history, analyst, skeptic, historian, verifier, cross-domain relationship discovery, change reports, natural-language querying | Users can investigate a development across multiple domains and inspect the evidence behind each conclusion |
| Milestone 5: Reality Engine 0.5 (Predictive World Model) | Forecast objects, evaluation criteria, outcome collection, forecasting pipeline, evaluation reporting | Forecasts can be evaluated against actual outcomes without changing their original published probabilities |
| Milestone 6: Reality Engine 1.0 (Global Reality Interface) | Interactive global world model, historical timeline, evidence explorer, change intelligence, forecast explorer, public API | An independent user can follow a global development from original observations through claim extraction, evidence relationships, revision, and final world-state assessment |

---

## 2. Constraints

1. **The milestones must be defined.**
2. **Each milestone must have acceptance criteria.**
