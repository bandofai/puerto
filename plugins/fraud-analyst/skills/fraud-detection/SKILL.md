# Fraud Detection Skill

Expert knowledge for fraud pattern detection, statistical analysis, and risk assessment in financial transactions.

## Table of Contents

1. [Rule-Based Detection Patterns](#rule-based-detection-patterns)
2. [Statistical Anomaly Detection](#statistical-anomaly-detection)
3. [Behavioral Analysis](#behavioral-analysis)
4. [ML Feature Engineering](#ml-feature-engineering)
5. [Risk Scoring Frameworks](#risk-scoring-frameworks)
6. [Confidence Scoring](#confidence-scoring)
7. [False Positive Reduction](#false-positive-reduction)

---

## Rule-Based Detection Patterns

### 1. Velocity Abuse

**Description**: Rapid succession of transactions indicating card testing or automated fraud

**Detection Rules**:
- **Critical (0.95 confidence)**: 10+ transactions in 10 minutes
- **High (0.85 confidence)**: 25+ transactions in 1 hour
- **Medium (0.70 confidence)**: 50+ transactions in 24 hours

**Indicators**:
- Multiple small amounts followed by large amount
- All transactions at different merchants
- Progressive testing: $1 → $10 → $100 → $1000
- Geographic clustering (same area)

**Example Pattern**:
```
08:30:00 - $1.00 - Merchant A
08:31:00 - $5.00 - Merchant B
08:32:00 - $10.00 - Merchant C
08:33:00 - $50.00 - Merchant D
08:34:00 - $100.00 - Merchant E
08:35:00 - $500.00 - Merchant F
08:36:00 - $1000.00 - Merchant G [FRAUD PEAK]
```

---

### 2. Account Takeover

**Description**: Unauthorized access to legitimate account via stolen credentials

**Detection Rules**:
- Device change + location change + transaction = 0.85 confidence
- Password reset + transaction within 1 hour = 0.80 confidence
- Spending spike (5x+ baseline) + new merchant categories = 0.75 confidence

**Indicators**:
- Device change (different OS/browser/hardware)
- Location change (different city/country)
- Password/email change within 24 hours
- Contact information updated
- Sudden spending spike
- New merchant categories
- Transactions outside normal hours
- Multiple failed authentication attempts before success

**Timeline Pattern**:
```
Day 0: Phishing email sent
Day 1: Credentials compromised
Day 1 + 2 hours: Password reset from new device
Day 1 + 2.5 hours: Contact info changed
Day 1 + 3 hours: Large transactions begin [FRAUD START]
```

---

### 3. Structuring (Smurfing)

**Description**: Multiple transactions to avoid $10,000 reporting threshold (CTR)

**Detection Rules**:
- 3+ transactions $9,000-$9,999 in 24 hours = 0.90 confidence
- 5+ transactions $9,000-$9,999 in 7 days = 0.95 confidence
- Same-day structured amounts at different locations = 0.98 confidence

**Indicators**:
- Amounts consistently just below $10,000
- Round or near-round amounts ($9,000, $9,500, $9,900)
- Multiple transactions same day
- Different branch locations
- No clear business purpose
- Customer avoids questions about purpose

**Red Flag Amounts**:
- $9,000 - $9,999 (most common)
- $8,000 - $8,999 (sophisticated structuring)
- Exactly $9,500 (common structured amount)

**Legal Reference**: 31 U.S.C. § 5324 (federal crime)

---

### 4. Card Testing

**Description**: Stolen card credentials being tested before large fraud

**Detection Rules**:
- Progressive amounts + all new merchants + <30 min = 0.90 confidence
- Multiple declined followed by approved = 0.85 confidence
- Small test + immediate large purchase = 0.88 confidence

**Testing Pattern**:
```
Stage 1: Validation ($1-$10)
  - Verify card is active
  - Check if fraud alerts triggered
  - Usually approved

Stage 2: Limit Testing ($50-$500)
  - Determine available credit
  - Test velocity limits
  - Multiple merchants

Stage 3: Maximization ($1000+)
  - Maximize fraud before detection
  - High-value merchants (electronics, jewelry)
  - Often multiple large transactions

Timing: Usually within 30 minutes to 2 hours
```

---

### 5. Bust-Out Fraud

**Description**: Build credit trust, then max out and disappear

**Detection Rules**:
- Recent limit increase + immediately maxed = 0.85 confidence
- New account + perfect payments + sudden max-out = 0.80 confidence
- Synthetic identity + bust-out pattern = 0.90 confidence

**Timeline Pattern**:
```
Month 0-3: Open account
  - Often with synthetic identity
  - Good credit score (manufactured)
  - Small initial limit ($500-$2000)

Month 3-6: Build trust
  - Small regular charges
  - On-time payments
  - Responsible behavior

Month 6: Request limit increase
  - Based on good payment history
  - Increase to $10,000-$25,000
  - Approved quickly

Month 6 + 1 week: Bust-out
  - Max out new limit immediately
  - Large purchases at multiple merchants
  - Cash advances
  - No intention to repay
  - Account abandoned
```

---

### 6. Mule Account

**Description**: Account used to launder money, often by unwitting victim

**Detection Rules**:
- Multiple small deposits + immediate withdrawals = 0.80 confidence
- Deposit/wire/cash-out same day = 0.85 confidence
- New account + high activity + no normal transactions = 0.88 confidence

**Pattern Characteristics**:
- Account opened recently (<90 days)
- Multiple incoming deposits from different sources
- Deposits quickly withdrawn via:
  - Wire transfers
  - Cash withdrawals
  - Person-to-person transfers
  - Cryptocurrency purchases
- Little to no normal transaction activity (groceries, bills, etc.)
- Often victim of employment scam ("money transfer agent")

**Typical Mule Profile**:
- Recent job seeker
- "Work from home" opportunity
- Asked to receive/forward funds
- Promised commission (10-20%)
- Unaware of criminal activity

---

### 7. Money Laundering Indicators

**Detection Rules**:
- Rapid in/out + no economic purpose = 0.75 confidence
- Round amounts + high frequency = 0.70 confidence
- Trade-based anomalies = 0.80 confidence

**Red Flags**:
- Round-dollar amounts ($1000, $5000, $10000 exactly)
- Transactions with no clear business purpose
- Immediate movement of funds (in and out same day)
- Multiple layering transactions
- Use of shell companies
- Transactions with high-risk jurisdictions
- Trade invoices that don't match typical values
- Overpayment and refund schemes

**Three Stages**:
```
1. Placement: Introduce illicit funds into financial system
   - Large cash deposits
   - Structuring to avoid reporting
   - Purchase of monetary instruments

2. Layering: Separate funds from criminal source
   - Multiple wire transfers
   - Purchase/sale of assets
   - International transactions
   - Complex transaction chains

3. Integration: Funds appear legitimate
   - Investment in legitimate business
   - Real estate purchases
   - Luxury goods
   - Appears as normal wealth
```

---

### 8. Geographic Anomaly Detection

**Impossible Travel**:
```python
distance_miles = calculate_distance(location1, location2)
time_hours = (transaction2_time - transaction1_time).total_seconds() / 3600
speed_mph = distance_miles / time_hours

MAX_FEASIBLE_SPEED = 600  # mph (accounting for commercial flights)

if speed_mph > MAX_FEASIBLE_SPEED:
    confidence = 0.95  # Impossible travel
elif speed_mph > 400:
    confidence = 0.80  # Extremely suspicious (would need private jet)
elif speed_mph > 200:
    confidence = 0.65  # Unusual (same-day long distance)
```

**High-Risk Locations**:
- Countries with high fraud rates
- Sanctioned countries (OFAC list)
- Countries with weak AML enforcement
- Known fraud hotspots

**Location Change Indicators**:
- First transaction in new country
- Transaction in high-risk jurisdiction
- Unusual location for customer profile
- Location inconsistent with recent activity

---

## Statistical Anomaly Detection

### Z-Score Method

**Purpose**: Identify statistical outliers in transaction behavior

**Formula**:
```python
z_score = (value - mean) / standard_deviation
```

**Interpretation**:
- |Z| ≥ 3.0: Extreme outlier (99.7% threshold) → CRITICAL (0.90 confidence)
- |Z| ≥ 2.0: Significant outlier (95% threshold) → HIGH (0.75 confidence)
- |Z| ≥ 1.5: Moderate outlier (86% threshold) → MEDIUM (0.60 confidence)
- |Z| < 1.5: Normal variation

**Apply To**:
- Transaction amounts
- Transaction frequency
- Daily volume
- Time between transactions

**Example**:
```
Customer's 90-day transaction amounts:
Mean: $87.50
Std Dev: $42.30

Current transaction: $500.00

Z-score = (500 - 87.50) / 42.30 = 9.75

Result: Extreme outlier (CRITICAL alert)
```

---

### IQR Method (Interquartile Range)

**Purpose**: Non-parametric outlier detection (robust to skewed distributions)

**Formula**:
```python
Q1 = 25th percentile
Q3 = 75th percentile
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

is_outlier = (value < lower_bound) or (value > upper_bound)
```

**Advantage**: Works well when data isn't normally distributed

**Example**:
```
Customer's 90-day amounts:
Q1 (25th percentile): $45.00
Q3 (75th percentile): $125.00
IQR: $80.00

Lower bound: $45 - (1.5 × $80) = -$75 (use $0)
Upper bound: $125 + (1.5 × $80) = $245.00

Current transaction: $500.00

Result: Outlier (above $245 threshold)
```

---

### Velocity Anomaly Detection

**Purpose**: Identify unusual transaction frequency

**Method**:
```python
# Calculate current velocity
current_velocity = transactions_in_window / time_window_hours

# Calculate baseline velocity
baseline_velocity = avg_transactions_per_day / 24

# Velocity ratio
velocity_ratio = current_velocity / baseline_velocity

# Risk assessment
if velocity_ratio >= 10:
    risk = "CRITICAL"
    confidence = 0.95
elif velocity_ratio >= 5:
    risk = "HIGH"
    confidence = 0.85
elif velocity_ratio >= 3:
    risk = "MEDIUM"
    confidence = 0.70
```

**Time Windows to Check**:
- Last 10 minutes (card testing)
- Last 1 hour (velocity abuse)
- Last 24 hours (daily patterns)
- Last 7 days (weekly trends)

---

## Behavioral Analysis

### Customer Baseline Profiling

**Data Collection Period**: 90 days minimum (180 days preferred)

**Baseline Metrics**:
```python
baseline = {
    # Transaction patterns
    "avg_transactions_per_day": float,
    "avg_transaction_amount": float,
    "median_transaction_amount": float,
    "std_dev_amount": float,
    "avg_daily_volume": float,

    # Merchant patterns
    "typical_merchants": List[str],  # Top 10 merchants
    "typical_categories": Dict[str, float],  # Category % breakdown
    "unique_merchants_per_month": int,

    # Temporal patterns
    "typical_hours": List[int],  # Hours with 80% of activity
    "typical_days_of_week": List[str],
    "weekend_vs_weekday_ratio": float,

    # Geographic patterns
    "typical_locations": List[str],
    "typical_cities": List[str],
    "typical_countries": List[str],
    "home_location": LatLng,

    # Device patterns
    "typical_devices": List[str],
    "os_types": List[str],
    "browser_types": List[str],
}
```

### Deviation Scoring

**Purpose**: Quantify how much current behavior deviates from baseline

**Formula**:
```python
def calculate_deviation_score(current, baseline):
    deviations = []

    # Amount deviation
    amount_dev = abs(current.amount - baseline.avg_amount) / baseline.std_dev_amount
    deviations.append(min(1.0, amount_dev / 3.0))  # Normalize to 0-1

    # Frequency deviation
    freq_dev = abs(current.txn_count - baseline.avg_daily_txns) / baseline.avg_daily_txns
    deviations.append(min(1.0, freq_dev))

    # Category deviation (binary: new category or not)
    if current.category not in baseline.typical_categories:
        deviations.append(1.0)
    else:
        deviations.append(0.0)

    # Time deviation
    if current.hour not in baseline.typical_hours:
        deviations.append(0.5)
    else:
        deviations.append(0.0)

    # Location deviation
    if current.location not in baseline.typical_locations:
        if current.city not in baseline.typical_cities:
            deviations.append(1.0)
        else:
            deviations.append(0.5)
    else:
        deviations.append(0.0)

    # Device deviation
    if current.device not in baseline.typical_devices:
        deviations.append(0.7)
    else:
        deviations.append(0.0)

    # Overall deviation score (0.0 - 1.0)
    return sum(deviations) / len(deviations)
```

**Interpretation**:
- 0.0 - 0.2: Typical behavior
- 0.2 - 0.4: Minor deviation
- 0.4 - 0.6: Moderate deviation
- 0.6 - 0.8: Significant deviation
- 0.8 - 1.0: Extreme deviation (fraud likely)

### Peer Group Comparison

**Purpose**: Compare customer to similar customers

**Peer Group Definition**:
```python
def find_peer_group(customer):
    return filter_customers(
        tenure_range=(customer.tenure - 180, customer.tenure + 180),  # days
        region=customer.region,
        activity_level=customer.activity_tier,  # low/medium/high
        account_type=customer.account_type,
        min_peer_count=100  # Need sufficient peers for statistics
    )
```

**Percentile Calculation**:
```python
customer_percentile = (
    count(peers where metric < customer.metric) / total_peers
) * 100

# Interpretation
if percentile >= 99.5:
    outlier_level = "EXTREME"  # Top 0.5%
    confidence = 0.90
elif percentile >= 95.0:
    outlier_level = "SIGNIFICANT"  # Top 5%
    confidence = 0.75
elif percentile >= 90.0:
    outlier_level = "MODERATE"  # Top 10%
    confidence = 0.60
```

---

## ML Feature Engineering

### Transaction Features (20+)
```python
transaction_features = {
    # Amount features
    "amount": float,
    "amount_zscore": float,
    "amount_percentile": float,
    "amount_ratio_to_avg": float,
    "is_round_amount": bool,

    # Time features
    "hour_of_day": int,
    "day_of_week": int,
    "is_weekend": bool,
    "is_holiday": bool,
    "is_unusual_hour": bool,

    # Merchant features
    "merchant_risk_score": float,
    "is_new_merchant": bool,
    "merchant_category": str,
    "is_high_risk_category": bool,

    # Transaction type features
    "is_card_present": bool,
    "is_international": bool,
    "is_ecommerce": bool,
    "transaction_type_encoded": int,
}
```

### Velocity Features (15+)
```python
velocity_features = {
    # Transaction counts
    "txns_last_10min": int,
    "txns_last_1hour": int,
    "txns_last_24hours": int,
    "txns_last_7days": int,

    # Volume totals
    "volume_last_10min": float,
    "volume_last_1hour": float,
    "volume_last_24hours": float,

    # Velocity ratios
    "velocity_ratio_10min": float,
    "velocity_ratio_1hour": float,
    "velocity_ratio_24hours": float,

    # Time gaps
    "seconds_since_last_txn": float,
    "avg_gap_between_txns_today": float,

    # Uniqueness
    "unique_merchants_last_hour": int,
    "unique_locations_last_hour": int,
    "unique_devices_last_hour": int,
}
```

### Geographic Features (10+)
```python
geo_features = {
    "distance_from_last_txn_miles": float,
    "distance_from_home_miles": float,
    "travel_speed_mph": float,
    "is_impossible_travel": bool,
    "is_home_country": bool,
    "is_new_country": bool,
    "is_high_risk_country": bool,
    "location_risk_score": float,
}
```

### Customer History Features (15+)
```python
customer_features = {
    "customer_tenure_days": int,
    "total_transactions_lifetime": int,
    "total_volume_lifetime": float,
    "avg_monthly_transactions": float,
    "avg_monthly_volume": float,
    "current_risk_tier": str,
    "previous_fraud_count": int,
    "previous_false_positive_count": int,
    "days_since_password_change": int,
    "days_since_device_change": int,
    "credit_score": int,
    "account_status": str,
}
```

### Pattern Features (20+)
```python
pattern_features = {
    # Account takeover
    "device_and_location_change": bool,
    "password_reset_recent": bool,
    "spending_spike_ratio": float,

    # Card testing
    "progressive_amounts_detected": bool,
    "multiple_new_merchants": bool,
    "test_pattern_score": float,

    # Structuring
    "near_threshold_count": int,
    "structured_pattern_detected": bool,

    # Money laundering
    "rapid_in_out_detected": bool,
    "round_dollar_pattern": bool,
    "layering_detected": bool,

    # Bust-out
    "recent_limit_increase": bool,
    "immediately_maxed_credit": bool,

    # Mule account
    "multiple_small_deposits": int,
    "mule_pattern_detected": bool,

    # General
    "anomaly_cluster_24h": int,
    "deviation_from_baseline": float,
    "peer_group_percentile": float,
}
```

**Total**: 80+ core features + derived/interaction features = 100+ features

---

## Risk Scoring Frameworks

### Composite Risk Score

**Formula**:
```python
risk_score = (
    transaction_risk * 0.30 +      # 30%
    customer_risk * 0.25 +          # 25%
    pattern_risk * 0.25 +           # 25%
    velocity_risk * 0.10 +          # 10%
    geographic_risk * 0.10          # 10%
)  # Result: 0-100 scale
```

### Risk Tiers

**CRITICAL (80-100)**:
- Action: BLOCK IMMEDIATELY
- Review: Mandatory manual review
- SLA: 4 hours
- Typical: Account takeover, structuring, impossible travel

**HIGH (60-79)**:
- Action: MANUAL REVIEW
- Review: Mandatory manual review
- SLA: 24 hours
- Typical: Large amounts, multiple red flags

**MEDIUM (40-59)**:
- Action: ENHANCED MONITORING
- Review: Automated monitoring
- SLA: 72 hours
- Typical: Minor deviations, single red flags

**LOW (0-39)**:
- Action: APPROVE
- Review: Standard processing
- SLA: None
- Typical: Normal behavior, no red flags

---

## Confidence Scoring

### Pattern Confidence Calculation

```python
def calculate_pattern_confidence(pattern_type, indicators):
    # Base confidence by pattern type
    base_confidence = {
        "account_takeover": 0.85,
        "card_testing": 0.80,
        "structuring": 0.90,
        "bust_out": 0.75,
        "mule_account": 0.80,
        "money_laundering": 0.70,
    }.get(pattern_type, 0.70)

    # Adjust based on indicator strength
    indicator_boost = 0
    for indicator in indicators:
        if indicator.present:
            indicator_boost += indicator.weight * 0.1

    # Adjust based on historical matches
    if similar_confirmed_cases_found:
        historical_boost = max_similarity * 0.15
    else:
        historical_boost = 0

    # Final confidence (cap at 0.98)
    confidence = base_confidence + indicator_boost + historical_boost
    return min(0.98, confidence)
```

### Confidence Interpretation

- **0.90-0.98**: Very High (near certainty)
- **0.80-0.89**: High (strong evidence)
- **0.70-0.79**: Moderate (substantial indicators)
- **0.60-0.69**: Fair (some indicators)
- **<0.60**: Low (weak indicators)

---

## False Positive Reduction

### Techniques

**1. Contextual Analysis**
- Consider customer history
- Account tenure (newer = higher FP risk)
- Previous fraud vs false positive ratio
- Life events (moving, traveling, shopping for big purchase)

**2. Temporal Patterns**
- Holiday shopping seasons
- End-of-month bill payments
- Payday spending patterns
- Travel seasons (summer, holidays)

**3. Progressive Alerting**
- First unusual transaction → Monitor (don't alert)
- Second unusual transaction → Alert (if pattern emerging)
- Third unusual transaction → High priority alert

**4. Whitelist Management**
- Trusted merchants
- Known travel locations
- Authorized devices
- Scheduled large purchases (customer pre-notification)

**5. Dynamic Thresholds**
```python
def adjust_threshold(customer):
    base_threshold = 80  # CRITICAL tier

    # Adjust for tenure
    if customer.tenure_days < 90:
        threshold += 5  # More lenient for new accounts (higher FP risk)
    elif customer.tenure_days > 1095:  # 3+ years
        threshold -= 5  # More strict for established accounts

    # Adjust for history
    if customer.false_positive_count > 3:
        threshold += 10  # More lenient (frequent false positives)
    if customer.fraud_count > 0:
        threshold -= 10  # More strict (previous fraud)

    return threshold
```

**6. Multi-Factor Decision**
- Don't rely on single indicator
- Require multiple corroborating signals
- Weight indicators by reliability
- Consider contradicting evidence

### Performance Metrics

**Track and Optimize**:
```python
# Confusion Matrix
true_positives = fraud_correctly_identified
false_positives = legitimate_incorrectly_flagged
true_negatives = legitimate_correctly_approved
false_negatives = fraud_missed

# Key Metrics
precision = true_positives / (true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)
f1_score = 2 * (precision * recall) / (precision + recall)

false_positive_rate = false_positives / (false_positives + true_negatives)
false_negative_rate = false_negatives / (false_negatives + true_positives)

# Target Performance
# Precision ≥ 85% (minimize false positives)
# Recall ≥ 90% (minimize false negatives)
# F1 Score ≥ 0.87
# FPR < 5%
# FNR < 2%
```

---

## Summary

**This skill provides**:
- 8 major fraud pattern definitions with detection rules
- Statistical anomaly detection methods (Z-score, IQR, velocity)
- Behavioral analysis frameworks (baseline, deviation, peer comparison)
- ML feature engineering (100+ features across 4 categories)
- Risk scoring frameworks (5-component composite score)
- Confidence scoring methodologies
- False positive reduction techniques

**Use this skill to**:
- Detect fraud patterns with high accuracy
- Calculate statistical outliers
- Analyze behavioral deviations
- Generate ML features
- Assess comprehensive fraud risk
- Optimize detection performance

**Remember**: Fraud detection is a balance between catching fraud (recall) and minimizing false positives (precision). Use multiple detection methods, consider context, and continuously optimize based on performance metrics.
