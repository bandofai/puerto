# Policy Validation Skill

**Expert frameworks for expense policy compliance checking and risk assessment**

## Core Principles

1. **Independence**: Validators must be read-only (no data modification)
2. **Consistency**: Same rules applied uniformly to all expenses
3. **Transparency**: Clear citations for every policy violation
4. **Risk-Based**: Prioritize by impact and likelihood
5. **Actionable**: Every finding includes remediation guidance

---

## Validation Framework

### Three-Tier Validation Model

**Tier 1: Structural Validation** (Data integrity)
- Required fields present
- Data types correct
- Formats valid
- References exist

**Tier 2: Policy Rule Validation** (Compliance)
- Amount limits
- Category restrictions
- Receipt requirements
- Timeframe compliance

**Tier 3: Context & Risk Validation** (Fraud detection)
- Spending patterns
- Duplicate detection
- Logic consistency
- Anomaly detection

---

## Policy Rule Engine

### Rule Definition Format

```json
{
  "policy_version": "2025.1",
  "effective_date": "2025-01-01",
  "rules": {
    "meals_and_entertainment": {
      "category_id": "meals",
      "rules": [
        {
          "rule_id": "meals_per_meal_limit",
          "type": "amount_limit",
          "condition": "per_transaction",
          "limit": 50.00,
          "severity": "warning",
          "action": "require_justification",
          "citation": "Company Policy §4.3.2"
        },
        {
          "rule_id": "meals_daily_limit",
          "type": "amount_limit",
          "condition": "per_day",
          "limit": 75.00,
          "severity": "high",
          "action": "require_manager_approval",
          "citation": "Company Policy §4.3.2"
        },
        {
          "rule_id": "meals_alcohol_limit",
          "type": "amount_limit",
          "condition": "per_transaction",
          "limit": 25.00,
          "severity": "high",
          "action": "require_manager_approval",
          "citation": "Company Policy §4.3.4"
        },
        {
          "rule_id": "meals_attendees_required",
          "type": "required_field",
          "field": "attendees",
          "condition": "amount > 50",
          "severity": "medium",
          "action": "request_information",
          "citation": "Company Policy §4.3.5"
        }
      ]
    },
    "lodging": {
      "category_id": "lodging",
      "rules": [
        {
          "rule_id": "lodging_standard_city_limit",
          "type": "amount_limit",
          "condition": "per_night",
          "limit": 200.00,
          "applies_to": "cities not in high_cost_list",
          "severity": "warning",
          "action": "require_justification",
          "citation": "Company Policy §4.4.1"
        },
        {
          "rule_id": "lodging_high_cost_city_limit",
          "type": "amount_limit",
          "condition": "per_night",
          "limit": 350.00,
          "applies_to": "high_cost_cities",
          "severity": "warning",
          "action": "require_justification",
          "citation": "Company Policy §4.4.1"
        },
        {
          "rule_id": "lodging_pre_approval",
          "type": "amount_limit",
          "condition": "per_night",
          "limit": 400.00,
          "severity": "critical",
          "action": "reject_without_pre_approval",
          "citation": "Company Policy §4.4.2"
        }
      ],
      "high_cost_cities": ["NYC", "San Francisco", "Los Angeles", "Seattle", "Boston", "Washington DC"]
    },
    "transportation": {
      "category_id": "transportation",
      "rules": [
        {
          "rule_id": "mileage_rate",
          "type": "calculation",
          "formula": "miles * 0.655",
          "severity": "info",
          "citation": "IRS Standard Mileage Rate 2025"
        },
        {
          "rule_id": "parking_limit",
          "type": "amount_limit",
          "condition": "per_transaction",
          "limit": 50.00,
          "severity": "medium",
          "action": "require_justification",
          "citation": "Company Policy §4.5.3"
        },
        {
          "rule_id": "ride_share_limit",
          "type": "amount_limit",
          "condition": "per_trip",
          "limit": 100.00,
          "severity": "high",
          "action": "require_justification",
          "citation": "Company Policy §4.5.4"
        }
      ]
    },
    "general": {
      "rules": [
        {
          "rule_id": "receipt_required_threshold",
          "type": "receipt_requirement",
          "condition": "amount >= 25.00",
          "severity": "critical",
          "action": "reject",
          "citation": "Company Policy §4.2.1, IRS Pub 463"
        },
        {
          "rule_id": "submission_timeframe",
          "type": "timeframe",
          "condition": "within_days_of_expense",
          "days": 30,
          "severity": "high",
          "action": "require_manager_approval",
          "citation": "Company Policy §4.1.3"
        },
        {
          "rule_id": "business_purpose_required",
          "type": "required_field",
          "field": "business_purpose",
          "min_length": 10,
          "severity": "high",
          "action": "request_information",
          "citation": "Company Policy §4.1.2, IRS Requirements"
        }
      ]
    }
  }
}
```

### Rule Evaluation Engine

```python
class PolicyRuleEngine:
    """Evaluate expenses against policy rules"""

    def __init__(self, policy_rules):
        self.policy = policy_rules
        self.findings = []

    def evaluate_expense(self, expense):
        """Run all applicable rules for an expense"""

        # Get category-specific rules
        category_key = expense['category'].lower().replace(' & ', '_').replace(' ', '_')
        category_rules = self.policy['rules'].get(category_key, {}).get('rules', [])

        # Get general rules (apply to all)
        general_rules = self.policy['rules']['general']['rules']

        # Evaluate all rules
        all_rules = category_rules + general_rules

        for rule in all_rules:
            finding = self._evaluate_rule(expense, rule)
            if finding:
                self.findings.append(finding)

        return self.findings

    def _evaluate_rule(self, expense, rule):
        """Evaluate a single rule"""

        rule_type = rule['type']

        if rule_type == 'amount_limit':
            return self._check_amount_limit(expense, rule)
        elif rule_type == 'receipt_requirement':
            return self._check_receipt_requirement(expense, rule)
        elif rule_type == 'required_field':
            return self._check_required_field(expense, rule)
        elif rule_type == 'timeframe':
            return self._check_timeframe(expense, rule)
        elif rule_type == 'calculation':
            return self._check_calculation(expense, rule)

        return None

    def _check_amount_limit(self, expense, rule):
        """Check if amount exceeds limit"""

        amount = expense['amount']
        limit = rule['limit']
        condition = rule['condition']

        # Handle different conditions
        if condition == 'per_transaction':
            if amount > limit:
                return self._create_finding(expense, rule, amount, limit)

        elif condition == 'per_day':
            # Would need to aggregate by day
            pass  # Implement day aggregation logic

        elif condition == 'per_night':
            # For lodging, divide by number of nights
            nights = expense.get('nights', 1)
            per_night = amount / nights
            if per_night > limit:
                return self._create_finding(expense, rule, per_night, limit)

        return None

    def _check_receipt_requirement(self, expense, rule):
        """Check if receipt is required and present"""

        condition = rule['condition']

        # Parse condition (e.g., "amount >= 25.00")
        if 'amount >=' in condition:
            threshold = float(condition.split('>=')[1].strip())
            if expense['amount'] >= threshold:
                if not expense.get('receipt_path') or expense['receipt_path'] == '':
                    return {
                        'expense_id': expense['expense_id'],
                        'rule_id': rule['rule_id'],
                        'severity': rule['severity'],
                        'message': f"Receipt required for amounts ≥ ${threshold}",
                        'action': rule['action'],
                        'citation': rule['citation'],
                        'actual_value': expense['amount'],
                        'expected': f"Valid receipt for ${expense['amount']}"
                    }

        return None

    def _check_required_field(self, expense, rule):
        """Check if required field is present and valid"""

        field = rule['field']
        value = expense.get(field)

        # Check presence
        if not value:
            return {
                'expense_id': expense['expense_id'],
                'rule_id': rule['rule_id'],
                'severity': rule['severity'],
                'message': f"Required field '{field}' is missing",
                'action': rule['action'],
                'citation': rule['citation']
            }

        # Check minimum length if specified
        if 'min_length' in rule:
            if len(str(value)) < rule['min_length']:
                return {
                    'expense_id': expense['expense_id'],
                    'rule_id': rule['rule_id'],
                    'severity': rule['severity'],
                    'message': f"Field '{field}' is too short (min {rule['min_length']} chars)",
                    'action': rule['action'],
                    'citation': rule['citation'],
                    'actual_value': value
                }

        return None

    def _check_timeframe(self, expense, rule):
        """Check if expense is submitted within timeframe"""

        from datetime import datetime, timedelta

        expense_date = datetime.strptime(expense['date'], '%Y-%m-%d')
        submission_date = datetime.now()

        days_elapsed = (submission_date - expense_date).days
        allowed_days = rule['days']

        if days_elapsed > allowed_days:
            return {
                'expense_id': expense['expense_id'],
                'rule_id': rule['rule_id'],
                'severity': rule['severity'],
                'message': f"Expense submitted {days_elapsed} days after date (limit: {allowed_days} days)",
                'action': rule['action'],
                'citation': rule['citation'],
                'expense_date': expense['date'],
                'submission_date': submission_date.strftime('%Y-%m-%d')
            }

        return None

    def _create_finding(self, expense, rule, actual, limit):
        """Create a finding object"""

        return {
            'expense_id': expense['expense_id'],
            'rule_id': rule['rule_id'],
            'severity': rule['severity'],
            'message': f"Amount ${actual:.2f} exceeds limit ${limit:.2f}",
            'action': rule['action'],
            'citation': rule['citation'],
            'actual_value': actual,
            'limit_value': limit,
            'overage': actual - limit
        }
```

---

## Severity Classification

### Severity Levels

**CRITICAL** (Reject/Block):
- Missing required receipts
- Prohibited expense categories
- Amounts exceeding hard limits without pre-approval
- IRS compliance violations
- Potential fraud indicators

**HIGH** (Requires Manager Override):
- Policy limit exceeded (within override range)
- Late submission (>30 days)
- Missing business justification
- Duplicate expense suspected
- Unusual spending pattern

**MEDIUM** (Requires Clarification):
- Incomplete information
- Vague business purpose
- Near policy limits
- Missing optional documentation

**LOW** (Best Practice Suggestions):
- Formatting improvements
- Additional context recommended
- Proactive fraud prevention tips

### Severity Decision Matrix

| Violation Type | Amount | Impact | Severity |
|----------------|--------|--------|----------|
| Missing receipt | ≥$25 | Audit fail | CRITICAL |
| Missing receipt | <$25 | Minor | MEDIUM |
| Over limit | >150% limit | Reject | CRITICAL |
| Over limit | 100-150% limit | Needs approval | HIGH |
| Over limit | 90-100% limit | Warning | MEDIUM |
| Late submission | >60 days | Risk | HIGH |
| Late submission | 30-60 days | Acceptable with approval | MEDIUM |
| Vague purpose | All amounts | Compliance | HIGH |
| Missing attendees | Meals >$50 | Context | MEDIUM |

---

## Duplicate Detection

### Advanced Duplicate Detection

```python
class DuplicateDetector:
    """Detect duplicate expenses with confidence levels"""

    def __init__(self):
        self.thresholds = {
            'exact_match': 1.0,      # Same vendor, date, amount
            'likely_duplicate': 0.85, # Very similar
            'possible_duplicate': 0.70, # Somewhat similar
        }

    def find_duplicates(self, expenses):
        """Find all potential duplicates"""

        duplicates = []

        for i, exp1 in enumerate(expenses):
            for exp2 in expenses[i+1:]:
                similarity = self._calculate_similarity(exp1, exp2)

                if similarity >= self.thresholds['possible_duplicate']:
                    duplicates.append({
                        'expense_1': exp1['expense_id'],
                        'expense_2': exp2['expense_id'],
                        'similarity': similarity,
                        'confidence': self._get_confidence_level(similarity),
                        'details': self._get_match_details(exp1, exp2)
                    })

        return duplicates

    def _calculate_similarity(self, exp1, exp2):
        """Calculate similarity score between two expenses"""

        score = 0.0
        weights = {
            'amount': 0.4,
            'vendor': 0.3,
            'date': 0.2,
            'category': 0.1
        }

        # Amount similarity
        if exp1['amount'] == exp2['amount']:
            score += weights['amount']
        elif abs(exp1['amount'] - exp2['amount']) < 0.01:
            score += weights['amount'] * 0.9

        # Vendor similarity (Levenshtein distance)
        vendor_sim = self._string_similarity(
            exp1['vendor'].lower(),
            exp2['vendor'].lower()
        )
        score += weights['vendor'] * vendor_sim

        # Date similarity
        date1 = exp1['date']
        date2 = exp2['date']

        if date1 == date2:
            score += weights['date']
        else:
            # Check if within 1 day
            from datetime import datetime
            d1 = datetime.strptime(date1, '%Y-%m-%d')
            d2 = datetime.strptime(date2, '%Y-%m-%d')
            days_diff = abs((d2 - d1).days)

            if days_diff <= 1:
                score += weights['date'] * 0.5

        # Category similarity
        if exp1['category'] == exp2['category']:
            score += weights['category']

        return score

    def _string_similarity(self, s1, s2):
        """Calculate string similarity (0.0 to 1.0)"""

        from difflib import SequenceMatcher
        return SequenceMatcher(None, s1, s2).ratio()

    def _get_confidence_level(self, similarity):
        """Convert similarity score to confidence level"""

        if similarity >= self.thresholds['exact_match']:
            return 'exact_match'
        elif similarity >= self.thresholds['likely_duplicate']:
            return 'likely_duplicate'
        elif similarity >= self.thresholds['possible_duplicate']:
            return 'possible_duplicate'
        else:
            return 'not_duplicate'

    def _get_match_details(self, exp1, exp2):
        """Get details of what matches"""

        matches = []

        if exp1['amount'] == exp2['amount']:
            matches.append(f"Same amount (${exp1['amount']})")

        if exp1['vendor'].lower() == exp2['vendor'].lower():
            matches.append(f"Same vendor ({exp1['vendor']})")

        if exp1['date'] == exp2['date']:
            matches.append(f"Same date ({exp1['date']})")

        if exp1['category'] == exp2['category']:
            matches.append(f"Same category ({exp1['category']})")

        return ', '.join(matches)
```

---

## Anomaly Detection

### Spending Pattern Analysis

```python
class AnomalyDetector:
    """Detect unusual spending patterns"""

    def analyze_patterns(self, expenses, historical_data=None):
        """Analyze expense patterns for anomalies"""

        anomalies = []

        # 1. Unusually high single transaction
        anomalies.extend(self._detect_high_transactions(expenses))

        # 2. Frequency anomalies (too many similar expenses)
        anomalies.extend(self._detect_frequency_anomalies(expenses))

        # 3. Geographic inconsistencies
        anomalies.extend(self._detect_geographic_anomalies(expenses))

        # 4. Timing anomalies (unlikely times)
        anomalies.extend(self._detect_timing_anomalies(expenses))

        # 5. Historical comparison (if available)
        if historical_data:
            anomalies.extend(self._detect_historical_anomalies(expenses, historical_data))

        return anomalies

    def _detect_high_transactions(self, expenses):
        """Find transactions significantly higher than median"""

        amounts = [e['amount'] for e in expenses]
        median = sorted(amounts)[len(amounts) // 2]

        anomalies = []

        for expense in expenses:
            if expense['amount'] > median * 3:  # 3x median
                anomalies.append({
                    'type': 'high_transaction',
                    'expense_id': expense['expense_id'],
                    'severity': 'medium',
                    'message': f"Amount ${expense['amount']} is 3x higher than median ${median:.2f}",
                    'recommendation': 'Verify expense legitimacy and business purpose'
                })

        return anomalies

    def _detect_frequency_anomalies(self, expenses):
        """Detect too many similar expenses"""

        from collections import Counter

        anomalies = []

        # Count expenses per vendor per day
        vendor_day_counts = Counter()

        for expense in expenses:
            key = (expense['vendor'], expense['date'])
            vendor_day_counts[key] += 1

        # Flag if >3 expenses from same vendor on same day
        for (vendor, date), count in vendor_day_counts.items():
            if count > 3:
                anomalies.append({
                    'type': 'frequency_anomaly',
                    'severity': 'medium',
                    'message': f"{count} expenses from {vendor} on {date}",
                    'recommendation': 'Verify not duplicate entries'
                })

        return anomalies

    def _detect_geographic_anomalies(self, expenses):
        """Detect expenses in impossible locations/times"""

        anomalies = []

        # Sort by date/time
        sorted_expenses = sorted(expenses, key=lambda e: e['date'])

        for i in range(len(sorted_expenses) - 1):
            curr = sorted_expenses[i]
            next_exp = sorted_expenses[i + 1]

            # Check if same day but different cities
            if curr['date'] == next_exp['date']:
                curr_location = self._extract_location(curr)
                next_location = self._extract_location(next_exp)

                if curr_location and next_location and curr_location != next_location:
                    # Check if distance is too large
                    distance = self._estimate_distance(curr_location, next_location)

                    if distance > 500:  # >500 miles apart
                        anomalies.append({
                            'type': 'geographic_anomaly',
                            'expense_ids': [curr['expense_id'], next_exp['expense_id']],
                            'severity': 'high',
                            'message': f"Expenses in {curr_location} and {next_location} on same day (~{distance} miles apart)",
                            'recommendation': 'Verify travel itinerary or check for errors'
                        })

        return anomalies

    def _extract_location(self, expense):
        """Extract location from expense (if available)"""
        # Would parse from vendor name, business purpose, or metadata
        return expense.get('location') or expense.get('city')

    def _estimate_distance(self, loc1, loc2):
        """Rough distance estimate between cities"""
        # Simplified; would use actual geocoding in production
        city_distances = {
            ('NYC', 'LA'): 2800,
            ('NYC', 'SF'): 2900,
            ('NYC', 'Boston'): 215,
            # ... more cities
        }

        return city_distances.get((loc1, loc2), 0)
```

---

## Compliance Reporting

### Comprehensive Compliance Report

**Report Structure**:
1. **Executive Summary**: Score, status, critical findings
2. **Findings by Severity**: CRITICAL, HIGH, MEDIUM, LOW
3. **Detailed Validation Results**: All three tiers
4. **Remediation Guidance**: Specific actions required
5. **Compliance Score**: Numerical rating
6. **Citations**: Policy/legal references

### Remediation Guidance

**Each finding MUST include**:
- **Problem**: Clear description
- **Risk**: What could happen
- **Fix**: Specific solution with example
- **Citation**: Policy reference
- **Priority**: How urgently to fix

**Example Remediation**:
```markdown
### Finding #1: Missing Receipt

**Problem**: Expense EXP-003 for $287.00 has no receipt attached

**Risk**:
- Audit rejection by IRS
- Reimbursement denial
- Compliance violation
- Potential tax implications

**Fix**:
1. Locate original receipt (email confirmation, credit card statement)
2. Attach to expense report as PDF or image
3. Ensure receipt shows:
   - Date of transaction
   - Vendor name
   - Amount paid
   - Payment method

**Alternative**: If receipt lost, provide:
- Written explanation
- Credit card statement showing charge
- Manager attestation

**Citation**: Company Policy §4.2.1, IRS Publication 463

**Priority**: CRITICAL - Must resolve before approval
```

---

## Best Practices

1. **Read-Only Validation**: Never modify data, only report findings
2. **Consistent Application**: Same rules for everyone
3. **Clear Communication**: Non-technical language for findings
4. **Actionable Guidance**: Tell them HOW to fix, not just WHAT is wrong
5. **Risk-Based Prioritization**: Focus on high-impact issues first
6. **Document Everything**: Trail of all checks performed
7. **Version Control**: Track which policy version was applied
8. **Appeal Process**: Allow employees to contest findings

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: Policy compliance checking, audit preparation, fraud detection
