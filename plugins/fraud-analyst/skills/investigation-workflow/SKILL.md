# Investigation Workflow Skill

Expert knowledge for fraud investigation case management, evidence collection, SLA tracking, and outcome determination.

## 10-Step Investigation Framework

### Step 1: Case Creation
**Duration**: <5 minutes (automated)

**Actions**:
- Generate unique case ID: INV-YYYY-XXXXX
- Assign priority (P1/P2/P3/P4)
- Calculate SLA deadline
- Create case directory structure
- Initialize case tracking file

**Priority Matrix**:
| Amount | Risk Score | Pattern Confidence | Priority | SLA |
|--------|-----------|-------------------|----------|-----|
| >$50K | Any | Any | P1 | 4 hours |
| Any | ≥90 | ≥0.90 | P1 | 4 hours |
| $10K-$50K | 80-89 | ≥0.80 | P2 | 24 hours |
| $1K-$10K | 60-79 | 0.70-0.79 | P3 | 48 hours |
| <$1K | <60 | <0.70 | P4 | 5 days |

**Case Directory Structure**:
```
data/investigations/INV-2025-XXXXX/
├── case_file.json
├── transactions.csv
├── pattern_analysis.pdf
├── risk_assessment.pdf
├── customer_profile.json
├── device_history.json
├── location_history.json
├── evidence_manifest.txt
└── timeline.json
```

---

### Step 2: Evidence Gathering
**Duration**: 10-30 minutes

**Required Evidence**:

**Transaction Evidence**:
- Complete transaction records (all flagged transactions)
- Customer transaction history (90 days minimum)
- Velocity metrics and calculations
- Geographic data with timestamps
- Device fingerprints

**Analysis Evidence**:
- Pattern analysis report from pattern-analyzer
- Risk assessment report from risk-scorer
- Original alert from transaction-monitor
- ML feature extraction (if available)

**Customer Evidence**:
- Customer profile snapshot (current state)
- Account history (opening date, status changes)
- Device history (90 days)
- Location history (30 days)
- Authentication logs (7 days)
- Previous fraud incidents
- Previous false positives
- Customer communication preferences

**External Evidence** (collect as needed):
- Merchant verification requests/responses
- Card network data pulls
- Law enforcement information
- Related case files

**Chain of Custody Requirements**:
```json
{
  "evidence_id": "EVID-001",
  "type": "transaction_records",
  "source": "transaction_database",
  "collected_by": "investigation-coordinator",
  "collected_timestamp": "2025-01-20T10:30:00Z",
  "file_location": "data/investigations/INV-2025-00234/transactions.csv",
  "file_hash": "sha256:abc123...",
  "chain_of_custody": [
    {
      "timestamp": "2025-01-20T10:30:00Z",
      "action": "collected",
      "actor": "investigation-coordinator"
    }
  ]
}
```

---

### Step 3: Analysis
**Duration**: 1-4 hours (depending on priority)

**Analysis Tasks**:

**Customer Contact**:
- Attempt 1: Automated SMS + Email (immediate)
- Attempt 2: Automated phone call (30 min later)
- Attempt 3: Manual analyst call (1 hour later)
- Document all contact attempts and responses

**Transaction Verification**:
- Review each flagged transaction
- Verify merchant legitimacy
- Check transaction details against customer profile
- Identify clear fraud indicators
- Note any contradictory evidence

**Timeline Construction**:
```
[Time] - [Event] - [Source] - [Significance]

Example:
08:30:00 - First suspicious transaction - Transaction log - Pattern start
08:35:00 - Multiple rapid transactions - Transaction log - Velocity abuse
09:15:00 - Pattern detected - Pattern analyzer - Alert triggered
10:20:00 - Card blocked - Fraud ops - Customer protection
10:22:00 - Customer notified - Communications - Customer contact
11:15:00 - Customer confirmed fraud - Phone call - Verification obtained
```

**Pattern Correlation**:
- Match detected patterns to known fraud typologies
- Search for similar historical cases
- Identify primary and secondary patterns
- Assess pattern strength and confidence

---

### Step 4: Preliminary Findings
**Duration**: 30 minutes - 2 hours

**Determination Options**:
- **Fraud Confirmed**: Strong evidence, customer verification, or clear indicators
- **Likely Fraud**: Strong indicators but lacking definitive proof
- **Inconclusive**: Mixed signals, need enhanced review
- **Likely Legitimate**: Weak indicators, customer claims legitimate
- **Not Fraud**: Verified as legitimate activity

**Confidence Assessment**:
```python
determination_confidence = (
    pattern_confidence * 0.30 +
    customer_verification * 0.30 +  # 0.0 if not reached, 1.0 if confirmed
    evidence_strength * 0.25 +
    historical_match * 0.15
)

# Confidence levels
if confidence >= 0.90: level = "Very High"
elif confidence >= 0.75: level = "High"
elif confidence >= 0.60: level = "Moderate"
else: level = "Low"
```

**Evidence Strength Factors**:
- Multiple independent indicators (stronger)
- Corroborating evidence from different sources (stronger)
- Clear timeline of suspicious activity (stronger)
- Similar to confirmed fraud cases (stronger)
- Customer verification obtained (strongest)

---

### Step 5: Enhanced Review
**Duration**: 2-8 hours (if needed)

**When Required**:
- Preliminary findings inconclusive
- High-value case (>$25K)
- Complex fraud pattern
- Legal implications
- Regulatory reporting implications

**Enhanced Review Actions**:

**Deep Merchant Analysis**:
- Verify merchant business legitimacy
- Check merchant fraud history
- Contact merchant for transaction verification
- Review merchant category risk

**Card Network Data**:
- Request detailed transaction data from card network
- Check for similar fraud patterns on other cards
- Review card-present vs card-not-present details
- Analyze authorization codes and decline reasons

**External Data Sources**:
- Credit bureau reports
- Public records search
- Social media verification
- Address verification
- Phone number verification

**Advanced Pattern Analysis**:
- Network analysis (connected accounts/devices)
- Time-series correlation
- Behavioral deviation deep dive
- Geolocation analysis (IP, GPS, cell tower)

---

### Step 6: Final Determination
**Duration**: 30 minutes - 1 hour

**Final Determination Options**:
1. **Confirmed Fraud**
   - Confidence: ≥0.80
   - Evidence: Strong, multiple indicators
   - Customer: Denies transactions OR unreachable
   - Next: Proceed to actions

2. **Not Fraud (Legitimate)**
   - Confidence: ≥0.80
   - Evidence: Contradicts fraud indicators
   - Customer: Confirms transactions as legitimate
   - Next: Close case, reverse blocks, apologize

3. **Fraud - Low Confidence**
   - Confidence: 0.60-0.79
   - Evidence: Some indicators but not conclusive
   - Customer: Mixed signals or unreachable
   - Next: Err on side of caution, proceed with limited actions

**Documentation Requirements**:
- Detailed summary of findings
- Evidence supporting determination
- Confidence level and rationale
- Customer contact summary
- External verification results
- Dissenting evidence (if any)
- Legal/compliance review (for high-value cases)

---

### Step 7: Action Recommended
**Duration**: 15-30 minutes

**Action Categories**:

**Account Actions**:
- Block card/account (if not already done)
- Close account (if fraud confirmed and severe)
- Reduce credit limit
- Require authentication for future transactions
- Add to watchlist

**Dispute Actions**:
- File merchant chargebacks (per transaction)
- Initiate card network dispute process
- Document dispute reasons
- Gather supporting evidence for disputes

**Communication Actions**:
- Notify customer of outcome
- Provide fraud prevention guidance
- Offer identity theft protection services
- Send account security recommendations

**Recovery Actions**:
- Provisional credit to customer
- Recovery strategy formulation
- Estimated recovery amount
- Recovery timeline

**Regulatory Actions** (if applicable):
- SAR filing (if threshold met)
- Law enforcement referral
- Credit bureau notification
- Other regulatory requirements

---

### Step 8: Action Taken
**Duration**: Variable (hours to days)

**Execution and Documentation**:

**Card/Account Actions**:
```json
{
  "timestamp": "2025-01-20T14:30:00Z",
  "action": "card_blocked",
  "reason": "Confirmed fraud - account takeover",
  "performed_by": "fraud_ops_team",
  "reversible": true,
  "customer_notified": true,
  "notification_method": "SMS + Email"
}
```

**Dispute Filing**:
- File disputes for each fraudulent transaction
- Track dispute ID and status
- Monitor merchant responses
- Escalate if disputes denied
- Document all correspondence

**Customer Communication**:
- Call or email customer with outcome
- Explain actions taken
- Provide fraud prevention tips
- Offer identity theft services
- Document customer response

**Recovery Initiation**:
- Issue provisional credit (Regulation E: 10 business days)
- Track recovery efforts
- Update recovery status
- Final settlement

---

### Step 9: Recovery Initiated
**Duration**: 30-90 days (chargeback process)

**Recovery Methods**:

**Merchant Chargebacks**:
- Timeline: 30-90 days
- Success Rate: 60-80% (varies by merchant)
- Process: Dispute filed → Merchant response → Resolution
- Requirements: Evidence package, dispute reason code

**Card Network Claims**:
- Timeline: 45-120 days
- Success Rate: 50-70%
- Process: Claim filed → Investigation → Settlement

**Direct Recovery** (if perpetrator identified):
- Timeline: Months to years
- Success Rate: 10-30%
- Process: Law enforcement → Prosecution → Restitution

**Insurance Claims** (if applicable):
- Timeline: 30-60 days
- Success Rate: 80-95%
- Process: Claim filed → Investigation → Payout

**Recovery Tracking**:
```json
{
  "total_loss": 45000.00,
  "recovery_strategy": [
    {
      "method": "merchant_chargeback",
      "amount_claimed": 45000.00,
      "transactions": 15,
      "status": "in_progress",
      "expected_recovery": 31500.00,  // 70%
      "timeline_days": 60
    }
  ],
  "provisional_credit_issued": 45000.00,
  "provisional_credit_date": "2025-01-22",
  "expected_total_recovery": 31500.00,
  "expected_net_loss": 13500.00
}
```

---

### Step 10: Case Closure
**Duration**: 30 minutes - 1 hour

**Closure Requirements**:

**Outcome Documentation**:
```json
{
  "case_id": "INV-2025-00234",
  "closure_date": "2025-03-20T15:00:00Z",
  "final_determination": "fraud_confirmed",
  "determination_confidence": 0.95,

  "financial_outcome": {
    "total_loss": 45000.00,
    "amount_recovered": 31500.00,
    "recovery_rate": 0.70,
    "net_loss": 13500.00,
    "provisional_credit": 45000.00,
    "insurance_payout": 0.00
  },

  "actions_taken": [
    "card_blocked",
    "chargebacks_filed",
    "customer_credited",
    "fraud_prevention_guidance_sent"
  ],

  "sar_filed": true,
  "sar_id": "SAR-2025-00045",
  "law_enforcement_notified": false,

  "resolution_timeline": {
    "detection_to_block": "2 minutes",
    "detection_to_investigation": "5 minutes",
    "investigation_to_determination": "6 hours",
    "determination_to_recovery": "2 days",
    "total_case_duration": "60 days"
  }
}
```

**Lessons Learned**:
- What worked well in this investigation?
- What could be improved?
- New fraud patterns discovered?
- Process improvements identified?
- Training needs identified?

**Metrics Update**:
```python
case_metrics = {
    "sla_met": True,  # Was case resolved within SLA?
    "fraud_detected": True,
    "amount_involved": 45000.00,
    "recovery_rate": 0.70,
    "time_to_detection": 120,  # seconds
    "time_to_investigation": 300,  # seconds
    "time_to_resolution": 21600,  # seconds (6 hours)
    "customer_impact": "minimal",  # Full provisional credit
    "pattern_type": "account_takeover",
    "detection_method": "automated_monitoring"
}

# Update global metrics
update_performance_metrics(case_metrics)
```

**Case Archival**:
- Move case files to archive directory
- Maintain for 5 years (regulatory requirement)
- Index for future pattern matching
- Make searchable for similar case lookups

---

## SLA Management

### SLA Tracking

**Calculate SLA Deadline**:
```python
def calculate_sla_deadline(case_created_time, priority):
    sla_hours = {
        "P1": 4,
        "P2": 24,
        "P3": 48,
        "P4": 120  # 5 business days
    }

    deadline = case_created_time + timedelta(hours=sla_hours[priority])
    return deadline
```

**Monitor SLA Status**:
```python
def check_sla_status(deadline, current_time):
    time_remaining = (deadline - current_time).total_seconds() / 3600  # hours

    if time_remaining < 0:
        return "BREACHED"
    elif time_remaining < sla_hours * 0.1:  # <10% remaining
        return "CRITICAL"
    elif time_remaining < sla_hours * 0.25:  # <25% remaining
        return "AT_RISK"
    else:
        return "ON_TRACK"
```

**Auto-Escalation**:
```python
escalation_triggers = {
    "P1": {
        "manager_alert": deadline - timedelta(minutes=30),
        "executive_alert": deadline - timedelta(minutes=10)
    },
    "P2": {
        "senior_analyst": deadline - timedelta(hours=4),
        "manager_alert": deadline - timedelta(hours=1)
    },
    "P3": {
        "team_lead": deadline - timedelta(hours=8)
    }
}
```

---

## Evidence Collection Standards

### Evidence Integrity

**Checklist**:
- ✅ Original source documented
- ✅ Collection timestamp recorded
- ✅ Collector identified
- ✅ File hash calculated (SHA-256)
- ✅ No alterations made to original
- ✅ Chain of custody maintained
- ✅ Secure storage location
- ✅ Access logging enabled

### Evidence Preservation

**Retention Periods**:
- Case files: 5 years minimum (regulatory)
- Transaction records: 5 years
- Customer communications: 5 years
- SAR-related evidence: 5 years
- Closed cases: Archive but maintain searchability

---

## Related Case Identification

### Search Criteria

**Primary Matches**:
- Same fraud pattern type
- Similar transaction amounts (±20%)
- Same merchant(s)
- Same customer (previous incidents)
- Same geographic region

**Secondary Matches**:
- Similar time patterns
- Similar velocity characteristics
- Similar device fingerprints
- Similar IP addresses

### Similarity Scoring

```python
def calculate_case_similarity(case1, case2):
    scores = []

    # Pattern match (40% weight)
    if case1.pattern == case2.pattern:
        scores.append(1.0 * 0.40)
    elif case1.pattern in case2.secondary_patterns:
        scores.append(0.5 * 0.40)
    else:
        scores.append(0.0)

    # Amount similarity (20% weight)
    amount_ratio = min(case1.amount, case2.amount) / max(case1.amount, case2.amount)
    scores.append(amount_ratio * 0.20)

    # Temporal similarity (15% weight)
    if abs((case1.date - case2.date).days) < 30:
        scores.append(1.0 * 0.15)
    elif abs((case1.date - case2.date).days) < 90:
        scores.append(0.7 * 0.15)
    else:
        scores.append(0.3 * 0.15)

    # Merchant match (15% weight)
    merchant_overlap = len(set(case1.merchants) & set(case2.merchants))
    merchant_total = len(set(case1.merchants) | set(case2.merchants))
    scores.append((merchant_overlap / merchant_total) * 0.15 if merchant_total > 0 else 0)

    # Indicator overlap (10% weight)
    indicator_overlap = len(set(case1.indicators) & set(case2.indicators))
    indicator_total = len(set(case1.indicators) | set(case2.indicators))
    scores.append((indicator_overlap / indicator_total) * 0.10 if indicator_total > 0 else 0)

    return sum(scores)
```

---

## Best Practices

### Investigation Quality

1. **Follow the Process**: Complete all 10 steps systematically
2. **Document Everything**: Comprehensive audit trail
3. **Evidence First**: Collect evidence before forming conclusions
4. **Customer Communication**: Keep customer informed throughout
5. **SLA Discipline**: Track deadlines, escalate proactively
6. **Chain of Custody**: Maintain evidence integrity
7. **Learn from History**: Search for similar cases
8. **Quality Over Speed**: Thorough investigation prevents errors

### Common Pitfalls to Avoid

- ❌ Skipping evidence collection (weakens case)
- ❌ Assuming fraud without verification (false positives)
- ❌ Poor customer communication (customer dissatisfaction)
- ❌ Missing SLA deadlines (operational failure)
- ❌ Incomplete documentation (audit/compliance issues)
- ❌ Ignoring contradictory evidence (bias)
- ❌ Not learning from historical cases (missed patterns)

---

## Summary

**This skill provides**:
- Complete 10-step investigation framework
- Evidence collection standards and requirements
- SLA management procedures (P1/P2/P3/P4)
- Chain of custody protocols
- Related case identification methods
- Outcome determination guidelines
- Recovery process workflows
- Case closure and metrics tracking

**Use this skill to**:
- Conduct thorough fraud investigations
- Maintain evidence integrity
- Meet SLA requirements
- Document comprehensive findings
- Maximize recovery rates
- Ensure regulatory compliance
- Learn from historical patterns

**Remember**: A well-documented investigation protects the institution legally, supports recovery efforts, enables regulatory compliance, and improves future fraud detection.
