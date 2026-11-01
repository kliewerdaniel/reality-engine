# API Specification

**Reality Engine — API Specification Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the API specification of Reality Engine. It covers the endpoints, the error model, and the versioning.

---

## 1. API Prefix

The API should be versioned from the beginning. Initial prefix: `/api/v1/`

---

## 2. Endpoints

### 2.1 Sources

| Method | Path | Description |
|---|---|---|
| GET | /sources | List sources |
| GET | /sources/{id} | Get a source |
| POST | /sources | Create a source |
| PATCH | /sources/{id} | Update a source |
| GET | /sources/{id}/health | Source health check |

### 2.2 Documents

| Method | Path | Description |
|---|---|---|
| GET | /documents | List documents |
| GET | /documents/{id} | Get a document |

### 2.3 Observations

| Method | Path | Description |
|---|---|---|
| GET | /observations | List observations |
| GET | /observations/{id} | Get an observation |
| POST | /observations | Create an observation |
| GET | /observations/{id}/related | Related observations |

### 2.4 Claims

| Method | Path | Description |
|---|---|---|
| GET | /claims | List claims |
| GET | /claims/{id} | Get a claim |
| GET | /claims/{id}/evidence | Claim evidence |
| GET | /claims/{id}/history | Claim revision history |
| GET | /claims/{id}/dependencies | Claim dependencies |
| GET | /documents/{id}/claims | Claims in a document |
| GET | /documents/{id}/provenance | Provenance for a document |

### 2.5 Entities

| Method | Path | Description |
|---|---|---|
| GET | /entities | List entities |
| GET | /entities/{id} | Get an entity |
| GET | /entities/{id}/relationships | Entity relationships |
| GET | /entities/{id}/timeline | Entity timeline |
| GET | /entities/{id}/state | Entity state |

### 2.6 Events

| Method | Path | Description |
|---|---|---|
| GET | /events | List events |
| GET | /events/{id} | Get an event |
| GET | /events/{id}/related | Related events |

### 2.7 World State

| Method | Path | Description |
|---|---|---|
| GET | /world/state | Current world state |
| GET | /world/state/{version} | World state at a version |
| GET | /world/history | Historical understanding |
| GET | /world/changes | Recent changes |
| POST | /world/query | Structured world query |

### 2.8 Revisions

| Method | Path | Description |
|---|---|---|
| GET | /revisions | List revisions |
| GET | /revisions/{id} | Get a revision |
| GET | /revisions/{id}/dependencies | Revision dependencies |
| GET | /revisions/{id}/audit | Revision audit trail |
| POST | /revisions/{id}/validate | Validate a revision |

### 2.9 Intelligence

| Method | Path | Description |
|---|---|---|
| POST | /intelligence/analyze | Agent analysis |
| POST | /intelligence/compare | Compare agents |
| POST | /intelligence/explain | Explain a conclusion |
| POST | /intelligence/query | Query the model |

### 2.10 Forecasting

| Method | Path | Description |
|---|---|---|
| GET | /forecasts | List forecasts |
| GET | /forecasts/{id} | Get a forecast |
| POST | /forecasts | Create a forecast |
| GET | /forecasts/{id}/evaluation | Forecast evaluation |

---

## 3. Constraints

1. **The API must be versioned from the beginning.**
2. **Public API access must not permit arbitrary modification of accepted world state.**
