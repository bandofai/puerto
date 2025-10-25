# Financial Goal Tracker Plugin

Financial goal setting and progress tracking specialist with SMART framework and automated recommendations.

## Overview

Achieve your financial dreams with systematic goal tracking, progress visualization, projection modeling, and automated savings recommendations.

## Agent

### goal-manager (Haiku)
**Description**: PROACTIVELY tracks financial goals with progress visualization

**Capabilities**:
- SMART goal framework (Specific, Measurable, Achievable, Relevant, Time-bound)
- Multiple goal tracking (emergency fund, house, retirement, debt payoff)
- Progress bars and milestone celebrations
- Projection modeling (when will I reach goal?)
- Automated savings recommendations
- Debt payoff optimization (snowball vs avalanche)

**Use When**:
- Setting new financial goals
- Updating progress
- Checking projections
- Getting savings recommendations
- Optimizing debt payoff strategy

**Tools**: Read, Write, Bash

## Features

✅ **SMART Goal Framework**: Structured, achievable goal setting
✅ **Progress Visualization**: Progress bars and percentage complete
✅ **Projection Modeling**: Calculate when you'll reach each goal
✅ **Automated Recommendations**: Optimal monthly savings amounts
✅ **Debt Optimization**: Compare snowball vs avalanche methods
✅ **Milestone Celebrations**: Motivation at key achievements
✅ **Multi-Goal Tracking**: Manage multiple goals simultaneously

## Usage Examples

### Create a New Goal

```
Use goal-manager to create emergency fund goal:
- Target: $30,000 (6 months expenses)
- Current: $5,000
- Monthly contribution: $500
- Deadline: Dec 2026
- Priority: High
```

**Result**:
```
✅ Goal created: Emergency Fund

Target: $30,000
Current: $5,000 (17%)
Monthly: $500
Deadline: Dec 31, 2026

Projection: Will reach goal in 50 months (Jan 2030)
⚠️ Behind schedule by 38 months

Recommendation: Increase to $1,050/month to hit deadline
```

### View All Goals with Progress

```
Use goal-manager to show all my financial goals
```

**Result**:
```
📊 Financial Goals Progress

1. Emergency Fund (High Priority)
   $12,000 / $30,000 ████████░░░░░░░░░░░░ 40%
   Monthly: $500 | Target: Dec 2026
   On track: Yes ✅

2. House Down Payment (High Priority)
   $8,000 / $40,000 ████░░░░░░░░░░░░░░░░ 20%
   Monthly: $800 | Target: Dec 2027
   Behind: Need $1,200/month ⚠️

3. Credit Card Debt (High Priority)
   $3,500 paid / $12,000 ██████░░░░░░░░░░░░░░ 29%
   Monthly: $500 | Balance: $8,500

Total progress: 24%
```

### Get Savings Recommendations

```
Use goal-manager to recommend how much I should save for each goal
Income: $6,000/month
Expenses: $4,500/month
```

**Result**:
```
💰 Savings Recommendations

Disposable income: $1,500/month
Recommended allocation:

Emergency Fund: $600/month (40%)
- On track to complete in 30 months

House Down Payment: $500/month (33%)
- Will reach target in 64 months

Credit Card Debt: $300/month (20%)
- Payoff in 30 months
- Interest saved: $1,200

Vacation Fund: $100/month (7%)
- Flexible spending

Total allocated: $1,500/month
```

### Compare Debt Payoff Strategies

```
Use goal-manager to compare snowball vs avalanche for my debts:
- Credit Card A: $8,500 @ 18.99%
- Credit Card B: $3,200 @ 15.49%
- Personal Loan: $5,000 @ 8.99%
Extra payment: $400/month
```

**Result**:
```
💳 Debt Payoff Strategy Comparison

SNOWBALL METHOD (smallest first):
Total time: 39 months
Total interest: $4,890
Motivation: ⭐⭐⭐⭐⭐ (Quick wins!)

AVALANCHE METHOD (highest interest first):
Total time: 37 months
Total interest: $4,120
Interest saved: $770 💰

RECOMMENDATION: Avalanche Method
- Saves $770
- Debt-free 2 months sooner
```

## Goal Types

| Type | Description | Priority |
|------|-------------|----------|
| **Emergency Fund** | 3-6 months expenses | High |
| **Debt Payoff** | Credit cards, loans | High |
| **House Down Payment** | 20% of home price | High |
| **Retirement** | 25× annual expenses | Medium |
| **Education Fund** | College tuition | Medium |
| **Vacation** | Travel and experiences | Low |
| **Investment** | Brokerage account | Medium |
| **Other** | Custom goals | Variable |

## SMART Framework

Every goal must be:

1. **Specific**: Clear target
   - ❌ "Save money"
   - ✅ "Save $30,000 for emergency fund"

2. **Measurable**: Trackable progress
   - ❌ "Get out of debt"
   - ✅ "Pay off $12,000 credit card debt"

3. **Achievable**: Realistic given income
   - ❌ "Save $100,000 in 1 year" (on $50k income)
   - ✅ "Save $20,000 in 3 years" (feasible)

4. **Relevant**: Aligned with life priorities
   - ✅ "Emergency fund for job security"
   - ✅ "House down payment for family"

5. **Time-bound**: Clear deadline
   - ❌ "Someday"
   - ✅ "By December 31, 2026"

## Debt Payoff Strategies

### Snowball Method
**Approach**: Pay smallest balance first

**Pros**:
- Quick wins for motivation
- Simpler to see progress
- Fewer accounts to manage quickly

**Best for**:
- People who need motivation
- Similar interest rates
- Many small debts

### Avalanche Method
**Approach**: Pay highest interest rate first

**Pros**:
- Saves more money
- Mathematically optimal
- Faster total payoff

**Best for**:
- Maximizing savings
- High interest rate differences
- Long-term planners

### Comparison Tool
Agent automatically compares both methods and recommends based on:
- Total interest savings
- Time to debt-free
- Your personal situation

## Projection Modeling

Calculate "when will I reach my goal?" scenarios:

```python
# Current pace
At $500/month: 50 months (Jan 2030)

# Required pace for deadline
To hit Dec 2026: $1,050/month needed

# Accelerated pace
At $750/month: 33 months (Aug 2028)
```

## Milestone Celebrations

Automatic celebrations at key milestones:
- **25%**: "Great start! Quarter of the way there!"
- **50%**: "Halfway point! You're on fire! 🔥"
- **75%**: "Final stretch! Almost there!"
- **100%**: "🎉 Goal achieved! Time to celebrate!"

Custom milestones can also be set (e.g., every $10,000).

## Data Structure

### Goal Record
```json
{
  "id": "goal-001",
  "name": "Emergency Fund",
  "type": "emergency",
  "targetAmount": 30000.00,
  "currentAmount": 12000.00,
  "deadline": "2026-12-31",
  "priority": "high",
  "monthlyContribution": 500.00,
  "status": "in_progress",
  "createdDate": "2024-01-01",
  "milestones": [
    {"amount": 10000, "reached": true, "date": "2024-08-15"},
    {"amount": 20000, "reached": false},
    {"amount": 30000, "reached": false}
  ]
}
```

### Debt Record
```json
{
  "id": "goal-002",
  "name": "Credit Card Debt",
  "type": "debt",
  "targetAmount": 0,
  "currentAmount": 8500.00,
  "startAmount": 12000.00,
  "interestRate": 18.99,
  "minimumPayment": 250.00,
  "actualPayment": 500.00,
  "strategy": "avalanche"
}
```

## Installation

```bash
# Plugin is ready to use
# Create your first goal using goal-manager
# Update progress regularly for accurate projections
```

## Design Decisions

**Model Choice**: Haiku
- Goal tracking is deterministic (math calculations)
- No complex judgment needed
- Fast response for quick updates
- Cost savings: ~90% cheaper than Sonnet
- Perfect for template-based outputs

**Tools**: Read, Write, Bash
- Read: Load goals database
- Write: Save updates
- Bash: Run Python calculations for projections

**Data Format**: JSON
- Simple structure for goals
- Easy to track progress over time
- Supports complex debt calculations

## Requirements Met

✅ SMART goal framework
✅ Multiple goal tracking (emergency, house, retirement, debt)
✅ Progress bars and visualization
✅ Projection modeling (when will I reach goal?)
✅ Automated savings recommendations
✅ Debt payoff optimization (snowball vs avalanche)

## Integration with Other Plugins

**receipt-processor** (#105):
- Expense data informs savings capacity
- Discretionary spending analysis

**portfolio-tracker** (#106):
- Investment goals aligned with portfolio
- Retirement goal tracking

**bill-reminder** (#104):
- Budget awareness for goal contributions
- Fixed expenses inform savings capacity

## Future Enhancements

- Automatic goal creation from income/expenses
- Goal prioritization algorithm
- Emergency scenario planning
- Retirement calculator (4% rule)
- College cost estimator
- Home affordability calculator
- Goal sharing/accountability partners
- Historical progress charts

## Troubleshooting

**Goal not progressing**:
- Check monthly contribution amount
- Verify progress updates are being logged
- Review budget for savings capacity

**Behind schedule**:
- Increase monthly contribution
- Extend deadline
- Adjust target amount
- Review expenses for savings opportunities

**Debt not decreasing**:
- Ensure payment exceeds minimum
- Check interest rate
- Consider balance transfer
- Review spending to avoid new debt

---

**Version**: 1.0.0
**Model**: Haiku (cost-optimized)
**Status**: Production-ready
