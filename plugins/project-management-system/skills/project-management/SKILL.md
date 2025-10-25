# Project Management Skill

**Version**: 1.0.0
**Last Updated**: 2025-01-21
**Category**: Project Management

## Overview

This skill provides comprehensive project management methodologies, frameworks, and best practices for managing projects from initiation through closure. It covers Work Breakdown Structures (WBS), dependency mapping, resource allocation, risk management, and project lifecycle phases.

## When to Use This Skill

Use this skill when:
- Planning a new project
- Creating Work Breakdown Structures
- Mapping task dependencies
- Allocating resources to tasks
- Identifying and managing project risks
- Creating project dashboards and status reports
- Archiving completed projects
- Conducting lessons learned sessions

## Core Methodologies

### Project Lifecycle Phases

All projects follow this standard lifecycle:

```
Initiation → Planning → Execution → Monitoring & Control → Closure
```

#### 1. Initiation Phase

**Purpose**: Define project at high level, obtain authorization

**Key Activities**:
- Develop project charter
- Identify stakeholders
- Define high-level scope
- Conduct feasibility study
- Secure project approval

**Deliverables**:
- Project charter (signed)
- Stakeholder register
- High-level requirements
- Initial risk assessment
- Business case

**Duration**: Typically 1-2 weeks for medium projects

#### 2. Planning Phase

**Purpose**: Establish scope, objectives, and course of action

**Key Activities**:
- Define detailed scope
- Create Work Breakdown Structure (WBS)
- Sequence activities and identify dependencies
- Estimate resources and durations
- Develop schedule and budget
- Plan quality, risk, communications
- Obtain plan approval

**Deliverables**:
- Project management plan
- WBS
- Schedule (Gantt chart)
- Budget
- Resource plan
- Risk register
- Communication plan
- Quality management plan

**Duration**: Typically 2-4 weeks for medium projects

#### 3. Execution Phase

**Purpose**: Complete work defined in project management plan

**Key Activities**:
- Direct and manage project work
- Manage team performance
- Conduct procurements
- Manage stakeholder engagement
- Implement quality assurance
- Execute communications plan

**Deliverables**:
- Project deliverables (product/service)
- Work performance data
- Change requests
- Quality reports
- Status reports

**Duration**: Typically 60-80% of total project time

#### 4. Monitoring & Control Phase

**Purpose**: Track, review, and regulate progress and performance

**Key Activities** (ongoing throughout execution):
- Monitor project work
- Perform integrated change control
- Validate and control scope
- Control schedule and costs
- Control quality
- Monitor risks
- Control communications

**Deliverables**:
- Work performance reports
- Change log
- Updated project documents
- Risk register updates
- Status dashboards

**Duration**: Parallel with Execution phase

#### 5. Closure Phase

**Purpose**: Finalize all activities to formally close project

**Key Activities**:
- Verify all deliverables complete
- Obtain final acceptance
- Transfer deliverables
- Release resources
- Document lessons learned
- Archive project information
- Celebrate success

**Deliverables**:
- Final project report
- Lessons learned document
- Project archive
- Formal acceptance
- Team recognition

**Duration**: Typically 1-2 weeks

## Work Breakdown Structure (WBS)

### WBS Principles

The WBS is a hierarchical decomposition of the total scope of work.

**Key Principles**:
1. **100% Rule**: WBS includes 100% of work (no more, no less)
2. **Mutually Exclusive**: No overlap between elements
3. **Outcome-Oriented**: Focus on deliverables, not activities
4. **Level of Detail**: Decompose to level that allows estimation and assignment
5. **8/80 Rule**: Work packages should be 8-80 hours of effort

### WBS Structure Levels

```
Level 0: Project (entire project)
Level 1: Major Deliverables or Phases
Level 2: Sub-deliverables or Major Tasks
Level 3: Work Packages
Level 4: Activities (optional, detailed level)
```

### WBS Decomposition Approaches

#### Approach 1: Phase-Based
Organize by project lifecycle phases:
```
1. Initiation
2. Planning
3. Design
4. Development
5. Testing
6. Deployment
7. Closure
```

**Best for**: Projects with clear sequential phases

#### Approach 2: Deliverable-Based
Organize by major deliverables:
```
1. Requirements Document
2. System Architecture
3. Database
4. Backend API
5. Frontend Application
6. Documentation
7. Training Materials
```

**Best for**: Product development projects

#### Approach 3: Functional Area
Organize by functional departments:
```
1. Project Management
2. Engineering
3. Quality Assurance
4. Documentation
5. Training
```

**Best for**: Cross-functional projects

### WBS Numbering Convention

Use hierarchical numbering for traceability:
```
1.0 Project Initiation
  1.1 Project Charter
    1.1.1 Define objectives
    1.1.2 Identify stakeholders
    1.1.3 Obtain approval
  1.2 Kickoff Meeting
    1.2.1 Prepare presentation
    1.2.2 Conduct meeting
    1.2.3 Document action items

2.0 Requirements & Planning
  2.1 Requirements Gathering
    2.1.1 Stakeholder interviews
    2.1.2 Document requirements
    2.1.3 Requirements approval
```

### Work Package Definition Template

For each work package, define:

```markdown
**Task ID**: [Unique identifier, e.g., DEV-001]
**Task Name**: [Descriptive name]
**Description**: [What work will be done]
**Duration**: [Calendar time needed]
**Effort**: [Person-days of work]
**Assigned To**: [Team member(s)]
**Dependencies**: [What must complete first]
**Deliverable**: [Tangible output]
**Acceptance Criteria**: [How to know it's done]
**Status**: [Not Started | In Progress | Blocked | Complete]
**% Complete**: [0-100%]
**Notes**: [Additional context]
```

## Dependency Mapping

### Types of Dependencies

#### 1. Finish-to-Start (FS) - Most Common
Task B cannot start until Task A finishes.
```
Task A ──> Task B
```
**Example**: Design must finish before development starts

#### 2. Start-to-Start (SS)
Task B cannot start until Task A starts.
```
Task A
  └──> Task B
```
**Example**: Frontend and backend development can start together

#### 3. Finish-to-Finish (FF)
Task B cannot finish until Task A finishes.
```
Task A ──┐
Task B ──┘
```
**Example**: Testing cannot finish until development finishes

#### 4. Start-to-Finish (SF) - Rare
Task B cannot finish until Task A starts.
```
Task A ──> Task B (finish)
```
**Example**: Old system support cannot end until new system goes live

### Dependency Categories

#### Mandatory Dependencies (Hard Logic)
Inherent in nature of work, cannot be changed.
- **Example**: Foundation must be poured before walls built

#### Discretionary Dependencies (Soft Logic)
Defined by project team based on best practices.
- **Example**: Preferring to complete all design before starting development

#### External Dependencies
Outside project team's control.
- **Example**: Waiting for third-party API access

#### Internal Dependencies
Within project team's control.
- **Example**: Database schema before API development

### Critical Path Method (CPM)

The **Critical Path** is the longest sequence of dependent tasks that determines minimum project duration.

**Critical Path Characteristics**:
- Tasks have zero float/slack (no room for delay)
- Any delay on critical path delays entire project
- Focus resource and management attention here
- Typically 20-30% of all project tasks

**Calculating Critical Path**:
1. List all tasks with durations
2. Identify dependencies
3. Calculate Early Start (ES) and Early Finish (EF) for each task
4. Calculate Late Start (LS) and Late Finish (LF) working backward
5. Calculate Float: `Float = LS - ES` or `LF - EF`
6. Tasks with zero float form critical path

**Managing Critical Path**:
- **Fast-Tracking**: Do tasks in parallel (increases risk)
- **Crashing**: Add resources to shorten duration (increases cost)
- **Monitoring**: Track critical path tasks daily
- **Buffer**: Add contingency time at end of critical path

### Dependency Notation

Use standard notation in WBS:
```
Dependencies: TASK-001, TASK-002  # Both must complete first
Dependencies: TASK-001 (SS)       # Start-to-start
Dependencies: TASK-002 (FF)       # Finish-to-finish
Dependencies: None                # Can start immediately
```

## Resource Allocation

### Resource Types

#### 1. Human Resources
- **Roles**: Developers, Designers, PMs, QA, etc.
- **Measurement**: Full-Time Equivalent (FTE), hours, % allocation

#### 2. Equipment
- **Examples**: Servers, laptops, testing devices
- **Measurement**: Units, cost, availability

#### 3. Materials
- **Examples**: Software licenses, cloud credits
- **Measurement**: Quantity, cost

#### 4. Budget
- **Measurement**: Currency, cost centers

### Resource Allocation Principles

#### 1. Skill Matching
Assign resources based on required skills:
- **Senior Developer**: Complex architecture, technical leadership
- **Mid-Level Developer**: Standard features, moderate complexity
- **Junior Developer**: Simple tasks, with mentorship

#### 2. Availability Consideration
Account for:
- **Vacation/PTO**: Plan around known absences
- **Other Projects**: Multi-project allocation
- **Meetings/Overhead**: Typically 15-20% of time
- **Ramp-Up Time**: New team members need time to get productive

#### 3. Resource Leveling
Smooth resource usage over time to avoid:
- **Over-allocation**: >100% of resource capacity
- **Under-utilization**: Significant idle time
- **Resource conflicts**: Same person needed in two places

**Resource Leveling Techniques**:
- **Delay non-critical tasks**: Use float/slack
- **Split tasks**: Do part now, part later
- **Reduce scope**: If over-allocated, reduce work
- **Add resources**: Hire contractors, reallocate team

#### 4. Resource Loading
Calculate resource usage over time:

```
Week 1: Developer A (80%), Developer B (60%) = 1.4 FTE
Week 2: Developer A (100%), Developer B (100%) = 2.0 FTE
Week 3: Developer A (100%), Developer B (40%) = 1.4 FTE
```

**Resource Histogram**: Visual chart showing resource usage per time period

### Effort Estimation Techniques

#### 1. Expert Judgment
Subject matter expert provides estimate based on experience.
- **Pros**: Fast, leverages experience
- **Cons**: Can be biased, single point of view

#### 2. Analogous Estimation (Top-Down)
Use historical data from similar past projects.
- **Formula**: `New Project Estimate = Similar Project Actual × Adjustment Factor`
- **Pros**: Quick, useful early in project
- **Cons**: Requires similar historical data

#### 3. Parametric Estimation
Use statistical relationship between historical data and variables.
- **Example**: `Effort = Number of Features × 8 hours per feature`
- **Pros**: Accurate if good historical data
- **Cons**: Requires robust historical database

#### 4. Three-Point Estimation (PERT)
Use optimistic, most likely, and pessimistic estimates.
- **Formula**: `Expected = (Optimistic + 4×Most Likely + Pessimistic) / 6`
- **Example**:
  - Optimistic: 5 days
  - Most Likely: 8 days
  - Pessimistic: 15 days
  - **Expected**: (5 + 4×8 + 15) / 6 = 8.3 days
- **Pros**: Accounts for uncertainty
- **Cons**: Requires three estimates per task

#### 5. Bottom-Up Estimation
Estimate each work package, then sum to higher levels.
- **Process**: Estimate lowest level tasks, aggregate upward
- **Pros**: Most accurate
- **Cons**: Time-consuming, requires detailed breakdown

### Effort vs Duration

**Critical Distinction**:
- **Effort**: Total work hours required (e.g., 40 person-hours)
- **Duration**: Calendar time to complete (e.g., 5 days)

**Relationship**:
```
Duration = Effort / (Number of Resources × Availability)
```

**Example**:
- Effort: 40 hours
- Resources: 2 developers at 80% availability each
- Duration: 40 / (2 × 0.8) = 25 hours = 3.1 days

## Risk Management

### Risk Identification

**Common Project Risks**:

#### Schedule Risks
- Optimistic estimates
- Scope creep
- Dependencies on external parties
- Resource availability
- Technical complexity underestimated

#### Budget Risks
- Inaccurate cost estimates
- Exchange rate fluctuations
- Vendor cost increases
- Scope changes

#### Technical Risks
- Unproven technology
- Integration complexity
- Performance requirements
- Security vulnerabilities
- Technical debt

#### Resource Risks
- Key person dependency
- Skill gaps
- Team turnover
- Competing priorities

#### External Risks
- Regulatory changes
- Market conditions
- Vendor stability
- Natural disasters

### Risk Assessment

#### Impact Scale (1-5)
1. **Minimal**: Negligible impact on project
2. **Minor**: Slight impact, easily absorbed
3. **Moderate**: Noticeable impact, some mitigation needed
4. **Major**: Significant impact, requires management attention
5. **Severe**: Critical impact, threatens project success

#### Probability Scale (1-5)
1. **Very Low**: <10% chance
2. **Low**: 10-30% chance
3. **Medium**: 30-50% chance
4. **High**: 50-70% chance
5. **Very High**: >70% chance

#### Risk Score
```
Risk Score = Impact × Probability
```

**Risk Priority**:
- **High**: Score 15-25 (red)
- **Medium**: Score 8-14 (yellow)
- **Low**: Score 1-7 (green)

### Risk Response Strategies

#### For Threats (Negative Risks)

1. **Avoid**: Eliminate the risk by changing plan
   - Example: Use proven technology instead of new framework

2. **Mitigate**: Reduce probability or impact
   - Example: Prototype complex feature early

3. **Transfer**: Shift impact to third party
   - Example: Purchase insurance, use vendor warranty

4. **Accept**: Acknowledge but take no action
   - Example: Low-priority, low-impact risks
   - Active Acceptance: Create contingency plan
   - Passive Acceptance: Deal with it if it happens

#### For Opportunities (Positive Risks)

1. **Exploit**: Ensure opportunity happens
   - Example: Assign best resources to maximize quality

2. **Enhance**: Increase probability or impact
   - Example: Add features to exceed expectations

3. **Share**: Partner with others to benefit
   - Example: Joint venture for shared success

4. **Accept**: Don't actively pursue but be ready
   - Example: If market conditions improve, expand scope

### Risk Register Template

```markdown
## Risk Register

### Risk ID: R-001
**Risk**: Requirements may change during development
**Category**: Scope
**Probability**: High (60%)
**Impact**: Major (4)
**Risk Score**: 24 (HIGH)
**Status**: Active

**Response Strategy**: Mitigate
**Mitigation Actions**:
- Implement strict change control process
- Weekly stakeholder reviews to catch changes early
- Include 15% contingency buffer in schedule

**Owner**: Project Manager
**Contingency Plan**: If major change occurs, convene steering committee for scope/budget/timeline adjustment
**Status Updates**: [Track over time]
```

## Status Reporting

### Project Health Indicators

#### RAG Status (Red-Amber-Green)

**Green (On Track)**:
- Schedule: Within 5% of plan
- Budget: Within 5% of plan
- Scope: No unapproved changes
- Quality: Meeting standards
- Risks: All risks managed

**Amber (At Risk)**:
- Schedule: 5-10% variance
- Budget: 5-10% variance
- Scope: Pending change requests
- Quality: Minor issues
- Risks: Medium risks present

**Red (Off Track)**:
- Schedule: >10% variance
- Budget: >10% variance
- Scope: Unapproved changes made
- Quality: Major issues
- Risks: High risks materialized

### Variance Analysis

#### Schedule Variance (SV)
```
SV = Actual Progress - Planned Progress
```
- Positive: Ahead of schedule
- Negative: Behind schedule

#### Cost Variance (CV)
```
CV = Budgeted Cost - Actual Cost
```
- Positive: Under budget
- Negative: Over budget

#### Variance Percentage
```
Variance % = (Actual - Planned) / Planned × 100%
```

## Best Practices

### 1. Planning Best Practices

- **Start with Why**: Clearly articulate project purpose and value
- **Engage Stakeholders Early**: Get buy-in before detailed planning
- **Plan at Right Level**: Not too detailed (micromanagement), not too high (no clarity)
- **Build in Buffers**: Add 15-20% contingency for unknowns
- **Document Assumptions**: Make implicit assumptions explicit
- **Define "Done"**: Clear acceptance criteria for every deliverable

### 2. Execution Best Practices

- **Daily Standups**: 15-minute team sync (what done, what today, blockers)
- **Regular Stakeholder Updates**: Weekly or bi-weekly demos/reviews
- **Track Issues Immediately**: Don't let problems fester
- **Celebrate Wins**: Recognize progress and achievements
- **Communicate Proactively**: Bad news early is better than late surprises

### 3. Monitoring Best Practices

- **Use Visual Dashboards**: Make status immediately visible
- **Track Leading Indicators**: Velocity, cycle time, not just % complete
- **Regular Reviews**: Weekly team review, monthly stakeholder review
- **Update Frequently**: Real-time or daily updates preferred
- **Root Cause Analysis**: Understand why, not just what happened

### 4. Risk Management Best Practices

- **Identify Risks Early**: Brainstorm during planning
- **Review Risks Regularly**: Weekly risk review
- **Focus on High Priority**: Don't over-manage low risks
- **Monitor Triggers**: Watch for early warning signs
- **Update Register**: Keep risk status current

### 5. Team Management Best Practices

- **Clear Roles**: Everyone knows their responsibilities
- **Empowerment**: Give team authority to make decisions
- **Remove Blockers**: PM's job to clear obstacles
- **Provide Context**: Help team understand "why"
- **Psychological Safety**: Team can raise concerns without fear

## Common Pitfalls to Avoid

### 1. Planning Pitfalls
- ❌ **Gold-plating**: Planning in excessive detail too early
- ❌ **Skipping Planning**: "We'll figure it out as we go"
- ❌ **Ignoring Risks**: "That probably won't happen"
- ❌ **Optimistic Estimates**: Best-case scenario estimates
- ❌ **No Stakeholder Buy-in**: Planning in isolation

### 2. Execution Pitfalls
- ❌ **Scope Creep**: Accepting every change request
- ❌ **Hero Culture**: Relying on individuals working overtime
- ❌ **Poor Communication**: Assuming people know what you know
- ❌ **Ignoring Early Warnings**: "It'll work itself out"
- ❌ **No Change Control**: Free-for-all on requirements

### 3. Monitoring Pitfalls
- ❌ **Vanity Metrics**: Tracking meaningless numbers
- ❌ **No Baseline**: Can't measure variance without baseline
- ❌ **Infrequent Updates**: Monthly status on fast project
- ❌ **Hiding Problems**: Only reporting good news
- ❌ **Analysis Paralysis**: Spending more time reporting than doing

## Templates & Checklists

### Project Charter Template

```markdown
# Project Charter: [Project Name]

## Business Case
[Why this project? What problem does it solve?]

## Objectives
1. [SMART objective 1]
2. [SMART objective 2]

## Scope
**In Scope**:
- [Item 1]
- [Item 2]

**Out of Scope**:
- [Item 1]
- [Item 2]

## Stakeholders
| Name | Role | Interest | Influence |
|------|------|----------|-----------|
| | | High/Med/Low | High/Med/Low |

## Success Criteria
- [ ] [Measurable criterion 1]
- [ ] [Measurable criterion 2]

## High-Level Timeline
- Start: [Date]
- Major Milestones: [Dates]
- Target Completion: [Date]

## Budget
Estimated: $[Amount]

## Approval
| Name | Role | Signature | Date |
|------|------|-----------|------|
| | Executive Sponsor | | |
| | Project Manager | | |
```

### WBS Checklist

- [ ] Each work package has unique ID
- [ ] Each work package has owner assigned
- [ ] Duration and effort estimated for all tasks
- [ ] Dependencies documented
- [ ] Deliverables specified
- [ ] Acceptance criteria defined
- [ ] WBS covers 100% of scope (no more, no less)
- [ ] Work packages sized 8-80 hours
- [ ] Critical path identified
- [ ] Resource allocation complete
- [ ] No resource over-allocation
- [ ] Risks identified and assessed

### Status Report Template

```markdown
# Status Report: Week of [Date]

## Executive Summary
Overall Status: 🟢 GREEN | 🟡 AMBER | 🔴 RED

## Accomplishments This Week
- [Achievement 1]
- [Achievement 2]

## Planned for Next Week
- [Plan 1]
- [Plan 2]

## Metrics
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Schedule | Week X | Week Y | 🟢/🟡/🔴 |
| Budget | $X | $Y | 🟢/🟡/🔴 |
| Quality | Z defects | A defects | 🟢/🟡/🔴 |

## Risks & Issues
### High Priority
- **Risk**: [Description]
  - Status: [Update]
  - Mitigation: [Action]

## Blockers
- [Blocker 1 - needs attention]

## Asks/Decisions Needed
- [Decision needed from stakeholder]
```

## References & Further Reading

### Frameworks
- **PMBOK (PMI)**: Project Management Body of Knowledge
- **PRINCE2**: PRojects IN Controlled Environments
- **Agile/Scrum**: For iterative project management
- **Lean/Kanban**: For continuous flow projects

### Key Concepts
- **Iron Triangle**: Scope, Time, Cost (pick 2)
- **Earned Value Management**: Integrated scope, schedule, cost measurement
- **Monte Carlo Simulation**: Risk analysis technique
- **RACI Matrix**: Responsible, Accountable, Consulted, Informed

### Recommended Tools
- **Project Planning**: MS Project, Smartsheet, Asana, Jira
- **Gantt Charts**: Mermaid, MS Project, GanttProject
- **Collaboration**: Slack, Teams, Confluence
- **Documentation**: Notion, Confluence, SharePoint

---

**Skill Version**: 1.0.0
**Maintained By**: Puerto AI Plugin System
**Last Review**: 2025-01-21

This skill should be read at the start of any project management task to ensure consistent, professional application of proven methodologies.
