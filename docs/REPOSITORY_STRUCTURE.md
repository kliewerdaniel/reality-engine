# Repository Structure

**Reality Engine — Repository Structure Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the repository structure of Reality Engine. It covers the directory layout and the package organization.

---

## 1. Repository Structure

```text
reality-engine/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── pyproject.toml
├── package.json
├── .env.example
├── .gitignore
│
├── docs/
│   ├── PROJECT_SPECIFICATION.md
│   ├── PROJECT_CONTEXT_AND_DECISIONS.md
│   ├── PROJECT_ROADMAP.md
│   ├── REQUIREMENTS.md
│   ├── DEFINITIONS_AND_TERMINOLOGY.md
│   ├── NON_GOALS.md
│   ├── ARCHITECTURE.md
│   ├── SYSTEM_COMPONENTS.md
│   ├── DATA_FLOW.md
│   ├── EVENT_ARCHITECTURE.md
│   ├── STORAGE_ARCHITECTURE.md
│   ├── LOCAL_FIRST_ARCHITECTURE.md
│   ├── MODEL_ABSTRACTION.md
│   ├── ARCHITECTURE_DECISIONS.md
│   ├── ONTOLOGY.md
│   ├── ENTITY_MODEL.md
│   ├── EVENT_MODEL.md
│   ├── RELATIONSHIP_MODEL.md
│   ├── OBSERVATION_MODEL.md
│   ├── CLAIM_MODEL.md
│   ├── EVIDENCE_MODEL.md
│   ├── HYPOTHESIS_MODEL.md
│   ├── FORECAST_MODEL.md
│   ├── DOMAIN_MODELS.md
│   ├── ONTOLOGY_EVOLUTION.md
│   ├── TEMPORAL_MODEL.md
│   ├── BITEMPORAL_DATA.md
│   ├── HISTORICAL_RECONSTRUCTION.md
│   ├── TIME_SEMANTICS.md
│   ├── REVISION_MODEL.md
│   ├── REVISION_STATE_MACHINE.md
│   ├── DEPENDENCY_GRAPH.md
│   ├── CONTRADICTION_DETECTION.md
│   ├── BELIEF_REVISION.md
│   ├── REVISION_VALIDATION.md
│   ├── REVISION_TRANSACTION_MODEL.md
│   ├── PROVENANCE_MODEL.md
│   ├── SOURCE_LINEAGE.md
│   ├── SOURCE_INDEPENDENCE.md
│   ├── SOURCE_QUALITY.md
│   ├── EVIDENCE_ASSESSMENT.md
│   ├── INFORMATION_RELIABILITY.md
│   ├── INTELLIGENCE_ARCHITECTURE.md
│   ├── AGENT_ROLES.md
│   ├── AGENT_CONTRACTS.md
│   ├── ANALYST_SPECIFICATION.md
│   ├── SKEPTIC_SPECIFICATION.md
│   ├── HISTORIAN_SPECIFICATION.md
│   ├── FORECASTER_SPECIFICATION.md
│   ├── VERIFIER_SPECIFICATION.md
│   ├── SYSTEMS_INTEGRATOR_SPECIFICATION.md
│   ├── AGENT_ORCHESTRATION.md
│   ├── OBSERVATION_ENGINE.md
│   ├── SOURCE_ADAPTER_SPECIFICATION.md
│   ├── INGESTION_PIPELINE.md
│   ├── DOCUMENT_PROCESSING.md
│   ├── ENTITY_RESOLUTION.md
│   ├── DEDUPLICATION.md
│   ├── COLLECTION_SCHEDULER.md
│   ├── INITIAL_DATA_SOURCES.md
│   ├── EPISTEMIC_MODEL.md
│   ├── UNCERTAINTY_MODEL.md
│   ├── OBSERVABILITY_MODEL.md
│   ├── KNOWLEDGE_GAPS.md
│   ├── ACTIVE_OBSERVATION.md
│   ├── VALUE_OF_INFORMATION.md
│   ├── SECURITY_MODEL.md
│   ├── THREAT_MODEL.md
│   ├── FROZEN_SPINE_INTEGRATION.md
│   ├── PERMISSION_MODEL.md
│   ├── AUDIT_MODEL.md
│   ├── PROMPT_INJECTION_DEFENSE.md
│   ├── DATA_PRIVACY.md
│   ├── DATABASE_SCHEMA.md
│   ├── DATABASE_MIGRATIONS.md
│   ├── DATABASE_INDEXING.md
│   ├── API_SPECIFICATION.md
│   ├── API_VERSIONING.md
│   ├── API_ERROR_MODEL.md
│   ├── USER_INTERFACE.md
│   ├── WORLD_OVERVIEW.md
│   ├── WORLD_EXPLORER.md
│   ├── REALITY_TIMELINE.md
│   ├── CHANGE_INTELLIGENCE.md
│   ├── EVIDENCE_EXPLORER.md
│   ├── ASK_REALITY.md
│   ├── SYSTEM_OBSERVATORY.md
│   ├── EVALUATION_FRAMEWORK.md
│   ├── BENCHMARKS.md
│   ├── REVISION_BENCHMARKS.md
│   ├── TEMPORAL_BENCHMARKS.md
│   ├── PROVENANCE_BENCHMARKS.md
│   ├── SOURCE_LINEAGE_BENCHMARKS.md
│   ├── FORECAST_EVALUATION.md
│   ├── HINDSIGHT_CONTAMINATION_TESTS.md
│   ├── ADVERSARIAL_TESTING.md
│   ├── DEVELOPMENT_GUIDE.md
│   ├── REPOSITORY_STRUCTURE.md
│   ├── CODING_STANDARDS.md
│   ├── TESTING_STRATEGY.md
│   ├── OBSERVABILITY_AND_MONITORING.md
│   ├── DEPLOYMENT.md
│   ├── BACKUP_AND_RECOVERY.md
│   ├── OPERATIONS_MANUAL.md
│   ├── CONTRIBUTING.md
│   ├── RESEARCH_REFERENCES.md
│   ├── IMPLEMENTATION_PLAN.md
│   ├── MILESTONES.md
│   ├── ACCEPTANCE_CRITERIA.md
│   ├── INITIAL_BACKLOG.md
│   └── DECISIONS/
│
├── schemas/
│   ├── source.json
│   ├── document.json
│   ├── observation.json
│   ├── entity.json
│   ├── event.json
│   ├── relationship.json
│   ├── claim.json
│   ├── evidence_link.json
│   ├── hypothesis.json
│   ├── forecast.json
│   ├── revision_proposal.json
│   ├── revision_event.json
│   ├── world_state_snapshot.json
│   ├── audit_event.json
│   ├── agent_task.json
│   └── agent_response.json
│
├── core/
│   ├── ontology/
│   ├── entities/
│   ├── events/
│   ├── relationships/
│   ├── temporal/
│   ├── world_state/
│   ├── revision/
│   └── event_ledger/
│
├── observation/
│   ├── adapters/
│   ├── collectors/
│   ├── scheduler/
│   ├── normalization/
│   └── deduplication/
│
├── evidence/
│   ├── extraction/
│   ├── claims/
│   ├── provenance/
│   ├── lineage/
│   ├── contradiction/
│   └── verification/
│
├── intelligence/
│   ├── analyst/
│   ├── skeptic/
│   ├── historian/
│   ├── forecaster/
│   ├── verifier/
│   └── integrator/
│
├── domains/
│   ├── geopolitical/
│   ├── economic/
│   ├── financial/
│   ├── scientific/
│   ├── technological/
│   ├── environmental/
│   ├── social/
│   ├── security/
│   ├── legal/
│   └── infrastructure/
│
├── governance/
│   ├── policies/
│   ├── permissions/
│   ├── frozen_spine/
│   └── audit/
│
├── storage/
│   ├── sqlite/
│   ├── documents/
│   ├── indexes/
│   ├── migrations/
│   └── projections/
│
├── api/
│   ├── routes/
│   ├── schemas/
│   └── services/
│
├── frontend/
│   ├── src/
│   ├── pages/
│   ├── explorer/
│   ├── timeline/
│   ├── evidence/
│   ├── intelligence/
│   └── observatory/
│
├── evaluation/
│   ├── datasets/
│   ├── extraction/
│   ├── provenance/
│   ├── temporal/
│   ├── revision/
│   ├── forecasting/
│   └── adversarial/
│
├── scripts/
├── migrations/
└── tests/
```

---

## 2. Constraints

1. **The repository structure must be as defined above.**
2. **The structure is a target architecture. Directories should be introduced as their functionality is implemented.**
