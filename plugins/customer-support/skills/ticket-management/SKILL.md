# Ticket Management Skill

## Purpose

Maintain high-quality, comprehensive ticket records for effective support operations, compliance, and continuous improvement.

## Ticket Lifecycle

```
New → Classified → In Progress → Resolved → Closed
                       ↓
                   Escalated → Specialist Review → Resolved
```

## Documentation Standards

### Required Fields

Every ticket MUST have:

✅ **Unique Ticket ID**: `TICKET-YYYYMMDD-HHMMSS` format
✅ **Customer Information**: ID, tier, email, name
✅ **Classification**: Type, category, urgency, priority, tags
✅ **Query Content**: Subject and full body
✅ **Interaction History**: Complete log of all actions
✅ **Current Status**: Always up-to-date
✅ **Timestamps**: Created, updated, resolved (ISO-8601 format)
✅ **Metrics**: Resolution time, response time, touches

### Optional But Recommended

- Resolution details and KB articles used
- Customer satisfaction score
- Escalation information
- Related tickets
- Follow-up schedule

---

## Interaction Logging

### Log Format

Every action MUST be logged:

```json
{
  "timestamp": "2025-01-20T14:35:15Z",
  "agent": "kb-searcher",
  "action": "kb_searched",
  "details": "Searched for 'API authentication', found KB-002",
  "outcome": "Relevant article found"
}
```

### Action Types

- `ticket_created`: New ticket generated
- `classified`: Query classified and routed
- `kb_searched`: Knowledge base searched
- `solution_provided`: Resolution sent to customer
- `escalated`: Escalated to specialist
- `status_changed`: Status transition
- `customer_response`: Customer replied
- `followup_scheduled`: Follow-up scheduled
- `closed`: Ticket closed

### Best Practices

✅ Log immediately (don't batch)
✅ Be specific ("Provided KB-002" not "gave answer")
✅ Include context (why action taken)
✅ Track time accurately
✅ Link resources (KB articles, docs)
✅ Never delete, only append

---

## Status Management

### Valid Status Values

- **new**: Just received, awaiting classification
- **classified**: Analyzed and routed
- **in_progress**: Being actively worked on
- **escalated**: Handed to human specialist
- **resolved**: Solution provided to customer
- **closed**: Customer confirmed or auto-closed
- **reopened**: Customer replied with additional issues

### Valid Transitions

```
✅ New → Classified
✅ Classified → In Progress
✅ In Progress → Resolved
✅ In Progress → Escalated
✅ Escalated → In Progress (specialist working)
✅ Escalated → Resolved
✅ Resolved → Closed
✅ Closed → Reopened (new customer message)
```

### Invalid Transitions

```
❌ New → Resolved (must classify first)
❌ Resolved → New (create new ticket)
❌ Closed → In Progress (reopen instead)
```

---

## SLA Tracking

### Response Time SLA

| Priority | First Response Target | Resolution Target |
|----------|----------------------|-------------------|
| P1 (Critical) | 15 minutes | 4 hours |
| P2 (High) | 1 hour | 8 hours |
| P3 (Medium) | 4 hours | 24 hours |
| P4 (Low) | 24 hours | 72 hours |

### Customer Tier Adjustments

**Premium/Enterprise**:
- Response time: 0.5× (twice as fast)
- Resolution time: 0.75× (25% faster)

**Standard**:
- Response time: 1.0× (standard)
- Resolution time: 1.0× (standard)

**Basic/Free**:
- Response time: 1.5× (50% slower)
- Resolution time: 1.5× (50% slower)

### SLA Monitoring

Calculate and track:
- Time to first response
- Time to resolution
- Time in each status
- SLA met/breached status
- Buffer time remaining

---

## Metrics to Track

### Per-Ticket Metrics

**Timing**:
- First response time (minutes)
- Total resolution time (minutes)
- Time in queue
- Time in progress
- Time escalated

**Activity**:
- Number of interactions
- Agent touches
- Customer responses
- KB articles used
- Escalation count

**Outcome**:
- Resolution type (KB, custom, escalated)
- Customer satisfaction (if collected)
- First contact resolution (yes/no)

### Aggregate Metrics

**Performance**:
- Average resolution time by priority
- First contact resolution rate
- Escalation rate
- SLA compliance rate

**Quality**:
- Customer satisfaction score
- KB hit rate (queries resolved with KB)
- Classification accuracy
- Resolution effectiveness

**Volume**:
- Tickets per day/week/month
- By type, priority, urgency
- Peak times and patterns

---

## Quality Checklist

Before closing a ticket, verify:

- [ ] All interactions logged with timestamps
- [ ] Resolution documented in detail
- [ ] KB articles referenced (if used)
- [ ] Customer response sent
- [ ] Metrics calculated accurately
- [ ] Tags applied appropriately
- [ ] Status set to "resolved"
- [ ] Follow-up scheduled (if needed)
- [ ] Ticket can be used for training

---

## Best Practices

### Documentation

1. **Immediate logging**: Don't wait to batch updates
2. **Specific details**: Include what, why, and outcome
3. **Complete context**: Future readers should understand
4. **Consistent format**: Follow templates
5. **Link resources**: KB articles, docs, related tickets

### Status Management

1. **Keep current**: Update status after each major action
2. **Follow transitions**: Only valid state changes
3. **Document reasons**: Why status changed
4. **Track timestamps**: Every transition timestamped

### Metrics

1. **Automate**: Calculate metrics programmatically
2. **Verify accuracy**: Spot-check calculations
3. **Track trends**: Look for patterns over time
4. **Use for improvement**: Identify bottlenecks

---

## Ticket Structure Template

```json
{
  "ticket_id": "TICKET-20250120-143022",
  "created_at": "2025-01-20T14:30:22Z",
  "updated_at": "2025-01-20T14:45:10Z",
  "status": "resolved",

  "customer": {
    "id": "CUST-12345",
    "tier": "premium",
    "email": "customer@example.com",
    "name": "Jane Doe"
  },

  "classification": {
    "type": "technical",
    "category": "api",
    "urgency": "high",
    "priority": 2,
    "tags": ["api", "authentication", "resolved", "kb-used"]
  },

  "query": {
    "subject": "API authentication failing",
    "body": "Getting 401 errors on all API calls...",
    "channel": "email"
  },

  "interactions": [
    {
      "timestamp": "2025-01-20T14:30:22Z",
      "agent": "query-classifier",
      "action": "classified",
      "details": "Classified as high-priority API authentication issue"
    },
    {
      "timestamp": "2025-01-20T14:35:15Z",
      "agent": "kb-searcher",
      "action": "kb_searched",
      "details": "Found KB-002: API Authentication Guide"
    },
    {
      "timestamp": "2025-01-20T14:42:30Z",
      "agent": "issue-resolver",
      "action": "resolved",
      "details": "Provided solution from KB-002: regenerate API key"
    }
  ],

  "resolution": {
    "solved": true,
    "solution_type": "kb_article",
    "kb_articles_used": ["KB-002"],
    "resolution_time_minutes": 12,
    "resolution_summary": "Customer API key expired. Guided through regeneration process.",
    "customer_satisfaction": 5
  },

  "escalation": {
    "escalated": false
  },

  "metrics": {
    "first_response_time_minutes": 2,
    "total_interactions": 3,
    "agent_touches": 3,
    "customer_touches": 1
  },

  "sla": {
    "response_target_minutes": 60,
    "resolution_target_hours": 8,
    "response_met": true,
    "resolution_met": true
  }
}
```

---

## Common Mistakes to Avoid

❌ **Missing timestamps**: Every interaction needs exact timestamp
❌ **Vague descriptions**: "Fixed issue" → "Regenerated API key per KB-002"
❌ **Status not updated**: Leaving status stale
❌ **Incomplete metrics**: Not calculating resolution time
❌ **No KB references**: Not linking to KB articles used
❌ **Batch documentation**: Waiting to document multiple actions
❌ **Deleting history**: Never remove interactions, only append
❌ **Closing prematurely**: Before customer confirmation

---

## Reporting & Analytics

### Daily Summary

```
Date: 2025-01-20
Tickets Processed: 45

Status Breakdown:
- Resolved: 38 (84%)
- Escalated: 5 (11%)
- In Progress: 2 (5%)

Performance:
- Avg Resolution Time: 14 minutes
- First Contact Resolution: 75%
- SLA Compliance: 95%
- KB Hit Rate: 82%

Top Issues:
1. API authentication (12 tickets)
2. Password reset (8 tickets)
3. Billing questions (6 tickets)
```

### Weekly Trends

Track week-over-week:
- Volume changes
- Resolution time trends
- Escalation rate changes
- New issue patterns
- KB effectiveness

### Monthly Analysis

Deep dive:
- Issue categorization analysis
- Agent performance metrics
- KB gap identification
- Process improvement opportunities
- Customer satisfaction trends

---

## Integration Points

### With Query Classifier

Classifier creates initial ticket structure with classification

### With KB Searcher

Logs KB search results and articles found

### With Issue Resolver

Logs resolution attempts and outcomes

### With Escalation Manager

Documents escalation details and specialist routing

### All Agents

Should call ticket-documenter for every significant action

---

## Continuous Improvement

### Learn from Tickets

- Identify frequently asked questions → Create KB articles
- Find common pain points → Improve product/docs
- Spot escalation patterns → Improve AI capabilities
- Track KB effectiveness → Update/improve articles

### Quality Assurance

Random sample review:
- Documentation completeness
- Classification accuracy
- Resolution quality
- SLA compliance
- Customer communication tone

---

## Summary

Effective ticket management requires:

1. **Complete documentation** of all interactions
2. **Accurate status** tracking and transitions
3. **Precise metrics** calculation and monitoring
4. **Consistent format** for easy analysis
5. **Immediate logging** without batching
6. **Quality focus** for continuous improvement

**Goal**: 100% complete ticket records enabling effective support operations and continuous improvement
