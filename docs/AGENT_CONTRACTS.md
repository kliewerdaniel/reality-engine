# Agent Contracts

**Reality Engine — Agent Contracts Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the agent contracts for the six intelligence agents of Reality Engine.

---

## 1. Agent Contracts Overview

| Agent | Input | Output |
|---|---|---|
| Analyst | Observations, context | Structured analysis, proposed hypotheses |
| Skeptic | Hypotheses, evidence | List of contradictions, alternative explanations |
| Historian | Event, context | Historical analysis, precedents |
| Forecaster | Hypothesis, context | Testable predictions, probabilities |
| Verifier | Proposal, evidence | Validation result |
| Systems Integrator | Observations, context | Revision proposal |

---

## 2. Analyst Contract

**Input:**

- Observations (structured data)
- Context (domain, time range, relevant sources)

**Contract:**

- The Analyst must produce a structured analysis.
- The analysis must include proposed hypotheses.
- The analysis must include evidence references.
- The analysis must include uncertainty.

**Expected output format:**

```json
{
  "analysis": "structured analysis of the observations",
  "hypotheses": [
    {
      "statement": "hypothesis statement",
      "status": "proposed",
      "evidence": ["evidence_reference_1"],
      "uncertainty": "low|medium|high"
    }
  ],
  "timestamp": "2026-11-01T12:00:00Z"
}
```

---

## 3. Skeptic Contract

**Input:**

- Hypothesis or claim
- Evidence (all evidence)

**Contract:**

- The Skeptic must produce a list of contradictions.
- The Skeptic must produce a list of alternative explanations.
- The Skeptic must produce a list of unsupported assumptions.
- The Skeptic must produce a list of missing information.

**Expected output format:**

```json
{
  "contradictions": [
    {
      "claim_id": "claim_000001",
      "evidence": "contradictory evidence",
      "severity": "low|medium|high"
    }
  ],
  "alternative_explanations": [
    {
      "statement": "alternative explanation",
      "evidence": "evidence supporting the explanation"
    }
  ],
  "unsupported_assumptions": [
    "assumption 1",
    "assumption 2"
  ],
  "missing_information": [
    "information 1",
    "information 2"
  ],
  "timestamp": "2026-11-01T12:00:00Z"
}
```

---

## 4. Historian Contract

**Input:**

- Event or topic
- Time range
- Context

**Contract:**

- The Historian must produce historical analysis.
- The analysis must include relevant precedents.
- The analysis must include historical differences.

**Expected output format:**

```json
{
  "historical_context": "historical context",
  "precedents": [
    {
      "event": "precedent event",
      "date_range": "date range",
      "relevance": "how the precedent relates"
    }
  ],
  "differences": [
    "difference 1",
    "difference 2"
  ],
  "timestamp": "2026-11-01T12:00:00Z"
}
```

---

## 5. Forecaster Contract

**Input:**

- Hypothesis
- Context

**Contract:**

- The Forecaster must produce testable predictions.
- The Forecaster must record probabilities.
- The Forecaster must define outcome conditions.
- The Forecaster must specify evaluation horizons.

**Important:** Every forecast must be immutable after publication except through an explicit correction record.

**Expected output format:**

```json
{
  "predictions": [
    {
      "predicted_outcome": "predicted outcome",
      "probability": 0.7,
      "time_horizon": "2026-12-31",
      "outcome_conditions": "conditions under which the prediction resolves"
    }
  ],
  "model_config": "model configuration",
  "timestamp": "2026-11-01T12:00:00Z"
}
```

---

## 6. Verifier Contract

**Input:**

- Proposal
- Evidence

**Contract:**

- The Verifier must produce a validation result.
- The Verifier must check provenance.
- The Verifier must validate schema compliance.
- The Verifier must verify source references.
- The Verifier must check temporal consistency.
- The Verifier must detect unsupported assertions.
- The Verifier must validate revision requirements.

**Expected output format:**

```json
{
  "status": "ACCEPT|REJECT|NEEDS_REVIEW",
  "checks": {
    "provenance": "pass|fail|unknown",
    "schema": "pass|fail|unknown",
    "source": "pass|fail|unknown",
    "temporal": "pass|fail|unknown",
    "unsupported": "pass|fail|unknown"
  },
  "issues": [
    "issue 1",
    "issue 2"
  ],
  "timestamp": "2026-11-01T12:00:00Z"
}
```

---

## 7. Systems Integrator Contract

**Input:**

- Observations
- Context

**Contract:**

- The Systems Integrator must coordinate analytical tasks.
- The Systems Integrator must collect agent outputs.
- The Systems Integrator must generate revision proposals.
- The Systems Integrator must resolve schema and dependency conflicts.
- The Systems Integrator must submit proposals to the deterministic revision engine.

**Constraint:** The Systems Integrator must not directly write authoritative world-state records.

**Expected output format:**

```json
{
  "revision_proposal": {
    "proposal_id": "proposal_000001",
    "trigger_observation_id": "obs_000001",
    "affected_records": ["record_1"],
    "changes": ["change 1"],
    "dependencies": ["dependency 1"],
    "status": "PROPOSED"
  },
  "timestamp": "2026-11-01T12:00:00Z"
}
```

---

## 8. Constraints

1. **Agents do not vote on what is true.**
2. **The Verifier should use deterministic validation wherever possible.**
3. **The Systems Integrator must not directly write authoritative world-state records.**
4. **Agents should be invoked when tasks require them.**
5. **Routine extraction should use inexpensive local models.**
6. **More capable reasoning models should be reserved for difficult interpretation and revision problems.**
