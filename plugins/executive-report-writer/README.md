# Executive Report Writer Plugin

**Professional executive communications using proven frameworks: Pyramid Principle, BLUF, McKinsey slide design, and data storytelling**

## Overview

This plugin provides a comprehensive suite of agents for creating high-impact executive communications. All agents leverage a shared Executive Communication skill containing battle-tested patterns from top consulting firms (McKinsey, BCG) and executive writing frameworks (Pyramid Principle by Barbara Minto, BLUF approach).

## What's Included

### Skill: Executive Communication
- **Pyramid Principle** structure (Barbara Minto method)
- **BLUF** (Bottom Line Up Front) approach
- **Data storytelling** frameworks (Three-Act, PIAI, SCR)
- **McKinsey-style** slide design principles
- **Board report** structure and requirements
- **Executive summary** best practices
- **RAG status reporting** (Red/Amber/Green)
- **Strategic vs tactical** information filtering

### Agents

1. **executive-summarizer** (Sonnet)
   - Creates 1-2 page executive summaries
   - Applies Pyramid Principle structure
   - BLUF approach with conclusion first
   - Perfect for distilling reports, analyses, proposals

2. **board-report-writer** (Sonnet)
   - Writes comprehensive board reports (8-15 pages)
   - Includes financial metrics, strategic initiatives, risks, decisions
   - RAG status indicators for all initiatives
   - Professional board-ready formatting

3. **metrics-storyteller** (Sonnet)
   - Transforms raw data into compelling narratives
   - Uses proven storytelling frameworks (Three-Act, PIAI, SCR)
   - Contextualizes all numbers (vs target, prior period, benchmark)
   - Connects metrics to business outcomes

4. **presentation-designer** (Sonnet)
   - Designs executive presentations following McKinsey principles
   - One message per slide rule
   - Complete sentence headlines stating conclusions
   - Executive-friendly visuals with minimal clutter

## Key Principles

### Pyramid Principle (Barbara Minto)

Structure every communication top-down:

```
[CONCLUSION]
    ├── Key Point 1
    │   ├── Support A
    │   ├── Support B
    │   └── Support C
    ├── Key Point 2
    │   └── [Supporting facts]
    └── Key Point 3
        └── [Supporting facts]
```

**Start with the answer, then support it.**

### BLUF (Bottom Line Up Front)

Every document starts with the conclusion:

- First sentence = recommendation or main finding
- First paragraph = key supporting points
- Details and analysis follow

**Example**:
> "We recommend expanding to Asian markets in Q1 2025 to capture a $2.5B opportunity with 18-month payback."
>
> Not: "After conducting market analysis and evaluating multiple factors, we have some recommendations regarding potential expansion opportunities..."

### Data Storytelling

Numbers need context and narrative:

- **Raw**: "Revenue is $2.5M"
- **Contextualized**: "Revenue reached $2.5M (+40% YoY, exceeding target by $500K)"
- **Story**: "Revenue growth accelerated to 40% YoY (vs 25% last quarter), driven by enterprise segment which doubled in size..."

### McKinsey Slide Design

One message per slide:

- **Headline**: Complete sentence stating conclusion (28-32pt)
- **Body**: Max 50 words, 3-5 bullet points (18-24pt)
- **Visual**: One chart or key number
- **White space**: 30-40% of slide

**Example headline**: ❌ "Q3 Results" → ✅ "Q3 revenue exceeded target by 15%, driven by enterprise growth"

## Installation

### Option 1: Project-Level (Recommended)

```bash
# Copy plugin to your project
cp -r plugins/executive-report-writer .claude/plugins/

# Or symlink for updates
ln -s $(pwd)/plugins/executive-report-writer ~/.claude/plugins/

# Verify installation
ls .claude/plugins/executive-report-writer/
```

### Option 2: User-Level (Available to all projects)

```bash
# Copy to user directory
cp -r plugins/executive-report-writer ~/.claude/plugins/

# Verify installation
ls ~/.claude/plugins/executive-report-writer/
```

## Usage

### Executive Summarizer

Creates concise 1-2 page executive summaries from any document.

```bash
# Automatic activation (skill-aware)
"I need an executive summary of this analysis report"
"Create a one-page executive summary for the board"
"Summarize this proposal for the CEO"

# Manual invocation
@executive-summarizer "Summarize the Q3 performance analysis.md"
```

**Output**:
- 1-2 page markdown summary
- Pyramid structure (conclusion → key points → support)
- Contextualized metrics
- Clear recommendations with owners and timelines

**Example output**:
```markdown
## Executive Summary

### The Bottom Line
We recommend launching in Germany by Q2 2025 with $3M investment to
capture the $800M European mid-market opportunity.

### Why This Matters
European expansion is critical to achieving our 2025 revenue target of
$50M. Germany represents 35% of the European market with minimal
localization required.

### Key Findings
• Market readiness: 2,400 qualified prospects, 60% using competitors
• Regulatory advantage: GDPR-native architecture provides edge
• Economic viability: 12-month payback, 42% gross margin, $12M ARR Year 2

### Recommended Actions
1. Establish legal entity - Legal team - By Dec 31, 2024
2. Hire country manager - Talent team - By Jan 31, 2025
3. Launch with 3 pilots - Sales team - By Mar 31, 2025

### Expected Impact
Year 1: $2M ARR | Year 2: $12M ARR | Year 3: $25M ARR
```

### Board Report Writer

Creates comprehensive board reports with all standard sections.

```bash
# Automatic activation
"Prepare the Q3 board report"
"Create board materials for next month's meeting"
"Write the board report with financials and strategic updates"

# Manual invocation
@board-report-writer "Create board report for November 2024 meeting"
```

**Output**:
- 8-15 page comprehensive report
- Executive summary (1 page)
- Business performance with metrics
- Strategic initiatives with RAG status
- Risk assessment
- Decisions requested
- Appendices with details

**Sections included**:
1. Executive Summary (1 page)
2. Business Performance (2-3 pages) - Financial + Operational metrics
3. Strategic Initiatives (2-3 pages) - With 🟢 🟡 🔴 status
4. Risks and Opportunities (1-2 pages)
5. Decisions Needed (1-2 pages) - Options + recommendation
6. Appendices (as needed)

### Metrics Storyteller

Turns data into compelling narratives with business context.

```bash
# Automatic activation
"Tell the story behind these revenue numbers"
"Create a narrative for the customer churn data"
"Explain what these metrics mean for the business"

# Manual invocation
@metrics-storyteller "Create story from metrics-dashboard.csv"
```

**Output**:
- Narrative with clear story arc (Setup → Conflict → Resolution)
- All numbers contextualized (vs target, prior period, benchmark)
- Root cause analysis
- Business impact quantified
- Actionable recommendations

**Storytelling frameworks used**:
- **Three-Act Structure**: Setup → Conflict → Resolution
- **PIAI**: Problem → Insight → Action → Impact
- **SCR**: Situation → Complication → Resolution

**Example output**:
```markdown
## Customer Churn: Investigation and Response

### What Happened
Customer churn increased from 3% to 8% in Q3 (+5pp), putting $2M ARR
at risk.

### Root Cause
Analysis reveals 80% of churned customers experienced billing issues
within 30 days. Our payment system fails to handle international credit
cards, affecting 35% of customers.

### Corrective Action
We'll implement Stripe International within 30 days and proactively
contact 850 at-risk accounts with billing issues.

### Expected Impact
Churn reduces to 5% (-3pp), saving $1.2M ARR annually. Additionally
unlocks European expansion where payment issues currently block 40%
of potential customers.
```

### Presentation Designer

Designs executive presentations following McKinsey principles.

```bash
# Automatic activation
"Design a board presentation"
"Create investor pitch deck structure"
"Build executive presentation for strategic review"

# Manual invocation
@presentation-designer "Create 30-min board update presentation"
```

**Output**:
- 10-20 slide presentation structure (markdown format)
- One message per slide
- Complete sentence headlines stating conclusions
- Visual descriptions and layout guidance
- Speaker notes and timing recommendations

**Slide design principles**:
- Headline: 28-32pt, complete sentence, states conclusion
- Body: Max 50 words, 18-24pt
- One visual per slide
- 30-40% white space
- 2-3 minutes per slide

**Example slide**:
```markdown
# Slide 5: Revenue Performance

## Q3 revenue exceeded target by 15%, driven by enterprise growth

### $8.2M
+45% YoY | 112% of target

**Growth drivers**:
• Enterprise deals averaged $85K (up from $52K in Q2)
• Win rate improved to 38% (up from 28%)
• Sales cycle decreased to 45 days (down from 67)

---
Source: Internal analysis | Page 5
```

## Workflow Examples

### Scenario 1: Quarterly Board Meeting

```bash
# 1. Create comprehensive board report
@board-report-writer "Create Q3 2024 board report with financial performance, strategic initiative updates, and Series B decision"

# 2. Extract executive summary for email
@executive-summarizer "Create 1-page summary from board-report-2024-11-15.md"

# 3. Design presentation for meeting
@presentation-designer "Create 20-minute board presentation from board-report-2024-11-15.md"

# 4. Add data storytelling for key metrics
@metrics-storyteller "Create narrative explaining the customer churn trend for board"
```

### Scenario 2: Investor Update

```bash
# 1. Create executive summary of progress
@executive-summarizer "Summarize our Q3 progress for investors"

# 2. Tell the story behind the metrics
@metrics-storyteller "Create compelling narrative from our growth metrics"

# 3. Design investor update deck
@presentation-designer "Create 10-slide investor update presentation"
```

### Scenario 3: Strategic Planning

```bash
# 1. Summarize market analysis
@executive-summarizer "Create executive summary of market-analysis.md"

# 2. Tell the opportunity story
@metrics-storyteller "Create narrative showing the Asia-Pacific opportunity"

# 3. Design strategic review presentation
@presentation-designer "Create strategic review presentation with 3 expansion options"

# 4. Write recommendation memo
@board-report-writer "Create decision memo for geographic expansion with financial analysis and recommendation"
```

## Best Practices

### For Executive Summaries

- ✅ Start with conclusion in first sentence
- ✅ Maximum 1-2 pages (300-600 words)
- ✅ Use Pyramid Principle structure
- ✅ Contextualize all numbers (vs what?)
- ✅ Specific recommendations with owner + timeline
- ✅ Quantify expected impact
- ❌ Don't bury the lead
- ❌ Don't exceed 2 pages
- ❌ Don't use jargon
- ❌ Don't make vague recommendations

### For Board Reports

- ✅ Executive summary on page 1 (max 1 page)
- ✅ Total 8-15 pages (excluding appendices)
- ✅ Include RAG status (🟢 🟡 🔴) for all initiatives
- ✅ Be balanced (report good and bad news)
- ✅ Forward-looking (60% future, 40% past)
- ✅ Distribute 5-7 days before meeting
- ❌ Don't exceed 15 pages for main report
- ❌ Don't sugarcoat challenges
- ❌ Don't present options without recommendation
- ❌ Don't use vague timelines

### For Metrics Stories

- ✅ Every number needs context (vs target, prior, benchmark)
- ✅ Apply storytelling framework (Three-Act, PIAI, SCR)
- ✅ Focus on business impact, not just data
- ✅ Identify root causes, not just symptoms
- ✅ Provide actionable insights
- ✅ Pass "So What?" test for every metric
- ❌ Don't present raw numbers without context
- ❌ Don't show data without interpretation
- ❌ Don't ignore the "why" behind numbers
- ❌ Don't use technical jargon

### For Presentations

- ✅ One message per slide (non-negotiable)
- ✅ Headlines are complete sentences stating conclusions
- ✅ Maximum 50 words per slide
- ✅ Minimum 18pt font for body text
- ✅ One visual per slide
- ✅ 30-40% white space on each slide
- ✅ 2-3 minutes per slide timing
- ❌ Don't use topic-only headlines ("Q3 Results")
- ❌ Don't cram multiple messages on one slide
- ❌ Don't use fonts smaller than 18pt
- ❌ Don't include chart AND table on same slide

## RAG Status Reporting

All agents understand and use traffic light (RAG) status:

### Status Definitions

**🟢 Green (On Track)**:
- Meeting or exceeding targets
- No significant blockers
- Within budget and timeline
- High confidence in delivery

**🟡 Yellow/Amber (At Risk)**:
- Slightly behind (5-15% variance)
- Minor blockers present
- Mitigation plan in place
- Medium confidence (needs attention)

**🔴 Red (Off Track)**:
- Significantly behind (>15% variance)
- Major blockers or issues
- Intervention required
- Low confidence without changes

### Usage in Reports

```markdown
## Strategic Initiatives

| Initiative | Status | Progress | Next Milestone |
|------------|--------|----------|----------------|
| Product Launch | 🟢 | 85% | Q1 launch on track |
| Sales Hiring | 🟡 | 60% | Slow hiring, engaging recruiters |
| Cloud Migration | 🔴 | 35% | Behind schedule, budget overrun |
```

## Output Locations

All agents save outputs to organized directories:

```
./executive-summaries/
  └── executive-summary-2024-11-15.md

./board-materials/
  └── board-report-2024-11-15.md

./metrics-stories/
  └── metrics-narrative-2024-11-15.md

./presentations/
  └── presentation-2024-11-15.md
```

You can customize output locations:

```bash
# Set custom output directory
OUTPUT_DIR="./reports" @executive-summarizer "Summarize analysis.md"

# Set meeting date for board materials
MEETING_DATE="2024-12-15" @board-report-writer "Create board report"
```

## Skill Reference

The Executive Communication skill contains:

1. **Pyramid Principle** (Barbara Minto)
   - Top-down structure
   - Conclusion first, support follows
   - Grouping and ordering logic

2. **Executive Writing Style**
   - Short sentences (15-20 words)
   - Active voice (>90%)
   - Strong verbs, concrete nouns
   - No jargon or hedging

3. **Data Storytelling Frameworks**
   - Three-Act Structure (Setup → Conflict → Resolution)
   - PIAI (Problem → Insight → Action → Impact)
   - SCR (Situation → Complication → Resolution)

4. **Visualization Guidelines**
   - Chart selection by data type
   - Simplification principles
   - Color strategy
   - Executive-friendly design

5. **Board Report Structure**
   - Standard sections and length
   - RAG status reporting
   - Decision frameworks
   - Timing and distribution

6. **Executive Summary Best Practices**
   - Perfect structure template
   - First sentence rule
   - Density rule (every sentence adds value)

7. **Strategic vs Tactical Filtering**
   - What executives need to know
   - What to delegate/exclude
   - Aggregation rules

8. **Key Message Frameworks**
   - Rule of Three
   - "So What?" test
   - FAB (Features → Advantages → Benefits)

All agents read this skill first to ensure consistent, high-quality outputs.

## Tips for Success

### Writing for Executives

1. **Respect their time**:
   - Get to the point immediately
   - Use formatting for scannability
   - Provide details in appendices

2. **Be specific**:
   - No vague statements ("soon", "many", "significant")
   - Quantify everything possible
   - Include owners and timelines

3. **Tell the truth**:
   - Share bad news directly
   - Don't sugarcoat challenges
   - Take responsibility

4. **Make it actionable**:
   - Clear recommendations
   - Specific next steps
   - Decisions requested explicitly

### Common Mistakes to Avoid

1. **Burying the lead**: Start with conclusion, not background
2. **Too much detail**: Focus on insights, not every data point
3. **Weak recommendations**: Be specific and decisive
4. **Data without story**: Always provide context and narrative
5. **No ask**: Be clear about what decision or action you need
6. **Wrong altitude**: Focus on strategy and outcomes, not tactics
7. **No risk discussion**: Be balanced, address challenges openly
8. **Vague timelines**: Use specific dates, not "soon" or "later"

## Support

For issues, questions, or contributions:

- **Documentation**: See `/skills/executive-communication/SKILL.md`
- **Examples**: Check agent definitions for templates
- **Patterns**: Review Pyramid Principle and BLUF sections

## Version

- **Version**: 1.0
- **Last Updated**: January 2025
- **License**: MIT
- **Framework Credits**:
  - Pyramid Principle: Barbara Minto
  - McKinsey Slide Design: McKinsey & Company
  - BLUF Approach: US Military communication standard

## Related Plugins

- **academic-researcher**: For research papers and literature reviews
- **brand-strategist**: For brand messaging and positioning
- **budget-analyst**: For financial analysis and variance reporting
- **orchestrator**: For complex multi-agent workflows

---

**Transform your executive communications with proven frameworks and professional polish.**
