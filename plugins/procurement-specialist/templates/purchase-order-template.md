# Purchase Order Template

**Note**: This is a markdown template representing an Excel/spreadsheet structure. Convert to XLSX format for actual use with formulas and formatting.

---

## PURCHASE ORDER

**PO Number**: PO-[YYYY]-[NNNN]
**Date**: [MM/DD/YYYY]
**Status**: [Draft / Pending Approval / Approved / Issued / Received / Closed / Cancelled]

---

### VENDOR INFORMATION

| Field | Value |
|-------|-------|
| **Vendor Name** | [Legal business name] |
| **Vendor ID** | [Vendor ID if applicable] |
| **Address** | [Street address] |
| | [City, State ZIP] |
| **Contact Person** | [Name] |
| **Phone** | [Phone number] |
| **Email** | [Email address] |
| **Vendor Tax ID** | [Tax ID / EIN] |

---

### BUYER INFORMATION

| Field | Value |
|-------|-------|
| **Company** | [Your company name] |
| **Department** | [Department name] |
| **Buyer Name** | [Buyer name] |
| **Title** | [Buyer title] |
| **Email** | [Buyer email] |
| **Phone** | [Phone number] |

---

### SHIPPING INFORMATION

| Field | Value |
|-------|-------|
| **Ship To** | [Company/Department] |
| | [Street address] |
| | [City, State ZIP] |
| **Attention** | [Recipient name] |
| **Phone** | [Recipient phone] |
| **Delivery Required By** | [Date] |
| **Delivery Method** | [Standard / Express / Freight / Other] |
| **Special Instructions** | [Any special handling, delivery notes, or requirements] |

---

### BILLING INFORMATION

| Field | Value |
|-------|-------|
| **Bill To** | [Company name] |
| | [Billing address] |
| | [City, State ZIP] |
| **AP Contact** | [Accounts Payable contact name] |
| **AP Email** | [AP email address] |
| **AP Phone** | [AP phone number] |
| **Payment Terms** | [Net 30 / Net 60 / Due on receipt / Other] |
| **Payment Method** | [Check / ACH / Wire / Credit card] |
| **Budget Code** | [Cost center or budget code] |
| **Project Code** | [Project code if applicable] |

---

### LINE ITEMS

| Line | Item/Part Number | Description | Quantity | Unit | Unit Price | Total |
|------|-----------------|-------------|----------|------|------------|-------|
| 1 | [Item # or SKU] | [Detailed description of item] | [Qty] | [ea/box/case/lb] | $[X.XX] | $[XX.XX] |
| 2 | [Item # or SKU] | [Detailed description of item] | [Qty] | [ea/box/case/lb] | $[X.XX] | $[XX.XX] |
| 3 | [Item # or SKU] | [Detailed description of item] | [Qty] | [ea/box/case/lb] | $[X.XX] | $[XX.XX] |
| 4 | [Item # or SKU] | [Detailed description of item] | [Qty] | [ea/box/case/lb] | $[X.XX] | $[XX.XX] |
| 5 | [Item # or SKU] | [Detailed description of item] | [Qty] | [ea/box/case/lb] | $[X.XX] | $[XX.XX] |

**Excel Formula for Total**: `=Quantity * Unit_Price`

---

### PRICING SUMMARY

| | Amount |
|---|---|
| **Subtotal** | $[X,XXX.XX] |
| **Shipping & Handling** | $[XXX.XX] |
| **Tax** ([X]%) | $[XXX.XX] |
| **Discount** ([X]%) | -$[XXX.XX] |
| **Other Charges** | $[XXX.XX] |
| **TOTAL** | **$[X,XXX.XX]** |

**Excel Formulas**:
- Subtotal: `=SUM(Line_Item_Totals)`
- Tax: `=(Subtotal + Shipping) * Tax_Rate`
- Total: `=Subtotal + Shipping + Tax - Discount + Other_Charges`

---

### TERMS AND CONDITIONS

1. **Acceptance**: Vendor acceptance of this PO constitutes agreement to all terms herein.

2. **Delivery**: Vendor must deliver items by the required date specified. If unable to meet delivery date, vendor must notify buyer immediately.

3. **Quality**: All items must meet specifications and be in merchantable condition. Items not meeting specifications will be rejected and returned at vendor's expense.

4. **Invoicing**: Invoice must reference this PO number and be sent to the billing address above. Invoice should be itemized matching line items on this PO.

5. **Payment**: Payment will be made per the payment terms specified above, subject to receipt and acceptance of goods/services.

6. **Inspection**: Buyer reserves the right to inspect goods upon delivery. Acceptance is subject to final inspection and verification.

7. **Changes**: No changes to this PO are valid without written amendment authorized by buyer.

8. **Cancellation**: Buyer may cancel this PO if vendor fails to deliver per terms, or for convenience with reasonable notice and payment for work completed.

9. **Warranties**: Vendor warrants that goods are new, merchantable, fit for intended purpose, and free from defects.

10. **Liability**: Each party shall be liable for damages caused by its negligence or breach of contract, subject to applicable limitations.

**Special Terms**: [Any additional terms specific to this purchase, such as:
- Return policy
- Warranty terms
- Service level agreements
- Liquidated damages
- Specific delivery requirements]

---

### APPROVALS

| Role | Name | Status | Date | Signature/Email |
|------|------|--------|------|-----------------|
| **Requisitioner** | [Name] | Approved | [Date] | [Signature or email confirmation] |
| **Budget Owner** | [Name] | [Pending/Approved/Rejected] | [Date] | [Signature or email] |
| **Procurement** | [Name] | [Pending/Approved/Rejected] | [Date] | [Signature or email] |
| **Finance** | [Name] | [Pending/Approved/Rejected] | [Date] | [Signature or email] |
| **[Other]** | [Name] | [Pending/Approved/Rejected] | [Date] | [Signature or email] |

**Approval Threshold**: This PO requires approval based on amount of $[Total] per company policy:
- < $1,000: Department manager only
- $1,000 - $5,000: Manager + Procurement
- $5,000 - $25,000: Director + Procurement + Finance
- $25,000+: VP + CFO

---

### TRACKING INFORMATION

| Field | Value |
|-------|-------|
| **Requisition Number** | [REQ-YYYY-NNNN] |
| **Quote/Proposal Reference** | [Quote # if applicable] |
| **Contract Number** | [Contract # if under existing contract] |
| **RFP/RFQ Number** | [RFP/RFQ # if applicable] |
| | |
| **Order Placed Date** | [Date PO sent to vendor] |
| **Vendor Confirmation** | [Date vendor confirmed receipt and acceptance] |
| **Vendor Confirmation #** | [Vendor's sales order or confirmation number] |
| | |
| **Expected Ship Date** | [Date vendor will ship] |
| **Expected Delivery Date** | [Date items expected to arrive] |
| **Actual Ship Date** | [Date items actually shipped] |
| **Actual Delivery Date** | [Date items actually received] |
| | |
| **Tracking Number** | [Carrier tracking number] |
| **Carrier** | [UPS / FedEx / USPS / Freight carrier] |
| **Carrier Website** | [Tracking URL if applicable] |

---

### RECEIVING INFORMATION

| Field | Value |
|-------|-------|
| **Received By** | [Name of person who received items] |
| **Date Received** | [Date items received] |
| **Time Received** | [Time if relevant] |
| **Condition** | [Good / Damaged / Partial / See notes] |
| **Quantity Received** | [Actual quantity received - note if different from ordered] |
| **Discrepancies** | [Any missing items, damages, or issues] |
| **Photos/Documentation** | [Reference to any photos or documentation] |
| **Receiving Notes** | [Any additional notes about the receipt] |

**Inspection Results**:
- [ ] All items received as ordered
- [ ] Items inspected and acceptable
- [ ] Discrepancies noted and communicated to vendor
- [ ] Receiving documentation filed

---

### INVOICE AND PAYMENT INFORMATION

| Field | Value |
|-------|-------|
| **Invoice Number** | [Vendor invoice number] |
| **Invoice Date** | [Date of invoice] |
| **Invoice Amount** | $[Amount] |
| **Invoice Received Date** | [Date we received invoice] |
| **Invoice Matched to PO** | [Yes / No / Discrepancies noted] |
| **Discrepancies** | [Any differences between invoice and PO] |
| | |
| **Payment Approved By** | [Name] |
| **Payment Approved Date** | [Date] |
| **Payment Due Date** | [Date based on payment terms] |
| **Payment Date** | [Date payment made] |
| **Payment Method** | [Check / ACH / Wire / Card] |
| **Payment Reference** | [Check #, ACH confirmation, etc.] |
| **Payment Amount** | $[Amount paid] |

---

### NOTES AND COMMENTS

**Internal Notes**:
[Any internal notes, comments, or history related to this PO]

**Vendor Communications**:
- [Date]: [Summary of communication]
- [Date]: [Summary of communication]

**Issue Log**:
- [Date]: [Issue description and resolution]

**Change History**:
- [Date]: [Description of any changes or amendments]

---

### ATTACHMENTS AND REFERENCES

**Documents Attached**:
- [ ] Requisition form
- [ ] Quote from vendor
- [ ] Specifications or drawings
- [ ] Contract or agreement
- [ ] RFP/RFQ documents
- [ ] Other: [Description]

**File Locations**:
- Requisition: [File path or link]
- Quote: [File path or link]
- Contract: [File path or link]
- Other: [File path or link]

---

### ADMINISTRATIVE INFORMATION

| Field | Value |
|-------|-------|
| **Created By** | [Name of person who created PO] |
| **Created Date** | [Date PO created] |
| **Last Updated By** | [Name of last person to update] |
| **Last Updated Date** | [Date of last update] |
| **PO Version** | [Version number if amended] |
| **Retention Date** | [Date PO can be archived per policy] |

---

## PURCHASE ORDER AMENDMENT

**Note**: Use this section if PO needs to be amended after issuance

**Amendment Number**: [PO Number]-AMD-[N]
**Amendment Date**: [Date]
**Reason for Amendment**: [Description of why amendment is needed]

### Changes

| Item | Original Value | Changed To | Reason |
|------|---------------|------------|--------|
| [Field name] | [Old value] | [New value] | [Reason for change] |
| [e.g., Line 1 Quantity] | 100 | 150 | Increased order due to higher demand |
| [e.g., Delivery Date] | 03/15/2025 | 03/22/2025 | Vendor requested extension |
| [e.g., Line 3] | [Description] | [DELETED] | Item no longer needed |
| [e.g., Line 6] | [NEW ITEM] | 50 ea @ $25 = $1,250 | Additional item added |

### Revised Pricing Summary

| | Original PO | Revised PO | Change |
|---|---|---|---|
| **Subtotal** | $[X,XXX.XX] | $[X,XXX.XX] | $[+/- XXX.XX] |
| **Shipping** | $[XXX.XX] | $[XXX.XX] | $[+/- XX.XX] |
| **Tax** | $[XXX.XX] | $[XXX.XX] | $[+/- XX.XX] |
| **TOTAL** | $[X,XXX.XX] | **$[X,XXX.XX]** | **$[+/- XXX.XX]** |

### Re-Approval Required?

**Re-approval needed**: [Yes / No]
- If amount increased and exceeds original approval authority: **Yes**
- If amount decreased or non-financial change: **No** (notify approvers)

| Role | Name | Status | Date |
|------|------|--------|------|
| Buyer | [Name] | Approved | [Date] |
| Budget Owner | [Name] | [Pending/Approved] | [Date] |
| [Other if needed] | [Name] | [Pending/Approved] | [Date] |

**Vendor Notified**: [Date amendment sent to vendor]
**Vendor Acceptance**: [Date vendor accepted amendment]

---

## Alternative PO Format: Services Purchase Order

**Use this format for professional services instead of goods**

### SERVICE DETAILS

| Field | Value |
|-------|-------|
| **Service Type** | [Consulting / Implementation / Support / Other] |
| **Statement of Work** | [Reference to SOW document or brief description] |
| **Service Period** | [Start date] to [End date] |
| **Service Location** | [On-site / Remote / Hybrid] |
| **Estimated Hours** | [Total hours or range] |

### SERVICE LINE ITEMS

| Line | Resource/Role | Description | Hours/Days | Rate | Total |
|------|--------------|-------------|-----------|------|-------|
| 1 | [Senior Consultant] | [Project management and oversight] | [100 hrs] | $[200/hr] | $[20,000] |
| 2 | [Consultant] | [Implementation and configuration] | [200 hrs] | $[150/hr] | $[30,000] |
| 3 | [Junior Consultant] | [Testing and documentation] | [100 hrs] | $[100/hr] | $[10,000] |

**Not-To-Exceed Amount**: $[XX,XXX.XX]
- Any work beyond this requires written approval and amendment

### DELIVERABLES

| Deliverable | Description | Due Date | Acceptance Criteria |
|-------------|-------------|----------|---------------------|
| 1. [Project Plan] | [Detailed project plan] | [Date] | [Approved by project sponsor] |
| 2. [Design Document] | [System design] | [Date] | [Reviewed and approved by IT] |
| 3. [Implementation] | [Working system] | [Date] | [Passes UAT testing] |
| 4. [Documentation] | [User and admin docs] | [Date] | [Complete and reviewed] |

### TIME & MATERIALS TERMS

**Invoicing**: Submit invoices [weekly / biweekly / monthly] with detailed time sheets

**Timesheet Requirements**:
- Date and hours worked
- Description of work performed
- Name of resource
- Approved by [designated approver]

**Payment**: Net [30] days from receipt of approved invoice

**Expenses**: [Reimbursable at cost / Not reimbursable / Reimbursable with [X]% markup]
- Approved expenses only (pre-approval required for > $[amount])
- Receipts required for all expenses

---

## Instructions for Using This Template

### For Goods Purchase Orders:

1. **Fill in header information**: PO number, date, status
2. **Enter vendor information**: Complete all vendor fields
3. **Enter buyer and shipping info**: Ensure delivery address is correct
4. **Add line items**: Include part numbers, descriptions, quantities, prices
5. **Calculate totals**: Use formulas for subtotal, tax, total
6. **Add any special terms**: Note any specific requirements
7. **Route for approvals**: Based on amount and company policy
8. **Send to vendor**: Once approved
9. **Track and receive**: Update tracking and receiving sections
10. **Process payment**: When invoice received and goods accepted

### For Services Purchase Orders:

1. Use alternative format above
2. Reference Statement of Work (SOW)
3. Include hourly rates and estimated hours
4. Define deliverables with acceptance criteria
5. Set not-to-exceed amount
6. Define invoicing and timesheet requirements

### Excel Setup Tips:

**Formulas to add**:
- Line item totals: `=Quantity * Unit_Price`
- Subtotal: `=SUM(Line_Item_Totals)`
- Tax: `=(Subtotal + Shipping) * Tax_Rate`
- Total: `=Subtotal + Shipping + Tax - Discount`

**Conditional Formatting**:
- Status: Green for Approved, Yellow for Pending, Red for Rejected/Cancelled
- Total: Red if exceeds budget
- Date: Red if delivery date is past due

**Data Validation**:
- Status: Drop-down list of valid statuses
- Unit: Drop-down list of valid units (ea, box, case, lb, etc.)
- Payment Terms: Drop-down list (Net 30, Net 60, etc.)

**Protect Sheet**:
- Lock all cells except input fields
- Allow editing only of specific ranges
- Require password to unprotect

### Approval Workflow:

**Set up approval routing based on amount**:
1. **< $1,000**: Manager approval only
2. **$1,000 - $5,000**: Manager + Procurement
3. **$5,000 - $25,000**: Director + Procurement + Finance
4. **$25,000 - $100,000**: VP + CFO
5. **> $100,000**: Executive committee

**Use status tracking**:
- Draft → Pending Approval → Approved → Issued → Received → Closed

### Best Practices:

1. **Assign PO numbers sequentially**: Don't skip numbers
2. **Reference requisition**: Always link to source requisition
3. **Be specific**: Detailed descriptions prevent confusion
4. **Document everything**: Notes, communications, changes
5. **Match invoices carefully**: Ensure invoice matches PO before paying
6. **Close POs promptly**: Close when fully received and paid
7. **Retain records**: Keep per company retention policy (typically 7 years)

---

## PO STATUS DEFINITIONS

| Status | Meaning | Who Can Set | Next Status |
|--------|---------|-------------|-------------|
| **Draft** | PO being created, not submitted | Buyer | Pending Approval |
| **Pending Approval** | Awaiting approvals | Buyer | Approved or Rejected |
| **Rejected** | Not approved, needs revision | Approver | Draft or Cancelled |
| **Approved** | All approvals obtained | Final Approver | Issued |
| **Issued** | Sent to vendor | Buyer | Received or Cancelled |
| **Received** | Goods received, awaiting payment | Receiving | Closed |
| **Closed** | Fully received and paid | AP/Buyer | (Final state) |
| **Cancelled** | PO cancelled, not proceeding | Buyer/Manager | (Final state) |

---

**Template Version**: 1.0
**Last Updated**: January 2025
**Maintained By**: Procurement Department

---

**END OF PURCHASE ORDER TEMPLATE**
