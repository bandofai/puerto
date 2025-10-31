# Project Reporting Skill

**Status report structures, KPI tracking, progress metrics, and stakeholder communication patterns for executive, management, and team-level reporting**

This skill codifies best practices from effective project communication across thousands of projects, incorporating lessons learned about what information stakeholders actually need and when.

---

## Core Principles

1. **Tailor to audience**: Executives want summaries, teams want details
2. **Be honest**: Transparency builds trust, sugar-coating destroys it
3. **Focus on decisions**: Highlight what needs stakeholder action
4. **Use visuals**: Charts communicate faster than text
5. **Trends matter more than snapshots**: Show direction, not just current state
6. **Actionable not historical**: What we're doing about it, not just what happened
7. **Consistent format**: Same structure every time aids comprehension
8. **Timely**: Report on schedule, don't skip bad weeks
9. **Data-driven**: Metrics over feelings
10. **Forward-looking**: Past is context, future is actionable

---

## Report Types by Audience

### Executive Summary Report

**Audience**: Sponsors, C-level executives, board members
**Frequency**: Monthly or at major milestones
**Length**: 1 page maximum
**Reading Time**: 2-3 minutes
**Focus**: Strategic decisions, critical issues, ROI

**Structure**:
```markdown
# Executive Summary - [Project Name]
**Date**: January 31, 2025 | **PM**: [Name] | **Sponsor**: [Name]

## Status at a Glance
🟢 **ON TRACK** to deliver May 1, 2025

| Area | Status | Comment |
|------|--------|---------|
| Schedule | 🟢 | On track, 42% complete |
| Budget | 🟡 | 5% variance (within tolerance) |
| Scope | 🟢 | No changes |
| Quality | 🟢 | All metrics green |
| Risks | 🟡 | 2 high risks, mitigating |

## Key Achievements This Month
✅ Requirements & Design completed on schedule
✅ Development 40% complete (baseline: 40%)
✅ All quality gates passed

## Critical Issues Requiring Decision
1. **Resource Gap**: Senior frontend developer needed by Feb 15
   - Impact: 2-week delay if unfilled
   - Cost: $36K for 6-week contractor
   - **Decision needed**: Approve contractor? (Due: Feb 5)

2. **Scope Change Request**: Mobile app addition
   - Impact: +6 weeks, +$50K
   - **Decision needed**: Approve or defer to Phase 2? (Due: Feb 10)

## Financial Summary
- Budget: $250K | Spent: $105K (42%)
- Forecast: $262.5K (5% over, within contingency)
- ROI: On track for 18-month payback

## Next 30 Days
- Complete development phase (target: 65%)
- Beta release (Feb 28 milestone)
- Begin user acceptance testing
```

**Key Features**:
- RAG status prominent
- Decisions needed clearly highlighted
- Financial summary always included
- No technical jargon
- Bullet points, not paragraphs

### Weekly Status Report

**Audience**: Project team, direct manager, active stakeholders
**Frequency**: Weekly (typically Friday)
**Length**: 2-3 pages
**Reading Time**: 5-10 minutes
**Focus**: Progress, blockers, near-term plans

**Structure**:
```markdown
# Weekly Status - [Project Name]
**Week Ending**: January 26, 2025 | **Status**: 🟢 On Track

## Progress Summary
**% Complete**: 42% (was 35% last week) ✅ +7%
**Tasks Completed**: 18 of 16 planned ✅ Ahead
**Burn Rate**: $21K/week (tracking to plan)

### Completed This Week
✅ Task 2.3: Database schema design (John, Jan 22)
✅ Task 2.4: API specs complete (Sarah, Jan 24)
✅ Task 2.5: Security review passed (Mike, Jan 25)
✅ Task 3.1: Dev environment ready (Team, Jan 23)
[+14 more tasks - see appendix]

### In Progress
🔄 Task 3.2: User auth module (John, 60% complete, due Jan 30)
🔄 Task 3.3: Data layer (Sarah, 40% complete, due Feb 2)
🔄 Task 3.4: Frontend scaffolding (Mike, 75% complete, due Jan 28)

### Blocked Tasks
🚫 Task 3.5: Payment integration (Amy, 0%)
   - Blocker: Waiting for vendor API credentials
   - Expected resolution: Jan 27
   - Action: Amy escalated to vendor, daily follow-up

## Metrics Dashboard

| Metric | This Week | Last Week | Trend | Target |
|--------|-----------|-----------|-------|--------|
| Tasks Done | 18 | 14 | ↑ +29% | 16 |
| % Complete | 42% | 35% | ↑ +7% | 40% |
| Velocity | 18 t/wk | 14 t/wk | ↑ +29% | 16 |
| Budget Spent | $105K | $84K | - | $100K |
| Test Coverage | 82% | 78% | ↑ +4% | >80% |
| Defects Open | 3 | 5 | ↓ -2 | <5 |

## Issues & Risks

### New Issues This Week
**Issue #12**: Production DB backup failed Jan 24
- Severity: Medium
- Impact: Potential data loss scenario
- Status: RESOLVED - Configuration fixed, tested

**Issue #13**: API rate limits too restrictive
- Severity: High
- Impact: Performance degradation under load
- Status: OPEN - Negotiating upgrade with vendor
- Owner: Tech Lead
- Due: Feb 1

### Top 3 Risks (No change from last week)
1. Key developer departure (Score: 12) - Mitigation underway
2. Scope creep (Score: 16) - Change control active
3. API reliability (Score: 12) - Load testing this week

## Next Week Plan (Jan 29 - Feb 2)

### Priorities
1. Complete auth module (John)
2. Deploy to staging (Mike, Thu)
3. Resolve payment API blocker (Amy, Mon)
4. Start integration testing (Sarah, Wed)

### Scheduled Events
- Monday 9am: Sprint planning
- Wednesday 2pm: Architecture review
- Friday 3pm: Stakeholder demo

### Expected Completions
20-22 tasks (assumes blocker resolved Monday)

## Action Items

| Item | Owner | Due | Status |
|------|-------|-----|--------|
| Get API credentials | Amy | Jan 27 | Open |
| Deploy staging | Mike | Jan 30 | In Progress |
| Schedule perf test | Sarah | Feb 2 | Not Started |

## Notes
Team morale high after successful design review. Sprint velocity increasing as team gels. Recommend contractor approval for frontend (see escalation to sponsor).
```

### Monthly Status Report

**Audience**: Management, steering committee, program managers
**Frequency**: Monthly (first week of new month)
**Length**: 4-6 pages
**Reading Time**: 15-20 minutes
**Focus**: Trends, forecasts, strategic alignment

**Key Sections**:
1. Executive summary
2. Progress vs baseline (earned value analysis)
3. KPI dashboard with trends
4. Risk and issue analysis
5. Resource utilization
6. Budget tracking and forecast
7. Quality metrics
8. Next month outlook
9. Decisions needed

---

## Key Performance Indicators (KPIs)

### Schedule KPIs

**Schedule Performance Index (SPI)**:
```
SPI = EV / PV

Where:
- EV (Earned Value) = % Actually Complete × Total Budget
- PV (Planned Value) = % Should Be Complete × Total Budget

Example:
Project Budget: $100K
Should be 50% complete: PV = 0.50 × $100K = $50K
Actually 45% complete: EV = 0.45 × $100K = $45K

SPI = $45K / $50K = 0.90

Interpretation:
SPI = 1.0 → On schedule
SPI > 1.0 → Ahead of schedule (1.1 = 10% ahead)
SPI < 1.0 → Behind schedule (0.9 = 10% behind)
```

**Schedule Variance (SV)**:
```
SV = EV - PV = $45K - $50K = -$5K

Negative → Behind schedule
Zero → On schedule
Positive → Ahead of schedule

SV in time = SV / (Budget / Duration)
= -$5K / ($100K / 100 days) = -5 days behind
```

**Percent Complete**:
```
Methods:
1. 0/100 Rule: 0% until done, 100% when complete
2. 50/50 Rule: 50% at start, 50% at completion
3. Weighted Milestone: % based on milestones achieved
4. Actual % Complete: Expert estimate

Recommendation: Use consistent method across all tasks
```

### Cost KPIs

**Cost Performance Index (CPI)**:
```
CPI = EV / AC

Where:
- AC (Actual Cost) = Money actually spent

Example:
EV = $45K (45% complete of $100K project)
AC = $50K (actually spent so far)

CPI = $45K / $50K = 0.90

Interpretation:
CPI = 1.0 → On budget
CPI > 1.0 → Under budget (1.1 = getting $1.10 value per $1 spent)
CPI < 1.0 → Over budget (0.9 = getting $0.90 value per $1 spent)
```

**Estimate at Completion (EAC)**:
```
Multiple formulas depending on assumptions:

1. Current CPI will continue:
   EAC = BAC / CPI
   = $100K / 0.90 = $111,111

2. Atypical variance (one-time issue):
   EAC = AC + (BAC - EV)
   = $50K + ($100K - $45K) = $105K

3. Both SPI and CPI influence future:
   EAC = AC + [(BAC - EV) / (SPI × CPI)]
   = $50K + [($100K - $45K) / (0.90 × 0.90)]
   = $50K + ($55K / 0.81) = $117,901

Use formula #1 for typical projects
```

**Variance at Completion (VAC)**:
```
VAC = BAC - EAC = $100K - $111K = -$11K

Expect to finish $11K over budget

If positive → Under budget
If negative → Over budget
```

**To-Complete Performance Index (TCPI)**:
```
TCPI = (BAC - EV) / (BAC - AC)
     = ($100K - $45K) / ($100K - $50K)
     = $55K / $50K = 1.10

Interpretation:
Need to achieve CPI of 1.10 for remaining work to stay on budget
If TCPI > 1.2, very difficult to recover
```

**Burn Rate**:
```
Burn Rate = Actual Cost / Time Elapsed
= $50K / 50 days = $1,000/day

Runway = Remaining Budget / Burn Rate
= ($100K - $50K) / $1,000/day = 50 days

If burn rate increases, runway decreases
```

### Quality KPIs

**Test Coverage**:
```
Test Coverage = (Lines Covered by Tests / Total Lines of Code) × 100%
Target: >80%

Example: 8,200 lines covered / 10,000 total = 82% ✅
```

**Defect Density**:
```
Defect Density = Total Defects / Size (KLOC)

Example: 15 defects in 10,000 lines = 1.5 defects/KLOC
Target: <2 defects/KLOC ✅

Trend over time more important than absolute number
```

**Defect Removal Efficiency (DRE)**:
```
DRE = Defects Found Pre-Release / Total Defects × 100%

Example:
Found in testing: 45
Found in production: 5
Total: 50

DRE = 45 / 50 = 90%
Target: >95%
```

**Code Review Coverage**:
```
% of commits reviewed = Reviewed Commits / Total Commits × 100%
Target: 100%
```

**Build Success Rate**:
```
% successful builds = Successful Builds / Total Builds × 100%
Target: >90%

Example: 94 success / 100 total = 94% ✅
```

### Productivity KPIs (Agile)

**Velocity** (Story Points per Sprint):
```
Sprint 1: 25 points
Sprint 2: 28 points
Sprint 3: 32 points

Average: (25 + 28 + 32) / 3 = 28.3 points/sprint

Use for forecasting:
Remaining: 140 points
Sprints needed: 140 / 28.3 = 4.95 ≈ 5 sprints
Timeline: 5 × 2 weeks = 10 weeks
```

**Cycle Time**:
```
Cycle Time = Time from "In Progress" to "Done"

Average across tasks:
Task A: 3 days
Task B: 5 days
Task C: 2 days
Task D: 4 days
Average: 3.5 days

Lower is better (faster delivery)
Monitor trend: improving or degrading?
```

**Lead Time**:
```
Lead Time = Time from "Created" to "Done"

Includes time in backlog before work starts
Always >= Cycle Time

Lead Time = Queue Time + Cycle Time
```

**Throughput**:
```
Throughput = Tasks Completed / Time Period

Example: 18 tasks completed this week
Last week: 14 tasks

Trend: Increasing ✅
```

### Risk KPIs

**Risk Exposure**:
```
Risk Exposure = Σ (Probability × Impact)

Example:
Risk 1: 0.5 × 4 = 2.0
Risk 2: 0.3 × 5 = 1.5
Risk 3: 0.7 × 2 = 1.4
Total: 4.9

Track weekly: decreasing trend indicates effective mitigation
```

**Risk Velocity**:
```
Average days from risk identification to mitigation plan
Target: <7 days

Example:
Risk A: 2 days
Risk B: 5 days
Risk C: 3 days
Average: 3.3 days ✅
```

---

## RAG Status (Red-Amber-Green)

### Criteria

**🟢 Green (On Track)**:
- Schedule: SPI ≥ 0.95 (within 5%)
- Budget: CPI ≥ 0.95 (within 5%)
- Scope: No unapproved changes
- Quality: All metrics meeting targets
- Risks: All high risks have active mitigation

**🟡 Yellow (At Risk / Caution)**:
- Schedule: 0.90 ≤ SPI < 0.95 (5-10% variance)
- Budget: 0.90 ≤ CPI < 0.95 (5-10% variance)
- Scope: Minor changes under review
- Quality: 1-2 metrics below target
- Risks: Some high risks, mitigation in progress

**🔴 Red (Off Track / Critical)**:
- Schedule: SPI < 0.90 (>10% behind)
- Budget: CPI < 0.90 (>10% over budget)
- Scope: Major uncontrolled scope creep
- Quality: Multiple critical quality issues
- Risks: Critical risks without adequate mitigation

### Overall Project RAG

Use **most conservative** status:
```
Schedule: 🟢 (SPI = 0.98)
Budget: 🟡 (CPI = 0.92)
Scope: 🟢 (No changes)
Quality: 🟢 (All green)
Risks: 🟡 (2 high risks)

Overall: 🟡 YELLOW
```

---

## Visualization Best Practices

### Burndown Chart
```
Story Points Remaining

120 |●
100 |  ●
 80 |    ●●              Ideal Trend: Linear decrease
 60 |       ●●           Actual: Should track near ideal
 40 |          ●●        Above ideal: Behind schedule
 20 |             ●●     Below ideal: Ahead of schedule
  0 |________________●
    S1 S2 S3 S4 S5 S6 S7

● Actual  ── Ideal
```

### Burnup Chart
```
Story Points Completed

150 |                   ─── Total Scope (may change)
120 |              ●●●──
100 |          ●●●
 80 |       ●●             Shows: Progress + Scope changes
 60 |    ●●                Better than burndown for changing scope
 40 |  ●●
 20 | ●
  0 |●____________________
    S1 S2 S3 S4 S5 S6 S7

● Completed  ─── Total Scope
```

### Cumulative Flow Diagram (CFD)
```
           ┌──────── Done (green)
           │┌─────── In Review (yellow)
           ││┌────── In Progress (blue)
           │││┌───── To Do (gray)
Tasks      ││││
50 │       ││││
40 │      ││││
30 │     ││││
20 │    ││││
10 │   ││││
 0 ││││││││
   W1 W2 W3 W4

Healthy: Bands grow at similar rates, stable WIP
Unhealthy: Bands widening (bottleneck), WIP increasing
```

### S-Curve (Earned Value)
```
Cumulative Cost ($K)

300 |              ╱─── Actual Cost (AC)
250 |           ╱─╱──── Planned Value (PV)
200 |        ╱─╱─────── Earned Value (EV)
150 |     ╱─╱
100 |  ╱─╱
 50 |╱─╱
  0 +────────────────
   J F M A M J

EV below PV: Behind schedule
AC above EV: Over budget
```

---

## Communication Best Practices

### Tailor Message to Audience

**Executives**:
- ✅ Start with status (RAG)
- ✅ Highlight decisions needed
- ✅ Business impact and ROI
- ✅ 1-page maximum
- ❌ Technical details
- ❌ Low-level tasks
- ❌ Team drama

**Management**:
- ✅ Progress vs plan
- ✅ Resource needs
- ✅ Risk mitigation
- ✅ Budget tracking
- ✅ 2-4 pages
- ❌ Technical implementation
- ❌ Daily minutiae

**Team**:
- ✅ Detailed task status
- ✅ Blockers and dependencies
- ✅ Technical details
- ✅ Recognition
- ✅ As detailed as needed
- ❌ Office politics
- ❌ Budget details

### Transparency and Honesty

**Good**:
- "We're 2 weeks behind due to X. Here's our recovery plan."
- "Budget is 10% over. Caused by Y. Mitigation: Z."
- "Risk #5 occurred. Impact: A. Response: B. Timeline adjusted."

**Bad**:
- "Everything is fine." (when it's not)
- "We'll make it up." (with no plan)
- "Just a small delay." (when it's significant)
- Hiding problems hoping they'll resolve

### Be Action-Oriented

Every issue should include:
- **Impact**: What happens if not resolved?
- **Owner**: Who is responsible?
- **Due Date**: When must this be resolved?
- **Plan**: What are we doing?
- **Status**: Where are we in execution?

❌ "Third-party API is unreliable"
✅ "Third-party API outages could lose $20K revenue per incident. Implementing circuit breaker failover (John, due Sprint 3) to reduce impact to <$2K. Design complete, development 30% done."

### Use Data, Not Opinions

❌ "Project is going well"
✅ "Project 42% complete vs 40% baseline. SPI = 1.05 (5% ahead). Velocity increased 29% this week."

❌ "Team is working hard"
✅ "Team completed 18 of 16 planned tasks. Burn rate on target at $21K/week."

---

## Report Timing and Distribution

### Weekly Status
- **When**: Every Friday by 5pm
- **To**: PM, team, active stakeholders
- **Format**: Email with attached report
- **Meeting**: Optional 15-min review at standup

### Monthly Status
- **When**: First Monday of new month
- **To**: Management, steering committee, all stakeholders
- **Format**: Email + presentation for meeting
- **Meeting**: 30-60 min review meeting

### Executive Summary
- **When**: Monthly or at milestones
- **To**: Sponsor, executives
- **Format**: 1-page email or attached PDF
- **Meeting**: Only if decisions needed

### Exception Reports (Red Status)
- **When**: Immediately when critical issue arises
- **To**: Sponsor, steering committee
- **Format**: Email with concise situation/impact/plan
- **Meeting**: Schedule ASAP (within 24 hours)

---

## Templates

Templates in `plugins/project-manager/templates/`:
- `status-report-template.docx`: Pre-formatted Word doc
- Project-plan with baseline metrics
- Risk register for Top Risks section

---

## Common Reporting Mistakes

1. **Reporting Late**: Damages credibility, makes problems worse
2. **Inconsistent Format**: Different structure each time confuses readers
3. **Too Much Detail**: 10-page reports don't get read
4. **Too Little Detail**: "All good" doesn't help stakeholders
5. **No Trends**: Snapshot without context is meaningless
6. **Hiding Bad News**: Destroys trust when discovered
7. **No Actions**: Reporting problems without solutions
8. **Metrics Without Context**: "CPI = 0.92" means nothing without explanation
9. **Stale Data**: Using week-old data for weekly report
10. **No Follow-Up**: Action items from last report not reviewed

---

**This skill is continuously updated with lessons learned from effective (and ineffective) project communication across thousands of projects.**
