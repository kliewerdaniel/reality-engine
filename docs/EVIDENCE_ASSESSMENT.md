# Evidence Assessment

**Reality Engine — Evidence Assessment Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines evidence assessment in Reality Engine. It covers how evidence is assessed and how evidentiary assessments are recorded.

---

## 1. Evidence Assessment Definition

Evidence assessment is the process of assessing the quality and weight of evidence supporting or challenging a claim.

---

## 2. Assessment Dimensions

| Dimension | Question |
|---|---|
| Source reliability | How dependable is the source for this type of information? |
| Directness | Is the evidence direct or secondhand? |
| Corroboration | Are there genuinely independent sources? |
| Temporal validity | Is the information current? |
| Measurement quality | How reliable is the underlying measurement? |
| Interpretation | How much inference is required? |
| Contradiction | What evidence challenges the claim? |
| Completeness | What important information is missing? |

**Constraint:** These dimensions must remain independently inspectable. The system may optionally calculate confidence estimates, but the methodology must be explicit and domain-specific.

---

## 4. Authority Dimensions

Authority is domain- and claim-specific, not a universal tie-breaker. "Most authoritative" must be evaluated as a vector of dimensions, each weighted per domain and per claim type.

| Dimension | Question | Example Weighting |
|---|---|---|
| **Institutional authority** | Does the source have the authority to make the specific claim about its own institution? (e.g., a central bank announces a rate) | High for official records, reports, regulatory filings |
| **Directness** | Was the information obtained directly through observation, measurement, or official recording? | Direct for sensor data, surveys, official statistics; secondhand for press summaries |
| **Measurement quality** | How reliable is the underlying measurement or methodology? | High for calibrated instruments, peer-reviewed methods; lower for anecdotal reports |
| **Independence** | Is the source genuinely independent from other sources? (No shared origin) | Independent sources weight more than syndicated reporting |
| **Provenance** | Is the source's origin traceable and verifiable? | Traceable, verifiable sources weight more than anonymous or unverified sources |
| **Incentives** | What are the source's potential incentives or reporting bias? | Filtered by domain; a market researcher and a political activist have different incentive profiles |
| **Qualification** | Is the source qualified to establish the particular claim type? | An economist reports on economics; a random blog post does not |

**Constraint:** Authority over an institution's own records does not imply authority over external events. A government ministry's budget numbers are authoritative for the ministry's budget; they are not the only evidence about the external economy.

**Constraint:** Authority dimensions are evaluated per claim and per domain, not as a single static score. A source may be highly authoritative for one domain and unreliable for another.

**Constraint:** Authority is updated as new information about the source becomes available. The system must track authority changes as part of its revision history.

---

## 5. Constraints

1. **Identity:** Each evidence assessment record must have a stable unique identifier.
2. **Temporal:** Evidence assessment has valid times.
3. **Provenance:** Each evidence assessment record must have provenance.
4. **Versioning:** Evidence assessment has versions.
5. **Consistency:** Evidence assessment records must be consistent.
