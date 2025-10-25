# Bill Payment Reminder Plugin

Bill management assistant with proactive payment reminders and deadline tracking.

## Overview

Never miss a payment again. This plugin tracks all your bills, sends multi-stage reminders, logs payments, and provides annual spending summaries.

## Agent

### bill-tracker (Haiku)
**Description**: PROACTIVELY tracks bills and sends payment reminders

**Capabilities**:
- Central database of all bills
- Automatic deadline tracking with 7/3/1-day reminders
- Payment confirmation logging
- Late payment alerts
- Recurring bill automation
- Annual cost summary by category

**Use When**:
- Adding new bills
- Checking upcoming payments
- Logging payments
- Reviewing bill history
- Getting late payment alerts

**Tools**: Read, Write, Bash

## Features

✅ **Multi-Stage Reminders**: 7 days, 3 days, 1 day before due date
✅ **Recurring Bills**: Auto-create next payment after logging
✅ **Payment History**: Track all payments with confirmation numbers
✅ **Late Alerts**: Immediate notification for overdue bills
✅ **Annual Summary**: Total spending by category
✅ **Cost-Optimized**: Haiku model for simple tracking ($0.001/1K tokens)

## Usage Examples

### Add a New Bill

```
Use bill-tracker to add electric bill:
- Name: SDG&E Electric
- Amount: $150
- Due: 15th of each month
- Category: utilities
```

**Result**: Bill added with automatic reminders set

### Check Upcoming Bills

```
Use bill-tracker to show all bills due in the next 7 days
```

**Result**:
```
📅 Upcoming Bills

Nov 15 - Electric Bill - $150.00 (3 days)
Nov 18 - Internet - $80.00 (6 days)

Total due: $230.00
```

### Log a Payment

```
Use bill-tracker to log payment for Electric Bill:
- Amount: $150
- Confirmation: CONF-789456
- Date: Nov 15, 2025
```

**Result**: Payment recorded, next month's bill auto-created

### Get Annual Summary

```
Use bill-tracker to calculate annual spending by category
```

**Result**:
```
📊 Annual Spending Summary

Utilities: $2,400
Rent: $18,000
Insurance: $1,800
Subscriptions: $600

Total: $22,800/year
```

## Bill Categories

- **utilities**: Electric, water, gas
- **rent**: Monthly rent/mortgage
- **insurance**: Car, health, life insurance
- **subscriptions**: Netflix, Spotify, etc.
- **loans**: Student, personal loans
- **credit-cards**: Credit card payments
- **other**: Miscellaneous bills

## Reminder Schedule

| Days Before | Alert Level | Example |
|-------------|-------------|---------|
| 7 days | Info | "Upcoming: Electric Bill due Nov 15 - $150" |
| 3 days | Warning | "Reminder: Electric Bill due in 3 days - $150" |
| 1 day | Urgent | "URGENT: Electric Bill due tomorrow - $150" |
| Due date | Critical | "DUE TODAY: Electric Bill - $150" |
| Overdue | Alert | "LATE: Electric Bill overdue by 2 days - $150" |

## Data Structure

### Bills Database
```json
{
  "id": "bill-001",
  "name": "Electric Bill",
  "category": "utilities",
  "amount": 150.00,
  "dueDate": "2025-11-15",
  "recurring": "monthly",
  "autoReminders": true,
  "status": "pending",
  "paymentHistory": [
    {
      "date": "2025-10-15",
      "amount": 145.00,
      "confirmationNumber": "CONF-12345"
    }
  ]
}
```

## Recurring Frequencies

- `monthly`: Every month on same day
- `quarterly`: Every 3 months
- `annual`: Once per year
- `biweekly`: Every 2 weeks
- `once`: One-time payment

## Installation

```bash
# Plugin is ready to use
# Bills database: plugins/bill-reminder/data/bills/bills.json
# Add your first bill using bill-tracker agent
```

## Design Decisions

**Model Choice**: Haiku
- Bill tracking is deterministic (date calculations, reminders)
- No complex judgment needed
- Cost savings: ~90% cheaper than Sonnet
- Fast response for quick lookups

**Tools**: Read, Write, Bash
- Read: Load bills database
- Write: Save updates
- Bash: Date calculations and formatting

**Data Format**: JSON
- Easy to read and modify
- Supports complex nested structures
- Standard format for data interchange

## Requirements Met

✅ Central database of all bills
✅ Automatic deadline tracking
✅ Multi-stage reminders (7/3/1 days)
✅ Payment confirmation logging
✅ Late payment alerts
✅ Recurring bill automation
✅ Annual cost summary

## Future Enhancements

- Email/SMS integration for reminders
- Bank account integration for auto-pay
- Budget tracking and overspending alerts
- Bill splitting for roommates
- Payment method tracking
- Late fee calculation
- Payment trend analysis

## Troubleshooting

**Bill not appearing in reminders**:
- Check `autoReminders` is true
- Verify `dueDate` is in future
- Ensure `status` is "pending"

**Dates showing incorrectly**:
- Use ISO format: YYYY-MM-DD
- Check timezone settings

**Recurring bills not auto-creating**:
- Log payment first
- Verify `recurring` field is set
- Check payment history updated

---

**Version**: 1.0.0
**Model**: Haiku (cost-optimized)
**Status**: Production-ready
