# Threat Model

**Reality Engine — Threat Model Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the threat model of Reality Engine. It covers the threat categories and the mitigations.

---

## 1. Threat Model Overview

The threat model defines the threats to Reality Engine and the mitigations.

---

## 2. Threat Categories

| Threat | Description | Mitigation |
|---|---|---|
| Information overload | Too much information can overwhelm the system | Domain prioritization and incremental processing |
| Hallucinated claims | The system generates claims that are not supported by evidence | Source-grounded extraction and validation |
| Duplicate reporting | Repeated reporting is mistaken for independent confirmation | Source lineage |
| Incorrect entity resolution | The system incorrectly resolves entities | Stable identities and ambiguity handling |
| False causal inference | The system infers causation from correlation | Explicit causal methodology |
| Historical contamination | The system uses future information in historical reconstruction | Bitemporal records and replay tests |
| Model bias | The model has biases | Multiple analytical perspectives and evidence-first evaluation |
| Model drift | The model changes over time | Versioned models and regression tests |
| Database complexity | The database becomes too complex | Modular monolith and incremental schema growth |
| Computational cost | The system is too expensive to run | Local models, batching, caching |
| Source instability | A source goes offline | Adapter health monitoring and multiple sources |
| Malicious documents | Documents contain malicious content | Treat all external content as untrusted data |
| Silent knowledge corruption | The system corrupts knowledge silently | Immutable evidence and audit events |
| Overconfident outputs | The system is overconfident in its outputs | Explicit uncertainty and observability |

---

## 3. Constraints

1. **External information is untrusted input.**
2. **Documents, websites, extracted text, and model-generated content must never be treated as executable instructions.**
3. **Prompt injection must be treated as a data-ingestion threat.**
