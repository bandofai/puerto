# Recovery Management Skill

Recovery optimization and injury prevention strategies for sustainable training progress.

## Recovery Principles

### Training Stress and Adaptation

```
Training Stimulus → Fatigue → Recovery → Adaptation → Stronger

If recovery insufficient: Fatigue accumulates → Performance decline → Injury risk
```

**Key Concept**: Gains happen during recovery, not during training. Training provides the stimulus; recovery provides the adaptation.

## Overtraining Detection

### Warning Signs

**Physical Indicators**:
- Persistent muscle soreness (>72 hours)
- Decreased performance despite rest
- Elevated resting heart rate (+10 bpm or more)
- Sleep disturbances
- Frequent minor illnesses
- Loss of appetite
- Excessive fatigue

**Performance Indicators**:
- Weights decreasing despite effort
- Inability to complete usual volume
- Longer recovery between sets needed
- Form degradation
- Lack of "pump" during workout

**Psychological Indicators**:
- Loss of motivation to train
- Irritability
- Depression or mood swings
- Difficulty concentrating
- Dreading workouts (vs. looking forward)

### Overtraining Detection Rules

**Volume Spike Detection**:
```python
def check_volume_spike(current_week_volume, previous_week_volume):
    increase = (current_week_volume - previous_week_volume) / previous_week_volume * 100

    if increase > 35:
        return {
            "severity": "severe",
            "action": "Reduce volume by 30-40% immediately",
            "message": f"Volume increased {increase:.1f}% (severe spike)"
        }
    elif increase > 20:
        return {
            "severity": "warning",
            "action": "Reduce volume by 20% next session",
            "message": f"Volume increased {increase:.1f}% (moderate spike)"
        }
    elif increase > 10:
        return {
            "severity": "monitor",
            "action": "Maintain current volume, don't increase further",
            "message": f"Volume increased {increase:.1f}% (healthy progression)"
        }

    return {"severity": "healthy"}
```

**Frequency Detection**:
```python
def check_training_frequency(workouts_last_7_days, consecutive_days):
    if consecutive_days >= 9:
        return {
            "severity": "severe",
            "action": "Take 2 rest days immediately",
            "message": f"{consecutive_days} consecutive training days"
        }
    elif consecutive_days >= 7:
        return {
            "severity": "warning",
            "action": "Take 1 rest day immediately",
            "message": f"{consecutive_days} consecutive training days"
        }

    if workouts_last_7_days > 6:
        return {
            "severity": "monitor",
            "action": "Ensure at least 1 rest day per week",
            "message": f"{workouts_last_7_days} workouts in 7 days"
        }

    return {"severity": "healthy"}
```

## Muscle Group Recovery

### Recovery Time Requirements

```json
{
  "muscle_groups": {
    "chest": {
      "minimum_rest_hours": 48,
      "optimal_rest_hours": 72,
      "frequency_per_week": 2
    },
    "back": {
      "minimum_rest_hours": 48,
      "optimal_rest_hours": 72,
      "frequency_per_week": 2
    },
    "legs": {
      "minimum_rest_hours": 72,
      "optimal_rest_hours": 96,
      "frequency_per_week": 2,
      "note": "Largest muscle group, needs more recovery"
    },
    "shoulders": {
      "minimum_rest_hours": 48,
      "optimal_rest_hours": 72,
      "frequency_per_week": 2
    },
    "arms": {
      "minimum_rest_hours": 24,
      "optimal_rest_hours": 48,
      "frequency_per_week": 2,
      "note": "Smaller muscles, recover faster"
    }
  }
}
```

### Recovery Status Calculation

```python
from datetime import datetime, timedelta

def calculate_recovery_status(muscle_group, last_trained_timestamp):
    now = datetime.now()
    hours_since = (now - last_trained_timestamp).total_seconds() / 3600

    recovery_times = {
        "chest": {"minimum": 48, "optimal": 72},
        "back": {"minimum": 48, "optimal": 72},
        "legs": {"minimum": 72, "optimal": 96},
        "shoulders": {"minimum": 48, "optimal": 72},
        "arms": {"minimum": 24, "optimal": 48}
    }

    times = recovery_times.get(muscle_group, {"minimum": 48, "optimal": 72})

    if hours_since < times["minimum"]:
        return {
            "status": "recovering",
            "emoji": "🔴",
            "ready_to_train": False,
            "hours_remaining": times["minimum"] - hours_since,
            "recommendation": f"Wait {int(times['minimum'] - hours_since)} more hours"
        }
    elif hours_since < times["optimal"]:
        return {
            "status": "minimally_recovered",
            "emoji": "🟡",
            "ready_to_train": True,
            "note": "Can train, but not optimal",
            "recommendation": "Light session OK, avoid PR attempts"
        }
    else:
        return {
            "status": "fully_recovered",
            "emoji": "🟢",
            "ready_to_train": True,
            "recommendation": "Ready for normal training"
        }
```

## Deload Protocols

### When to Deload

**Time-Based**:
- Every 4-6 weeks of hard training
- After completing training program/phase
- Before competition or testing maxes

**Symptom-Based**:
- Persistent fatigue despite adequate sleep
- Performance plateau or decline
- Elevated resting heart rate
- Loss of motivation
- Accumulated minor aches/pains

### Deload Week Structure

**Volume Deload** (Recommended):
```
Reduce total sets by 40-50%
Maintain same weights (intensity)
Maintain same rep ranges

Example:
Normal: Bench Press 4x8 @ 185 lbs
Deload: Bench Press 2x8 @ 185 lbs (50% volume reduction)
```

**Intensity Deload** (Alternative):
```
Maintain same volume (sets × reps)
Reduce weight by 20-30%

Example:
Normal: Squat 4x5 @ 275 lbs
Deload: Squat 4x5 @ 220 lbs (20% intensity reduction)
```

**Hybrid Deload**:
```
Reduce both volume and intensity moderately

Example:
Normal: Deadlift 5x5 @ 315 lbs
Deload: Deadlift 3x5 @ 275 lbs (40% volume, 13% intensity reduction)
```

### Deload Week Goals

- Reduce systemic fatigue
- Allow joints and connective tissue to recover
- Practice technique with lighter loads
- Maintain movement patterns
- Return feeling refreshed and strong

**NOT a Deload**:
- Complete rest week (maintain some training stimulus)
- Test maxes (save for after deload)
- Try new exercises (stick to familiar movements)

## Periodization for Recovery

### Linear Periodization Example

```
Week 1: 4x8 @ 185 lbs (base volume)
Week 2: 4x8 @ 190 lbs (progress)
Week 3: 4x8 @ 195 lbs (progress)
Week 4: 2x8 @ 185 lbs (deload)
Week 5: 4x8 @ 200 lbs (return stronger)
```

### Undulating Periodization Example

```
Monday (Heavy):    5x5 @ 225 lbs
Wednesday (Light): 3x10 @ 165 lbs
Friday (Medium):   4x8 @ 195 lbs

Built-in recovery variation within week
```

## Sleep and Recovery

### Sleep Requirements

```json
{
  "recommendations": {
    "general_population": "7-9 hours",
    "athletes": "8-10 hours",
    "hard_training_phase": "9+ hours"
  },
  "sleep_quality_factors": [
    "Consistent sleep schedule",
    "Dark, cool room (65-68°F)",
    "Avoid screens 1 hour before bed",
    "Avoid caffeine 6+ hours before bed",
    "Avoid large meals 2-3 hours before bed"
  ],
  "impact_on_performance": {
    "adequate_sleep": "Optimal recovery, strength gains, muscle growth",
    "sleep_deprived": "Reduced performance, increased injury risk, impaired recovery"
  }
}
```

### Sleep Tracking

If user provides sleep data:
```python
def analyze_sleep_impact(workout_data, sleep_data):
    for workout in workout_data:
        sleep_previous_night = get_sleep(workout.date - 1)

        if sleep_previous_night < 6:
            workout["sleep_impact"] = "poor"
            workout["performance_note"] = "Low sleep may affect performance"
        elif sleep_previous_night < 7:
            workout["sleep_impact"] = "suboptimal"
        else:
            workout["sleep_impact"] = "adequate"

    # Correlate sleep with performance trends
    return analyze_correlation(sleep_hours, workout_performance)
```

## Nutrition for Recovery

### Protein Requirements

```
General: 0.8-1.0g per lb body weight daily
Hard training: 1.0-1.2g per lb body weight daily
Cutting (fat loss): 1.2-1.5g per lb body weight daily

Example (180 lb person):
Minimum: 144g protein/day
Optimal: 180g protein/day
```

**Timing**:
- Post-workout: 20-40g protein within 2 hours
- Distribute throughout day: 4-5 meals with 30-40g protein each

### Hydration

```
Baseline: 0.5-1 oz per lb body weight daily
Training day: Add 16-32 oz per hour of exercise

Example (180 lb person):
Baseline: 90-180 oz (2.7-5.3 liters)
With 1 hour workout: 106-212 oz
```

**Signs of Dehydration**:
- Dark yellow urine
- Decreased performance
- Increased perceived exertion
- Muscle cramps
- Headache

## Active Recovery

### Active Recovery Activities

**Light Intensity** (60-70% max heart rate):
- Walking (20-30 minutes)
- Light cycling
- Swimming (easy pace)
- Yoga or stretching
- Foam rolling

**Benefits**:
- Increased blood flow to muscles
- Reduced muscle soreness (DOMS)
- Maintains movement patterns
- Psychological benefits (staying active)

**NOT Active Recovery**:
- HIIT workouts
- Long distance running
- Additional strength training
- Sports/competitive activities

### Foam Rolling Protocol

```
Target: Sore or tight muscles
Duration: 30-60 seconds per muscle group
Pressure: Uncomfortable but not painful
Frequency: Daily or post-workout

Focus areas:
- Quads (after leg workouts)
- IT band (after squats/deadlifts)
- Upper back (after pressing)
- Lats (after pulling)
```

## Injury Prevention

### Red Flag Movements

Stop and assess if you experience:

```json
{
  "sharp_pain": {
    "description": "Sudden, acute pain (not muscle burn)",
    "action": "Stop exercise immediately, seek medical advice if persists"
  },
  "joint_pain": {
    "description": "Pain in knees, shoulders, elbows, wrists",
    "action": "Reduce weight, check form, consider alternative exercise"
  },
  "clicking_with_pain": {
    "description": "Joint clicking/popping accompanied by pain",
    "action": "Stop exercise, consult physical therapist"
  },
  "numbness_tingling": {
    "description": "Nerve symptoms (numbness, tingling, radiating pain)",
    "action": "Stop immediately, seek medical evaluation"
  }
}
```

### Progressive Overload Safety

**The 10% Rule**:
```
Don't increase total volume by more than 10% per week

Example:
Week 1: 50,000 lbs total volume
Week 2 maximum: 55,000 lbs (10% increase)
Week 3 maximum: 60,500 lbs (10% increase from week 2)
```

**Intensity Progression**:
```
Don't increase weight by more than:
- Upper body: 2.5-5 lbs per week
- Lower body: 5-10 lbs per week

If you can't add weight, add reps or sets instead
```

## Recovery Metrics Dashboard

```markdown
## Recovery Status: [Date]

### Sleep
- Last night: 7.5 hours ✅
- 7-day average: 7.8 hours ✅
- Status: Adequate

### Training Load
- This week: 65,000 lbs volume (+15% vs. last week) ⚠️
- Consecutive training days: 5 ✅
- Weeks since deload: 5 ⚠️

### Muscle Group Recovery
| Muscle | Last Trained | Status | Ready? |
|--------|--------------|--------|--------|
| Chest  | 48h ago      | 🟢 Recovered | Yes |
| Back   | 24h ago      | 🔴 Recovering | No (24h left) |
| Legs   | 72h ago      | 🟢 Recovered | Yes |

### Recommendations
- ⚠️ Deload week recommended next week (5 weeks since last)
- ⚠️ Volume spike this week, maintain or reduce next week
- ✅ Sleep adequate
- ⛔ Don't train back today (needs 24h more)
```

This skill provides comprehensive recovery management to maximize gains and minimize injury risk.
