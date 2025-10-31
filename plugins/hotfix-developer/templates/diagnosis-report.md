# Incident Diagnosis Report

## Incident Summary
- **Incident ID**: [AUTO-GENERATED or TICKET-NUMBER]
- **Severity**: P0 / P1 / P2 / P3
- **Start Time**: [YYYY-MM-DD HH:MM:SS UTC]
- **Detection Time**: [YYYY-MM-DD HH:MM:SS UTC] (time we became aware)
- **Status**: Active / Mitigated / Resolved
- **Diagnosed By**: [Agent/Engineer name]
- **User Impact**: [X% of users / specific feature / geographic region]

## Symptoms

### User-Facing Issues
[What users are experiencing]
- Example: "Users cannot complete checkout"
- Example: "Payment button shows error message"
- Example: "Page loads but shows blank screen"

### System Behavior
[What the system is doing abnormally]
- Example: "Error rate jumped from 0.3% to 45%"
- Example: "Response time increased from 200ms to 8s"
- Example: "Service returning 500 errors"

### Affected Components
[Which services/features are impacted]
- [ ] Component 1
- [ ] Component 2
- [ ] Component 3

## Evidence Collected

### Error Logs

**Source**: [path/to/log/file or monitoring system]

**Sample Errors** (with timestamps):
```
[2024-01-15 14:22:47] ERROR: NullPointerException in PaymentProcessor
  at com.example.PaymentProcessor.processPayment(PaymentProcessor.java:147)
  ...

[2024-01-15 14:23:15] ERROR: Payment processing failed for user 12345
  Caused by: java.lang.NullPointerException
  ...
```

**Error Pattern**:
- First occurrence: [timestamp]
- Frequency: [X errors/minute]
- Trend: [Increasing / Stable / Decreasing]
- Total count: [~X errors]

### Stack Traces

**Most Common Stack Trace**:
```
[Paste full stack trace here]
```

**Key Observations**:
- Exception type: [e.g., NullPointerException]
- Error location: [file:line - your code, not framework]
- Call path: [How we got there]

### Metrics

| Metric | Baseline | During Incident | Change |
|--------|----------|----------------|--------|
| Error Rate | 0.3% | 45% | +44.7% ⬆️ |
| Response Time (p95) | 250ms | 320ms | +28% ⬆️ |
| Request Volume | 1000/min | 950/min | -5% ⬇️ |
| [Custom Metric] | [baseline] | [current] | [change] |

### Recent Changes

**Deployments** (last 24 hours):
```bash
2024-01-15 14:15:00 - payment-service v2.3.1 deployed to production
  Commit: abc123def
  Changes: Updated Stripe integration, refactored payment processor
```

**Configuration Changes**:
```
2024-01-15 12:00:00 - Feature flag enabled: use_new_payment_flow=true (25% rollout)
```

**Infrastructure Changes**:
```
[Any scaling events, database migrations, dependency updates]
```

**External Factors**:
```
[Traffic spikes, third-party service outages, DDoS attempts]
```

## Root Cause Analysis (5 Whys)

1. **Why did users experience checkout failures?**
   → [Answer]

2. **Why [answer from #1]?**
   → [Answer]

3. **Why [answer from #2]?**
   → [Answer]

4. **Why [answer from #3]?**
   → [Answer]

5. **Why [answer from #4]?**
   → [ROOT CAUSE]

**Root Cause**: [Clear, specific statement of the underlying cause]

**Contributing Factors**:
1. [Factor that made root cause more likely or severe]
2. [Another contributing factor]
3. [Another contributing factor]

## Root Cause (Summary)

[Concise, actionable statement of what went wrong]

**Example**: "The PaymentProcessor.processPayment() method accesses user.paymentMethod.token at line 147 without checking if paymentMethod is null. When users have no saved payment method, this throws NullPointerException, causing checkout to fail."

**Evidence Supporting This Conclusion**:
- Stack trace shows NPE at PaymentProcessor.java:147
- Code review confirms no null check at that line
- Error rate matches deployment time of new payment code
- Only affects users without saved payment methods (45% of attempts)

## Impact Assessment

### User Impact
- **Total Users Affected**: [~X users or Y% of user base]
- **Affected User Segments**: [All users / New users / Premium users / Geographic region]
- **Severity for Users**: Critical (can't use service) / Major (degraded) / Minor (inconvenience)
- **Duration**: [X minutes/hours]

### Business Impact
- **Revenue Loss** (estimated): $[X,XXX]
  - Calculation: [show your work]
  - Example: 500 failed orders × $25 avg × 70% abandonment = $8,750

- **Reputation Impact**:
  - Support tickets: [X tickets]
  - Social media mentions: [X complaints]
  - Public visibility: Low / Medium / High

- **SLA Impact**:
  - Uptime SLA: [X% - breach or within target]
  - Performance SLA: [within/outside target]

### Technical Impact
- **Scope**: Single feature / Multiple features / Entire service / Multiple services
- **Systems Affected**: [list of services/databases/components]
- **Data Loss**: None / Partial / Significant
- **Downtime**: Full (100%) / Partial (X%) / Degraded

## Recommended Fix

### Approach
[Rollback / Patch / Configuration Change / Data Fix]

**Specific Actions**:
1. [First action]
2. [Second action]
3. [Third action]

**Example**:
```
Approach: Patch

Actions:
1. Add null check before accessing paymentMethod.token
2. Return clear error message if payment method missing
3. Log occurrence for monitoring
```

### Complexity
- [ ] Simple (one-line fix, low risk)
- [ ] Moderate (multiple files, medium risk)
- [ ] Complex (architectural change, high risk)

### Risk Level
- [ ] Low (well-understood fix, easy rollback)
- [ ] Medium (some unknowns, rollback tested)
- [ ] High (complex interactions, difficult rollback)

### Estimated Time to Fix
- **Development**: [X minutes/hours]
- **Testing**: [X minutes/hours]
- **Deployment**: [X minutes/hours]
- **Total**: [X minutes/hours]

**Confidence**: [High / Medium / Low]

## Testing Requirements

Before deploying fix, validate:

- [ ] **Fix Validation**: Verify fix resolves original issue
  - Test case: [Specific scenario that was failing]

- [ ] **Regression Testing**: Ensure no new issues introduced
  - Test areas: [list specific features to test]

- [ ] **Performance Testing**: No performance degradation
  - Metric to watch: [response time, error rate, etc.]

- [ ] **Backwards Compatibility**: Works with existing data
  - Test with: [old data formats, legacy clients]

- [ ] **Edge Cases**: Handle null, invalid, missing data
  - Test scenarios: [list edge cases]

## Deployment Strategy

**Recommended Approach**: Canary / Blue-Green / Rolling / Immediate Rollback

**Phasing**:
1. Phase 1: [10% traffic, 10 minutes monitoring]
2. Phase 2: [50% traffic, 10 minutes monitoring]
3. Phase 3: [100% traffic]

**Rollback Criteria**:
- Error rate > [X%]
- Response time > [Xms]
- [Custom metric] exceeds [threshold]

## Timeline

| Time | Event | Notes |
|------|-------|-------|
| 14:15:00 | Deployment started | payment-service v2.3.1 |
| 14:22:47 | First error logged | NullPointerException |
| 14:23:15 | Error rate climbing | 0.5% → 2% → 8% |
| 14:25:03 | Alert fired | Error rate > 5% threshold |
| 14:25:30 | On-call paged | 27 seconds to page |
| 14:27:15 | Investigation started | Engineer began debugging |
| 14:32:45 | Root cause identified | Null check missing |
| [CURRENT] | Diagnosis complete | Awaiting fix development |

## Next Steps

1. **Immediate**: [Hand off to patch-developer for fix implementation]
2. **Short-term**: [Monitoring plan while fix is being developed]
3. **Follow-up**: [Post-incident review scheduled]

## Appendix

### Additional Evidence
[Any supplementary logs, screenshots, or data]

### Hypotheses Considered and Rejected
1. **Hypothesis**: [What you thought might be the cause]
   - **Why rejected**: [Evidence that disproved this]

2. **Hypothesis**: [Another theory]
   - **Why rejected**: [Why this wasn't the root cause]

### References
- Incident ticket: [LINK]
- Monitoring dashboard: [LINK]
- Deployment record: [LINK]
- Similar past incidents: [LINK]

---

**Diagnosis completed at**: [YYYY-MM-DD HH:MM:SS UTC]
**Diagnosis duration**: [X minutes]
**Handoff to**: patch-developer / deployment team / [other]
