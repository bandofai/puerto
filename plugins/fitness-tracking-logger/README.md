# Fitness Tracking Logger Plugin

Comprehensive workout logging and fitness progress tracking system for Puerto.

## Overview

The Fitness Tracking Logger plugin provides a complete fitness tracking solution with workout logging, progress analysis, personal records tracking, template management, and injury prevention monitoring.

## Features

- **Workout Logging**: Fast, accurate exercise entry with volume calculations
- **Progress Analysis**: Visualize strength gains and track trends over time
- **Personal Records**: Automatic PR detection and celebration
- **Workout Templates**: Reusable routines with progressive overload
- **Health Monitoring**: Overtraining detection and recovery recommendations

## Agents

### workout-logger (Primary Entry Point)
- **Model**: Haiku (fast, cost-effective)
- **Purpose**: Log workouts with exercises, sets, reps, and weight
- **Usage**: `@workout-logger log my workout`

### progress-analyzer
- **Model**: Sonnet (analysis and judgment)
- **Purpose**: Analyze progress, generate charts, identify trends
- **Usage**: `@progress-analyzer show bench press progress last 6 months`

### record-tracker
- **Model**: Haiku (deterministic tracking)
- **Purpose**: Track personal records and detect new PRs
- **Usage**: `@record-tracker check for PRs`

### template-manager
- **Model**: Haiku (CRUD operations)
- **Purpose**: Manage workout templates and routines
- **Usage**: `@template-manager load upper body power`

### health-monitor
- **Model**: Sonnet (medical judgment)
- **Purpose**: Monitor for overtraining and provide recovery advice
- **Usage**: `@health-monitor am I overtraining?`

## Skills

### workout-logging
Best practices for exercise logging, data capture, and validation

### progress-tracking
Frameworks for analyzing and visualizing fitness progress

### exercise-library
Comprehensive exercise database with categorization and alternatives

### recovery-management
Recovery optimization and injury prevention strategies

## Data Structure

Workouts are stored in `./fitness/workouts/` as JSON files:

```json
{
  "workout_id": "20250121-001",
  "date": "2025-01-21",
  "duration_minutes": 75,
  "exercises": [
    {
      "name": "Barbell Bench Press",
      "category": "chest",
      "sets": [
        {"set_number": 1, "reps": 8, "weight_lbs": 185, "rpe": 7}
      ],
      "total_volume_lbs": 4255
    }
  ],
  "total_volume_lbs": 12500
}
```

## Installation

```bash
# Plugin is automatically available in Puerto
# Initialize your fitness data directory:
mkdir -p ./fitness/{workouts,records,templates/custom,reports/charts,health,config}
```

## Usage Examples

### Log a Workout
```
@workout-logger Log my workout

User: Bench press 185x8, 185x8, 185x7
      Squat 225x5, 225x5, 225x5

Agent: ✅ Workout logged: 2025-01-21-001
```

### Check Progress
```
@progress-analyzer Show squat progress last 3 months

Agent: 📊 Squat Progress Analysis
Starting: 185 lbs x 5
Current: 225 lbs x 5
Gain: +40 lbs (+21.6%)
```

### Track Personal Records
```
@record-tracker Check for PRs in today's workout

Agent: 🎉 NEW PR! Bench Press: 225 lbs x 5
Previous PR: 220 lbs x 5 (+5 lbs improvement)
```

### Use Workout Template
```
@template-manager Load my upper body template

Agent: 📋 Loading "Upper Body Power"
Progressive overload applied:
1. Bench Press: 4x5 @ 195 lbs (prev: 190 lbs, +5 lbs)
```

### Monitor Recovery
```
@health-monitor Check my recovery status

Agent: ⚠️ Warning: 9 consecutive training days
Recommendation: Take 1-2 rest days immediately
```

## Integration Points

- **Strava**: Export cardio workouts (script provided)
- **MyFitnessPal**: Sync calorie estimates (script provided)
- **Wearables**: Import sleep/activity data (future)

## Cost & Performance

- Workout logging: ~$0.001 per session (Haiku)
- Progress analysis: ~$0.020 per report (Sonnet)
- Weekly cost: ~$0.16 (4 workouts + 1 analysis)

## Requirements

- Python 3.8+ (for visualization scripts)
- Optional: matplotlib, numpy, pandas (for charts)

## File Structure

```
plugins/fitness-tracking-logger/
├── agents/                      # 5 specialized agents
│   ├── workout-logger.md
│   ├── progress-analyzer.md
│   ├── record-tracker.md
│   ├── template-manager.md
│   └── health-monitor.md
├── skills/                      # 4 comprehensive skills
│   ├── workout-logging/
│   ├── progress-tracking/
│   ├── exercise-library/
│   └── recovery-management/
├── templates/                   # Sample templates
├── scripts/                     # Python utilities
└── README.md
```

## Roadmap

**Current (v1.0)**:
- ✅ Core workout logging
- ✅ Progress tracking
- ✅ Personal records
- ✅ Templates
- ✅ Health monitoring

**Future**:
- Nutrition tracking integration
- Body composition tracking
- Photo progress tracking
- Mobile app companion
- AI workout recommendations

## Support

For issues or questions, refer to Puerto documentation or create an issue in the Puerto repository.

## License

Part of the Puerto plugin ecosystem.

---

**Addresses**: Issue #114 - Fitness Tracking Logger