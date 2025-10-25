# Workout Logging Skill

Best practices for exercise logging, data capture, and validation in fitness tracking.

## Exercise Naming Conventions

**Standard Format**: `[Equipment] [Exercise Name]`

Examples:
- Barbell Bench Press
- Dumbbell Bicep Curl
- Bodyweight Pull-up
- Machine Leg Press
- Cable Tricep Pushdown

**Aliases**: Common variations should be normalized
- "Bench" → "Barbell Bench Press"
- "Squat" → "Barbell Back Squat"
- "Deadlift" → "Barbell Deadlift"

## Sets, Reps, Weight Validation

**Required Fields**:
- `set_number`: Integer (1, 2, 3, ...)
- `reps`: Integer (1-50)
- `weight_lbs` or `weight_kg`: Decimal (0-1000)

**Optional Fields**:
- `rpe`: Rate of Perceived Exertion (1-10 scale)
- `rest_seconds`: Integer (30-600)
- `notes`: String (form cues, feelings)

**Validation Rules**:
```javascript
{
  "reps": {
    "min": 1,
    "max": 50,
    "warning_above": 30 // Likely cardio, not strength
  },
  "weight_lbs": {
    "min": 0,
    "max": 1000,
    "bodyweight_exercises": 0 // Pull-ups, dips, etc.
  },
  "rpe": {
    "min": 1,
    "max": 10,
    "scale": "1=very easy, 10=maximum effort"
  }
}
```

## RPE Scale (Rate of Perceived Exertion)

| RPE | Description | Reps in Reserve (RIR) |
|-----|-------------|----------------------|
| 1-2 | Very easy warmup | Could do 10+ more reps |
| 3-4 | Light effort | Could do 7-8 more reps |
| 5-6 | Moderate effort | Could do 4-6 more reps |
| 7 | Hard but controlled | Could do 3 more reps |
| 8 | Very hard | Could do 2 more reps |
| 9 | Extremely hard | Could do 1 more rep |
| 10 | Maximum effort | Could do 0 more reps (failure) |

**Usage**:
- Track intensity across workouts
- Identify when form may be compromised (RPE 10)
- Plan deloads (keep RPE 6-7 during deload)

## Volume Calculation Formulas

**Exercise Volume**:
```
Exercise Volume = Σ(sets) (reps × weight)
```

Example:
```
Bench Press:
Set 1: 8 reps × 185 lbs = 1,480 lbs
Set 2: 8 reps × 185 lbs = 1,480 lbs
Set 3: 7 reps × 185 lbs = 1,295 lbs
Total: 4,255 lbs
```

**Workout Volume**:
```
Total Workout Volume = Σ(all exercises) Exercise Volume
```

**Weekly Volume** (for muscle group):
```
Weekly Chest Volume = Σ(all chest exercises in week) Exercise Volume
```

## Workout Duration Tracking

Track total time from first set to last set:
```json
{
  "start_time": "09:30:00",
  "end_time": "10:45:00",
  "duration_minutes": 75
}
```

**Efficiency Metrics**:
- Volume per minute: Total Volume / Duration
- Higher = more efficient workout
- Track trends over time

## Input Parsing Patterns

Accept flexible user input and normalize:

**Pattern 1**: `weight x reps`
```
Input: "185x8"
Parse: 185 lbs, 8 reps
```

**Pattern 2**: `weight x reps, weight x reps, ...`
```
Input: "185x8, 185x8, 185x7"
Parse: 3 sets with specified weights/reps
```

**Pattern 3**: `sets x reps @ weight`
```
Input: "3x8 @ 185"
Parse: 3 sets, 8 reps each, 185 lbs
```

**Pattern 4**: Natural language
```
Input: "Bench press 185 pounds for 3 sets of 8 reps"
Parse: Exercise=Barbell Bench Press, 3 sets, 8 reps, 185 lbs
```

## Workout Structure Best Practices

**Recommended Order**:
1. Warmup (5-10 minutes, not logged)
2. Compound exercises first (squat, bench, deadlift)
3. Accessory exercises second
4. Isolation exercises last
5. Cooldown/stretching (not logged)

**Set Progression**:
- Warmup sets: Lower weight, higher reps (not counted in volume)
- Working sets: Target weight and reps (counted)
- Drop sets: Reduce weight, maintain reps (optional)

## Notes and Form Cues

Encourage users to add notes:

**Good Notes**:
- "Felt strong, perfect form"
- "Last rep was a grinder"
- "Elbows flared out, fix next time"
- "New PR!"
- "Lower back felt tight, reduce weight"

**Form Cues to Track**:
- Bench: Retract scapula, feet drive, bar path
- Squat: Depth, knee tracking, chest up
- Deadlift: Neutral spine, lats engaged, hip hinge

## Quality Checklist

Before saving workout:
- [ ] All exercises have valid names
- [ ] All sets have reps and weight
- [ ] Volume calculated correctly
- [ ] Workout duration recorded
- [ ] Date and time accurate
- [ ] Unique workout ID generated
- [ ] JSON structure valid

## Common Errors and Fixes

**Error**: Missing weight for set
```json
// Bad
{"set": 1, "reps": 8}

// Good
{"set": 1, "reps": 8, "weight_lbs": 185}
```

**Error**: Invalid exercise name
```
User input: "bench"
Correction: "Did you mean: Barbell Bench Press?"
```

**Error**: Unrealistic values
```
User input: "Bench press 500 lbs x 20"
Validation: "⚠️ This seems unusual. Please confirm weight (500 lbs) and reps (20)"
```

## Exercise Categorization

Group exercises by muscle:

```json
{
  "chest": ["Barbell Bench Press", "Dumbbell Fly", "Push-up"],
  "back": ["Pull-up", "Barbell Row", "Lat Pulldown"],
  "legs": ["Barbell Squat", "Leg Press", "Romanian Deadlift"],
  "shoulders": ["Overhead Press", "Lateral Raise", "Face Pull"],
  "arms": ["Barbell Curl", "Tricep Dip", "Hammer Curl"]
}
```

Used for:
- Muscle group volume tracking
- Recovery monitoring
- Program balance analysis

## Data Persistence

**File Naming**: `YYYY-MM-DD-session-XXX.json`
- YYYY-MM-DD: Workout date
- XXX: Session number (001, 002, ...)

**File Location**: `./fitness/workouts/`

**Backup**: Recommend backing up to cloud storage regularly

## Integration Points

After saving workout:
1. Check for PRs (use record-tracker)
2. Update weekly volume stats
3. Check recovery status (use health-monitor)
4. Update template progress if using one

## Example Complete Workout

```json
{
  "workout_id": "20250121-001",
  "date": "2025-01-21",
  "start_time": "09:30:00",
  "end_time": "10:45:00",
  "duration_minutes": 75,
  "type": "strength",
  "template_id": "upper-body-power",
  "exercises": [
    {
      "name": "Barbell Bench Press",
      "category": "chest",
      "movement_pattern": "horizontal_push",
      "sets": [
        {"set_number": 1, "reps": 8, "weight_lbs": 185, "rpe": 7, "rest_seconds": 180},
        {"set_number": 2, "reps": 8, "weight_lbs": 185, "rpe": 7.5, "rest_seconds": 180},
        {"set_number": 3, "reps": 7, "weight_lbs": 185, "rpe": 9, "rest_seconds": 180, "notes": "Last rep tough"}
      ],
      "total_volume_lbs": 4255,
      "total_reps": 23,
      "max_weight_lbs": 185,
      "notes": "Good session"
    },
    {
      "name": "Barbell Row",
      "category": "back",
      "movement_pattern": "horizontal_pull",
      "sets": [
        {"set_number": 1, "reps": 8, "weight_lbs": 135, "rpe": 6, "rest_seconds": 120},
        {"set_number": 2, "reps": 8, "weight_lbs": 135, "rpe": 7, "rest_seconds": 120},
        {"set_number": 3, "reps": 8, "weight_lbs": 135, "rpe": 7, "rest_seconds": 120}
      ],
      "total_volume_lbs": 3240,
      "total_reps": 24,
      "max_weight_lbs": 135
    }
  ],
  "body_weight_lbs": 180,
  "total_volume_lbs": 7495,
  "total_exercises": 2,
  "notes": "Felt strong today, bench moving well",
  "created_at": "2025-01-21T10:45:00Z"
}
```

This skill provides the foundation for consistent, accurate workout tracking across all fitness logging agents.
