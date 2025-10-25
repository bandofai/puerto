# A/B Test Analysis Report Template

**Use this template for rigorous experiment analysis and decision-making**

---

## Experiment Analysis: [Experiment Name]

**Experiment ID**: `exp_[id]`
**Analyst**: [Your name]
**Date**: [Analysis date]

---

## Executive Summary

- **Decision**: [SHIP IT ✅ / KILL IT ❌ / CONTINUE 📊 / INVESTIGATE 🔍]
- **Winner**: [Control / Treatment / No Clear Winner]
- **Primary Metric Impact**: [+/-X%] ([Statistically Significant/Not Significant])
- **Recommendation**: [Clear, one-sentence action to take]

**Quick Stats**:
- Baseline conversion: [X]%
- Treatment conversion: [Y]%
- Relative lift: [Z]%
- P-value: [value]
- Confidence: [95% / 99%]

---

## Experiment Details

### Hypothesis

**We believe** [specific change]

**Will cause** [specific metric] to [increase/decrease] by [amount]

**Because** [reasoning based on data, user research, or theory]

**Example**:
> We believe adding customer testimonials to the checkout page will increase purchase completion rate by at least 10% because exit surveys show users don't trust us with payment info and session recordings show hesitation at the payment step.

---

### Configuration

**Variants**:
- **Control (A)**: [Description of current experience]
- **Treatment (B)**: [Description of change being tested]

**Primary Metric**: [Metric name and definition]

**Secondary Metrics** (Guardrails):
- [Metric 1]
- [Metric 2]
- [Metric 3]

**Traffic Allocation**: [50/50 or other split]

**Run Dates**: [Start date] to [End date] ([X] days)

**Target Sample Size**: [Y] users per variant

---

## Sample Size & Power

### Pre-Experiment Calculation

**Baseline Conversion Rate**: [X]%

**Minimum Detectable Effect (MDE)**: [Y]% relative ([Z]% absolute)

**Statistical Power**: 80%

**Significance Level**: 95% (α = 0.05)

**Required Sample Size**: [N] users per variant

**Expected Runtime**: [Days] days at [traffic/day] users per day

---

### Actual Sample Achieved

| Variant | Users | % of Total | Status |
|---------|-------|------------|--------|
| Control | [X] | [50%] | ✅ Sufficient |
| Treatment | [Y] | [50%] | ✅ Sufficient |
| **Total** | **[X+Y]** | **100%** | ✅ |

**Sample Ratio Mismatch Check**: ✅ No SRM (50.2% vs 49.8%)

**Runtime**: [X] days (met minimum of [Y] days for weekly seasonality)

---

## Primary Metric Results

### [Metric Name]

| Variant | Users | Conversions | Rate | 95% CI | Status |
|---------|-------|-------------|------|--------|--------|
| Control | 10,000 | 1,000 | 10.00% | 9.42% - 10.58% | Baseline |
| Treatment | 10,100 | 1,212 | 12.00% | 11.41% - 12.59% | ✅ +20% |

**Absolute Lift**: +2.00 percentage points

**Relative Lift**: +20.0%

**Statistical Significance**:
- **Z-score**: 4.52
- **P-value**: < 0.001 (0.0006)
- **Result**: ✅ **HIGHLY SIGNIFICANT** (p < 0.01)

**Confidence Interval on Lift**: Treatment is between +15.2% and +24.8% better (95% CI)

**Interpretation**: We are 99.9% confident this is a real improvement, not due to chance.

---

### Practical Significance

**Is a +20% lift meaningful?**

✅ **YES** - This translates to:
- +212 conversions per 10,000 users
- +$[X] in revenue per day
- +$[Y] in annual revenue
- Exceeds our MDE threshold of [Z]%

---

## Secondary Metrics Analysis

| Metric | Control | Treatment | Change | Significant? | Status |
|--------|---------|-----------|--------|--------------|--------|
| **Revenue per User** | $15.20 | $16.80 | +10.5% | ✅ Yes (p=0.02) | ✅ Positive |
| **Session Duration** | 8.2 min | 8.5 min | +3.7% | ❌ No (p=0.31) | → Neutral |
| **Bounce Rate** | 32.5% | 31.8% | -2.2% | ❌ No (p=0.54) | → Neutral |
| **Cart Size (items)** | 2.3 | 2.4 | +4.3% | ❌ No (p=0.18) | → Neutral |
| **Churn Rate** | 5.2% | 5.1% | -1.9% | ❌ No (p=0.89) | → Neutral |

**Assessment**: ✅ No negative effects detected. Revenue per user also improved (bonus!).

---

## Segment Analysis

Does the treatment work for everyone?

### By User Type

| Segment | Control Rate | Treatment Rate | Lift | Significant? | Status |
|---------|--------------|----------------|------|--------------|--------|
| **New Users** | 8.5% | 11.2% | +31.8% | ✅ Yes (p<0.01) | ✅✅ Excellent |
| **Returning Users** | 12.3% | 13.1% | +6.5% | ❌ No (p=0.12) | → Neutral |

**Insight**: Treatment works exceptionally well for new users (+32%). Moderate effect for returning users.

---

### By Device

| Segment | Control Rate | Treatment Rate | Lift | Significant? | Status |
|---------|--------------|----------------|------|--------------|--------|
| **Mobile** | 9.2% | 11.0% | +19.6% | ✅ Yes (p=0.03) | ✅ Good |
| **Desktop** | 11.5% | 13.8% | +20.0% | ✅ Yes (p<0.01) | ✅ Good |
| **Tablet** | 10.1% | 11.8% | +16.8% | ❌ No (p=0.15) | → Neutral |

**Insight**: Treatment works consistently across mobile and desktop. Tablet sample too small.

---

### By Traffic Source

| Segment | Control Rate | Treatment Rate | Lift | Significant? | Status |
|---------|--------------|----------------|------|--------------|--------|
| **Organic** | 11.2% | 13.5% | +20.5% | ✅ Yes | ✅ Good |
| **Paid** | 8.8% | 10.8% | +22.7% | ✅ Yes | ✅ Good |
| **Social** | 7.5% | 9.2% | +22.7% | ✅ Yes | ✅ Good |

**Insight**: Treatment works across all traffic sources.

---

## Validity Checks

### 1. Sample Ratio Mismatch (SRM)

**Expected**: 50% Control, 50% Treatment

**Actual**: 49.8% Control, 50.2% Treatment

**Status**: ✅ No SRM detected (within acceptable range)

**Implication**: Randomization worked correctly.

---

### 2. Novelty/Primacy Effects

**Runtime**: 15 days

**Week 1 Performance**: +18% lift
**Week 2 Performance**: +21% lift

**Trend**: Effect stable or increasing

**Status**: ✅ No novelty effect detected

---

### 3. AA Test (Sanity Check)

**Pre-experiment AA test**: Control vs Control

**Result**: No significant difference (p=0.87)

**Status**: ✅ Tracking working correctly

---

### 4. Data Quality

- [ ] ✅ No missing data
- [ ] ✅ Event tracking verified
- [ ] ✅ Test accounts excluded
- [ ] ✅ Bot traffic filtered
- [ ] ✅ No major bugs reported
- [ ] ✅ Consistent sample size across days

---

## Statistical Tests Performed

1. **Z-test for proportions** (primary metric: conversion rate)
2. **T-test** (secondary metrics: revenue, duration)
3. **Chi-square test** (categorical outcomes)
4. **Sample Ratio Mismatch check** (no SRM detected)
5. **Multiple testing correction** (Bonferroni: α = 0.05/3 = 0.017 for 3 secondary metrics)

---

## Trends Over Time

### Daily Performance

| Date | Control Rate | Treatment Rate | Lift | Status |
|------|--------------|----------------|------|--------|
| Day 1 | 9.8% | 11.5% | +17.3% | → Early |
| Day 5 | 10.2% | 12.3% | +20.6% | ✅ Strong |
| Day 10 | 9.9% | 11.9% | +20.2% | ✅ Strong |
| Day 15 | 10.1% | 12.1% | +19.8% | ✅ Strong |

**Trend**: Effect consistent throughout experiment (no decay).

---

## Financial Impact

### Projected Annual Impact

**Current State** (Control):
- Conversion rate: 10.0%
- Monthly users: 300,000
- Monthly conversions: 30,000
- Monthly revenue: $450,000
- Annual revenue: $5.4M

**If Treatment Ships** (+20% lift):
- Conversion rate: 12.0%
- Monthly conversions: 36,000 (+6,000)
- Monthly revenue: $540,000 (+$90,000)
- **Annual revenue: $6.48M (+$1.08M)** 💰

**ROI**: Implementation cost $[X] → Annual benefit $1.08M → **ROI: [Y]x**

---

## Risk Assessment

### Potential Risks

| Risk | Likelihood | Severity | Mitigation |
|------|-----------|----------|------------|
| [Risk 1] | Low | Low | [How to handle] |
| [Risk 2] | Medium | Low | [How to handle] |

**Overall Risk Level**: ✅ Low (safe to ship)

---

## Decision & Recommendation

### SHIP IT ✅

**Reasoning**:
1. ✅ Statistically significant 20% improvement (p < 0.001)
2. ✅ Meaningful business impact: +$1.08M annual revenue
3. ✅ No negative effects on guardrail metrics
4. ✅ Consistent improvement across all segments
5. ✅ Sufficient sample size and experiment duration
6. ✅ No validity concerns (SRM, novelty effects, data quality)
7. ✅ Low risk, high reward

**Expected Impact** (per 10,000 users per day):
- +200 conversions per day
- +$30,000 revenue per day
- +$900,000 revenue per month
- No increase in churn or support load

---

## Implementation Plan

### Rollout Strategy

**Phase 1: Ship to 100%** (Immediate)
- [ ] Deploy treatment to production
- [ ] Remove control variant
- [ ] Update analytics tracking

**Phase 2: Monitor** (Week 1)
- [ ] Watch for regressions
- [ ] Check error rates
- [ ] Monitor support tickets
- [ ] Validate revenue impact

**Phase 3: Document** (Week 2)
- [ ] Document learnings
- [ ] Share results with team
- [ ] Update best practices

**Rollback Plan**: If issues detected, revert to control within 1 hour.

---

## Learnings & Next Steps

### Key Learnings

1. **[Learning 1]**: [What we learned from this experiment]
2. **[Learning 2]**: [Another learning]
3. **[Learning 3]**: [Another learning]

### Future Experiments

Based on this success, we should test:

1. **[Test idea 1]**: [Description and expected impact]
2. **[Test idea 2]**: [Description and expected impact]
3. **[Test idea 3]**: [Description and expected impact]

---

## Appendix

### SQL Queries

All analysis queries available in:
- `analytics/experiments/exp_[id]_main_analysis.sql`
- `analytics/experiments/exp_[id]_segments.sql`
- `analytics/experiments/exp_[id]_secondary_metrics.sql`
- `analytics/experiments/exp_[id]_trends.sql`

### Screenshots

- [Link to treatment screenshot]
- [Link to control screenshot]
- [Link to analytics dashboard]

### References

- [Link to original hypothesis doc]
- [Link to design mocks]
- [Link to implementation PR]

---

**Report Version**: 1.0
**Created**: [Date]
**Reviewed By**: [@pm-name], [@data-science-lead]
**Approved**: [Date]
**Shipped**: [Date or TBD]
