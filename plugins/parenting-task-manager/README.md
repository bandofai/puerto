# Parenting Task Manager Plugin

Child activity and developmental milestone tracking specialist for Puerto.

## Overview

The Parenting Task Manager plugin helps parents organize school events, activity schedules, developmental milestones, chores, and family coordination.

## Features

- **School Calendar**: Track events, holidays, permission slips, deadlines
- **Activity Scheduling**: Manage sports, music, tutoring, extracurriculars
- **Milestone Tracking**: Monitor developmental progress by age
- **Chore System**: Assign chores, track completion, manage allowance
- **Coordination**: Prevent conflicts, manage carpools, track contacts

## Agents

### 1. school-calendar-manager (Haiku)
Fast school event and permission slip tracking.

**Usage:**
```
@school-calendar-manager Add field trip to Science Museum on March 15, permission slip due March 10
@school-calendar-manager Show upcoming school events for Emma
@school-calendar-manager Remind me about permission slips due this week
```

### 2. activity-scheduler (Haiku)
Activity and extracurricular scheduling.

**Usage:**
```
@activity-scheduler Add soccer practice: Tuesdays and Thursdays 4:30-5:30pm
@activity-scheduler Show this week's activity schedule for all kids
@activity-scheduler Check for scheduling conflicts on Wednesday
```

### 3. milestone-tracker (Sonnet)
Developmental milestone tracking and guidance.

**Usage:**
```
@milestone-tracker What milestones should I expect for my 18-month-old?
@milestone-tracker Log milestone: Emma said her first sentence today
@milestone-tracker Show developmental progress for the past 6 months
```

### 4. chore-manager (Haiku)
Chore assignment and allowance tracking.

**Usage:**
```
@chore-manager Create age-appropriate chore list for 8-year-old
@chore-manager Mark Emma's chores as complete for today
@chore-manager Calculate this week's allowance
```

## Skills

### school-management
School calendar patterns, permission slip tracking, deadline management.

### child-activities
Activity scheduling, coordination, conflict resolution, balance guidelines.

### developmental-tracking
Age-based milestones across physical, cognitive, language, social-emotional domains.

## Templates

### school-calendar.json
School year events, permission slips, deadlines.

### activity-schedule.json
Extracurricular activities with schedules, contacts, costs.

### chore-system.json
Chore assignments, allowance tracking, completion records.

## Getting Started

### 1. Add Children
```
@school-calendar-manager Add child: Emma, Grade 3, Mrs. Johnson, Lincoln Elementary
```

### 2. Import School Calendar
```
@school-calendar-manager Import school calendar for 2024-2025
```

### 3. Add Activities
```
@activity-scheduler Add Emma to soccer (Tuesdays/Thursdays 4:30pm)
```

### 4. Set Up Chores
```
@chore-manager Create chore system for Emma (age 8, $5/week allowance)
```

### 5. Track Milestones
```
@milestone-tracker Show expected milestones for 3-year-old
```

## Best Practices

1. **Update weekly**: Review calendar and activities every Sunday
2. **Set reminders**: Permission slips 5 days before due date
3. **Balance activities**: Max 2-3 per child per season
4. **Track milestones**: Note achievements during well-child visits
5. **Involve children**: Age-appropriate input on activities and chores

## Cost Optimization

- **Haiku agents** (school-calendar-manager, activity-scheduler, chore-manager): Fast, frequent operations
- **Sonnet agent** (milestone-tracker): Developmental guidance and analysis

## License

MIT
