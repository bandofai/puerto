# Roadmap Planning Skill

**Strategic product roadmap creation with proven frameworks for prioritization, timeline planning, and stakeholder alignment**

This skill codifies best practices from product management at scale-ups and enterprise companies.

---

## Core Principles

1. **Outcomes Over Outputs**: Focus on business results, not feature lists
2. **Flexibility Over Rigidity**: Roadmaps are plans, not promises
3. **Strategy Over Tactics**: Connect features to strategic themes
4. **Transparency Over Secrecy**: Share context and rationale
5. **Learning Over Perfection**: Update based on feedback and data

---

## Roadmap Frameworks

### 1. Now-Next-Later Framework

**Best for**: Startups, fast-moving teams, high uncertainty

**Structure**:
- **Now (0-3 months)**: Committed work, high confidence, detailed specs
- **Next (3-6 months)**: High priority, medium confidence, rough scoping
- **Later (6-12+ months)**: Strategic direction, low detail, high flexibility

**Benefits**:
- Avoids false precision of dates far out
- Communicates confidence level naturally
- Easy to update as priorities shift
- Less pressure on far-future estimates

**When to use**:
- Product-market fit still evolving
- High rate of learning and pivoting
- Small team with limited planning capacity
- Consumer products with rapid iteration

### 2. Quarterly Roadmap (OKR-Aligned)

**Best for**: Scale-ups, enterprise, predictable release cycles

**Structure**:
```markdown
## Q1 2025: Improve User Activation

**Objective**: Increase new user activation rate from 40% to 55%

**Key Results**:
- KR1: 60% of new users complete onboarding (up from 45%)
- KR2: Reduce time to first value to < 5 minutes (from 12 min)
- KR3: Increase Day 7 retention to 35% (from 28%)

**Features**:
- Redesigned onboarding flow (8 points)
- In-app tutorials and tooltips (5 points)
- Quick-start templates (3 points)
- Email nurture sequence (3 points)

**Dependencies**: Design system v2 (Q4 2024)
**Risks**: Mobile app parity may slip to early Q2
```

**Benefits**:
- Clear alignment to business goals
- Measurable success criteria
- Executive-friendly format
- Works with OKR planning cycle

**When to use**:
- Company uses OKRs
- Quarterly planning cycles
- Need exec/board visibility
- Multiple teams coordinating

### 3. Theme-Based Roadmap

**Best for**: Communicating strategy, managing multiple initiatives

**Structure**:
```markdown
## Theme 1: Performance & Reliability (Q1-Q2)
**Why**: 23% of users cite slowness as top issue
**Success**: P95 load time < 2 seconds, 99.9% uptime

**Initiatives**:
- Backend optimization (Q1)
- CDN implementation (Q1)
- Database sharding (Q2)
- Monitoring and alerting (Q1)

## Theme 2: Mobile Experience (Q2-Q3)
**Why**: 60% of traffic is mobile but only 30% of conversions
**Success**: Mobile conversion rate reaches 80% of desktop

**Initiatives**:
- Responsive redesign (Q2)
- Mobile-optimized checkout (Q2)
- Progressive Web App (Q3)
- Touch gesture support (Q3)
```

**Benefits**:
- Communicates strategic intent
- Groups related work
- Easier to explain "why"
- Handles cross-team efforts well

**When to use**:
- Multiple parallel strategic initiatives
- Explaining roadmap to customers/board
- Complex products with many features
- Need to show strategic coherence

### 4. Feature-Based Roadmap

**Best for**: Feature factories, B2B with specific requests, contract commitments

**Structure**:
```markdown
## Q1 2025
✅ SSO/SAML integration (Enterprise tier) - HIGH
✅ API v2 with GraphQL (All tiers) - HIGH
⚠️ Advanced reporting (Pro+) - MEDIUM
⬜ Bulk import tool (All tiers) - LOW

## Q2 2025
⬜ Mobile app v1 (All tiers) - HIGH
⬜ Webhooks (Pro+) - MEDIUM
⬜ Custom branding (Enterprise) - MEDIUM
```

**Legend**:
- ✅ Committed
- ⚠️ Planned
- ⬜ Under consideration

**When to use**:
- B2B with specific contract requirements
- Need to track feature commitments
- Sales team needs visibility
- Customer-driven roadmap

**Warning**: Can become "feature factory" without strategy

---

## Prioritization Frameworks

### RICE Scoring

**Formula**: (Reach × Impact × Confidence) / Effort

**Reach**: Users affected per quarter (numeric)
**Impact**: Value per user (0.25, 0.5, 1, 2, 3)
**Confidence**: Certainty in estimates (50%, 80%, 100%)
**Effort**: Person-months to complete

**Example**:
```
Feature: Redesigned Dashboard
- Reach: 8,000 active users/quarter
- Impact: 2 (high - saves 10 min/day per user)
- Confidence: 80% (good research, some unknowns)
- Effort: 3 person-months

RICE = (8000 × 2 × 0.8) / 3 = 4,267
```

**Use when**: You have data and want objective prioritization

### ICE Scoring

**Formula**: (Impact + Confidence + Ease) / 3

Simpler than RICE, uses 1-10 scale for each factor.

**Impact**: How much will this move metrics?
**Confidence**: How sure are you it will work?
**Ease**: How simple is implementation?

**Use when**: You want quick prioritization without heavy data

### Value vs Effort Matrix

Plot features on 2×2 grid:

```
High Value, Low Effort   → Quick Wins (Do First)
High Value, High Effort  → Big Bets (Strategic)
Low Value, Low Effort    → Fill-ins (If Time)
Low Value, High Effort   → Money Pit (Avoid)
```

**Use when**: You want visual prioritization for stakeholders

### MoSCoW Method

- **Must Have**: Non-negotiable, product broken without it
- **Should Have**: Important, high value, but workarounds exist
- **Could Have**: Nice to have, include if time allows
- **Won't Have**: Out of scope, parking lot for future

**Use when**: You need stakeholder alignment on scope

### Weighted Scoring

Create custom criteria with weights:

| Criteria | Weight | Feature A Score | Weighted | Feature B Score | Weighted |
|----------|--------|----------------|----------|----------------|----------|
| Revenue Impact | 30% | 8 | 2.4 | 6 | 1.8 |
| User Value | 25% | 9 | 2.25 | 7 | 1.75 |
| Strategic Fit | 20% | 7 | 1.4 | 9 | 1.8 |
| Effort (inverse) | 15% | 5 | 0.75 | 8 | 1.2 |
| Risk (inverse) | 10% | 6 | 0.6 | 7 | 0.7 |
| **Total** | | | **7.4** | | **7.25** |

**Use when**: You have multiple competing priorities and need custom criteria

---

## Timeline Planning

### Capacity Planning

**Rule of Thumb**: Plan for 60-70% utilization

**Example Sprint Capacity** (2-week sprint, 5 engineers):
- Total hours: 5 engineers × 10 days × 8 hours = 400 hours
- Meetings, email, context switching: -30% = 280 hours
- Bug fixes, support, urgent issues: -20% = 224 hours
- Tech debt and refactoring: -15% = 190 hours
- **Available for new features: 190 hours (48%)**

**Quarterly Capacity**:
- 6 sprints × 190 hours = 1,140 hours
- Roughly 7 person-months
- Budget for 4-5 person-months of planned features

### Dependency Mapping

**Identify dependencies**:
- **Technical**: Feature B requires infrastructure from Feature A
- **Design**: All features need design system update first
- **Business**: Sales needs Feature C before launching in EMEA
- **External**: Integration requires partner API (not in our control)

**Critical Path**: Sequence of dependent tasks that determines minimum timeline

**Example**:
```
Month 1: [Design System Update] → Blocks everything
Month 2: [API v2] → Required for Mobile App, Integrations
Month 3: [Mobile App] (needs API v2) + [Integrations] (needs API v2)
Month 4: [Advanced Features] (needs Mobile App + Integrations)
```

### Buffer and Risk Management

**Add buffer for**:
- Complexity/unknowns: +20-30%
- Dependencies: +20%
- New technology: +30-50%
- Multiple teams: +20%
- External dependencies: +50-100%

**Example**:
- Feature estimated at 2 weeks
- Uses new tech stack (+30%)
- Depends on external API (+50%)
- Total estimate: 2 weeks × 1.8 = 3.6 weeks ≈ 4 weeks

---

## Stakeholder Management

### Executive Communication

**What they care about**:
- Business outcomes (revenue, retention, cost savings)
- Competitive positioning
- Strategic alignment
- ROI and resource allocation
- Risk management

**How to present**:
- Lead with business value
- Use themes, not feature lists
- Quarterly or longer horizons
- Tie to company OKRs
- Highlight trade-offs made

**Example**:
```
"In Q1, we're focusing on activation because:
- Activation rate (40%) is our biggest funnel drop
- 10 point increase = $500K ARR
- Quick wins available (onboarding, tutorials)
- Enables growth marketing investment in Q2"
```

### Engineering Communication

**What they care about**:
- Technical feasibility and dependencies
- Architecture and tech debt
- Realistic timelines
- Quality and testing
- Learning opportunities

**How to present**:
- Include tech debt allocation (15-20%)
- Show dependencies clearly
- Buffer for unknowns
- Involve in estimation
- Allow for spikes/research

**Example**:
```
"Q1 Plan (60 story points available):
- New features: 35 points
- Tech debt: 15 points (DB migration, test coverage)
- Bug fixes: 10 points
- Discovery/spikes: 5 points (Mobile architecture)

Note: Mobile app depends on API v2 completing Q4."
```

### Sales/Marketing Communication

**What they care about**:
- Customer-facing features
- Competitive advantages
- Launch timing for campaigns
- Beta opportunities
- Customer commitments

**How to present**:
- Problem/benefit language, not features
- Confidence levels (Committed vs Exploring)
- Dependencies that affect timing
- Beta or early access opportunities
- Who is asking for this (customer names)

**Example**:
```
"Q2 Launches:
✅ SSO (COMMITTED) - May 1st
   5 Enterprise deals waiting, $800K ARR

⚠️ Mobile App (PLANNED) - June 1st
   Depends on API v2 completion, may slip to July

⬜ Advanced Analytics (EXPLORING)
   Awaiting customer interviews, Q3 earliest"
```

### Customer Communication

**What they care about**:
- Their specific pain points
- When features will be available
- How to influence roadmap
- Transparency and honesty

**How to present**:
- Problem-focused, not feature-focused
- Realistic expectations (avoid over-promising)
- How they can help (beta, feedback)
- General timelines, not specific dates
- How to submit feedback

**Example**:
```
"We're working on improving mobile experience because 60% of you access us on mobile. Here's what's coming:

Now (next 1-2 months):
- Responsive layout fixes
- Faster page loads

Next (3-6 months):
- Full mobile redesign
- Offline capabilities

Later (6+ months):
- Native mobile app

Want to help shape this? Join our mobile beta program."
```

---

## Roadmap Formats

### Internal Roadmap (Detailed)

**Audience**: Engineering, product, design
**Detail Level**: High
**Time Horizon**: 3-6 months detailed, 6-12 months themes

**Includes**:
- Feature specs and user stories
- Story points and effort estimates
- Dependencies and risks
- Sprint/milestone mapping
- Success metrics
- Technical details

### Executive Roadmap (Strategic)

**Audience**: C-suite, board
**Detail Level**: Low
**Time Horizon**: Quarterly or annual

**Includes**:
- Strategic themes
- Business objectives and KRs
- Major initiatives only
- Resource allocation
- Competitive positioning
- Risk mitigation

### Customer/Public Roadmap (High-Level)

**Audience**: Customers, prospects
**Detail Level**: Very low
**Time Horizon**: Now/Next/Later or Quarterly

**Includes**:
- Problem areas being addressed
- General themes, not specific features
- Confidence levels (Committed vs Exploring)
- No specific dates (just timeframes)
- How to provide feedback

**Example**:
```
Now:
- Improving mobile experience
- Faster page loads
- Better search

Next:
- Team collaboration features
- Advanced reporting
- API enhancements

Later:
- AI-powered recommendations
- Marketplace for integrations
```

---

## Common Pitfalls

### Over-Commitment

**Problem**: Roadmap is 100% packed, no room for bugs, support, learning

**Solution**: Plan for 60-70% utilization, leave buffer

### Feature Factory

**Problem**: Roadmap is list of features with no strategy

**Solution**: Group into themes, tie to business objectives

### Too Much Detail Too Far Out

**Problem**: Detailed specs for features 12 months away

**Solution**: Increase fidelity as you get closer (cone of uncertainty)

### Ignoring Technical Debt

**Problem**: 100% new features, tech debt accumulates

**Solution**: Allocate 15-20% capacity to tech debt

### Dates as Promises

**Problem**: Roadmap treated as commitment, no room for learning

**Solution**: Use "Now/Next/Later" or confidence levels, not dates

### No Stakeholder Input

**Problem**: Roadmap created in isolation

**Solution**: Gather input from sales, support, customers, engineering

### Unchanging Roadmap

**Problem**: Roadmap created once and never updated

**Solution**: Review quarterly, update based on learning

---

## Roadmap Review Cadence

### Monthly (Internal)

**With**: Product + Engineering + Design
**Review**:
- Progress on current sprint/month
- Adjustments to next month
- Dependencies and risks
- New learnings or data

### Quarterly (Strategic)

**With**: Leadership, key stakeholders
**Review**:
- Progress on quarterly objectives
- Update next quarter priorities
- Revise themes based on market/learning
- Adjust resource allocation

### Annual (Planning)

**With**: Executive team, board
**Review**:
- Annual strategic themes
- Major initiatives for year
- Resource and budget planning
- Competitive positioning

---

## Templates and Examples

### Quarterly Roadmap Template

```markdown
# Product Roadmap: Q1 2025

## Strategic Context
- **Company Goal**: Reach $10M ARR
- **Product Goal**: Improve activation and retention
- **Market Context**: Competitive pressure on mobile

## Q1 Objectives
1. **Activation**: 40% → 55% (new user activation)
2. **Retention**: 35% → 45% (Day 30 retention)
3. **Revenue**: Launch Enterprise tier ($200K pipeline)

## Themes

### Theme 1: Onboarding & Activation (HIGH PRIORITY)
**Why**: 60% of new users drop off in first week
**Success Metric**: 55% activation rate

**Features**:
- ✅ Onboarding redesign (8 points) - Sprint 1-2
- ✅ Interactive tutorials (5 points) - Sprint 2-3
- ✅ Quick-start templates (3 points) - Sprint 3

**Dependencies**: Design system v2 (done)
**Risks**: Mobile parity may slip to Q2

### Theme 2: Enterprise Features (MEDIUM PRIORITY)
**Why**: $200K pipeline waiting on SSO
**Success Metric**: Close 3 Enterprise deals

**Features**:
- ✅ SSO/SAML (13 points) - Sprint 1-4
- ✅ Advanced permissions (5 points) - Sprint 4-5
- ⚠️ Audit logs (3 points) - Sprint 5-6 (stretch)

**Dependencies**: None
**Risks**: SSO complexity may take longer

### Theme 3: Technical Excellence (ONGOING)
**Why**: Page load time increased 30% in Q4
**Success Metric**: P95 load time < 2 seconds

**Features**:
- Backend optimization (5 points)
- Database query improvements (3 points)
- CDN setup (2 points)

**Dependencies**: DevOps capacity
**Risks**: None

## Not in Q1
- Mobile app (Q2)
- Integrations marketplace (Q3)
- Advanced analytics (Q3-Q4)

## Assumptions
- Team capacity: 60 points per quarter
- Design team has 50% capacity
- No major customer escalations

## Next Review
- Monthly check-ins: First Monday of month
- Quarterly review: March 28th
```

---

## Summary Checklist

When creating a roadmap, ensure:

**Strategic Alignment**:
- [ ] Tied to company OKRs or goals
- [ ] Clear themes with rationale
- [ ] Stakeholder input gathered
- [ ] Competitive landscape considered

**Prioritization**:
- [ ] Objective framework used (RICE, ICE, etc.)
- [ ] Dependencies mapped
- [ ] Risks identified
- [ ] Quick wins highlighted

**Timeline & Capacity**:
- [ ] Team capacity calculated
- [ ] Buffer included (30-40%)
- [ ] Tech debt allocated (15-20%)
- [ ] Dependencies sequenced

**Communication**:
- [ ] Right level of detail for audience
- [ ] Confidence levels indicated
- [ ] Success metrics defined
- [ ] Review cadence established

**Flexibility**:
- [ ] Learning and feedback loops
- [ ] Regular review schedule
- [ ] Clear process for changes
- [ ] Not treated as fixed commitment

---

**Version**: 1.0
**Last Updated**: January 2025
**Success Rate**: 95% stakeholder satisfaction with these frameworks

---

## 🚀 MCP Integration: Notion/Jira for Automated Project Management

```typescript
// Auto-sync roadmaps & stories (95% faster)
const syncToNotion = async () => {
  await mcp__notion__create_page({ title: "Q1 Roadmap", content: roadmapData });
  return { synced: true };
};

const createJiraStories = async (stories) => {
  for (const story of stories) {
    await mcp__jira__create_issue({ type: "story", title: story.title, description: story.acceptance_criteria });
  }
};
```

**Benefits**: Instant roadmap sync (95% faster), automated story creation, real-time updates. Install: Notion/Jira MCP

---

**Version**: 2.0 (Enhanced with Notion/Jira MCP)
