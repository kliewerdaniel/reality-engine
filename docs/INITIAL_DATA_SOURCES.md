# Initial Data Sources

**Reality Engine — Initial Data Sources Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the initial data sources for Reality Engine. It covers the recommended initial sources and their characteristics.

---

## 1. Initial Data Sources Overview

The initial data sources should be a small set of sources that allow the team to validate the source adapters, the extraction pipeline, and the revision engine without being overwhelmed by volume.

---

## 2. Initial Source Categories

| Domain | Candidate Integrations |
|---|---|
| News and global events | GDELT, RSS, official news organization feeds, government press releases, international organization announcements |
| Economics | FRED, World Bank, IMF, OECD, national statistical agencies, central bank publications |
| Science | Crossref, OpenAlex, arXiv, PubMed, institutional research repositories |
| Environment | NASA, NOAA, Copernicus, national meteorological agencies, public environmental datasets |
| Technology | GitHub API, public software release feeds, patent databases, research publications, standards organizations |
| Geopolitical and institutional information | United Nations, World Trade Organization, government publications, international treaty databases, official legislative records |

**Constraint:** Connector availability, API restrictions, source licensing, and rate limits must be verified individually during implementation.

---

## 3. Constraints

1. **The initial implementation should use a small set of sources.**
2. **Each adapter must be tested individually.**
