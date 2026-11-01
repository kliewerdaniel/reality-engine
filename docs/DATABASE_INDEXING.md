# Database Indexing

**Reality Engine — Database Indexing Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the database indexing of Reality Engine. It covers the indexes and the indexing strategy.

---

## 1. Indexing Strategy

The system uses FTS5 for full-text search and standard B-tree indexes for primary key lookups.

---

## 2. FTS5 Indexes

FTS5 indexes are maintained on:

- sources.name
- documents.content
- documents.canonical_url
- claims.statement
- entities.canonical_name
- hypotheses.statement
- events.description

---

## 3. Constraints

1. **Indexes must be maintained on frequently queried columns.**
2. **FTS5 indexes must be maintained for full-text search.**
