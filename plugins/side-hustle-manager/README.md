# Side Hustle Manager Plugin

Professional side business income and growth tracking specialist with revenue analysis, expense tracking, and comprehensive business reporting.

## Overview

The Side Hustle Manager Plugin transforms how you track and optimize your side business by providing intelligent revenue analysis, tax-optimized expense tracking, and strategic business insights. Instead of spreadsheets and guesswork, get data-driven recommendations for maximizing profitability and sustainable growth.

## What's Included

### 3 Specialized Agents

#### 1. revenue-analyzer (Sonnet)

A revenue tracking and growth analysis specialist that:
- **Tracks income by stream** - Categorize revenue by consulting, freelance, products, etc.
- **Calculates hourly rates** - True profitability through time investment analysis
- **Analyzes growth trends** - Month-over-month, quarter-over-quarter tracking
- **Compares stream performance** - Identify your most profitable revenue sources
- **Forecasts revenue** - Project future income based on historical trends
- **Provides actionable insights** - Data-driven recommendations for income optimization

**Activation**: Use `@revenue-analyzer` or let it activate automatically when tracking revenue.

#### 2. expense-tracker (Haiku)

An expense categorization specialist focused on tax optimization:
- **Records business expenses** - Track all deductible costs
- **Categorizes for taxes** - Uses IRS Schedule C categories
- **Identifies deductions** - Maximize legitimate business deductions
- **Calculates profit margins** - Net profit after all expenses
- **Tracks receipts** - Documentation for audit protection
- **Generates quarterly summaries** - Tax-ready expense reports

**Activation**: Use `@expense-tracker` or let it activate automatically when logging expenses.

#### 3. business-reporter (Sonnet)

A comprehensive business reporting specialist that:
- **Creates quarterly reviews** - Professional QBR reports
- **Generates growth dashboards** - Visual metrics and trends
- **Tracks KPIs** - Monitor critical business indicators
- **Analyzes business health** - Graded assessment with recommendations
- **Compares periods** - Historical perspective and trends
- **Sets strategic goals** - Data-driven targets for next quarter

**Activation**: Use `@business-reporter` or let it activate automatically for quarterly reviews.

### 1 Comprehensive Skill: side-hustle-analytics

Expert patterns library covering:
- **Revenue analysis strategies** - Stream optimization, growth metrics, forecasting
- **Tax deduction tactics** - IRS categories, documentation, optimization
- **Profitability calculations** - Hourly rates, margins, break-even analysis
- **Business health metrics** - KPI tracking, health scoring, risk assessment
- **Growth strategies** - From $0 to $25K+/month roadmaps
- **Strategic recommendations** - Data-driven insights for scaling

All agents read this skill automatically for expert guidance.

### 3 Professional Templates

#### 1. revenue_tracking.json

Complete revenue tracking structure with:
- Revenue stream categorization
- Transaction logging with time tracking
- Client relationship tracking
- KPI targets and benchmarks
- Usage instructions and best practices

#### 2. expense_categories.json

Tax-optimized expense tracking with:
- IRS Schedule C categories
- Deductibility percentages and limits
- Monthly/annual budgets by category
- Receipt requirements and documentation
- Audit protection guidelines

#### 3. quarterly_business_review.md

Professional QBR template including:
- Executive summary dashboard
- Revenue and expense analysis
- Profitability metrics
- Client analysis
- Business health assessment
- Strategic recommendations
- Action plans and goals

## Features

### Revenue Tracking & Analysis

**Track Every Dollar**:
```bash
@revenue-analyzer "Record $1,250 from Acme Corp for consulting on 2025-01-20"
```

The agent:
- Records transaction with stream, client, date
- Calculates running totals
- Updates monthly progress
- Provides insights on performance

**Analyze Growth**:
```bash
@revenue-analyzer "Show monthly growth trends"
```

Get comprehensive analysis:
- Period-over-period growth rates
- Revenue by stream breakdown
- Trend detection (growing/declining/stable)
- Forecasts for upcoming periods

**Calculate True Profitability**:
```bash
@revenue-analyzer "What are my hourly rates by stream?"
```

Reveals:
- Effective hourly rate by revenue stream
- Which work pays best per hour
- Where to focus time for maximum profit
- Pricing optimization recommendations

**Compare Streams**:
```bash
@revenue-analyzer "Which revenue stream is performing best?"
```

Analysis includes:
- Revenue share by stream
- Transaction counts and averages
- Client concentration
- Diversification assessment

### Expense Tracking & Tax Optimization

**Log Expenses Immediately**:
```bash
@expense-tracker "Record $49.99 for Adobe subscription in Software category"
```

The agent:
- Categorizes using IRS tax categories
- Calculates deductible amount (50% for meals, 100% for most)
- Tracks receipt status
- Provides tax savings estimate

**Analyze by Category**:
```bash
@expense-tracker "Show expense breakdown by category this quarter"
```

Get detailed view:
- Expenses by IRS category
- Deductible amounts
- Share of total expenses
- Receipt compliance rate

**Calculate Net Profit**:
```bash
@expense-tracker "What's my net profit?"
```

Complete P&L analysis:
- Total revenue vs total expenses
- Net profit and profit margin
- Expense ratio assessment
- Health indicators

**Quarterly Tax Summary**:
```bash
@expense-tracker "Generate Q1 tax summary"
```

Tax-ready report with:
- Deductible expenses by category
- Estimated tax savings
- Receipt documentation status
- Next steps for tax filing

### Business Reporting & Strategic Planning

**Generate Quarterly Review**:
```bash
@business-reporter "Generate Q1 2025 quarterly business review"
```

Comprehensive QBR including:
- Executive summary with key metrics
- Revenue breakdown by stream
- Expense analysis by category
- Top clients and concentration risk
- Business health score (0-100)
- Strategic recommendations
- Next quarter goals

**Growth Dashboard**:
```bash
@business-reporter "Show growth metrics dashboard"
```

12-month dashboard with:
- Monthly revenue/expense/profit trends
- Growth rates and trend detection
- Visual text-based charts
- Key metrics summary
- 3-month projection

**Track Goals**:
```bash
@business-reporter "How am I tracking against annual goals?"
```

Goal tracking includes:
- Progress vs annual targets
- Pacing analysis (ahead/behind)
- Quarterly breakdown
- Recommendations to hit goals

## Installation

```bash
/plugin install side-hustle-manager@puerto
```

After installation, restart Claude Code to activate the agents and skill.

## Quick Start

### Step 1: Initialize Your Business Data

Create your business directory structure:

```bash
mkdir -p .side-hustle
```

Copy templates to start tracking:

```bash
# Revenue tracking
cp ~/.claude/plugins/side-hustle-manager/templates/revenue_tracking.json .side-hustle/

# Expense tracking
cp ~/.claude/plugins/side-hustle-manager/templates/expense_categories.json .side-hustle/
```

### Step 2: Record Your First Revenue

```bash
@revenue-analyzer "Record $1,500 from ClientName for Consulting work on 2025-01-15"
```

### Step 3: Log Your First Expense

```bash
@expense-tracker "Record $49.99 for Zoom subscription in Software category"
```

### Step 4: Generate Your First Report

At end of month/quarter:

```bash
@business-reporter "Generate Q1 2025 quarterly business review"
```

## Usage Examples

### Scenario 1: Freelance Consultant Tracking Weekly Income

**Week 1 - Record Revenue**:
```
@revenue-analyzer "Record $2,500 from TechCorp for website redesign consulting, 15 hours worked on Jan 15"
```

**Week 2 - Log Expenses**:
```
@expense-tracker "Record $99 for Figma subscription in Software category"
@expense-tracker "Record $65 for client lunch meeting in Meals category"
```

**Week 4 - Monthly Check-in**:
```
@revenue-analyzer "Show monthly growth trends"
@expense-tracker "What's my net profit this month?"
```

**Result**:
- Revenue: $8,500 (3 projects)
- Expenses: $1,247
- Net Profit: $7,253 (85% margin)
- Hourly Rate: $142/hr
- Insight: "Consulting stream 2x more profitable than freelance projects"

### Scenario 2: Product Creator Analyzing Multiple Streams

**Revenue Streams**:
- Digital product sales: $3,200
- Consulting: $4,500
- Affiliate income: $850
- Course sales: $1,200

**Analysis Request**:
```
@revenue-analyzer "Compare revenue streams - which should I focus on?"
```

**Insights Provided**:
- Consulting has highest hourly rate ($150/hr)
- Products have best margins (85% vs 65% consulting)
- Affiliate is passive but small (9% of revenue)
- Recommendation: "Allocate 60% time to consulting, 30% to product development, 10% to affiliate partnerships"

### Scenario 3: Quarter-End Business Review

**Request**:
```
@business-reporter "Generate comprehensive Q1 2025 review"
```

**Report Includes**:
- Total Revenue: $28,450 (+18% vs Q4)
- Net Profit: $19,115 (67% margin)
- Top Client: TechCorp (32% of revenue) ⚠️ Concentration risk
- Best Stream: Products (85% margin)
- Health Score: 78/100 (Good)
- Key Recommendation: "Diversify clients - top client represents >50% revenue"
- Q2 Goals: $32,000 revenue (+12%), add 3 new clients, launch second product

### Scenario 4: Tax Preparation (Year-End)

**Quarterly Summaries**:
```
@expense-tracker "Generate Q4 tax summary"
```

**Output**:
- Total Deductible Expenses: $14,827
- Top Categories:
  - Software & Subscriptions: $2,400
  - Home Office: $3,600
  - Professional Services: $2,100
  - Marketing: $1,800
- Estimated Tax Savings (30% rate): $4,448
- Receipt Compliance: 94% ✓

**Year-End Actions**:
- Export all quarterly summaries for accountant
- Organize receipts by category
- Review for missed deductions
- Plan estimated tax payments

## File Structure

```
side-hustle-manager/
├── .claude-plugin/
│   └── plugin.json                     # Plugin metadata
├── agents/
│   ├── revenue-analyzer.md             # Revenue tracking & analysis (Sonnet)
│   ├── expense-tracker.md              # Expense categorization (Haiku)
│   └── business-reporter.md            # Quarterly reviews (Sonnet)
├── skills/
│   └── side-hustle-analytics/
│       └── SKILL.md                    # Comprehensive analytics patterns
├── templates/
│   ├── revenue_tracking.json           # Revenue tracking structure
│   ├── expense_categories.json         # IRS tax categories template
│   └── quarterly_business_review.md    # QBR template
└── README.md                           # This file
```

## Your Business Data Structure

Once you start using the plugin, your data lives in `.side-hustle/`:

```
.side-hustle/
├── revenue_tracking.json               # All revenue transactions
├── expense_tracking.json               # All business expenses
├── client_database.json                # Client information (optional)
├── project_pipeline.json               # Sales pipeline (optional)
└── qbr_Q1_2025_20250401.txt           # Generated reports
```

## Key Metrics Explained

### Revenue Metrics

**Total Revenue**: Sum of all income across all streams
- Target: Growing 10%+ month-over-month

**Revenue by Stream**: Breakdown by category (consulting, products, etc.)
- Goal: 3+ streams for diversification

**Average Transaction Value**: Total revenue / number of transactions
- Optimize: Increase through pricing or upselling

**Revenue per Client**: Total revenue / unique clients
- Insight: Which clients are most valuable

**Effective Hourly Rate**: Net profit / hours worked
- Target: $75-150+ depending on expertise

### Expense Metrics

**Total Expenses**: All business costs
- Benchmark: <40% of revenue for service businesses

**Expense Ratio**: Total expenses / total revenue × 100
- Healthy: 20-40% for most side hustles

**Deductible Amount**: Sum of tax-deductible expenses
- Maximize: Through proper categorization and documentation

**Receipt Compliance**: % of expenses with receipts tracked
- Target: 100% for expenses >$75, 80%+ overall

### Profitability Metrics

**Net Profit**: Revenue - Expenses
- Goal: Growing faster than revenue

**Profit Margin**: (Net Profit / Revenue) × 100
- Excellent: >40%
- Good: 30-40%
- Needs Work: <20%

**Profit per Transaction**: Net profit / number of transactions
- Optimize: Through pricing and efficiency

**Profit per Hour**: Net profit / hours worked
- Same as effective hourly rate

### Growth Metrics

**Month-over-Month Growth**: (Current month - Previous month) / Previous month × 100
- Strong: >20%
- Good: 10-20%
- Maintain: >0%

**Quarter-over-Quarter Growth**: Same calculation for quarters
- Target: 15%+ per quarter

**Compound Monthly Growth Rate**: Geometric mean of monthly growth
- Sustainable: 10-15%

**Year-over-Year Growth**: Compare same period previous year
- Healthy: 30%+ annually

### Business Health Metrics

**Client Concentration**: % of revenue from top client
- Low Risk: <25%
- Moderate: 25-50%
- High Risk: >50%

**Stream Diversification**: Number of active revenue streams
- Good: 3+ streams
- Risky: Single stream

**Days Cash on Hand**: Cash reserves / average daily expenses
- Healthy: 90+ days
- Minimum: 30 days

**Client Acquisition Cost**: Cost to acquire new client
- Target: <10% of client lifetime value

## Best Practices

### Revenue Tracking

1. **Record immediately** - Don't wait until month-end, log as payments arrive
2. **Be specific with streams** - Use consistent naming (not "misc" or "other")
3. **Track time** - Essential for calculating true hourly rate
4. **Tag clients consistently** - Enables relationship analysis
5. **Review weekly** - Quick check-in to catch issues early
6. **Analyze monthly** - Deep dive into trends and opportunities

### Expense Tracking

1. **Separate business and personal** - Use dedicated business accounts
2. **Log same day** - Don't let receipts pile up
3. **Use correct categories** - Matches IRS Schedule C for easy tax filing
4. **Keep receipts** - Digital photos or scans for all >$75
5. **Document business purpose** - Especially for meals, travel, home office
6. **Review quarterly** - Prepare for estimated taxes
7. **Conservative estimates** - For mixed-use items (phone, internet, vehicle)

### Business Reporting

1. **Review quarterly** - Don't wait for year-end
2. **Compare periods** - Track trends over time
3. **Set specific goals** - Measurable targets for next quarter
4. **Act on insights** - Don't just report, improve
5. **Share with advisors** - Discuss with mentors, accountants
6. **Celebrate wins** - Acknowledge progress and milestones

### Tax Optimization

1. **Quarterly estimated taxes** - Avoid penalties and surprises
2. **Maximize deductions** - Track all legitimate business expenses
3. **Home office deduction** - If you qualify (exclusive use, principal place)
4. **Retirement contributions** - SEP-IRA or Solo 401(k) reduce taxable income
5. **Keep records 7 years** - IRS audit protection
6. **Consult professional** - For complex situations or optimization

## Common Workflows

### Weekly Check-in (15 minutes)

```bash
# Record week's revenue
@revenue-analyzer "Record $X,XXX from [client] for [work] on [date]"

# Log week's expenses
@expense-tracker "Record $XX for [expense] in [category]"

# Quick status check
@revenue-analyzer "What's my revenue this month so far?"
```

### Monthly Review (30 minutes)

```bash
# Growth analysis
@revenue-analyzer "Show monthly growth trends"

# Expense analysis
@expense-tracker "Show expense breakdown by category this month"

# Profit check
@expense-tracker "What's my net profit this month?"

# Hourly rate
@revenue-analyzer "What are my hourly rates by stream?"
```

### Quarterly Business Review (2 hours)

```bash
# Generate comprehensive report
@business-reporter "Generate Q[X] 2025 quarterly business review"

# Review the report and:
# 1. Analyze what's working
# 2. Identify areas for improvement
# 3. Set goals for next quarter
# 4. Create action plan

# Save report for records
# Share with accountant/advisors
```

### Year-End Tax Prep (4 hours)

```bash
# Generate all quarterly summaries
@expense-tracker "Generate Q1 tax summary"
@expense-tracker "Generate Q2 tax summary"
@expense-tracker "Generate Q3 tax summary"
@expense-tracker "Generate Q4 tax summary"

# Full year review
@business-reporter "Show growth metrics dashboard"

# Export data for accountant
# Organize receipts
# Review for missed deductions
# Plan next year's strategy
```

## Troubleshooting

### "No revenue data found"

**Solution**: Initialize revenue tracking file
```bash
cp ~/.claude/plugins/side-hustle-manager/templates/revenue_tracking.json .side-hustle/
```

### "Expense category not recognized"

**Solution**: Use exact IRS Schedule C category names from template:
- Advertising & Marketing
- Office Supplies
- Software & Subscriptions
- Professional Services
- Equipment & Tools
- Education & Training
- Travel & Transportation
- Meals & Entertainment (50%)
- Home Office
- Internet & Phone
- Insurance
- Licenses & Permits
- Bank Fees
- Miscellaneous

### "Can't calculate hourly rate"

**Solution**: Time tracking required
```bash
# When recording revenue, include hours worked:
@revenue-analyzer "Record $1,500 from Client for Project, 12 hours worked"
```

### "Missing receipts warning"

**Solution**: Track receipt status when logging expenses
```bash
@expense-tracker "Record $125 for expense in category, receipt: filename.pdf"
```

## Advanced Features

### Pipeline-Based Forecasting

Track your sales pipeline for better forecasting:

```json
// .side-hustle/project_pipeline.json
{
  "opportunities": [
    {
      "client": "Prospect Corp",
      "value": 5000,
      "probability": 0.7,
      "expected_close": "2025-02-15",
      "stage": "Proposal Sent"
    }
  ]
}
```

### Client Database

Track client relationships and lifetime value:

```json
// .side-hustle/client_database.json
{
  "clients": [
    {
      "name": "TechCorp",
      "first_project": "2024-06-01",
      "total_revenue": 15500,
      "projects": 8,
      "status": "Active",
      "notes": "Monthly retainer client"
    }
  ]
}
```

### Multi-Year Analysis

Compare performance across years:

```bash
@business-reporter "Compare 2025 vs 2024 performance"
```

### Goal Setting & Tracking

Set annual goals and track progress:

```json
// .side-hustle/goals.json
{
  "year": 2025,
  "annual_goals": {
    "revenue": 60000,
    "profit": 24000,
    "new_clients": 15,
    "hourly_rate": 125
  },
  "quarterly_goals": {
    "Q1": {"revenue": 12000, "profit": 5000},
    "Q2": {"revenue": 15000, "profit": 6500},
    "Q3": {"revenue": 16000, "profit": 7000},
    "Q4": {"revenue": 17000, "profit": 5500}
  }
}
```

## Integration with Other Tools

### Accounting Software

Export data to:
- QuickBooks Self-Employed
- Wave Accounting (free)
- FreshBooks
- Xero

### Time Tracking

Sync time data from:
- Toggl Track
- Harvest
- Clockify

### Banking

Import transactions from:
- Business checking account
- Business credit card
- PayPal/Stripe

## Security & Privacy

### Data Storage

- All data stored locally in `.side-hustle/` directory
- JSON format for easy backup and portability
- No cloud sync (your choice)

### Backup Recommendations

```bash
# Regular backups
cp -r .side-hustle/ backups/side-hustle-$(date +%Y%m%d)/

# Cloud backup (optional)
# Upload .side-hustle/ to your preferred cloud storage
```

### Sensitive Information

- Keep receipts with payment info secure
- Don't commit to public repositories
- Add `.side-hustle/` to `.gitignore` if needed

## Support & Community

### Getting Help

1. **Review the skill**: `~/.claude/plugins/side-hustle-manager/skills/side-hustle-analytics/SKILL.md`
2. **Check templates**: See examples in `templates/` directory
3. **Agent documentation**: Read individual agent files for detailed workflows
4. **Ask agents**: `@revenue-analyzer "How do I...?"`

### Feedback & Improvements

This plugin is part of the Puerto marketplace. Contributions and feedback welcome!

### Related Plugins

Consider also:
- **orchestrator**: For complex multi-agent workflows
- **subagent-creator**: For creating custom business-specific agents

## FAQs

**Q: Can I use this for multiple side hustles?**
A: Yes! Create separate directories for each business:
```bash
mkdir -p ~/business1/.side-hustle
mkdir -p ~/business2/.side-hustle
```

**Q: What if I'm not in the US?**
A: Expense categories may differ. Adjust categories in template to match your tax jurisdiction.

**Q: Can I track inventory/COGS?**
A: Yes, add inventory costs to expense tracking. The agents calculate gross vs net profit.

**Q: How often should I review my numbers?**
A:
- Weekly: Quick check (5-10 min)
- Monthly: Growth review (30 min)
- Quarterly: Full business review (2 hours)
- Annually: Year-end analysis and planning (4 hours)

**Q: Is this a replacement for an accountant?**
A: No - it's a tool to track and analyze your business. Still consult a tax professional for filing and optimization.

**Q: Can I export data to Excel/Google Sheets?**
A: JSON files can be imported to spreadsheets. Or ask agents to generate CSV format.

**Q: What's the minimum to start tracking?**
A: Just revenue and expenses. Time tracking and other features are optional but valuable.

## Pricing & Value

**This plugin is free** - Part of Puerto open-source marketplace

**Value delivered**:
- **Tax savings**: Proper expense tracking = $1,000-5,000+ in deductions
- **Revenue optimization**: Hourly rate insights = 20-50% income increase
- **Time saved**: Automated tracking vs manual spreadsheets = 10+ hours/month
- **Better decisions**: Data-driven insights = focus on profitable work
- **Peace of mind**: Audit-ready records, quarterly tax preparation

**ROI Example**:
- Time saved: 10 hours/month × $50/hr = $500/month value
- Tax savings: $3,000/year additional deductions
- Revenue increase: 20% growth = $12,000/year (on $60K base)
- **Total value: $15,000+/year**

## Conclusion

The Side Hustle Manager Plugin transforms chaotic side business tracking into professional, data-driven financial management.

**Track it. Analyze it. Optimize it. Scale it.**

### Quick Start Recap

1. Install plugin: `/plugin install side-hustle-manager@puerto`
2. Copy templates to `.side-hustle/` directory
3. Start tracking: `@revenue-analyzer` and `@expense-tracker`
4. Review monthly, quarterly, annually
5. Act on insights to grow profitability

### Key Takeaways

- **Revenue is vanity** - Track all income but focus on profit
- **Profit is sanity** - Know your true margins after expenses
- **Cash flow is reality** - Monitor what actually hits your account
- **Hourly rate matters** - Work on high-value activities
- **Diversification reduces risk** - Multiple streams and clients
- **Data drives decisions** - Review metrics, adjust strategy
- **Tax optimization** - Track everything, maximize deductions

**Your side hustle deserves professional financial management. Start tracking today.**

---

*For issues, questions, or feedback, see the main Puerto repository.*
