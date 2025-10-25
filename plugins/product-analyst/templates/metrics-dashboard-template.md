# Product Metrics Dashboard Template

**Use this template to create comprehensive, actionable product metrics dashboards**

---

## Dashboard: [Product Name] Product Health

**Last Updated**: [Auto-generated timestamp]
**Owner**: Product Analytics Team
**Refresh Frequency**: Daily at 6 AM UTC

---

## 🎯 North Star Metric

### [Your North Star Metric Name]

**Current**: [Value] | **Target**: [Goal] | **Status**: [On Track / At Risk / Off Track]

```
[ASCII chart or emoji trend indicator]
↗️ +12% vs last week
↗️ +45% vs last month
↗️ +125% vs last year
```

**Definition**: [Clear definition of what this metric measures]

**Why it matters**: [Business impact and connection to company goals]

**SQL Query**: `queries/north_star_metric.sql`

---

## 📊 AARRR Metrics (Pirate Metrics)

### 🎣 Acquisition

| Metric | Current | vs Last Week | vs Last Month | Target | Status |
|--------|---------|--------------|---------------|--------|--------|
| New Users | 1,245 | +8% ↗️ | +15% ↗️ | 1,200 | ✅ On Track |
| Organic Signups | 780 | +12% ↗️ | +20% ↗️ | 700 | ✅ On Track |
| Paid Signups | 465 | +2% ↗️ | +8% ↗️ | 500 | ⚠️ At Risk |
| CAC (Customer Acquisition Cost) | $42.50 | -5% ↗️ | -8% ↗️ | $45 | ✅ On Track |

**Insights**:
- Organic growth accelerating due to [reason]
- Paid campaigns underperforming, investigate [specific campaign]

**SQL**: `queries/acquisition_metrics.sql`

---

### ⚡ Activation

| Metric | Current | vs Last Week | vs Last Month | Target | Status |
|--------|---------|--------------|---------------|--------|--------|
| Signup → Activation Rate | 45.2% | +2.1pp ↗️ | +5.3pp ↗️ | 40% | ✅ On Track |
| Time to First Value (median) | 8.5 min | -1.2 min ↗️ | -2.8 min ↗️ | < 10 min | ✅ On Track |
| Onboarding Completion | 68% | +3% ↗️ | +7% ↗️ | 65% | ✅ On Track |

**Insights**:
- Onboarding redesign having positive impact
- Mobile activation still lagging (35% vs 52% desktop)

**SQL**: `queries/activation_metrics.sql`

---

### 🔁 Retention

| Metric | Current | vs Last Week | vs Last Month | Target | Status |
|--------|---------|--------------|---------------|--------|--------|
| DAU (Daily Active Users) | 12,450 | +3% ↗️ | +8% ↗️ | 12,000 | ✅ On Track |
| WAU (Weekly Active Users) | 45,000 | +5% ↗️ | +12% ↗️ | 42,000 | ✅ On Track |
| MAU (Monthly Active Users) | 125,000 | +8% ↗️ | +18% ↗️ | 120,000 | ✅ On Track |
| DAU/MAU (Stickiness) | 10.0% | -0.3pp ↘️ | -1.2pp ↘️ | 12% | ⚠️ At Risk |
| Day 1 Retention | 62% | +1% ↗️ | +4% ↗️ | 60% | ✅ On Track |
| Day 7 Retention | 42% | Flat → | +2% ↗️ | 40% | ✅ On Track |
| Day 30 Retention | 28% | -1% ↘️ | -1% ↘️ | 30% | ⚠️ At Risk |
| Monthly Churn Rate | 5.2% | +0.3pp ↘️ | +0.5pp ↘️ | < 5% | 🔴 Off Track |

**Insights**:
- MAU growing but stickiness declining (users less engaged)
- Day 30 retention needs attention
- Investigate churn spike in [segment]

**SQL**: `queries/retention_metrics.sql`

---

### 💰 Revenue

| Metric | Current | vs Last Week | vs Last Month | Target | Status |
|--------|---------|--------------|---------------|--------|--------|
| MRR (Monthly Recurring Revenue) | $245,000 | +$8,500 ↗️ | +$32,000 ↗️ | $240,000 | ✅ On Track |
| ARR (Annual Recurring Revenue) | $2.94M | +$102K ↗️ | +$384K ↗️ | $2.88M | ✅ On Track |
| ARPU (Avg Revenue Per User) | $19.60 | +$0.50 ↗️ | +$1.20 ↗️ | $18 | ✅ On Track |
| LTV (Lifetime Value) | $470 | +$15 ↗️ | +$45 ↗️ | $450 | ✅ On Track |
| LTV:CAC Ratio | 11.1:1 | +0.5 ↗️ | +1.2 ↗️ | > 3:1 | ✅ On Track |
| Conversion Rate (Free → Paid) | 12.5% | +0.8pp ↗️ | +1.5pp ↗️ | 12% | ✅ On Track |

**Insights**:
- Healthy LTV:CAC ratio indicates sustainable growth
- ARPU increasing due to upsells to higher tiers

**SQL**: `queries/revenue_metrics.sql`

---

### 📣 Referral

| Metric | Current | vs Last Week | vs Last Month | Target | Status |
|--------|---------|--------------|---------------|--------|--------|
| Viral Coefficient (K-factor) | 0.42 | +0.03 ↗️ | +0.08 ↗️ | 0.40 | ✅ On Track |
| Referral Rate (% referring) | 15.2% | +1.1pp ↗️ | +2.8pp ↗️ | 15% | ✅ On Track |
| Invites Sent per User | 2.8 | +0.2 ↗️ | +0.5 ↗️ | 2.5 | ✅ On Track |
| Invite Acceptance Rate | 32% | -2% ↘️ | Flat → | 35% | ⚠️ At Risk |

**Insights**:
- More users referring but acceptance rate declining
- Review invite messaging and incentives

**SQL**: `queries/referral_metrics.sql`

---

## 🎯 Feature Adoption

| Feature | Adoption Rate | Users This Week | Trend | Status |
|---------|---------------|-----------------|-------|--------|
| [Feature A] | 45% | 5,625 | +3% ↗️ | ✅ On Track |
| [Feature B] | 28% | 3,500 | +8% ↗️ | ✅ Growing |
| [Feature C] | 12% | 1,500 | -2% ↘️ | ⚠️ Declining |
| [New Feature] | 8% | 1,000 | New | 🆕 Launch |

**SQL**: `queries/feature_adoption.sql`

---

## 📱 Segmentation

### By Platform

| Platform | Users | % of Total | Engagement | Retention (D30) | Revenue per User |
|----------|-------|------------|------------|-----------------|------------------|
| iOS | 45,000 | 36% | High | 32% | $24.50 |
| Android | 52,000 | 42% | Medium | 26% | $16.80 |
| Web | 28,000 | 22% | Low | 22% | $18.20 |

### By User Segment

| Segment | Users | % of Total | Engagement | Retention (D30) | Revenue per User |
|---------|-------|------------|------------|-----------------|------------------|
| Power Users (daily) | 12,450 | 10% | Very High | 85% | $45.00 |
| Regular Users (weekly) | 32,550 | 26% | High | 52% | $22.50 |
| Casual Users (monthly) | 80,000 | 64% | Low | 18% | $8.50 |

**SQL**: `queries/segmentation_metrics.sql`

---

## 🚨 Alerts & Action Items

### Critical Issues (Immediate Action Required)

| Issue | Metric | Current | Target | Change | Owner | Due |
|-------|--------|---------|--------|--------|-------|-----|
| Churn spike | Monthly Churn | 5.2% | < 5% | +0.5pp | @pm-name | Today |
| D30 retention drop | Day 30 Retention | 28% | 30% | -1% | @pm-name | This week |

### Opportunities (Positive Trends to Amplify)

| Opportunity | Metric | Current | Trend | Action | Owner |
|-------------|--------|---------|-------|--------|-------|
| Organic growth | Organic Signups | 780 | +20% | Double down on SEO | @growth-lead |
| Feature B adoption | Adoption Rate | 28% | +8% | Promote in onboarding | @product-lead |

---

## 📈 Trends & Insights

### Week-over-Week Summary

✅ **Wins**:
- North Star metric up 12% (best week this quarter)
- Activation rate hit all-time high
- Revenue targets exceeded

⚠️ **Concerns**:
- Stickiness declining despite MAU growth
- Day 30 retention trending down
- Churn rate above target

📋 **Action Plan**:
1. Investigate churn cohorts (who's churning and why)
2. Run engagement experiments to improve stickiness
3. Review retention tactics (email campaigns, in-app prompts)

---

## 📊 SQL Queries

All queries available in `analytics/queries/` directory:

- `north_star_metric.sql`
- `acquisition_metrics.sql`
- `activation_metrics.sql`
- `retention_metrics.sql`
- `revenue_metrics.sql`
- `referral_metrics.sql`
- `feature_adoption.sql`
- `segmentation_metrics.sql`

---

## 🔄 Refresh Schedule

- **Real-time**: North Star, DAU
- **Hourly**: Revenue, signups
- **Daily**: All metrics (6 AM UTC)
- **Weekly**: Trends, cohorts (Monday 9 AM)
- **Monthly**: Executive summary (1st of month)

---

## 📚 Definitions

**Active User**: User who performed [key action] in the time period

**Activated User**: User who completed [key action] within [timeframe] of signup

**Churned User**: Paid user who canceled or did not renew subscription

**Stickiness**: DAU/MAU ratio, indicates engagement frequency

**Viral Coefficient**: Average number of new users each existing user brings

---

**Dashboard Version**: 1.0
**Created**: [Date]
**Last Review**: [Date]
**Next Review**: [Date]
