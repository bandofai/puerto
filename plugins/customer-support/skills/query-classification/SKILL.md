# Query Classification Skill

## Purpose

Accurately classify customer queries for optimal routing and resolution efficiency.

## Classification Framework

### Query Types

#### 1. Technical Issues

**Indicators**: Error messages, system problems, feature malfunctions, integration failures

**Keywords**: error, bug, broken, not working, failed, crash, down, slow, timeout, 401, 404, 500

**Examples**:
- "API returning 401 unauthorized errors"
- "Dashboard loading very slowly"
- "Integration with Salesforce not syncing"
- "Getting 'connection timeout' error"

**Default Urgency**: Medium (unless service down)

---

#### 2. Billing Inquiries

**Indicators**: Payment issues, subscription questions, invoice problems, refund requests

**Keywords**: invoice, payment, charge, refund, billing, subscription, credit card, upgrade, downgrade, pricing

**Examples**:
- "Was charged twice this month"
- "How do I upgrade my subscription?"
- "Need invoice for last month"
- "Request refund for unused period"

**Default Urgency**: Medium (High if payment blocking service)

---

#### 3. Account Management

**Indicators**: Access problems, authentication issues, settings changes, permissions

**Keywords**: login, password, access, can't sign in, locked out, permission, settings, profile, user management

**Examples**:
- "Cannot login to my account"
- "Need to reset password"
- "User doesn't have access to feature"
- "How to add team members"

**Default Urgency**: High (access blocking work)

---

#### 4. General Inquiries

**Indicators**: Questions, feature requests, feedback, how-to questions

**Keywords**: how to, can I, is it possible, does it support, feature request, suggestion, feedback

**Examples**:
- "How do I export data to CSV?"
- "Does the platform support SSO?"
- "Feature request: dark mode"
- "Documentation for API webhooks"

**Default Urgency**: Low

---

## Urgency Determination

### Critical (Response: 15 min | Resolution: 4 hours)

**Triggers**:
- Service completely down
- Security breach or vulnerability
- Data loss or corruption
- Payment processing completely failing
- Multiple users unable to access system

**Keywords**: down, breach, security, data loss, emergency, critical, all users, production down

**Example**: "Entire platform is down, all users getting 503 errors"

---

### High (Response: 1 hour | Resolution: 8 hours)

**Triggers**:
- Major feature broken for user
- Payment issues blocking service
- Cannot access account
- Integration completely failing

**Keywords**: broken, can't access, payment failed, urgent, blocking, critical feature

**Example**: "Cannot login to account, password reset not working"

---

### Medium (Response: 4 hours | Resolution: 24 hours)

**Triggers**:
- Minor bugs with workarounds
- Feature questions
- Single user affected
- Non-blocking issues

**Keywords**: issue, problem, help, question, sometimes, occasionally

**Example**: "Export feature sometimes times out with large datasets"

---

### Low (Response: 24 hours | Resolution: 72 hours)

**Triggers**:
- General questions
- Feature requests
- Documentation requests
- Feedback

**Keywords**: feature, suggestion, feedback, inquiry, how to, can you

**Example**: "Would love to see dark mode added in the future"

---

## Priority Calculation

Priority = f(Urgency, Customer Tier, Business Impact)

### Formula

```
Priority 1 (Critical):
  - Urgency = Critical + Any tier
  - Urgency = High + Premium/Enterprise tier

Priority 2 (High):
  - Urgency = High + Standard tier
  - Urgency = Medium + Premium tier

Priority 3 (Medium):
  - Urgency = Medium + Standard tier
  - Urgency = Low + Premium tier

Priority 4 (Low):
  - Urgency = Low + Any tier
```

### Customer Tier Impact

**Premium/Enterprise**:
- Priority boost: +1 level
- SLA multiplier: 0.5× (faster response)
- Escalation threshold: Lower

**Standard**:
- Priority boost: 0
- SLA multiplier: 1.0× (standard)
- Escalation threshold: Normal

**Basic/Free**:
- Priority boost: 0
- SLA multiplier: 1.5× (slower)
- Escalation threshold: Higher

---

## Pattern Recognition

### Error Keywords

Indicate technical issues requiring KB search or L2:
- error, exception, failed, crash
- timeout, 401, 403, 404, 500, 503
- broken, not working, doesn't work
- bug, glitch, issue

### Urgency Keywords

Indicate elevated priority:
- urgent, asap, immediately, emergency
- critical, blocking, can't work
- production, all users, entire team
- security, breach, vulnerability

### Scope Keywords

Indicate business impact:
- **High impact**: all users, entire team, production, company-wide
- **Medium impact**: multiple users, department, team
- **Low impact**: just me, my account, single user

### Security Keywords

Immediate escalation required:
- security, breach, vulnerability, exploit
- unauthorized access, data leak, exposed
- hacked, compromised, suspicious activity

---

## Routing Rules

### Auto-Resolve Candidates

Route directly to KB without human review:
- Simple password reset
- Basic FAQ questions
- Standard how-to queries
- Common account setup questions

**Characteristics**:
- Exact match in FAQ
- No ambiguity
- Standard procedure
- Low risk of error

---

### KB Search First

Search knowledge base before other actions:
- Technical questions with keywords matching KB
- Troubleshooting requests
- Feature inquiries
- Common error codes

**Process**:
1. Search KB for relevant articles
2. If match found → route to issue-resolver
3. If no match → route to issue-resolver for custom solution
4. If complex → consider escalation

---

### Immediate Escalation

Route directly to human specialists without KB search:
- Security issues
- Legal matters
- Executive requests
- Service completely down
- Data loss scenarios
- Compliance questions

**Escalation Levels**:
- **Security** → Security team + L3
- **Legal** → Legal department
- **Service down** → L3 Engineering + Management
- **Executive** → Customer Success Manager
- **Data loss** → L3 + Management

---

## Context Signals

### Time Sensitivity

Look for these patterns:
- "urgent", "asap", "immediately" → Boost urgency
- "when you can", "no rush", "whenever" → Lower urgency
- "blocking work", "can't proceed" → High priority
- "nice to have", "future" → Low priority

### Customer Sentiment

Analyze tone for escalation triggers:
- **Frustrated**: Multiple previous attempts, express frustration
- **Angry**: Threatening to leave, demanding refund
- **Calm**: Polite inquiry, patient tone
- **Confused**: Lots of questions, seeking clarification

### Business Context

Consider business impact:
- "Production environment" → Higher priority
- "Testing/staging" → Lower priority
- "Revenue impacting" → Escalate
- "Internal tool" → Standard priority

---

## Classification Examples

### Example 1: Simple FAQ

**Query**: "How do I reset my password?"

**Classification**:
- Type: Account
- Category: Password reset
- Urgency: Low (standard procedure)
- Priority: 4
- Tags: [password, reset, account]
- Routing: auto_resolve → KB-001

---

### Example 2: Technical Issue

**Query**: "Getting 401 errors when calling the API with my key"

**Classification**:
- Type: Technical
- Category: API authentication
- Urgency: High (blocking integration)
- Priority: 2
- Tags: [api, authentication, 401, error]
- Routing: kb_search → issue-resolver

---

### Example 3: Critical Issue

**Query**: "Production dashboard showing 503 errors, all users affected"

**Classification**:
- Type: Technical
- Category: System outage
- Urgency: Critical (service down)
- Priority: 1
- Tags: [outage, 503, production, critical]
- Routing: immediate_escalation → L3 Engineering

---

### Example 4: Billing Question

**Query**: "I was charged $200 but my plan is $100/month"

**Classification**:
- Type: Billing
- Category: Incorrect charge
- Urgency: Medium
- Priority: 3 (2 if premium customer)
- Tags: [billing, overcharge, dispute]
- Routing: kb_search → escalation to billing team

---

## Quality Metrics

### Accuracy Targets

- **Classification accuracy**: > 95% correct type
- **Routing accuracy**: > 90% correct handler
- **Priority accuracy**: > 95% correct urgency
- **SLA assignment**: 100% correct

### Speed Targets

- **Average classification time**: < 5 seconds
- **Complex queries**: < 10 seconds
- **Batch classification**: < 2 seconds per query

### Consistency

Same query type should always get:
- Same classification type
- Same urgency level (unless context differs)
- Same routing destination
- Same tags

---

## Edge Cases

### Ambiguous Queries

**Problem**: "My account isn't working"

**Solution**:
- Flag for clarification
- Classify as "Account/General" with medium urgency
- Route to issue-resolver for clarification questions
- Tag as "needs_clarification"

---

### Multiple Issues

**Problem**: "Can't login AND billing charge is wrong"

**Solution**:
- Create separate tickets
- TICKET-1: Account/Login (High urgency)
- TICKET-2: Billing/Charge (Medium urgency)
- Link tickets as related
- Prioritize access issue first

---

### VIP Customers

**Problem**: Known high-value customer with standard issue

**Solution**:
- Auto-boost priority by 1 level
- Reduce SLA timers by 50%
- Flag for customer success awareness
- Ensure white-glove treatment

---

### Off-Hours

**Problem**: Query received outside business hours

**Solution**:
- If Critical → Immediate escalation to on-call
- If High → Queue for first thing next business day
- If Medium/Low → Standard queue
- Auto-reply with expected response time

---

## Best Practices

### Do's

✅ Read full query before classifying (don't judge by subject line alone)
✅ Extract all relevant context clues
✅ Consider customer history and tier
✅ Apply consistent rules
✅ Log classification reasoning
✅ Flag uncertainty for review
✅ Track metrics for improvement

### Don'ts

❌ Assume urgency without reading details
❌ Over-escalate simple issues
❌ Miss security-related keywords
❌ Ignore customer tier in priority calculation
❌ Classify without extracting all tags
❌ Skip SLA assignment
❌ Use inconsistent criteria

---

## Continuous Improvement

### Learn from Feedback

Track these metrics to improve:
- **Misclassification rate**: When routing was wrong
- **Escalation success**: If escalated tickets needed it
- **Resolution correlation**: Which classifications resolve fastest
- **Customer feedback**: Satisfaction by classification accuracy

### KB Gap Analysis

When "no KB match" occurs frequently:
- Log the query pattern
- Identify KB gaps
- Suggest new KB articles
- Update classification rules

### Classification Refinement

Monthly review:
- Top misclassified patterns
- New issue types emerging
- Keywords needing addition
- Routing rule adjustments

---

## Summary

Effective query classification requires:

1. **Complete analysis** of query content
2. **Context awareness** of customer tier and history
3. **Urgency assessment** based on impact and scope
4. **Accurate routing** to appropriate handler
5. **Consistent application** of classification rules
6. **Continuous learning** from feedback and metrics

**Goal**: 95%+ accuracy in classification with <5 second average time
