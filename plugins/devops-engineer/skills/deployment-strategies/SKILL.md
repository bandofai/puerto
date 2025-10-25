# Deployment Strategies Skill

**Expert-level deployment patterns: Blue-Green, Canary, Rolling, and Progressive Delivery**

## Strategy Selection Matrix

| Strategy | Downtime | Rollback Speed | Resource Cost | Complexity | Use When |
|----------|----------|----------------|---------------|------------|----------|
| **Recreate** | Yes (1-5 min) | Slow | 1x | Low | Dev/staging, non-critical |
| **Rolling** | No | Medium | 1x | Low | Standard deployments |
| **Blue-Green** | No | Instant | 2x | Medium | Zero-downtime required |
| **Canary** | No | Fast | 1.1-1.5x | High | Risk mitigation critical |
| **A/B Testing** | No | N/A | 1.5x | Very High | Feature testing |

## 1. Blue-Green Deployment

### Concept
Maintain two identical environments. Switch traffic instantly between them.

```
Before: Blue (100%) ─┐
                     ├─> Load Balancer ─> Users
After:  Green (100%) ┘
```

### Implementation (Kubernetes)
```yaml
# Service switches between blue and green
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
    version: blue  # Change to 'green' to switch
  ports:
  - port: 80
    targetPort: 8080
```

### Pros
- Instant rollback (flip selector back)
- Full environment testing before switch
- Zero downtime

### Cons
- 2x infrastructure cost during deployment
- Database schema must be compatible with both versions
- Requires traffic router control

### Best For
- Financial systems (zero downtime critical)
- Applications with long-running transactions
- When instant rollback is mandatory

## 2. Canary Deployment

### Concept
Gradually shift traffic from old to new version while monitoring metrics.

```
Phase 1:  v1 (95%)  v2 (5%)   Monitor 10 min
Phase 2:  v1 (75%)  v2 (25%)  Monitor 10 min
Phase 3:  v1 (50%)  v2 (50%)  Monitor 15 min
Phase 4:  v1 (0%)   v2 (100%) Complete
```

### Implementation (Istio VirtualService)
```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: myapp
spec:
  hosts:
  - myapp.example.com
  http:
  - route:
    - destination:
        host: myapp
        subset: v1
      weight: 75
    - destination:
        host: myapp
        subset: v2
      weight: 25
```

### Automated Canary with Flagger
```yaml
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: myapp
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  service:
    port: 80
  analysis:
    interval: 1m
    threshold: 5
    maxWeight: 50
    stepWeight: 10
    metrics:
    - name: request-success-rate
      thresholdRange:
        min: 99
      interval: 1m
    - name: request-duration
      thresholdRange:
        max: 500
      interval: 1m
```

### Monitoring Decision Points
```python
# Automated go/no-go decision
def should_continue_canary(metrics):
    """Check if canary should proceed"""
    if metrics['error_rate'] > 0.01:  # >1% errors
        return False, "High error rate"

    if metrics['p95_latency'] > 500:  # >500ms p95
        return False, "High latency"

    if metrics['cpu_usage'] > 80:  # >80% CPU
        return False, "High CPU usage"

    return True, "Metrics healthy"
```

### Pros
- Gradual rollout limits blast radius
- Real production traffic testing
- Data-driven go/no-go decisions

### Cons
- Longer deployment time
- Requires sophisticated traffic routing
- Need good metrics/observability

### Best For
- High-traffic applications
- When A/B testing user behavior
- Microservices with complex dependencies

## 3. Rolling Update

### Concept
Replace instances one (or few) at a time, ensuring minimum availability.

```
Initial:  [v1] [v1] [v1] [v1]
Step 1:   [v2] [v1] [v1] [v1]
Step 2:   [v2] [v2] [v1] [v1]
Step 3:   [v2] [v2] [v2] [v1]
Final:    [v2] [v2] [v2] [v2]
```

### Implementation (Kubernetes)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 10
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 2        # Max 2 extra pods during update
      maxUnavailable: 1  # Max 1 pod down at a time
  template:
    spec:
      containers:
      - name: myapp
        image: myapp:v2.0.0
        readinessProbe:  # CRITICAL: Prevents serving before ready
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Rollback
```bash
# Automatic rollback on failure
kubectl rollout undo deployment/myapp

# Rollback to specific revision
kubectl rollout undo deployment/myapp --to-revision=3

# Pause during rollout
kubectl rollout pause deployment/myapp

# Resume
kubectl rollout resume deployment/myapp
```

### Pros
- No extra infrastructure cost
- Kubernetes native (automatic)
- Automatic rollback on health check failure

### Cons
- Slower than blue-green
- Mixed versions running simultaneously
- Partial rollout on failure

### Best For
- Most standard deployments
- Resource-constrained environments
- Stateless applications

## 4. Recreate Strategy

### Concept
Stop all old instances, start all new instances.

```
Step 1: [v1] [v1] [v1] → Stop all
Step 2: [ ]  [ ]  [ ]  → Downtime
Step 3: [v2] [v2] [v2] → Start all
```

### Implementation
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  strategy:
    type: Recreate
```

### Pros
- Simplest to implement
- No version compatibility issues
- Lowest resource usage

### Cons
- Downtime during deployment
- All-or-nothing risk

### Best For
- Development environments
- Maintenance windows
- Applications that can't run multiple versions

## Health Checks & Readiness

### Readiness vs Liveness Probes
```yaml
# Readiness: Is the app ready to serve traffic?
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
  successThreshold: 1   # Mark ready after 1 success
  failureThreshold: 3   # Mark not ready after 3 failures

# Liveness: Is the app alive (not deadlocked)?
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10
  failureThreshold: 3   # Restart after 3 failures
```

### Health Check Endpoint
```python
@app.route('/health')
def health():
    """Liveness: Is process running?"""
    return {'status': 'healthy'}, 200

@app.route('/ready')
def ready():
    """Readiness: Can we serve traffic?"""
    try:
        # Check critical dependencies
        db.execute('SELECT 1')
        redis.ping()
        return {'status': 'ready'}, 200
    except Exception as e:
        return {'status': 'not ready', 'error': str(e)}, 503
```

## Graceful Shutdown

### Signal Handling
```python
import signal
import sys

def graceful_shutdown(signum, frame):
    """Handle SIGTERM gracefully"""
    print("Received SIGTERM, shutting down gracefully...")

    # Stop accepting new connections
    server.stop()

    # Wait for in-flight requests (max 30s)
    for i in range(30):
        if active_requests == 0:
            break
        time.sleep(1)

    # Close database connections
    db.close()

    print("Shutdown complete")
    sys.exit(0)

signal.signal(signal.SIGTERM, graceful_shutdown)
```

### Kubernetes Configuration
```yaml
spec:
  containers:
  - name: myapp
    image: myapp:v2.0.0
    lifecycle:
      preStop:
        exec:
          command: ["/bin/sh", "-c", "sleep 10"]  # Wait for connection draining
  terminationGracePeriodSeconds: 30  # Max time before SIGKILL
```

## Database Migrations

### Compatible Schema Changes
```sql
-- Phase 1: Add new column (nullable)
ALTER TABLE users ADD COLUMN email VARCHAR(255);

-- Deploy v2 code (uses email if present)

-- Phase 2: Backfill data
UPDATE users SET email = username + '@example.com' WHERE email IS NULL;

-- Phase 3: Make NOT NULL
ALTER TABLE users ALTER COLUMN email SET NOT NULL;

-- Phase 4: Remove old column (if needed)
ALTER TABLE users DROP COLUMN username;
```

### Migration Strategy
1. **Expand**: Add new columns/tables (backward compatible)
2. **Migrate**: Dual-write to old and new (app changes)
3. **Contract**: Remove old columns/tables (cleanup)

## Traffic Shifting Methods

### 1. DNS-Based
```bash
# Update DNS to new version
aws route53 change-resource-record-sets --hosted-zone-id Z123 --change-batch '{
  "Changes": [{
    "Action": "UPSERT",
    "ResourceRecordSet": {
      "Name": "app.example.com",
      "Type": "A",
      "TTL": 60,
      "ResourceRecords": [{"Value": "10.0.1.100"}]
    }
  }]
}'
```
**Pros**: Simple
**Cons**: TTL-based, no fine-grained control

### 2. Load Balancer
```bash
# AWS ALB target groups
aws elbv2 modify-listener --listener-arn arn:aws:... --default-actions '[{
  "Type": "forward",
  "ForwardConfig": {
    "TargetGroups": [
      {"TargetGroupArn": "arn:aws:...:target-green", "Weight": 100}
    ]
  }
}]'
```
**Pros**: Instant switch, health checks integrated
**Cons**: Platform-specific

### 3. Service Mesh (Istio)
```yaml
# Fine-grained traffic control
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: myapp
spec:
  http:
  - match:
    - headers:
        user-type:
          exact: "beta-tester"
    route:
    - destination:
        host: myapp
        subset: v2
  - route:
    - destination:
        host: myapp
        subset: v1
      weight: 90
    - destination:
        host: myapp
        subset: v2
      weight: 10
```
**Pros**: Advanced routing (header-based, geo, etc.)
**Cons**: Complexity, learning curve

## Rollback Procedures

### Automated Rollback Triggers
```yaml
# Flagger automatic rollback
analysis:
  threshold: 3  # Failed checks before rollback
  metrics:
  - name: error-rate
    thresholdRange:
      max: 1  # >1% errors triggers rollback
  webhooks:
  - name: rollback-alert
    url: http://slack-webhook/alert
```

### Manual Rollback
```bash
# Kubernetes
kubectl rollout undo deployment/myapp

# Blue-green (switch service selector back)
kubectl patch service myapp -p '{"spec":{"selector":{"version":"blue"}}}'

# Docker Compose
docker-compose up -d --scale app-blue=3 --scale app-green=0
```

### Rollback Checklist
- [ ] Identify issue (errors, latency, business metrics)
- [ ] Execute rollback (instant switch or gradual)
- [ ] Verify metrics return to normal
- [ ] Notify team
- [ ] Post-mortem (root cause analysis)
- [ ] Fix issue before retry

## Progressive Delivery

### Feature Flags
```python
from unleash import UnleashClient

client = UnleashClient(url="http://unleash", app_name="myapp")

def new_checkout_flow(user_id):
    if client.is_enabled("new-checkout", context={"userId": user_id}):
        return checkout_v2()
    else:
        return checkout_v1()
```

**Benefits**:
- Deploy code, enable for subset
- Instant rollback (disable flag)
- A/B testing
- Kill switch

## Best Practices Summary

✅ **DO**:
- Implement readiness probes (CRITICAL)
- Test rollback procedures
- Monitor during deployment
- Gradual rollout for high-risk changes
- Automate deployment
- Have clear go/no-go criteria
- Use graceful shutdown
- Make compatible database changes

❌ **DON'T**:
- Deploy without health checks
- Ignore metrics during deployment
- Break backward compatibility
- Deploy all at once to prod
- Forget to test rollback
- Use synchronous migrations on deploy
- Deploy Friday afternoon

---

**Version**: 1.0.0
**Patterns**: Battle-tested in production
