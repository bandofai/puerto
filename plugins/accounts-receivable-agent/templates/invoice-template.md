# Invoice Template

Use this template for generating professional invoices.

---

# INVOICE

**From:**
[Your Company Name]
[Street Address]
[City, State ZIP]
Tax ID: [EIN/Tax ID Number]

**To:**
[Customer Company Name]
[Billing Street Address]
[City, State ZIP]
Customer ID: [CUST-####]

---

**Invoice #:** INV-YYYY-####
**Date:** [Invoice Date]
**Due Date:** [Due Date]
**Payment Terms:** [Net 30 | Net 15 | 2/10 Net 30 | etc.]
**PO #:** [Purchase Order Number] *(if applicable)*

---

## Line Items

| Item | Description | Quantity | Unit Price | Amount |
|------|-------------|----------|------------|--------|
| 001 | [Service/Product Description] | [Qty] | $[Price] | $[Amount] |
| 002 | [Service/Product Description] | [Qty] | $[Price] | $[Amount] |
| 003 | [Service/Product Description] | [Qty] | $[Price] | $[Amount] |

---

## Summary

| | |
|---|---|
| **Subtotal** | $[Subtotal] |
| **Discount ([X]%)** | -$[Discount] |
| **Subtotal After Discount** | $[Subtotal After Discount] |
| **Sales Tax ([X]%)** | $[Tax Amount] |
| **Shipping** | $[Shipping] |
| **TOTAL DUE** | **$[Total Amount]** |

---

## Payment Information

**Payment Methods:** Check, ACH, Wire Transfer, Credit Card

**ACH/Wire Details:**
- Bank: [Bank Name]
- Routing: [Routing Number]
- Account: [Account Number]
- Swift: [Swift Code] *(for international)*

**Check Payable To:**
[Your Company Name]
[Mailing Address]
[City, State ZIP]

**Credit Card:**
Visit: [Online Payment URL]

---

## Notes

- [Any special payment terms or early payment discounts]
- [Late payment fees if applicable: e.g., "Late payment fee of 1.5% per month applies to overdue balances"]
- Please include invoice number with payment

**Questions?** Contact [email@company.com] or call [Phone Number]

Thank you for your business!

---

## Calculation Formulas

**Line Item Amount:**
```
Amount = Quantity × Unit Price
```

**Subtotal:**
```
Subtotal = Sum of all Line Item Amounts
```

**Discount:**
```
Discount Amount = Subtotal × Discount Percentage
Subtotal After Discount = Subtotal - Discount Amount
```

**Tax:**
```
Tax Amount = Subtotal After Discount × Tax Rate
```

**Total:**
```
Total = Subtotal After Discount + Tax + Shipping
```

---

## Payment Terms Reference

| Term | Description | Due Date Calculation |
|------|-------------|---------------------|
| **Net 30** | Due in 30 days | Invoice Date + 30 days |
| **Net 15** | Due in 15 days | Invoice Date + 15 days |
| **Due on Receipt** | Immediate payment | Invoice Date |
| **2/10 Net 30** | 2% discount if paid in 10 days, else due in 30 | Discount until: Invoice Date + 10 days<br>Due: Invoice Date + 30 days |
| **1/15 Net 45** | 1% discount if paid in 15 days, else due in 45 | Discount until: Invoice Date + 15 days<br>Due: Invoice Date + 45 days |
| **EOM** | End of month | Last day of invoice month |

---

## Tax Rates by Jurisdiction

**US Sales Tax (Examples)**:
- California: 7.25% (state) + local
- New York: 4.00% (state) + local
- Texas: 6.25%
- Washington: 6.50%

**VAT (International)**:
- UK: 20%
- Germany: 19%
- France: 20%
- Canada (GST): 5%

*Note: Always verify current tax rates for your jurisdiction*

---

## Invoice Number Format

**Recommended**: `INV-YYYY-####`

Example:
- INV-2025-0001 (First invoice of 2025)
- INV-2025-0002 (Second invoice of 2025)

**Sequential numbering ensures**:
- Easy tracking
- Audit compliance
- No duplicate invoices
- Clear chronological order
