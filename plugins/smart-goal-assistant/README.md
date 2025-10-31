# SMART Goal Setting Assistant Plugin

A comprehensive goal-setting and tracking system that helps individuals and teams set, plan, track, and achieve SMART goals through structured validation, milestone planning, progress tracking, regular reviews, and strategic pivoting.

## Overview

This plugin provides a complete framework for:
- Validating goals against SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound)
- Breaking down goals into actionable milestones with dependencies
- Tracking progress with automated dashboards
- Conducting structured weekly and monthly reviews
- Identifying stuck goals and recommending strategic pivots
- Celebrating wins and learning from setbacks

## Plugin Structure

```
smart-goal-assistant/
├── README.md (this file)
├── agents/
│   ├── goal-validator.md         # SMART criteria validation
│   ├── milestone-planner.md       # Goal decomposition & roadmap
│   ├── progress-tracker.md        # Fast progress logging
│   ├── review-facilitator.md      # Weekly/monthly reviews
│   └── pivot-advisor.md           # Stuck goal detection & pivoting
├── skills/
│   ├── smart-validation/
│   │   └── SKILL.md              # SMART framework patterns
│   ├── milestone-decomposition/
│   │   └── SKILL.md              # Decomposition strategies
│   ├── progress-tracking/
│   │   └── SKILL.md              # Metrics & tracking patterns
│   ├── review-facilitation/
│   │   └── SKILL.md              # Review frameworks
│   └── pivot-strategy/
│       └── SKILL.md              # Pivot decision matrices
└── templates/
    ├── smart-goal-template.md         # Initial goal definition
    ├── milestone-roadmap.md           # Milestone planning output
    ├── progress-dashboard.md          # Progress tracking view
    ├── weekly-review-template.md      # Weekly review format
    ├── monthly-review-template.md     # Monthly review format
    └── pivot-decision-template.md     # Pivot analysis output
```

## Agents

### 1. Goal Validator (@goal-validator)
**Model**: Sonnet | **Tools**: Read, Write, Bash, Glob

Validates goals against SMART criteria and provides actionable improvement suggestions.

**Use when**:
- Setting new goals
- Refining vague objectives
- Ensuring goals are well-structured before planning

**Output**: Validated SMART goal with scoring and improvement recommendations

### 2. Milestone Planner (@milestone-planner)
**Model**: Sonnet | **Tools**: Read, Write, Bash, Glob

Decomposes goals into actionable milestones with dependencies, timelines, and success criteria.

**Use when**:
- Breaking down validated goals
- Planning quarterly or annual objectives
- Creating project roadmaps

**Output**: Milestone roadmap with dependencies, timelines, and metrics

### 3. Progress Tracker (@progress-tracker)
**Model**: Haiku | **Tools**: Read, Write, Bash, Glob

Fast progress logging and automated dashboard generation for real-time goal tracking.

**Use when**:
- Logging daily/weekly progress
- Updating milestone completion
- Generating progress reports

**Output**: Updated progress dashboard with completion percentages and trends

### 4. Review Facilitator (@review-facilitator)
**Model**: Sonnet | **Tools**: Read, Write, Bash, Glob

Conducts structured weekly and monthly reviews to identify obstacles, adjust plans, and celebrate wins.

**Use when**:
- Weekly goal reviews
- Monthly retrospectives
- Quarterly planning sessions

**Output**: Review report with insights, adjustments, and action items

### 5. Pivot Advisor (@pivot-advisor)
**Model**: Sonnet | **Tools**: Read, Write, Bash, Glob

Detects stuck or off-track goals and recommends strategic pivots or course corrections.

**Use when**:
- Goals are consistently behind schedule
- Circumstances have changed
- Need to decide: push through or pivot

**Output**: Pivot analysis with recommendations and decision framework

## Typical Workflows

### Workflow 1: New Goal Setup
```bash
# Step 1: Validate goal against SMART criteria
@goal-validator "Increase revenue by improving customer retention"

# Step 2: Break down into milestones
@milestone-planner /mnt/user-data/outputs/validated-goal.md

# Step 3: Set up progress tracking
@progress-tracker --init /mnt/user-data/outputs/milestone-roadmap.md
```

### Workflow 2: Weekly Review
```bash
# Update progress
@progress-tracker "Completed milestone 2, started milestone 3"

# Conduct weekly review
@review-facilitator --weekly /mnt/user-data/outputs/progress-dashboard.md
```

### Workflow 3: Monthly Strategic Review
```bash
# Generate progress report
@progress-tracker --report monthly

# Facilitate monthly review
@review-facilitator --monthly /mnt/user-data/outputs/progress-dashboard.md

# Check for stuck goals
@pivot-advisor /mnt/user-data/outputs/monthly-review.md
```

### Workflow 4: Pivot Decision
```bash
# Analyze stuck goal
@pivot-advisor "Goal: Launch product by Q1 - Currently 60 days behind"

# Review pivot recommendations
# Make decision and update plan
@milestone-planner --revise /mnt/user-data/outputs/pivot-decision.md
```

## Skills Overview

### SMART Validation Skill
Provides comprehensive SMART criteria framework:
- **Specific**: Clear, unambiguous goal statements
- **Measurable**: Quantifiable success metrics
- **Achievable**: Realistic given resources and constraints
- **Relevant**: Aligned with broader objectives
- **Time-bound**: Clear deadlines and timeframes

### Milestone Decomposition Skill
Teaches effective goal breakdown:
- Backward planning from deadline
- Dependency mapping
- Critical path identification
- Buffer time allocation
- Success criteria definition

### Progress Tracking Skill
Defines tracking best practices:
- Leading vs lagging indicators
- Velocity tracking
- Burndown charts
- Red/yellow/green status criteria
- Trend analysis

### Review Facilitation Skill
Structures effective reviews:
- Pre-review preparation
- Facilitation techniques
- Obstacle identification
- Action item generation
- Celebration rituals

### Pivot Strategy Skill
Provides decision frameworks:
- Sunk cost analysis
- Opportunity cost evaluation
- Pivot vs persevere criteria
- Graceful goal retirement
- Learning capture

## Templates

All templates are located in `templates/` and serve as:
- **Input guides**: What information to provide
- **Output formats**: Consistent structure for agent outputs
- **Reference**: Examples of well-structured goals and plans

## Installation

### Project-Level (Recommended)
```bash
# Copy entire plugin to project
cp -r /path/to/smart-goal-assistant .claude/plugins/

# Agents auto-activate in Puerto
```

### User-Level (Global)
```bash
# Copy agents to user config
cp agents/*.md ~/.claude/agents/

# Skills remain in project for reference
```

## Configuration

### Goal Storage
By default, goals are stored in:
```
/mnt/user-data/outputs/goals/
├── active/           # Current goals
├── completed/        # Achieved goals
├── archived/         # Retired/pivoted goals
└── templates/        # Goal templates
```

### Progress Tracking
Progress data stored in:
```
/mnt/user-data/outputs/progress/
├── dashboards/       # Current progress views
├── history/          # Historical snapshots
└── metrics/          # Raw progress data
```

## Best Practices

### 1. Start with Validation
Always validate goals with @goal-validator before planning. Poorly defined goals lead to wasted planning effort.

### 2. Review Regularly
- **Daily**: Quick progress updates (@progress-tracker)
- **Weekly**: Review and adjust (@review-facilitator --weekly)
- **Monthly**: Strategic review (@review-facilitator --monthly)
- **Quarterly**: Major pivots and planning (@pivot-advisor)

### 3. Be Honest About Progress
Accurate progress tracking enables better decisions. Don't sugar-coat delays or obstacles.

### 4. Celebrate Wins
Use @review-facilitator to explicitly celebrate milestone completions. Motivation matters.

### 5. Don't Fear Pivots
Sometimes the best decision is to change course. Use @pivot-advisor objectively.

### 6. Maintain Context
Keep all goal documents in organized folders. Link related goals and milestones.

## Integration with Other Plugins

### With Expense Manager
Track costs associated with goal milestones:
```bash
@expense-tracker "Project milestone: $5,000 marketing spend"
```

### With Tax Compliance
Plan tax implications of business goals:
```bash
@tax-planner "Revenue goal: $500K - estimate quarterly taxes"
```

### With Orchestrator
Coordinate complex multi-goal projects:
```bash
@orchestrator "Coordinate Q1 goals: product launch, hiring, revenue targets"
```

## Metrics & Success

### Plugin Effectiveness Metrics
- Goal completion rate (target: >70%)
- On-time milestone delivery (target: >80%)
- Pivot success rate (target: >60% of pivots improve outcomes)
- Review consistency (target: 90% weekly reviews completed)

### Quality Indicators
- SMART score of validated goals (target: >85/100)
- Milestone granularity (target: 2-4 week milestones)
- Progress update frequency (target: weekly minimum)

## Troubleshooting

### "Goal too vague"
Use @goal-validator iteratively to refine. Start with rough idea, improve through multiple passes.

### "Too many milestones"
Aim for 5-8 major milestones per goal. Use @milestone-planner to consolidate.

### "Falling behind schedule"
Run @pivot-advisor early. Don't wait until completely off track.

### "Lost motivation"
Use @review-facilitator to identify root causes. Often misaligned goals or unclear progress.

## Examples

### Example 1: Business Goal
```
Goal: Increase MRR from $50K to $75K by Q4 2024

Milestones:
1. Implement customer feedback system (Month 1)
2. Launch referral program (Month 2)
3. Expand to enterprise tier (Month 3)
4. Achieve $75K MRR (Month 4)

Weekly reviews identify: referral program underperforming
Pivot: Shift resources from referrals to enterprise expansion
Result: Hit $72K MRR (96% of goal)
```

### Example 2: Personal Goal
```
Goal: Run a half-marathon in under 2 hours by June 2024

Milestones:
1. Establish 3x/week running habit (Weeks 1-4)
2. Complete 5K in under 30min (Week 8)
3. Complete 10K in under 60min (Week 12)
4. Complete half-marathon training plan (Weeks 13-16)
5. Race day: sub-2-hour finish (Week 16)

Monthly reviews track: injury risk, motivation, progress
Result: Completed in 1:58:32
```

## Version History

### v1.0.0 (2024-01-21)
- Initial release
- 5 agents with skills-first approach
- Complete template library
- Integrated workflow support

## Support & Contributions

This plugin is part of the Puerto agent framework. For issues, improvements, or questions:
- GitHub Issues: #120
- Documentation: See individual SKILL.md files for detailed patterns
- Examples: See templates/ directory

## License

Part of Puerto framework - see main repository license.

---

**Remember**: Goals are meant to be guides, not shackles. Use this plugin to maintain clarity and momentum, but don't be afraid to pivot when circumstances change. The goal is progress, not perfection.
