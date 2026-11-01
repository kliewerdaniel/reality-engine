# Dependency Graph

**Reality Engine — Dependency Graph Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the dependency graph of Reality Engine. It covers direct dependencies, transitive dependencies, independent support, alternative support, circular dependencies, invalid dependencies, and cross-domain dependencies.

---

## 1. Dependency Graph

The revision engine maintains an explicit dependency graph between conclusions.

**Example:**

```text
H1: Energy supply is declining.
    |
    |--> H2: Energy prices will increase.
    |         |
    |         |--> H3: Industrial production will decline.
    |                   |
    |                   |--> H4: Inflationary pressure will increase.
    |
    |--> H5: Energy imports will increase.
```

### 1.1 Direct Dependencies

Direct dependencies are relationships where one conclusion directly depends on another.

| Type | Example |
|---|---|
| DIRECT | H2 depends on H1 |
| INDIRECT | H3 depends on H2, which depends on H1 |

### 1.2 Transitive Dependencies

Transitive dependencies are indirect dependencies through intermediate conclusions.

| Step | Dependency |
|---|---|
| 1 | H2 depends on H1 |
| 2 | H3 depends on H2 |
| 3 | H3 transitively depends on H1 |

### 1.3 Independent Support

Independent support is when multiple independent pieces of evidence support the same claim.

| Pattern | Meaning |
|---|---|
| INDEPENDENT_SUPPORT | Multiple independent sources support the same claim |

### 1.4 Alternative Support

Alternative support is when multiple pieces of evidence provide alternative support for the same claim.

| Pattern | Meaning |
|---|---|
| ALTERNATIVE_SUPPORT | Multiple pieces of evidence provide alternative support |

### 1.5 Circular Dependencies

Circular dependencies exist when a conclusion depends on itself through a chain of dependencies.

| Pattern | Meaning |
|---|---|
| CIRCULAR | A conclusion depends on itself |

### 1.6 Invalid Dependencies

Invalid dependencies are dependencies that have been invalidated.

| Pattern | Meaning |
|---|---|
| INVALID | The dependency is invalid |

### 1.7 Cross-Domain Dependencies

Cross-domain dependencies are dependencies that span domains.

| Pattern | Meaning |
|---|---|
| CROSS_DOMAIN | The dependency spans domains |

---

## 2. Dependency Graph Rules

### 2.1 Dependency Traversal

| Step | Action |
|---|---|
| 1 | Identify the directly affected claims. |
| 2 | Traverse the dependency graph to find downstream hypotheses. |
| 3 | Evaluate whether the supporting evidence remains valid. |
| 4 | Recalculate affected assessments. |
| 5 | Preserve unaffected assessments. |
| 6 | Record the revision. |

### 2.2 Dependency Version Checks

Each dependency must record its version. When a dependency changes, the dependent conclusion must be flagged.

| Field | Description |
|---|---|
| dependency_id | Unique identifier |
| dependent_id | Dependent conclusion |
| prerequisite_id | Prerequisite conclusion |
| dependency_type | Type of dependency |
| version | Dependency version |
| status | Status of the dependency |

### 2.3 Cycle Detection

The system must detect circular dependencies. If a cycle is found, the system must flag it and not proceed with the revision.

---

## 3. Cross-Domain Dependencies

Cross-domain dependencies are traversable:

| Domain | Cross-Domain Connection |
|---|---|
| Economic | Energy crisis affects inflation, industrial output, diplomatic relationships |
| Geopolitical | Sanctions affect trade, currency, and conflict |
| Scientific | New research affects technology and environmental policy |
| Environmental | Climate change affects agriculture, migration, and security |

**Constraint:** The system must be able to trace cross-domain connections without automatically interpreting correlation as causation.

---

## 4. Dependency Graph Examples

### 4.1 Linear Dependency

```text
H1: Energy supply is declining.
    |
    |--> H2: Energy prices will increase.
    |         |
    |         |--> H3: Industrial production will decline.
    |                   |
    |                   |--> H4: Inflationary pressure will increase.
```

### 4.2 Independent Support

```text
SOURCE A --> CLAIM X
SOURCE B --> CLAIM X
SOURCE C --> CLAIM X
SOURCE D --> CLAIM X
SOURCE E --> CLAIM X
```

All five sources are independent. They each provide independent confirmation.

### 4.3 Alternative Support

```text
SOURCE A --> CLAIM X
SOURCE B --> CLAIM X
SOURCE C --> CLAIM X
```

Sources A, B, and C provide alternative support for Claim X.

### 4.4 Circular Dependency

```text
H1 --> H2 --> H3 --> H1
```

This is a circular dependency.

---

## 5. Dependency Graph Constraints

1. **Identity:** Each dependency must have a stable unique identifier.
2. **Temporal:** Dependencies have a valid time.
3. **Provenance:** Each dependency must have provenance.
4. **Versioning:** Dependencies have versions.
5. **Consistency:** The dependency graph must be acyclic (or cycles must be flagged).

---

## 6. Dependency Graph Constraints

| Constraint | Description |
|---|---|
| Identity | Each dependency has a stable unique identifier |
| Temporal | Dependencies have a valid time |
| Provenance | Each dependency has provenance |
| Versioning | Dependencies have versions |
| Consistency | The dependency graph must be acyclic (or cycles must be flagged) |

---

## 7. Summary

- The dependency graph maintains explicit dependencies between conclusions.
- It supports six dependency types.
- It enforces deterministic traversal.
- It flags circular and invalid dependencies.
- It supports cross-domain dependencies.

---

## 8. References

- ONTOLOGY.md — common ontology definitions
- TEMPORAL_MODEL.md — bitemporal semantics
- HYPOTHESIS_MODEL.md — hypothesis definitions
- FORECAST_MODEL.md — forecast definitions
- REVISION_MODEL.md — revision model
- REVISION_STATE_MACHINE.md — revision state machine
- REVISION_VALIDATION.md — revision validation
