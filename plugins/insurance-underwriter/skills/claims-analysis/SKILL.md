# Insurance Claims Analysis Skill

Expert guidance for analyzing insurance claims history, identifying risk patterns, and evaluating loss experience for underwriting decisions.

## Overview

This skill provides comprehensive methodologies for reviewing claims data, detecting fraud indicators, calculating loss ratios, and using claims history to inform pricing and underwriting decisions.

## Core Competencies

### 1. Claims History Review

#### Loss Runs Analysis

**Required Information**:
- Claim date (date of loss)
- Report date (when reported)
- Claim type/cause of loss
- Claim status (open/closed)
- Paid amount (to date)
- Reserved amount (open claims)
- Total incurred (paid + reserved)
- Claimant information
- Description of loss

**Standard Review Periods**:
- Personal lines: 5 years minimum
- Commercial lines: 5-7 years
- Workers compensation: 10 years
- Professional liability: 10+ years (long tail)

**Loss Run Format Requirements**:
- ACORD standard format preferred
- Complete claim detail (not summary only)
- Current as of recent date (within 60 days)
- All policies with current/prior carriers
- Include "zero loss" confirmations

#### Claims Data Extraction

**Key Metrics to Calculate**:

**Frequency** (number of claims):
```
Claim Frequency = Number of Claims / Exposure Units
```

**Severity** (average claim cost):
```
Average Severity = Total Incurred / Number of Claims
```

**Loss Ratio**:
```
Loss Ratio = Total Incurred Losses / Total Premium × 100
```

**Pure Premium**:
```
Pure Premium = Total Incurred / Exposure Units
```

**Example Analysis**:
```
Review Period: 5 years
Policies: Homeowners insurance
Claims:
- Year 1: 0 claims, Premium $1,200
- Year 2: 1 claim ($5,000 water damage), Premium $1,250
- Year 3: 0 claims, Premium $1,300
- Year 4: 1 claim ($2,500 theft), Premium $1,350
- Year 5: 0 claims, Premium $1,400

Totals:
- Claims: 2
- Total Incurred: $7,500
- Total Premium: $6,500
- Exposure: 5 policy years

Frequency: 2 / 5 = 0.40 claims per year
Severity: $7,500 / 2 = $3,750 per claim
Loss Ratio: $7,500 / $6,500 = 115%
Pure Premium: $7,500 / 5 = $1,500 per year
```

### 2. Frequency and Severity Analysis

#### Frequency Patterns

**Personal Lines Benchmarks**:

**Homeowners**:
- Excellent: 0 claims in 5 years (0%)
- Good: 1 claim in 5 years (20%)
- Average: 2 claims in 5 years (40%)
- Poor: 3 claims in 5 years (60%)
- Unacceptable: 4+ claims in 5 years (80%+)

**Auto**:
- Excellent: 0 claims in 5 years
- Good: 1 claim in 5 years
- Average: 2 claims in 5 years
- Poor: 3 claims in 5 years
- Unacceptable: 4+ claims in 5 years

**Commercial Lines Benchmarks**:

**General Liability**:
- Excellent: <0.10 claims per $100K receipts
- Good: 0.10-0.25 claims per $100K receipts
- Average: 0.25-0.50 claims per $100K receipts
- Poor: 0.50-1.00 claims per $100K receipts
- Unacceptable: >1.00 claims per $100K receipts

**Workers Compensation**:
- Excellent: <2 claims per 100 employees
- Good: 2-4 claims per 100 employees
- Average: 4-8 claims per 100 employees
- Poor: 8-15 claims per 100 employees
- Unacceptable: >15 claims per 100 employees

#### Severity Analysis

**Small Claims** (<$2,500):
- Nuisance level
- May indicate claims consciousness
- Watch for pattern (many small claims = red flag)
- Low impact on pricing

**Medium Claims** ($2,500-$25,000):
- Standard severity range
- Typical homeowner/auto claims
- Expected in normal claim experience
- Moderate pricing impact

**Large Claims** ($25,000-$100,000):
- Significant losses
- Require detailed investigation
- May indicate serious exposure
- Substantial pricing impact

**Catastrophic Claims** (>$100,000):
- Major losses
- Often total losses or serious liability
- Require senior underwriter review
- May be declination factor

**Severity Trends to Watch**:
- Escalating severity (small → medium → large)
- Consistent high-severity claims
- Severity increasing faster than inflation
- Single large claim vs. pattern of smaller claims

### 3. Claim Type Analysis

#### Property Claims

**Water Damage**:
- Single incident: May be acceptable
- Multiple water claims: Major red flag
- Indicates maintenance issues
- May require inspection

**Categories**:
- Plumbing failure: Common, usually acceptable
- Roof leak: Check roof age/condition
- Basement seepage: Chronic issue concern
- Appliance failure: Generally acceptable
- Frozen pipes: Check insulation/heating

**Red Flags**:
- 2+ water claims in 3 years
- Same cause recurring
- Mold involvement
- No preventive action taken

**Fire Claims**:
- Cooking fire (small): Generally acceptable
- Electrical fire: Check wiring status
- Heating system: Check maintenance
- Arson suspected: Investigate thoroughly
- Total loss: Detailed review required

**Assessment Factors**:
- Cause determination
- Prevention measures taken
- Property improvements made
- Fire department report available

**Theft Claims**:
- Single theft: Usually acceptable
- Multiple thefts: Security concern
- High-value items: Verify security
- Location factor: Crime statistics

**Considerations**:
- Security improvements made
- Neighborhood watch participation
- Alarm system installed
- High-risk items secured

**Wind/Hail Claims**:
- Catastrophic event: More acceptable
- Isolated damage: Check property condition
- Roof age: Verify if replacement needed
- Multiple wind claims: Durability concern

**Weather vs. Maintenance**:
- CAT event (hurricane, tornado): Acceptable
- Normal weather exposure: May indicate deferred maintenance
- Roof damage pattern: Age vs. storm

#### Liability Claims

**Premises Liability**:
- Slip and fall: Investigate circumstances
- Dog bite: Breed restrictions may apply
- Swimming pool: Verify safety measures
- Trampoline: Often excluded

**Severity Considerations**:
- Bodily injury severity
- Legal representation involved
- Claim duration (open how long)
- Lawsuit filed vs. settled

**Auto Liability**:
- At-fault accidents: Major factor
- Severity of injuries
- Multiple vehicles involved
- Distracted driving involved

**Pattern Analysis**:
- Frequency of at-fault claims
- Type of accidents (rear-end, side-swipe)
- Time of day/conditions
- Passengers injured

#### First-Party Auto Claims

**Comprehensive** (not-at-fault):
- Theft: Acceptable, verify recovery
- Vandalism: Isolated incident OK
- Weather: Hail, flood - acceptable
- Animal collision: Acceptable

**Collision** (may be at-fault):
- Single accident: Verify fault
- Multiple collisions: Pattern concern
- Backing accidents: Driver care issue
- Parking lot incidents: Minor

### 4. Claims Pattern Recognition

#### Red Flag Patterns

**Multiple Claims - Same Type**:
- 3+ water damage claims: Maintenance failure
- 2+ fire claims: Serious concern
- 3+ theft claims: Security inadequate
- Multiple liability claims: Hazard present

**Escalating Frequency**:
```
Year 1: 0 claims
Year 2: 1 claim
Year 3: 1 claim
Year 4: 2 claims
Year 5: 3 claims
Trend: Increasing risk/claims consciousness
```

**Suspicious Timing**:
- Claim shortly after inception: Possible concealment
- Claim just before policy cancellation: Timing concern
- Multiple claims near policy anniversary: Pattern
- Large claim after coverage increase: Investigation needed

**Geographic Clustering**:
- All claims in same location: Property issue
- Claims following moves: Possible fraud
- Claims in multiple states: Verify accuracy

#### Positive Indicators

**Long Claims-Free Period**:
- 5+ years no claims: Excellent
- 7+ years no claims: Preferred pricing
- 10+ years no claims: Maximum discount

**Claim Responsiveness**:
- Prompt reporting
- Cooperation with investigation
- Reasonable expectations
- Accepted settlement offers

**Post-Claim Improvements**:
- Security system installed after theft
- Plumbing upgraded after water damage
- Roof replaced after wind damage
- Loss control measures implemented

### 5. Loss Ratio Calculations

#### Personal Lines Loss Ratios

**Acceptable Ranges**:
- Homeowners: 40%-60% target
- Auto: 60%-70% target
- Umbrella: 30%-40% target

**Premium-to-Loss Relationship**:

**Profitable** (Loss Ratio <50%):
- Few or no claims
- Premium adequate for risk
- Preferred renewal pricing

**Acceptable** (Loss Ratio 50%-70%):
- Normal claim activity
- Premium aligned with risk
- Standard renewal pricing

**Marginal** (Loss Ratio 70%-90%):
- Higher claim frequency/severity
- Premium may be inadequate
- Rate increase likely at renewal

**Unprofitable** (Loss Ratio >90%):
- Excessive losses
- Premium significantly inadequate
- Major rate increase or non-renewal

**Example Calculation**:
```
5-Year Commercial General Liability Review:

Year 1: Premium $10,000, Losses $3,000
Year 2: Premium $10,500, Losses $15,000
Year 3: Premium $11,000, Losses $5,000
Year 4: Premium $11,500, Losses $8,000
Year 5: Premium $12,000, Losses $2,000

Totals:
Total Premium: $55,000
Total Losses: $33,000
Loss Ratio: $33,000 / $55,000 = 60%

Assessment: Acceptable range for GL
Action: Standard renewal, modest increase for trend
```

#### Commercial Lines Loss Ratios

**Workers Compensation**:
- Target: 55%-65%
- Excellent: <50%
- Acceptable: 50%-75%
- Poor: 75%-100%
- Unacceptable: >100%

**Commercial Auto**:
- Target: 60%-70%
- Excellent: <55%
- Acceptable: 55%-80%
- Poor: 80%-95%
- Unacceptable: >95%

**Experience Modification Impact**:
```
Loss Ratio → Experience Mod

30%: 0.70 (30% credit)
50%: 0.85 (15% credit)
70%: 1.00 (no mod)
90%: 1.15 (15% debit)
110%: 1.30 (30% debit)
130%+: 1.50+ (50%+ debit)
```

### 6. Open Claims Evaluation

#### Reserve Adequacy

**Reserve Analysis**:
- Compare reserves to similar closed claims
- Evaluate adjuster's reserve history
- Consider legal involvement
- Account for medical specials

**Reserve Ranges by Claim Type**:

**Property Damage**:
- Minor: $500-$5,000
- Moderate: $5,000-$25,000
- Significant: $25,000-$100,000
- Major: $100,000+

**Bodily Injury**:
- Minor (soft tissue): $2,500-$15,000
- Moderate (fractures): $15,000-$50,000
- Serious (surgery): $50,000-$250,000
- Severe (permanent): $250,000+

**Open Claim Concerns**:
- Long-tail claims (open >2 years): Potential for escalation
- Attorney representation: 3x settlement typical
- Medical treatment ongoing: Indeterminate severity
- Litigation filed: Significant increase expected
- Multiple claimants: Multiplicative effect

#### IBNR (Incurred But Not Reported)

**Considerations**:
- Recent policy period: Allow for reporting lag
- Long-tail exposures: Professional liability, WC
- Typical reporting patterns by line
- Historical IBNR development

**Estimation**:
- Review historical development patterns
- Apply industry standard factors
- Consider recent exposure changes
- Add IBNR to total incurred for complete picture

### 7. Fraud Indicators

#### Suspicious Claim Patterns

**Red Flags - High Priority**:
- Claim shortly after policy inception (<30 days)
- Claim reported late (>90 days after occurrence)
- No police report for theft/vandalism
- Insured has financial difficulties
- Recent coverage increase before large claim
- Conflicting statements
- Missing documentation
- Uncooperative with investigation

**Red Flags - Medium Priority**:
- Multiple claims different properties
- Insured frequently changes insurers
- Claims exceed statistical norms
- Witnesses unavailable or uncooperative
- Medical treatment excessive for injury
- Prior fraud indicators in database

**Red Flags - Pattern Analysis**:
- Claims with same contractor repeatedly
- Similar claims at different properties
- Claims timing near financial events
- Beneficiary relationships questionable

#### Investigation Triggers

**Require Special Investigation Unit (SIU) Referral**:
- Suspected arson/incendiary fire
- Questionable theft claim (no forced entry)
- Staged auto accident indicators
- Inflated damage claims
- Medical treatment inconsistent with injury
- Prior fraud convictions
- Multiple policies on same risk

**Investigation Outcomes Impact**:
- Claim denial: Underwriting must non-renew
- Claim paid with reservation: Close monitoring
- Suspicious but inconclusive: Document for future
- Exonerated: Note in file, continue coverage

### 8. Comparative Analysis

#### Industry Benchmarking

**ISO Loss Cost Data**:
- Compare to territory/class averages
- Identify deviations from expected
- Benchmark frequency and severity
- Evaluate relative to exposure base

**Peer Comparison**:
- Similar business types
- Similar geographic areas
- Similar coverage limits
- Similar deductible levels

**Internal Book Comparison**:
- Compare to company averages
- Identify outliers
- Risk selection validation
- Pricing adequacy verification

### 9. Underwriting Decision Impact

#### Claims-Based Actions

**0 Claims in 5 Years**:
- Action: Preferred pricing
- Discount: Maximum allowed (-20% to -25%)
- Renewal: Aggressively retain
- Risk score: Improve by 15-20 points

**1 Claim in 5 Years**:
- Action: Standard pricing
- Discount: Claims-free removed
- Renewal: Standard retention efforts
- Risk score: Minimal impact (0-5 points)

**2 Claims in 5 Years**:
- Action: Surcharge applied
- Surcharge: +15% to +25%
- Renewal: Conditional on no further claims
- Risk score: Increase by 10-15 points

**3 Claims in 5 Years**:
- Action: Significant surcharge or non-renew
- Surcharge: +40% to +60% if renewed
- Renewal: Non-renew unless exceptional circumstances
- Risk score: Increase by 25-30 points

**4+ Claims in 5 Years**:
- Action: Non-renew or decline
- Surcharge: Not applicable (typically decline)
- Renewal: Non-renew mandatory
- Risk score: Unacceptable (80+ points)

#### Claim Type Impact Matrix

| Claim Type | Single Claim | Two Claims | Three+ Claims |
|------------|-------------|------------|---------------|
| Weather (CAT) | No impact | Minimal | Review |
| Water damage | +10% | +25% | Decline |
| Theft | +5% | +15% | Decline |
| Fire | +15% | Decline | Decline |
| Liability | +20% | +35% | Decline |
| Auto at-fault | +20% | +40% | Decline |

### 10. Claims Analysis Report Structure

#### Standard Report Format

```
CLAIMS ANALYSIS REPORT

Applicant: [Name]
Policy Type: [Type]
Review Period: [Dates]
Prior Carrier(s): [List]

Claims Summary:
Total Claims: [Number]
Total Incurred: $[Amount]
Total Premium Paid: $[Amount]
Loss Ratio: [Percentage]

Claims Detail:

Claim 1:
Date of Loss: [Date]
Type: [Type]
Cause: [Cause]
Paid: $[Amount]
Reserved: $[Amount]
Status: [Open/Closed]
Assessment: [Brief analysis]

[Repeat for each claim]

Frequency Analysis:
Claims per year: [Number]
Benchmark comparison: [Above/At/Below average]

Severity Analysis:
Average claim: $[Amount]
Benchmark comparison: [Above/At/Below average]

Pattern Recognition:
[Any concerning patterns identified]

Red Flags:
[List any suspicious indicators]

Open Claims Impact:
[Analysis of open claim reserves]

Industry Comparison:
Loss ratio vs. industry: [Percentage above/below]
Frequency vs. industry: [Percentage above/below]

Underwriting Impact:
Recommended Action: [Approve/Decline/Surcharge/Refer]
Pricing Impact: [Percentage adjustment]
Risk Score Adjustment: [Points]
Renewal Recommendation: [Renew/Non-renew/Conditional]

Rationale:
[Clear explanation of recommendation based on analysis]

Supporting Documentation:
- Loss runs attached: [Yes/No]
- Claim detail reviewed: [Yes/No]
- Industry benchmarks consulted: [Yes/No]
- Fraud indicators checked: [Yes/No]

Prepared by: [Name]
Date: [Date]
```

## Best Practices Checklist

Before completing claims analysis:

- [ ] Complete loss runs obtained (5+ years)
- [ ] All claims reviewed individually
- [ ] Frequency calculated and benchmarked
- [ ] Severity calculated and analyzed
- [ ] Loss ratio computed
- [ ] Patterns identified
- [ ] Fraud indicators checked
- [ ] Open claims reserves evaluated
- [ ] Industry comparison completed
- [ ] Underwriting impact determined
- [ ] Pricing recommendation documented
- [ ] Renewal action specified
- [ ] Report formatted professionally
- [ ] Supporting documentation attached

## Special Considerations

### Long-Tail Claims
- Professional liability may take years to develop
- Workers comp claims can reopen
- Reserve increases common
- IBNR critical for accurate picture

### Catastrophic Events
- Don't penalize for acts of God
- Distinguish CAT vs. normal weather
- Consider if whole area affected
- May not impact renewal pricing

### Subrogation Recoveries
- Reduce incurred by recovery amount
- Improves loss ratio
- Consider when analyzing experience
- May offset claim surcharge

### Self-Insured Retentions
- Only evaluate excess losses
- Consider total exposure in analysis
- Retention level affects frequency
- Compare retained vs. insured losses

This skill should be read and applied for all insurance claims analysis tasks.
