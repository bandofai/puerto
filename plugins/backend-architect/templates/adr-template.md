# ADR-NNN: [Short Descriptive Title]

**Date**: YYYY-MM-DD
**Status**: Proposed | Accepted | Deprecated | Superseded by ADR-XXX
**Deciders**: [Names or roles of decision makers]
**Technical Story**: [Link to issue/ticket if applicable]

## Context and Problem Statement

[Describe the context and background. What is the issue or problem that needs to be addressed? What forces are at play? What constraints or requirements exist?]

[Keep this section focused on the problem, not the solution.]

## Decision Drivers

* [Driver 1 - e.g., "Need to support 10,000 concurrent users"]
* [Driver 2 - e.g., "Team has Python/Django expertise"]
* [Driver 3 - e.g., "Budget constraint of $500/month for infrastructure"]
* [Driver 4 - e.g., "Must deploy within 3 months"]
* [Driver 5 - e.g., "Requirement for 99.9% uptime SLA"]

## Considered Options

* [Option 1 - e.g., "PostgreSQL for primary database"]
* [Option 2 - e.g., "MySQL for primary database"]
* [Option 3 - e.g., "MongoDB for primary database"]

## Decision Outcome

Chosen option: "[Option X]", because [provide 1-2 sentence justification of why this option was chosen over others].

### Positive Consequences

* [Positive consequence 1 - e.g., "Leverages team's existing PostgreSQL expertise"]
* [Positive consequence 2 - e.g., "Excellent support for JSON data via JSONB"]
* [Positive consequence 3 - e.g., "Strong ACID guarantees for transactional data"]

### Negative Consequences

* [Negative consequence 1 - e.g., "Vertical scaling limits for write-heavy workloads"]
  - [Mitigation strategy - e.g., "Plan to implement read replicas and sharding if needed"]
* [Negative consequence 2 - e.g., "Higher operational complexity than managed NoSQL"]
  - [Mitigation strategy - e.g., "Use managed PostgreSQL service (RDS/Cloud SQL)"]

## Pros and Cons of the Options

### [Option 1 - PostgreSQL]

* ✅ Good, because [argument 1 - e.g., "Team has 5 years of PostgreSQL experience"]
* ✅ Good, because [argument 2 - e.g., "Excellent support for complex queries and joins"]
* ✅ Good, because [argument 3 - e.g., "Strong data consistency and ACID compliance"]
* ✅ Good, because [argument 4 - e.g., "Rich ecosystem of extensions (PostGIS, pg_trgm, etc.)"]
* ❌ Bad, because [argument 5 - e.g., "Requires careful tuning for high write throughput"]
* ❌ Bad, because [argument 6 - e.g., "Horizontal scaling more complex than NoSQL alternatives"]

### [Option 2 - MySQL]

* ✅ Good, because [argument 1 - e.g., "Simpler replication setup"]
* ✅ Good, because [argument 2 - e.g., "Excellent read performance"]
* ❌ Bad, because [argument 3 - e.g., "Team has limited MySQL experience"]
* ❌ Bad, because [argument 4 - e.g., "Less feature-rich than PostgreSQL (no JSONB, limited window functions)"]

### [Option 3 - MongoDB]

* ✅ Good, because [argument 1 - e.g., "Flexible schema for rapid iteration"]
* ✅ Good, because [argument 2 - e.g., "Built-in horizontal scaling via sharding"]
* ❌ Bad, because [argument 3 - e.g., "Eventual consistency model may complicate business logic"]
* ❌ Bad, because [argument 4 - e.g., "Limited support for complex relational queries"]
* ❌ Bad, because [argument 5 - e.g., "Team lacks NoSQL experience"]

## Links

* [Link to related ADRs - e.g., "ADR-005: API Framework Selection"]
* [External reference - e.g., "PostgreSQL vs MySQL benchmark: https://example.com/benchmark"]
* [Documentation - e.g., "PostgreSQL documentation: https://postgresql.org/docs"]
* [Technical Story/Issue - e.g., "GitHub Issue #123"]

---

## Notes

* [Any additional notes, follow-up actions, or implementation considerations]
* [Timeline for implementation]
* [Migration plan from current state if applicable]
