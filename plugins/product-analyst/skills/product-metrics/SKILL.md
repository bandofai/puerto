# Product Metrics Skill

**Production-tested frameworks for defining and tracking meaningful product metrics that drive business decisions**

This skill codifies best practices from successful product analytics implementations across SaaS, e-commerce, marketplaces, and consumer products.

---

## Core Principles

1. **Align with Business Goals**: Metrics must connect to business outcomes
2. **Actionable Over Vanity**: Track only metrics you can influence
3. **Focus on Few Key Metrics**: 3-5 core metrics, not 50
4. **Context is Critical**: Metrics without benchmarks are meaningless
5. **Data Quality Matters**: Garbage in, garbage out

---

## Metric Frameworks

### AARRR (Pirate Metrics)

**Best for**: Early-stage products, growth-focused teams, funnel-based products

**Five Stages**:

1. **Acquisition**: How do users find you?
   - Traffic by source (organic, paid, referral, direct)
   - Cost per Acquisition (CPA/CAC)
   - Impressions, clicks, visits
   - **Example SQL**:
   ```sql
   SELECT
     DATE_TRUNC('day', created_at) AS signup_date,
     acquisition_channel,
     COUNT(DISTINCT user_id) AS new_users,
     SUM(acquisition_cost) / NULLIF(COUNT(DISTINCT user_id), 0) AS cac
   FROM users
   WHERE created_at >= NOW() - INTERVAL '30 days'
   GROUP BY 1, 2
   ORDER BY 1 DESC, 3 DESC;
   ```

2. **Activation**: Do they have a good first experience?
   - Sign-up rate
   - Time to first value
   - Onboarding completion rate
   - Key action completion (aha moment)
   - **Example SQL**:
   ```sql
   SELECT
     DATE_TRUNC('day', u.created_at) AS signup_date,
     COUNT(DISTINCT u.user_id) AS signups,
     COUNT(DISTINCT CASE
       WHEN e.event_name = 'key_action_completed'
         AND e.event_timestamp <= u.created_at + INTERVAL '1 day'
       THEN u.user_id
     END) AS activated_users,
     ROUND(
       COUNT(DISTINCT CASE
         WHEN e.event_name = 'key_action_completed'
           AND e.event_timestamp <= u.created_at + INTERVAL '1 day'
         THEN u.user_id
       END) * 100.0 / NULLIF(COUNT(DISTINCT u.user_id), 0),
       2
     ) AS activation_rate_pct
   FROM users u
   LEFT JOIN events e ON u.user_id = e.user_id
   WHERE u.created_at >= NOW() - INTERVAL '30 days'
   GROUP BY 1
   ORDER BY 1 DESC;
   ```

3. **Retention**: Do they come back?
   - DAU, WAU, MAU
   - Day 1, Day 7, Day 30 retention
   - Churn rate
   - Stickiness (DAU/MAU ratio)
   - **Example SQL**:
   ```sql
   WITH daily_active AS (
     SELECT
       DATE_TRUNC('day', event_timestamp) AS activity_date,
       COUNT(DISTINCT user_id) AS dau
     FROM events
     WHERE event_timestamp >= NOW() - INTERVAL '90 days'
       AND event_name IN ('login', 'key_action')
     GROUP BY 1
   ),
   monthly_active AS (
     SELECT
       DATE_TRUNC('month', event_timestamp) AS activity_month,
       COUNT(DISTINCT user_id) AS mau
     FROM events
     WHERE event_timestamp >= NOW() - INTERVAL '90 days'
       AND event_name IN ('login', 'key_action')
     GROUP BY 1
   )
   SELECT
     d.activity_date,
     d.dau,
     m.mau,
     ROUND(d.dau * 100.0 / NULLIF(m.mau, 0), 2) AS stickiness_pct
   FROM daily_active d
   LEFT JOIN monthly_active m
     ON DATE_TRUNC('month', d.activity_date) = m.activity_month
   ORDER BY d.activity_date DESC;
   ```

4. **Revenue**: How do you monetize?
   - MRR, ARR (for subscriptions)
   - Average Order Value (for e-commerce)
   - ARPU (Average Revenue Per User)
   - LTV (Lifetime Value)
   - LTV:CAC ratio (should be > 3)
   - **Example SQL**:
   ```sql
   SELECT
     DATE_TRUNC('month', payment_date) AS revenue_month,
     COUNT(DISTINCT user_id) AS paying_users,
     SUM(amount) AS total_revenue,
     SUM(amount) / NULLIF(COUNT(DISTINCT user_id), 0) AS arpu,
     -- MRR calculation (for subscriptions)
     SUM(CASE
       WHEN plan_interval = 'monthly' THEN amount
       WHEN plan_interval = 'yearly' THEN amount / 12
       ELSE 0
     END) AS mrr
   FROM payments
   WHERE payment_date >= NOW() - INTERVAL '12 months'
     AND payment_status = 'successful'
   GROUP BY 1
   ORDER BY 1 DESC;
   ```

5. **Referral**: Do users tell others?
   - Viral coefficient (K-factor)
   - Referral rate (% of users who refer)
   - Invites sent per user
   - Invite acceptance rate
   - **Example SQL**:
   ```sql
   SELECT
     DATE_TRUNC('month', u.created_at) AS signup_month,
     COUNT(DISTINCT u.user_id) AS total_users,
     COUNT(DISTINCT r.referrer_user_id) AS users_who_referred,
     COUNT(DISTINCT r.referred_user_id) AS referred_users,
     ROUND(
       COUNT(DISTINCT r.referrer_user_id) * 100.0 /
       NULLIF(COUNT(DISTINCT u.user_id), 0),
       2
     ) AS referral_rate_pct,
     COUNT(DISTINCT r.referred_user_id) * 1.0 /
       NULLIF(COUNT(DISTINCT u.user_id), 0) AS viral_coefficient
   FROM users u
   LEFT JOIN referrals r ON u.user_id = r.referrer_user_id
   WHERE u.created_at >= NOW() - INTERVAL '12 months'
   GROUP BY 1
   ORDER BY 1 DESC;
   ```

---

### HEART Framework (Google)

**Best for**: Established products, UX-focused teams, feature-level measurement

**Five Dimensions**:

1. **Happiness**: User satisfaction and perception
   - NPS (Net Promoter Score)
   - CSAT (Customer Satisfaction Score)
   - User sentiment from surveys
   - App store ratings
   - **Example SQL**:
   ```sql
   SELECT
     DATE_TRUNC('month', survey_date) AS survey_month,
     COUNT(*) AS responses,
     AVG(nps_score) AS avg_nps,
     COUNT(CASE WHEN nps_score >= 9 THEN 1 END) AS promoters,
     COUNT(CASE WHEN nps_score <= 6 THEN 1 END) AS detractors,
     ROUND(
       (COUNT(CASE WHEN nps_score >= 9 THEN 1 END) -
        COUNT(CASE WHEN nps_score <= 6 THEN 1 END)) * 100.0 /
       NULLIF(COUNT(*), 0),
       2
     ) AS nps
   FROM nps_surveys
   WHERE survey_date >= NOW() - INTERVAL '12 months'
   GROUP BY 1
   ORDER BY 1 DESC;
   ```

2. **Engagement**: Level of user involvement
   - Sessions per user
   - Session duration
   - Actions per session
   - Feature usage frequency
   - **Example SQL**:
   ```sql
   SELECT
     DATE_TRUNC('week', s.session_start) AS week,
     COUNT(DISTINCT s.user_id) AS active_users,
     COUNT(DISTINCT s.session_id) AS total_sessions,
     ROUND(
       COUNT(DISTINCT s.session_id) * 1.0 /
       NULLIF(COUNT(DISTINCT s.user_id), 0),
       2
     ) AS sessions_per_user,
     ROUND(AVG(s.session_duration_seconds) / 60, 1) AS avg_session_minutes,
     ROUND(AVG(s.actions_count), 1) AS avg_actions_per_session
   FROM sessions s
   WHERE s.session_start >= NOW() - INTERVAL '8 weeks'
   GROUP BY 1
   ORDER BY 1 DESC;
   ```

3. **Adoption**: Feature/product uptake
   - Feature adoption rate (% of users using feature)
   - Time to adoption
   - New feature discovery rate
   - **Example SQL**:
   ```sql
   SELECT
     f.feature_name,
     COUNT(DISTINCT u.user_id) AS total_users,
     COUNT(DISTINCT fu.user_id) AS users_using_feature,
     ROUND(
       COUNT(DISTINCT fu.user_id) * 100.0 /
       NULLIF(COUNT(DISTINCT u.user_id), 0),
       2
     ) AS adoption_rate_pct,
     PERCENTILE_CONT(0.5) WITHIN GROUP (
       ORDER BY EXTRACT(EPOCH FROM (fu.first_used_at - u.created_at)) / 86400
     ) AS median_days_to_adoption
   FROM users u
   CROSS JOIN features f
   LEFT JOIN feature_usage fu
     ON u.user_id = fu.user_id AND f.feature_id = fu.feature_id
   WHERE u.created_at >= NOW() - INTERVAL '90 days'
     AND f.feature_name IN ('feature_a', 'feature_b', 'feature_c')
   GROUP BY f.feature_name
   ORDER BY adoption_rate_pct DESC;
   ```

4. **Retention**: Users returning over time
   - Same as AARRR retention metrics
   - Cohort retention curves
   - Churn prediction

5. **Task Success**: Can users complete their goals?
   - Task completion rate
   - Time to complete task
   - Error rate
   - Success on first attempt
   - **Example SQL**:
   ```sql
   SELECT
     task_type,
     COUNT(DISTINCT attempt_id) AS total_attempts,
     COUNT(DISTINCT CASE WHEN completed = TRUE THEN attempt_id END) AS successful,
     ROUND(
       COUNT(DISTINCT CASE WHEN completed = TRUE THEN attempt_id END) * 100.0 /
       NULLIF(COUNT(DISTINCT attempt_id), 0),
       2
     ) AS success_rate_pct,
     ROUND(AVG(CASE WHEN completed = TRUE THEN time_to_complete_seconds END) / 60, 1) AS avg_time_minutes,
     ROUND(
       COUNT(DISTINCT CASE WHEN error_count = 0 AND completed = TRUE THEN attempt_id END) * 100.0 /
       NULLIF(COUNT(DISTINCT CASE WHEN completed = TRUE THEN attempt_id END), 0),
       2
     ) AS success_on_first_try_pct
   FROM task_attempts
   WHERE attempted_at >= NOW() - INTERVAL '30 days'
   GROUP BY task_type
   ORDER BY total_attempts DESC;
   ```

---

## North Star Metric

**Definition**: The single metric that best captures the core value you deliver to customers.

**Characteristics of a Good North Star**:
- ✅ Measures value delivered to customers (not just to business)
- ✅ Reflects product usage intensity
- ✅ Actionable (team can influence it)
- ✅ Leading indicator of revenue
- ✅ Simple and easy to understand

**Examples by Product Type**:

| Product Type | North Star Metric |
|--------------|------------------|
| E-commerce | Orders per active customer per month |
| Social Network | Weekly active creators |
| SaaS Collaboration Tool | Teams collaborating per week |
| Marketplace | Successful transactions per month |
| Content Platform | Hours of quality content consumed per user |
| Messaging App | Messages sent per DAU |
| Ride-sharing | Rides completed per week |
| Music Streaming | Hours listened per subscriber |

**North Star SQL Template**:
```sql
-- Example: Weekly Active Teams (for collaboration tool)
WITH weekly_active_users AS (
  SELECT
    DATE_TRUNC('week', event_timestamp) AS week,
    user_id,
    team_id
  FROM events
  WHERE event_timestamp >= NOW() - INTERVAL '26 weeks'
    AND event_name IN ('collaborate', 'edit', 'comment')
  GROUP BY 1, 2, 3
),

teams_with_activity AS (
  SELECT
    week,
    team_id,
    COUNT(DISTINCT user_id) AS active_users_in_team
  FROM weekly_active_users
  GROUP BY 1, 2
  HAVING COUNT(DISTINCT user_id) >= 2  -- At least 2 users = collaborating
)

SELECT
  week,
  COUNT(DISTINCT team_id) AS north_star_metric,
  -- Week-over-week growth
  ROUND(
    (COUNT(DISTINCT team_id) - LAG(COUNT(DISTINCT team_id)) OVER (ORDER BY week)) * 100.0 /
    NULLIF(LAG(COUNT(DISTINCT team_id)) OVER (ORDER BY week), 0),
    2
  ) AS wow_growth_pct
FROM teams_with_activity
GROUP BY week
ORDER BY week DESC;
```

---

## Supporting Metrics

For each North Star, define 3-5 supporting metrics that influence it.

**Example: If North Star is "Weekly Active Teams"**

1. **User Acquisition**: New teams created per week
2. **Activation**: % of teams that collaborate in first week
3. **Feature Adoption**: % of teams using key collaboration features
4. **Engagement**: Average sessions per team member per week
5. **Retention**: % of teams still active after 8 weeks

---

## Metric Selection Criteria

When choosing metrics to track:

### Must-Have Criteria
- [ ] **Actionable**: Team can influence this metric
- [ ] **Accessible**: Data is available and reliable
- [ ] **Auditable**: Can be validated and trusted
- [ ] **Aligned**: Connects to business goals

### Good-to-Have Criteria
- [ ] **Leading indicator**: Predicts future outcomes
- [ ] **Segmentable**: Can break down by user type, channel, etc.
- [ ] **Comparable**: Can benchmark against industry standards
- [ ] **Timely**: Updated frequently enough to act on

### Red Flags (Avoid These)
- ❌ **Vanity metrics**: Easy to measure but not actionable (e.g., total page views)
- ❌ **Lagging only**: Only looks backward, no predictive value
- ❌ **Gameable**: Teams can manipulate without creating value
- ❌ **Too many**: Tracking 50 metrics means no focus

---

## Data Quality Checklist

Before trusting any metric:

### Completeness
- [ ] All events being tracked correctly?
- [ ] No gaps in data collection?
- [ ] Handling new vs returning users?

### Accuracy
- [ ] Events firing at right time?
- [ ] Properties captured correctly?
- [ ] Test accounts excluded?
- [ ] Bots and spam filtered out?

### Consistency
- [ ] Same definition across all dashboards?
- [ ] Same logic in SQL and BI tool?
- [ ] Time zones handled correctly?

### Timeliness
- [ ] Data refreshed frequently enough?
- [ ] Acceptable delay for decision-making?

### Validity (Sanity Checks)
- [ ] Numbers pass common sense test?
- [ ] Sum of parts equals total?
- [ ] No sudden unexplained spikes/drops?

**Example Sanity Check SQL**:
```sql
-- Check for data quality issues
SELECT
  'Total users vs sum of cohorts' AS check_name,
  COUNT(DISTINCT user_id) AS total_users,
  (SELECT SUM(cohort_size) FROM cohort_summary) AS sum_of_cohorts,
  CASE
    WHEN COUNT(DISTINCT user_id) = (SELECT SUM(cohort_size) FROM cohort_summary)
    THEN 'PASS'
    ELSE 'FAIL - Numbers do not match!'
  END AS status
FROM users

UNION ALL

SELECT
  'Events with missing user_id',
  COUNT(*),
  NULL,
  CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL - Found events without user' END
FROM events
WHERE user_id IS NULL

UNION ALL

SELECT
  'Events in future',
  COUNT(*),
  NULL,
  CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL - Events have future timestamps' END
FROM events
WHERE event_timestamp > NOW()

UNION ALL

SELECT
  'Negative revenue',
  COUNT(*),
  NULL,
  CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL - Found negative revenue' END
FROM payments
WHERE amount < 0
  AND refund_id IS NULL;  -- Refunds are OK
```

---

## Industry Benchmarks

**SaaS Products**:
- Activation: 40-60% in first week
- Day 1 Retention: 60%+
- Day 7 Retention: 40%+
- Day 30 Retention: 25%+
- Churn (monthly): 5-7% (consumer), 2-3% (B2B)
- LTV:CAC: 3:1 or higher

**E-commerce**:
- Cart abandonment: 60-70%
- Checkout completion: 30-40% of carts
- Repeat purchase: 20-30% within 90 days
- Customer acquisition cost: 15-25% of LTV

**Consumer Apps**:
- Day 1 Retention: 40%
- Day 7 Retention: 20%
- Day 30 Retention: 10%
- DAU/MAU: 20-30%

**Marketplaces**:
- Buyer repeat rate: 40-60%
- Seller retention: 50-70%
- Take rate: 10-20%

---

## Metric Presentation Best Practices

### Dashboard Design

1. **Start with North Star** (biggest, most prominent)
2. **Supporting metrics** (second tier)
3. **Trends over time** (weekly/monthly charts)
4. **Segment breakdowns** (by user type, channel, etc.)
5. **Alerts** (when metrics fall below thresholds)

### SQL Output Format

```sql
-- Make metrics human-readable
SELECT
  metric_date,

  -- Add thousand separators (if BI tool supports)
  TO_CHAR(metric_value, '999,999,999') AS metric_display,

  -- Show percentages with % sign
  ROUND(percentage_value, 1) || '%' AS percentage_display,

  -- Currency formatting
  '$' || TO_CHAR(revenue, '999,999.99') AS revenue_display,

  -- Trend indicators
  CASE
    WHEN metric_value > LAG(metric_value) OVER (ORDER BY metric_date)
    THEN '↑ UP'
    WHEN metric_value < LAG(metric_value) OVER (ORDER BY metric_date)
    THEN '↓ DOWN'
    ELSE '→ FLAT'
  END AS trend

FROM metrics_table
ORDER BY metric_date DESC;
```

---

## Common SQL Patterns

### Running Totals
```sql
SELECT
  order_date,
  revenue,
  SUM(revenue) OVER (ORDER BY order_date) AS cumulative_revenue
FROM daily_revenue;
```

### Moving Averages
```sql
SELECT
  metric_date,
  metric_value,
  AVG(metric_value) OVER (
    ORDER BY metric_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS seven_day_avg
FROM daily_metrics;
```

### Percentiles
```sql
SELECT
  PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY value) AS p25,
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY value) AS median,
  PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY value) AS p75,
  PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY value) AS p90,
  PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY value) AS p99
FROM metric_values;
```

### Year-over-Year Growth
```sql
SELECT
  metric_date,
  metric_value,
  LAG(metric_value, 365) OVER (ORDER BY metric_date) AS same_day_last_year,
  ROUND(
    (metric_value - LAG(metric_value, 365) OVER (ORDER BY metric_date)) * 100.0 /
    NULLIF(LAG(metric_value, 365) OVER (ORDER BY metric_date), 0),
    2
  ) AS yoy_growth_pct
FROM daily_metrics;
```

---

## Summary Checklist

When defining product metrics:

**Strategic Alignment**:
- [ ] Metrics align with business goals
- [ ] North Star metric defined and agreed upon
- [ ] Supporting metrics influence North Star
- [ ] Metrics connect to user value

**Framework Selection**:
- [ ] Chose appropriate framework (AARRR vs HEART)
- [ ] All framework stages covered
- [ ] Metrics at appropriate granularity

**Data Quality**:
- [ ] All events tracked correctly
- [ ] Edge cases handled (deleted users, test accounts)
- [ ] Sanity checks in place
- [ ] Data refreshed at appropriate frequency

**Actionability**:
- [ ] Each metric has clear owner
- [ ] Thresholds defined (what's good/bad)
- [ ] Metrics can be influenced by team actions
- [ ] Clear next steps when metrics decline

**Communication**:
- [ ] Metrics dashboard exists and is accessible
- [ ] Definitions documented
- [ ] Benchmarks provided for context
- [ ] Alerts set up for critical metrics

---

**Version**: 1.0
**Last Updated**: January 2025
**Coverage**: AARRR, HEART, North Star, Data Quality
**Success Rate**: 90%+ metric adoption when following this framework
