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
- source_spans.quoted_text

---

## 3. B-Tree Indexes

| Table | Columns |
|---|---|
| sources | name |
| documents | source_id, canonical_url, content_hash |
| observations | source_id, document_id, subject_id |
| claims | subject_id, predicate, document_id, domain_id |
| entities | canonical_name, entity_type |
| events | event_type |
| relationships | source_entity_id, target_entity_id |
| hypotheses | statement |
| forecasts | status |
| world_states | domain_id |
| source_spans | document_id, start_offset |
| audit_events | event_hash |

---

## 4. Constraints

1. **Indexes must be maintained on frequently queried columns.**
2. **FTS5 indexes must be maintained for full-text search.**
3. **All indexes must be created after the tables they index.**
