# Volunteer Time Tracker

Comprehensive volunteer service logging and impact measurement system with hours tracking, organization management, tax documentation, and skills-based matching.

## Features

### 6 Specialized Agents

1. **hours-logger** (Haiku, Fast) - Session logging
   - Log volunteer hours with activity details
   - Track mileage for tax purposes
   - Generate hour summaries

2. **organization-manager** (Sonnet) - Organization relationships
   - Manage nonprofit contacts
   - Verify 501(c)(3) status
   - Track volunteer opportunities

3. **impact-analyzer** (Sonnet) - Impact measurement
   - Calculate monetary value ($33.49/hour for 2024)
   - Analyze service patterns
   - Generate impact reports

4. **skills-matcher** (Sonnet) - Opportunity matching
   - Match skills to opportunities
   - Recommend volunteer positions
   - Track skill development

5. **tax-documenter** (Sonnet) - Tax compliance
   - Calculate IRS-compliant deductions
   - Generate year-end summaries
   - Mileage tracking ($0.14/mile for 2024)

6. **commitment-scheduler** (Haiku, Fast) - Calendar management
   - Manage recurring commitments
   - Track volunteer schedule
   - Send reminders

### 1 Comprehensive Skill

**volunteer-management** - Complete patterns for:
- Volunteer session logging
- Impact measurement formulas
- IRS Publication 526 compliance
- Organization verification
- Skills-based matching

## Quick Start

### Log Volunteer Hours

```bash
@hours-logger "Volunteered at Downtown Food Bank today 9am-12pm, sorted food donations, drove 12 miles"
```

### View Impact

```bash
@impact-analyzer "Show my volunteer impact this month"
```

### Generate Tax Summary

```bash
@tax-documenter "Generate 2024 tax deduction summary"
```

## Key Features

### IRS-Compliant Tax Documentation
- Mileage deduction: $0.14/mile (2024 rate)
- Out-of-pocket expense tracking
- 501(c)(3) organization verification
- Audit-ready documentation

### Impact Measurement
- Total hours and sessions
- People served calculations
- Monetary value (Independent Sector rate)
- Trend analysis

### Skills-Based Matching
- Profile your volunteer skills
- Find matching opportunities
- Track skill development
- Discover new causes

## Data Storage

Events are stored locally in `~/.volunteer-tracker/`:
- `sessions.json` - All volunteer sessions
- `organizations.json` - Organization database
- `commitments.json` - Schedule and commitments
- `tax/` - Tax documentation by year

## IRS Requirements (Important!)

**DEDUCTIBLE Expenses:**
- Mileage: $0.14/mile (2024 charitable rate)
- Supplies, parking, tolls
- Required uniforms

**NOT DEDUCTIBLE:**
- Volunteer time value
- Personal meals
- Childcare
- Optional uniforms

**Documentation Requirements:**
- Contemporaneous records (log at time of service)
- Verification letters from organizations
- Mileage log with date, miles, purpose
- Receipts for expenses over $250

## Model Selection

- **Haiku agents** (hours-logger, commitment-scheduler): Fast CRUD operations, frequent use
- **Sonnet agents** (organization-manager, impact-analyzer, skills-matcher, tax-documenter): Analysis, matching, and compliance

## License

MIT

---

**Generated as part of Puerto Plugin Collection - Issue #141**
