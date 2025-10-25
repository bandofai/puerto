# Event Planning Orchestrator

Comprehensive event planning and coordination system for large events (weddings, parties, conferences) with guest management, vendor coordination, budget tracking, and timeline planning.

## Features

### 6 Specialized Agents

1. **event-coordinator** (Sonnet) - Master orchestrator
   - Event initialization and strategic planning
   - Multi-agent workflow coordination
   - Comprehensive event package generation
   - Progress reporting and oversight

2. **guest-manager** (Haiku, Fast) - Guest list operations
   - Add/update guests and RSVPs
   - Dietary restriction tracking
   - Seating chart creation and management
   - Guest list reporting

3. **vendor-manager** (Sonnet) - Vendor relationships
   - Vendor contact database
   - Contract and payment tracking
   - Payment deadline monitoring
   - Vendor performance ratings

4. **budget-tracker** (Haiku, Fast) - Financial management
   - Budget allocation by category
   - Expense tracking and reporting
   - Budget vs. actual monitoring
   - Overrun alerts

5. **timeline-planner** (Sonnet) - Timeline management
   - Event timeline generation from templates
   - Milestone and dependency tracking
   - Deadline monitoring and alerts
   - Day-of schedule creation

6. **task-tracker** (Haiku, Fast) - Task management
   - Comprehensive task checklists
   - Task assignment and tracking
   - Deadline monitoring
   - Progress reporting

### 1 Comprehensive Skill

**event-planning** - Complete patterns for:
- Event type templates (wedding, party, conference)
- Guest management workflows
- Vendor coordination strategies
- Budget allocation guidelines
- Timeline planning patterns
- Task management best practices
- Communication schedules
- Emergency preparedness

### Templates

1. **wedding-budget-template.json**: Budget allocation for $50k wedding
2. **party-budget-template.json**: Budget allocation for $10k party

## Installation

```bash
# Install plugin (when available)
/plugin install event-planning-orchestrator@puerto

# Or clone manually
git clone [repo-url] ~/.claude/plugins/event-planning-orchestrator
```

## Quick Start

### 1. Initialize Event Planner

```bash
@event-coordinator "Initialize event planner system"
```

### 2. Create Your Event

```bash
# Wedding example
@event-coordinator "Create wedding event for June 15, 2025, 150 guests, budget $50,000"

# Party example
@event-coordinator "Create birthday party event for August 20, 2025, 50 guests, budget $5,000"
```

### 3. Set Up Guest List

```bash
# Add individual guests
@guest-manager "Add guest: John Doe, email john@example.com, category bride-family"

# Import from CSV (if available)
@guest-manager "Import guest list from wedding-guests.csv"
```

### 4. Add Vendors

```bash
@vendor-manager "Add caterer: Delicious Catering, quote $15,000, contact Mary Chef mary@delicious.com +1-555-0456"

@vendor-manager "Add photographer: Picture Perfect, quote $3,500"
```

### 5. Track Budget

```bash
@budget-tracker "Initialize budget with wedding template"

@budget-tracker "Record expense: catering deposit $5,000"

@budget-tracker "Show budget summary"
```

### 6. Create Timeline

```bash
@timeline-planner "Create wedding timeline for June 15, 2025"

@timeline-planner "Show upcoming deadlines in next 30 days"
```

### 7. Manage Tasks

```bash
@task-tracker "Add task: Finalize menu with caterer, due March 15, priority high, assign to Bob"

@task-tracker "Show all pending tasks"
```

## Common Workflows

### Complete Event Setup

```bash
# 1. Create event
@event-coordinator "Create wedding for June 15, 2025, 150 guests, $50k budget"

# 2. Set up timeline
@timeline-planner "Create wedding timeline for June 15, 2025"

# 3. Initialize budget
@budget-tracker "Initialize wedding budget"

# 4. Add vendors
@vendor-manager "Add venue: Garden Estate, quote $12,500"
@vendor-manager "Add caterer: Delicious Catering, quote $15,000"

# 5. Start guest list
@guest-manager "Add guest: John Doe, bride-family, john@example.com"
```

### Monthly Progress Review

```bash
# Check overall status
@event-coordinator "Generate event overview for wedding-2025-06-15"

# Review budget
@budget-tracker "Show budget summary"

# Check RSVPs
@guest-manager "Show RSVP summary"

# Vendor payments
@vendor-manager "Check payment deadlines for next 30 days"

# Timeline progress
@timeline-planner "Show upcoming deadlines"

# Task status
@task-tracker "Show overdue tasks"
```

### Pre-Event Final Checks

```bash
# Generate comprehensive package
@event-coordinator "Generate complete event package for wedding-2025-06-15"

# Create day-of schedule
@timeline-planner "Generate day-of schedule for June 15, 2025"

# Final guest count
@guest-manager "Show dietary restrictions summary"

# Vendor contacts
@vendor-manager "Show all vendor contacts"

# Outstanding tasks
@task-tracker "Show all pending tasks"
```

## Data Storage

Events are stored locally in:
- **User-level**: `~/.event-planner/` (recommended for personal events)
- **Project-level**: `.event-planner/` (for shared/team events)

Directory structure per event:
```
.event-planner/events/{event-id}/
├── event.json              # Master event configuration
├── guests.json             # Guest list with RSVPs
├── vendors.json            # Vendor database
├── budget.json             # Budget tracking
├── timeline.json           # Event timeline
├── tasks.json              # Task checklist
├── seating/
│   └── seating-chart.json  # Seating arrangements
├── documents/
│   ├── contracts/          # Vendor contracts
│   └── correspondence/     # Email records
└── reports/
    ├── event-package.md    # Comprehensive event package
    └── day-of-schedule.md  # Day-of timeline
```

## Event Types Supported

### Weddings
- 12-18 month planning timeline
- Full vendor coordination
- Guest RSVP tracking with dietary restrictions
- Seating chart management
- Budget allocation: Venue (25%), Catering (30%), Photography (10%), Music (8%), Florist (8%), Attire (8%), Other (11%)

### Parties
- 2-6 month planning timeline
- Simplified vendor management
- Guest list and RSVP tracking
- Budget allocation: Venue (20%), Catering (40%), Entertainment (15%), Decorations (10%), Other (15%)

### Conferences
- 6-12 month planning timeline
- Speaker and exhibitor management
- Registration tracking
- Budget allocation: Venue (30%), Catering (20%), A/V (15%), Marketing (15%), Speakers (10%), Other (10%)

## Key Features

### Guest Management
- Add/update guests individually or bulk import
- Track RSVP status (invited, confirmed, declined, pending)
- Manage dietary restrictions and special needs
- Plus-one tracking
- Seating chart creation with auto-assignment
- Guest category organization

### Vendor Coordination
- Vendor contact database by category
- Quote comparison and tracking
- Contract status monitoring
- Payment schedule management
- Deadline alerts (7/14/30 days before)
- Vendor performance ratings

### Budget Tracking
- Category-based budget allocation
- Real-time expense tracking
- Budget vs. actual comparison
- Overrun alerts (at 90% and over 100%)
- Payment tracking (paid vs. outstanding)
- Financial forecasting

### Timeline Planning
- Event type templates (wedding, party, conference)
- Critical milestone tracking
- Dependency management
- Deadline alerts with urgency levels
- Day-of schedule generation
- Progress monitoring

### Task Management
- Comprehensive task checklists
- Priority levels (critical, high, medium, low)
- Task assignment and tracking
- Deadline monitoring
- Overdue task alerts
- Category-based organization
- Progress reporting

## Best Practices

1. **Start Early**: Initialize event 12-18 months before for weddings, 2-6 months for parties
2. **Budget First**: Set and allocate budget before booking vendors
3. **Track Everything**: Document all decisions, payments, and communications
4. **Regular Reviews**: Monthly progress checks, weekly in final month
5. **Build Contingencies**: Plan for 10-15% budget overruns
6. **Clear Communication**: Maintain written records of all vendor agreements
7. **Backup Plans**: Have backup vendors and weather contingencies
8. **Final Confirmations**: Confirm all vendors 1 week before event

## Model Selection

- **Sonnet agents** (event-coordinator, vendor-manager, timeline-planner): Strategic planning, analysis, and complex coordination
- **Haiku agents** (guest-manager, budget-tracker, task-tracker): Fast CRUD operations, calculations, and data management

This optimizes for both capability and cost-efficiency.

## Integration with Other Plugins

- **Orchestrator Plugin**: Coordinate multi-event weekends (rehearsal dinner, wedding, brunch)
- **Subagent Creator**: Create specialized agents for unique event types

## Performance

- **Small events** (<50 guests): All operations instant
- **Medium events** (50-200 guests): Fast response, slight delay in seating chart
- **Large events** (200+ guests): Consider batch operations for complex tasks

## Troubleshooting

### Event not found
```bash
# List all events
ls ~/.event-planner/events/
```

### Re-initialize event planner
```bash
@event-coordinator "Initialize event planner system"
```

### Data validation
```bash
# Check JSON format
cat ~/.event-planner/events/*/event.json | python -m json.tool
```

## Contributing

This plugin follows Puerto plugin architecture with:
- Skill-aware agents (all agents read event-planning skill)
- Local-first data storage
- JSON-based data structures
- Python for complex operations

## License

MIT

## Support

For issues and feature requests, visit the Puerto repository.

---

**Generated as part of Puerto Plugin Collection - Issue #140**
