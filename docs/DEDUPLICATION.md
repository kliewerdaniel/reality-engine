# Deduplication

**Reality Engine — Deduplication Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the deduplication of Reality Engine. It covers how the system deduplicates documents and claims.

---

## 1. Deduplication Overview

Deduplication is the process of detecting and removing duplicate information.

---

## 2. Deduplication Rules

### 2.1 Document Deduplication

The system must deduplicate identical content from multiple URLs.

**Constraint:** Identical content retrieved through multiple URLs should be recognized without discarding the individual source records.

---

### 2.2 Claim Deduplication

The system must deduplicate claims that are semantically equivalent.

**Constraint:** Duplicate claims must be merged, not duplicated.

---

### 2.3 Observation Deduplication

The system must deduplicate observations that are identical.

---

## 3. Deduplication Rules

1. **The pipeline must be idempotent.**
2. **Each stage must have explicit input/output contracts.**
3. **Failed stages must be retryable.**

---

## 4. Constraints

1. **The pipeline must be idempotent.**
2. **Each stage must have explicit input/output contracts.**
3. **Failed stages must be retryable.**
