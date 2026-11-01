# Historian Specification

**Reality Engine — Historian Specification Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the Historian specification. It defines the structured input, output, permissions, error handling, model selection, and evaluation requirements.

---

## 1. Historian Role

The Historian connects current events to historical precedents and tracks how previous interpretations changed.

---

## 2. Input

**Context:**

- Event or topic
- Time range
- Context

**Prompt:**

- Context
- Task: retrieve historical context and compare with current events

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

## 3. Output

The Historian must produce:

- Historical context.
- Precedents.
- Historical differences.

---

## 4. Permissions

The Historian has these permissions:

- Read authorized information.
- Generate candidate observations.
- Propose claims.
- Suggest relationships.
- Generate hypotheses.
- Propose revisions.

The Historian may not:

- Modify immutable evidence.
- Delete audit records.
- Override validation.
- Grant themselves permissions.
- Directly change accepted world state.
- Execute arbitrary external actions.

---

## 5. Model Selection

The Historian should use:

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

The Historian is evaluated by:

- Historical reconstruction accuracy.
- Temporal integrity benchmarks.

---

## 8. Constraints

1. **Historical similarity must not automatically be interpreted as causal equivalence.**
