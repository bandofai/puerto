# Habit Formation Coach Plugin

**Science-based habit formation using tiny habits, behavior analysis, and compassionate coaching**

## Overview

The Habit Formation Coach plugin helps you build lasting habits using evidence-based behavioral science. It implements BJ Fogg's Behavior Model (B=MAP), tiny habits methodology, habit stacking, and compassionate relapse recovery to create sustainable behavior change.

## Features

✅ **Tiny Habits Design**: Start small with habits that take <30 seconds
✅ **Behavior Analysis**: Track patterns and identify triggers/obstacles
✅ **Habit Stacking**: Connect new habits to existing routines
✅ **Daily Check-ins**: Fast accountability tracking with streak monitoring
✅ **Compassionate Recovery**: Evidence-based relapse recovery without shame
✅ **Progressive Scaling**: Optimize and grow habits once established
✅ **Implementation Intentions**: "When X happens, I will do Y" planning
✅ **Motivation Wave Surfing**: Strategies for high and low motivation states

## Architecture

### 5 Specialized Agents

1. **habit-designer** (Sonnet - Requires Judgment)
   - Creates comprehensive habit plans using behavioral science
   - Applies BJ Fogg Behavior Model (Behavior = Motivation × Ability × Prompt)
   - Designs tiny habits that guarantee early success
   - Implements habit stacking and implementation intentions
   - Customizes to individual context and goals

2. **behavior-analyst** (Sonnet - Pattern Recognition)
   - Analyzes check-in data for patterns and insights
   - Identifies triggers, obstacles, and success factors
   - Generates personalized recommendations
   - Tracks progress metrics and trends
   - Creates visual progress reports

3. **accountability-tracker** (Haiku - Fast & Simple)
   - Handles daily/weekly check-ins quickly
   - Tracks streaks and completion rates
   - Records context (time, location, feelings)
   - Minimal friction for consistent use
   - Immediate positive reinforcement

4. **recovery-coach** (Sonnet - Compassion Required)
   - Provides empathetic support after missed habits
   - Creates personalized recovery protocols
   - Identifies environmental/systemic obstacles
   - Reframes setbacks as learning opportunities
   - Prevents shame spirals with science-based perspective

5. **habit-optimizer** (Sonnet - Strategic Thinking)
   - Scales established habits strategically
   - Suggests habit stacking opportunities
   - Optimizes timing and context
   - Identifies consolidation opportunities
   - Prevents overwhelm from too many changes

### 5 Comprehensive Skills

1. **habit-formation**: BJ Fogg model, tiny habits, implementation intentions
2. **behavior-analysis**: Pattern recognition, obstacle identification, data insights
3. **accountability-systems**: Check-in design, streak psychology, reinforcement
4. **relapse-recovery**: Compassionate coaching, obstacle removal, reframing
5. **habit-optimization**: Scaling strategies, stacking frameworks, consolidation

### Templates

- **habit-plan.md**: Comprehensive habit design with all behavioral elements
- **check-in-log.json**: Daily/weekly check-in data structure
- **recovery-protocol.md**: Personalized plan after setbacks
- **progress-report.md**: Analysis and insights from tracking data

## Installation

### Prerequisites

**Required**:
- Claude Code CLI

**Optional**:
- Reminder system (calendar, phone notifications)
- Journal or tracking app

### Install Plugin

```bash
# Copy to your Claude plugins directory
cp -r plugins/habit-formation-coach ~/.claude/plugins/

# Or use project-level
cp -r plugins/habit-formation-coach .claude/plugins/
```

### Verify Installation

```bash
# Check plugin structure
tree ~/.claude/plugins/habit-formation-coach/

# Verify agents are available
# (Claude Code will automatically discover agents in the plugins directory)
```

## Usage

### Complete Workflow Example

**Step 1: Design Your Habit**

"I want to start meditating daily but I've failed at this before"

The habit-designer will:
- Interview you about your goal, past failures, and context
- Design a tiny habit (2 minutes, specific trigger)
- Create implementation intention
- Identify celebration for completion
- Generate comprehensive habit plan

**Step 2: Daily Check-ins**

"Log my habit check-in: meditated for 2 minutes after morning coffee ✓"

The accountability-tracker will:
- Record completion and context
- Update streak counter
- Provide immediate positive reinforcement
- Store data for pattern analysis

**Step 3: Weekly Review**

"Analyze my habit progress this week"

The behavior-analyst will:
- Review check-in data
- Identify patterns (best times, success factors)
- Spot obstacles
- Generate insights and recommendations
- Create progress visualization

**Step 4: Handle Setbacks (If Needed)**

"I missed my meditation habit for 3 days in a row"

The recovery-coach will:
- Respond with empathy (no shame)
- Analyze what happened (obstacles)
- Create recovery protocol
- Adjust habit if needed
- Get you back on track

**Step 5: Scale When Ready**

"My 2-minute meditation is solid. Ready to grow it."

The habit-optimizer will:
- Confirm habit is truly established (21+ days, >80% completion)
- Suggest scaling strategy (small increments)
- Propose additional habit stacking
- Monitor for sustainability
- Prevent premature optimization

## Agent Details

### habit-designer

**Trigger**: "Create habit plan", "Design new habit", "Help me build a habit"

**Capabilities**:
- BJ Fogg Behavior Model application
- Tiny habits methodology
- Implementation intention design
- Habit stacking recommendations
- Personalized celebration selection
- Context-specific customization

**Output**: Complete habit plan in `./habits/plans/`

**Key Principles**:
- Start ridiculously small (2 minutes or less)
- Anchor to existing routine (after X, I will Y)
- Celebrate immediately (wire in the habit)
- Design for your actual life, not ideal life
- Make it easier than you think necessary

### behavior-analyst

**Trigger**: "Analyze habit progress", "What patterns do you see", "Review my habits"

**Capabilities**:
- Pattern recognition in check-in data
- Trigger and obstacle identification
- Success rate calculation
- Context correlation analysis
- Trend visualization
- Personalized recommendations

**Output**: Analysis report in `./habits/analysis/`

**Metrics Tracked**:
- Completion rate (daily/weekly)
- Streak length (current/longest)
- Best times/contexts
- Common obstacles
- Motivation patterns
- Habit correlation

### accountability-tracker

**Trigger**: "Log habit", "Check in", "Record completion"

**Capabilities**:
- Sub-30-second check-ins
- Streak tracking and celebration
- Context recording (time, place, mood)
- Positive reinforcement
- Reminder suggestions
- Data export for analysis

**Output**: Check-in logs in `./habits/check-ins/`

**Security**: Write-only for new data (can't modify history)

### recovery-coach

**Trigger**: "Missed my habit", "Failed again", "Having trouble"

**Capabilities**:
- Empathetic response (zero shame)
- Obstacle analysis
- Environment modification suggestions
- Habit redesign if needed
- Fresh start framing
- Systemic issue identification

**Output**: Recovery protocol in `./habits/recovery/`

**Approach**:
- Normalize setbacks (expected, not failure)
- Focus on obstacles, not willpower
- Adjust system, not person
- Smaller steps if needed
- Compassionate reframing

### habit-optimizer

**Trigger**: "Scale my habit", "Ready to level up", "Optimize habits"

**Capabilities**:
- Establishment verification (data-driven)
- Safe scaling strategies
- Habit stacking design
- Timing optimization
- Consolidation opportunities
- Overextension prevention

**Output**: Optimization plan in `./habits/optimization/`

**Safety Checks**:
- Minimum 21 days established
- 80%+ completion rate
- Feels automatic, not effortful
- Won't compromise existing habits

## Behavioral Science Foundation

### BJ Fogg Behavior Model (B=MAP)

**Behavior = Motivation × Ability × Prompt**

For a behavior to occur:
1. **Motivation**: Desire to do it (varies by moment)
2. **Ability**: Easy enough to do (design-controlled)
3. **Prompt**: Reminder at right moment (anchoring)

**Key Insight**: When motivation is low (which it will be), make ability extremely high (make it tiny and easy).

### Tiny Habits Method

**Core Principles**:
1. Start with behaviors taking <30 seconds
2. Anchor to existing routine ("After I X, I will Y")
3. Celebrate immediately to wire in habit
4. Scale up only after establishment
5. Focus on repetition, not perfection

### Implementation Intentions

**Format**: "When [situation], I will [behavior]"

**Examples**:
- "After I pour my morning coffee, I will meditate for 2 minutes"
- "When I close my laptop for the day, I will write 3 things I'm grateful for"
- "After I brush my teeth at night, I will floss one tooth"

**Why It Works**: Pre-decides behavior, reduces decision fatigue, creates automatic cue.

### Habit Stacking

**Build on existing habits**:

```
Existing Routine → New Tiny Habit → Celebration
      ↓                  ↓               ↓
  Pour coffee  →  2-min meditation  →  "Nice work!"
      ↓                  ↓               ↓
  Brush teeth  →    Floss 1 tooth   →   Smile
```

### Compassionate Recovery Framework

**When habits are missed**:
1. **No shame**: Setbacks are normal, expected, informative
2. **Analyze obstacles**: What made it hard? (not "why didn't I do it?")
3. **Adjust system**: Change environment, not person
4. **Fresh start**: Every moment is a new opportunity
5. **Learn and iterate**: Each attempt provides data

## Configuration

### Customize Your Habit Plan

Create `./habits/config.json`:

```json
{
  "user": {
    "name": "Your Name",
    "timezone": "America/New_York",
    "energy_patterns": "morning_person",
    "existing_routines": [
      "Morning coffee at 7am",
      "Lunch at 12pm",
      "Brush teeth at 10pm"
    ]
  },
  "preferences": {
    "check_in_style": "quick",
    "reminder_frequency": "daily",
    "celebration_style": "verbal_affirmation",
    "analysis_frequency": "weekly"
  },
  "goals": {
    "primary_focus_areas": ["health", "mindfulness", "learning"],
    "max_concurrent_habits": 3,
    "commitment_level": "sustainable"
  }
}
```

## Workflow Coordination

The agents work together in a supportive cycle:

```
New Goal
   ↓
┌──────────────┐
│habit-designer│ (Design tiny habit)
└──────────────┘
   ↓
Habit Plan Created
   ↓
┌────────────────────┐
│accountability-     │ (Daily check-ins)
│tracker             │
└────────────────────┘
   ↓
Check-in Data Accumulated
   ↓
┌──────────────────┐
│behavior-analyst  │ (Weekly insights)
└──────────────────┘
   ↓
Patterns Identified
   ↓
   ├─────[Success]─────→┌──────────────────┐
   │                    │habit-optimizer   │ (Scale up)
   │                    └──────────────────┘
   │
   └────[Setback]─────→┌──────────────────┐
                       │recovery-coach    │ (Get back on track)
                       └──────────────────┘
```

## Cost Optimization

**Model Selection Strategy**:
- **Haiku** for check-ins (fast, simple, ~$0.001/1K tokens)
- **Sonnet** for design, analysis, recovery, optimization (~$0.015/1K tokens)

**Why Not Opus**:
- Habit formation doesn't require maximum reasoning
- Sonnet provides excellent judgment and empathy
- Haiku handles routine tracking efficiently

**Estimated Costs** (per month with 3 habits):
- Initial habit design: ~$0.20 (Sonnet, 3 plans)
- Daily check-ins: ~$0.30 (Haiku, 90 check-ins)
- Weekly analysis: ~$0.40 (Sonnet, 4 analyses)
- Recovery support: ~$0.10 (Sonnet, as needed)
- **Total: ~$1.00/month**

## Best Practices

### Starting New Habits

1. **Make it tiny**: 2 minutes or less
2. **Be specific**: "After coffee, meditate 2 min" not "meditate daily"
3. **Anchor to routine**: Use existing behavior as trigger
4. **Celebrate immediately**: Wire in the positive feeling
5. **Track consistently**: Check in every day, even if you miss
6. **One at a time**: Master one before adding another
7. **Design for low motivation**: Assume you'll feel tired/busy

### Maintaining Habits

1. **Check in daily**: Use accountability-tracker even for misses
2. **Review weekly**: Get insights from behavior-analyst
3. **Don't skip twice**: One miss is normal, two starts a pattern
4. **Celebrate streaks**: Acknowledge milestones (7, 21, 30, 66 days)
5. **Track obstacles**: Note what makes it hard
6. **Adjust as needed**: Life changes, habits should too

### Recovering from Setbacks

1. **Use recovery-coach**: Don't try to power through alone
2. **No shame**: Treat yourself like a good friend
3. **Analyze obstacles**: Environmental, not character flaw
4. **Make it easier**: Reduce size or change trigger
5. **Fresh start**: Don't wait for Monday, start now
6. **Keep data**: Even misses provide valuable information

### Scaling Successfully

1. **Wait until established**: 21+ days, 80%+ completion, feels automatic
2. **Scale slowly**: Add 10-20% at a time
3. **Monitor carefully**: Watch for strain or declining completion
4. **Stack thoughtfully**: Add related habits to same anchor
5. **Maintain core**: Don't sacrifice consistency for size
6. **Use habit-optimizer**: Don't guess, use data-driven approach

## Examples

### Example 1: Building Meditation Habit

**Week 1-3: Establishment**
```
Goal: Daily meditation
Designed habit: "After I pour morning coffee, I will meditate for 2 minutes"
Anchor: Morning coffee (existing routine)
Location: Kitchen table
Celebration: "I'm building my meditation practice!"

Week 1: 6/7 days (missed Saturday - slept at friend's house)
Week 2: 7/7 days (brought practice to friend's house)
Week 3: 7/7 days (feels automatic now)
```

**Week 4: Analysis & Scaling**
```
Analyst findings:
- 95% completion rate
- Best time: 7:15am after coffee
- Success factor: Phone on airplane mode
- Obstacle removed: Moved cushion to visible spot

Optimizer recommendation:
- Increase to 5 minutes (ready to scale)
- Keep same anchor (working well)
- Add session logging if interested
```

### Example 2: Recovery from Setback

**Situation**: Missed flossing habit 4 days running
```
User: "I've failed at flossing again. I never stick with anything."

Recovery Coach Response:
"Let's look at what happened without judgment. You successfully
flossed for 18 days - that's real progress, not failure.

Analysis of the last 4 days:
- All 4 days you were traveling for work
- Different bathroom, no visible floss
- Evening routine disrupted by client dinners

This isn't a willpower issue. Your system worked great at home
(18 days!), but the environment changed.

Recovery protocol:
1. Put floss in travel toiletry bag (make visible)
2. New anchor: 'After I set hotel alarm, I floss one tooth'
3. Fresh start today - you've got this
4. Track: Did travel create obstacle? (Yes/No)

You haven't failed. You've discovered that your habit needs
travel-proofing. That's valuable information."
```

### Example 3: Habit Stacking

**Building on established habits**
```
Established habit 1: "After morning coffee → meditate 2 min" (45 days, 93%)
Established habit 2: "After dinner → walk 10 min" (30 days, 87%)

Optimizer suggestions:
1. Stack gratitude: "After meditation → write 1 thing I'm grateful for"
2. Stack stretching: "After walk → stretch 3 minutes"
3. Time spacing: Both stacks are hours apart (no overwhelm risk)

Implementation:
Week 1: Add gratitude stack only (one change at a time)
Week 5: If gratitude solid, add stretching stack
```

## Advanced Features

### Motivation Wave Surfing

**High motivation state** (Don't over-commit):
- Maintain tiny habit size (resist urge to do more)
- Build consistency, not intensity
- Use energy for obstacle removal (make environment easier)
- Remember: This wave will pass

**Low motivation state** (Design for this):
- Rely on tiny size (2 minutes is doable even when exhausted)
- Lean on automatic anchor (no decision needed)
- Celebrate attempt, not perfection
- This is the design target (not high motivation)

### Obstacle Pre-Mortems

Before starting habit, identify potential obstacles:

| Obstacle | Prevention Strategy |
|----------|-------------------- |
| Traveling | Pack cue/tools, identify travel anchor |
| Illness | Define "minimum viable habit" (even smaller) |
| Schedule change | Secondary anchor for different contexts |
| Low energy | Make even easier, reduce to absolute minimum |
| Forgetfulness | Visual reminder at anchor point |

### Keystone Habits

Some habits create cascading benefits:

**Recognized keystone habits**:
- Exercise (improves energy, mood, sleep)
- Sleep routine (improves everything)
- Meditation (reduces stress, increases awareness)
- Planning (improves time management, reduces anxiety)

**Identifying your keystones**:
- Which habits make other habits easier?
- What has ripple effects across your life?
- What gives you energy vs. depletes you?

## Troubleshooting

### "I keep forgetting to do my habit"

**Problem**: No reliable prompt
**Solutions**:
1. Make anchor more visible (put cue where you'll see it)
2. Add phone reminder initially (remove once automatic)
3. Choose different anchor with stronger trigger
4. Stack on more frequent behavior

### "I do it sometimes but it's not consistent"

**Problem**: Habit not yet automatic (needs more time)
**Solutions**:
1. Keep it tiny (don't increase size yet)
2. Track every day (even misses)
3. Strengthen celebration (make it feel good)
4. Remove obstacles (analyze what makes it hard)
5. Give it more time (21-66 days typical)

### "I'm motivated for a week then stop"

**Problem**: Relying on motivation instead of system
**Solutions**:
1. Make it even smaller (ridiculously easy)
2. Strengthen anchor (more reliable trigger)
3. Design for low motivation (that's normal)
4. Use recovery-coach at first slip (not after pattern)

### "I want to do too many habits at once"

**Problem**: Overextension leads to nothing sticking
**Solutions**:
1. Pick ONE habit to start with
2. Wait until truly established (21+ days, 80%+)
3. Add second habit only when first is automatic
4. Use habit-optimizer to check readiness
5. Remember: 3 solid habits > 10 attempted habits

## Roadmap

Future enhancements planned:
- [ ] Habit correlation analysis (which habits support each other)
- [ ] Social accountability features (habit buddies)
- [ ] Integration with habit tracking apps
- [ ] Voice-based check-ins
- [ ] Machine learning for personalized timing
- [ ] Habit library with proven templates
- [ ] Progress visualization dashboard
- [ ] Environmental design recommendations

## Support

- **Issues**: Report bugs or request features on GitHub
- **Documentation**: Full skill documentation in `skills/` directory
- **Examples**: Additional examples and templates included

## License

Part of Puerto plugin marketplace. See main project LICENSE.

---

**Plugin Version**: 1.0.0
**Last Updated**: January 2025
**Based on**: BJ Fogg's Behavior Model, Atomic Habits, behavioral science research
**Compatible with**: Claude Code CLI
