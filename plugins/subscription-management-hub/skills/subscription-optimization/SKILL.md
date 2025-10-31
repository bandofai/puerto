# Subscription Optimization Skill

Comprehensive patterns for subscription tracking, cost analysis, and optimization strategies used by Subscription Management Hub agents.

## Data Structures

### Core Subscription Schema

```json
{
  "id": "uuid-string",
  "name": "Service Name",
  "provider": "Company Name",
  "category": "streaming-video|streaming-music|software-saas|cloud-storage|...",
  "cost": 15.99,
  "billing_cycle": "monthly|annual|quarterly|biannual",
  "monthly_cost_equivalent": 15.99,
  "annual_cost_equivalent": 191.88,
  "currency": "USD",
  "status": "active|trial|cancelled|paused",
  "renewal_date": "2025-11-23",
  "trial_end_date": "2025-11-15",
  "cancellation_deadline": "2025-11-20",
  "auto_renew": true,
  "payment_method": "Visa *1234",
  "date_started": "2025-01-15T10:00:00Z",
  "date_cancelled": null,
  "last_used": "2025-10-20",
  "usage_frequency": "daily|weekly|biweekly|monthly|rarely|never|unknown",
  "website": "https://service.com",
  "login_email": "user@example.com",
  "notes": "Family plan, shared with 3 people",
  "alternatives": ["Alternative1", "Alternative2"],
  "tags": ["entertainment", "essential"],
  "metadata": {
    "plan_name": "Premium",
    "features": ["4K", "Multi-device"],
    "user_count": 4,
    "price_history": [
      {"date": "2024-01-01", "cost": 13.99},
      {"date": "2025-01-01", "cost": 15.99}
    ]
  }
}
```

### Database Structure

```json
{
  "version": "1.0",
  "created": "2025-01-15T10:00:00Z",
  "last_updated": "2025-10-23T10:00:00Z",
  "subscriptions": {
    "uuid-1": { /* subscription object */ },
    "uuid-2": { /* subscription object */ }
  },
  "metadata": {
    "total_subscriptions": 15,
    "active_subscriptions": 12,
    "cancelled_subscriptions": 2,
    "trial_subscriptions": 1,
    "total_monthly_cost": 234.50,
    "total_annual_cost": 2814.00,
    "by_category": {
      "streaming-video": {
        "count": 3,
        "monthly_cost": 45.00,
        "annual_cost": 540.00
      }
    }
  }
}
```

### Cost Analysis Report Schema

```json
{
  "version": "1.0",
  "report_date": "2025-10-23T10:00:00Z",
  "summary": {
    "total_monthly": 234.50,
    "total_annual": 2814.00,
    "average_per_subscription": 19.54,
    "most_expensive": {
      "name": "Adobe Creative Cloud",
      "monthly_cost": 54.99
    },
    "least_used": [
      {
        "name": "Unused Service",
        "last_used": "2025-01-15",
        "days_unused": 281,
        "monthly_cost": 9.99
      }
    ]
  },
  "by_category": {
    "streaming-video": {
      "count": 3,
      "monthly_cost": 45.00,
      "annual_cost": 540.00,
      "percentage_of_total": 19.2,
      "subscriptions": ["Netflix", "Hulu", "Disney+"]
    }
  },
  "recommendations": [
    {
      "priority": "HIGH",
      "type": "cancel_unused",
      "subscription": "Unused Service",
      "reasoning": "Not used in 9 months",
      "potential_savings_annual": 119.88
    }
  ]
}
```

### Cancellation Calendar Schema

```json
{
  "version": "1.0",
  "last_updated": "2025-10-23T10:00:00Z",
  "upcoming_renewals": [
    {
      "type": "renewal",
      "subscription_id": "uuid",
      "subscription_name": "Netflix",
      "date": "2025-11-23",
      "days_until": 31,
      "cost": 15.99,
      "billing_cycle": "monthly",
      "auto_renew": true
    }
  ],
  "trial_endings": [
    {
      "type": "trial_end",
      "subscription_id": "uuid",
      "subscription_name": "Adobe CC",
      "date": "2025-11-05",
      "days_until": 13,
      "cost": 54.99,
      "billing_cycle": "monthly",
      "action_required": "Cancel or accept charge"
    }
  ],
  "cancellation_deadlines": [
    {
      "type": "cancellation_deadline",
      "subscription_id": "uuid",
      "subscription_name": "Annual Service",
      "date": "2025-11-20",
      "days_until": 28,
      "action_required": "Last day to cancel without charge"
    }
  ],
  "price_changes": [
    {
      "subscription_name": "Streaming Service",
      "old_price": 13.99,
      "new_price": 15.99,
      "effective_date": "2025-12-01",
      "increase_percentage": 14.3
    }
  ]
}
```

## Subscription Categories

Standard categories for organization:

- **streaming-video**: Netflix, Hulu, Disney+, HBO Max, Prime Video
- **streaming-music**: Spotify, Apple Music, YouTube Music, Amazon Music
- **streaming-audio**: Audible, Podcast subscriptions
- **software-saas**: SaaS tools, web applications
- **software-desktop**: Desktop software licenses
- **cloud-storage**: Dropbox, Google Drive, iCloud
- **productivity**: Microsoft 365, Google Workspace, Notion
- **fitness**: Gym memberships, fitness apps, Peloton
- **gaming**: Xbox Game Pass, PlayStation Plus, Nintendo Online
- **news-media**: Newspapers, magazines, news subscriptions
- **education**: Online courses, learning platforms
- **professional**: LinkedIn Premium, industry tools
- **other**: Everything else

## Cost Calculation Patterns

### Monthly Cost Equivalents

```python
def calculate_monthly_equivalent(cost, billing_cycle):
    """Convert any billing cycle to monthly equivalent"""

    cycles = {
        'monthly': 1,
        'annual': 12,
        'yearly': 12,
        'quarterly': 3,
        'biannual': 6,
        'weekly': 0.23,  # 1/4.33
        'biweekly': 0.46  # 2/4.33
    }

    divisor = cycles.get(billing_cycle.lower(), 1)
    return round(cost / divisor, 2)

def calculate_annual_equivalent(cost, billing_cycle):
    """Convert any billing cycle to annual equivalent"""

    monthly = calculate_monthly_equivalent(cost, billing_cycle)
    return round(monthly * 12, 2)
```

### ROI and Value Scoring

```python
def calculate_usage_score(usage_frequency):
    """Convert usage frequency to numerical score"""

    scores = {
        'daily': 10,
        'weekly': 7,
        'biweekly': 5,
        'monthly': 3,
        'rarely': 1,
        'never': 0,
        'unknown': None
    }

    return scores.get(usage_frequency.lower())

def calculate_value_score(usage_score, monthly_cost):
    """Calculate value score (higher = better value)"""

    if usage_score is None or monthly_cost == 0:
        return None

    # Normalize cost by dividing by 10
    # Value = Usage / Normalized Cost
    return round(usage_score / (monthly_cost / 10), 2)

def categorize_value(value_score):
    """Categorize subscription by value"""

    if value_score is None:
        return 'unknown'
    elif value_score > 5:
        return 'excellent'
    elif value_score > 2:
        return 'good'
    elif value_score > 1:
        return 'fair'
    else:
        return 'poor'
```

## Optimization Strategies

### 1. Identify Underutilized Subscriptions

**Criteria for underutilization:**
- Usage frequency: rarely or never
- Last used: more than 90 days ago
- Value score: less than 1
- Cost: any amount (even $5/month adds up)

**Action:** Recommend cancellation with annual savings calculation

### 2. Annual vs Monthly Billing Analysis

**Common annual discounts:**
- Typical: 15-20% (equivalent to 2 free months)
- Aggressive: 25-30%
- Conservative: 10-15%

**Calculation pattern:**
```python
def estimate_annual_savings(monthly_cost):
    """Estimate savings from switching to annual billing"""

    current_annual = monthly_cost * 12
    # Assume 16.7% discount (2 months free)
    estimated_annual = monthly_cost * 10
    savings = current_annual - estimated_annual

    return round(savings, 2)
```

**Recommendation criteria:**
- Only suggest for subscriptions used for 12+ months
- User committed to keeping long-term
- Financial flexibility to pay upfront

### 3. Bundle Opportunity Detection

**Common bundles:**

```python
BUNDLES = {
    'disney': {
        'name': 'Disney Bundle',
        'services': ['Disney+', 'Hulu', 'ESPN+'],
        'cost': 14.99,
        'individual_cost': 24.97
    },
    'apple': {
        'name': 'Apple One',
        'services': ['Apple Music', 'Apple TV+', 'Apple Arcade', 'iCloud+'],
        'cost': 19.95,
        'individual_cost': 32.95
    },
    'amazon': {
        'name': 'Amazon Prime',
        'services': ['Prime Video', 'Prime Music', 'Free Shipping'],
        'cost': 14.99,
        'individual_cost': 18.98  # Video + Music only
    },
    'youtube': {
        'name': 'YouTube Premium Family',
        'services': ['YouTube Premium', 'YouTube Music'],
        'cost': 22.99,
        'individual_cost': 11.99,  # Per person
        'note': 'For up to 5 family members'
    }
}
```

**Detection pattern:**
```python
def detect_bundle_opportunity(subscriptions, bundle):
    """Check if user has 2+ services from a bundle"""

    user_has = []
    for sub in subscriptions:
        for service in bundle['services']:
            if service.lower() in sub['name'].lower():
                user_has.append(sub)
                break

    return len(user_has) >= 2, user_has
```

### 4. Alternative Service Suggestions

**Suggestion criteria:**
- Similar features and functionality
- Lower cost
- Better user reviews
- Better suited to usage patterns

**Example alternatives database:**

```python
ALTERNATIVES = {
    'Netflix': [
        {'name': 'Hulu', 'cost': 7.99, 'pros': 'More TV shows', 'cons': 'Fewer movies'},
        {'name': 'Disney+', 'cost': 7.99, 'pros': 'Family friendly', 'cons': 'Limited adult content'}
    ],
    'Spotify Premium': [
        {'name': 'YouTube Music', 'cost': 10.99, 'pros': 'Included with YouTube Premium'},
        {'name': 'Amazon Music', 'cost': 9.99, 'pros': 'Cheaper for Prime members'}
    ],
    'Adobe Creative Cloud': [
        {'name': 'Affinity Suite', 'cost': 169.99, 'type': 'one-time', 'pros': 'No subscription'},
        {'name': 'Canva Pro', 'cost': 12.99, 'pros': 'Simpler, web-based'}
    ]
}
```

### 5. Price Increase Monitoring

**Track price changes:**
```python
def detect_price_increase(old_price, new_price):
    """Detect and calculate price increase"""

    if new_price <= old_price:
        return None

    increase = new_price - old_price
    percentage = round((increase / old_price) * 100, 1)
    annual_impact = round(increase * 12, 2)  # For monthly subscriptions

    return {
        'increase_amount': increase,
        'increase_percentage': percentage,
        'annual_impact': annual_impact
    }
```

**Alert thresholds:**
- Any increase: notify user
- 10%+ increase: flag for review
- 20%+ increase: strongly suggest reviewing alternatives

### 6. Usage Tracking Best Practices

**Update usage frequency:**
- After each use: ideal but impractical
- Weekly: good balance
- Monthly: acceptable minimum

**Last used date tracking:**
- Critical for identifying waste
- Update manually or via API integration
- Flag if not used in 30/60/90 days

## Cancellation Strategies

### Service-Specific Cancellation Procedures

**Common services:**

```python
CANCELLATION_PROCEDURES = {
    'Netflix': {
        'url': 'https://www.netflix.com/cancelplan',
        'steps': [
            'Log in to Netflix.com',
            'Go to Account',
            'Click "Cancel Membership"',
            'Confirm cancellation'
        ],
        'notice_period': 'None - immediate',
        'access_until': 'End of billing period'
    },
    'Spotify': {
        'url': 'https://www.spotify.com/account/subscription/',
        'steps': [
            'Log in to Spotify',
            'Go to Account > Subscription',
            'Click "Cancel Premium"'
        ],
        'notice_period': 'None',
        'access_until': 'End of billing period'
    },
    'Adobe Creative Cloud': {
        'url': 'https://account.adobe.com/plans',
        'steps': [
            'Log in to Adobe Account',
            'Go to Plans',
            'Click "Cancel Plan"',
            'WARNING: May have early termination fee'
        ],
        'notice_period': '14 days for annual plans',
        'early_termination_fee': 'Possible - 50% of remaining contract'
    }
}
```

### Cancellation Timing Strategies

**Best practices:**
1. **Trial periods:** Cancel 24-48 hours before end
2. **Monthly subscriptions:** Cancel anytime (usually keep access until period ends)
3. **Annual subscriptions:** Check cancellation deadline (often 30-60 days before renewal)
4. **Contracts:** Review early termination fees before canceling

### Negotiation Tactics

**When to negotiate:**
- Long-time customer (2+ years)
- Price increases announced
- Considering cancellation
- Found cheaper alternative

**Negotiation script:**
```
"I've been a customer for [X years] and I'm considering canceling
due to [price increase / found alternative]. Are there any loyalty
discounts or promotional rates available?"
```

**Success rate:** 30-50% for established customers

## Renewal Alert Patterns

### Alert Timing

```python
def calculate_alert_schedule(renewal_date, subscription_type):
    """Calculate when to send renewal alerts"""

    if subscription_type == 'trial':
        # More urgent for trials
        return [3, 1, 0]  # days before
    elif subscription_type == 'annual':
        # More advance notice for annual
        return [30, 14, 7, 1]
    else:  # monthly
        return [7, 1]
```

### Alert Priority Levels

- **CRITICAL**: Trial ending today or tomorrow
- **HIGH**: Renewal in 1-3 days, trial in 3-7 days
- **MEDIUM**: Renewal in 7-14 days
- **LOW**: Renewal in 14-30 days

## Reporting Standards

### Monthly Summary Report

**Include:**
1. Total spending (monthly and annual)
2. Category breakdown with percentages
3. Top 5 most expensive subscriptions
4. Underutilized subscriptions
5. Upcoming renewals (next 30 days)
6. Recommendations with savings calculations
7. Month-over-month comparison

### Optimization Report

**Include:**
1. Executive summary (total potential savings)
2. Prioritized recommendations (HIGH/MEDIUM/LOW)
3. Underutilized subscription details
4. Bundle opportunities
5. Annual billing savings potential
6. Alternative service suggestions
7. Action items with deadlines

## File Organization

```
.subscription-tracker/
├── subscription-database.json    # Main database
├── cost-analysis-report.json     # Latest analysis
├── cancellation-calendar.json    # Upcoming events
├── config.json                   # User preferences
├── reports/                      # Historical reports
│   ├── 2025-10-monthly.json
│   └── 2025-Q4-quarterly.json
├── exports/                      # User exports
│   └── subscriptions_20251023.csv
└── archives/                     # Deleted subscriptions
    └── OldService_uuid.json
```

## Privacy and Security

**Sensitive data:**
- Login emails
- Payment methods
- Passwords (NEVER store)

**Best practices:**
- Store locally only
- Encrypt sensitive fields if sharing
- Never commit credentials to git
- Provide .gitignore patterns

**Recommended .gitignore:**
```
.subscription-tracker/
*.subscription-tracker.json
subscription-database.json
config.json
```

## Integration Opportunities

**Potential integrations:**
- Bank/credit card APIs for automatic detection
- Calendar apps for renewal reminders
- Email for alerts and notifications
- Budgeting apps (YNAB, Mint) for expense tracking

## Best Practices Summary

1. **Update regularly:** Weekly usage updates, monthly cost reviews
2. **Track everything:** Include free trials, even if planning to cancel
3. **Set reminders:** 7 days before renewal minimum
4. **Review quarterly:** Comprehensive optimization analysis every 3 months
5. **Cancel promptly:** Don't delay cancellation decisions
6. **Document reasons:** Track why you keep or cancel services
7. **Monitor prices:** Set up alerts for price increases
8. **Consider annual:** If committed, annual billing usually saves money
9. **Bundle when possible:** Take advantage of family/bundle plans
10. **Negotiate:** Don't be afraid to ask for discounts

---

**This skill provides the foundation for intelligent subscription management. Agents should reference these patterns for consistent, effective subscription tracking and optimization.**
