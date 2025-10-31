# Cohort Analysis Report Template

**Use this template for retention analysis and cohort comparisons**

---

## Cohort Analysis: [Analysis Name]

**Date**: [Analysis date]
**Analyst**: [Your name]
**Period**: [Date range]

---

## Executive Summary

- **Best Performing Cohort**: [Month/Week] with [X]% Month-3 retention
- **Retention Trend**: [Improving/Stable/Declining] by [X]% per cohort
- **Key Insight**: [Most important finding in one sentence]
- **Recommendation**: [Top priority action]

---

## Analysis Configuration

**Cohort Definition**: Users grouped by [signup date / feature adoption / first purchase]

**Retention Definition**: User is "retained" if [performed specific action / logged in]

**Time Granularity**: [Daily / Weekly / Monthly]

**Analysis Period**: [Start date] to [End date]

**Cohorts Analyzed**: [Number] cohorts

---

## Classic Retention Table

| Cohort | Size | M0 | M1 | M2 | M3 | M6 | M12 |
|--------|------|----|----|----|----|----|-----|
| 2024-10 | 1,523 | 100% | 45% | 35% | 30% | - | - |
| 2024-09 | 1,412 | 100% | 42% | 33% | 28% | 25% | - |
| 2024-08 | 1,687 | 100% | 48% | 38% | 32% | 28% | - |
| 2024-07 | 1,234 | 100% | 40% | 30% | 25% | 22% | 20% |
| 2024-06 | 1,456 | 100% | 38% | 28% | 23% | 20% | 18% |
| 2024-05 | 1,589 | 100% | 36% | 26% | 21% | 18% | 16% |
| **Average** | **1,484** | **100%** | **41.5%** | **31.7%** | **26.5%** | **22.6%** | **18.0%** |

**Trend**: Retention [improving/declining/stable] - Recent cohorts retain [X]% [better/worse] than older cohorts

---

## N-Day Retention Summary

| Retention Point | Current | Previous Month | Target | Status |
|-----------------|---------|----------------|--------|--------|
| Day 1 | 62% | 59% | 60% | ✅ Above Target |
| Day 7 | 42% | 41% | 40% | ✅ Above Target |
| Day 30 | 28% | 30% | 30% | ⚠️ Below Target |
| Day 90 | 20% | 21% | 25% | 🔴 Below Target |

**Industry Benchmarks** ([Your industry]):
- Day 1: [X]%
- Day 7: [Y]%
- Day 30: [Z]%

**Status**: [Above/Below/At] industry average

---

## Retention Curve Visualization

```
Month 0: 100% |████████████████████|
Month 1:  42% |████████            |  (-58%)
Month 2:  32% |██████              |  (-10pp)
Month 3:  27% |█████               |  (-5pp)
Month 6:  23% |████                |  (-4pp)
Month 12: 20% |████                |  (-3pp)  ← Flattening curve ✅
```

**Curve Shape**: [Flattening / Declining / Smiling]

**Interpretation**:
- [What the curve shape means for product health]
- [Where users are churning most]
- [When retention stabilizes]

---

## Key Findings

### 1. Retention Curve Analysis

**Pattern**: [Flattening/Declining/Stable curve]

**What it means**:
- [Interpretation of retention behavior]
- [Critical retention milestones]
- [When users become "sticky"]

**Implication**: [What actions to take based on pattern]

---

### 2. Cohort Trends Over Time

**Recent Cohorts vs Older Cohorts**:
- Month 1 retention: [X]% → [Y]% ([Change])
- Month 3 retention: [X]% → [Y]% ([Change])
- **Trend**: [Improving/Declining/Stable]

**Why**:
- [Hypothesis 1 for trend]
- [Hypothesis 2 for trend]
- [Hypothesis 3 for trend]

**Supporting Evidence**:
- [Product changes that occurred]
- [User feedback]
- [Market conditions]

---

### 3. Segment Performance Differences

**Best Segment**: [Segment name] with [X]% Month-3 retention

**Worst Segment**: [Segment name] with [Y]% Month-3 retention

**Gap**: [X-Y]pp difference

**Why this matters**: [Business impact of segment differences]

**Root Causes**:
- [Reason 1 why segments differ]
- [Reason 2]
- [Reason 3]

---

## Detailed Segment Comparison

### By User Type

| Segment | M0 | M1 | M3 | M6 | Cohort Size | Trend |
|---------|----|----|----|----|-------------|-------|
| Power Users | 100% | 85% | 72% | 65% | 1,250 | ✅ Excellent |
| Regular Users | 100% | 55% | 38% | 28% | 3,800 | ✅ Good |
| Casual Users | 100% | 28% | 15% | 8% | 6,950 | ⚠️ Low |

---

### By Plan Type

| Plan | M0 | M1 | M3 | M6 | Cohort Size | MRR Impact |
|------|----|----|----|----|-------------|------------|
| Enterprise | 100% | 92% | 85% | 80% | 450 | $225K |
| Pro | 100% | 68% | 52% | 42% | 2,100 | $180K |
| Free | 100% | 32% | 18% | 10% | 9,450 | $0 |

**Insight**: Enterprise retention excellent but small cohort size. Opportunity to grow this segment.

---

### By Acquisition Channel

| Channel | M0 | M1 | M3 | M6 | Cohort Size | CAC | LTV:CAC |
|---------|----|----|----|----|-------------|-----|---------|
| Organic | 100% | 48% | 35% | 28% | 4,500 | $12 | 9.8:1 |
| Paid Search | 100% | 42% | 30% | 22% | 3,200 | $45 | 2.4:1 |
| Social | 100% | 35% | 22% | 15% | 2,800 | $38 | 1.6:1 |
| Referral | 100% | 62% | 48% | 40% | 1,500 | $8 | 15.5:1 |

**Insight**: Referral users have best retention and economics. Invest in referral program.

---

## Leading Indicators of Retention

Analysis of what high-retention users do differently:

### High-Retention Users (Top 25%) vs Low-Retention (Bottom 25%)

| Behavior | High-Retention | Low-Retention | Difference |
|----------|----------------|---------------|------------|
| Complete onboarding | 95% | 42% | +53pp |
| Invite team member | 78% | 8% | +70pp |
| Use Feature X in Week 1 | 85% | 15% | +70pp |
| Sessions in first 7 days | 8.2 | 2.1 | +6.1 |
| Time to first value | 5.3 min | 28.7 min | -23.4 min |

**Key Drivers of Retention**:
1. **[Behavior 1]**: Users who [action] are [X]x more likely to retain
2. **[Behavior 2]**: [Impact on retention]
3. **[Behavior 3]**: [Impact on retention]

---

## Churn Analysis

### When Do Users Churn?

| Period | Churn Rate | Cumulative Churn | Users Lost |
|--------|------------|------------------|------------|
| Month 0-1 | 58% | 58% | 7,250 |
| Month 1-2 | 10pp | 68% | 1,250 |
| Month 2-3 | 5pp | 73% | 625 |
| Month 3-6 | 4pp | 77% | 500 |
| Month 6-12 | 3pp | 80% | 375 |

**Critical Churn Period**: [Month X-Y] when [Z]% of users churn

**Why Users Churn** (Top reasons from exit surveys):
1. [Reason 1] - [X]% of churned users
2. [Reason 2] - [Y]% of churned users
3. [Reason 3] - [Z]% of churned users

---

## Recommendations

### Immediate Actions (0-30 Days)

#### 1. Improve [Metric Name] from [X]% to [Y]%

**Goal**: Reduce Month 1 churn by [Z]pp

**Actions**:
- [ ] [Specific action item 1]
- [ ] [Specific action item 2]
- [ ] [Specific action item 3]

**Owner**: [@team-member]

**Expected Impact**: +[X] retained users per cohort

---

#### 2. [Recommendation 2]

[Same structure]

---

### Short-term Initiatives (1-3 Months)

#### 3. [Recommendation 3]

[Same structure]

---

### Long-term Investments (3+ Months)

#### 4. [Recommendation 4]

[Same structure]

---

## Experimentation Ideas

### Test 1: Improve Onboarding Completion

**Hypothesis**: Users who complete onboarding are 2x more likely to retain. Improving completion from 65% → 80% will improve Day 30 retention by [X]%.

**Target Audience**: New users in first 7 days

**Treatment**: [Description of onboarding changes]

**Primary Metric**: Day 30 retention

**Secondary Metrics**: Onboarding completion rate, time to first value

**Success Criteria**: +[X]pp improvement in Day 30 retention

---

### Test 2: [Test Name]

[Same structure]

---

## Forward-Looking Metrics

### Projected Churn (Next 90 Days)

Based on current cohort trends:

| Cohort | Size | Expected Churn | Impact |
|--------|------|----------------|--------|
| 2024-10 | 1,523 | 890 (58%) | -$17,800 MRR |
| 2024-09 | 1,412 | 564 (40%) | -$11,280 MRR |
| 2024-08 | 1,687 | 337 (20%) | -$6,748 MRR |

**Total Projected Churn**: [X] users, -$[Y] MRR over next 90 days

**If we improve retention by [Z]pp**: Save [A] users, +$[B] MRR

---

## Next Steps

1. **Share findings** with product, engineering, and growth teams - [Date]
2. **Deep dive on leading indicators** - Why do these behaviors correlate with retention? - [Date]
3. **Design experiments** to improve Day 1 and Month 1 retention - [Date]
4. **Set up automated cohort reporting** (monthly refresh) - [Date]
5. **Re-analyze in 30 days** to track progress - [Date]

---

## Appendix

### Methodology

**Cohort Definition**: [How cohorts were defined]

**Retention Event**: [What action constitutes "retained"]

**Data Source**: [Analytics platform, database]

**Analysis Period**: [Dates]

**Sample Size**: [Number of users across all cohorts]

---

### SQL Queries

All queries available in:
- `analytics/cohorts/retention_table.sql`
- `analytics/cohorts/n_day_retention.sql`
- `analytics/cohorts/segment_comparison.sql`
- `analytics/cohorts/leading_indicators.sql`
- `analytics/cohorts/churn_analysis.sql`

---

**Report Version**: 1.0
**Created**: [Date]
**Last Updated**: [Date]
**Next Review**: [30 days from now]
