# Insurance Policy Pricing Skill

Expert guidance for calculating accurate insurance premiums across all policy types using industry-standard rating methodologies.

## Overview

This skill provides comprehensive premium calculation techniques, rating factor application, and pricing strategies based on actuarial principles and competitive market positioning.

## Core Pricing Components

### 1. Base Rate Determination

#### Rate Manual Structure
**Components of Base Rate**:
- Pure premium (expected losses)
- Loss adjustment expenses (LAE)
- Underwriting expenses
- Profit and contingencies
- State premium taxes

**Formula**:
```
Base Rate = (Pure Premium + LAE) / (1 - Expense Ratio - Profit Margin - Tax Rate)
```

**Example Calculation**:
```
Pure Premium: $400
LAE (12%): $48
Expenses (25%): To be divided out
Profit (5%): To be divided out
Taxes (2%): To be divided out

Base Rate = ($400 + $48) / (1 - 0.25 - 0.05 - 0.02)
Base Rate = $448 / 0.68
Base Rate = $659
```

### 2. Rating Factors Application

#### Personal Lines - Homeowners

**Base Premium Calculation**:
```
Base Premium = (Dwelling Amount / $1000) × Base Rate × Territory Factor
```

**Territory Factors** (varies by location):
- Urban core (high claims): 1.20-1.50
- Suburban: 0.95-1.05
- Rural (low claims): 0.80-0.95
- Coastal (hurricane): 1.50-3.00
- Earthquake zone: 1.25-2.00

**Construction Type Factors**:
- Frame: 1.00 (base)
- Brick veneer: 0.90
- Masonry: 0.85
- Fire-resistive: 0.70
- Superior construction: 0.65

**Protection Class Factors**:
- Class 1: 0.50
- Class 2-3: 0.65-0.75
- Class 4-5: 0.85-0.95
- Class 6-7: 1.00-1.10
- Class 8-9: 1.20-1.40
- Class 10: 1.60+

**Age of Home Factors**:
- 0-4 years: 0.85 (new home discount)
- 5-14 years: 0.95
- 15-24 years: 1.00 (base)
- 25-39 years: 1.10
- 40-59 years: 1.25
- 60+ years: 1.40-1.60

**Deductible Credits**:
- $500: 1.00 (base)
- $1,000: 0.92
- $2,500: 0.82
- $5,000: 0.72
- $10,000: 0.62

**Example Homeowners Calculation**:
```
Dwelling: $400,000
Territory: Suburban (1.00)
Construction: Brick veneer (0.90)
Protection Class: 4 (0.90)
Age: 10 years (0.95)
Deductible: $2,500 (0.82)
Base Rate: $1.20 per $1000

Calculation:
Base Premium = ($400,000 / $1,000) × $1.20 = $480
Territory Factor: $480 × 1.00 = $480
Construction: $480 × 0.90 = $432
Protection: $432 × 0.90 = $389
Age: $389 × 0.95 = $370
Deductible: $370 × 0.82 = $303

Additional Coverages:
Contents (Coverage C): $300,000 × $0.40 = $120
Liability (Coverage E): $500,000 = $50
Medical Payments: $5,000 = $10

Subtotal: $303 + $120 + $50 + $10 = $483

Protective Devices:
Central station alarm: -15% = $483 × 0.85 = $410
Sprinkler system: -20% = $410 × 0.80 = $328

Total Annual Premium: $328
Monthly Premium: $328 / 12 = $27.33
```

#### Personal Lines - Auto

**Base Premium Calculation**:
```
Total Premium = (Liability + Comprehensive + Collision + PIP + UM/UIM) × Rating Factors
```

**Coverage Components**:

**Liability Premium**:
- Bodily Injury: Based on limits selected
- Property Damage: Based on limits selected
- Base rates vary by territory and vehicle class

**Limits Factors** (relative to 50/100/50):
- 25/50/25: 0.80
- 50/100/50: 1.00 (base)
- 100/300/100: 1.25
- 250/500/250: 1.50
- 500/500/500: 1.80

**Comprehensive Premium**:
```
Comp Premium = (Vehicle Value × Comp Rate × Territory Factor) / Deductible Credit
```

**Deductible Credits** (Comp/Coll):
- $100: 1.20
- $250: 1.10
- $500: 1.00 (base)
- $1,000: 0.85
- $2,500: 0.70

**Collision Premium**:
```
Coll Premium = (Vehicle Value × Coll Rate × Territory Factor) / Deductible Credit
```

**Driver Age Factors**:
- 16-17: 2.80
- 18-19: 2.40
- 20-24: 1.70
- 25-29: 1.25
- 30-49: 1.00 (base)
- 50-64: 0.95
- 65-74: 1.05
- 75+: 1.25

**Driving Record Factors**:
- Clean 3+ years: 0.80
- One minor violation: 1.00
- Two minor violations: 1.25
- Major violation: 1.40
- At-fault accident: 1.35
- DUI/DWI: 2.00+
- Multiple accidents: 1.75

**Annual Mileage Factors**:
- 0-5,000: 0.80
- 5,001-7,500: 0.90
- 7,501-10,000: 0.95
- 10,001-15,000: 1.00 (base)
- 15,001-20,000: 1.10
- 20,001-25,000: 1.25
- 25,001+: 1.50

**Example Auto Calculation**:
```
Vehicle: 2020 Honda Accord
Value: $25,000
Driver: 35 years old, clean record
Territory: Urban
Miles: 12,000/year
Coverage: 100/300/100, $500 deductibles

Liability (100/300/100):
Base: $600
Territory (1.15): $600 × 1.15 = $690
Age (1.00): $690
Driving record (0.80): $690 × 0.80 = $552

Comprehensive:
Vehicle value rate: $25,000 × 0.015 = $375
Territory (1.10): $375 × 1.10 = $413
Deductible ($500 = 1.00): $413

Collision:
Vehicle value rate: $25,000 × 0.025 = $625
Territory (1.10): $625 × 1.10 = $688
Deductible ($500 = 1.00): $688
Age (1.00): $688
Driving record (1.00): $688

PIP (if required): $150
UM/UIM (100/300): $75

Subtotal: $552 + $413 + $688 + $150 + $75 = $1,878

Multi-car discount: -15% = $1,878 × 0.85 = $1,596
Paperless discount: -3% = $1,596 × 0.97 = $1,548

Total Annual Premium: $1,548
Monthly Premium: $1,548 / 12 = $129
```

### 3. Commercial Lines Pricing

#### Business Owners Policy (BOP)

**Base Premium Components**:
- Building premium (if owned)
- Business personal property premium
- Business liability premium
- Business income premium (optional)

**Building Premium**:
```
Building Premium = (Building Limit / $1000) × Building Rate × Modifiers
```

**Building Rates** (per $1000):
- Office building: $0.80-$1.20
- Retail store: $1.00-$1.50
- Restaurant: $1.50-$2.50
- Light manufacturing: $1.80-$3.00
- Warehouse: $1.20-$2.00

**Business Personal Property**:
```
BPP Premium = (BPP Limit / $1000) × BPP Rate × Modifiers
```

**BPP Rates** (per $1000):
- Office contents: $1.50-$2.50
- Retail inventory: $2.00-$3.50
- Restaurant equipment: $2.50-$4.00
- Manufacturing equipment: $3.00-$5.00

**Liability Premium**:
```
Liability Premium = Base Premium × Receipts Factor × Classification Factor
```

**Liability Limits Factors** (relative to $1M/$2M):
- $500K/$1M: 0.75
- $1M/$2M: 1.00 (base)
- $2M/$4M: 1.40
- $3M/$6M: 1.70

**Classification Factors**:
- Office (low hazard): 1.00
- Retail store: 1.15
- Restaurant (no alcohol): 1.40
- Restaurant (with alcohol): 1.80
- Contractor (light): 1.60
- Contractor (general): 2.20

**Example BOP Calculation**:
```
Business: Retail clothing store
Building: $500,000 (owned)
BPP: $200,000
Liability: $1M/$2M
Gross receipts: $750,000
Territory: Suburban

Building Premium:
$500,000 / $1,000 = 500 units
500 × $1.20 = $600
Sprinkler credit (-15%): $600 × 0.85 = $510

BPP Premium:
$200,000 / $1,000 = 200 units
200 × $2.50 = $500

Liability Premium:
Base: $800
Classification (retail 1.15): $800 × 1.15 = $920
Receipts factor (0.75M): $920 × 1.05 = $966

Subtotal: $510 + $500 + $966 = $1,976

Business income (optional): $300

Total Annual Premium: $2,276
Monthly Premium: $2,276 / 12 = $190
```

#### Workers Compensation

**Premium Calculation**:
```
Premium = (Payroll / $100) × Class Code Rate × Experience Modifier × Other Modifiers
```

**Class Code Examples** (rates per $100 payroll):
- Office clerical: $0.30-$0.60
- Outside sales: $0.80-$1.50
- Retail store: $1.00-$2.00
- Restaurant workers: $2.50-$4.00
- Carpentry: $8.00-$15.00
- Roofing: $25.00-$50.00
- Tree trimming: $30.00-$65.00

**Experience Modification**:
- Better than average: 0.70-0.99
- Average: 1.00
- Worse than average: 1.01-2.00+

**Example WC Calculation**:
```
Business: Construction company
Total payroll: $2,000,000

Breakdown by class:
Office staff: $400,000 @ $0.50 = $2,000
Carpenters: $1,200,000 @ $12.00 = $144,000
Laborers: $400,000 @ $8.00 = $32,000

Subtotal: $178,000
Experience Mod (1.15): $178,000 × 1.15 = $204,700
Schedule credit (safety program -5%): $204,700 × 0.95 = $194,465

Annual Premium: $194,465
Minimum deposit: $50,000 (typical 25%)
Monthly installments: $14,447
```

### 4. Discounts and Credits

#### Multi-Policy Discounts
- Home + Auto: -15% to -25%
- Multiple vehicles: -10% to -20%
- Multiple properties: -5% to -15%

#### Claims-Free Discounts
- 3 years: -10%
- 5 years: -15%
- 7 years: -20%
- 10+ years: -25%

#### Safety and Prevention Credits
- Alarm system (central station): -15% to -20%
- Sprinkler system: -15% to -40%
- Fire extinguishers: -5%
- Deadbolt locks: -3% to -5%
- Gated community: -5% to -10%

#### Payment and Account Credits
- Paid in full: -5% to -8%
- Automatic payment: -3% to -5%
- Paperless billing: -2% to -3%
- Online account: -2%

#### Age/Tenure Credits
- Age 55+: -5% to -10%
- Retired: -5% to -10%
- Customer tenure 3+ years: -5%
- Customer tenure 5+ years: -10%

#### Professional/Affinity Credits
- Professional association member: -5% to -10%
- Alumni association: -3% to -8%
- Good student (auto): -10% to -20%
- Military/veteran: -5% to -15%

### 5. Surcharges and Increased Rates

#### Claims Surcharges
- One claim: +10% to +20%
- Two claims: +25% to +40%
- Three+ claims: +50% to +80%
- Large loss ($50K+): +30% to +60%

**Claim Type Impact**:
- Weather (not-at-fault): +5% to +10%
- Theft: +10% to +15%
- Fire: +15% to +25%
- Water damage: +10% to +20%
- Liability claim: +20% to +35%

#### Violation Surcharges (Auto)
- Speeding (minor): +10% to +15%
- Speeding (major 20+ mph): +20% to +30%
- Reckless driving: +30% to +50%
- DUI/DWI: +50% to +150%
- At-fault accident: +20% to +40%
- Driving without insurance: +40% to +60%

#### Property Condition Surcharges
- Roof age 15-20 years: +10%
- Roof age 20-25 years: +20%
- Roof age 25+ years: May decline
- Knob and tube wiring: +25% to +50%
- Aluminum wiring: +15% to +30%
- Oil heat tank (underground): +20% or decline

#### Occupancy/Use Surcharges
- Secondary home: +10% to +20%
- Seasonal occupancy: +15% to +25%
- Home business: +10% to +50%
- Short-term rental: +50% to +100% or commercial policy
- High-value contents: Schedule separately

## Premium Calculation Workflow

### Step-by-Step Process

**Step 1: Gather Information**
- Complete application data
- Verify all coverage selections
- Obtain loss history
- Pull credit/insurance score
- Inspect property (if required)

**Step 2: Determine Base Rate**
- Identify rate manual version
- Select appropriate class/territory
- Verify effective date of rates
- Check for rate changes pending

**Step 3: Calculate Base Premium**
- Apply coverage amounts to base rates
- Calculate each coverage component
- Sum all base premiums

**Step 4: Apply Rating Factors**
- Construction type
- Protection class
- Territory
- Age factors
- Deductibles
- Coverage limits

**Step 5: Apply Credits**
- Protective devices
- Multi-policy discounts
- Claims-free credits
- Payment method discounts
- Affinity/professional credits

**Step 6: Apply Surcharges**
- Claims history surcharges
- Violations (auto)
- Property condition
- Occupancy factors
- Credit-based insurance score

**Step 7: Add Fees and Taxes**
- Policy fee: $25-$100
- Inspection fee (if applicable): $50-$150
- State premium tax: 1%-4% (varies by state)
- Municipal taxes (if applicable)
- Surplus lines tax (if applicable): 3%-6%

**Step 8: Calculate Payment Plans**
- Annual premium (total)
- Semi-annual: Total / 2 + small fee
- Quarterly: Total / 4 + fee
- Monthly: Total / 12 (or 10-pay) + 3%-5% installment fee

**Step 9: Competitive Analysis**
- Compare to market rates
- Verify competitiveness
- Adjust if needed (within guidelines)
- Document pricing rationale

**Step 10: Quality Check**
- Verify all calculations
- Check for reasonableness
- Ensure compliance with guidelines
- Document worksheet

## Special Rating Situations

### Agreed Value vs. Actual Cash Value

**Replacement Cost** (standard):
- Pays to rebuild/replace with like materials
- No depreciation applied to dwelling
- Contents may be ACV or RC

**Actual Cash Value**:
- Replacement cost minus depreciation
- Lower premium (-20% to -30%)
- Risk of underinsurance
- Typically for older homes

**Agreed Value** (high-value homes):
- Value agreed upon at inception
- No depreciation at claim time
- Requires appraisal
- Higher premium (+10% to +15%)

### Replacement Cost Estimators

**Square Foot Method**:
```
Dwelling Replacement Cost = Square Feet × Cost per Square Foot × Local Modifier
```

**Cost per Square Foot** (varies by quality):
- Economy: $100-$150/sqft
- Standard: $150-$200/sqft
- Custom: $200-$300/sqft
- Luxury: $300-$500/sqft
- Ultra-luxury: $500+/sqft

**Local Cost Modifiers**:
- National average: 1.00
- High-cost areas (SF, NYC): 1.50-2.00
- Low-cost areas (rural): 0.80-0.90

### Coinsurance and Rate Adjustments

**80% Coinsurance Requirement**:
- Insure to at least 80% of replacement cost
- Failure results in coinsurance penalty at claim

**Coinsurance Penalty Formula**:
```
Payment = (Amount of Insurance Carried / Amount Should Carry) × Loss - Deductible
```

**Example**:
```
Replacement cost: $500,000
Should carry (80%): $400,000
Actually carrying: $300,000
Loss amount: $100,000
Deductible: $2,500

Payment = ($300,000 / $400,000) × $100,000 - $2,500
Payment = 0.75 × $100,000 - $2,500
Payment = $75,000 - $2,500 = $72,500

Penalty: $100,000 - $72,500 = $27,500 not covered
```

### Scheduled Personal Property

**High-value items requiring scheduling**:
- Jewelry: Over $2,500 per item
- Fine art: Over $2,500 per item
- Firearms: Collections over $5,000
- Cameras: Professional equipment
- Musical instruments: Over $2,500
- Furs: Over $2,500

**Scheduled Item Rates** (per $100 of value):
- Jewelry: $1.50-$2.50
- Fine art: $0.50-$1.50
- Cameras: $2.00-$4.00
- Musical instruments: $1.00-$2.00
- Firearms: $0.50-$1.50

## Premium Audit Process

### Commercial Policies Subject to Audit
- Workers compensation (payroll-based)
- General liability (receipts-based)
- Commercial auto (vehicle count)
- Equipment floater (valued items)

### Audit Premium Adjustment
```
Final Premium = (Actual Exposure / Estimated Exposure) × Deposit Premium
```

**Return Premium** (if over-estimated):
- Credit to insured
- Typically within 30 days

**Additional Premium** (if under-estimated):
- Bill to insured
- May offer payment plan
- Due within 30 days typically

## Competitive Positioning

### Market Rate Comparison

**Competitiveness Targets**:
- Preferred risks: Within 5% of market low
- Standard risks: Within 10% of market average
- Substandard: May be 20%+ above market

**When to Negotiate**:
- Large accounts (premium >$25K)
- Package business (multiple policies)
- Clean risks (preferred classification)
- Long-term customer retention

**Pricing Flexibility**:
- Schedule rating credits: Up to -25%
- Deductible optimization
- Coverage adjustments
- Payment plan modifications

## Documentation Requirements

### Rating Worksheet Must Include

- [ ] Applicant information
- [ ] Coverage selections and limits
- [ ] Base rates applied (with manual reference)
- [ ] All rating factors with values
- [ ] All credits applied with percentages
- [ ] All surcharges applied with percentages
- [ ] Subtotal before fees
- [ ] Policy fees and taxes
- [ ] Total annual premium
- [ ] Payment plan options
- [ ] Competitive comparison (if available)
- [ ] Underwriter approval (if required)
- [ ] Date prepared and preparer initials

### Pricing Checklist

Before finalizing premium:

- [ ] All information verified
- [ ] Correct rate manual version used
- [ ] All rating factors applied correctly
- [ ] Credits and surcharges documented
- [ ] Calculations verified (double-check)
- [ ] Competitive position reviewed
- [ ] Underwriting guidelines followed
- [ ] Special authority obtained (if needed)
- [ ] Regulatory compliance verified
- [ ] Premium reasonableness confirmed

## Output Format

All pricing calculations should follow this structure:

```
PREMIUM CALCULATION WORKSHEET

Policy Information:
- Insured: [Name]
- Policy Type: [Type]
- Effective Date: [Date]
- Coverage Period: [Period]

Coverage Summary:
[Coverage A: $XXX,XXX]
[Coverage B: $XXX,XXX]
[etc.]

Base Premium Calculation:
[Coverage] × [Rate] = $XXX
[Detail each component]

Rating Factors Applied:
[Factor name]: [Value] → Premium: $XXX
[Continue for each factor]

Credits Applied:
[Credit description]: -XX% → Premium: $XXX
[Continue for each credit]

Surcharges Applied:
[Surcharge description]: +XX% → Premium: $XXX
[Continue for each surcharge]

Subtotal: $X,XXX
Policy Fee: $XX
State Tax (X%): $XX
TOTAL ANNUAL PREMIUM: $X,XXX

Payment Plans:
- Annual (pay in full): $X,XXX (-5% discount)
- Semi-annual: $XXX × 2 payments
- Quarterly: $XXX × 4 payments
- Monthly: $XXX × 12 payments (+3% installment fee)

Competitive Analysis:
[Market comparison if available]

Notes:
[Any special considerations]

Prepared by: [Name]
Date: [Date]
```

This skill should be read and applied for all insurance pricing calculations.
