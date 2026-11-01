# Document Processing

**Reality Engine — Document Processing Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the document processing of Reality Engine. It covers normalization, content hashing, and document identity.

---

## 1. Document Processing Overview

Document processing transforms source documents into normalized documents ready for extraction.

---

## 2. Normalization

The normalization component converts source-specific formats into normalized documents:

```python
class Normalizer:
    def normalize(self, raw_item, source_id) -> NormalizedDocument:
        ...
```

**Critical rule:** Normalization must not lose metadata.

---

## 3. Content Hashing

Content hashing is used for deduplication and integrity:

```python
def generate_content_hash(document) -> str:
    ...
```

**Constraint:** Identical content retrieved through multiple URLs should be recognized without discarding the individual source records.

---

## 4. Document Identity

Documents should have stable identities based on source identifiers where available. A content hash should also be generated.

---

## 5. Constraints

1. **Normalization must not lose metadata.**
2. **Identical content retrieved through multiple URLs should be recognized without discarding the individual source records.**
