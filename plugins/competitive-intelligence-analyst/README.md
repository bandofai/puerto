# Competitive Intelligence Analyst Plugin

Competitor monitoring and market intelligence specialist for tracking competitors, analyzing features, pricing, and assessing competitive threats.

## Overview

The Competitive Intelligence Analyst plugin provides comprehensive competitive intelligence capabilities through specialized agents that monitor competitors, analyze features and pricing, and assess strategic threats. All agents leverage WebSearch for real-time market intelligence and follow skill-aware patterns for professional analysis.

## What's Included

### 4 Specialized Agents

1. **competitor-monitor** (Sonnet, WebSearch-enabled)
   - Real-time competitor monitoring for product launches, pricing changes, strategic moves
   - Uses WebSearch for latest intelligence
   - Threat assessment with severity levels
   - Generates comprehensive competitor intelligence reports
   - **Skill-aware**: Reads `competitive-intelligence/SKILL.md`

2. **feature-comparator** (Sonnet, Skill-Aware)
   - Creates detailed feature comparison matrices
   - Uses Excel (xlsx skill) for professional spreadsheets
   - Gap analysis with prioritization (P0/P1/P2/P3)
   - Identifies differentiators and competitive gaps
   - **Skill-aware**: Reads both `xlsx/SKILL.md` and `competitive-intelligence/SKILL.md`

3. **pricing-analyzer** (Sonnet, WebSearch-enabled)
   - Analyzes competitive pricing strategies
   - Tracks pricing changes over time
   - Calculates total cost of ownership (TCO)
   - Price positioning and recommendations
   - **Skill-aware**: Reads `pricing-analysis/SKILL.md`

4. **threat-assessor** (Sonnet, Skill-Aware)
   - Assesses competitive threats with scoring framework
   - Strategic risk analysis
   - Response strategy development (defensive/offensive)
   - Threat monitoring and escalation
   - **Skill-aware**: Reads `competitive-intelligence/SKILL.md`

### 3 Comprehensive Skills

1. **competitive-intelligence** (30KB, 830+ lines)
   - Legal and ethical boundaries for intelligence gathering
   - Information triangulation methodology (3+ sources)
   - Porter's Five Forces framework
   - Competitive profile matrices
   - SWOT analysis patterns
   - Win/loss analysis techniques
   - Signal detection for predicting competitor moves
   - Monitoring cadence and red flags

2. **feature-comparison** (25KB, 680+ lines)
   - Feature inventory methodology
   - Jobs-to-be-Done comparison approach
   - Tiered analysis (compare features per pricing tier)
   - Feature scoring systems (binary, quality rating, customer satisfaction)
   - Gap analysis framework (deficit, quality, differentiation)
   - Comparison presentation formats (matrices, heatmaps, radar charts)
   - Data collection from docs, trials, reviews, technical analysis
   - Kano model feature classification

3. **pricing-analysis** (28KB, 750+ lines)
   - Pricing model types (per-user, usage-based, tiered, freemium, flat-rate, hybrid)
   - Pricing tier analysis (Good-Better-Best framework)
   - Feature gating strategies
   - Price positioning (premium, parity, value, freemium)
   - TCO calculation beyond list prices
   - Price-per-feature value analysis
   - Pricing psychology tactics (charm pricing, anchoring, decoys)
   - Recommendation frameworks for price changes

### 3 Professional Templates

1. **competitor-profile.md** (2,200+ lines)
   - Complete competitor intelligence template
   - Company overview, product analysis, pricing
   - Strengths, weaknesses, recent activity
   - Win/loss intelligence, customer sentiment
   - Threat assessment, response strategy
   - Monitoring plan with data sources

2. **feature-comparison-matrix.xlsx** (Template guide)
   - 5-sheet Excel structure
   - Feature comparison with color coding
   - Scoring matrix with weighted calculations
   - Gap analysis (missing, ahead, quality gaps)
   - Recommendations by priority
   - Tier comparison

3. **competitive-landscape.md** (1,800+ lines)
   - Market size and growth analysis
   - Competitive structure by market share
   - Porter's Five Forces analysis
   - Competitive positioning maps (3 dimensions)
   - Strategic groups analysis
   - Threat assessment and opportunities
   - Strategic recommendations

## Key Features

✓ **Real-Time Intelligence**: WebSearch integration for current competitive data
✓ **Legal & Ethical**: All intelligence from publicly available sources
✓ **Triangulated Data**: 3+ source validation for key claims
✓ **Professional Output**: Excel, Markdown reports following skill patterns
✓ **Threat Scoring**: Quantitative framework (Probability × Impact × Vulnerability)
✓ **Gap Prioritization**: P0/P1/P2/P3 framework for feature gaps
✓ **TCO Analysis**: Beyond list pricing to total cost
✓ **Strategic Frameworks**: Porter's Five Forces, SWOT, perceptual mapping
✓ **Skill-Aware**: All agents read skills for consistent quality

## Design Process

Designed with @ultimate-subagent-creator following expert patterns:
- **WebSearch integration**: All monitoring agents use real-time search
- **Skill-first approach**: All agents read relevant skills before starting
- **Single responsibility**: Each agent focuses on one intelligence aspect
- **Sonnet model**: Competitive analysis requires strategic judgment
- **Tool minimization**: Appropriate permissions for each task
- **Ethical boundaries**: All intelligence from legal, public sources

## Workflows

### Complete Competitive Analysis

```bash
# 1. Monitor competitors for recent activity
@competitor-monitor "Monitor top 5 competitors: CompA, CompB, CompC, CompD, CompE
Focus on product launches, pricing, funding, strategic moves in last 30 days"

# 2. Compare features systematically
@feature-comparator "Create feature comparison matrix for our product vs. 4 competitors
Categories: Core features, Integrations, Security, Advanced features
Include gap analysis with P0/P1/P2 priorities"

# 3. Analyze pricing strategies
@pricing-analyzer "Analyze pricing for top 5 competitors
Compare all tiers, calculate TCO, identify our positioning
Provide pricing recommendations"

# 4. Assess competitive threats
@threat-assessor "Assess threats from all competitors
Score using Probability × Impact × Vulnerability
Provide defensive and offensive response strategies"
```

### Quick Competitor Check

```bash
# Weekly monitoring
@competitor-monitor "Quick check on CompetitorX for the past week
Any product updates, pricing changes, or strategic moves?"
```

### Feature Gap Analysis

```bash
# When losing deals
@feature-comparator "Analyze feature gaps vs. CompetitorY
We lost 3 enterprise deals to them this month
Focus on enterprise features (SSO, SAML, advanced security)"
```

### Pricing Strategy

```bash
# Before pricing changes
@pricing-analyzer "We're considering raising Pro tier from $99 to $119/mo
Analyze competitor pricing in this tier, calculate our new positioning
Assess risk and recommend approach"
```

### Threat Response

```bash
# When competitor makes move
@threat-assessor "CompetitorZ just raised $50M Series B
Announced plans to expand to enterprise segment
Assess threat level and recommend our response"
```

## Use Cases

### Use Case 1: New Competitor Entry

**Scenario**: New well-funded competitor enters market

**Workflow**:
1. **@competitor-monitor**: Gather initial intelligence (product, pricing, team, funding)
2. **@feature-comparator**: Compare features vs. our product
3. **@pricing-analyzer**: Analyze their pricing strategy
4. **@threat-assessor**: Assess threat level, develop response

**Output**: Complete competitor profile, threat assessment, response strategy

### Use Case 2: Losing Deals

**Scenario**: Lost 5 enterprise deals to same competitor

**Workflow**:
1. **@feature-comparator**: Identify feature gaps mentioned in losses
2. **@pricing-analyzer**: Compare pricing (are we overpriced?)
3. **@threat-assessor**: Assess threat to enterprise segment
4. **Internal**: Prioritize gaps, adjust strategy

**Output**: Gap analysis with P0 priorities, pricing recommendations, response plan

### Use Case 3: Pricing Strategy

**Scenario**: Considering price increase

**Workflow**:
1. **@pricing-analyzer**: Full competitive pricing analysis
2. **@feature-comparator**: Calculate our price-per-feature value
3. **@threat-assessor**: Assess risk of customer churn

**Output**: Pricing recommendations with risk assessment

### Use Case 4: Market Expansion

**Scenario**: Considering new market segment

**Workflow**:
1. **@competitor-monitor**: Identify competitors in that segment
2. **@feature-comparator**: Compare feature requirements vs. our product
3. **@pricing-analyzer**: Analyze pricing expectations in segment
4. **@threat-assessor**: Assess competitive intensity

**Output**: Go/no-go recommendation with gap analysis

## Issue Requirements Met

✅ **Role**: Competitor monitoring and analysis specialist
✅ **Competitor monitoring**: Real-time with WebSearch integration
✅ **Feature comparison analysis**: Comprehensive matrices with gap analysis
✅ **Pricing intelligence**: Detailed pricing strategy analysis
✅ **Market positioning analysis**: Positioning maps, strategic groups
✅ **Threat assessment**: Quantitative scoring framework
✅ **Tools Required**:
  - ✅ Web scraping: WebSearch for all monitoring agents
  - ✅ Monitoring tools: Systematic intelligence gathering
  - ✅ Analysis: Professional reports with Excel, Markdown

## Testing

Plugin structure verified:
- 4 agents with proper tools and models
- All agents skill-aware with mandatory skill reading
- 3 comprehensive skills (83KB total)
- 3 professional templates
- Complete README with workflows

## Best Practices

### Intelligence Gathering
- **Always triangulate**: 3+ sources for key claims
- **Document sources**: Include URLs for verification
- **Stay legal**: Only publicly available information
- **Update regularly**: Intelligence ages quickly (30-90 days)
- **Focus on strategic**: Insights that drive decisions, not data for data's sake

### Threat Assessment
- **Quantify risk**: Use Probability × Impact × Vulnerability formula
- **Time-bound**: Immediate/Short/Medium/Long horizons
- **Actionable**: Every threat needs response strategy
- **Monitor continuously**: Set up early warning indicators

### Feature Comparison
- **Weight strategically**: Not all features matter equally
- **Customer-focused**: Compare based on customer impact
- **Quality matters**: Implementation quality, not just availability
- **Prioritize gaps**: P0 (critical) vs. P3 (nice-to-have)

### Pricing Analysis
- **Total cost**: TCO beyond list prices
- **Segment appropriately**: Enterprise vs. SMB pricing differs
- **Track changes**: Pricing evolution reveals strategy
- **Value comparison**: Price-per-feature, customer satisfaction

## Monitoring Cadence

- **Daily**: Google Alerts, news feeds
- **Weekly**: Pricing pages, feature releases, blog posts
- **Monthly**: Win/loss patterns, review sentiment, market share
- **Quarterly**: Full threat assessment, battlecard refresh, landscape analysis

## Ethical Guidelines

**DO**:
- ✅ Use official websites, pricing pages
- ✅ Sign up for legitimate trials
- ✅ Read public news, reviews, social media
- ✅ Analyze publicly available data
- ✅ Triangulate with multiple sources

**DON'T**:
- ❌ Misrepresent identity to gather information
- ❌ Hack or unauthorized access
- ❌ Bribe employees for secrets
- ❌ Industrial espionage
- ❌ Violate NDAs or confidentiality

**Remember**: If you question legality, don't do it.

## Data Sources

All intelligence from publicly available sources:
- Official company websites
- Pricing pages
- Product documentation
- Press releases
- News articles
- Customer reviews (G2, Capterra, TrustRadius)
- Social media
- Job postings
- Conference presentations
- Regulatory filings
- WebSearch results

## Next Steps

1. **Set up monitoring**: Configure Google Alerts for competitors
2. **Initial analysis**: Run @competitor-monitor on top 5 competitors
3. **Feature audit**: Use @feature-comparator for comprehensive gap analysis
4. **Pricing review**: @pricing-analyzer for current market positioning
5. **Threat assessment**: @threat-assessor for strategic planning
6. **Regular updates**: Establish quarterly review cadence

---

**Plugin Version**: 1.0.0
**Last Updated**: 2025-01-21
**Designed with**: @ultimate-subagent-creator expert patterns
**Model**: Sonnet (all agents require strategic judgment)
**WebSearch**: Enabled for all monitoring and analysis agents
