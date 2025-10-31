# Business Strategist Plugin

**Comprehensive strategic planning, competitive analysis, growth strategy, and M&A evaluation**

Corporate strategy development specialist for strategic planning, growth strategies, market entry analysis, M&A opportunities, and business model innovation using battle-tested frameworks.

## Overview

The Business Strategist plugin provides expert-level strategic planning capabilities using proven frameworks like Porter's Five Forces, SWOT Analysis, BCG Matrix, Ansoff Matrix, Blue Ocean Strategy, and OKR methodology. It includes a comprehensive strategic planning skill and four specialized agents for different aspects of business strategy.

## Components

### Skill: Strategic Planning

**Location**: `skills/strategic-planning/SKILL.md`

Comprehensive strategic planning frameworks and methodologies including:

- **Strategic Analysis Frameworks**: Porter's Five Forces, SWOT Analysis, PESTEL, VRIO, BCG Matrix, Ansoff Matrix
- **Vision & Mission Development**: Vision statements, mission statements, core values definition
- **Goal-Setting Frameworks**: OKR (Objectives & Key Results), KPI frameworks, balanced scorecard
- **Market Entry Strategies**: Entry mode selection, market attractiveness assessment, risk evaluation
- **M&A Evaluation**: Target evaluation, valuation methods (comparables, DCF, precedent transactions), due diligence frameworks, synergy analysis
- **Business Model Innovation**: Business Model Canvas, competitive positioning, Blue Ocean Strategy
- **Strategic Planning**: Scenario planning, strategic roadmapping (3-horizon model), change management (Kotter's 8 steps)

## Agents

### 1. Strategic Planner (Sonnet)
**File**: `agents/strategic-planner.md`
**Tools**: Read, Write, Edit, Bash

Develops comprehensive strategic plans with vision, mission, strategic objectives, OKRs, and 3-5 year roadmaps.

**Use for**:
- 3-5 year strategic plans
- Annual strategic planning
- Vision/mission/values development
- OKR framework implementation
- Strategic reviews and board presentations

**Key Capabilities**:
- Porter's Five Forces industry analysis
- SWOT analysis with strategic implications
- Vision, mission, and values development
- OKR framework with quarterly breakdown
- Strategic roadmap (Horizon 1, 2, 3)
- Risk assessment and mitigation strategies
- Implementation governance structure

**Example**:
```
@strategic-planner Develop a 3-year strategic plan for our SaaS company.
Current state: $10M ARR, 50 employees, Series A funded ($15M raised)
Vision: Become category leader in project management for remote teams
Market: HR tech, mid-market companies (100-500 employees)
Include: SWOT analysis, strategic objectives, key initiatives, OKRs
Frameworks: Porter's Five Forces, competitive positioning
```

**Outputs**:
- `strategy/strategic-plan.md` - Complete strategic plan
- `strategy/vision-mission-values.md` - V/M/V statements
- `strategy/okrs.md` - Objectives and key results
- `strategy/strategic-roadmap.md` - 3-5 year timeline
- `strategy/competitive-analysis.md` - Market analysis
- `strategy/implementation-plan.md` - Execution details

---

### 2. Growth Strategist (Sonnet)
**File**: `agents/growth-strategist.md`
**Tools**: Read, Write, Bash, WebSearch

Formulates growth strategies using Ansoff Matrix: market penetration, product development, market development, diversification.

**Use for**:
- Revenue growth planning
- Market expansion strategies
- Customer acquisition optimization
- Unit economics modeling
- Scaling plans

**Key Capabilities**:
- Ansoff Matrix analysis (all 4 growth vectors)
- Market opportunity sizing (TAM/SAM/SOM)
- Unit economics modeling (CAC, LTV, payback period)
- Revenue projections (base, target, stretch scenarios)
- Customer acquisition channel strategy
- Conversion funnel optimization
- Geographic expansion prioritization

**Example**:
```
@growth-strategist Design a growth strategy to 3x revenue in 3 years.
Current: $50M revenue, B2B fintech, payment processing for SMBs in US
Metrics: 10K customers, $5K ACV, 85% retention, $500 CAC
Goal: $150M revenue by 2027
Evaluate: New markets (EU, LatAm), new products (lending, banking), new segments (enterprise)
Frameworks: Ansoff Matrix, TAM/SAM/SOM, unit economics
```

**Outputs**:
- `growth/growth-strategy.md` - Overall growth strategy
- `growth/market-analysis.md` - Market opportunity assessment
- `growth/revenue-model.md` - Financial projections
- `growth/customer-acquisition.md` - CAC strategy
- `growth/expansion-plan.md` - Market expansion roadmap

---

### 3. Market Entry Analyst (Sonnet)
**File**: `agents/market-entry-analyst.md`
**Tools**: Read, Write, Bash, WebSearch

Analyzes market entry opportunities: market assessment, competitive landscape, entry strategy, go-to-market plan.

**Use for**:
- Geographic expansion (international markets)
- New market segments
- Product launches in new markets
- Entry mode selection (export, JV, acquisition)
- Market risk assessment

**Key Capabilities**:
- Market attractiveness scoring (6-factor framework)
- Entry barrier analysis (regulatory, capital, knowledge, competitive)
- Entry mode evaluation (export, licensing, JV, wholly-owned subsidiary)
- Risk assessment (political, economic, market, operational, legal)
- Implementation roadmap (preparation, soft launch, scale, optimization)
- Go/No-Go recommendation framework
- WebSearch for market intelligence

**Example**:
```
@market-entry-analyst Evaluate entering European market.
Product: HR software for mid-market companies (100-500 employees)
Target markets: UK, Germany, France
Budget: $1M for market entry
Analysis needed:
- Market size and growth in each country
- Competitive landscape and key players
- Regulatory requirements (GDPR, data residency)
- Localization needs (language, features, support)
Entry strategy: Recommend entry mode (subsidiary vs partnership), timing, investment
```

**Outputs**:
- `market-entry/market-analysis-[country].md` - Attractiveness assessment
- `market-entry/entry-mode-analysis.md` - Mode evaluation
- `market-entry/entry-strategy.md` - Recommended strategy
- `market-entry/risk-assessment.md` - Risks and mitigation
- `market-entry/implementation-plan.md` - Execution roadmap

---

### 4. M&A Analyst (Sonnet)
**File**: `agents/ma-analyst.md`
**Tools**: Read, Write, Edit, Bash

Assesses M&A opportunities: strategic fit, synergies, valuation ranges, integration risks.

**Use for**:
- Acquisition target evaluation
- Merger analysis
- Strategic fit assessment
- Valuation (comparables, DCF, precedent transactions)
- Due diligence planning
- Synergy analysis
- Post-merger integration planning

**Key Capabilities**:
- Strategic fit assessment (market, operational, cultural, financial)
- Target company evaluation (financials, market position, management, technology)
- Multi-method valuation (trading multiples, precedent transactions, DCF, sum-of-parts)
- Comprehensive due diligence framework (financial, legal, operational, commercial)
- Synergy analysis (revenue, cost, financial synergies with risk adjustment)
- Integration planning (Day 1, 30-day, 90-day, 6-month, 1-year roadmap)
- Deal-breaker identification

**Example**:
```
@ma-analyst Evaluate acquisition target.
Acquirer: E-commerce platform ($200M revenue, $50M EBITDA)
Target: Customer data analytics startup
  - Revenue: $10M (growing 40% YoY)
  - EBITDA: $3M (30% margin)
  - Customers: 200 (mid-market retailers)
  - Employees: 75 (strong engineering team)
  - Asking price: $50M
Strategic rationale:
  - Add analytics capabilities (build vs buy analysis)
  - Cross-sell to our 5,000 customers
  - Enter predictive analytics market
Analyze: Strategic fit, valuation (is $50M fair?), synergies, integration complexity
```

**Outputs**:
- `ma/strategic-rationale.md` - Why acquire, strategic fit
- `ma/target-evaluation.md` - Target assessment
- `ma/valuation-analysis.md` - Valuation models
- `ma/due-diligence-checklist.md` - DD framework
- `ma/synergy-analysis.md` - Synergies and value creation
- `ma/integration-plan.md` - Post-merger integration
- `ma/deal-recommendation.md` - Final recommendation

## Strategic Frameworks Reference

### Porter's Five Forces
Assess industry structure and competitive dynamics:
1. **Threat of New Entrants**: Barriers to entry (capital, scale, brand, regulations)
2. **Bargaining Power of Suppliers**: Supplier concentration, switching costs
3. **Bargaining Power of Buyers**: Buyer concentration, price sensitivity
4. **Threat of Substitutes**: Alternative solutions, switching ease
5. **Competitive Rivalry**: Number of competitors, industry growth, differentiation

### SWOT Analysis
Internal and external factor analysis:
- **Strengths** (Internal, Positive): What we do well, unique resources, competitive advantages
- **Weaknesses** (Internal, Negative): What to improve, resource gaps, disadvantages
- **Opportunities** (External, Positive): Market trends, gaps, technology changes
- **Threats** (External, Negative): Obstacles, competitor actions, regulatory changes

### BCG Matrix (Growth-Share Matrix)
Portfolio analysis for resource allocation:
- **Stars** (High Growth, High Share): Invest heavily, future cash cows
- **Cash Cows** (Low Growth, High Share): Harvest, fund other ventures
- **Question Marks** (High Growth, Low Share): Invest selectively or divest
- **Dogs** (Low Growth, Low Share): Divest or reposition

### Ansoff Matrix
Four growth strategies by risk level:
1. **Market Penetration** (Existing Products → Existing Markets): Low risk, increase market share
2. **Market Development** (Existing Products → New Markets): Medium risk, new geographies/segments
3. **Product Development** (New Products → Existing Markets): Medium risk, innovation for current customers
4. **Diversification** (New Products → New Markets): High risk, enter new business

### Blue Ocean Strategy
Create uncontested market space using Four Actions Framework:
- **Eliminate**: What factors can be eliminated that industry takes for granted?
- **Reduce**: What factors can be reduced well below industry standard?
- **Raise**: What factors should be raised well above industry standard?
- **Create**: What factors should be created that industry never offered?

### OKRs (Objectives and Key Results)
Goal-setting framework:
- **Objective**: Qualitative, inspirational goal (what we want to achieve)
- **Key Results**: Quantitative, measurable outcomes (how we know we achieved it)
- Set at company, team, and individual levels
- Quarterly cycles with 60-70% confidence in achieving
- Scoring: 0.0-0.3 (failed), 0.4-0.6 (made progress), 0.7-1.0 (delivered)

## Workflows

### Complete Strategic Planning
```
1. Situation analysis
   @strategic-planner Conduct SWOT and Porter's Five Forces analysis

2. Growth strategy
   @growth-strategist Identify opportunities via Ansoff Matrix

3. Market entry (if applicable)
   @market-entry-analyst Evaluate new market opportunities

4. Inorganic growth (if applicable)
   @ma-analyst Identify and evaluate acquisition targets

5. Consolidate into comprehensive plan
   @strategic-planner Develop final 3-year strategic plan with OKRs
```

### Annual Strategic Review
```
@strategic-planner Conduct annual strategy review:
- Review last year's performance vs strategic objectives
- Update SWOT analysis with current state
- Refine strategic priorities for coming year
- Set OKRs aligned with 3-year plan
- Identify resource allocation and budget needs
```

### Growth Initiative Planning
```
1. @growth-strategist Analyze growth opportunities
2. @market-entry-analyst Evaluate specific market entry (if expansion)
3. @strategic-planner Integrate into overall strategy
4. Execute and track with OKRs
```

### M&A Transaction Process
```
1. @ma-analyst Initial target screening and strategic fit
2. @ma-analyst Full valuation analysis (if interested)
3. @ma-analyst Due diligence framework
4. @ma-analyst Synergy analysis and integration planning
5. @strategic-planner Integrate acquired company into strategy
6. @growth-strategist Model combined entity growth
```

## Installation

```bash
# Copy to your plugins directory
cp -r plugins/business-strategist ~/.claude/plugins/business-strategist

# Verify installation
ls ~/.claude/plugins/business-strategist/agents/
ls ~/.claude/plugins/business-strategist/skills/strategic-planning/
```

## Best Practices

### Strategic Planning
- Start with thorough analysis (use frameworks systematically)
- Be specific with numbers, timelines, and metrics
- Make clear strategic choices (what NOT to do is as important)
- Balance ambition with realism
- Build in flexibility for market changes
- Create measurable success criteria (OKRs, KPIs)
- Align resources with strategic priorities
- Communicate vision simply and memorably

### Growth Strategy
- Size the market opportunity rigorously (TAM/SAM/SOM)
- Validate unit economics (LTV:CAC ratio >3:1, payback <12 months)
- Model multiple scenarios (base, target, stretch)
- Diversify customer acquisition channels
- Optimize full funnel (awareness → conversion)
- Plan phased expansion (pilot → scale)
- Track leading indicators, not just lagging
- Maintain capital efficiency

### Market Entry
- Assess market attractiveness systematically (score all factors)
- Understand entry barriers upfront (regulatory, competitive, cultural)
- Choose entry mode based on resources and risk tolerance
- Plan phased approach (pilot in one city/region before full launch)
- Build local partnerships (navigate culture, regulations)
- Adapt to cultural differences (product, marketing, operations)
- Have clear go/no-go criteria defined in advance
- Define exit strategy before entering

### M&A
- Start with strategic rationale (not opportunistic deals)
- Use multiple valuation methods (triangulate fair value)
- Conduct thorough due diligence (financial, legal, operational, commercial)
- Be realistic about synergies (risk-adjust assumptions)
- Define walk-away price before negotiating
- Plan integration from day 1 (culture, systems, processes)
- Focus on culture and talent retention
- Track synergy realization rigorously (don't assume they happen)

## Key Metrics

### Strategic Planning
- Strategic fit score (/10)
- OKR achievement rate (target >70%)
- Strategic initiative on-time completion
- Stakeholder alignment score

### Growth
- Revenue growth rate (MoM, YoY)
- CAC (Customer Acquisition Cost)
- LTV (Lifetime Value)
- LTV:CAC ratio (target >3:1)
- CAC payback period (target <12 months)
- MRR/ARR growth
- NRR (Net Revenue Retention, target >120%)

### Market Entry
- Market attractiveness score (/10)
- Time to first customer
- Local market share achievement
- Customer acquisition cost vs. home market
- ROI (3-year)

### M&A
- Strategic fit score (/10)
- Deal multiples (EV/Revenue, EV/EBITDA)
- Synergy realization (% of target)
- Post-merger customer retention
- Post-merger employee retention
- Time to integration completion

## Requirements Met

✅ Role: Corporate strategy development specialist
✅ Strategic plan development: strategic-planner with comprehensive frameworks
✅ Growth strategy formulation: growth-strategist with Ansoff Matrix and TAM/SAM/SOM
✅ Market entry analysis: market-entry-analyst with competitive landscape and regulatory assessment
✅ M&A opportunity assessment: ma-analyst with strategic fit and valuation analysis
✅ Business model innovation: Covered in strategic-planning skill with Business Model Canvas and Blue Ocean Strategy
✅ Tools: Analysis frameworks (skills), research (WebSearch), financial modeling, file operations

## Version

**Version**: 1.0.0
**Last Updated**: 2025-01-28
**Compatibility**: Claude Code (Sonnet model)

## Support

For issues, questions, or contributions, refer to the Puerto Plugin Marketplace documentation.

---

**Transform your business strategy with AI-powered strategic planning, growth modeling, market entry analysis, and M&A evaluation using battle-tested frameworks.**
