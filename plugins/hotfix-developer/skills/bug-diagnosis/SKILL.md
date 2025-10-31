# Bug Diagnosis Skill

## Overview
Expert knowledge for rapid root cause identification in production incidents. This skill covers systematic debugging approaches, log analysis techniques, and critical thinking patterns for time-sensitive bug diagnosis.

## Core Debugging Methodologies

### 1. The Scientific Method for Debugging

**Observe** → **Hypothesize** → **Test** → **Conclude**

1. **Observe**: What is actually happening? (errors, symptoms, metrics)
2. **Hypothesize**: What could cause this behavior?
3. **Test**: Can I reproduce it? Does evidence support hypothesis?
4. **Conclude**: Is this the root cause or a symptom?

### 2. 5 Whys Root Cause Analysis

Keep asking "Why?" until you reach the systemic root cause:

```
Why did the system fail?
→ Because service crashed

Why did service crash?
→ Because of out-of-memory error

Why was there out-of-memory?
→ Because of memory leak

Why was there a memory leak?
→ Because connections weren't being closed

Why weren't connections closed?
→ Because error handling skipped cleanup

ROOT CAUSE: Error handling doesn't include resource cleanup
```

**Common Mistakes**:
- ❌ Stopping at first technical cause (service crashed)
- ❌ Blaming individuals (developer forgot to close connections)
- ✅ Finding systemic issue (error handling pattern missing cleanup)

### 3. Binary Search Debugging

When bug started between two known states:

```
Known Good ──────────────────────────── Known Bad
     ↓                                         ↓
   v1.0                                     v2.0

Step 1: Test v1.5 (midpoint)
  → Bug present? Search v1.0 to v1.5
  → Bug absent? Search v1.5 to v2.0

Step 2: Continue bisecting until exact change found
```

Use `git bisect` for code-related bugs:
```bash
git bisect start
git bisect bad HEAD  # Current version has bug
git bisect good v1.0  # v1.0 was working
# Git will checkout middle commits for testing
```

## Log Analysis Techniques

### Pattern Recognition

#### Error Rate Patterns

**Sudden Spike** (0% → 50% in seconds):
- Likely: Deployment, config change, dependency failure
- Search for: Recent deployments, config commits

**Gradual Increase** (0.1% → 1% → 5% over hours):
- Likely: Resource exhaustion, memory leak, disk filling
- Search for: Resource metrics, connection pools

**Intermittent Errors** (5% baseline, random):
- Likely: Race condition, timeout, distributed system issue
- Search for: Concurrent requests, timing-related logs

#### Temporal Analysis

```bash
# Find when errors started
grep ERROR logs/app.log | head -1
# → 2024-01-15 14:22:47

# What happened just before? (deployment, config, traffic spike)
git log --since="2024-01-15 14:00" --until="2024-01-15 14:25"
grep "deployed\|config changed" logs/system.log
```

### Stack Trace Analysis

**Anatomy of a Stack Trace**:
```
Exception: NullPointerException at PaymentProcessor.java:147
  at com.example.PaymentProcessor.processPayment(PaymentProcessor.java:147)
  at com.example.CheckoutController.checkout(CheckoutController.java:89)
  at javax.servlet.http.HttpServlet.service(HttpServlet.java:646)
  ...
```

**Reading Strategy**:
1. **Exception Type**: What went wrong? (NullPointerException)
2. **Error Location**: Where in OUR code? (PaymentProcessor.java:147)
3. **Call Path**: How did we get there? (CheckoutController → PaymentProcessor)
4. **Ignore Framework**: Focus on your code, not servlet internals

**Common Exceptions and Causes**:
- `NullPointerException`: Missing null check, unexpected null value
- `OutOfMemoryError`: Memory leak, insufficient heap, large data
- `TimeoutException`: Slow dependency, network issue, infinite loop
- `ConnectionRefusedError`: Service down, wrong host/port, firewall
- `DeadlockException`: Circular lock dependency, poor locking strategy

### Log Correlation

**Correlate across multiple sources**:

```bash
# Application logs
grep "request_id=abc123" app.log

# Database logs
grep "abc123" db/query.log

# Load balancer logs
grep "abc123" lb/access.log

# Timeline across all systems
cat app.log db/query.log lb/access.log | grep "abc123" | sort
```

## Common Bug Patterns

### Pattern 1: Null/Undefined Reference
**Symptoms**: NullPointerException, undefined is not a function
**Common Causes**:
- Database query returned no results
- API response missing expected field
- Optional parameter not provided

**Diagnosis**:
```bash
# Find the null access
grep -A 5 "NullPointerException" logs/error.log

# Check what should have value
# Look for: user.paymentMethod.token
# Ask: When is user.paymentMethod null?
```

### Pattern 2: Resource Exhaustion
**Symptoms**: Out of memory, too many connections, disk full
**Common Causes**:
- Memory leak (unclosed resources)
- Connection pool exhausted
- Disk not cleaned up

**Diagnosis**:
```bash
# Memory growth over time
grep "heap usage" logs/metrics.log | awk '{print $3}'

# Connection pool status
grep "active connections" logs/db.log

# Disk usage
df -h /var/log
```

### Pattern 3: Race Condition
**Symptoms**: Intermittent failures, non-reproducible, timing-dependent
**Common Causes**:
- Multiple threads accessing shared state
- Async operations completing out of order
- Database transaction isolation issues

**Diagnosis**:
- Look for concurrent access patterns
- Check if error rate correlates with traffic
- Test with different concurrency levels

### Pattern 4: Configuration Error
**Symptoms**: Works in staging, fails in production
**Common Causes**:
- Environment variable mismatch
- Feature flag difference
- External dependency configuration

**Diagnosis**:
```bash
# Compare configurations
diff staging.env production.env

# Check feature flags
curl https://api.com/flags

# Verify external endpoints
curl https://external-api.com/health
```

### Pattern 5: Dependency Failure
**Symptoms**: External API errors, database timeouts, service unavailable
**Common Causes**:
- Downstream service degraded
- API version incompatibility
- Network connectivity issue

**Diagnosis**:
```bash
# Check dependency health
curl https://payment-api.com/health

# Test connectivity
ping payment-api.com
telnet payment-api.com 443

# Check error logs for API errors
grep "payment-api" logs/error.log
```

## Impact Assessment Framework

### User Impact Calculation

```
User Impact = (Affected Users / Total Users) × Severity Factor

Severity Factors:
- Complete failure: 1.0
- Degraded experience: 0.5
- Minor inconvenience: 0.2
```

**Example**:
- Total daily users: 10,000
- Checkout failures: 4,500 users
- Complete failure (can't checkout)
- Impact: (4,500 / 10,000) × 1.0 = 45% severe impact

### Business Impact Quantification

```
Revenue Impact = Failed Transactions × Average Order Value × Duration (hours) × Conversion Recovery Rate

Recovery Rate: % of users who retry later
- P0 incidents: ~30% recovery (users leave)
- P1 incidents: ~60% recovery
- P2 incidents: ~80% recovery
```

**Example**:
- Failed transactions: ~500
- Average order: $25
- Duration: 0.37 hours (22 min)
- Recovery: 30% (70% leave)
- Revenue loss: 500 × $25 × 0.37 × 0.70 = ~$3,200

### Severity Classification

| Severity | Criteria | Response Time | Example |
|----------|----------|---------------|---------|
| **P0** | Critical outage, >25% users affected | < 15 min | Core service down, payment completely broken |
| **P1** | Major impact, 5-25% users affected | < 30 min | Feature broken, high error rate |
| **P2** | Moderate impact, <5% users affected | < 60 min | Edge case failures, minor degradation |
| **P3** | Low impact, minimal user effect | < 4 hours | Cosmetic issues, rare edge cases |

## Debugging Tools & Commands

### Log Analysis
```bash
# Find errors in time window
grep ERROR app.log | awk '$1 >= "14:20" && $1 <= "14:30"'

# Count error types
grep ERROR app.log | awk -F: '{print $2}' | sort | uniq -c | sort -rn

# Find most common error
grep ERROR app.log | cut -d' ' -f4- | sort | uniq -c | sort -rn | head -5

# Extract stack traces
awk '/^Exception/,/^[[:space:]]*$/' logs/error.log
```

### Code Search
```bash
# Find where variable is accessed
grep -r "user\.paymentMethod" src/

# Find function definitions
grep -r "def processPayment" src/

# Find recent changes to file
git log -p --since="1 week ago" -- src/PaymentProcessor.java
```

### System Inspection
```bash
# Memory usage
free -m
ps aux | sort -k4 -rn | head -10

# Disk usage
df -h
du -sh /var/* | sort -rh

# Network connections
netstat -an | grep ESTABLISHED | wc -l
lsof -i :8080

# Process inspection
ps aux | grep java
jstack <pid>  # Java thread dump
```

## Critical Thinking Checklist

When diagnosing a production bug, ask:

- [ ] **What changed recently?** (deployments, config, dependencies)
- [ ] **Can I reproduce it?** (consistently, intermittently, not at all)
- [ ] **What's the timing?** (sudden, gradual, periodic)
- [ ] **What's the scope?** (all users, specific region, specific feature)
- [ ] **What's the error rate?** (100%, 50%, 5%, 0.1%)
- [ ] **Are there similar past incidents?** (check incident history)
- [ ] **What's different in prod vs staging?** (config, data, scale)
- [ ] **What do the metrics show?** (CPU, memory, latency, errors)
- [ ] **What evidence supports my hypothesis?** (logs, traces, metrics)
- [ ] **Am I assuming or do I have proof?** (mark assumptions clearly)

## Red Herrings to Avoid

**Common False Leads**:
1. **Correlation ≠ Causation**: Errors started at 2pm, deployment at 1:55pm
   - Maybe deployment caused it... or maybe traffic spike at 2pm
   - Need evidence, not just timing

2. **Confirmation Bias**: Found one error that matches hypothesis
   - But is it THE cause or A symptom?
   - Check if fixing it would prevent the issue

3. **Recency Bias**: Most recent change must be the cause
   - Sometimes bugs from weeks ago manifest suddenly
   - Check full history, not just latest changes

4. **Framework Internals**: Stack trace shows framework error
   - Focus on YOUR code that called the framework
   - Framework bugs are rare, misuse is common

## Speed vs. Thoroughness Balance

**For P0 (Critical)**:
- Speed priority: 80% confidence is enough
- Get it working first, understand fully later
- Diagnosis target: 15 minutes

**For P1 (Major)**:
- Balanced: 90% confidence before acting
- Understand enough to avoid making it worse
- Diagnosis target: 30 minutes

**For P2 (Moderate)**:
- Thoroughness priority: 95% confidence
- Full understanding prevents future issues
- Diagnosis target: 60 minutes

## Documentation Standards

Every diagnosis should capture:

1. **Symptoms**: What users experienced
2. **Evidence**: Logs, traces, metrics that led to root cause
3. **Root Cause**: Specific, actionable cause (not vague)
4. **Impact**: Quantified user and business impact
5. **Fix Direction**: What needs to change (not exact code)
6. **Testing Needs**: How to verify fix works

**Good Root Cause**: "PaymentProcessor.processPayment() accesses user.paymentMethod.token without null check, throws NullPointerException when user has no payment method saved"

**Bad Root Cause**: "Code has a bug" (too vague)

## Learning from Patterns

After each incident, update your mental model:
- What pattern was this? (null, race, config, dependency)
- Have I seen this before?
- What was the early signal I missed?
- How could I diagnose faster next time?

Build a personal runbook of common patterns in your system.
