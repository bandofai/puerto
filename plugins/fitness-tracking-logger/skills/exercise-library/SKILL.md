# Exercise Library Skill

Comprehensive exercise database with categorization, alternatives, and form guidance.

## Exercise Categorization

### By Muscle Group

```json
{
  "chest": {
    "primary_exercises": [
      "Barbell Bench Press",
      "Incline Barbell Bench Press",
      "Dumbbell Bench Press",
      "Incline Dumbbell Bench Press"
    ],
    "secondary_exercises": [
      "Cable Fly",
      "Dumbbell Fly",
      "Push-up",
      "Dip"
    ]
  },
  "back": {
    "thickness": [
      "Barbell Row",
      "Dumbbell Row",
      "T-Bar Row",
      "Seated Cable Row"
    ],
    "width": [
      "Pull-up",
      "Lat Pulldown",
      "Wide Grip Pull-up"
    ]
  },
  "legs": {
    "quad_dominant": [
      "Barbell Back Squat",
      "Front Squat",
      "Leg Press",
      "Bulgarian Split Squat"
    ],
    "hip_dominant": [
      "Barbell Deadlift",
      "Romanian Deadlift",
      "Hip Thrust",
      "Glute Ham Raise"
    ],
    "isolation": [
      "Leg Extension",
      "Leg Curl",
      "Calf Raise"
    ]
  },
  "shoulders": {
    "overhead_press": [
      "Barbell Overhead Press",
      "Dumbbell Shoulder Press",
      "Arnold Press"
    ],
    "lateral": [
      "Lateral Raise",
      "Cable Lateral Raise",
      "Machine Lateral Raise"
    ],
    "rear_delt": [
      "Face Pull",
      "Reverse Fly",
      "Rear Delt Fly"
    ]
  },
  "arms": {
    "biceps": [
      "Barbell Curl",
      "Dumbbell Curl",
      "Hammer Curl",
      "Cable Curl"
    ],
    "triceps": [
      "Close Grip Bench Press",
      "Tricep Dip",
      "Overhead Tricep Extension",
      "Cable Tricep Pushdown"
    ]
  }
}
```

### By Movement Pattern

```json
{
  "horizontal_push": [
    "Barbell Bench Press",
    "Dumbbell Bench Press",
    "Push-up",
    "Machine Chest Press"
  ],
  "horizontal_pull": [
    "Barbell Row",
    "Dumbbell Row",
    "Seated Cable Row",
    "T-Bar Row"
  ],
  "vertical_push": [
    "Barbell Overhead Press",
    "Dumbbell Shoulder Press",
    "Handstand Push-up"
  ],
  "vertical_pull": [
    "Pull-up",
    "Lat Pulldown",
    "Chin-up"
  ],
  "squat_pattern": [
    "Barbell Back Squat",
    "Front Squat",
    "Goblet Squat",
    "Bulgarian Split Squat"
  ],
  "hinge_pattern": [
    "Barbell Deadlift",
    "Romanian Deadlift",
    "Kettlebell Swing",
    "Good Morning"
  ]
}
```

### By Equipment

```json
{
  "barbell": [
    "Bench Press",
    "Squat",
    "Deadlift",
    "Overhead Press",
    "Row"
  ],
  "dumbbell": [
    "Dumbbell Bench Press",
    "Dumbbell Row",
    "Dumbbell Curl",
    "Dumbbell Fly"
  ],
  "bodyweight": [
    "Pull-up",
    "Push-up",
    "Dip",
    "Bodyweight Squat"
  ],
  "machine": [
    "Leg Press",
    "Lat Pulldown",
    "Cable Fly",
    "Leg Extension"
  ],
  "cable": [
    "Cable Fly",
    "Cable Row",
    "Cable Curl",
    "Face Pull"
  ]
}
```

## Exercise Database Structure

```json
{
  "exercises": [
    {
      "name": "Barbell Bench Press",
      "category": "chest",
      "secondary_muscles": ["triceps", "shoulders"],
      "movement_pattern": "horizontal_push",
      "equipment": "barbell",
      "difficulty": "intermediate",
      "type": "compound",
      "alternatives": [
        "Dumbbell Bench Press",
        "Machine Chest Press",
        "Push-up"
      ],
      "form_cues": [
        "Retract scapula (squeeze shoulder blades together)",
        "Arch lower back slightly",
        "Bar path should be straight down to mid-chest",
        "Drive feet into ground",
        "Elbows at 45-degree angle, not flared",
        "Full ROM: touch chest, lock out elbows"
      ],
      "safety_notes": "Use spotter for heavy sets. Don't bounce bar off chest. Control descent.",
      "common_mistakes": [
        "Elbows flared too wide (90 degrees)",
        "No leg drive",
        "Bouncing bar off chest",
        "Uneven bar path"
      ],
      "recommended_rep_ranges": {
        "strength": "1-5 reps",
        "hypertrophy": "6-12 reps",
        "endurance": "12-20 reps"
      },
      "typical_weight_progression": "2.5-5 lbs per week for beginners"
    },
    {
      "name": "Barbell Back Squat",
      "category": "legs",
      "secondary_muscles": ["glutes", "hamstrings", "core"],
      "movement_pattern": "squat_pattern",
      "equipment": "barbell",
      "difficulty": "intermediate",
      "type": "compound",
      "alternatives": [
        "Front Squat",
        "Goblet Squat",
        "Leg Press",
        "Bulgarian Split Squat"
      ],
      "form_cues": [
        "Bar on upper traps (high bar) or rear delts (low bar)",
        "Feet shoulder-width apart, toes slightly out",
        "Chest up, core braced",
        "Break at hips and knees simultaneously",
        "Knees track over toes",
        "Depth: hip crease below knee (parallel or below)",
        "Drive through heels and midfoot"
      ],
      "safety_notes": "Use safety bars/spotter. Don't round lower back. Bail safely if needed.",
      "common_mistakes": [
        "Knees caving in (valgus collapse)",
        "Chest dropping forward",
        "Not hitting depth",
        "Rising onto toes",
        "Lower back rounding"
      ],
      "recommended_rep_ranges": {
        "strength": "1-5 reps",
        "hypertrophy": "6-10 reps",
        "endurance": "12-20 reps"
      },
      "typical_weight_progression": "5-10 lbs per week for beginners"
    },
    {
      "name": "Barbell Deadlift",
      "category": "back",
      "secondary_muscles": ["legs", "glutes", "traps", "core"],
      "movement_pattern": "hinge_pattern",
      "equipment": "barbell",
      "difficulty": "advanced",
      "type": "compound",
      "alternatives": [
        "Romanian Deadlift",
        "Trap Bar Deadlift",
        "Sumo Deadlift"
      ],
      "form_cues": [
        "Feet hip-width apart, bar over mid-foot",
        "Grip bar just outside legs",
        "Neutral spine (not rounded, not hyperextended)",
        "Engage lats (pull shoulder blades down and back)",
        "Hip hinge: push hips back",
        "Drive through floor with legs",
        "Lockout: hips and knees extend simultaneously"
      ],
      "safety_notes": "Keep bar close to body. Neutral spine essential. Don't jerk the bar.",
      "common_mistakes": [
        "Rounded lower back",
        "Bar drifting away from body",
        "Starting with hips too low (turning into squat)",
        "Hyperextending at lockout",
        "Jerking the bar off floor"
      ],
      "recommended_rep_ranges": {
        "strength": "1-5 reps",
        "hypertrophy": "5-8 reps",
        "endurance": "8-12 reps"
      },
      "typical_weight_progression": "5-10 lbs per week for beginners"
    }
  ]
}
```

## Exercise Substitutions

When exercise not available, suggest alternatives:

### Barbell Unavailable
```
User: "Barbell Bench Press"
No barbell? Try:
- Dumbbell Bench Press (nearly identical movement)
- Push-up (bodyweight alternative)
- Machine Chest Press (guided movement)
```

### Injury Modifications
```
Shoulder pain during Barbell Bench Press?
Try:
- Dumbbell Bench Press (allows natural arm path)
- Floor Press (reduced ROM, less shoulder stress)
- Cable Fly (constant tension, less joint stress)
```

### Home Gym Alternatives
```
Gym exercise → Home alternative:
- Lat Pulldown → Pull-up/Chin-up
- Leg Press → Goblet Squat
- Cable Fly → Resistance Band Fly
- Machine Row → Dumbbell Row
```

## Difficulty Levels

```json
{
  "beginner": {
    "definition": "0-6 months training experience",
    "exercises": [
      "Machine Chest Press",
      "Goblet Squat",
      "Dumbbell Row",
      "Assisted Pull-up"
    ],
    "notes": "Focus on learning movement patterns, prioritize form over weight"
  },
  "intermediate": {
    "definition": "6 months - 2 years experience",
    "exercises": [
      "Barbell Bench Press",
      "Barbell Squat",
      "Romanian Deadlift",
      "Barbell Row"
    ],
    "notes": "Can handle free weights, developing strength base"
  },
  "advanced": {
    "definition": "2+ years consistent training",
    "exercises": [
      "Barbell Deadlift",
      "Front Squat",
      "Overhead Press",
      "Deficit Deadlift"
    ],
    "notes": "Mastered basic movements, can handle complex variations"
  }
}
```

## Form Cue Library

### Universal Cues

**Bracing**:
- "Take deep breath, brace core like taking punch"
- "360-degree abdominal pressure"
- "Maintain rigidity through lift"

**Shoulder Position**:
- "Retract scapula (squeeze shoulder blades together)"
- "Pull shoulders down and back"
- "Create stable shelf for bar"

**Breathing**:
- "Inhale before descent"
- "Exhale at top/lockout"
- "Hold breath during hardest part (Valsalva maneuver for heavy lifts)"

### Exercise-Specific Cues

**Bench Press**:
- "Bend the bar" (engage lats)
- "Leg drive" (push feet into floor)
- "Elbows at 45 degrees"

**Squat**:
- "Spread the floor" (drive knees out)
- "Break at hips and knees together"
- "Chest up, look ahead"

**Deadlift**:
- "Pull the slack out of the bar"
- "Push the floor away"
- "Hips and shoulders rise together"

**Overhead Press**:
- "Squeeze glutes"
- "Push head through at lockout"
- "Keep bar path vertical"

## Safety Guidelines

### Red Flags (Stop Immediately)

- Sharp pain (vs. muscle burn)
- Joint clicking/popping with pain
- Numbness or tingling
- Dizziness or lightheadedness
- Loss of control of weight

### When to Use Spotter

Required:
- Barbell Bench Press (heavy sets)
- Barbell Squat (near-maximal weights)
- Any lift attempting new 1RM

Optional but recommended:
- Dumbbell exercises near failure
- Learning new exercises
- Training alone

### Weight Selection Guidelines

**First Time with Exercise**:
- Start with empty bar (45 lbs) or very light dumbbells
- Focus on form, not weight
- Gradually increase over weeks

**Progressive Loading**:
- Warm up with lighter sets first
- Increase weight 5-10% per set
- Working sets should be challenging but controlled

## Common Exercise Variations

### Bench Press Variations
```
- Flat Barbell Bench Press (standard)
- Incline Bench Press (upper chest emphasis)
- Decline Bench Press (lower chest emphasis)
- Close Grip Bench Press (triceps emphasis)
- Pause Bench Press (strength at bottom)
```

### Squat Variations
```
- High Bar Back Squat (upright torso, quad focus)
- Low Bar Back Squat (hip hinge, posterior chain)
- Front Squat (quad emphasis, upright)
- Box Squat (depth consistency, power)
- Pause Squat (strength out of hole)
```

### Deadlift Variations
```
- Conventional Deadlift (standard stance)
- Sumo Deadlift (wide stance, upright)
- Romanian Deadlift (hamstring focus)
- Trap Bar Deadlift (beginner-friendly)
- Deficit Deadlift (increased ROM)
```

## Exercise Selection for Goals

### Strength (Powerlifting)
```
Primary: Squat, Bench Press, Deadlift
Accessories: Pause variations, Close Grip Bench, Romanian Deadlift
Rep Range: 1-5 reps
```

### Hypertrophy (Bodybuilding)
```
Primary: Compound movements (Squat, Bench, Row)
Accessories: Isolation (Curls, Lateral Raises, Leg Extensions)
Rep Range: 8-12 reps
Volume: High (15-20 sets per muscle per week)
```

### Athletic Performance
```
Primary: Power movements (Clean, Snatch, Jump Squat)
Accessories: Compound lifts, Unilateral work
Rep Range: 3-6 reps (explosive)
```

### General Fitness
```
Balanced approach:
- 2-3 compound movements per workout
- 2-3 accessory movements
- Mix of rep ranges (5-12 reps)
- Full body or Upper/Lower split
```

This skill provides comprehensive exercise knowledge for proper logging, substitutions, and program design.
