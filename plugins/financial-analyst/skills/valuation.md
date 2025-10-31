# Valuation Skill

Comprehensive guide to company valuation using DCF, comparable company analysis, precedent transactions, and other valuation methods.

---

## Table of Contents

1. [DCF Valuation](#1-dcf-valuation)
2. [Comparable Company Analysis](#2-comparable-company-analysis)
3. [Precedent Transactions](#3-precedent-transactions)
4. [Other Valuation Methods](#4-other-valuation-methods)

---

## 1. DCF Valuation

Discounted Cash Flow (DCF) analysis values a company based on the present value of its future cash flows. It's considered the most theoretically sound valuation method.

### 1.1 Free Cash Flow Calculation

Free cash flow represents the cash available to all providers of capital (debt and equity).

#### Free Cash Flow to the Firm (FCFF)

FCFF is the cash flow available to all investors (both debt and equity holders).

**Method 1: Starting from EBIT**
```
EBIT (Earnings Before Interest & Tax)
× (1 - Tax Rate)
= NOPAT (Net Operating Profit After Tax)

+ Depreciation & Amortization (non-cash expense)
- Capital Expenditures (cash outflow for PP&E)
- Increase in Net Working Capital (cash tied up)
= Free Cash Flow to Firm (FCFF)
```

**Example:**
```
EBIT:                               $10,000
Tax Rate:                                25%
NOPAT = $10,000 × (1 - 0.25)         $7,500

Depreciation & Amortization:          $2,000
Capital Expenditures:                ($3,000)
Increase in NWC:                       ($500)

FCFF = $7,500 + $2,000 - $3,000 - $500 = $6,000
```

**Method 2: Starting from Net Income**
```
Net Income
+ Interest Expense × (1 - Tax Rate)     [add back after-tax interest]
+ Depreciation & Amortization
- Capital Expenditures
- Increase in Net Working Capital
= Free Cash Flow to Firm (FCFF)
```

**Example:**
```
Net Income:                           $6,750
Interest Expense:                     $1,000
Tax Rate:                                25%
After-tax Interest:                     $750

FCFF = $6,750 + $750 + $2,000 - $3,000 - $500 = $6,000
```

**Method 3: Starting from Operating Cash Flow**
```
Cash Flow from Operations
+ Interest Expense × (1 - Tax Rate)
- Capital Expenditures
= Free Cash Flow to Firm (FCFF)
```

#### Free Cash Flow to Equity (FCFE)

FCFE is the cash flow available only to equity holders, after debt obligations.

**Formula:**
```
Free Cash Flow to Firm (FCFF)
- Interest Expense × (1 - Tax Rate)
- Net Debt Repayment (Repayment - New Borrowing)
= Free Cash Flow to Equity (FCFE)
```

**Or, starting from Net Income:**
```
Net Income
+ Depreciation & Amortization
- Capital Expenditures
- Increase in Net Working Capital
+ Net Borrowing (New Debt - Repayment)
= Free Cash Flow to Equity (FCFE)
```

**Example:**
```
FCFF:                                 $6,000
Interest Expense:                     $1,000
Tax Rate:                                25%
After-tax Interest:                     $750
Debt Repayment:                       $1,500
New Borrowing:                        $1,000
Net Debt Repayment:                     $500

FCFE = $6,000 - $750 - $500 = $4,750
```

#### Components Explained

**1. NOPAT (Net Operating Profit After Tax)**
- Operating profit (EBIT) adjusted for taxes
- Excludes impact of capital structure (interest)
- Represents operating performance after tax

**2. Depreciation & Amortization**
- Non-cash expenses that reduce net income
- Added back because they don't represent cash outflow
- PP&E depreciation and intangible amortization

**3. Capital Expenditures (CapEx)**
- Cash spent on long-term assets (PP&E)
- Maintenance CapEx: Sustain current operations
- Growth CapEx: Support expansion
- Both types reduce free cash flow

**4. Change in Net Working Capital**
```
Net Working Capital = Current Assets - Current Liabilities
(excluding cash and debt)

Components:
  Accounts Receivable
+ Inventory
- Accounts Payable
= Net Working Capital

Change in NWC = Ending NWC - Beginning NWC

If NWC increases: Cash is tied up (negative to FCF)
If NWC decreases: Cash is released (positive to FCF)
```

**Example:**
```
                        Year 1    Year 2    Change
Accounts Receivable      $5,000    $6,000   +$1,000
Inventory                $3,000    $3,500     +$500
Accounts Payable        ($2,000)  ($2,300)    -$300

Net Working Capital      $6,000    $7,200   +$1,200

Increase in NWC of $1,200 is a use of cash (negative to FCF)
```

#### Unlevered vs Levered Cash Flow

**Unlevered Free Cash Flow = FCFF**
- Independent of capital structure
- Used for WACC-based DCF
- Values entire firm (enterprise value)

**Levered Free Cash Flow = FCFE**
- Accounts for debt obligations
- Used for equity cost of capital DCF
- Values equity directly

**When to Use Each:**

Use FCFF when:
- Valuing the entire firm
- Company has changing leverage
- Want to separate operating and financing decisions

Use FCFE when:
- Valuing equity directly
- Stable capital structure
- Focus on equity investor perspective

### 1.2 WACC Calculation

Weighted Average Cost of Capital (WACC) represents the average rate a company pays for its capital.

#### WACC Formula

```
WACC = (E/V) × Cost of Equity + (D/V) × Cost of Debt × (1 - Tax Rate)

Where:
E = Market value of equity
D = Market value of debt
V = E + D (Total value)
E/V = Equity weight
D/V = Debt weight
```

#### Component Calculations

**1. Market Value of Equity (E)**

For public companies:
```
Market Value of Equity = Share Price × Shares Outstanding
```

For private companies:
```
Use most recent valuation or estimated value
Or iterate: Assume equity value, calculate WACC, value company
```

**2. Market Value of Debt (D)**

```
For traded debt: Use market value
For bank debt: Book value ≈ market value (if recent)
Total Debt = Short-term Debt + Long-term Debt
```

Should you include other items?
- Operating leases: Convert to debt equivalent (capitalize)
- Preferred stock: Treat as debt or separate component
- Minority interest: Sometimes included in debt

**3. Cost of Equity**

**Method 1: Capital Asset Pricing Model (CAPM)**
```
Cost of Equity = Risk-Free Rate + Beta × (Market Risk Premium)

Components:
- Risk-Free Rate: 10-year government bond yield
- Beta: Stock volatility relative to market
- Market Risk Premium: Expected market return - risk-free rate
  (typically 5-7%)
```

**Example:**
```
Risk-Free Rate:              4.0%
Beta:                        1.2
Market Risk Premium:         6.0%

Cost of Equity = 4.0% + 1.2 × 6.0% = 11.2%
```

**Finding Beta:**
- Public company: Use historical beta (Bloomberg, Yahoo Finance)
- Private company: Use industry average beta
- Unlever peer betas, then relever to company's capital structure

**Unlevering and Relevering Beta:**
```
Unlevered Beta = Levered Beta / [1 + (1 - Tax Rate) × (D/E)]

Then relever to target company:
Levered Beta = Unlevered Beta × [1 + (1 - Tax Rate) × (D/E)]
```

**Example:**
```
Peer Company:
  Levered Beta:              1.5
  Debt/Equity:               0.5
  Tax Rate:                  25%

Unlevered Beta = 1.5 / [1 + (1 - 0.25) × 0.5] = 1.2

Target Company:
  Debt/Equity:               0.3
  Tax Rate:                  25%

Relevered Beta = 1.2 × [1 + (1 - 0.25) × 0.3] = 1.47
```

**Method 2: Build-Up Method** (for private companies)
```
Cost of Equity = Risk-Free Rate + Equity Risk Premium + Size Premium + Company-Specific Risk

Typical ranges:
- Equity Risk Premium:       5-7%
- Size Premium (small cap):  2-4%
- Company-Specific Risk:     0-5%
```

**4. Cost of Debt**

```
Cost of Debt = Interest Rate on Debt

For multiple debt sources:
Weighted Average Interest Rate = Σ (Debt Amount × Interest Rate) / Total Debt
```

**If no debt currently:**
- Use company's likely borrowing rate
- Based on credit rating or comparable companies
- Add credit spread to risk-free rate

**Credit Spread by Rating:**
```
AAA:     +0.5% to 1.0%
AA:      +1.0% to 1.5%
A:       +1.5% to 2.0%
BBB:     +2.0% to 3.0%
BB:      +3.0% to 5.0%
B:       +5.0% to 7.0%
```

**After-Tax Cost of Debt:**
```
After-Tax Cost of Debt = Pre-Tax Cost × (1 - Tax Rate)

Example:
Pre-Tax Cost:        8.0%
Tax Rate:            25%
After-Tax Cost:      6.0%
```

Interest is tax-deductible, so we use after-tax cost in WACC.

#### WACC Calculation Example

```
INPUTS:
Market Value of Equity:      $500M
Market Value of Debt:        $200M
Total Value (V):             $700M

Equity Weight (E/V):         71.4%
Debt Weight (D/V):           28.6%

Cost of Equity:              11.2%
Pre-Tax Cost of Debt:        7.0%
Tax Rate:                    25%
After-Tax Cost of Debt:      5.25%

WACC CALCULATION:
WACC = (71.4% × 11.2%) + (28.6% × 5.25%)
WACC = 8.0% + 1.5%
WACC = 9.5%
```

#### WACC Considerations

**Capital Structure Weights:**
- Use market values, not book values
- Use target capital structure, not current (if temporary)
- Consider industry norms

**Adjustments:**
- Adjust WACC for different business segments
- Use project-specific WACC for project valuation
- Consider time-varying WACC for changing leverage

**Common Ranges by Industry:**
```
Technology (software):       8-12%
Consumer products:           7-10%
Utilities:                   5-8%
Healthcare:                  8-11%
Financial services:          9-13%
```

### 1.3 Terminal Value

Terminal value represents the value of all cash flows beyond the explicit forecast period. It typically represents 60-80% of total DCF value.

#### Method 1: Perpetuity Growth Method

Assumes cash flows grow at a constant rate forever.

**Formula:**
```
Terminal Value = FCF(final year) × (1 + g) / (WACC - g)

Where:
FCF(final year) = Free cash flow in the last forecast year
g = Perpetual growth rate
WACC = Discount rate
```

**Example:**
```
Year 5 FCF:                  $10,000
Perpetual Growth Rate:       2.5%
WACC:                        9.5%

Terminal Value = $10,000 × (1.025) / (0.095 - 0.025)
Terminal Value = $10,250 / 0.070
Terminal Value = $146,429
```

**Choosing Growth Rate (g):**

Guidelines:
- Long-term GDP growth rate: 2-3%
- Industry growth rate (if slower than GDP)
- Inflation rate: 2-2.5%
- Never exceed GDP growth long-term

**Important:**
- g must be less than WACC (otherwise formula breaks)
- Small changes in g have large impact on value
- Be conservative; justify your assumption

**Sensitivity:**
```
Growth Rate     Terminal Value    % Change
    1.5%           $125,000          -15%
    2.0%           $136,667           -7%
    2.5%           $146,429         Base
    3.0%           $157,692          +8%
    3.5%           $170,833          +17%
```

#### Method 2: Exit Multiple Method

Values the company based on a trading multiple at the end of the forecast period.

**Formula:**
```
Terminal Value = Financial Metric(final year) × Exit Multiple

Common Metrics:
- EV/EBITDA
- EV/Revenue
- P/E
```

**Example:**
```
Year 5 EBITDA:               $25,000
Exit EV/EBITDA Multiple:     8.0x

Terminal Value = $25,000 × 8.0 = $200,000
```

**Choosing Exit Multiple:**

Sources:
1. Current trading multiples of comparable companies
2. Historical average multiples for the industry
3. Recent transaction multiples
4. Typically use a conservative multiple (midpoint or lower)

**Example Multiples by Industry:**
```
SaaS Software:          EV/Revenue: 5-10x, EV/EBITDA: 15-25x
Manufacturing:          EV/Revenue: 0.5-2x, EV/EBITDA: 6-10x
Healthcare Services:    EV/Revenue: 1-3x, EV/EBITDA: 8-12x
Consumer Products:      EV/Revenue: 1-3x, EV/EBITDA: 10-15x
```

**Considerations:**
- Ensure metric is normalized (not artificially high/low in final year)
- Consider where company will be in lifecycle (mature = lower multiple)
- Account for market conditions (don't use peak multiples)

#### Comparing Methods

**Perpetuity Growth Method:**
- More theoretically sound
- Good when growth is predictable
- Sensitive to growth rate assumption
- Better for mature, stable companies

**Exit Multiple Method:**
- Easier to explain and understand
- Market-based (reflects investor views)
- Sensitive to multiple selection
- Good when comparable data available
- Better for high-growth companies

**Best Practice:**
Use both methods and compare results:
```
Perpetuity Growth Terminal Value:    $146,429
Exit Multiple Terminal Value:        $200,000
Average:                             $173,215
```

Or create scenarios:
```
                    Low Case    Base Case    High Case
Perpetuity Growth    $125,000    $146,429     $170,833
Exit Multiple        $175,000    $200,000     $225,000
```

#### Terminal Value in the DCF

Terminal value must be discounted to present value:

```
PV of Terminal Value = Terminal Value / (1 + WACC)^n

Where n = number of years to terminal year
```

**Example:**
```
Terminal Value (Year 5):     $146,429
WACC:                        9.5%
Discount Period:             5 years

PV of Terminal Value = $146,429 / (1.095)^5
PV of Terminal Value = $146,429 / 1.574
PV of Terminal Value = $93,000
```

### 1.4 NPV Calculation

Net Present Value brings all cash flows to present value and sums them.

#### Step-by-Step DCF Calculation

**Step 1: Project Free Cash Flows**

```
                        Year 1  Year 2  Year 3  Year 4  Year 5
EBIT                    $8,000  $9,500 $11,000 $12,800 $14,500
Tax Rate                   25%     25%     25%     25%     25%
NOPAT                   $6,000  $7,125  $8,250  $9,600 $10,875

+ D&A                   $2,000  $2,200  $2,400  $2,600  $2,800
- CapEx                ($3,500)($3,800)($4,000)($4,200)($4,400)
- Increase in NWC        ($500)  ($600)  ($650)  ($700)  ($750)

Free Cash Flow          $4,000  $5,025  $6,000  $7,300  $8,525
```

**Step 2: Calculate Terminal Value**

```
Using Perpetuity Growth Method:
Year 5 FCF:              $8,525
Growth Rate:             2.5%
WACC:                    9.5%

Terminal Value = $8,525 × 1.025 / (0.095 - 0.025)
Terminal Value = $8,738 / 0.070
Terminal Value = $124,831
```

**Step 3: Discount Cash Flows**

```
                        Year 1  Year 2  Year 3  Year 4  Year 5
Free Cash Flow          $4,000  $5,025  $6,000  $7,300  $8,525
Terminal Value                                          $124,831
Total Cash Flow         $4,000  $5,025  $6,000  $7,300 $133,356

Discount Factor @ 9.5%:
  (1/(1+WACC)^year)      0.913   0.834   0.762   0.696   0.636

Present Value           $3,652  $4,191  $4,572  $5,081  $84,814
```

**Step 4: Sum to Enterprise Value**

```
PV of Forecast Period FCF:
  Year 1:                $3,652
  Year 2:                $4,191
  Year 3:                $4,572
  Year 4:                $5,081
  Year 5:                $5,421    [FCF only, not including TV]
  Total:                $22,917

PV of Terminal Value:   $79,393   [TV of $124,831 discounted]

Enterprise Value:      $102,310
```

**Step 5: Calculate Equity Value**

```
Enterprise Value:              $102,310
+ Cash and Cash Equivalents:     $5,000
- Total Debt:                  ($20,000)
- Minority Interest:               ($500)
+ Investments:                    $2,000

Equity Value:                   $88,810
```

**Step 6: Per Share Value**

```
Equity Value:           $88,810
÷ Shares Outstanding:    10,000

Value per Share:         $8.88
```

#### DCF Model Template

```
DCF VALUATION MODEL
===================

FORECAST PERIOD                Year 1  Year 2  Year 3  Year 4  Year 5
Revenue                       $50,000 $57,500 $66,125 $76,044 $87,450
EBIT                           $8,000  $9,500 $11,000 $12,800 $14,500
NOPAT                          $6,000  $7,125  $8,250  $9,600 $10,875
+ D&A                          $2,000  $2,200  $2,400  $2,600  $2,800
- CapEx                       ($3,500)($3,800)($4,000)($4,200)($4,400)
- Increase in NWC               ($500)  ($600)  ($650)  ($700)  ($750)
Free Cash Flow                 $4,000  $4,925  $6,000  $7,300  $8,525

TERMINAL VALUE (Year 5)
Method: Perpetuity Growth
  Year 5 FCF:                  $8,525
  Growth Rate:                   2.5%
  WACC:                          9.5%
Terminal Value:              $124,831

DISCOUNTED CASH FLOW
WACC:                            9.5%

                               Year 1  Year 2  Year 3  Year 4  Year 5
Free Cash Flow                 $4,000  $4,925  $6,000  $7,300  $8,525
Terminal Value                                                $124,831
Total Cash Flow                $4,000  $4,925  $6,000  $7,300 $133,356
Discount Factor                 0.913   0.834   0.762   0.696   0.636
Present Value                  $3,652  $4,107  $4,572  $5,081  $84,814

Present Value of FCF:         $22,326
Present Value of TV:           $79,393
Enterprise Value:             $101,719

Plus: Cash:                     $5,000
Less: Debt:                   ($20,000)
Less: Minority Interest:         ($500)
Equity Value:                  $86,219

Shares Outstanding:            10,000
Value per Share:                $8.62
```

#### Sensitivity Analysis

Create tables to show impact of key assumptions:

**Two-Way: WACC vs Growth Rate**
```
                    Perpetual Growth Rate
WACC        1.5%      2.0%      2.5%      3.0%      3.5%
8.5%     $92,857  $100,000  $108,333  $118,182  $130,000
9.0%     $86,667   $93,333  $101,250  $110,714  $122,143
9.5%     $81,081   $87,097   $94,118  $102,439  $112,500  <- Base
10.0%    $76,000   $81,579   $87,838   $95,000  $103,333
10.5%    $71,333   $76,667   $82,353   $88,571   $95,652
```

**One-Way: Exit Multiple**
```
Exit EV/EBITDA     Terminal Value    Equity Value/Share
    6.0x              $150,000              $7.85
    7.0x              $175,000              $8.35
    8.0x              $200,000              $8.85  <- Base
    9.0x              $225,000              $9.35
   10.0x              $250,000              $9.85
```

#### Common DCF Pitfalls

**1. Terminal Value Issues:**
- Growth rate too high (exceeds GDP)
- Exit multiple too high (peak multiples)
- Terminal value as % of total value >80%

**2. Forecast Period:**
- Too short (doesn't reach steady state)
- Too long (low visibility, low accuracy)
- Optimal: 5-10 years

**3. Working Capital:**
- Forgetting to project NWC changes
- Using wrong sign (increase is negative to FCF)
- Ignoring cash conversion cycle

**4. Capital Structure:**
- Using book values instead of market values
- Not adjusting for changing leverage
- Incorrect tax rate on cost of debt

**5. WACC Issues:**
- Beta from wrong peer group
- Stale risk-free rate
- Market risk premium too high/low
- Using wrong weights

---

## 2. Comparable Company Analysis

Comparable company analysis (Comps) values a company based on how similar companies are valued by the market.

### 2.1 Trading Multiples

Multiples express value relative to a financial metric. They enable quick comparison across companies.

#### Enterprise Value Multiples

**EV/EBITDA**

Most common multiple for most industries.

```
EV/EBITDA = Enterprise Value / EBITDA

Where:
Enterprise Value = Market Cap + Debt - Cash + Minority Interest - Investments

EBITDA = Earnings Before Interest, Tax, Depreciation, Amortization
```

**Why EV/EBITDA?**
- Capital structure neutral (EV includes debt)
- Excludes non-cash charges (D&A)
- Easy to calculate
- Useful even for unprofitable companies (if EBITDA positive)
- Widely used and understood

**Limitations:**
- Ignores CapEx differences
- Can be manipulated (non-recurring adjustments)
- Not meaningful if EBITDA is negative

**Example Calculation:**
```
Company A:
  Share Price:              $50
  Shares Outstanding:       100M
  Market Cap:               $5,000M

  Debt:                     $1,500M
  Cash:                       $500M
  Enterprise Value:         $6,000M

  EBITDA (LTM):               $750M
  EV/EBITDA:                8.0x

Company B:
  Enterprise Value:         $4,500M
  EBITDA:                     $500M
  EV/EBITDA:                9.0x
```

**EV/Revenue**

Used when EBITDA is negative (early-stage companies) or for high-growth companies.

```
EV/Revenue = Enterprise Value / Revenue

Also called: EV/Sales, Price-to-Sales (P/S) multiple
```

**When to use:**
- Pre-profitability companies (startups)
- High-growth SaaS companies
- Revenue visibility is high
- Profitability margins expected to normalize

**Limitations:**
- Ignores profitability entirely
- Companies with different margins not comparable
- Can result in very high multiples

**Example by Industry:**
```
Industry                    Typical EV/Revenue
SaaS (high growth):         5-15x
SaaS (mature):              3-8x
E-commerce:                 1-4x
Manufacturing:              0.5-2x
Consumer Products:          1-3x
```

**EV/EBIT**

Similar to EV/EBITDA but includes depreciation.

```
EV/EBIT = Enterprise Value / EBIT

Where EBIT = EBITDA - Depreciation & Amortization
```

**When to use:**
- Capital-intensive industries (manufacturing, telecom)
- When D&A is significant
- Provides more conservative multiple than EV/EBITDA

**EV/Invested Capital**

Used for capital-intensive businesses or financial services.

```
EV/Invested Capital = Enterprise Value / Invested Capital

Where:
Invested Capital = Equity + Debt + Minority Interest - Cash
                 = Total Assets - Non-Interest-Bearing Liabilities
```

#### Equity Value Multiples

**P/E (Price-to-Earnings)**

Most widely known equity multiple.

```
P/E = Share Price / Earnings per Share (EPS)

Or:
P/E = Market Cap / Net Income
```

**Variations:**

**Trailing P/E:**
```
Based on last 12 months (LTM) earnings
```

**Forward P/E:**
```
Based on next 12 months (NTM) projected earnings
Usually lower than trailing (if company growing)
```

**Why P/E?**
- Simple and intuitive
- Widely available
- Long history of data
- Equity investor perspective

**Limitations:**
- Affected by capital structure (leverage)
- Can be distorted by one-time items
- Negative when earnings are negative
- Varies with accounting policies

**Example:**
```
Company:
  Share Price:              $50
  Shares Outstanding:       100M
  Market Cap:               $5,000M
  Net Income:                 $250M
  EPS:                      $2.50
  P/E:                      20.0x

Industry Average P/E:       18.0x
(Company trades at premium to peers)
```

**PEG Ratio (P/E to Growth)**

Adjusts P/E for growth rate.

```
PEG = P/E / Earnings Growth Rate (%)

Example:
  P/E:                      20.0x
  Expected EPS Growth:        25%
  PEG:                      0.80

Interpretation:
  PEG < 1.0: Potentially undervalued
  PEG > 1.0: Potentially overvalued
```

**P/B (Price-to-Book)**

Compares market value to book value of equity.

```
P/B = Share Price / Book Value per Share

Or:
P/B = Market Cap / Shareholders' Equity
```

**When to use:**
- Financial services (banks, insurance)
- Asset-heavy businesses
- Distressed situations

**Limitations:**
- Book value may not reflect economic value
- Intangible-heavy businesses (tech) have low book value
- Accounting policies affect book value

**Example:**
```
Bank:
  Market Cap:               $5,000M
  Shareholders' Equity:     $3,500M
  P/B:                      1.43x

Interpretation: Trading at 43% premium to book value
```

### 2.2 Selecting Comparables

The quality of comps analysis depends entirely on selecting appropriate peer companies.

#### Selection Criteria

**1. Industry and Business Model**

Most important criterion:
- Same industry (SIC/NAICS codes)
- Similar business model
- Similar value proposition

**Example - SaaS Company:**
Good comps:
- Other SaaS companies
- Similar end-markets (e.g., marketing SaaS)
- Comparable delivery model

Bad comps:
- On-premise software companies
- Hardware companies
- Professional services

**2. Size**

Companies of similar scale:
- Revenue within 0.5x - 2x of target
- Market cap comparable
- Similar operations scale

**Why size matters:**
- Different growth trajectories
- Different margin profiles
- Different access to capital
- Different valuation multiples

**Example:**
```
Target Company Revenue: $500M

Good Size Range:
  Lower bound:          $250M
  Upper bound:          $1,000M

Avoid:
  Too small:            $50M (much higher growth, different stage)
  Too large:            $10B (mature, lower growth, different scale)
```

**3. Growth Profile**

Similar growth rates and trajectories:
- Revenue growth rate
- Earnings growth rate
- Stage of lifecycle (startup, growth, mature)

**4. Profitability**

Similar margin profiles:
- Gross margin
- EBITDA margin
- Net margin
- Path to profitability (if pre-profitable)

**5. Geography**

- Domestic vs international
- Mature vs emerging markets
- Currency considerations

**6. Other Factors**

- Public vs private (liquidity premium)
- Diversification (pure-play vs conglomerate)
- Management quality
- Competitive position

#### Building a Comps Universe

**Step 1: Cast a Wide Net**

Start with 15-25 potential comparables:
- Industry databases
- Stock screeners
- Analyst reports
- Trade associations
- Investment bank comps

**Step 2: Screen for Key Criteria**

Apply filters:
```
Initial Universe:         25 companies

Filter 1 - Industry:      18 companies remain
Filter 2 - Size:          12 companies remain
Filter 3 - Geography:     10 companies remain
Filter 4 - Public/Liquid:  8 companies remain
```

**Step 3: Rank by Similarity**

Create scoring system:
```
Criteria               Weight    Score 1-5    Weighted Score
Industry/Business       30%         5            1.50
Size                    25%         4            1.00
Growth                  20%         5            1.00
Profitability          15%         3            0.45
Geography              10%         4            0.40
Total                  100%                     4.35
```

**Step 4: Select Final Comps Set**

Typically 5-10 companies:
- Include most similar companies
- Ensure diversity (avoid concentration)
- Exclude outliers
- Document why excluded

**Example Comps Set:**

```
Target: Mid-market B2B SaaS company, $300M revenue, 30% growth

Comparable Companies:
1. Company A: CRM SaaS, $250M revenue, 35% growth
2. Company B: Marketing SaaS, $400M revenue, 28% growth
3. Company C: HR SaaS, $350M revenue, 32% growth
4. Company D: Sales SaaS, $280M revenue, 29% growth
5. Company E: Analytics SaaS, $320M revenue, 31% growth

Excluded:
- Company F: Too large ($2B revenue)
- Company G: Different model (on-premise)
- Company H: Outlier multiple (merger pending)
```

### 2.3 Adjustments and Normalization

Raw multiples often need adjustment to ensure true comparability.

#### Financial Statement Adjustments

**1. Non-Recurring Items**

Remove one-time events:
- Restructuring charges
- Litigation settlements
- Asset impairments
- Gains/losses on asset sales
- Acquisition-related costs

**Example:**
```
Reported EBITDA:        $80M
  + Restructuring:       $5M
  + Litigation:          $3M
Adjusted EBITDA:        $88M

Reported EV/EBITDA:     10.0x
Adjusted EV/EBITDA:      9.1x  (lower, more comparable)
```

**2. Stock-Based Compensation (SBC)**

Treatment of SBC varies:

**Approach A: Add back to EBITDA** (most aggressive)
```
Reported EBITDA:        $80M
  + SBC:                $10M
Adjusted EBITDA:        $90M
```

**Approach B: Subtract from EBITDA** (most conservative)
```
Reported EBITDA:        $80M
  No adjustment
Cash EBITDA:            $80M
```

**Approach C: Adjust equity value** (middle ground)
```
Keep EBITDA as reported, but account for dilution:
  Fully diluted shares = Basic shares + Options/RSUs
```

**Best practice:** Be consistent across all comps.

**3. Operating Leases**

Under new accounting standards (ASC 842/IFRS 16), most leases are capitalized. For older data:

```
Convert operating leases to debt equivalent:
  Operating Lease Debt = Annual Rent / Discount Rate

Add to enterprise value:
  Adjusted EV = EV + Operating Lease Debt
```

**4. Pension and Post-Retirement Benefits**

Adjust for under/overfunded pensions:
```
If pension is underfunded:
  Add unfunded liability to EV

If pension is overfunded:
  Subtract overfunded amount from EV
```

#### Fiscal Year and Timing Adjustments

**Fiscal Year Differences**

Ensure all multiples are on same time basis:
```
Company A: December fiscal year-end
Company B: June fiscal year-end (6 months out of sync)

Solution:
- Use calendar year data for both
- Or adjust B's data to calendar year basis
```

**LTM vs NTM**

**Last Twelve Months (LTM):**
- Most recent 12 months of actual results
- Based on reality, not projections
- More reliable

**Next Twelve Months (NTM):**
- Forward-looking projections
- Accounts for expected growth
- Subject to forecast risk

**Best practice:**
Show both and ensure all comps use same basis:
```
                    LTM Multiple    NTM Multiple
Company A               8.5x            7.2x
Company B               9.0x            7.5x
Company C               8.8x            7.4x
Average                 8.8x            7.4x
```

#### Adjustments for Capital Structure

**1. Cash Adjustment**

**Excess Cash:**
Cash beyond operating needs should be added to equity value:
```
Operating Cash Needed:  $20M (e.g., 1 month of revenue)
Total Cash:             $100M
Excess Cash:            $80M

Enterprise Value:       $500M
Add: Excess Cash:       $80M
Adjusted Equity Value:  $580M
```

**2. Debt Adjustments**

Include all debt-like obligations:
- Bank debt
- Bonds
- Capital leases
- Operating leases (debt equivalent)
- Pension obligations
- Preferred stock

**3. Minority Interest**

If parent company owns <100% of subsidiary:
```
Enterprise Value includes 100% of consolidated sub
But equity value should exclude minority interest

Equity Value = EV - Debt + Cash - Minority Interest
```

#### Statistical Adjustments

**Dealing with Outliers**

**Method 1: Exclude extreme outliers**
```
Multiples: 6.5x, 7.2x, 7.8x, 8.0x, 8.3x, 8.5x, 15.0x

Exclude 15.0x (potential merger, unusual situation)
Use range: 6.5x - 8.5x
```

**Method 2: Use median instead of mean**
```
Multiples: 6.5x, 7.2x, 7.8x, 8.0x, 8.3x, 8.5x, 15.0x

Mean:   8.8x (skewed by outlier)
Median: 8.0x (not affected by outlier)

Median is more robust.
```

**Method 3: Interquartile range**
```
Sort multiples and remove top and bottom quartile
Use middle 50% of data
```

#### Comps Analysis Output Table

```
COMPARABLE COMPANY ANALYSIS

Company       Market    Enter-    LTM      LTM     LTM    NTM     Rev    EBITDA
              Cap       prise    Revenue  EBITDA  EV/Rev EV/EBITDA Growth Margin
              ($M)      Value    ($M)     ($M)

Company A     $2,500    $2,800   $450     $110    6.2x    25.5x   28%    24.4%
Company B     $3,200    $3,500   $520     $125    6.7x    28.0x   32%    24.0%
Company C     $2,100    $2,300   $380     $95     6.1x    24.2x   25%    25.0%
Company D     $2,800    $3,100   $480     $115    6.5x    27.0x   30%    24.0%
Company E     $2,400    $2,650   $420     $105    6.3x    25.2x   27%    25.0%

Average       $2,600    $2,870   $450     $110    6.4x    26.0x   28%    24.5%
Median        $2,500    $2,800   $450     $110    6.3x    25.5x   28%    24.4%

Target Co     ???       ???      $400     $100    ???     ???     29%    25.0%

IMPLIED VALUATION (based on comps average):
  EV/Revenue:     $400M × 6.4x = $2,560M EV
  EV/EBITDA:      $100M × 26.0x = $2,600M EV

  Average EV:                     $2,580M
  Less: Debt                        ($300M)
  Plus: Cash                         $150M
  Equity Value:                    $2,430M

  Shares Outstanding:               100M
  Implied Price/Share:             $24.30
```

---

## 3. Precedent Transactions

Precedent transaction analysis values a company based on prices paid in M&A transactions for similar companies.

### 3.1 Transaction Multiples

Same multiples as comps analysis, but based on acquisition prices rather than trading prices.

#### Transaction Value vs Enterprise Value

**Transaction Value = Purchase Price for Acquired Company**

```
Transaction Value = Enterprise Value + Control Premium

Control Premium = Transaction Value - Pre-Announcement EV
                  (as % of pre-announcement EV)
```

**Example:**
```
Target Company (pre-announcement):
  Share Price:          $40
  Shares:               50M
  Market Cap:           $2,000M
  Plus: Debt:           $500M
  Less: Cash:           ($200M)
  Enterprise Value:     $2,300M

Acquisition Terms:
  Price per Share:      $50
  Transaction Value:    $2,500M (equity)
  Plus: Debt Assumed:   $500M
  Less: Cash Acquired:  ($200M)
  Transaction EV:       $2,800M

Control Premium:
  = ($2,800M - $2,300M) / $2,300M
  = 21.7%
```

#### Key Transaction Multiples

**EV/Revenue**
```
Transaction EV / LTM Revenue

Example:
  Transaction EV:       $2,800M
  LTM Revenue:          $500M
  EV/Revenue:           5.6x
```

**EV/EBITDA**
```
Transaction EV / LTM EBITDA

Example:
  Transaction EV:       $2,800M
  LTM EBITDA:           $100M
  EV/EBITDA:            28.0x
```

**Transaction multiples are typically higher than trading multiples due to control premium and synergies.**

### 3.2 Control Premiums

Control premium is the amount an acquirer pays above market price to gain control of the target.

#### Typical Control Premiums

**By Industry:**
```
Technology:             25-40%
Healthcare:             20-35%
Financial Services:     15-30%
Consumer Products:      20-30%
Industrial:             15-25%

Overall Average:        25-35%
```

**Components of Control Premium:**

**1. Synergies**
- Revenue synergies (cross-selling, market expansion)
- Cost synergies (elimination of redundancies)
- Financial synergies (tax benefits, lower cost of capital)

**2. Strategic Value**
- Eliminate competitor
- Acquire technology/IP
- Enter new market
- Acquire talent

**3. Control Rights**
- Change management
- Strategic direction
- Asset deployment
- Dividend policy

#### Calculating Control Premium

**Method 1: Based on Pre-Announcement Price**
```
Control Premium = (Offer Price - Pre-Announcement Price) / Pre-Announcement Price

Example:
  Pre-Announcement:     $40
  Offer Price:          $50
  Control Premium:      25%
```

**Method 2: Based on 1-Week Average**

Use average stock price 1 week before announcement to avoid information leakage:
```
1-Week Avg Price:       $38
Offer Price:            $50
Control Premium:        31.6%
```

**Method 3: Based on Unaffected Price**

Use price before any M&A rumors:
```
Unaffected Price:       $36
Offer Price:            $50
Control Premium:        38.9%
```

### 3.3 Deal Screening

Not all transactions are relevant comparables. Screen carefully.

#### Screening Criteria

**1. Timeframe**

Use recent transactions:
- Last 3-5 years preferred
- Adjust for market conditions if using older deals
- Consider market cycle (bull vs bear market)

**2. Deal Size**

Similar transaction size:
```
Target Company EV:      $2,500M

Relevant Range:
  Minimum:              $1,000M
  Maximum:              $5,000M

Exclude:
  Too small:            $100M (different buyer pool)
  Too large:            $25B (mega-deals, different dynamics)
```

**3. Industry Similarity**

Same criteria as comps analysis:
- Same industry
- Similar business model
- Comparable characteristics

**4. Deal Structure**

**Consider:**
- Cash vs stock
- Friendly vs hostile
- Financial vs strategic buyer
- Public vs private target

**Different structures can affect multiples:**
```
Cash Deal:              Higher multiples (certainty of value)
Stock Deal:             Lower multiples (market risk)
Strategic Buyer:        Higher multiples (synergies)
Financial Buyer:        Lower multiples (standalone value)
```

**5. Deal Status**

**Use only:**
- Completed transactions
- Announced and pending (if likely to close)

**Exclude:**
- Rumored/speculative
- Terminated deals
- Distressed sales (unless relevant)

**6. Geographic Considerations**

- Domestic vs cross-border
- Regulatory environment
- Tax considerations

#### Building Precedent Transaction Set

**Example: B2B SaaS Company**

```
PRECEDENT TRANSACTIONS

Date    Target         Acquirer       Trans      LTM      LTM    EV/   EV/    Control
                                      EV($M)     Rev($M)  EBITDA Rev   EBITDA Premium

Q2'23   SalesTech Co   Oracle         $3,200     $550     $130   5.8x  24.6x   28%
Q4'22   MarketPro      Salesforce     $2,800     $480     $110   5.8x  25.5x   32%
Q1'23   Analytics Inc  Adobe          $3,500     $620     $145   5.6x  24.1x   25%
Q3'22   HR Systems     Workday        $2,400     $420     $95    5.7x  25.3x   30%
Q2'22   CustomSoft     Microsoft      $4,200     $750     $165   5.6x  25.5x   27%

Average                               $3,220     $564     $129   5.7x  25.0x   28%
Median                                $3,200     $550     $130   5.7x  25.3x   28%

Target Company                        ???        $400     $100   ???   ???     ???

IMPLIED VALUATION (based on transaction medians):
  EV/Revenue:    $400M × 5.7x = $2,280M
  EV/EBITDA:     $100M × 25.3x = $2,530M

  Average Transaction EV:         $2,405M
  Less: Debt                        ($300M)
  Plus: Cash                         $150M
  Implied Equity Value:            $2,255M
```

#### Adjusting for Market Conditions

**Market Condition Impact on Multiples:**

```
Multiples by Market Period:

                    2019-2020   2021-2022   2023-2024
                    (Pre-COVID) (Bull)      (Correction)
EV/Revenue              4.5x        7.5x        5.2x
EV/EBITDA              18.0x       28.0x       22.0x

If using 2021-2022 transactions for 2024 valuation:
  Adjust downward by ~30% to reflect market correction
```

**Considerations:**
- Interest rate environment
- M&A market activity level
- Sector-specific trends
- Economic outlook

#### Precedent Transactions Caveats

**Limitations:**

1. **Limited Sample Size**
   - Fewer relevant transactions than trading comps
   - May lack recent data

2. **Data Quality**
   - Private company financials often unavailable
   - Must rely on estimates or disclosed data
   - Adjustments unknown

3. **Synergy Premium**
   - Multiples include buyer-specific synergies
   - May not apply to your situation
   - Strategic vs financial buyer differences

4. **Timing Issues**
   - Market conditions change
   - Stale data less relevant

**Best Practice:**
- Use precedent transactions as one data point
- Combine with trading comps and DCF
- Apply judgment based on current context

---

## 4. Other Valuation Methods

### 4.1 Asset-Based Valuation

Values company based on its assets, used primarily for asset-heavy businesses or liquidation scenarios.

#### Book Value Method

**Net Asset Value = Total Assets - Total Liabilities**

Simply uses balance sheet carrying values.

**Example:**
```
Total Assets:           $10,000M
Total Liabilities:       $6,000M
Net Asset Value:         $4,000M

Shares Outstanding:      100M
Book Value per Share:    $40
```

**When to use:**
- Financial institutions (banks, insurance)
- Holding companies
- Investment funds
- Distressed/bankruptcy situations

**Limitations:**
- Historical cost, not current value
- Ignores intangibles (brand, customers)
- Doesn't reflect earning power
- Depreciation policies vary

#### Adjusted Book Value

Adjust book values to fair market values.

**Common Adjustments:**

**1. Real Estate:**
```
Carried at historical cost:     $500M
Current market value:           $800M
Adjustment:                    +$300M
```

**2. Inventory:**
```
FIFO book value:                $200M
Current replacement cost:       $230M
Adjustment:                     +$30M
```

**3. Intangibles:**
```
Unrecorded brand value:         +$100M
Unrecorded customer relationships: +$50M
```

**4. Liabilities:**
```
Pension unfunded liability:     -$75M
Environmental remediation:      -$25M
```

**Example:**
```
Book Equity:                    $4,000M

Adjustments:
  Real estate mark-to-market:    +$300M
  Inventory LIFO reserve:         +$30M
  Unrecorded intangibles:        +$150M
  Unfunded pension:               -$75M
  Environmental liabilities:      -$25M

Adjusted Net Asset Value:       $4,380M
```

#### Liquidation Value

Values company assuming assets are sold and liabilities paid off.

**Formula:**
```
Liquidation Value = Σ (Asset × Recovery %) - Liabilities - Liquidation Costs

Recovery % varies by asset type:
  Cash:                     100%
  Marketable securities:    95-100%
  Accounts receivable:      70-90%
  Inventory:                50-80%
  PP&E:                     30-70%
  Intangibles:              0-20%
```

**Example:**
```
Assets:
  Cash:               $100M × 100% = $100M
  AR:                 $200M × 80%  = $160M
  Inventory:          $150M × 60%  = $90M
  PP&E:               $500M × 50%  = $250M
  Total Recovery:                   $600M

Less:
  Liabilities:                      $400M
  Liquidation costs:                $50M

Liquidation Value:                  $150M
```

**When to use:**
- Bankruptcy/distressed situations
- Asset-rich, earnings-poor companies
- Provides floor value

### 4.2 LBO Analysis Basics

Leveraged Buyout analysis determines what a financial sponsor (private equity firm) would pay.

#### LBO Valuation Approach

**Concept:**
PE firm uses leverage to purchase company, improves operations, then sells (5-7 years) for profit.

**Target Returns:**
- 20-25% IRR
- 2-3x Money Multiple (MOIC)

#### LBO Valuation Steps

**Step 1: Determine Exit Value**

```
Year 5 EBITDA:                  $150M
Exit Multiple:                  8.0x
Exit Enterprise Value:          $1,200M
```

**Step 2: Calculate Required Equity Return**

```
Exit EV:                        $1,200M
Less: Remaining Debt:             ($200M)
Exit Equity Value:              $1,000M

Target IRR:                     25%
Years:                          5

Required Equity Investment = Exit Equity / (1 + IRR)^Years
Required Equity Investment = $1,000M / (1.25)^5
Required Equity Investment = $1,000M / 3.05
Required Equity Investment = $328M
```

**Step 3: Calculate Purchase Price**

```
Assuming Debt/Equity = 60%/40%:

Equity:                         $328M (40%)
Debt:                           $492M (60%)
Total Purchase Price:           $820M
```

**Step 4: Implied Entry Multiple**

```
Purchase Price:                 $820M
Current EBITDA:                 $100M
Entry EV/EBITDA:                8.2x
```

**Key LBO Valuation Drivers:**

1. **Entry Multiple**: Lower is better for PE firm
2. **EBITDA Growth**: Organic growth + margin improvement
3. **Leverage**: Higher debt increases returns (and risk)
4. **Exit Multiple**: Higher exit multiple increases returns
5. **Debt Paydown**: Deleveraging creates equity value

#### LBO Valuation Model

```
LBO VALUATION MODEL

TRANSACTION ASSUMPTIONS
Entry EV/EBITDA:                8.0x
Current EBITDA:                 $100M
Entry Enterprise Value:         $800M

Debt/Equity Split:              60%/40%
Debt:                           $480M
Equity Investment:              $320M

OPERATING ASSUMPTIONS
Revenue CAGR:                   12%
EBITDA Margin Improvement:      100 bps/year
Current Margin:                 20%
Year 5 Margin:                  24%

DEBT ASSUMPTIONS
Interest Rate:                  6%
Annual Debt Paydown:            $50M

PROJECTIONS
                    Year 0  Year 1  Year 2  Year 3  Year 4  Year 5
Revenue              $500    $560    $627    $702    $787    $881
EBITDA               $100    $117    $137    $159    $183    $211
Margin                20%     21%     22%     23%     23%     24%

Debt Balance         $480    $430    $380    $330    $280    $230
Interest Expense      $29     $26     $23     $20     $17     $14

EXIT ASSUMPTIONS
Exit EV/EBITDA:                 8.5x
Year 5 EBITDA:                  $211M
Exit Enterprise Value:          $1,794M

Less: Remaining Debt:            ($230M)
Exit Equity Value:              $1,564M

RETURNS
Equity Invested:                $320M
Exit Equity Value:              $1,564M
Money Multiple (MOIC):          4.9x
IRR:                            37.6%

Meets target return? YES
```

**Implied Purchase Price Ranges:**

```
Scenario Analysis - Max Purchase Price by Target IRR:

Exit Multiple    Target IRR    Max Entry EV/EBITDA
    7.5x            20%              7.2x
    8.0x            20%              7.6x
    8.5x            20%              8.1x

    7.5x            25%              6.5x
    8.0x            25%              6.9x
    8.5x            25%              7.3x

    7.5x            30%              5.9x
    8.0x            30%              6.3x
    8.5x            30%              6.6x
```

### 4.3 Sum-of-the-Parts (SOTP)

Values diversified company by valuing each business segment separately.

#### SOTP Methodology

**Step 1: Identify Segments**

Break down into distinct business units:
- Different industries
- Different growth/margin profiles
- Separately reportable segments

**Step 2: Value Each Segment**

Use most appropriate method for each:
- High-growth segment: EV/Revenue or DCF
- Mature segment: EV/EBITDA
- Financial services: P/E or P/B

**Step 3: Sum Segment Values**

```
SOTP = Σ (Segment Value) + Corporate Items
```

#### SOTP Example

**Diversified Industrial Company:**

```
SEGMENT 1: AEROSPACE (high margin, stable)
Revenue:                        $2,000M
EBITDA:                          $400M
Margin:                           20%
Comparable EV/EBITDA:            12.0x
Segment EV:                     $4,800M

SEGMENT 2: AUTOMOTIVE (cyclical, lower margin)
Revenue:                        $3,000M
EBITDA:                          $300M
Margin:                           10%
Comparable EV/EBITDA:            7.0x
Segment EV:                     $2,100M

SEGMENT 3: INDUSTRIAL SOFTWARE (high growth)
Revenue:                          $500M
EBITDA:                           $75M
Margin:                           15%
Comparable EV/Revenue:           5.0x
Segment EV:                     $2,500M

SUBTOTAL - OPERATING SEGMENTS:  $9,400M

CORPORATE/OTHER ADJUSTMENTS:
Corporate overhead (capitalized):  ($500M)
Pension surplus:                   +$200M
Real estate holdings (excess):     +$300M

TOTAL ENTERPRISE VALUE:         $9,400M

Less: Debt                      ($2,000M)
Plus: Cash                         $500M
EQUITY VALUE:                   $7,900M

Shares Outstanding:               100M
Value per Share:                $79.00
```

#### SOTP Considerations

**Benefits:**
- More accurate for diversified companies
- Highlights value of different segments
- Can identify under/over valued parts

**Limitations:**
- Requires detailed segment data
- Conglomerate discount may apply
- Allocation of corporate costs
- Intercompany transactions

**Conglomerate Discount:**

Diversified companies often trade at 10-20% discount to SOTP value:
```
SOTP Value:                     $79.00
Conglomerate Discount:          15%
Adjusted Value:                 $67.15
```

**Reasons for discount:**
- Lack of focus
- Hidden cross-subsidies
- Management complexity
- Less attractive to investors

### 4.4 Other Specialized Methods

#### Real Options Valuation

Values flexibility and strategic options:
- Option to expand
- Option to abandon
- Option to delay
- Option to switch

**When to use:**
- High uncertainty (R&D, natural resources)
- Strategic flexibility valuable
- Traditional DCF undervalues optionality

#### Venture Capital Method

For early-stage companies with high uncertainty:

```
Terminal Value = Year N Revenue × Exit Multiple
or
Terminal Value = Year N Profit × P/E Multiple

PV = Terminal Value / (1 + Discount Rate)^N

Where Discount Rate = 40-70% for early stage
```

**Example:**
```
Year 5 Revenue Forecast:        $50M
Exit Revenue Multiple:          3.0x
Terminal Value:                 $150M

VC Discount Rate:               50%
PV = $150M / (1.5)^5 = $19.8M

Dilution (Series A, B, C):      60%
Pre-money Valuation:            $7.9M
```

#### Replacement Cost

Cost to recreate the company's assets:

```
Replacement Cost = Cost to Build/Acquire All Assets

Includes:
- Physical assets (PP&E)
- Working capital
- Intangibles (brand, customers, technology)
- Time value
```

**When to use:**
- Natural resource companies
- Real estate
- Insurance claims
- Provides valuation ceiling (can't be worth more than replacement cost)

---

## Valuation Summary & Integration

### Triangulation Approach

Use multiple methods to arrive at valuation range.

#### Weighting Different Methods

```
VALUATION SUMMARY

Method                          Value       Weight    Weighted Value
DCF (WACC)                     $85.00        40%         $34.00
DCF (Scenario Analysis)        $82.00
Comparable Companies           $78.00        30%         $23.40
Precedent Transactions         $88.00        20%         $17.60
Asset-Based                    $65.00        10%          $6.50

WEIGHTED AVERAGE VALUE:                                  $81.50

VALUATION RANGE:               $75.00 - $90.00
MIDPOINT:                      $82.50
```

**Weighting Considerations:**

**Give more weight to:**
- DCF if high-quality projections available
- Comps if strong set of comparables
- Precedent transactions if strategic transaction
- Asset-based if mature, stable industry

**Give less weight to:**
- DCF if projections highly uncertain
- Comps if poor comparable set
- Precedent transactions if stale or few transactions
- Asset-based if high intangible value

#### Presenting Valuation Results

**Football Field Chart:**

Visual representation of valuation ranges:
```
Methods                    $60    $70    $80    $90    $100
DCF                                |-----------|
Comparable Companies               |------|
Precedent Transactions                |-----------|
Asset-Based            |-------|
LBO Analysis                         |--------|

Implied Range:                     $75 - $90
Current Trading:           $72
```

**Valuation Bridge:**

Shows path from one valuation to another:
```
Starting Point:
  Comparable Companies Midpoint:    $78.00

Adjustments:
  + Growth premium (vs comps):      +$3.00
  + Margin potential:               +$2.00
  - Smaller scale:                  -$1.50
  + Unique technology:              +$2.50

Adjusted Valuation:                 $84.00
```

### Sanity Checks

**1. Implied Returns:**
```
Current Price:                      $72
Target Price:                       $85
Implied Return:                     18%

Market Return Expectation:          10-12%

Question: Why would market misprice by 18%?
```

**2. Implied Multiples:**
```
Equity Value:                       $8,500M
Current EBITDA:                     $1,000M
Net Debt:                           $500M
Enterprise Value:                   $9,000M
Implied EV/EBITDA:                  9.0x

Industry Average:                   8.5x

Reasonable? If company is higher quality than average, yes.
```

**3. Growth-Multiple Relationship:**
```
Valuation Multiple:                 12.0x EBITDA
Growth Rate:                        15%
PEG-like Ratio:                     0.80

Typically, growth companies with 15% growth trade at 10-15x EBITDA.
12.0x is reasonable.
```

**4. Market Cap as % of Revenue:**
```
Market Cap:                         $8,500M
Revenue:                            $5,000M
Market Cap/Revenue:                 1.7x

SaaS companies: 3-10x
Industrial companies: 0.5-2x
Consumer products: 1-3x

As industrial company, 1.7x is reasonable.
```

### Common Valuation Mistakes

**1. DCF Errors:**
- Terminal value too high (>80% of value)
- Growth rate exceeds GDP
- WACC too low
- Circular reference errors
- Ignoring working capital

**2. Comps Errors:**
- Poor comparable selection
- Not adjusting for one-time items
- Using stale data
- Ignoring size/scale differences
- Mean instead of median (with outliers)

**3. Transaction Errors:**
- Not adjusting for synergies
- Using outdated transactions
- Ignoring market condition changes
- Mixing strategic and financial buyer deals

**4. General Errors:**
- Anchoring bias (fixating on one number)
- Over-precision (value to the penny)
- Ignoring qualitative factors
- Not considering downside scenarios
- Overconfidence in projections

---

## Valuation Best Practices Checklist

**PREPARATION**
- [ ] Understand the business model thoroughly
- [ ] Review historical financials (3-5 years)
- [ ] Understand industry dynamics
- [ ] Research comparable companies
- [ ] Review recent transactions

**DCF ANALYSIS**
- [ ] Build detailed forecast model
- [ ] Calculate free cash flows correctly
- [ ] Compute WACC with current market data
- [ ] Use reasonable terminal value assumptions
- [ ] Perform sensitivity analysis
- [ ] Sanity check: Is TV <80% of value?

**COMPARABLE COMPANIES**
- [ ] Select truly comparable companies (5-10)
- [ ] Use consistent time periods (LTM or NTM)
- [ ] Adjust for one-time items
- [ ] Calculate multiple metrics
- [ ] Remove outliers appropriately
- [ ] Use median, not just mean

**PRECEDENT TRANSACTIONS**
- [ ] Screen for relevant transactions
- [ ] Use recent deals (3-5 years)
- [ ] Adjust for market conditions
- [ ] Understand control premiums
- [ ] Account for synergies
- [ ] Note deal structures

**INTEGRATION**
- [ ] Use multiple methodologies
- [ ] Create valuation range, not point estimate
- [ ] Weight methods appropriately
- [ ] Triangulate to reasonable range
- [ ] Perform sanity checks
- [ ] Consider qualitative factors

**PRESENTATION**
- [ ] Show work and assumptions clearly
- [ ] Present range, not single value
- [ ] Include sensitivity analysis
- [ ] Explain weighting rationale
- [ ] Caveat limitations
- [ ] Be prepared to defend assumptions

---

## Conclusion

Valuation is part science, part art. The techniques in this skill provide the scientific framework, but judgment and experience provide the art.

Key principles to remember:

**1. Multiple Methods**
No single method is perfect. Use DCF, comps, precedent transactions, and other methods. Triangulate to a range.

**2. Reasonable Assumptions**
Aggressive assumptions produce aggressive valuations. Be realistic and conservative. Your credibility depends on it.

**3. Range, Not Point**
Valuation is inherently uncertain. Present a range with clear rationale, not a false sense of precision.

**4. Context Matters**
Purpose of valuation affects approach:
- M&A: Include synergies, control premium
- Investment: Focus on market multiples
- Fairness opinion: Conservative, defensible

**5. Sanity Checks**
Step back and ask: Does this make sense? Compare to:
- Historical valuations
- Industry norms
- Implied returns
- Market expectations

**6. Document Everything**
- Assumptions and sources
- Calculations and methods
- Comparable company selection
- Adjustments made
- Judgment calls

The goal of valuation is to inform better decisions. A well-supported valuation analysis, even if not perfectly "right," is infinitely more valuable than a number pulled from thin air.

Remember: All models are wrong, but some are useful. Strive to be useful.

---

**Skill Version:** 1.0
**Last Updated:** 2024
**Maintained By:** Band of AI
**Related Skills:** financial-modeling.md, merger-analysis.md
