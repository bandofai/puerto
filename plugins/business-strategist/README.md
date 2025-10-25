# Business Strategist Plugin

Corporate strategy development specialist for strategic planning, growth strategies, market entry analysis, M&A opportunities, and business model innovation.

## Overview

The Business Strategist plugin provides agents for comprehensive corporate strategy development using proven frameworks like Porter's Five Forces, SWOT, Ansoff Matrix, BCG Matrix, and business model canvas.

## Agents

### 1. strategic-planner (Sonnet, Skill-Aware, WebSearch)
Develops comprehensive strategic plans with vision, mission, strategic objectives, initiatives, and KPIs.

**Use for**: 3-5 year strategic plans, annual planning, strategic reviews, board presentations

**Example**:
```
Use strategic-planner to develop 3-year strategic plan for SaaS company.
Current state: $10M ARR, 50 employees, Series A funded
Vision: Become category leader in project management for remote teams
Include: SWOT analysis, strategic objectives, key initiatives, OKRs
Frameworks: Porter's Five Forces, VRIO analysis
```

### 2. growth-strategist (Sonnet, Skill-Aware, WebSearch)
Formulates growth strategies using Ansoff Matrix: market penetration, product development, market development, diversification.

**Use for**: Revenue growth planning, expansion strategies, new revenue streams, scaling plans

**Example**:
```
Use growth-strategist to identify growth opportunities for B2B fintech.
Current: $50M revenue, payment processing for SMBs in US
Goal: 3x revenue in 3 years
Evaluate: New markets (EU, LatAm), new products (lending, banking), new segments (enterprise)
Frameworks: Ansoff Matrix, TAM/SAM/SOM, unit economics
```

### 3. market-entry-analyst (Sonnet, Skill-Aware, WebSearch)
Analyzes market entry opportunities: market assessment, competitive landscape, entry strategy, go-to-market plan.

**Use for**: Geographic expansion, new market segments, international entry, product launches

**Example**:
```
Use market-entry-analyst to evaluate entering European market.
Product: HR software for mid-market companies
Target markets: UK, Germany, France
Analysis: Market size, competition, regulatory requirements, localization
Strategy: Entry mode (subsidiary vs partnership), timing, investment required
```

### 4. ma-analyst (Sonnet, Skill-Aware, WebSearch)
Assesses M&A opportunities: strategic fit, synergies, valuation ranges, integration risks.

**Use for**: Acquisition targets, merger evaluation, strategic partnerships, acquihire opportunities

**Example**:
```
Use ma-analyst to evaluate acquisition target.
Acquirer: E-commerce platform ($200M revenue)
Target: Customer data analytics startup ($10M revenue, $3M EBITDA)
Strategic rationale: Add analytics capabilities, cross-sell to customer base
Analyze: Strategic fit, financial synergies, integration complexity, valuation (3-5x revenue multiple)
```

## Skills

### strategic-planning
Comprehensive strategic planning frameworks: Porter's Five Forces, SWOT, PESTEL, VRIO, BCG Matrix, Ansoff Matrix, business model canvas, balanced scorecard, OKR methodology, competitive positioning.

## Templates

### strategic-plan-template.md
Complete strategic plan structure: Executive summary, situation analysis, vision/mission, strategic objectives, key initiatives, financial projections, implementation roadmap, KPIs.

### market-entry-analysis-template.md
Market entry evaluation framework: Market assessment, competitive analysis, regulatory landscape, entry mode selection, go-to-market plan, investment requirements, risk assessment.

### ma-evaluation-template.md
M&A analysis template: Strategic rationale, target profile, financial analysis, synergy identification, valuation analysis, integration plan, risk assessment, deal structure recommendations.

## Workflows

### Complete Strategic Planning
```
1. Situation analysis
Use strategic-planner to conduct SWOT and Porter's Five Forces analysis

2. Growth strategy
Use growth-strategist to identify opportunities via Ansoff Matrix

3. Market entry
Use market-entry-analyst to evaluate new market opportunities

4. Inorganic growth
Use ma-analyst to identify and evaluate acquisition targets
```

### Annual Strategic Review
```
Use strategic-planner for annual strategy review:
- Review last year's performance vs strategic objectives
- Update SWOT analysis with current state
- Refine strategic priorities for coming year
- Set OKRs aligned with 3-year plan
- Identify resource allocation and budget needs
```

## Requirements Met

✅ Role: Corporate strategy development specialist
✅ Strategic plan development: strategic-planner with comprehensive frameworks
✅ Growth strategy formulation: growth-strategist with Ansoff Matrix and TAM/SAM/SOM
✅ Market entry analysis: market-entry-analyst with competitive landscape and regulatory assessment
✅ M&A opportunity assessment: ma-analyst with strategic fit and valuation analysis
✅ Business model innovation: Covered in strategic-planning skill
✅ Tools: Analysis frameworks (skills), research (WebSearch), financial modeling, file operations

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 1 comprehensive strategic-planning skill
- ✅ 3 professional templates for strategic planning, market entry, and M&A
- ✅ Complete README with workflows

Closes #66
