# User Interface

**Reality Engine — User Interface Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the user interface of Reality Engine. It covers the design objective, navigation, and the main views.

---

## 1. Design Objective

The interface should resemble a global research and intelligence environment rather than a conventional chatbot. It should expose the underlying model and allow users to investigate how conclusions were reached.

---

## 2. Main Navigation

Required sections:

1. World Overview
2. World Explorer
3. Reality Timeline
4. Change Intelligence
5. Evidence Explorer
6. Ask Reality
7. Forecast Observatory
8. System Observatory
9. Administration

---

## 3. World Overview

Display:

- Major global developments
- Recently revised world-state assessments
- Domain-level changes
- Emerging developments
- Significant unresolved questions
- Information coverage limitations

**Constraint:** Do not confuse news volume with importance. Rankings must explain their methodology.

---

## 4. World Explorer

An interactive map and graph interface. Selecting a country, company, institution, or event must expose its provenance and revision history.

---

## 5. Reality Timeline

A historical reconstruction interface. Support:

- Historical date selection
- Historical state reconstruction
- Observation chronology
- Knowledge chronology
- Revision chronology
- Comparison between historical and current understanding

---

## 6. Change Intelligence

Show changes rather than merely showing new documents. Each change report should include:

- Changed object
- Previous state
- New state
- Triggering evidence
- Related claims
- Downstream dependencies
- Revision status
- Remaining uncertainty

---

## 7. Evidence Explorer

Allow users to inspect:

- Original source
- Extracted passage
- Evidence
- Hypotheses
- Revision history

---

## 8. Ask Reality

Natural-language questions should be translated into structured queries against the world model. The query engine must retrieve evidence before generating an answer.

The LLM must not invent missing observations or silently fill gaps.

---

## 9. System Observatory

Expose operational health:

- Collection status
- Source failures
- Processing queues
- Revision backlog
- Model utilization
- Database size
- Failed validation
- Data coverage

---

## 10. Constraints

1. **The interface should resemble a global research and intelligence environment rather than a conventional chatbot.**
2. **Every change in the model must be attributable to a specific revision event.**
3. **The LLM must not invent missing observations or silently fill gaps.**
