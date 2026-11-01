# API Error Model

**Reality Engine — API Error Model Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the API error model of Reality Engine. It covers the error response format.

---

## 1. API Error Model Overview

The API must use a consistent error model.

**Error response format:**

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable description",
    "details": "Additional details"
  }
}
```

---

## 2. Constraints

1. **The API must use a consistent error model.**
