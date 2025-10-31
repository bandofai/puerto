# Affiliate Marketing Skill

Comprehensive patterns for affiliate program management, commission structures, recruitment, fraud detection, and compliance.

## Affiliate Program Models

### CPA (Cost Per Action)
**Definition**: Advertiser pays when affiliate drives a specific action.

**Actions**:
- Sign-up (email capture)
- Free trial start
- Demo request
- Form submission
- App download

**Commission Structure**:
```json
{
  "model": "CPA",
  "action": "email-signup",
  "commission": {
    "amount": 5.00,
    "currency": "USD",
    "type": "fixed"
  },
  "qualifications": {
    "emailVerified": true,
    "uniqueIP": true,
    "minAge": 18
  }
}
```

**Best For**:
- Lead generation businesses
- SaaS free trials
- Content downloads
- Newsletter subscriptions

**Typical Rates**:
- Email signup: $1-$10
- Free trial: $10-$50
- Demo request: $20-$100

### CPS (Cost Per Sale)

**Definition**: Advertiser pays when affiliate drives a completed sale.

**Commission Structure**:
```json
{
  "model": "CPS",
  "commission": {
    "type": "percentage",
    "rate": 15,
    "minimumSale": 50.00,
    "maximumCommission": 1000.00
  },
  "eligibleProducts": ["all"],
  "excludedProducts": ["gift-cards"],
  "recurringCommission": {
    "enabled": true,
    "duration": "lifetime",
    "rate": 10
  }
}
```

**Variations**:
- **Percentage**: 5%-50% of sale value
- **Fixed per sale**: $10 per order regardless of value
- **Tiered**: Different rates for different products
- **Recurring**: Commission on subscription renewals

**Best For**:
- E-commerce
- Digital products
- SaaS subscriptions
- High-ticket items

**Typical Rates**:
- Physical products: 5-15%
- Digital products: 20-50%
- SaaS (recurring): 20-30%
- High-ticket (>$1000): 5-10%

### CPL (Cost Per Lead)

**Definition**: Advertiser pays for qualified leads meeting specific criteria.

**Lead Qualification**:
```json
{
  "model": "CPL",
  "qualification": {
    "required": [
      "valid_email",
      "phone_number",
      "company_size"
    ],
    "scoring": {
      "companySize": {
        "1-10": 20,
        "11-50": 40,
        "51-200": 60,
        "201+": 100
      },
      "jobTitle": {
        "executive": 100,
        "manager": 60,
        "individual": 20
      }
    },
    "minimumScore": 80
  },
  "commission": {
    "base": 50.00,
    "bonus": {
      "score100": 25.00,
      "converted": 100.00
    }
  }
}
```

**Lead Quality Tiers**:
- **Tier 1 (Hot Lead)**: $50-$200
  - Decision maker
  - Immediate need
  - Budget confirmed

- **Tier 2 (Warm Lead)**: $20-$50
  - Influencer role
  - 3-6 month timeline
  - Budget likely

- **Tier 3 (Cold Lead)**: $5-$20
  - Researcher
  - Exploratory stage
  - Budget unclear

**Best For**:
- B2B services
- Insurance
- Finance
- Real estate
- Education

### Hybrid Models

**CPA + CPS**:
```json
{
  "model": "hybrid",
  "structure": {
    "initialAction": {
      "type": "CPA",
      "action": "signup",
      "commission": 10.00
    },
    "firstPurchase": {
      "type": "CPS",
      "rate": 20,
      "bonus": 50.00
    },
    "recurring": {
      "type": "CPS",
      "rate": 10,
      "duration": "lifetime"
    }
  }
}
```

**Two-Tier Programs**:
```json
{
  "model": "two-tier",
  "tier1": {
    "description": "Direct referrals",
    "commission": 20
  },
  "tier2": {
    "description": "Sub-affiliate referrals",
    "commission": 5,
    "requirements": {
      "minTier1Sales": 10
    }
  }
}
```

## Commission Structures

### Performance Tiers

**Volume-Based Tiers**:
```json
{
  "tierStructure": "volume",
  "tiers": [
    {
      "name": "Bronze",
      "threshold": {
        "sales": 0,
        "revenue": 0
      },
      "commission": 10,
      "perks": ["Basic dashboard access"]
    },
    {
      "name": "Silver",
      "threshold": {
        "sales": 10,
        "revenue": 1000
      },
      "commission": 15,
      "perks": ["Priority support", "Marketing materials"]
    },
    {
      "name": "Gold",
      "threshold": {
        "sales": 50,
        "revenue": 5000
      },
      "commission": 20,
      "perks": ["Dedicated manager", "Co-marketing", "Higher payout"]
    },
    {
      "name": "Platinum",
      "threshold": {
        "sales": 200,
        "revenue": 25000
      },
      "commission": 25,
      "perks": ["Custom terms", "API access", "Quarterly bonus"]
    }
  ],
  "evaluation": "monthly"
}
```

**Performance Bonuses**:
```json
{
  "bonuses": {
    "monthlyTarget": {
      "threshold": 100,
      "metric": "sales",
      "bonus": 500.00
    },
    "quarterlyTarget": {
      "threshold": 250,
      "metric": "sales",
      "bonus": 2000.00
    },
    "firstSale": {
      "bonus": 50.00,
      "oneTimeOnly": true
    },
    "milestone": {
      "sales50": 100.00,
      "sales100": 250.00,
      "sales500": 1000.00
    }
  }
}
```

### Cookie Attribution

**Cookie Settings**:
```json
{
  "cookieDuration": {
    "days": 30,
    "description": "30-day cookie window"
  },
  "attributionModel": "last-click",
  "cookieOverride": {
    "enabled": true,
    "priority": "first-click",
    "description": "First affiliate gets credit if within window"
  },
  "crossDevice": {
    "enabled": true,
    "method": "user-id-matching"
  }
}
```

**Attribution Models**:

**Last-Click Attribution**:
- Last affiliate before purchase gets 100% credit
- Most common model
- Simple to implement
- May undervalue early-funnel affiliates

**First-Click Attribution**:
- First affiliate gets 100% credit
- Rewards discovery
- May overvalue awareness stage

**Linear Attribution**:
```python
# Split credit equally among all touchpoints
affiliates = ["aff-001", "aff-003", "aff-007"]
commission_per_affiliate = total_commission / len(affiliates)
```

**Time-Decay Attribution**:
```python
# More recent touchpoints get more credit
def time_decay_weight(days_ago, half_life=7):
    return 0.5 ** (days_ago / half_life)

# Touchpoints
touchpoints = [
    {"affiliate": "aff-001", "days_ago": 20},
    {"affiliate": "aff-003", "days_ago": 10},
    {"affiliate": "aff-007", "days_ago": 1}
]

# Calculate weights
total_weight = sum(time_decay_weight(t["days_ago"]) for t in touchpoints)
for t in touchpoints:
    t["commission"] = (time_decay_weight(t["days_ago"]) / total_weight) * total_commission
```

### Payment Terms

**Payment Schedule**:
```json
{
  "paymentFrequency": "monthly",
  "paymentDay": 15,
  "minimumPayout": 50.00,
  "paymentMethods": [
    "PayPal",
    "Bank Transfer",
    "Check",
    "Stripe"
  ],
  "paymentDelay": {
    "days": 30,
    "reason": "Refund protection period"
  },
  "holdback": {
    "percentage": 10,
    "duration": 90,
    "reason": "Fraud and chargeback protection"
  }
}
```

**Payment Status Tracking**:
```json
{
  "affiliateId": "aff-001",
  "period": "2025-02",
  "commissionEarned": 1250.00,
  "adjustments": -50.00,
  "refunds": -100.00,
  "holdback": -110.00,
  "payable": 990.00,
  "paymentStatus": "scheduled",
  "paymentDate": "2025-03-15",
  "previousBalance": 25.00
}
```

## Recruitment Strategies

### Affiliate Personas

**Influencer/Content Creator**:
- **Characteristics**:
  - Large engaged audience
  - Content creation skills
  - Social media presence

- **Recruitment Approach**:
  - Personalized outreach
  - Higher commission rates
  - Co-marketing opportunities
  - Exclusive deals for audience

- **Commission**: 20-30%

**Coupon/Deal Sites**:
- **Characteristics**:
  - High traffic volume
  - Price-sensitive audience
  - SEO expertise

- **Recruitment Approach**:
  - Exclusive discount codes
  - Higher volume, lower margin
  - Flash sale opportunities

- **Commission**: 5-10%

**Review/Comparison Sites**:
- **Characteristics**:
  - Product expertise
  - SEO rankings
  - Buyer intent traffic

- **Recruitment Approach**:
  - Product samples
  - Exclusive review access
  - Featured placement

- **Commission**: 10-20%

**Email Marketers**:
- **Characteristics**:
  - Large email lists
  - Targeted audiences
  - Direct response expertise

- **Recruitment Approach**:
  - Swipe copy provided
  - Segment-specific offers
  - Performance incentives

- **Commission**: 15-25%

**Niche Bloggers**:
- **Characteristics**:
  - Targeted audience
  - Trust and authority
  - Long-form content

- **Recruitment Approach**:
  - Educational content
  - Tutorial opportunities
  - Affiliate success stories

- **Commission**: 15-30%

### Outreach Templates

**Initial Outreach (Influencer)**:
```markdown
Subject: Partnership Opportunity with [Your Brand]

Hi [Name],

I've been following your content on [platform] and love your approach to [topic]. Your audience would be a perfect fit for [product/service].

We're looking for [3-5] select partners and I'd love to discuss:
- [Commission rate]% commission on all sales
- Exclusive discount code for your audience
- Co-marketing opportunities
- [Other unique benefit]

Would you be interested in a quick call this week?

Best regards,
[Your Name]
[Your Title]

P.S. Here's what [similar influencer] earned last month: $[amount]
```

**Application Process**:
```json
{
  "applicationForm": {
    "required": [
      "name",
      "email",
      "website_url",
      "traffic_source",
      "monthly_visitors",
      "promotion_method"
    ],
    "optional": [
      "social_media_handles",
      "audience_demographics",
      "previous_affiliate_experience",
      "why_interested"
    ]
  },
  "autoApproval": {
    "enabled": false,
    "criteria": {
      "minMonthlyVisitors": 10000,
      "validWebsite": true,
      "noRedFlags": true
    }
  },
  "manualReview": {
    "evaluationCriteria": [
      "content_quality",
      "audience_fit",
      "traffic_legitimacy",
      "brand_alignment"
    ],
    "responseTime": "24-48 hours"
  }
}
```

### Onboarding Process

**Welcome Sequence**:
```json
{
  "step1": {
    "timing": "immediate",
    "content": "Welcome email with login credentials",
    "includes": [
      "Dashboard access",
      "Affiliate link",
      "Unique coupon code",
      "Commission structure"
    ]
  },
  "step2": {
    "timing": "day 1",
    "content": "Getting started guide",
    "includes": [
      "Best practices",
      "Marketing materials",
      "Product information",
      "Case studies"
    ]
  },
  "step3": {
    "timing": "day 3",
    "content": "Promotional strategies",
    "includes": [
      "Content ideas",
      "Email templates",
      "Social media posts",
      "Banner ads"
    ]
  },
  "step4": {
    "timing": "day 7",
    "content": "Check-in and support",
    "includes": [
      "Performance review",
      "Questions answered",
      "Optimization tips",
      "Manager introduction"
    ]
  }
}
```

## Performance Metrics and KPIs

### Affiliate-Level Metrics

**Core Metrics**:
```json
{
  "affiliateId": "aff-001",
  "period": "2025-02",
  "metrics": {
    "clicks": 5420,
    "conversions": 163,
    "conversionRate": 3.01,
    "revenue": 24650.00,
    "commission": 4930.00,
    "epc": 0.91,
    "averageOrderValue": 151.23,
    "refundRate": 3.2,
    "customerLifetimeValue": 450.00
  }
}
```

**Performance Indicators**:

**EPC (Earnings Per Click)**:
```python
epc = total_commission / total_clicks
# Good EPC: $0.50+
# Excellent EPC: $1.00+
```

**Conversion Rate**:
```python
conversion_rate = (conversions / clicks) * 100
# Good: 1-3%
# Excellent: 3-5%+
```

**ROI for Advertiser**:
```python
roi = ((revenue - commission) / commission) * 100
# Healthy: 300%+
# Excellent: 500%+
```

**Reversal Rate**:
```python
reversal_rate = (refunds + chargebacks) / total_sales * 100
# Acceptable: <5%
# Concerning: >10%
```

### Program-Level Metrics

**Overall Performance**:
```json
{
  "program": "main-affiliate-program",
  "period": "2025-Q1",
  "metrics": {
    "totalAffiliates": 450,
    "activeAffiliates": 187,
    "activeRate": 41.6,
    "totalClicks": 125000,
    "totalConversions": 3250,
    "totalRevenue": 487500.00,
    "totalCommission": 73125.00,
    "commissionRate": 15.0,
    "newAffiliates": 45,
    "churnedAffiliates": 12
  }
}
```

**Cohort Analysis**:
```json
{
  "cohort": "2025-01",
  "affiliatesJoined": 32,
  "performance": {
    "month1": {
      "active": 28,
      "revenue": 4200.00,
      "revenuePerAffiliate": 150.00
    },
    "month2": {
      "active": 24,
      "revenue": 6800.00,
      "revenuePerAffiliate": 283.33
    },
    "month3": {
      "active": 22,
      "revenue": 9200.00,
      "revenuePerAffiliate": 418.18
    }
  }
}
```

## Fraud Detection Patterns

### Common Fraud Types

**Cookie Stuffing**:
- **Description**: Dropping affiliate cookies without user consent
- **Detection**:
  ```python
  # Unusual click patterns
  clicks_per_session = clicks / unique_sessions
  if clicks_per_session > 3:
      flag_for_review("cookie_stuffing")

  # Zero-second clicks
  if time_on_page < 1 and conversion_occurred:
      flag_for_review("cookie_stuffing")
  ```

**Click Fraud**:
- **Description**: Generating fake clicks to inflate metrics
- **Detection**:
  ```python
  # IP repetition
  unique_ips = len(set(click_ips))
  ip_diversity = unique_ips / total_clicks
  if ip_diversity < 0.3:
      flag_for_review("click_fraud")

  # Bot detection
  if user_agent in known_bot_agents:
      flag_for_review("click_fraud")

  # Impossible click velocity
  clicks_per_minute = clicks / time_window_minutes
  if clicks_per_minute > 10:
      flag_for_review("click_fraud")
  ```

**Self-Referral Fraud**:
- **Description**: Affiliates purchasing through own links
- **Detection**:
  ```python
  # Match customer data with affiliate data
  if customer_email == affiliate_email:
      flag_for_review("self_referral")

  if customer_ip == affiliate_ip:
      flag_for_review("self_referral")

  # Billing address match
  if customer_address == affiliate_address:
      flag_for_review("self_referral")
  ```

**Trademark Bidding**:
- **Description**: Bidding on brand terms without permission
- **Detection**:
  ```python
  # Manual monitoring of paid search
  # Automated trademark monitoring tools
  # Review referring URLs for PPC patterns
  if "gclid" in referrer and brand_term_detected:
      flag_for_review("trademark_bidding")
  ```

**Incentivized Traffic**:
- **Description**: Paying users to click/convert (if prohibited)
- **Detection**:
  ```python
  # High conversion rate with low quality
  if conversion_rate > 20 and refund_rate > 30:
      flag_for_review("incentivized_traffic")

  # Referrer analysis
  if referrer_domain in known_cashback_sites and prohibited:
      flag_for_review("incentivized_traffic")
  ```

### Fraud Scoring System

**Risk Score Calculation**:
```python
def calculate_fraud_risk_score(affiliate_data):
    score = 0

    # Conversion rate anomaly (too high)
    if affiliate_data["conversion_rate"] > program_avg * 3:
        score += 30

    # Reversal rate (too high)
    if affiliate_data["reversal_rate"] > 15:
        score += 40

    # Traffic source concerns
    if affiliate_data["traffic_source"] == "unknown":
        score += 20

    # Velocity concerns
    if affiliate_data["sales_in_24h"] > 50:
        score += 25

    # New affiliate with high volume
    if affiliate_data["days_active"] < 7 and affiliate_data["sales"] > 20:
        score += 35

    # Geographic mismatch
    if affiliate_data["affiliate_country"] != affiliate_data["traffic_country"]:
        score += 15

    return score

# Risk levels
# 0-30: Low risk
# 31-60: Medium risk - monitor closely
# 61-80: High risk - investigate
# 81+: Critical risk - suspend pending review
```

### Monitoring Systems

**Real-Time Alerts**:
```json
{
  "alertRules": [
    {
      "name": "High velocity sales",
      "condition": "sales_in_1h > 10",
      "action": "pause_affiliate",
      "notification": ["fraud_team", "affiliate_manager"]
    },
    {
      "name": "Unusual refund rate",
      "condition": "refund_rate > 20",
      "action": "flag_for_review",
      "notification": ["affiliate_manager"]
    },
    {
      "name": "IP concentration",
      "condition": "ip_diversity < 0.2 AND clicks > 100",
      "action": "block_traffic",
      "notification": ["fraud_team"]
    }
  ]
}
```

## Legal Compliance

### FTC Guidelines (United States)

**Disclosure Requirements**:
```markdown
# Required Disclosures

Affiliates MUST clearly disclose their relationship:

✅ GOOD Examples:
- "This post contains affiliate links. I earn a commission if you purchase."
- "I'm an affiliate for [Brand]. If you buy through my link, I get paid."
- "Affiliate link - I may earn a commission at no cost to you."

❌ BAD Examples:
- Burying disclosure at bottom in small text
- Using unclear language ("I'm a partner")
- No disclosure at all

Placement: Before affiliate link, clear and conspicuous
```

**Terms of Service Requirements**:
```json
{
  "requiredTerms": [
    "Clear commission structure",
    "Payment terms and schedule",
    "Termination conditions",
    "Prohibited practices",
    "Disclosure requirements",
    "Cookie policy",
    "Intellectual property guidelines",
    "Dispute resolution"
  ]
}
```

### GDPR Compliance (European Union)

**Data Protection**:
```json
{
  "dataCollection": {
    "personalData": [
      "name",
      "email",
      "payment_info",
      "IP_address"
    ],
    "legalBasis": "contract",
    "purpose": "affiliate_program_management",
    "retention": "7 years for tax purposes",
    "rights": [
      "access",
      "rectification",
      "erasure",
      "portability",
      "objection"
    ]
  },
  "cookieConsent": {
    "required": true,
    "mechanism": "opt-in",
    "affiliateLinks": "require_consent"
  }
}
```

### Tax Compliance

**1099 Requirements (US)**:
```json
{
  "threshold": 600.00,
  "required": "annual",
  "forms": ["W-9", "1099-NEC"],
  "deadline": "January 31",
  "affiliateResponsibilities": [
    "Provide accurate tax information",
    "Report income on tax returns",
    "Pay estimated taxes quarterly if needed"
  ]
}
```

**International Tax**:
- Withholding requirements for international affiliates
- VAT considerations for EU affiliates
- Tax treaty benefits
- Local tax registration requirements

## Best Affiliate Networks and Platforms

### Major Networks

**ShareASale**:
```json
{
  "name": "ShareASale",
  "type": "Network",
  "bestFor": ["Physical products", "Digital products", "Services"],
  "features": {
    "merchants": "6000+",
    "affiliates": "1M+",
    "minimumPayout": 50.00,
    "paymentFrequency": "monthly",
    "fee": "Network fee + platform fee"
  },
  "pros": [
    "Large merchant base",
    "Reliable tracking",
    "Good reporting"
  ],
  "cons": [
    "Approval process varies",
    "Interface dated"
  ]
}
```

**CJ Affiliate (Commission Junction)**:
- Largest network
- Premium brands
- Advanced reporting
- Higher requirements

**Rakuten Advertising**:
- Global reach
- Premium merchants
- Multi-currency support
- Enterprise focus

**Impact**:
- Modern platform
- Comprehensive tracking
- API access
- Partnership automation

**PartnerStack**:
- B2B/SaaS focus
- Multi-tier programs
- Partner portal
- Integrations

### Self-Hosted Solutions

**Post Affiliate Pro**:
```json
{
  "type": "Self-hosted",
  "deployment": ["Cloud", "On-premise"],
  "features": [
    "Multi-level marketing",
    "Custom commission rules",
    "API access",
    "White-label",
    "Multiple campaigns"
  ],
  "pricing": "One-time license or subscription",
  "bestFor": "Custom requirements"
}
```

**Tapfiliate**:
- SaaS solution
- Easy integration
- Customizable
- Recurring commissions
- API access

**Refersion**:
- E-commerce focus
- Shopify integration
- Influencer management
- Ambassador programs

## Contract Templates

### Affiliate Agreement Structure

```markdown
# AFFILIATE AGREEMENT

**AGREEMENT DATE**: [Date]

**PARTIES**:
- Company: [Legal Company Name] ("Company")
- Affiliate: [Affiliate Name/Entity] ("Affiliate")

## 1. APPOINTMENT
Company appoints Affiliate to promote [Products/Services] under the terms of this Agreement.

## 2. AFFILIATE OBLIGATIONS
Affiliate agrees to:
- Promote Company products/services in compliance with all terms
- Make all required disclosures (FTC, GDPR, etc.)
- Not engage in prohibited practices (see Section 6)
- Provide accurate tax information (W-9/W-8)

## 3. COMMISSION STRUCTURE
- Model: [CPA/CPS/CPL/Hybrid]
- Rate: [X%] or [Fixed Amount]
- Cookie Duration: [X days]
- Attribution Model: [Last-click/First-click/Linear]

## 4. PAYMENT TERMS
- Frequency: Monthly on the [day]
- Minimum Payout: $[amount]
- Payment Method: [PayPal/Bank Transfer/Check]
- Payment Delay: [X days] after period end
- Holdback: [X%] for [duration] for refund protection

## 5. TRACKING AND REPORTING
- Unique affiliate tracking link provided
- Real-time dashboard access
- Monthly performance reports

## 6. PROHIBITED PRACTICES
Affiliate shall NOT:
- Engage in cookie stuffing
- Bid on Company trademarks (without permission)
- Use misleading advertising
- Spam or send unsolicited emails
- Self-refer (without permission)
- Misrepresent Company products/services

## 7. INTELLECTUAL PROPERTY
- Company grants limited license to use trademarks/materials
- Affiliate does not acquire ownership rights
- Must follow brand guidelines

## 8. TERM AND TERMINATION
- Term: Ongoing until terminated
- Either party may terminate with [X days] notice
- Company may terminate immediately for violations
- Commissions earned before termination will be paid

## 9. CONFIDENTIALITY
Affiliate agrees to keep confidential:
- Commission rates
- Proprietary business information
- Customer data

## 10. LIMITATION OF LIABILITY
Company's liability limited to unpaid commissions.

## 11. GOVERNING LAW
This Agreement governed by laws of [State/Country].

## 12. ENTIRE AGREEMENT
This Agreement constitutes the entire agreement between parties.

**COMPANY**:                    **AFFILIATE**:
_______________________         _______________________
[Name]                          [Name]
[Title]                         [Title]
[Date]                          [Date]
```

## Best Practices

### Program Setup
1. **Clear Terms**: Transparent commission structure
2. **Competitive Rates**: Research competitor programs
3. **Quality Materials**: Professional marketing assets
4. **Easy Signup**: Streamlined application process
5. **Fast Approval**: 24-48 hour turnaround

### Affiliate Management
1. **Regular Communication**: Monthly newsletters
2. **Performance Reviews**: Quarterly check-ins
3. **Optimization Tips**: Ongoing education
4. **Recognition**: Top performer awards
5. **Relationship Building**: Personal outreach

### Fraud Prevention
1. **Monitoring**: Daily fraud checks
2. **Verification**: New affiliate vetting
3. **Holdbacks**: Payment protection
4. **Terms Enforcement**: Consistent action
5. **Technology**: Anti-fraud tools

### Compliance
1. **Legal Review**: Regular terms updates
2. **Disclosure Monitoring**: Check affiliate sites
3. **Training**: Compliance education
4. **Documentation**: Maintain records
5. **Privacy**: GDPR/CCPA adherence

### Performance Optimization
1. **A/B Testing**: Test creative variations
2. **Segment Analysis**: Identify top performers
3. **Incentive Programs**: Boost activity
4. **New Products**: Keep content fresh
5. **Competitive Analysis**: Monitor market rates
