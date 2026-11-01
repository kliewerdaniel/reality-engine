# Source Independence

**Reality Engine — Source Independence Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines source independence in Reality Engine. It covers how the system distinguishes independent observations from syndicated reporting, and how source dependence affects evidentiary assessments.

---

## 1. Source Independence Definition

Source independence is the assessment of whether information from different sources is genuinely independent or derived from a common origin.

**Example:**

```text
SOURCE A → CLAIM X
SOURCE B → CLAIM X
SOURCE C → CLAIM X
SOURCE D → CLAIM X
SOURCE E → CLAIM X
```

If all five sources are independent, they provide five independent confirmations.

If all five sources derive from one press release:

```text
ORIGINAL STATEMENT → NEWS A
ORIGINAL STATEMENT → NEWS B
ORIGINAL STATEMENT → NEWS C
ORIGINAL STATEMENT → NEWS D
ORIGINAL STATEMENT → NEWS E
```

The five reports do not represent five independent observations.

---

## 2. Source Independence Classifications

| Classification | Meaning |
|---|---|
| Independent | Genuinely separate observations |
| Shared origin | Common source or dataset |
| Partially dependent | Partially shared origin |
| Unknown | Dependence cannot be determined |
| Not applicable | No relationship exists |

**Constraint:** An unknown relationship must not be interpreted as independence.

---

## 3. Source Independence Assessment

The system must assess source independence when:

1. A claim is supported by multiple sources.
2. A claim is contradicted by multiple sources.
3. A source propagates information from another source.
4. A source quotes another source.

---

## 4. Constraints

1. **Identity:** Each source independence record must have a stable unique identifier.
2. **Temporal:** Source independence has valid times.
3. **Provenance:** Each source independence record must have provenance.
4. **Versioning:** Source independence has versions.
5. **Consistency:** Source independence records must be consistent.
