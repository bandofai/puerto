# Progress Tracking Skill

## Overview

This skill provides efficient techniques for tracking goal progress, calculating velocity metrics, identifying trends, and generating actionable dashboards. Optimized for speed and clarity.

## Core Tracking Principles

### Principle 1: Track Leading and Lagging Indicators
**Lagging**: What happened (results, outcomes)
**Leading**: What's happening (activities, inputs that predict results)

### Principle 2: Keep It Simple
Track minimum viable metrics. Over-tracking creates overhead without insight.

### Principle 3: Make It Visual
Numbers alone don't tell the story. Use progress bars, trends, status indicators.

### Principle 4: Update Frequently
Weekly minimum. Daily for fast-moving goals.

### Principle 5: Flag Issues Early
Red/Yellow/Green status helps spot problems before they're critical.

## Essential Metrics

### 1. Overall Progress (%)
```
Calculation: Weighted by milestone duration

Example:
M1: Complete (100%) × 2 weeks = 200
M2: Complete (100%) × 3 weeks = 300
M3: In progress (60%) × 2 weeks = 120
M4: Not started (0%) × 3 weeks = 0

Total: 620 / (2+3+2+3) weeks = 620/10 = 62% overall
```

### 2. Velocity (% per week)
```
Calculation: Progress gained / Time elapsed

Example:
Started: March 1 (0% complete)
Current: March 29 (4 weeks later, 32% complete)

Velocity: 32% / 4 weeks = 8% per week
```

### 3. Projected Completion Date
```
Calculation: Current date + (Remaining progress / Velocity)

Example:
Current: 62% complete, Velocity: 8%/week
Remaining: 38%
Time needed: 38% / 8% per week = 4.75 weeks
Projected: Current date + 5 weeks
```

### 4. Schedule Variance (days ahead/behind)
```
Calculation: Expected progress vs Actual progress

Example:
Timeline: 12 weeks total
Elapsed: 4 weeks (33% of timeline)
Expected progress: 33%
Actual progress: 32%
Variance: 1% behind

At current pace: ~3 days behind schedule
```

### 5. Burn Rate (for budget-tracked goals)
```
Calculation: Budget spent vs Budget allocated vs Progress

Example:
Budget: $10,000
Spent: $4,500
Progress: 40%

Expected spend at 40%: $4,000
Actual spend: $4,500
Over by: $500 (12.5% over budget at this stage)
```

## Status Determination

### Red/Yellow/Green Framework

**🟢 Green (On Track)**:
- Progress >= 90% of expected
- Velocity >= 90% of required
- No critical blockers
- On or under budget

**🟡 Yellow (At Risk)**:
- Progress 70-89% of expected
- Velocity 70-89% of required
- Some blockers present
- Slightly over budget (<20%)

**🔴 Red (Off Track)**:
- Progress <70% of expected
- Velocity <70% of required
- Critical blockers
- Significantly over budget (>20%)

### Example Status Logic
```python
def determine_status(expected_progress, actual_progress, blockers):
    variance = (actual_progress / expected_progress) * 100

    if variance >= 90 and not critical_blockers(blockers):
        return "🟢 On Track"
    elif variance >= 70:
        return "🟡 At Risk"
    else:
        return "🔴 Off Track"
```

## Tracking Patterns

### Pattern 1: Percentage-Based Tracking
Best for milestones with clear deliverables.

```
Milestone: "Build user authentication"
Tasks:
- Login page: 25% weight
- Registration: 25% weight
- Password reset: 25% weight
- Session management: 25% weight

Progress:
- Login: Complete (25%)
- Registration: Complete (25%)
- Password reset: In progress (15%)
- Session: Not started (0%)

Milestone progress: 65%
```

### Pattern 2: Task Completion Tracking
Best for milestones with discrete tasks.

```
Milestone: "Content marketing campaign"
Tasks: 20 total

Completed: 12
In Progress: 3
Not Started: 5

Progress: 12/20 = 60%
(In progress tasks = 0% until complete for simplicity)
```

### Pattern 3: Time-Based Tracking
Best for research, learning, or time-boxed activities.

```
Milestone: "Complete certification course"
Planned: 40 hours total
Spent: 24 hours
Remaining: 16 hours

Progress: 24/40 = 60%

Note: Time spent ≠ value created, but useful proxy for effort-based goals
```

### Pattern 4: Outcome-Based Tracking
Best for results-oriented goals.

```
Milestone: "Acquire 100 new customers"
Target: 100
Current: 67
Remaining: 33

Progress: 67%
```

## Dashboard Components

### Minimal Viable Dashboard

**Must Have**:
1. Goal statement
2. Overall progress percentage
3. Milestone status table
4. Red/yellow/green indicator
5. Active blockers list
6. Last updated date

**Should Have**:
7. Velocity and trend
8. Projected completion date
9. Recent activity log
10. Next milestones preview

**Nice to Have**:
11. Progress chart/graph
12. Historical comparison
13. Resource utilization
14. Risk assessment

### Dashboard Template

```markdown
# Progress Dashboard
**Goal**: [Goal statement]
**Status**: 🟢/🟡/🔴
**Last Updated**: [Date]

## Overall Progress: XX%
████████████░░░░░░░░

**Timeline**:
- Elapsed: [X] of [Y] weeks
- Remaining: [Z] weeks
- Projected completion: [Date]

**Velocity**: [A]% per week (expected: [B]%)

## Milestones

| Milestone | Progress | Status | Due | Risk |
|-----------|----------|--------|-----|------|
| M1 | 100% ✓ | Done | Past | 🟢 |
| M2 | 75% ⋯ | In Progress | Week X | 🟡 |
| M3 | 0% ○ | Not Started | Week Y | 🟢 |

## Active Blockers
- [Blocker 1]: [Impact] - [Owner]
- [Blocker 2]: [Impact] - [Owner]

## Recent Activity (This Week)
- [Activity 1]
- [Activity 2]
- [Activity 3]

## Next Focus
- [What to work on next]
```

## Velocity Analysis

### Calculating Velocity Trend

```bash
# Simple moving average (last 4 weeks)
Week 1: 6% progress
Week 2: 8% progress
Week 3: 7% progress
Week 4: 9% progress

Average velocity: (6+8+7+9)/4 = 7.5% per week

Trend: ↑ Improving (9% > 7.5% average)
```

### Interpreting Velocity

**Accelerating** (↑):
- Recent weeks faster than average
- Good sign: team hitting stride
- Action: Can we sustain? Any risks?

**Steady** (→):
- Consistent week-to-week
- Predictable progress
- Action: Monitor for changes

**Decelerating** (↓):
- Recent weeks slower than average
- Warning sign: obstacles increasing
- Action: Investigate root cause

### Velocity-Based Forecasting

```
Current velocity: 7% per week
Remaining progress: 45%
Weeks needed: 45% / 7% = 6.4 weeks

If velocity improves to 9%: 45% / 9% = 5 weeks
If velocity drops to 5%: 45% / 5% = 9 weeks

Best case: 5 weeks early
Likely case: 6 weeks (on track)
Worst case: 3 weeks late
```

## Blocker Tracking

### Blocker Classification

**By Impact**:
- **High**: Blocks all progress on milestone
- **Medium**: Slows progress significantly
- **Low**: Minor inconvenience

**By Type**:
- **Dependency**: Waiting on external factor
- **Technical**: Problem with approach/implementation
- **Resource**: Missing people, budget, tools
- **Decision**: Needs stakeholder input

**By Age**:
- **New**: <3 days old
- **Active**: 3-7 days old
- **Stuck**: >7 days old (escalate!)

### Blocker Template

```markdown
## Active Blockers

### Blocker 1: [Name]
**Impact**: High/Medium/Low
**Type**: Dependency/Technical/Resource/Decision
**Age**: [X] days
**Owner**: [Person resolving]
**Status**: Open/In Progress/Resolved
**Blocking**: [Which milestone(s)]
**Description**: [What's blocked and why]
**Action**: [What's being done to resolve]
**ETA**: [When expected to resolve]
```

## Progress Update Workflow

### Update Checklist

**Every Update**:
- [ ] Review milestone progress
- [ ] Update completion percentages
- [ ] Recalculate overall progress
- [ ] Recalculate velocity
- [ ] Update milestone status (red/yellow/green)
- [ ] Log recent activities
- [ ] Add/update blockers
- [ ] Project completion date
- [ ] Archive snapshot

**Weekly**:
- [ ] All of the above, plus:
- [ ] Calculate velocity trend
- [ ] Review if pace sufficient
- [ ] Flag at-risk milestones
- [ ] Update next week priorities

**Monthly**:
- [ ] All of the above, plus:
- [ ] Analyze trends over month
- [ ] Compare to last month
- [ ] Strategic assessment
- [ ] Communicate to stakeholders

## Data Formats

### JSON State File Structure

```json
{
  "goal_id": "increase-blog-traffic-2024q2",
  "goal_statement": "Increase blog traffic 10K→15K by June 30",
  "start_date": "2024-03-01",
  "target_date": "2024-06-30",
  "last_update": "2024-03-29T10:30:00Z",
  "status": "on_track",
  "metrics": {
    "overall_progress": 62,
    "velocity": 8,
    "projected_completion": "2024-06-28",
    "schedule_variance_days": -2
  },
  "milestones": [
    {
      "id": "m1",
      "name": "Content Strategy",
      "progress": 100,
      "status": "complete",
      "due_date": "2024-03-15",
      "completed_date": "2024-03-14"
    },
    {
      "id": "m2",
      "name": "Optimize Content",
      "progress": 75,
      "status": "in_progress",
      "due_date": "2024-03-29",
      "risk": "yellow"
    }
  ],
  "blockers": [
    {
      "id": "b1",
      "description": "SEO tool access delayed",
      "impact": "medium",
      "age_days": 5,
      "owner": "Alice",
      "status": "in_progress"
    }
  ],
  "recent_activity": [
    "Optimized 7 of 10 target posts",
    "Fixed 3 broken links",
    "Improved mobile load time by 15%"
  ]
}
```

## Trend Analysis

### Progress Over Time Chart

```
Week 1:  15% ███░░░░░░░░░░░░░░░░░
Week 2:  28% █████░░░░░░░░░░░░░░░
Week 3:  45% █████████░░░░░░░░░░░
Week 4:  62% ████████████░░░░░░░░

Linear trend: +15.67% per week (good acceleration)
```

### Cumulative Flow

```
Week:    1    2    3    4    5    6
--------|----|----|----|----|----|----|
Done    | 15 | 28 | 45 | 62 | 78 | 95 |
Current | 10 | 17 | 15 | 13 | 12 |  5 |
Planned |  0 |  0 |  0 |  5 | 10 | 15 |
Total   | 25 | 45 | 60 | 80 |100 |115 |

Interpretation:
- Scope increased week 4 (total jumped)
- Completion rate steady
- On track to finish week 6
```

## Health Signals

### Early Warning Indicators

**Velocity Declining for 2+ Weeks**:
```
Week 1: 10%
Week 2: 8%
Week 3: 6%
Week 4: 4%

Trend: ↓↓ Concerning
Action: Conduct review, identify root cause
```

**Blocker Age Increasing**:
```
Open blockers >7 days: 3
Open blockers >14 days: 1

Trend: Blockers not resolving
Action: Escalate stuck blockers
```

**Milestone Duration Overrun >20%**:
```
Milestone: "Build API" (planned 2 weeks)
Elapsed: 2.5 weeks
Progress: 70%

Overrun: 25% and still not done
Action: Assess if completion realistic, consider pivot
```

### Positive Indicators

**Velocity Increasing**:
```
Week 1-2: 6% avg
Week 3-4: 9% avg

Trend: ↑ Improving
Action: Understand what's working, sustain it
```

**Blockers Resolving Quickly**:
```
Average blocker age: 2.5 days
Blockers resolved: 8/10

Trend: Good problem-solving
Action: Continue current approach
```

**Milestones Completing Early**:
```
M1: -2 days (early)
M2: -1 day (early)

Trend: Ahead of schedule
Action: Can we accelerate remaining milestones?
```

## Quick Reference

### Status at a Glance

```bash
# Quick check command
check_status() {
    PROGRESS=$(get_progress)
    EXPECTED=$(get_expected_progress)
    VARIANCE=$(calculate_variance)

    if [ $VARIANCE -ge 90 ]; then
        echo "🟢 On Track ($PROGRESS% complete)"
    elif [ $VARIANCE -ge 70 ]; then
        echo "🟡 At Risk ($PROGRESS% complete, ${VARIANCE}% of expected)"
    else
        echo "🔴 Off Track ($PROGRESS% complete, ${VARIANCE}% of expected)"
    fi
}
```

### Update Template

```bash
# Quick update format
@progress-tracker "[goal-id] M2 completed 75%, finished tasks A,B,C, blocked on API access"

Parsed:
- Milestone: M2
- Progress: 75%
- Activities: finished tasks A,B,C
- Blocker: blocked on API access
```

## Usage Guidelines

1. **Update frequently** - Weekly minimum, daily for fast-paced goals
2. **Keep it simple** - Track essential metrics only
3. **Be honest** - Accurate tracking enables good decisions
4. **Flag early** - Don't wait for red status to raise concerns
5. **Celebrate wins** - Note milestones completed, progress made
6. **Archive history** - Keep snapshots for trend analysis
7. **Make it visual** - Progress bars > numbers alone
8. **Review regularly** - Dashboard is input to reviews
9. **Act on signals** - Tracking without action is waste

This skill should be read before setting up or updating progress tracking for any goal.
