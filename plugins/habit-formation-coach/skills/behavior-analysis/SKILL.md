# Behavior Analysis Skill

**Pattern recognition and data-driven insights for habit optimization**

## Core Principles

1. **Data Over Intuition**: Use actual check-in data, not assumptions
2. **Patterns Reveal Truth**: What you do consistently shows what works
3. **Context Matters**: Time, location, mood all influence success
4. **Obstacles Are Systemic**: Not character flaws, environmental issues
5. **Trends Over Snapshots**: Direction matters more than single days

---

## Metrics That Matter

### Primary Metrics

**Completion Rate**:
```bash
Completion Rate = (Days Completed / Total Days) × 100

Interpretation:
- 80%+: Excellent, habit establishing well
- 60-79%: Moderate, needs attention
- 40-59%: Struggling, redesign recommended
- <40%: Not working, major redesign needed
```

**Current Streak**:
- Consecutive days completed
- Psychological motivator
- Indicates momentum
- Celebrate milestones (7, 14, 21, 30, 66 days)

**Longest Streak**:
- Historical peak performance
- Shows capability
- Goal to beat

**Trend Direction**:
```bash
Compare: (Last 7 days rate) vs (First 7 days rate)

- Improving: Rate increasing over time ↗️
- Stable: Rate consistent ➡️
- Declining: Rate decreasing over time ↘️
```

### Contextual Metrics

**Best Time of Day**:
- When is completion rate highest?
- Time buckets: Early morning (5-8am), Morning (8-11am), Midday (11am-2pm), Afternoon (2-5pm), Evening (5-8pm), Night (8pm+)
- Use this to optimize anchor timing

**Best Day of Week**:
- Which days have highest completion?
- Weekend vs weekday patterns
- Identify challenging days (need support)

**Mood Correlation**:
```
Track: Mood before (1-10) and after (1-10)
Analyze:
- Does habit improve mood? (after > before)
- What mood level predicts completion?
- Is habit effective emotional regulation?
```

**Location Success Rate**:
- Where does habit succeed most?
- Home vs work vs travel
- Optimize environment based on data

---

## Pattern Recognition Techniques

### Success Factor Analysis

**Methodology**: Examine completed instances, find commonalities

**What to look for**:
- **Temporal patterns**: Specific times that work consistently
- **Spatial patterns**: Locations with high success
- **Social patterns**: Alone vs with others
- **Sequence patterns**: What happens right before/after
- **Mood patterns**: Emotional states that predict success

**Example analysis**:
```
Meditation habit completed 25/30 days (83%)

Success factors identified:
- 90% completed between 7-8am (vs 50% at other times)
- 95% completed at kitchen table (vs 60% elsewhere)
- 88% completed when alone (vs 71% with family present)
- Avg mood before: 5.2, after: 7.1 (significant boost)

Recommendation: Protect 7-8am, kitchen table, alone time
```

### Obstacle Pattern Analysis

**Methodology**: Examine missed instances, find commonalities

**Common obstacle categories**:
1. **Environmental**: Physical barriers (location, tools unavailable)
2. **Temporal**: Time conflicts (schedule changes, rush)
3. **Social**: Other people interfering
4. **Physiological**: Tired, sick, low energy
5. **Psychological**: Forgot, unmotivated, stressed
6. **Systemic**: Routine disrupted (travel, life events)

**Example analysis**:
```
Missed 7/30 days (23% miss rate)

Obstacle breakdown:
- "Forgot": 4 occurrences (57% of misses)
- "Traveling": 2 occurrences (29% of misses)
- "Sick": 1 occurrence (14% of misses)

Root cause: Weak trigger (forgetting = anchor not strong enough)

Solution: Strengthen anchor, add visual cue
```

### Correlation Analysis

**What correlates with success?**

**Time-based**:
```python
# Pseudo-code for time analysis
for each_completion:
    bucket = get_time_bucket(completion.time)
    success_by_time[bucket] += 1

# Find optimal window
best_time = max(success_by_time)
```

**Context-based**:
```python
# What context factors predict success?
completed_when = {
    'location': [],
    'mood': [],
    'day_of_week': [],
    'alone_vs_social': []
}

for each_completed_day:
    collect_context_factors()

identify_common_patterns()
```

**Example findings**:
- "80% success when mood before is 6+, only 50% when mood is 4-"
- "90% success on weekdays, 60% on weekends" → Need weekend-specific strategy
- "95% success when traveling for work, 70% at home" → Home environment needs work

---

## Trend Analysis Methods

### Week-over-Week Comparison

```
Week 1: 6/7 (86%)
Week 2: 7/7 (100%)  ↗️ Improving
Week 3: 5/7 (71%)   ↘️ Declining
Week 4: 6/7 (86%)   ↗️ Recovering

Overall trend: Stable with volatility
```

**Interpretation**:
- Consistent improvement: Habit establishing well
- Stable plateau: Maintenance phase
- Declining: Something changed, investigate
- Volatile: External factors, identify patterns

### Moving Average

```bash
# Smooth out daily variance
7-day moving average:
Day 7:  6/7 = 86%
Day 14: 13/14 = 93%
Day 21: 18/21 = 86%

Trend: Peaked mid-way, slight decline
Action: Investigate what changed around day 14
```

### Establishment Trajectory

```
Expected trajectory for typical habit:
Days 1-7:   60-80% (learning, remembering)
Days 8-14:  70-85% (establishing)
Days 15-21: 80-90% (becoming automatic)
Days 22+:   85-95% (established)

If trajectory differs significantly, analyze why.
```

---

## Data Visualization Patterns

### Streak Visualization

```
Week 1: ✓✓✓✗✓✓✓  (6/7)
Week 2: ✓✓✓✓✓✓✓  (7/7)
Week 3: ✓✓✓✗✗✓✓  (5/7)

Current streak: 2 days
Longest streak: 10 days
```

### Completion Rate Graph

```
100% |    ●━━●
     |   ╱    ╲
 80% |  ●      ●━━●
     | ╱
 60% |●
     |
     +━━━━━━━━━━━━━━━━>
      W1 W2 W3 W4 W5
```

### Time Distribution Heatmap

```
Hour | Mon Tue Wed Thu Fri Sat Sun
6am  | ─── ─── ─── ─── ─── ─── ───
7am  | ✓✓✓ ✓✓✓ ✓✓  ✓✓✓ ✓✓✓ ─── ✓
8am  | ─── ─── ✓   ─── ─── ─── ───
9am  | ─── ─── ─── ─── ─── ✓   ───

Pattern: Strong 7am completion Mon-Fri, weekend at 9am
```

---

## Insight Generation Framework

### From Data to Recommendations

**Process**:
1. **Observe**: What does the data show?
2. **Interpret**: What does this mean?
3. **Recommend**: What should user do?

**Example**:
```
Observe: 95% completion rate at 7am, 60% at other times
Interpret: Morning anchor is strong, later times are weak
Recommend: Make 7am the primary habit time, consider 7am sacred
```

### Actionable vs Vague Insights

**❌ Vague**:
- "Try to be more consistent"
- "Stay motivated"
- "Don't give up"

**✅ Actionable**:
- "Your 7am completion rate is 95%. Protect this time slot."
- "You miss 80% on weekends. Create weekend-specific anchor: 'After breakfast' instead of 'After coffee'"
- "Traveling disrupts habit. Next trip: Pack [tool] and use 'After brushing teeth' as travel anchor"

---

## Establishment Assessment

### Is Habit Established?

**Criteria checklist**:
```
[ ] Duration: 21+ days of practice
[ ] Consistency: 80%+ completion rate
[ ] Automaticity: Feels easy, not effortful
[ ] Resilience: Survives disruptions (travel, stress)
[ ] Subjective: User reports "feels natural"
```

**Data-based assessment**:
```bash
if [ $DAYS -ge 21 ] && [ $COMPLETION_RATE -ge 80 ] && \
   [ $RECENT_7_DAYS -ge 70 ] && \
   [ $HARD_PERCENTAGE -lt 30 ]; then
    echo "✅ Habit is established"
else
    echo "⏳ Continue building (not quite established)"
fi
```

**Establishment indicators**:
- Feels weird to skip (not just willpower to continue)
- Don't think about it (automatic)
- Part of identity ("I'm someone who...")
- Integrated into routine (not separate effort)

---

## Recommendation Types

### Keep Doing (Strengths)

**Format**: [What's working] + [Evidence] + [Why maintain]

Example:
- "Your 7am timing is perfect - 95% success rate. This time works with your energy and schedule. Protect it."

### Adjust (Improvements)

**Format**: [What to change] + [Why it's not working] + [Specific solution]

Example:
- "Weekend completion is 60% vs 90% weekday. Your 'after coffee' anchor works great weekdays but weekends you sleep in. New weekend anchor: 'After I check phone in morning' - this happens regardless of wake time."

### Consider (Optional)

**Format**: [Enhancement opportunity] + [Potential benefit] + [No pressure]

Example:
- "You could add gratitude journaling after meditation (habit stacking). Your meditation is solid (21 days, 90%), so you could layer this. But also fine to keep meditation solo."

---

## Red Flags and Warnings

### Warning Signs

**Declining trend** (3+ weeks of decreasing completion):
- "Your completion rate has dropped from 85% (week 1-2) to 60% (week 3-4)"
- Action: Investigate what changed, consider recovery-coach

**High miss rate** (<60% overall):
- "23% completion rate suggests habit design issue"
- Action: Recommend redesign (smaller, better anchor, different time)

**"Hard" reports** (>40% report feeling difficult):
- "60% of check-ins marked 'hard' - habit may be too big"
- Action: Reduce size or change timing

**Streak pattern** (lots of short streaks, no long ones):
- "Longest streak is 3 days across 30 days - can't get momentum"
- Action: Identify recurring obstacle breaking streaks

---

## Advanced Analysis Patterns

### Multi-Habit Correlation

**When tracking multiple habits**:
```
Habit A (meditation): 90% completion
Habit B (exercise): 85% completion

Cross-analysis:
- Days with both: 75% of days
- Meditation only: 15% of days
- Exercise only: 10% of days

Pattern: Habits support each other, doing one predicts other
Recommendation: These form good stack, maintain both
```

### Seasonal Patterns

```
Month 1 (Jan): 85%
Month 2 (Feb): 82%
Month 3 (Mar): 90%

Spring break: 45% (disruption)
Post-break: 88% (recovered)

Insight: Habit resilient except major routine disruption
Recommendation: Pre-plan for known disruptions
```

### Mood Impact Analysis

```
Mood before habit: Avg 5.2
Mood after habit: Avg 7.1
Net gain: +1.9 points

Statistical significance: p < 0.01
Conclusion: Habit reliably improves mood

Use case: When mood is low, doing habit helps
Recommendation: On hard days, remember this pattern
```

---

## Reporting Best Practices

### Progress Report Structure

1. **Executive Summary**: Overall status in 2-3 sentences
2. **Key Metrics**: Completion rate, streak, trend
3. **What's Working**: Success factors with evidence
4. **What's Challenging**: Obstacles with solutions
5. **Recommendations**: Specific, prioritized actions
6. **Next Steps**: Clear immediate tasks

### Communication Guidelines

**Be honest but encouraging**:
- Acknowledge struggles without shame
- Celebrate all progress (even 50% is data)
- Frame setbacks as learning opportunities

**Be specific**:
- "Your 7am completion is 95%" vs "Morning is good"
- "Weekend anchor needs adjustment" vs "Weekends are hard"

**Be actionable**:
- Every insight should have clear next step
- Prioritize (most important first)
- Make recommendations concrete

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: Habit tracking analysis, pattern identification, optimization recommendations
