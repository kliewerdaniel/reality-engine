# Prompt Injection Defense

**Reality Engine — Prompt Injection Defense Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the prompt injection defense of Reality Engine. It covers how the system defends against prompt injection.

---

## 1. Prompt Injection Defense Overview

Prompt injection is a data-ingestion threat. The system must treat prompt injection as a data-ingestion threat, not as a prompt-engineering problem.

---

## 2. Defense Principles

| Principle | Description |
|---|---|
| **No execution** | Documents, websites, extracted text, and model-generated content must never be treated as executable instructions. |
| **Sandboxing** | Untrusted documents must be processed in a sandbox. |
| **Input validation** | Input must be validated. |
| **Credential isolation** | Credentials must be isolated. |

---

## 3. Constraints

1. **External information is untrusted input.**
2. **Documents, websites, extracted text, and model-generated content must never be treated as executable instructions.**
3. **Prompt injection must be treated as a data-ingestion threat.**
