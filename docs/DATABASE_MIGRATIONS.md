# Database Migrations

**Reality Engine — Database Migrations Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the database migrations of Reality Engine. It covers the migration conventions and the migration process.

---

## 1. Migration Conventions

Migrations are versioned, ordered, and applied sequentially.

**Migration fields:**

| Field | Description |
|---|---|
| migration_id | Unique identifier |
| version | Migration version |
| description | Description of the change |
| applied_at | When the migration was applied |
| status | Status of the migration |

---

## 2. Migration Rules

1. **Immutability:** Migrations are applied in order and are not reordered.
2. **Idempotency:** Migrations must be idempotent.
3. **Rollback:** Rollback is not supported. Revert by applying a new migration.
4. **Testing:** Each migration must be tested before deployment.

---

## 3. Constraints

1. **Migrations must be applied in order.**
2. **Migrations must be idempotent.**
3. **Migrations must be tested.**
