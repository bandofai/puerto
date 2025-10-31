# Energy Usage Monitor Plugin

Smart energy analysis and monitoring with pattern detection, cost projections, efficiency recommendations, and appliance-specific insights for reducing electricity costs.

## Overview

Understand your energy consumption, identify savings opportunities, and optimize electricity usage through data-driven analysis and actionable recommendations.

## What's Included

### Agent: energy-analyzer
- **Smart meter data analysis** (CSV, API, manual import)
- **Usage pattern detection** (peak times, baseline, anomalies)
- **Cost projections** (monthly, annual, seasonal)
- **Efficiency recommendations** (quick wins to major upgrades)
- **Comparative benchmarking** (similar households, regional)
- **Seasonal trend analysis** (heating/cooling patterns)
- **Appliance consumption estimation** (breakdown by device)
- **ROI calculations** for efficiency improvements

### Skill: energy-monitoring
Comprehensive guide covering:
- Smart meter data processing and validation
- Usage pattern detection frameworks
- Cost projection models (TOU, tiered pricing)
- Efficiency recommendations by investment level
- Appliance consumption estimates
- Benchmark comparisons (national, regional)
- Reporting templates and metrics

### Templates
- **energy-usage.csv** - Smart meter data format
- **usage-analysis.json** - Processed statistics and patterns
- **cost-projections.json** - Future cost estimates with scenarios
- **recommendations.md** - Prioritized efficiency improvements
- **appliance-breakdown.json** - Estimated consumption by device

## Key Features

### Data Analysis
- Import from utility CSV or API
- Hourly/daily/monthly aggregation
- Anomaly detection
- Pattern recognition

### Cost Intelligence
- Current spending analysis
- Future projections
- TOU rate optimization
- Tiered pricing strategies

### Efficiency Roadmap
- Quick wins ($0-50, immediate payback)
- Medium investments ($50-1000, 1-3 year payback)
- Major upgrades ($1000+, 3-10 year payback)
- ROI calculations for each

### Benchmarking
- Compare to similar households
- Regional/national averages
- Historical trends
- Efficiency percentile ranking

## Installation

```bash
/plugin install energy-usage-monitor@puerto
```

After installation, restart Claude Code to activate the agent and skill.

## Usage Examples

### Import Smart Meter Data
```
@energy-analyzer Import my smart meter data from utility-export.csv and analyze usage patterns.
```

### Cost Projections
```
@energy-analyzer Project my annual electricity costs and show me potential savings scenarios.
```

### Efficiency Recommendations
```
@energy-analyzer Give me prioritized recommendations to reduce my energy bill by 20%.
```

### Appliance Breakdown
```
@energy-analyzer Estimate how much electricity each major appliance is using.
```

### Benchmark Comparison
```
@energy-analyzer Compare my usage to similar households in my region.
```

## File Structure

```
energy-usage-monitor/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   └── energy-analyzer.md
├── skills/
│   └── energy-monitoring/
│       └── SKILL.md
├── templates/
│   ├── energy-usage.csv
│   ├── usage-analysis.json
│   ├── cost-projections.json
│   ├── recommendations.md
│   └── appliance-breakdown.json
└── README.md
```

## Savings Potential

**Typical Household** (1200 kWh/month, $150/mo):

**Quick Wins** (1-6 months):
- Thermostat adjustment: $20/year
- LED bulbs: $100/year
- Phantom loads: $44/year
- **Total**: $164/year, $65 investment

**Medium Term** (1-3 years):
- Smart thermostat: $100/year
- Energy Star appliances: $50-150/year
- Insulation: $189/year
- **Total**: $339-439/year

**Long Term** (3-10 years):
- Heat pump water heater: $227/year
- HVAC upgrade: $315/year
- Solar panels: $1,697/year
- **Total**: $2,239/year (80% reduction)

## Integration

Works with data from:
- Utility company exports (CSV)
- Smart meter APIs
- Smart home energy monitors (Sense, Emporia)
- Manual bill entry

## Best Practices

1. **Monthly Review**: Track usage trends
2. **Seasonal Awareness**: Adjust for weather
3. **Implementation Priority**: Quick wins first
4. **ROI Focus**: Payback period <5 years
5. **Benchmark Regularly**: Track progress

## License

MIT License - See main repository for details

---

**Reduce your energy costs, lower your carbon footprint, and take control of your electricity usage with data-driven insights.**
