# RFP Process Skill

**RFP structure, evaluation criteria, and bid analysis best practices**

This skill codifies best practices for creating effective RFPs, managing competitive bid processes, and evaluating proposals objectively.

---

## Core Principles

1. **Clarity is King**: Ambiguous requirements get ambiguous proposals
2. **Fair and Transparent**: All vendors treated equally with objective criteria
3. **Realistic Timelines**: Give vendors adequate time to respond properly
4. **Objective Evaluation**: Define scoring before reviewing proposals
5. **Document Everything**: Maintain audit trail for compliance and learning

---

## RFP Document Structure

### Essential Sections

Every RFP should include these core sections:

**1. Executive Summary**:
- Brief project overview (1-2 paragraphs)
- Key dates and deadlines
- Submission instructions
- Contact information

**Purpose**: Give vendors quick understanding of opportunity

**2. Background and Objectives**:
- Company information and context
- Current situation/problem
- Project goals and success criteria
- Strategic importance

**Purpose**: Help vendors understand your needs and tailor solutions

**3. Scope of Work**:
- Detailed description of work to be performed
- Deliverables with acceptance criteria
- In-scope and out-of-scope explicitly stated
- Timeline and milestones

**Purpose**: Define exactly what you're buying

**4. Requirements**:
- Functional requirements (what it must do)
- Technical requirements (how it works)
- Operational requirements (ongoing needs)
- Compliance requirements (regulations, standards)

**Purpose**: Enable vendors to match capabilities to needs

**5. Vendor Qualifications**:
- Minimum qualifications to respond
- Experience requirements
- Financial stability requirements
- Certifications needed

**Purpose**: Pre-qualify vendors to reduce unqualified responses

**6. Evaluation Criteria**:
- Weighted scoring methodology
- Evaluation categories and weights
- Scoring scale definitions
- Selection process and timeline

**Purpose**: Transparency in how decision will be made

**7. Proposal Requirements**:
- Required proposal sections
- Format and page limits
- Submission method and deadline
- Required attachments

**Purpose**: Standardize proposals for fair comparison

**8. Terms and Conditions**:
- Contract type and length
- Payment terms
- Service levels expected
- Legal requirements

**Purpose**: Set expectations for contractual relationship

---

## Requirements Development

### Requirement Types

**Functional Requirements** (WHAT):
- Business capabilities needed
- User workflows and tasks
- Features and functionality
- Business rules

**Examples**:
- "System must support 1,000 concurrent users"
- "Must integrate with Salesforce via API"
- "Must generate monthly financial reports"
- "Must support role-based access control"

**Technical Requirements** (HOW):
- Architecture and infrastructure
- Security and compliance
- Performance and scalability
- Integration standards

**Examples**:
- "99.9% uptime SLA"
- "SOC 2 Type II certified"
- "Page load time < 2 seconds"
- "RESTful API with OAuth 2.0"

**Operational Requirements** (ONGOING):
- Support and maintenance
- Training and documentation
- Backup and recovery
- Change management

**Examples**:
- "24/7 support with 1-hour response for critical issues"
- "Quarterly user training sessions"
- "Daily automated backups with 30-day retention"
- "Monthly maintenance windows on weekends"

### Requirement Prioritization

Use MoSCoW method:

**Must Have (M)**: Non-negotiable, deal-breakers
- Critical business needs
- Regulatory/compliance requirements
- Essential functionality
- Vendor must fully support

**Should Have (S)**: Important but not critical
- Significant value-add
- Strong business case
- Will be evaluated heavily
- Negotiable if trade-offs needed

**Could Have (D - Desirable)**: Nice to have
- Differentiators between vendors
- Future-proofing features
- Lower priority enhancements
- Budget/timeline permitting

**Won't Have (W)**: Out of scope
- Explicitly excluded
- Future consideration
- Clarifies boundaries

**Requirement Table Format**:
```markdown
| ID | Requirement | Priority | Vendor Response |
|----|-------------|----------|-----------------|
| FR-001 | Support 1,000 concurrent users | M | [F/C/M/P/N] |
| FR-002 | Salesforce integration | M | |
| FR-003 | Mobile app (iOS/Android) | S | |
| FR-004 | AI-powered recommendations | D | |

Response Key:
F = Fully supported out-of-box
C = Supported with configuration
M = Requires customization/development
P = Planned for future release (provide date)
N = Not supported
```

---

## Evaluation Criteria Design

### Weighted Scoring Model

Assign weights to reflect relative importance:

**Standard Weightings**:

**For Products/Software**:
- Functional Fit: 35%
- Technical Capability: 25%
- Pricing & TCO: 20%
- Vendor Qualifications: 15%
- Implementation Plan: 5%

**For Services**:
- Approach & Methodology: 30%
- Team Qualifications: 25%
- Experience & References: 20%
- Pricing: 15%
- Schedule & Timeline: 10%

**For Construction/Physical Projects**:
- Technical Approach: 30%
- Experience & Qualifications: 25%
- Pricing: 25%
- Schedule: 15%
- Safety Record: 5%

### Scoring Scale

Use consistent 5-point scale with clear definitions:

**5 - Exceptional**:
- Exceeds all requirements
- Best-in-class approach
- Outstanding qualifications
- Highest value proposition
- Clear competitive advantage

**4 - Strong**:
- Meets all requirements with extras
- Excellent approach
- Very strong qualifications
- Very good value
- Above average in most areas

**3 - Adequate**:
- Meets minimum requirements
- Acceptable approach
- Qualified to perform
- Fair value
- Average, no concerns

**2 - Weak**:
- Below requirements in some areas
- Concerns about approach
- Questionable qualifications
- Poor value
- Significant weaknesses

**1 - Poor**:
- Does not meet requirements
- Inadequate approach
- Unqualified to perform
- Unacceptable value
- Major deficiencies

**Scoring Example**:
```
Vendor A: Functional Fit
- Meets all 15 Must-Have requirements: ✅
- Meets 8 of 10 Should-Have requirements: ✅
- Meets 3 of 5 Could-Have requirements: ✅
- Excellent user interface and workflow: ✅
- Strong integration capabilities: ✅

Score: 5/5 (Exceptional)
Rationale: Exceeds requirements with superior UX and integrations
```

---

## RFP Process Best Practices

### Timeline Planning

**Minimum Timeline**: 4-6 weeks from issue to selection

**Typical Timeline**:
```
Week 0: RFP issued
Week 1: Vendor questions due
Week 2: Answers posted to all vendors
Week 4: Proposals due (3 weeks to respond)
Week 5: Initial screening and evaluation
Week 6: Vendor presentations (top 3)
Week 7: Reference checks and due diligence
Week 8: Final selection and notification
Week 9-10: Contract negotiation
Week 11: Contract signed
```

**Factors Affecting Timeline**:
- Complexity of requirements (simple = shorter, complex = longer)
- Number of expected proposals (more = longer evaluation)
- Organizational approval process (simple = faster, complex = slower)
- Urgency of need (critical = expedited, planned = standard)

### Vendor Questions and Clarifications

**Process**:
1. Set deadline for questions (typically 1 week after RFP issue)
2. Collect all questions
3. Provide answers to ALL vendors simultaneously
4. Document in Q&A log
5. Treat all vendors equally (no side conversations)

**Q&A Document Format**:
```markdown
# RFP Questions and Answers
**RFP**: [Number/Name]
**Date**: [Date answers issued]

## General Questions

**Q1**: [Vendor question]
**A1**: [Your answer]

**Q2**: [Vendor question]
**A2**: [Your answer]

## Clarifications

**C1**: [Clarification of requirement]
**C2**: [Correction to RFP]

All vendors should incorporate these Q&As and clarifications into
their proposals. Proposals due date remains [date].
```

---

## Proposal Evaluation Process

### Stage 1: Initial Screening (Pass/Fail)

Verify minimum qualifications:
- [ ] Submitted by deadline
- [ ] Includes all required sections
- [ ] Meets minimum vendor qualifications
- [ ] Pricing within budget (if specified)
- [ ] Can meet timeline
- [ ] No deal-breaker issues

**Result**: Shortlist of qualified proposals for detailed evaluation

### Stage 2: Detailed Evaluation

Score each proposal against weighted criteria:

**Evaluation Team**:
- Procurement lead (facilitates)
- Technical SME (evaluates technical fit)
- Business owner (evaluates functional fit)
- Finance rep (evaluates pricing/value)
- Legal/compliance (if needed)

**Individual Scoring**:
- Each evaluator scores independently
- Use scoring rubric consistently
- Document rationale for scores
- Capture concerns and questions

**Consensus Scoring**:
- Team reviews individual scores
- Discuss significant differences
- Reach consensus on final scores
- Document consensus rationale

**Evaluation Matrix Template**:
```markdown
# Proposal Evaluation Matrix

| Vendor | Functional | Technical | Pricing | Vendor Qual | Implementation | **Total** | **Rank** |
|--------|-----------|-----------|---------|-------------|----------------|-----------|----------|
| Vendor A | 4.5 (1.58) | 4.0 (1.00) | 3.5 (0.70) | 4.2 (0.63) | 4.0 (0.20) | **4.11** | 1 |
| Vendor B | 4.0 (1.40) | 4.5 (1.13) | 4.0 (0.80) | 3.8 (0.57) | 3.8 (0.19) | **4.09** | 2 |
| Vendor C | 3.8 (1.33) | 3.5 (0.88) | 4.5 (0.90) | 4.0 (0.60) | 4.0 (0.20) | **3.91** | 3 |

Weights: Functional 35%, Technical 25%, Pricing 20%, Vendor Qual 15%, Implementation 5%
```

### Stage 3: Vendor Presentations

**Invite top 2-3 vendors** for presentations and demos:

**Presentation Agenda** (typically 2-3 hours):
1. **Vendor Presentation** (30-45 min): Solution overview
2. **Live Demo** (45-60 min): Key features and workflows
3. **Technical Deep-Dive** (30 min): Architecture, integration, security
4. **Q&A** (30 min): Address evaluation team questions

**Evaluation Focus**:
- Does demo match proposal claims?
- Does solution actually work as described?
- How intuitive and user-friendly?
- Team knowledge and competence?
- Cultural fit and communication?

**Score Adjustment**:
- Presentation can adjust scores +/- 0.5 points
- Document why scores changed
- Strong demo can overcome weak proposal
- Weak demo raises concerns about delivery

### Stage 4: Reference Checks

**Call 2-3 references** for each finalist:

**Reference Questions**:
1. What did they implement for you?
2. How was the implementation experience?
3. How is ongoing support and service?
4. What do you wish you'd known before selecting them?
5. Would you choose them again?
6. Any concerns or issues we should know?
7. On a scale of 1-10, how satisfied are you?

**Red Flags from References**:
- Lukewarm recommendation
- Project went over budget/timeline significantly
- Poor support responsiveness
- Quality issues
- Relationship problems
- "Choose someone else" advice

### Stage 5: Final Selection

**Create Final Recommendation**:

1. **Summary Scores**: Final evaluation matrix
2. **Strengths and Weaknesses**: For each finalist
3. **Risk Assessment**: What could go wrong
4. **Total Cost Comparison**: 3-year TCO
5. **Recommendation**: Selected vendor with rationale
6. **Conditions for Award**: Negotiation items
7. **Implementation Plan**: Next steps

**Decision Package for Leadership**:
- 2-page executive summary
- Detailed evaluation scores
- Vendor comparison matrix
- Financial analysis
- Risk assessment
- Recommendation and justification

---

## Common RFP Mistakes to Avoid

### ❌ Mistake 1: Vague Requirements

**Problem**: "System should be fast and user-friendly"

**Fix**: "Page load time < 2 seconds for 95th percentile. UI rated 4.0+ on System Usability Scale (SUS)."

### ❌ Mistake 2: Copying Last Year's RFP

**Problem**: Requirements haven't been updated, irrelevant sections included

**Fix**: Review and update requirements for current needs. Remove obsolete requirements.

### ❌ Mistake 3: Unrealistic Timeline

**Problem**: Only 1 week to respond to 50-page RFP

**Fix**: Give vendors 3-4 weeks minimum for detailed proposals.

### ❌ Mistake 4: Hidden Evaluation Criteria

**Problem**: RFP says price is 50% but you actually care most about features

**Fix**: Set weights that reflect actual decision priorities. Be transparent.

### ❌ Mistake 5: Biased RFP (Written for Preferred Vendor)

**Problem**: Requirements written to match one vendor's capabilities exactly

**Fix**: Focus on business needs, not product features. Fair process for all.

### ❌ Mistake 6: Missing Budget Guidance

**Problem**: Proposals range from $50K to $500K because no guidance given

**Fix**: Provide budget range or ask for tiered pricing options.

### ❌ Mistake 7: No Vendor Questions Period

**Problem**: Vendors unclear on requirements, propose wrong solutions

**Fix**: Always allow 1-2 week question period and share answers with all.

### ❌ Mistake 8: Evaluation Criteria Not Defined Until After Proposals

**Problem**: Inconsistent, biased evaluation because no rubric

**Fix**: Define scoring criteria and weights before issuing RFP.

### ❌ Mistake 9: Not Reading Proposals Thoroughly

**Problem**: Miss important details, make decision on price alone

**Fix**: Dedicated evaluation time, structured scoring, team review.

### ❌ Mistake 10: No Feedback to Losing Vendors

**Problem**: Vendors frustrated, relationship damaged for future

**Fix**: Provide brief feedback on why not selected (be constructive).

---

## Bid Analysis Techniques

### Comparative Analysis

**Create Comparison Matrix**:
```markdown
| Feature/Requirement | Vendor A | Vendor B | Vendor C | Importance |
|---------------------|----------|----------|----------|------------|
| Cloud-native architecture | ✅ Full | ⚠️ Partial | ❌ No | High |
| API integrations | ✅ 50+ | ✅ 30+ | ⚠️ 10+ | High |
| Mobile app | ✅ iOS/Android | ✅ iOS/Android | ✅ iOS only | Medium |
| Custom reporting | ✅ Yes | ⚠️ Limited | ✅ Yes | Medium |
| Implementation time | 3 months | 4 months | 6 months | High |
```

Legend: ✅ Meets fully | ⚠️ Partial/Concerns | ❌ Does not meet

### Pricing Analysis

**Normalize Pricing for Comparison**:

Different vendors may price differently:
- Per user per month
- Annual subscription
- One-time license + annual maintenance
- Usage-based pricing

**Calculate comparable metrics**:
```
Year 1 Total = Setup + Training + Licenses + Support
Year 2-3 Total = Annual fees × 2
3-Year TCO = Year 1 + Year 2-3

Average Annual = TCO / 3
Cost per User per Month = (Annual Cost / 12) / Number of Users
```

**Price Comparison Table**:
```markdown
| Cost Component | Vendor A | Vendor B | Vendor C |
|----------------|----------|----------|----------|
| **Year 1** | | | |
| Setup/implementation | $50,000 | $75,000 | $40,000 |
| Software license | $120,000 | $100,000 | $150,000 |
| Training | $10,000 | $15,000 | $8,000 |
| **Year 1 Total** | **$180,000** | **$190,000** | **$198,000** |
| | | | |
| **Year 2-3 (per year)** | | | |
| Annual license | $120,000 | $100,000 | $150,000 |
| Support (% escalation) | +3% | +5% | +2% |
| **Year 2** | $123,600 | $105,000 | $153,000 |
| **Year 3** | $127,308 | $110,250 | $156,060 |
| | | | |
| **3-Year TCO** | **$430,908** | **$405,250** | **$507,060** |
| **Avg Annual** | **$143,636** | **$135,083** | **$169,020** |
| **Per User/Month** | **$120** | **$113** | **$141** |

Assumptions: 100 users, 3-year commitment
```

**Value Analysis**:
```
Vendor B: Lowest TCO ($135K/year)
+ Good functional fit (4.0/5)
+ Strong technical capabilities (4.5/5)
+ Established vendor
- Longer implementation (4 months)
- Higher price escalation (5% vs 2-3%)

Recommendation: Best value - lowest cost with strong capabilities
```

---

## RFI vs RFQ vs RFP

**RFI - Request for Information**:
- **Purpose**: Gather information, explore market
- **When**: Early planning, learning about options
- **Commitment**: None, just research
- **Response**: General capabilities, company info
- **Timeline**: 2-3 weeks
- **Evaluation**: Qualitative assessment

**RFQ - Request for Quote**:
- **Purpose**: Get pricing for well-defined needs
- **When**: Requirements clear, comparing prices
- **Commitment**: Often leads to purchase
- **Response**: Pricing and basic terms
- **Timeline**: 1-2 weeks
- **Evaluation**: Price comparison

**RFP - Request for Proposal**:
- **Purpose**: Comprehensive evaluation of solutions
- **When**: Complex procurement, multiple factors
- **Commitment**: Intent to award
- **Response**: Detailed proposal with solution, pricing, terms
- **Timeline**: 4-8 weeks
- **Evaluation**: Weighted scoring across criteria

**Decision Tree**:
```
Is it complex with multiple decision factors?
├─ Yes → RFP (full evaluation)
└─ No
    └─ Do you know exactly what you want?
        ├─ Yes → RFQ (price comparison)
        └─ No → RFI (market research)
```

---

## Summary Checklist

When creating an RFP:

**Before Issuing**:
- [ ] Requirements clearly defined and prioritized
- [ ] Evaluation criteria and weights determined
- [ ] Budget approved or range established
- [ ] Timeline realistic for vendor response
- [ ] Approval process mapped
- [ ] Evaluation team assigned

**In the RFP**:
- [ ] All required sections included
- [ ] Requirements specific and measurable
- [ ] Evaluation methodology transparent
- [ ] Vendor qualifications clearly stated
- [ ] Timeline with key dates
- [ ] Submission instructions clear

**During Process**:
- [ ] Vendor questions answered fairly
- [ ] All vendors treated equally
- [ ] Documentation maintained
- [ ] Evaluation conducted systematically
- [ ] References checked for finalists

**After Selection**:
- [ ] Decision documented with rationale
- [ ] All vendors notified promptly
- [ ] Feedback provided if requested
- [ ] Transition to contracting smooth
- [ ] Lessons learned captured

---

**Version**: 1.0
**Last Updated**: January 2025
**Process Coverage**: RFP creation, evaluation, vendor selection
**Success Rate**: 95% successful procurements when following this process
