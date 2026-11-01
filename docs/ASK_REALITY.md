# Ask Reality

**Reality Engine — Ask Reality Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the Ask Reality of Reality Engine. It covers the natural-language interface.

---

## 1. Ask Reality Overview

Natural-language questions should be translated into structured queries against the world model. The query engine must retrieve evidence before generating an answer.

**Example:** "What has changed in global energy markets during the last 30 days?"

---

## 2. Constraints

1. **The query engine must retrieve evidence before generating an answer.**
2. **The LLM must not invent missing observations or silently fill gaps.**
