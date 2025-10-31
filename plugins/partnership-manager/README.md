# Partnership Manager Plugin

Strategic partnership specialist for identifying potential partners, creating partnership proposals, structuring deals, negotiating contracts, and managing ongoing partner relationships.

## Overview

The Partnership Manager plugin provides agents for the complete partnership lifecycle: from partner identification and qualification through proposal creation, deal structuring, and ongoing relationship management. All agents leverage comprehensive partnership strategy frameworks including qualification criteria, economic models, negotiation tactics, and performance tracking.

## Agents

### 1. partner-identifier (Sonnet, WebSearch-Enabled, Skill-Aware)
Researches and identifies potential strategic partners with qualification scoring and prioritization.

**Use for**: Partner research, market analysis, partner qualification, tier classification

**Example**:
```
Use partner-identifier to find channel partners.
Business context: B2B SaaS HR platform ($20M ARR, 2000 customers)
Partnership objective: Expand into mid-market segment through reseller channels
Target partners:
- HR consultancies with 50+ consultants
- Implementation partners serving mid-market (100-1000 employees)
- Geography: North America initially
- Must have: Strong mid-market customer base, implementation capabilities, existing HR tech partnerships

Research and identify top 5 Tier 1 partners with:
- Weighted scorecard (strategic fit, market reach, capabilities, financial health, track record)
- Estimated revenue potential ($500K+ annually)
- Key decision-makers and contact information
- Recommendation and next steps
```

### 2. proposal-writer (Sonnet, Skill-Aware)
Creates compelling partnership proposals, pitch decks, and value propositions.

**Use for**: Partnership proposals, pitch decks, one-pagers, value proposition development

**Example**:
```
Use proposal-writer for technology integration partnership.
Partner: Salesforce (CRM platform, 100K+ customers)
Our company: Email marketing platform ($15M ARR, 3000 customers)
Partnership type: Bi-directional API integration + co-marketing
Value for Salesforce:
- Access to our 3000 SMB customers (many use Salesforce, want seamless integration)
- Strengthens Salesforce's marketing automation ecosystem
- Integration featured in AppExchange
Value for us:
- Access to Salesforce's enterprise customer base
- Co-marketing (joint webinars, case studies, events)
- Increased product stickiness through integration
- 15% higher retention for integrated customers (based on similar partnerships)
Proposed model:
- Free bi-directional integration (mutual engineering investment: 400 hours each)
- Co-marketing budget: $200K (50/50 split)
- Referral agreement (no rev share, both companies refer customers to each other)
Timeline: 6 months (4 months engineering, 2 months co-marketing launch)

Create: Full proposal (8-10 pages), pitch deck outline (15 slides), and one-pager for initial outreach.
```

### 3. deal-structurer (Sonnet, Skill-Aware)
Designs partnership agreements with appropriate economic models, terms, and governance structures.

**Use for**: Deal structuring, contract negotiation strategy, economic model design, risk mitigation

**Example**:
```
Use deal-structurer for reseller partnership.
Partner: Global systems integrator (5000 employees, $2B revenue, enterprise focus)
Our company: Cloud infrastructure platform
Partnership goals:
- Partner resells our platform to their enterprise customers
- Partner provides implementation and managed services
- We provide platform, training, and technical support

Proposed structure:
- Economic model: 35% reseller margin (partner buys at 35% off list, sells at list)
- Minimum annual commitment: $2M in year 1, $5M in year 2
- Term: 3-year initial term with auto-renewal
- Exclusivity: Non-exclusive (both parties can work with other partners)
- Training: We provide free certification for 50 partner consultants
- Support: We provide 24/7 technical support for partner's customers

Concerns:
- Partner wants exclusivity in financial services vertical (we have other bank customers)
- Need clear IP ownership (partner builds custom solutions on our platform)
- Liability caps appropriate for enterprise deals ($10M+ contract values)
- Quarterly business reviews to ensure targets met

Create: Complete deal structure document with economic model, key terms, governance, risk mitigation, negotiation strategy (ideal/acceptable/walk-away positions).
```

### 4. relationship-manager (Sonnet, Skill-Aware)
Manages ongoing partnership relationships with performance tracking and continuous improvement.

**Use for**: Partnership performance tracking, QBRs, issue resolution, expansion planning, renewals

**Example**:
```
Use relationship-manager for Q3 QBR with AWS partnership.
Partnership context:
- Type: Technology partnership (certified AWS partner, ISV program)
- Start date: January 2024
- Economic model: AWS Marketplace co-sell (AWS takes 3% fee, we get marketplace exposure)
- Q3 targets: 75 AWS Marketplace customers, $1M Marketplace GMV, 3 co-marketing campaigns

Q3 Performance:
- AWS Marketplace customers: 92 (123% of target) ✅
- Marketplace GMV: $850K (85% of target) ⚠️
- Co-marketing campaigns: 3 completed (100% of target) ✅
  - AWS re:Invent sponsorship
  - Joint webinar (450 attendees, 80 MQLs)
  - Co-authored solution brief
- AWS co-sell pipeline: $3.2M (growing rapidly)
- Integration: AWS Well-Architected certified ✅

Issues:
- Marketplace GMV below target due to longer sales cycles for enterprise deals (45-60 days vs expected 30)
- AWS sales team awareness low (only 20% of reps aware of our partnership)

Wins:
- Featured in AWS Partner Success Stories
- 3 joint customer wins with AWS sales team ($800K total value)
- AWS technical validation completed (enables enterprise opportunities)

Next quarter plans:
- Launch AWS PrivateLink integration for enterprise security requirements
- AWS sales enablement session (train 100 AWS reps on our value prop)
- Submit for AWS ISV Accelerate program (faster co-sell payouts)

Create: Complete Q3 QBR document with KPI dashboard, wins, challenges, action plan, Q4 roadmap, and renewal planning (partnership renews in Q4).
```

## Skills

### partnership-strategy (23KB)
Comprehensive partnership management frameworks and best practices:

**Partner Identification and Qualification**:
- Partnership types (strategic alliance, channel, technology, co-marketing, referral, JV)
- Qualification framework (weighted scorecard: strategic fit 30%, market reach 25%, capabilities 20%, financial 15%, track record 10%)
- Partner tier system (Tier 1: 85-100%, Tier 2: 70-84%, Tier 3: 50-69%)

**Partnership Value Propositions**:
- Articulating mutual value (revenue opportunity, market access, product enhancement, brand association, operational efficiency)
- Value proposition formula framework

**Deal Structuring and Economics**:
- Revenue share models (percentage splits, tiered structures)
- Referral fees (flat or percentage, one-time payment)
- Reseller margin (20-40% typical)
- Co-marketing budget share (usually 50/50)
- Technology licensing
- Joint venture structures

**Contract Negotiation Strategies**:
- BATNA (Best Alternative To Negotiated Agreement)
- Anchoring, bundling, creating options, time pressure tactics
- Key contract terms (term/termination, exclusivity, IP, data/privacy, warranties, indemnification, liability caps, governance)

**Partnership Relationship Management**:
- Partnership lifecycle (launch, ramp-up, steady-state, renewal)
- Performance metrics (business, activity, relationship, ROI)
- Communication and governance (weekly working team, monthly steering, quarterly executive)
- Conflict resolution process
- Partnership expansion opportunities
- Exit planning and wind-down

**Best Practices**:
- Do's and don'ts
- Success factors
- Common partnership mistakes
- Partnership playbook framework

## Templates

### partnership-proposal-template.md
Complete partnership proposal structure with executive summary, value proposition, proposed model, success metrics, investment required, and next steps. Includes one-pager format for initial outreach.

### partnership-agreement-template.md
Business terms for partnership contract covering parties, scope, term/termination, roles/responsibilities, economic terms, exclusivity, IP, confidentiality, data/privacy, warranties, indemnification, liability, governance, and dispute resolution.

### partner-evaluation-scorecard.md
Weighted scorecard for partner qualification with 5 categories (strategic fit, market reach, capabilities, financial health, track record), tier classification, value proposition summary, and recommendation.

### partnership-playbook-template.md
Comprehensive lifecycle playbook covering strategy, identification, proposal, structuring, launch, ongoing management, expansion, and renewal/exit processes.

## Workflows

### Complete Partnership Lifecycle
```
1. Identify and qualify partners
Use partner-identifier to research potential partners with scoring

2. Create partnership proposal
Use proposal-writer to articulate value and structure deal

3. Negotiate and structure deal
Use deal-structurer to design economic model and contract terms

4. Launch and manage partnership
Use relationship-manager for performance tracking and optimization
```

### Channel Partner Recruitment
```
1. Define ideal partner profile (use partner-identifier)
Research target partners, score, and prioritize

2. Outreach with tailored proposal (use proposal-writer)
Customized value proposition for each Tier 1 partner

3. Structure reseller agreement (use deal-structurer)
Economic model, margin, training, support, targets

4. Onboard and enable (use relationship-manager)
Sales training, co-marketing plan, quick wins
```

### Technology Partnership
```
1. Research integration partners (use partner-identifier)
Find complementary platforms with customer overlap

2. Propose integration + co-marketing (use proposal-writer)
Value: better customer experience, increased stickiness, co-marketing reach

3. Define integration scope and go-to-market (use deal-structurer)
Free integration, mutual engineering investment, co-marketing budget, referral agreement

4. Launch integration and track adoption (use relationship-manager)
Marketplace listing, joint customer success stories, adoption metrics
```

### Partnership Renewal
```
1. Performance assessment (use relationship-manager)
60-90 days before expiration, comprehensive review vs. targets

2. Document value delivered (use relationship-manager)
ROI analysis, wins, case studies, partner satisfaction

3. Renewal proposal (use proposal-writer if expanding)
Continue as-is, expand scope, or modify terms based on learnings

4. Negotiate renewal (use deal-structurer if needed)
Updated economic model or scope, or plan exit if not delivering value
```

## Requirements Met

✅ **Role**: Strategic partnership specialist
✅ **Partner identification**: partner-identifier with WebSearch, qualification scoring, tier classification
✅ **Partnership proposals**: proposal-writer with value proposition frameworks, multiple formats (one-pager, full proposal, pitch deck)
✅ **Deal structuring**: deal-structurer with economic models (revenue share, referral, reseller, co-marketing), contract terms, negotiation strategy
✅ **Contract negotiation**: Negotiation tactics, objection handling, BATNA, concessions strategy
✅ **Relationship management**: relationship-manager with QBRs, performance tracking, issue resolution, expansion planning
✅ **Tools Required**:
  - ✅ Research capabilities: WebSearch for partner research
  - ✅ File operations: All agents have Read, Write for documentation
  - ✅ Relationship tracking: Performance dashboards, QBR templates

## Key Features

✓ **Complete Partnership Lifecycle**: From identification through renewal or exit
✓ **WebSearch Integration**: Real-time partner research and market intelligence
✓ **Weighted Qualification**: Objective partner scoring across 5 categories
✓ **Economic Model Library**: Revenue share, referral, reseller, co-marketing, licensing, JV
✓ **Negotiation Frameworks**: BATNA, anchoring, bundling, objection handling
✓ **Performance Tracking**: Business, activity, relationship, and ROI metrics
✓ **Governance Structure**: Weekly, monthly, quarterly communication cadence
✓ **Skill-Aware**: All agents read comprehensive partnership strategy skill
✓ **Professional Templates**: Proposals, contracts, scorecards, playbooks

## Partnership Types Supported

**Strategic Alliance**: Long-term collaboration for competitive advantage
- Joint product development
- Shared market expansion investment
- Deep multi-functional integration
- Example: Microsoft + Adobe

**Channel Partnership**: Distribution and reselling
- Partner sells your product to their customers
- Partner provides implementation and support
- Reseller margin economic model
- Example: AWS Partner Network

**Technology Integration**: API and platform partnerships
- Bi-directional product integration
- Marketplace listings
- Referral or free integration model
- Example: Salesforce AppExchange

**Co-Marketing**: Joint marketing and lead generation
- Shared content (webinars, whitepapers, events)
- Co-branded campaigns
- Shared budget and lead exchange
- Example: HubSpot + LinkedIn campaigns

**Referral Partnership**: Simple lead exchange
- Commission-based customer referrals
- Low integration, transactional
- Referral fee economic model
- Example: Real estate agents referring mortgage brokers

**Joint Venture**: Separate legal entity
- Shared equity and governance
- Significant investment and risk sharing
- For major market opportunities
- Example: Sony Ericsson (mobile phone JV)

## Economic Models

### Revenue Share
- **Structure**: Percentage split of revenue generated through partnership
- **Common splits**: 70/30, 75/25, 80/20 (generating party gets larger share)
- **When to use**: Revenue directly attributable, long-term value, ongoing roles
- **Example**: SaaS reseller gets 25% of recurring revenue for customers they sell and support

### Referral Fee
- **Structure**: Flat fee or 10-30% of initial sale value
- **One-time payment**: Upon customer sign-up or first payment
- **When to use**: Simple lead exchange, no ongoing involvement
- **Example**: $2000 per qualified customer referral

### Reseller Margin
- **Structure**: Partner buys at 20-40% discount, sells at (or near) list price
- **Partner keeps margin**: Compensation for sales, implementation, support
- **When to use**: Partner owns customer relationship
- **Example**: Partner buys at 35% off, sells at list, keeps 35%

### Co-Marketing Budget
- **Structure**: Shared investment in joint marketing (typically 50/50)
- **Shared leads**: Generated leads distributed per agreement
- **When to use**: Building awareness or demand together
- **Example**: $100K campaign, both contribute $50K, leads split 50/50

## Partnership Performance Metrics

### Business Impact
- Revenue generated (partnership-attributable)
- Customers acquired or retained
- Average deal size or LTV increase
- Market share or brand awareness lift

### Activity Metrics
- Leads generated and conversion rate
- Co-marketing campaigns executed
- Referrals exchanged (both directions)
- Integration usage/adoption rate
- Joint customers (using both products)

### Relationship Health
- Partner satisfaction score (quarterly survey, target: 8+/10)
- Stakeholder engagement (meeting attendance, responsiveness)
- Issue resolution time (target: <7 days for critical issues)
- Joint activity completion rate (target: 90%+)

### ROI Metrics
- Partnership ROI (value delivered vs. investment, target: 3:1+)
- Cost per customer acquired through partnership
- Revenue per partner
- Partnership profitability margin

## Governance and Communication

### Weekly (Working Team)
- **Duration**: 30 minutes
- **Format**: Slack/email or quick call
- **Attendees**: Project managers and operational leads
- **Agenda**: Active initiative updates, blockers, coordination

### Monthly (Steering Committee)
- **Duration**: 1 hour
- **Format**: Video call with slide deck
- **Attendees**: Senior managers (Director/VP level)
- **Agenda**: KPI review, wins, challenges, upcoming initiatives, decisions

### Quarterly (Executive Sponsors)
- **Duration**: 1-2 hours
- **Format**: In-person preferred, comprehensive QBR deck
- **Attendees**: VP or C-level from each company
- **Agenda**: Performance assessment, strategic decisions, renewal planning, expansion opportunities

## Negotiation Best Practices

### Preparation
1. **Define BATNA**: What's your alternative if deal doesn't happen?
2. **Set three positions**: Ideal (best case), Acceptable (walkaway), Walk-away (deal-breakers)
3. **Prioritize terms**: Must-have (non-negotiable), Important (flexible), Nice-to-have (tradable)
4. **Research partner**: Likely priorities, constraints, leverage, similar deals

### Tactics
- **Anchor**: Start with your position (don't ask "what do you think?")
- **Bundle**: Trade concessions together ("If you give X, we'll give Y and Z")
- **Create options**: Multiple acceptable deal structures
- **Time pressure**: Deadlines create urgency (but don't manufacture fake urgency)
- **Focus on interests**: "Why do you need that?" vs. positional haggling
- **Silence**: Don't fill pauses, let partner respond

### Common Objections

| Partner Objects To | Response Strategy |
|--------------------|-------------------|
| Revenue share too low | "Based on value contributed, analysis shows fair split is X. What's your calculation?" |
| Term too long | "We need X years to justify investment. Alternative: 1-year + auto-renewal if targets met?" |
| Exclusivity too broad | "We can offer exclusivity in [limited scope] for [duration]. Performance-based after that." |
| Liability cap too low | "Standard for partnerships this size is 1-2x annual value. Insurance requires adequate caps." |
| IP ownership unclear | "Pre-existing IP stays with creator. Jointly created is joint ownership with mutual licenses." |

## Warning Signs (Partnership at Risk)

🔴 **Critical Issues**:
- Declining performance for 2+ consecutive quarters
- Partner stakeholder turnover (loss of champion)
- Reduced responsiveness or cancelled meetings
- Partner pursuing competitive partnerships
- Negative customer feedback about partnership
- Misalignment on strategy or priorities

**Action**: Emergency steering committee meeting, executive escalation, develop remediation plan or prepare for exit.

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 1 comprehensive partnership-strategy skill (23KB, production-tested patterns)
- ✅ 4 professional templates (proposal, agreement, scorecard, playbook)
- ✅ Complete README with frameworks and workflows

## Design Philosophy

**Skill-Aware**: All agents read partnership-strategy skill for consistent, expert-level guidance
**Model Selection**: Sonnet for all agents (complex judgment, negotiation, relationship management)
**WebSearch Integration**: partner-identifier uses real-time research for current market intelligence
**Complete Lifecycle**: From initial partner identification through renewal or exit
**Mutual Value**: Emphasis on win-win partnerships (not one-sided deals)
**Data-Driven**: Objective scoring, performance metrics, ROI tracking
**Professional Templates**: Production-ready proposals, contracts, scorecards, playbooks

Closes #86
