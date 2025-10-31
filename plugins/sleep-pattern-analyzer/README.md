# Sleep Pattern Analyzer Plugin

> Sleep quality analysis and optimization specialist - Sleep tracking, pattern recognition, quality insights, and optimization recommendations

## Overview

The Sleep Pattern Analyzer plugin helps you understand and optimize your sleep patterns through systematic tracking, intelligent analysis, and personalized recommendations. Track sleep quality, identify what affects your sleep, and receive actionable insights for better rest.

## Features

### Agents

- **sleep-logger** (Haiku): Log daily sleep data and calculate metrics
- **pattern-analyzer** (Sonnet): Analyze sleep patterns and find correlations
- **quality-scorer**: Score sleep quality based on multiple factors
- **recommendation-engine**: Generate personalized sleep optimization tips
- **wearable-integrator**: Import data from fitness trackers

### Skills

- **sleep-tracking**: Sleep logging patterns, metric calculations, quality scoring
- **pattern-analysis**: Trend analysis, correlation detection, visualization patterns

## Quick Start

### Installation

```bash
/plugin install sleep-pattern-analyzer@puerto
```

### Basic Usage

**Log last night's sleep:**
```bash
@sleep-logger log --bedtime "23:00" --wake "07:00" --quality 4
```

**Analyze sleep patterns:**
```bash
@pattern-analyzer analyze --period "30days"
```

**Get recommendations:**
```bash
@recommendation-engine suggest-improvements
```

## Sleep Tracking

### Daily Sleep Log

Track these key metrics:

**Core Metrics**:
- Bedtime (when you got in bed)
- Wake time (when you woke up)
- Sleep quality (1-5 scale)
- Sleep disruptions (number and reasons)

**Optional Metrics**:
- Sleep latency (time to fall asleep)
- Time in bed vs actual sleep time
- Sleep efficiency percentage
- Morning energy level (1-5)

**Lifestyle Factors**:
- Exercise (yes/no, time of day)
- Caffeine (yes/no, latest time)
- Alcohol (yes/no, amount)
- Stress level (1-5)
- Screen time before bed (minutes)
- Naps (duration)

### Sleep Quality Scale

**5 - Excellent**:
- Fell asleep quickly (< 15 min)
- Slept through night
- Woke feeling refreshed
- High energy all day

**4 - Good**:
- Minor disruptions (1-2)
- Felt rested
- Good energy most of day

**3 - Fair**:
- Several disruptions or long sleep latency
- Moderate grogginess in morning
- Adequate energy, needed caffeine

**2 - Poor**:
- Significant sleep problems
- Groggy most of morning
- Low energy, struggled through day

**1 - Very Poor**:
- Insomnia or multiple wake-ups
- Exhausted all day
- Impaired function

## Sleep Metrics

### Sleep Duration

**Recommended**: 7-9 hours for adults

```python
# Automatic calculation
sleep_duration = wake_time - bedtime
# Handles crossing midnight
```

### Sleep Efficiency

```
Sleep Efficiency = (Actual Sleep Time / Time in Bed) × 100

85-100%: Excellent
75-84%: Good
65-74%: Fair
< 65%: Poor
```

### Sleep Debt

```
Sleep Debt = Σ (Target Hours - Actual Hours)

< 5 hours: Manageable
5-10 hours: Concerning
> 10 hours: Significant impact
```

### Consistency Score

```
Consistency = 100 - (Std Dev of Bedtime × 10)

90-100: Very consistent
70-89: Moderately consistent
< 70: Inconsistent
```

## Pattern Analysis

### What Gets Analyzed

**Trends Over Time**:
- Average sleep duration (weekly, monthly)
- Quality trends (improving, stable, declining)
- Sleep efficiency changes
- Sleep debt accumulation

**Correlations**:
- Exercise → Sleep quality
- Caffeine timing → Sleep quality
- Screen time → Sleep latency
- Stress level → Sleep disruptions
- Alcohol → Sleep efficiency

**Patterns**:
- Weekday vs weekend sleep
- Chronotype identification (early bird vs night owl)
- Sleep debt cycles
- Best/worst sleep days

### Sample Analysis Report

```
Sleep Analysis: Last 30 Days

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SLEEP METRICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Average Sleep: 7.2 hrs (Target: 8.0)
Average Quality: 3.4/5
Sleep Efficiency: 92.3%
Sleep Debt: 24 hours
Consistency: 78% (moderate)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KEY INSIGHTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Exercise Impact: +25% better quality
  Days with exercise: 4.1/5
  Days without: 3.1/5

✗ Late Caffeine: -18% worse quality
  No caffeine after 2pm: 3.8/5
  Caffeine after 2pm: 2.9/5

✓ Bedtime Consistency: Good
  Std deviation: 42 minutes

⚠ Sleep Debt: Accumulating
  Losing 48 min/day average
  Catching up on weekends (+2.1 hrs)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PATTERNS DETECTED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Weekend Catch-Up Sleep
   Sleeping 2.1 hrs more on weekends
   → Indicates weekday sleep insufficiency

2. Exercise-Sleep Connection
   100% of your best sleep nights (4-5 rating)
   occurred on days you exercised

3. Caffeine Sensitivity
   No caffeine after 2pm → 95% good sleep
   Caffeine after 2pm → 45% good sleep

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOP RECOMMENDATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Target 10:30pm bedtime (recover sleep debt)
2. Continue daily exercise (huge positive impact)
3. Hard cutoff: No caffeine after 2pm
4. Reduce weekend variability (maintain schedule)
```

## Use Cases

### Example 1: Identify Sleep Disruptors

```bash
# After 2 weeks of logging
@pattern-analyzer correlations

# Discovers:
"Caffeine after 3pm reduces sleep quality by 23%"
"Exercise before 8pm improves sleep quality by 31%"
"Screen time > 30min before bed increases sleep latency by 18min"

# Actionable insights for behavior change
```

### Example 2: Optimize Bedtime

```bash
@pattern-analyzer recommend-bedtime

# Analysis:
Based on your data:
- You naturally wake around 6:45am
- You need ~8 hours for optimal function
- You typically take 20 minutes to fall asleep

Recommended bedtime: 10:30pm
- Lights out: 10:30pm
- Expected sleep: 10:50pm-6:45am (7h 55min)
- Buffer for sleep latency included
```

### Example 3: Track Recovery from Sleep Debt

```bash
@pattern-analyzer sleep-debt --trend

# Week 1: 12 hours debt
# Week 2: 9 hours debt (improving)
# Week 3: 6 hours debt (improving)
# Week 4: 4 hours debt (nearly recovered)

Status: On track to full recovery
Continue current sleep schedule
```

## Wearable Integration

### Supported Devices

- **Fitbit**: Import sleep stages, heart rate
- **Apple Watch**: Import sleep data, resting heart rate
- **Oura Ring**: Import sleep scores, readiness
- **Garmin**: Import sleep stages, body battery
- **Whoop**: Import sleep performance, recovery

### Import Sleep Data

```bash
# Export from wearable app (usually CSV or JSON)
@wearable-integrator import \
    --device "fitbit" \
    --file "fitbit-sleep-export.csv" \
    --date-range "2025-01-01:2025-01-31"

# Data automatically merged with manual logs
```

### Enhanced Metrics from Wearables

- **Sleep stages**: Deep, light, REM percentages
- **Heart rate variability**: Recovery indicator
- **Resting heart rate**: Health/stress indicator
- **Movement**: Sleep disturbance measurement
- **Sleep score**: Device-specific scoring

## Sleep Optimization Tips

### Foundation (Sleep Hygiene)

1. **Consistent schedule**: Same bedtime/wake time (± 30 min)
2. **Dark environment**: Blackout curtains or eye mask
3. **Cool temperature**: 60-67°F (15-19°C) optimal
4. **Quiet or white noise**: Block disruptive sounds
5. **Comfortable mattress**: Replace every 7-10 years

### Lifestyle Factors

**Exercise**:
- ✓ Regular exercise improves sleep
- ✗ Avoid intense exercise < 3 hours before bed
- ✓ Morning exercise = best for sleep

**Caffeine**:
- Half-life: 5-6 hours
- Cutoff: 6-8 hours before bedtime
- Individual sensitivity varies

**Alcohol**:
- ✗ Reduces REM sleep
- ✗ Increases sleep disruptions
- ✗ Avoid within 3 hours of bedtime

**Screen Time**:
- Blue light suppresses melatonin
- Use night mode after sunset
- Stop screens 30-60 min before bed
- Reading > scrolling

**Stress**:
- Evening wind-down routine
- Meditation or breathing exercises
- Worry journal (write worries down)
- Reserve bed for sleep only

### Pre-Bed Routine

**90 minutes before bed**:
- Dim lights (signals melatonin production)
- Stop caffeine/alcohol
- Light snack if hungry (not heavy meal)

**30 minutes before bed**:
- Put away screens
- Relaxing activity (reading, stretching)
- Prepare for next day (reduce morning anxiety)
- Cool down bedroom

**Bedtime**:
- Same time every night (± 30 min)
- 10-15 min to fall asleep is normal
- If not asleep in 20 min, get up and read

## Troubleshooting

**Issue**: Trouble falling asleep

**Analysis**:
```bash
@pattern-analyzer analyze-latency

# Checks:
- Average time to fall asleep
- Correlation with daytime factors
- Bedtime consistency
- Pre-bed routine

# Recommendations based on your data
```

**Issue**: Waking up during night

**Analysis**:
```bash
@pattern-analyzer analyze-disruptions

# Identifies patterns:
- Typical wake times (bladder, temperature)
- External factors (noise, light, pet)
- Internal factors (stress, pain)
- Sleep environment issues
```

**Issue**: Tired despite adequate hours

**Analysis**:
```bash
@pattern-analyzer analyze-quality

# Investigates:
- Sleep efficiency (time asleep vs time in bed)
- Sleep debt accumulation
- Lifestyle factors affecting quality
- Potential sleep disorders (recommend doctor visit)
```

## Data Privacy

- **All data stored locally** on your device
- **No cloud sync** unless you explicitly configure it
- **No data sharing** with any external services
- **Export available** for your own analysis

## Best Practices

### Tracking Habits

1. **Log every morning**: Make it a habit (like brushing teeth)
2. **Be honest**: Accurate data = useful insights
3. **Track consistently**: Need 2 weeks minimum, 30 days better
4. **Note factors**: Capture what might affect sleep
5. **Review weekly**: Check patterns and adjust

### Using Insights

1. **Focus on patterns**: Don't obsess over single nights
2. **Test changes one at a time**: Can't learn from multiple changes
3. **Give changes time**: 1-2 weeks to see impact
4. **Trust your body**: Data supplements, doesn't replace, how you feel
5. **Seek professional help**: If persistent issues (insomnia, apnea)

## When to See a Doctor

**Consider sleep specialist if you experience**:
- Chronic insomnia (> 3 nights/week for > 3 months)
- Loud snoring or breathing pauses (sleep apnea)
- Excessive daytime sleepiness despite adequate sleep
- Unusual sleep behaviors (sleepwalking, etc.)
- Persistent nightmares or night terrors
- Restless legs syndrome

## Integration

### With Habit Trackers

```bash
# Link sleep quality to daily habits
@pattern-analyzer correlate --habits "exercise,meditation,diet"
```

### With Productivity Tools

```bash
# Analyze sleep impact on productivity
@pattern-analyzer productivity-correlation --metrics "focus,energy,mood"
```

## Data Storage

```
data/
├── sleep-logs/          # Daily sleep entries
├── analyses/            # Generated analysis reports
├── wearable-imports/    # Imported device data
└── patterns/            # Detected patterns and trends
```

## License

MIT

## Support

For issues and questions:
- GitHub Issues: https://github.com/bandofai/puerto/issues

---

**Remember**: Sleep is a skill that can be optimized. Track consistently, identify what works for you, and prioritize sleep as essential to health and performance.
