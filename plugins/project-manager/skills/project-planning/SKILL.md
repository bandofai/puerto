# Project Planning Skill

**Comprehensive project planning methodologies: WBS creation, estimation techniques, scheduling, resource allocation, and project management frameworks (Agile, Waterfall, Hybrid)**

This skill codifies industry best practices from PMI/PMBOK, Agile frameworks, and real-world project delivery across thousands of successful projects.

---

## Core Principles

1. **Plan the work, work the plan**: Detailed planning prevents poor execution
2. **Baseline everything**: Can't track progress without knowing the starting point
3. **Engage stakeholders early**: Buy-in starts with planning involvement
4. **Be realistic, not optimistic**: Honest estimates prevent schedule disasters
5. **Plan for change**: Change is inevitable, plan for how to manage it
6. **Bottom-up beats top-down**: People doing the work provide best estimates
7. **Document assumptions**: Make implicit knowledge explicit
8. **Iterate and refine**: Plans improve as you learn more
9. **Build in buffers**: Murphy's Law applies to every project
10. **Measure everything**: If you can't measure it, you can't manage it

---

## Project Planning Process

### 1. Initiation

**Project Charter**:
```markdown
# Project Charter

**Project Name**: [Name]
**Project Manager**: [Name]
**Sponsor**: [Name]
**Start Date**: [Date]
**Target End Date**: [Date]

## Business Case
Why are we doing this project?
- Problem to solve
- Opportunity to capture
- Strategic alignment
- Expected ROI

## Objectives
SMART objectives (Specific, Measurable, Achievable, Relevant, Time-bound):
1. Deliver [X] by [Date] to achieve [Outcome]
2. Reduce [Y] by [Z%] by [Date]
3. Increase [A] from [B] to [C] by [Date]

## Scope (High-Level)
In Scope:
- Major deliverable 1
- Major deliverable 2

Out of Scope:
- Explicitly excluded items

## Success Criteria
How do we know we've succeeded?
- Metric 1: [Target]
- Metric 2: [Target]
- Stakeholder acceptance

## Assumptions
- Budget available: $X
- Resources available: Y people
- Technology: Z platform

## Constraints
- Fixed deadline: [Date]
- Maximum budget: $X
- Regulatory requirements: [List]

## Stakeholders
| Name | Role | Interest | Influence |
|------|------|----------|-----------|
| CEO | Sponsor | High | High |
| IT Director | Approver | Medium | High |
| End Users | Users | High | Low |

## Authorization
Sponsor Signature: _____________ Date: _______
```

**Stakeholder Analysis**:
```
Power/Interest Grid:

High Power, High Interest (MANAGE CLOSELY):
- Project sponsor
- Steering committee
→ Regular updates, active engagement

High Power, Low Interest (KEEP SATISFIED):
- Senior executives
- Budget approvers
→ Summary reports, minimal burden

Low Power, High Interest (KEEP INFORMED):
- End users
- Support team
→ Regular communication, feedback channels

Low Power, Low Interest (MONITOR):
- Peripheral stakeholders
→ General communications only
```

### 2. Scope Definition

**Scope Statement**:
- **Project deliverables**: Tangible outcomes
- **Acceptance criteria**: How to know deliverable is complete
- **Exclusions**: What's NOT included (prevents scope creep)
- **Constraints**: Limitations we must work within
- **Assumptions**: What we're taking as given

**Requirements Gathering**:
```
Techniques:
- Interviews: One-on-one with key stakeholders
- Workshops: Group sessions for consensus
- Surveys: Broad input from many users
- Observation: Watch current process
- Document analysis: Review existing specs
- Prototyping: Build to learn

Requirements Template:
| ID | Requirement | Priority | Source | Acceptance Criteria |
|----|-------------|----------|--------|---------------------|
| R-001 | User login | Must | Security | 2FA, <2sec response |
| R-002 | Export PDF | Should | Users | All reports exportable |
| R-003 | Dark mode | Could | UX | Theme switchable |
```

**MoSCoW Prioritization**:
- **Must Have**: Non-negotiable, MVP requirements
- **Should Have**: Important but not critical
- **Could Have**: Nice to have if time/budget allows
- **Won't Have**: Explicitly out of scope (this release)

### 3. Work Breakdown Structure (WBS)

**WBS Principles**:
- **100% Rule**: WBS includes 100% of scope (all deliverables)
- **Mutually Exclusive**: No overlap between work packages
- **Outcome-Oriented**: Focus on deliverables, not activities
- **Appropriate Depth**: Level of detail based on control needs
- **8-80 Hour Rule**: Work packages 8-80 hours (1-2 weeks max)

**WBS Decomposition Levels**:
```
Level 1: Project
├── Level 2: Major Deliverables/Phases
    ├── Level 3: Sub-Deliverables
        ├── Level 4: Work Packages
            └── Level 5: Activities (optional, used in schedule)

Example: Website Development Project

1.0 Website Development Project
├── 1.1 Project Management
│   ├── 1.1.1 Initiation
│   ├── 1.1.2 Planning
│   ├── 1.1.3 Monitoring & Control
│   └── 1.1.4 Closure
├── 1.2 Requirements & Design
│   ├── 1.2.1 Stakeholder Interviews
│   ├── 1.2.2 Requirements Document
│   ├── 1.2.3 Wireframes
│   ├── 1.2.4 Visual Design
│   └── 1.2.5 Design Approval
├── 1.3 Development
│   ├── 1.3.1 Frontend Development
│   │   ├── 1.3.1.1 Homepage
│   │   ├── 1.3.1.2 Product Pages
│   │   ├── 1.3.1.3 Shopping Cart
│   │   └── 1.3.1.4 Checkout
│   ├── 1.3.2 Backend Development
│   │   ├── 1.3.2.1 Database Design
│   │   ├── 1.3.2.2 API Development
│   │   ├── 1.3.2.3 Payment Integration
│   │   └── 1.3.2.4 Admin Panel
│   └── 1.3.3 Integration
├── 1.4 Testing
│   ├── 1.4.1 Unit Testing
│   ├── 1.4.2 Integration Testing
│   ├── 1.4.3 UAT
│   ├── 1.4.4 Performance Testing
│   └── 1.4.5 Security Testing
├── 1.5 Deployment
│   ├── 1.5.1 Staging Deployment
│   ├── 1.5.2 Production Deployment
│   ├── 1.5.3 Data Migration
│   └── 1.5.4 Go-Live Support
└── 1.6 Training & Documentation
    ├── 1.6.1 User Documentation
    ├── 1.6.2 Admin Documentation
    ├── 1.6.3 Training Materials
    └── 1.6.4 Training Delivery
```

**WBS Dictionary**:
For each work package, document:
```markdown
## Work Package: 1.3.1.1 Homepage Development

**Description**: Develop responsive homepage with hero section, feature highlights, testimonials, and newsletter signup

**Deliverables**:
- HTML/CSS/JS for homepage
- Responsive design (mobile, tablet, desktop)
- Accessible (WCAG 2.1 AA)
- Integrated with CMS

**Acceptance Criteria**:
- Passes stakeholder review
- Lighthouse score >90
- All accessibility tests pass
- Works in Chrome, Firefox, Safari, Edge

**Resources**:
- Frontend Developer (80 hours)
- Designer review (4 hours)

**Duration**: 2 weeks

**Dependencies**:
- Design mockups complete (1.2.4)
- Development environment setup

**Assumptions**:
- Design assets provided by deadline
- No scope changes during development

**Risks**:
- Design iteration delays
- Browser compatibility issues
```

### 4. Estimation Techniques

#### Three-Point Estimation (PERT)

**Formula**:
```
Expected Duration (E) = (Optimistic + 4×Most Likely + Pessimistic) / 6
Standard Deviation (σ) = (Pessimistic - Optimistic) / 6
```

**Example**:
```
Task: Develop user authentication module

Optimistic (O): 5 days (everything goes perfectly)
Most Likely (M): 8 days (realistic estimate)
Pessimistic (P): 15 days (worst case: integration issues, bugs)

E = (5 + 4×8 + 15) / 6 = (5 + 32 + 15) / 6 = 52 / 6 = 8.67 days

σ = (15 - 5) / 6 = 1.67 days

Use: 9 days with ±2 day buffer
```

**Confidence Levels**:
```
68% confidence: E ± 1σ = 8.67 ± 1.67 = 7 to 10.3 days
95% confidence: E ± 2σ = 8.67 ± 3.34 = 5.3 to 12 days
99.7% confidence: E ± 3σ = 8.67 ± 5.01 = 3.7 to 13.7 days
```

#### Analogous Estimation (Top-Down)

**Approach**: Use historical data from similar projects

**Example**:
```
Previous Project A: 500 KLOC, 12 months, 10 developers
New Project B: 750 KLOC, ?, ?

Simple Scaling:
750 / 500 = 1.5× size
Estimate: 12 × 1.5 = 18 months

Adjusted for:
- Team experience: -10% (team more experienced now)
- Technology familiarity: -5% (same stack)
- Complexity: +20% (more complex requirements)

Adjusted: 18 × (1 - 0.10 - 0.05 + 0.20) = 18 × 1.05 = 18.9 months
Final Estimate: 19 months
```

#### Parametric Estimation

**Approach**: Use statistical relationships (cost per unit)

**Examples**:
```
Software Development:
- 10 hours per function point
- 20 hours per use case
- $150 per hour developer rate

Construction:
- $200 per square foot
- 100 bricks per hour per mason

Manufacturing:
- 5 minutes per unit
- $50 materials per unit

Calculation:
100 function points × 10 hours = 1,000 hours
1,000 hours × $150/hour = $150,000
```

#### Bottom-Up Estimation

**Approach**: Estimate each work package, sum up

**Example**:
```
Work Packages (from WBS):
1.3.1.1 Homepage: 80 hours
1.3.1.2 Product Pages: 120 hours
1.3.1.3 Shopping Cart: 160 hours
1.3.1.4 Checkout: 200 hours

Subtotal Frontend: 560 hours

1.3.2.1 Database: 40 hours
1.3.2.2 API: 200 hours
1.3.2.3 Payment Integration: 80 hours
1.3.2.4 Admin Panel: 100 hours

Subtotal Backend: 420 hours

Total Development: 980 hours

Add Contingency:
- Known risks: +10% = 98 hours
- Unknown unknowns: +15% = 147 hours

Final Estimate: 980 + 98 + 147 = 1,225 hours
```

#### Agile Estimation (Planning Poker)

**Story Points** (Fibonacci: 1, 2, 3, 5, 8, 13, 21):

**Process**:
1. Product owner reads user story
2. Team discusses scope, complexity
3. Each member privately selects card (story points)
4. All reveal simultaneously
5. Discuss discrepancies (highest and lowest explain)
6. Re-vote until consensus

**Example**:
```
User Story: "As a user, I want to reset my password via email"

Developer A: 5 points (straightforward, done before)
Developer B: 13 points (email deliverability concerns, security requirements)

Discussion:
- B raises valid security concerns (rate limiting, token expiry)
- A forgot about email template design

Re-vote:
All agree: 8 points

Reference Stories:
- 3 pts: Simple CRUD operation
- 8 pts: Password reset (our story)
- 13 pts: Payment integration
```

**Velocity Tracking**:
```
Sprint 1: 25 points completed
Sprint 2: 30 points completed
Sprint 3: 28 points completed

Average Velocity: (25 + 30 + 28) / 3 = 27.67 ≈ 28 points/sprint

Total Backlog: 280 points
Sprints Needed: 280 / 28 = 10 sprints
Timeline: 10 sprints × 2 weeks = 20 weeks
```

### 5. Schedule Development

#### Network Diagram (Precedence Diagramming)

**Dependency Types**:
- **Finish-to-Start (FS)**: Task B starts when Task A finishes (most common)
- **Start-to-Start (SS)**: Task B starts when Task A starts
- **Finish-to-Finish (FF)**: Task B finishes when Task A finishes
- **Start-to-Finish (SF)**: Task B finishes when Task A starts (rare)

**Lag and Lead**:
- **Lag**: Delay between tasks (FS + 2 days)
- **Lead**: Overlap between tasks (FS - 2 days)

#### Critical Path Method (CPM)

**Steps**:
1. List all activities with durations and dependencies
2. Draw network diagram
3. Forward pass: Calculate Early Start (ES) and Early Finish (EF)
4. Backward pass: Calculate Late Start (LS) and Late Finish (LF)
5. Calculate Total Float: LF - EF (or LS - ES)
6. Critical Path = tasks with zero float

**Example**:
```
Task A: 5 days, no dependencies
Task B: 3 days, depends on A
Task C: 2 days, depends on A
Task D: 4 days, depends on B and C
Task E: 3 days, depends on D

Forward Pass:
A: ES=0, EF=5
B: ES=5, EF=8 (5+3)
C: ES=5, EF=7 (5+2)
D: ES=8, EF=12 (must wait for both B and C; latest EF is 8)
E: ES=12, EF=15

Backward Pass (start from end):
E: LF=15, LS=12 (15-3)
D: LF=12, LS=8 (12-4)
C: LF=12, LS=10 (12-2) [can start late and still finish on time]
B: LF=8, LS=5 (8-3)
A: LF=5, LS=0 (5-5)

Total Float:
A: 5-5=0 [CRITICAL]
B: 8-8=0 [CRITICAL]
C: 12-7=5 days [can delay 5 days without impacting project]
D: 12-12=0 [CRITICAL]
E: 15-15=0 [CRITICAL]

Critical Path: A → B → D → E (15 days)
```

**Critical Path Implications**:
- Delay on critical path = project delay
- Focus management attention on critical tasks
- Crashing critical path shortens project
- Free float = delay without affecting next task
- Total float = delay without affecting project

#### Resource Leveling

**Problem**: Resources over-allocated

**Example**:
```
Developer X assigned:
Jan 5: Task A (8 hours) + Task B (4 hours) = 12 hours [OVERALLOCATED]

Solutions:
1. Delay Task B (if not critical)
2. Assign Task B to Developer Y
3. Split Task A across 2 days
4. Extend Task B duration (work part-time)
5. Add another resource
```

**Resource Histogram**:
```
Developer A Hours/Day

10 |     ███        [Over-allocated]
 8 | ███ ███ ███ ███ [Fully allocated]
 6 | ███ ███ ███ ███
 4 | ███ ███ ███ ███ ███
 2 | ███ ███ ███ ███ ███ ███
 0 +─────────────────────────
   M   T   W   T   F   M   T
        Week 1        Week 2

Goal: Smooth out peaks, maintain consistent workload
```

### 6. Resource Planning

**Resource Breakdown Structure**:
```
Project Resources
├── Human Resources
│   ├── Project Manager (0.5 FTE)
│   ├── Business Analyst (1.0 FTE)
│   ├── Developers (3.0 FTE)
│   ├── QA Engineer (1.0 FTE)
│   └── Designer (0.5 FTE)
├── Equipment
│   ├── Development Laptops (4)
│   ├── Test Devices (10)
│   └── Servers (Cloud - AWS)
├── Software/Tools
│   ├── IDE Licenses (4)
│   ├── Design Tools (2)
│   ├── Project Management (Jira)
│   └── CI/CD Platform (GitHub Actions)
└── Facilities
    ├── Office Space
    └── Conference Rooms
```

**Skills Matrix**:
```
| Team Member | Role | React | Node | AWS | Testing | Availability |
|-------------|------|-------|------|-----|---------|--------------|
| Alice | Dev | Expert | Advanced | Basic | Intermediate | 100% |
| Bob | Dev | Advanced | Expert | Advanced | Advanced | 100% |
| Carol | QA | Basic | - | - | Expert | 100% |
| Dan | PM | - | - | Basic | - | 50% |

Identify Gaps:
- No expert in AWS (Risk: deployment issues)
- Limited testing skills in dev team (Risk: quality issues)

Mitigation:
- Hire AWS contractor for deployment
- Cross-train Alice in testing
```

**Capacity Planning**:
```
Sprint Capacity Calculation:

Team: 5 developers
Sprint: 2 weeks (10 working days)
Hours/day: 6 (exclude meetings, email, context switching)

Gross Capacity: 5 × 10 × 6 = 300 hours

Deductions:
- Holidays: 2 people × 1 day × 6 hours = -12 hours
- Training: 1 person × 2 days × 6 hours = -12 hours
- Production support: 1 person × 50% × 60 hours = -30 hours

Net Capacity: 300 - 12 - 12 - 30 = 246 hours

If velocity = 35 story points/sprint and historical = 300 hours:
Points per hour: 35 / 300 = 0.117
Adjusted capacity: 246 × 0.117 = 28.8 ≈ 29 story points this sprint
```

### 7. Budget Estimation

**Cost Categories**:
```
Labor Costs:
Role         | Rate      | Hours | Cost
-------------|-----------|-------|----------
PM           | $120/hr   | 400   | $48,000
Sr Developer | $100/hr   | 800   | $80,000
Jr Developer | $70/hr    | 800   | $56,000
QA Engineer  | $80/hr    | 400   | $32,000
Designer     | $90/hr    | 200   | $18,000
                          Total: $234,000

Software/Tools:
Jira: $10/user/month × 6 users × 6 months = $360
AWS: $2,000/month × 6 months = $12,000
Design Tools: $50/month × 6 months = $300
IDE Licenses: $500/year × 4 = $2,000
                          Total: $14,660

Hardware:
Laptops: $2,000 × 4 = $8,000
Test Devices: $500 × 10 = $5,000
                          Total: $13,000

Other:
Office Space: $1,000/month × 6 months = $6,000
Training: $2,000
Travel: $3,000
                          Total: $11,000

Subtotal: $272,660

Contingency Reserve (15%): $40,899
Management Reserve (10% of total): $31,356

Total Budget: $344,915
Round to: $350,000
```

**Cost Baseline**:
Track cumulative planned cost over time for S-curve

---

## Project Methodologies

### Waterfall (Traditional Sequential)

**Best For**:
- Fixed, well-understood requirements
- Regulated industries (FDA, aviation, construction)
- Hardware projects with physical deliverables
- Projects requiring extensive documentation

**Phases**:
1. **Requirements**: Gather and document all requirements
2. **Design**: Create detailed design specifications
3. **Implementation**: Build according to design
4. **Testing**: Verify against requirements
5. **Deployment**: Release to production
6. **Maintenance**: Support and bug fixes

**Pros**:
- Clear structure and milestones
- Extensive documentation
- Easy to understand and explain
- Good for projects with fixed scope

**Cons**:
- Inflexible to change
- Late discovery of issues
- Long time to market
- Customer sees product only at end

**When Requirements Change**:
Use formal change control process with impact analysis

### Agile (Iterative Incremental)

**Best For**:
- Evolving requirements
- Software development
- Innovation projects
- Projects needing frequent feedback

**Core Values** (Agile Manifesto):
- Individuals and interactions > processes and tools
- Working software > comprehensive documentation
- Customer collaboration > contract negotiation
- Responding to change > following a plan

**Scrum Framework**:
```
Sprint Planning (Start) → Daily Standup (Daily) → Sprint Review (End) → Sprint Retro (End)
                ↓                                           ↓
         Sprint Execution (1-4 weeks)              Potentially Shippable Increment

Roles:
- Product Owner: Maximizes product value, manages backlog
- Scrum Master: Facilitates process, removes impediments
- Development Team: Cross-functional, self-organizing

Artifacts:
- Product Backlog: Prioritized list of features
- Sprint Backlog: Committed work for current sprint
- Increment: Working product at sprint end

Ceremonies:
- Sprint Planning: What and how to build this sprint
- Daily Standup: 15-min sync (What did I do? What will I do? Blockers?)
- Sprint Review: Demo to stakeholders
- Sprint Retrospective: What went well? What to improve?
```

**Kanban**:
```
To Do | In Progress (WIP: 3) | In Review (WIP: 2) | Done
------------------------------------------------------
Story | Story A              | Story D            | Story F
Story | Story B              | Story E            | Story G
Story | Story C              |                    | Story H
Story |                      |                    |

Rules:
1. Visualize workflow
2. Limit WIP (prevents multitasking, identifies bottlenecks)
3. Manage flow (optimize cycle time)
4. Make policies explicit
5. Improve collaboratively
```

**XP (Extreme Programming)**:
```
Practices:
- Pair Programming: Two developers, one workstation
- TDD: Write test before code
- Continuous Integration: Integrate daily
- Refactoring: Improve code structure continuously
- Simple Design: Build what's needed now
- Collective Code Ownership: Anyone can change any code
- Coding Standards: Team style guide
- Sustainable Pace: 40-hour weeks (no heroics)
```

### Hybrid (Agile-Waterfall Mix)

**Best For**:
- Large enterprises transitioning to Agile
- Projects with fixed and flexible components
- Regulated industries adopting Agile

**Approach**:
```
Waterfall for:
- Requirements gathering (phase-gate)
- Architecture design (upfront)
- Infrastructure setup (prerequisite)
- Compliance documentation (required)

Agile for:
- Feature development (sprints)
- UI/UX design (iterative)
- Testing (continuous)

Example Timeline:
Months 1-2: Requirements & Architecture (Waterfall)
Months 3-8: Feature Development in 2-week Sprints (Agile)
Month 9: Final Testing & Deployment (Waterfall)
```

**Scaled Agile (SAFe)**:
For large enterprises with multiple Agile teams

---

## Key Documents

1. **Project Charter**: Authorization and high-level scope
2. **Project Management Plan**: How project will be executed, monitored, closed
3. **WBS**: Hierarchical decomposition of deliverables
4. **Schedule**: Timeline with dependencies and milestones
5. **Budget**: Cost estimates and funding plan
6. **Risk Register**: Identified risks and mitigation plans
7. **Stakeholder Register**: Who cares and how to engage
8. **Communication Plan**: Who gets what info, when, how
9. **Quality Management Plan**: Standards and metrics
10. **Change Management Plan**: How to handle scope changes

---

## Common Pitfalls

1. **Optimistic Estimation**: Add buffers (10-20%)
2. **Scope Creep**: Implement change control process
3. **Resource Overload**: Level resources, be realistic
4. **Ignoring Dependencies**: Map all dependencies early
5. **No Contingency**: Always include reserves
6. **Skipping Stakeholders**: Engage early and often
7. **Poor Communication**: Communicate more than you think necessary
8. **No Baseline**: Can't measure progress without baseline
9. **Analysis Paralysis**: Perfect plan is enemy of good plan
10. **Ignoring Risks**: Identify and mitigate proactively

---

## Tools and Techniques Quick Reference

| Need | Tool/Technique |
|------|----------------|
| High-level estimate | Analogous estimation |
| Detailed estimate | Bottom-up estimation |
| Uncertainty in estimate | Three-point estimation (PERT) |
| Historical data available | Parametric estimation |
| Agile team estimation | Planning Poker |
| Find critical path | CPM (Critical Path Method) |
| Level resources | Resource histogram |
| Prioritize requirements | MoSCoW method |
| Engage stakeholders | Power/Interest grid |
| Manage scope changes | Change control board |
| Track Agile progress | Burndown/Burnup charts |
| Visualize workflow | Kanban board |
| Complex dependencies | Network diagram |

---

**This skill is continuously updated with lessons learned from real-world project delivery.**
