# Site Reliability Engineer Plugin

**Expert SRE practices for monitoring, incident response, performance optimization, and capacity planning**

## Overview

This plugin provides comprehensive Site Reliability Engineering capabilities following Google SRE principles. It includes a detailed skill covering SRE fundamentals and four specialized agents for different aspects of site reliability.

## Contents

### Skills

#### 📚 SRE Practices (`skills/sre-practices/SKILL.md`)

Comprehensive SRE knowledge base covering:

- **Google SRE Fundamentals**
  - SLIs (Service Level Indicators)
  - SLOs (Service Level Objectives)
  - SLAs (Service Level Agreements)
  - Error budgets and policies

- **Monitoring & Observability**
  - The three pillars: Metrics, Logs, Traces
  - Golden signals: Latency, Traffic, Errors, Saturation
  - Alerting best practices
  - Alert runbook templates

- **Incident Management**
  - Response lifecycle (Detection → Response → Resolution)
  - Severity assessment (P0-P3)
  - Blameless postmortem templates
  - Communication strategies

- **Toil Reduction**
  - Identifying automatable work
  - Automation opportunities
  - Toil budgets

- **Capacity Planning**
  - Forecasting methodologies
  - Resource planning (CPU, memory, storage)
  - Capacity triggers and thresholds

- **Performance Optimization**
  - Performance budgets
  - Optimization strategies
  - Load testing approaches

- **Chaos Engineering**
  - Resilience testing principles
  - Common experiments

- **SRE Metrics**
  - MTBF, MTTR, availability
  - Error budget burn rate

- **Tools & Technologies**
  - Prometheus, Grafana
  - ELK Stack, Datadog
  - PagerDuty

---

### Agents

#### 1. 📊 Monitoring Architect (`agents/monitoring-architect.md`)

**Model**: Sonnet | **Tools**: Read, Write, Edit, Bash

**Use for**:
- Designing comprehensive monitoring and observability systems
- Defining SLIs, SLOs, and SLAs for services
- Creating alerting strategies and runbooks
- Configuring Prometheus and Grafana
- Setting up error budget tracking

**Deliverables**:
- Prometheus configuration with scrape targets and recording rules
- Alert rules with actionable thresholds
- Grafana dashboards (JSON)
- SLO documentation with error budgets
- Runbooks for each alert with investigation steps

**Example Usage**:
```
Design a monitoring system for our API service with:
- 99.9% availability SLO
- P95 latency < 200ms
- Comprehensive alerting with runbooks
```

---

#### 2. 🚨 Incident Responder (`agents/incident-responder.md`)

**Model**: Sonnet | **Tools**: Read, Write, Bash, Grep

**Use for**:
- Coordinating response to production incidents
- Executing runbooks during incidents
- Creating real-time incident timelines
- Writing blameless postmortems
- Tracking action items from incidents

**Deliverables**:
- Incident reports with severity assessment
- Detailed timeline of events
- Root cause analysis
- Blameless postmortem with lessons learned
- Action items with owners and due dates
- Communication templates (internal/external)

**Example Usage**:
```
We have a P0 incident - API error rate spiked to 80%.
Help coordinate incident response and create postmortem.
```

---

#### 3. ⚡ Performance Optimizer (`agents/performance-optimizer.md`)

**Model**: Sonnet | **Tools**: Read, Write, Edit, Bash, Grep

**Use for**:
- Analyzing system performance bottlenecks
- Optimizing API latency and throughput
- Database query optimization
- Implementing caching strategies
- Load testing and benchmarking
- Resource utilization optimization

**Deliverables**:
- Performance analysis report with bottlenecks identified
- Optimization recommendations (prioritized)
- Load test scripts (k6) and results
- Before/after benchmarks
- Caching strategy implementation
- Database optimization (indexes, query tuning)

**Example Usage**:
```
Our API p95 latency is 450ms, target is 200ms.
Analyze performance and recommend optimizations.
```

---

#### 4. 📈 Capacity Planner (`agents/capacity-planner.md`)

**Model**: Sonnet | **Tools**: Read, Write, Bash

**Use for**:
- Forecasting future capacity needs
- Analyzing resource utilization trends
- Creating growth projections
- Planning infrastructure scaling
- Cost optimization recommendations
- Risk assessment for capacity

**Deliverables**:
- Capacity forecast (6-12 months)
- Growth trend analysis
- Resource utilization analysis
- Scaling recommendations with timelines
- Cost impact analysis
- Cost optimization opportunities
- Risk assessment and mitigation plans

**Example Usage**:
```
We're growing 15% monthly. Forecast capacity needs
for next 6 months and provide scaling recommendations.
```

---

## Quick Start

### 1. Install the Plugin

```bash
# Copy to your Puerto plugins directory
cp -r site-reliability-engineer ~/.puerto/plugins/

# Or for project-specific
cp -r site-reliability-engineer ./plugins/
```

### 2. Verify Installation

```bash
# Check skills are available
ls ~/.claude/skills/sre-practices/

# Check agents are available
ls ~/.claude/agents/monitoring-architect.md
ls ~/.claude/agents/incident-responder.md
ls ~/.claude/agents/performance-optimizer.md
ls ~/.claude/agents/capacity-planner.md
```

### 3. Use the Agents

Agents will activate automatically based on your request:

```bash
# Monitoring
"Design monitoring for our e-commerce API"

# Incident Response
"P0 incident: Database is down, coordinate response"

# Performance
"Optimize our checkout API, it's too slow"

# Capacity
"Forecast capacity needs for Black Friday"
```

---

## Typical Workflows

### New Service Monitoring Setup

1. **@monitoring-architect**: Design SLIs/SLOs and monitoring
2. Deploy Prometheus and Grafana
3. Import dashboards and alert rules
4. **@monitoring-architect**: Create runbooks for alerts
5. Set up PagerDuty integration
6. Configure on-call rotation

### Incident Response

1. **@incident-responder**: Assess severity and declare incident
2. **@incident-responder**: Execute runbook for affected service
3. Coordinate mitigation and recovery
4. **@incident-responder**: Document timeline
5. **@incident-responder**: Write blameless postmortem
6. Track action items to completion

### Performance Investigation

1. **@performance-optimizer**: Baseline current performance
2. **@performance-optimizer**: Identify bottlenecks
3. **@performance-optimizer**: Recommend optimizations
4. Implement Priority 1 optimizations
5. **@performance-optimizer**: Run load tests
6. Validate improvements meet targets

### Capacity Planning Cycle

1. **@capacity-planner**: Analyze historical growth trends
2. **@capacity-planner**: Forecast 6-month capacity needs
3. Review recommendations with stakeholders
4. Approve budget and procurement
5. Execute scaling plan
6. **@capacity-planner**: Monthly capacity reviews

---

## SRE Metrics Dashboard

Track these key metrics for your services:

### Availability Metrics
- **Uptime %**: (Total time - Downtime) / Total time
- **MTBF**: Mean Time Between Failures
- **MTTR**: Mean Time To Repair
- **Error Budget**: Remaining budget vs consumed

### Performance Metrics
- **Latency**: p50, p95, p99 response times
- **Throughput**: Requests per second
- **Error Rate**: % of failed requests
- **Saturation**: Resource utilization %

### Operational Metrics
- **Alert Volume**: Alerts per day/week
- **Incident Count**: Incidents by severity
- **Toil Hours**: Manual work time
- **On-call Load**: Pages per shift

---

## Best Practices

### Monitoring

✅ **DO**:
- Define SLIs based on user experience
- Set realistic SLOs based on historical data
- Create actionable alerts (not noisy)
- Write runbooks for every alert
- Track error budgets actively
- Use recording rules for expensive queries

❌ **DON'T**:
- Alert on symptoms not problems
- Create alerts without clear actions
- Set unrealistic SLOs (five 9s for everything)
- Ignore error budget violations
- Skip runbook creation

### Incident Response

✅ **DO**:
- Declare incidents early (better safe than sorry)
- Assign clear roles (IC, TL, Comms)
- Document timeline in real-time
- Communicate frequently (internal + external)
- Focus on mitigation first, root cause second
- Write blameless postmortems
- Track action items to completion

❌ **DON'T**:
- Blame individuals in postmortems
- Skip postmortems for "minor" incidents
- Let action items languish
- Hide incidents from stakeholders
- Optimize for looking good vs learning

### Performance

✅ **DO**:
- Define performance budgets upfront
- Measure baseline before optimizing
- Profile to find actual bottlenecks
- Optimize highest-impact items first
- Load test before production
- Monitor continuously after changes

❌ **DON'T**:
- Optimize prematurely without data
- Ignore database query performance
- Skip caching opportunities
- Deploy without load testing
- Assume optimization worked without measuring

### Capacity

✅ **DO**:
- Review capacity monthly
- Forecast 6-12 months ahead
- Account for seasonal patterns
- Define clear scaling triggers
- Optimize costs with reserved instances
- Plan for failure scenarios

❌ **DON'T**:
- Wait until resources are exhausted
- Ignore growth trends
- Scale without cost analysis
- Over-provision "to be safe"
- Skip disaster recovery planning

---

## Example Scenarios

### Scenario 1: New Service Launch

**Situation**: Launching new user dashboard service

**Workflow**:
1. **@monitoring-architect**: "Design monitoring for user dashboard service with 99.9% availability SLO"
   - Creates SLIs/SLOs
   - Configures Prometheus scraping
   - Creates Grafana dashboards
   - Defines alert rules

2. **@capacity-planner**: "Forecast capacity for 100K users in first month"
   - Estimates resource needs
   - Plans infrastructure provisioning
   - Sets scaling triggers

3. **@performance-optimizer**: "Run load tests for 10K concurrent users"
   - Creates k6 load test script
   - Validates performance under load
   - Recommends optimizations if needed

**Result**: Service launches with comprehensive monitoring, adequate capacity, and validated performance.

---

### Scenario 2: Performance Degradation

**Situation**: API latency increased from 100ms to 500ms

**Workflow**:
1. **@performance-optimizer**: "API latency degraded to 500ms, analyze bottlenecks"
   - Analyzes metrics and logs
   - Identifies database query slowdown
   - Recommends adding indexes

2. Implement database indexes

3. **@performance-optimizer**: "Re-run load tests to validate improvement"
   - Validates latency reduced to 120ms
   - Confirms throughput maintained

**Result**: Performance restored to acceptable levels with data-driven optimizations.

---

### Scenario 3: Production Outage

**Situation**: Database connection pool exhausted, API returning errors

**Workflow**:
1. **@incident-responder**: "P0 incident: API error rate 80%, database connections exhausted"
   - Declares incident
   - Executes runbook
   - Coordinates response team

2. Technical team scales connection pool

3. Service recovers

4. **@incident-responder**: "Write postmortem for database connection pool incident"
   - Analyzes root cause
   - Documents timeline
   - Creates action items
   - Writes blameless postmortem

**Result**: Service restored, team learns from incident, prevents recurrence.

---

### Scenario 4: Growth Planning

**Situation**: Traffic growing 20% monthly, need to plan scaling

**Workflow**:
1. **@capacity-planner**: "We're growing 20% monthly, forecast capacity for Q2"
   - Analyzes historical trends
   - Projects 6-month growth
   - Calculates resource needs

2. **@capacity-planner**: "What's our scaling plan and cost impact?"
   - Recommends specific scaling actions
   - Estimates costs
   - Identifies optimization opportunities

3. Execute scaling plan with cost optimizations

**Result**: Infrastructure scales ahead of demand, costs optimized, no performance issues.

---

## Integration with Other Plugins

### With Backend Architect
- Backend Architect designs systems
- Monitoring Architect adds observability
- Performance Optimizer validates at scale

### With DevOps/Infrastructure
- Capacity Planner forecasts needs
- DevOps provisions infrastructure
- Monitoring Architect validates deployment

### With API Developer
- API Developer implements features
- Performance Optimizer benchmarks
- Monitoring Architect adds instrumentation

---

## SLO Framework

### Defining SLOs

**Start with users**: What do users care about?
- Availability: Can they access the service?
- Latency: How fast is the response?
- Correctness: Is the result accurate?

**Example SLOs**:
```
E-commerce Platform:
- Availability: 99.95% (22 min/month downtime)
- Latency: 95th percentile < 200ms
- Error rate: < 0.1% (1 in 1000 requests)

API Service:
- Availability: 99.9% (43 min/month)
- Latency: 99th percentile < 500ms
- Throughput: Handle 10,000 RPS

Background Job Processor:
- Success rate: 99.5% (0.5% job failures acceptable)
- Processing time: 95% of jobs complete in <10 minutes
```

### Error Budget

```
Error Budget = 100% - SLO

Examples:
- 99.9% SLO → 0.1% error budget → 43.2 min/month downtime
- 99.95% SLO → 0.05% error budget → 21.6 min/month downtime
- 99.99% SLO → 0.01% error budget → 4.32 min/month downtime

Budget Policies:
- Budget > 50%: Ship features aggressively
- Budget 20-50%: Balance features and reliability
- Budget < 20%: Feature freeze, focus on reliability
- Budget exhausted: All hands on reliability
```

---

## The Four Golden Signals

1. **Latency**: Time to process a request
   - Metrics: P50, P95, P99
   - SLO: P95 < 200ms

2. **Traffic**: Demand on the system
   - Metrics: Requests/second, bandwidth
   - Use for: Capacity planning

3. **Errors**: Rate of failed requests
   - Metrics: Error rate (%), 5xx errors
   - SLO: < 0.1% error rate

4. **Saturation**: How "full" the service is
   - Metrics: CPU, memory, disk, queue depth
   - Alert at: 80% for proactive scaling

---

## Incident Severity Levels

- **P0 (Critical)**: Customer-facing outage, revenue impact, security breach
  - Response: Immediate, page on-call, all-hands
  - MTTR target: <30 minutes

- **P1 (High)**: Degraded service, subset of users affected
  - Response: Within 15 minutes, notify manager
  - MTTR target: <2 hours

- **P2 (Medium)**: Minor degradation, workaround available
  - Response: Within 1 hour
  - MTTR target: <1 business day

- **P3 (Low)**: Cosmetic issue, no user impact
  - Response: Next business day
  - MTTR target: Next sprint

---

## Metrics Collection

All agents rely on metrics from monitoring systems. Ensure you have:

### Required
- **Prometheus**: Time-series metrics
- **Logs**: Structured logging (JSON preferred)
- **APM**: Application performance monitoring

### Recommended
- **Grafana**: Visualization and dashboards
- **Alertmanager**: Alert routing and notification
- **PagerDuty**: Incident management
- **Distributed Tracing**: Request flow visibility

### Optional but Valuable
- **ELK Stack**: Centralized logging
- **Datadog**: All-in-one observability
- **New Relic**: APM and monitoring
- **Sentry**: Error tracking

---

## Resources

### Google SRE Books (Free Online)
- Site Reliability Engineering: https://sre.google/sre-book/table-of-contents/
- The Site Reliability Workbook: https://sre.google/workbook/table-of-contents/
- Building Secure and Reliable Systems: https://sre.google/books/building-secure-reliable-systems/

### Tools Documentation
- Prometheus: https://prometheus.io/docs/
- Grafana: https://grafana.com/docs/
- k6 Load Testing: https://k6.io/docs/
- PagerDuty: https://support.pagerduty.com/

### Community
- SRE Weekly Newsletter: https://sreweekly.com/
- r/sre: https://reddit.com/r/sre
- CNCF SIG Observability: https://github.com/cncf/sig-observability

---

## License

MIT License - See LICENSE file for details

---

**Remember**: The goal of SRE is to balance reliability with velocity. Use these tools to build systems that are reliable enough to enable rapid innovation, not so reliable they slow everything down.

**"Hope is not a strategy. Luck is not a factor. Fear is not an option."**
— Google SRE Motto
