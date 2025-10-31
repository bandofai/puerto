# Carbon Tracking Skill

**Expert knowledge for carbon footprint calculation, analysis, and reduction strategies**

This skill provides comprehensive emission factors, calculation methodologies, and proven reduction strategies for personal carbon footprint tracking.

---

## Part 1: Emission Factors Database

### Transport Emissions

**Personal Vehicles** (kg CO2 per mile):
- Gasoline car (average): 0.21 kg/mile
- Diesel car: 0.19 kg/mile
- Hybrid car: 0.12 kg/mile
- Electric vehicle (US grid avg): 0.08 kg/mile
- Electric vehicle (renewable energy): 0.01 kg/mile
- Motorcycle: 0.15 kg/mile
- Scooter/moped: 0.08 kg/mile

**Public Transportation** (kg CO2 per mile):
- Bus: 0.05 kg/mile (per passenger)
- Subway/metro: 0.04 kg/mile
- Commuter train: 0.06 kg/mile
- Intercity train: 0.04 kg/mile

**Ride Services** (kg CO2 per mile):
- Taxi/Uber/Lyft: 0.25 kg/mile (solo)
- UberPool/shared: 0.13 kg/mile
- Bike share: 0.00 kg/mile
- E-scooter share: 0.03 kg/mile

**Air Travel** (kg CO2 per mile):
- Short-haul (<300 mi): 0.24 kg/mile
- Medium-haul (300-2300 mi): 0.18 kg/mile
- Long-haul (>2300 mi): 0.15 kg/mile
- First class: 2-3x economy (more space = higher allocation)

**Radiative Forcing Multiplier for Aviation**: 2.0
(Air travel has additional climate impact beyond CO2, multiply by 2.0 for total climate impact)

---

### Energy Emissions

**Electricity** (kg CO2 per kWh by grid):
- US average: 0.42 kg/kWh
- Coal-heavy regions: 0.80 kg/kWh
- California (cleaner grid): 0.22 kg/kWh
- Renewable energy: 0.00 kg/kWh
- EU average: 0.30 kg/kWh
- Global average: 0.48 kg/kWh

**Natural Gas** (kg CO2 per therm):
- Heating: 5.3 kg/therm
- Water heating: 5.3 kg/therm

**Heating Oil** (kg CO2 per gallon):
- Home heating oil: 10.2 kg/gallon

**Propane** (kg CO2 per gallon):
- 5.7 kg/gallon

**Typical Home Energy Usage** (monthly averages):
- Average US home electricity: 877 kWh/month = 368 kg CO2/month
- Natural gas heating: 40 therms/month (winter) = 212 kg CO2/month
- Natural gas (summer): 10 therms/month = 53 kg CO2/month

---

### Food Emissions

**Meat** (kg CO2 per kg):
- Beef: 27.0 kg CO2/kg
- Lamb: 39.2 kg CO2/kg
- Pork: 12.1 kg CO2/kg
- Chicken: 6.9 kg CO2/kg
- Turkey: 10.9 kg CO2/kg
- Fish (farmed): 13.6 kg CO2/kg
- Fish (wild-caught): 5.0 kg CO2/kg

**Dairy** (kg CO2 per kg):
- Cheese: 13.5 kg CO2/kg
- Milk: 1.9 kg CO2/L
- Butter: 12.0 kg CO2/kg
- Yogurt: 2.2 kg CO2/kg
- Eggs: 4.8 kg CO2/kg (per dozen)

**Plant-Based Proteins** (kg CO2 per kg):
- Tofu: 2.0 kg CO2/kg
- Beans/lentils: 0.9 kg CO2/kg
- Nuts: 2.3 kg CO2/kg
- Peas: 0.9 kg CO2/kg

**Produce** (kg CO2 per kg):
- Vegetables (local, in-season): 0.4 kg CO2/kg
- Vegetables (imported, off-season): 2.0 kg CO2/kg
- Fruit (local, in-season): 0.4 kg CO2/kg
- Fruit (air-freighted): 5.0 kg CO2/kg
- Root vegetables: 0.3 kg CO2/kg

**Grains & Starches** (kg CO2 per kg):
- Rice: 2.7 kg CO2/kg
- Wheat bread: 0.9 kg CO2/kg
- Pasta: 1.2 kg CO2/kg
- Potatoes: 0.3 kg CO2/kg

**Meal Estimates** (kg CO2 per meal):
- Beef-based meal (8 oz beef): 6.1 kg CO2
- Chicken-based meal (6 oz chicken): 1.2 kg CO2
- Fish-based meal (6 oz fish): 1.5 kg CO2
- Vegetarian meal: 0.5 kg CO2
- Vegan meal: 0.3 kg CO2

**Food Waste**:
- Add 25% to all food emissions if not consumed
- Food waste in landfills produces methane (higher impact)

---

### Goods & Services Emissions

**Clothing** (kg CO2 per item):
- T-shirt (cotton): 7.0 kg CO2
- Jeans: 33.4 kg CO2
- Dress: 47.0 kg CO2
- Shoes: 14.0 kg CO2
- Winter coat: 40.0 kg CO2
- Secondhand (any): 0.5 kg CO2 (transport only)

**Electronics** (kg CO2 per item):
- Smartphone: 80 kg CO2
- Laptop: 200 kg CO2
- Desktop computer: 350 kg CO2
- Tablet: 120 kg CO2
- TV (50"): 300 kg CO2
- Smartwatch: 30 kg CO2

**Household Items** (kg CO2 per item):
- Furniture (average piece): 100 kg CO2
- Mattress: 150 kg CO2
- Appliances (average): 200 kg CO2

**Services** (kg CO2):
- Online shopping delivery: 1.0 kg CO2 per package
- Express shipping: 2.5 kg CO2 per package
- Streaming video: 0.05 kg CO2/hour
- Cloud storage: 0.2 kg CO2/month per 100 GB

**Repair vs. Replace Credit**:
- Repairing an item: -50% of replacement emissions avoided

---

## Part 2: Calculation Methodologies

### Activity-Based Calculation

```python
def calculate_emission(activity_type, amount, unit, metadata=None):
    """
    Calculate carbon emissions for an activity

    Args:
        activity_type: Type of activity (e.g., 'car_gasoline', 'beef', 'electricity')
        amount: Quantity of activity
        unit: Unit of measurement (miles, kg, kWh, etc.)
        metadata: Optional dict with additional context (location, efficiency, etc.)

    Returns:
        float: kg CO2 equivalent
    """

    # Get emission factor from database
    factor = EMISSION_FACTORS[activity_type]

    # Apply regional adjustments if applicable
    if metadata and 'location' in metadata:
        factor = adjust_for_location(factor, metadata['location'])

    # Calculate base emissions
    emissions = amount * factor

    # Apply special multipliers
    if activity_type.startswith('flight'):
        # Radiative forcing for aviation
        emissions *= 2.0

    return round(emissions, 2)
```

### Time-Period Aggregation

```python
def calculate_period_total(entries, start_date, end_date):
    """
    Calculate total emissions for a time period

    Returns:
        dict: {
            'total_kg': float,
            'by_category': dict,
            'by_activity': dict,
            'daily_average': float,
            'days_in_period': int
        }
    """

    filtered = [e for e in entries if start_date <= e['date'] <= end_date]

    total = sum(e['carbon_kg'] for e in filtered)

    by_category = {}
    for entry in filtered:
        cat = entry['category']
        by_category[cat] = by_category.get(cat, 0) + entry['carbon_kg']

    days = (end_date - start_date).days + 1
    daily_avg = total / days

    return {
        'total_kg': total,
        'by_category': by_category,
        'daily_average': daily_avg,
        'days_in_period': days,
        'annual_projection': daily_avg * 365
    }
```

### Comparison Calculations

```python
def compare_to_benchmarks(annual_kg):
    """
    Compare user's emissions to national and global averages

    Returns:
        dict: Percentage above/below each benchmark
    """

    benchmarks = {
        'us_average': 16000,
        'eu_average': 8000,
        'global_average': 4800,
        'paris_target': 2300,
        'net_zero': 0
    }

    comparisons = {}
    for name, value in benchmarks.items():
        diff_pct = ((annual_kg - value) / value) * 100
        comparisons[name] = {
            'kg': value,
            'user_vs_benchmark_pct': diff_pct,
            'above_below': 'above' if diff_pct > 0 else 'below'
        }

    return comparisons
```

---

## Part 3: Benchmarks & Targets

### National Averages (kg CO2/year)

- **United States**: 16,000 kg/year (~44 kg/day)
- **Canada**: 15,600 kg/year
- **Australia**: 16,800 kg/year
- **Germany**: 8,400 kg/year
- **United Kingdom**: 5,500 kg/year
- **France**: 4,600 kg/year
- **Japan**: 8,500 kg/year
- **China**: 7,400 kg/year
- **India**: 1,900 kg/year
- **Global Average**: 4,800 kg/year (~13 kg/day)

### Climate Targets

- **Paris Agreement Target** (2°C pathway): 2,300 kg/year by 2050
- **Net-Zero Target**: 0-500 kg/year (with offsets)
- **1.5°C Pathway**: 2,000 kg/year by 2030, 500 kg/year by 2050

### Category Breakdowns (US Average)

**Total**: 16,000 kg CO2/year

- Transport: 6,400 kg (40%)
- Energy: 4,800 kg (30%)
- Food: 3,200 kg (20%)
- Goods: 1,600 kg (10%)

### Low-Carbon Lifestyle Targets

**Level 1 - Below National Average**: <12,000 kg/year (US)
- Making some conscious choices
- Room for significant improvement

**Level 2 - Climate Conscious**: 6,000-8,000 kg/year
- Active reduction efforts
- Above global average, below US average

**Level 3 - Low-Carbon Leader**: 3,000-6,000 kg/year
- Major lifestyle changes implemented
- Near global average

**Level 4 - Climate Champion**: 1,500-3,000 kg/year
- Significant sacrifices and investments
- Paris Agreement pathway

**Level 5 - Near Net-Zero**: <1,500 kg/year
- Extreme dedication
- Offsetting remaining emissions

---

## Part 4: Reduction Strategies

### High-Impact Strategies (>500 kg CO2/year)

#### Transport

**1. Electric Vehicle** (-2,000 to -4,000 kg/year)
- Replace gasoline car with EV
- Savings: 0.21 - 0.08 = 0.13 kg/mile
- Average 15,000 miles/year = 1,950 kg saved
- More with renewable energy charging
- Cost: $30,000-50,000 (minus incentives)
- Difficulty: 🔴 Hard (high upfront cost)
- Timeframe: When current car needs replacement

**2. Go Car-Free** (-2,500 to -5,000 kg/year)
- Use bike/walk/transit exclusively
- Savings: Entire transport footprint
- Cost: Save money! (no car payments, insurance, gas)
- Difficulty: 🔴 Hard (requires lifestyle change, location dependent)
- Timeframe: Consider when relocating

**3. Reduce Air Travel** (-500 to -2,000 kg per avoided flight)
- One avoided round-trip flight (US coast-to-coast): -1,000 kg
- International flight avoided: -1,500 to -2,500 kg
- Cost: Free (save money)
- Difficulty: 🟡 Moderate (depends on job, family situation)
- Timeframe: Immediate

**4. Remote Work 2-3 Days/Week** (-1,000 to -1,500 kg/year)
- Avoid commuting 40-60% of days
- 20-mile round-trip commute × 100 days = 420 miles = 88 kg saved
- Cost: Free (save money on gas)
- Difficulty: 🟡 Moderate (requires employer flexibility)
- Timeframe: Immediate if employer allows

#### Energy

**5. Renewable Energy Plan** (-3,000 to -5,000 kg/year)
- Switch electricity to 100% renewable
- Average home 877 kWh/month × 0.42 kg/kWh × 12 = 4,418 kg saved
- Cost: Often same or slightly higher than standard plan
- Difficulty: 🟢 Easy (one phone call)
- Timeframe: Immediate

**6. Solar Panels** (-4,000 to -6,000 kg/year)
- 5 kW system generates ~7,000 kWh/year
- Savings: 7,000 × 0.42 = 2,940 kg (plus natural gas offset)
- Cost: $15,000-25,000 (minus incentives), pays back in 7-10 years
- Difficulty: 🔴 Hard (high upfront cost, requires home ownership)
- Timeframe: 3-6 months planning and installation

**7. Heat Pump** (-1,000 to -3,000 kg/year)
- Replace gas furnace with electric heat pump
- Savings varies by climate and current system
- Cost: $5,000-15,000 (minus incentives)
- Difficulty: 🔴 Hard (significant investment)
- Timeframe: When HVAC needs replacement

#### Food

**8. Vegetarian Diet** (-700 to -1,000 kg/year)
- Eliminate all meat, keep dairy/eggs
- Average American eats 100 kg meat/year
- Savings: ~10 kg CO2/kg meat avoided = 1,000 kg
- Cost: Save money (meat is expensive)
- Difficulty: 🟡 Moderate (habit change)
- Timeframe: Can start immediately, fully transition in 3-6 months

**9. Vegan Diet** (-900 to -1,400 kg/year)
- Eliminate all animal products
- Savings: Meat + dairy = higher than vegetarian
- Cost: Save money
- Difficulty: 🔴 Hard (significant lifestyle change, social challenges)
- Timeframe: 6-12 months for full transition

---

### Medium-Impact Strategies (100-500 kg CO2/year)

#### Transport

**10. Public Transit for Commute** (-1,000 to -2,000 kg/year)
- Replace car commute with bus/train
- 20-mile commute × 250 days = 5,000 miles
- Savings: (0.21 - 0.05) × 5,000 = 800 kg
- Cost: Save money (transit pass < gas + parking)
- Difficulty: 🟡 Moderate (requires good transit access)
- Timeframe: Immediate

**11. Carpool 3 Days/Week** (-400 to -800 kg/year)
- Share rides with coworker
- Split driving = 50% of commute emissions
- Cost: Save money
- Difficulty: 🟢 Easy (requires finding carpool partner)
- Timeframe: Immediate

**12. Bike for Short Trips (<5 mi)** (-300 to -600 kg/year)
- Replace car trips with biking
- 10 short trips/week × 5 miles × 0.21 kg/mile × 52 weeks = 546 kg
- Cost: Save money (one-time bike cost)
- Difficulty: 🟢 Easy (weather and safety dependent)
- Timeframe: Immediate

#### Energy

**13. Improve Home Insulation** (-500 to -1,500 kg/year)
- Reduce heating/cooling needs 20-30%
- Savings: 20% of heating/cooling emissions
- Cost: $1,000-5,000 (varies by home size)
- Difficulty: 🟡 Moderate (requires contractor)
- Timeframe: 1-3 months

**14. Smart Thermostat** (-300 to -500 kg/year)
- Optimize heating/cooling automatically
- 10-15% energy savings
- Cost: $100-250, pays back in 1-2 years
- Difficulty: 🟢 Easy (DIY installation)
- Timeframe: Immediate

**15. LED Lighting** (-100 to -200 kg/year)
- Replace all bulbs with LEDs
- 75% less energy than incandescent
- Cost: $50-150 for whole home, pays back in 1 year
- Difficulty: 🟢 Easy
- Timeframe: Immediate

#### Food

**16. Reduce Beef 50%** (-400 to -600 kg/year)
- Cut beef consumption in half
- Replace with chicken or plant-based
- Beef: 27 kg CO2/kg, Chicken: 6.9 kg CO2/kg
- Savings per kg switched: 20 kg CO2
- Cost: Save money
- Difficulty: 🟢 Easy (gradual shift)
- Timeframe: Start immediately

**17. Meatless 3 Days/Week** (-300 to -500 kg/year)
- Plant-based meals 3x/week
- 43% of meals meat-free
- Cost: Save money
- Difficulty: 🟢 Easy (many recipes available)
- Timeframe: Immediate

**18. Reduce Food Waste 50%** (-200 to -400 kg/year)
- Better meal planning, use leftovers
- Average American wastes 40% of food
- Reducing waste = not needing to produce that food
- Cost: Save money ($1,000+/year)
- Difficulty: 🟢 Easy (requires planning)
- Timeframe: Immediate

#### Goods

**19. Buy Secondhand Clothing** (-100 to -300 kg/year)
- Avoid new clothing production
- Average American buys 60 new items/year
- New: 20 kg CO2/item avg, Secondhand: 0.5 kg
- Savings: 30 items × 19.5 kg = 585 kg (if 50% secondhand)
- Cost: Save money
- Difficulty: 🟢 Easy
- Timeframe: Immediate

**20. Reduce Online Shopping 50%** (-100 to -200 kg/year)
- Less frequent purchases, consolidate orders
- Savings on shipping emissions + reduced consumption
- Cost: Save money
- Difficulty: 🟢 Easy (requires mindful purchasing)
- Timeframe: Immediate

---

### Low-Impact Strategies (<100 kg CO2/year)

**21. Line-Dry Clothes** (-50 to -100 kg/year)
- Skip the dryer when possible
- Cost: Save money on electricity
- Difficulty: 🟢 Easy

**22. Cold Water Laundry** (-50 to -100 kg/year)
- 90% of washing machine energy is heating water
- Difficulty: 🟢 Easy

**23. Reusable Bags & Containers** (-10 to -30 kg/year)
- Avoid single-use plastics
- Difficulty: 🟢 Easy

**24. Plant-Based Milk** (-30 to -60 kg/year)
- Oat/soy milk: 0.9 kg CO2/L vs. Dairy: 1.9 kg CO2/L
- Difficulty: 🟢 Easy

---

## Part 5: Offset Recommendations

### Offset Quality Criteria

**Look for**:
- Third-party verification (Gold Standard, VCS, CAR)
- Additionality (wouldn't happen without offset funding)
- Permanence (carbon stays sequestered long-term)
- Co-benefits (biodiversity, local community support)

### Offset Project Types

**1. Renewable Energy Projects**
- Wind farms, solar installations in developing countries
- Cost: $10-20/ton CO2
- Quality: High additionality
- Impact timeline: Immediate

**2. Reforestation/Afforestation**
- Tree planting and forest protection
- Cost: $5-15/ton CO2
- Quality: Medium (permanence risk from fires)
- Impact timeline: 10-30 years for full sequestration

**3. Direct Air Capture**
- Technology that removes CO2 from atmosphere
- Cost: $100-600/ton CO2
- Quality: Highest permanence
- Impact timeline: Immediate and permanent

**4. Cookstove Projects**
- Efficient cookstoves in developing countries
- Cost: $5-10/ton CO2
- Quality: High co-benefits (health, poverty reduction)
- Impact timeline: Immediate

### Recommended Offset Amounts

**For Average American** (16,000 kg/year):
- After reductions to 6,000 kg/year: Offset ~6,000 kg
- Cost at $15/ton: $90/year
- Remaining 6,000 kg: Continue reducing over time

**For Climate Champion** (2,000 kg/year):
- Offset remaining 2,000 kg
- Cost at $15/ton: $30/year
- Approaching net-zero!

---

## Part 6: Data Quality & Validation

### Logging Best Practices

**1. Consistency**
- Log daily or weekly (not monthly)
- Capture all categories
- Don't cherry-pick (log high-emission activities too)

**2. Accuracy**
- Use actual data when possible (odometer, utility bills)
- Estimate portion sizes for food (kitchen scale helps)
- Round to reasonable precision (no false precision)

**3. Completeness**
- Include all four categories
- Track irregular events (flights, major purchases)
- Note seasonal variations

### Common Estimation Errors

**Underestimation**:
- Forgetting indirect emissions (online shopping shipping)
- Omitting categories (goods purchases)
- Not tracking small frequent activities (coffee shop trips)

**Overestimation**:
- Double-counting (electricity already includes appliances)
- Using worst-case emission factors
- Not accounting for shared emissions (carpooling)

### Data Validation Checks

```python
def validate_entry(entry):
    """Validate emissions log entry for data quality"""

    issues = []

    # Reasonableness checks
    if entry['category'] == 'transport':
        if entry['carbon_kg'] > 100:  # ~500 miles driving in one day
            issues.append("Very high daily transport emissions - verify accuracy")

    if entry['category'] == 'energy':
        if entry['carbon_kg'] > 50:  # ~120 kWh in one day
            issues.append("Very high daily energy use - check if monthly data entered as daily")

    if entry['category'] == 'food':
        if entry['carbon_kg'] > 20:  # Multiple beef meals
            issues.append("High food emissions for one day - verify portions")

    # Required fields
    required = ['date', 'category', 'activity', 'amount', 'carbon_kg']
    for field in required:
        if field not in entry:
            issues.append(f"Missing required field: {field}")

    # Valid categories
    if entry['category'] not in ['transport', 'energy', 'food', 'goods']:
        issues.append(f"Invalid category: {entry['category']}")

    return issues
```

---

## Part 7: Behavioral Psychology for Reduction

### Motivation Strategies

**1. Make Progress Visible**
- Track daily/weekly totals
- Show cumulative savings
- Visualize equivalents (trees, miles, etc.)

**2. Celebrate Wins**
- Acknowledge any reduction
- Compare to previous periods
- Share achievements

**3. Start Small**
- Pick 1-2 easy changes first
- Build momentum with quick wins
- Add more changes gradually

**4. Focus on Co-Benefits**
- Health (biking, plant-based diet)
- Money savings (energy efficiency, less shopping)
- Quality of life (less commuting, decluttering)

### Common Barriers & Solutions

**Barrier**: "Too expensive"
**Solution**: Focus on free/money-saving changes first (meatless meals, line-dry clothes, bike for short trips)

**Barrier**: "Too inconvenient"
**Solution**: Start with easiest changes, make low-carbon option the default

**Barrier**: "Won't make a difference"
**Solution**: Show cumulative impact, connect to larger movement

**Barrier**: "Don't know where to start"
**Solution**: Use footprint analyzer to identify biggest categories, start there

### Habit Formation Tips

**1. Stack with Existing Habits**
- "When I make coffee, I'll choose plant milk"
- "When I drive, I'll combine errands to reduce trips"

**2. Make It Easy**
- Keep reusable bags in car
- Set smart thermostat once
- Meal prep on Sundays

**3. Track Publicly**
- Share progress with friends
- Join online community
- Accountability partner

---

## Summary: Using This Skill

All carbon-tracking agents should:

1. **Read this skill first** - Contains authoritative data
2. **Use accurate emission factors** - From Part 1
3. **Apply correct calculations** - From Part 2
4. **Compare to benchmarks** - From Part 3
5. **Recommend proven strategies** - From Part 4
6. **Suggest quality offsets** - From Part 5
7. **Validate data quality** - From Part 6
8. **Apply behavioral insights** - From Part 7

This ensures consistent, accurate carbon tracking and effective reduction guidance.

---

**Version**: 1.0
**Last Updated**: January 2025
**Sources**: IPCC, EPA, Carbon Trust, Our World in Data
**Scope**: Personal carbon footprint (excludes government/infrastructure emissions allocated to individuals)
