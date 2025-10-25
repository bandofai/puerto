# Site Reliability Engineer Plugin

System reliability and uptime specialist for monitoring setup, incident response, performance optimization, capacity planning, and post-mortem analysis following Google SRE principles.

## Overview

The Site Reliability Engineer plugin provides agents for maintaining high availability, reducing MTTR (Mean Time To Recovery), improving system performance, and planning capacity using SRE best practices and SLO/SLI frameworks.

## Agents

### 1. monitoring-architect (Sonnet, Skill-Aware)
Designs comprehensive monitoring systems with metrics, logs, traces, and alerts based on SLIs/SLOs.

**Use for**: Monitoring strategy, SLO definition, alerting rules, observability setup

**Example**:
```
Use monitoring-architect to set up monitoring for e-commerce platform.
Services: Web app, API, database, cache, queue
SLOs to define:
- Availability: 99.9% uptime (43 minutes downtime/month)
- Latency: 95th percentile < 200ms
- Error rate: < 0.1% requests
Monitoring stack: Prometheus, Grafana, Loki, Jaeger
Alerts:
- Page on-call for SLO violations
- Warning alerts for trending issues
- Resource utilization thresholds
```

### 2. incident-responder (Sonnet, Skill-Aware)
Manages incident response with runbooks, escalation procedures, and communication protocols.

**Use for**: Incident triage, response coordination, runbook execution, stakeholder communication

**Example**:
```
Use incident-responder for database outage incident.
Incident: Primary database unresponsive
Severity: SEV-1 (customer-facing outage)
Actions:
1. Incident declaration and war room setup
2. Failover to replica (runbook: db-failover-001)
3. Investigate primary DB (disk full, OOM, network?)
4. Customer communication (status page update)
5. Restore primary and verify replication
Timeline: Every action timestamped for post-mortem
```

### 3. performance-optimizer (Sonnet, Skill-Aware)
Optimizes system performance through profiling, bottleneck identification, and tuning.

**Use for**: Performance analysis, optimization, bottleneck removal, latency reduction

**Example**:
```
Use performance-optimizer to improve API latency.
Current state: P95 latency 800ms (SLO: <200ms)
Analysis:
- Profile requests (APM data)
- Identify slow queries (N+1, missing indexes)
- Find external API bottlenecks
- Check resource constraints (CPU, memory, I/O)
Optimizations:
- Database query optimization (indexes, query rewrite)
- Caching strategy (Redis for frequently accessed data)
- Connection pooling tuning
- Async processing for non-critical work
Target: P95 <150ms (margin for growth)
```

### 4. capacity-planner (Sonnet, Skill-Aware)
Plans infrastructure capacity based on growth projections, resource utilization, and cost optimization.

**Use for**: Capacity forecasting, resource planning, cost optimization, scaling strategy

**Example**:
```
Use capacity-planner for 3-month capacity plan.
Current usage:
- Web servers: 60% CPU, 70% memory (10 instances)
- Database: 75% CPU, 80% disk (read replica needed)
- Cache: 50% memory (16GB allocated)
Growth forecast: 30% user growth over 3 months
Capacity plan:
- Add 4 web servers (14 total) - provision at 70% usage
- Add read replica for database - offload 40% of reads
- Increase cache to 32GB - handle growth + reduce DB load
- Cost: $2K/month increase vs $10K revenue increase
Include: Scaling triggers, lead times, cost projections
```

## Skills

### sre-practices
Google SRE principles and practices:
- **SLIs/SLOs/SLAs**: Service Level Indicators, Objectives, Agreements
- **Error Budget**: Acceptable downtime based on SLO (99.9% = 43 min/month)
- **Toil Reduction**: Automate repetitive operational work
- **Blameless Post-Mortems**: What happened, why, how to prevent (no blame)
- **Monitoring**: The Four Golden Signals (latency, traffic, errors, saturation)
- **Alerting**: Symptom-based alerts (not cause-based), actionable, low false positives
- **Incident Management**: Severity levels, escalation, communication, documentation
- **On-Call**: Rotation, handoffs, escalation paths, burnout prevention
- **Capacity Planning**: Forecasting, headroom (20-30%), organic vs inorganic growth
- **Performance**: Profiling, optimization, resource utilization

## Templates

### monitoring-setup-template.md
Monitoring architecture: SLI/SLO definitions, metrics to collect (Four Golden Signals), alerting rules with thresholds, dashboard design, on-call rotation.

### incident-runbook-template.md
Incident runbook: Symptoms, severity classification, investigation steps, mitigation actions, escalation procedures, recovery verification, rollback steps.

### post-mortem-template.md
Blameless post-mortem: Incident summary, timeline (all actions timestamped), root cause analysis, impact assessment, action items (prevent recurrence), lessons learned.

### capacity-plan-template.md
Capacity planning document: Current utilization, growth projections, resource requirements, scaling triggers, procurement timeline, cost analysis, risk mitigation.

## Workflows

### Complete SRE Setup
```
1. Define SLOs
Use monitoring-architect to set availability, latency, error rate SLOs

2. Setup monitoring
Use monitoring-architect to implement metrics, logs, traces, alerts

3. Create runbooks
Use incident-responder to document incident response procedures

4. Plan capacity
Use capacity-planner to forecast resource needs for 3-6 months
```

### Incident Response Workflow
```
1. Detection
Monitoring alert triggers → Incident declared

2. Response
Use incident-responder to triage, mitigate, and communicate

3. Recovery
Restore service, verify SLOs met

4. Post-Mortem
Use incident-responder to document lessons learned (blameless)

5. Prevention
Implement action items to prevent recurrence
```

## Requirements Met

✅ Role: System reliability and uptime specialist
✅ System monitoring setup: monitoring-architect with SLI/SLO framework
✅ Incident response: incident-responder with runbooks and escalation
✅ Performance optimization: performance-optimizer with profiling and tuning
✅ Capacity planning: capacity-planner with forecasting and scaling
✅ Post-mortem analysis: Covered in incident-responder and templates
✅ Tools: Monitoring tools (guidance), Bash (system commands), Cloud APIs

## Key Features

✓ **SLI/SLO Framework**: Define and measure reliability
✓ **Error Budget**: Acceptable downtime based on SLO
✓ **Four Golden Signals**: Latency, traffic, errors, saturation
✓ **Blameless Post-Mortems**: Learning-focused incident reviews
✓ **Toil Reduction**: Automate repetitive work
✓ **On-Call Best Practices**: Rotation, escalation, burnout prevention
✓ **Capacity Forecasting**: Resource planning with 20-30% headroom
✓ **Performance Optimization**: Profiling, bottleneck removal

## SRE Metrics

### Availability
- **Uptime**: % of time service is available
- **SLO**: 99.9% (43 min/month), 99.95% (22 min/month), 99.99% (4.3 min/month)
- **Error Budget**: 100% - SLO = acceptable downtime

### Incident Response
- **MTTR**: Mean Time To Recovery (target: <30 minutes for SEV-1)
- **MTTD**: Mean Time To Detect (target: <5 minutes)
- **Incident Frequency**: SEV-1 incidents per month (target: <2)

### Performance
- **Latency**: P50, P95, P99 response times
- **Throughput**: Requests per second (RPS)
- **Error Rate**: % of failed requests (target: <0.1%)
- **Resource Utilization**: CPU, memory, disk, network (target: 60-70% for headroom)

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

## SLO Best Practices

### Defining SLOs
- **Start with users**: What do users care about? (availability, latency)
- **Measure what matters**: Use SLIs that reflect user experience
- **Be realistic**: 100% is impossible and too expensive
- **Allow error budget**: Use budget for releases, experiments

### Example SLOs
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

## Incident Severity Levels

- **SEV-1 (Critical)**: Customer-facing outage, revenue impact, security breach
  - Response: Immediate, page on-call, all-hands
  - MTTR target: <30 minutes

- **SEV-2 (High)**: Degraded service, subset of users affected
  - Response: Within 15 minutes, notify manager
  - MTTR target: <2 hours

- **SEV-3 (Medium)**: Minor degradation, workaround available
  - Response: Next business day
  - MTTR target: <1 business day

- **SEV-4 (Low)**: Cosmetic issue, no user impact
  - Response: Planned work
  - MTTR target: Next sprint

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 1 comprehensive sre-practices skill with Google SRE principles
- ✅ 4 professional templates for monitoring, runbooks, post-mortems, capacity
- ✅ Complete README with SLO framework and incident response

Closes #80
