# Risk Management Skill

**Comprehensive risk identification, assessment matrices, probability-impact analysis, and mitigation strategies following PMI/PMBOK standards**

This skill codifies best practices from thousands of projects across industries, incorporating lessons learned from both successful risk mitigation and realized risks.

---

## Core Principles

1. **Risk is opportunity**: Negative risks (threats) and positive risks (opportunities)
2. **Proactive beats reactive**: Identify and mitigate before occurrence
3. **Continuous process**: Risk management never stops
4. **Everyone's responsibility**: Not just the PM's job
5. **Honest assessment**: Wishful thinking doesn't reduce risk
6. **Document everything**: Undocumented risks are forgotten risks
7. **Prioritize ruthlessly**: Focus on high-impact risks
8. **Plan for contingencies**: Hope for best, plan for worst
9. **Monitor triggers**: Early warning enables early response
10. **Learn from experience**: Feed realized risks into future planning

---

## Risk Management Process (PMI/PMBOK)

### 1. Plan Risk Management

Define how to conduct risk management activities.

**Risk Management Plan Contents**:
```markdown
# Risk Management Plan

## Methodology
- Tools: Risk register (Excel), Risk matrix
- Data sources: Historical data, expert interviews, lessons learned
- Techniques: Brainstorming, SWOT, checklist analysis

## Roles and Responsibilities
- Risk Manager: [Name] - Maintains register, coordinates reviews
- Risk Owners: Assigned per risk - Implement mitigation
- Team Members: Identify and report risks
- Sponsor: Escalation point for critical risks

## Risk Categories (RBS - Risk Breakdown Structure)
1. Technical
2. Schedule
3. Cost
4. Resource
5. External
6. Organizational

## Probability and Impact Definitions
[See scales below]

## Risk Appetite
- Critical risks (score >16): Zero tolerance
- High risks (score 10-16): Mitigation required
- Medium risks (score 5-9): Mitigation planned
- Low risks (score 1-4): Accept and monitor

## Review Cadence
- Weekly: High-priority risks
- Bi-weekly: All active risks
- Monthly: Comprehensive review
- Ad-hoc: When triggers observed

## Reporting
- Weekly status: Top 5 risks
- Monthly: Full risk register
- Immediate: Critical risk escalation
```

### 2. Identify Risks

**Identification Techniques**:

**Brainstorming**:
```
Structured session with team:
1. Set context (project overview)
2. Silent idea generation (5 min)
3. Round-robin sharing (no criticism)
4. Clarification and discussion
5. Categorization
6. Documentation

Prompts:
- "What could prevent us from meeting the deadline?"
- "What assumptions are we making that might be wrong?"
- "What happened in similar projects?"
- "What keeps you awake at night about this project?"
```

**SWOT Analysis**:
```
Strengths (Internal Positive):
- Experienced team → Leverage for mentoring
- Proven technology → Reuse components

Weaknesses (Internal Negative):
- Limited budget → Risk of insufficient resources
- Tight timeline → Risk of quality shortcuts

Opportunities (External Positive):
- Early market entry → Accelerate for competitive advantage
- Industry partnership → Explore collaboration

Threats (External Negative → RISKS):
- Competitor launching similar product → Risk of market saturation
- Regulatory changes pending → Risk of compliance issues
```

**Delphi Technique**:
```
Anonymous expert polling:
1. Distribute questionnaire to experts
2. Collect responses anonymously
3. Share aggregate results
4. Experts revise their inputs
5. Repeat until consensus
6. Minimizes groupthink and bias
```

**Checklist Analysis**:
```
Use standardized risk checklists by industry:

Software Development:
□ Technology risks (new frameworks, integration, performance)
□ Requirements risks (incomplete, changing, misunderstood)
□ Team risks (turnover, skill gaps, availability)
□ Dependency risks (third-party APIs, vendor delays)
□ Security risks (vulnerabilities, data breaches)
□ Technical debt risks (legacy code, poor architecture)

Construction:
□ Weather delays
□ Material availability
□ Regulatory approvals
□ Site conditions
□ Labor availability
```

**Assumptions Analysis**:
```
Every assumption is a potential risk.

Example Assumptions:
1. "Database can handle 10K concurrent users"
   → Risk: Performance degradation if assumption wrong
   → Validation: Load testing early

2. "Key developer available full-time"
   → Risk: Resource unavailable due to other projects
   → Validation: Confirm allocation with resource manager

3. "Third-party API will have 99.9% uptime"
   → Risk: API downtime affects our application
   → Validation: Review vendor SLA, plan fallback
```

**Root Cause Analysis**:
```
Use "5 Whys" technique:

Problem: Project might be delayed

Why? Development taking longer than estimated
Why? Team unfamiliar with new framework
Why? No training provided before project start
Why? Training budget not allocated
Why? Training needs not identified during planning

Root Cause Risk: Inadequate skills assessment in planning phase
Mitigation: Conduct skills assessment, allocate training budget
```

### 3. Analyze Risks (Qualitative)

**Probability Scale (1-5)**:
```
5 - Very High (>70%):  Almost certain to occur
4 - High (50-70%):     Likely to occur
3 - Medium (30-50%):   May occur
2 - Low (10-30%):      Unlikely to occur
1 - Very Low (<10%):   Rare
```

**Impact Scale (1-5)** - Multi-dimensional:

**Schedule Impact**:
```
5 - Critical:   >1 month delay / Project deadline missed
4 - High:       2-4 weeks delay
3 - Medium:     1-2 weeks delay
2 - Low:        3-5 days delay
1 - Very Low:   <3 days delay
```

**Cost Impact**:
```
5 - Critical:   >20% budget increase / Project cancelled
4 - High:       10-20% budget increase
3 - Medium:     5-10% budget increase
2 - Low:        2-5% budget increase
1 - Very Low:   <2% budget increase
```

**Quality Impact**:
```
5 - Critical:   Unusable deliverable / Safety hazard
4 - High:       Major functionality broken
3 - Medium:     Significant quality degradation
2 - Low:        Minor quality issues
1 - Very Low:   Negligible quality impact
```

**Scope Impact**:
```
5 - Critical:   Major scope reduction required
4 - High:       Significant features cut
3 - Medium:     Some features affected
2 - Low:        Minor scope adjustment
1 - Very Low:   No scope impact
```

**Overall Impact**: Use highest impact among dimensions

**Risk Score Calculation**:
```
Risk Score = Probability × Impact

Example Risk: "Key developer may leave project"

Probability: 3 (30-50% chance based on indicators)
Impact (Schedule): 4 (2-4 weeks to replace and ramp up)
Impact (Quality): 3 (knowledge loss affects quality)
Overall Impact: 4 (use highest)

Risk Score: 3 × 4 = 12 (HIGH)
```

**Probability-Impact Matrix**:
```
                    IMPACT
              1    2    3    4    5
         1 |  1  |  2  |  3  |  4  |  5  |
         2 |  2  |  4  |  6  |  8  | 10  |
    P    3 |  3  |  6  |  9  | 12  | 15  |
    R    4 |  4  |  8  | 12  | 16  | 20  |
    O    5 |  5  | 10  | 15  | 20  | 25  |
    B

Risk Levels:
1-4:    LOW (Green) - Accept and monitor
5-9:    MEDIUM (Yellow) - Mitigation planned
10-16:  HIGH (Orange) - Mitigation required
17-25:  CRITICAL (Red) - Immediate action
```

### 4. Analyze Risks (Quantitative)

**Expected Monetary Value (EMV)**:
```
EMV = Probability × Impact (in dollars)

Example:
Risk: "Server failure causes 2-day outage"
Probability: 20%
Impact: $50,000 (lost revenue + recovery cost)
EMV: 0.20 × $50,000 = $10,000

Use EMV to prioritize and budget contingency reserves.

Total Project Risk Exposure:
Risk 1 EMV: $10,000
Risk 2 EMV: $15,000
Risk 3 EMV: $8,000
Total: $33,000

Contingency Reserve: $33,000 (covers expected value of known risks)
Management Reserve: +10% of budget (unknown unknowns)
```

**Decision Tree Analysis**:
```
Decision: Build in-house vs Buy COTS (Commercial Off-The-Shelf)

Build In-House:
├─ Success (70%): -$100K cost, $200K value = +$100K × 0.7 = +$70K
└─ Failure (30%): -$100K cost, $0 value = -$100K × 0.3 = -$30K
EMV: $70K - $30K = +$40K

Buy COTS:
├─ Success (90%): -$50K cost, $150K value = +$100K × 0.9 = +$90K
└─ Failure (10%): -$50K cost, $0 value = -$50K × 0.1 = -$5K
EMV: $90K - $5K = +$85K

Decision: Buy COTS (higher EMV)
```

**Monte Carlo Simulation**:
```
For complex projects, simulate 1000s of scenarios:

Task A: 5-10 days (triangular distribution)
Task B: 3-8 days
Task C: 2-6 days

Run 10,000 simulations:
- 10% chance of completing in <15 days
- 50% chance of completing in <18 days
- 90% chance of completing in <22 days

Use 90% confidence level: Plan for 22 days
```

### 5. Plan Risk Responses

**Four Strategies for Threats (Negative Risks)**:

#### 1. Avoid (Eliminate the Risk)
```
Risk: New technology may not meet performance requirements
Response: Use proven technology instead

Risk: Vendor may not deliver on time
Response: Build capability in-house

Risk: Regulatory approval uncertain
Response: Redesign to avoid regulatory requirement

When to use: High probability and high impact risks that can be eliminated
```

#### 2. Mitigate (Reduce Probability or Impact)

**Reduce Probability**:
```
Risk: Integration failures between systems
Probability: 60% → Target: 20%
Actions:
- Proof of concept to validate integration (before full build)
- Early integration testing (start week 2, not week 10)
- Dedicated integration engineer
- Weekly integration reviews

Risk: Team members lack required skills
Probability: 50% → Target: 10%
Actions:
- Skills assessment before project start
- Training program (2 weeks before coding)
- Pair programming with experts
- Access to online learning resources
```

**Reduce Impact**:
```
Risk: Key person leaves project
Impact: 4 weeks delay → Target: 1 week delay
Actions:
- Cross-training (2 people know each critical area)
- Documentation (architecture, key decisions)
- Knowledge sharing sessions (weekly)
- Backup resources identified (contractor on standby)

Risk: Data loss due to system failure
Impact: Critical → Target: Low
Actions:
- Automated daily backups
- Backup to multiple locations (local + cloud)
- Regular restore testing
- 4-hour recovery time objective (RTO)
```

#### 3. Transfer (Shift to Third Party)
```
Risk: Hardware failure
Transfer: Cloud hosting (AWS/Azure assumes hardware risk)

Risk: Project delay penalties
Transfer: Insurance policy or performance bond

Risk: Security breach liability
Transfer: Cyber insurance + legal indemnification

Risk: Cost overruns
Transfer: Fixed-price contract with vendor (they bear overrun)

When to use: Risks others are better equipped to handle
Cost: Insurance premium, higher vendor rates, contract terms
```

#### 4. Accept (Acknowledge and Monitor)

**Active Acceptance** (create contingency plan):
```
Risk: Minor UI bugs in initial release
Acceptance: Budget 40 hours for post-release fixes
Contingency Plan:
- Bug fix process defined
- Hotfix deployment procedure ready
- Support team on standby for first week

Risk: Some requirements may change
Acceptance: Reserve 10% timeline buffer
Contingency Plan:
- Change request process documented
- Impact assessment template ready
- Stakeholder approval workflow defined
```

**Passive Acceptance** (do nothing, monitor):
```
Risk: Exchange rate fluctuation (USD/EUR)
Impact: Low ($2K on $200K project)
Response: Accept, no action

Risk: Team member sick 2-3 days
Impact: Low (team cross-trained)
Response: Accept, normal process
```

**Three Strategies for Opportunities (Positive Risks)**:

#### 1. Exploit (Ensure Opportunity Occurs)
```
Opportunity: Early completion possible
Response: Add resources to definitely finish early, capture market

Opportunity: Technology enables additional features
Response: Allocate budget to implement features now
```

#### 2. Enhance (Increase Probability or Impact)
```
Opportunity: Might win industry award
Response: Dedicate resources to award submission, PR campaign

Opportunity: Could gain key partnership
Response: Executive sponsor engagement, proposal preparation
```

#### 3. Share (Partner to Realize Opportunity)
```
Opportunity: Large contract possible
Response: Joint venture with partner who has capacity

Opportunity: New market entry
Response: Strategic alliance with local firm
```

### 6. Implement Risk Responses

**Risk Response Plan Template**:
```markdown
## Risk #012: Third-Party API Reliability

**Category**: Technical - External Dependency
**Description**: Third-party payment API has history of outages (3 in last 6 months),
each lasting 2-4 hours. Outage during peak hours could prevent customers from
completing purchases.

**Analysis**:
- Probability: 4 (50-70% chance of outage during our 6-month project)
- Impact (Revenue): 4 (Could lose $20K in sales during 4-hour peak time outage)
- Impact (Reputation): 3 (Customer frustration, negative reviews)
- Risk Score: 4 × 4 = 16 (HIGH)
- EMV: 0.60 × $20,000 = $12,000

**Triggers/Early Warning Signs**:
- API response time increasing (>2 seconds)
- Vendor status page shows "investigating"
- Error rate above 1%
- Support tickets mentioning payment issues

**Response Strategy**: Mitigate + Accept

**Mitigation Actions** (Reduce probability and impact):
1. Implement circuit breaker pattern
   - Auto-failover to backup payment processor
   - Owner: Backend Lead
   - Due: Sprint 3 (Week 6)
   - Cost: 40 hours dev time ($4,000)

2. Add comprehensive monitoring
   - API health checks every 30 seconds
   - Alert if 3 consecutive failures
   - Owner: DevOps
   - Due: Sprint 2 (Week 4)
   - Cost: 16 hours ($1,600)

3. Queue payment processing
   - Decouple order creation from payment
   - Retry logic for failed payments
   - Owner: Backend Lead
   - Due: Sprint 3 (Week 6)
   - Cost: 24 hours ($2,400)

**Total Mitigation Cost**: $8,000
**Remaining Risk** (after mitigation):
- Probability: 2 (still might occur, but we'll handle it)
- Impact: 2 (5-minute failover, minimal revenue impact)
- New Score: 2 × 2 = 4 (LOW)
- Residual EMV: 0.15 × $2,000 = $300

**Contingency Plan** (if risk occurs despite mitigation):
1. Circuit breaker activates backup processor (automatic)
2. Monitor dashboard for alert
3. Post incident report on status page (within 15 min)
4. Customer support team alerted (automated)
5. Retry queued payments when primary API restored
6. Post-mortem within 24 hours

**Acceptance**:
Residual risk (score 4) is acceptable given mitigation cost vs. remaining exposure.

**Owner**: Backend Lead
**Status**: Active - Mitigation in progress
**Last Review**: 2025-01-20
**Next Review**: 2025-02-01
```

### 7. Monitor Risks

**Risk Review Meeting Agenda**:
```
Weekly Risk Review (30 min):

1. Status of Top 10 Risks (15 min)
   - Any changes in probability/impact?
   - Triggers observed?
   - Mitigation actions on track?

2. New Risks Identified (5 min)
   - From team members
   - From project changes
   - Quick assessment (full analysis offline)

3. Risks to Close (5 min)
   - Risks no longer relevant
   - Risks successfully mitigated
   - Archive with lessons learned

4. Escalations (5 min)
   - Risks exceeding tolerance
   - Decisions needed
   - Resource requests

5. Action Items (5 min)
   - Who, what, when
```

**Risk Monitoring Metrics**:

```
Risk Exposure (Trend over time):
Week 1: 145 (sum of all risk scores)
Week 2: 138 ↓
Week 3: 142 ↑
Week 4: 125 ↓

Goal: Decreasing trend (mitigation working)

Risk Velocity:
Time from identification to response plan:
- Average: 3.2 days
- Target: <5 days
- Status: On track

Risk Burndown:
Week 1: 24 open risks
Week 2: 26 open risks (+3 new, -1 closed)
Week 3: 24 open risks (+2 new, -4 closed)
Week 4: 21 open risks (+1 new, -4 closed)

Risks by Status:
- Identified: 3
- Analyzed: 5
- Response Planned: 8
- Mitigating: 10
- Closed: 15
- Realized: 2 (occurred, managed)
```

**Risk Triggers and Monitoring**:
```
Risk: Schedule Delay
Triggers:
✓ Sprint velocity <80% of average (Monitor: Weekly)
✓ Critical path tasks >90% time used (Monitor: Daily)
✓ >20% of tasks delayed (Monitor: Weekly)
✓ Resource availability <90% (Monitor: Weekly)

Risk: Budget Overrun
Triggers:
✓ Burn rate >10% above plan (Monitor: Weekly)
✓ CPI <0.95 (Monitor: Bi-weekly)
✓ Unplanned expenses >5% (Monitor: Weekly)

Risk: Quality Issues
Triggers:
✓ Test coverage <80% (Monitor: Daily)
✓ Defect density >2 per KLOC (Monitor: Sprint)
✓ Failed builds >10% (Monitor: Daily)
✓ Production defects detected (Monitor: Real-time)
```

---

## Risk Categories (Risk Breakdown Structure)

```
Project Risks
├── Technical Risks
│   ├── Technology Risks
│   │   ├── Unproven technology
│   │   ├── Technology obsolescence
│   │   ├── Vendor lock-in
│   │   └── Technical complexity
│   ├── Performance Risks
│   │   ├── Scalability issues
│   │   ├── Response time
│   │   └── Resource utilization
│   ├── Integration Risks
│   │   ├── Interface compatibility
│   │   ├── Data format issues
│   │   └── Third-party dependencies
│   └── Security Risks
│       ├── Vulnerabilities
│       ├── Data breaches
│       └── Compliance failures
├── Schedule Risks
│   ├── Estimation errors (optimistic)
│   ├── Dependency delays
│   ├── Resource availability
│   ├── Scope creep
│   └── Rework due to defects
├── Cost Risks
│   ├── Budget estimation errors
│   ├── Scope changes
│   ├── Resource rate increases
│   ├── Vendor cost overruns
│   └── Exchange rate fluctuations
├── Resource Risks
│   ├── Skill gaps
│   ├── Team turnover
│   ├── Competing priorities
│   ├── Low productivity
│   └── Key person dependency
├── External Risks
│   ├── Vendor/Supplier Issues
│   │   ├── Vendor bankruptcy
│   │   ├── Delivery delays
│   │   └── Quality issues
│   ├── Market Risks
│   │   ├── Competitive threats
│   │   ├── Market changes
│   │   └── Economic downturn
│   ├── Regulatory/Legal
│   │   ├── Regulatory changes
│   │   ├── Compliance requirements
│   │   └── Legal disputes
│   └── Environmental
│       ├── Natural disasters
│       ├── Pandemic
│       └── Political instability
└── Organizational Risks
    ├── Stakeholder conflict
    ├── Changing priorities
    ├── Inadequate sponsorship
    ├── Poor communication
    ├── Organizational restructuring
    └── Cultural resistance to change
```

---

## Common Project Risks (Checklist)

**Software Development**:
- [ ] Requirements unclear or changing
- [ ] Technology unproven or complex
- [ ] Team lacks required skills
- [ ] Third-party dependencies unreliable
- [ ] Integration more complex than expected
- [ ] Performance requirements not met
- [ ] Security vulnerabilities discovered
- [ ] Testing inadequate (time/coverage)
- [ ] Key developer leaves
- [ ] Scope creep from stakeholders

**Construction**:
- [ ] Weather delays
- [ ] Material availability/cost
- [ ] Site conditions differ from survey
- [ ] Regulatory approvals delayed
- [ ] Labor availability/strikes
- [ ] Design changes
- [ ] Subcontractor delays
- [ ] Equipment failures
- [ ] Safety incidents
- [ ] Neighbor complaints

**Product Launch**:
- [ ] Competitor launches first
- [ ] Market conditions change
- [ ] Manufacturing delays
- [ ] Quality issues in production
- [ ] Marketing campaign ineffective
- [ ] Distribution channel issues
- [ ] Pricing strategy fails
- [ ] Supply chain disruption
- [ ] Negative early reviews
- [ ] Intellectual property disputes

---

## Best Practices

1. **Involve the team**: Those doing the work identify best risks
2. **Create psychological safety**: No blame for raising risks
3. **Be specific**: "Database performance" not "Technical issues"
4. **Quantify**: "30% probability" not "might happen"
5. **Focus on root causes**: Not just symptoms
6. **Assign owners**: Every risk needs someone responsible
7. **Document triggers**: Enable early detection
8. **Update regularly**: Risks change constantly
9. **Close risks**: Archive when no longer relevant
10. **Learn from realized risks**: Feed into future projects
11. **Don't hide bad news**: Surface risks early while options exist
12. **Balance paranoia with pragmatism**: Not every risk needs mitigation
13. **Use data**: Historical data beats gut feel
14. **Plan contingencies for high-impact risks**: Even if low probability
15. **Communicate risk status**: Keep stakeholders informed

---

## Risk Management Anti-Patterns

❌ **"Risk Register as Checkbox"**: Creating register but never updating
✅ **Solution**: Schedule regular reviews, assign owners, track actions

❌ **"Wishful Thinking"**: Assuming risks won't occur
✅ **Solution**: Use historical data, be realistic in assessments

❌ **"Analysis Paralysis"**: Endless risk analysis, no action
✅ **Solution**: Time-box analysis, focus on top 20% of risks

❌ **"Hiding Risks"**: Not reporting risks that reflect poorly
✅ **Solution**: Create no-blame culture, reward risk identification

❌ **"One-Time Activity"**: Identify risks at start, forget about them
✅ **Solution**: Continuous identification, weekly reviews

❌ **"PM-Only Responsibility"**: Only PM manages risks
✅ **Solution**: Team-wide responsibility, distributed ownership

❌ **"No Contingency Budget"**: Spend contingency on scope creep
✅ **Solution**: Protect reserves, require approval for use

---

## Integration with Project Planning

**During Initiation**:
- Identify high-level risks
- Include in project charter
- Assess project viability

**During Planning**:
- Comprehensive risk identification
- Detailed analysis
- Build mitigation costs into budget
- Add buffers to schedule

**During Execution**:
- Monitor triggers
- Implement mitigation actions
- Identify new risks
- Update register weekly

**During Closure**:
- Archive risk register
- Lessons learned
- Feed into organizational process assets

---

**This skill is continuously updated with lessons learned from both successfully mitigated and realized risks across thousands of projects.**
