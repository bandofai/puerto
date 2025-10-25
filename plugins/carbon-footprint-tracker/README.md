# Carbon Footprint Tracker Plugin

Personal emissions tracking and reduction specialist with comprehensive carbon calculation, reduction recommendations, and progress tracking toward net-zero goals.

## Overview

This plugin provides a complete system for tracking, analyzing, and reducing your personal carbon footprint across all major categories: transport, energy, food, and goods.

**Key Features**:
- Fast daily emissions logging with automatic calculations
- Comprehensive footprint analysis with national/global comparisons
- Ranked reduction recommendations based on your data
- Monthly progress tracking with goal monitoring
- Expert carbon tracking skill with emission factors and proven strategies

## What's Included

### 4 Specialized Agents

1. **emissions-logger** (Haiku, Fast)
   - Quick daily activity logging
   - Automatic carbon calculation using emission factors
   - Categories: transport, energy, food, goods
   - JSON-based data storage

2. **footprint-analyzer** (Sonnet)
   - Comprehensive emissions analysis by time period
   - Category breakdowns and pattern identification
   - Comparison to US, EU, global averages and Paris targets
   - Top contributors and trend analysis

3. **reduction-advisor** (Sonnet)
   - Personalized reduction strategies ranked by impact
   - High/medium/low impact classifications
   - Implementation difficulty assessment
   - Cost-benefit analysis and action plans

4. **progress-reporter** (Sonnet)
   - Monthly progress reports vs. baseline
   - Goal tracking toward net-zero
   - Wins celebration and challenge identification
   - Updated recommendations based on progress

### 1 Comprehensive Skill

**carbon-tracking** - Expert knowledge including:
- Complete emission factors database (transport, energy, food, goods)
- Calculation methodologies and formulas
- National/global benchmarks and climate targets
- 20+ proven reduction strategies with impact estimates
- Offset recommendations and quality criteria
- Data validation and behavioral psychology insights

### Templates

1. **emissions-log-template.json**: Daily emissions logging structure
2. **reduction-plan-template.json**: Personalized reduction roadmap
3. **progress-report-template.json**: Monthly tracking format

## Quick Start

### 1. Install the Plugin

```bash
# Copy to your Puerto plugins directory
cp -r carbon-footprint-tracker ~/.claude/plugins/

# Or project-specific
cp -r carbon-footprint-tracker .claude/plugins/
```

### 2. Log Your First Emissions

Use the emissions-logger agent:

```
"Log 30 miles of driving today"
"Had a beef burger for lunch"
"Used 35 kWh of electricity this week"
```

The agent automatically:
- Reads carbon-tracking skill for emission factors
- Calculates CO2 emissions
- Saves to data/emissions-log.json
- Confirms entry with carbon total

### 3. Analyze Your Footprint

After logging for 7-30 days, use footprint-analyzer:

```
"Analyze my carbon footprint for the last 30 days"
```

Get comprehensive analysis:
- Total emissions and daily average
- Category breakdown (transport/energy/food/goods)
- Comparison to national and global averages
- Top 10 emission contributors
- Patterns and trends

### 4. Get Reduction Recommendations

Use reduction-advisor after analysis:

```
"Give me carbon reduction recommendations"
```

Receive personalized strategies:
- Ranked by potential impact (kg CO2/year saved)
- Categorized by difficulty (easy/moderate/hard)
- Specific action steps
- Implementation timeline
- Cost-benefit analysis

### 5. Track Progress

Use progress-reporter monthly:

```
"Generate my monthly carbon progress report"
```

See your journey:
- Current vs. previous period comparison
- Progress toward goals
- Wins and achievements
- Implemented strategies and results
- Updated recommendations

## Example Workflow

**Week 1-2**: Establish Baseline
```
1. Log daily activities with emissions-logger
2. After 14 days, run footprint-analyzer
3. Review category breakdowns
4. Understand your emissions profile
```

**Week 3-4**: Create Reduction Plan
```
1. Use reduction-advisor for personalized strategies
2. Choose 1-2 "quick wins" to start
3. Continue logging with emissions-logger
4. Implement chosen strategies
```

**Month 2+**: Track and Improve
```
1. Monthly: Run progress-reporter
2. Celebrate reductions, identify challenges
3. Adjust strategies based on results
4. Use reduction-advisor for next-level improvements
```

## Data Structure

### Emissions Log (data/emissions-log.json)

```json
{
  "entries": [
    {
      "id": "2025-01-22-001",
      "date": "2025-01-22",
      "category": "transport",
      "activity": "car_gasoline",
      "amount": 30,
      "unit": "miles",
      "carbon_kg": 6.3,
      "notes": "Commute to work"
    }
  ],
  "summary": {
    "total_entries": 1,
    "last_updated": "2025-01-22 14:30:00"
  }
}
```

### Categories

- **transport**: Cars, public transit, flights, rideshare
- **energy**: Electricity, natural gas, heating oil
- **food**: Meals, groceries (meat, dairy, plant-based)
- **goods**: Clothing, electronics, household items

## Emission Factor Examples

From carbon-tracking skill:

**Transport**:
- Gasoline car: 0.21 kg CO2/mile
- Electric vehicle: 0.08 kg CO2/mile
- Flight (medium-haul): 0.18 kg CO2/mile × 2.0 (radiative forcing)

**Energy**:
- Electricity (US avg): 0.42 kg CO2/kWh
- Natural gas: 5.3 kg CO2/therm

**Food**:
- Beef: 27 kg CO2/kg
- Chicken: 6.9 kg CO2/kg
- Plant-based meal: 0.3 kg CO2/meal

**Goods**:
- T-shirt (new): 7 kg CO2
- Smartphone: 80 kg CO2
- Secondhand clothing: 0.5 kg CO2

## Benchmarks

**National Averages** (kg CO2/year):
- United States: 16,000
- European Union: 8,000
- Global Average: 4,800
- Paris Agreement Target: 2,300
- Net-Zero Goal: <500

**US Breakdown**:
- Transport: 6,400 kg (40%)
- Energy: 4,800 kg (30%)
- Food: 3,200 kg (20%)
- Goods: 1,600 kg (10%)

## High-Impact Reduction Strategies

Top strategies from carbon-tracking skill:

1. **Electric Vehicle**: -2,000 to -4,000 kg/year
2. **Renewable Energy Plan**: -3,000 to -5,000 kg/year
3. **Solar Panels**: -4,000 to -6,000 kg/year
4. **Vegetarian Diet**: -700 to -1,000 kg/year
5. **Reduce Air Travel**: -500 to -2,000 kg/flight avoided
6. **Public Transit Commute**: -1,000 to -2,000 kg/year
7. **Remote Work 2-3x/week**: -1,000 to -1,500 kg/year

## Architecture

### Skills-First Approach

All agents follow Puerto's skill-aware pattern:

1. **Read carbon-tracking skill first** (MANDATORY)
2. Use authoritative emission factors
3. Apply proven calculation methods
4. Follow best practices for analysis and recommendations

### Cost-Optimized Model Selection

- **emissions-logger**: Haiku (fast, cheap for deterministic calculations)
- **footprint-analyzer**: Sonnet (analysis requires judgment)
- **reduction-advisor**: Sonnet (personalization and strategy)
- **progress-reporter**: Sonnet (comprehensive reporting)

### Data Flow

```
emissions-logger → data/emissions-log.json
                          ↓
              footprint-analyzer → data/analysis-{date}.json
                          ↓
              reduction-advisor → data/reduction-plan.json
                          ↓
              progress-reporter → data/progress-{date}.json
```

## Configuration

No configuration required. The plugin works out of the box with:
- Default emission factors (US-based, adjustable)
- Standard benchmarks
- Proven reduction strategies

Optional customization:
- Edit emission factors in carbon-tracking skill for your region
- Adjust benchmarks for your country
- Add custom activities and emission factors

## Use Cases

**Individual**: Track personal footprint, set reduction goals, monitor progress

**Family**: Household emissions tracking, shared reduction targets

**Small Business**: Employee commute and office energy tracking

**Researcher**: Personal carbon accounting for climate research

**Climate Activist**: Lead by example, share progress with community

## Integration

Works well with other Puerto plugins:

- **Energy Usage Monitor**: Detailed electricity/gas tracking
- **Meal Planning & Nutrition**: Food emission optimization
- **Travel Planning Assistant**: Low-carbon travel options
- **Bill Optimization Analyzer**: Renewable energy plan switching

## Privacy & Data

- All data stored locally in plugin data/ directory
- No external API calls or data sharing
- JSON format for easy backup and portability
- User has complete control over data

## Limitations

- Emission factors are averages (actual may vary by region)
- Food portions are estimates (unless weighed)
- Some categories harder to track (embodied emissions in goods)
- Relies on user consistency in logging

## Future Enhancements

Potential additions:
- Integration with utility APIs for automatic energy data
- Receipt scanning for goods emissions
- GPS tracking for automatic transport logging
- Social features for community challenges
- Offset marketplace integration

## Support

For issues, suggestions, or contributions:
- GitHub: https://github.com/bandofai/puerto
- Issue template: Carbon Footprint Tracker - #128

## License

Part of Puerto plugin ecosystem.

## Credits

- Emission factors: IPCC, EPA, Carbon Trust, Our World in Data
- Reduction strategies: Project Drawdown, Carbon Brief
- Plugin architecture: Puerto/Claude Code best practices

---

**Version**: 1.0.0
**Last Updated**: January 2025
**Status**: Production Ready

Start tracking your carbon footprint today and join the journey to net-zero! 🌍💚
