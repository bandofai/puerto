# Hot-fix Developer Plugin

**Version**: 1.0.0
**Category**: Work Agent - Critical Incident Response
**Complexity**: Advanced
**Time-Critical**: Yes (P0 targets < 75 minutes resolution)

---

## Overview

Comprehensive plugin for handling production bugs and emergency patches. Provides end-to-end workflow from diagnosis through deployment to post-incident analysis, optimized for time-critical production incidents.

### Key Capabilities

✅ **Complete Incident Lifecycle**: Diagnosis → Fix → Test → Deploy → Learn
✅ **Time-Optimized**: Fast models (Haiku) for deterministic tasks, Sonnet for judgment
✅ **Production-Safe**: Multiple validation checkpoints, tested rollback procedures
✅ **Blameless Culture**: Post-mortems focus on systems, not individuals
✅ **Evidence-Based**: All decisions backed by logs, metrics, and data
✅ **Skills-Aware**: Agents read expertise before acting

---

## Plugin Structure

```
hotfix-developer/
├── README.md                          # This file
├── agents/
│   ├── bug-diagnostician.md          # Root cause identification (Sonnet, Read-only)
│   ├── patch-developer.md            # Emergency fix development (Sonnet, Write)
│   ├── hotfix-tester.md              # Validation and testing (Haiku, Fast)
│   ├── deployment-coordinator.md     # Production rollout (Sonnet, Orchestration)
│   └── incident-analyzer.md          # Post-incident RCA (Sonnet, Learning)
├── skills/
│   └── bug-diagnosis/
│       └── SKILL.md                  # Debugging expertise and patterns
├── templates/
│   ├── diagnosis-report.md           # Bug investigation template
│   ├── rca-template.md               # Root cause analysis template
│   └── deployment-plan.md            # Deployment strategy template
```

---

## Agents

### 1. bug-diagnostician
**Model**: Sonnet (complex analysis required)
**Tools**: Read, Grep, Glob (read-only for safety)
**Purpose**: Rapid root cause identification for production incidents

**Capabilities**:
- Log analysis and pattern recognition
- Stack trace interpretation
- 5 Whys root cause methodology
- Impact assessment (users, revenue, systems)
- Timeline creation
- Hypothesis testing

**Target Times**:
- P0 (critical): 15 minutes
- P1 (major): 30 minutes
- P2 (moderate): 60 minutes

**Output**: Comprehensive diagnosis report with root cause and recommended fix

**Example Usage**:
```
"Critical production bug: Users cannot complete checkout.
Error rate jumped from 0.1% to 45% at 14:32 UTC.
Analyze logs in logs/payment-service/ and identify root cause."
```

---

### 2. patch-developer
**Model**: Sonnet (judgment required for safe fixes)
**Tools**: Read, Write, Edit, Grep, Glob
**Purpose**: Create minimal, safe emergency patches

**Capabilities**:
- Minimal change principle (smallest fix possible)
- Defensive programming (null checks, validation, error handling)
- Backwards compatibility verification
- Safety checklist enforcement
- Risk assessment
- Rollback plan creation

**Core Principles**:
- No refactoring during hot-fixes
- Defensive guards on all changes
- Multiple validation checkpoints
- Clear documentation of every change

**Output**: Code patch with safety checklist and rollback plan

**Example Usage**:
```
"Create emergency patch for payment processing null pointer error.
Root cause: user.paymentMethod can be null but code doesn't check.
File: src/payment/processor.py:147
Make minimal fix with null check and error handling."
```

---

### 3. hotfix-tester
**Model**: Haiku (fast validation, deterministic process)
**Tools**: Read, Bash, Grep, Glob
**Purpose**: Fast but thorough validation of emergency patches

**Capabilities**:
- Fix validation (does it work?)
- Regression testing (nothing else broke?)
- Performance impact measurement
- Backwards compatibility verification
- Rollback testing

**Test Categories**:
1. **Fix Validation**: Original bug resolved?
2. **Regression**: Related features still work?
3. **Performance**: Acceptable speed?
4. **Compatibility**: Works with old data?
5. **Rollback**: Can we revert safely?

**Target Times**:
- P0: 15 minutes (critical tests only)
- P1: 30 minutes (comprehensive)
- P2: 60 minutes (full suite)

**Output**: Test report with approval recommendation

**Example Usage**:
```
"Test the payment null pointer hot-fix in staging.
Original bug: Checkout fails when user.paymentMethod is null.
Fix: Added null check and error handling.
Run fix validation, regression tests, and approve for deployment."
```

---

### 4. deployment-coordinator
**Model**: Sonnet (orchestration and judgment required)
**Tools**: Read, Write, Bash, Grep, Glob
**Purpose**: Safe production deployment with phased rollout

**Capabilities**:
- Canary deployment planning (10% → 50% → 100%)
- Blue-green deployment strategies
- Rollback procedures (one-command revert)
- Monitoring checklists
- Stakeholder communication
- Success/failure criteria definition

**Deployment Phases**:
1. **Phase 1**: 10% canary, 10 min monitoring
2. **Phase 2**: 50% expansion, 10 min monitoring
3. **Phase 3**: 100% full rollout, 30 min validation

**Rollback Triggers**:
- Error rate > 5%
- Response time > 2x baseline
- New critical errors appear
- Any uncertainty about stability

**Output**: Complete deployment plan with monitoring and rollback

**Example Usage**:
```
"Create deployment plan for payment null pointer hot-fix.
Severity: P0 (45% of checkouts failing)
Environment: Production (5M requests/day)
Strategy: Canary deployment with feature flag
Create complete deployment plan with monitoring and rollback."
```

---

### 5. incident-analyzer
**Model**: Sonnet (deep analysis and learning)
**Tools**: Read, Write, Grep, Glob
**Purpose**: Blameless post-incident reviews and prevention

**Capabilities**:
- Complete timeline creation
- 5 Whys root cause analysis
- Contributing factors identification
- Blameless post-mortem facilitation
- Action item creation (SMART goals)
- Prevention measure recommendations

**RCA Components**:
- Executive summary
- Detailed timeline
- Root cause (5 Whys)
- What went well ✅
- What could improve 🔄
- Action items with owners
- Prevention measures
- Lessons learned

**Output**: Comprehensive RCA document with action items

**Example Usage**:
```
"Create RCA for payment processing incident on 2024-01-15.
Duration: 14:23-14:45 UTC (22 minutes)
Impact: 45% checkout failures, 4,500 users affected
Root cause: Null pointer in PaymentProcessor
Include complete timeline, 5 Whys analysis, action items."
```

---

## Skills

### bug-diagnosis/SKILL.md

Comprehensive debugging expertise covering:

**Methodologies**:
- Scientific method for debugging
- 5 Whys root cause analysis
- Binary search debugging
- Hypothesis testing

**Log Analysis**:
- Error rate patterns (sudden, gradual, intermittent)
- Temporal analysis
- Stack trace interpretation
- Log correlation across systems

**Common Bug Patterns**:
- Null/undefined reference
- Resource exhaustion
- Race conditions
- Configuration errors
- Dependency failures

**Tools & Commands**:
- Log analysis (grep, awk, sort, uniq)
- Code search (grep, git)
- System inspection (ps, netstat, lsof)

**Impact Assessment**:
- User impact calculation
- Business impact quantification
- Severity classification (P0-P3)

---

## Templates

### 1. diagnosis-report.md

Structured template for bug diagnosis including:
- Incident summary (severity, timeline, impact)
- Symptoms (user-facing and system behavior)
- Evidence collected (logs, traces, metrics)
- Recent changes (deployments, config)
- Root cause analysis (5 Whys)
- Impact assessment
- Recommended fix
- Testing requirements

### 2. rca-template.md

Comprehensive post-incident review template:
- Executive summary
- Incident details
- Complete timeline
- Root cause analysis (5 Whys)
- Impact assessment
- What went well ✅
- What could improve 🔄
- Action items (SMART goals with owners)
- Prevention measures
- Lessons learned

### 3. deployment-plan.md

Complete deployment strategy template:
- Pre-deployment checklist
- Phased rollout plan (10% → 50% → 100%)
- Monitoring plan with metrics
- Success criteria per phase
- Rollback procedure
- Communication templates
- Post-deployment activities

---

## Complete Workflow Example

### Scenario: Payment Processing Failure

**Context**: 45% of users cannot complete checkout. Error rate spiked from 0.3% to 45% at 14:32 UTC.

#### Step 1: Diagnosis (10-15 minutes)

```
Use bug-diagnostician:

"Critical bug: users cannot complete checkout.
Error rate jumped from 0.1% to 45% at 14:32 UTC.
Recent deployment: payment-service v2.3.1 at 14:15 UTC.
Analyze logs/payment-service/ and identify root cause."
```

**Agent Actions**:
1. Reads bug-diagnosis skill for patterns
2. Searches logs around 14:32 UTC
3. Finds NullPointerException at PaymentProcessor.java:147
4. Performs 5 Whys analysis
5. Identifies root cause: missing null check for paymentMethod
6. Creates diagnosis report with impact assessment

**Result**: Root cause identified in 12 minutes

---

#### Step 2: Patch Development (20-30 minutes)

```
Use patch-developer:

"Create emergency patch for payment null pointer error.
Root cause (from diagnosis): user.paymentMethod can be null but
code accesses .token without check at PaymentProcessor.java:147.
Make minimal fix with defensive null check and error handling."
```

**Agent Actions**:
1. Reads diagnosis report
2. Locates exact code at processor.py:147
3. Adds defensive null check
4. Adds error handling and logging
5. Ensures backwards compatibility
6. Completes safety checklist
7. Documents changes and rollback plan

**Result**: Safe patch created in 25 minutes

---

#### Step 3: Testing (15-20 minutes)

```
Use hotfix-tester:

"Test the payment null pointer hot-fix in staging environment.
Original bug: Checkout fails when user.paymentMethod is null.
Fix: Added null check and error handling at processor.py:147.
Run fix validation, regression tests, performance check, and
provide approval recommendation."
```

**Agent Actions**:
1. Reviews diagnosis and patch docs
2. Runs fix validation (null case now works)
3. Runs regression suite (247/247 tests pass)
4. Checks performance (248ms, +1.2% - acceptable)
5. Validates rollback procedure
6. Creates test report: ✅ APPROVED

**Result**: Testing complete in 18 minutes, deployment approved

---

#### Step 4: Deployment (30-45 minutes)

```
Use deployment-coordinator:

"Deploy payment null pointer hot-fix to production.
Severity: P0 (45% checkout failure rate)
Environment: Production (5M requests/day, 1000 req/min)
Strategy: Canary deployment with monitoring
Create complete deployment plan and execute phased rollout."
```

**Agent Actions**:
1. Creates pre-deployment checklist
2. Deploys Phase 1 (10% canary)
3. Monitors for 10 minutes: ✅ Success
4. Deploys Phase 2 (50% expansion)
5. Monitors for 10 minutes: ✅ Success
6. Deploys Phase 3 (100% full rollout)
7. Monitors for 30 minutes: ✅ Stable
8. Updates stakeholders and status page

**Result**: Deployment successful in 40 minutes

---

#### Step 5: Post-Incident Analysis (1-2 hours)

```
Use incident-analyzer:

"Create comprehensive RCA for payment processing incident.
Date: 2024-01-15, Duration: 14:23-14:45 UTC (22 min)
Impact: 45% checkout failures, 4,500 users, ~$8,750 revenue loss
Root cause: Missing null check in PaymentProcessor
Include timeline, 5 Whys, what went well, improvements,
action items with owners, and prevention measures."
```

**Agent Actions**:
1. Gathers complete timeline from logs and git
2. Performs thorough 5 Whys analysis
3. Quantifies user and business impact
4. Identifies positives (fast detection, smooth rollback)
5. Identifies improvements (test coverage, deployment strategy)
6. Creates SMART action items with owners and due dates
7. Documents prevention measures (technical and cultural)
8. Extracts lessons learned

**Result**: Comprehensive RCA completed in 90 minutes

---

### Total Time-to-Resolution

| Phase | Target | Actual | Status |
|-------|--------|--------|--------|
| Diagnosis | 15 min | 12 min | ✅ Under target |
| Patch Development | 30 min | 25 min | ✅ Under target |
| Testing | 15 min | 18 min | ⚠️ Slightly over |
| Deployment | 30 min | 40 min | ⚠️ Slightly over |
| **TOTAL RESOLUTION** | **90 min** | **95 min** | ✅ Acceptable |
| Post-Incident RCA | 2 hours | 90 min | ✅ Under target |

**P0 Target**: < 120 minutes ✅ Achieved

---

## Performance Targets by Severity

| Severity | Criteria | Diagnosis | Fix | Test | Deploy | Total |
|----------|----------|-----------|-----|------|--------|-------|
| **P0** | Critical outage, >25% users | 15 min | 30 min | 15 min | 15 min | **75 min** |
| **P1** | Major impact, 5-25% users | 30 min | 60 min | 30 min | 30 min | **150 min** |
| **P2** | Moderate, <5% users | 60 min | 120 min | 60 min | 60 min | **300 min** |
| **P3** | Low impact, minimal effect | 240 min | 480 min | 120 min | 120 min | **960 min** |

---

## Best Practices Embodied

### 1. Evidence-Based Decisions
- Always use logs, metrics, and data
- Never guess or assume
- Mark hypotheses clearly
- Cite sources in reports

### 2. Minimal Changes
- Smallest possible fix
- No refactoring during hot-fixes
- No "while I'm here" improvements
- Focus on resolution only

### 3. Defensive Programming
- Add null checks everywhere
- Implement try-catch error handling
- Validate all inputs
- Add logging for debugging

### 4. Backwards Compatibility
- Works with old and new data
- No breaking changes
- Gradual deprecation if needed
- Test with legacy clients

### 5. Thorough Testing
- Fix validation first
- Regression testing required
- Performance impact measured
- Rollback validated

### 6. Safe Deployments
- Always canary deployment
- Start small (10%), expand gradually
- Monitor constantly
- Rollback immediately if issues

### 7. Blameless Culture
- Focus on systems, not people
- Include "what went well"
- Psychological safety matters
- Learning over blame

### 8. Continuous Learning
- Every incident produces RCA
- Action items tracked to completion
- Patterns become runbooks
- Knowledge shared organization-wide

---

## Integration Patterns

### Standalone Usage

Invoke individual agents for specific tasks:

```
# Diagnosis only
@bug-diagnostician "Analyze payment errors in logs/payment/"

# Fix only (when root cause known)
@patch-developer "Add null check to PaymentProcessor.java:147"

# Testing only
@hotfix-tester "Test payment-fix branch in staging"

# Deployment only
@deployment-coordinator "Deploy payment-fix to production with canary"

# Post-incident only
@incident-analyzer "Create RCA for 2024-01-15 payment incident"
```

### Orchestrated Workflow

Use multiple agents in sequence for complete incident response:

```
# Complete hot-fix workflow
"Production incident: 45% payment failures. Execute complete hot-fix workflow:
1. Diagnose root cause
2. Develop minimal patch
3. Test thoroughly
4. Deploy with canary
5. Create post-incident RCA

Use all hot-fix agents in sequence. Provide complete documentation trail."
```

### Emergency Triage

For P0 incidents, prioritize speed:

```
# Fast-track for critical outages
"URGENT P0: Complete service outage.
Diagnose immediately (target: 10 minutes).
If not immediately fixable, recommend rollback.
Speed is critical - get us operational first."
```

---

## Cost Analysis

**Per P0 Incident (Complete Lifecycle)**:

| Agent | Model | Approx Tokens | Cost |
|-------|-------|---------------|------|
| bug-diagnostician | Sonnet | 8K in / 3K out | ~$0.25 |
| patch-developer | Sonnet | 10K in / 2K out | ~$0.28 |
| hotfix-tester | Haiku | 6K in / 2K out | ~$0.02 |
| deployment-coordinator | Sonnet | 12K in / 4K out | ~$0.40 |
| incident-analyzer | Sonnet | 15K in / 8K out | ~$0.60 |
| **TOTAL PER INCIDENT** | | | **~$1.55** |

**Cost Savings**:
- Prevents hours of manual debugging
- Reduces MTTR (Mean Time To Resolution)
- Systematic approach reduces errors
- Knowledge captured for future incidents

**ROI**: One prevented hour of downtime (at $10K/hour) pays for 6,400+ incident responses.

---

## Monitoring & Metrics

Track plugin effectiveness:

### Speed Metrics
- Mean Time To Detect (MTTD)
- Mean Time To Resolve (MTTR)
- Diagnosis time
- Fix development time
- Deployment time

### Quality Metrics
- Hot-fix success rate (% without rollback)
- Regression introduction rate
- Rollback frequency
- Action item completion rate (from RCAs)

### Learning Metrics
- RCAs produced per incident
- Prevention measures implemented
- Runbooks created
- Knowledge base articles generated

---

## Troubleshooting

### Issue: Diagnosis taking too long

**Solutions**:
- Ensure logs are accessible and well-structured
- Use grep/search efficiently (see bug-diagnosis skill)
- Focus on recent changes first
- Binary search for when issue started

### Issue: Patch not working in production

**Causes**:
- Testing didn't catch edge case
- Production data different from test data
- Configuration difference between environments

**Recovery**:
1. Rollback immediately
2. Investigate why patch failed
3. Update patch and retest
4. Retry deployment

### Issue: Rollback failing

**Prevention**:
- Always test rollback BEFORE deployment
- Document exact rollback commands
- Keep previous version artifacts available
- Practice rollback procedures regularly

---

## Future Enhancements

### Planned Features
- [ ] Automated incident detection and triage
- [ ] Integration with monitoring systems (Datadog, New Relic)
- [ ] Auto-rollback on metric threshold violations
- [ ] Pattern matching against incident knowledge base
- [ ] Chaos engineering integration for prevention

### Potential Skills to Add
- `patch-development/SKILL.md`: Hot-fix safety patterns
- `hotfix-testing/SKILL.md`: Emergency testing strategies
- `deployment-strategy/SKILL.md`: Production rollout patterns
- `incident-analysis/SKILL.md`: Advanced RCA methodology

---

## Related Plugins

- **DevOps Engineer**: Infrastructure and deployment automation
- **Backend Developer**: Long-term fixes after hot-fixes
- **Site Reliability Engineer**: Monitoring and reliability engineering
- **Database Architect**: Database-related incident response

---

## References

- [Google SRE Book - Incident Management](https://sre.google/sre-book/managing-incidents/)
- [Atlassian Incident Management](https://www.atlassian.com/incident-management)
- [PagerDuty Incident Response Guide](https://response.pagerduty.com/)
- [Etsy Blameless Post-Mortems](https://www.etsy.com/codeascraft/blameless-postmortems)

---

## License

Part of Puerto Plugin Collection
MIT License

---

**Created**: 2024-01-XX
**Version**: 1.0.0
**Maintainer**: Puerto Team
**Status**: Production Ready ✅
