# Spaced Repetition Skill

**Evidence-based scheduling for optimal knowledge retention using proven algorithms**

This skill codifies the science of memory and forgetting, including the SM-2 algorithm, Leitner system, optimal review intervals, and the spacing effect.

---

## Core Principle

**The Spacing Effect**: Information reviewed at increasing intervals is retained far better than information reviewed all at once (massed practice).

**Research**: Spaced repetition improves long-term retention by 200-300% compared to cramming.

---

## The Forgetting Curve

### Ebbinghaus Discovery (1885)

Without review, we forget information at a predictable rate:

```
100% ─┐
      │
 80%  │ ╲
      │  ╲
 60%  │   ╲___
      │       ╲___
 40%  │           ╲___
      │               ╲___
 20%  │                   ╲___
      │                       ╲___
  0%  └────────────────────────────╲___
      1h   1d    1w    1m    6m    1y

Retention without review
```

**Key Points**:
- 50% forgotten within 1 hour without review
- 70% forgotten within 24 hours
- 90% forgotten within 1 week
- Steepest drop in first 24 hours

### Combating Forgetting with Reviews

Each successful review:
1. Resets the forgetting curve (back to ~100%)
2. Makes the curve less steep (forget slower)
3. Allows longer interval before next review

```
100% ─┐ Review    Review      Review
      │   ↑         ↑           ↑
 80%  │ ╲ │       ╲ │         ╲ │
      │  ╲│        ╲│          ╲│
 60%  │   ╲___     ╲│___       ╲│___
      │       ╲___  ╲│   ╲___   ╲│
 40%  │           ╲_╲│       ╲___╲│___
      │             ╲│           ╲│
 20%  │              ╲│___        ╲│___
      │               ╲│           ╲│
  0%  └────────────────╲│___________╲│___
      1d   3d    7d    14d   30d   60d

Multiple spaced reviews flatten the curve
```

---

## SM-2 Algorithm (SuperMemo 2)

### Overview

The **most widely used** spaced repetition algorithm (Anki, SuperMemo, many apps use variants).

**Core Idea**: Each item has an interval that increases after successful recall. The easier you find it, the longer until next review.

### Algorithm Components

**1. Easiness Factor (EF)**
- Represents how easy an item is to remember
- Range: 1.3 to 2.5
- Higher = easier = longer intervals

**2. Interval (I)**
- Days until next review
- Increases with each successful review

**3. Quality of Recall (Q)**
- Self-rated after each review
- Scale: 0-5

**Quality Scale**:
```
5 - Perfect recall, instant
4 - Correct recall after slight hesitation
3 - Correct recall with difficulty
2 - Incorrect, but upon seeing answer it felt familiar
1 - Incorrect, answer seemed vaguely familiar
0 - Complete blackout, no recall
```

### SM-2 Formula

**Initial Learning**:
- Interval 1: 1 day
- Interval 2: 6 days

**Subsequent Intervals**:
```
If Quality >= 3 (Passed):
    New Interval = Old Interval × Easiness Factor

If Quality < 3 (Failed):
    Reset Interval = 1 day
    (Learn again from scratch)
```

**Easiness Factor Adjustment**:
```
New EF = Old EF + (0.1 - (5 - Quality) × (0.08 + (5 - Quality) × 0.02))
```

Simplified understanding:
- Quality 5 → EF increases (item getting easier)
- Quality 4 → EF stays about the same
- Quality 3 → EF decreases slightly (item getting harder)
- Quality 0-2 → EF decreases more (item is difficult)

### SM-2 Example

**Day 0: Learn "JavaScript closure"**
- Initial EF: 2.5
- Next review: Day 1

**Day 1: Review**
- Quality: 4 (correct with slight hesitation)
- EF: 2.5 (stays about same)
- Interval: 6 days
- Next review: Day 7

**Day 7: Review**
- Quality: 5 (perfect recall)
- EF: 2.6 (increased)
- Interval: 6 × 2.6 = 15.6 days ≈ 16 days
- Next review: Day 23

**Day 23: Review**
- Quality: 3 (correct but difficult)
- EF: 2.36 (decreased)
- Interval: 16 × 2.36 = 37.8 days ≈ 38 days
- Next review: Day 61

**Day 61: Review**
- Quality: 1 (failed, forgot)
- EF: 1.96 (decreased significantly)
- Interval: RESET to 1 day (re-learn)
- Next review: Day 62

### Implementation in Learning Schedule

```markdown
## Spaced Repetition Tracking

### Concepts to Review

| Concept | Learned | Last Review | Quality | Next Review | Interval |
|---------|---------|-------------|---------|-------------|----------|
| JavaScript closures | Jan 1 | Jan 23 | 3 | Jan 61 | 38 days |
| React hooks | Jan 3 | Jan 10 | 5 | Jan 27 | 17 days |
| SQL joins | Jan 5 | Jan 6 | 2 | Jan 7 | 1 day |

### Today's Reviews (Jan 7)

- [ ] SQL joins (struggled yesterday, re-learning)

### This Week's Reviews

- Monday Jan 7: SQL joins
- Tuesday Jan 8: (SQL joins again if Quality < 3)
- Friday Jan 10: JavaScript closures (maybe, if falls within week)
```

---

## Leitner System

### Overview

A **simpler alternative** to SM-2, using physical or virtual "boxes".

**Concept**: Items move between boxes based on recall success. Each box has a different review frequency.

### Box Structure

```
Box 1: Daily (New items and failed recalls)
Box 2: Every 3 days
Box 3: Weekly
Box 4: Bi-weekly
Box 5: Monthly (Mastered)
```

### Rules

**Successful recall**: Move item to next box (longer interval)
**Failed recall**: Move item back to Box 1 (daily review)

### Example Flow

**Day 0**: Learn "JavaScript closures" → Box 1

**Day 1** (Box 1 review):
- Recall successfully → Move to Box 2
- Next review: Day 4

**Day 4** (Box 2 review):
- Recall successfully → Move to Box 3
- Next review: Day 11

**Day 11** (Box 3 review):
- Fail to recall → Move back to Box 1
- Next review: Day 12

**Day 12** (Box 1 review):
- Recall successfully → Move to Box 2
- Next review: Day 15

Eventually reaches Box 5 (monthly review) = Mastered

### Leitner Implementation

```markdown
## Leitner Box System

### Box 1: Daily Review (New/Struggling)
- JavaScript closures
- SQL joins
- React useEffect hook

**Review Schedule**: Every day
**Count**: 3 items

### Box 2: Every 3 Days
- HTML semantic elements
- CSS flexbox
- Git branching

**Review Schedule**: Days 1, 4, 7, 10, 13...
**Count**: 3 items

### Box 3: Weekly
- JavaScript arrays
- React props
- HTTP methods

**Review Schedule**: Weeks 1, 2, 3, 4...
**Count**: 3 items

### Box 4: Bi-weekly
- CSS selectors
- JavaScript functions
- npm basics

**Review Schedule**: Weeks 1, 3, 5, 7...
**Count**: 3 items

### Box 5: Monthly (Mastered)
- HTML basics
- CSS basics
- Git basics

**Review Schedule**: Months 1, 2, 3...
**Count**: 3 items

### Daily Task: Review Box 1 + any box scheduled for today
```

---

## Optimal Review Intervals

### Research-Based Intervals

**Standard progression** (works for most learners):

```
Review 1: 1 day after learning
Review 2: 3 days after Review 1
Review 3: 7 days after Review 2
Review 4: 14 days after Review 3
Review 5: 30 days after Review 4
Review 6: 60 days after Review 5
Review 7: 6 months after Review 6
```

### Adjusting Intervals

**For easier material** (Quality consistently 5):
- Accelerate: 1d → 7d → 30d → 90d

**For harder material** (Quality consistently 3):
- Decelerate: 1d → 2d → 4d → 7d → 14d → 21d → 30d

**For critical material** (must not forget):
- More frequent: 1d → 3d → 7d → 10d → 14d → 21d → 30d

---

## Interleaving with Spaced Repetition

### The Problem with Blocking

**Blocked Practice**:
```
Week 1: Learn Arrays (all week)
Week 2: Learn Linked Lists (all week)
Week 3: Learn Trees (all week)
```

**Result**: Poor long-term retention, difficulty distinguishing concepts

### Interleaved + Spaced Practice

**Better Approach**:
```
Week 1:
- Monday: Learn Arrays
- Tuesday: Review Arrays (Day 1), Learn Linked Lists
- Wednesday: Learn Linked Lists continued
- Thursday: Review Arrays (Day 3), Review Linked Lists (Day 1)
- Friday: Review Linked Lists (Day 2), Learn Trees intro

Week 2:
- Monday: Review Arrays (Day 8), Review Linked Lists (Day 5), Learn Trees
- Tuesday: Review Trees (Day 1), Review Linked Lists (Day 6)
- Wednesday: Review Arrays (Day 10), Practice all three mixed
- Thursday: Review Trees (Day 3), mixed practice
- Friday: Mixed practice (all three)
```

**Result**: Better retention, better discrimination, better transfer

### Daily Schedule Template

```markdown
## Daily Study Plan

### New Material (60-70% of time)
- [Primary topic for today]

### Recent Reviews (20-25% of time)
- [Topics learned in past week - 1 day or 3 day reviews]

### Older Reviews (10-15% of time)
- [Topics from 1-4 weeks ago - 7 day, 14 day, or 30 day reviews]

### Example:
**Tuesday, Week 3**

New Material (90 min):
- React Hooks: useContext

Recent Reviews (30 min):
- React Hooks: useState (learned Monday - 1 day review)
- JavaScript async/await (learned last Thursday - 5 day review)

Older Reviews (15 min):
- JavaScript functions (learned Week 1 - 14 day review)
```

---

## Balancing New Material vs. Review

### The 70/30 Rule

**Optimal balance**:
- **70% of study time**: New material
- **30% of study time**: Review (spaced repetition)

**Why**: Ensures forward progress while maintaining retention

### As Content Accumulates

**Early weeks** (few topics to review):
- New: 80-90%
- Review: 10-20%

**Middle weeks** (moderate review load):
- New: 70%
- Review: 30%

**Later weeks** (many topics to maintain):
- New: 60%
- Review: 40%

**Final weeks** (mastery phase):
- New: 40%
- Review: 60%

### Managing Review Overload

**If review pile grows too large**:

1. **Prioritize**: Review most important/difficult topics first
2. **Batch**: Group similar items for efficient review
3. **Reduce new material**: Slow down new learning temporarily
4. **Extend intervals**: If retention is good, space out reviews more
5. **Archive**: Some topics may not need continued review

---

## Creating a Spaced Repetition Schedule

### Step 1: Identify All Concepts

List every concept/skill to be learned:

```
Phase 1 Concepts:
1. HTML semantic elements
2. CSS box model
3. CSS flexbox
4. CSS grid
5. JavaScript variables
6. JavaScript functions
7. JavaScript arrays
8. [etc.]
```

### Step 2: Assign Learning Dates

Based on curriculum sequence:

```
Week 1:
- Day 1: HTML semantic elements
- Day 2: CSS box model
- Day 3: CSS flexbox
- Day 4: CSS grid
- Day 5: JavaScript variables

Week 2:
- Day 1: JavaScript functions
- Day 2: JavaScript arrays
- [etc.]
```

### Step 3: Calculate Review Dates

For each concept, schedule reviews at 1, 3, 7, 14, 30-day intervals:

```
HTML semantic elements:
- Learned: Week 1, Day 1
- Review 1: Week 1, Day 2 (1 day later)
- Review 2: Week 1, Day 5 (3 days after Review 1)
- Review 3: Week 2, Day 5 (7 days after Review 2)
- Review 4: Week 4, Day 5 (14 days after Review 3)
- Review 5: Week 8, Day 5 (30 days after Review 4)
```

### Step 4: Build Daily Review Lists

Compile what needs review each day:

```markdown
## Week 2, Day 3

### New Material
- JavaScript objects

### Reviews Due Today
- CSS box model (3-day review from Week 1, Day 7)
- JavaScript variables (7-day review from Week 1, Day 5)

### Time Allocation
- New Material: 90 minutes
- Reviews: 30 minutes (15 min each)
- Total: 2 hours
```

### Step 5: Track and Adjust

After each review, adjust based on recall quality:

```
CSS box model review (Week 2, Day 3):
- Quality: 5 (perfect recall)
- Action: Keep next review at 14 days

JavaScript variables review (Week 2, Day 3):
- Quality: 2 (struggled, forgot)
- Action: Review again tomorrow (reset to 1 day)
```

---

## Active Recall Techniques

### Why Active Recall?

**Passive review** (re-reading notes): 30% retention
**Active recall** (testing yourself): 80% retention

**Always use active recall for reviews**

### Techniques

#### 1. Flashcards

**Front**: Question/prompt
**Back**: Answer

```
Front: What does Array.map() do in JavaScript?
Back: Creates a new array by applying a function to each element
      of the original array. Returns new array, doesn't modify original.

Example:
[1,2,3].map(x => x * 2) // [2,4,6]
```

#### 2. Blank-Sheet Recall

1. Start with blank paper
2. Write everything you remember about topic
3. Check against notes/resources
4. Identify what you forgot
5. Study those parts specifically

#### 3. Explain to Others (Feynman Technique)

1. Try explaining concept to imaginary beginner
2. Note where you struggle to explain
3. Study those areas
4. Try again until fluent

#### 4. Code from Scratch

1. Close all references
2. Implement concept from memory
3. Run and test
4. Check against solution
5. Note what you got wrong

#### 5. Self-Testing

Create quiz questions for yourself:

```markdown
## JavaScript Functions Self-Test

1. Write a function that returns the sum of two numbers
2. Convert this function to an arrow function
3. What's the difference between parameters and arguments?
4. Write a function with a default parameter
5. How do you return multiple values from a function?
```

---

## Preventing Burnout

### The Danger of Aggressive Scheduling

**Too much review** = burnout, giving up

**Warning signs**:
- Review sessions taking 2+ hours/day
- Feeling overwhelmed by review pile
- Dreading study sessions
- Declining motivation

### Sustainable Review Load

**Beginner**: Max 30 min/day review
**Intermediate**: Max 45 min/day review
**Advanced**: Max 60 min/day review

**If exceeding limits**:
1. **Slow down new material**: Learn fewer new concepts
2. **Extend intervals**: If retention is good, review less frequently
3. **Archive old material**: Some concepts don't need infinite review
4. **Focus on weak areas**: Don't over-review what you know well

---

## Measuring Retention Success

### Metrics to Track

**Retention Rate**:
```
Retention Rate = (Successful Reviews / Total Reviews) × 100%

Target: 80-85%
- Below 70%: Intervals too long, review more frequently
- Above 90%: Intervals too short, can extend further
```

**Review Load**:
```
Daily Review Time / Total Study Time

Target: 25-30%
- Below 20%: May forget too much long-term
- Above 40%: Slowing down progress too much
```

**Time to Mastery**:
```
Days from initial learning to Box 5 (monthly review)

Typical: 60-90 days for well-learned concept
```

---

## Common Mistakes

### ❌ Cramming Before Tests

**Problem**: All-night study session before exam
**Why it fails**: Short-term memory only, forgotten within days
**Solution**: Distributed practice over weeks with spaced reviews

### ❌ Never Reviewing

**Problem**: Learn once, move on, never look back
**Why it fails**: 90% forgotten within weeks
**Solution**: Schedule reviews at 1, 3, 7, 14, 30-day intervals

### ❌ Reviewing Too Soon

**Problem**: Review same material multiple times in one day
**Why it fails**: Not challenging memory (desirable difficulty)
**Solution**: Wait at least until next day for first review

### ❌ Passive Review

**Problem**: Re-reading notes without testing
**Why it fails**: Recognition ≠ Recall
**Solution**: Always use active recall (test yourself)

### ❌ Same Interval for Everything

**Problem**: Review all topics weekly regardless of difficulty
**Why it fails**: Wastes time on easy topics, neglects hard ones
**Solution**: Adjust intervals based on recall quality

---

## Integration with Learning Plan

### When Creating Schedule

1. **Identify all concepts** in curriculum
2. **Assign learning dates** based on prerequisite sequence
3. **Calculate review dates** for each concept
4. **Build daily task lists** combining new + recent + old reviews
5. **Allocate time**: 70% new, 30% review
6. **Track quality** and adjust intervals

### Example Week Structure

```markdown
## Week 3 Schedule

### Monday
- New: React components (90 min)
- Review: JavaScript functions (from Week 1 - 14 day) (15 min)
- Review: CSS grid (from Week 2 - 7 day) (15 min)

### Tuesday
- New: React props (90 min)
- Review: React components (from yesterday - 1 day) (10 min)
- Review: JavaScript arrays (from Week 1 - 14 day) (15 min)

### Wednesday
- New: React state (90 min)
- Review: React props (from yesterday - 1 day) (10 min)
- Review: CSS flexbox (from Week 1 - 14 day) (15 min)

[Continue pattern...]

### Weekend
- Project: Build app using Week 1-3 concepts (3 hours)
- Mixed review: All concepts (30 min)
```

---

## Tools and Tracking

### Manual Tracking (Spreadsheet)

```
| Concept | Learned | Last Review | Quality | Next Review | Box |
|---------|---------|-------------|---------|-------------|-----|
| JS closures | 2025-01-01 | 2025-01-08 | 4 | 2025-01-22 | 3 |
| React hooks | 2025-01-03 | 2025-01-04 | 5 | 2025-01-11 | 2 |
```

### Automated Tools

**Physical flashcards**: Leitner box system
**Digital**: Anki, SuperMemo, Quizlet, RemNote
**Custom**: JSON/CSV file + script to generate daily lists

### Progress Tracking Integration

Link to progress-tracker agent:
- Update review quality after each session
- Track time spent on reviews
- Identify concepts needing more frequent review
- Celebrate concepts reaching "mastered" status

---

## Research References

This skill is based on:
- Ebbinghaus Forgetting Curve (1885)
- Leitner System (1970s)
- SM-2 Algorithm - SuperMemo (Wozniak, 1988)
- Spacing Effect - Cepeda et al. (2006)
- Testing Effect - Roediger & Karpicke (2006)
- Desirable Difficulties - Bjork (1994)

---

**Version**: 1.0.0
**Last Updated**: January 2025
**Use**: Read by schedule-optimizer agent before creating study schedules
