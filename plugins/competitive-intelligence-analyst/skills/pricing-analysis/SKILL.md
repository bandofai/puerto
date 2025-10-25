# Pricing Analysis Skill

**Expert patterns for competitive pricing intelligence and strategic pricing recommendations**

## Overview

Pricing analysis examines how competitors price products, structures tiers, and positions themselves in the market to inform pricing strategy and competitive positioning.

---

## Pricing Model Types

### Model 1: Per-User (Seat-Based)

**Structure**: $X per user per month

**Characteristics**:
- Predictable revenue scaling
- Clear unit economics
- Easy to understand
- Common in SaaS (Slack, Salesforce)

**Variants**:
- Flat per-user: $10/user regardless of volume
- Tiered per-user: $15/user (1-10), $12/user (11-50), $10/user (51+)
- Active users only vs. all provisioned users

**Analysis Questions**:
- Is there a minimum user count?
- Do inactive users count?
- Are admin/view-only users charged?
- What's the volume discount structure?

### Model 2: Usage-Based (Consumption)

**Structure**: $X per [unit of consumption]

**Units**:
- API calls (Stripe, Twilio)
- GB storage/transfer (AWS S3)
- Compute hours (cloud hosting)
- Transactions processed
- Messages sent

**Characteristics**:
- Revenue scales with customer value
- Unpredictable for customers
- Can drive very high LTV
- Risk of "bill shock"

**Analysis Questions**:
- What's the unit of measurement?
- Are there committed tiers or pure PAYG?
- What are overage rates?
- Are there free allowances?

### Model 3: Tiered/Feature-Gated

**Structure**: Fixed price per tier, features differ

**Example**:
- **Free**: $0/mo - Basic features
- **Pro**: $29/mo - Add advanced features
- **Business**: $99/mo - Add team features
- **Enterprise**: Custom - Add enterprise features

**Characteristics**:
- Clear differentiation
- Upsell path obvious
- Value-based segmentation

**Analysis Questions**:
- How many tiers?
- What differentiates each tier?
- Where is "good-better-best" positioned?
- Is Enterprise always custom pricing?

### Model 4: Freemium

**Structure**: Free tier + paid upgrades

**Free tier limitations**:
- Usage limits (100 API calls/mo)
- Feature restrictions (no advanced features)
- User limits (1-2 users)
- Data retention (30 days)
- Support (community only)

**Conversion triggers**:
- Hit usage limit
- Need premium feature
- Team growth
- Require support/SLA

**Analysis Questions**:
- How generous is free tier?
- What % of users convert? (if known)
- Is free tier loss leader or customer acquisition?
- Can you build real business on free?

### Model 5: Flat-Rate

**Structure**: One price for unlimited/all-inclusive

**Example**: $99/mo unlimited everything

**Characteristics**:
- Simple messaging
- Predictable for customer
- Hard to segment willingness-to-pay
- Risk of "all you can eat" abuse

**Less common** in SaaS, more in B2C

### Model 6: Hybrid/Modular

**Structure**: Combination of models

**Example**:
- Base: $50/mo (platform access)
- Plus: $5/user/mo (additional users)
- Plus: $0.01/API call (usage)

**Characteristics**:
- Captures value multiple ways
- Complex to explain
- Aligns revenue with value delivery

**Analysis Questions**:
- What's the minimum all-in price?
- How do components interact?
- Where's the "gotcha" that drives up price?

---

## Pricing Tier Analysis Framework

### Framework 1: Good-Better-Best

Most effective: 3-4 tiers with clear value ladder

**Tier Design Principles**:

**Tier 1: Entry/Starter**
- **Goal**: Low barrier, get users in door
- **Price**: Lowest or Free
- **Features**: Core value prop, limited scale
- **Target**: Individuals, small teams, trial users

**Tier 2: Professional/Plus** (ANCHOR)
- **Goal**: Where most customers land
- **Price**: 2-3x Tier 1
- **Features**: Adds most-wanted features
- **Target**: Power users, small businesses
- **Note**: Often best margin tier

**Tier 3: Business/Premium**
- **Goal**: Team/company tier
- **Price**: 3-5x Tier 1
- **Features**: Team collaboration, admin
- **Target**: Growing companies, departments

**Tier 4: Enterprise**
- **Goal**: Large organizations, custom deals
- **Price**: Custom (often 10x+ Tier 1)
- **Features**: Enterprise-only (SSO, SLA, CSM)
- **Target**: Large enterprises, regulated industries

### Framework 2: Feature Gating Strategy

**Which features go in which tier?**

**Free/Starter Tier**:
- ✅ Core product functionality (essential for value)
- ✅ Key differentiators (so users see value)
- ❌ Scale/advanced features
- ❌ Team features
- ❌ Enterprise features

**Mid Tiers**:
- ✅ Features most customers want (80% use cases)
- ✅ Productivity boosters
- ✅ Integrations
- ⚠️ Some advanced features (save best for top tier)

**Top Paid Tier**:
- ✅ Advanced/power features
- ✅ Team collaboration
- ✅ Higher limits
- ❌ Enterprise-specific (save for Enterprise tier)

**Enterprise Tier**:
- ✅ SSO/SAML
- ✅ Advanced security/compliance
- ✅ SLA/support commitments
- ✅ Custom integrations
- ✅ Dedicated resources (CSM, support)

### Framework 3: Upgrade Incentives

**What triggers users to upgrade?**

**Approach 1: Usage Limits**
- Free: 100 widgets/mo → Pro: 1,000 widgets/mo
- Trigger: Hit limit → Soft upgrade prompt

**Approach 2: Feature Paywalls**
- Free: Try premium feature (limited) → See value → Paywall
- Trigger: Need feature → Hard upgrade requirement

**Approach 3: Team Growth**
- Free: 1 user → Pro: 5 users → Business: Unlimited
- Trigger: Add teammates → Upgrade required

**Approach 4: Support/SLA**
- Free: Community support → Pro: Email support → Enterprise: Phone/dedicated
- Trigger: Need help → Upgrade for better support

**Best Practice**: Multiple upgrade triggers (usage + features + team)

---

## Price Positioning Analysis

### Position 1: Premium Pricing

**Strategy**: Highest price in market

**Justification**:
- Superior quality/features
- Better support/service
- Brand/reputation premium
- Target: enterprises willing to pay more

**Examples**: Salesforce, Marketo

**Analysis**:
If competitor uses premium pricing:
- What justifies the premium?
- Do customers pay it? (win rate, retention)
- Is premium sustainable or eroding?

### Position 2: Mid-Market/Parity Pricing

**Strategy**: Priced similarly to competitors

**Justification**:
- Similar value proposition
- Avoid price as decision factor
- Compete on other dimensions (features, UX, support)

**Examples**: Most competitive markets

### Position 3: Value/Discount Pricing

**Strategy**: Undercut competitors on price

**Justification**:
- Lower cost structure
- Market share grab
- Serve price-sensitive segment
- Newer entrant

**Examples**: Disruptors, challengers

**Risk**: "Cheap = low quality" perception

### Position 4: Freemium/Land & Expand

**Strategy**: Free tier + aggressive monetization

**Justification**:
- Network effects
- Viral growth
- High conversion value
- Usage monetization

**Examples**: Slack, Zoom, Dropbox

---

## Pricing Intelligence Gathering

### Source 1: Pricing Pages

**What to capture**:
- All tiers and prices
- Features per tier
- Add-ons and extras
- Discounts (annual, volume)
- Free trial terms

**Pro tip**: Check via:
- Main .com domain
- Regional sites (.co.uk, .de) for geo pricing
- Logged-out vs. logged-in (personalized pricing)

### Source 2: Sales Calls/Demos

**If possible** (ethically):
- Request demo as legitimate prospect
- Ask about pricing during demo
- Inquire about discounts
- Understand negotiation flexibility

**Ethical**: Use real info, don't misrepresent

### Source 3: Customer References

**Sources**:
- Customer case studies (sometimes reveal pricing)
- RFP responses (if publicly available)
- Contract leaks (use cautiously)
- Customer interviews (if willing to share)

### Source 4: Third-Party Data

**Sources**:
- Review sites (G2, Capterra) - users sometimes mention pricing
- Reddit, forums - complaints about price increases
- News articles - pricing announcements
- Analyst reports - pricing comparisons

### Source 5: Historical Tracking

**Track over time**:
- Price changes (increases/decreases)
- New tiers introduced
- Features moved between tiers
- Free tier restrictions

**Insight**: Pricing evolution reveals strategy shifts

Example:
```
2023 Q1: 3 tiers, entry at $19/mo
2023 Q4: Added Enterprise tier, entry still $19/mo
2024 Q2: Entry moved to $29/mo (+50% increase)
2024 Q4: Freemium tier introduced

Analysis: Moved upmarket (enterprise tier), then added free to maintain top-of-funnel
```

---

## Competitive Price Comparison Techniques

### Technique 1: Apples-to-Apples Tier Matching

**Challenge**: Tiers don't align perfectly

**Approach**: Match on *value*, not name

Example:
```
Our "Pro" tier ($50/mo, 10 users, Feature Set A)

Best match:
- Comp A "Business" ($60/mo, 15 users, similar features) ← Most comparable
- Comp B "Pro" ($40/mo, 5 users, fewer features) ← Not comparable (less value)
```

### Technique 2: Total Cost of Ownership (TCO)

**Don't just compare list prices**

Consider:
- Setup/onboarding fees
- Training costs
- Integration costs
- Support tier costs
- Add-on costs
- Annual vs. monthly price difference

Example:
```
Us: $100/mo × 12 = $1,200/yr

Comp A: $80/mo × 12 = $960/yr
  + $500 onboarding
  + $300/yr premium support
  = $1,760/yr ← More expensive!
```

### Technique 3: Price-Per-Feature Ratio

**Calculate value density**:

```
Formula: Price ÷ Number of Features = Price per Feature

Us: $99/mo, 45 features = $2.20/feature
Comp A: $129/mo, 60 features = $2.15/feature ← Better value
Comp B: $79/mo, 30 features = $2.63/feature ← Worse value
```

**Caveat**: Assumes all features equally valuable (rarely true)

**Better**: Weight by feature importance

### Technique 4: Price Elasticity Estimation

**If you have data on competitor behavior**:

```
When Comp A dropped price from $100 → $80:
- Customer growth: +25%
- Churn reduction: -15%

Interpretation: Customers are price-sensitive in this segment
```

### Technique 5: Willingness-to-Pay Analysis

**From customer research/surveys**:

```
What would you pay for [product]?

Responses:
- $50/mo: 80% would pay
- $100/mo: 50% would pay ← Optimal price point
- $150/mo: 20% would pay
- $200/mo: 5% would pay

Competitor prices:
- Comp A: $75 (priced below WTP)
- Comp B: $125 (priced above median WTP)

Opportunity: Price at $100-110 (captures WTP, above Comp A)
```

---

## Pricing Recommendations Framework

### Recommendation Type 1: Price Increase

**When to recommend**:
- Our price significantly below market (leaving money on table)
- Our value demonstrably higher than competitors
- Costs have increased
- Market matured (less price sensitivity)

**How much**: 10-20% increases are typically tolerated

**Execution**:
- Grandfather existing customers (optional)
- Communicate value justification
- Announce with advance notice (30-90 days)

### Recommendation Type 2: Price Decrease

**When to recommend**:
- Losing deals primarily on price
- Competitor drastically undercut us
- Need market share over margin
- Cost structure improved

**Risk**: Hard to raise later, "cheap" perception

### Recommendation Type 3: New Tier Introduction

**When to recommend**:
- Gap in tier structure
- Missing segment (Enterprise tier for Fortune 500)
- Too many customers on Free (introduce low-paid tier)

**Example**:
```
Current: Free → Pro ($99)
Issue: Huge jump, low conversion

Add: Starter ($29)
Result: Smoother upgrade path, capture more users
```

### Recommendation Type 4: Feature Repackaging

**When to recommend**:
- Premium features undervalued in current tier
- Can create upsell by moving features

**Example**:
```
Current: API access in Pro tier ($99)
Change: Move API access to Business tier ($199)
Result: Power users forced to upgrade (+$100/mo)
```

**Risk**: Anger existing customers (grandfather them)

### Recommendation Type 5: Pricing Model Shift

**When to recommend**:
- Current model doesn't capture value
- Competitive model more aligned

**Example**:
```
Current: Per-user pricing ($10/user)
Issue: Usage varies wildly per user

Change to: Usage-based ($0.01/API call)
Result: Heavy users pay more, light users pay less
```

---

## Pricing Psychology Tactics

### Tactic 1: Charm Pricing

$99 instead of $100

**Effect**: Perceived significantly lower (left-digit effect)

**Data**: Can increase conversion by 5-10%

### Tactic 2: Anchoring

Show expensive tier first, makes mid-tier seem reasonable

Example:
```
Enterprise: $999/mo
↓
Pro: $199/mo ← Seems like a deal!
```

### Tactic 3: Decoy Pricing

Introduce tier designed to make another tier attractive:

```
Basic: $49/mo (limited features)
Pro: $99/mo (good features) ← BEST VALUE
Premium: $149/mo (few extra features) ← Decoy (makes Pro look good)
```

Most people choose Pro (middle option with best value)

### Tactic 4: Annual Discount

"Save 20% with annual billing"

**Effect**:
- Upfront cash flow
- Lower churn (committed for year)
- Customer lifetime value boost

**Standard discount**: 15-20% for annual

### Tactic 5: Social Proof

"Most popular" or "Best value" badges

**Effect**: Guides customers to desired tier

---

## Red Flags in Competitor Pricing

**Flag 1: Frequent price changes**
- Indicates instability, uncertainty
- May be testing, may be desperate

**Flag 2: Aggressive discounting**
- May signal low conversion/retention
- Could indicate cash flow issues

**Flag 3: "Contact for pricing" on mid-tiers**
- Often hiding high prices
- Friction in sales process

**Flag 4: Complex pricing structure**
- Indicates trying to capture value but confuses customers
- Opportunity for simpler alternative

**Flag 5: Very low prices**
- May be unsustainable (burning VC money)
- Quality concerns

---

## Summary Checklist

For pricing analysis:

- [ ] All competitor pricing pages captured
- [ ] All tiers and features documented
- [ ] Pricing model identified for each competitor
- [ ] Apples-to-apples comparison (same value tier)
- [ ] TCO calculated (not just list price)
- [ ] Price positioning assessed (premium/parity/value)
- [ ] Historical pricing changes tracked
- [ ] Upgrade triggers identified
- [ ] Psychological pricing tactics noted
- [ ] Recommendations are specific and justified
- [ ] Risk/benefit of changes considered

**Remember**: Pricing is strategy, not just tactics. Consider positioning, customer perception, and long-term sustainability, not just revenue maximization.
