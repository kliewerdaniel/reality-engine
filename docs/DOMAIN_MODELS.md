# Domain Models

**Reality Engine — Domain Models Document**
**Version:** 0.1.0
**Date:** November 1, 2026

This document defines the domain models of Reality Engine. Each domain implements a specialized schema that extends the common ontology.

---

## 1. Domain Definition

A domain is a logical division of the world model. Domains share a common ontology but retain their own specialized schemas.

**Domains:**

| ID | Name |
|---|---|
| geopolitical | Geopolitical systems |
| economic | Economic systems |
| financial | Financial systems |
| scientific | Scientific systems |
| technological | Technological systems |
| environmental | Environmental systems |
| social | Social and demographic systems |
| security | Military and security systems |
| legal | Legal and institutional systems |
| infrastructure | Infrastructure and energy systems |

**Constraint:** A domain cannot replace the common ontology. Domains extend the common ontology.

---

## 2. Geopolitical Model

**Purpose:** Model states, governments, alliances, conflicts, diplomacy, and territorial changes.

**Key objects:**

| Object | Types | Fields |
|---|---|---|
| Country | COUNTRY | name, capital, currency, population, GDP |
| Government | GOVERNMENT | name, type, leader, term_start, term_end |
| Alliance | ORGANIZATION | members, formation_date, dissolution_date |
| Treaty | DOCUMENT | name, signatories, effective_date, expiration_date |
| Diplomatic Relationship | RELATIONSHIP | type, status, start_date, end_date |
| Territorial Change | EVENT | territory, change_type, effective_date |
| Conflict | EVENT | type, location, belligerents, start_date, end_date |
| Sanction | POLICY | target, type, effective_date, expiration_date |
| Political Institution | INSTITUTION | name, type, jurisdiction, member_entities |

**Example:**

```json
{
  "id": "geo_000001",
  "statement": "Country X imposed sanctions on Country Y",
  "domain_id": "geopolitical",
  "status": "SUPPORTED",
  "prior_assumptions": "Sanctions are publicly announced",
  "methodology": "Government press releases and news reports",
  "created_at": "2026-10-15T00:00:00Z",
  "revised_at": null
}
```

**Example Relationship:**

```json
{
  "id": "rel_000001",
  "source_entity_id": "entity_000001",
  "target_entity_id": "entity_000002",
  "relationship_type": "SANCTIONS",
  "valid_from": "2026-10-15T00:00:00Z",
  "valid_to": null,
  "recorded_at": "2026-10-16T10:00:00Z",
  "evidence_status": "SUPPORTED",
  "created_at": "2026-10-16T10:00:00Z"
}
```

---

## 3. Economic Model

**Purpose:** Model production, trade, employment, prices, debt, consumption, monetary policy, and fiscal policy.

**Key objects:**

| Object | Types | Fields |
|---|---|---|
| Country | COUNTRY | GDP, inflation_rate, unemployment_rate |
| Industry | ORGANIZATION | sector, output, employment |
| Trade | RELATIONSHIP | trade_volume, direction, partner |
| Price | OBSERVATION | price, unit, valid_from |
| Employment | OBSERVATION | employment, unit, valid_from |
| Interest Rate | OBSERVATION | rate, unit, valid_from |
| Debt | OBSERVATION | debt, unit, valid_from |
| Monnetary Policy | HYPOTHESIS | type, effective_date |
| Fiscal Policy | HYPOTHESIS | type, effective_date |
| Economic Indicator | OBSERVATION | indicator, value, unit, valid_from |

**Example:**

```json
{
  "id": "geo_000002",
  "statement": "Country X inflation rate is 3.2%",
  "domain_id": "economic",
  "status": "SUPPORTED",
  "prior_assumptions": "CPI is the appropriate measure",
  "methodology": "Central bank CPI data",
  "created_at": "2026-10-15T00:00:00Z",
  "revised_at": null
}
```

---

## 4. Financial Model

**Purpose:** Model markets, instruments, central banking, capital flows, and financial publications.

**Key objects:**

| Object | Types | Fields |
|---|---|---|
| Market | ORGANIZATION | market_type, region, hours |
| Instrument | TECHNOLOGY | type, issuer, maturity |
| Central Bank | INSTITUTION | name, type, policy_rate |
| Capital Flow | RELATIONSHIP | direction, amount, source, destination |
| Financial Publication | DOCUMENT | type, publisher, date |

**Example:**

```json
{
  "id": "fin_000001",
  "statement": "Central Bank lowered policy rate",
  "domain_id": "financial",
  "status": "SUPPORTED",
  "prior_assumptions": "Rate change is publicly announced",
  "methodology": "Central bank announcement",
  "created_at": "2026-10-15T00:00:00Z",
  "revised_at": null
}
```

---

## 5. Scientific Model

**Purpose:** Model research, discoveries, theories, replication, retractions, and research domains.

**Key objects:**

| Object | Types | Fields |
|---|---|---|
| Publication | DOCUMENT | type, authors, journal, date |
| Researcher | PERSON | name, affiliation, field |
| Institution | INSTITUTION | name, type, research_areas |
| Hypothesis | HYPOTHESIS | statement, domain, status |
| Experimental Result | OBSERVATION | result, method, units |
| Replication | OBSERVATION | original_claim, new_result, status |
| Retraction | OBSERVATION | original_claim, reason, date |
| Research Domain | DOMAIN | name, description |

**Example:**

```json
{
  "id": "sci_000001",
  "statement": "New study confirms the theory",
  "domain_id": "scientific",
  "status": "SUPPORTED",
  "prior_assumptions": "Peer review is adequate",
  "methodology": "Peer-reviewed publication",
  "created_at": "2026-10-15T00:00:00Z",
  "revised_at": null
}
```

**Example Relationship:**

```json
{
  "id": "rel_000001",
  "source_entity_id": "hypothesis_000001",
  "target_entity_id": "publication_000001",
  "relationship_type": "CORROBORATES",
  "valid_from": "2026-10-15T00:00:00Z",
  "valid_to": null,
  "recorded_at": "2026-10-16T10:00:00Z",
  "evidence_status": "SUPPORTED",
  "created_at": "2026-10-16T10:00:00Z"
}
```

---

## 6. Technological Model

**Purpose:** Model companies, software projects, hardware, patents, technical capabilities, standards, and research developments.

**Key objects:**

| Object | Types | Fields |
|---|---|---|
| Company | ORGANIZATION | name, sector, revenue |
| Software Project | TECHNOLOGY | name, language, repository |
| Hardware | TECHNOLOGY | name, manufacturer, specs |
| Patent | DOCUMENT | number, title, assignee, date |
| Technical Capability | CONDITION | capability, level, scope |
| Standard | DOCUMENT | organization, version, date |
| Research Development | EVENT | type, location, date |

**Example:**

```json
{
  "id": "tech_000001",
  "statement": "Company X released a new processor",
  "domain_id": "technological",
  "status": "SUPPORTED",
  "prior_assumptions": "Press release is accurate",
  "methodology": "Company press release",
  "created_at": "2026-10-15T00:00:00Z",
  "revised_at": null
}
```

---

## 7. Environmental Model

**Purpose:** Model climate indicators, weather observations, ecosystems, natural resources, emissions, and environmental events.

**Key objects:**

| Object | Types | Fields |
|---|---|---|
| Climate Indicator | OBSERVATION | indicator, value, unit, valid_from |
| Weather Observation | OBSERVATION | type, value, unit, valid_from |
| Ecosystem | CONDITION | name, type, health |
| Natural Resource | RESOURCE | name, type, quantity |
| Emission | OBSERVATION | type, value, unit, valid_from |
| Environmental Event | EVENT | type, location, start_date, end_date |

**Example:**

```json
{
  "id": "env_000001",
  "statement": "CO2 emissions increased 5% this year",
  "domain_id": "environmental",
  "status": "SUPPORTED",
  "prior_assumptions": "Data is from a reliable source",
  "methodology": "Satellite and ground measurements",
  "created_at": "2026-10-15T00:00:00Z",
  "revised_at": null
}
```

---

## 8. Social Model

**Purpose:** Model demographics, population changes, education, and public opinion.

**Key objects:**

| Object | Types | Fields |
|---|---|---|
| Population | OBSERVATION | type, value, unit, valid_from |
| Demographics | OBSERVATION | type, value, unit, valid_from |
| Education | OBSERVATION | type, value, unit, valid_from |
| Public Opinion | OBSERVATION | type, value, unit, valid_from |
| Social Movement | EVENT | type, location, start_date, end_date |

**Example:**

```json
{
  "id": "soc_000001",
  "statement": "Population grew 1% this year",
  "domain_id": "social",
  "status": "SUPPORTED",
  "prior_assumptions": "Census is reliable",
  "methodology": "Census data",
  "created_at": "2026-10-15T00:00:00Z",
  "revised_at": null
}
```

---

## 9. Security Model

**Purpose:** Model military developments, conflicts, treaties, sanctions, and arms control.

**Key objects:**

| Object | Types | Fields |
|---|---|---|
| Military Unit | ORGANIZATION | name, type, location |
| Deployment | EVENT | unit, location, start_date, end_date |
| Weapon System | TECHNOLOGY | type, category, effective_date |
| Treaty | DOCUMENT | name, signatories, effective_date |
| Sanction | POLICY | target, type, effective_date |
| Conflict | EVENT | type, location, belligerents, start_date, end_date |

**Example:**

```json
{
  "id": "sec_000001",
  "statement": "New military base established in Region X",
  "domain_id": "security",
  "status": "SUPPORTED",
  "prior_assumptions": "Reports are accurate",
  "methodology": "Satellite imagery and news reports",
  "created_at": "2026-10-15T00:00:00Z",
  "revised_at": null
}
```

---

## 10. Legal Model

**Purpose:** Model courts, legislation, regulatory actions, treaty disputes, and institutional changes.

**Key objects:**

| Object | Types | Fields |
|---|---|---|
| Court | INSTITUTION | name, jurisdiction |
| Legislation | DOCUMENT | name, type, effective_date |
| Regulatory Action | EVENT | type, target, effective_date |
| Treaty Dispute | EVENT | parties, issue, status |
| Institutional Change | EVENT | institution, type, effective_date |

**Example:**

```json
{
  "id": "law_000001",
  "statement": "Court ruled that the policy is invalid",
  "domain_id": "legal",
  "status": "SUPPORTED",
  "prior_assumptions": "Court decision is final",
  "methodology": "Court ruling",
  "created_at": "2026-10-15T00:00:00Z",
  "revised_at": null
}
```

---

## 11. Infrastructure Model

**Purpose:** Model grids, transport, supply chains, energy production, and industrial facilities.

**Key objects:**

| Object | Types | Fields |
|---|---|---|
| Grid | INFRASTRUCTURE_SYSTEM | type, capacity, region |
| Power Plant | INFRASTRUCTURE_SYSTEM | type, capacity, fuel |
| Transport Route | OBSERVATION | route, capacity, status |
| Supply Chain | RELATIONSHIP | origin, destination, volume |
| Energy Production | OBSERVATION | type, value, unit, valid_from |
| Industrial Facility | INFRASTRUCTURE_SYSTEM | name, type, capacity |

**Example:**

```json
{
  "id": "inf_000001",
  "statement": "Shipping route X is restricted",
  "domain_id": "infrastructure",
  "status": "SUPPORTED",
  "prior_assumptions": "Authority announcement is accurate",
  "methodology": "Maritime authority notice",
  "created_at": "2026-10-15T00:00:00Z",
  "revised_at": null
}
```

---

## 12. Cross-Domain Relationships

Cross-domain relationships are traversable:

| Domain | Cross-Domain Connection |
|---|---|
| Economic | Energy crisis affects inflation, industrial output, diplomatic relationships |
| Geopolitical | Sanctions affect trade, currency, and conflict |
| Scientific | New research affects technology and environmental policy |
| Environmental | Climate change affects agriculture, migration, and security |

**Constraint:** The system must be able to trace cross-domain connections without automatically interpreting correlation as causation.

---

## 13. Domain-Specific Observations

Each domain tracks its own observations:

| Domain | Observation Types |
|---|---|
| Geopolitical | Sanctions, treaties, conflicts, diplomatic moves |
| Economic | GDP, inflation, employment, interest rates |
| Financial | Markets, instruments, capital flows |
| Scientific | Publications, hypotheses, experimental results |
| Technological | Patents, releases, capabilities |
| Environmental | Climate indicators, emissions, weather |
| Social | Demographics, public opinion |
| Security | Military deployments, weapons systems |
| Legal | Court decisions, legislation |
| Infrastructure | Energy production, transport capacity |

---

## 14. Summary

- Domains share a common ontology.
- Each domain implements a specialized schema.
- Cross-domain relationships are traversable.
- Causal relationships require stronger evidence than ordinary associations.
- Domain-specific observations are stored with domain metadata.

---

## 15. References

- ONTOLOGY.md — common ontology definitions
- TEMPORAL_MODEL.md — bitemporal semantics
- REVISION_MODEL.md — how domains are revised
- BELIEF_REVISION.md — how domain revisions interact
