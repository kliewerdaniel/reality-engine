# Information Reliability

**Reality Engine — Information Reliability Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines information reliability in Reality Engine. It covers how the system assesses the reliability of information and how reliability is recorded.

---

## 1. Information Reliability Definition

Information reliability is the assessment of the reliability of information. It is distinct from evidence quality. Information reliability focuses on the reliability of the information itself, not the quality of the evidence.

---

## 2. Reliability Dimensions

| Dimension | Question |
|---|---|
| Source reliability | How dependable is the source for this type of information? |
| Directness | Is the information direct or secondhand? |
| Corroboration | Are there genuinely independent sources? |
| Temporal validity | Is the information current? |
| Measurement quality | How reliable is the underlying measurement? |
| Interpretation | How much inference is required? |
| Contradiction | What evidence challenges the claim? |
| Completeness | What important information is missing? |

**Constraint:** These dimensions must remain independently inspectable. The system may optionally calculate confidence estimates, but the methodology must be explicit and domain-specific.

---

## 3. Authority Dimensions

Authority is domain- and claim-specific, not a universal tie-breaker.

| Dimension | Question | Example Weighting |
|---|---|---|
| **Institutional authority** | Does the source have the authority to speak about its own institution's records? | High for official reports, regulatory filings |
| **Directness** | Was the information obtained directly through observation or measurement? | Direct for sensor data, official statistics; secondhand for summaries |
| **Measurement quality** | How reliable is the underlying measurement or methodology? | High for calibrated instruments, peer-reviewed methods |
| **Independence** | Is the source genuinely independent from other sources? | Independent sources weight more than syndicated reporting |
| **Provenance** | Is the source's origin traceable and verifiable? | Traceable sources weight more than unverified sources |
| **Incentives** | What are the source's potential incentives or reporting bias? | Filtered by domain; a market researcher and a political activist differ |
| **Qualification** | Is the source qualified to establish the particular claim type? | An economist reports on economics; a random blog post does not |

**Constraint:** Authority over an institution's own records does not imply authority over external events. A government ministry's budget numbers are authoritative for the ministry's budget; they are not the only evidence about the external economy.

**Constraint:** Authority dimensions are evaluated per claim and per domain, not as a single static score. A source may be highly authoritative for one domain and unreliable for another.

**Constraint:** Authority is updated as new information about the source becomes available. The system must track authority changes as part of its revision history.

---

## 4. Constraints

1. **Identity:** Each information reliability record must have a stable unique identifier.
2. **Temporal:** Information reliability has valid times.
3. **Provenance:** Each information reliability record must have provenance.
4. **Versioning:** Information reliability has versions.
5. **Consistency:** Information reliability records must be consistent.
