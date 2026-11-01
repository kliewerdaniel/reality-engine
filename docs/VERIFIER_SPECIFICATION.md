# Verifier Specification

**Reality Engine — Verifier Specification Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the Verifier specification. It defines the structured input, output, permissions, error handling, model selection, and evaluation requirements.

---

## 1. Verifier Role

The Verifier checks source attribution, evidence relationships, temporal consistency, and schema validity.

---

## 2. Input

**Context:**

- Proposal
- Evidence

**Prompt:**

- Context
- Task: verify source attribution, evidence relationships, temporal consistency, and schema validity

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

## 3. Output

The Verifier must produce:

- A validation result.
- Check results for provenance, schema, source, temporal, and unsupported.

---

## 4. Permissions

The Verifier has these permissions:

- Read authorized information.
- Generate candidate observations.
- Propose claims.
- Suggest relationships.
- Generate hypotheses.
- Propose revisions.

The Verifier may not:

- Modify immutable evidence.
- Delete audit records.
- Override validation.
- Grant themselves permissions.
- Directly change accepted world state.
- Execute arbitrary external actions.

---

## 5. Model Selection

The Verifier should use:

- Small local model: for classification.
- Small instruction model: for entity extraction.

---

## 6. Error Handling

| Error | Handling |
|---|---|
| Extraction failure | Log, preserve original, do not fabricate |
| Model failure | Fall back to a backup model or retry |
| Schema validation failure | Reject the output and log |

---

## 7. Evaluation

The Verifier is evaluated by:

- Verification checklist coverage.
- Contradiction detection accuracy.
- Temporal validation.

---

## 8. Constraints

1. **The Verifier should use deterministic validation wherever possible.**
2. **The Verifier checks source attribution, evidence relationships, temporal consistency, and schema validity.**
