# Milestone Decomposition Skill

## Overview

This skill provides comprehensive techniques for breaking down SMART goals into actionable milestones with clear dependencies, realistic timelines, and measurable success criteria. Master milestone planning transforms abstract goals into executable roadmaps.

## Core Principles

### Principle 1: Work Backwards from Success
Start with the end goal and reverse-engineer the path.

### Principle 2: Right-Size Milestones
Not too big (>6 weeks), not too small (<1 week). Sweet spot: 2-4 weeks.

### Principle 3: Make Dependencies Explicit
Clearly show what must happen before what.

### Principle 4: Build in Buffer Time
Things take longer than expected. Add 20-30% buffer.

### Principle 5: Define Success Clearly
Each milestone needs unambiguous completion criteria.

## Backward Planning Methodology

### The Backward Planning Process

**Step 1: Define End State** (the goal achievement)
```
Goal: Launch product by December 15, 2024

End state visualization:
- Product live in production
- Customers can sign up and use
- Support team trained
- Marketing materials published
```

**Step 2: Identify Final Prerequisite** (what must happen immediately before)
```
Before product launch:
- Final testing complete
- Documentation ready
- Support team trained
- Marketing campaign prepared
```

**Step 3: Continue Backward** (chain prerequisites)
```
Before final testing:
- Beta testing complete
- Bugs fixed
- Performance optimized

Before beta testing:
- Alpha version complete
- Test users recruited
- Feedback mechanism built
```

**Step 4: Reach Current State**
```
Current state:
- Product concept validated
- Technical architecture decided
- Team assembled
```

**Step 5: Reverse Sequence** (create forward roadmap)
```
1. Build core features (current → alpha)
2. Alpha testing and iteration
3. Beta testing
4. Final testing and bug fixes
5. Launch preparation
6. Launch
```

### Backward Planning Example

**Goal**: "Achieve AWS Solutions Architect certification by June 30, 2024"

**Backward chain**:
```
June 30: PASS EXAM ← Take real exam
June 23: Ready to test ← Pass 3 practice exams at 85%+
June 1-22: Practice testing ← Complete all practice exams
May 1-31: Deep study ← Study all domains thoroughly
April 15-30: Foundation study ← Complete intro course
April 1-14: Planning ← Assess current knowledge, create study plan
March 31: START ← Register for exam, buy study materials
```

**Forward roadmap** (reversed):
```
Milestone 1 (2 weeks): Planning & Setup (Apr 1-14)
Milestone 2 (2 weeks): Foundation Learning (Apr 15-30)
Milestone 3 (4 weeks): Deep Domain Study (May 1-31)
Milestone 4 (3 weeks): Practice Testing (Jun 1-22)
Milestone 5 (1 week): Final Prep & Exam (Jun 23-30)

Total: 12 weeks with some buffer
```

## Milestone Sizing Guidelines

### Ideal Milestone Characteristics

**Duration**: 2-4 weeks
- Short enough to maintain momentum
- Long enough to deliver meaningful value
- Allows for weekly progress checks

**Scope**: Single major deliverable
- One clear outcome or capability
- Multiple tasks but unified theme
- Can be demonstrated/validated

**Value**: Tangible progress
- Moves significantly toward goal
- Produces visible result
- Creates foundation for next milestone

**Dependencies**: Minimal blocking
- Can mostly work independently
- Critical path identified
- Parallel work opportunities

### Sizing Decision Tree

```
Is duration > 6 weeks?
  YES → TOO BIG: Break down further
  NO → Continue

Is duration < 1 week?
  YES → TOO SMALL: Combine with others
  NO → Continue

Can you clearly demo/verify completion?
  YES → Continue
  NO → UNCLEAR: Refine completion criteria

Does it deliver standalone value?
  YES → GOOD SIZE
  NO → Consider restructuring
```

### Breaking Down Large Milestones

**When milestone is >6 weeks**, apply decomposition:

**Option 1: Functional Decomposition** (by feature/capability)
```
Large: "Build complete e-commerce platform" (12 weeks)

Broken down:
- M1: Product catalog and browsing (3 weeks)
- M2: Shopping cart and checkout (3 weeks)
- M3: Payment processing (2 weeks)
- M4: Order management (2 weeks)
- M5: Admin dashboard (2 weeks)
```

**Option 2: Phase Decomposition** (by iteration)
```
Large: "Redesign website" (10 weeks)

Broken down:
- M1: Research and wireframes (2 weeks)
- M2: Design mockups (2 weeks)
- M3: Homepage implementation (2 weeks)
- M4: Key pages implementation (3 weeks)
- M5: Testing and polish (1 week)
```

**Option 3: Vertical Slice** (thin end-to-end)
```
Large: "Implement user authentication" (8 weeks)

Broken down:
- M1: Basic email/password login (2 weeks)
- M2: Social auth (Google, GitHub) (2 weeks)
- M3: Password reset flow (1 week)
- M4: Two-factor authentication (2 weeks)
- M5: Session management (1 week)
```

### Combining Small Milestones

**When milestones are <1 week**, combine logically:

```
Too small:
- M1: Design logo (2 days)
- M2: Choose color scheme (1 day)
- M3: Create brand guidelines (2 days)
- M4: Design business card (1 day)

Combined:
- M1: Complete brand identity package (1 week)
  - Logo design
  - Color scheme selection
  - Brand guidelines
  - Business card design
```

## Dependency Mapping

### Types of Dependencies

**Finish-to-Start (FS)** - Most common
```
M1 (Design) must FINISH before M2 (Development) can START

Timeline:
Week 1-2: Design ████████
Week 3-4:         ████████ Development
```

**Start-to-Start (SS)** - Parallel work
```
M2 (Development) can START when M1 (Design) STARTS

Timeline:
Week 1-4: Design ████████████████
Week 1-4: Dev    ████████████████
```

**Finish-to-Finish (FF)** - Synchronized completion
```
M2 (Testing) must FINISH when M1 (Development) FINISHES

Timeline:
Week 1-4: Development ████████████████
Week 2-4: Testing        ████████████
```

**Start-to-Finish (SF)** - Rare, mostly in operations
```
M2 (New system) cannot FINISH until M1 (Old system) STARTS shutdown

Handoff/transition scenarios
```

### Dependency Analysis

**Step 1: List all milestones**
```
M1: User authentication
M2: User profiles
M3: Content creation
M4: Content sharing
M5: Analytics
```

**Step 2: For each milestone, ask:**
- What MUST be done before this can start?
- What CAN be done in parallel?
- What SHOULD wait for this to complete?

**Step 3: Map dependencies**
```
M1: No dependencies (foundation)
M2: Depends on M1 (need auth to have profiles)
M3: Depends on M2 (need profiles to create content)
M4: Depends on M3 (need content to share)
M5: Depends on M1, M2, M3, M4 (needs data from all)
```

**Step 4: Identify critical path**
```
Critical Path: M1 → M2 → M3 → M4 → M5
(Cannot be parallelized)

Alternative structure:
M1 → M2 → M3 → M4
       ↘ M5 (can start after M2)
```

### Dependency Visualization

**Linear Dependencies**:
```
M1 → M2 → M3 → M4 → M5
████   ████   ████   ████   ████
```

**Parallel Opportunities**:
```
M1 → M2 ┬→ M4 → M5
  ████  │ ████   ████
         │
         └→ M3
            ████
```

**Complex Dependencies**:
```
M1 (Foundation)
 ├─→ M2 (Feature A)
 │    └─→ M4 (Integration)
 │         └─→ M5 (Launch)
 └─→ M3 (Feature B)
      └─→ M4 (Integration)
```

### Resolving Dependency Conflicts

**Problem: Circular Dependencies**
```
Bad:
M1 depends on M2
M2 depends on M3
M3 depends on M1
(Impossible!)

Solution: Break the cycle
M1 → M2 → M3 → M4
(Redefine scopes to eliminate circular dependency)
```

**Problem: Bottleneck Dependencies**
```
Issue:
M2, M3, M4 all depend on M1
M1 is on critical path and delayed

Solution 1: Parallelize M1 work
Solution 2: Stub/mock M1 for M2-4 to start
Solution 3: Descope M1 to minimum for M2-4 to proceed
```

## Time Allocation and Buffering

### Estimation Techniques

**Three-Point Estimation**:
```
For each milestone, estimate:
- Optimistic (O): Best case if everything goes perfectly
- Most Likely (M): Realistic middle ground
- Pessimistic (P): Worst case with expected obstacles

Expected Time = (O + 4M + P) / 6

Example:
Milestone: "Build user authentication"
- Optimistic: 1 week
- Most Likely: 2 weeks
- Pessimistic: 4 weeks

Expected = (1 + 4*2 + 4) / 6 = 13/6 = 2.2 weeks
Round up: 3 weeks with buffer
```

**Historical Velocity**:
```
If you have past data:
Average milestone completion: 2.5 weeks
Average overrun: 20%

New milestone estimate: 2 weeks
Adjusted: 2 * 1.20 = 2.4 weeks (round to 3)
```

**Task-Based Bottom-Up**:
```
List all tasks for milestone:
- Task 1: 2 days
- Task 2: 3 days
- Task 3: 2 days
- Task 4: 1 day
- Task 5: 2 days

Subtotal: 10 days = 2 weeks
Add buffer (30%): 2.6 weeks (round to 3)
```

### Buffer Allocation Strategies

**Option 1: Per-Milestone Buffer** (20-30% per milestone)
```
M1: 2 weeks planned + 0.5 week buffer = 2.5 weeks
M2: 3 weeks planned + 0.75 week buffer = 3.75 weeks
M3: 2 weeks planned + 0.5 week buffer = 2.5 weeks

Total: 7 weeks + 1.75 weeks buffer = 8.75 weeks
```

**Option 2: Project-Level Buffer** (single buffer at end)
```
M1: 2 weeks
M2: 3 weeks
M3: 2 weeks
Subtotal: 7 weeks

Project buffer: 2 weeks (28% of total)
Total: 9 weeks
```

**Option 3: Critical Path Buffer** (buffer only critical path)
```
Critical path: M1 → M2 → M4 (7 weeks)
Add buffer: 2 weeks
Critical path total: 9 weeks

Non-critical: M3 (2 weeks, can slip without impacting deadline)
```

### Buffer Consumption Monitoring

```
Track buffer usage:
- Milestone 1: Used 0.5 week buffer (50% of allocated)
- Milestone 2: Used 0 buffer (0%)
- Milestone 3: Used 1 week buffer (200% of allocated)

Status:
- Total buffer: 1.5 weeks used of 2 weeks allocated
- Remaining buffer: 0.5 weeks
- Trend: Concerning (used more than planned on M3)

Action: Consider descoping remaining milestones or extending deadline
```

## Success Criteria Definition

### Completion Criteria Components

**1. Deliverable Specification**
What must exist when milestone is done?

```
Example - Milestone: "User Authentication"

Deliverables:
- Login page (email/password)
- Registration page
- Password reset flow
- Session management
- Logout functionality
```

**2. Quality Standards**
What level of quality is required?

```
Quality criteria:
- All automated tests pass (>90% coverage)
- Security audit completed (no critical vulnerabilities)
- Performance: <500ms response time for auth endpoints
- Accessibility: WCAG 2.1 AA compliance
- Cross-browser: Works in Chrome, Firefox, Safari, Edge
```

**3. Acceptance Tests**
How will we verify it works?

```
Acceptance tests:
- [ ] User can register with email/password
- [ ] User can log in with correct credentials
- [ ] User cannot log in with incorrect credentials
- [ ] User can reset forgotten password via email
- [ ] User session persists across page refreshes
- [ ] User can log out successfully
```

**4. Demonstration Criteria**
What will we show to prove completion?

```
Demo:
- Show live registration flow (end-to-end)
- Attempt login with wrong password (shows error)
- Attempt login with correct password (succeeds)
- Navigate app while logged in (session persists)
- Log out (session cleared)
- Reset password (email received, link works)
```

### Success Criteria Template

```markdown
## Milestone: [Name]

### Deliverables
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]
- [ ] [Deliverable 3]

### Quality Standards
- [ ] [Standard 1 with measurable threshold]
- [ ] [Standard 2 with measurable threshold]

### Acceptance Tests
- [ ] [Test 1: Specific user action and expected result]
- [ ] [Test 2: Specific user action and expected result]
- [ ] [Test 3: Specific user action and expected result]

### Definition of Done
This milestone is complete when:
1. All deliverables are produced
2. All quality standards are met
3. All acceptance tests pass
4. Stakeholder demo completed and approved

### Completion Gate
**Demo to**: [Stakeholder name/role]
**Approval required from**: [Name/role]
**Blocked until**: [Any prerequisites]
```

## Resource Planning

### Resource Categories

**1. Personnel**
```
Milestone: "Build API integration"

Required:
- Backend developer (20 hours/week for 3 weeks)
- Frontend developer (10 hours/week for 2 weeks)
- QA engineer (10 hours/week for 1 week)

Total effort: 90 person-hours
Duration: 3 weeks (with parallel work)
```

**2. Budget**
```
Milestone: "Launch marketing campaign"

Budget:
- Ad spend: $5,000
- Creative design: $2,000
- Copywriting: $1,000
- Tools/software: $500

Total: $8,500
```

**3. Tools and Equipment**
```
Milestone: "Set up CI/CD pipeline"

Required tools:
- GitHub Actions (included in current plan)
- AWS resources ($200/month)
- Docker Hub ($50/month)
- Testing tools (existing licenses)

New costs: $250/month during milestone
```

**4. External Dependencies**
```
Milestone: "Integrate payment processing"

External dependencies:
- Stripe account setup (requires business verification, 2-5 days)
- PCI compliance review (requires security audit, $1,500)
- Legal review of terms (attorney time, $800)

Lead time: 2 weeks for account approval
```

### Resource Allocation Matrix

```markdown
| Milestone | Week 1 | Week 2 | Week 3 | Week 4 | Resources |
|-----------|--------|--------|--------|--------|-----------|
| M1: Design | Alice(20h) | Alice(20h) | - | - | Designer |
| M2: Frontend | - | - | Bob(30h) | Bob(30h) | FE Dev |
| M3: Backend | - | Carol(30h) | Carol(30h) | - | BE Dev |
| M4: Testing | - | - | - | Dave(20h) | QA |

Resource utilization:
- Alice: Fully utilized weeks 1-2, available after
- Bob: Available weeks 1-2, fully utilized weeks 3-4
- Carol: Available week 1, fully utilized weeks 2-3, available week 4
- Dave: Available weeks 1-3, utilized week 4
```

### Resource Constraint Handling

**Problem: Limited Resources**
```
Situation:
- Only 1 developer available
- Need to complete M2 and M3 (both require developer)
- Both estimated at 2 weeks

Options:
1. Sequential: M2 (weeks 1-2) → M3 (weeks 3-4) = 4 weeks total
2. Hire contractor for M3: M2 and M3 parallel = 2 weeks total
3. Descope: Do M2 only, defer M3 to next phase

Recommendation: Option 1 if time allows, Option 2 if deadline critical
```

**Problem: Overallocation**
```
Situation:
- Alice scheduled for 40 hours/week
- M2 needs Alice 30 hours
- M3 needs Alice 20 hours
- Both in same week

Resolution:
- Prioritize: Which is critical path?
- Extend: Spread M3 across 2 weeks (10 hours each)
- Delegate: Can anyone else do part of M3?
- Descope: Can we reduce scope of either milestone?
```

## Milestone Planning Patterns

### Pattern 1: Sequential (Waterfall)
Each milestone completes before next begins.

**When to use**:
- Strong dependencies between milestones
- Regulated environment requiring gates
- High risk of rework if done in parallel
- Clear requirements upfront

**Example**: Hardware product development
```
M1: Requirements & Design (4 weeks)
     ████████
M2: Prototype Build (6 weeks)
             ████████████
M3: Testing & Validation (4 weeks)
                         ████████
M4: Manufacturing Setup (6 weeks)
                                 ████████████
M5: Production Launch (2 weeks)
                                             ████
```

**Pros**:
- Clear gates and quality checks
- Reduces risk of wasted parallel work
- Easier to manage and track

**Cons**:
- Slower (no parallelization)
- Delays cascade through sequence
- Less flexibility to adapt

### Pattern 2: Parallel (Concurrent)
Multiple milestones run simultaneously.

**When to use**:
- Independent work streams
- Abundant resources
- Time-critical delivery
- Low interdependency risk

**Example**: Multi-channel marketing launch
```
M1: Website update (4 weeks)
     ████████████████
M2: Email campaign (4 weeks)
     ████████████████
M3: Social media (4 weeks)
     ████████████████
M4: PR outreach (4 weeks)
     ████████████████
M5: Coordination (entire period)
     ████████████████
```

**Pros**:
- Fastest time to completion
- Maximizes resource utilization
- Can deliver multiple features simultaneously

**Cons**:
- Requires more resources
- Risk of integration issues
- Harder to coordinate

### Pattern 3: Iterative (Agile Sprints)
Milestones are iterations adding incremental value.

**When to use**:
- Evolving requirements
- Need for frequent feedback
- Building MVP then enhancing
- User validation important

**Example**: SaaS product development
```
Sprint 1: Core login + dashboard (2 weeks)
          ████ → DEMO 1
Sprint 2: Basic CRUD operations (2 weeks)
                    ████ → DEMO 2
Sprint 3: Advanced features (2 weeks)
                          ████ → DEMO 3
Sprint 4: Polish + performance (2 weeks)
                                ████ → DEMO 4
```

**Pros**:
- Frequent validation and course correction
- Always have working product
- Can adapt to changing requirements
- Early value delivery

**Cons**:
- Requires discipline (time-boxing)
- Can lack long-term architectural vision
- Harder to estimate total timeline

### Pattern 4: Hybrid (Phased with Parallel)
Mix of sequential phases with parallel work within phases.

**When to use**:
- Complex projects with varied dependencies
- Some components sequential, others parallel
- Need balance of speed and risk management

**Example**: Platform migration
```
Phase 1: Planning (Sequential)
  M1: Assessment
       ████ → Gate 1

Phase 2: Build (Parallel)
  M2: Data migration
            ████████████
  M3: Feature parity
            ████████████ → Gate 2

Phase 3: Rollout (Sequential)
  M4: Pilot
                        ████
  M5: Full rollout
                            ████████ → Gate 3
```

**Pros**:
- Balances speed and safety
- Parallelizes where possible
- Gates at critical points
- Flexible to project needs

**Cons**:
- More complex to plan
- Requires good dependency management
- Can be harder to explain to stakeholders

## Risk Management in Milestone Planning

### Risk Identification

**Technical Risks**:
```
Milestone: "Integrate with external API"

Risks:
- API changes unexpectedly
- API has poor documentation
- Rate limiting issues
- Authentication complexity
- Data format mismatches
```

**Resource Risks**:
```
Milestone: "Complete Q1 sales targets"

Risks:
- Key salesperson leaves
- Budget cut mid-quarter
- Tools/systems unavailable
- Competing priorities
- Team member illness
```

**External Risks**:
```
Milestone: "Launch in new market"

Risks:
- Regulatory approval delays
- Currency fluctuations
- Competitor launches first
- Market conditions change
- Partner delays
```

### Risk Mitigation Strategies

**Strategy 1: Build Slack Time**
```
Risky Milestone: "Migrate legacy database"
Risk: Data corruption, downtime, unforeseen issues

Mitigation:
- Estimate: 2 weeks
- Add 50% buffer: 3 weeks
- Schedule during low-traffic period
- Prepare rollback plan
```

**Strategy 2: De-risk Early**
```
Risky Milestone: "Integrate complex payment system"
Risk: Integration more complex than expected

Mitigation:
- M1: "Research and spike integration" (1 week)
  - Proof of concept
  - Identify gotchas
  - Refine estimates
- M2: "Full integration implementation" (revised estimate based on M1)
```

**Strategy 3: Parallel Backup Plan**
```
Risky Milestone: "Get regulatory approval"
Risk: Approval delayed or denied

Mitigation:
- Primary: Pursue regulatory approval (M1)
- Backup: Develop alternative approach (M2, parallel)
- If M1 delayed past week 4, pivot to M2
```

**Strategy 4: Incremental Commitment**
```
Risky Milestone: "Build custom analytics engine"
Risk: Too complex, may not be worth it

Mitigation:
- M1: "MVP analytics" (2 weeks)
  - Prove value hypothesis
  - Gate: If not valuable, switch to off-shelf tool
- M2: "Enhanced analytics" (only if M1 succeeds)
```

## Example: Complete Milestone Plan

### Goal
"Increase monthly blog traffic from 10,000 to 15,000 visitors by June 30, 2024"

### Backward Planning
```
June 30: Achieve 15K visitors
  ← Need consistent 15K/month traffic
  ← Need SEO improvements working
  ← Need content ranking
  ← Need content published
  ← Need content created
  ← Need content strategy
  ← Current: 10K visitors, ad-hoc content
```

### Milestone Breakdown

**M1: Content Strategy & SEO Audit** (Weeks 1-2)
```
Duration: 2 weeks
Dependencies: None (starting milestone)
Owner: Content lead + SEO specialist

Deliverables:
- [ ] Keyword research (50 target keywords)
- [ ] Content gap analysis
- [ ] Editorial calendar (6 months)
- [ ] SEO audit of existing content
- [ ] Competitor analysis

Success Criteria:
- Editorial calendar covers 6 months
- 50 keywords identified with search volume >100/month
- Audit identifies top 10 optimization opportunities
- Strategy approved by marketing director

Resources:
- Content lead: 20 hours
- SEO specialist: 15 hours
- Tools: Ahrefs, SEMrush (existing)

Risks:
- May find fewer opportunities than hoped (Medium)
  Mitigation: Expand keyword research, consider long-tail

Completion gate: Strategy review meeting
```

**M2: Optimize Existing Content** (Weeks 3-4)
```
Duration: 2 weeks
Dependencies: M1 (needs audit results)
Owner: Content writer + SEO specialist

Deliverables:
- [ ] 10 top posts optimized for SEO
- [ ] Updated title tags and meta descriptions
- [ ] Improved internal linking
- [ ] Added relevant images/media
- [ ] Fixed technical SEO issues

Success Criteria:
- All 10 posts optimized per SEO checklist
- Page speed improved by 20%
- Mobile usability issues resolved
- Measurable improvement in search console

Resources:
- Content writer: 25 hours
- SEO specialist: 10 hours
- Designer: 5 hours (images)

Risks:
- Optimization doesn't improve rankings quickly (High)
  Mitigation: Focus on low-hanging fruit, quick wins
  Note: Results may lag by 4-6 weeks (normal)

Buffer: 0.5 weeks
```

**M3: Create New High-Value Content** (Weeks 3-8, parallel with M2)
```
Duration: 6 weeks
Dependencies: M1 (needs content calendar)
Can run parallel with M2
Owner: Content writer

Deliverables:
- [ ] 12 new blog posts (2 per week)
- [ ] All posts 1,500+ words
- [ ] SEO-optimized per guidelines
- [ ] Published and promoted

Success Criteria:
- 12 posts published on schedule
- Each post targets specific keyword from M1
- All posts meet quality checklist
- Each post promoted on social media

Resources:
- Content writer: 30 hours/week for 6 weeks
- Editor: 5 hours/week for 6 weeks
- Designer: 3 hours/week for featured images

Risks:
- Writer bandwidth limited (High)
  Mitigation: Front-load content creation, build buffer

Buffer: 1 week
```

**M4: Build Backlinks & Promotion** (Weeks 7-10)
```
Duration: 4 weeks
Dependencies: M3 (needs content to promote)
Owner: Marketing coordinator

Deliverables:
- [ ] 20 quality backlinks acquired
- [ ] 10 guest post placements
- [ ] Outreach to 50 relevant sites
- [ ] Social media promotion campaign
- [ ] Email newsletter promotion

Success Criteria:
- Domain authority increased by 2+ points
- 20 backlinks from DA 30+ sites
- 10 guest posts published
- 5,000+ social media impressions
- Newsletter sent to entire list

Resources:
- Marketing coordinator: 20 hours/week
- Budget: $500 for outreach tools
- Designer: 5 hours (promotional graphics)

Risks:
- Low response rate on outreach (Medium)
  Mitigation: Cast wide net, personalize outreach

Buffer: 1 week
```

**M5: Monitor & Iterate** (Weeks 11-12)
```
Duration: 2 weeks
Dependencies: M2, M3, M4 (needs all tactics implemented)
Owner: Content lead

Deliverables:
- [ ] Analytics review
- [ ] Identify top performers
- [ ] Identify underperformers
- [ ] Iteration plan for next cycle
- [ ] Traffic goal assessment

Success Criteria:
- Traffic reaches 15,000/month OR
- Clear trend toward 15K with action plan
- Top 5 posts identified for amplification
- Bottom 5 posts identified for improvement
- Plan for next quarter approved

Resources:
- Content lead: 15 hours
- SEO specialist: 10 hours

Risks:
- May not hit 15K exactly by deadline (Medium)
  Mitigation: This is OK if trend is clear and plan solid

No buffer (end of timeline)
```

### Timeline Visualization

```
Week:  1  2  3  4  5  6  7  8  9  10 11 12
M1:    ████
M2:       ████
M3:       ████████████████
M4:                   ████████
M5:                            ████

Critical Path: M1 → M3 → M5
Buffer: 2.5 weeks total (21% buffer)
Total: 12 weeks (Mar 1 - Jun 30)
```

### Resource Summary

```
Content Writer:
- Weeks 1-2: 20h (M1)
- Weeks 3-8: 30h (M3)
Total: 220 hours

SEO Specialist:
- Weeks 1-2: 15h (M1)
- Weeks 3-4: 10h (M2)
- Weeks 11-12: 10h (M5)
Total: 45 hours

Marketing Coordinator:
- Weeks 7-10: 20h/week (M4)
Total: 80 hours

Budget: $500 (outreach tools)
```

## Usage Guidelines

1. **Always start with backward planning** - It reveals the critical path naturally
2. **Right-size milestones** - 2-4 weeks is sweet spot for most goals
3. **Make dependencies explicit** - Don't assume, document clearly
4. **Add 20-30% buffer** - Things always take longer than expected
5. **Define success criteria clearly** - Avoid "done but not really done"
6. **Plan resources realistically** - Check actual availability, not wishful thinking
7. **Identify and mitigate risks** - Don't hope problems away
8. **Use appropriate pattern** - Sequential, parallel, iterative, or hybrid based on context
9. **Review and adjust** - Plans are living documents, update as you learn

This skill should be read in full before decomposing any goal into milestones.
