# Agent Roles

**Reality Engine — Agent Roles Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the agent roles of Reality Engine. It covers the responsibilities and outputs of each agent.

---

## 1. Agent Roles Overview

| Agent | Responsibility |
|---|---|
| **Analyst** | Extracts meaning, identifies relationships, constructs interpretations, proposes hypotheses |
| **Skeptic** | Searches for contradictions, missing evidence, alternative explanations, unsupported assumptions |
| **Historian** | Connects current events to historical precedents, tracks how previous interpretations changed |
| **Forecaster** | Generates explicitly testable predictions, records the conditions under which they should be evaluated |
| **Verifier** | Checks source attribution, evidence relationships, temporal consistency, schema validity |
| **Systems Integrator** | Coordinates revision proposals, updates affected world-state projections |

---

## 2. Analyst

**Responsibilities:**

- Interpret observations.
- Extract candidate claims.
- Identify possible relationships.
- Generate hypotheses.
- Explain developments.
- Find contradictory evidence.

**Outputs must include:**

- Evidence references.
- Uncertainty.

**Constraint:** The Analyst must not write authoritative world-state records directly.

---

## 3. Skeptic

**Responsibilities:**

- Find contradictory evidence.
- Identify unsupported assumptions.
- Detect alternative explanations.
- Challenge weak inferences.
- Identify missing information.

**Outputs must include:**

- Evidence references.
- Uncertainty.

**Constraint:** The Skeptic should be independently prompted and evaluated. Its agreement with another model does not constitute verification.

---

## 4. Historian

**Responsibilities:**

- Retrieve historical context.
- Compare previous events.
- Identify recurring patterns.
- Track previous interpretations.
- Identify historical differences.

**Outputs must include:**

- Evidence references.
- Uncertainty.

**Constraint:** Historical similarity must not automatically be interpreted as causal equivalence.

---

## 5. Forecaster

**Responsibilities:**

- Generate testable predictions.
- Record probabilities.
- Define outcome conditions.
- Specify evaluation horizons.
- Track forecast performance.

**Key constraint:** Every forecast must be immutable after publication except through an explicit correction record.

---

## 6. Verifier

**Responsibilities:**

- Check provenance.
- Validate schema compliance.
- Verify source references.
- Check temporal consistency.
- Detect unsupported assertions.
- Validate revision requirements.

**Requirement:** The Verifier should use deterministic validation wherever possible.

---

## 7. Systems Integrator

**Responsibilities:**

- Coordinate analytical tasks.
- Collect agent outputs.
- Generate revision proposals.
- Resolve schema and dependency conflicts.
- Submit proposals to the deterministic revision engine.

**Key constraint:** The Systems Integrator must not directly write authoritative world-state records.

---

## 8. Constraints

1. **Agents do not vote on what is true.**
2. **The Verifier should use deterministic validation wherever possible.**
3. **The Systems Integrator must not directly write authoritative world-state records.**
4. **Agents should be invoked when tasks require them.**
5. **Routine extraction should use inexpensive local models.**
6. **More capable reasoning models should be reserved for difficult interpretation and revision problems.**
