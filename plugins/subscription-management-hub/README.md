# Subscription Management Hub Plugin

A comprehensive subscription tracking and cost optimization system for Claude Code that helps you manage all your subscriptions, track renewals, analyze costs, and optimize spending.

## Overview

The Subscription Management Hub plugin provides intelligent agents and tools for complete subscription lifecycle management. From tracking streaming services to monitoring SaaS tools, this plugin ensures you never miss a cancellation deadline or pay for unused subscriptions.

## What's Included

### Agents

#### 1. subscription-cataloger (Haiku)
Fast subscription inventory management and cataloging.

**Key Features:**
- Add/remove/update subscriptions with complete metadata
- Bulk import from CSV
- Search and filter by category, cost, status
- Export to multiple formats
- Quick data entry for large subscription lists
- Automatic monthly/annual cost calculations

**Activation**: Automatically activates for inventory operations, or use `@subscription-cataloger`.

#### 2. cost-analyzer (Sonnet)
Deep cost analysis, ROI calculations, and optimization recommendations.

**Key Features:**
- Monthly/annual spending breakdowns
- Usage-based ROI analysis
- Identify underutilized subscriptions
- Find cheaper alternatives
- Detect bundle opportunities
- Annual vs monthly billing comparison
- Generate comprehensive optimization reports

**Activation**: Use `@cost-analyzer` for cost analysis and optimization.

#### 3. renewal-monitor (Haiku)
Proactive renewal tracking and deadline management.

**Key Features:**
- Track upcoming renewals (7, 14, 30 day alerts)
- Monitor trial expiration dates
- Identify cancellation deadlines
- Generate daily subscription digest
- Comprehensive cancellation calendar
- Price increase alerts
- Auto-renewal status tracking

**Activation**: Use `@renewal-monitor` for renewal alerts and calendar.

### Skills

#### subscription-optimization
Comprehensive patterns for subscription management:
- Data structure standards
- Cost calculation methods
- ROI and value scoring algorithms
- Optimization strategies
- Alternative service databases
- Cancellation procedures for major services
- Bundle opportunity detection
- Price tracking patterns

All agents read this skill for consistent subscription management.

### Templates

#### 1. subscription-database.json
Complete subscription inventory template with 5 example subscriptions showing:
- Active subscriptions (Netflix, Spotify, NYT)
- Trial subscriptions (Adobe Creative Cloud)
- Underutilized subscriptions (Unused Fitness App)
- Full metadata structure
- Cost calculations

#### 2. cost-analysis-report.json
Comprehensive cost analysis template including:
- Overall spending summary
- Category breakdowns with percentages
- Usage analysis (excellent/good/needs review/underutilized)
- Prioritized recommendations
- Potential savings calculations
- Urgent alerts

#### 3. cancellation-calendar.json
Deadline tracking template with:
- Upcoming renewals timeline
- Trial ending dates
- Cancellation deadlines
- Price change history
- Calendar views (week/month)
- Urgent action items

## Installation

```bash
/plugin install subscription-management-hub@puerto
```

**Prerequisites:**
- Python 3.9+
- No external API keys required (all local)

After installation, restart Claude Code to activate all agents and skill.

## Quick Start

### Initial Setup

```bash
# Initialize subscription tracker
@subscription-cataloger "Initialize new subscription tracker"

# The tracker will be created at:
# ~/.subscription-tracker/ (user-level) or
# .subscription-tracker/ (project-level if in git repo)
```

### Adding Subscriptions

**Add single subscription:**
```
@subscription-cataloger Add Netflix Premium, $15.99/month, streaming-video category
```

**Bulk import from CSV:**
```
@subscription-cataloger Import subscriptions from subscriptions.csv
```

**CSV format:**
```csv
name,cost,billing_cycle,category,provider,renewal_date,website,login_email
Netflix Premium,15.99,monthly,streaming-video,Netflix Inc.,2025-11-23,https://netflix.com,user@example.com
Spotify Premium,10.99,monthly,streaming-music,Spotify,2025-11-15,https://spotify.com,user@example.com
```

### Daily Usage

**Check what's renewing:**
```
@renewal-monitor Show upcoming renewals
```

**Analyze costs:**
```
@cost-analyzer Generate cost analysis report
```

**Update usage:**
```
@subscription-cataloger Update last_used for Netflix to today
@subscription-cataloger Mark Fitness App usage as never
```

**Search subscriptions:**
```
@subscription-cataloger Show all streaming subscriptions
@subscription-cataloger Find subscriptions over $20/month
```

### Weekly Reviews

```
@renewal-monitor Generate daily digest
@cost-analyzer Show underutilized subscriptions
```

### Monthly Optimization

```
@cost-analyzer Generate comprehensive optimization report
# Provides:
# - Total spending analysis
# - Underutilized subscription identification
# - Alternative service suggestions
# - Bundle opportunities
# - Annual billing savings potential
# - Prioritized action items
```

## Data Structure

All subscription data is stored locally in:
- `~/.subscription-tracker/` (user-level, default)
- `.subscription-tracker/` (project-level, if in git repo)

### Directory Layout

```
.subscription-tracker/
├── subscription-database.json    # Main subscription inventory
├── cost-analysis-report.json     # Latest cost analysis
├── cancellation-calendar.json    # Renewal and deadline tracking
├── config.json                   # User preferences
├── reports/                      # Historical reports
│   ├── 2025-10-monthly.json
│   └── 2025-Q4-quarterly.json
├── exports/                      # User exports
│   └── subscriptions_20251023.csv
└── archives/                     # Deleted subscriptions
    └── OldService_uuid.json
```

### Core Data Model

#### Subscription Entry

```json
{
  "id": "uuid",
  "name": "Netflix Premium",
  "provider": "Netflix Inc.",
  "category": "streaming-video",
  "cost": 15.99,
  "billing_cycle": "monthly",
  "monthly_cost_equivalent": 15.99,
  "annual_cost_equivalent": 191.88,
  "status": "active|trial|cancelled",
  "renewal_date": "2025-11-23",
  "trial_end_date": null,
  "cancellation_deadline": null,
  "auto_renew": true,
  "last_used": "2025-10-22",
  "usage_frequency": "daily|weekly|monthly|rarely|never",
  "website": "https://netflix.com",
  "login_email": "user@example.com",
  "notes": "Family plan shared with 3 people",
  "alternatives": ["Hulu", "Disney+"],
  "tags": ["entertainment", "essential"]
}
```

## Features

### Cost Tracking

**Automatic calculations:**
- Monthly cost equivalents for all billing cycles
- Annual cost projections
- Category-based spending breakdowns
- Total monthly/annual spending

**Supported billing cycles:**
- Monthly
- Annual/Yearly
- Quarterly
- Biannual
- Weekly/Biweekly

### Usage Analysis

**Value scoring:**
- Combines usage frequency with cost
- Identifies excellent value subscriptions
- Flags underutilized subscriptions
- Calculates ROI for each service

**Usage tracking:**
- Last used date tracking
- Usage frequency (daily/weekly/monthly/rarely/never)
- Days since last use
- Automatic underutilization detection

### Renewal Management

**Proactive alerts:**
- 30 days before renewal
- 14 days before renewal
- 7 days before renewal
- 1 day before renewal
- Day-of alerts

**Trial tracking:**
- Trial end date monitoring
- Cancellation deadline alerts (3 days, 1 day, same day)
- Auto-charge warnings
- Decision reminders

**Calendar features:**
- Comprehensive deadline calendar
- Weekly/monthly views
- Urgent action items
- Auto-renewal status tracking

### Cost Optimization

**Optimization strategies:**

1. **Cancel Underutilized**
   - Identifies subscriptions not used in 90+ days
   - Calculates annual savings
   - Prioritizes by cost

2. **Switch to Annual Billing**
   - Estimates 15-20% savings
   - Only suggests for committed users
   - Calculates payback period

3. **Bundle Opportunities**
   - Detects Disney Bundle opportunities (Disney+, Hulu, ESPN+)
   - Apple One opportunities (Music, TV+, Arcade, iCloud+)
   - Amazon Prime bundling
   - YouTube Premium Family plans
   - Calculates bundle savings

4. **Alternative Services**
   - Suggests cheaper alternatives
   - Compares features
   - Shows annual savings
   - Includes free alternatives

5. **Price Increase Monitoring**
   - Tracks historical prices
   - Alerts on increases
   - Suggests review when prices rise
   - Calculates impact

### Reporting

**Cost Analysis Report includes:**
- Overall spending summary
- Category breakdowns with percentages
- Top 5 most expensive subscriptions
- Underutilized subscription list
- Value-scored subscription ranking
- Prioritized recommendations
- Potential savings calculations

**Calendar Report includes:**
- Next 90 days of renewals
- Trial ending dates
- Cancellation deadlines
- Month-by-month view
- Urgent action items

## Subscription Categories

**Supported categories:**
- streaming-video: Netflix, Hulu, Disney+, HBO Max
- streaming-music: Spotify, Apple Music, YouTube Music
- streaming-audio: Audible, podcasts
- software-saas: Web applications, SaaS tools
- software-desktop: Desktop software licenses
- cloud-storage: Dropbox, Google Drive, iCloud
- productivity: Microsoft 365, Google Workspace, Notion
- fitness: Gym memberships, fitness apps
- gaming: Xbox Game Pass, PlayStation Plus
- news-media: Newspapers, magazines
- education: Online courses, learning platforms
- professional: LinkedIn Premium, industry tools
- other: Everything else

## Common Workflows

### Complete Subscription Lifecycle

```bash
# 1. Start free trial
@subscription-cataloger Add Adobe Creative Cloud trial, $54.99/month, trial ends 2025-11-05

# 2. Track usage during trial
@subscription-cataloger Update Adobe CC usage to weekly
@subscription-cataloger Note: "Using for design project"

# 3. Get trial reminder
@renewal-monitor Check trial expirations
# Output: Trial ends in 3 days, cancel by 2025-11-04 to avoid $54.99 charge

# 4. Make decision
@cost-analyzer Show alternatives for Adobe Creative Cloud
# Output: Affinity Suite $169.99 one-time, Canva Pro $12.99/month

# 5. Cancel or convert
@subscription-cataloger Cancel Adobe Creative Cloud
# or
@subscription-cataloger Update Adobe CC status to active
```

### Monthly Optimization Review

```bash
# 1. Generate cost analysis
@cost-analyzer Generate comprehensive optimization report

# Output includes:
# - Total spending: $234.50/month ($2,814/year)
# - Underutilized: Fitness App (not used in 250 days)
# - Potential savings: $119.88/year
# - Bundle opportunities: Disney Bundle saves $10/month
# - Annual billing savings: $88/year

# 2. Check upcoming renewals
@renewal-monitor Show next 30 days

# 3. Take action on recommendations
@subscription-cataloger Cancel Unused Fitness App
@subscription-cataloger Update Netflix to annual billing
```

### Trial Management Workflow

```bash
# Set up trial tracking
@subscription-cataloger Add trial: ServiceName, $X/month, ends 2025-11-15

# Track trial usage
@subscription-cataloger Update ServiceName last_used to today

# Get reminders
@renewal-monitor Daily digest
# Shows: Trial ends in 3 days, decide to keep or cancel

# Make informed decision
@cost-analyzer Analyze ServiceName value
# Shows: Usage score, cost comparison, alternatives

# Act before deadline
@subscription-cataloger Cancel ServiceName
# or keep it
```

### Budget Control Workflow

```bash
# 1. Set budget target
# (Note: Track in notes, future version will have budget alerts)

# 2. Monthly review
@cost-analyzer Generate cost breakdown

# 3. Identify cuts if over budget
@cost-analyzer Show underutilized subscriptions sorted by cost

# 4. Prioritize essentials
@subscription-cataloger Tag Netflix as essential
@subscription-cataloger Tag Fitness App as non-essential

# 5. Make cuts to meet budget
@subscription-cataloger Cancel non-essential subscriptions
```

## Commands Summary

### Cataloging
```bash
@subscription-cataloger "Add [name], $[cost]/[cycle], [category]"
@subscription-cataloger "Update [name] [field] to [value]"
@subscription-cataloger "Remove [name]"
@subscription-cataloger "Search [category/cost range/status]"
@subscription-cataloger "Import from [file.csv]"
@subscription-cataloger "Export to [format]"
```

### Cost Analysis
```bash
@cost-analyzer "Generate cost analysis"
@cost-analyzer "Show underutilized subscriptions"
@cost-analyzer "Find alternatives for [name]"
@cost-analyzer "Compare annual vs monthly billing"
@cost-analyzer "Identify bundle opportunities"
@cost-analyzer "Generate optimization report"
```

### Renewal Monitoring
```bash
@renewal-monitor "Show upcoming renewals"
@renewal-monitor "Check trial expirations"
@renewal-monitor "Generate cancellation calendar"
@renewal-monitor "Daily digest"
@renewal-monitor "Show renewals next [7/14/30] days"
```

## Configuration

Edit `~/.subscription-tracker/config.json`:

```json
{
  "currency": "USD",
  "currency_symbol": "$",
  "reminder_days_before_renewal": 7,
  "trial_reminder_days": 3,
  "usage_tracking_enabled": true,
  "categories": [
    "streaming-video",
    "streaming-music",
    "software-saas",
    "cloud-storage",
    "productivity",
    "fitness",
    "gaming",
    "news-media",
    "education",
    "professional",
    "other"
  ],
  "notification_preferences": {
    "renewal_reminders": true,
    "trial_expiration": true,
    "price_increases": true,
    "unused_subscriptions": true
  }
}
```

## Best Practices

### 1. Track Everything
Include all subscriptions, even small ones:
- Free trials (especially important!)
- Annual subscriptions
- Gym memberships
- App subscriptions
- Professional tools
- Streaming services

### 2. Update Usage Weekly
Keep usage information current:
- Mark when you last used each service
- Update usage frequency honestly
- Note changes in usage patterns

### 3. Set Reminders
Check renewal calendar regularly:
- Daily digest for urgent items
- Weekly for upcoming renewals
- Monthly for optimization review

### 4. Act on Trials Promptly
Don't let trials auto-convert:
- Track trial end dates immediately
- Set cancellation reminders 2-3 days before
- Make decision before deadline
- Cancel if unsure (you can always re-subscribe)

### 5. Review Quarterly
Deep optimization every 3 months:
- Run full cost analysis
- Review all subscriptions
- Check for new bundle opportunities
- Evaluate alternatives
- Update usage patterns

### 6. Consider Annual Billing
Switch to annual for committed subscriptions:
- Typical savings: 15-20%
- Only for services you're sure about
- Keep emergency fund for upfront payment

### 7. Use Categories
Organize subscriptions by type:
- Makes analysis easier
- Identifies spending patterns
- Helps with budget allocation

### 8. Document Everything
Add notes for context:
- Why you subscribed
- What you use it for
- Sharing with others
- Decision factors

## Alternative Services Database

Common alternatives included in cost analyzer:

**Streaming Video:**
- Netflix → Hulu, Disney+, Amazon Prime Video
- Hulu → Netflix, Disney+, Paramount+
- HBO Max → Hulu, Showtime

**Streaming Music:**
- Spotify → Apple Music, YouTube Music, Amazon Music
- Apple Music → Spotify, YouTube Music
- YouTube Music → Spotify (if don't need YouTube Premium)

**Software/SaaS:**
- Adobe CC → Affinity Suite, Canva Pro, Figma
- Microsoft 365 → Google Workspace, LibreOffice (free)
- Dropbox → Google Drive, iCloud, OneDrive

**Productivity:**
- Notion → Obsidian (free), OneNote (free)
- Evernote → Notion, Apple Notes (free)

## Cancellation Procedures

Common services with cancellation links:

**Streaming:**
- Netflix: netflix.com/cancelplan
- Hulu: hulu.com/account
- Disney+: disneyplus.com/account
- Spotify: spotify.com/account/subscription

**Software:**
- Adobe CC: account.adobe.com/plans (warning: may have termination fee)
- Microsoft 365: account.microsoft.com/services
- Google Workspace: admin.google.com/billing

**Important notes:**
- Most services: Cancel anytime, access until period ends
- Annual plans: Check cancellation deadline (often 30-60 days before renewal)
- Trials: Cancel 24-48 hours before end to ensure no charge
- Contracts: Review early termination fees before canceling

## Troubleshooting

### Database Not Found

**Issue**: "Subscription tracker not initialized"

**Solution**:
```bash
@subscription-cataloger "Initialize subscription tracker"
```

### Incorrect Totals

**Issue**: Metadata totals don't match subscriptions

**Solution**:
- Agents automatically recalculate on every operation
- If persists, export subscriptions and re-import

### Missing Renewal Dates

**Issue**: Can't track renewals without dates

**Solution**:
```bash
@subscription-cataloger "Update [name] renewal_date to 2025-11-23"
```

Check your billing statements or subscription account pages for renewal dates.

### Trial Not Alerting

**Issue**: Not receiving trial expiration alerts

**Solution**:
- Ensure trial_end_date is set
- Ensure status is set to "trial"
- Run daily digest manually to check

## Privacy & Security

**Local-first approach:**
- All data stored locally on your machine
- No cloud sync (unless you set it up)
- No telemetry or tracking
- No account required

**Sensitive data:**
- Login emails stored locally only
- Payment methods stored as masked (e.g., "Visa *1234")
- NEVER store passwords
- Consider encrypting .subscription-tracker directory

**Git safety:**
Add to `.gitignore`:
```
.subscription-tracker/
*.subscription-tracker.json
subscription-database.json
config.json
```

## Performance Notes

- Lightweight JSON-based storage
- Fast search and filtering
- Handles 100+ subscriptions easily
- Python-based calculations (included with Claude Code)
- No external dependencies

## Future Enhancements

Planned features:
- Bank/credit card integration for auto-detection
- Calendar app integration for reminders
- Email alerts for urgent deadlines
- Budget tracking and alerts
- Price tracking over time
- Subscription recommendations based on usage
- Family plan management
- Shared subscription tracking

## Support & Feedback

This plugin is part of the Puerto marketplace. For issues or suggestions, refer to the main Puerto repository.

## Related Tools

**Works well with:**
- Budget tracking apps (YNAB, Mint)
- Calendar apps (for deadline integration)
- Password managers (for login storage)

## License

MIT License - See main repository for details

---

**Take control of your subscriptions. Track every service, optimize every dollar, never miss a cancellation deadline.**
