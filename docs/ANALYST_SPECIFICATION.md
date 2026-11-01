# Analyst Specification

**Reality Engine — Analyst Specification Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the Analyst specification. It defines the structured input, output, permissions, error handling, model selection, and evaluation requirements.

---

## 1. Analyst Role

The Analyst extracts meaning, identifies relationships, constructs interpretations, and proposes hypotheses.

---

## 2. Input

**Context:**

- Observations (structured data)
- Domain
- Time range
- Relevant sources

**Prompt:**

- Context
- Task: interpret observations and propose hypotheses

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

## 3. Output

The Analyst must produce:

- A structured analysis.
- Proposed hypotheses.
- Evidence references.
- Uncertainty.

---

## 4. Permissions

The Analyst has these permissions:

- Read authorized information.
- Generate candidate observations.
- Propose claims.
- Suggest relationships.
- Generate hypotheses.
- Propose revisions.

The Analyst may not:

- Modify immutable evidence.
- Delete audit records.
- Override validation.
- Grant themselves permissions.
- Directly change accepted world state.
- Execute arbitrary external actions.

---

## 5. Model Selection

The Analyst should use:

- Small instruction model: for routine extraction and interpretation.
- Reasoning-capable model: for relationship discovery.
- Long-context model: for historical synthesis.

---

## 6. Error Handling

| Error | Handling |
|---|---|
| Extraction failure | Log, preserve original, do not fabricate |
| Model failure | Fall back to a backup model or retry |
| Schema validation failure | Reject the output and log |

---

## 7. Evaluation

The Analyst is evaluated by:

- Extraction accuracy.
- Claim type classification.
- Entity resolution correctness.

---

## 8. Constraints

1. **The Analyst must not write authoritative world-state records directly.**
2. **Analysts produce structured outputs.**
3. **Unsupported claims are identified.**
4. **Contradictions are surfaced.**
