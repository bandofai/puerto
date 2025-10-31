# Observability Skill

**Comprehensive monitoring, logging, alerting, and tracing patterns**

## The Three Pillars of Observability

1. **Metrics**: Numerical measurements over time
2. **Logs**: Discrete events with context
3. **Traces**: Request flow through distributed system

## The Four Golden Signals (Google SRE)

| Signal | What | Why | Target |
|--------|------|-----|--------|
| **Latency** | Time to process requests | User experience | p95 < 200ms, p99 < 500ms |
| **Traffic** | Demand on system | Capacity planning | Baseline + 20% headroom |
| **Errors** | Failed requests | Reliability | <0.1% error rate |
| **Saturation** | How "full" system is | Performance degradation | <70% CPU/memory |

## RED Method (Services)

- **Rate**: Requests per second
- **Errors**: Failed requests per second
- **Duration**: Time per request (latency distribution)

```promql
# Rate
sum(rate(http_requests_total[5m])) by (service)

# Errors
sum(rate(http_requests_total{status=~"5.."}[5m])) by (service)

# Duration (p95)
histogram_quantile(0.95,
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service)
)
```

## USE Method (Resources)

- **Utilization**: % time resource is busy
- **Saturation**: Queue length or waiting
- **Errors**: Error count

```promql
# CPU Utilization
100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Memory Utilization
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# Disk Saturation
rate(node_disk_io_time_seconds_total[5m])
```

## Metrics Collection

### Prometheus Instrumentation (Python)
```python
from prometheus_client import Counter, Histogram, Gauge

# Counters (always increasing)
http_requests_total = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

# Histograms (latency distribution)
http_request_duration_seconds = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration',
    ['method', 'endpoint'],
    buckets=[0.001, 0.01, 0.1, 0.5, 1, 2, 5, 10]
)

# Gauges (current value)
active_connections = Gauge(
    'active_connections',
    'Number of active connections'
)

# Usage
@app.route('/api/users')
def get_users():
    start = time.time()
    active_connections.inc()

    try:
        users = db.query("SELECT * FROM users")
        http_requests_total.labels('GET', '/api/users', '200').inc()
        return jsonify(users), 200
    except Exception as e:
        http_requests_total.labels('GET', '/api/users', '500').inc()
        raise
    finally:
        duration = time.time() - start
        http_request_duration_seconds.labels('GET', '/api/users').observe(duration)
        active_connections.dec()
```

### Key Metrics to Track

**Application Metrics**:
```python
# Business metrics
orders_total = Counter('orders_total', 'Total orders', ['status'])
revenue_total = Counter('revenue_total', 'Total revenue in cents')
active_users = Gauge('active_users', 'Currently active users')

# Performance metrics
db_query_duration = Histogram('db_query_duration_seconds', 'Database query time')
cache_hit_rate = Gauge('cache_hit_rate', 'Percentage of cache hits')
queue_length = Gauge('queue_length', 'Number of items in queue')
```

**System Metrics** (Node Exporter):
- CPU: `node_cpu_seconds_total`
- Memory: `node_memory_MemAvailable_bytes`
- Disk: `node_disk_io_time_seconds_total`
- Network: `node_network_receive_bytes_total`

## Structured Logging

### JSON Logging Pattern
```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }

        # Add custom fields
        if hasattr(record, 'user_id'):
            log_obj['user_id'] = record.user_id
        if hasattr(record, 'request_id'):
            log_obj['request_id'] = record.request_id
        if hasattr(record, 'trace_id'):
            log_obj['trace_id'] = record.trace_id

        if record.exc_info:
            log_obj['exception'] = self.formatException(record.exc_info)

        return json.dumps(log_obj)

# Usage
logger = logging.getLogger('myapp')
logger.info(
    'User login successful',
    extra={'user_id': 123, 'request_id': 'abc-123', 'ip': '10.0.1.5'}
)
```

### Log Levels
```
CRITICAL: System is unusable (disk full, OOM)
ERROR:    Operation failed (database connection lost)
WARNING:  Something unexpected (retry succeeded, deprecated API used)
INFO:     Normal operations (user logged in, order placed)
DEBUG:    Detailed diagnostic (SQL queries, API calls)
```

### What to Log
```python
# ✅ DO log
logger.info('User logged in', extra={'user_id': user.id, 'ip': request.ip})
logger.error('Payment failed', extra={'order_id': order.id, 'error': str(e)})
logger.warning('API rate limit approaching', extra={'api_key': key, 'usage': 95})

# ❌ DON'T log
logger.info('Password: ' + password)  # NEVER log secrets
logger.debug('SSN: ' + ssn)           # NEVER log PII
logger.info('In function foo')        # Too noisy, use DEBUG
```

## SLI/SLO/SLA Hierarchy

### Service Level Indicators (SLIs)
Quantitative measures of service quality:
```
- Availability: % of successful requests
- Latency: p50, p95, p99 response time
- Throughput: Requests per second
- Correctness: % of correct results
```

### Service Level Objectives (SLOs)
Targets for SLIs:
```yaml
slos:
  availability:
    target: 99.9%        # 3 nines
    window: 30 days      # Rolling window
    error_budget: 43.2m  # 30d * 0.1% = 43.2 minutes

  latency:
    target: p95 < 200ms
    window: 30 days

  error_rate:
    target: < 0.1%
    window: 30 days
```

### Error Budget
```
Error Budget = 100% - SLO

If SLO = 99.9%:
  Error Budget = 0.1%
  In 30 days = 43.2 minutes downtime
  In 1 day = 1.44 minutes = 86 seconds
```

### Error Budget Policy
```
If error budget > 50%:
  ✅ Ship new features aggressively
  ✅ Experiment with new technologies
  ✅ Take calculated risks

If error budget < 50%:
  ⚠️  Slow down feature velocity
  ⚠️  Focus on reliability
  ⚠️  Fix known issues

If error budget exhausted:
  🛑 Feature freeze
  🛑 Focus ONLY on reliability
  🛑 Postmortems for incidents
```

## Alert Design

### Alert Philosophy
**Alerts should be**: Actionable, not informational

```
❌ BAD:  "CPU > 50%" (What should I do?)
✅ GOOD: "CPU > 80% for 10 minutes" (Investigate performance)

❌ BAD:  "Disk usage > 50%" (No urgency)
✅ GOOD: "Disk will fill in < 24 hours" (Add capacity)
```

### Alert Severity Levels
```yaml
CRITICAL:
  - User-facing service down
  - Data loss occurring
  - Security breach detected
  Action: Page on-call immediately

HIGH:
  - SLO burn rate high (will exhaust error budget)
  - Degraded performance (p95 latency > threshold)
  - Approaching capacity (disk 85% full)
  Action: Notify during business hours

MEDIUM:
  - Non-critical service issues
  - Warning thresholds reached
  Action: Create ticket

LOW:
  - Informational
  - Metrics trending in wrong direction
  Action: Review in weekly meeting
```

### Alert Rules (Prometheus)
```yaml
groups:
- name: slo_alerts
  rules:
  # Fast burn (1h window): 14.4x error budget consumption
  - alert: SLOBurnRateTooFast
    expr: |
      (
        1 - (
          sum(rate(http_requests_total{status!~"5.."}[1h]))
          /
          sum(rate(http_requests_total[1h]))
        )
      ) > (0.001 * 14.4)
    labels:
      severity: critical
    annotations:
      summary: "Error budget exhausting rapidly"
      description: "At this rate, error budget will be gone in 2 hours"
      runbook: "https://wiki/runbooks/slo-burn-rate"

  # Slow burn (6h window): 6x error budget consumption
  - alert: SLOBurnRateElevated
    expr: |
      (
        1 - (
          sum(rate(http_requests_total{status!~"5.."}[6h]))
          /
          sum(rate(http_requests_total[6h]))
        )
      ) > (0.001 * 6)
    for: 15m
    labels:
      severity: warning
    annotations:
      summary: "Error budget consumption elevated"
      description: "Error budget will exhaust in 5 days at this rate"
```

### Alert Runbooks
```markdown
# Runbook: High Error Rate

## Symptoms
- Error rate > 5%
- Users reporting 500 errors
- SLO burn rate elevated

## Diagnosis
1. Check recent deployments
   ```bash
   kubectl rollout history deployment/myapp
   ```

2. Check application logs
   ```bash
   kubectl logs -l app=myapp --tail=100
   ```

3. Check upstream dependencies
   - Database: `SELECT 1` test query
   - Redis: PING command
   - External APIs: Health check endpoints

## Resolution
If recent deployment:
  ```bash
  kubectl rollout undo deployment/myapp
  ```

If database issue:
  - Check connections: `SHOW PROCESSLIST`
  - Check slow queries
  - Scale read replicas if needed

If external API issue:
  - Enable circuit breaker
  - Use fallback/cached data

## Prevention
- Add more integration tests
- Implement canary deployment
- Add circuit breakers for external deps
```

## Distributed Tracing

### OpenTelemetry Pattern
```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

# Setup tracing
trace.set_tracer_provider(TracerProvider())
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

tracer = trace.get_tracer(__name__)

# Instrument code
@app.route('/api/order')
def create_order():
    with tracer.start_as_current_span("create_order") as span:
        span.set_attribute("user_id", user_id)

        # Database call
        with tracer.start_as_current_span("db_insert_order"):
            order = db.insert_order(data)

        # Call payment service
        with tracer.start_as_current_span("payment_service_charge"):
            payment = payment_service.charge(order.total)

        # Send notification
        with tracer.start_as_current_span("send_email"):
            email.send_confirmation(order)

        return jsonify(order)
```

### Trace Context Propagation
```python
# Extract trace context from incoming request
from opentelemetry.propagate import extract

context = extract(request.headers)

with tracer.start_as_current_span("handle_request", context=context):
    # Your code here
    pass

# Inject trace context into outgoing request
from opentelemetry.propagate import inject

headers = {}
inject(headers)
requests.post("http://api/endpoint", headers=headers)
```

## Dashboard Design

### Service Overview Dashboard
```
┌─────────────────────────────────────────┐
│ Service Health: myapp                   │
├─────────────────────────────────────────┤
│ Request Rate (RPS)          [Graph]     │
│ Error Rate (%)              [Graph]     │
│ Latency (p50, p95, p99)     [Graph]     │
│ Active Instances            [Gauge]     │
├─────────────────────────────────────────┤
│ SLO Status                              │
│ ├─ Availability: 99.95% ✅ (target 99.9%)│
│ ├─ Latency p95: 180ms ✅ (target <200ms)│
│ └─ Error budget: 75% remaining ✅       │
└─────────────────────────────────────────┘
```

### Resource Dashboard
```
┌─────────────────────────────────────────┐
│ Resource Utilization                    │
├─────────────────────────────────────────┤
│ CPU Usage (%)               [Graph]     │
│ Memory Usage (%)            [Graph]     │
│ Disk I/O (ops/sec)          [Graph]     │
│ Network Traffic (MB/s)      [Graph]     │
└─────────────────────────────────────────┘
```

## Retention Policies

```yaml
metrics:
  raw: 15 days          # Full resolution
  5m_avg: 90 days       # Downsampled
  1h_avg: 2 years       # Long-term trends

logs:
  hot: 7 days           # Fast search
  warm: 30 days         # Slower search
  cold: 1 year          # Archive

traces:
  sampled: 7 days       # 1% sample rate
  errors: 30 days       # 100% error traces
```

## Best Practices Summary

✅ **DO**:
- Implement The Four Golden Signals
- Use structured (JSON) logging
- Define SLOs and track error budget
- Make alerts actionable with runbooks
- Use distributed tracing for microservices
- Monitor business metrics, not just technical
- Set up dashboards before incidents
- Review and tune alerts regularly

❌ **DON'T**:
- Log sensitive data (passwords, PII, SSNs)
- Create alerts for everything (alert fatigue)
- Use high-cardinality labels (user IDs, IPs)
- Ignore SLO violations
- Monitor without acting on data
- Create dashboards no one uses
- Set alerts without runbooks

---

**Version**: 1.0.0
**Patterns**: Google SRE Workbook-based
