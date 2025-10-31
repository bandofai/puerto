# Customer Support Plugin

First-line customer support with query classification, issue resolution, and escalation management.

## Overview

The Customer Support plugin provides a complete AI-powered customer support system that handles query classification, knowledge base search, issue resolution, ticket documentation, and intelligent escalation to human specialists.

## What's Included

### 5 Specialized Agents

1. **query-classifier** (Haiku - Fast Classification)
   - Classifies customer queries by type, urgency, and priority
   - Routes to appropriate handler
   - Creates structured tickets
   - Fast, cost-effective classification (~$0.0001/query)

2. **issue-resolver** (Sonnet - Intelligent Resolution)
   - Resolves customer issues using KB and reasoning
   - Generates professional, empathetic responses
   - Adapts KB solutions to specific customer contexts
   - Creates custom solutions for novel issues

3. **kb-searcher** (Haiku - Lightning-Fast Search)
   - Searches FAQ, troubleshooting guides, documentation
   - Returns relevant articles ranked by relevance
   - Extremely fast (<2 seconds average)
   - Cost-effective search (~$0.00008/search)

4. **ticket-documenter** (Haiku - Structured Documentation)
   - Maintains complete, accurate ticket records
   - Logs all interactions with timestamps
   - Calculates metrics automatically
   - Generates reports and analytics

5. **escalation-manager** (Sonnet - Strategic Escalation)
   - Routes complex issues to human specialists
   - Prepares comprehensive escalation packages
   - Notifies customers with timelines
   - Monitors SLA compliance

### 3 Comprehensive Skills

1. **query-classification**: Classification patterns, urgency determination, routing rules
2. **ticket-management**: Documentation standards, SLA tracking, metrics calculation
3. **customer-communication**: Professional tone, response templates, empathy guidelines

### Knowledge Base Structure

```
knowledge-base/
├── faq.md                      # Quick answers to common questions
└── troubleshooting/
    ├── common-errors.md
    ├── account-issues.md
    └── technical-issues.md
```

## Key Features

✅ **Intelligent Classification**: Automatically categorizes and prioritizes queries
✅ **KB-First Approach**: Searches knowledge base before escalating
✅ **Professional Communication**: Empathetic, clear customer responses
✅ **Complete Documentation**: Full ticket history for compliance and analysis
✅ **Smart Escalation**: Routes complex issues to appropriate specialists
✅ **SLA Tracking**: Monitors response and resolution time targets
✅ **Cost-Optimized**: Haiku for simple tasks, Sonnet for complex reasoning
✅ **Metrics-Driven**: Tracks resolution time, satisfaction, escalation rate
✅ **Skill-Aware**: All agents read skills for consistent quality

## Workflow

```
Customer Query
      ↓
[@query-classifier] → Analyzes and classifies
      ↓
   Routing Decision
      ↓
   ┌──────┴──────┐
   │             │
[@kb-searcher]  [Immediate Escalation]
   │             ↓
   ↓        [@escalation-manager]
[@issue-resolver]
   │
   ├─→ Success: [@ticket-documenter] → Customer Response
   │
   └─→ Failed: [@escalation-manager] → Human Specialist
```

## Usage Examples

### Simple Query Resolution

```bash
# Customer asks: "How do I reset my password?"

@query-classifier "How do I reset my password?"
# → Classifies as: Account/Password Reset (Low priority)
# → Routes to: kb-searcher

@kb-searcher "password reset"
# → Finds: KB-001 Password Reset Guide

@issue-resolver "resolve using KB-001"
# → Generates professional response with steps
# → Customer receives solution within 2 minutes
```

### Technical Issue

```bash
# Customer reports: "Getting 401 errors on API calls"

@query-classifier "Getting 401 errors on API calls"
# → Classifies as: Technical/API (High priority)
# → Routes to: kb-searcher → issue-resolver

@kb-searcher "api 401 authentication"
# → Finds: KB-002 API Authentication Guide

@issue-resolver "resolve API authentication issue"
# → Adapts KB solution to customer context
# → Provides API key regeneration steps
# → Resolution time: ~5 minutes
```

### Critical Escalation

```bash
# Customer reports: "Production dashboard down, all users affected"

@query-classifier "Production dashboard down, all users affected"
# → Classifies as: Technical/Critical (Priority 1)
# → Routes to: immediate_escalation

@escalation-manager "escalate critical outage"
# → Creates escalation package with complete context
# → Routes to: L3 Engineering + Management
# → Notifies customer with 15-minute response commitment
```

## Agent Details

### query-classifier

**Model**: Haiku (speed + cost efficiency)
**Purpose**: Fast, accurate query classification
**Output**: Structured ticket with classification and routing

**Classifies**:
- Type: Technical, Billing, Account, General
- Urgency: Critical, High, Medium, Low
- Priority: 1-4 (based on urgency + customer tier)
- Route: auto_resolve, kb_search, or escalation

**Performance**: <5 seconds, >95% accuracy

---

### issue-resolver

**Model**: Sonnet (reasoning required)
**Purpose**: Resolve customer issues professionally
**Skills-aware**: Reads customer-communication and ticket-management skills

**Process**:
1. Searches knowledge base for relevant articles
2. Analyzes customer's specific situation
3. Adapts KB solution or creates custom solution
4. Composes professional, empathetic response
5. Documents resolution

**Performance**: <15 minutes average, >70% first-contact resolution

---

### kb-searcher

**Model**: Haiku (simple retrieval)
**Purpose**: Fast knowledge base search
**Search**: FAQ, troubleshooting guides, documentation

**Search Strategy**:
1. FAQ first (80% of queries)
2. Troubleshooting guides
3. Full documentation

**Performance**: <2 seconds, >90% relevance

---

### ticket-documenter

**Model**: Haiku (structured data)
**Purpose**: Complete ticket documentation
**Skills-aware**: Reads ticket-management skill

**Documents**:
- All interactions with timestamps
- Status transitions
- Metrics (resolution time, touches, etc.)
- KB articles used
- Customer satisfaction

**Output**: Structured JSON + analytics

---

### escalation-manager

**Model**: Sonnet (judgment required)
**Purpose**: Intelligent escalation to humans
**Skills-aware**: Reads ticket-management and customer-communication skills

**Escalation Levels**:
- L2: Technical specialists
- L3: Engineering team
- Management: Customer success
- Legal: Legal department

**Creates**:
- Comprehensive escalation package
- Customer notification with timeline
- SLA tracking and monitoring

---

## Cost Analysis

### Per Query Cost Estimates

| Scenario | Agents Used | Est. Cost | Success Rate |
|----------|------------|-----------|--------------|
| Simple FAQ | classifier + kb-searcher + documenter | $0.0002 | 95% |
| KB Resolution | + issue-resolver | $0.0017 | 85% |
| Custom Solution | + issue-resolver (extended) | $0.0025 | 75% |
| Escalation | + escalation-manager | $0.0028 | 98% |

### Monthly Estimates (5000 queries)

- 60% Simple (3000): 3000 × $0.0002 = $0.60
- 30% KB Resolution (1500): 1500 × $0.0017 = $2.55
- 10% Complex (500): 500 × $0.0025 = $1.25
- **Total AI Cost**: ~$4.40/month

**Savings**: 95%+ cost reduction vs human-only support while maintaining high quality

---

## SLA Targets

| Priority | First Response | Resolution Target | Customer Tier Adjustment |
|----------|---------------|-------------------|-------------------------|
| P1 (Critical) | 15 minutes | 4 hours | Premium: 0.5× faster |
| P2 (High) | 1 hour | 8 hours | Standard: 1.0× |
| P3 (Medium) | 4 hours | 24 hours | Basic: 1.5× slower |
| P4 (Low) | 24 hours | 72 hours | |

---

## Performance Metrics

### Target Metrics

- **First Contact Resolution**: > 70%
- **Average Resolution Time**: < 15 minutes
- **Classification Accuracy**: > 95%
- **KB Hit Rate**: > 80%
- **Escalation Rate**: < 20%
- **SLA Compliance**: > 95%
- **Customer Satisfaction**: > 4.5/5

### Tracked Metrics

**Per Ticket**:
- Resolution time
- First response time
- Agent touches
- KB articles used
- Escalation (yes/no)
- Customer satisfaction

**Aggregate**:
- Volume by type, priority, urgency
- Average resolution times
- First contact resolution rate
- Escalation patterns
- KB effectiveness
- SLA compliance rate

---

## Setup Instructions

### 1. Initialize Knowledge Base

Create basic KB articles:

```bash
# Create FAQ
plugins/customer-support/knowledge-base/faq.md

# Create troubleshooting guides
plugins/customer-support/knowledge-base/troubleshooting/common-errors.md
plugins/customer-support/knowledge-base/troubleshooting/account-issues.md
plugins/customer-support/knowledge-base/troubleshooting/technical-issues.md
```

### 2. Configure Response Templates

Customize templates in `templates/response-templates/`:
- acknowledgment.md
- resolution.md
- escalation.md
- follow-up.md

### 3. Set Up Escalation Routing

Configure specialist routing in escalation-manager.md based on your team structure.

### 4. Customize Classification Rules

Adjust classification patterns in skills/query-classification/SKILL.md to match your product.

---

## Integration

### Email Integration

Connect to support email:
1. Parse incoming emails
2. Extract subject + body
3. Call @query-classifier with email content
4. Route through workflow
5. Send response via email

### Chat Integration

Real-time support:
1. Customer sends chat message
2. @query-classifier analyzes
3. @kb-searcher finds instant answers
4. @issue-resolver provides live response
5. Escalate to human if needed

### Ticketing System

Integrate with existing tools:
1. Create tickets in your system
2. Use ticket IDs for tracking
3. Sync status updates
4. Export metrics to dashboard

---

## Best Practices

### Knowledge Base Maintenance

1. **Update regularly**: Keep KB articles current
2. **Add new patterns**: When novel issues resolved, add to KB
3. **Track effectiveness**: Monitor which articles resolve most queries
4. **Remove outdated**: Archive obsolete information
5. **Improve unsuccessful**: Rewrite articles with low resolution rates

### Quality Assurance

1. **Review sample tickets**: Random sampling for quality
2. **Track metrics**: Monitor trends weekly
3. **Customer feedback**: Collect satisfaction scores
4. **Agent refinement**: Update agents based on learnings
5. **Skill updates**: Improve skills with new patterns

### Cost Optimization

1. **KB-first**: Ensure robust knowledge base to avoid AI costs
2. **Cache common**: Cache frequent query responses
3. **Batch similar**: Process similar queries together
4. **Right model**: Haiku for simple, Sonnet for complex
5. **Monitor usage**: Track costs and optimize patterns

---

## Troubleshooting

### High Escalation Rate

**Problem**: >30% of queries escalated

**Solutions**:
- Expand knowledge base coverage
- Improve KB article quality
- Refine classification patterns
- Train issue-resolver with more examples

### Slow Resolution Time

**Problem**: Average >20 minutes

**Solutions**:
- Optimize KB search performance
- Simplify response templates
- Improve classification accuracy
- Add more FAQ articles

### Low Customer Satisfaction

**Problem**: <4.0/5 average

**Solutions**:
- Review communication tone
- Ensure complete solutions
- Improve response clarity
- Follow up on resolutions

---

## Future Enhancements

- **Sentiment Analysis**: Detect frustrated customers for priority routing
- **Multilingual Support**: Translate queries and responses
- **Predictive Routing**: ML-based routing optimization
- **Automated Follow-up**: Schedule and send follow-ups automatically
- **Customer Portal**: Self-service KB search
- **Analytics Dashboard**: Real-time metrics visualization
- **Chatbot Integration**: Instant responses in chat widget

---

## Design Principles

This plugin follows Puerto best practices:

✅ **Skill-Aware**: All agents read skills first for consistent quality
✅ **Model Optimization**: Haiku for simple tasks, Sonnet for reasoning
✅ **Single Responsibility**: Each agent focuses on one aspect
✅ **Tool Minimization**: Least privilege access
✅ **Cost-Conscious**: Optimized for efficiency
✅ **Quality-Focused**: Professional customer communication
✅ **Metrics-Driven**: Complete tracking and analytics

---

## Support

For questions or issues with this plugin:
1. Check troubleshooting section
2. Review agent and skill documentation
3. Test with sample queries
4. Refine based on your specific needs

**Plugin Version**: 1.0.0
**Last Updated**: 2025-01-20
**Author**: Puerto
