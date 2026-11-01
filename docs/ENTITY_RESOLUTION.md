# Entity Resolution

**Reality Engine — Entity Resolution Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the entity resolution of Reality Engine. It covers how the system resolves entities and how resolution confidence is recorded.

---

## 1. Entity Resolution Overview

Entity resolution is the process of identifying the entity that a reference in a document corresponds to.

---

## 2. Resolution Process

1. **Extract reference:** Extract the name from the document.
2. **Match against registry:** Match against existing entity canonical names and aliases.
3. **Disambiguation:** If multiple entities match, request additional evidence.
4. **Create new entity:** If no match, create a new entity.
5. **Resolve confidence:** Record the confidence and evidence for the resolution.

---

## 3. Resolution Triggers

Entity resolution is triggered by:

- A name appearing in a document.
- An organization name appearing in a document.
- A person's name appearing in a document.
- A geographic region appearing in a document.
- A technology appearing in a document.

---

## 4. Resolution Decision Factors

Entity resolution considers:

- Name similarity.
- Context in the document.
- Domain.
- Source independence.
- Temporal validity.

---

## 5. Ambiguity Handling

Ambiguous identity resolution must remain **unresolved** until sufficient evidence exists. Do not guess.

---

## 6. Constraints

1. **Ambiguous identity resolution must remain unresolved until sufficient evidence exists.**
2. **There must be no silent name-based entity resolution.**
