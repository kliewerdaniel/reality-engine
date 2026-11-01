# Security Model

**Reality Engine — Security Model Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the security model of Reality Engine. It covers the fundamental security model, model permissions, Frozen Spine integration, and security requirements.

---

## 1. Security Model Overview

The security model is built on the premise that external information is untrusted input.

---

## 2. Fundamental Security Model

| Principle | Description |
|---|---|
| **Untrusted input** | External information is untrusted input. |
| **Prompt injection as data-ingestion threat** | Prompt injection must be treated as a data-ingestion threat. |
| **No execution** | Documents, websites, extracted text, and model-generated content must never be treated as executable instructions. |

---

## 3. Model Permissions

LLMs may:

- Read authorized information.
- Generate candidate observations.
- Propose claims.
- Suggest relationships.
- Generate hypotheses.
- Propose revisions.

LLMs may not:

- Modify immutable evidence.
- Delete audit records.
- Override validation.
- Grant themselves permissions.
- Directly change accepted world state.
- Execute arbitrary external actions.

---

## 4. Frozen Spine Integration

Frozen Spine provides the authorization and execution boundary. The model proposes an operation. The deterministic control plane validates:

- Actor
- Requested operation
- Resource
- Permission

The operation is either accepted or rejected. The resulting decision is recorded.

---

## 5. Security Requirements

| Requirement | Description |
|---|---|
| Preconditions | Preconditions must be checked |
| Schema | Schemas must be validated |
| Execution policy | Execution policy must be enforced |
| Least-privilege permissions | Least-privilege permissions must be enforced |
| Sandboxed document processing | Documents must be processed in a sandbox |
| Safe file handling | Files must be handled safely |
| Credential isolation | Credentials must be isolated |
| API rate limits | API rate limits must be enforced |
| Input validation | Input must be validated |
| Dependency auditing | Dependencies must be audited |
| Signed software releases | Software releases must be signed |
| Backup and recovery | Backup and recovery must be supported |
| Audit history | Audit history must be maintained |
| Controlled external network access | External network access must be controlled |

---

## 6. Privacy

The initial application should prioritize public information. Private data integrations must require explicit authorization and appropriate access controls. Public and private information must have separate access boundaries.

---

## 7. Constraints

1. **External information is untrusted input.**
2. **Documents, websites, extracted text, and model-generated content must never be treated as executable instructions.**
3. **Prompt injection must be treated as a data-ingestion threat.**
