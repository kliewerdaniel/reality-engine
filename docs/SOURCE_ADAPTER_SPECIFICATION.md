# Source Adapter Specification

**Reality Engine — Source Adapter Specification Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the source adapter contract for Reality Engine. It defines the interface and required capabilities.

---

## 1. Contract Overview

Every source adapter must implement a common interface:

```python
class SourceAdapter:
    def identify(self) -> SourceIdentity:
        ...

    def collect(self, cursor=None) -> CollectionBatch:
        ...

    def normalize(self, raw_item) -> NormalizedDocument:
        ...

    def checkpoint(self) -> CollectionCheckpoint:
        ...

    def health(self) -> AdapterHealth:
        ...
```

---

## 2. Required Capabilities

Adapters must support:

- Pagination.
- Incremental collection.
- Retry handling.
- Rate limiting.
- Duplicate detection.
- Failure reporting.
- Source-specific metadata.
- Collection checkpoint persistence.

---

## 3. Constraints

1. **Each adapter must implement the full interface.**
2. **Each adapter must support incremental collection.**
3. **Each adapter must support checkpoint persistence.**
4. **Each adapter must support health reporting.**
