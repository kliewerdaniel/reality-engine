# Research References

**Reality Engine — Research References Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the research references for Reality Engine. It covers the sources and the references.

---

## 1. Research References Overview

The following external technical resources informed the architecture:

| Source | What was learned | How it affects the architecture |
|---|---|---|
| W3C PROV Model Primer | Provenance model concepts | Source-lineage graph design |
| Event sourcing literature | Event-sourced database concepts | The evidence store as an append-only event ledger |
| Bitemporal modeling literature | Temporal database patterns | Valid time vs. transaction time in all time-sensitive objects |
| Belief revision theory | Principles of belief revision | The revision engine and its dependency-aware operations |

---

## 2. Constraints

1. **The documentation must be based on research.**
2. **Research references must be recorded.**
