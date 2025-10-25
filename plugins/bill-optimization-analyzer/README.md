# Bill Optimization Analyzer Plugin

Utility and service bill optimization with plan analysis, provider comparison, savings calculation, and negotiation assistance for significantly reducing recurring monthly costs.

## Overview

Systematically reduce monthly expenses through research, negotiation, and strategic provider switching across utilities, telecommunications, insurance, and subscriptions.

## What's Included

### Agent: bill-optimizer
- **Current plan analysis** (costs, usage, contract status)
- **Alternative provider research** (competitive options)
- **Savings calculation** (immediate and long-term)
- **Negotiation scripts** (retention department strategies)
- **Switching process guides** (step-by-step instructions)
- **Contract expiration tracking** (avoid rate increases)
- **Bundle opportunity analysis** (multi-service savings)
- **Annual review system** (systematic optimization)

### Skill: bill-optimization
Comprehensive guide covering:
- Bill optimization cycle (audit → research → negotiate → switch → track)
- Service-specific strategies (internet, mobile, insurance, subscriptions)
- Negotiation psychology and proven scripts
- Switching process details with timelines
- Bundle analysis framework
- Typical savings potential by service
- Contract tracking systems

### Templates
- **current-bills.json** - All recurring expenses with contract details
- **provider-comparison.md** - Research results and recommendations
- **savings-calculation.json** - Cost analysis and projections
- **negotiation-script.md** - Talking points for retention calls
- **contract-tracker.json** - Expiration dates and review reminders

## Key Features

### Intelligent Analysis
- Full cost calculation (base + taxes + fees)
- Usage analysis (right-sized plans)
- Contract status tracking
- Promotional rate monitoring

### Competitive Research
- WebFetch-powered provider lookup
- Real-time plan comparison
- Customer review analysis
- Coverage availability checking

### Negotiation Tools
- Proven retention scripts
- Leverage point identification
- Counter-offer strategies
- Written confirmation guidance

### Switching Support
- Step-by-step guides
- Timeline management
- Testing checklists
- Equipment return tracking

## Installation

```bash
/plugin install bill-optimization-analyzer@puerto
```

After installation, restart Claude Code to activate the agent and skill.

## Usage Examples

### Analyze Internet Bill
```
@bill-optimizer Analyze my internet bill and find better options. I'm paying $100/mo for 300Mbps.
```

### Mobile Phone Optimization
```
@bill-optimizer I'm paying $160/mo for 2 phone lines. Help me reduce this cost.
```

### Auto Insurance Review
```
@bill-optimizer My auto insurance increased 20%. Research competitive rates and help me negotiate.
```

### Full Bill Audit
```
@bill-optimizer Audit all my recurring bills and find optimization opportunities.
```

### Negotiation Prep
```
@bill-optimizer Create a negotiation script for my upcoming call with Comcast retention.
```

## File Structure

```
bill-optimization-analyzer/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   └── bill-optimizer.md
├── skills/
│   └── bill-optimization/
│       └── SKILL.md
├── templates/
│   ├── current-bills.json
│   ├── provider-comparison.md
│   ├── savings-calculation.json
│   ├── negotiation-script.md
│   └── contract-tracker.json
└── README.md
```

## Savings Potential

**Typical Household Optimization**:

| Service | Current | Optimized | Savings |
|---------|---------|-----------|---------|
| Internet | $100/mo | $60/mo | $480/year |
| Mobile (2 lines) | $160/mo | $80/mo | $960/year |
| Auto Insurance | $240/mo | $180/mo | $720/year |
| Subscriptions | $85/mo | $45/mo | $480/year |
| **Total** | **$585/mo** | **$365/mo** | **$2,640/year** |

**Time Investment**: 15-25 hours
**Return**: $120-200/hour
**Plus ongoing annual savings**

## Best Practices

1. **Annual Review**: Audit all bills every 12 months
2. **Pre-Expiration**: Negotiate 60 days before promotion ends
3. **Market Awareness**: Know what new customers pay
4. **Switching Readiness**: Must be willing to actually switch
5. **Written Confirmation**: Always get rate guarantees in writing
6. **Calendar Reminders**: Track all expiration dates

## Optimization Priority

**High Impact** (>$50/mo savings):
1. Internet
2. Mobile phone
3. Auto insurance

**Medium Impact** ($20-50/mo):
4. Subscriptions
5. Home insurance
6. Electricity (deregulated markets)

**Lower Impact** (<$20/mo):
7. Streaming consolidation
8. Gym membership

## Integration

Works with:
- WebFetch for provider research
- Market rate lookup tools
- Comparison websites
- Customer review sites

## Success Metrics

- **Total monthly savings**: Track reduction
- **Successful negotiations**: % that yield discounts
- **Switches completed**: Services optimized
- **Annual savings**: Cumulative reduction
- **Time invested**: ROI calculation

## License

MIT License - See main repository for details

---

**Reduce your recurring bills by 20-40% through systematic optimization, competitive research, and effective negotiation. Your loyalty deserves better rates.**
