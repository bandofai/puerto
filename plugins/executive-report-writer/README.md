# Executive Report Writer Plugin

Executive reporting specialist for creating board reports, executive summaries, high-level metric reporting, strategic insight synthesis, and executive-friendly visualizations.

## Overview

The Executive Report Writer plugin provides agents for effective executive communication using proven frameworks: pyramid principle, executive summary structure, data storytelling, and strategic narrative.

## Agents

### 1. executive-summarizer (Sonnet, Skill-Aware)
Creates concise executive summaries using pyramid principle: conclusion first, supporting details after.

**Use for**: Executive summaries, one-pagers, memo writing, decision documents

**Example**:
```
Use executive-summarizer for Q4 business review.
Content to summarize:
- Revenue: $12M (+20% YoY, -5% vs plan)
- New customers: 450 (+15% YoY)
- Churn: 6% (target: 5%, concerning trend)
- Product launches: 3 major features shipped
- Market: Increased competition from Competitor X

Executive summary (1 page):
## Q4 2023 Summary

Bottom line: Strong growth (+20% YoY) but missed revenue target by 5% due to higher churn.

Key highlights:
• Revenue: $12M (+20% YoY, -5% vs $12.6M plan)
• Customer growth: +15% YoY (450 new customers)
• Churn elevated: 6% vs 5% target (action plan in progress)

Recommendation: Prioritize retention initiatives in Q1 to reduce churn to 5%.
```

### 2. board-report-writer (Sonnet, Skill-Aware)
Writes board meeting materials with strategic focus, financial metrics, and governance updates.

**Use for**: Board decks, board memos, quarterly reviews, strategic updates

**Example**:
```
Use board-report-writer for quarterly board meeting.
Agenda:
1. Business update (10 min)
2. Financial review (10 min)
3. Strategic initiatives (15 min)
4. Discussion: Fundraising timing (20 min)

Board deck structure (15-20 slides):
1. Cover + agenda
2. Executive summary (1 slide: highlights, concerns, asks)
3. Business metrics (KPIs: ARR, customers, churn, NRR)
4. Financial summary (P&L, burn rate, runway)
5. Product roadmap (shipped, in progress, planned)
6. Strategic initiatives (3 key initiatives + progress)
7. Team update (headcount, key hires, org changes)
8. Fundraising discussion (market timing, terms, timeline)
9. Appendix (detailed metrics, backup slides)

Tone: Strategic, data-driven, transparent about challenges
```

### 3. metrics-storyteller (Sonnet, Skill-Aware)
Transforms data into narratives with context, insights, and implications for decision-making.

**Use for**: Data storytelling, metric interpretation, insight synthesis, trend analysis

**Example**:
```
Use metrics-storyteller to explain churn increase.
Data:
- Churn increased from 5% to 7% over 6 months
- Cohort analysis: Recent cohorts have worse retention
- Exit surveys: Top reasons are "too expensive" (40%), "missing features" (30%), "switching to competitor" (20%)

Story:
"Our churn rate has increased 40% (5% → 7%) over the past two quarters, primarily driven by price sensitivity in recent cohorts.

What's happening:
• New customers acquired during our recent price increase show 2x higher churn
• Competitor X launched at 30% lower price point in Q3
• Feature gaps (integrations, mobile app) cited by 30% of churners

Impact:
• $200K monthly revenue at risk if trend continues
• Increasing CAC payback period from 12 to 16 months
• Jeopardizes path to profitability timeline

Actions:
1. Launch value-add features to justify pricing (Q1)
2. Introduce annual plans with discount (immediate)
3. Improve onboarding to increase perceived value (ongoing)"
```

### 4. presentation-designer (Sonnet, Skill-Aware)
Designs executive-friendly presentations with clear visuals, minimal text, and strategic narrative flow.

**Use for**: Board decks, investor presentations, strategic reviews, all-hands presentations

**Example**:
```
Use presentation-designer for investor pitch deck.
Audience: Series A investors
Goal: Raise $10M
Length: 15-20 slides (15 min presentation)

Deck structure:
1. Cover: Company name + tagline
2. Problem: What pain are we solving? (customer quotes, market data)
3. Solution: Our product (screenshots, demo video)
4. Why now: Market timing (trends, catalysts)
5. Market size: TAM/SAM/SOM ($100M SAM)
6. Business model: Pricing, unit economics (LTV:CAC = 5:1)
7. Traction: Growth metrics (chart showing hockey stick)
8. Competition: Positioning map (why we win)
9. Product roadmap: Next 12 months
10. Go-to-market: Customer acquisition strategy
11. Team: Founders + key hires
12. Financials: 3-year projections
13. The ask: $10M for 18 months runway
14. Use of funds: Allocation breakdown
15. Vision: Where we're headed (5-10 years)

Design principles:
- One idea per slide
- Big, clear visuals
- Minimal text (bullets, not paragraphs)
- Data charts with callouts
- Consistent color scheme
```

## Skills

### executive-communication
Executive communication best practices and frameworks:
- **Pyramid Principle**: Conclusion first, supporting details after (Minto Pyramid)
- **SCQA Framework**: Situation, Complication, Question, Answer
- **Executive Summary**: Bottom line up front (BLUF), 1-page max
- **Data Storytelling**: Context → Insight → Implication → Action
- **Slide Design**: One idea per slide, visual over text, 6x6 rule (6 bullets, 6 words each)
- **Board Communication**: Strategic focus, transparency, requests explicit
- **Metrics Selection**: Focus on outcomes (revenue, customers) not activities (emails sent)
- **Visualization**: Simplified charts, big numbers, trend arrows (↑↓)
- **Narrative Flow**: Problem → Solution → Impact → Next steps
- **Tone**: Direct, confident, data-driven, transparent about challenges

## Templates

### executive-summary-template.md
Executive summary structure: Bottom line (1 sentence), key highlights (3-5 bullets), detailed context (paragraphs), recommendation/next steps, appendix (supporting data).

### board-deck-template.md
Board meeting deck: Cover, executive summary (1 slide), business metrics, financial summary, strategic initiatives, team update, asks/decisions needed, appendix.

### quarterly-business-review-template.md
QBR structure: Quarter highlights, KPI dashboard, wins/challenges, strategic initiatives progress, team updates, next quarter priorities, financial review.

### strategic-update-template.md
Strategic update memo: Executive summary, strategic context (market, competition), progress on initiatives, key decisions needed, resource requests, timeline.

## Workflows

### Quarterly Board Meeting
```
1. Synthesize insights
Use metrics-storyteller to turn data into narrative

2. Write executive summary
Use executive-summarizer for 1-page overview

3. Create board deck
Use board-report-writer for comprehensive board materials

4. Design presentation
Use presentation-designer for visual polish and flow
```

### Monthly Executive Report
```
1. Metrics storytelling
Use metrics-storyteller to explain trends and insights

2. Executive summary
Use executive-summarizer for key highlights and concerns

3. Distribution
Email summary + link to detailed dashboard
```

## Requirements Met

✅ Role: Executive reporting specialist
✅ Executive summary creation: executive-summarizer with pyramid principle
✅ Board presentation materials: board-report-writer with strategic focus
✅ High-level metric reporting: metrics-storyteller with data narratives
✅ Strategic insight synthesis: All agents provide context and implications
✅ Visualization for executives: presentation-designer with simplified visuals
✅ Tools: Presentation tools (guidance), data analysis, templates

## Key Features

✓ **Pyramid Principle**: Conclusion first, details after
✓ **BLUF (Bottom Line Up Front)**: Key message in first sentence
✓ **Data Storytelling**: Context → Insight → Implication → Action
✓ **Executive Brevity**: 1-page summaries, concise slides
✓ **Strategic Focus**: Outcomes over activities, big picture
✓ **Visual Clarity**: Simplified charts, big numbers, minimal text
✓ **Transparent Communication**: Address challenges directly
✓ **Action-Oriented**: Clear next steps and decisions needed

## Executive Communication Principles

### Pyramid Principle (Minto)
```
Start with conclusion:
"We should prioritize retention over acquisition in Q1."

Why? (Supporting arguments):
• Churn increased 40% (5% → 7%)
• CAC payback extended from 12 to 16 months
• Retention programs have 3x ROI vs new acquisition

How? (Implementation details):
• Launch value-add features
• Introduce annual plans with discount
• Improve onboarding
```

### SCQA Framework
```
Situation: What's the context?
"Our SaaS business grew 100% last year to $10M ARR."

Complication: What's the problem/opportunity?
"But churn increased to 7%, threatening profitability timeline."

Question: What should we do?
"Should we prioritize retention or continue growth focus?"

Answer: What's the recommendation?
"Prioritize retention in Q1 to reduce churn to 5%, then resume growth."
```

### Data Storytelling Structure
```
1. Context: "Churn has increased from 5% to 7%"
2. Insight: "Driven by price sensitivity in recent cohorts"
3. Implication: "$200K monthly revenue at risk"
4. Action: "Launch annual plans with discount"
```

## Executive Deck Best Practices

### Slide Design Rules
- **One idea per slide**: Don't cram multiple messages
- **Big, clear visuals**: Charts over tables
- **Minimal text**: Bullets, not paragraphs (6x6 rule)
- **Consistent design**: Same fonts, colors, layout
- **Callouts**: Highlight key numbers on charts

### Metric Presentation
```
Good:
"Revenue: $12M (+20% YoY) ↑"
[Big number with trend arrow and context]

Bad:
"Q4 revenue was $12,014,532 compared to $10,021,445 in Q4 2022..."
[Too precise, no visual, hard to parse]
```

### Chart Simplification
```
Operational dashboard (too detailed):
• 15 metrics, 4 decimal places, color-coded by threshold

Executive dashboard (simplified):
• 3-5 key metrics, rounded numbers, trend arrows (↑↓)
• Big number cards: "ARR: $12M (+20%)"
• Simple trend lines (not complex multi-axis charts)
```

## Board Meeting Structure (Typical 2-hour meeting)

```
1. Executive summary (5 min)
   - CEO presents 1-slide summary
   - Bottom line, highlights, asks

2. Business update (20 min)
   - Metrics dashboard
   - Key wins and challenges
   - Q&A

3. Financial review (20 min)
   - P&L, cash flow, burn rate
   - Variance to plan/budget
   - Forecast update
   - Q&A

4. Strategic deep-dive (30 min)
   - 1-2 strategic topics (product, market, competition)
   - Discussion and decision

5. Governance (20 min)
   - Approvals (budgets, comp, hires)
   - Committee reports
   - Formal motions

6. Executive session (20 min)
   - Board-only discussion (no management)
```

## Executive Summary Template
```
TO: [Audience]
FROM: [Author]
DATE: [Date]
RE: [Subject]

EXECUTIVE SUMMARY

[Bottom line in one sentence - recommendation or key message]

KEY HIGHLIGHTS
• [Highlight 1 - most important metric/outcome]
• [Highlight 2 - second most important]
• [Highlight 3 - key challenge or risk]

RECOMMENDATION
[What should we do? Clear next step or decision needed]

---

DETAILED CONTEXT

[Situation - what's the background?]
[Complication - what's the problem/opportunity?]
[Question - what decision is needed?]
[Answer - what's the recommendation and why?]

APPENDIX
[Supporting data, charts, analysis]
```

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 1 comprehensive executive-communication skill
- ✅ 4 professional templates for summaries, boards, QBRs, strategic updates
- ✅ Complete README with pyramid principle and communication frameworks

## Tone Guidelines

**For Board**:
- Strategic, transparent, data-driven
- Address challenges directly (don't hide bad news)
- Be clear about asks (decisions, approvals, guidance)

**For Executives**:
- Direct, concise, action-oriented
- Focus on implications (so what?)
- Provide context for decisions

**For Investors**:
- Confident, visionary, evidence-based
- Balance optimism with realism
- Demonstrate traction and momentum

Closes #83
