# Progress Tracking Skill

Frameworks for analyzing and visualizing fitness progress over time.

## Progress Metrics

### Strength Metrics

**Maximum Weight Lifted**:
- Track heaviest weight for each rep range (1RM, 3RM, 5RM, 10RM)
- Calculate estimated 1RM from submaximal lifts
- Monitor trends over weeks/months

**Example**:
```
Barbell Bench Press 5RM Progression:
Jan 1:  185 lbs
Feb 1:  195 lbs (+10 lbs, +5.4%)
Mar 1:  205 lbs (+10 lbs, +5.1%)
Total gain: +20 lbs over 2 months (+10.8%)
```

**Volume Progression**:
- Total weight lifted per exercise
- Total weight lifted per muscle group
- Total weight lifted per workout
- Weekly/monthly volume trends

### Trend Analysis Algorithms

**Linear Regression**:
```python
from scipy import stats

dates = [convert_to_ordinal(date) for date in workout_dates]
weights = [max_weight for workout in workouts]

slope, intercept, r_value, p_value, std_err = stats.linregress(dates, weights)

# slope: lbs gained per day
# r_value: correlation strength (0-1, higher = more consistent)
# r_value² (R²): goodness of fit
```

**R² Interpretation**:
- R² > 0.7: Excellent consistency, strong linear progress
- R² 0.4-0.7: Good progress, some variation
- R² < 0.4: Inconsistent progress, investigate plateaus

**Rate of Progress**:
```
Strength Gain Rate = (Current Max - Starting Max) / Weeks Elapsed
```

Example:
```
Bench Press: Started 185 lbs, now 225 lbs, 16 weeks elapsed
Gain Rate = (225 - 185) / 16 = 2.5 lbs/week
Projected 1-year gain: 2.5 × 52 = 130 lbs (unrealistic long-term, but good short-term)
```

## Plateau Detection

**Plateau Definition**: No improvement for 3+ consecutive workouts on same exercise

**Detection Algorithm**:
```python
def detect_plateau(workout_history, exercise_name, weeks=3):
    recent_workouts = get_last_n_weeks(workout_history, weeks)
    max_weights = [get_max_weight(w, exercise_name) for w in recent_workouts]

    # Check if max weight hasn't increased
    if len(set(max_weights)) == 1:  # All same weight
        return {
            "plateaued": True,
            "weight": max_weights[0],
            "duration_weeks": weeks,
            "recommendation": "Consider deload, volume increase, or form check"
        }

    # Check if trending downward
    if max_weights[-1] < max_weights[0]:
        return {
            "plateaued": True,
            "declining": True,
            "recommendation": "Rest, deload, or check for overtraining"
        }

    return {"plateaued": False}
```

**Plateau Solutions**:
1. **Deload Week**: Reduce volume 40-50%, maintain intensity
2. **Volume Increase**: Add 1-2 sets per exercise
3. **Frequency Change**: Train muscle 2x/week instead of 1x
4. **Technique Work**: Focus on form with lighter weight
5. **Program Change**: Switch to different rep ranges or exercises

## Chart Generation Best Practices

### Line Charts (Strength Over Time)

**Use Cases**:
- Single exercise progress (bench press over 6 months)
- Multiple exercises comparison (squat vs deadlift progress)
- Volume trends

**Python Example** (matplotlib):
```python
import matplotlib.pyplot as plt
from datetime import datetime

def create_strength_progress_chart(exercise_name, workout_data):
    dates = []
    weights = []

    for workout in workout_data:
        if exercise_name in workout['exercises']:
            dates.append(datetime.fromisoformat(workout['date']))
            max_weight = max(set['weight_lbs'] for set in workout['exercises'][exercise_name]['sets'])
            weights.append(max_weight)

    plt.figure(figsize=(12, 6))
    plt.plot(dates, weights, marker='o', linewidth=2, markersize=6)
    plt.title(f'{exercise_name} - Strength Progress', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Weight (lbs)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # Add trend line
    from scipy import stats
    dates_ordinal = [d.toordinal() for d in dates]
    slope, intercept, r, p, se = stats.linregress(dates_ordinal, weights)
    trend_line = [slope * x + intercept for x in dates_ordinal]
    plt.plot(dates, trend_line, '--', color='red', alpha=0.7, label=f'Trend (R²={r**2:.2f})')

    plt.legend()
    plt.savefig(f'./fitness/reports/charts/{exercise_name.lower().replace(" ", "-")}-progress.png', dpi=300)
    plt.close()
```

### Bar Charts (Volume by Muscle Group)

**Use Cases**:
- Weekly volume breakdown
- Muscle group balance analysis
- Compare time periods

**Python Example**:
```python
def create_volume_by_muscle_chart(week_data):
    muscle_groups = {}

    for workout in week_data:
        for exercise in workout['exercises']:
            muscle = exercise['category']
            volume = exercise['total_volume_lbs']
            muscle_groups[muscle] = muscle_groups.get(muscle, 0) + volume

    plt.figure(figsize=(10, 6))
    plt.bar(muscle_groups.keys(), muscle_groups.values(), color='steelblue')
    plt.title('Weekly Volume by Muscle Group', fontsize=16, fontweight='bold')
    plt.xlabel('Muscle Group', fontsize=12)
    plt.ylabel('Total Volume (lbs)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('./fitness/reports/charts/weekly-volume-by-muscle.png', dpi=300)
    plt.close()
```

### Heatmaps (Training Frequency)

**Use Cases**:
- Visualize training patterns over months
- Identify rest day patterns
- Spot overtraining periods

**Python Example** (plotly):
```python
import plotly.graph_objects as go
import pandas as pd

def create_training_frequency_heatmap(workouts, months=3):
    # Create date range
    dates = pd.date_range(end=datetime.now(), periods=months*30)

    # Mark workout days
    workout_dates = [w['date'] for w in workouts]
    workout_counts = pd.Series(1, index=workout_dates).resample('D').sum().fillna(0)

    # Create heatmap data
    heatmap_data = []
    for date in dates:
        heatmap_data.append({
            'date': date,
            'day_of_week': date.strftime('%A'),
            'week': date.week,
            'workouts': workout_counts.get(date, 0)
        })

    df = pd.DataFrame(heatmap_data)
    pivot = df.pivot(index='day_of_week', columns='week', values='workouts')

    fig = go.Figure(data=go.Heatmap(
        z=pivot.values,
        x=pivot.columns,
        y=pivot.index,
        colorscale='Blues'
    ))

    fig.update_layout(
        title='Training Frequency Heatmap',
        xaxis_title='Week',
        yaxis_title='Day of Week'
    )

    fig.write_image('./fitness/reports/charts/frequency-heatmap.png')
```

## Report Formatting Standards

### Executive Summary Format

```markdown
## Executive Summary

**Period**: [Start Date] - [End Date]
**Total Workouts**: N
**Total Volume**: X,XXX,XXX lbs

**Key Achievements**:
- [Exercise]: +X lbs (+Y%)
- [Exercise]: +X lbs (+Y%)
- [Achievement milestone]

**Overall Trend**: ↗️ Improving / → Maintaining / ↘️ Declining

**Recommendation**: [Primary action item]
```

### Detailed Analysis Format

```markdown
## Strength Progression Analysis

### [Exercise Name]

**Progress**:
- Starting point (6 months ago): X lbs × Y reps
- Current status: X lbs × Y reps
- Total gain: +X lbs (+Y%)
- Average gain: X lbs/month

**Trend**: [Description of consistency, plateaus, breakthroughs]

**Chart**: ![Progress Chart](./charts/exercise-name-progress.png)

**Recommendations**:
- [Specific action 1]
- [Specific action 2]
```

## Comparative Analysis Methods

### Period-over-Period Comparison

Compare current performance to previous period:

```
Current Month vs. Previous Month:
- Bench Press: 225 lbs (prev: 215 lbs, +10 lbs, +4.7%)
- Squat: 275 lbs (prev: 265 lbs, +10 lbs, +3.8%)
- Volume: 250,000 lbs (prev: 235,000 lbs, +15,000 lbs, +6.4%)
```

### Goal Progress Tracking

If user has goals defined:

```json
{
  "goals": {
    "bench_press_1rm": {
      "target": 315,
      "current": 225,
      "progress": 71.4%,
      "gap": 90,
      "estimated_completion": "2025-06-15"
    }
  }
}
```

### Personal Best Timeline

Show when PRs were achieved:

```markdown
## Personal Records Timeline

**Barbell Bench Press**:
- 2025-01-21: 225 lbs × 5 ⭐ Current PR
- 2024-12-15: 220 lbs × 5
- 2024-11-01: 215 lbs × 5
- 2024-09-10: 205 lbs × 5
- 2024-07-20: 195 lbs × 5

**Time Between PRs**:
- Average: 29 days
- Fastest: 23 days (Nov to Dec)
- Slowest: 37 days (Jan to current)
```

## Visualization Color Schemes

**Progress Status Colors**:
- 🟢 Green: Improving (positive trend)
- 🟡 Yellow: Plateaued (no change 3+ weeks)
- 🔴 Red: Declining (negative trend)

**Chart Colors** (colorblind-friendly):
- Primary: `#1f77b4` (blue)
- Secondary: `#ff7f0e` (orange)
- Success: `#2ca02c` (green)
- Warning: `#d62728` (red)
- Neutral: `#7f7f7f` (gray)

## Data Aggregation Patterns

### Weekly Summary

```python
def get_weekly_summary(workouts, week_start_date):
    week_workouts = filter_by_week(workouts, week_start_date)

    return {
        "week_start": week_start_date,
        "total_workouts": len(week_workouts),
        "total_volume": sum(w['total_volume_lbs'] for w in week_workouts),
        "total_exercises": sum(w['total_exercises'] for w in week_workouts),
        "average_duration": avg(w['duration_minutes'] for w in week_workouts),
        "muscle_groups_trained": unique(e['category'] for w in week_workouts for e in w['exercises']),
        "prs_achieved": count_prs(week_workouts)
    }
```

### Monthly Summary

```python
def get_monthly_summary(workouts, month):
    month_workouts = filter_by_month(workouts, month)
    weeks = group_by_week(month_workouts)

    return {
        "month": month,
        "total_workouts": len(month_workouts),
        "weeks_trained": len(weeks),
        "total_volume": sum(w['total_volume_lbs'] for w in month_workouts),
        "avg_weekly_volume": avg(week_volume for week in weeks),
        "volume_consistency": std_dev(week_volume for week in weeks),
        "strength_gains": calculate_strength_gains(month_workouts),
        "prs_achieved": count_prs(month_workouts)
    }
```

## Progress Milestones

Define and celebrate major milestones:

```json
{
  "milestones": {
    "bench_press": [
      {"weight": 135, "name": "Plate", "achieved": "2024-03-15"},
      {"weight": 185, "name": "Plate +25", "achieved": "2024-06-20"},
      {"weight": 225, "name": "Two Plates", "achieved": "2025-01-21"},
      {"weight": 315, "name": "Three Plates", "achieved": null, "next_goal": true}
    ],
    "squat": [
      {"weight": 225, "name": "Two Plates", "achieved": "2024-05-10"},
      {"weight": 315, "name": "Three Plates", "achieved": "2024-11-15"},
      {"weight": 405, "name": "Four Plates", "achieved": null, "next_goal": true}
    ]
  }
}
```

This skill provides comprehensive frameworks for analyzing progress and creating insightful visualizations.
