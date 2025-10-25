# Payment Tracking Skill

AR aging, payment status management, and DSO calculation.

## AR Aging Framework

### Aging Bucket Classification
- **Current (0-30 days)**: Normal payment period, no action needed
- **31-60 days**: Slightly overdue, Tier 1 reminder
- **61-90 days**: Overdue, Tier 2 escalated reminder
- **91-120 days**: Seriously overdue, Tier 3 final notice
- **120+ days**: Collections consideration

### DSO Calculation
```
DSO = (Accounts Receivable / Total Credit Sales) × Days in Period

Example:
AR: $50,000
Credit Sales (last 30 days): $75,000
DSO = ($50,000 / $75,000) × 30 = 20 days

Interpretation:
- DSO < Payment Terms: Good (DSO 20 when terms are Net 30)
- DSO = Payment Terms: Acceptable
- DSO > Payment Terms: Poor, collection issues
```

## Payment Status Lifecycle

**PENDING** → **DUE** → **PAID**
            ↓         ↓
       **OVERDUE** **PARTIAL**
            ↓
       **DISPUTED** or **COLLECTIONS**

### Status Definitions
- **PENDING**: Invoice sent, payment not yet due
- **DUE**: Payment due date reached, no payment
- **PARTIAL**: Partial payment received, balance outstanding
- **PAID**: Full payment received and reconciled
- **OVERDUE**: Payment past due date
- **DISPUTED**: Customer raised billing dispute
- **WRITTEN_OFF**: Uncollectible
- **CREDITED**: Invoice voided/credited

## Payment Reconciliation

### Matching Rules
**Priority 1 - Exact Match** (auto-reconcile):
- Invoice number in payment reference
- Exact amount match
- Customer ID match

**Priority 2 - Partial Match** (suggest for approval):
- Amount matches one invoice
- Customer match, no invoice reference

**Priority 3 - Manual Review**:
- Amount doesn't match any invoice
- Multiple possible matches

### Overpayment Handling
1. Identify overpayment amount
2. Check for other outstanding invoices
3. Options:
   - Apply to oldest invoice first
   - Create customer credit
   - Refund excess

### Underpayment Handling
1. Calculate shortfall
2. Mark invoice PARTIAL
3. Track remaining balance
4. Create follow-up task
