# SRE Practices Skill

**Expert patterns for Site Reliability Engineering: monitoring, incident response, performance optimization, and capacity planning**

## Core Principles

1. **Reliability**: Systems should meet SLOs while enabling velocity
2. **Automation**: Toil reduction through automation
3. **Observability**: Comprehensive monitoring, logging, and tracing
4. **Blameless Culture**: Learn from incidents, don't blame
5. **Error Budgets**: Balance reliability with innovation

---

## Google SRE Fundamentals

### SLIs (Service Level Indicators)

**Quantitative measures of service behavior**:

```
Common SLIs:
- Availability: % of successful requests
- Latency: % of requests < threshold (e.g., 95% < 200ms)
- Throughput: Requests per second
- Error Rate: % of failed requests
- Data Freshness: Age of data
- Durability: % of data retained

Examples:
✅ GOOD - Measurable, user-centric:
"99.9% of requests complete successfully"
"95% of API requests respond in < 200ms"
"99.99% of data writes are durable"

❌ BAD - Vague, not user-centric:
"Server is fast"
"System is reliable"
"Database works well"
```

**SLI Calculation**:
```python
# Availability SLI
availability = successful_requests / total_requests * 100

# Latency SLI (95th percentile < 200ms)
latency_sli = requests_under_200ms / total_requests * 100

# Error Rate SLI
error_rate = failed_requests / total_requests * 100
success_rate = 100 - error_rate
```

### SLOs (Service Level Objectives)

**Target values for SLIs over a time window**:

```
Format: [SLI] [Target] over [Time Window]

Examples:
✅ GOOD:
"99.9% availability over 30 days"
"95% of requests < 200ms over 7 days"
"99.95% of writes durable over 90 days"
"Error rate < 0.1% over 24 hours"

Time Windows:
- 24 hours: Real-time services
- 7 days: Weekly review cadence
- 30 days: Standard (most common)
- 90 days: Long-term trends
```

**SLO Selection Matrix**:

| Service Tier | Availability | Latency (p95) | Error Rate |
|--------------|--------------|---------------|------------|
| Critical | 99.99% | < 100ms | < 0.01% |
| High | 99.9% | < 200ms | < 0.1% |
| Standard | 99.5% | < 500ms | < 0.5% |
| Best Effort | 99% | < 1s | < 1% |

### SLAs (Service Level Agreements)

**Customer-facing contracts with consequences**:

```
Structure:
1. Service covered
2. Target (usually more lenient than internal SLO)
3. Measurement method
4. Consequences if violated (credits, refunds)

Example:
"API Availability SLA:
- Target: 99.9% uptime per month
- Measurement: Successful API responses / Total requests
- Credits:
  - 99.9% - 99.5%: 10% service credit
  - 99.5% - 99.0%: 25% service credit
  - < 99.0%: 50% service credit"

Rule: SLA < SLO (internal)
Example:
- SLA: 99.9% (customer promise)
- SLO: 99.95% (internal target, buffer for safety)
```

### Error Budgets

**Allowable downtime/errors within SLO**:

```
Calculation:
Error Budget = 100% - SLO

Examples:

99.9% SLO (30 days):
- Error Budget: 0.1%
- Allowed Downtime: 43 minutes/month
- Allowed Errors: 0.1% of requests

99.95% SLO (30 days):
- Error Budget: 0.05%
- Allowed Downtime: 21.6 minutes/month
- Allowed Errors: 0.05% of requests

99.99% SLO (30 days):
- Error Budget: 0.01%
- Allowed Downtime: 4.32 minutes/month
- Allowed Errors: 0.01% of requests
```

**Error Budget Policies**:
```markdown
Budget > 50%: ✅ Green
- Ship new features aggressively
- Take calculated risks
- Focus on velocity

Budget 20-50%: ⚠️ Yellow
- Balance features and reliability
- Increase testing coverage
- Review risky changes

Budget < 20%: 🚨 Red
- Feature freeze (except reliability)
- Focus on stability
- Postmortems for all incidents
- Increase monitoring

Budget Exhausted: 🛑 Critical
- Complete feature freeze
- All hands on reliability
- Executive escalation
- Recovery plan required
```

---

## Monitoring and Observability

### The Three Pillars

**1. Metrics** (Time-series data):
```
System Metrics:
- CPU usage, memory, disk I/O
- Network traffic, packet loss
- Process counts, file descriptors

Application Metrics:
- Request rate, latency, error rate
- Active connections, queue depth
- Business metrics (orders, signups)

Format:
metric_name{label1="value1", label2="value2"} value timestamp

Example (Prometheus):
http_requests_total{method="GET", status="200"} 1234 1642680000
api_latency_seconds{endpoint="/users", percentile="0.95"} 0.15 1642680000
```

**2. Logs** (Discrete events):
```json
// Structured logging (JSON)
{
  "timestamp": "2025-01-20T10:30:15.123Z",
  "level": "ERROR",
  "service": "api-server",
  "traceId": "abc-123-def-456",
  "userId": "user-789",
  "endpoint": "/api/users/123",
  "method": "GET",
  "statusCode": 500,
  "latency": 523,
  "error": "Database connection timeout",
  "stack": "...",
  "metadata": {
    "region": "us-east-1",
    "pod": "api-server-5f7c8b-xyz"
  }
}
```

**Log Levels**:
```
DEBUG: Detailed diagnostic info (verbose)
INFO: General informational messages
WARN: Warning conditions (degraded but functional)
ERROR: Error conditions (operation failed)
FATAL: Critical errors (service crash)

Production: INFO and above
Debugging: DEBUG and above
```

**3. Traces** (Request flow):
```
Distributed tracing shows request path through services:

User Request → API Gateway → Auth Service → User Service → Database
   100ms          10ms          20ms          50ms         40ms

Trace ID: abc-123-def-456
Total: 120ms (including parallel calls)

Identifies:
- Slow services
- Bottlenecks
- Failed dependencies
- N+1 queries
```

### Golden Signals (USE Method)

**Latency**:
```
Measure response time distribution:
- p50 (median): 50th percentile
- p95: 95th percentile (good UX threshold)
- p99: 99th percentile (worst cases)
- p99.9: 99.9th percentile (tail latency)

Example:
p50: 50ms   ← Most requests
p95: 150ms  ← SLO threshold
p99: 300ms  ← Outliers
p99.9: 1s   ← Worst cases
```

**Traffic**:
```
Measure demand on system:
- Requests per second (RPS)
- Concurrent connections
- Bandwidth utilization

Patterns:
- Baseline: Normal traffic level
- Peak: Maximum expected
- Spike: Sudden increase
- Anomaly: Unexpected pattern
```

**Errors**:
```
Measure failure rate:
- 4xx errors: Client errors
- 5xx errors: Server errors
- Timeout errors
- Circuit breaker trips

Error Budget Impact:
1000 requests, 5 errors = 0.5% error rate
If SLO is 99.9% (0.1% error budget), this exceeds budget!
```

**Saturation**:
```
Measure resource utilization:
- CPU: % utilized
- Memory: % used
- Disk: % full, IOPS
- Network: % bandwidth
- Database: Connection pool usage

Warning thresholds:
- 70%: Monitor closely
- 80%: Capacity planning needed
- 90%: Urgent action required
- 95%: Imminent failure
```

### Alerting Best Practices

**Alert Fatigue Prevention**:
```
✅ GOOD Alerts (actionable):
"API error rate > 1% for 5 minutes"
"Disk usage > 90% on prod-db-01"
"Pod restart count > 5 in 10 minutes"

❌ BAD Alerts (noise):
"CPU spike for 10 seconds" (too sensitive)
"Single 500 error" (not statistically significant)
"Disk usage > 50%" (too early, not urgent)

Alert Criteria:
1. Actionable: Can operator do something?
2. Urgent: Requires immediate attention?
3. Real: Actual problem, not false positive?
4. User-Impacting: Affects customers?
```

**Alert Severity Levels**:
```
P0 - Critical (Page):
- Service completely down
- Data loss occurring
- Security breach
- SLA violation imminent
Response: Immediate (5 minutes)

P1 - High (Notify):
- Significant degradation
- Error budget burning fast
- Multiple components affected
Response: Within 30 minutes

P2 - Medium (Ticket):
- Minor degradation
- Single component affected
- Approaching thresholds
Response: Within 4 hours

P3 - Low (Info):
- Informational
- Trends to watch
- Capacity planning
Response: Next business day
```

**Alert Runbook Template**:
```markdown
## Alert: API Error Rate High

### Trigger
Error rate > 1% for 5 minutes

### Impact
- Users experiencing failed requests
- Error budget consumption: 10x normal

### Investigation Steps
1. Check error dashboard: [link]
2. Review recent deployments: `kubectl rollout history`
3. Check dependency health: [service status page]
4. Examine error logs: `kubectl logs -l app=api --tail=100`

### Common Causes
1. Recent deployment introduced bug
2. Database connection pool exhausted
3. Downstream service degraded
4. Rate limiting triggered

### Resolution Steps
1. If recent deployment, rollback:
   `kubectl rollout undo deployment/api-server`
2. If database issue, restart connection pool:
   `kubectl exec -it api-server-xxx -- kill -USR1 1`
3. If downstream service, enable circuit breaker:
   `kubectl set env deployment/api-server CIRCUIT_BREAKER_ENABLED=true`

### Escalation
- After 15 minutes: Page SRE lead
- After 30 minutes: Incident commander
- Contact: #incidents Slack channel
```

---

## Incident Management

### Incident Response Lifecycle

**1. Detection** (MTTD - Mean Time To Detect):
```
Automated:
- Alert fires from monitoring
- Health check fails
- User-reported (tickets, social media)

Goal: < 5 minutes for critical issues

Improve detection:
- Comprehensive monitoring
- Synthetic monitoring (canaries)
- User session monitoring
- Anomaly detection
```

**2. Response** (MTTR - Mean Time To Respond):
```
Immediate Actions:
1. Acknowledge alert (stop paging others)
2. Assess severity (P0/P1/P2/P3)
3. Declare incident if needed
4. Assemble response team
5. Create incident channel (#incident-123)

Roles:
- Incident Commander: Coordinates response
- Technical Lead: Investigates and fixes
- Communications Lead: Updates stakeholders
- Scribe: Documents timeline
```

**3. Triage** (MTTK - Mean Time To Know):
```
Investigation:
1. Gather symptoms
   - What's broken?
   - When did it start?
   - What changed recently?

2. Check dashboards
   - Error rates
   - Latency
   - Resource utilization

3. Review logs and traces
   - Error messages
   - Stack traces
   - Correlation IDs

4. Form hypothesis
   - What's the root cause?
   - Can we verify?
```

**4. Mitigation** (MTTR - Mean Time To Resolve):
```
Fix or Mitigate:
1. Quick mitigation (restore service)
   - Rollback deployment
   - Scale resources
   - Disable feature
   - Failover to backup

2. Monitor impact
   - Is service restored?
   - Are errors decreasing?
   - Are customers unblocked?

3. Document actions taken

Goal: Service restored < 30 minutes for P0
```

**5. Resolution** (Permanent Fix):
```
After Service Restored:
1. Implement permanent fix
2. Verify fix in staging
3. Deploy to production
4. Monitor closely
5. Confirm resolution
6. Close incident
```

**6. Postmortem** (Learning):
```
Blameless Postmortem Template:

# Incident Postmortem: API Outage 2025-01-20

## Summary
API service was unavailable for 45 minutes affecting 10,000 users.

## Timeline
| Time | Event |
|------|-------|
| 10:00 | Deploy v2.3.0 to production |
| 10:15 | Error rate spike to 80% |
| 10:17 | Alert fired, SRE paged |
| 10:20 | Incident declared (P0) |
| 10:25 | Root cause identified: database migration failed |
| 10:30 | Rollback initiated |
| 10:35 | Service restored |
| 10:45 | Confirmed all systems healthy |

## Root Cause
Database migration script contained invalid SQL that locked the users table.

## Impact
- 45 minutes downtime
- 10,000 users affected
- 500,000 failed requests
- 43.2 minutes of 99.9% SLO error budget consumed (100%)
- Estimated revenue impact: $50,000

## What Went Well
✅ Alert fired quickly (2 minutes)
✅ Team responded promptly
✅ Rollback procedure worked smoothly
✅ Communication was clear and frequent

## What Went Wrong
❌ Database migration not tested in staging
❌ No automated rollback for failed migrations
❌ Deployment at peak traffic time
❌ Insufficient pre-deploy validation

## Action Items
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| Add database migration tests to CI | @jane | 2025-01-27 | Open |
| Implement automatic migration rollback | @john | 2025-02-03 | Open |
| Establish deployment windows (off-peak) | @sre-lead | 2025-01-22 | Open |
| Add migration validation step to deploy | @jane | 2025-01-27 | Open |
| Update runbook with rollback procedure | @john | 2025-01-24 | Open |

## Lessons Learned
1. Test migrations thoroughly in staging
2. Avoid deployments during peak hours
3. Add validation gates before production
4. Automated rollback is critical

---
No blame, only learning and improvement.
```

### Incident Severity Matrix

```
P0 - Critical:
- Complete service outage
- Data loss or corruption
- Security breach
- Revenue-impacting
Response: Immediate, all hands
Example: "Website down, all users affected"

P1 - High:
- Major feature unavailable
- Significant user impact
- SLO violation
- Escalating issue
Response: Within 15 minutes
Example: "Login failing for 30% of users"

P2 - Medium:
- Minor feature degraded
- Small user subset affected
- Performance degradation
- Approaching SLO
Response: Within 1 hour
Example: "Image upload slow for mobile users"

P3 - Low:
- Cosmetic issues
- Minimal impact
- Non-urgent
Response: Next business day
Example: "Typo in email template"
```

---

## Toil Reduction

### What is Toil?

```
Toil = Manual, repetitive, automatable work with no enduring value

Examples of Toil:
❌ Manual deployment to production
❌ Restarting services when they crash
❌ Manually provisioning servers
❌ Copying data between environments
❌ Responding to the same alerts repeatedly
❌ Manual log analysis for common issues

NOT Toil:
✅ Incident response (requires human judgment)
✅ Architecture design
✅ Code review
✅ Postmortem analysis
✅ Capacity planning
```

### Toil Budget

```
SRE teams should spend:
- < 50% time on toil
- > 50% time on engineering (automation, improvements)

Measure Toil:
toil_percentage = toil_hours / total_working_hours * 100

If toil > 50%:
1. Identify top toil sources
2. Prioritize automation
3. Reduce manual processes
4. Improve tooling
```

### Automation Opportunities

**Deployment Automation**:
```bash
# Before (Manual Toil):
# 1. SSH to server
# 2. Pull latest code
# 3. Stop service
# 4. Run migrations
# 5. Start service
# 6. Check logs
# Total: 30 minutes per deploy

# After (Automated):
./deploy.sh production v2.3.0
# Total: 2 minutes
```

**Alert Remediation**:
```python
# Auto-remediation for common issues
REMEDIATION_MAP = {
    "disk_space_low": "clean_old_logs",
    "memory_high": "restart_leaky_service",
    "connection_pool_exhausted": "scale_up_connections",
}

def auto_remediate(alert_name):
    if alert_name in REMEDIATION_MAP:
        action = REMEDIATION_MAP[alert_name]
        log(f"Auto-remediating {alert_name} with {action}")
        execute(action)
        monitor_for_recovery()
    else:
        page_human()
```

**Provisioning Automation**:
```yaml
# Infrastructure as Code (Terraform)
resource "aws_instance" "web_server" {
  count         = 5
  ami           = "ami-12345678"
  instance_type = "t3.medium"

  tags = {
    Name = "web-server-${count.index}"
    Team = "platform"
  }
}

# One command to create 5 servers:
terraform apply
```

---

## Capacity Planning

### Forecasting Methodology

**1. Historical Analysis**:
```
Examine past growth:
- Traffic trends (daily, weekly, seasonal)
- Resource utilization over time
- Storage growth rate
- User growth rate

Example:
Monthly Active Users:
- Jan: 10,000
- Feb: 12,000 (+20%)
- Mar: 14,000 (+16.7%)
- Apr: 17,000 (+21.4%)

Average growth: ~19% per month
Forecast: 17,000 * 1.19 = 20,230 users in May
```

**2. Organic Growth**:
```python
# Linear projection
future_load = current_load * (1 + monthly_growth_rate) ** months

# Example: 1000 RPS growing 15% monthly
current = 1000
growth = 0.15
months = 6

future = current * (1 + growth) ** months
# = 1000 * 1.15^6 = 2313 RPS in 6 months
```

**3. Launch Planning**:
```
New Feature Launch:
1. Estimate adoption rate (conservative, expected, optimistic)
2. Load per user
3. Peak vs average
4. Cache hit rate
5. Database queries per request

Example:
Feature: Real-time notifications
- Adoption: 30% of 100K users = 30K
- WebSocket connections: 30K concurrent
- Message rate: 10/minute/user = 5K messages/second
- Infrastructure needed: 50 servers @ 600 connections each
```

**4. Seasonality**:
```
Account for predictable patterns:
- Holiday traffic (e-commerce)
- Tax season (finance)
- Back to school (education)
- Business hours (B2B)

Example:
Black Friday traffic: 10x normal
Need: 10x capacity ready by Nov 1
Lead time: 1 month for procurement
Action: Order by Oct 1
```

### Resource Planning

**CPU Sizing**:
```
Current: 1000 RPS @ 60% CPU (10 cores)
Expected: 2000 RPS in 6 months

CPU needed: (2000 / 1000) * 60% = 120% of 10 cores = 12 cores
With 30% buffer: 12 * 1.3 = 15.6 cores → 16 cores

Decision: Scale from 10 to 16 cores by month 5
```

**Memory Sizing**:
```
Current: 32 GB RAM, 70% utilized, 1M users
Expected: 2M users in 12 months

Assumption: Linear scaling
Memory needed: 32 GB * (2M / 1M) * 0.7 / 0.7 = 64 GB
With 20% buffer: 64 * 1.2 = 76.8 GB → 80 GB

Decision: Upgrade to 80 GB RAM by month 10
```

**Storage Sizing**:
```
Current: 1 TB, growing 50 GB/month
Forecast: 1 TB + (50 GB * 12) = 1.6 TB in 12 months

With 50% buffer: 1.6 TB * 1.5 = 2.4 TB
Add compression (2x): 2.4 TB / 2 = 1.2 TB actual

Decision: Plan for 2 TB storage (comfortable headroom)
```

### Capacity Triggers

**Proactive Scaling Thresholds**:
```
Green (< 60% utilization):
- Monitor trends
- Normal operations

Yellow (60-70% utilization):
- Plan capacity increase
- Review projections

Orange (70-85% utilization):
- Accelerate scaling plans
- Optimize inefficiencies

Red (85-95% utilization):
- Emergency capacity addition
- Throttle non-critical traffic

Critical (> 95% utilization):
- Immediate action required
- Risk of service degradation
```

---

## Performance Optimization

### Performance Budget

```
Define acceptable limits:
- Time to First Byte (TTFB): < 200ms
- First Contentful Paint (FCP): < 1s
- Largest Contentful Paint (LCP): < 2.5s
- Time to Interactive (TTI): < 3.5s
- Total Page Load: < 5s

API Performance:
- p50 latency: < 50ms
- p95 latency: < 200ms
- p99 latency: < 500ms
```

### Optimization Strategies

**1. Latency Reduction**:
```
Techniques:
✅ Caching (Redis, CDN)
✅ Database query optimization (indexes, N+1 prevention)
✅ Connection pooling
✅ Async processing (queues)
✅ Load balancing
✅ Geographic distribution (edge locations)
✅ Protocol optimization (HTTP/2, gRPC)

Example: Cache hot data
Before: 500ms (database query)
After: 5ms (Redis cache)
Speedup: 100x
```

**2. Throughput Increase**:
```
Techniques:
✅ Horizontal scaling (more servers)
✅ Vertical scaling (bigger servers)
✅ Batch processing
✅ Compression
✅ Connection keep-alive
✅ Request pipelining

Example: Horizontal scaling
Before: 1 server @ 1000 RPS
After: 5 servers @ 1000 RPS each = 5000 RPS total
Throughput: 5x
```

**3. Resource Utilization**:
```
CPU Optimization:
- Profile hot paths (flame graphs)
- Optimize algorithms (O(n²) → O(n log n))
- Reduce unnecessary computation
- Use appropriate data structures

Memory Optimization:
- Fix memory leaks
- Reduce object allocations
- Use object pooling
- Implement pagination
- Stream large datasets

Example: Memory leak fix
Before: Memory grows 1GB/hour, restart daily
After: Stable memory, no restarts needed
Savings: 24 manual restarts/month eliminated
```

### Performance Testing

**Load Testing**:
```bash
# Simulate production traffic
# Tool: k6, Gatling, JMeter

# k6 example
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '5m', target: 1000 },  // Ramp to 1000 users
    { duration: '10m', target: 1000 }, // Stay at 1000
    { duration: '5m', target: 0 },     // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95% < 500ms
    http_req_failed: ['rate<0.01'],    // < 1% errors
  },
};

export default function () {
  let response = http.get('https://api.example.com/users');
  check(response, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });
  sleep(1);
}
```

**Stress Testing**:
```
Push system beyond limits:
1. Find breaking point
2. Observe failure mode
3. Improve resilience

Example:
Expected capacity: 10K RPS
Test with: 15K RPS
Result: Degrades gracefully (500ms → 2s, no crashes)
Conclusion: Good failure mode, adjust capacity trigger
```

**Soak Testing**:
```
Run at sustained load:
Duration: 24-72 hours
Goal: Find memory leaks, resource exhaustion

Example:
Load: 5K RPS for 48 hours
Monitor: Memory, CPU, disk, connections
Look for: Gradual degradation, leaks, accumulation
```

---

## Chaos Engineering

### Principles

```
1. Build a hypothesis around steady state behavior
2. Vary real-world events
3. Run experiments in production
4. Automate experiments
5. Minimize blast radius
```

### Common Experiments

**1. Instance Failure**:
```bash
# Randomly terminate pods
# Tool: Chaos Monkey, Chaos Mesh

# Does system recover?
# Is failover automatic?
# Do users notice?

kubectl delete pod -l app=api-server --random-one
```

**2. Network Latency**:
```bash
# Inject latency to dependencies
# Tool: Toxiproxy, Chaos Mesh

# Add 500ms latency to database
toxiproxy-cli toxic add \
  --type latency \
  --attribute latency=500 \
  db_proxy

# Does circuit breaker activate?
# Are timeouts appropriate?
# Does fallback work?
```

**3. Resource Exhaustion**:
```bash
# Fill disk, exhaust memory, max CPU
# Tool: stress-ng

stress-ng --cpu 8 --vm 4 --vm-bytes 8G --timeout 60s

# Does monitoring alert?
# Does auto-scaling trigger?
# Do health checks fail correctly?
```

**4. Dependency Failure**:
```bash
# Simulate downstream service outage

# Block traffic to payment service
iptables -A OUTPUT -d payment-service -j DROP

# Does circuit breaker open?
# Are errors handled gracefully?
# Is fallback behavior acceptable?
```

---

## SRE Metrics

### Availability Metrics

**Uptime**:
```
uptime_percentage = (total_time - downtime) / total_time * 100

Example (30 days):
Total time: 43,200 minutes
Downtime: 43 minutes
Uptime: (43,200 - 43) / 43,200 * 100 = 99.9%
```

**MTBF** (Mean Time Between Failures):
```
MTBF = total_uptime / number_of_failures

Example (90 days):
Total uptime: 129,557 minutes
Failures: 3
MTBF = 129,557 / 3 = 43,186 minutes (30 days)
```

**MTTR** (Mean Time To Repair):
```
MTTR = total_downtime / number_of_incidents

Example:
Incident 1: 45 minutes
Incident 2: 20 minutes
Incident 3: 15 minutes
MTTR = (45 + 20 + 15) / 3 = 27 minutes
```

**Error Budget Burn Rate**:
```
Burn Rate = Actual Error Rate / Allowed Error Rate

Example:
SLO: 99.9% (error budget: 0.1%)
Actual error rate: 0.5%
Burn Rate = 0.5% / 0.1% = 5x

At 5x burn rate:
- 30-day budget will be exhausted in 6 days
- Immediate action required!

Alerting:
- 1x: Normal
- 2x: Warning (budget will exhaust in 15 days)
- 5x: Critical (budget will exhaust in 6 days)
- 10x: Emergency (budget will exhaust in 3 days)
```

---

## Tools and Technologies

### Monitoring Tools

**Prometheus** (Metrics):
```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'api-server'
    static_configs:
      - targets: ['localhost:9090']
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance

# PromQL queries
# Error rate
rate(http_requests_total{status=~"5.."}[5m])

# 95th percentile latency
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# Availability
sum(rate(http_requests_total{status="200"}[5m]))
/
sum(rate(http_requests_total[5m]))
```

**Grafana** (Visualization):
```json
{
  "dashboard": {
    "title": "API Server Health",
    "panels": [
      {
        "title": "Request Rate",
        "targets": [
          {
            "expr": "rate(http_requests_total[5m])"
          }
        ]
      },
      {
        "title": "Error Rate",
        "targets": [
          {
            "expr": "rate(http_requests_total{status=~\"5..\"}[5m])"
          }
        ]
      }
    ]
  }
}
```

**ELK Stack** (Logs):
```json
// Elasticsearch query
{
  "query": {
    "bool": {
      "must": [
        { "match": { "level": "ERROR" } },
        { "range": { "@timestamp": { "gte": "now-1h" } } }
      ]
    }
  },
  "aggs": {
    "errors_by_service": {
      "terms": { "field": "service.keyword" }
    }
  }
}
```

**Datadog** (All-in-one):
```python
# Application instrumentation
from datadog import statsd

# Increment counter
statsd.increment('api.requests', tags=['endpoint:/users', 'method:GET'])

# Record latency
statsd.histogram('api.latency', request_duration, tags=['endpoint:/users'])

# Set gauge
statsd.gauge('api.connections', active_connections)
```

**PagerDuty** (Incident Management):
```python
# Trigger incident
import pdpyras

session = pdpyras.APISession(API_KEY)
session.trigger_incident(
    service_id='SERVICE_ID',
    title='API Error Rate High',
    severity='critical',
    details={'error_rate': '5%', 'duration': '10 minutes'}
)
```

---

## Best Practices Checklist

**Monitoring & Alerting**:
- [ ] SLIs defined and measured
- [ ] SLOs documented and tracked
- [ ] Error budgets calculated and monitored
- [ ] Alerts are actionable and non-noisy
- [ ] Runbooks exist for all alerts
- [ ] Dashboards for all services
- [ ] On-call rotation defined

**Incident Management**:
- [ ] Incident response process documented
- [ ] Roles defined (IC, TL, Comms)
- [ ] Postmortem template ready
- [ ] Blameless culture enforced
- [ ] Action items tracked to completion

**Performance**:
- [ ] Performance budgets defined
- [ ] Regular load testing
- [ ] Optimization roadmap
- [ ] Caching strategy implemented
- [ ] Database queries optimized

**Capacity**:
- [ ] Growth forecasts updated quarterly
- [ ] Capacity triggers defined
- [ ] Scaling playbooks documented
- [ ] Lead times for procurement known
- [ ] Budget allocated for growth

**Automation**:
- [ ] Toil measured and tracked
- [ ] Automation roadmap prioritized
- [ ] Deployment fully automated
- [ ] Auto-remediation for common issues
- [ ] Infrastructure as Code

**Resilience**:
- [ ] Chaos experiments running regularly
- [ ] Circuit breakers implemented
- [ ] Graceful degradation tested
- [ ] Disaster recovery plan documented
- [ ] Regular DR drills conducted

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: SRE practices, monitoring, incident response, performance optimization, capacity planning
