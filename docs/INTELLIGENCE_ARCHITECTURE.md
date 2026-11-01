# Intelligence Architecture

**Reality Engine — Intelligence Architecture Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document describes the intelligence architecture of Reality Engine. It covers the agent roles, agent contracts, agent specifications, and agent orchestration.

---

## 1. Intelligence Architecture Overview

The Intelligence Engine uses specialized, task-driven agents. Agents are not authoritative databases. They produce structured analytical proposals that must be validated before affecting the accepted world model.

**Key constraint:** Agents do not vote on what is true. Three LLMs agreeing with each other does not constitute independent evidence.

---

## 2. Agent Roles

| Agent | Role |
|---|---|
| **Analyst** | Extracts meaning, identifies relationships, constructs interpretations, and proposes hypotheses |
| **Skeptic** | Searches for contradictions, missing evidence, alternative explanations, and unsupported assumptions |
| **Historian** | Connects current events to historical precedents and tracks how previous interpretations changed |
| **Forecaster** | Generates explicitly testable predictions and records the conditions under which they should be evaluated |
| **Verifier** | Checks source attribution, evidence relationships, temporal consistency, and schema validity |
| **Systems Integrator** | Coordinates revision proposals and updates affected world-state projections |

---

## 3. Agent Contracts

Each agent has a structured contract and a defined interface. The agent must be prompted with context, the task, and the expected output format.

---

## 4. Agent Execution Model

Agents should be invoked when tasks require them. Do not run every agent continuously. The scheduler should use task complexity, uncertainty, novelty, and resource cost to determine which agents are needed.

- Routine extraction should use inexpensive local models.
- More capable reasoning models should be reserved for difficult interpretation and revision problems.

---

## 5. Agent Output Requirements

Each agent must produce:

| Output | Description |
|---|---|
| Structured analysis | The agent's analysis in a structured format |
| Evidence references | References to the evidence supporting the analysis |
| Uncertainty | The uncertainty associated with the analysis |
| Proposed changes | Any proposed changes to the world model |

---

## 6. Agent Validation

All agent proposals must be validated by the Verifier before they affect the accepted world model. The Verifier checks:

- Source attribution
- Evidence relationships
- Temporal consistency
- Schema validity
- Underlying model configuration

The Verifier should use deterministic validation wherever possible.

---

## 7. Agent Orchestration

The Systems Integrator coordinates the agents:

1. Collect agent outputs.
2. Generate revision proposals.
3. Resolve schema and dependency conflicts.
4. Submit proposals to the deterministic revision engine.

The Systems Integrator must not directly write authoritative world-state records.

---

## 8. Agent Contracts

Each agent has a contract that defines its input and output:

| Agent | Input | Output |
|---|---|---|
| Analyst | Observations, context | Structured analysis, proposed hypotheses |
| Skeptic | Hypotheses, evidence | List of contradictions, alternative explanations |
| Historian | Event, context | Historical analysis, precedents |
| Forecaster | Hypothesis, context | Testable predictions, probabilities |
| Verifier | Proposal, evidence | Validation result |
| Systems Integrator | Observations, context | Revision proposal |

---

## 9. Agent Specifications

Each agent has a detailed specification. The specifications define:

- Context
- Prompt
- Expected output format
- Evaluation criteria

---

## 10. Constraints

1. **Agents do not vote on what is true.**
2. **The Verifier should use deterministic validation wherever possible.**
3. **The Systems Integrator must not directly write authoritative world-state records.**
4. **Agents should be invoked when tasks require them.**
5. **Routine extraction should use inexpensive local models.**
6. **More capable reasoning models should be reserved for difficult interpretation and revision problems.**
