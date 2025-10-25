# Invoice Generation Skill

Comprehensive patterns for professional, compliant invoice generation.

## Professional Invoice Structure

### Header Section
- Company logo and branding
- Legal business name and entity type (LLC, Inc, Corp)
- Complete business address with jurisdiction
- Tax identification numbers (EIN for US, VAT/GST for international)
- Contact information (phone, email, website)
- **Invoice number**: Sequential numbering system (INV-YYYY-NNNNN)
- **Invoice date**: Date invoice created
- **Due date**: Based on payment terms
- **Payment terms**: Net 30, Net 60, 2/10 Net 30, etc.

### Customer Information
- **Bill-to**: Legal entity name and billing address
- **Ship-to**: Delivery address (if different from billing)
- Customer account number
- Payment terms reference
- Purchase order number (if applicable)
- Tax exempt status and certificate number

### Line Item Detail
Each line item must include:
- Line number (sequential)
- Description (clear, specific)
- Quantity
- Unit of measure (hours, units, licenses, etc.)
- Unit price
- Extended amount (quantity × unit price)
- Taxable flag (yes/no)
- Tax rate and amount
- GL account code (for accounting integration)
- Revenue recognition category

**Description Standards**:
- Be specific: "Professional Services - Web Development, January 2025" not "Services"
- Include dates/periods: "Annual Subscription (Jan 1 - Dec 31, 2025)"
- Reference work: "Project Phoenix - Phase 2 Implementation"

### Summary Section
Calculation order (critical for accuracy):
1. **Subtotal**: Sum of all line item extended amounts
2. **Discount**: Apply percentage or fixed amount discount
3. **Taxable Amount**: Subtotal minus non-taxable items
4. **Tax**: Calculate on taxable amount per jurisdiction
5. **Total Amount Due**: Subtotal - Discount + Tax
6. **Currency**: Clearly specify (USD, EUR, GBP, etc.)

### Footer Section
- Payment methods accepted (ACH, wire, credit card, check)
- Remittance instructions (bank details, mailing address)
- Payment terms (e.g., "Payment due within 30 days of invoice date")
- Late payment terms ("1.5% monthly interest on overdue balances")
- Early payment discount ("2% discount if paid within 10 days")
- Dispute deadline ("Disputes must be raised within 30 days")
- Customer service contact
- Terms and conditions reference

## Tax Calculation Framework

### Sales Tax (US)
**Nexus Determination**:
- Physical presence (office, warehouse, employee)
- Economic nexus (revenue/transaction thresholds by state)
- Marketplace facilitator rules

**Rate Application**:
```
Customer address: San Francisco, CA 94102
State rate: 7.25%
County rate: 0%
City rate: 0%
District rate: 1.5%
Total rate: 8.75%
```

**Tax-Exempt Handling**:
- Require valid exemption certificate
- Verify certificate expiration
- Match certificate to customer and jurisdiction
- Document exemption reason (resale, nonprofit, government)
- Maintain certificate file for audit

### VAT/GST (International)
**VAT Calculation**:
- Standard rate: 20% (UK), 19% (Germany), varies by country
- Reduced rates for specific goods/services
- Zero-rated vs. exempt distinction

**Reverse Charge Mechanism**:
- B2B sales to VAT-registered customers in other EU countries
- Customer pays VAT, not seller
- Invoice must state "Reverse charge applies"
- Include customer VAT number

**Export Documentation**:
- Proof of export required for zero-rating
- Commercial invoice
- Shipping documentation
- Customs declarations

## Revenue Recognition Integration (ASC 606)

### Performance Obligation Tagging
Each invoice line item must specify:
```json
{
  "performance_obligation_id": "PO-001",
  "description": "Software License",
  "recognition_type": "point_in_time",
  "recognition_trigger": "delivery",
  "allocated_value": 10000.00,
  "contract_reference": "CONTRACT-2025-001"
}
```

### Recognition Types

**Point-in-Time** (recognize upon delivery):
- Product sales
- One-time services
- Software licenses (when delivered)
- Triggers: delivery, customer acceptance, title transfer

**Over-Time** (recognize throughout service period):
- Subscriptions
- Maintenance contracts
- Long-term services
- Triggers: time elapsed, milestones achieved, percentage complete

### Deferred Revenue Calculation
```
Annual subscription: $12,000 paid upfront on Jan 1

Journal entries:
Jan 1:
  DR Cash                      $12,000
     CR Deferred Revenue               $12,000

Monthly (Jan 31, Feb 28, etc.):
  DR Deferred Revenue         $1,000
     CR Revenue                        $1,000
```

## Billing Terms Library

### Standard Payment Terms

**Net 30**: Full payment due 30 days from invoice date
- Most common for B2B
- Provides working capital to customer
- Standard credit check required

**Net 60**: Full payment due 60 days from invoice date
- Large enterprise customers
- Longer sales cycles
- Stronger credit requirements

**Net 15**: Full payment due 15 days from invoice date
- Faster cash collection
- New or risky customers
- Smaller transactions

**Due on Receipt**: Payment immediately due
- Cash-on-delivery scenarios
- High-risk customers
- Small transactions

**2/10 Net 30**: 2% discount if paid within 10 days, otherwise due in 30
- Incentivizes early payment
- Effective annual interest rate: ~36%
- Improves cash flow

**EOM (End of Month)**: Payment due at end of month
- Invoices issued during month due on last day
- Simplifies payment processing
- Common in certain industries

### Installment Plans
Used for high-value invoices:
```
Total: $30,000
Terms: 3 monthly installments

Invoice 1: $10,000 due on delivery
Invoice 2: $10,000 due 30 days later
Invoice 3: $10,000 due 60 days later

Or: Single invoice with payment schedule
```

**Include**:
- Number of payments
- Payment amounts (equal or custom)
- Payment dates (specific dates or intervals)
- Interest charges (if applicable)
- Default consequences

### Progress Billing
For long-term projects:
```
Project total: $100,000
Terms: Bill based on milestones

Invoice 1 (Kickoff): 20% = $20,000
Invoice 2 (Design Complete): 30% = $30,000
Invoice 3 (Development Complete): 30% = $30,000
Invoice 4 (Final Delivery): 20% = $20,000
```

**Retainage**: Withhold 10% until project completion/acceptance

## Multi-Format Output Standards

### PDF Format (Customer-Facing)
**Design Requirements**:
- Professional template with branding
- Clear typography (sans-serif, 10-12pt body)
- Logical visual hierarchy
- White space for readability
- Print-ready (8.5x11" or A4)
- Email-optimized file size (<1MB)

**Technical Specs**:
- PDF/A-1b for archival
- Embedded fonts
- 300 DPI for printing
- Searchable text (not image-only)
- Digital signature support

### Excel Format (Accounting Import)
**Structure**:
```
Sheet 1: Invoice Header
- Invoice number, date, customer, terms, totals

Sheet 2: Line Items
- Line-by-line detail with GL codes

Sheet 3: Summary
- Subtotal, tax, discount, total breakdown
```

**GL Account Mapping**:
- Each line item linked to chart of accounts
- Debit/credit account specifications
- Cost center or project codes
- Revenue recognition tags

### JSON Format (API/Integration)
**Complete Invoice Object**:
```json
{
  "invoice_number": "INV-2025-00001",
  "invoice_date": "2025-01-15",
  "due_date": "2025-02-14",
  "customer": {
    "id": "CUST-001",
    "name": "Acme Corporation",
    "billing_address": {...}
  },
  "line_items": [...],
  "summary": {
    "subtotal": 10000.00,
    "tax": 875.00,
    "total": 10875.00
  },
  "audit_trail": {...}
}
```

### XML Format (EDI/B2B)
**Standards**:
- UBL (Universal Business Language) 2.1
- EDIFACT INVOIC
- Partner-specific schemas

**Validation**:
- XML schema validation
- Business rule validation
- Partner certification requirements

## Audit Trail Requirements

Every invoice must log:
```json
{
  "audit_trail": {
    "created_by": "invoice-generator",
    "created_at": "2025-01-15T10:30:00Z",
    "created_by_user": "john@company.com",
    "approved_by": "manager@company.com",
    "approved_at": "2025-01-15T11:00:00Z",
    "sent_at": "2025-01-15T11:15:00Z",
    "sent_via": "email",
    "sent_to": "billing@acmecorp.com",
    "source_document": "PO-2025-123",
    "contract_reference": "CONTRACT-2024-456",
    "revenue_schedule_id": "SCHED-2025-001",
    "modifications": [
      {
        "timestamp": "2025-01-15T14:00:00Z",
        "changed_by": "john@company.com",
        "change_type": "correction",
        "reason": "Updated tax rate",
        "previous_total": 10850.00,
        "new_total": 10875.00
      }
    ]
  }
}
```

## Error Prevention Checklist

Before generating invoice:
- [ ] Customer information verified (name, address, tax ID)
- [ ] All line items have descriptions, quantities, prices
- [ ] Tax jurisdiction determined correctly
- [ ] Tax exemption certificate validated (if applicable)
- [ ] Payment terms specified
- [ ] Revenue recognition type determined
- [ ] Contract/PO reference included
- [ ] All calculations verified (subtotal, tax, total)
- [ ] Invoice number sequential (no gaps/duplicates)
- [ ] GL accounts mapped correctly
- [ ] Audit trail complete

## Quality Standards

**Professional Appearance**:
- Consistent formatting
- No typos or grammatical errors
- Clear, readable layout
- Professional branding
- Contact information prominent

**Accuracy**:
- All calculations correct
- Tax rates current and accurate
- Customer information complete
- Line item descriptions specific
- Payment terms clear

**Compliance**:
- Meets legal requirements for jurisdiction
- Includes all required tax information
- Revenue recognition properly tagged
- Audit trail complete
- SOX controls followed
