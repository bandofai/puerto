# Tax Tracking Skill

Comprehensive patterns and methodologies for tracking tax obligations, monitoring deadlines, and managing multi-jurisdiction compliance requirements.

## Purpose

This skill provides standardized frameworks for:
- Obligation identification and classification
- Deadline calculation and tracking
- Alert threshold management
- Multi-entity coordination
- Status tracking taxonomies
- Calendar integration methods

## Core Concepts

### 1. Obligation Classification

All tax obligations should be classified by:

**Jurisdiction Levels**:
- Federal (IRS)
- State (FTB, DTF, Comptroller, etc.)
- Local (City, County)

**Form Categories**:
- Income tax returns (1040, 1120, 1120-S, 1065)
- Information returns (W-2, 1099, K-1)
- Payroll tax reports (941, 940)
- Excise tax returns (720, 2290)
- Sales/use tax filings
- Property tax declarations

**Frequency Patterns**:
- Annual (once per year)
- Quarterly (four times per year)
- Monthly (twelve times per year)
- Semi-annual (twice per year)
- Event-driven (on occurrence)

**Priority Levels**:
- Critical: Penalties >$1,000 or criminal implications
- High: Penalties $100-$1,000
- Medium: Penalties <$100
- Low: No direct penalty (compliance quality)

### 2. Deadline Calculation Methodology

#### Basic Deadline Rules

**Federal Returns**:
- C-Corps (1120): 15th day of 4th month after year-end
- S-Corps (1120-S): 15th day of 3rd month after year-end
- Partnerships (1065): 15th day of 3rd month after year-end
- Individuals (1040): April 15 (calendar year filers)
- Quarterly payroll (941): Last day of month following quarter
- Annual payroll (940): January 31

**Extension Deadlines**:
- C-Corps: +6 months (automatic with Form 7004)
- S-Corps: +6 months (automatic with Form 7004)
- Partnerships: +6 months (automatic with Form 7004)
- Individuals: +6 months (automatic with Form 4868)

**Weekend/Holiday Rules**:
When deadline falls on weekend or federal holiday, deadline extends to next business day.

```bash
# Weekend/Holiday Adjustment Algorithm
calculate_due_date() {
    local raw_date="$1"
    local day_of_week=$(date -d "$raw_date" +%u)  # 1=Mon, 7=Sun

    # If Saturday (6), move to Monday
    if [ "$day_of_week" -eq 6 ]; then
        date -d "$raw_date + 2 days" +%Y-%m-%d
    # If Sunday (7), move to Monday
    elif [ "$day_of_week" -eq 7 ]; then
        date -d "$raw_date + 1 day" +%Y-%m-%d
    else
        echo "$raw_date"
    fi

    # TODO: Check federal holiday calendar and adjust if needed
}
```

### 3. Alert Threshold Framework

Implement multi-level alert system:

**Standard Alert Schedule**:

| Threshold | Days Before | Priority | Action Required |
|-----------|------------|----------|-----------------|
| Advance Warning | 30 days | Low | Begin planning, gather documentation |
| Reminder | 14 days | Medium | Confirm preparation underway |
| Urgent | 7 days | High | Daily status checks, prioritize completion |
| Critical | 1 day | Critical | Emergency status, same-day completion |

**Escalation Procedures**:

```markdown
## 30-Day Alert (Advance Warning)
**Recipients**: Assigned preparer, entity contact
**Actions**:
- Email notification sent
- Added to preparation schedule
- Documentation gathering begins
**Escalation**: None at this stage

## 14-Day Alert (Reminder)
**Recipients**: Assigned preparer, entity contact, supervisor (CC)
**Actions**:
- Confirm preparation started
- Review documentation completeness
- Assess progress toward completion
**Escalation**: If no progress, escalate to supervisor

## 7-Day Alert (Urgent)
**Recipients**: All above + management
**Actions**:
- Daily status updates required
- Reprioritize other work if needed
- Consider extension filing if at risk
**Escalation**: Daily status reports to management

## 1-Day Alert (Critical)
**Recipients**: All above + emergency contacts
**Actions**:
- Emergency status declared
- All resources focused on completion
- File extension immediately if cannot complete
**Escalation**: Immediate management involvement, post-mortem required
```

### 4. Status Tracking Taxonomy

Use consistent status nomenclature:

**Status Progression**:

1. **pending**: Obligation identified, not yet started
   - Deadline tracked
   - No action taken yet
   - Documentation not gathered

2. **documentation_gathering**: Initial work begun
   - Source documents being collected
   - Templates prepared
   - Preparer assigned

3. **in_preparation**: Active preparation underway
   - Forms being completed
   - Calculations in progress
   - Draft being created

4. **ready_for_review**: Preparation complete, awaiting validation
   - Filing package complete
   - Ready for compliance check
   - No further preparation needed

5. **under_review**: Compliance validation in progress
   - Being reviewed by compliance-checker
   - Findings being generated
   - Awaiting approval

6. **revision_required**: Issues identified, needs correction
   - Compliance findings returned
   - Corrections being made
   - Will return to ready_for_review when done

7. **approved**: Validation passed, ready to file
   - All compliance checks passed
   - Final approval received
   - Can proceed to filing

8. **filed**: Successfully submitted
   - Submission confirmed
   - Confirmation number obtained
   - Payment processed (if due)

9. **completed**: Fully processed
   - Filing accepted by taxing authority
   - Refund received (if applicable)
   - Documentation archived

10. **extended**: Extension filed, new deadline
    - Extension form submitted
    - New deadline set
    - Return to pending status with new date

11. **delinquent**: Missed deadline
    - Deadline passed without filing
    - Penalty assessment likely
    - Emergency filing required

**Status Transitions**:

```
pending → documentation_gathering → in_preparation → ready_for_review
                                                           ↓
delinquent ← filed ← approved ← under_review → revision_required
    ↓           ↓                  ↑                ↓
[emergency]  completed         [resubmit] ← ←  ← ← ↑
    ↓
  filed → completed

extended → pending (with new deadline)
```

### 5. Multi-Jurisdiction Coordination

Track obligations across jurisdictions systematically:

**Jurisdiction Mapping**:

```json
{
  "entity": "Acme Corporation",
  "ein": "12-3456789",
  "fiscal_year_end": "12-31",
  "jurisdictions": {
    "federal": {
      "obligations": [
        {
          "form": "1120",
          "frequency": "annual",
          "base_due": "4th month, 15th day",
          "extension": "+6 months"
        },
        {
          "form": "941",
          "frequency": "quarterly",
          "base_due": "last day of month after quarter",
          "extension": "none"
        },
        {
          "form": "940",
          "frequency": "annual",
          "base_due": "January 31",
          "extension": "none"
        }
      ]
    },
    "state": {
      "CA": {
        "obligations": [
          {
            "form": "100 (Franchise Tax)",
            "frequency": "annual",
            "base_due": "4th month, 15th day",
            "extension": "+6 months",
            "conforms_to_federal": true
          },
          {
            "form": "DE-9 (Payroll)",
            "frequency": "quarterly",
            "base_due": "last day of month after quarter",
            "conforms_to_federal": true
          }
        ]
      },
      "NY": {
        "obligations": [
          {
            "form": "CT-3 (Franchise Tax)",
            "frequency": "annual",
            "base_due": "3rd month, 15th day",
            "extension": "+6 months",
            "conforms_to_federal": false
          }
        ]
      }
    },
    "local": {
      "San Francisco, CA": {
        "obligations": [
          {
            "form": "Business Registration",
            "frequency": "annual",
            "base_due": "January 31",
            "extension": "none"
          },
          {
            "form": "Payroll Expense Tax",
            "frequency": "quarterly",
            "base_due": "last day of month after quarter",
            "extension": "none"
          }
        ]
      }
    }
  }
}
```

**Conformity Tracking**:

Many states conform to federal deadlines. Track conformity to coordinate filings:

- **Conforming States**: When federal deadline extends, state often extends too
- **Non-Conforming States**: Maintain separate deadline tracking
- **Partial Conforming**: Some obligations conform, others don't

### 6. Multi-Entity Management

Coordinate obligations across multiple entities:

**Entity Grouping Strategies**:

```markdown
## By Entity Type
- C-Corporations (1120 filers)
- S-Corporations (1120-S filers)
- Partnerships (1065 filers)
- Individuals (1040 filers)

## By Fiscal Year End
- Calendar year (12/31)
- June 30 fiscal year
- September 30 fiscal year
- Other fiscal years

## By Jurisdiction
- Federal only
- Multi-state filers
- International operations

## By Complexity
- Simple (single-jurisdiction, standard forms)
- Moderate (multi-state, some complexity)
- Complex (multi-national, special forms)
```

**Batch Processing Opportunities**:

Identify entities with similar obligations for efficient preparation:

```markdown
## Q1 2025 Payroll Tax Filings (Form 941)

### All Entities - Due April 30, 2025

| Entity | Preparer | Status | Alert Date |
|--------|----------|--------|------------|
| Acme Corp | John | in_preparation | April 16 (14-day) |
| Beta LLC | John | in_preparation | April 16 (14-day) |
| Gamma Inc | Sarah | ready_for_review | April 16 (14-day) |
| Delta Corp | Sarah | pending | April 16 (14-day) |

**Batch Action**: John can prepare Acme and Beta together (similar payroll profiles)
**Batch Action**: Sarah can review Gamma and start Delta in same session
```

### 7. Calendar Integration Methods

**Data Export Formats**:

```ics
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Claude Tax Tracker//EN
BEGIN:VEVENT
UID:2025-federal-1120-acme@tax-compliance
DTSTAMP:20250101T120000Z
DTSTART:20250415T235959Z
SUMMARY:DUE: Federal 1120 - Acme Corporation
DESCRIPTION:Federal Form 1120 Corporate Return\nTax Year: 2024\nEntity: Acme Corporation\nStatus: in_preparation
LOCATION:IRS
BEGIN:VALARM
TRIGGER:-P30D
DESCRIPTION:30-Day Alert: Begin preparation
END:VALARM
BEGIN:VALARM
TRIGGER:-P14D
DESCRIPTION:14-Day Alert: Confirm progress
END:VALARM
BEGIN:VALARM
TRIGGER:-P7D
DESCRIPTION:7-Day Alert: URGENT - Complete soon
END:VALARM
BEGIN:VALARM
TRIGGER:-P1D
DESCRIPTION:1-Day Alert: CRITICAL - File today
END:VALARM
END:VEVENT
END:VCALENDAR
```

### 8. Recurring Obligation Patterns

Automate recurring obligation generation:

**Annual Pattern**:
```bash
generate_annual_obligations() {
    local entity="$1"
    local year="$2"

    # C-Corp annual obligations
    if [ "$entity_type" == "c-corp" ]; then
        create_obligation "$entity" "Federal 1120" "$year-04-15" "annual"
        create_obligation "$entity" "Form 940 (Unemployment)" "$year-01-31" "annual"
    fi

    # Generate quarterly payroll
    for quarter in Q1 Q2 Q3 Q4; do
        due_date=$(calculate_941_due_date "$quarter" "$year")
        create_obligation "$entity" "Form 941 $quarter" "$due_date" "quarterly"
    done
}
```

**Quarterly Pattern**:
```bash
calculate_941_due_date() {
    local quarter="$1"
    local year="$2"

    case "$quarter" in
        Q1) echo "${year}-04-30" ;;  # Jan-Mar, due Apr 30
        Q2) echo "${year}-07-31" ;;  # Apr-Jun, due Jul 31
        Q3) echo "${year}-10-31" ;;  # Jul-Sep, due Oct 31
        Q4) echo "${year}-01-31" ;;  # Oct-Dec, due Jan 31 next year
    esac
}
```

### 9. Dashboard Design Patterns

**Executive Dashboard** (High-level overview):
```markdown
# Tax Compliance Dashboard
Generated: 2025-03-21

## Status Summary
- Total Obligations: 45
- Completed: 28 (62%)
- In Progress: 10 (22%)
- Pending: 5 (11%)
- Delinquent: 2 (4%) ⚠️

## Critical Alerts (Next 7 Days)
- **URGENT**: 3 obligations due within 7 days
- **AT RISK**: 1 obligation with no progress

## Upcoming (Next 30 Days)
- 8 obligations due within 30 days
- 6 in preparation (on track)
- 2 pending (need to start)

## Recent Activity
- Last 7 days: 4 obligations completed
- This month: 12 obligations completed
- On-time filing rate: 95%
```

**Detailed Dashboard** (Full obligation list):
```markdown
# Detailed Obligation Tracking

## Critical - Next 7 Days

### Due: April 15, 2025 (3 days)
1. **Federal Form 1120 - Acme Corporation TY 2024**
   - Status: ready_for_review
   - Preparer: John Smith
   - Progress: 95% (awaiting compliance check)
   - Risk: Low (on track)

2. **State CA 100 - Acme Corporation TY 2024**
   - Status: in_preparation
   - Preparer: John Smith
   - Progress: 70% (schedules in progress)
   - Risk: Medium (tight timeline)

### Due: April 18, 2025 (6 days)
3. **State NY CT-3 - New York Holdings TY 2024**
   - Status: pending
   - Preparer: Sarah Johnson
   - Progress: 0% (not started)
   - Risk: HIGH ⚠️ (no progress yet)

## Upcoming - Next 30 Days

### Due: April 30, 2025 (18 days)
4. **Federal Form 941 Q1 - Acme Corporation**
   - Status: in_preparation
   - Preparer: John Smith
   - Progress: 40%
   - Risk: Low

5. **State DE-9 Q1 - Acme Corporation (California)**
   - Status: in_preparation
   - Preparer: John Smith
   - Progress: 40%
   - Risk: Low

[... additional obligations ...]

## Recently Completed

### Completed This Week
- ✓ Federal 941 Q4 2024 - Beta LLC (Completed: 4/10/2025)
- ✓ State NY DTF-17 Q4 2024 - Gamma Inc (Completed: 4/12/2025)

### Completed This Month
[... list ...]
```

### 10. Performance Optimization

**Efficiency Patterns**:

1. **Batch Date Calculations**: Calculate all deadlines for year at once
2. **Cache Results**: Store calculated deadlines, recalculate only when regulations change
3. **Incremental Updates**: Update only changed obligations, not entire database
4. **Indexed Queries**: Index obligations by due date, entity, and status for fast retrieval
5. **Parallel Processing**: Check multiple jurisdictions simultaneously

**Data Structure Optimization**:

```json
{
  "obligations_by_date": {
    "2025-04-15": [
      "federal-1120-acme-2024",
      "state-ca-100-acme-2024",
      "federal-1040-john-doe-2024"
    ]
  },
  "obligations_by_entity": {
    "acme-corporation": [
      "federal-1120-acme-2024",
      "federal-941-q1-acme-2025",
      "state-ca-100-acme-2024"
    ]
  },
  "obligations_by_status": {
    "in_preparation": [
      "federal-941-q1-acme-2025",
      "state-ca-de9-q1-acme-2025"
    ]
  }
}
```

## Common Pitfalls to Avoid

1. **Not Accounting for Weekends/Holidays**: Always adjust for business days
2. **Forgetting Extensions**: Track extended deadlines separately
3. **Ignoring State Differences**: States may not conform to federal deadlines
4. **Missing Local Obligations**: City/county taxes often overlooked
5. **Not Tracking Payments Separately**: Payment deadlines sometimes differ from filing
6. **Static Alert Dates**: Recalculate alerts when deadlines change
7. **No Escalation Process**: Critical deadlines need management visibility
8. **Incomplete Status Updates**: Real-time status crucial for accurate tracking
9. **Not Coordinating Multi-Entity**: Batch opportunities missed
10. **Forgetting Prior Year Issues**: Review prior year problems and document

## Integration with Other Skills

This tax-tracking skill integrates with:

- **filing-preparation**: Tracking triggers preparation workflow
- **compliance-validation**: Status updates after validation complete
- **regulation-monitor**: Deadline changes from regulation updates

## Best Practices Summary

✓ Classify all obligations by jurisdiction, frequency, and priority
✓ Implement multi-level alert system (30/14/7/1 days)
✓ Use consistent status taxonomy across all obligations
✓ Coordinate multi-jurisdiction tracking with conformity awareness
✓ Batch similar obligations for efficiency
✓ Integrate with calendar systems for visibility
✓ Generate recurring obligations automatically
✓ Maintain executive and detailed dashboards
✓ Optimize data structures for performance
✓ Escalate critical deadlines appropriately

---

**This skill enables professional, systematic tax obligation tracking that prevents missed deadlines and ensures compliance across all jurisdictions.**
