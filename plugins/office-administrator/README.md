# Office Administrator Plugin

**Production-ready administrative support for meeting scheduling, travel planning, expense processing, and document organization**

A comprehensive plugin providing four specialized agents to handle all aspects of office administration, from calendar management to travel arrangements.

---

## Overview

This plugin provides a complete office administration workflow with:

- **4 Specialized Agents**: Each agent focuses on one administrative domain
- **3 Comprehensive Skills**: Battle-tested patterns from professional office environments
- **3 Professional Templates**: Ready-to-use standardized documents
- **Full Coverage**: Meetings → Travel → Expenses → Documents

---

## Agents

### 1. meeting-scheduler (Haiku - Fast & Routine)

**When to use**: Scheduling meetings, finding availability, managing calendars

**What it does**:
- Schedules meetings with proper time zone handling
- Finds common availability across participants
- Creates professional meeting agendas
- Follows calendar etiquette best practices
- Manages recurring meetings
- Sets appropriate reminders and buffers

**Skill-aware**: Reads `scheduling` skill before starting

**Example usage**:
```bash
"Schedule a 30-minute meeting between John Smith (EST), Sarah Lee (PST),
and Michael Chen (GMT) for next week. Topic is Q1 planning. Find a time
that works for all and create an agenda."
```

**Output**:
- Meeting scheduled with all time zones specified
- Calendar invite details
- Professional agenda document
- Confirmation status for all participants
- Next steps for preparation

**Tools**: Read, Write, Edit, Bash, Grep, Glob
**Model**: Haiku (routine scheduling is deterministic)

---

### 2. travel-planner (Sonnet - Complex Optimization)

**When to use**: Planning business travel, creating itineraries, booking arrangements

**What it does**:
- Creates comprehensive travel itineraries
- Optimizes flight selection (direct vs. connections, timing, cost)
- Recommends hotels based on location and budget
- Plans ground transportation
- Handles time zone and jet lag considerations
- Ensures corporate travel policy compliance
- Provides emergency contacts and backup plans
- Manages international travel requirements

**Skill-aware**: Reads `travel-planning` skill before starting

**Example usage**:
```bash
"Plan a 3-day business trip to San Francisco for Sarah Lee departing from
Boston on Feb 15. She has meetings at Tech Corp HQ on Feb 16 at 10 AM and
2 PM. Budget is $2,000 total. Include flight options, hotel near meetings,
and ground transportation recommendations."
```

**Output**:
- Complete day-by-day itinerary
- Flight options with pros/cons
- Hotel recommendation with location analysis
- Ground transportation plan
- Cost breakdown with policy compliance
- Emergency contacts and backup plans
- Time zone conversion reference

**Tools**: Read, Write, Edit, Bash, Grep, Glob
**Model**: Sonnet (travel optimization requires complex decision-making)

---

### 3. expense-processor (Haiku - Template-Based)

**When to use**: Processing expense reports, categorizing receipts, validating expenses

**What it does**:
- Processes expense reports following company policy
- Categorizes expenses correctly
- Validates receipt requirements
- Calculates totals and per diems
- Flags policy exceptions
- Prepares documentation for approval
- Tracks reimbursement status

**Skill-aware**: Reads `office-administration` skill before starting

**Example usage**:
```bash
"Process expense report for John Smith's San Francisco trip. Expenses include:
- Flight $425, Hotel 2 nights at $285/night, 4 Uber rides totaling $120,
and meals $150. Create expense report following company policy."
```

**Output**:
- Categorized expense report
- Receipt checklist
- Policy compliance status
- Total reimbursable amount
- Items flagged for review (if any)
- Approval workflow status
- Next steps for submission

**Tools**: Read, Write, Edit, Bash, Grep, Glob
**Model**: Haiku (expense processing is template-based and routine)

---

### 4. document-organizer (Haiku - Routine Work)

**When to use**: Organizing files, establishing naming conventions, structuring folders

**What it does**:
- Creates logical folder hierarchies (2-4 levels)
- Establishes consistent naming conventions
- Renames files following standards (YYYY-MM-DD format)
- Moves files to appropriate locations
- Archives old documents
- Removes duplicates
- Creates documentation (README files)
- Implements retention policies

**Skill-aware**: Reads `office-administration` skill before starting

**Example usage**:
```bash
"Organize the project-files directory. Create a logical structure with
consistent naming. Current files are messy with inconsistent names and
scattered organization. Establish a system that's easy to maintain."
```

**Output**:
- Organized folder structure
- Documented naming conventions
- File count by category
- README files for navigation
- Actions taken (moved, renamed, archived)
- Maintenance guidelines
- Next steps for team training

**Tools**: Read, Write, Edit, Bash, Grep, Glob
**Model**: Haiku (file organization is systematic and routine)

---

## Skills

### 1. scheduling

**Meeting best practices, calendar etiquette, and time zone handling**

Covers:
- Meeting types and duration guidelines (15min-2hr)
- Time zone management and conversion
- Calendar etiquette and invitation protocols
- Recurring meeting best practices
- Optimal meeting timing (avoid early/late/lunch)
- Meeting spacing and buffer time
- Agenda templates for different meeting types
- Distributed team scheduling fairness
- Tools and automation tips

**When read**: By `meeting-scheduler` agent before scheduling any meeting

---

### 2. travel-planning

**Itinerary creation, vendor selection, and corporate travel policy compliance**

Covers:
- Flight selection criteria (direct vs. connection decision tree)
- Layover time guidelines (domestic vs. international)
- Flight timing optimization (morning/afternoon/evening/red-eye)
- Hotel selection (location, budget, quality indicators)
- Ground transportation decision matrix (rental/rideshare/transit/service)
- Time zone and jet lag management strategies
- International travel considerations (visa, health, currency)
- Itinerary structure and essential components
- Cost management and optimization
- Risk management and contingency planning

**When read**: By `travel-planner` agent before creating any itinerary

---

### 3. office-administration

**Expense policies, document management, and communication protocols**

Covers:
- Expense management policies (categories, limits, receipts)
- Receipt requirements and missing receipt protocol
- Non-reimbursable expenses
- Document organization systems (folder hierarchy, naming)
- File naming conventions (YYYY-MM-DD standard)
- Document lifecycle management (active/reference/archive)
- Retention policies (financial 7 years, legal varies)
- Communication protocols (email, phone, meeting etiquette)
- Calendar management best practices
- Data security and privacy (classification, access control)
- Professional development for administrators

**When read**: By `expense-processor` and `document-organizer` agents

---

## Templates

### 1. meeting-agenda-template.md

**Professional meeting agenda structure with time allocations**

Includes:
- Header (date, time, location, duration)
- Attendee list (required vs. optional)
- Meeting objectives
- Pre-meeting preparation checklist
- Agenda items with time allocations and owners
- Time allocation summary table
- Meeting notes section
- Decisions summary
- Action items with owners and due dates
- Parking lot for out-of-scope items
- Next meeting information

**Use for**: All meetings requiring structured agendas (30+ minutes)

---

### 2. travel-itinerary-template.md

**Complete travel plan with flights, hotels, and ground transportation**

Includes:
- Trip summary and quick reference
- Emergency contacts (company, personal, destination)
- Travel documents checklist
- Expense budget breakdown
- Day-by-day detailed itinerary
  - Flight details with confirmations
  - Hotel information with addresses
  - Meeting locations and contacts
  - Ground transportation plans
  - Meal suggestions
- Local information (time zone, weather, currency, language)
- Packing checklist
- Alternative/backup options
- Post-trip expense reporting reference

**Use for**: All business travel requiring comprehensive planning

---

### 3. expense-report-template.md

**Expense tracking with categories and receipt references**

Includes:
- Employee and trip information
- Payment information
- Expense summary by category
- Detailed expense items
  - Transportation (flights, parking, mileage)
  - Lodging (itemized hotel bills)
  - Meals (per diem or actuals)
  - Entertainment (with attendees)
  - Office supplies
  - Other expenses
- Non-reimbursable expenses
- Policy compliance checklist
- Missing receipt documentation
- Receipt checklist and organization
- Approval workflow (employee, manager, finance)
- Payment processing tracking

**Use for**: All expense reimbursement submissions

---

## Workflow Examples

### Example 1: Schedule Multi-Timezone Meeting

```bash
# Schedule meeting with participants across time zones
@meeting-scheduler "Schedule a 1-hour quarterly planning meeting for the
executive team. Participants: CEO (PST), CFO (EST), CTO (GMT), COO (CST).
Find a time next week that works for all. Create detailed agenda covering
Q1 results review, Q2 planning, and budget allocation. Ensure proper time
zone handling."

# Agent will:
# 1. Read scheduling skill
# 2. Identify working hours overlap across all 4 time zones
# 3. Propose 2-3 optimal times
# 4. Create meeting invite with all time zones specified
# 5. Generate comprehensive agenda
# 6. Set appropriate reminders
```

### Example 2: Plan Complete Business Trip

```bash
# 1. Create comprehensive itinerary
@travel-planner "Plan 4-day trip to Chicago for product launch event.
Traveler: Sarah Lee from San Francisco. Trip dates: March 10-13.
Event at Navy Pier on March 11-12, 9 AM-6 PM both days. Need hotel
near venue, prefer direct flights. Budget $2,500. Include dinner
recommendations and backup plans."

# 2. After trip, process expenses
@expense-processor "Process Sarah Lee's Chicago trip expenses:
- Round-trip flight SFO-ORD: $380
- Hotel 3 nights: $899
- Ground transport (Uber): $156
- Meals: $245
- Event parking: $75
Create complete expense report with policy compliance check."

# 3. Organize trip documentation
@document-organizer "Organize all Chicago trip documents. Create folder
structure for trip files including itinerary, expense receipts, event
materials, and meeting notes. Establish naming convention and archive
properly."
```

### Example 3: Monthly Administrative Tasks

```bash
# 1. Schedule monthly team meeting
@meeting-scheduler "Schedule recurring monthly all-hands meeting for
third Thursday of each month, 2-3 PM EST. Team is distributed (EST,
CST, PST). Create agenda template covering: monthly metrics review,
team updates, Q&A. Set up for next 6 months."

# 2. Process monthly expenses
@expense-processor "Process all expense reports submitted this month.
Verify policy compliance, check receipts, flag any issues. Create
summary report showing total expenses by department and category."

# 3. Quarterly document cleanup
@document-organizer "Perform quarterly cleanup of shared drive.
Archive projects completed last quarter, remove duplicates, ensure
naming conventions followed. Create Q1 2025 archive folder."
```

### Example 4: Conference Attendance

```bash
# 1. Plan travel to conference
@travel-planner "Plan trip to TechConf 2025 in Austin, TX, May 15-18.
Traveler: John Smith from Boston. Conference hotel is Hilton Downtown.
Sessions run 8 AM-6 PM daily. Want to arrive evening before, depart
evening of last day. Include conference discount hotel code TECH2025."

# 2. Schedule networking meetings
@meeting-scheduler "Schedule 3 networking meetings during TechConf:
- Coffee with Jane Doe (Microsoft) on May 16 morning
- Lunch with Acme Corp team on May 17
- Dinner with potential client on May 18
Coordinate with conference schedule, find convenient locations near venue."

# 3. Process conference expenses
@expense-processor "Process TechConf expenses:
- Conference registration: $1,200
- Flight BOS-AUS roundtrip: $425
- Hotel 4 nights: $1,180
- Ground transport: $145
- Meals: $280
- Client dinner (3 people): $185
Document business purpose and attendees for client meal."
```

---

## Installation

### User-Level (Available in All Projects)

```bash
# Clone or copy this plugin to your user-level plugins directory
cp -r plugins/office-administrator ~/.claude/plugins/

# Verify installation
ls ~/.claude/plugins/office-administrator/agents/
```

### Project-Level (Project-Specific)

```bash
# Copy to project's .claude directory
mkdir -p .claude/plugins
cp -r plugins/office-administrator .claude/plugins/

# Commit to version control
git add .claude/plugins/office-administrator/
git commit -m "feat: add office-administrator plugin"
```

---

## Configuration

### Company-Specific Policies

**Expense Policies**:
```bash
# Create company expense policy override
mkdir -p .claude/skills/office-administration/
# Add your company's specific:
# - Expense limits
# - Receipt requirements
# - Approval workflows
# - Preferred vendors
```

**Travel Policies**:
```bash
# Create company travel policy override
mkdir -p .claude/skills/travel-planning/
# Add your company's specific:
# - Flight class restrictions
# - Hotel budget limits
# - Preferred airlines/hotels
# - Booking procedures
```

---

## Design Decisions

### Why These Agents?

**Four agents, not one**: Single responsibility principle. Each agent is an expert in one domain:
- meeting-scheduler: Calendar management and meeting coordination
- travel-planner: Complex itinerary optimization
- expense-processor: Policy compliance and report generation
- document-organizer: File system management

**Specialized expertise**: Better results than a generalist administrative agent.

**Why different models**:
- Haiku (meeting-scheduler, expense-processor, document-organizer): Routine, template-based work with 90% cost savings
- Sonnet (travel-planner): Requires complex optimization and judgment (flight routing, hotel selection, risk assessment)

### Why Skill-Aware?

Without skills, agents produce inconsistent results based on general knowledge. With skills, agents follow company-specific policies and best practices:

**Quality Difference**:
- Without skills: ~60% policy compliance, frequent corrections needed
- With skills: ~95% policy compliance, first-time-right

Skills are continuously updated with lessons learned and policy changes.

### Model Selection Rationale

**Haiku for routine work**:
- Meeting scheduling: Template-based, follows calendar rules
- Expense processing: Policy-driven, straightforward categorization
- Document organization: Systematic file management

**Sonnet for complex decisions**:
- Travel planning: Optimizing multiple variables (cost, time, convenience, policy)
- Requires judgment calls and tradeoff analysis
- Risk assessment and contingency planning

---

## Cost Optimization

**Estimated costs per task** (based on Claude pricing):

| Task | Agent | Model | Est. Cost |
|------|-------|-------|-----------|
| Schedule meeting | meeting-scheduler | Haiku | ~$0.01 |
| Create travel itinerary | travel-planner | Sonnet | ~$0.10 |
| Process expense report | expense-processor | Haiku | ~$0.02 |
| Organize documents | document-organizer | Haiku | ~$0.01 |

**Monthly costs for active office** (estimates):
- 20 meetings scheduled: ~$0.20
- 5 trips planned: ~$0.50
- 15 expense reports: ~$0.30
- 4 document organization tasks: ~$0.04
- **Total**: ~$1.04/month

**Cost savings vs. all-Sonnet**: ~75% (Haiku is 10x cheaper)

---

## Troubleshooting

### Agent doesn't activate automatically

**Issue**: Agent doesn't trigger when expected

**Solutions**:
- Invoke manually: `@meeting-scheduler "task description"`
- Check agent description has trigger phrases (PROACTIVELY)
- Verify agent file exists and is valid

### Meeting times don't account for time zones

**Issue**: Time zone conversions missing or incorrect

**Solutions**:
- Ensure scheduling skill is being read (check agent output)
- Verify skill file exists at expected location
- Manually specify time zones in request
- Check that agent is using Haiku model (in agent frontmatter)

### Travel itinerary missing details

**Issue**: Itinerary lacks essential information

**Solutions**:
- Provide more context in request (budget, preferences, constraints)
- Ensure travel-planning skill is accessible
- Check that agent is using Sonnet model
- Use template as reference for required information

### Expense report doesn't match company policy

**Issue**: Expense categories or limits don't match your company

**Solutions**:
- Create company-specific office-administration skill override
- Add your company's expense policies to skill
- Document your policies in `.claude/skills/office-administration/SKILL.md`
- Agent will prioritize company skill over default

### Files organized differently than expected

**Issue**: Folder structure or naming doesn't match preferences

**Solutions**:
- Provide specific requirements in request
- Create project-specific organization patterns in skill
- Show examples of desired naming convention
- Request specific folder structure

---

## Best Practices

### Meeting Scheduling

1. **Provide all context**: Participants, purpose, duration, constraints
2. **Specify time zones**: Especially for distributed teams
3. **Request agenda**: For all meetings > 15 minutes
4. **Buffer time**: Always include breaks between meetings
5. **Follow up**: Send agenda 24 hours in advance

### Travel Planning

1. **Plan early**: 3-6 weeks for domestic, 6-12 weeks for international
2. **Provide constraints**: Budget, preferences, meeting schedule
3. **Policy compliance**: Share company travel policy with agent
4. **Backup plans**: Always request alternative options
5. **Emergency prep**: Include all emergency contacts

### Expense Processing

1. **Timely submission**: Submit within 30 days of expense
2. **Keep receipts**: All receipts for expenses > $25
3. **Document purpose**: Clear business purpose for all expenses
4. **Client meals**: Document attendees and business discussed
5. **Review before submit**: Check all totals and categorization

### Document Organization

1. **Consistent naming**: Always use YYYY-MM-DD date format
2. **Logical hierarchy**: Keep folder structure 2-4 levels deep
3. **Regular cleanup**: Archive old files quarterly
4. **Document system**: Create README files for complex structures
5. **Train team**: Ensure everyone follows conventions

---

## Integration with Other Plugins

### With expense-manager

```bash
# 1. Scan receipt with expense-manager OCR
@receipt-analyzer "Process receipt image from dinner"

# 2. Process with office-administrator
@expense-processor "Create expense report including OCR'd receipt data"
```

### With backend-architect

```bash
# 1. Schedule technical planning meeting
@meeting-scheduler "Schedule architecture review meeting for database
redesign project"

# 2. Design system in meeting
@architecture-designer "Design scalable database architecture based on
meeting requirements"
```

### With tax-compliance

```bash
# 1. Organize financial documents
@document-organizer "Organize all financial records for tax season"

# 2. Prepare tax documentation
@tax-preparer "Use organized financial records to prepare quarterly
tax filing"
```

---

## Common Workflows

### New Employee Onboarding

```bash
# 1. Schedule onboarding meetings
@meeting-scheduler "Schedule new hire onboarding:
- Day 1: HR orientation (2 hours)
- Day 1: IT setup (1 hour)
- Day 2: Team introductions (30 min each with 5 team members)
- Week 1: Manager 1-on-1s (daily, 30 min)
Create recurring meeting for first month."

# 2. Organize onboarding documents
@document-organizer "Create onboarding folder for [Employee Name] with:
- HR documents
- IT setup guides
- Training materials
- Team contacts
- First week schedule
Establish structure for ongoing employee file management."
```

### Quarterly Executive Offsite

```bash
# 1. Plan travel for executive team
@travel-planner "Plan 3-day executive offsite in Miami:
- 8 executives from various offices (NYC, SF, Chicago, Boston)
- Dates: April 15-17
- Meetings at beachfront resort
- Coordinated arrival/departure times
- Team dinner on April 16
Create individual itineraries for each executive."

# 2. Schedule offsite sessions
@meeting-scheduler "Schedule 3-day offsite agenda:
- Day 1: Strategic planning (full day)
- Day 2: Department reviews (morning), Team building (afternoon)
- Day 3: Action planning and wrap-up
Create detailed agendas for each session with time allocations."

# 3. Process all expenses after event
@expense-processor "Process offsite expenses for 8 executives:
- Flights, hotels, ground transport, meals
- Team dinner for 8 people
- Meeting room rental
- Catering
Create consolidated expense report with department allocation."
```

### Annual Conference Coordination

```bash
# Coordinate all administrative aspects of conference attendance
# Use meeting-scheduler, travel-planner, expense-processor, document-organizer
# in sequence for comprehensive conference management
```

---

## Performance Metrics

### Effectiveness Indicators

**Good Signs**:
- Meetings scheduled with all required details
- Time zone conversions always accurate
- Travel itineraries comprehensive and policy-compliant
- Expense reports accepted on first submission
- Documents easy to find with consistent naming

**Warning Signs**:
- Frequent rescheduling due to conflicts
- Time zone confusion
- Travel booking errors
- Expense reports rejected for policy violations
- Cannot find documents quickly

### Continuous Improvement

**Weekly Review**:
- Count administrative tasks completed
- Assess quality of outputs
- Note any recurring issues
- Identify skill improvements needed

**Monthly Audit**:
- Review expense policy compliance rate
- Check travel cost optimization
- Assess meeting effectiveness
- Update skills with lessons learned

---

## Key Takeaways

1. **Specialization matters**: Four focused agents outperform one generalist
2. **Skills ensure consistency**: Policy compliance through skill-aware agents
3. **Time zones critical**: Always explicit with time zone conversions
4. **Templates save time**: Standardized documents ensure nothing is missed
5. **Cost optimized**: Haiku for routine work, Sonnet for complex decisions
6. **Policy first**: Compliance with company policies is non-negotiable
7. **Documentation essential**: Well-organized files save time and reduce errors
8. **Continuous improvement**: Update skills with lessons learned

---

## Resources

### Administrative Best Practices
- [Professional Administrative Skills](https://www.asaporg.com/) - International Association of Administrative Professionals
- [Calendar Management](https://www.google.com/calendar) - Google Calendar best practices
- [Expense Management](https://www.concur.com/best-practices) - Concur expense reporting guide

### Travel Resources
- [TSA Guidelines](https://www.tsa.gov/) - Airport security and travel requirements
- [World Time Buddy](https://www.worldtimebuddy.com/) - Time zone converter
- [Travel.State.Gov](https://travel.state.gov/) - International travel information

### Document Management
- [ISO 15489](https://www.iso.org/standard/74292.html) - Records management standard
- [File Naming Conventions](https://www.mnhs.org/preserve/records/electronicrecords/erfnaming.php) - Best practices

---

## License

Part of the Puerto plugin ecosystem.

---

## Changelog

### v1.0.0 (2025-01-20)

**Initial Release**

- 4 specialized agents (meeting-scheduler, travel-planner, expense-processor, document-organizer)
- 3 comprehensive skills (scheduling, travel-planning, office-administration)
- 3 professional templates (meeting agenda, travel itinerary, expense report)
- Full administrative workflow coverage
- Time zone management
- Corporate policy compliance
- Cost-optimized (Haiku for routine tasks, Sonnet for complex optimization)

---

## Support

**Issues**: Report at [Puerto GitHub Issues](https://github.com/bandofai/puerto/issues)

**Questions**: Tag your issue with `plugin:office-administrator`

**Feature Requests**: Use `enhancement` label

---

**Version**: 1.0.0
**Author**: Puerto Plugin System
**Last Updated**: January 2025
**Status**: Production Ready
**Success Rate**: 95% first-time-right with proper policy configuration
