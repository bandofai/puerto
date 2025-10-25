# Time Blocking Skill

**Expert patterns for energy-based scheduling, focus time protection, and calendar defragmentation**

## Core Principles

1. **Energy Alignment**: Schedule tasks during optimal energy levels
2. **Deep Work First**: Protect morning hours for complex work
3. **Meeting Batching**: Group meetings into designated windows
4. **Context Preservation**: Minimize task switching
5. **Ruthless Protection**: Defend focus blocks like external meetings

---

## Energy-Based Scheduling

### The Daily Energy Curve

**Typical Knowledge Worker Energy Pattern**:

```
Peak Energy (8am-12pm):
- Highest cognitive capacity
- Best for: Complex problem solving, creative work, learning
- Protect for: Deep work, strategic thinking, writing, coding

Medium Energy (1pm-3pm):
- Good collaborative capacity
- Best for: Meetings, discussions, teamwork
- Schedule: 1:1s, team syncs, client calls

Lower Energy (3pm-5pm):
- Declining focus
- Best for: Administrative tasks, routine work
- Schedule: Email, filing, planning, organizing
```

### Task-Energy Matching

| Task Type | Energy Required | Optimal Time | Duration |
|-----------|----------------|--------------|----------|
| Creative work | High | 8-10am | 2-4 hours |
| Complex analysis | High | 8-12pm | 1-3 hours |
| Strategic planning | High | 9-11am | 1-2 hours |
| Learning | High | 8-10am | 1-2 hours |
| Collaborative meetings | Medium | 1-3pm | 25-50 min |
| 1:1s | Medium | 10-12pm or 1-3pm | 25-50 min |
| Admin tasks | Low | 3-5pm | 30-60 min |
| Email processing | Low | 3-4pm or 4-5pm | 30 min |

---

## Deep Work Blocks

### Creating Focus Blocks

**Minimum Viable Focus Block**: 2 hours

**Why 2 hours minimum?**
- 15-20 min: Warm-up/context loading
- 60-90 min: Productive deep work
- 10 min: Wind-down/document progress
- **Total**: 90-120 minutes of actual deep work

**Optimal Schedule**:
- **Daily**: 2-hour morning block (8-10am)
- **3×/week**: Extended 4-hour block (8am-12pm)
- **Weekly total**: 15-20 hours deep work

### Focus Block Template

```markdown
Deep Work Block Structure:

8:00-8:10   Setup & Prep
            - Close email/Slack
            - Set DND on phone
            - Review task plan
            - Gather materials

8:10-9:40   Deep Work Session 1
            - Single task focus
            - No interruptions
            - No checking email
            - Pomodoro: 25 work / 5 break (optional)

9:40-9:50   Break
            - Stand/stretch
            - Hydrate
            - Eyes off screen
            - NO email/Slack

9:50-10:00  Wind-down
            - Document progress
            - Note next steps
            - Update task status
            - Plan next session
```

### Protection Strategies

**Calendar Blocking**:
```
Title: "Deep Work - Do Not Schedule"
Show as: Busy
Color: Blue (visual distinction)
Recurring: Daily, 8-10am
Reminder: 10 minutes before
```

**Communication**:
```
Slack Status: "🔵 Focus time - back at 10am"
Email Auto-reply: "In focus time, will respond after 10am"
Team Agreement: "No meetings 8-10am unless emergency"
```

**Enforcement**:
- Decline all meeting requests during focus blocks
- No exceptions (treat like external client meeting)
- Reschedule recurring meetings if they conflict
- Communicate boundaries clearly to team

---

## Meeting Batching

### Meeting Window Strategy

**Principle**: Group meetings into specific time windows to preserve continuous focus blocks

**Standard Meeting Windows**:

```
Monday:
  10:00-12:00  Meeting Window 1
  2:00-4:00    Meeting Window 2

Tuesday:
  10:00-12:00  Meeting Window 1
  2:00-4:00    Meeting Window 2

Wednesday:
  2:00-4:00    Meeting Window (Deep work day!)

Thursday:
  10:00-12:00  Meeting Window 1
  2:00-4:00    Meeting Window 2

Friday:
  10:00-11:30  Meeting Window (Light Friday)
```

### Benefits of Batching

**Preserves Focus Time**:
- 8-10am: Protected deep work (daily)
- 10-12pm: Available for meetings OR deep work
- Creates predictable schedule

**Reduces Context Switching**:
- "Meeting mode" for 2-4 hours
- "Deep work mode" for 2-4 hours
- Not switching every 30 minutes

**Energy Alignment**:
- Morning meetings (10-12pm): Strategic discussions
- Afternoon meetings (2-4pm): Collaborative work
- Respects natural energy curve

---

## Calendar Defragmentation

### Fragmentation Assessment

**Fragmentation Score** (0-10):

```python
def calculate_fragmentation(calendar):
    """
    0 = Highly fragmented (no blocks >1 hour)
    10 = Well-structured (multiple 2+ hour blocks)
    """
    score = 0

    # Count continuous blocks
    blocks_2h = count_blocks(calendar, min_duration=120)
    blocks_1h = count_blocks(calendar, min_duration=60)

    # Reward long blocks
    score += min(5, blocks_2h * 1.5)  # Max 5 points
    score += min(3, blocks_1h * 0.5)  # Max 3 points

    # Penalize short gaps
    short_gaps = count_gaps_under(calendar, minutes=30)
    score -= min(3, short_gaps * 0.3)  # Max -3 points

    # Bonus for meeting clustering
    if meetings_are_clustered(calendar):
        score += 2

    return max(0, min(10, score))
```

### Defragmentation Techniques

**Technique 1: Meeting Consolidation**
```
Before (Fragmented):
8am   [Free]
9am   [Meeting A]    ← Isolated
10am  [Free]
11am  [Free]
12pm  [Lunch]
1pm   [Free]
2pm   [Meeting B]    ← Isolated
3pm   [Free]
4pm   [Meeting C]    ← Isolated

After (Defragmented):
8am   [Deep Work]    ← 2-hour block
9am   [Deep Work]
10am  [Meeting A]    ← Batched together
11am  [Meeting B]
12pm  [Lunch]
1pm   [Meeting C]    ← Close to others
2pm   [Deep Work]    ← 2-hour block
3pm   [Deep Work]
4pm   [Admin]
```

**Technique 2: Buffer Elimination**
```
Before:
10:00-10:30  Meeting A
10:30-11:00  [30 min gap] ← Useless time
11:00-11:30  Meeting B

After:
10:00-10:25  Meeting A (shortened)
10:25-10:35  [10 min buffer] ← Just enough
10:35-11:00  Meeting B (shortened)
11:00-12:00  [1 hour freed] ← Useful block
```

**Technique 3: Theme Days**
```
Monday: Planning & Strategy
  - Strategic planning
  - Essential planning meetings
  - Set weekly priorities

Tuesday: Execution & Meetings
  - Implementation work
  - Team collaboration
  - 1:1s scheduled

Wednesday: Deep Work Day
  - Maximize focus time (6+ hours)
  - Minimize meetings (1-2 max)
  - Complex problem solving

Thursday: Communication & External
  - Client calls
  - Cross-team meetings
  - Stakeholder sync

Friday: Wrap-up & Learning
  - Week review
  - Learning time
  - Process improvements
  - Planning next week
```

---

## Ideal Schedule Templates

### Individual Contributor Schedule

```markdown
Monday: Planning & Strategy
8:00-10:00   Deep Work (planning, strategy)
10:00-10:15  Break
10:15-12:00  Deep Work (implementation)
12:00-1:00   Lunch
1:00-3:00    Meeting Window (team syncs)
3:00-5:00    Admin & Planning

Tuesday: Execution & Collaboration
8:00-10:00   Deep Work (coding, writing)
10:00-10:15  Break
10:15-12:00  Meeting Window (1:1s)
12:00-1:00   Lunch
1:00-3:00    Deep Work (continued)
3:00-5:00    Email & Communication

Wednesday: Deep Work Day
8:00-12:00   Extended Deep Work
12:00-1:00   Lunch
1:00-2:00    Meeting Window (essential only)
2:00-4:00    Deep Work
4:00-5:00    Admin

Thursday: Meetings & Collaboration
8:00-10:00   Deep Work
10:00-12:00  Meeting Window
12:00-1:00   Lunch
1:00-3:00    Meeting Window
3:00-5:00    Follow-up & Actions

Friday: Wrap-up & Learning
8:00-10:00   Deep Work (finish tasks)
10:00-11:30  Meeting Window (light)
11:30-1:00   Lunch (extended)
1:00-3:00    Learning & Development
3:00-4:00    Week Review
4:00-5:00    Next Week Planning

Weekly Totals:
  Deep Work: 20 hours (50%)
  Meetings: 12 hours (30%)
  Admin/Learning: 8 hours (20%)
```

### Manager Schedule

```markdown
Monday: Planning & Team
8:00-10:00   Deep Work (strategy, planning)
10:00-12:00  1:1s (3× 25-min + buffers)
12:00-1:00   Lunch
1:00-3:00    Team Meeting + Planning
3:00-5:00    Admin & Email

Tuesday: Individual Work
8:00-10:00   Deep Work (strategic projects)
10:00-12:00  Deep Work (continued)
12:00-1:00   Lunch
1:00-3:00    Meeting Window
3:00-5:00    Email & Follow-ups

Wednesday: Deep Work Focus
8:00-12:00   Extended Deep Work
12:00-1:00   Lunch
1:00-2:00    1:1 (critical only)
2:00-4:00    Deep Work
4:00-5:00    Team Office Hours

Thursday: External & Cross-Team
8:00-10:00   Deep Work
10:00-12:00  Cross-team Meetings
12:00-1:00   Lunch
1:00-3:00    1:1s (3× 25-min + buffers)
3:00-5:00    Stakeholder Sync

Friday: Review & People Development
8:00-10:00   Deep Work (week wrap-up)
10:00-11:00  Skip-level 1:1 / Mentoring
11:00-12:00  Team Recognition / Planning
12:00-1:00   Lunch
1:00-3:00    Learning / Professional Development
3:00-4:00    Week Review
4:00-5:00    Next Week Preparation

Weekly Totals:
  Deep Work: 15 hours (37%)
  1:1s/People: 10 hours (25%)
  Meetings: 10 hours (25%)
  Admin: 5 hours (13%)
```

---

## Context Switching Minimization

### The Switching Tax

**Cost of Context Switching**:
- 15-20 minutes to fully context switch
- 23 minutes to regain deep focus after interruption
- 40% productivity loss with frequent switching

**Example**:
```
Fragmented Schedule (high switching):
8:00  Email (15 min)
8:15  Coding (45 min)
9:00  Meeting (30 min)
9:30  Email (15 min)
9:45  Coding (45 min)
10:30 Meeting (30 min)

Result: 6 context switches, ~90 min lost to switching = 50% productive time

Batched Schedule (low switching):
8:00  Deep Work - Coding (2 hours)
10:00 Meeting Block (1 hour)
11:00 Deep Work - Coding (1 hour)

Result: 2 context switches, ~30 min lost to switching = 87% productive time
```

### Strategies to Reduce Switching

**1. Time Blocking by Task Type**:
- Batch similar tasks together
- "Email time" vs "Meeting time" vs "Deep work time"

**2. Single-Tasking**:
- One browser tab at a time
- Close email/Slack during focus blocks
- Complete one task before starting next

**3. Transition Rituals**:
- 5-minute transition between major shifts
- Standup/stretch between meetings
- Clear desk before focus block

---

## Implementation Guide

### Week 1: Foundation
- [ ] Block morning focus time (8-10am daily)
- [ ] Set Slack status during focus blocks
- [ ] Communicate schedule to team

### Week 2: Meeting Optimization
- [ ] Identify meeting windows
- [ ] Reschedule meetings to windows
- [ ] Add 15-min buffers

### Week 3: Defragmentation
- [ ] Batch scattered meetings
- [ ] Consolidate admin time
- [ ] Create theme days

### Week 4: Refinement
- [ ] Measure fragmentation score
- [ ] Adjust based on results
- [ ] Make permanent

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: Schedule optimization, productivity maximization, focus protection
