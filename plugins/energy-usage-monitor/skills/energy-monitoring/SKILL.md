# Energy Usage Monitoring & Optimization Skill

Comprehensive guide for analyzing electricity consumption, detecting patterns, projecting costs, and identifying efficiency improvements.

## Core Principles

1. **Data-Driven Decisions**: Base recommendations on actual usage data
2. **ROI Focus**: Prioritize improvements by payback period
3. **Behavioral + Technical**: Combine zero-cost changes with upgrades
4. **Seasonal Awareness**: Account for heating/cooling variations
5. **Benchmark Context**: Compare to similar households for perspective

## Data Analysis Framework

### Smart Meter Data Processing

**Data Sources**:
- Utility CSV export (interval data)
- Smart meter API (real-time or hourly)
- Monthly bills (high-level only)
- Smart home devices (Sense, Emporia)

**Key Fields**:
- Timestamp (date/time)
- Usage (kWh per interval)
- Cost (optional)
- Rate tier (if applicable)

**Processing Steps**:
1. Import and validate data
2. Handle missing values (interpolate or flag)
3. Detect and investigate anomalies
4. Calculate summary statistics
5. Identify patterns and trends

### Usage Pattern Detection

**Baseline Load** (overnight minimum):
- Refrigerator, phantom loads, always-on devices
- Typically 0.3-1.0 kW for most homes
- Sudden increases indicate new always-on device

**Peak Times**:
- **Morning** (6-9am): Water heater, coffee, breakfast
- **Evening** (5-10pm): Cooking, lighting, entertainment, HVAC
- Identify specific appliance signatures

**Day-of-Week Patterns**:
- Weekdays vs weekends
- Work-from-home vs away patterns
- Opportunity for scheduling optimization

**Seasonal Variations**:
- Summer: AC drives peaks (30-50% increase)
- Winter: Heating if electric (20-40% increase)
- Spring/Fall: Lowest usage periods

### Anomaly Detection

**Red Flags**:
- Usage spike >200% of normal (appliance malfunction?)
- Extended zero usage (meter/data issue)
- Baseline increase (new always-on device)
- Unexpected high overnight usage (water heater issue?)

**Investigation Questions**:
- When did it start?
- Any new appliances or changes?
- Weather correlation?
- Similar pattern on other days?

## Cost Projection Models

### Basic Monthly Projection
```
Daily average kWh × 30 days × Rate = Monthly cost
Monthly cost × 12 = Annual projection
```

### Seasonal Adjustment
```
Summer (Jun-Aug): Base × 1.35
Winter (Dec-Feb): Base × 1.25 (if electric heat)
Spring/Fall: Base × 0.90
```

### Time-of-Use (TOU) Rates
```
Peak hours (typically 2pm-8pm): Higher rate ($0.25-0.40/kWh)
Off-peak hours (9pm-8am): Lower rate ($0.10-0.15/kWh)
Mid-peak: Medium rate ($0.15-0.20/kWh)

Optimal: Shift usage to off-peak (dishwasher, laundry, EV charging)
```

### Tiered Pricing
```
Tier 1: 0-500 kWh @ base rate
Tier 2: 501-1000 kWh @ base + 20%
Tier 3: 1001+ kWh @ base + 40%

Strategy: Stay in lower tiers through conservation
```

## Efficiency Recommendations

### Quick Wins (Free - $50)

**Behavioral Changes** (Immediate, $0):
1. **Thermostat adjustment**: +2°F summer, -2°F winter = 5-10% savings
2. **Unplug phantom loads**: Electronics, chargers = 5-10% savings
3. **Cold water washing**: Avoid water heater = 3-5% savings
4. **Natural lighting**: Reduce daytime lights = 2-3% savings
5. **Air-dry dishes**: Skip dishwasher heat dry = 1-2% savings

**Low-Cost Fixes** (<$50):
1. **LED bulbs**: $5-10 each, 75% lighting reduction, 1-year payback
2. **Smart power strips**: $20-30, eliminate phantom loads
3. **Weather stripping**: $15-30, reduce HVAC air leaks
4. **Faucet aerators**: $10-20, reduce hot water use
5. **Door sweeps**: $15-25, seal drafts

### Medium Investments ($50-$1000)

**Programmable/Smart Thermostats** ($100-250):
- Savings: 10-15% HVAC costs
- Payback: 1-2 years
- Features: Scheduling, learning, remote control

**Energy Star Appliances**:
- **Refrigerator** ($600-1200): 300-400 kWh/year savings
- **Washing machine** ($500-900): 200-300 kWh/year savings
- **Dishwasher** ($400-800): 100-200 kWh/year savings
- Payback: 3-5 years depending on current appliance age

**Water Heater Improvements** ($300-800):
- Tank insulation blanket: $30, 5-10% savings
- Pipe insulation: $20, 3-5% savings
- Timer: $50-100, 5-10% savings
- Upgrade to tankless/heat pump: $800-3000, 30-50% savings

**Window Treatments** ($200-600):
- Cellular shades: Reduce heat loss/gain 20-40%
- Window film: Block solar heat, reduce AC load 10-15%
- Thermal curtains: Insulate windows, 10-25% heat reduction

### Major Upgrades ($1000+)

**HVAC System Upgrade** ($3000-8000):
- Heat pump: 50% more efficient than resistance heating
- High-SEER AC: 20-40% improvement over old systems
- Proper sizing critical for efficiency
- Payback: 5-10 years

**Insulation** ($1500-4000):
- Attic: R-38 to R-60, 15-25% HVAC savings
- Walls: R-13 to R-21, 10-15% savings
- Payback: 5-8 years

**Solar Panels** ($15,000-30,000):
- Eliminate 70-100% of grid usage
- Federal tax credit: 30%
- Payback: 7-12 years (varies by location)
- 25-30 year lifespan

**Windows** ($3000-10,000):
- Double/triple pane
- Low-E coating
- 25-30% heat loss reduction
- Payback: 10-20 years

**Battery Storage** ($8000-15,000):
- Shift usage to off-peak
- Backup power
- Maximize solar value
- Payback: 10-15 years

## Appliance Consumption Estimates

### Major Energy Users

**HVAC (40-50% of total)**:
- Central AC: 3000-5000 kWh/year
- Electric furnace: 5000-10,000 kWh/year
- Heat pump: 3000-6000 kWh/year

**Water Heating (15-20%)**:
- Tank: 3000-4500 kWh/year
- Tankless: 2000-3000 kWh/year
- Heat pump: 1500-2500 kWh/year

**Lighting (10-15%)**:
- Incandescent: 1000-1500 kWh/year
- CFL: 400-600 kWh/year
- LED: 250-375 kWh/year

**Kitchen Appliances (10-15%)**:
- Refrigerator: 400-600 kWh/year
- Dishwasher: 300-500 kWh/year
- Oven/stove: 500-800 kWh/year

**Laundry (5-8%)**:
- Washer: 50-150 kWh/year
- Dryer: 700-1000 kWh/year

**Electronics (5-10%)**:
- TV + streaming: 100-200 kWh/year
- Computer: 100-200 kWh/year
- Gaming console: 100-300 kWh/year
- Phantom loads: 300-500 kWh/year

### Estimation Method

1. **Identify baseline**: Overnight minimum = always-on
2. **Detect spikes**: Match timing to appliance use
3. **Calculate draw**: Spike - baseline = appliance
4. **Multiply duration**: kW × hours = kWh
5. **Extrapolate annual**: Daily use × 365

## Benchmark Comparisons

### National Averages (US)

**By Home Size**:
- <1000 sq ft: 500-700 kWh/month
- 1000-2000 sq ft: 700-1000 kWh/month
- 2000-3000 sq ft: 1000-1500 kWh/month
- 3000+ sq ft: 1500+ kWh/month

**By Region** (monthly average):
- Northeast: 650 kWh ($90-130)
- Midwest: 850 kWh ($95-120)
- South: 1200 kWh ($130-160) - high AC use
- West: 750 kWh ($110-150)

**By Household Size**:
- 1 person: 500-700 kWh/month
- 2 people: 700-900 kWh/month
- 3-4 people: 900-1200 kWh/month
- 5+ people: 1200+ kWh/month

### Efficiency Categories

**Excellent** (Top 10%): <6 kWh/sq.ft/year
**Good** (Top 25%): 6-9 kWh/sq.ft/year
**Average** (50th %ile): 9-12 kWh/sq.ft/year
**High** (Top 25%): >12 kWh/sq.ft/year

## Reporting Templates

### Monthly Summary
```markdown
# Energy Usage Report - [Month Year]

## Usage Summary
- Total kWh: [X]
- Total Cost: $[Y]
- Average daily: [Z] kWh
- vs Last Month: [+/-]%
- vs Last Year: [+/-]%

## Pattern Analysis
- Peak day: [Date] ([X] kWh)
- Peak hour: [Hour] ([X] kW)
- Baseline load: [X] kW (always-on)
- Notable anomalies: [List]

## Cost Breakdown
- Electricity: $[X]
- Delivery charges: $[Y]
- Taxes: $[Z]
- Effective rate: $[X]/kWh

## Projections
- This month forecast: $[X]
- Annual projection: $[Y]
- Potential savings: $[Z]

## Top Recommendations
1. [Recommendation] - Save $[X]/year
2. [Recommendation] - Save $[X]/year
3. [Recommendation] - Save $[X]/year
```

### Annual Review
```markdown
# Annual Energy Review - [Year]

## Summary
- Total Usage: [X] kWh
- Total Cost: $[Y]
- Average monthly: [Z] kWh
- vs Previous Year: [+/-]%

## Seasonal Analysis
- Summer (Jun-Aug): [X] kWh avg/month
- Winter (Dec-Feb): [X] kWh avg/month
- Spring (Mar-May): [X] kWh avg/month
- Fall (Sep-Nov): [X] kWh avg/month

## Benchmark Comparison
- Your usage: [X] kWh/sq.ft/year
- Similar homes: [Y] kWh/sq.ft/year
- You rank: [Top X%ile]
- Potential savings: $[Z]/year to reach avg

## Efficiency Progress
- Improvements made: [List]
- kWh saved: [X]
- Cost saved: $[Y]
- ROI achieved: [Z]%

## Next Year Goals
1. [Goal] - Target [X]% reduction
2. [Goal] - Implement [Y]
3. [Goal] - Achieve $[Z] savings
```

## Quality Checklist

Before completing analysis:
- [ ] Data validated for completeness
- [ ] Usage patterns identified and explained
- [ ] Cost projections include all rate factors
- [ ] Min 5 recommendations with ROI
- [ ] Benchmark comparison provided
- [ ] Seasonal analysis if >3 months data
- [ ] Appliance estimates included
- [ ] Summary actionable and clear

---

**Remember**: Energy efficiency is a journey, not a destination. Small consistent improvements compound to significant savings over time.
