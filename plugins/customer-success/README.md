# Customer Success Plugin

Customer relationship and retention specialist for Puerto, focused on onboarding excellence, health monitoring, and strategic renewals.

## Overview

The Customer Success plugin provides specialized agents and skills for managing high-value B2B customer relationships throughout the entire customer lifecycle. Built on proven patterns from successful CS organizations, it helps teams drive adoption, prevent churn, and maximize expansion revenue.

## Features

- **Intelligent Onboarding**: Create personalized onboarding plans with clear milestones and success criteria
- **Proactive Health Monitoring**: Multi-dimensional health scores with automated risk detection
- **Strategic Renewals**: Data-driven renewal strategies with expansion opportunity identification
- **Skill-Aware Agents**: All agents leverage battle-tested customer success patterns
- **Production Templates**: Ready-to-use frameworks for onboarding, health scoring, and renewals

## Agents

### 1. Onboarding Coordinator (Sonnet)

**Purpose**: Orchestrate customer onboarding workflows and ensure smooth adoption

**When to Use**:
- New customer kickoff
- Creating onboarding plans
- Setting up success milestones
- Tracking implementation progress

**Capabilities**:
- Personalized onboarding plan creation
- Milestone and timeline definition
- Stakeholder mapping
- Resource preparation
- Risk identification

**Example Usage**:
```
Create an onboarding plan for Acme Corp, enterprise customer starting Jan 15,
with 100 users, focus on sales automation workflows, 90-day timeline to full adoption.
```

**Output**:
- Customized onboarding plan
- Week-by-week milestones
- Action items with owners
- Communication schedule
- Risk mitigation strategies

### 2. Health Monitor (Haiku)

**Purpose**: Track customer health scores and identify at-risk accounts

**When to Use**:
- Regular health score updates
- Monthly/quarterly reviews
- Risk assessment
- Churn prevention
- Engagement tracking

**Capabilities**:
- Multi-dimensional health scoring (Usage, Engagement, Support, Satisfaction, Financial)
- Trend analysis and alerts
- Risk factor identification
- Action recommendations
- Red flag detection

**Example Usage**:
```
Generate health report for Acme Corp for Q4 2024. Latest metrics:
- Active users: 85/100
- Avg logins/week: 4.2
- Support tickets: 3 (all resolved)
- NPS: 8
- Last contact: 5 days ago
```

**Output**:
- Overall health score (0-100)
- Component scores with trends
- Risk assessment
- Recommended actions
- Alert triggers

### 3. Renewal Strategist (Sonnet)

**Purpose**: Prepare renewal strategies and identify upsell opportunities

**When to Use**:
- 120+ days before renewal
- Quarterly renewal planning
- Expansion discussions
- At-risk account recovery
- Multi-year negotiations

**Capabilities**:
- Risk-based renewal assessment
- ROI documentation
- Expansion opportunity identification
- Multi-option proposal creation
- Stakeholder alignment planning

**Example Usage**:
```
Create renewal strategy for Acme Corp:
- Renewal date: June 30, 2025
- Current ARR: $120k
- Health score: 78 (Yellow)
- Key concern: Usage declining in Q4
- Expansion potential: 25 additional seats, premium tier
```

**Output**:
- Renewal risk assessment
- Value delivered summary
- Expansion recommendations
- Timeline with milestones
- Conversation guides
- Multiple proposal options

## Skills

### Customer Success Skill

**Location**: `skills/customer-success/SKILL.md`

**Contains**:
- Time-to-value framework
- Health score methodology
- Retention strategies
- Expansion playbooks
- Renewal best practices
- Communication patterns
- Success metrics and KPIs

**Key Patterns**:

**Onboarding**:
- Week 1: Foundation (kickoff, access, training)
- Week 2-4: Implementation (configuration, first workflows)
- Week 5-8: Adoption (all users, advanced features)
- Day 90: Success checkpoint (QBR, ROI review)

**Health Scoring**:
- Usage Health (30%): Active users, logins, features
- Engagement Health (25%): Communication, meetings
- Support Health (20%): Ticket volume, satisfaction
- Satisfaction Health (15%): NPS, CSAT
- Financial Health (10%): Payment status, expansion

**Renewal Timeline**:
- T-120: Internal kickoff, ROI documentation
- T-90: Executive engagement, QBR
- T-60: Proposal development
- T-30: Contract execution
- T-0: Celebration, new goals

## Templates

### 1. Onboarding Checklist

**Purpose**: Standard customer onboarding workflow template

**Phases**:
- Pre-kickoff preparation
- Week 1: Foundation
- Week 2-4: Implementation
- Week 5-8: Adoption
- Day 90: Success checkpoint
- Ongoing success

### 2. Health Score Framework

**Purpose**: Customer health calculation methodology

**Components**:
- 5-dimensional scoring model
- Point allocation by metric
- Status classification (Green/Yellow/Red)
- Monitoring cadence
- Action triggers

### 3. Renewal Playbook

**Purpose**: Renewal preparation and execution guide

**Includes**:
- 120-day renewal timeline
- Risk assessment framework
- Value documentation template
- Expansion opportunity framework
- Objection handling scripts
- Proposal options template

## Workflow Examples

### Example 1: New Customer Onboarding

```
1. Use onboarding-coordinator to create personalized plan
2. Execute Week 1 kickoff activities
3. Track progress with health-monitor
4. Adjust plan based on health signals
5. Conduct 90-day success review
6. Transition to renewal-strategist at 9 months
```

### Example 2: At-Risk Customer Recovery

```
1. Use health-monitor to identify declining health score
2. Generate detailed health report with risk factors
3. Use onboarding-coordinator for re-engagement plan
4. Address specific issues from health report
5. Monitor weekly with health-monitor
6. Use renewal-strategist to develop recovery plan
```

### Example 3: Renewal Preparation

```
1. Use renewal-strategist 120 days before renewal
2. Review health score from health-monitor
3. Document ROI and value delivered
4. Identify expansion opportunities
5. Create multi-option proposal
6. Execute renewal timeline
7. Use onboarding-coordinator for expansion onboarding
```

## Best Practices

### Agent Usage

1. **Read Skills First**: All agents require reading the customer success skill before execution
2. **Personalization**: Never use generic templates; always customize to customer context
3. **Data-Driven**: Base decisions on metrics and trends, not assumptions
4. **Proactive**: Start renewal process 120+ days early, monitor health continuously
5. **Multi-Threading**: Build relationships across the customer organization

### Success Metrics

**Retention**:
- Gross revenue retention: >90%
- Net revenue retention: >110%
- Logo retention: >95%

**Growth**:
- Expansion rate: >20% of customer base
- Upsell ARR: >25% of renewals

**Health**:
- Customers in green: >70%
- Average health score: >75

**Engagement**:
- QBR completion: >90%
- NPS: >40
- CSAT: >4.5/5

### Common Pitfalls

❌ **Reactive approach**: Waiting for customer issues
✅ **Proactive engagement**: Regular data-driven outreach

❌ **Product-focused**: Talking about features
✅ **Value-focused**: Discussing business outcomes

❌ **Single-threaded**: One stakeholder relationship
✅ **Multi-threaded**: Relationships across organization

❌ **Late renewal start**: 30 days before expiration
✅ **Early preparation**: 120+ days timeline

## Integration Points

### CRM Integration
- Customer profiles and contact information
- Communication history
- Account hierarchy
- Opportunity tracking

### Product Analytics
- Usage metrics (logins, active users, features)
- Adoption trends
- Power user identification

### Support System
- Ticket volume and trends
- Issue severity
- Resolution times
- Satisfaction ratings

### Billing System
- Contract value and terms
- Payment status
- Renewal dates
- Expansion revenue

## Requirements Met

✅ **Role**: Customer relationship and retention specialist
✅ **Responsibilities**:
  - Customer onboarding with clear workflows
  - Adoption tracking through health monitoring
  - Health score monitoring with multi-dimensional model
  - Renewal preparation with 120-day timeline
  - Upsell identification through expansion framework
✅ **Tools**: Data analysis, email templates, CRM access patterns
✅ **Plugin Structure**: agents/, skills/, templates/
✅ **Agent Count**: 3 agents (onboarding-coordinator, health-monitor, renewal-strategist)
✅ **Skill**: Comprehensive customer-success skill (400 lines)
✅ **Model Optimization**: Haiku for health monitoring, Sonnet for strategy
✅ **Puerto Best Practices**: Skill-aware, single responsibility, production-ready

## Getting Started

1. **Install Plugin**: Copy to `~/.claude/plugins/customer-success/`
2. **Review Skill**: Read `skills/customer-success/SKILL.md` for patterns
3. **Choose Agent**: Select based on customer lifecycle stage
4. **Provide Context**: Give customer details and specific objectives
5. **Execute**: Let agent create customized plans and strategies
6. **Track**: Use health-monitor regularly for ongoing success

## File Structure

```
plugins/customer-success/
├── .claude-plugin/
│   └── plugin.json                    # Plugin manifest
├── agents/
│   ├── onboarding-coordinator.md      # Onboarding workflows (Sonnet)
│   ├── health-monitor.md              # Health tracking (Haiku)
│   └── renewal-strategist.md          # Renewal strategy (Sonnet)
├── skills/
│   └── customer-success/
│       └── SKILL.md                   # CS patterns and best practices
├── templates/
│   ├── onboarding-checklist.md        # Standard onboarding template
│   ├── health-score-framework.md      # Health scoring methodology
│   └── renewal-playbook.md            # Renewal execution guide
└── README.md                          # This file
```

## Version

**Version**: 1.0.0
**Author**: Puerto Plugin System
**License**: MIT

## Support

For issues, questions, or contributions, please refer to the Puerto plugin system documentation.

---

**Note**: This plugin is designed for B2B customer success teams managing high-value accounts. Adapt frameworks and metrics to your specific product and customer segment.
