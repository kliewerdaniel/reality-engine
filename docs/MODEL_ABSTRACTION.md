# Model Abstraction

**Reality Engine — Model Abstraction Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document describes the model abstraction layer of Reality Engine. It defines how the system interacts with AI models, how models are selected by task, and how the system achieves model independence.

---

## 1. Purpose

The model abstraction layer ensures that:

1. The knowledge infrastructure does not depend on a particular commercial LLM or inference provider.
2. Any model can be plugged in without changing the underlying data model.
3. Models are selected by task, not by convenience.
4. The system can run several models against the same evidence and compare their interpretations.

This is a core requirement of the architecture (P10: Model independence).

---

## 2. The Model Abstraction Interface

All inference must pass through a common model interface.

### 2.1 Python Interface

```python
class ModelProvider:
    def generate(self, request):
        """
        Generate text or structured output from a request.
        Returns the model's response.
        """
        ...

    def embed(self, request):
        """
        Generate an embedding vector for the input.
        Returns the embedding vector.
        """
        ...

    def health(self):
        """
        Check the health of the model provider.
        Returns health status.
        """
        ...

    def capabilities(self):
        """
        Return the capabilities of the model provider.
        Returns a dictionary of capabilities.
        """
        ...
```

### 2.2 Required Capabilities

The interface must expose:

| Capability | Meaning |
|---|---|
| `generate` | Generate text or structured output |
| `embed` | Generate embeddings |
| `health` | Health check |
| `capabilities` | List of capabilities |

### 2.3 Provider Agnosticism

The application must not depend directly on a single provider's proprietary request format. The model abstraction layer translates between the application's request format and the provider's request format.

### 2.4 Model Versioning

The system must record:

- Model identifier
- Model version
- Prompt version
- Schema version
- Software version

This enables reproducibility (P9).

---

## 3. Model Selection by Task

Different tasks require different model capabilities. The system should use the most appropriate model for each task.

### 3.1 Task-to-Model Mapping

| Task | Preferred Model Capability | Rationale |
|---|---|---|
| Entity extraction | Small instruction model | Fast, sufficient for structured extraction |
| Claim extraction | Structured-output model | Must produce valid structured output |
| Classification | Small local model | Routine classification does not need large context |
| Relationship discovery | Reasoning-capable model | Requires understanding of connections |
| Contradiction analysis | Independent reasoning model | Requires analysis of competing evidence |
| Historical synthesis | Long-context model | Requires understanding of extensive historical records |
| Final explanation | Instruction-following model | Must produce clear, well-structured explanations |

### 3.2 Example Execution Plan

For a revision triggered by new evidence:

1. **Extraction:** Small local model extracts observations from the new document.
2. **Entity resolution:** Small local model resolves entities.
3. **Claim classification:** Small local model classifies claims.
4. **Relationship discovery:** Reasoning-capable model identifies possible downstream relationships.
5. **Contradiction analysis:** Independent reasoning model analyzes the contradiction.
6. **Historical synthesis:** Long-context model synthesizes the historical context.
7. **Final explanation:** Instruction-following model produces the explanation for the user.

---

## 4. Model Providers

### 4.1 Local Inference

The initial configuration uses local inference:

| Provider | Use Case |
|---|---|
| Ollama | Easy local model management, common model ecosystem |
| llama.cpp | Lightweight, portable, fine-grained control |

### 4.2 Cloud Providers (Optional)

Cloud providers may be optional integrations, not architectural dependencies. The model abstraction layer must support plugging in cloud providers.

### 4.3 Model Categories

The system should support:

- Small instruction models (for extraction and classification)
- Structured-output models (for claim extraction)
- Reasoning-capable models (for relationship discovery and contradiction analysis)
- Long-context models (for historical synthesis)
- Instruction-following models (for final explanations)

---

## 5. Model Health and Capabilities

### 5.1 Health Checking

Every model provider must expose a health-check endpoint. The system must:

- Check health before using a model.
- Fall back to a backup model if the primary model is unhealthy.
- Report model health status in the System Observatory.

### 5.2 Capabilities Discovery

Every model provider must report its capabilities. The system must:

- Match task requirements to provider capabilities.
- Never request a capability the provider does not report.
- Log capability mismatches.

---

## 6. Model Independence

### 6.1 Principles

- The model abstraction layer is the only component that depends on a model provider.
- All other components depend on the model abstraction layer, not on a provider.
- Models can be swapped without changing the data model.
- The system can run several models against the same evidence.
- The system can compare interpretations from different models.

### 6.2 Comparison of Interpretations

The system should support running several models against the same evidence and comparing their interpretations. This supports:

- Evidence-first evaluation
- Model bias detection
- Model drift detection
- Model version regression testing

### 6.3 Versioned Models

Every model used in the system must be versioned:

| Field | Meaning |
|---|---|
| model_id | The model identifier |
| model_version | The model version |
| prompt_version | The prompt version |
| schema_version | The schema version |
| software_version | The software version |
| reproducibility_status | EXACT, APPROXIMATE, or NOT_REPRODUCIBLE |

---

## 7. Model Metrics

The system must track model metrics:

| Metric | Meaning |
|---|---|
| Model utilization | How often each model is used |
| Model latency | Response latency per model |
| Model error rate | Errors per model |
| Model quality | Quality scores per model |
| Model calibration | Forecast calibration per model |

---

## 8. Summary

- The model abstraction layer is the single point of dependence on AI models.
- All inference passes through the `ModelProvider` interface.
- Models are selected by task, not by convenience.
- The system achieves model independence by never depending on a specific provider.
- The system can run several models against the same evidence and compare interpretations.
- Model versioning is mandatory for reproducibility.
- The system is local-first: Ollama and llama.cpp are the default inference backends.
