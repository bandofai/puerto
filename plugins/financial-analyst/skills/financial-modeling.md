# Financial Modeling Skill

Comprehensive guide to building integrated financial models with best practices for structure, forecasting, and analysis.

---

## Table of Contents

1. [Financial Statements](#1-financial-statements)
2. [Forecasting](#2-forecasting)
3. [Three-Statement Model](#3-three-statement-model)
4. [Best Practices](#4-best-practices)

---

## 1. Financial Statements

### 1.1 Income Statement Structure

The income statement shows a company's profitability over a period. Proper structure ensures clarity and enables accurate forecasting.

#### Core Components

**Revenue Section**
- Gross Revenue/Sales
- Less: Returns and allowances
- Less: Discounts
- Net Revenue

**Cost of Goods Sold (COGS)**
- Direct materials
- Direct labor
- Manufacturing overhead
- Cost of services delivered
- Gross Profit = Net Revenue - COGS

**Operating Expenses**
- Sales & Marketing
  - Salaries and commissions
  - Advertising and promotion
  - Travel and entertainment
- Research & Development
  - Personnel costs
  - Materials and supplies
  - Prototype development
- General & Administrative
  - Executive compensation
  - Office expenses
  - Professional fees (legal, accounting)
  - Insurance
  - Rent and utilities

**Operating Income (EBIT)**
= Gross Profit - Operating Expenses

**Non-Operating Items**
- Interest Income
- Interest Expense
- Gains/Losses on investments
- Foreign exchange gains/losses
- Other income/expense

**Pre-Tax Income (EBT)**
= EBIT + Non-Operating Items

**Income Tax**
- Current tax expense
- Deferred tax expense

**Net Income**
= EBT - Income Tax

#### Income Statement Template

```
INCOME STATEMENT
For the Year Ended December 31, 20XX
($ in thousands)

Revenue
  Product Revenue                           100,000
  Service Revenue                            50,000
  Total Revenue                             150,000

Cost of Revenue
  Product COGS                               40,000
  Service Delivery Costs                     20,000
  Total Cost of Revenue                      60,000

Gross Profit                                 90,000
Gross Margin %                                 60%

Operating Expenses
  Sales & Marketing                          30,000
  Research & Development                     20,000
  General & Administrative                   15,000
  Total Operating Expenses                   65,000

Operating Income (EBIT)                      25,000
Operating Margin %                           16.7%

Non-Operating Items
  Interest Income                               500
  Interest Expense                           (2,000)
  Other Income/(Expense)                        100
  Total Non-Operating Items                  (1,400)

Income Before Tax (EBT)                      23,600

Income Tax Expense                            5,900
Effective Tax Rate %                           25%

Net Income                                   17,700
Net Margin %                                 11.8%
```

#### Key Metrics from Income Statement

**Profitability Margins**
- Gross Margin = Gross Profit / Revenue
- EBITDA Margin = EBITDA / Revenue
- Operating Margin = EBIT / Revenue
- Net Margin = Net Income / Revenue

**Growth Rates**
- Revenue Growth = (Current Revenue - Prior Revenue) / Prior Revenue
- Expense Growth ratios
- Profit Growth rates

### 1.2 Balance Sheet Structure

The balance sheet provides a snapshot of a company's financial position at a point in time.

#### Asset Section

**Current Assets** (convertible to cash within 1 year)
- Cash and Cash Equivalents
- Marketable Securities
- Accounts Receivable
  - Gross receivables
  - Less: Allowance for doubtful accounts
  - Net receivables
- Inventory
  - Raw materials
  - Work in progress
  - Finished goods
- Prepaid Expenses
- Other Current Assets

**Non-Current Assets**
- Property, Plant & Equipment (PP&E)
  - Land
  - Buildings
  - Machinery & Equipment
  - Furniture & Fixtures
  - Gross PP&E
  - Less: Accumulated Depreciation
  - Net PP&E
- Intangible Assets
  - Goodwill
  - Patents and trademarks
  - Customer relationships
  - Software
  - Less: Accumulated Amortization
- Long-term Investments
- Deferred Tax Assets
- Other Non-Current Assets

**Total Assets**

#### Liability Section

**Current Liabilities** (due within 1 year)
- Accounts Payable
- Accrued Expenses
  - Accrued compensation
  - Accrued taxes
  - Other accruals
- Short-term Debt
- Current Portion of Long-term Debt
- Deferred Revenue
- Other Current Liabilities

**Non-Current Liabilities**
- Long-term Debt
  - Term loans
  - Bonds payable
  - Less: Current portion
- Deferred Tax Liabilities
- Pension Obligations
- Other Long-term Liabilities

**Total Liabilities**

#### Equity Section

**Shareholders' Equity**
- Common Stock (par value)
- Additional Paid-in Capital
- Retained Earnings
  - Beginning retained earnings
  - Plus: Net income
  - Less: Dividends
  - Ending retained earnings
- Treasury Stock
- Accumulated Other Comprehensive Income

**Total Equity**

**Total Liabilities & Equity** = Total Assets

#### Balance Sheet Template

```
BALANCE SHEET
As of December 31, 20XX
($ in thousands)

ASSETS

Current Assets
  Cash and Cash Equivalents                  25,000
  Accounts Receivable, net                   30,000
  Inventory                                  15,000
  Prepaid Expenses                            2,000
  Total Current Assets                       72,000

Non-Current Assets
  Property, Plant & Equipment
    Gross PP&E                               80,000
    Less: Accumulated Depreciation          (30,000)
    Net PP&E                                 50,000

  Intangible Assets, net                     10,000
  Goodwill                                   20,000
  Other Non-Current Assets                    3,000
  Total Non-Current Assets                   83,000

TOTAL ASSETS                                155,000

LIABILITIES & EQUITY

Current Liabilities
  Accounts Payable                           12,000
  Accrued Expenses                            8,000
  Current Portion of Long-term Debt           5,000
  Deferred Revenue                            4,000
  Total Current Liabilities                  29,000

Non-Current Liabilities
  Long-term Debt                             40,000
  Deferred Tax Liabilities                    3,000
  Other Long-term Liabilities                 2,000
  Total Non-Current Liabilities              45,000

Total Liabilities                            74,000

Shareholders' Equity
  Common Stock                                1,000
  Additional Paid-in Capital                 30,000
  Retained Earnings                          50,000
  Total Shareholders' Equity                 81,000

TOTAL LIABILITIES & EQUITY                  155,000
```

#### Key Metrics from Balance Sheet

**Liquidity Ratios**
- Current Ratio = Current Assets / Current Liabilities
- Quick Ratio = (Current Assets - Inventory) / Current Liabilities
- Cash Ratio = Cash / Current Liabilities

**Leverage Ratios**
- Debt-to-Equity = Total Debt / Total Equity
- Debt-to-Assets = Total Debt / Total Assets
- Interest Coverage = EBIT / Interest Expense

**Efficiency Ratios**
- Asset Turnover = Revenue / Average Total Assets
- Inventory Turnover = COGS / Average Inventory
- Days Sales Outstanding = (Accounts Receivable / Revenue) × 365

### 1.3 Cash Flow Statement

The cash flow statement reconciles net income to actual cash movements.

#### Three Sections

**1. Operating Activities**
Shows cash generated from core business operations.

**Indirect Method** (most common):
- Start with Net Income
- Add back non-cash expenses (Depreciation, Amortization)
- Adjust for changes in working capital:
  - Decrease in Accounts Receivable (cash in)
  - Increase in Accounts Receivable (cash out)
  - Decrease in Inventory (cash in)
  - Increase in Inventory (cash out)
  - Increase in Accounts Payable (cash in)
  - Decrease in Accounts Payable (cash out)

**Direct Method** (less common):
- Cash received from customers
- Less: Cash paid to suppliers
- Less: Cash paid for operating expenses
- Less: Cash paid for interest
- Less: Cash paid for taxes

**2. Investing Activities**
Cash flows from buying/selling long-term assets.

Outflows:
- Capital expenditures (PP&E purchases)
- Acquisitions
- Purchases of investments

Inflows:
- Sale of PP&E
- Sale of business units
- Sale of investments

**3. Financing Activities**
Cash flows from transactions with investors and creditors.

Inflows:
- Debt issuance
- Equity issuance

Outflows:
- Debt repayment
- Dividend payments
- Share buybacks

#### Cash Flow Statement Template

```
CASH FLOW STATEMENT
For the Year Ended December 31, 20XX
($ in thousands)

Operating Activities
  Net Income                                 17,700

  Adjustments to reconcile net income:
    Depreciation & Amortization               8,000
    Stock-based Compensation                  2,000
    Deferred Taxes                              500

  Changes in Operating Assets/Liabilities:
    Accounts Receivable                      (3,000)
    Inventory                                (1,500)
    Prepaid Expenses                           (200)
    Accounts Payable                          2,000
    Accrued Expenses                          1,200
    Deferred Revenue                            800

Cash from Operating Activities              27,500

Investing Activities
  Capital Expenditures                      (10,000)
  Acquisitions                               (5,000)
  Purchase of Investments                    (2,000)
  Sale of Equipment                           1,000

Cash from Investing Activities             (16,000)

Financing Activities
  Proceeds from Debt Issuance                10,000
  Debt Repayment                             (8,000)
  Dividends Paid                             (3,000)
  Share Buybacks                             (5,000)

Cash from Financing Activities              (6,000)

Net Change in Cash                            5,500
Beginning Cash Balance                       19,500
Ending Cash Balance                          25,000
```

#### Key Metrics from Cash Flow

**Cash Flow Measures**
- Free Cash Flow = Operating Cash Flow - Capital Expenditures
- Free Cash Flow to Equity = FCF - Net Debt Payments + New Debt
- Operating Cash Flow Margin = Operating Cash Flow / Revenue

**Quality of Earnings**
- Cash Flow to Net Income = Operating Cash Flow / Net Income
  - Ratio > 1.0 indicates high-quality earnings
  - Ratio < 1.0 may indicate aggressive accounting

### 1.4 Statement Linkages

Understanding how the three statements connect is critical for building integrated models.

#### Income Statement to Cash Flow Statement

**Connection Point: Net Income**
- Net Income from IS flows to top of CFS (Operating section)
- Non-cash expenses (D&A) added back
- Working capital changes reconcile accrual to cash basis

#### Cash Flow Statement to Balance Sheet

**Connection Points:**

1. **Operating Activities:**
   - Changes in working capital accounts (AR, Inventory, AP) link to BS
   - Change in AR on CFS = Ending AR (BS) - Beginning AR (BS)

2. **Investing Activities:**
   - CapEx on CFS increases PP&E on BS
   - Acquisitions increase assets on BS

3. **Financing Activities:**
   - Debt issuance/repayment changes debt balances on BS
   - Dividends reduce retained earnings on BS
   - Share buybacks reduce equity on BS

4. **Cash:**
   - Net change in cash on CFS = Ending Cash (BS) - Beginning Cash (BS)

#### Income Statement to Balance Sheet

**Connection Points:**

1. **Net Income to Retained Earnings:**
   - Net Income increases Retained Earnings
   - Dividends decrease Retained Earnings

2. **Depreciation & Amortization:**
   - D&A expense on IS reduces asset values on BS
   - Accumulated Depreciation increases

3. **Interest Expense:**
   - Interest on IS relates to Debt on BS

4. **Working Capital:**
   - Revenue drives Accounts Receivable
   - COGS drives Inventory and Accounts Payable

#### The Financial Statement Flow

```
Income Statement
    ↓
Net Income
    ↓
Cash Flow Statement (Operating Activities)
  + Depreciation & Amortization
  + Working Capital Changes
    ↓
Operating Cash Flow
  - Capital Expenditures
    ↓
Free Cash Flow
  + Financing Activities
    ↓
Net Change in Cash
    ↓
Balance Sheet (Cash)

Net Income also flows to:
Balance Sheet (Retained Earnings)
```

---

## 2. Forecasting

### 2.1 Revenue Drivers and Forecasting Methods

Revenue forecasting is the foundation of any financial model. Different business models require different approaches.

#### Revenue Driver Analysis

**Identify Core Drivers:**
- Volume metrics (units, customers, transactions)
- Price metrics (ASP, subscription tiers)
- Mix metrics (product/segment composition)
- Timing metrics (seasonality, growth trajectory)

**Volume-Based Businesses**
```
Revenue = Units Sold × Average Selling Price (ASP)

Forecast Components:
1. Total Addressable Market (TAM)
2. Market penetration rate
3. Units sold = TAM × Penetration %
4. Price trends and elasticity
```

**Subscription Businesses (SaaS)**
```
MRR = Number of Customers × Average Revenue Per User (ARPU)
ARR = MRR × 12

Forecast Components:
1. Beginning customers
2. + New customers (from sales pipeline)
3. - Churned customers (churn rate %)
4. = Ending customers
5. × ARPU (may vary by cohort)
6. = Monthly Recurring Revenue
```

**Detailed SaaS Metrics:**
- Customer Acquisition Cost (CAC)
- Lifetime Value (LTV)
- LTV/CAC Ratio (target > 3x)
- Months to Recover CAC
- Net Revenue Retention (NRR)
- Gross Revenue Retention (GRR)
- Magic Number = Net New ARR / Sales & Marketing Spend

**Transaction-Based Businesses**
```
Revenue = Transactions × Average Transaction Value (ATV)

Forecast Components:
1. Active users/customers
2. Transactions per user
3. Total transactions
4. Average transaction value
5. Take rate (for marketplaces)
```

**Project-Based Businesses**
```
Revenue = Number of Projects × Average Project Value

Forecast Components:
1. Pipeline of opportunities
2. Win rate %
3. Projects won
4. Average project size
5. Revenue recognition timing
```

#### Top-Down Forecasting

Start with market size and work down to company revenue.

**Process:**
1. Define Total Addressable Market (TAM)
2. Estimate Serviceable Addressable Market (SAM)
3. Determine achievable market share
4. Calculate revenue: TAM × Market Share %

**Example:**
```
TAM (Cloud Storage Market):        $100 billion
SAM (Enterprise segment):          $30 billion
Target Market Share:               2%
Revenue Forecast:                  $600 million
```

**Advantages:**
- Provides market context
- Useful for new products/markets
- Good reality check

**Disadvantages:**
- Relies on market estimates
- Less precise
- Doesn't capture company-specific dynamics

#### Bottom-Up Forecasting

Build revenue from underlying drivers and unit economics.

**Process:**
1. Define smallest revenue unit
2. Forecast unit volumes
3. Apply pricing/economics
4. Aggregate to total revenue

**Example - SaaS Company:**
```
Year 1 Beginning Customers:         1,000
Monthly New Customer Adds:          100
Annual New Customers:               1,200
Monthly Churn Rate:                 2%
Annual Churn:                       240 (assumes avg of 1,100 customers)
Year 1 Ending Customers:            1,960

Average MRR per Customer:           $500
Year 1 Avg Customers:               1,480
Annual Revenue:                     $8,880,000
```

**Advantages:**
- More precise and granular
- Ties to operational metrics
- Testable assumptions

**Disadvantages:**
- Requires detailed data
- Can miss macro trends
- More complex to build

#### Historical Growth Analysis

Use historical patterns to project future growth.

**Simple Growth Rate:**
```
Historical CAGR = (Ending Value / Beginning Value)^(1/Years) - 1

Apply to forecast:
Year N Revenue = Year N-1 Revenue × (1 + Growth Rate)
```

**Regression Analysis:**
- Linear regression for steady growth
- Exponential regression for accelerating growth
- Polynomial regression for complex patterns

**Time Series Methods:**
- Moving averages
- Exponential smoothing
- Seasonal decomposition

#### Cohort Analysis

For subscription businesses, analyze customer behavior by cohort.

**Cohort Revenue Model:**
```
Month 0:   100 customers × $100 = $10,000
Month 1:   95 customers × $100 = $9,500  (5% churn)
Month 2:   90 customers × $100 = $9,000  (5% churn)
Month 3:   86 customers × $105 = $9,030  (5% churn, 5% price increase)
```

**Key Metrics by Cohort:**
- Retention rates over time
- Revenue expansion within cohort
- Lifetime value calculation
- Payback period

### 2.2 Cost Structures

Understanding and forecasting costs is essential for accurate profit projections.

#### Fixed vs Variable Costs

**Fixed Costs:**
- Remain constant regardless of output/revenue
- Examples: Rent, salaries, insurance, depreciation
- Forecast: Typically flat or stepped (increase at thresholds)

**Variable Costs:**
- Change proportionally with output/revenue
- Examples: Raw materials, commissions, shipping
- Forecast: As % of revenue or per unit

**Semi-Variable Costs:**
- Have both fixed and variable components
- Examples: Utilities, staffing (base + overtime)
- Forecast: Fixed base + variable component

#### Cost of Goods Sold (COGS)

**Product-Based COGS:**
```
COGS = Direct Materials + Direct Labor + Manufacturing Overhead

Per Unit:
  Material Cost:               $20
  Labor Cost:                  $10
  Overhead Allocation:         $5
  Total Unit COGS:             $35

Units Sold:                    10,000
Total COGS:                    $350,000
```

**Forecasting Methods:**
1. **% of Revenue Method:**
   - Historical COGS % of revenue
   - Adjust for scale efficiencies
   - Adjust for input cost inflation

2. **Unit Economics Method:**
   - Unit COGS × Units sold
   - Incorporate learning curve effects
   - Factor in supplier negotiations

**Service-Based Cost of Revenue:**
```
Cost of Revenue = Direct Labor + Third-party Services + Infrastructure

Example - SaaS Company:
  Customer Success Team:       $500,000
  Cloud Infrastructure:        $200,000
  Third-party Tools:          $100,000
  Total Cost of Revenue:       $800,000

Revenue:                       $5,000,000
Cost of Revenue %:             16%
Gross Margin:                  84%
```

#### Operating Expenses (OpEx)

**Sales & Marketing:**

Fixed Components:
- Base salaries for sales team
- Marketing team salaries
- Software subscriptions (CRM, marketing tools)

Variable Components:
- Sales commissions (% of revenue)
- Performance bonuses
- Advertising spend (% of revenue or fixed budget)
- Event costs (trade shows, conferences)

**Forecasting Approach:**
```
Base S&M (salaries, tools):    $2,000,000
Variable (commissions at 10%): Revenue × 10%
Additional marketing budget:   $500,000

At $10M revenue:
  Base:                        $2,000,000
  Commissions:                 $1,000,000
  Marketing:                   $500,000
  Total S&M:                   $3,500,000
  S&M % of Revenue:            35%
```

**Research & Development:**

Typically fixed with stepped increases:
- Engineering salaries
- Product management
- QA/Testing
- R&D facilities and equipment

Forecast by:
- Headcount planning
- Average compensation per role
- Equipment/infrastructure needs
- Growth in team size tied to product roadmap

**General & Administrative:**

Mostly fixed with some scale:
- Executive compensation
- Finance & Accounting team
- Legal fees
- Office rent and utilities
- Insurance
- Professional services

Forecast as:
- Fixed base that grows with company size
- % of revenue for variable items (legal, insurance)

#### Working Capital Forecasting

Working capital = Current Assets - Current Liabilities

**Accounts Receivable (AR):**
```
AR = Revenue × (Days Sales Outstanding / 365)

DSO = (Accounts Receivable / Revenue) × 365

Example:
  Annual Revenue:              $10,000,000
  DSO:                         45 days
  Ending AR:                   $1,232,877

Change in AR = Ending AR - Beginning AR
```

**Inventory:**
```
Inventory = COGS × (Days Inventory Outstanding / 365)

DIO = (Inventory / COGS) × 365

Example:
  Annual COGS:                 $6,000,000
  DIO:                         60 days
  Ending Inventory:            $986,301
```

**Accounts Payable (AP):**
```
AP = COGS × (Days Payable Outstanding / 365)

DPO = (Accounts Payable / COGS) × 365

Example:
  Annual COGS:                 $6,000,000
  DPO:                         30 days
  Ending AP:                   $493,151
```

**Cash Conversion Cycle:**
```
CCC = DSO + DIO - DPO
CCC = 45 + 60 - 30 = 75 days

This means 75 days elapse between paying for inventory
and collecting cash from customers.
```

### 2.3 Historical Analysis and Growth Rates

#### Historical Financial Analysis

**Year-over-Year (YoY) Growth:**
```
YoY Growth % = ((Current Year - Prior Year) / Prior Year) × 100

Example:
  2023 Revenue:    $10,000,000
  2022 Revenue:    $8,500,000
  YoY Growth:      17.6%
```

**Compound Annual Growth Rate (CAGR):**
```
CAGR = (Ending Value / Beginning Value)^(1/Number of Years) - 1

Example - 5 Year Revenue CAGR:
  2019 Revenue:    $5,000,000
  2024 Revenue:    $12,000,000
  CAGR:            19.1%
```

**Quarterly Growth Rates:**
```
Sequential Growth (QoQ):
  Q2 vs Q1 growth percentage

Year-over-Year Quarterly:
  Q2 2024 vs Q2 2023 growth percentage
```

#### Common Size Analysis

**Common Size Income Statement:**
Express all line items as % of revenue.

```
                        2024        2023        2022
Revenue              100.0%      100.0%      100.0%
COGS                  40.0%       42.0%       45.0%
Gross Profit          60.0%       58.0%       55.0%
S&M                   30.0%       32.0%       35.0%
R&D                   15.0%       14.0%       13.0%
G&A                   10.0%       12.0%       14.0%
Operating Income       5.0%        0.0%       -7.0%
```

**Insights:**
- Gross margin improving (economies of scale)
- S&M becoming more efficient
- G&A leverage improving
- Achieved profitability in 2024

**Common Size Balance Sheet:**
Express all line items as % of total assets.

#### Trend Analysis

**Identifying Patterns:**
1. Growth trends (accelerating, decelerating, stable)
2. Margin trends (expanding, contracting)
3. Efficiency trends (improving, deteriorating)
4. Seasonality patterns

**Example - Quarterly Revenue Trend:**
```
Q1 2023:  $2.0M  (baseline)
Q2 2023:  $2.2M  (+10% QoQ, +20% YoY)
Q3 2023:  $2.4M  (+9% QoQ, +20% YoY)
Q4 2023:  $2.8M  (+17% QoQ, +27% YoY)  [seasonal strength]
Q1 2024:  $2.5M  (-11% QoQ, +25% YoY)  [seasonal softness]
Q2 2024:  $2.8M  (+12% QoQ, +27% YoY)

Pattern: Consistent YoY growth ~20-27%
         Seasonal spike in Q4
         Sequential growth ex-seasonality ~10%
```

#### Benchmarking

Compare company metrics to:
- Industry averages
- Direct competitors
- Best-in-class companies
- Historical company performance

**Key Benchmarks:**
- Growth rates
- Profitability margins
- Efficiency ratios
- Return metrics (ROE, ROA, ROIC)
- Valuation multiples

---

## 3. Three-Statement Model

### 3.1 Building an Integrated Model

An integrated financial model links the income statement, balance sheet, and cash flow statement so they automatically update together.

#### Model Structure and Flow

**1. Assumptions Sheet**
Central location for all key inputs:
- Revenue growth rates
- Pricing assumptions
- Cost % of revenue
- Working capital days
- Capital expenditure plans
- Debt and interest rates
- Tax rate

**2. Historical Financials**
- 3-5 years of historical data
- Actual financial statements
- Calculated metrics and ratios
- Used for trending and validation

**3. Income Statement Projection**
- Flows from assumptions
- Calculates EBIT
- Interest links to debt schedule
- Tax based on pre-tax income
- Net income to retained earnings

**4. Balance Sheet Projection**
- Operating assets driven by IS
- Working capital from assumptions
- PP&E from beginning balance + CapEx - D&A
- Debt schedule integration
- Retained earnings from IS

**5. Cash Flow Statement**
- Starts with net income from IS
- Working capital changes from BS
- CapEx from assumptions
- Financing from debt schedule
- Ending cash to BS

**6. Supporting Schedules**
- Debt schedule (principal and interest)
- Depreciation schedule
- Working capital schedule
- Revenue build-up

#### Step-by-Step Build Process

**Step 1: Set Up Assumptions**

Create a dedicated assumptions section:
```
ASSUMPTIONS                      2024    2025    2026    2027    2028

Revenue Growth %                  20%     25%     20%     18%     15%

Gross Margin %                    60%     62%     63%     64%     65%

Operating Expenses % of Revenue:
  S&M                            35%     33%     30%     28%     26%
  R&D                            15%     14%     14%     13%     13%
  G&A                            12%     11%     10%     10%      9%

Working Capital Days:
  DSO                             45      45      42      42      40
  DIO                             30      30      28      28      25
  DPO                             30      32      35      35      38

Tax Rate                          25%     25%     25%     25%     25%

CapEx % of Revenue                8%      7%      7%      6%      6%
```

**Step 2: Build Income Statement**

```
INCOME STATEMENT         2023    2024    2025    2026    2027    2028

Revenue                 10.0    12.0    15.0    18.0    21.2    24.4
  YoY Growth %                   20%     25%     20%     18%     15%

COGS                     4.0     4.8     5.7     6.7     7.6     8.5
Gross Profit             6.0     7.2     9.3    11.3    13.6    15.9
Gross Margin %           60%     60%     62%     63%     64%     65%

Operating Expenses:
  S&M                    3.5     4.2     5.0     5.4     5.9     6.3
  R&D                    1.5     1.8     2.1     2.5     2.8     3.2
  G&A                    1.2     1.4     1.7     1.8     2.1     2.2
Total OpEx               6.2     7.4     8.8     9.7    10.8    11.7

EBIT                    -0.2    -0.2     0.5     1.6     2.8     4.1
EBIT Margin %           -2%     -2%      3%      9%     13%     17%

Interest Expense         0.3     0.4     0.5     0.4     0.3     0.2
Interest Income          0.1     0.1     0.2     0.2     0.3     0.4

EBT                     -0.4    -0.5     0.2     1.4     2.8     4.3
Tax                      0.0     0.0     0.1     0.4     0.7     1.1
Net Income              -0.4    -0.5     0.2     1.1     2.1     3.2
Net Margin %            -4%     -4%      1%      6%     10%     13%
```

**Step 3: Build Supporting Schedules**

**Depreciation Schedule:**
```
DEPRECIATION SCHEDULE    2023    2024    2025    2026    2027    2028

Beginning PP&E (gross)   5.0     5.8     6.9     8.2     9.5    11.0
  + CapEx                0.8     1.0     1.1     1.3     1.3     1.5
Ending PP&E (gross)      5.8     6.9     8.2     9.5    11.0    12.5

Beginning Accum Depr     2.0     2.6     3.3     4.1     5.0     5.9
  + Depreciation         0.6     0.7     0.8     0.9     1.0     1.1
Ending Accum Depr        2.6     3.3     4.1     5.0     5.9     7.0

Net PP&E                 3.2     3.6     4.1     4.5     5.0     5.5
```

**Working Capital Schedule:**
```
WORKING CAPITAL          2023    2024    2025    2026    2027    2028

Accounts Receivable:
  Revenue               10.0    12.0    15.0    18.0    21.2    24.4
  DSO (days)              45      45      45      42      42      40
  AR Balance             1.2     1.5     1.8     2.1     2.4     2.7

Inventory:
  COGS                   4.0     4.8     5.7     6.7     7.6     8.5
  DIO (days)              30      30      30      28      28      25
  Inventory Balance      0.3     0.4     0.5     0.5     0.6     0.6

Accounts Payable:
  COGS                   4.0     4.8     5.7     6.7     7.6     8.5
  DPO (days)              30      30      32      35      35      38
  AP Balance             0.3     0.4     0.5     0.6     0.7     0.9
```

**Debt Schedule:**
```
DEBT SCHEDULE            2023    2024    2025    2026    2027    2028

Beginning Debt           5.0     5.0     6.0     6.0     5.0     4.0
  + New Borrowings       0.0     1.0     0.0     0.0     0.0     0.0
  - Repayments           0.0     0.0     0.0     1.0     1.0     1.0
Ending Debt              5.0     6.0     6.0     5.0     4.0     3.0

Interest Rate            6%      6%      7%      7%      7%      7%
Interest Expense         0.3     0.3     0.4     0.4     0.3     0.2
```

**Step 4: Build Cash Flow Statement**

```
CASH FLOW STATEMENT      2023    2024    2025    2026    2027    2028

Operating Activities:
  Net Income            -0.4    -0.5     0.2     1.1     2.1     3.2

  Adjustments:
    Depreciation         0.6     0.7     0.8     0.9     1.0     1.1

  Changes in WC:
    Increase in AR      -0.2    -0.2    -0.4    -0.3    -0.3    -0.2
    Increase in Inv     -0.1    -0.1    -0.1     0.0    -0.1     0.0
    Increase in AP       0.1     0.1     0.1     0.2     0.1     0.2

Cash from Ops            0.0     0.0     0.6     1.9     2.8     4.3

Investing Activities:
  CapEx                 -0.8    -1.0    -1.1    -1.3    -1.3    -1.5

Cash from Investing     -0.8    -1.0    -1.1    -1.3    -1.3    -1.5

Financing Activities:
  Debt Issuance          0.0     1.0     0.0     0.0     0.0     0.0
  Debt Repayment         0.0     0.0     0.0    -1.0    -1.0    -1.0

Cash from Financing      0.0     1.0     0.0    -1.0    -1.0    -1.0

Net Change in Cash      -0.8     0.0    -0.5    -0.4     0.5     1.8

Beginning Cash           3.0     2.2     2.2     1.7     1.3     1.8
Ending Cash              2.2     2.2     1.7     1.3     1.8     3.6
```

**Step 5: Build Balance Sheet**

```
BALANCE SHEET            2023    2024    2025    2026    2027    2028

ASSETS
Cash                     2.2     2.2     1.7     1.3     1.8     3.6
Accounts Receivable      1.2     1.5     1.8     2.1     2.4     2.7
Inventory                0.3     0.4     0.5     0.5     0.6     0.6
Total Current Assets     3.7     4.1     4.0     3.9     4.8     6.9

PP&E, net                3.2     3.6     4.1     4.5     5.0     5.5

TOTAL ASSETS             6.9     7.7     8.1     8.4     9.8    12.4

LIABILITIES
Accounts Payable         0.3     0.4     0.5     0.6     0.7     0.9
Total Current Liab       0.3     0.4     0.5     0.6     0.7     0.9

Long-term Debt           5.0     6.0     6.0     5.0     4.0     3.0
Total Liabilities        5.3     6.4     6.5     5.6     4.7     3.9

EQUITY
Common Stock             1.0     1.0     1.0     1.0     1.0     1.0
Retained Earnings        0.6     0.3     0.6     1.8     4.1     7.5
Total Equity             1.6     1.3     1.6     2.8     5.1     8.5

TOTAL LIAB & EQUITY      6.9     7.7     8.1     8.4     9.8    12.4
```

### 3.2 Circular References (Debt Schedule)

Circular references occur when cells reference each other, creating loops. The most common example is the debt-interest circularity.

#### The Problem

**Circular Logic:**
1. Interest expense depends on average debt balance
2. Net income depends on interest expense
3. Cash flow depends on net income
4. Ending cash depends on cash flow
5. If cash is negative, need more debt
6. More debt increases interest expense (back to step 1)

#### Solution: Debt Schedule with Revolver

**Approach:**
Build a cash sweep mechanism that automatically borrows or repays based on cash position.

```
CASH CALCULATION                 2024    2025    2026

Operating Cash Flow               0.0     0.6     1.9
- CapEx                          -1.0    -1.1    -1.3
- Mandatory Debt Repayment        0.0     0.0    -1.0
= Cash Available/(Needed)        -1.0    -0.5    -0.4

Target Minimum Cash               2.0     2.0     2.0

DEBT CALCULATIONS
Beginning Revolver                5.0     6.0     6.0
  + Draw (if cash needed)         1.0     0.5     0.4
  - Paydown (if excess cash)      0.0     0.5     1.0
= Ending Revolver                 6.0     6.0     5.0

Average Debt Balance              5.5     6.0     5.5
Interest Rate                     6%      7%      7%
Interest Expense                  0.3     0.4     0.4
```

#### Excel Implementation

**Iteration Settings:**
Enable iterative calculation in Excel:
- File > Options > Formulas
- Enable iterative calculation
- Set Maximum Iterations: 100
- Maximum Change: 0.001

**Formula Structure:**
```
Cell C10 (Interest Expense):
= C20 (Average Debt) * C21 (Interest Rate)

Cell C15 (Net Income):
= C12 (EBIT) - C10 (Interest Expense) - C13 (Taxes)

Cell C30 (Cash Flow):
= C15 (Net Income) + C16 (Depreciation) - C17 (CapEx) - ...

Cell C40 (Ending Cash):
= C39 (Beginning Cash) + C30 (Cash Flow)

Cell C45 (Revolver Draw):
= IF(C40 < Target Minimum, Target Minimum - C40, 0)

Cell C50 (Ending Debt):
= C49 (Beginning Debt) + C45 (Draw) - C46 (Paydown)

Cell C20 (Average Debt):
= (C49 (Beginning Debt) + C50 (Ending Debt)) / 2
```

This creates a circular reference: C10 → C15 → C30 → C40 → C45 → C50 → C20 → C10

Excel's iteration feature will calculate this correctly.

#### Alternative: Manual Iteration

If you can't use Excel iteration, manually iterate:

**Method:**
1. Start with beginning debt balance
2. Calculate interest expense
3. Calculate cash flow
4. Determine debt draw/paydown needed
5. Recalculate interest with new debt balance
6. Repeat until change is minimal (converges)

### 3.3 Balancing the Model

A properly built model will balance automatically, but errors can cause imbalances.

#### The Balance Check

**Primary Check:**
```
Balance Sheet Check:
Total Assets = Total Liabilities + Equity

If Assets ≠ Liabilities + Equity, there's an error.
```

**Insert Balance Check Row:**
```
Row 100: Balance Check
= Total Assets - (Total Liabilities + Total Equity)

Result should be $0 in all periods.
```

#### Common Balance Errors

**1. Retained Earnings Not Flowing Correctly**

Error: Net income not linking to retained earnings

Fix:
```
Ending Retained Earnings =
  Beginning Retained Earnings
  + Net Income
  - Dividends
```

**2. Cash Flow Not Linking to Balance Sheet**

Error: Change in cash on CFS ≠ change in cash on BS

Fix:
```
Balance Sheet Cash (Period N) =
  Balance Sheet Cash (Period N-1)
  + Net Change in Cash from CFS (Period N)
```

**3. Working Capital Changes Incorrect**

Error: Working capital changes on CFS don't match BS changes

Fix:
```
CFS: Increase in AR =
  BS: Ending AR (Period N)
  - BS: Beginning AR (Period N-1)

Sign convention:
  Increase in AR = Use of cash (negative in CFS)
  Decrease in AR = Source of cash (positive in CFS)
```

**4. PP&E Schedule Not Linking**

Error: PP&E balance doesn't reconcile with CapEx and depreciation

Fix:
```
Ending Net PP&E =
  Beginning Net PP&E
  + CapEx
  - Depreciation
  +/- Acquisitions/Disposals
```

**5. Debt Schedule Not Linking**

Error: Debt balance doesn't match schedule

Fix:
```
Ending Debt Balance =
  Beginning Debt Balance
  + New Borrowings
  - Repayments
```

#### Debugging Process

**Step-by-Step Debug:**

1. **Check Period 1 First**
   - Balance should work in first forecast period
   - If Period 1 is wrong, later periods will be wrong

2. **Trace Each Statement**
   - Income Statement: Does Net Income look reasonable?
   - Cash Flow: Do the three sections add up to change in cash?
   - Balance Sheet: Does BS cash = BS cash (prior) + CFS change?

3. **Check Individual Line Items**
   - AR: Revenue × DSO/365
   - Inventory: COGS × DIO/365
   - AP: COGS × DPO/365
   - PP&E: Prior + CapEx - Depreciation

4. **Verify Formulas**
   - Are formulas copying correctly across periods?
   - Are cell references absolute ($) vs relative?
   - Are there any hard-coded numbers that should be formulas?

### 3.4 Sensitivity Tables

Sensitivity analysis shows how changes in key assumptions impact outputs.

#### One-Way Sensitivity Table

Shows impact of changing one variable.

**Example: Revenue Growth Sensitivity on 2028 Net Income**

```
Revenue Growth Rate    2028 Net Income
        12%                 $2.5M
        14%                 $2.8M
        15% (base)          $3.2M
        17%                 $3.6M
        20%                 $4.2M
```

**Excel Setup:**
1. Create table with input values in left column
2. Formula in top-left cell references output cell
3. Select table range
4. Data > What-If Analysis > Data Table
5. Column input cell: Cell containing growth rate assumption
6. Excel populates table with results

#### Two-Way Sensitivity Table

Shows impact of changing two variables simultaneously.

**Example: 2028 EBIT Sensitivity to Revenue Growth and Gross Margin**

```
                    Gross Margin %
Rev Growth    60%     62%     64%     66%     68%
   12%       $2.1M   $2.5M   $2.9M   $3.3M   $3.7M
   14%       $2.5M   $2.9M   $3.4M   $3.8M   $4.3M
   15% (base) $2.7M   $3.2M   $3.7M   $4.1M   $4.6M
   17%       $3.1M   $3.6M   $4.1M   $4.6M   $5.2M
   20%       $3.7M   $4.3M   $4.9M   $5.5M   $6.1M
```

**Excel Setup:**
1. Input values for Variable 1 in left column
2. Input values for Variable 2 in top row
3. Formula in top-left cell references output
4. Select entire table
5. Data > What-If Analysis > Data Table
6. Row input cell: Cell for Variable 2
7. Column input cell: Cell for Variable 1

#### Scenario Analysis

Compare discrete scenarios (Base, Upside, Downside).

**Example: 2028 Scenarios**

```
Assumptions          Base Case   Upside    Downside
Revenue Growth          15%        20%        10%
Gross Margin            65%        67%        62%
OpEx % of Revenue       48%        45%        50%

Results:
Revenue              $24.4M     $26.8M     $22.1M
EBIT                  $4.1M      $5.9M      $2.7M
Net Income            $3.2M      $4.4M      $2.0M
EBIT Margin            17%        22%        12%
```

**Implementation:**
1. Create separate columns for each scenario
2. Link assumptions to scenario column
3. Use drop-down or switch to select active scenario
4. OR: Build separate full models for each scenario

---

## 4. Best Practices

### 4.1 Model Structure and Layout

A well-structured model is easier to build, audit, and maintain.

#### Worksheet Organization

**Recommended Sheet Structure:**

1. **Cover/Documentation**
   - Model purpose and scope
   - Key contacts and version history
   - Table of contents
   - Key assumptions summary
   - Executive summary of results

2. **Assumptions**
   - All key inputs in one place
   - Clearly labeled and organized
   - Color-coded (blue font = input)
   - Include data sources and justification

3. **Historical Financials**
   - 3-5 years of actuals
   - Three financial statements
   - Supporting schedules
   - Key metrics and ratios

4. **Income Statement**
   - Forecast period
   - Monthly, quarterly, or annual
   - Clear section breaks
   - Calculated metrics below statements

5. **Supporting Schedules**
   - Revenue build-up
   - Operating expense detail
   - Depreciation schedule
   - Working capital schedule
   - Debt schedule

6. **Cash Flow Statement**
   - Three sections clearly labeled
   - Links to other statements
   - Free cash flow calculation

7. **Balance Sheet**
   - Asset section
   - Liability section
   - Equity section
   - Balance check

8. **Valuation** (if applicable)
   - DCF analysis
   - Comparable companies
   - Outputs and summary

9. **Sensitivity & Scenarios**
   - One-way and two-way tables
   - Scenario comparison
   - Charts and visualizations

#### Layout Principles

**Consistent Formatting:**
- Time periods flow left to right
- Similar items align vertically
- Consistent indentation for sub-items
- Consistent decimal places and units

**Clear Headers:**
```
                    2023    2024    2025    2026    2027
                  (Actual) (Proj) (Proj) (Proj) (Proj)
```

**Section Breaks:**
- Use blank rows to separate sections
- Use borders or shading for major sections
- Bold headers for main categories

**Units Consistency:**
```
($ in thousands)          or          ($ in millions)

Clearly state at top of each statement.
```

#### Color Coding

**Standard Color Convention:**
- Blue font = Hard-coded input or assumption
- Black font = Formula/calculation
- Green font = Link from another worksheet
- Red font = Link from external file
- Yellow highlight = Important or needs attention
- Gray = Historical/actual data

**Example:**
```
Revenue Growth Rate:     15%     [Blue = user input]
Revenue:              $10,000    [Black = calculated]
Benchmark Growth:       18%     [Green = from "Market Data" sheet]
```

### 4.2 Formula Best Practices

#### Use Named Ranges

Instead of:
```
=C10*$G$5
```

Use:
```
=Revenue*GrowthRate
```

**Benefits:**
- Easier to understand formulas
- Reduces errors
- Easier to audit
- Self-documenting

**How to Create:**
1. Select cell/range
2. Name Box (left of formula bar) or Ctrl+F3
3. Enter descriptive name (no spaces)

#### Avoid Hard-Coding Numbers

**Bad:**
```
=Revenue*0.15
```

**Good:**
```
=Revenue*GrowthRate

Where GrowthRate references a cell in the assumptions section.
```

**Exception:** Constants that never change (e.g., days in year):
```
=AccountsReceivable/Revenue*365
```

#### Use Consistent Formula Structure

**Consistency Across Periods:**
When copying formulas across periods, ensure:
- Relative references update correctly
- Absolute references ($) stay fixed
- Formula logic remains consistent

**Example:**
```
Period 1:  =B10+B20+B30
Period 2:  =C10+C20+C30    [correctly copied]
NOT:       =C10+D20+B30    [inconsistent!]
```

#### Break Complex Formulas into Steps

**Bad:**
```
=((Revenue*(1-TaxRate))+Depreciation-
(WorkingCapital_End-WorkingCapital_Begin)-CapEx)/
((1+WACC)^Year)
```

**Good:**
```
Row 10: NOPAT = Revenue*(1-TaxRate)
Row 11: Plus: D&A = Depreciation
Row 12: Less: Change in WC = WorkingCapital_End - WorkingCapital_Begin
Row 13: Less: CapEx = CapEx
Row 14: = Free Cash Flow = SUM(Row10:Row13 with signs)
Row 15: Discount Factor = 1/(1+WACC)^Year
Row 16: PV of FCF = Row14*Row15
```

**Benefits:**
- Easier to audit
- Easier to debug
- Easier to understand
- Can check intermediate calculations

#### Use Excel Functions Appropriately

**SUM vs + :**
```
Good:    =SUM(C10:C20)
Risky:   =C10+C11+C12+C13+C14+C15+C16+C17+C18+C19+C20
```
If you insert a row, SUM auto-adjusts, but + chain might break.

**Conditional Logic:**
```
=IF(Revenue>10000, "Large", "Small")
=IF(CashFlow<0, -CashFlow, 0)  [Borrow if cash negative]
```

**Lookup Functions:**
```
=VLOOKUP(CompanyName, CompsTable, ColumnNumber, FALSE)
=INDEX(DataRange, MATCH(LookupValue, LookupRange, 0))
```

**Error Handling:**
```
=IFERROR(Revenue/0, "N/A")
Instead of: #DIV/0! error
```

### 4.3 Scenario Management

#### Scenario Switches

**Method 1: Drop-Down Selection**

```
Cell B1: Scenario Selection [Drop-down: Base, Upside, Downside]

Cell B5: Revenue Growth Rate
=IF($B$1="Base", 15%, IF($B$1="Upside", 20%, 10%))

Cell B6: Gross Margin
=IF($B$1="Base", 65%, IF($B$1="Upside", 68%, 62%))
```

**Method 2: CHOOSE Function**

```
Cell B1: Scenario Number [1=Base, 2=Upside, 3=Downside]

Cell B5: Revenue Growth
=CHOOSE($B$1, 15%, 20%, 10%)
```

**Method 3: Lookup Table**

```
Scenario Table:
             Base    Upside  Downside
Rev Growth    15%      20%      10%
Gross Margin  65%      68%      62%
OpEx %        48%      45%      50%

Cell B5: Revenue Growth
=INDEX(ScenarioTable, 1, SelectedScenarioColumn)
```

#### Scenario Comparison View

Create a summary that shows all scenarios side-by-side:

```
                        Base Case  Upside   Downside
2028 Revenue              $24.4M   $26.8M    $22.1M
2028 EBIT                  $4.1M    $5.9M     $2.7M
2028 Net Income            $3.2M    $4.4M     $2.0M

2028 EBIT Margin            17%      22%       12%
2028 Net Margin             13%      16%        9%

2024-28 Revenue CAGR        20%      22%       17%
2024-28 EBIT CAGR          110%     135%       85%

NPV @ 10% WACC            $15.2M   $19.8M    $11.5M
IRR                         25%      32%       18%
```

### 4.4 Error Checking

#### Built-in Checks

**Balance Sheet Check:**
```
Row 100: Balance Check
= TotalAssets - (TotalLiabilities + TotalEquity)

Conditional Formatting:
If <> 0, highlight red
If = 0, highlight green
```

**Cash Flow Check:**
```
Check 1: Change in Cash
= EndingCash_BS - BeginningCash_BS - NetChangeInCash_CFS
Should = 0

Check 2: Operating Cash Flow Components
= NetIncome + D&A + Sum(WorkingCapitalChanges)
Should equal Operating Cash Flow total
```

**Working Capital Checks:**
```
Check: Change in AR on CFS
= EndingAR_BS - BeginningAR_BS
Should match (with correct sign) AR change on CFS
```

#### Formula Auditing

**Excel Tools:**
- Trace Precedents (Show which cells feed into formula)
- Trace Dependents (Show which cells depend on this cell)
- Error Checking
- Evaluate Formula (Step through calculation)

**Manual Checks:**
- Sort by formula to find inconsistencies
- Check for absolute vs relative references
- Verify formulas copied correctly across periods
- Check for circular references (unless intentional)

#### Reasonableness Checks

**Sanity Checks to Include:**

1. **Growth Rates:**
   - Are growth rates consistent with industry/plan?
   - Do growth rates moderate over time (reversion to mean)?
   - Are they achievable given market size?

2. **Margins:**
   - Are margins within industry norms?
   - Do margins improve with scale (if expected)?
   - Are margins sustainable?

3. **Ratios:**
   - Is leverage (Debt/Equity) reasonable?
   - Is interest coverage (EBIT/Interest) adequate (>3x)?
   - Are return metrics (ROE, ROIC) achievable?

4. **Cash Flow:**
   - Does the company generate positive cash flow eventually?
   - Are capital needs fundable?
   - Does cash position make sense?

5. **Balance Sheet:**
   - Are asset balances reasonable given revenue?
   - Is working capital in line with operating metrics?
   - Does equity grow with retained earnings?

#### Common Errors to Watch For

1. **Linking Errors:**
   - Broken links to other workbooks
   - References to deleted sheets/rows
   - Incorrect cell references

2. **Formula Errors:**
   - Inconsistent formulas across periods
   - Hard-coded numbers instead of references
   - Incorrect order of operations

3. **Logic Errors:**
   - Wrong signs (positive vs negative)
   - Incorrect IF statement logic
   - Missing scenarios in IF statements

4. **Copy/Paste Errors:**
   - Pasted values instead of formulas
   - Pasted with incorrect formatting
   - References not updated correctly

5. **Rounding Errors:**
   - Accumulated rounding causes imbalances
   - Use ROUND() function sparingly
   - Consider keeping extra decimal places in calculations

### 4.5 Model Documentation

#### Documentation Best Practices

**Cover Sheet:**
```
MODEL DOCUMENTATION
===================

Model Name: [Company Name] Financial Model
Version: 2.1
Date: January 15, 2024
Prepared By: [Your Name]
Reviewed By: [Reviewer Name]

PURPOSE
-------
5-year financial projection for [Company] to support:
- Strategic planning
- Fundraising (Series B)
- Valuation analysis

SCOPE
-----
- 5-year projection (2024-2028)
- Annual periods
- Three financial statements
- DCF valuation

KEY ASSUMPTIONS
--------------
- Revenue CAGR: 20%
- Gross Margin: 60-65%
- Achieves profitability in 2025
- Tax Rate: 25%

CHANGE LOG
----------
v2.1 (Jan 15, 2024): Added sensitivity analysis
v2.0 (Jan 10, 2024): Updated Q4 2023 actuals
v1.0 (Dec 15, 2023): Initial model
```

**Assumptions Documentation:**
```
ASSUMPTION                  VALUE   SOURCE/RATIONALE
----------                  -----   -----------------
Revenue Growth 2024          20%    Management plan;
                                    consistent with 2023 actual

Gross Margin 2024            60%    Current actual;
                                    improvement expected with scale

S&M % of Revenue             35%    Industry benchmark 30-40%;
                                    higher for growth phase
```

**Worksheet Notes:**
- Use comments (right-click > Insert Comment) for:
  - Unusual assumptions
  - Complex formulas
  - Data sources
  - Questions or items to review

**Instructions for Users:**
```
HOW TO USE THIS MODEL
====================

1. INPUTS
   - All inputs are on the "Assumptions" sheet
   - Input cells are marked in BLUE
   - Do not change any other cells

2. SCENARIOS
   - Select scenario in cell B1 of Assumptions sheet
   - Options: Base Case, Upside, Downside
   - All outputs will automatically update

3. OUTPUTS
   - View financial statements on respective tabs
   - Summary metrics on "Dashboard" sheet
   - Valuation outputs on "DCF" sheet

4. CHECKS
   - Balance Check on Balance Sheet must = $0
   - If not, do not rely on model outputs
   - Contact model owner for support
```

#### Version Control

**File Naming Convention:**
```
[Company]_FinancialModel_[Version]_[Date]_[InitialsIfDraft].xlsx

Examples:
Acme_FinancialModel_v2.1_20240115.xlsx            (official version)
Acme_FinancialModel_v2.2_20240120_JD_DRAFT.xlsx   (working draft)
```

**Version Tracking in Model:**
Create a version log on cover sheet:
```
VERSION HISTORY
===============
v2.1  Jan 15, 2024  [JD]  Added sensitivity analysis
v2.0  Jan 10, 2024  [JD]  Updated with Q4 2023 actuals
v1.5  Dec 20, 2023  [JD]  Revised revenue assumptions
v1.0  Dec 15, 2023  [JD]  Initial model creation
```

---

## Summary: Financial Modeling Skill Checklist

When building or reviewing a financial model, use this checklist:

**STRUCTURE**
- [ ] Clear worksheet organization
- [ ] Separate assumptions sheet
- [ ] Historical financials included
- [ ] Time flows left to right
- [ ] Consistent formatting and units
- [ ] Color coding applied

**ASSUMPTIONS**
- [ ] All key inputs in assumptions sheet
- [ ] Inputs clearly labeled and blue-coded
- [ ] Assumptions documented and sourced
- [ ] Reasonable and benchmarked

**INCOME STATEMENT**
- [ ] Complete IS structure
- [ ] Revenue ties to drivers
- [ ] COGS appropriate method
- [ ] OpEx categories detailed
- [ ] Tax calculated correctly
- [ ] Net income flows to retained earnings

**BALANCE SHEET**
- [ ] Complete BS structure
- [ ] Working capital calculated from assumptions
- [ ] PP&E tied to depreciation schedule
- [ ] Debt tied to debt schedule
- [ ] Retained earnings linked to net income
- [ ] Balance check = $0

**CASH FLOW STATEMENT**
- [ ] Starts with net income
- [ ] D&A added back
- [ ] Working capital changes correct
- [ ] CapEx included
- [ ] Financing activities complete
- [ ] Change in cash ties to BS

**SUPPORTING SCHEDULES**
- [ ] Depreciation schedule built
- [ ] Working capital schedule detailed
- [ ] Debt schedule with interest
- [ ] Revenue build-up documented

**INTEGRATION**
- [ ] Three statements link correctly
- [ ] Circular references handled (if any)
- [ ] All formulas flow properly
- [ ] No broken links

**CHECKS & VALIDATION**
- [ ] Balance sheet balances
- [ ] Cash flow reconciles
- [ ] Ratios reasonable
- [ ] Growth rates sensible
- [ ] Error checks included

**SCENARIOS & SENSITIVITY**
- [ ] Scenario capability built
- [ ] Sensitivity tables created
- [ ] Key value drivers analyzed
- [ ] Outputs easy to compare

**DOCUMENTATION**
- [ ] Cover sheet with model info
- [ ] Assumptions documented
- [ ] Version control in place
- [ ] User instructions clear
- [ ] Complex formulas explained

**BEST PRACTICES**
- [ ] Named ranges used
- [ ] No hard-coded numbers (except constants)
- [ ] Formulas broken into steps
- [ ] Consistent formula structure
- [ ] Appropriate Excel functions

---

## Conclusion

Financial modeling is both an art and a science. Technical proficiency with Excel and accounting principles is essential, but equally important is business judgment, clear communication, and attention to detail.

A well-built model should be:
- **Accurate**: Reflects business reality and accounting rules
- **Transparent**: Easy to follow and audit
- **Flexible**: Can accommodate different scenarios and assumptions
- **Robust**: Handles edge cases and includes error checks
- **Professional**: Well-formatted, documented, and maintainable

This skill provides the foundation. Apply these principles consistently, adapt to your specific business context, and always prioritize clarity and accuracy over complexity.

Remember: The goal of a financial model is to support better decision-making. A model that no one understands or trusts won't achieve that goal, no matter how sophisticated it is.

---

**Skill Version:** 1.0
**Last Updated:** 2024
**Maintained By:** Band of AI
**Related Skills:** valuation.md, excel-financial-analysis.md
