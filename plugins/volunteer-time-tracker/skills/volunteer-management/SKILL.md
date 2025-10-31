# Volunteer Management Skill

Comprehensive patterns for volunteer time tracking, impact measurement, and IRS-compliant tax documentation.

## Core Principles

1. **Log Immediately**: Record sessions within 24 hours for accuracy
2. **Track Mileage**: Contemporaneous mileage logs required for IRS
3. **Verify 501(c)(3)**: Only qualified organizations eligible for deductions
4. **Save Receipts**: Keep all expense documentation
5. **Annual Review**: Generate tax summaries by January 31

## Data Structures

### Session Schema

```json
{
  "session_id": "uuid",
  "organization_id": "uuid",
  "date": "2025-01-20",
  "start_time": "09:00",
  "end_time": "12:30",
  "duration_hours": 3.5,
  "activity": "Food bank sorting and distribution",
  "role": "Volunteer coordinator",
  "location": "Downtown Food Bank",
  "skills_used": ["organization", "leadership", "physical"],
  "people_served": 150,
  "mileage": 12.5,
  "expenses": 0,
  "notes": "Helped organize winter distribution",
  "verification": {
    "verified_by": "Jane Smith",
    "verified_date": "2025-01-21"
  }
}
```

### Organization Schema

```json
{
  "organization_id": "uuid",
  "name": "Downtown Food Bank",
  "ein": "12-3456789",
  "tax_exempt_status": "501(c)(3)",
  "mission": "Provide food assistance to families",
  "contacts": [
    {
      "name": "Jane Smith",
      "role": "Volunteer Coordinator",
      "email": "jane@foodbank.org",
      "phone": "(555) 123-4567"
    }
  ],
  "address": {
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345"
  }
}
```

## IRS Tax Documentation Requirements

### Deductible Expenses (IRS Publication 526)

**DEDUCTIBLE**:
- **Mileage**: IRS standard charitable rate ($0.14/mile for 2024)
- **Out-of-pocket expenses**: Supplies, parking, tolls, required uniforms
- **Travel expenses**: If away from home overnight for volunteer work

**NOT DEDUCTIBLE**:
- **Volunteer time value**: Hours cannot be deducted
- **Personal expenses**: Meals (unless overnight travel), childcare
- **Optional items**: Clothing not required as uniform

### Documentation Requirements

1. **Contemporaneous Records**: Log maintained at time of service
2. **Mileage Log**: Date, miles, purpose for each trip
3. **Expense Receipts**: Keep receipts for expenses over $250
4. **Organization Verification**: Written acknowledgment from charity
5. **501(c)(3) Status**: Verify organization is qualified
6. **Retention**: Keep records for 7 years

### IRS Mileage Rates (Update Annually)

- 2024: $0.14/mile (charitable)
- 2025: $0.14/mile (charitable)

### Verification Letters

Organizations should provide:
- Organization name and EIN
- Volunteer's name
- Dates and hours of service
- Description of services provided
- Statement: "No goods or services provided in return"

## Impact Measurement

### Monetary Value Calculation

**Method**: Independent Sector volunteer value rate
- 2024: $33.49/hour
- 2025: $34.00/hour (update annually)

**Formula**: Total Hours × Hourly Rate = Monetary Value

**Note**: This is for impact reporting only, NOT tax deductible.

### Impact Metrics

Track:
- Total volunteer hours
- Total sessions
- Organizations served
- People impacted
- Projects completed
- Monetary value (reporting only)
- Skills developed

### Reporting Standards

- Monthly summaries
- Yearly impact reports
- Organization breakdowns
- Skills utilization analysis
- Trend visualization

## Volunteer Session Logging Workflow

1. **Capture Basic Info**
   - Date and time (start/end)
   - Organization name
   - Activity description

2. **Calculate Duration**
   - End time - start time = duration
   - Round to nearest 0.25 hours

3. **Track Transportation**
   - Record round-trip mileage
   - Note starting location
   - Log immediately

4. **Document Impact**
   - People served (if applicable)
   - Skills used
   - Outcomes achieved

5. **Save & Verify**
   - Store session record
   - Request supervisor verification
   - Update organization totals

## Organization Management Best Practices

### Adding Organizations

1. Verify 501(c)(3) status (IRS website or GuideStar)
2. Record EIN (required for tax deductions)
3. Store contact information
4. Document mission and focus areas
5. Track verification requirements

### Maintaining Relationships

- Update contact information annually
- Track total hours per organization
- Request verification letters yearly
- Monitor volunteer opportunities
- Record supervisor feedback

## Skills-Based Volunteering

### Skills Categories

- **Professional**: Accounting, legal, marketing, IT, design
- **Technical**: Coding, data analysis, engineering
- **Creative**: Writing, photography, graphic design
- **Leadership**: Management, training, coordination
- **Physical**: Construction, moving, outdoor work
- **Social**: Counseling, mentoring, teaching
- **Administrative**: Data entry, filing, scheduling

### Skills Matching Process

1. Profile volunteer skills and proficiency
2. Identify interests and causes
3. Check availability and constraints
4. Match to organization needs
5. Calculate match score
6. Recommend opportunities

### Skill Development Tracking

Track:
- Skills used per session
- Hours per skill
- Proficiency growth
- New skills gained
- Certifications earned

## Tax Year-End Process

### December Preparation

1. **Log Final Sessions**: Complete all 2024 logging by Dec 31
2. **Gather Receipts**: Organize expense documentation
3. **Update Mileage Log**: Ensure all trips recorded
4. **Verify Organizations**: Confirm all are 501(c)(3)

### January Tax Summary

1. **Calculate Total Hours**: Sum all 2024 sessions
2. **Calculate Mileage Deduction**: Total miles × $0.14
3. **Sum Out-of-Pocket Expenses**: Add deductible expenses
4. **Request Verification Letters**: Contact all organizations
5. **Generate Tax Summary**: Create IRS-compliant report
6. **Organize Documentation**: File for 7-year retention

### Tax Filing

- Report charitable contributions on Schedule A
- Itemize deductions (if exceeds standard deduction)
- Include mileage and expense deductions
- Attach verification letters if audited
- Keep contemporaneous mileage log

## Storage Architecture

```
~/.volunteer-tracker/
├── sessions.json              # All volunteer sessions
├── organizations.json         # Organization database
├── commitments.json          # Schedule and recurring commitments
├── config.json               # User preferences
├── tax/
│   ├── 2024/
│   │   ├── summary.json
│   │   ├── mileage-log.csv
│   │   ├── expenses.json
│   │   └── verification-letters/
│   └── 2025/
├── impact/
│   ├── monthly/
│   └── yearly/
└── exports/
```

## Common Workflows

### Daily: Log Volunteer Session
1. `@hours-logger "Volunteered 3 hours at Food Bank, drove 12 miles"`
2. System calculates duration, logs mileage
3. Updates organization totals
4. Adds to tax year records

### Monthly: Review Impact
1. `@impact-analyzer "Show this month's impact"`
2. View hours, organizations, people served
3. Check monetary value
4. Analyze trends

### Yearly: Tax Preparation
1. `@tax-documenter "Generate 2024 tax summary"`
2. Review deductible mileage and expenses
3. Request verification letters
4. Export for tax software

### Ongoing: Find Opportunities
1. `@skills-matcher "Find opportunities matching my skills"`
2. Review recommendations
3. Contact organizations
4. Schedule commitments

## Best Practices

1. **Log Immediately**: Record within 24 hours of service
2. **Track Mileage Contemporaneously**: Log trips when they occur
3. **Save All Receipts**: Photograph receipts immediately
4. **Request Verification**: Get supervisor signature
5. **Verify 501(c)(3)**: Check before first volunteer session
6. **Annual Letters**: Request by January for previous year
7. **Backup Data**: Export records quarterly
8. **Update Rates**: Check IRS mileage rates annually

## Error Handling

### Invalid Sessions
- Date not in future
- Duration 0-24 hours
- Organization must exist

### Tax Calculation Errors
- Missing EIN warning
- Unverified 501(c)(3) flag
- Invalid expense categories

### Data Integrity
- Session IDs must be unique
- Organization IDs must match
- Hours must be positive

---

**This skill provides the foundation for compliant volunteer tracking. All agents should reference these patterns for IRS compliance and accurate impact measurement.**
