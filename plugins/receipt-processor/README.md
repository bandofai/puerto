# Receipt Processor Plugin

Receipt processing and expense categorization specialist with OCR capabilities.

## Overview

Never lose a receipt again. This plugin uses OCR to extract data from receipt images, auto-categorizes expenses, flags tax-deductible items, and creates a searchable digital archive.

## Agent

### receipt-analyzer (Sonnet)
**Description**: PROACTIVELY processes receipt images with OCR and auto-categorization

**Capabilities**:
- OCR text extraction from photos/PDFs
- Merchant identification and item parsing
- Auto-categorization (9 expense categories)
- Tax-deductible flagging
- Digital archive with searchable index
- Monthly expense summaries
- Tax preparation export

**Use When**:
- Processing receipt images
- Categorizing expenses
- Searching for specific receipts
- Generating monthly summaries
- Preparing for tax season

**Tools**: Read, Write, Bash

## Features

✅ **OCR Capability**: Extract text from receipt images and PDFs
✅ **Auto-Categorization**: 9 expense categories with smart matching
✅ **Tax-Deductible Flagging**: Automatically identify deductible expenses
✅ **Digital Archive**: Organized by year and month
✅ **Searchable Index**: Find receipts by merchant, category, or item
✅ **Monthly Summaries**: Spending breakdown by category
✅ **Tax Export**: Year-end summary for tax preparation

## Usage Examples

### Process a Receipt Image

```
Use receipt-analyzer to process this receipt:
[Upload image: ~/Downloads/whole-foods-receipt.jpg]
```

**Result**:
```
✅ Receipt processed: Whole Foods

Date: Nov 15, 2025
Total: $87.42
Category: Groceries
Tax-deductible: No

Items: 8 items extracted
Saved: data/receipts/processed/2025-11/receipt-001.jpg
```

### Generate Monthly Summary

```
Use receipt-analyzer to show my November 2025 expense summary
```

**Result**:
```
📊 November 2025 Expenses

Groceries          $423.89
Dining             $287.50
Transportation     $156.32
Utilities          $245.00
Entertainment      $89.99

Total: $1,202.70
Tax-deductible: $45.00 (3.7%)
```

### Search Receipts

```
Use receipt-analyzer to find all coffee purchases
```

**Result**:
```
🔍 Search: "coffee"

Nov 10 - Starbucks - $5.99 (Dining)
Nov 12 - Blue Bottle - $8.50 (Dining)
Nov 15 - Whole Foods - $12.99 (Groceries - coffee beans)

3 results found
Total: $27.48
```

### Export for Taxes

```
Use receipt-analyzer to export all tax-deductible expenses for 2025
```

**Result**: JSON file with all business expenses, medical costs, and charitable donations

## Categories

| Category | Examples | Tax-Deductible |
|----------|----------|----------------|
| **Groceries** | Whole Foods, Safeway, Kroger | No |
| **Dining** | Restaurants, cafes, Starbucks | No |
| **Transportation** | Gas, Uber, parking, tolls | No |
| **Shopping** | Amazon, Target, clothing | No |
| **Healthcare** | CVS, prescriptions, doctors | Yes* |
| **Utilities** | Electric, internet, phone | No |
| **Entertainment** | Netflix, movies, concerts | No |
| **Business** | Office supplies, software | Yes |
| **Travel** | Hotels, flights, rental cars | Sometimes |

\* Medical expenses above 7.5% of AGI are deductible

## OCR Capabilities

The agent uses Claude's vision capabilities to read:
- **Receipt photos** (JPG, PNG)
- **Scanned receipts** (PDF)
- **Screenshots** of digital receipts
- **Email receipts** (as images)

**Extracted Information**:
- Merchant name and location
- Transaction date and time
- Individual items with prices
- Subtotal, tax, total
- Payment method
- Tip (if applicable)

## Data Structure

### Receipt Record
```json
{
  "id": "receipt-001",
  "merchant": "Whole Foods",
  "date": "2025-11-15",
  "total": 87.42,
  "tax": 7.89,
  "category": "groceries",
  "subcategory": "food",
  "paymentMethod": "credit",
  "taxDeductible": false,
  "items": [
    {
      "description": "Organic bananas",
      "quantity": 1,
      "price": 3.99
    }
  ],
  "imagePath": "data/receipts/processed/2025-11/receipt-001.jpg",
  "processed": "2025-11-15T10:30:00Z"
}
```

## Tax-Deductible Categories

**Business Expenses**:
- Office supplies
- Software subscriptions
- Equipment
- Conference fees
- Business meals (50% deductible)

**Medical Expenses** (>7.5% AGI):
- Prescriptions
- Doctor visits
- Medical equipment
- Insurance premiums

**Charitable Donations**:
- Cash donations
- Goods donations

**Home Office**:
- Proportional utilities
- Office equipment
- Furniture

## Installation

```bash
# Plugin is ready to use
# Upload receipts to: plugins/receipt-processor/data/receipts/incoming/
# Processed receipts saved to: data/receipts/processed/
```

## Workflow

1. **Upload receipt** image to incoming folder or share directly
2. **Agent processes** with OCR and extracts data
3. **Auto-categorizes** based on merchant and items
4. **Flags tax-deductible** items automatically
5. **Saves to archive** organized by year-month
6. **Updates searchable index** for easy retrieval

## Design Decisions

**Model Choice**: Sonnet
- OCR requires vision capabilities (Sonnet or Opus)
- Merchant/category matching needs judgment
- Item parsing benefits from context understanding
- Cost: ~$0.015/1K tokens (worth it for accuracy)

**Tools**: Read, Write, Bash
- Read: Process images with vision capability
- Write: Save receipt data and updates
- Bash: Run Python scripts for summaries

**Data Organization**: By Year-Month
- Easy to find receipts by date
- Natural tax year organization
- Auto-archive old receipts

## Requirements Met

✅ OCR text extraction from photos/PDFs
✅ Merchant identification
✅ Item-level parsing
✅ Auto-categorization (9 categories)
✅ Tax-deductible flagging
✅ Digital archive with searchable index
✅ Monthly expense summaries

## Integration with Other Plugins

**tax-preparation-assistant** (#108):
- Provides organized expense data
- Exports tax-deductible receipts
- Year-end summaries

**expense-manager**:
- Receipt data feeds into budgets
- Spending trends analysis
- Category-based alerts

## Future Enhancements

- Email receipt forwarding (receipts@yourdomain.com)
- Mobile app integration
- Bulk receipt processing
- Duplicate detection
- Expense policy violations
- Budget alerts
- Multi-currency support
- Mileage tracking from gas receipts

## Troubleshooting

**OCR not working**:
- Ensure image is clear and readable
- Good lighting on receipt
- Receipt not crumpled or faded

**Wrong category**:
- Manually recategorize
- Add merchant to category rules
- Update category keywords

**Missing items**:
- OCR may miss items if receipt is faded
- Manually add key items if needed

**Duplicate receipts**:
- Agent checks date, merchant, total
- Prompts for confirmation if match found

---

**Version**: 1.0.0
**Model**: Sonnet (vision-capable)
**Status**: Production-ready
