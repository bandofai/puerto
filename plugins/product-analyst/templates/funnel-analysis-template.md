# Funnel Analysis Report Template

**Use this template for comprehensive funnel analysis and optimization recommendations**

---

## Funnel Analysis: [Funnel Name]

**Date**: [Analysis date]
**Analyst**: [Your name]
**Stakeholders**: [Product, Engineering, Design, Growth teams]

---

## Executive Summary

- **Overall Conversion Rate**: [X]% (from step 1 to goal)
- **Biggest Drop-Off**: [Step Name] → [Next Step] ([X]% loss)
- **Top Recommendation**: [Priority #1 action item]
- **Potential Impact**: +[X]% conversion improvement = +[Y] conversions per day

---

## Funnel Overview

**Goal**: [What constitutes success for this funnel]

**Time Window**: [How long users have to complete the funnel]

**Analysis Period**: [Date range analyzed]

**Sample Size**: [Number of users who entered funnel]

**Steps**:
1. **[Step 1 Name]**: [Description of what user does]
2. **[Step 2 Name]**: [Description]
3. **[Step 3 Name]**: [Description]
4. **[Step 4 Name]**: [Description]
5. **Goal: [Goal Name]**: [Final success action]

---

## Conversion Metrics

| Step | Users | Conversion % | Drop-Off % | Median Time | Status |
|------|-------|--------------|------------|-------------|--------|
| 1. [Step Name] | 10,000 | 100% | - | - | ✅ Entry |
| 2. [Step Name] | 7,500 | 75% | 25% | 2.3 min | ⚠️ High drop-off |
| 3. [Step Name] | 5,625 | 56.3% | 25% | 5.1 min | ✅ Normal |
| 4. [Step Name] | 3,938 | 39.4% | 30% | 3.2 min | ✅ Normal |
| Goal: [Goal Name] | 2,363 | 23.6% | 40% | 8.7 min | 🔴 Critical drop-off |

**Overall Conversion**: 23.6% (2,363 / 10,000)

**Industry Benchmark**: [X]%

**Status**: [Above/Below/At] benchmark

---

## Visualization

```
Step 1: [Step Name]        10,000 users  100%  |████████████████████|
                                    ↓ -25%
Step 2: [Step Name]         7,500 users   75%  |███████████████     |
                                    ↓ -25%
Step 3: [Step Name]         5,625 users   56%  |███████████         |
                                    ↓ -30%
Step 4: [Step Name]         3,938 users   39%  |████████            |
                                    ↓ -40%
Goal: [Goal Name]           2,363 users   24%  |█████               |
```

---

## Key Findings

### 1. 🔴 Critical: High Drop-Off at [Step Name → Next Step]

**Drop-off**: 40% of users abandon ([Number] users lost)

**Likely Causes** (based on data + qualitative research):
- [Hypothesis 1 with supporting evidence]
- [Hypothesis 2 with supporting evidence]
- [Hypothesis 3 with supporting evidence]

**Evidence**:
- Session recordings show [user behavior pattern]
- Heatmaps indicate [click/attention pattern]
- Exit surveys mention [common feedback]
- Support tickets about [specific issues]

---

### 2. ⚠️ Warning: Above-Average Time at [Step Name]

**Median Time**: 8.7 minutes (vs 2-3 min for other steps)

**Indicates**: Friction, confusion, or complex process

**Observations**:
- [Specific observation from data]
- [Another observation]

---

### 3. ✅ Positive: [Step Name] Performing Well

**Drop-off**: Only 25% (below industry average of 35%)

**Why it works**:
- [Success factor 1]
- [Success factor 2]

---

## Segment Analysis

### By Device Type

| Device | Entry Users | Conversions | Conversion Rate | vs Overall |
|--------|-------------|-------------|-----------------|------------|
| Desktop | 5,000 | 1,400 | 28.0% | +4.4pp ↗️ |
| Mobile | 4,500 | 850 | 18.9% | -4.7pp ↘️ |
| Tablet | 500 | 113 | 22.6% | -1.0pp ↘️ |

**Insight**: Mobile conversion significantly lower. Investigate mobile UX issues.

---

### By User Type

| User Type | Entry Users | Conversions | Conversion Rate | vs Overall |
|-----------|-------------|-------------|-----------------|------------|
| New Users | 6,000 | 1,200 | 20.0% | -3.6pp ↘️ |
| Returning Users | 4,000 | 1,163 | 29.1% | +5.5pp ↗️ |

**Insight**: Returning users convert better (trust, familiarity). Improve onboarding for new users.

---

### By Traffic Source

| Source | Entry Users | Conversions | Conversion Rate | vs Overall |
|--------|-------------|-------------|-----------------|------------|
| Organic Search | 3,500 | 945 | 27.0% | +3.4pp ↗️ |
| Paid Search | 2,500 | 550 | 22.0% | -1.6pp ↘️ |
| Social | 2,000 | 400 | 20.0% | -3.6pp ↘️ |
| Direct | 1,500 | 398 | 26.5% | +2.9pp ↗️ |
| Referral | 500 | 70 | 14.0% | -9.6pp ↘️ |

**Insight**: Referral traffic converts poorly. Review referral messaging and landing page fit.

---

## Recommendations (Prioritized)

### 🚀 High Priority (Quick Wins)

#### 1. [Recommendation Name]
- **Issue**: [Problem identified from data]
- **Action**: [Specific change to implement]
- **Expected Impact**: +[X]% conversion ([Y] additional conversions/day)
- **Effort**: Low [1-2 days]
- **Owner**: [@team-member]
- **Timeline**: Ship by [date]

**Implementation**:
```
- [ ] [Specific task 1]
- [ ] [Specific task 2]
- [ ] [Specific task 3]
```

---

#### 2. [Recommendation Name]
- **Issue**: [Problem]
- **Action**: [Solution]
- **Expected Impact**: +[X]% conversion
- **Effort**: Low
- **Owner**: [@team-member]
- **Timeline**: [Date]

---

### ⚡ Medium Priority (Moderate Effort, High Impact)

#### 3. [Recommendation Name]
- **Issue**: [Problem]
- **Action**: [Solution]
- **Expected Impact**: +[X]% conversion
- **Effort**: Medium [1-2 weeks]
- **Owner**: [@team-member]
- **Timeline**: [Date]

---

#### 4. [Recommendation Name]
- **Issue**: [Problem]
- **Action**: [Solution]
- **Expected Impact**: +[X]% conversion
- **Effort**: Medium
- **Owner**: [@team-member]
- **Timeline**: [Date]

---

### 📋 Low Priority (Long-term Investments)

#### 5. [Recommendation Name]
- **Issue**: [Problem]
- **Action**: [Solution]
- **Expected Impact**: +[X]% conversion
- **Effort**: High [1+ months]
- **Owner**: [@team-member]
- **Timeline**: [Quarter]

---

## Proposed A/B Tests

### Test 1: [Test Name]

**Hypothesis**: We believe [change] will increase [metric] by [amount] because [reasoning]

**Control**: Current experience ([description])

**Treatment**: [Description of change]

**Primary Metric**: [Funnel step] conversion rate

**Secondary Metrics**:
- [Metric 1]
- [Metric 2]

**Sample Size Needed**: [X] users per variant

**Runtime**: [Y] days

**Success Criteria**: +[Z]% improvement, statistically significant (p < 0.05)

---

### Test 2: [Test Name]

[Same structure as Test 1]

---

### Test 3: [Test Name]

[Same structure as Test 1]

---

## Competitive Benchmarks

| Competitor | Funnel Type | Reported Conversion | Source |
|------------|-------------|---------------------|--------|
| [Competitor A] | [Similar funnel] | [X]% | [Source] |
| [Competitor B] | [Similar funnel] | [Y]% | [Source] |
| Industry Average | [Funnel type] | [Z]% | [Source] |

**Our Performance**: [Above/Below/At] industry average by [X]pp

---

## Technical Considerations

### Performance Issues

- [Step Name] loads in [X] seconds (target: < 2s)
- [Another step] has [Y]% error rate
- Mobile responsiveness issues on [screens]

### Implementation Requirements

- [ ] [Technical requirement 1]
- [ ] [Technical requirement 2]
- [ ] [Technical requirement 3]

---

## Next Steps

### Immediate (This Week)
1. [Action item with owner]
2. [Action item with owner]
3. [Action item with owner]

### Short-term (This Month)
1. [Action item with owner]
2. [Action item with owner]

### Long-term (This Quarter)
1. [Action item with owner]
2. [Action item with owner]

---

## Appendix

### Methodology

**Data Sources**:
- Event tracking from [analytics platform]
- Session recordings from [tool]
- User surveys from [tool]

**Analysis Period**: [Dates]

**Filters Applied**:
- Excluded test accounts
- Excluded bot traffic
- Excluded incomplete sessions < [X] seconds

**Time Window**: [X] hours/days from first step to goal

---

### SQL Queries

All analysis queries available in:
- `analytics/funnels/[funnel_name]_overall.sql`
- `analytics/funnels/[funnel_name]_segments.sql`
- `analytics/funnels/[funnel_name]_time_analysis.sql`
- `analytics/funnels/[funnel_name]_trends.sql`

---

### Change Log

| Date | Change | Impact | Owner |
|------|--------|--------|-------|
| [Date] | [Description] | [Conversion change] | [@name] |
| [Date] | [Description] | [Conversion change] | [@name] |

---

**Report Version**: 1.0
**Created**: [Date]
**Last Updated**: [Date]
**Next Review**: [Date] (or after implementing top 3 recommendations)
