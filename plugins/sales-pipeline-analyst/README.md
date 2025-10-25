# Sales Pipeline Analyst Plugin

A comprehensive sales pipeline analysis system for monitoring pipeline health, identifying deal risks, building accurate forecasts, conducting win/loss analysis, and tracking sales performance metrics.

## Overview

The Sales Pipeline Analyst plugin provides data-driven insights that help sales leaders make informed decisions, identify risks early, improve forecast accuracy, and optimize sales team performance.

**Key Capabilities**:
- 📊 **Pipeline Health Monitoring**: Coverage ratios, velocity tracking, conversion rates, aging analysis
- 🚨 **Deal Risk Identification**: Proactive risk scoring, pattern recognition, mitigation playbooks
- 🔮 **Forecasting Models**: Stage-based, MEDDIC-enhanced, and AI/ML forecasting with accuracy tracking
- 🎯 **Win/Loss Analysis**: Competitive intelligence, pattern recognition, ICP refinement
- 📈 **Performance Metrics**: Rep performance, team metrics, trend analysis, coaching insights

---

## Installation

### Prerequisites

- Claude Code CLI
- Sonnet model access (required for analytical depth)
- CRM data export capability (CSV or JSON)

### Install Plugin

```bash
# Clone or copy the plugin to your plugins directory
cp -r plugins/sales-pipeline-analyst ~/.claude/plugins/

# Verify installation
ls ~/.claude/plugins/sales-pipeline-analyst
```

---

## Quick Start

### 1. Weekly Pipeline Health Check

```
@sales-pipeline-analyst Run weekly pipeline health check
```

The agent will:
- Read CRM data from your export
- Calculate coverage ratios, velocity, conversion rates
- Identify aging deals and quality issues
- Integrate qualification data from sales-lead-qualifier
- Generate comprehensive health report

**Output**: `pipeline-data/health-reports/YYYY-MM-DD-weekly-health.md`

### 2. Deal Risk Assessment

```
@sales-pipeline-analyst Assess risk for Acme Corp deal
```

The agent will:
- Locate deal data in CRM or deal folder
- Read qualification, proposal, and technical engagement data
- Calculate quantitative and qualitative risk scores
- Identify risk category and mitigation actions

**Output**: `pipeline-data/risk-assessments/acme-corp-risk-assessment.md`

### 3. Generate Sales Forecast

```
@sales-pipeline-analyst Generate Q1 2025 forecast
```

The agent will:
- Collect all pipeline data for Q1 close dates
- Apply stage-based probabilities
- Enhance with MEDDIC/BANT scores
- Categorize deals (Commit/Best Case/Pipeline/Omitted)
- Calculate weighted forecast with deal-by-deal breakdown

**Output**: `pipeline-data/forecasts/2025-Q1-forecast.md`

### 4. Win/Loss Analysis

```
@sales-pipeline-analyst Analyze Q4 2024 wins and losses
```

The agent will:
- Identify all closed-won and closed-lost deals in Q4
- Read qualification, proposal, and technical data
- Identify win/loss reasons and patterns
- Conduct competitive analysis
- Extract lessons learned

**Output**: `pipeline-data/win-loss/2024-Q4-win-loss-summary.md`

### 5. Rep Performance Review

```
@sales-pipeline-analyst Performance review for John Doe (Q1 2025)
```

The agent will:
- Collect all deals owned by John Doe in Q1
- Calculate quota attainment, pipeline generation, win rate
- Analyze deal size and sales cycle
- Compare to team averages
- Generate coaching insights

**Output**: `pipeline-data/performance/john-doe-Q1-2025.md`

---

## Plugin Structure

```
plugins/sales-pipeline-analyst/
├── plugin.json                             # Plugin metadata
├── README.md                               # This file
│
├── agents/
│   └── sales-pipeline-analyst.md           # Main agent (skill-aware)
│
├── skills/
│   └── pipeline-analysis/
│       └── SKILL.md                        # Comprehensive skill (8 sections)
│
└── templates/
    ├── pipeline-health-report.md           # Weekly health report template
    ├── forecast-report.md                  # Forecast template
    ├── deal-risk-assessment.md             # Risk assessment template
    ├── win-loss-analysis.md                # Win/loss template
    └── performance-dashboard.md            # Executive dashboard template
```

---

## Features

### 1. Pipeline Health Monitoring

**Metrics Tracked**:
- Pipeline coverage ratio (by stage and overall)
- Pipeline velocity (average days per stage)
- Stage conversion rates
- Deal aging analysis (on track / aging / stale / dead)
- Quality indicators (MEDDIC scores, EB engagement, champion status)

**Health Scoring**:
- Composite health score (0-100) based on coverage, velocity, conversion, quality
- Green/Yellow/Red status indicators
- Trend analysis vs. previous periods

**Example Use Case**:
```
@sales-pipeline-analyst Run weekly health check

Result:
- Health Score: 76/100 (GOOD - Yellow)
- Coverage: 3.2x (below 3.5x target)
- Velocity: Slowing by 12%
- At-Risk Deals: 8 deals, $1.2M
- Recommended Actions: Pipeline generation sprint, disqualify 3 stale deals
```

### 2. Deal Risk Identification

**Risk Scoring Framework**:
- Quantitative signals (50 points): MEDDIC score, aging, momentum, budget
- Qualitative signals (50 points): EB engagement, champion, competition, decision process
- Risk categories: Low / Medium / High / Critical

**Common Risk Patterns**:
- No Economic Buyer access (35% win rate drop)
- Decision date keeps slipping (50% less likely to close)
- No champion identified (40% win rate drop)
- Poor MEDDIC scores (<60)
- Long silence periods (>14 days)
- Procurement/legal delays

**Example Use Case**:
```
@sales-pipeline-analyst Assess risk for deal OPP-12345

Result:
- Risk Level: HIGH (72/100)
- MEDDIC: 58 (weak qualification)
- 14 days silence after proposal
- No EB engagement
- Recommended Action: Get EB meeting or disqualify
- Historical Pattern: Similar deals have 25% win rate
```

### 3. Forecasting Models

**Forecast Categories**:
- **Commit** (90-100%): Verbal commit, contract in legal, MEDDIC >85
- **Best Case** (70-89%): Strong MEDDIC (70-85), EB engaged, proposal delivered
- **Pipeline** (30-69%): Qualified (MEDDIC 50-70), active engagement
- **Omitted** (<30%): Weak qualification, stale, unresponsive

**Calculation Methods**:
- Stage-based probability
- MEDDIC/BANT-enhanced forecasting
- Historical accuracy tracking
- Slippage and push analysis

**Example Use Case**:
```
@sales-pipeline-analyst Generate Q1 forecast

Result:
- Commit: $800K (90% accuracy expected)
- Best Case: $1.2M (70% accuracy expected)
- Total: $2.0M (80% of $2.5M quota)
- Gap: $500K (need 3 Best Case deals to move to Commit)
- Top Risks: 2 deals at risk of slipping
```

### 4. Win/Loss Analysis

**Analysis Framework**:
- Win reasons (product fit, value/ROI, relationship, services, pricing)
- Loss reasons (competitor, no decision, price, timing, product gaps)
- Competitive intelligence (who we beat, who beats us)
- Pattern recognition (ICP refinement)

**Outputs**:
- Detailed post-mortem reports
- Lessons learned extraction
- Replicability analysis (can we repeat wins? avoid losses?)
- Battlecard updates

**Example Use Case**:
```
@sales-pipeline-analyst Analyze deal OPP-54321 (WON)

Result:
- Primary Win Reason: Product Fit (60%)
  - Only vendor with real-time predictive maintenance
- Secondary: Value/ROI (30%)
  - 14-month payback vs. competitor's 24 months
- Key Success: Early champion, customized demo, strong ROI
- Replicable: Yes - manufacturing vertical, ROI-led approach
```

### 5. Performance Metrics Tracking

**Individual Rep Metrics**:
- Quota attainment (monthly, quarterly, annual)
- Pipeline generation (new pipeline added)
- Win rate (by stage, by segment)
- Average deal size and sales cycle length
- Activity metrics (calls, meetings, proposals)

**Team Metrics**:
- Overall quota attainment
- Pipeline coverage ratio
- Forecast accuracy (commit vs. actual)
- Revenue by product, segment, region

**Coaching Insights**:
- Performance tiers (top / core / struggling)
- Gap diagnosis (qualification, closing, prospecting)
- Best practices from top performers

**Example Use Case**:
```
@sales-pipeline-analyst Performance review for Rep C (Q1 2025)

Result:
- Quota Attainment: 78% (below 100% target)
- Win Rate: 22% (vs. 28% team average)
- Sales Cycle: 95 days (vs. 75 day target)
- Root Cause: Poor qualification (MEDDIC avg: 52)
- Coaching Focus: MEDDIC training, disqualification discipline
- Goal: MEDDIC 70+ on all new opps, 90% attainment in Q2
```

---

## Integration with Sales Plugins

### With `sales-lead-qualifier`

**Data Flow**: Qualification → Pipeline Analysis

The pipeline analyst reads qualification scores to:
- Assess deal risk (low MEDDIC = high risk)
- Adjust forecast probability
- Evaluate pipeline quality
- Provide coaching recommendations

**Example**:
```json
{
  "company": "Acme Corp",
  "meddic_score": 68,
  "priority": "P2"
}

Pipeline Analysis:
- Risk: MEDIUM (MEDDIC 60-70 range)
- Forecast: Best Case (65% probability)
- Action: Improve EB engagement to move to Commit
```

### With `sales-proposal-writer`

**Data Flow**: Proposal Sent → Pipeline Analysis

The pipeline analyst monitors:
- Days since proposal sent (if >14 days, flag as at-risk)
- Proposal version count (multiple versions = negotiation)
- Pricing changes (discounting patterns)

**Example**:
```json
{
  "company": "Beta Industries",
  "sent_date": "2025-01-12",
  "discount_pct": 12,
  "responded": false
}

Pipeline Analysis:
- Risk: MEDIUM (14 days silence + 12% discount)
- Action: Follow-up call to address objections
- Pattern: Discount + silence = 60% loss rate
```

### With `sales-engineer`

**Data Flow**: Technical Engagement → Pipeline Analysis

The pipeline analyst tracks:
- POC/demo completion
- Technical documentation delivered
- ROI analysis acceptance

**Example**:
```json
{
  "company": "Gamma Healthcare",
  "demo_completed": true,
  "roi_delivered": true,
  "poc_status": "completed"
}

Pipeline Analysis:
- Risk: LOW (strong technical engagement)
- Forecast: Best Case (75% probability)
- Pattern: POC + positive ROI = 82% win rate
```

---

## Report Templates

### 1. Pipeline Health Report
**Purpose**: Weekly or bi-weekly deep dive into pipeline quality and coverage
**Sections**: Overview, stage breakdown, quality assessment, aging, velocity, risks
**Audience**: Sales managers, sales leadership

### 2. Forecast Report
**Purpose**: Weekly or monthly sales forecast with commit/best case/pipeline breakdown
**Sections**: Forecast vs. quota, deal-by-deal breakdown, changes from last forecast, path to quota
**Audience**: Sales leadership, finance, exec team

### 3. Deal Risk Assessment
**Purpose**: On-demand risk analysis for individual deals
**Sections**: Risk score breakdown, historical context, integration data, recommended actions
**Audience**: Sales reps, sales managers

### 4. Win/Loss Analysis
**Purpose**: Post-mortem analysis of closed deals
**Sections**: Win/loss reasons, competitive situation, key factors, lessons learned
**Audience**: Sales team, product, marketing

### 5. Performance Dashboard
**Purpose**: Executive-level snapshot of sales performance
**Sections**: Quota attainment, pipeline health, top risks, key metrics, rep performance
**Audience**: Sales leadership, exec team

---

## Data Requirements

### CRM Data Export

**Required Fields**:
- Deal ID
- Company Name
- Deal Amount (ACV)
- Stage
- Created Date
- Expected Close Date
- Owner (Sales Rep)
- Source (Inbound, Outbound, etc.)
- Industry
- Company Size

**Optional but Recommended**:
- MEDDIC/BANT scores
- Competitor (if known)
- Win/Loss reason (when closed)
- Engagement metrics (meetings, emails)

**Export Formats Supported**:
- CSV (standard format)
- JSON (preferred for integration)

### Integration Data Locations

**Qualification Data**: `./leads/{client-name}-qualification.json`
**Proposal Data**: `./proposals/{client-name}/`
**Technical Engagement**: `./technical-docs/{client-name}-*`, `./demos/{client-name}-*`

---

## Best Practices

### DO ✅

1. **Run Weekly Health Checks**
   - Consistent monitoring catches issues early
   - Recommended: Every Monday morning

2. **Assess High-Value Deals**
   - Run risk assessments on all deals >$50K
   - Re-assess monthly or when stage changes

3. **Track Forecast Accuracy**
   - Compare forecasts to actuals
   - Identify and coach reps with poor accuracy

4. **Conduct Win/Loss Reviews**
   - Review all deals >$50K within 7 days of close
   - Extract lessons and update playbooks

5. **Use Integration Data**
   - Leverage qualification, proposal, and technical data
   - Richer data = better insights

6. **Act on Insights**
   - Analysis is worthless without action
   - Assign owners and due dates to recommendations

### DON'T ❌

1. **Don't Skip Data Quality Checks**
   - Garbage in = garbage out
   - Verify completeness and accuracy

2. **Don't Ignore Early Warning Signs**
   - Stale deals, poor MEDDIC, no EB access
   - Address or disqualify quickly

3. **Don't Overforecast**
   - Optimism bias kills forecast accuracy
   - Respect qualification scores

4. **Don't Analyze in Isolation**
   - Use integration data from other sales plugins
   - Context is critical

5. **Don't Create Reports and Forget Them**
   - Follow up on action items
   - Track progress on recommendations

6. **Don't Focus Only on Lagging Indicators**
   - Balance closed revenue with pipeline health
   - Leading indicators predict future performance

---

## Advanced Usage

### Custom Analysis Requests

The agent can handle custom analysis requests:

```
@sales-pipeline-analyst Compare Q1 2025 pipeline to Q1 2024 - what changed?

@sales-pipeline-analyst Analyze why our win rate dropped from 32% to 24% this quarter

@sales-pipeline-analyst Which deals should we focus on this week to hit quota?

@sales-pipeline-analyst Create a quarterly business review deck with key metrics
```

### Scenario Analysis

Test "what if" scenarios:

```
@sales-pipeline-analyst If we close 3 of the top 5 Best Case deals, do we hit quota?

@sales-pipeline-analyst What's our forecast if we lose the top 2 at-risk deals?

@sales-pipeline-analyst How much pipeline do we need to generate to hit 120% of quota?
```

### Competitive Analysis

Deep dive on competitors:

```
@sales-pipeline-analyst Analyze our win/loss record vs. Competitor X over the last 6 months

@sales-pipeline-analyst When do we win vs. Competitor Y? What's our advantage?

@sales-pipeline-analyst Update the battlecard for Competitor Z based on recent deals
```

---

## Troubleshooting

### Issue: "No CRM data found"

**Solution**: Export CRM data to CSV or JSON and place in accessible location. Tell the agent where to find it:
```
@sales-pipeline-analyst Run health check on CRM data at ./crm-export-2025-01-19.csv
```

### Issue: "MEDDIC scores missing"

**Solution**: The agent will still analyze but with limited accuracy. Either:
- Add MEDDIC scores to CRM export, or
- Use sales-lead-qualifier to generate qualification data first

### Issue: "Forecast accuracy is low (<80%)"

**Root Causes**:
- Overforecasting (reps too optimistic)
- Weak qualification (advancing unqualified deals)
- Poor MEDDIC/BANT data

**Solutions**:
- Coach reps on realistic forecasting
- Strengthen qualification process
- Use MEDDIC-enhanced forecasting

### Issue: "Risk assessments too conservative"

**Solution**: The agent uses battle-tested benchmarks. If your business is different:
- Provide historical win rate data
- Adjust MEDDIC thresholds in skill
- Calibrate risk scoring to your reality

---

## Customization

### Modify Risk Scoring

Edit `skills/pipeline-analysis/SKILL.md` Section 2.2 to adjust risk point allocations:

```markdown
**1. MEDDIC/BANT Score (20 points)**:
- MEDDIC >80: 0 points (low risk)
- MEDDIC 60-80: 10 points (medium risk)
- MEDDIC 40-60: 15 points (high risk)
- MEDDIC <40: 20 points (critical risk)
```

Change thresholds based on your data.

### Adjust Forecast Categories

Edit Section 3.1 to change probability ranges:

```markdown
**COMMIT** (90-100% confidence):
- Criteria: Verbal commit, contract in legal, MEDDIC >85
```

Modify MEDDIC threshold or add custom criteria.

### Add Custom Metrics

Edit Section 5.1 to track additional metrics:

```markdown
**7. Custom Metric**:
- Formula: [Your formula]
- Target: [Your target]
- Track: [Frequency]
```

---

## Performance Characteristics

**Speed**:
- Health check: 30-45 seconds
- Risk assessment: 15-20 seconds per deal
- Forecast generation: 45-60 seconds
- Win/loss analysis: 20-30 seconds per deal

**Token Usage**:
- Health check: 12K-15K tokens
- Risk assessment: 5K-8K tokens per deal
- Forecast: 15K-20K tokens
- Win/loss: 8K-12K tokens per deal

**Cost** (using Sonnet):
- Health check: ~$0.25
- Risk assessment: ~$0.10 per deal
- Forecast: ~$0.30
- Win/loss: ~$0.15 per deal

**ROI**: Highly cost-effective for sales teams. Catching one at-risk $100K deal pays for thousands of analyses.

---

## Model Requirements

**Required Model**: Sonnet (claude-sonnet-4-5)

**Why Sonnet** (not Haiku):
- Pipeline analysis requires judgment and nuanced interpretation
- Pattern recognition across multiple data sources
- Risk assessment with subtle signal detection
- Forecasting with statistical reasoning
- Executive-level communication

Haiku may be added in the future for simple metric calculations.

---

## Contributing

### Report Issues

Found a bug or have a feature request?
- Open an issue in the plugin repository
- Include sample data (anonymized) if possible

### Suggest Improvements

Have ideas for better analysis?
- What additional metrics would be valuable?
- What reports or templates are missing?
- What integrations would help?

### Share Learnings

If you customize the plugin:
- Share modifications that improved accuracy
- Contribute industry-specific benchmarks
- Submit win/loss patterns for your vertical

---

## Version History

**v1.0.0** (2025-01-19):
- Initial release
- 5 core capabilities: health monitoring, risk identification, forecasting, win/loss, performance
- 8-section comprehensive skill
- 5 professional report templates
- Integration with sales-lead-qualifier, sales-proposal-writer, sales-engineer

---

## Support

**Documentation**: This README and inline skill documentation

**Examples**: See Quick Start section for common use cases

**Questions**: Contact plugin maintainer or open an issue

---

## License

[Your license here]

---

## Credits

**Based on**: Battle-tested patterns from 1000+ B2B deals across SaaS, Mid-Market, and Enterprise segments

**Frameworks**: BANT, MEDDIC, standard B2B sales methodologies

**Integrates with**: sales-lead-qualifier, sales-proposal-writer, sales-engineer plugins

---

**Plugin Version**: 1.0.0
**Last Updated**: 2025-01-19
**Maintained by**: Puerto Marketplace
