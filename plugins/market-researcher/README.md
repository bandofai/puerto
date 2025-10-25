# Market Researcher Plugin

**Production-ready market research and competitive analysis with TAM/SAM/SOM sizing, competitive intelligence, trend analysis, and customer segmentation**

A comprehensive plugin providing four specialized agents to handle all aspects of strategic market research, from market sizing to customer personas.

---

## Overview

This plugin provides a complete market research workflow with:

- **4 Specialized Agents**: Each agent focuses on one aspect of market research
- **3 Comprehensive Skills**: Battle-tested frameworks from consulting firms and research professionals
- **3 Professional Templates**: Ready-to-use Excel, PowerPoint, and Word templates
- **Full Research Coverage**: Market Sizing → Competitive Analysis → Trends → Customer Insights

---

## Agents

### 1. market-analyzer (Sonnet - Strategic Analysis)

**When to use**: Market sizing, TAM/SAM/SOM analysis, opportunity assessment

**What it does**:
- Calculates Total Addressable Market (TAM) using multiple methods
- Filters to Serviceable Addressable Market (SAM) with realistic constraints
- Estimates Serviceable Obtainable Market (SOM) with conservative market share
- Uses data triangulation (3+ sources) for validation
- Applies top-down, bottom-up, and value theory approaches
- Provides sensitivity analysis (best/base/worst case)
- Documents all assumptions transparently

**Skill-aware**: Reads `market-research` skill before starting

**Example usage**:
```bash
"Calculate the TAM, SAM, and SOM for cloud-based project management software
targeting mid-market companies (50-500 employees) in North America. Include
3-year growth forecast and confidence levels."
```

**Output**:
- Market sizing report with TAM/SAM/SOM
- Excel model with all calculations
- Assumptions log with sources
- Sensitivity analysis
- Growth forecast
- Confidence assessment

**Tools**: Read, Write, Edit, Bash, Grep, Glob, WebSearch
**Model**: Sonnet (requires strategic judgment for market analysis)

---

### 2. competitor-analyst (Sonnet - Strategic Intelligence)

**When to use**: Competitive landscape analysis, positioning, SWOT, Porter's 5 Forces

**What it does**:
- Identifies and categorizes competitors (direct, indirect, potential, substitutes)
- Applies Porter's 5 Forces framework for industry analysis
- Conducts SWOT analysis for us and top competitors
- Creates competitive positioning maps (price/quality, features, segments)
- Develops competitor profiles with strengths/weaknesses
- Analyzes strategic moves and predicts next moves
- Provides actionable competitive recommendations

**Skill-aware**: Reads `competitive-analysis` skill before starting

**Example usage**:
```bash
"Analyze the competitive landscape for our SaaS HR platform. Focus on top 5
direct competitors. Include Porter's 5 Forces, SWOT analysis, feature comparison,
and positioning maps. Identify key threats and opportunities."
```

**Output**:
- Competitive analysis report
- Porter's 5 Forces analysis
- Competitor profiles (top 5)
- Feature comparison matrix
- Positioning maps
- SWOT analysis
- Strategic recommendations
- Monitoring plan

**Tools**: Read, Write, Edit, Bash, Grep, Glob, WebSearch
**Model**: Sonnet (requires strategic judgment and synthesis)

---

### 3. trend-researcher (Sonnet - Strategic Foresight)

**When to use**: Industry trends, emerging technologies, market shifts, future forecasting

**What it does**:
- Researches industry trends across STEEP categories (Social, Technology, Economic, Environmental, Political)
- Assesses trend maturity using Gartner Hype Cycle
- Evaluates trend impact (likelihood, magnitude, timeframe)
- Identifies trend drivers and convergence patterns
- Validates trends with multiple sources (not just hype)
- Creates trend timeline (near/medium/long-term)
- Provides strategic implications and recommendations

**Skill-aware**: Reads `market-research` skill before starting

**Example usage**:
```bash
"Research key trends affecting the cybersecurity industry over the next 3-5 years.
Include technology trends (AI/ML), regulatory trends (compliance), and market trends
(cloud adoption). Assess impact on our market and recommend strategic responses."
```

**Output**:
- Trend analysis report
- Trend impact matrix (prioritized)
- STEEP analysis summary
- Trend timeline (near/medium/long-term)
- Converging mega-trends
- Strategic implications
- Monitoring dashboard
- Recommendations

**Tools**: Read, Write, Edit, Bash, Grep, Glob, WebSearch
**Model**: Sonnet (requires strategic judgment and synthesis)

---

### 4. segment-profiler (Sonnet - Skill-Aware Customer Insights)

**When to use**: Customer segmentation, persona development, needs analysis

**What it does**:
- Creates market segmentation using hybrid approach (demographic, behavioral, psychographic, needs-based)
- Develops detailed personas (3-7 per market) based on research
- Documents jobs-to-be-done and customer needs
- Sizes each segment with revenue potential
- Prioritizes segments using attractiveness/fit/accessibility framework
- Creates segment-specific strategies and messaging
- Provides actionable recommendations for product, marketing, and sales

**Skill-aware**: Reads `customer-segmentation` skill before starting

**Example usage**:
```bash
"Create customer segmentation for our B2B analytics platform. Identify 3-5 key
segments based on company size, industry, and use case. Develop detailed personas
for top 2 segments including goals, pain points, buying process, and how to reach them."
```

**Output**:
- Segmentation analysis report
- Detailed personas (1-2 per segment) using Word template
- Segment comparison matrix
- Segment prioritization (Tier 1/2/3)
- Segment-specific strategies
- Revenue potential by segment
- Recommendations for targeting

**Tools**: Read, Write, Edit, Bash, Grep, Glob, WebSearch
**Model**: Sonnet (requires judgment for segmentation and persona development)

---

## Skills

### 1. market-research

**Production-tested market sizing methodologies and research techniques**

Covers:
- TAM/SAM/SOM framework and definitions
- Market sizing techniques (top-down, bottom-up, value theory)
- Data source quality tiers (Tier 1: government/public filings, Tier 2: analyst reports, Tier 3: blogs/press releases)
- Data triangulation methodology (3+ sources required)
- Growth rate calculation (CAGR) and forecasting
- Assumption documentation requirements
- Sensitivity analysis (best/base/worst case)
- Common mistakes to avoid
- Market research workflow

**When read**: By `market-analyzer` and `trend-researcher` agents before starting

**Key frameworks**:
- TAM/SAM/SOM definitions and calculations
- Top-Down Approach: Start with total market, filter down
- Bottom-Up Approach: Build from customer count × ARPU
- Value Theory Approach: Value created × % captured
- Data Triangulation: Weighted average of 3+ sources
- Sensitivity Analysis: Best/base/worst case scenarios

---

### 2. competitive-analysis

**Strategic frameworks for competitive intelligence and positioning**

Covers:
- Porter's 5 Forces Framework (complete methodology for each force)
- SWOT Analysis (strengths, weaknesses, opportunities, threats)
- Competitive positioning maps (price/quality, features, segments)
- Competitor profiling template
- Feature comparison matrices
- Competitive intelligence gathering (ethical sources only)
- Strategic group analysis
- Win/loss analysis
- Monitoring and tracking

**When read**: By `competitor-analyst` agent before starting

**Key frameworks**:
- Porter's 5 Forces: Threat of new entrants, supplier power, buyer power, substitutes, rivalry
- SWOT: Internal (S/W) vs External (O/T), Positive vs Negative
- Positioning Maps: 2D visualization of competitive position
- Competitor Profiles: Comprehensive analysis template
- Strategic Recommendations: SO/ST/WO/WT strategies

---

### 3. customer-segmentation

**Segmentation frameworks, persona development, and jobs-to-be-done**

Covers:
- Segmentation frameworks (demographic, behavioral, psychographic, needs-based, hybrid)
- B2C vs B2B segmentation variables
- Comprehensive persona template (40+ sections)
- Jobs-to-be-Done framework
- Segment validation criteria (measurable, substantial, accessible, differentiable, actionable)
- Segment prioritization matrix (attractiveness, fit, accessibility, strategic value)
- Persona research methods (quantitative and qualitative)
- Needs analysis (functional, emotional, social)
- Buyer journey mapping
- Segment-specific strategies

**When read**: By `segment-profiler` agent before starting

**Key frameworks**:
- Hybrid Segmentation: Demographics + Behaviors + Psychographics + Needs
- Jobs-to-be-Done: When [situation], I want to [motivation], so I can [outcome]
- Persona Template: Comprehensive profile (goals, pain points, buying process)
- Segment Prioritization: 4-dimension scoring (attractiveness, fit, accessibility, strategic value)
- Buyer Journey: Awareness → Consideration → Decision → Post-Purchase

---

## Templates

### 1. market-analysis-template.xlsx

**Excel spreadsheet for TAM/SAM/SOM calculations**

Includes:
- **Executive Summary**: Key numbers and insights
- **TAM Calculation**: Top-down, bottom-up, value theory approaches
- **SAM Calculation**: Filters applied to TAM
- **SOM Calculation**: Market share assumptions by year
- **Growth Forecast**: Historical and future projections
- **Sensitivity Analysis**: Best/base/worst case scenarios
- **Assumptions Log**: Complete documentation of all assumptions
- **Data Sources**: Full bibliography with URLs
- **Calculations Reference**: Formula documentation
- **Presentation Summary**: One-page executive summary

**When used**: By `market-analyzer` agent for market sizing deliverables

---

### 2. competitive-analysis-template.pptx

**PowerPoint presentation deck for competitive landscape**

Includes (20-25 slides):
- **Executive Summary**: Key findings and recommendations
- **Competitive Landscape Overview**: Market map and categorization
- **Porter's 5 Forces**: Complete analysis of all 5 forces
- **Competitor Deep Dives**: Profiles of top 5 competitors
- **Positioning Maps**: Multiple dimensions (price/quality, features, segments)
- **Feature Comparison**: Detailed matrix
- **SWOT Analysis**: For us and competitors
- **Strategic Recommendations**: Prioritized actions
- **Monitoring Plan**: Ongoing tracking

**When used**: By `competitor-analyst` agent for presentation deliverables

---

### 3. customer-persona-template.docx

**Word document for detailed customer personas**

Includes (40+ sections):
- **Executive Summary**: Quick facts and quote
- **Demographics/Firmographics**: Full profile
- **Background & Day-in-the-Life**: Context and workflows
- **Goals & Success Metrics**: What they're trying to achieve
- **Pain Points & Challenges**: Top problems and frustrations
- **Buying Behavior**: Decision process and criteria
- **Objections & Concerns**: How to overcome
- **Psychographics**: Values, personality, communication style
- **Media Consumption**: Where to reach them
- **Needs Analysis**: Jobs-to-be-done framework
- **Our Solution Fit**: Value proposition and messaging
- **Engagement Strategy**: Content by buyer journey stage
- **Segment Economics**: Size, revenue potential, acquisition costs
- **Real Quotes**: Actual customer quotes from research

**When used**: By `segment-profiler` agent for persona deliverables

---

## Workflow Examples

### Example 1: Full Market Opportunity Assessment

```bash
# 1. Size the market
@market-analyzer "Calculate TAM/SAM/SOM for AI-powered customer service automation
targeting enterprise companies (1000+ employees) in North America. Include 5-year
forecast and identify key growth drivers."

# 2. Analyze competition
@competitor-analyst "Analyze competitive landscape for AI customer service automation.
Top 5 competitors. Include Porter's 5 Forces, positioning maps, and feature comparison.
Identify our differentiation opportunities."

# 3. Research trends
@trend-researcher "Research trends affecting customer service automation market:
AI/ML advances, customer expectations, regulatory, and workforce trends. 3-5 year outlook."

# 4. Define target customers
@segment-profiler "Create customer segmentation for enterprises buying customer service
automation. Identify 3-5 segments by company size, industry, and maturity. Develop detailed
personas for top 2 segments."
```

**Deliverables**:
- Complete market opportunity assessment
- TAM/SAM/SOM with growth forecast
- Competitive positioning strategy
- Trend implications for strategy
- Target customer profiles
- Go-to-market recommendations

---

### Example 2: Competitive Intelligence for Product Launch

```bash
# 1. Deep competitive analysis
@competitor-analyst "Comprehensive competitive analysis for our upcoming CRM product
launch. Analyze top 7 competitors (Salesforce, HubSpot, Pipedrive, Zoho, Freshsales,
Close, Copper). Include feature gaps we can exploit."

# 2. Market trends
@trend-researcher "Research CRM industry trends: sales automation, AI integration,
mobile-first, integration ecosystems. What features will matter most in 2-3 years?"

# 3. Target segments
@segment-profiler "Who should we target first with our CRM? Segment by company size,
sales team maturity, and current CRM (if any). Identify the beachhead segment."
```

**Deliverables**:
- Competitive positioning strategy
- White space opportunities
- Feature prioritization based on trends
- Beachhead customer segment
- Launch messaging and positioning

---

### Example 3: Market Entry Decision

```bash
# 1. Market sizing
@market-analyzer "Should we enter the cybersecurity insurance market? Size the TAM/SAM/SOM
for cyber insurance targeting mid-market companies. Include growth forecast and assess
market maturity."

# 2. Competitive intensity
@competitor-analyst "Analyze competitive landscape for cyber insurance. How crowded is it?
Porter's 5 Forces analysis. What's the barrier to entry? Where are the opportunities?"

# 3. Industry trends
@trend-researcher "What trends are driving/hindering cyber insurance adoption? Regulatory,
claims trends, pricing dynamics. Is this market growing or consolidating?"

# 4. Customer insights
@segment-profiler "Who buys cyber insurance and why? Segment by industry and risk profile.
What are their pain points with current offerings? What job are they hiring insurance to do?"
```

**Deliverables**:
- Market entry recommendation (Go/No-Go)
- Market opportunity size and growth
- Competitive barriers and advantages
- Target customer segments
- Entry strategy and positioning

---

### Example 4: Strategic Planning / Annual Planning

```bash
# 1. Market trends
@trend-researcher "What trends will most impact our business in the next 3 years?
Technology, competitive, regulatory, customer behavior. Which are threats vs opportunities?"

# 2. Competitive moves
@competitor-analyst "What have our competitors done in the last 12 months? Funding,
product launches, partnerships, M&A. What are they likely to do next?"

# 3. Market sizing update
@market-analyzer "Update our TAM/SAM/SOM calculations. How has the market grown?
Update our 3-year forecast. Are we on track with our market share assumptions?"

# 4. Customer evolution
@segment-profiler "How have our customer segments evolved? Are there new segments
emerging? Update our personas based on latest customer feedback."
```

**Deliverables**:
- Strategic trends report
- Competitive threat assessment
- Updated market opportunity
- Customer insights for roadmap
- Strategic priorities for next year

---

## Installation

### User-Level (Available in All Projects)

```bash
# Clone or copy this plugin to your user-level plugins directory
cp -r plugins/market-researcher ~/.claude/plugins/

# Verify installation
ls ~/.claude/plugins/market-researcher/agents/
```

### Project-Level (Project-Specific)

```bash
# Copy to project's .claude directory
mkdir -p .claude/plugins
cp -r plugins/market-researcher .claude/plugins/

# Commit to version control
git add .claude/plugins/market-researcher/
git commit -m "feat: add market-researcher plugin"
```

---

## Configuration

### Project-Specific Data Sources

Create a file with your preferred data sources:

```bash
# Create project-specific data sources
cat > .claude/market-research-sources.md << 'EOF'
# Project Data Sources

## Internal Data
- CRM: Salesforce data export
- Analytics: Google Analytics + Mixpanel
- Sales: Win/loss analysis database

## Industry-Specific Sources
- [Industry Association]: Annual reports
- [Trade Publication]: Market data
- [Analyst Firm]: Subscribed reports

## Competitors to Track
1. [Competitor A]: Website, LinkedIn, press releases
2. [Competitor B]: Public filings, blog, job postings
EOF
```

---

## Design Decisions

### Why These Agents?

**Four agents, not one**: Single responsibility principle. Each agent is an expert in one domain:
- market-analyzer: Quantitative market sizing
- competitor-analyst: Strategic competitive intelligence
- trend-researcher: Future-focused trend analysis
- segment-profiler: Customer insights and personas

**Why all Sonnet**: Market research requires strategic judgment, synthesis, and analysis. These are not deterministic tasks suitable for Haiku. The cost is justified by the strategic value of the insights.

**Why skill-aware**: Market research has established frameworks (TAM/SAM/SOM, Porter's 5 Forces, SWOT, segmentation) that must be applied correctly. Skills ensure consistent, professional-quality output following best practices from consulting firms and research professionals.

### Why WebSearch Integration?

Market research requires current, external data:
- Market size data from analyst reports
- Competitor information (funding, products, customers)
- Industry trends and news
- Technology adoption data
- Regulatory changes

Without WebSearch, agents would be limited to general knowledge. With WebSearch, they can gather real-time market intelligence.

### Why These Frameworks?

**TAM/SAM/SOM**: Industry standard for market sizing, required by VCs and executives

**Porter's 5 Forces**: 40+ years of validation, taught in every business school, comprehensive view of competitive dynamics

**SWOT**: Simple, actionable, widely understood by business stakeholders

**Jobs-to-be-Done**: Customer-centric approach that reveals unmet needs and innovation opportunities

**Segmentation**: Essential for targeting, positioning, and go-to-market strategy

These aren't trendy frameworks - they're time-tested tools used by McKinsey, BCG, Bain, and every major consulting firm.

---

## Best Practices

### Market Sizing

1. **Always triangulate**: Use 2-3 methods (top-down + bottom-up minimum)
2. **Be conservative**: Better to under-promise than over-promise
3. **Document assumptions**: Every assumption must be explicit and justified
4. **Use quality sources**: Tier 1 (government, public filings) > Tier 2 (analysts) > Tier 3 (blogs)
5. **Validate with customers**: Does the SOM match # of customers × ACV?
6. **Show sensitivity**: Best/base/worst case always
7. **Update quarterly**: Markets change, keep sizing current

### Competitive Analysis

1. **Comprehensive coverage**: Direct + indirect + substitutes + potential entrants
2. **Evidence-based only**: Every claim backed by specific evidence
3. **Ethical sources only**: Public information, analyst reports, customer reviews
4. **Multiple frameworks**: Porter's 5 Forces + SWOT + Positioning - no single view is complete
5. **Strategic focus**: Analysis must drive actionable recommendations
6. **Monitor continuously**: Quarterly competitive updates, track major moves
7. **Validate with sales**: Do they recognize these competitors and dynamics?

### Trend Research

1. **Distinguish signal from noise**: Media hype ≠ real trend, validate with data
2. **Multi-source validation**: 3+ independent sources for major trends
3. **STEEP coverage**: Social, Technology, Economic, Environmental, Political
4. **Assess maturity**: Use Gartner Hype Cycle or similar framework
5. **Impact assessment**: Likelihood × Impact × Timeframe
6. **Connect trends**: Look for convergence and mega-trends
7. **Strategic implications**: Every trend must have "so what?" answer

### Customer Segmentation

1. **Research-based personas**: 10-15 customer interviews per segment minimum
2. **Hybrid segmentation**: Demographics + Behaviors + Psychographics + Needs
3. **Must prioritize**: Tier 1/2/3 with clear resource allocation
4. **Actionable segments**: If you'd market the same way, don't segment
5. **Include real quotes**: Bring personas to life with actual customer voice
6. **Validate segments**: Measurable, substantial, accessible, differentiable, actionable
7. **Update quarterly**: Personas get stale, refresh with new customer feedback

---

## Cost Optimization

**Estimated costs per task** (based on Claude Sonnet pricing):

| Task | Agent | Model | Est. Cost |
|------|-------|-------|-----------|
| Market sizing | market-analyzer | Sonnet | ~$0.15 |
| Competitive analysis | competitor-analyst | Sonnet | ~$0.20 |
| Trend research | trend-researcher | Sonnet | ~$0.18 |
| Customer segmentation | segment-profiler | Sonnet | ~$0.25 |

**Total cost for full market research**: ~$0.80

**Value delivered**: These analyses would cost $5,000-$50,000 from consulting firms or $10,000-$25,000 from market research agencies.

**ROI**: 6,000x - 62,000x cost savings

**Cost justification**: Sonnet is required for strategic analysis (no Haiku option makes sense). The absolute cost is low (~$1) for deliverables that inform million-dollar decisions.

---

## Troubleshooting

### Market sizing numbers seem off

**Issue**: TAM/SAM/SOM don't pass sanity check

**Solutions**:
- Check that TAM > SAM > SOM (strictly)
- Validate bottom-up matches top-down (within 50%)
- Verify market share assumptions (new entrant rarely >5% Year 3)
- Review data sources (are they for the same market definition?)
- Check assumptions log (unrealistic assumptions?)

### Competitive analysis missing key competitors

**Issue**: Major competitor not included in analysis

**Solutions**:
- Explicitly mention competitor: "Include [Company] in analysis"
- Provide competitor list: "Analyze these 5 competitors: ..."
- Use more specific search: "Direct competitors in [specific category]"
- Review categorization (might be listed as indirect or potential)

### Persona doesn't match our customers

**Issue**: Persona feels generic or doesn't reflect real customers

**Solutions**:
- Ensure agent has access to customer data/CRM
- Provide actual customer examples: "Base persona on customers like [Company A, Company B]"
- Share customer interviews/feedback: "Read customer-feedback.md before creating persona"
- Validate with sales/CS team: "Does this match who we actually sell to?"
- Create project-specific customer-segmentation skill with your customer archetypes

### Trends seem like hype, not real

**Issue**: Trend analysis includes overhyped or unlikely trends

**Solutions**:
- Request validation: "Validate trends with quantitative data, not just media coverage"
- Specify timeframe: "Focus on near-term trends (0-2 years) with evidence of adoption"
- Filter by maturity: "Only include trends past Peak of Inflated Expectations"
- Require proof: "Show market size data or adoption rates for each trend"

---

## Integration with Other Plugins

### With backend-architect

```bash
# 1. Market research defines opportunity
@market-analyzer "Size the market for API management platforms"

# 2. Architect designs for target market
@api-designer "Design API architecture for mid-market companies based on market-analyzer findings"
```

### With frontend-developer

```bash
# 1. Segment profiler identifies customers
@segment-profiler "Create personas for our design tool"

# 2. Frontend builds for personas
@component-builder "Build drag-and-drop interface optimized for [Persona Name] who needs simplicity over power"
```

### With orchestrator

```bash
# Use orchestrator to run full market research workflow
@orchestrator "Conduct complete market opportunity assessment:
1. @market-analyzer: Size the market
2. @competitor-analyst: Analyze competition
3. @trend-researcher: Research trends
4. @segment-profiler: Define target customers
Synthesize findings into go-to-market strategy."
```

---

## Examples Gallery

### Market Sizing Examples

**B2B SaaS**: Project management for agencies
- TAM: $4.2B (global PM software market × agency segment)
- SAM: $850M (agencies with 10+ employees, English-speaking markets)
- SOM: $25M (3% market share Year 3)
- CAGR: 12% (2024-2029)

**B2C Consumer**: Meal kit delivery
- TAM: $18B (US households × % that cook × $ meal replacement)
- SAM: $5.4B (urban/suburban households with delivery access)
- SOM: $180M (1M subscribers × $15/order × 12 orders/year)
- CAGR: 8% (slower growth, market maturing)

### Competitive Analysis Examples

**Five Forces Analysis**: SaaS Marketing Automation
- Threat of New Entrants: Medium (low capital requirements but high switching costs)
- Supplier Power: Low (many technology suppliers, commoditized infrastructure)
- Buyer Power: Medium-High (SMB low power, Enterprise high power)
- Threat of Substitutes: Medium (spreadsheets, email tools, consulting)
- Competitive Rivalry: High (many players, slow growth, high fixed costs)
- **Industry Attractiveness**: Medium

**SWOT Analysis**: Cybersecurity Startup
- Strengths: AI-powered detection, faster time-to-value, modern UX
- Weaknesses: Limited track record, small team, narrow product
- Opportunities: Growing SMB market, compliance requirements, cloud migration
- Threats: Incumbents adding AI, budget cuts, commoditization

### Trend Examples

**Critical Trend**: AI Integration in B2B SaaS
- Likelihood: High (90% of vendors investing)
- Impact: High (table stakes for competition)
- Timeframe: Near-term (1-2 years)
- Maturity: Slope of Enlightenment
- Action: Prioritize AI features in roadmap

**Trend to Monitor**: Decentralized Identity
- Likelihood: Medium (30% adoption by 2027)
- Impact: High (could disrupt auth/access management)
- Timeframe: Medium-term (3-5 years)
- Maturity: Trough of Disillusionment
- Action: Monitor, pilot internally

### Segmentation Examples

**B2B Segment**: Fast-Growing Tech Startups
- Size: 8,000 companies (Series A/B, 10-50 employees, tech hubs)
- Behavior: Early adopters, daily active users, rapid deployment
- Needs: Scale operations without slowing velocity
- Revenue: $25k ACV × 8,000 = $200M TAM
- Priority: Tier 1 (best product fit, expansion potential)

**B2C Persona**: "Busy Professional" (Meal Kit Customer)
- Demographics: 30-40, dual income household, no time to cook
- Pain Points: Dinner decision fatigue, food waste, health concerns
- Buying Trigger: New baby or job change (less time)
- Decision Criteria: Convenience > cost, health-focused options
- Lifetime Value: $2,400 (24 months × $100/month)

---

## Contributing

Found a better framework? Have a more effective approach? Contributions welcome!

1. Test your improvement in actual research projects
2. Document the methodology clearly
3. Submit PR with explanation and examples
4. Include before/after results if applicable

**Areas especially welcome**:
- Additional market sizing techniques
- New competitive frameworks beyond Porter's/SWOT
- Improved persona templates
- Industry-specific research approaches
- International market sizing methods

---

## Resources

### Market Research

**Books**:
- "Competitive Strategy" by Michael Porter (Porter's 5 Forces origin)
- "Crossing the Chasm" by Geoffrey Moore (Market segmentation)
- "The Mom Test" by Rob Fitzpatrick (Customer interviews)
- "Competing Against Luck" by Clayton Christensen (Jobs-to-be-Done)

**Online Resources**:
- CB Insights: Market research reports
- Gartner, Forrester, IDC: Industry analyst reports
- Statista: Market size data
- Census.gov: US demographic data
- Crunchbase: Company funding and competitive intelligence

### Competitive Analysis

**Frameworks**:
- Harvard Business Review: Porter's articles
- Blue Ocean Strategy: Value innovation framework
- Playing to Win: Strategy framework (Lafley & Martin)

**Tools**:
- SimilarWeb: Competitive website analytics
- BuiltWith: Technology stack analysis
- G2, Capterra, TrustRadius: Customer reviews
- LinkedIn Sales Navigator: Competitive intelligence

### Customer Research

**Books**:
- "The Lean Startup" by Eric Ries (Customer development)
- "Inspired" by Marty Cagan (Product discovery)
- "Obviously Awesome" by April Dunford (Positioning)

**Resources**:
- NN/g (Nielsen Norman Group): UX research methods
- Jobs-to-be-Done: Intercom's JTBD framework
- Persona templates: HubSpot, Xtensio

---

## License

Part of the Puerto plugin ecosystem.

---

## Changelog

### v1.0.0 (2025-01-20)

**Initial Release**

- 4 specialized agents (market-analyzer, competitor-analyst, trend-researcher, segment-profiler)
- 3 comprehensive skills (market-research, competitive-analysis, customer-segmentation)
- 3 professional templates (Excel, PowerPoint, Word)
- Full WebSearch integration for real-time market intelligence
- TAM/SAM/SOM framework with data triangulation
- Porter's 5 Forces and SWOT analysis
- STEEP trend analysis with impact assessment
- Hybrid customer segmentation with detailed personas
- Jobs-to-be-Done framework
- Production-ready deliverables

---

## Support

**Issues**: Report at [Puerto GitHub Issues](https://github.com/bandofai/puerto/issues)

**Questions**: Tag your issue with `plugin:market-researcher`

**Feature Requests**: Use `enhancement` label

---

**Version**: 1.0.0
**Author**: Puerto Plugin System
**Last Updated**: January 2025
**Status**: Production Ready
**Use Cases**: Market sizing, competitive analysis, strategic planning, customer segmentation, go-to-market strategy, investment decisions

---

## Quick Start Guide

**New to market research?** Start here:

1. **Market Sizing** (Start here if entering new market):
   ```bash
   @market-analyzer "Calculate TAM/SAM/SOM for [your product] in [your market]"
   ```

2. **Competitive Analysis** (Start here if in existing market):
   ```bash
   @competitor-analyst "Analyze competitive landscape for [your product]. Top 5 competitors."
   ```

3. **Customer Insights** (Start here if unclear on target customer):
   ```bash
   @segment-profiler "Who should we target? Create customer segmentation for [your product]."
   ```

4. **Strategic Planning** (Annual planning cycle):
   ```bash
   Run all 4 agents, review together, synthesize into strategic plan
   ```

**Pro tip**: Start with segmentation. Once you know your target customer, market sizing and competitive analysis become much more focused and actionable.

---

**Ready to get started?** Install the plugin and invoke your first agent!
