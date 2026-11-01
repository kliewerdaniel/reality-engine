# Observation Engine

**Reality Engine — Observation Engine Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the Observation Engine of Reality Engine. It covers the source adapter contract, initial integration priorities, and collection scheduling.

---

## 1. Observation Engine Overview

The Observation Engine continuously gathers information relevant to the global world model. It must support multiple source types through a common adapter interface.

---

## 2. Source Adapter Interface

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

## 3. Source Adapter Capabilities

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

## 4. Document Identity

Documents should have stable identities based on source identifiers where available. A content hash should also be generated. Identical content retrieved through multiple URLs should be recognized without discarding the individual source records.

**Recommended fields:**

- Document ID
- Source ID
- Source-native identifier
- Canonical URL
- Content hash
- Publication timestamp
- Collection timestamp
- Original language
- Content type
- Original content reference
- Processing status
- Source update frequency
- Domain importance
- Historical reliability
- Information freshness
- Resource cost
- Unresolved knowledge gaps

---

## 5. Initial Source Categories

| Domain | Candidate Integrations |
|---|---|
| News and global events | GDELT, RSS feeds, official news organization feeds, government press releases, international organization announcements |
| Economics | FRED, World Bank, IMF, OECD, national statistical agencies, central bank publications |
| Science | Crossref, OpenAlex, arXiv, PubMed, institutional research repositories |
| Environment | NASA, NOAA, Copernicus, national meteorological agencies, public environmental datasets |
| Technology | GitHub API, public software release feeds, patent databases, research publications, standards organizations |
| Geopolitical and institutional information | United Nations, World Trade Organization, government publications, international treaty databases, official legislative records |

**Constraint:** Connector availability, API restrictions, source licensing, and rate limits must be verified individually during implementation.

---

## 6. Collection Scheduling

Collection priority should be configurable. Potential factors:

- Source update frequency
- Domain importance
- Historical reliability
- Information freshness
- Resource cost
- Unresolved knowledge gaps

**Constraint:** The scheduler must not allow one high-volume source to consume the entire processing budget.

---

## 7. Constraints

1. **The Observation Engine must support multiple source types.**
2. **Each adapter must support incremental collection.**
3. **Each adapter must support checkpoint persistence.**
4. **Each adapter must support health reporting.**
