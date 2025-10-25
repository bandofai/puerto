# Child Activities Skill

Comprehensive patterns for activity scheduling, coordination, and conflict management.

## Activity Data Structure

```json
{
  "activity": {
    "id": "activity-001",
    "childId": "child-001",
    "type": "sports",
    "name": "Soccer",
    "season": "Fall 2025",
    "schedule": {
      "practice": [
        {"day": "Tuesday", "time": "16:30", "duration": 60},
        {"day": "Thursday", "time": "16:30", "duration": 60}
      ],
      "games": [
        {"date": "2025-09-15", "time": "09:00", "location": "Field 3"}
      ]
    },
    "location": "Community Sports Complex",
    "coach": {
      "name": "Coach Smith",
      "phone": "555-1234",
      "email": "coach.smith@email.com"
    },
    "costs": {
      "registration": 150,
      "uniform": 45,
      "equipment": 30
    },
    "requirements": ["Cleats", "Shin guards", "Water bottle"],
    "carpool": ["Parent A", "Parent B"]
  }
}
```

## Activity Categories

### Sports
- Team sports (soccer, basketball, baseball)
- Individual sports (swimming, tennis, martial arts)
- Seasonal considerations
- Equipment needs
- Tournament schedules

### Arts & Music
- Music lessons (instrument, voice)
- Dance classes (ballet, hip-hop, jazz)
- Art classes (painting, pottery)
- Theater programs
- Recital/performance dates

### Academic
- Tutoring sessions
- Test preparation
- STEM clubs (robotics, coding)
- Language classes
- Academic enrichment

### Other
- Scouts (Boy Scouts, Girl Scouts)
- Religious education
- Community service
- Summer camps

## Scheduling Best Practices

### Conflict Detection
- Overlapping activities for same child
- Transportation conflicts (can't be two places)
- Family dinner time protection
- Homework time preservation
- Sibling event conflicts

### Balance Guidelines
- Maximum 2-3 activities per child per season
- At least 2 free weekday evenings
- Preserve family time on weekends
- Consider child's interests vs. parent's goals
- Allow downtime for free play

### Registration Cycles
- Fall: August-September (school sports, music)
- Winter: November-December (basketball, indoor activities)
- Spring: February-March (soccer, baseball, outdoor)
- Summer: April-May (camps, summer programs)
