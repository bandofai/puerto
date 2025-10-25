# Expense Manager Plugin

**Comprehensive expense management automation with OCR, policy validation, and approval workflow coordination**

## Overview

The Expense Manager plugin automates the complete expense reporting lifecycle, from receipt scanning to reimbursement approval. It uses OCR to extract data from receipt images, validates expenses against company policy, and routes reports through multi-tier approval workflows with SLA tracking.

## Features

✅ **Receipt OCR**: Automatic data extraction from receipt images
✅ **Policy Compliance**: Real-time validation against company expense policies
✅ **Approval Routing**: Intelligent workflow routing based on amount and category
✅ **SLA Tracking**: Monitor approval deadlines and auto-escalate overdue items
✅ **Audit Trail**: Complete history of all actions and decisions
✅ **Multi-Format Output**: JSON, Markdown, and CSV report generation
✅ **Duplicate Detection**: Identify potential duplicate expenses
✅ **Risk Assessment**: Anomaly detection for fraud prevention

## Architecture

### 4 Specialized Agents

1. **receipt-analyzer** (Haiku - Fast & Cost-Effective)
   - OCR processing of receipt images
   - Data extraction (vendor, date, amount, category)
   - Confidence scoring
   - Batch processing support

2. **expense-processor** (Sonnet - Judgment Required)
   - Comprehensive expense report assembly
   - Policy compliance checking during processing
   - Multi-format report generation (JSON/MD/CSV)
   - Business purpose validation

3. **policy-validator** (Sonnet - Read-Only for Security)
   - Three-tier validation framework
   - Risk-based findings (Critical/High/Medium/Low)
   - Detailed remediation guidance
   - Compliance scoring

4. **approval-router** (Sonnet - Workflow Coordination)
   - Dynamic approval chain construction
   - SLA management and tracking
   - Status monitoring and notifications
   - Auto-escalation for overdue approvals

### 3 Comprehensive Skills

1. **expense-processing**: OCR best practices, receipt data extraction patterns
2. **policy-validation**: Compliance checking frameworks, risk assessment
3. **approval-workflow**: Approval routing logic, SLA management, escalation handling

### Templates

- **expense-report-template.json**: Standard expense report structure
- **policy-checklist.md**: Pre-submission compliance checklist
- **approval-workflow-state.json**: Workflow status tracking template

## Installation

### Prerequisites

**Required**:
- Claude Code CLI
- Python 3.x (for OCR processing)

**Optional but Recommended**:
- Tesseract OCR: `brew install tesseract` (macOS) or `apt-get install tesseract-ocr` (Linux)
- Python packages: `pip install pytesseract pillow`

### Install Plugin

```bash
# Copy to your Claude plugins directory
cp -r plugins/expense-manager ~/.claude/plugins/

# Or use project-level
cp -r plugins/expense-manager .claude/plugins/
```

### Verify Installation

```bash
# Check plugin structure
tree ~/.claude/plugins/expense-manager/

# Verify agents are available
# (Claude Code will automatically discover agents in the plugins directory)
```

## Usage

### Complete Workflow Example

**Step 1: Process Receipt Images**

```bash
# Place receipt images in a directory
mkdir -p ./receipts
# Add your receipt images (JPG, PNG, PDF)

# Invoke receipt-analyzer
# Claude will automatically use the agent when you mention processing receipts
```

"Please process all receipt images in ./receipts directory"

**Step 2: Create Expense Report**

After receipts are processed:

"Create a comprehensive expense report from the processed receipts for January 2025"

The expense-processor agent will:
- Load all processed receipt data
- Aggregate by category
- Check policy compliance
- Generate report in multiple formats

**Step 3: Validate Policy Compliance**

"Validate the expense report against company policy"

The policy-validator agent will:
- Run three-tier validation
- Identify violations and risks
- Generate compliance report with scores
- Provide remediation guidance

**Step 4: Submit for Approval**

If validation passes:

"Submit the expense report for approval"

The approval-router agent will:
- Build approval chain based on amount
- Route to appropriate approvers
- Set SLA deadlines
- Track approval status

**Step 5: Monitor Status**

"Check approval status for EXP-2025-001"

The approval-router will show:
- Current approval step
- Time remaining on SLA
- Approver status
- Overall progress

## Agent Details

### receipt-analyzer

**Trigger**: "Process receipt images", "Extract data from receipts", "OCR receipts"

**Capabilities**:
- OCR using Tesseract
- Automatic vendor detection
- Amount and date extraction
- Category inference
- Confidence scoring
- Batch processing

**Output**: JSON files with extracted data in `./expenses/receipts/`

**Example**:
```json
{
  "receipt_id": "receipt_20250120_001",
  "vendor": "Starbucks Coffee",
  "date": "2025-01-20",
  "amount": 15.47,
  "currency": "USD",
  "category": "Meals & Entertainment",
  "confidence_score": 0.95
}
```

### expense-processor

**Trigger**: "Create expense report", "Compile expenses", "Generate expense summary"

**Capabilities**:
- Report assembly from receipts
- Real-time policy checking
- Category aggregation
- Multi-format output (JSON, Markdown, CSV)
- Duplicate detection
- Business purpose validation

**Output**: Reports in `./expenses/reports/`
- `expense_report_EXP-YYYY-NNN.json` (machine-readable)
- `expense_report_EXP-YYYY-NNN.md` (human-readable)
- `expense_report_EXP-YYYY-NNN.csv` (accounting import)

### policy-validator

**Trigger**: "Validate policy compliance", "Check expense policy", "Compliance review"

**Capabilities**:
- Structural validation (data integrity)
- Policy rule validation (limits, requirements)
- Context validation (fraud detection)
- Risk-based severity classification
- Compliance scoring (0-100)
- Detailed remediation guidance

**Output**: Compliance report in `./expenses/compliance/`

**Security**: Read-only agent (no data modification) for audit independence

### approval-router

**Trigger**: "Submit for approval", "Route expense report", "Check approval status"

**Capabilities**:
- Dynamic approval chain construction
- Amount-based escalation
- Category-specific routing
- SLA calculation and tracking
- Status monitoring
- Auto-escalation for overdue approvals
- Notification scheduling

**Output**: Workflow state in `./expenses/approvals/`

## Configuration

### Company Policy Rules

Create a policy file at `./expenses/policy.json`:

```json
{
  "policy_version": "2025.1",
  "rules": {
    "meals_and_entertainment": {
      "per_meal_limit": 50.00,
      "daily_limit": 75.00,
      "alcohol_limit": 25.00
    },
    "lodging": {
      "per_night_standard": 200.00,
      "per_night_high_cost_city": 350.00,
      "high_cost_cities": ["NYC", "SF", "LA", "Seattle", "Boston"]
    },
    "transportation": {
      "mileage_rate": 0.655,
      "parking_limit": 50.00,
      "ride_share_limit": 100.00
    },
    "receipts": {
      "required_above": 25.00
    },
    "approval_thresholds": {
      "manager": 5000.00,
      "director": 10000.00,
      "vp": 25000.00
    }
  }
}
```

### Organization Structure

For approval routing, optionally create `./expenses/org-structure.json`:

```json
{
  "departments": {
    "Engineering": {
      "manager": "Jane Smith",
      "director": "Bob Johnson",
      "vp": "Alice Williams"
    }
  },
  "approvers": {
    "Jane Smith": "jane.smith@company.com",
    "Bob Johnson": "bob.johnson@company.com",
    "Alice Williams": "alice.williams@company.com"
  }
}
```

## Workflow Coordination

The agents work together in a coordinated workflow:

```
Receipt Images
      ↓
┌─────────────────┐
│ receipt-analyzer │ (Haiku - Fast OCR)
└─────────────────┘
      ↓
Receipt JSON Files
      ↓
┌──────────────────┐
│ expense-processor │ (Sonnet - Judgment)
└──────────────────┘
      ↓
Expense Report (JSON/MD/CSV)
      ↓
┌─────────────────┐
│ policy-validator │ (Sonnet - Read-Only)
└─────────────────┘
      ↓
Compliance Report (Pass/Fail)
      ↓
┌─────────────────┐
│ approval-router  │ (Sonnet - Workflow)
└─────────────────┘
      ↓
Approval Workflow (Tracking)
```

## Cost Optimization

**Model Selection Strategy**:
- **Haiku** for OCR (fast, deterministic, ~$0.001/1K tokens)
- **Sonnet** for judgment tasks (policy validation, approval routing, ~$0.015/1K tokens)

**Why Not Opus**:
- Expense processing doesn't require maximum reasoning
- Sonnet provides excellent judgment at 5x lower cost
- Haiku handles routine OCR efficiently

**Estimated Costs** (per expense report with 10 receipts):
- OCR processing: ~$0.01 (Haiku)
- Report assembly: ~$0.10 (Sonnet)
- Policy validation: ~$0.05 (Sonnet)
- Approval routing: ~$0.02 (Sonnet)
- **Total: ~$0.18 per report**

## Security & Compliance

### Security Features

1. **Read-Only Validator**: policy-validator has no write permissions
2. **Audit Trail**: Complete history of all actions
3. **No Secret Storage**: Never stores credentials
4. **Least Privilege**: Each agent has minimal necessary tools
5. **Independent Validation**: Validator cannot modify data it checks

### Compliance Support

- **IRS Requirements**: Receipt validation per IRS Pub 463
- **SOX Compliance**: Segregation of duties (read-only validator)
- **Audit Ready**: Complete audit trail with timestamps
- **Policy Citations**: Every rule links to policy section
- **Data Retention**: All receipts and reports retained

## Troubleshooting

### OCR Issues

**Problem**: "Tesseract not found"
**Solution**:
```bash
# macOS
brew install tesseract

# Linux
sudo apt-get install tesseract-ocr

# Verify
tesseract --version
```

**Problem**: "Poor OCR quality"
**Solution**:
- Ensure receipt images are clear and well-lit
- Minimum 1000px width recommended
- Use PNG or high-quality JPEG
- Pre-process skill includes enhancement techniques

### Policy Validation Issues

**Problem**: "Too many false positives"
**Solution**:
- Adjust policy limits in `./expenses/policy.json`
- Review severity thresholds
- Consider company-specific rules

### Approval Routing Issues

**Problem**: "Wrong approvers selected"
**Solution**:
- Check `./expenses/org-structure.json`
- Verify approval thresholds in policy
- Review amount-based escalation rules

## Examples

### Example 1: Simple Meal Expense

```bash
# 1. Process receipt
"Extract data from receipt_coffee.jpg"

# Output: receipt_20250120_001.json
# Vendor: Starbucks, Amount: $15.47, Category: Meals

# 2. Create report
"Create expense report from this receipt"

# Output: expense_report_EXP-2025-001.json

# 3. Validate
"Check policy compliance"

# Output: ✅ Compliant (Score: 100/100)

# 4. Submit
"Submit for approval"

# Output: Routed to Manager (Jane Smith), SLA: 48 hours
```

### Example 2: Multi-Day Trip

```bash
# 1. Batch process receipts
"Process all receipts in ./receipts/trip-nyc/"

# Output: 15 receipt JSON files

# 2. Create comprehensive report
"Create expense report for NYC trip Jan 15-18"

# Output: Report with $2,847 total, 15 expenses

# 3. Validate
"Validate against policy"

# Output: ⚠️ 1 warning - Hotel rate $325/night (>$200 standard)

# 4. Add justification
"Add note: NYC is high-cost city, within $350 limit"

# 5. Revalidate
"Check compliance again"

# Output: ✅ Compliant (Score: 98/100)

# 6. Submit
"Submit for approval"

# Output: Routed to Manager → Director (>$1000), SLA tracking enabled
```

## Advanced Features

### Duplicate Detection

Automatically identifies:
- Exact duplicates (same vendor/date/amount)
- Likely duplicates (>85% similarity)
- Possible duplicates (>70% similarity)

### Anomaly Detection

Flags unusual patterns:
- Transactions 3x higher than median
- Multiple expenses same vendor/day
- Geographic inconsistencies
- Spending pattern deviations

### SLA Management

- Automatic deadline calculation
- Reminder schedule (50%, 80%, 100%)
- Auto-escalation after 24h overdue
- Business hours support

## Roadmap

Future enhancements planned:
- [ ] Mobile receipt capture integration
- [ ] Credit card statement import
- [ ] Mileage calculation from GPS data
- [ ] Currency conversion for international expenses
- [ ] Machine learning for category prediction
- [ ] Integration with accounting systems (QuickBooks, Xero)
- [ ] Budget tracking and variance analysis

## Support

- **Issues**: Report bugs or request features on GitHub
- **Documentation**: Full skill documentation in `skills/` directory
- **Examples**: Additional examples in project README

## License

Part of Puerto plugin marketplace. See main project LICENSE.

---

**Plugin Version**: 1.0.0
**Last Updated**: January 2025
**Designed with**: @ultimate-subagent-creator expert
**Compatible with**: Claude Code CLI
