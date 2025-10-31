# Process Improvement Skill

## Overview
Comprehensive patterns for process mapping, bottleneck analysis, automation identification, and ROI calculation.

## Process Mapping Framework

### Process Documentation Elements
1. **Process Name**: Clear, descriptive name
2. **Purpose**: Why this process exists
3. **Trigger**: What starts the process
4. **Steps**: Sequential actions
5. **Stakeholders**: Roles involved
6. **Outputs**: What's produced
7. **Success Criteria**: How to know it worked

### Swimlane Diagrams (Markdown)

```
| Step | Owner | Action | Time | Issues |
|------|-------|--------|------|--------|
| 1 | Customer | Submit request | 5 min | - |
| 2 | Sales | Review request | 30 min | Manual review |
| → | (Handoff) | Email to CS | - | Delay |
| 3 | CS | Create ticket | 10 min | Manual entry |
```

## Bottleneck Analysis

### Common Bottlenecks
1. **Wait Time**: Delays between steps (handoffs, approvals)
2. **Resource Constraints**: Not enough people/capacity
3. **Manual Work**: Repetitive tasks that could be automated
4. **Rework**: Errors requiring correction
5. **Dependencies**: Waiting for external inputs

### Analysis Methods
- **Cycle Time**: Total time from start to finish
- **Touch Time**: Actual work time
- **Wait Time**: Cycle Time - Touch Time
- **Efficiency**: Touch Time / Cycle Time × 100%

Target: >80% efficiency (touch time)

## Automation Opportunity Assessment

### High-Value Automation Criteria
Score each process (0-5 points per criterion):
- **Frequency**: >5x/week = 5 pts
- **Time per instance**: >30 min = 5 pts
- **Error rate**: >5% = 5 pts
- **Rule-based**: Clear logic = 5 pts
- **Volume**: >50 people affected = 5 pts

**Total Score**:
- 20-25: High priority (automate ASAP)
- 15-19: Medium priority
- <15: Low priority or not suitable

### Automation Types
1. **RPA**: Robotic Process Automation (UI automation)
2. **Integration**: API connections between systems
3. **Workflow**: No-code workflow tools (Zapier, n8n)
4. **Scripts**: Custom automation code
5. **AI/ML**: Intelligent automation

## ROI Calculation Framework

### Standard Formula

**Annual Savings**:
```
Hours Saved/Month × Frequency × Hourly Rate × 12 months
```

**Implementation Cost**:
```
Development Hours × Dev Rate + Tool Cost + Training Cost
```

**Payback Period**:
```
Implementation Cost / Monthly Savings
```

**3-Year ROI**:
```
(3-Year Savings - 3-Year Cost) / Implementation Cost × 100%
```

### Conservative Estimation
- Use low-end time savings (75% of expected)
- Include hidden costs (maintenance, training)
- Account for adoption curve (not 100% from day 1)
- Add contingency buffer (20%)

### Fully Loaded Labor Cost
Base salary × 1.4 (benefits, overhead) ÷ 2080 hours = Hourly rate

## Implementation Prioritization

### Impact vs Effort Matrix

```
High Impact, Low Effort = QUICK WINS (do first)
High Impact, High Effort = STRATEGIC (plan carefully)
Low Impact, Low Effort = NICE TO HAVE (if time permits)
Low Impact, High Effort = AVOID (don't do)
```

### Quick Win Criteria
- <3 months payback
- <40 hours implementation
- High user demand
- Low technical risk
- Clear success metrics

## Continuous Improvement

### PDCA Cycle
1. **Plan**: Identify problem, plan improvement
2. **Do**: Implement on small scale
3. **Check**: Measure results
4. **Act**: Standardize if successful, adjust if not

### Key Metrics
- Cycle time reduction
- Error rate improvement
- Cost per transaction
- Customer satisfaction
- Employee satisfaction

## Common Process Wastes (Lean)

1. **Defects**: Errors requiring rework
2. **Overproduction**: Doing more than needed
3. **Waiting**: Delays and idle time
4. **Non-utilized talent**: People not working at skill level
5. **Transportation**: Unnecessary movement of data/materials
6. **Inventory**: Work in progress piling up
7. **Motion**: Unnecessary steps or clicks
8. **Extra processing**: More work than necessary
