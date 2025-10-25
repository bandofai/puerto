# School Management Skill

Comprehensive patterns for school calendar tracking, permission slips, and deadline management.

## School Calendar Structure

```json
{
  "schoolYear": "2024-2025",
  "children": [
    {
      "id": "child-001",
      "name": "Emma",
      "grade": 3,
      "teacher": "Mrs. Johnson",
      "school": "Lincoln Elementary",
      "events": []
    }
  ],
  "events": [
    {
      "id": "event-001",
      "type": "field-trip",
      "title": "Science Museum Field Trip",
      "date": "2025-03-15",
      "childId": "child-001",
      "permissionSlipDue": "2025-03-10",
      "cost": 15,
      "requirements": ["Sack lunch", "Comfortable shoes"],
      "notes": "Departs 8:30 AM, returns 2:30 PM",
      "status": "pending"
    }
  ]
}
```

## Event Types

### School Calendar Events
- **Holidays/Breaks**: Winter break, spring break, summer
- **Early Dismissals**: Half days, teacher planning
- **Parent-Teacher Conferences**: Fall and spring
- **Testing Dates**: Standardized tests, finals
- **Report Cards**: Distribution dates
- **School Events**: Performances, open house, book fair

### Permission Slips
- Field trips
- Special activities
- Media release forms
- Emergency medical authorization
- Photo day purchases
- Fundraiser participation

### Deadlines
- Registration (school, after-school programs)
- Supply lists
- Forms (emergency contacts, health info)
- Payment due dates
- Volunteer signups

## Best Practices

### Reminder System
- Permission slips: 5 days before due date
- Event reminders: 2 days before event
- Registration deadlines: 1 week before
- Payment reminders: 3 days before due
- Conference signups: When announced

### Organization
- Separate calendars per child (if multiple)
- Color-code by event type
- Track confirmation status
- Maintain school contact directory
- Keep digital copies of forms
