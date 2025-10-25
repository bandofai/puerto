# Budget Management Skill

## Overview
Patterns for transaction categorization, budget tracking, and spending analysis for personal finance management.

## Transaction Categorization Patterns

### Merchant Patterns
**Housing**:
- Rent, mortgage, property management, utilities (electric, gas, water)
- Home insurance, HOA fees

**Food**:
- Groceries: Whole Foods, Trader Joe's, Safeway, Kroger, Walmart
- Restaurants: Any restaurant, fast food
- Coffee shops: Starbucks, Peet's, local cafes
- Delivery: DoorDash, Uber Eats, Grubhub

**Transportation**:
- Gas: Shell, Chevron, BP, Exxon
- Ride sharing: Uber, Lyft
- Public transit: BART, Metro, bus fare
- Parking: parking lots, meters
- Car: payment, insurance, maintenance

**Shopping**:
- Amazon, eBay, Target, Costco
- Clothing stores
- Electronics: Best Buy, Apple Store
- Home goods: IKEA, HomeDepot, Lowe's

**Entertainment**:
- Movies: AMC, Regal
- Streaming: Netflix, Spotify, Disney+, Hulu
- Events: concerts, sports
- Hobbies: books, games

**Healthcare**:
- Doctors, dentists, hospitals
- Pharmacy: CVS, Walgreens, Rite Aid
- Health insurance

**Bills**:
- Phone: AT&T, Verizon, T-Mobile
- Internet: Comcast, Spectrum
- Subscriptions: software, services

**Income**:
- Salary, paycheck, direct deposit
- Refunds, reimbursements
- Interest, dividends

### Amount Patterns
- **Large recurring (>$1000)**: Likely rent/mortgage
- **Round numbers ($50, $100)**: Often cash withdrawals, payments
- **Small recurring ($9.99, $14.99)**: Subscriptions
- **Refunds (positive amounts)**: Returns, reimbursements

### Confidence Scoring
- **High (90-100%)**: Exact merchant match
- **Medium (70-89%)**: Pattern match
- **Low (<70%)**: Guess based on amount/description
- **Manual Review**: Unusual or ambiguous

## Budget Tracking Framework

### Setting Budgets

**50/30/20 Rule** (guideline):
- 50% Needs (housing, food, utilities, transport)
- 30% Wants (entertainment, dining out, shopping)
- 20% Savings/Debt (emergency fund, retirement, debt payoff)

**Monthly Budget Template**:
```
Income: $5,000/month

Needs (50% = $2,500):
- Housing: $1,200
- Food (groceries): $400
- Utilities: $200
- Transportation: $300
- Healthcare: $200
- Phone/Internet: $200

Wants (30% = $1,500):
- Dining Out: $300
- Entertainment: $200
- Shopping: $400
- Hobbies: $200
- Travel fund: $400

Savings (20% = $1,000):
- Emergency fund: $500
- Retirement: $400
- Debt payoff: $100
```

### Budget Monitoring

**Alert Levels**:
- 70%: Gentle reminder
- 80%: Warning
- 90%: Urgent alert
- 100%: Budget reached
- >100%: Over budget (requires attention)

**Actions by Level**:
- 70-80%: "You've used 75% of your dining budget - $150 remaining"
- 90%+: "Alert: Only $50 left in shopping budget for this month"
- Over: "You're $80 over your entertainment budget - review recent spending"

## Spending Analysis Patterns

### Trend Analysis
- **Month-over-Month**: Compare to last month
- **Year-over-Year**: Compare to same month last year
- **Moving Average**: 3-month average for smoothing
- **Percentage Change**: (Current - Previous) / Previous × 100%

### Anomaly Detection
- Spending >2x average for category = anomaly
- New merchants (never seen before) = flag for review
- Large single transactions (>$500) = highlight
- Unusual timing (spending at 3am) = potential fraud

### Insights Generation

**Top Spending Categories**:
```
Where Your Money Goes (January 2025)
1. Housing: $1,200 (35%)
2. Food: $620 (18%) - $420 groceries, $200 dining
3. Transportation: $450 (13%)
4. Shopping: $380 (11%)
5. Bills: $280 (8%)
Other: $520 (15%)
Total: $3,450
```

**Trend Insights**:
- "Dining out increased 45% vs last month ($200 → $290)"
- "Transportation down 20% (good job!)"
- "New subscription detected: $14.99/month to Netflix"

**Opportunity Insights**:
- "You have 5 active streaming services ($65/month) - consider consolidating"
- "Dining out is 30% of food budget - cooking more could save $150/month"
- "You're paying for gym but only went 2x this month"

### Comparison Analysis
- Spending vs Budget
- Current period vs Last period
- Category distribution (pie chart data)
- Spending trajectory (on track to exceed? under budget?)

## Data Structures

### Transaction Format
```json
{
  "id": "uuid",
  "date": "YYYY-MM-DD",
  "description": "Merchant name",
  "amount": -49.99,
  "category": "Shopping",
  "subcategory": "Electronics",
  "confidence": 95,
  "source": "chase",
  "notes": ""
}
```

### Budget Format
```json
{
  "period": "2025-01",
  "budgets": {
    "Housing": 1200,
    "Food": 500,
    "Transportation": 300,
    "Shopping": 400,
    "Entertainment": 150,
    "Bills": 300,
    "Healthcare": 200,
    "Personal": 100
  },
  "income": 5000
}
```

## Privacy & Security

- All data stored locally
- No data sent to external services
- Merchant names anonymized in reports if requested
- Secure storage of financial data
- Regular data backups recommended

## Best Practices

1. **Import Regularly**: Weekly or bi-weekly (don't wait until end of month)
2. **Review Categories**: Check AI categorization, correct as needed
3. **Update Budgets**: Adjust quarterly based on actual spending
4. **Track Trends**: Look at month-over-month, not just single month
5. **Set Realistic Budgets**: Base on actual spending, not wishful thinking
6. **Emergency Fund**: Build 3-6 months of expenses
7. **Review Subscriptions**: Audit quarterly, cancel unused
8. **Seasonal Adjust**: Expect higher spending in December, summer vacation
