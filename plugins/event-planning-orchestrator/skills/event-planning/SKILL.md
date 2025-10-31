# Event Planning Skill

Comprehensive patterns and best practices for event planning, coordination, and management.

## Core Principles

1. **Start Early**: Timeline begins 12-52 weeks before event depending on size
2. **Budget First**: Establish total budget and allocate by category before booking
3. **Track Everything**: Document all decisions, payments, and communications
4. **Communicate Clearly**: Maintain regular contact with vendors and guests
5. **Build Contingencies**: Plan for 10-15% budget overruns and backup vendors

## Event Types

### Wedding Events
- Timeline: 12-18 months planning period
- Budget categories: Venue (25%), Catering (30%), Photography (10%), Music (8%), Florist (8%), Attire (8%), Other (11%)
- Critical milestones: Venue (12mo), Vendors (6-8mo), Invites (3mo), Final details (1mo)

### Party Events
- Timeline: 2-6 months planning period
- Budget categories: Venue (20%), Catering (40%), Entertainment (15%), Decorations (10%), Other (15%)
- Critical milestones: Venue (2-3mo), Catering (1-2mo), Invites (4-6 weeks), Finalize (1 week)

### Conference Events
- Timeline: 6-12 months planning period
- Budget categories: Venue (30%), Catering (20%), A/V Equipment (15%), Marketing (15%), Speakers (10%), Other (10%)
- Critical milestones: Venue (6-8mo), Speakers (4-6mo), Registration (2-3mo), Logistics (2-4 weeks)

## Data Structures

### Storage Location
```
~/.event-planner/events/{event-id}/
├── event.json              # Master configuration
├── guests.json             # Guest list
├── vendors.json            # Vendor database
├── budget.json             # Budget tracking
├── timeline.json           # Event timeline
├── tasks.json              # Task checklist
└── seating/
    └── seating-chart.json  # Seating arrangements
```

### Event Configuration Schema
```json
{
  "id": "wedding-2025-06-15",
  "name": "Smith-Johnson Wedding",
  "type": "wedding|party|conference",
  "date": "2025-06-15",
  "time": "16:00",
  "venue": {
    "name": "Garden Estate",
    "address": "123 Main St",
    "capacity": 200,
    "contact": "venue@example.com"
  },
  "guest_count": {
    "invited": 150,
    "confirmed": 120,
    "declined": 15,
    "pending": 15
  },
  "budget": {
    "total": 50000,
    "spent": 35000,
    "remaining": 15000
  }
}
```

### Guest Entry Schema
```json
{
  "id": "guest-001",
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1-555-0123",
  "category": "bride-family",
  "rsvp_status": "pending|confirmed|declined",
  "guest_count": 2,
  "plus_one": {
    "name": "Jane Doe",
    "dietary_restrictions": ["vegetarian"]
  },
  "dietary_restrictions": [],
  "table_assignment": null,
  "invite_sent": "2025-01-01",
  "thank_you_sent": false
}
```

### Vendor Entry Schema
```json
{
  "id": "vendor-catering-001",
  "name": "Delicious Catering Co.",
  "category": "catering",
  "contact": {
    "name": "Mary Chef",
    "email": "mary@delicious.com",
    "phone": "+1-555-0456"
  },
  "quote": 15000,
  "contract_signed": true,
  "deposit_paid": 5000,
  "payment_schedule": [
    {
      "amount": 5000,
      "due_date": "2025-03-01",
      "paid": true
    }
  ]
}
```

## Guest Management Patterns

### RSVP Tracking Workflow
1. Send invitations 12 weeks before (weddings) or 4-6 weeks (parties)
2. Set RSVP deadline 4 weeks before event
3. Send reminder 2 weeks before RSVP deadline
4. Follow up with non-responders 1 week after deadline
5. Finalize headcount 2 weeks before event

### Dietary Restrictions Management
- Collect dietary restrictions on RSVP
- Categorize: Vegetarian, Vegan, Gluten-free, Dairy-free, Nut allergies, Other
- Aggregate totals for catering (include plus-ones)
- Share with caterer 4 weeks before event
- Confirm final counts 1 week before

### Seating Chart Best Practices
- Capacity: 8-10 guests per round table, 6-8 per rectangular table
- Group families together
- Separate conflicting guests
- Mix friend groups for social connection
- Head table/VIP tables for special guests
- Kids table if multiple families with children

## Vendor Coordination Patterns

### Vendor Categories
- **Venue**: Location, tables, chairs, basic setup
- **Catering**: Food, beverages, service staff, bartending
- **Photography**: Photos, video, editing, albums
- **Music/DJ**: Music, MC services, sound equipment
- **Florist**: Flowers, centerpieces, bouquets
- **Other**: Rentals, transportation, invitations, favors

### Payment Schedule Best Practices
- **Deposit**: 25-50% upon contract signing
- **Progress Payment**: 25% at 2-4 weeks before event
- **Final Payment**: Remaining balance 1 week before or day-of

### Contract Checklist
- Scope of services clearly defined
- Payment schedule documented
- Cancellation policy
- Liability insurance verification
- Setup/breakdown times
- Contact information for day-of coordination

## Budget Management Patterns

### Budget Allocation by Event Type

**Wedding (Example: $50,000)**
- Venue: $12,500 (25%)
- Catering: $15,000 (30%)
- Photography: $5,000 (10%)
- Music: $4,000 (8%)
- Florist: $4,000 (8%)
- Attire: $4,000 (8%)
- Invitations: $1,500 (3%)
- Miscellaneous: $4,000 (8%)

**Party (Example: $10,000)**
- Venue: $2,000 (20%)
- Catering: $4,000 (40%)
- Entertainment: $1,500 (15%)
- Decorations: $1,000 (10%)
- Rentals: $500 (5%)
- Miscellaneous: $1,000 (10%)

### Budget Tracking Best Practices
1. Set category budgets before booking vendors
2. Track both budgeted vs. actual costs
3. Monitor paid vs. outstanding balances
4. Alert when category exceeds 90% of budget
5. Maintain 10-15% contingency for overruns

## Timeline Planning Patterns

### Wedding Timeline (12-18 Month Planning)
- **12 months before**: Book venue and major vendors (catering, photography)
- **9-10 months**: Book florist, music/DJ, finalize guest list
- **6-8 months**: Send save-the-dates, book accommodations
- **3-4 months**: Send invitations, finalize menu
- **2 months**: RSVP deadline, create seating chart
- **1 month**: Final vendor confirmations, print materials
- **1 week**: Finalize timeline, confirm headcount, rehearsal
- **Day-of**: Execute timeline, coordinate vendors

### Day-of Timeline Template
```
8:00 AM - Venue access, florist setup
9:00 AM - Catering setup
10:00 AM - Music/AV setup
2:00 PM - Photography begins
4:00 PM - Event start
4:30 PM - Ceremony/program
5:00 PM - Cocktail hour
6:00 PM - Reception/dinner
7:00 PM - Speeches/toasts
8:00 PM - Dancing
10:00 PM - Event end, breakdown begins
```

### Critical Path Milestones
Identify dependencies where one task must complete before another:
- Venue → Catering (menu depends on venue kitchen)
- Guest count → Seating chart
- RSVP deadline → Final vendor confirmations
- Vendor booking → Payment scheduling

## Task Management Patterns

### Task Categories
- **Venue**: Booking, walkthrough, setup coordination
- **Catering**: Menu selection, tastings, headcount confirmation
- **Guests**: Invitations, RSVP tracking, seating chart
- **Vendors**: Booking, contract review, payment tracking
- **Coordination**: Timeline creation, day-of logistics, emergency planning

### Task Priority Levels
- **Critical**: Must complete for event to happen (venue, catering, invitations)
- **High**: Important for event quality (photography, music, florist)
- **Medium**: Nice-to-have enhancements (favors, programs, decorations)
- **Low**: Optional extras (photo booth, special lighting)

### Task Assignment Best Practices
- Assign specific person to each task
- Set realistic deadlines based on event timeline
- Track dependencies (e.g., menu selection requires final guest count)
- Regular check-ins on high-priority tasks
- Escalate overdue critical tasks immediately

## Communication Patterns

### Vendor Communication Schedule
- **Initial Contact**: Get quotes, check availability
- **Booking**: Sign contract, pay deposit
- **Planning Phase**: Monthly check-ins, finalize details
- **Final Month**: Weekly check-ins, confirm logistics
- **Final Week**: Daily contact, finalize timeline
- **Day-of**: On-call coordination

### Guest Communication Timeline
- **Save-the-Dates**: 6-12 months before (weddings)
- **Invitations**: 12 weeks before (weddings), 4-6 weeks before (parties)
- **RSVP Deadline**: 4 weeks before event
- **Event Details**: 2 weeks before (parking, attire, schedule)
- **Thank-you Notes**: 2-4 weeks after event

## Emergency Preparedness

### Backup Plans
- **Venue**: Have backup indoor location for outdoor events
- **Vendors**: Keep contact list of backup vendors by category
- **Weather**: Monitor forecast, have tent/heating/cooling plan
- **Medical**: Know location of first aid kit, emergency contacts

### Day-of Emergency Kit
- Vendor contact list with phone numbers
- Event timeline printed
- First aid kit
- Sewing kit for wardrobe issues
- Stain remover
- Phone chargers
- Cash for tips/emergencies

## Post-Event Follow-up

### Immediate (1-2 Days After)
- Send thank-you to vendors who performed well
- Collect feedback from key coordinators
- Document lessons learned

### Short-term (1-2 Weeks)
- Process final vendor payments
- Review vendor performance for ratings
- Return rented items

### Medium-term (2-4 Weeks)
- Send thank-you notes to guests
- Share photos when available
- Complete post-event financial reconciliation

## Success Metrics

- **Budget**: Stayed within total budget (±5%)
- **Timeline**: Met all critical milestones
- **Guests**: 80%+ RSVP rate, 90%+ satisfaction
- **Vendors**: All showed up, performed as expected
- **Tasks**: 100% critical tasks completed

## Common Pitfalls to Avoid

1. **Under-budgeting**: Add 15% contingency
2. **Late Bookings**: Popular vendors book 6-12 months out
3. **Poor Communication**: Maintain written records of all vendor agreements
4. **No Backup Plans**: Weather, vendor no-shows happen
5. **Inadequate Timeline**: Allow buffer time between activities
6. **Ignoring Dietary Restrictions**: Can create serious medical issues
7. **Late RSVP Follow-up**: Chase non-responders early
8. **Payment Tracking**: Missed payments damage vendor relationships

## Integration Workflows

### Complete Event Planning Workflow
1. **@event-coordinator**: Create new event, set budget
2. **@timeline-planner**: Generate event timeline
3. **@guest-manager**: Import/add guests
4. **@vendor-manager**: Add vendors, track contracts
5. **@budget-tracker**: Allocate budget, track expenses
6. **@task-tracker**: Create comprehensive task list
7. **@event-coordinator**: Generate progress reports monthly
8. **@timeline-planner**: Create day-of schedule 1 week before
9. **@event-coordinator**: Generate final event package

### Monthly Review Workflow
1. Check budget status (on track?)
2. Review RSVP progress
3. Confirm upcoming vendor payments
4. Check timeline milestone completion
5. Review overdue tasks
6. Update event plan as needed

---

**This skill provides the foundation for professional event planning. All agents should reference these patterns for consistency and best practices.**
