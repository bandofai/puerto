# Release Manager Plugin

Release coordination and deployment specialist for planning releases, coordinating deployments, managing rollbacks, creating release notes, and communicating with stakeholders.

## Overview

The Release Manager plugin provides agents for systematic release management using proven practices: release trains, deployment strategies (blue-green, canary, rolling), feature flags, and comprehensive stakeholder communication.

## Agents

### 1. release-planner (Sonnet, Skill-Aware)
Plans releases with scope, timeline, dependencies, risks, and go/no-go criteria.

**Use for**: Release planning, scope definition, timeline creation, risk assessment

**Example**:
```
Use release-planner for Q1 2024 major release.
Release: v2.0 (breaking changes, new pricing, major features)
Scope:
- 15 new features (5 customer-facing, 10 internal)
- 3 breaking API changes
- Database schema migration
- UI redesign
Timeline:
- Code freeze: Jan 15
- QA testing: Jan 16-22
- Staging deployment: Jan 23
- Production deployment: Jan 30 (Tuesday 10am EST)
Go/no-go criteria: Zero P0 bugs, <5 P1 bugs, all smoke tests passing
```

### 2. deployment-coordinator (Sonnet, Skill-Aware)
Coordinates deployments with runbooks, deployment strategies, and monitoring.

**Use for**: Deployment execution, strategy selection (blue-green, canary), monitoring, verification

**Example**:
```
Use deployment-coordinator for production deployment.
Strategy: Canary deployment (reduce blast radius)
Phases:
1. Deploy to 5% of servers (canary group)
2. Monitor for 30 minutes (error rates, latency, alerts)
3. If healthy, proceed to 25%
4. Monitor for 30 minutes
5. If healthy, proceed to 100%
6. Monitor for 2 hours post-deployment
Rollback triggers:
- Error rate >0.5%
- P95 latency >500ms
- Any critical alerts
Verification: Smoke tests, health checks, key user journeys
```

### 3. release-notes-writer (Sonnet, Skill-Aware)
Creates release notes for different audiences: developers, users, executives.

**Use for**: Release notes, changelog, upgrade guides, announcement copy

**Example**:
```
Use release-notes-writer for v2.0 release.
Audiences:
- End users: New features, improvements, breaking changes
- Developers: API changes, migration guide, deprecations
- Internal: Full changelog, technical details

Format:
## What's New
- [Feature name]: [User benefit] (with screenshot)

## Improvements
- [Enhancement]: [How it helps]

## Breaking Changes
- [API change]: [Migration steps]

## Bug Fixes
- [Issue]: [Resolution]

Include: Version number, release date, upgrade instructions
```

### 4. rollback-specialist (Sonnet, Skill-Aware)
Develops rollback procedures and executes emergency rollbacks when needed.

**Use for**: Rollback planning, emergency rollback execution, data migration rollback

**Example**:
```
Use rollback-specialist to create rollback plan for database migration.
Change: Add new column to users table (100M rows)
Forward migration:
1. Add column (nullable, default null)
2. Backfill data in batches (100K rows/batch)
3. Add index after backfill
4. Make column NOT NULL

Rollback procedure:
- If deployed but not backfilled: Simple column drop
- If partially backfilled: Drop column (data loss acceptable)
- If fully deployed: Cannot rollback (migration is one-way)

Decision: Make migration reversible by keeping old column for 1 release
```

## Skills

### release-management
Comprehensive release management practices:
- **Release Trains**: Time-based releases (weekly, bi-weekly, monthly)
- **Deployment Strategies**: Blue-green, canary, rolling, feature flags
- **Release Types**: Major (breaking changes), minor (new features), patch (bug fixes)
- **Semantic Versioning**: MAJOR.MINOR.PATCH (v2.1.3)
- **Feature Flags**: Gradual rollout, A/B testing, emergency kill switch
- **Deployment Pipeline**: Build → Test → Deploy to staging → Deploy to production
- **Monitoring**: Pre-deployment baseline, deployment monitoring, post-deployment verification
- **Rollback**: Fast rollback (<5 min), database migration rollback, data consistency
- **Communication**: Release notes, stakeholder updates, incident communication
- **Testing**: Smoke tests, regression tests, performance tests, security tests

## Templates

### release-plan-template.md
Release plan structure: Release overview, scope (features, fixes), timeline with milestones, dependencies, risks and mitigations, go/no-go criteria, rollback plan, stakeholder communication plan.

### deployment-checklist-template.md
Deployment checklist: Pre-deployment (code freeze, testing complete, approvals), deployment steps, monitoring and verification, post-deployment tasks, rollback procedure.

### release-notes-template.md
Release notes format: Version and date, what's new (features), improvements, bug fixes, breaking changes, known issues, upgrade instructions, deprecations.

### rollback-runbook-template.md
Rollback runbook: Rollback triggers (error rates, latency, alerts), rollback steps (automated and manual), data migration rollback, verification steps, post-rollback actions.

## Workflows

### Complete Release Cycle
```
1. Plan release
Use release-planner to define scope, timeline, and criteria

2. Coordinate deployment
Use deployment-coordinator to execute deployment strategy

3. Write release notes
Use release-notes-writer for user-facing and technical documentation

4. Prepare rollback
Use rollback-specialist to create rollback runbook
```

### Production Deployment
```
Pre-deployment:
- release-planner: Verify go/no-go criteria met
- deployment-coordinator: Review deployment runbook

Deployment:
- deployment-coordinator: Execute canary/blue-green deployment
- Monitor metrics and alerts during rollout

Post-deployment:
- release-notes-writer: Publish release notes
- deployment-coordinator: Monitor for 24 hours

If issues:
- rollback-specialist: Execute rollback procedure
```

## Requirements Met

✅ Role: Release coordination and deployment specialist
✅ Release planning: release-planner with scope, timeline, and criteria
✅ Deployment coordination: deployment-coordinator with multiple strategies
✅ Rollback procedures: rollback-specialist with runbooks and execution
✅ Release notes creation: release-notes-writer for multiple audiences
✅ Stakeholder communication: Covered in release-planner and templates
✅ Tools: CI/CD tools (guidance), version control, communication

## Key Features

✓ **Release Trains**: Time-based, predictable releases
✓ **Deployment Strategies**: Blue-green, canary, rolling, feature flags
✓ **Semantic Versioning**: Clear version numbering
✓ **Go/No-Go Criteria**: Data-driven release decisions
✓ **Rollback Plans**: Fast rollback (<5 min for code, planned for DB)
✓ **Multi-Audience**: Release notes for users, developers, executives
✓ **Risk Mitigation**: Gradual rollout, monitoring, verification
✓ **Feature Flags**: Decouple deployment from release

## Deployment Strategies

### Blue-Green Deployment
```
Setup: Two identical environments (blue = current, green = new)
Process:
1. Deploy new version to green environment
2. Test green thoroughly
3. Switch traffic from blue to green (instant cutover)
4. Keep blue for rollback (can switch back instantly)

Pros: Zero downtime, instant rollback
Cons: 2x infrastructure cost, database migrations tricky
```

### Canary Deployment
```
Setup: Deploy to small subset first (canary group)
Process:
1. Deploy to 5% of servers
2. Monitor for 30 min (errors, latency, alerts)
3. If healthy, deploy to 25%
4. If healthy, deploy to 50%
5. If healthy, deploy to 100%

Pros: Limited blast radius, early problem detection
Cons: Longer deployment time, requires traffic routing
```

### Rolling Deployment
```
Setup: Deploy to servers in batches
Process:
1. Take server out of load balancer
2. Deploy new version
3. Add back to load balancer
4. Repeat for all servers

Pros: No extra infrastructure needed
Cons: Mixed versions during deployment, slower rollback
```

### Feature Flags
```
Setup: Code deployed but features hidden behind flags
Process:
1. Deploy code with feature flag OFF
2. Enable for internal users (testing)
3. Enable for 5% of users (canary)
4. Gradually increase to 100%
5. Remove flag in next release

Pros: Decouple deployment from release, instant rollback (toggle flag)
Cons: Technical debt (flag cleanup), code complexity
```

## Release Metrics

- **Deployment Frequency**: Weekly, daily, hourly (DORA metric)
- **Lead Time**: Commit to production (DORA metric)
- **Change Failure Rate**: % of deployments causing issues (DORA metric)
- **MTTR**: Mean Time To Recovery from failed deployment (DORA metric)
- **Rollback Rate**: % of deployments rolled back (target: <5%)

## Go/No-Go Criteria

### Code Quality
- [ ] All tests passing (unit, integration, E2E)
- [ ] Code coverage >80%
- [ ] No P0/critical bugs
- [ ] <5 P1/high bugs
- [ ] Security scan passed

### Testing
- [ ] QA sign-off
- [ ] Performance testing passed
- [ ] Load testing passed (can handle 2x expected traffic)
- [ ] Smoke tests on staging

### Documentation
- [ ] Release notes written
- [ ] API documentation updated
- [ ] Runbooks updated
- [ ] Rollback plan documented

### Approvals
- [ ] Product owner approval
- [ ] Engineering lead approval
- [ ] Security review (for security-sensitive changes)

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 1 comprehensive release-management skill
- ✅ 4 professional templates for planning, deployment, notes, rollback
- ✅ Complete README with deployment strategies and DORA metrics

## Best Practices

### Release Timing
- **Avoid Fridays**: No Friday deployments (harder to fix issues over weekend)
- **Morning deployments**: Deploy early in day (more time to fix issues)
- **Avoid holidays**: Don't deploy before major holidays
- **Release trains**: Predictable schedule (every Tuesday at 10am)

### Communication
- **Advance notice**: Notify stakeholders 1 week ahead
- **Maintenance windows**: Schedule downtime (if needed) during low traffic
- **Status page**: Keep updated during deployment
- **Post-deployment**: Send summary email with release notes

Closes #81
