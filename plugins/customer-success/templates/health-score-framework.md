# Customer Health Score Framework

## Health Score Calculation

**Total Score**: 100 points

### 1. Usage Health (30 points)

**Active Users** (12 points):
- 0-25% of licenses: 0-3 points
- 26-50% of licenses: 4-6 points
- 51-75% of licenses: 7-9 points
- 76-100% of licenses: 10-12 points

**Login Frequency** (9 points):
- <1x per week: 0-2 points
- 1-2x per week: 3-5 points
- 3-5x per week: 6-7 points
- Daily: 8-9 points

**Feature Adoption** (9 points):
- <25% of features: 0-2 points
- 25-50% of features: 3-5 points
- 51-75% of features: 6-7 points
- >75% of features: 8-9 points

### 2. Engagement Health (25 points)

**Email Response Rate** (8 points):
- <25%: 0-2 points
- 25-50%: 3-4 points
- 51-75%: 5-6 points
- >75%: 7-8 points

**Meeting Attendance** (8 points):
- <50%: 0-2 points
- 50-70%: 3-5 points
- 71-90%: 6-7 points
- >90%: 8 points

**Days Since Last Contact** (9 points):
- >30 days: 0-2 points
- 15-30 days: 3-5 points
- 8-14 days: 6-7 points
- <7 days: 8-9 points

### 3. Support Health (20 points)

**Ticket Volume** (7 points):
- High (above baseline): 0-2 points
- Moderate: 3-4 points
- Low: 5-6 points
- Very low: 7 points

**Critical Issues** (6 points):
- 2+ open: 0-1 points
- 1 open: 2-3 points
- 0 open, recent history: 4-5 points
- 0 open or closed: 6 points

**Support Satisfaction** (7 points):
- <3.0/5: 0-2 points
- 3.0-3.9/5: 3-4 points
- 4.0-4.4/5: 5-6 points
- 4.5-5.0/5: 7 points

### 4. Satisfaction Health (15 points)

**NPS Score** (7 points):
- Detractor (0-6): 0-2 points
- Passive (7-8): 3-5 points
- Promoter (9-10): 6-7 points

**CSAT Score** (8 points):
- <3.5/5: 0-2 points
- 3.5-3.9/5: 3-4 points
- 4.0-4.4/5: 5-6 points
- 4.5-5.0/5: 7-8 points

### 5. Financial Health (10 points)

**Payment Status** (5 points):
- >30 days overdue: 0 points
- 1-30 days overdue: 2 points
- Current: 5 points

**Expansion/Growth** (5 points):
- Contraction: 0-1 points
- Flat: 2-3 points
- Growth: 4-5 points

## Health Status Classification

- **80-100 points**: 🟢 Healthy (Low risk, expansion opportunity)
- **50-79 points**: 🟡 At Risk (Monitor closely, intervention needed)
- **0-49 points**: 🔴 Critical (High churn risk, urgent action)

## Monitoring Cadence

- **Green**: Monthly review
- **Yellow**: Bi-weekly review
- **Red**: Weekly review + escalation

## Action Triggers

**Yellow Alert** (Score drops below 80):
- Schedule executive check-in
- Conduct usage audit
- Increase touch-point frequency
- Address specific concerns

**Red Alert** (Score drops below 50):
- Immediate escalation to leadership
- Emergency response plan
- Daily monitoring
- C-level engagement
