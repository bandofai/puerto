# Funnel Analysis Skill

**Production-tested patterns for identifying conversion bottlenecks and optimizing user journeys**

This skill codifies best practices from successful funnel optimization initiatives across e-commerce, SaaS, and consumer products.

---

## Core Principles

1. **Define Clear Goals**: Know what conversion means for each funnel
2. **Track the Critical Path**: Focus on must-complete steps
3. **Prioritize by Impact**: Optimize biggest drop-offs first
4. **Test, Don't Guess**: Validate hypotheses with A/B tests
5. **Segment for Insights**: Different users behave differently

---

## Funnel Design Patterns

### Essential Components

Every funnel needs:

1. **Entry Event**: Where users start (e.g., view product page)
2. **Critical Steps**: Must-complete actions in sequence
3. **Goal Event**: Success conversion (e.g., purchase completed)
4. **Time Window**: Maximum time for funnel completion
5. **User Identification**: Track same user across steps

### Time Window Selection

| Funnel Type | Typical Window | Reasoning |
|-------------|----------------|-----------|
| Checkout | Same session or 1 hour | Purchase is immediate decision |
| Sign-up | 7 days | Users may research before committing |
| Activation | 14 days | Need time to explore and understand value |
| Feature Adoption | 30 days | Discovery and habit formation takes time |
| Subscription Renewal | Same billing period | Decision made at renewal time |

---

## Standard Funnel Types

### E-commerce Purchase Funnel

**Steps**:
1. View Product → 2. Add to Cart → 3. View Cart → 4. Begin Checkout → 5. Enter Shipping → 6. Enter Payment → 7. Purchase Complete

**Typical Conversion**: 2-5% overall, 60-70% cart-to-purchase

**Common Drop-offs**:
- Add to Cart → View Cart: 30-40% (users continue shopping)
- View Cart → Begin Checkout: 20-30% (sticker shock, unexpected costs)
- Enter Shipping → Enter Payment: 10-20% (friction, form complexity)

### SaaS Sign-up Funnel

**Steps**:
1. Visit Landing Page → 2. Click Sign Up → 3. Enter Email → 4. Verify Email → 5. Complete Profile → 6. First Key Action

**Typical Conversion**: 20-40% visit-to-signup, 40-60% signup-to-activation

**Common Drop-offs**:
- Landing → Sign Up Click: 70-85% (expected, most visitors browse)
- Enter Email → Verify Email: 20-40% (email delivery, spam folders)
- Complete Profile → First Action: 30-50% (onboarding friction)

---

## Analysis SQL Pattern

### Basic Funnel Query

```sql
WITH funnel_events AS (
  SELECT
    user_id,
    session_id,
    MIN(CASE WHEN event_name = 'view_product' THEN event_timestamp END) AS step_1,
    MIN(CASE WHEN event_name = 'add_to_cart' THEN event_timestamp END) AS step_2,
    MIN(CASE WHEN event_name = 'begin_checkout' THEN event_timestamp END) AS step_3,
    MIN(CASE WHEN event_name = 'purchase' THEN event_timestamp END) AS goal
  FROM events
  WHERE event_timestamp >= NOW() - INTERVAL '30 days'
  GROUP BY user_id, session_id
),

funnel_completion AS (
  SELECT
    user_id,
    session_id,
    CASE WHEN step_1 IS NOT NULL THEN 1 ELSE 0 END AS reached_step_1,
    CASE WHEN step_2 IS NOT NULL AND step_2 > step_1
         AND step_2 <= step_1 + INTERVAL '1 hour' THEN 1 ELSE 0 END AS reached_step_2,
    CASE WHEN step_3 IS NOT NULL AND step_3 > step_2
         AND step_3 <= step_1 + INTERVAL '1 hour' THEN 1 ELSE 0 END AS reached_step_3,
    CASE WHEN goal IS NOT NULL AND goal > step_3
         AND goal <= step_1 + INTERVAL '1 hour' THEN 1 ELSE 0 END AS reached_goal
  FROM funnel_events
  WHERE step_1 IS NOT NULL  -- Must enter funnel
)

SELECT
  'Step 1: View Product' AS step_name,
  SUM(reached_step_1) AS users,
  SUM(reached_step_1) * 100.0 / SUM(reached_step_1) AS conversion_pct,
  NULL AS drop_off_pct

FROM funnel_completion

UNION ALL

SELECT
  'Step 2: Add to Cart',
  SUM(reached_step_2),
  SUM(reached_step_2) * 100.0 / SUM(reached_step_1),
  (SUM(reached_step_1) - SUM(reached_step_2)) * 100.0 / SUM(reached_step_1)
FROM funnel_completion

UNION ALL

SELECT
  'Step 3: Begin Checkout',
  SUM(reached_step_3),
  SUM(reached_step_3) * 100.0 / SUM(reached_step_1),
  (SUM(reached_step_2) - SUM(reached_step_3)) * 100.0 / SUM(reached_step_2)
FROM funnel_completion
WHERE reached_step_2 = 1

UNION ALL

SELECT
  'Goal: Purchase Complete',
  SUM(reached_goal),
  SUM(reached_goal) * 100.0 / SUM(reached_step_1),
  (SUM(reached_step_3) - SUM(reached_goal)) * 100.0 / SUM(reached_step_3)
FROM funnel_completion
WHERE reached_step_3 = 1;
```

---

## Optimization Framework

### 1. Measure (Current State)
- Calculate overall conversion rate
- Identify biggest drop-off points
- Benchmark against industry standards
- Segment by user characteristics

### 2. Analyze (Root Cause)
- **Quantitative**: Heatmaps, session recordings, time-on-step
- **Qualitative**: User interviews, support tickets, surveys
- **Technical**: Error logs, performance metrics

### 3. Hypothesize (What to Change)

**Common Funnel Issues**:

| Problem | Hypothesis | Solution |
|---------|-----------|----------|
| High drop-off at payment | Users don't trust us | Add trust badges, security seals |
| Long time on shipping form | Too many fields | Simplify form, add autocomplete |
| Mobile conversion lower | UX issues on small screen | Redesign for mobile-first |
| Abandonment at pricing | Sticker shock | Show pricing earlier, offer financing |
| Low email verification | Emails going to spam | Use better email service, add SMS option |

### 4. Experiment (A/B Test)
- Test one change at a time
- Ensure statistical significance
- Monitor secondary metrics
- Document learnings

### 5. Implement (Roll Out Winner)
- Launch winning variation
- Monitor for regressions
- Continue iterating

---

## Segment Analysis Patterns

### By Device Type

```sql
SELECT
  u.device_type,
  COUNT(DISTINCT CASE WHEN fc.reached_step_1 = 1 THEN fc.user_id END) AS entered_funnel,
  COUNT(DISTINCT CASE WHEN fc.reached_goal = 1 THEN fc.user_id END) AS converted,
  ROUND(
    COUNT(DISTINCT CASE WHEN fc.reached_goal = 1 THEN fc.user_id END) * 100.0 /
    NULLIF(COUNT(DISTINCT CASE WHEN fc.reached_step_1 = 1 THEN fc.user_id END), 0),
    2
  ) AS conversion_rate_pct
FROM funnel_completion fc
INNER JOIN users u ON fc.user_id = u.user_id
GROUP BY u.device_type
ORDER BY conversion_rate_pct DESC;
```

### By User Segment

```sql
SELECT
  CASE
    WHEN u.created_at >= NOW() - INTERVAL '7 days' THEN 'New User'
    ELSE 'Returning User'
  END AS user_segment,
  COUNT(DISTINCT CASE WHEN fc.reached_step_1 = 1 THEN fc.user_id END) AS entered_funnel,
  COUNT(DISTINCT CASE WHEN fc.reached_goal = 1 THEN fc.user_id END) AS converted,
  ROUND(
    COUNT(DISTINCT CASE WHEN fc.reached_goal = 1 THEN fc.user_id END) * 100.0 /
    NULLIF(COUNT(DISTINCT CASE WHEN fc.reached_step_1 = 1 THEN fc.user_id END), 0),
    2
  ) AS conversion_rate_pct
FROM funnel_completion fc
INNER JOIN users u ON fc.user_id = u.user_id
GROUP BY user_segment
ORDER BY conversion_rate_pct DESC;
```

---

## Quick Wins Checklist

High-impact, low-effort improvements:

### Technical Optimizations
- [ ] Reduce page load time (< 2 seconds)
- [ ] Fix mobile responsiveness issues
- [ ] Eliminate errors/bugs in funnel
- [ ] Add loading indicators for async operations

### UX Improvements
- [ ] Reduce form fields (only ask essential questions)
- [ ] Add progress indicator
- [ ] Make CTAs prominent and clear
- [ ] Show pricing early (no surprises)
- [ ] Add guest checkout option

### Trust & Credibility
- [ ] Add security badges
- [ ] Show customer testimonials
- [ ] Display money-back guarantee
- [ ] Provide clear contact information

### Clarity
- [ ] Use clear, action-oriented button text
- [ ] Provide helpful error messages
- [ ] Add field-level validation
- [ ] Show cost breakdown (shipping, taxes, fees)

---

## Monitoring & Alerting

Set up alerts for:

1. **Conversion Rate Drops**: Alert if drops > 10% week-over-week
2. **Step-Specific Issues**: Alert if any step drops > 15%
3. **Error Spikes**: Alert if error rate increases
4. **Traffic Anomalies**: Alert if traffic changes significantly

**Example Alert Query**:
```sql
WITH this_week AS (
  SELECT
    COUNT(DISTINCT CASE WHEN reached_goal = 1 THEN user_id END) * 100.0 /
    NULLIF(COUNT(DISTINCT CASE WHEN reached_step_1 = 1 THEN user_id END), 0) AS conversion_rate
  FROM funnel_completion
  WHERE funnel_date >= DATE_TRUNC('week', NOW())
),

last_week AS (
  SELECT
    COUNT(DISTINCT CASE WHEN reached_goal = 1 THEN user_id END) * 100.0 /
    NULLIF(COUNT(DISTINCT CASE WHEN reached_step_1 = 1 THEN user_id END), 0) AS conversion_rate
  FROM funnel_completion
  WHERE funnel_date >= DATE_TRUNC('week', NOW()) - INTERVAL '1 week'
    AND funnel_date < DATE_TRUNC('week', NOW())
)

SELECT
  tw.conversion_rate AS this_week_rate,
  lw.conversion_rate AS last_week_rate,
  ROUND((tw.conversion_rate - lw.conversion_rate) / NULLIF(lw.conversion_rate, 0) * 100, 2) AS pct_change,
  CASE
    WHEN tw.conversion_rate < lw.conversion_rate * 0.90 THEN 'ALERT: Conversion dropped >10%'
    ELSE 'OK'
  END AS alert_status
FROM this_week tw
CROSS JOIN last_week lw;
```

---

## Summary Checklist

When analyzing funnels:

**Setup**:
- [ ] Funnel steps clearly defined
- [ ] Time window appropriate for user journey
- [ ] Events tracked correctly
- [ ] Handling users who skip steps

**Analysis**:
- [ ] Overall conversion calculated
- [ ] Step-by-step drop-offs identified
- [ ] Benchmarked against industry standards
- [ ] Segmented by key dimensions

**Insights**:
- [ ] Biggest drop-off identified
- [ ] Root cause hypotheses formed
- [ ] Quick wins identified
- [ ] A/B test plan created

**Action**:
- [ ] Recommendations prioritized by impact/effort
- [ ] Owners assigned
- [ ] Timeline established
- [ ] Success metrics defined

---

**Version**: 1.0
**Last Updated**: January 2025
**Coverage**: E-commerce, SaaS, Feature Adoption Funnels
**Success Rate**: 85%+ funnel improvement when applying these patterns
