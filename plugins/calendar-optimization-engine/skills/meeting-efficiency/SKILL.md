# Meeting Efficiency Skill

**Expert patterns for meeting value assessment, optimization frameworks, and efficiency improvement**

## Core Principles

1. **Value First**: Every meeting must justify its time investment
2. **Async by Default**: Meeting only when necessary, email/doc when possible
3. **Right People**: Only required attendees, make others optional
4. **Right Duration**: 25/50 minute rule (not 30/60)
5. **Continuous Audit**: Review recurring meetings quarterly

---

## Meeting Value Framework

### Value Assessment Dimensions

**5-Point Scoring System** (1-10 scale per dimension):

1. **Decision Impact**: Does meeting make important decisions?
2. **Action Items**: Does it produce clear next steps?
3. **Participant Necessity**: Are all attendees required?
4. **Time Efficiency**: Is duration appropriate?
5. **Async Alternative**: Could this be email/doc?

**Overall Score = Average of 5 dimensions**

**Value Categories**:
- **High Value (8-10)**: Keep and optimize
- **Medium Value (5-7)**: Optimize or reduce frequency
- **Low Value (1-4)**: Eliminate or make async

### Heuristic-Based Quick Scoring

When full analysis unavailable, use metadata heuristics:

```python
def quick_value_score(meeting):
    """
    Estimate value from meeting metadata.

    Positive signals (+):
    - 1:1 meetings (+2)
    - Has agenda (+1)
    - Small group <=5 (+1)
    - Decision-making type (+2)
    - Client facing (+1)

    Negative signals (-):
    - Large group >10 (-2)
    - Duration >60 min (-1)
    - "FYI" in title (-2)
    - No agenda, recurring (-1)
    - "Status" or "Sync" (-1)
    """
    score = 5  # Neutral start

    # Apply heuristics...
    return max(1, min(10, score))
```

---

## Meeting Type Analysis

### Meetings to KEEP (High Value)

**Decision-Making Meetings**:
- Strategic planning
- Budget allocation
- Product roadmap
- Hiring decisions
- Architecture decisions

**1:1 Meetings**:
- Manager <> Direct report
- Mentor <> Mentee
- Cross-functional partnerships
- Career development

**Client/External Meetings**:
- Sales calls
- Client check-ins
- Partner collaborations
- User research sessions

**Creative Collaboration**:
- Brainstorming
- Design reviews
- Whiteboarding sessions
- Problem-solving workshops

### Meetings to OPTIMIZE (Medium Value)

**Team Syncs**:
- **Current**: 60 min weekly
- **Optimized**: 25-30 min with strict agenda
- **Alternative**: Async standup in Slack

**Planning Meetings**:
- **Current**: 90 min sprint planning
- **Optimized**: 50 min with pre-work
- **Pre-work**: Review proposals before meeting

**Reviews/Demos**:
- **Current**: 60 min with full team
- **Optimized**: 25 min with required attendees only
- **Recording**: Share for others to watch async

### Meetings to ELIMINATE (Low Value)

**FYI Meetings**:
- **Why**: One-way information flow
- **Alternative**: Email summary or doc
- **Time Saved**: 100%

**Status Update Meetings**:
- **Why**: Could be async
- **Alternative**: Written status in shared doc
- **Time Saved**: 100%

**Recurring Meetings Without Purpose**:
- **Why**: Purpose drift over time
- **Alternative**: Cancel until needed again
- **Time Saved**: 100%

**Meetings With Too Many Attendees**:
- **Why**: Most people passive observers
- **Alternative**: Reduce to required attendees, share notes
- **Time Saved**: 50-80%

---

## Recurring Meeting Audit

### Audit Checklist

For each recurring meeting, evaluate:

- [ ] **Still Relevant?**: Does original purpose still apply?
- [ ] **Right Frequency?**: Could be less frequent?
- [ ] **Right Duration?**: Could be shorter?
- [ ] **Right Attendees?**: All still necessary?
- [ ] **Has Agenda?**: Clear structure each time?
- [ ] **Produces Action Items?**: Clear outcomes?
- [ ] **Could Be Async?**: Email/doc instead?

### Red Flags

**High-Cost Meetings** (Person-Hours/Week):
```python
def calculate_meeting_cost(meeting):
    """
    Calculate total person-hours per week.

    Example:
    - 60-min weekly meeting
    - 8 attendees
    - Cost = 1 hour × 8 people × 1/week = 8 person-hours/week
    - Annual cost = 8 × 52 = 416 person-hours/year
    """
    duration_hours = meeting['duration_minutes'] / 60
    attendees = len(meeting['attendees'])
    frequency = meetings_per_week(meeting['recurrence'])

    weekly_cost = duration_hours * attendees * frequency

    return {
        'weekly': weekly_cost,
        'monthly': weekly_cost * 4,
        'annual': weekly_cost * 52
    }
```

**Warning Thresholds**:
- >10 person-hours/week: High cost, audit carefully
- >20 person-hours/week: Very expensive, strong justification needed
- >50 person-hours/week: Critical, likely needs restructuring

### Optimization Actions

**Reduce Frequency**:
- Weekly → Biweekly (50% time saving)
- Daily → 3×/week (40% time saving)
- Biweekly → Monthly (50% time saving)

**Reduce Duration**:
- 60 min → 50 min (17% time saving)
- 30 min → 25 min (17% time saving)
- 90 min → 60 min or 2×45 min (33% time saving)

**Reduce Attendees**:
- Make non-essential attendees optional
- Share recording/notes instead
- Time saving = (removed attendees / total) × 100%

---

## Attendee Optimization

### Attendee Categories

**Required**:
- Decision makers
- Subject matter experts
- Action item owners
- Directly impacted stakeholders

**Optional**:
- "FYI" stakeholders (send notes instead)
- Adjacent teams (only if discussion relevant)
- Observers (watch recording)

**Unnecessary**:
- Added "for visibility" (email them)
- Rarely attend (remove from invite)
- No participation (not engaged)

### Optimization Formula

```
Optimal Attendees = Decision Makers + SMEs + Action Owners
```

**Rule of Thumb**:
- ≤5 attendees: Optimal (productive discussion)
- 6-8 attendees: Acceptable (watch for passive attendees)
- 9-15 attendees: Large (likely some unnecessary)
- >15 attendees: Too large (restructure or make optional for most)

---

## Duration Optimization

### The 25/50 Minute Rule

**Principle**: Default to 25 or 50-minute meetings instead of 30/60

**Benefits**:
- Built-in 5-10 minute buffer
- Forces conciseness
- Prevents Parkinson's Law (work expands to fill time)
- Allows back-to-back with breathing room

**Recommended Durations**:
- Quick sync: 15 minutes
- Standard meeting: 25 minutes
- Deep discussion: 50 minutes
- Workshop/planning: 90 minutes max (or split into two sessions)

### Meeting Duration Guide

| Meeting Type | Recommended | Current Average | Time Saved |
|--------------|-------------|----------------|------------|
| Standup | 15 min | 30 min | 50% |
| 1:1 | 25-50 min | 60 min | 17-58% |
| Team Sync | 25 min | 60 min | 58% |
| Planning | 50 min | 90 min | 44% |
| Review | 25 min | 45 min | 44% |
| Workshop | 90 min | 120 min | 25% |

---

## Async Alternatives

### When to Make Async

**High Async Viability** (Use email/doc):
- Information sharing (announcements, updates)
- Status reports (project updates, metrics)
- FYI meetings (no discussion needed)
- Decision ratification (already decided, just informing)
- Documentation review (can read on own time)

**Medium Async Viability** (Try async first):
- Simple Q&A (can use Slack/email)
- Small updates (quick Loom video)
- Routine check-ins (written update)
- Progress reviews (dashboard/doc)

**Low Async Viability** (Keep as meeting):
- Complex problem solving
- Brainstorming/ideation
- Sensitive topics (layoffs, feedback)
- Negotiation/conflict resolution
- Relationship building (especially new relationships)

### Async Tools & Formats

**Email**:
- Announcements
- Weekly updates
- Simple decisions

**Shared Documents**:
- Status reports
- Project plans
- Meeting notes

**Slack/Chat**:
- Quick questions
- Brief updates
- Informal check-ins

**Video (Loom/Async)**:
- Demos
- Presentations
- Walkthroughs
- Training

**Dashboards**:
- Metrics review
- Progress tracking
- KPI monitoring

---

## ROI Calculation

### Meeting ROI Formula

```
ROI = (Value Generated) / (Time Invested)

Where:
  Value = Decisions made + Actions spawned + Problems solved
  Time = (Duration × Attendees) + Prep time + Follow-up time

High ROI: >2 (value > 2× time invested)
Medium ROI: 1-2 (value ≈ time invested)
Low ROI: <1 (time > value generated)
```

### Time Savings Calculator

```python
def calculate_time_savings(optimizations):
    """
    Calculate total time savings from optimizations.

    Example:
    - Eliminate 3 meetings (6 hours/week)
    - Reduce 5 meetings by 30% (4 hours/week)
    - Make 2 meetings async (2 hours/week)
    - Total: 12 hours/week = 48 hours/month = 576 hours/year
    """
    weekly_savings = 0

    for opt in optimizations:
        if opt['action'] == 'eliminate':
            weekly_savings += opt['hours_per_week']
        elif opt['action'] == 'reduce_duration':
            weekly_savings += opt['hours_per_week'] * opt['reduction_percentage']
        elif opt['action'] == 'async':
            weekly_savings += opt['hours_per_week']
        elif opt['action'] == 'reduce_attendees':
            weekly_savings += opt['hours_per_week'] * (opt['removed_attendees'] / opt['total_attendees'])

    return {
        'weekly': weekly_savings,
        'monthly': weekly_savings * 4,
        'annual': weekly_savings * 52,
        'work_days_annual': weekly_savings * 52 / 8
    }
```

---

## Meeting Best Practices

### Before the Meeting

- [ ] **Clear objective**: Know what success looks like
- [ ] **Agenda shared**: At least 24 hours in advance
- [ ] **Right attendees**: Only required people invited
- [ ] **Pre-work assigned**: Read materials beforehand
- [ ] **Duration appropriate**: As short as possible

### During the Meeting

- [ ] **Start on time**: Don't wait for latecomers
- [ ] **Follow agenda**: Stay on track
- [ ] **Designate note-taker**: Capture decisions/actions
- [ ] **Time-box discussions**: Move on after time limit
- [ ] **End with action items**: Who does what by when
- [ ] **End early if done**: Don't fill time

### After the Meeting

- [ ] **Send notes**: Within 24 hours
- [ ] **Action items clear**: Assignee + deadline
- [ ] **Decisions documented**: What was decided and why
- [ ] **Follow up**: Track action item completion

---

## Quality Metrics

### Meeting Health Metrics

**Meeting Load**:
- Target: <50% of time in meetings
- Good: 30-50%
- Excessive: >50%

**Meeting Value**:
- Target: Average value score >7
- Good: 6-7
- Poor: <6

**Action Item Ratio**:
- Target: >2 actions per meeting
- Good: 1-2 actions
- Poor: <1 action

**Attendee Engagement**:
- Target: >80% actively participate
- Good: 60-80%
- Poor: <60%

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: Meeting optimization, calendar efficiency, time management
