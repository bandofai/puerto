# Real Estate Analysis Skill

**Version**: 1.0.0
**Last Updated**: 2025-10-30
**Purpose**: Comprehensive real estate valuation, investment analysis, and market research methodologies

## Overview

This skill provides systematic approaches to real estate analysis, covering property valuation, investment metrics, market research, due diligence, and financing considerations. Use these frameworks to evaluate residential, commercial, and investment properties with professional-grade analysis.

## Table of Contents

1. [Property Valuation](#1-property-valuation)
2. [Investment Analysis](#2-investment-analysis)
3. [Market Research](#3-market-research)
4. [Due Diligence](#4-due-diligence)
5. [Financing & Tax](#5-financing--tax)

---

## 1. Property Valuation

Property valuation determines the fair market value of real estate using three primary approaches. Each method has specific applications and limitations.

### 1.1 Comparable Sales Approach (Sales Comparison)

The most common method for residential properties, comparing the subject property to recent sales of similar properties.

#### Core Methodology

**Step 1: Identify Comparable Properties**

Criteria for good comparables:
- Same neighborhood or similar location (within 1 mile ideal)
- Similar property type (single-family, condo, multi-family)
- Similar size (within 20% of subject property square footage)
- Similar age (within 10 years)
- Similar condition
- Sold within last 6 months (3 months ideal)
- Arm's length transactions (no family/distress sales)

**Step 2: Adjustment Grid**

Create an adjustment grid comparing each comparable to the subject property:

```
Feature Adjustment Grid Template:

Feature                 | Comp 1    | Comp 2    | Comp 3    | Adjustment Factor
------------------------|-----------|-----------|-----------|-------------------
Sale Price              | $350,000  | $365,000  | $340,000  | -
Square Feet             | 1,800     | 1,950     | 1,750     | $80-120/sq ft
Bedrooms                | 3         | 4         | 3         | $10,000-15,000/bedroom
Bathrooms               | 2         | 2.5       | 2         | $5,000-8,000/bath
Garage                  | 2-car     | 2-car     | 1-car     | $8,000-12,000/space
Lot Size                | 6,000 sf  | 7,500 sf  | 5,500 sf  | $2-5/sq ft
Age/Condition           | Similar   | Better    | Similar   | 1-3% per year
Location                | Similar   | Inferior  | Superior  | 5-15%
Upgrades/Features       | Similar   | Better    | Similar   | Itemize
```

#### Standard Adjustment Factors

**Square Footage Adjustments:**
- Calculate cost per square foot from comparables
- Typical adjustment: $80-150 per sq ft (varies by market)
- Formula: `(Subject SF - Comp SF) × $/sq ft = Adjustment`

**Example:**
```
Subject Property: 2,000 sq ft
Comparable: 1,800 sq ft, sold for $350,000

Market $/sq ft = $350,000 ÷ 1,800 = $194/sq ft
Adjustment = (2,000 - 1,800) × $194 = +$38,800
Adjusted Comp Value = $350,000 + $38,800 = $388,800
```

**Bedroom/Bathroom Adjustments:**
- Additional bedroom: +$10,000 to +$20,000 (market dependent)
- Additional full bath: +$8,000 to +$15,000
- Half bath: +$4,000 to +$7,000

**Age and Condition Adjustments:**
- Depreciation: 1-3% per year difference
- Major updates can add back value:
  - New roof: +$8,000 to +$15,000
  - New HVAC: +$5,000 to +$12,000
  - Kitchen remodel: +$15,000 to +$40,000
  - Bathroom remodel: +$8,000 to +$20,000

**Location Adjustments:**
- Same subdivision: 0-2% adjustment
- Adjacent subdivision: 2-10% adjustment
- Different school district: 5-15% adjustment
- Busy street vs quiet street: 3-8% adjustment
- View premium: 5-20% adjustment

#### Complete Comparable Analysis Example

**Subject Property:**
- 2,000 sq ft, 4 bed, 2.5 bath
- 2-car garage, 7,000 sq ft lot
- 10 years old, good condition
- Quiet street, desirable subdivision

**Comparable 1:**
- Sale Price: $375,000
- 1,900 sq ft, 3 bed, 2 bath
- 2-car garage, 6,500 sq ft lot
- 8 years old, excellent condition
- Similar location

**Adjustments:**
```
Base Price:                                    $375,000
Square Feet: (2,000-1,900) × $100             +$10,000
Bedrooms: Subject has 1 more                   +$15,000
Bathrooms: Subject has 0.5 more                +$6,000
Lot Size: (7,000-6,500) × $3                   +$1,500
Condition: Comp is better                      -$8,000
                                               ---------
Adjusted Value:                                $399,500
```

**Final Valuation:**

After analyzing 3-5 comparables:
```
Comp 1 Adjusted Value:  $399,500
Comp 2 Adjusted Value:  $405,000
Comp 3 Adjusted Value:  $392,000
Comp 4 Adjusted Value:  $398,000
                        ---------
Average:                $398,625
Median:                 $398,750

Recommended Value Range: $395,000 - $405,000
Most Probable Value:     $400,000
```

### 1.2 Income Approach

Used primarily for investment and commercial properties. Value is based on the income the property generates.

#### Net Operating Income (NOI)

**NOI Formula:**
```
Gross Rental Income
- Vacancy & Collection Loss
= Effective Gross Income
- Operating Expenses
= Net Operating Income (NOI)
```

#### Detailed NOI Calculation

**Step 1: Gross Rental Income**
```
Monthly rent per unit × Number of units × 12 months = Annual Gross Income

Example:
4-unit property, $1,200/month per unit
$1,200 × 4 × 12 = $57,600 annual gross income
```

**Step 2: Vacancy & Collection Loss**
```
Typical vacancy rates:
- Class A properties: 3-5%
- Class B properties: 5-8%
- Class C properties: 8-12%

Example with 7% vacancy:
$57,600 × 0.93 = $53,568 Effective Gross Income
```

**Step 3: Operating Expenses**

Typical operating expense categories:
```
Property taxes:           15-25% of EGI
Insurance:               3-8% of EGI
Property management:     8-10% of EGI
Repairs & maintenance:   8-15% of EGI
Utilities (owner-paid):  5-10% of EGI
Landscaping/snow:        2-5% of EGI
HOA fees:                Variable
Legal/accounting:        1-2% of EGI
Advertising/vacancy:     2-4% of EGI
Reserve for replacements: 5-10% of EGI
```

**Example Operating Expense Calculation:**
```
Effective Gross Income:           $53,568

Operating Expenses:
Property taxes:        $6,500  (12.1%)
Insurance:            $2,400  (4.5%)
Property management:  $5,400  (10%)
Repairs & maint:      $5,000  (9.3%)
Utilities:            $3,600  (6.7%)
Landscaping:          $1,200  (2.2%)
Legal/accounting:     $800    (1.5%)
Marketing:            $600    (1.1%)
Reserves:             $3,000  (5.6%)
                      -------
Total Operating Exp:  $28,500 (53.2% of EGI)

Net Operating Income: $25,068
```

#### Capitalization Rate (Cap Rate)

**Cap Rate Formula:**
```
Cap Rate = Net Operating Income (NOI) ÷ Property Value

Solving for Value:
Property Value = NOI ÷ Cap Rate
```

**Cap Rate Applications:**

1. **Valuing a Property:**
```
Given:
- NOI: $25,068
- Market cap rate: 7.5%

Value = $25,068 ÷ 0.075 = $334,240
```

2. **Determining Market Cap Rate:**
```
Recent comparable sale:
- Sale price: $340,000
- NOI: $26,000

Cap Rate = $26,000 ÷ $340,000 = 7.65%
```

**Typical Cap Rate Ranges by Property Type:**
```
Property Type              | Cap Rate Range
---------------------------|----------------
Class A Multi-family       | 4.0% - 6.0%
Class B Multi-family       | 6.0% - 8.0%
Class C Multi-family       | 8.0% - 10.0%
Retail (anchored)          | 6.0% - 8.0%
Office (Class A)           | 5.0% - 7.0%
Industrial/Warehouse       | 6.0% - 8.5%
Single-family rentals      | 7.0% - 10.0%
```

**Cap Rate Factors:**
- Lower cap rates = lower risk, lower returns (Class A properties)
- Higher cap rates = higher risk, higher returns (Class C properties)
- Location quality inversely affects cap rate
- Property condition inversely affects cap rate
- Market growth expectations affect cap rates

#### Gross Rent Multiplier (GRM)

Simplified income valuation method:

**GRM Formula:**
```
GRM = Sale Price ÷ Gross Annual Rent
Property Value = Gross Annual Rent × GRM
```

**Example:**
```
Comparable property sold for $400,000
Annual gross rent: $48,000
GRM = $400,000 ÷ $48,000 = 8.33

Subject property gross rent: $52,000
Estimated value = $52,000 × 8.33 = $433,160
```

**Typical GRM Ranges:**
- Single-family rentals: 8-15
- Small multi-family (2-4 units): 8-12
- Larger multi-family (5+ units): 6-10
- Commercial properties: Varies widely, use cap rate instead

**GRM Limitations:**
- Ignores expenses (useful for quick screening only)
- Varies significantly by market
- Less accurate than cap rate method
- Best for preliminary analysis

### 1.3 Cost Approach

Value = Land Value + (Replacement Cost - Depreciation)

#### Step 1: Land Value

Determine land value using:
- Recent land sales in area
- Assessed land value (tax records)
- Allocation method (% of total value)
- Extraction method (sale price - building value)

**Example:**
```
Recent vacant lot sales in neighborhood:
Lot 1: 7,000 sq ft, $70,000 ($10/sq ft)
Lot 2: 6,500 sq ft, $68,000 ($10.46/sq ft)
Lot 3: 7,500 sq ft, $72,000 ($9.60/sq ft)

Average: $10/sq ft
Subject lot: 7,000 sq ft
Land Value = 7,000 × $10 = $70,000
```

#### Step 2: Replacement Cost

**Replacement Cost per Square Foot:**

Typical construction costs by property type:
```
Property Type              | Cost per SF
---------------------------|-------------
Economy home              | $100 - $150
Standard home             | $150 - $200
Custom home               | $200 - $300+
Luxury home               | $300 - $500+
Basic apartment           | $120 - $180
Multi-family (wood frame) | $140 - $200
Commercial office         | $150 - $250
Retail                    | $100 - $180
Industrial/warehouse      | $60 - $120
```

**Additional Cost Factors:**
```
Site improvements:
- Driveway/parking:     $3-8 per sq ft
- Landscaping:          $5,000-25,000
- Fencing:              $15-40 per linear foot
- Deck/patio:           $15-35 per sq ft
- Pool:                 $30,000-80,000

Detached structures:
- Garage (attached):    $15,000-30,000
- Garage (detached):    $20,000-40,000
- Shed:                 $3,000-10,000
```

**Example Replacement Cost:**
```
Main house: 2,000 sq ft × $175/sq ft  = $350,000
Garage: 400 sq ft × $60/sq ft         = $24,000
Driveway: 600 sq ft × $5/sq ft        = $3,000
Landscaping                            = $12,000
Deck: 200 sq ft × $25/sq ft           = $5,000
Fence: 200 lf × $25/lf                = $5,000
                                        --------
Total Replacement Cost New             = $399,000
```

#### Step 3: Depreciation

Three types of depreciation:

**Physical Depreciation (Curable and Incurable):**
```
Age-Life Method:
Depreciation = (Effective Age ÷ Total Economic Life) × Replacement Cost

Typical Economic Life:
- Wood frame residential: 50-60 years
- Brick/masonry residential: 75-100 years
- Commercial buildings: 40-60 years
- Steel frame buildings: 60-80 years

Example:
Replacement cost: $399,000
Effective age: 15 years (property is 20 years old but remodeled)
Economic life: 60 years

Physical depreciation = (15 ÷ 60) × $399,000 = $99,750
```

**Functional Obsolescence:**
Outdated design or functionality:
- Poor floor plan: -$5,000 to -$20,000
- Small/inadequate kitchen: -$15,000 to -$30,000
- Insufficient bathrooms: -$10,000 to -$25,000
- Low ceilings (< 8 ft): -$5,000 to -$15,000
- No central AC: -$8,000 to -$15,000
- Single-pane windows: -$5,000 to -$12,000

**External Obsolescence:**
Outside factors affecting value:
- Adjacent to commercial/industrial: -5% to -15%
- Busy street/highway: -5% to -10%
- Power lines overhead: -3% to -8%
- Environmental issues: -10% to -50%+
- Economic decline in area: Variable

**Complete Cost Approach Example:**
```
Land Value:                              $70,000
Replacement Cost New:                    $399,000
Less: Physical Depreciation:             -$99,750
Less: Functional Obsolescence:           -$15,000 (outdated kitchen)
Less: External Obsolescence:             -$8,000 (busy street)
                                         ---------
Depreciated Building Value:              $276,250

Total Property Value:                    $346,250
```

### 1.4 Reconciliation of Values

After calculating values using multiple approaches, reconcile to final value:

**Example Reconciliation:**
```
Valuation Approach Results:
Sales Comparison Approach:    $400,000  (Weight: 50%)
Income Approach:              $385,000  (Weight: 30%)
Cost Approach:               $395,000  (Weight: 20%)

Weighted Average:
($400,000 × 0.50) + ($385,000 × 0.30) + ($395,000 × 0.20)
= $200,000 + $115,500 + $79,000
= $394,500

Recommended Value: $395,000 (rounded)
Value Range: $385,000 - $405,000
```

**Approach Weight Considerations:**

For Residential Properties:
- Sales Comparison: 60-80%
- Income: 0-20% (if applicable)
- Cost: 20-40%

For Investment Properties:
- Income: 60-80%
- Sales Comparison: 20-30%
- Cost: 10-20%

For New Construction:
- Cost: 50-70%
- Sales Comparison: 30-50%
- Income: 0-20%

### 1.5 Key Valuation Metrics Summary

**Price per Square Foot:**
```
$/sq ft = Sale Price ÷ Total Square Feet
Used for quick comparisons and screening
```

**Price per Unit (Multi-family):**
```
$/unit = Sale Price ÷ Number of Units
Common metric for apartment buildings
```

**Price per Bedroom:**
```
$/bedroom = Sale Price ÷ Total Bedrooms
Alternative comparison metric
```

**Land to Value Ratio:**
```
Land Ratio = Land Value ÷ Total Property Value
Typical: 20-30% for residential
Higher ratios indicate development potential
```

**Valuation Accuracy Checklist:**
- [ ] Used 3+ comparable sales
- [ ] Comparables within 6 months
- [ ] All adjustments documented and justified
- [ ] Multiple approaches used (when applicable)
- [ ] Market conditions considered
- [ ] Property-specific factors included
- [ ] Final value reconciliation completed
- [ ] Value range provided (not just point estimate)

---

## 2. Investment Analysis

Comprehensive analysis of investment property potential using standard real estate metrics and frameworks.

### 2.1 Cash Flow Analysis

Cash flow is the foundation of investment property analysis.

#### Complete Cash Flow Template

**Annual Cash Flow Statement:**
```
═══════════════════════════════════════════════════════════════
                    ANNUAL CASH FLOW ANALYSIS
═══════════════════════════════════════════════════════════════

INCOME
─────────────────────────────────────────────────────────────
Gross Rental Income (Monthly rent × 12)          $XX,XXX
Other Income (laundry, parking, etc.)            $X,XXX
                                                  ─────────
Total Gross Income                                $XX,XXX

VACANCY & CREDIT LOSS
─────────────────────────────────────────────────────────────
Vacancy Loss (X% of gross income)                ($X,XXX)
                                                  ─────────
Effective Gross Income                            $XX,XXX

OPERATING EXPENSES
─────────────────────────────────────────────────────────────
Property Taxes                                    $X,XXX
Insurance                                         $X,XXX
Property Management (8-10%)                       $X,XXX
Repairs & Maintenance                             $X,XXX
Utilities (owner-paid)                            $X,XXX
HOA Fees                                          $X,XXX
Landscaping/Snow Removal                          $XXX
Pest Control                                      $XXX
Legal & Professional Fees                         $XXX
Advertising & Marketing                           $XXX
Supplies                                          $XXX
Reserve for Replacements (CapEx)                  $X,XXX
Miscellaneous                                     $XXX
                                                  ─────────
Total Operating Expenses                          ($XX,XXX)
                                                  ─────────
Net Operating Income (NOI)                        $XX,XXX

DEBT SERVICE
─────────────────────────────────────────────────────────────
Mortgage Payment (Principal & Interest)           ($XX,XXX)
                                                  ─────────
Cash Flow Before Taxes                            $X,XXX

INCOME TAXES
─────────────────────────────────────────────────────────────
Income Tax (estimated)                            ($X,XXX)
                                                  ─────────
Cash Flow After Taxes                             $X,XXX

═══════════════════════════════════════════════════════════════
```

#### Detailed Cash Flow Example

**Property Details:**
- Purchase price: $400,000
- Down payment: $80,000 (20%)
- Loan amount: $320,000
- Interest rate: 7%
- Loan term: 30 years
- Monthly rent: 4 units × $1,200 = $4,800

**Cash Flow Calculation:**
```
═══════════════════════════════════════════════════════════════
INCOME
─────────────────────────────────────────────────────────────
Gross Rental Income: $4,800/mo × 12              $57,600
Laundry income                                    $600
                                                  ─────────
Total Gross Income                                $58,200

VACANCY & CREDIT LOSS
─────────────────────────────────────────────────────────────
Vacancy Loss (7% of gross)                        ($4,074)
                                                  ─────────
Effective Gross Income                            $54,126

OPERATING EXPENSES
─────────────────────────────────────────────────────────────
Property Taxes ($400k × 1.5%)                     $6,000
Insurance ($400k × 0.6%)                          $2,400
Property Management (10% of rent collected)       $5,413
Repairs & Maintenance (10% of EGI)                $5,413
Utilities (water/sewer/trash)                     $3,600
HOA Fees                                          $0
Landscaping                                       $1,200
Pest Control                                      $400
Legal & Accounting                                $800
Advertising                                       $600
Supplies                                          $300
CapEx Reserve (8% of EGI)                         $4,330
                                                  ─────────
Total Operating Expenses                          ($30,456)
Operating Expense Ratio: 56.3% of EGI
                                                  ─────────
Net Operating Income (NOI)                        $23,670

DEBT SERVICE
─────────────────────────────────────────────────────────────
Loan: $320,000 @ 7% for 30 years
Monthly payment: $2,129.45
Annual debt service                               ($25,553)
                                                  ─────────
Cash Flow Before Taxes (CFBT)                     ($1,883)

Note: Negative cash flow in year 1 (not uncommon)
This improves as rents increase and debt service stays fixed.
═══════════════════════════════════════════════════════════════
```

### 2.2 Return on Investment (ROI) Metrics

#### Cash-on-Cash Return

**Formula:**
```
Cash-on-Cash Return = Annual Cash Flow Before Taxes ÷ Total Cash Invested

Where Total Cash Invested includes:
- Down payment
- Closing costs
- Immediate repairs/improvements
- Cash reserves
```

**Example:**
```
Cash Invested:
Down payment:              $80,000
Closing costs:             $8,000
Immediate repairs:         $5,000
                           --------
Total Cash Invested:       $93,000

Annual Cash Flow (CFBT):   $6,500

Cash-on-Cash = $6,500 ÷ $93,000 = 6.99%
```

**Target Cash-on-Cash Returns:**
- Conservative: 6-8%
- Moderate: 8-10%
- Aggressive: 10-12%+
- Reality: Varies by market and leverage

#### Capitalization Rate (Cap Rate)

**Formula:**
```
Cap Rate = Net Operating Income (NOI) ÷ Purchase Price
```

**Cap Rate vs Cash-on-Cash:**
- Cap rate ignores financing (all-cash perspective)
- Cash-on-cash includes debt service (leveraged return)
- Cap rate useful for comparing properties
- Cash-on-cash shows actual investor return

**Example:**
```
Purchase price: $400,000
NOI: $23,670

Cap Rate = $23,670 ÷ $400,000 = 5.92%
```

**Cap Rate Analysis:**
```
If cap rate > mortgage rate: Positive leverage
If cap rate < mortgage rate: Negative leverage

Example:
Cap rate: 5.92%
Mortgage rate: 7.0%
Result: Negative leverage (hurts cash flow)

Solution: Increase rents, reduce expenses, or pass
```

#### Internal Rate of Return (IRR)

IRR accounts for time value of money and property appreciation.

**IRR Calculation Method:**
```
IRR = Rate where NPV of all cash flows = 0

Cash flows to include:
Year 0: Initial investment (negative)
Years 1-N: Annual cash flows (positive/negative)
Year N: Sale proceeds (positive)
```

**Example IRR Calculation:**
```
Year 0: -$93,000 (initial investment)
Year 1: $3,000 (cash flow)
Year 2: $4,500 (cash flow, rent increased)
Year 3: $6,000 (cash flow)
Year 4: $7,500 (cash flow)
Year 5: $9,000 + $475,000 (cash flow + sale proceeds)

Sale calculation (Year 5):
Original price:          $400,000
Appreciation (3%/year):  $463,635
Less selling costs (6%): $27,818
Net proceeds:            $435,817
Less loan balance:       ($273,500)
Less capital gains tax:  ($17,317)
Net sale proceeds:       $145,000
Plus Year 5 cash flow:   $9,000
Total Year 5 inflow:     $154,000

Using financial calculator or spreadsheet:
IRR ≈ 12.5%
```

**IRR Target Ranges:**
- Core investments: 8-12%
- Value-add: 12-18%
- Opportunistic: 18%+
- Development: 20%+

#### Return on Equity (ROE)

Measures return on your equity position (changes as you pay down loan):

**Formula:**
```
ROE = (NOI - Debt Service) ÷ Current Equity

Current Equity = Property Value - Loan Balance
```

**Example Year 1 vs Year 5:**
```
Year 1:
Property value:     $400,000
Loan balance:       $320,000
Equity:             $80,000
NOI:                $23,670
Debt service:       $25,553
Cash flow:          ($1,883)
ROE = -2.35%

Year 5:
Property value:     $463,635 (3% annual appreciation)
Loan balance:       $273,500
Equity:             $190,135
NOI:                $28,500 (rent growth)
Debt service:       $25,553
Cash flow:          $2,947
ROE = 1.55%

Note: ROE improves as equity builds and rents increase
```

### 2.3 Investment Rules of Thumb

#### The 1% Rule

**Rule:**
```
Monthly rent should equal 1% of purchase price
```

**Example:**
```
Purchase price: $300,000
Required monthly rent: $300,000 × 0.01 = $3,000

Actual rent: $2,400
Rent/price ratio: 0.8%
Result: Fails 1% rule (may still work depending on expenses)
```

**Reality Check:**
- 1% rule increasingly difficult in appreciating markets
- More realistic in lower-cost markets
- Use as initial screening, not absolute requirement
- 0.7-0.8% may work in low-tax, low-expense markets
- 1%+ typically needed in high-tax, high-expense areas

#### The 50% Rule

**Rule:**
```
Operating expenses ≈ 50% of gross rental income
Therefore: NOI ≈ 50% of gross rental income
```

**Application:**
```
Gross rental income: $50,000
Estimated operating expenses: $25,000
Estimated NOI: $25,000

Quick cash flow estimate:
NOI: $25,000
Debt service: ($22,000)
Estimated cash flow: $3,000
```

**50% Rule Breakdown:**
```
Typical operating expense categories:
Property taxes:      10-15%
Insurance:           3-5%
Management:          8-10%
Maintenance:         8-12%
CapEx reserves:      5-10%
Utilities:           0-10%
Other:               4-8%
                     --------
Total:               45-60% (50% average)
```

**When 50% Rule Varies:**
- Higher than 50%: High-tax states, older properties, Class C
- Lower than 50%: Low-tax states, newer properties, tenant-paid utilities

#### The 70% Rule (Fix and Flip)

**Rule:**
```
Maximum purchase price = (ARV × 0.70) - Repair Costs

Where:
ARV = After Repair Value
70% = Factor accounting for holding costs, financing, profit
```

**Example:**
```
After Repair Value (ARV): $300,000
Estimated repair costs: $40,000

Maximum purchase price:
($300,000 × 0.70) - $40,000 = $170,000

Cost breakdown:
Purchase: $170,000
Repairs: $40,000
Holding costs: $10,000
Selling costs: $18,000
                --------
Total costs: $238,000
Sale price: $300,000
Profit: $62,000 (20.7% of ARV)
```

**70% Rule Variations:**
```
Competitive markets: 75-80% (lower profit margin)
Distressed markets: 60-65% (higher risk premium)
Experienced investors: 75-80% (lower contingency needed)
New investors: 65-70% (higher safety margin)
```

#### The 2% Rule

**Rule:**
```
Monthly rent should equal 2% of purchase price
(More aggressive than 1% rule)
```

**Example:**
```
Purchase price: $150,000
Required monthly rent: $150,000 × 0.02 = $3,000

Reality: 2% rule primarily achievable in:
- Lower-cost markets (Midwest, South)
- C and D class properties
- Markets with rent control or high demand
```

**2% Rule Analysis:**
```
Property at 2% rule:
Purchase: $150,000
Monthly rent: $3,000
Annual rent: $36,000
Rent/price: 24%

Property at 1% rule:
Purchase: $150,000
Monthly rent: $1,500
Annual rent: $18,000
Rent/price: 12%

2% properties typically higher risk but higher return
```

### 2.4 Deal Analysis Checklist

**Phase 1: Initial Screening**
```
[ ] Rent/price ratio meets minimum threshold (0.8-1%+)
[ ] Location meets investment criteria
[ ] Property type fits strategy
[ ] Price range within budget
[ ] Initial numbers show potential
[ ] No obvious red flags
```

**Phase 2: Financial Analysis**
```
[ ] Detailed income projection completed
[ ] All operating expenses identified and estimated
[ ] NOI calculation verified
[ ] Cap rate calculated and compared to market
[ ] Cash flow projection: Year 1-5
[ ] Cash-on-cash return meets target (6-10%+)
[ ] IRR projection meets target (10-15%+)
[ ] Break-even analysis completed
[ ] Sensitivity analysis performed
[ ] Exit strategy defined with projected returns
```

**Phase 3: Property Analysis**
```
[ ] Physical inspection completed
[ ] Deferred maintenance identified and costed
[ ] Major systems condition assessed (roof, HVAC, plumbing, electrical)
[ ] Property photos/documentation collected
[ ] Rent roll analyzed (if multi-family)
[ ] Lease terms reviewed
[ ] Current occupancy verified
[ ] Market rent analysis completed
[ ] Comparable sales analyzed
[ ] Neighborhood assessment completed
```

**Phase 4: Risk Assessment**
```
[ ] Market risk: Supply/demand balance
[ ] Property risk: Condition and deferred maintenance
[ ] Financial risk: Can sustain negative cash flow if needed
[ ] Tenant risk: Quality and stability of tenant base
[ ] Location risk: Crime, schools, employment
[ ] Liquidity risk: Can sell within reasonable timeframe
[ ] Interest rate risk: Impact of rate changes
[ ] Regulatory risk: Zoning, rent control, regulations
[ ] Environmental risk: Flood zone, contamination, etc.
```

**Phase 5: Financing Analysis**
```
[ ] Financing options compared
[ ] Down payment requirement confirmed
[ ] Interest rate locked or confirmed
[ ] Loan terms reviewed
[ ] Closing costs estimated
[ ] Cash reserves planned (6-12 months expenses)
[ ] Emergency fund in place
[ ] Impact of leverage analyzed
```

**Phase 6: Deal Comparison**
```
[ ] Compared to other opportunities
[ ] Ranked against investment criteria
[ ] Risk/return profile assessed
[ ] Opportunity cost considered
[ ] Strategic fit evaluated
[ ] Resource requirements assessed
[ ] Timeline and effort estimated
```

**Go/No-Go Decision Matrix:**
```
Deal Scoring (Rate 1-10):

Financial Performance:        ___/10
Property Condition:           ___/10
Location Quality:             ___/10
Market Fundamentals:          ___/10
Risk Profile:                 ___/10
Strategic Fit:                ___/10
Financing Terms:              ___/10
Management Ease:              ___/10
                              ------
Total Score:                  ___/80

Decision Guidelines:
70-80: Excellent deal, proceed
60-69: Good deal, verify key assumptions
50-59: Marginal deal, negotiate improvements
Below 50: Pass unless unique circumstances
```

### 2.5 Investment Property Pro Forma Template

**5-Year Investment Pro Forma:**
```
═══════════════════════════════════════════════════════════════════════
                     5-YEAR INVESTMENT PRO FORMA
═══════════════════════════════════════════════════════════════════════

PROPERTY INFORMATION
───────────────────────────────────────────────────────────────────────
Property Address:        [Address]
Property Type:           [Single-family / Multi-family / Commercial]
Units:                   [Number]
Total Square Feet:       [SF]
Purchase Price:          $XXX,XXX
Purchase Date:           [Date]

FINANCING DETAILS
───────────────────────────────────────────────────────────────────────
Loan Amount:             $XXX,XXX
Down Payment:            $XX,XXX (XX%)
Interest Rate:           X.XX%
Loan Term:               XX years
Monthly Payment:         $X,XXX.XX
Total Interest (life):   $XXX,XXX

INITIAL INVESTMENT
───────────────────────────────────────────────────────────────────────
Down Payment:            $XX,XXX
Closing Costs:           $X,XXX
Immediate Repairs:       $X,XXX
Reserves:                $X,XXX
                         --------
Total Cash Investment:   $XX,XXX

═══════════════════════════════════════════════════════════════════════
                           YEAR 1    YEAR 2    YEAR 3    YEAR 4    YEAR 5
───────────────────────────────────────────────────────────────────────

INCOME
Gross Rent Income         XX,XXX    XX,XXX    XX,XXX    XX,XXX    XX,XXX
Other Income              X,XXX     X,XXX     X,XXX     X,XXX     X,XXX
Vacancy Loss (X%)         (X,XXX)   (X,XXX)   (X,XXX)   (X,XXX)   (X,XXX)
                          ------    ------    ------    ------    ------
Effective Gross Income    XX,XXX    XX,XXX    XX,XXX    XX,XXX    XX,XXX

OPERATING EXPENSES
Property Taxes            X,XXX     X,XXX     X,XXX     X,XXX     X,XXX
Insurance                 X,XXX     X,XXX     X,XXX     X,XXX     X,XXX
Management                X,XXX     X,XXX     X,XXX     X,XXX     X,XXX
Repairs & Maintenance     X,XXX     X,XXX     X,XXX     X,XXX     X,XXX
Utilities                 X,XXX     X,XXX     X,XXX     X,XXX     X,XXX
CapEx Reserves            X,XXX     X,XXX     X,XXX     X,XXX     X,XXX
Other Expenses            X,XXX     X,XXX     X,XXX     X,XXX     X,XXX
                          ------    ------    ------    ------    ------
Total Operating Expenses  XX,XXX    XX,XXX    XX,XXX    XX,XXX    XX,XXX
                          ------    ------    ------    ------    ------
Net Operating Income      XX,XXX    XX,XXX    XX,XXX    XX,XXX    XX,XXX

DEBT SERVICE
Annual Debt Service       XX,XXX    XX,XXX    XX,XXX    XX,XXX    XX,XXX
                          ------    ------    ------    ------    ------
Cash Flow Before Taxes    X,XXX     X,XXX     X,XXX     X,XXX     X,XXX

EQUITY BUILD-UP
Principal Pay-Down        X,XXX     X,XXX     X,XXX     X,XXX     X,XXX
Property Appreciation     XX,XXX    XX,XXX    XX,XXX    XX,XXX    XX,XXX
                          ------    ------    ------    ------    ------
Total Equity Gain         XX,XXX    XX,XXX    XX,XXX    XX,XXX    XX,XXX

RETURN METRICS
Cash-on-Cash Return       X.X%      X.X%      X.X%      X.X%      X.X%
Cap Rate                  X.X%      X.X%      X.X%      X.X%      X.X%
Operating Expense Ratio   XX%       XX%       XX%       XX%       XX%
Debt Coverage Ratio       X.XX      X.XX      X.XX      X.XX      X.XX

CUMULATIVE TOTALS
Cumulative Cash Flow      X,XXX     X,XXX     XX,XXX    XX,XXX    XX,XXX
Cumulative Equity Gain    XX,XXX    XX,XXX    XX,XXX    XXX,XXX   XXX,XXX
Property Value            XXX,XXX   XXX,XXX   XXX,XXX   XXX,XXX   XXX,XXX
Loan Balance              XXX,XXX   XXX,XXX   XXX,XXX   XXX,XXX   XXX,XXX
Equity Position           XX,XXX    XXX,XXX   XXX,XXX   XXX,XXX   XXX,XXX

═══════════════════════════════════════════════════════════════════════

ASSUMPTIONS
───────────────────────────────────────────────────────────────────────
Annual Rent Growth:              X.X%
Annual Expense Growth:           X.X%
Annual Property Appreciation:    X.X%
Vacancy Rate:                    X.X%
Management Fee:                  X.X%
CapEx Reserve:                   X.X% of EGI

EXIT ANALYSIS (YEAR 5)
───────────────────────────────────────────────────────────────────────
Projected Sale Price:            $XXX,XXX
Less: Selling Costs (6%):        ($XX,XXX)
Net Sale Proceeds:               $XXX,XXX
Less: Loan Balance:              ($XXX,XXX)
Gross Equity at Sale:            $XXX,XXX
Less: Capital Gains Tax:         ($XX,XXX)
Net Equity at Sale:              $XXX,XXX

TOTAL RETURN SUMMARY
───────────────────────────────────────────────────────────────────────
Initial Investment:              $XX,XXX
Cumulative Cash Flow (5 years):  $XX,XXX
Net Equity at Sale:              $XXX,XXX
                                 ---------
Total Profit:                    $XXX,XXX
Total Return:                    XXX%
Annualized Return (IRR):         XX.X%

═══════════════════════════════════════════════════════════════════════
```

---

## 3. Market Research

Understanding real estate market dynamics, cycles, and indicators for informed investment decisions.

### 3.1 Supply and Demand Indicators

#### Demand Indicators

**Population Growth:**
```
Strong demand indicators:
- Population growth > 1.5% annually
- Net migration positive (people moving in)
- Age demographics favorable (25-45 year olds)
- Household formation increasing

Example analysis:
City population:
2020: 500,000
2024: 535,000
Growth: 7% (1.75% annually) ✓ Strong

Sources:
- US Census Bureau
- City/county planning departments
- Regional economic development agencies
```

**Employment Indicators:**
```
Strong demand signals:
- Job growth > national average
- Unemployment < national average
- Diversified employment base (not one industry)
- Major employers expanding
- Corporate relocations to area

Example:
Metro area jobs:
2020: 300,000
2024: 318,000
Growth: 6% (1.5% annually)
Unemployment: 3.5% (vs 4.0% national)
Assessment: Strong ✓

Key sectors to monitor:
- Technology: High-paying, growth
- Healthcare: Stable, growing
- Education: Stable
- Manufacturing: Cyclical
- Government: Stable
```

**Income Growth:**
```
Median household income trends:
2020: $65,000
2024: $72,000
Growth: 10.8% (2.6% annually)
Above inflation: Yes ✓

Income growth > 2% annually = Strong demand
Income growth < 1% annually = Weak demand
```

**Rent Growth:**
```
Strong rental demand:
- Rent growth > 3% annually
- Low vacancy rates (< 5%)
- Decreasing time on market
- Multiple applications per unit
- Rent growth exceeding income growth

Example:
Average 2-bed apartment rent:
2020: $1,200
2024: $1,380
Growth: 15% (3.6% annually) ✓ Very strong
```

#### Supply Indicators

**Housing Inventory:**
```
Months of inventory = Active listings ÷ Monthly sales

Interpretation:
0-3 months: Severe shortage, seller's market
4-5 months: Slight shortage, favors sellers
6 months: Balanced market
7-9 months: Slight surplus, favors buyers
10+ months: Oversupply, buyer's market

Example:
Active listings: 450
Average monthly sales: 90
Months of inventory: 5.0
Assessment: Slight shortage ✓
```

**Construction Pipeline:**
```
Monitor new construction:

Single-family permits:
Current year: 2,500 permits
Last year: 2,200 permits
Change: +13.6%
Assessment: Supply increasing

Multi-family permits:
Current year: 800 units
Last year: 1,200 units
Change: -33.3%
Assessment: Supply decreasing

Key question: Can demand absorb new supply?

Red flag: New supply > 10% of existing inventory
```

**Absorption Rate:**
```
Absorption rate = Units sold or leased ÷ Time period

Example (for-sale market):
90 homes sold per month
450 active listings
Absorption period: 5 months
Assessment: Healthy

Example (rental market):
New 200-unit building
50 units leased in first 2 months
Absorption rate: 25 units/month
Time to fill: 8 months total
Assessment: If > 6 months, potential oversupply issue
```

**Vacancy Rates:**
```
Healthy vacancy rates by type:

Single-family rentals: 2-4%
Multi-family apartments: 4-7%
Office: 10-15%
Retail: 5-10%
Industrial: 3-7%

Example analysis:
Market vacancy: 3.5%
Your property: 5%
Assessment: Property underperforming, investigate why

Trend analysis:
2022: 4.5%
2023: 4.0%
2024: 3.5%
Trend: Tightening (demand increasing) ✓
```

### 3.2 Market Cycle Stages

Real estate markets move in cycles. Identify the current stage:

#### Stage 1: Recovery (Bottom)

**Characteristics:**
```
Supply Indicators:
- High vacancy rates (declining from peak)
- Construction at standstill
- Concessions common
- Negative rent growth (improving)

Demand Indicators:
- Economic recovery beginning
- Job growth turning positive
- Household formation increasing
- Population growth resuming

Investment Implications:
- Best time to buy (lowest prices)
- Most risk (catching falling knife)
- Requires strong conviction and reserves
- Long-term focused investors only
```

**Example Metrics:**
```
Vacancy rate: 12% (was 15%)
Rent growth: -1% (was -4%)
Employment growth: +0.5%
New construction: Minimal
Cap rates: 8-10%
```

#### Stage 2: Expansion (Growth)

**Characteristics:**
```
Supply Indicators:
- Vacancy declining steadily
- New construction beginning
- Concessions eliminated
- Rent growth accelerating

Demand Indicators:
- Strong job growth
- Positive migration
- Income growth solid
- Household formation strong

Investment Implications:
- Great time to buy (value remains)
- Lower risk than recovery
- Both appreciation and cash flow
- Most investors comfortable here
```

**Example Metrics:**
```
Vacancy rate: 6% (declining)
Rent growth: 3-4%
Employment growth: 2%
New construction: Increasing
Cap rates: 6-7%
```

#### Stage 3: Hyper Supply (Peak)

**Characteristics:**
```
Supply Indicators:
- Vacancy low but stabilizing
- Heavy construction activity
- Rent growth slowing
- Absorption slowing

Demand Indicators:
- Job growth steady but may slow
- Population growth steady
- Economic expansion long-running
- Some demand saturation

Investment Implications:
- Proceed with caution
- New supply may exceed demand
- Prices may be overheated
- Consider selling, not buying
- Focus on unique properties only
```

**Example Metrics:**
```
Vacancy rate: 3% (stable)
Rent growth: 1-2% (slowing)
Employment growth: 1%
New construction: Very high
Cap rates: 4-5%
```

#### Stage 4: Recession (Decline)

**Characteristics:**
```
Supply Indicators:
- Vacancy increasing
- Excess supply apparent
- Concessions increasing
- Negative rent growth

Demand Indicators:
- Job losses occurring
- Out-migration beginning
- Economic contraction
- Household formation declining

Investment Implications:
- Avoid buying (falling prices)
- Consider selling if needed
- Focus on cash reserves
- Reposition for next cycle
- Distressed opportunities emerging (risky)
```

**Example Metrics:**
```
Vacancy rate: 8% (rising)
Rent growth: -2%
Employment growth: -1%
New construction: Halted
Cap rates: 7-9%
```

#### Cycle Timing Strategy

**Buy:**
- Recovery phase (best value, most risk)
- Early expansion phase (good value, lower risk)

**Hold:**
- Expansion phase (maximize appreciation)
- Early hyper supply (ride momentum)

**Sell:**
- Late hyper supply (take profits)
- Early recession (before prices fall)

**Wait:**
- Recession phase (preserve capital)
- Late recession (prepare for recovery)

### 3.3 Key Economic Indicators

#### Leading Indicators (Predict Future)

**Building Permits:**
```
Signals future supply:
- Rising permits: More supply coming (6-18 months)
- Falling permits: Supply tightening

Example:
Current permits: 2,000/month
12-month average: 1,800/month
Change: +11%
Implication: Supply increasing, monitor absorption
```

**Initial Unemployment Claims:**
```
Predicts job market:
- Rising claims: Job market weakening
- Falling claims: Job market strengthening

Example:
Current claims: 5,000/week
52-week average: 6,500/week
Assessment: Job market improving ✓
```

**Consumer Confidence:**
```
Predicts spending:
- Rising confidence: More home buying
- Falling confidence: Housing demand weakening

Index interpretation:
> 100: Optimistic
80-100: Neutral
< 80: Pessimistic
```

#### Coincident Indicators (Current State)

**Employment Levels:**
```
Current job market state:
Total employment: 300,000
Change from last year: +6,000 (+2%)
Unemployment rate: 3.8%
Assessment: Strong employment ✓
```

**Gross Metro Product (GMP):**
```
Economic output:
Current GMP: $45 billion
Growth rate: 3.5%
vs National GDP: 2.5%
Assessment: Outperforming ✓
```

**Income Levels:**
```
Median household income: $75,000
Growth rate: 3.0%
vs Inflation: 2.5%
Real income growth: 0.5%
Assessment: Positive ✓
```

#### Lagging Indicators (Confirm Trends)

**Average Home Prices:**
```
Median sale price: $425,000
Change YoY: +5%
vs Peak: -2% (from $434,000)
Assessment: Prices stabilizing after peak
```

**Foreclosure Rates:**
```
Current rate: 0.5% of loans
12-month ago: 0.4%
Assessment: Slight increase, monitor trend
```

**Long-term Rent Growth:**
```
5-year rent growth: 18%
Annualized: 3.4%
Assessment: Healthy long-term fundamentals
```

### 3.4 Data Sources

#### Public Data Sources

**Government Sources:**
```
US Census Bureau (census.gov)
- Population data
- Demographic trends
- American Community Survey
- Building permits

Bureau of Labor Statistics (bls.gov)
- Employment data
- Unemployment rates
- Wage data
- Consumer Price Index

Federal Housing Finance Agency (fhfa.gov)
- House Price Index
- Market trends
- Mortgage data

HUD User (huduser.gov)
- Fair Market Rents
- Income limits
- Housing data
```

**Local Government:**
```
County Assessor/Tax Collector
- Property tax data
- Assessed values
- Sales records

City Planning Department
- Building permits
- Zoning information
- Development plans

Economic Development Agency
- Job growth data
- Major employers
- Business expansions
```

#### Commercial Data Sources

**MLS (Multiple Listing Service):**
```
Access through:
- Real estate agent
- MLS subscription
- Public MLS portals

Data available:
- Active listings
- Sold properties
- Days on market
- Price trends
- Inventory levels
```

**Real Estate Websites:**
```
Zillow.com
- Zestimate values
- Rental estimates
- Market trends
- For-sale inventory

Redfin.com
- Detailed market data
- School information
- Neighborhood insights

Apartments.com / Rent.com
- Rental rates
- Vacancy data
- Amenity comparisons
```

**Commercial Data Providers:**
```
CoStar (costar.com)
- Commercial property data
- Market analytics
- Lease comps
- Subscription required

Yardi Matrix
- Multi-family data
- Market reports
- Supply pipeline

RealPage
- Rental market data
- Revenue management
- Analytics
```

#### Research Process

**Step 1: Macro Analysis**
```
1. Review national economic trends
2. Identify growing regions
3. Research state-level trends
4. Shortlist target metros
```

**Step 2: Metro Analysis**
```
1. Population growth trends
2. Employment diversity
3. Major employers
4. Infrastructure projects
5. Quality of life factors
6. Economic development plans
```

**Step 3: Micro Analysis**
```
1. Neighborhood demographics
2. School ratings
3. Crime statistics
4. Amenities and services
5. Transportation access
6. Future development plans
```

**Step 4: Property-Level Research**
```
1. Comparable sales analysis
2. Rental rate analysis
3. Occupancy/vacancy trends
4. Property condition assessment
5. Neighborhood walk-through
6. Talk to neighbors/tenants
```

**Market Research Checklist:**
```
[ ] Population trends analyzed (5-year)
[ ] Employment data reviewed
[ ] Income levels and growth assessed
[ ] Housing inventory measured
[ ] Construction pipeline evaluated
[ ] Rent and price trends analyzed
[ ] Vacancy rates researched
[ ] Market cycle stage identified
[ ] Economic indicators reviewed
[ ] Competitive properties surveyed
[ ] Neighborhood assessed in person
[ ] Future development researched
[ ] Risk factors identified
[ ] Growth catalysts identified
[ ] Data sources documented
```

---

## 4. Due Diligence

Comprehensive property investigation process before purchase to identify risks, defects, and opportunities.

### 4.1 Physical Inspection

#### Structure and Foundation

**Foundation Inspection:**
```
Visual Inspection Checklist:
[ ] Cracks in foundation (width, location, pattern)
[ ] Settlement or heaving
[ ] Water stains or moisture
[ ] Proper grading away from foundation
[ ] Foundation walls plumb and level
[ ] Basement or crawl space condition
[ ] Drainage systems functioning
[ ] Sump pump (if applicable)

Red Flags:
- Cracks > 1/4 inch wide
- Horizontal cracks
- Stair-step cracks in block foundations
- Bowing or leaning walls
- Standing water in basement/crawl space
- Efflorescence (white mineral deposits)

Estimated Repair Costs:
Minor cracks (sealing): $500-2,000
Major cracks (structural): $3,000-10,000
Foundation stabilization: $10,000-30,000
Severe structural issues: $30,000-100,000+
```

**Structural Elements:**
```
Check:
[ ] Roof sag or unevenness
[ ] Floors level and solid
[ ] Wall cracks or bulging
[ ] Door and window operation
[ ] Framing condition (if visible)
[ ] Load-bearing modifications
[ ] Pest damage (termites, carpenter ants)

Warning Signs:
- Bouncy or sloping floors
- Doors/windows don't close properly
- Visible structural modifications
- Evidence of pest infestation
- Water damage to structural members

Repair Cost Ranges:
Beam replacement: $5,000-15,000
Floor joist repair: $3,000-10,000
Pest damage repair: $2,000-20,000+
Structural reinforcement: $5,000-30,000+
```

#### Roof System

**Roof Inspection:**
```
Key Items:
[ ] Roof age and remaining life
[ ] Shingle/material condition
[ ] Flashing around penetrations
[ ] Gutters and downspouts
[ ] Attic ventilation
[ ] Signs of leaks or damage
[ ] Chimney condition
[ ] Valleys and ridges

Roof Life Expectancy:
Asphalt shingles: 15-25 years
Architectural shingles: 25-30 years
Metal: 40-70 years
Tile: 50-100 years
Flat/built-up: 15-25 years

Replacement Costs (per square foot):
Asphalt shingles: $3-7/sf
Architectural: $4-8/sf
Metal: $8-14/sf
Tile: $10-18/sf
Flat roof: $4-10/sf

Example:
2,000 sq ft roof
Asphalt shingle replacement: $6,000-14,000
Life remaining: 5 years
Budget for replacement in capital reserves
```

#### Mechanical Systems

**HVAC System:**
```
Inspection Points:
[ ] System age and type
[ ] Operation test (heating and cooling)
[ ] Condition of equipment
[ ] Ductwork condition
[ ] Thermostat function
[ ] Air filter condition
[ ] Refrigerant levels
[ ] Recent maintenance records

HVAC Life Expectancy:
Central AC: 10-15 years
Furnace (gas): 15-20 years
Heat pump: 10-15 years
Boiler: 15-25 years

Replacement Costs:
Central AC (3-ton): $3,000-7,000
Furnace: $2,500-6,000
Complete system: $5,000-12,000
Ductwork: $2,000-5,000

Age Assessment:
0-5 years: Excellent, minimal reserve needed
6-10 years: Good, start building reserves
11-15 years: Fair, replacement budget needed
16+ years: Replace soon, negotiate or budget
```

**Plumbing System:**
```
Check:
[ ] Water pressure throughout
[ ] Drain function and speed
[ ] Supply line condition
[ ] Drain line condition
[ ] Water heater age and condition
[ ] Visible leaks or corrosion
[ ] Main shut-off valve
[ ] Pipe material (copper, PVC, galvanized)

Pipe Material Issues:
Galvanized steel: Replace if present (40+ years old)
Polybutylene: Replace (known to fail)
Lead: Replace (health hazard)
Copper: Good, 50+ year life
PEX: Good, modern standard

Water Heater:
Life expectancy: 8-12 years
Replacement cost: $800-2,500 (tank)
Tankless: $2,000-4,500

Plumbing Repairs:
Re-pipe house: $4,000-15,000
Water heater: $800-2,500
Sewer line: $3,000-10,000+
Main line: $1,500-5,000
```

**Electrical System:**
```
Inspection:
[ ] Service panel capacity (amps)
[ ] Panel condition and age
[ ] Circuit breaker function
[ ] Outlet testing (GFCI where required)
[ ] Wiring type and condition
[ ] Grounding present
[ ] No DIY work/violations
[ ] Adequate circuits for modern use

Service Capacity:
60-amp: Inadequate for modern home
100-amp: Minimum acceptable
150-amp: Good for most homes
200-amp: Ideal for modern home

Wiring Issues:
Knob and tube: Replace (insurance issue)
Aluminum: Monitor, potential fire hazard
Ungrounded: Update for safety

Electrical Repairs:
Panel upgrade: $1,500-3,000
Re-wire house: $6,000-20,000
New circuit: $200-500
Outlet/switch: $50-150
```

#### Interior Condition

**Interior Assessment:**
```
Check Each Room:
[ ] Floor condition and type
[ ] Wall condition
[ ] Ceiling condition
[ ] Windows (operation, seals, condition)
[ ] Doors (operation, condition)
[ ] Built-ins and fixtures
[ ] Closet space and condition
[ ] Smoke/CO detectors

Kitchen:
[ ] Appliance condition and age
[ ] Cabinet condition
[ ] Countertop condition
[ ] Plumbing fixtures
[ ] Flooring
[ ] Lighting and electrical

Bathrooms:
[ ] Fixtures condition and age
[ ] Tile and grout
[ ] Ventilation fan
[ ] Plumbing condition
[ ] Water pressure
[ ] Drainage

Cosmetic Update Costs:
Paint (whole house): $3,000-8,000
Flooring (carpet): $2,000-5,000 per 1,000 sf
Flooring (hardwood): $5,000-12,000 per 1,000 sf
Kitchen update: $10,000-30,000
Kitchen remodel: $30,000-60,000+
Bathroom update: $5,000-15,000
Bathroom remodel: $15,000-35,000+
```

### 4.2 Title and Legal Review

#### Title Examination

**Standard Title Issues to Check:**
```
[ ] Clear chain of ownership
[ ] No liens (mortgage, tax, mechanic's, judgment)
[ ] No encumbrances affecting use
[ ] Easements identified and acceptable
[ ] No pending legal actions
[ ] Property boundaries accurate
[ ] Zoning compliance
[ ] Building permit history
```

**Common Title Issues:**
```
Tax Liens:
- Must be paid at closing
- Take priority over other liens
- Check county tax records

Mortgage Liens:
- Existing mortgages
- Should be paid off at closing
- Verify payoff amount

Mechanic's Liens:
- From unpaid contractors
- Can be filed up to 90-120 days after work
- Verify no recent work or get lien releases

Judgment Liens:
- From court judgments
- Must be satisfied to clear title
- Can affect property value

Easements:
- Utility easements (standard)
- Access easements (review carefully)
- Drainage easements
- Verify don't impact intended use
```

**Title Insurance:**
```
Owner's Policy:
- Protects buyer
- One-time premium at closing
- Coverage equals purchase price
- Cost: 0.5-1% of purchase price

Lender's Policy:
- Protects lender
- Required by lender
- Coverage decreases as loan paid down
- Buyer typically pays

Example:
Purchase price: $400,000
Owner's policy: $2,000-4,000
Lender's policy: $1,000-2,000
```

#### Zoning and Land Use

**Zoning Verification:**
```
Verify:
[ ] Current zoning designation
[ ] Intended use is permitted
[ ] Building complies with zoning
[ ] No zoning violations exist
[ ] Future zoning changes planned
[ ] Setback requirements met
[ ] Parking requirements met
[ ] Density requirements met

Example Check:
Property zoned: R-2 (Two-family residential)
Current use: Single-family with ADU
Verify: ADU permitted under R-2? Yes ✓
Non-conforming use: No ✓
```

**Permitted Uses:**
```
Review local zoning code:
- Permitted uses (by right)
- Conditional uses (special permit required)
- Prohibited uses
- Accessory uses allowed

Investment Opportunity:
If zoning allows higher/better use than current,
may represent value-add opportunity.

Example:
Current: Single-family
Zoning allows: Duplex
Opportunity: Convert or rebuild as duplex
```

#### Legal Documents

**Purchase Agreement Review:**
```
Key Terms to Verify:
[ ] Purchase price and terms
[ ] Earnest money amount and terms
[ ] Contingencies (inspection, financing, appraisal)
[ ] Closing date
[ ] Included/excluded items
[ ] Seller disclosures
[ ] As-is clause (if applicable)
[ ] Default remedies
[ ] Closing cost allocation
```

**HOA Documents (if applicable):**
```
Request and Review:
[ ] CC&Rs (Covenants, Conditions & Restrictions)
[ ] HOA bylaws
[ ] Financial statements (2-3 years)
[ ] Meeting minutes (last 12 months)
[ ] Budget and reserves
[ ] Insurance coverage
[ ] Pending litigation
[ ] Special assessments planned
[ ] Reserve study
[ ] Delinquency rates

Red Flags:
- Low reserves (< 25% funded)
- High delinquency (> 10%)
- Pending litigation
- Special assessments
- Restrictions affecting rental use
- Increasing fees without reserve building

HOA Fee Analysis:
Monthly fee: $250
Annual cost: $3,000
Impact on NOI: -$3,000
Impact on value (8% cap): -$37,500
```

### 4.3 Financial Document Review

#### Rent Roll Analysis (Multi-family)

**Rent Roll Review:**
```
For Each Unit Verify:
[ ] Tenant name
[ ] Lease start and end date
[ ] Monthly rent amount
[ ] Security deposit amount
[ ] Lease type (month-to-month, annual)
[ ] Payment history
[ ] Outstanding balance
[ ] Utilities responsibility
[ ] Parking included
[ ] Special terms or concessions

Analysis:
Total units: 10
Occupied: 9 (90%)
Vacant: 1 (10%)
Total monthly rent: $11,200
Average rent per unit: $1,244

Lease Expiration Schedule:
Next 3 months: 2 leases (20%)
3-6 months: 3 leases (30%)
6-12 months: 4 leases (40%)
Month-to-month: 0 (0%)

Assessment:
- Occupancy healthy at 90%
- Staggered expirations (good)
- No month-to-month risk
- Verify market rents vs actual rents
```

**Rent Comparison to Market:**
```
Unit 1: $1,200/month (Market: $1,275) -$75
Unit 2: $1,250/month (Market: $1,275) -$25
Unit 3: $1,300/month (Market: $1,275) +$25

Analysis:
Average rent: $1,250
Market rent: $1,275
Upside: $25/unit average
Annual upside: $25 × 10 × 12 = $3,000/year

At 8% cap rate:
Value upside = $3,000 ÷ 0.08 = $37,500

Opportunity: Raise rents to market at lease renewal
```

#### Operating Statements

**Request 3 Years of Statements:**
```
Income Items to Verify:
[ ] Rental income (compare to rent roll)
[ ] Other income sources
[ ] Vacancy rate (actual vs claimed)
[ ] Collection loss
[ ] Concessions or discounts

Expense Items to Verify:
[ ] Property taxes (compare to tax records)
[ ] Insurance (get quote)
[ ] Utilities (verify which owner-paid)
[ ] Repairs and maintenance (adequate?)
[ ] Property management (if applicable)
[ ] Legal and professional
[ ] Landscaping and snow
[ ] Other operating expenses

Common Seller Misrepresentations:
- Understated vacancy
- Missing expense categories
- Owner-performed maintenance not counted
- One-time expenses excluded
- Property tax based on old assessment
```

**Reconstructing Pro Forma:**
```
Seller's NOI: $45,000

Adjustments:
Gross income: $120,000 (verified from rent roll)
Vacancy (7%): ($8,400) [Seller used 5%]
Effective income: $111,600

Expenses:
Property tax: $12,000 [Seller: $10,000, verified higher]
Insurance: $3,600 [Verified with quote]
Management: $11,160 [Seller: $0, add 10%]
Repairs: $8,928 [Seller: $6,000, increase to 8%]
Utilities: $4,800 [Verified with bills]
Other: $2,500 [Verified]
CapEx reserve: $8,928 [Seller: $0, add 8%]
Total expenses: $51,916

Reconstructed NOI: $59,684

Seller's NOI: $45,000
Actual NOI: $59,684
Difference: +$14,684 (Better than claimed!)

At 7% cap rate:
Seller's value: $45,000 ÷ 0.07 = $642,857
Actual value: $59,684 ÷ 0.07 = $852,629
Potential upside: $209,772

Note: This example shows upside, but often the
reconstruction reveals LOWER actual NOI.
```

#### Tax Returns

**Review Property Tax Returns:**
```
Request:
[ ] Schedule E (rental property income)
[ ] Last 2-3 years
[ ] Depreciation schedules

Verify:
- Reported income matches operating statements
- Expenses reasonable and complete
- No major discrepancies
- Capital improvements identified

Red Flags:
- Income doesn't match claims
- Significant one-time expenses
- Evidence of deferred maintenance
- Depreciation accelerated (condition issues?)
```

### 4.4 Environmental and Site

**Environmental Concerns:**
```
Check:
[ ] Flood zone status (FEMA maps)
[ ] Wetlands present
[ ] Soil contamination risk
[ ] Former uses of property
[ ] Underground storage tanks
[ ] Asbestos (pre-1980 buildings)
[ ] Lead paint (pre-1978)
[ ] Radon levels
[ ] Mold issues

Phase I Environmental Assessment:
Cost: $2,000-5,000
When needed:
- Commercial properties
- Industrial properties
- Former gas stations
- Dry cleaners
- Manufacturing sites
- Any environmental concern

Flood Insurance:
Check FEMA flood maps at msc.fema.gov
Zone X: Minimal risk, no insurance required
Zone A/AE: High risk, insurance required
Zone V/VE: Very high risk (coastal)

Annual flood insurance:
Low risk: $400-1,000
High risk: $2,000-5,000+
Very high risk: $5,000-10,000+

Impact on investment:
$3,000 annual insurance = $3,000 lower NOI
At 8% cap = $37,500 lower value
```

**Site Conditions:**
```
Evaluate:
[ ] Drainage and grading
[ ] Retaining walls condition
[ ] Driveway and parking
[ ] Landscaping condition
[ ] Trees (health, proximity to structures)
[ ] Fencing condition
[ ] Outdoor structures (shed, etc.)
[ ] Utilities access
[ ] Septic system (if applicable)
[ ] Well condition (if applicable)

Septic System:
Last pumped: ________
Last inspection: ________
Tank size: ________
Drain field condition: ________
Inspection cost: $300-500
Replacement cost: $10,000-30,000

Well System:
Last tested: ________
Flow rate: ________ GPM
Water quality: ________
Pressure tank: ________
Testing cost: $200-400
Replacement cost: $5,000-15,000
```

**Due Diligence Checklist Summary:**
```
PHYSICAL INSPECTION
[ ] Professional home inspection completed
[ ] Major systems evaluated (roof, HVAC, plumbing, electrical)
[ ] Structural issues identified
[ ] Deferred maintenance documented
[ ] Repair costs estimated
[ ] Interior condition assessed
[ ] Environmental concerns investigated

TITLE AND LEGAL
[ ] Title search completed
[ ] No liens or encumbrances (or identified)
[ ] Zoning verified
[ ] Permitted use confirmed
[ ] Survey reviewed
[ ] Property boundaries clear
[ ] Easements acceptable
[ ] HOA documents reviewed (if applicable)

FINANCIAL REVIEW
[ ] Rent roll verified
[ ] Operating statements reviewed (3 years)
[ ] Expenses reconstructed
[ ] Tax returns reviewed
[ ] Market rents confirmed
[ ] Pro forma adjusted for reality
[ ] Lease terms reviewed
[ ] Tenant quality assessed

FINAL ASSESSMENT
[ ] All contingencies addressed
[ ] Repair negotiations completed
[ ] Final purchase price determined
[ ] Financing confirmed
[ ] Closing timeline set
[ ] Post-closing plan documented
```

---

## 5. Financing & Tax

Understanding financing options, loan metrics, and tax strategies for real estate investments.

### 5.1 Common Loan Types

#### Conventional Loans

**Primary Residence:**
```
Minimum down payment: 3-5%
Best rates with: 20%+ down
Typical terms: 15 or 30 years
Interest rates: Market rate
PMI required: If < 20% down
Max loan amount: $726,200 (2024, conforming)

Example:
Purchase price: $400,000
Down payment: $80,000 (20%)
Loan amount: $320,000
Rate: 7.0%
Term: 30 years
Monthly P&I: $2,129.45

Pros:
- Lowest rates available
- Long fixed-rate terms
- Conventional product

Cons:
- Strict qualification
- Lower DTI allowed for investors
- Limited to 10 financed properties per person
```

**Investment Property:**
```
Minimum down payment: 15-25%
Best rates with: 25%+ down
Typical terms: 15 or 30 years
Interest rates: 0.5-0.75% higher than owner-occupied
Max loan amount: Same conforming limits

Example:
Purchase price: $400,000
Down payment: $100,000 (25%)
Loan amount: $300,000
Rate: 7.5%
Term: 30 years
Monthly P&I: $2,097.55

Pros:
- Fixed long-term rate
- Predictable payment
- Non-recourse in some states

Cons:
- Higher rates than owner-occupied
- Stricter qualification (rental income)
- Limited to 10 financed properties
```

#### FHA Loans

**FHA Characteristics:**
```
Minimum down payment: 3.5%
Credit score: 580+ (500-579 with 10% down)
Max loan amount: Varies by county ($498,257 in many areas)
Upfront MIP: 1.75% of loan amount
Annual MIP: 0.55-0.85% (depending on LTV and term)
Owner-occupied: Required

Multi-family (2-4 units):
Can use FHA for investment if owner-occupied
Rental income can qualify borrower
Higher loan limits (up to $1,396,800 for 4-unit)

Example (house hack):
Purchase: $400,000 (4-unit)
Down payment: $14,000 (3.5%)
Loan: $386,000
Rate: 6.5%
Upfront MIP: $6,755 (added to loan)
Annual MIP: $2,702/year ($225/month)
Monthly P&I: $2,439
Monthly MIP: $225
Total payment: $2,664

Your unit: $1,000/month equivalent
Other 3 units: $1,200/month each = $3,600
Net after your mortgage: $936/month positive cash flow
+ You're living for free
= Effective income increase of $1,936/month

Pros:
- Very low down payment
- Easier credit qualification
- Allows multi-family
- Good for house hacking

Cons:
- MIP required (for life on 30-year loans > 90% LTV)
- Must owner-occupy
- Property condition requirements
- Loan limits
```

#### Commercial Loans

**Portfolio/Commercial Characteristics:**
```
Used for: 5+ units, commercial property
Down payment: 20-30%
Terms: 5-10 years (20-25 year amortization)
Rates: Varies (often SOFR + spread)
Based on: Property cash flow (DSCR), not personal income

Example:
Purchase: $2,000,000 (20-unit apartment)
Down payment: $500,000 (25%)
Loan: $1,500,000
Rate: 7.5%
Term: 10 years (balloon)
Amortization: 25 years
Monthly P&I: $10,989
Balloon payment year 10: $1,232,847

Required DSCR: 1.25x
Required NOI: $10,989 × 12 × 1.25 = $164,835

Pros:
- Based on property, not personal income
- Can finance large properties
- Non-recourse often available

Cons:
- Balloon payment (refinance risk)
- Higher rates
- Strict underwriting on property
- More expensive to obtain
```

### 5.2 Key Loan Metrics

#### Loan-to-Value (LTV)

**Formula:**
```
LTV = Loan Amount ÷ Property Value

Example:
Property value: $400,000
Loan amount: $320,000
LTV = $320,000 ÷ $400,000 = 80%
Down payment: 20%
```

**LTV Guidelines:**
```
Property Type               | Max LTV
----------------------------|----------
Primary residence (conv)    | 97%
Primary residence (FHA)     | 96.5%
Second home                 | 90%
Investment (1-unit)         | 85%
Investment (2-4 units)      | 80%
Investment (5+ units)       | 75%
Commercial                  | 70-75%
```

**Combined LTV (CLTV):**
```
When multiple loans exist:
First mortgage: $320,000
Second mortgage (HELOC): $40,000
Total loans: $360,000
Property value: $400,000

CLTV = $360,000 ÷ $400,000 = 90%
```

#### Debt Service Coverage Ratio (DSCR)

**Formula:**
```
DSCR = Net Operating Income (NOI) ÷ Annual Debt Service

Example:
NOI: $30,000/year
Annual debt service: $25,000/year
DSCR = $30,000 ÷ $25,000 = 1.20
```

**DSCR Interpretation:**
```
DSCR < 1.0: Negative cash flow (doesn't cover debt)
DSCR = 1.0: Break-even (just covers debt)
DSCR 1.0-1.15: Tight cash flow
DSCR 1.15-1.25: Acceptable (typical minimum)
DSCR 1.25-1.35: Good cash flow cushion
DSCR > 1.35: Strong cash flow

Lender Requirements:
Residential (1-4 units): 1.15-1.25
Commercial (5+ units): 1.25-1.30
Higher risk: 1.30-1.40
```

**DSCR Loan Analysis:**
```
Property NOI: $28,000/year
Required DSCR: 1.25
Maximum debt service: $28,000 ÷ 1.25 = $22,400/year

At 7% rate, 30-year amortization:
Maximum loan amount ≈ $336,000

If purchase price is $400,000:
Maximum loan: $336,000
Minimum down payment: $64,000 (16%)
```

#### Debt-to-Income (DTI)

**Formula:**
```
DTI = Total Monthly Debt Payments ÷ Gross Monthly Income

Front-end DTI (housing only):
Housing payment ÷ Gross income

Back-end DTI (all debt):
(Housing + other debt) ÷ Gross income
```

**Example:**
```
Monthly income: $10,000
Proposed mortgage (PITI): $2,500
Car payment: $500
Student loans: $300
Credit cards: $200
Total debt: $3,500

Front-end DTI: $2,500 ÷ $10,000 = 25%
Back-end DTI: $3,500 ÷ $10,000 = 35%
```

**DTI Limits:**
```
Loan Type           | Front-end | Back-end
--------------------|-----------|----------
Conventional        | 28%       | 36%
FHA                 | 31%       | 43%
Investment property | 25%       | 36%
Portfolio lenders   | Varies    | Varies
```

**Investment Property Income:**
```
Rental income can offset DTI:

Gross monthly rent: $3,000
Less: Vacancy (5%): ($150)
Less: Expenses (50%): ($1,500)
Net qualifying income: $1,350

If mortgage is $2,500:
Net impact on DTI: -$1,150 (negative)

Note: Lenders vary on how much rental income they count
- Some: 75% of gross rent
- Some: Net rent from Schedule E
- DSCR loans: Don't use DTI at all (property cash flow only)
```

### 5.3 Tax Strategies

#### Depreciation

**Residential Rental Property:**
```
Depreciation period: 27.5 years
Formula: Building value ÷ 27.5 years

Example:
Purchase price: $400,000
Land value: $80,000 (20%)
Building value: $320,000

Annual depreciation: $320,000 ÷ 27.5 = $11,636

Tax benefit:
Tax bracket: 24%
Tax savings: $11,636 × 0.24 = $2,793/year
```

**Commercial Property:**
```
Depreciation period: 39 years
Formula: Building value ÷ 39 years

Example:
Purchase price: $2,000,000
Land value: $400,000 (20%)
Building value: $1,600,000

Annual depreciation: $1,600,000 ÷ 39 = $41,026

Tax benefit:
Tax bracket: 32%
Tax savings: $41,026 × 0.32 = $13,128/year
```

**Cost Segregation:**
```
Accelerates depreciation by segregating components:

Normal depreciation (27.5 years):
Building: $320,000 over 27.5 years = $11,636/year

Cost segregation study identifies:
5-year property: $60,000 (appliances, carpets)
7-year property: $40,000 (furniture, fixtures)
15-year property: $60,000 (land improvements)
27.5-year property: $160,000 (building structure)

Year 1 depreciation (accelerated):
5-year: $60,000 × 20% = $12,000
7-year: $40,000 × 14.29% = $5,716
15-year: $60,000 × 5% = $3,000
27.5-year: $160,000 ÷ 27.5 = $5,818
Total Year 1: $26,534

vs Normal: $11,636
Extra deduction: $14,898
Tax savings (24%): $3,575 extra in Year 1

Cost seg study cost: $5,000-15,000
Best for: Properties > $1M, higher tax brackets
```

#### 1031 Exchange

**1031 Exchange Basics:**
```
Purpose: Defer capital gains tax by exchanging investment properties

Requirements:
- Both properties must be investment or business use
- Must use qualified intermediary
- Must identify replacement within 45 days
- Must close on replacement within 180 days
- Must purchase equal or greater value
- Must reinvest all equity
```

**1031 Exchange Example:**
```
Sale of Original Property:
Sale price: $600,000
Original purchase: $400,000
Depreciation taken: $60,000
Adjusted basis: $340,000

Capital gain: $600,000 - $340,000 = $260,000

Without 1031:
Capital gains tax (20%): $52,000
Depreciation recapture (25%): $15,000
Net investment tax (3.8%): $9,880
Total tax: $76,880
Net proceeds: $523,120

With 1031:
Tax deferred: $76,880
Full proceeds to reinvest: $600,000

Purchase of Replacement:
Must purchase: $600,000+ (equal or greater)
Must reinvest: All $600,000 equity

Result: No current tax, basis carries forward
```

**1031 Timeline:**
```
Day 0: Close on sale of relinquished property
Day 1-45: Identify replacement property (written)
Day 46-180: Close on replacement property

Identification rules (choose one):
- 3-property rule: Up to 3 properties (any value)
- 200% rule: Any number if total value ≤ 200% of sold
- 95% rule: Any number if acquire 95% of identified value
```

#### Depreciation Recapture

**When You Sell:**
```
Original purchase: $400,000
Land: $80,000
Building: $320,000
Years held: 10 years
Depreciation: $320,000 ÷ 27.5 × 10 = $116,364
Adjusted basis: $400,000 - $116,364 = $283,636

Sale price: $500,000
Capital gain: $500,000 - $283,636 = $216,364

Tax calculation:
Depreciation recapture: $116,364 @ 25% = $29,091
Long-term capital gain: $100,000 @ 20% = $20,000
Net investment tax: $216,364 @ 3.8% = $8,222
Total tax: $57,313

Strategies to defer/minimize:
1. 1031 exchange (defer entirely)
2. Installment sale (spread over years)
3. Opportunity Zone investment
4. Hold until death (heirs get step-up basis)
```

#### Passive Activity Loss Rules

**Passive Loss Limitations:**
```
Real estate rental income is "passive"
Passive losses can only offset passive income

Exception for active participation:
- If AGI < $100,000: Can deduct up to $25,000 losses
- If AGI $100,000-$150,000: Phased out ($1 per $2)
- If AGI > $150,000: No deduction (losses suspended)

Example:
Rental property loss: ($15,000)
W-2 income: $120,000
AGI: $120,000

Phase-out:
$120,000 - $100,000 = $20,000 over
$25,000 - ($20,000 ÷ 2) = $15,000 allowed

Can deduct: $15,000 of the $15,000 loss
Suspended: $0

If AGI was $160,000:
No deduction allowed (fully phased out)
$15,000 loss suspended (carries forward)
```

**Real Estate Professional Status:**
```
If you qualify as real estate professional:
- Losses not subject to passive loss limits
- Can offset W-2 income

Requirements:
1. More than 50% of personal services in real estate
2. More than 750 hours per year in real estate
3. Material participation in each rental activity

Benefits:
Can deduct unlimited rental losses against any income

Example:
Real estate professional with 3 rentals
Total rental loss: ($40,000)
W-2 income: $150,000
Taxable income: $150,000 - $40,000 = $110,000

vs Non-professional:
Taxable income: $150,000 (losses suspended)

Tax savings (24% bracket): $9,600/year
```

#### Deductible Expenses

**Operating Expense Deductions:**
```
Fully deductible in year incurred:

Property management fees
Property taxes
Insurance
Utilities (owner-paid)
Repairs and maintenance
Advertising
Legal and professional fees
Property management software
Travel to inspect property
HOA fees
Pest control
Landscaping
Snow removal
Supplies
```

**Capital Improvements:**
```
Must be depreciated (not immediately deducted):

New roof
HVAC replacement
Major remodel
Addition
Structural repairs
New appliances (> $2,500)

These add to property basis and depreciate over:
- 27.5 years (residential)
- 39 years (commercial)
- 5-7 years if segregated
```

**Repairs vs Improvements:**
```
Repair (deductible):
- Fixes something to original condition
- Examples: Patch roof, fix leak, paint

Improvement (capitalize):
- Adds value, extends life, or adapts to new use
- Examples: New roof, add room, convert to rental

Gray areas (consult CPA):
Replacing kitchen cabinets (improvement)
Replacing broken cabinet door (repair)
Painting entire interior (repair)
Adding new rooms (improvement)
```

### 5.4 Financing Strategy Checklist

**Pre-Purchase Analysis:**
```
[ ] Credit score checked and optimized (720+ ideal)
[ ] Down payment source confirmed
[ ] Closing costs budgeted (2-5% of purchase)
[ ] Cash reserves planned (6-12 months expenses)
[ ] Loan options compared (rate, terms, costs)
[ ] Pre-approval obtained
[ ] DTI calculated and acceptable
[ ] Property DSCR verified (if applicable)
[ ] Financing timeline confirmed
[ ] Backup financing plan if needed
```

**Tax Planning:**
```
[ ] Property allocated between land and building
[ ] Depreciation schedule established
[ ] Cost segregation considered (if > $1M)
[ ] Record keeping system established
[ ] Expense tracking implemented
[ ] CPA/tax professional consulted
[ ] Tax entity structure optimized (LLC, S-corp, etc.)
[ ] Exit strategy tax implications understood
[ ] 1031 exchange possibility considered
```

---

## Appendix: Quick Reference

### Formula Summary

**Valuation:**
```
Price per SF = Sale Price ÷ Square Feet
Cap Rate = NOI ÷ Property Value
Value = NOI ÷ Cap Rate
GRM = Sale Price ÷ Gross Annual Rent
```

**Cash Flow:**
```
Effective Gross Income = Gross Income - Vacancy
NOI = Effective Gross Income - Operating Expenses
Cash Flow = NOI - Debt Service
```

**Returns:**
```
Cash-on-Cash = Annual Cash Flow ÷ Total Cash Invested
ROE = (NOI - Debt Service) ÷ Equity
```

**Financing:**
```
LTV = Loan Amount ÷ Property Value
DSCR = NOI ÷ Annual Debt Service
DTI = Monthly Debt ÷ Monthly Income
```

**Tax:**
```
Annual Depreciation = Building Value ÷ 27.5 years (residential)
Annual Depreciation = Building Value ÷ 39 years (commercial)
```

### Key Benchmarks

**Cash Flow:**
```
Rent/Price Ratio: 0.8-1.0%+ (market dependent)
Operating Expense Ratio: 45-60% of gross income
Cap Rate: 4-10% (varies by property class and market)
Cash-on-Cash Return: 6-12% target
```

**Property Condition:**
```
Roof life: 15-30 years (varies by material)
HVAC life: 10-20 years
Water heater life: 8-12 years
Carpet life: 5-10 years
Paint life: 5-7 years
```

**Market Health:**
```
Months of Inventory: 4-6 = balanced
Vacancy Rate: 4-7% = healthy (multi-family)
Population Growth: 1.5%+ = strong
Job Growth: > national average = strong
```

---

## Best Practices Summary

1. **Always use multiple valuation approaches** when possible (sales comp, income, cost)

2. **Verify all seller-provided financial information** independently

3. **Account for all operating expenses** including reserves (CapEx)

4. **Use conservative assumptions** in projections:
   - Higher vacancy than current (7-10%)
   - Lower rent growth (2-3%)
   - Higher expense growth (3-4%)

5. **Conduct thorough due diligence**:
   - Professional inspection
   - Title review
   - Financial verification
   - Market research

6. **Understand market cycle** position before investing

7. **Plan for taxes** from day one:
   - Proper entity structure
   - Maximize deductions
   - Consider depreciation and future recapture
   - Plan exit strategy (1031, etc.)

8. **Maintain adequate reserves**:
   - Emergency fund: 6-12 months expenses
   - CapEx reserve: 5-10% of income
   - Vacancy reserve: Cover 2-3 months

9. **Know your exit strategy** before buying:
   - Hold period
   - Target returns
   - Market conditions for sale
   - Tax implications

10. **Continue education**:
    - Local market trends
    - Economic indicators
    - Regulatory changes
    - Investment strategies

---

**This skill document is a living reference. Update with market-specific data, personal experience, and lessons learned from each deal.**

---

**End of Real Estate Analysis Skill v1.0.0**
