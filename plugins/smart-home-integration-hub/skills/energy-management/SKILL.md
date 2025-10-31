# Energy Management Skill

**Expert strategies for monitoring, analyzing, and optimizing smart home energy consumption**

This skill provides comprehensive patterns and best practices for tracking energy usage, detecting anomalies, calculating costs, and implementing optimization strategies in smart homes.

---

## Core Principles

### 1. Accurate Measurement
Energy management starts with reliable data:
- Use calibrated meters and sensors
- Account for phantom/standby power
- Measure at multiple points (whole home, circuits, devices)
- Validate readings against utility bills
- Maintain measurement history

### 2. Actionable Insights
Data without action is just noise:
- Identify specific savings opportunities
- Prioritize high-impact changes
- Provide clear cost-benefit analysis
- Make recommendations concrete and measurable
- Track impact of changes

### 3. Continuous Optimization
Energy management is ongoing:
- Monitor trends over time
- Adapt to seasonal changes
- Learn from usage patterns
- Adjust as household changes
- Celebrate savings achieved

### 4. User Engagement
Users must understand and care:
- Visualize consumption clearly
- Show real costs, not just kWh
- Gamify savings goals
- Provide timely feedback
- Make it easy to act

---

## Data Collection Patterns

### Device-Level Monitoring

**Smart Plug Measurement**:
```json
{
  "device_id": "tv-entertainment-center",
  "measurement": {
    "timestamp": "2025-10-21T10:30:00Z",
    "power_w": 245,
    "voltage_v": 120,
    "current_a": 2.04,
    "power_factor": 0.98,
    "energy_today_kwh": 1.24,
    "cost_today_usd": 0.15
  }
}
```

**Circuit-Level Monitoring**:
```json
{
  "circuit_id": "kitchen-circuit-1",
  "measurement": {
    "timestamp": "2025-10-21T10:30:00Z",
    "power_w": 1850,
    "devices_on_circuit": ["fridge", "microwave", "dishwasher", "outlets"],
    "peak_today_w": 3200,
    "energy_today_kwh": 8.4,
    "breaker_rating_a": 20
  }
}
```

**Whole-Home Monitoring**:
```json
{
  "home_id": "main-residence",
  "measurement": {
    "timestamp": "2025-10-21T10:30:00Z",
    "total_power_w": 3420,
    "net_power_w": 2850,
    "solar_generation_w": 570,
    "grid_import_w": 3420,
    "grid_export_w": 0,
    "energy_today_kwh": 42.3,
    "cost_today_usd": 5.08,
    "solar_today_kwh": 6.2
  }
}
```

### Sampling Strategies

**High-Frequency Sampling** (expensive, detailed):
- Sample every 1-5 seconds
- Capture transients and spikes
- Required for power quality analysis
- Large data volume
- Use for problem diagnosis

**Standard Sampling** (recommended):
- Sample every 1-5 minutes
- Balance accuracy and storage
- Sufficient for most analysis
- Manageable data volume
- Use for general monitoring

**Low-Frequency Sampling** (economical):
- Sample every 15-60 minutes
- Long-term trend analysis
- Minimal data storage
- May miss short events
- Use for historical archives

---

## Cost Calculation Strategies

### Flat Rate Pricing
```python
def calculate_flat_rate_cost(energy_kwh, rate_per_kwh=0.12):
    """Simple flat rate calculation"""
    return {
        "energy_kwh": energy_kwh,
        "rate": rate_per_kwh,
        "cost": energy_kwh * rate_per_kwh,
        "rate_type": "flat"
    }
```

### Time-of-Use (TOU) Pricing
```python
def calculate_tou_cost(energy_data, tou_rates):
    """
    Calculate cost with time-of-use rates

    tou_rates = {
        "peak": {"rate": 0.25, "hours": ["16:00-21:00"]},
        "off_peak": {"rate": 0.08, "hours": ["00:00-06:00"]},
        "shoulder": {"rate": 0.12, "hours": ["06:00-16:00", "21:00-24:00"]}
    }
    """
    from datetime import datetime

    total_cost = 0
    breakdown = {"peak": 0, "off_peak": 0, "shoulder": 0}

    for entry in energy_data:
        timestamp = datetime.fromisoformat(entry["timestamp"])
        hour = timestamp.hour
        minute = timestamp.minute
        energy = entry.get("energy_kwh", 0)

        # Determine rate tier
        tier = determine_tou_tier(hour, minute, tou_rates)
        rate = tou_rates[tier]["rate"]

        cost = energy * rate
        total_cost += cost
        breakdown[tier] += cost

    return {
        "total_cost": total_cost,
        "breakdown": breakdown,
        "rate_type": "time_of_use"
    }
```

### Tiered Pricing
```python
def calculate_tiered_cost(total_kwh, tier_rates):
    """
    Calculate cost with tiered rates

    tier_rates = [
        {"limit": 500, "rate": 0.10},
        {"limit": 1000, "rate": 0.15},
        {"limit": None, "rate": 0.20}
    ]
    """
    total_cost = 0
    remaining_kwh = total_kwh
    breakdown = []

    for tier in tier_rates:
        tier_limit = tier["limit"]
        tier_rate = tier["rate"]

        if tier_limit is None:
            # Last tier, unlimited
            tier_kwh = remaining_kwh
        else:
            tier_kwh = min(remaining_kwh, tier_limit)

        tier_cost = tier_kwh * tier_rate
        total_cost += tier_cost

        breakdown.append({
            "tier_kwh": tier_kwh,
            "tier_rate": tier_rate,
            "tier_cost": tier_cost
        })

        remaining_kwh -= tier_kwh
        if remaining_kwh <= 0:
            break

    return {
        "total_kwh": total_kwh,
        "total_cost": total_cost,
        "breakdown": breakdown,
        "rate_type": "tiered"
    }
```

### Demand Charges
```python
def calculate_demand_cost(peak_demand_kw, demand_rate=10.00, energy_cost=0.12, energy_kwh=1000):
    """
    Calculate cost with demand charges (common for commercial)

    Demand charge = peak kW × rate (e.g., $10/kW)
    Energy charge = kWh × rate
    """
    demand_cost = peak_demand_kw * demand_rate
    energy_cost_total = energy_kwh * energy_cost

    return {
        "demand_charge": demand_cost,
        "energy_charge": energy_cost_total,
        "total_cost": demand_cost + energy_cost_total,
        "peak_demand_kw": peak_demand_kw,
        "rate_type": "demand"
    }
```

---

## Usage Pattern Analysis

### Baseline Calculation
```python
def calculate_baseline(historical_data, method="median"):
    """Calculate baseline consumption for comparison"""
    import statistics

    daily_totals = aggregate_by_day(historical_data)

    if method == "median":
        baseline = statistics.median(daily_totals)
    elif method == "mean":
        baseline = statistics.mean(daily_totals)
    elif method == "percentile_25":
        baseline = statistics.quantiles(daily_totals, n=4)[0]
    else:
        baseline = statistics.mean(daily_totals)

    return {
        "baseline_kwh_per_day": baseline,
        "method": method,
        "sample_size": len(daily_totals)
    }
```

### Peak Hour Identification
```python
def identify_peak_hours(energy_data):
    """Identify hours with highest consumption"""
    from collections import defaultdict
    from datetime import datetime

    hourly_totals = defaultdict(float)
    hourly_counts = defaultdict(int)

    for entry in energy_data:
        timestamp = datetime.fromisoformat(entry["timestamp"])
        hour = timestamp.hour
        energy = entry.get("energy_kwh", 0)

        hourly_totals[hour] += energy
        hourly_counts[hour] += 1

    # Calculate average per hour
    hourly_averages = {
        hour: hourly_totals[hour] / hourly_counts[hour]
        for hour in hourly_totals
    }

    # Sort by consumption
    sorted_hours = sorted(
        hourly_averages.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return {
        "peak_hours": sorted_hours[:3],
        "valley_hours": sorted_hours[-3:],
        "hourly_distribution": hourly_averages
    }
```

### Weekday vs Weekend Analysis
```python
def analyze_weekday_weekend(energy_data):
    """Compare weekday vs weekend consumption"""
    from datetime import datetime

    weekday_total = 0
    weekday_count = 0
    weekend_total = 0
    weekend_count = 0

    for entry in energy_data:
        timestamp = datetime.fromisoformat(entry["timestamp"])
        energy = entry.get("energy_kwh", 0)

        if timestamp.weekday() < 5:  # Monday-Friday
            weekday_total += energy
            weekday_count += 1
        else:  # Saturday-Sunday
            weekend_total += energy
            weekend_count += 1

    weekday_avg = weekday_total / weekday_count if weekday_count > 0 else 0
    weekend_avg = weekend_total / weekend_count if weekend_count > 0 else 0

    return {
        "weekday_avg_kwh": weekday_avg,
        "weekend_avg_kwh": weekend_avg,
        "difference_kwh": abs(weekday_avg - weekend_avg),
        "difference_percent": ((weekend_avg - weekday_avg) / weekday_avg * 100) if weekday_avg > 0 else 0
    }
```

### Seasonal Patterns
```python
def analyze_seasonal_patterns(energy_data):
    """Identify seasonal consumption patterns"""
    from datetime import datetime
    from collections import defaultdict

    seasonal_totals = defaultdict(float)
    seasonal_counts = defaultdict(int)

    season_map = {
        12: "winter", 1: "winter", 2: "winter",
        3: "spring", 4: "spring", 5: "spring",
        6: "summer", 7: "summer", 8: "summer",
        9: "fall", 10: "fall", 11: "fall"
    }

    for entry in energy_data:
        timestamp = datetime.fromisoformat(entry["timestamp"])
        season = season_map[timestamp.month]
        energy = entry.get("energy_kwh", 0)

        seasonal_totals[season] += energy
        seasonal_counts[season] += 1

    seasonal_averages = {
        season: seasonal_totals[season] / seasonal_counts[season]
        for season in seasonal_totals
    }

    return {
        "seasonal_averages": seasonal_averages,
        "highest_season": max(seasonal_averages, key=seasonal_averages.get),
        "lowest_season": min(seasonal_averages, key=seasonal_averages.get)
    }
```

---

## Anomaly Detection Strategies

### Statistical Anomaly Detection
```python
def detect_statistical_anomalies(device_id, current_value, historical_data, threshold_std=2):
    """Detect anomalies using statistical methods"""
    import statistics

    # Get historical values for this device
    device_history = [
        entry.get("power_w", 0)
        for entry in historical_data
        if entry["device_id"] == device_id
    ]

    if len(device_history) < 10:
        return {"anomaly": False, "reason": "Insufficient data"}

    mean = statistics.mean(device_history)
    stdev = statistics.stdev(device_history)

    # Calculate z-score
    z_score = abs((current_value - mean) / stdev) if stdev > 0 else 0

    is_anomaly = z_score > threshold_std

    return {
        "anomaly": is_anomaly,
        "z_score": z_score,
        "current_value": current_value,
        "historical_mean": mean,
        "historical_stdev": stdev,
        "severity": "critical" if z_score > 3 else "high" if z_score > 2 else "normal"
    }
```

### Unusual Consumption Patterns
```python
def detect_unusual_patterns(energy_data):
    """Detect unusual consumption patterns"""
    anomalies = []

    # 1. Always-on devices with high power
    always_on_threshold = 20  # hours per day
    high_power_threshold = 100  # watts

    device_runtime = calculate_device_runtime(energy_data)
    for device_id, runtime_hours in device_runtime.items():
        if runtime_hours > always_on_threshold:
            avg_power = get_average_power(device_id, energy_data)
            if avg_power > high_power_threshold:
                anomalies.append({
                    "type": "vampire_power",
                    "device_id": device_id,
                    "runtime_hours": runtime_hours,
                    "avg_power_w": avg_power,
                    "estimated_waste_kwh_month": (avg_power * 24 * 30) / 1000,
                    "severity": "medium"
                })

    # 2. Unexpected usage during typical sleep hours
    for entry in energy_data:
        from datetime import datetime
        timestamp = datetime.fromisoformat(entry["timestamp"])
        hour = timestamp.hour

        if 2 <= hour <= 5:  # Deep night hours
            power = entry.get("power_w", 0)
            if power > 500:  # High power during night
                anomalies.append({
                    "type": "night_usage",
                    "timestamp": entry["timestamp"],
                    "device_id": entry["device_id"],
                    "power_w": power,
                    "severity": "low"
                })

    # 3. Sudden consumption spikes
    for i in range(1, len(energy_data)):
        prev = energy_data[i-1].get("power_w", 0)
        current = energy_data[i].get("power_w", 0)

        if current > prev * 3 and current > 1000:  # 3x increase and >1kW
            anomalies.append({
                "type": "consumption_spike",
                "timestamp": energy_data[i]["timestamp"],
                "device_id": energy_data[i]["device_id"],
                "previous_w": prev,
                "current_w": current,
                "increase_percent": ((current - prev) / prev * 100) if prev > 0 else 0,
                "severity": "high"
            })

    return anomalies
```

### Device Offline Detection
```python
def detect_offline_devices(device_registry, energy_data, threshold_hours=24):
    """Detect devices that should be reporting but aren't"""
    from datetime import datetime, timedelta

    now = datetime.now()
    threshold = timedelta(hours=threshold_hours)

    # Get last report time for each device
    last_seen = {}
    for entry in energy_data:
        device_id = entry["device_id"]
        timestamp = datetime.fromisoformat(entry["timestamp"])

        if device_id not in last_seen or timestamp > last_seen[device_id]:
            last_seen[device_id] = timestamp

    offline_devices = []

    # Check all monitored devices
    for device in device_registry.get("devices", []):
        device_id = device["device_id"]

        # Skip devices not expected to report energy
        if not device.get("energy_monitoring_enabled", False):
            continue

        if device_id not in last_seen:
            offline_devices.append({
                "device_id": device_id,
                "device_name": device["name"],
                "status": "never_reported",
                "severity": "low"
            })
        elif (now - last_seen[device_id]) > threshold:
            hours_offline = (now - last_seen[device_id]).total_seconds() / 3600
            offline_devices.append({
                "device_id": device_id,
                "device_name": device["name"],
                "status": "offline",
                "last_seen": last_seen[device_id].isoformat(),
                "hours_offline": hours_offline,
                "severity": "critical" if hours_offline > 72 else "high"
            })

    return offline_devices
```

---

## Optimization Strategies

### Load Shifting Recommendations
```python
def recommend_load_shifting(energy_data, tou_rates):
    """Recommend shifting loads to off-peak hours"""
    recommendations = []

    # Identify high-consumption devices during peak hours
    peak_hours = get_tou_hours(tou_rates, "peak")

    for device_id in get_unique_devices(energy_data):
        peak_usage = get_usage_during_hours(device_id, energy_data, peak_hours)

        if peak_usage > 1.0:  # More than 1 kWh during peak
            peak_rate = tou_rates["peak"]["rate"]
            off_peak_rate = tou_rates["off_peak"]["rate"]

            potential_savings = peak_usage * (peak_rate - off_peak_rate)

            recommendations.append({
                "device_id": device_id,
                "current_peak_usage_kwh": peak_usage,
                "potential_monthly_savings": potential_savings * 30,
                "recommendation": f"Shift {device_id} usage to off-peak hours ({tou_rates['off_peak']['hours']})",
                "priority": "high" if potential_savings * 30 > 10 else "medium"
            })

    return sorted(recommendations, key=lambda x: x["potential_monthly_savings"], reverse=True)
```

### Standby Power Elimination
```python
def identify_standby_power_waste(energy_data):
    """Identify devices wasting power on standby"""
    recommendations = []

    for device_id in get_unique_devices(energy_data):
        # Get power consumption when device should be "off"
        off_state_power = get_off_state_power(device_id, energy_data)

        if off_state_power > 5:  # More than 5W standby
            daily_waste_kwh = (off_state_power * 24) / 1000
            monthly_cost = daily_waste_kwh * 30 * 0.12  # Assume $0.12/kWh

            recommendations.append({
                "device_id": device_id,
                "standby_power_w": off_state_power,
                "daily_waste_kwh": daily_waste_kwh,
                "monthly_waste_cost": monthly_cost,
                "annual_waste_cost": monthly_cost * 12,
                "recommendation": "Use smart plug or power strip to eliminate standby power",
                "priority": "high" if monthly_cost > 2 else "medium"
            })

    return recommendations
```

### HVAC Optimization
```python
def optimize_hvac_schedule(energy_data, occupancy_data, weather_data):
    """Optimize HVAC schedule based on occupancy and weather"""
    recommendations = []

    # Identify HVAC devices
    hvac_devices = get_devices_by_type(energy_data, "hvac")

    for device_id in hvac_devices:
        # Check for heating/cooling when nobody home
        unoccupied_runtime = 0
        for entry in energy_data:
            if entry["device_id"] != device_id:
                continue

            timestamp = entry["timestamp"]
            if not is_occupied(timestamp, occupancy_data):
                unoccupied_runtime += entry.get("duration_minutes", 0)

        if unoccupied_runtime > 60:  # More than 1 hour per day
            daily_waste_kwh = (unoccupied_runtime / 60) * 2  # Assume 2 kW HVAC
            monthly_savings = daily_waste_kwh * 30 * 0.12

            recommendations.append({
                "device_id": device_id,
                "unoccupied_runtime_minutes": unoccupied_runtime,
                "potential_monthly_savings": monthly_savings,
                "recommendation": "Use occupancy-based or geofencing automation to reduce HVAC runtime when unoccupied",
                "priority": "high"
            })

        # Check for poor temperature setpoints
        avg_temp_setpoint = get_average_setpoint(device_id, energy_data)
        outdoor_avg = get_average_outdoor_temp(weather_data)

        # Summer cooling recommendation
        if outdoor_avg > 75 and avg_temp_setpoint < 72:
            savings_per_degree = 0.03  # 3% savings per degree
            degrees_to_raise = 72 - avg_temp_setpoint
            current_cost = get_monthly_cost(device_id, energy_data)
            potential_savings = current_cost * (degrees_to_raise * savings_per_degree)

            recommendations.append({
                "device_id": device_id,
                "recommendation": f"Raise cooling setpoint from {avg_temp_setpoint}°F to 72°F or higher",
                "potential_monthly_savings": potential_savings,
                "priority": "medium"
            })

    return recommendations
```

### Energy-Efficient Device Recommendations
```python
def recommend_device_upgrades(energy_data, device_registry):
    """Recommend upgrading inefficient devices"""
    recommendations = []

    # Database of typical consumption for efficient vs inefficient devices
    efficiency_benchmarks = {
        "refrigerator": {"efficient": 40, "inefficient": 150},
        "hvac": {"efficient": 1500, "inefficient": 3000},
        "light": {"efficient": 10, "inefficient": 60},
        "washer": {"efficient": 200, "inefficient": 500}
    }

    for device in device_registry.get("devices", []):
        device_id = device["device_id"]
        device_type = device.get("type")

        if device_type not in efficiency_benchmarks:
            continue

        avg_power = get_average_power(device_id, energy_data)
        efficient_power = efficiency_benchmarks[device_type]["efficient"]
        inefficient_threshold = efficiency_benchmarks[device_type]["inefficient"]

        if avg_power > inefficient_threshold:
            # Calculate savings from upgrade
            hours_per_day = get_runtime_hours(device_id, energy_data) / 30
            current_monthly_kwh = (avg_power * hours_per_day * 30) / 1000
            efficient_monthly_kwh = (efficient_power * hours_per_day * 30) / 1000

            monthly_savings_kwh = current_monthly_kwh - efficient_monthly_kwh
            monthly_savings_cost = monthly_savings_kwh * 0.12
            annual_savings = monthly_savings_cost * 12

            # Estimate payback period (rough)
            upgrade_cost = get_typical_upgrade_cost(device_type)
            payback_years = upgrade_cost / annual_savings if annual_savings > 0 else 999

            recommendations.append({
                "device_id": device_id,
                "device_type": device_type,
                "current_avg_power_w": avg_power,
                "efficient_power_w": efficient_power,
                "monthly_savings": monthly_savings_cost,
                "annual_savings": annual_savings,
                "upgrade_cost": upgrade_cost,
                "payback_years": payback_years,
                "recommendation": f"Upgrade {device_type} to Energy Star certified model",
                "priority": "high" if payback_years < 3 else "medium" if payback_years < 5 else "low"
            })

    return sorted(recommendations, key=lambda x: x["annual_savings"], reverse=True)
```

---

## Reporting & Visualization

### Daily Summary Report
```json
{
  "report_type": "daily_summary",
  "date": "2025-10-21",
  "summary": {
    "total_kwh": 42.3,
    "total_cost": 5.08,
    "vs_baseline": {
      "kwh_difference": -3.2,
      "percent_change": -7.0,
      "trend": "below_baseline"
    },
    "peak_hour": 18,
    "peak_power_w": 4250
  },
  "top_consumers": [
    {"device": "HVAC", "kwh": 18.2, "cost": 2.18, "percent": 43},
    {"device": "Water Heater", "kwh": 8.4, "cost": 1.01, "percent": 20},
    {"device": "Refrigerator", "kwh": 2.8, "cost": 0.34, "percent": 7}
  ],
  "anomalies": [
    {
      "type": "unusual_consumption",
      "device": "Garage Heater",
      "severity": "medium",
      "message": "2x normal usage"
    }
  ],
  "recommendations": [
    {
      "title": "Shift dishwasher to off-peak",
      "savings": "$0.15/day",
      "priority": "high"
    }
  ]
}
```

### Monthly Summary Report
```json
{
  "report_type": "monthly_summary",
  "month": "2025-10",
  "summary": {
    "total_kwh": 1247,
    "total_cost": 149.64,
    "avg_daily_kwh": 40.2,
    "vs_previous_month": {
      "kwh_change": -85,
      "percent_change": -6.4,
      "cost_change": -10.20
    }
  },
  "breakdown": {
    "heating_cooling": {"kwh": 548, "cost": 65.76, "percent": 44},
    "water_heating": {"kwh": 249, "cost": 29.88, "percent": 20},
    "appliances": {"kwh": 312, "cost": 37.44, "percent": 25},
    "lighting": {"kwh": 87, "cost": 10.44, "percent": 7},
    "other": {"kwh": 51, "cost": 6.12, "percent": 4}
  },
  "cost_by_tier": {
    "peak": 45.20,
    "shoulder": 68.40,
    "off_peak": 36.04
  },
  "achievements": [
    "7% reduction vs. last month",
    "Stayed under 1300 kWh target",
    "Shifted 15% of usage to off-peak"
  ],
  "opportunities": [
    {
      "title": "HVAC optimization",
      "potential_savings": "$12/month"
    },
    {
      "title": "Eliminate standby power",
      "potential_savings": "$8/month"
    }
  ]
}
```

---

## Best Practices Summary

### Monitoring
1. **Measure at multiple levels** (whole home, circuits, devices)
2. **Validate against utility bills** monthly
3. **Maintain consistent sampling** intervals
4. **Store sufficient history** (minimum 12 months)
5. **Document measurement points** and calibrations

### Analysis
1. **Establish baselines** before comparing
2. **Account for external factors** (weather, occupancy, etc.)
3. **Use statistical methods** for anomaly detection
4. **Identify root causes** not just symptoms
5. **Segment by time periods** (weekday/weekend, seasonal)

### Optimization
1. **Prioritize high-impact changes** (Pareto principle)
2. **Calculate payback periods** for upgrades
3. **Measure impact** of changes
4. **Start with behavioral changes** (free savings)
5. **Then automate** proven strategies

### Reporting
1. **Show costs, not just kWh** (more relatable)
2. **Visualize trends** clearly
3. **Provide actionable recommendations** (specific, measurable)
4. **Celebrate achievements** (gamification)
5. **Make it regular** (daily/weekly/monthly cadence)

---

## Summary

Effective energy management requires:

1. **Accurate Data**: Reliable measurements at appropriate granularity
2. **Smart Analysis**: Statistical methods to identify patterns and anomalies
3. **Clear Insights**: Cost-focused reporting that shows impact
4. **Actionable Recommendations**: Specific, prioritized optimization opportunities
5. **Continuous Improvement**: Regular monitoring and adjustment

Follow these patterns to help users understand their energy consumption, identify waste, and implement optimizations that deliver real, measurable savings.
