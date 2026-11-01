# Initial Backlog

**Reality Engine — Initial Backlog Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the initial backlog for Reality Engine. It covers the backlog items and the priority.

---

## 1. Initial Backlog Overview

The initial backlog is organized by milestone. Each item has an identifier, description, dependencies, files or packages affected, expected behavior, acceptance criteria, tests required, estimated complexity, and completion status.

---

## 2. Backlog Items

| ID | Description | Dependencies | Files or packages affected | Expected behavior | Acceptance criteria | Tests required | Estimated complexity | Status |
|---|---|---|---|---|---|---|---|---|
| M0-1 | Final ontology specification (common ontology + domain schemas) | — | schemas/, core/ontology | All core objects can be represented without depending on an LLM | All core objects can be represented without depending on an LLM | — | High (foundational) | Not started |
| M0-2 | Core object definitions (Entity, Event, Observation, Claim, Evidence, Relationship, Hypothesis, Forecast, Conclusion) | M0-1 | core/ontology | All core objects can be represented without depending on an LLM | All core objects can be represented without depending on an LLM | — | High (foundational) | Not started |
| M0-3 | Database schema (SQLite DDL with foreign keys, indexes, constraints) | M0-1 | storage/sqlite | Database schema is complete | Database schema is complete | — | High (foundational) | Not started |
| M0-4 | Temporal model (bitemporal records, interval semantics) | M0-1 | storage/sqlite, core/temporal | Temporal model is complete | Temporal model is complete | — | High (foundational) | Not started |
| M0-5 | Event model (event registry, event types) | M0-1 | core/events | Event model is complete | Event model is complete | — | High (foundational) | Not started |
| M0-6 | Source adapter interface specification | M0-1 | api/routes, observation/adapters | Source adapter interface is specified | Source adapter interface is specified | — | Medium | Not started |
| M0-7 | Revision state machine specification | M0-1 | core/revision | Revision state machine is specified | Revision state machine is specified | — | Medium | Not started |
| M0-8 | Initial architecture decision records | M0-1 | docs/DECISIONS | Architecture decision records exist | Architecture decision records exist | — | Medium | Not started |

---

## 3. Constraints

1. **The initial backlog must be defined.**
2. **Each backlog item must have an identifier, description, dependencies, files or packages affected, expected behavior, acceptance criteria, tests required, estimated complexity, and completion status.**
