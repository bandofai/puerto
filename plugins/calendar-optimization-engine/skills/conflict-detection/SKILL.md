# Conflict Detection Skill

**Expert patterns for calendar conflict detection, buffer time analysis, and scheduling optimization**

## Core Principles

1. **Early Detection**: Identify conflicts before they cause problems
2. **Severity Classification**: Prioritize critical issues over minor ones
3. **Automatic Resolution**: Suggest fixes, don't just report problems
4. **Proactive Prevention**: Set rules to prevent future conflicts
5. **Context Awareness**: Consider meeting type, attendees, and priorities

---

## Conflict Types

### 1. Double Booking (Critical)

**Definition**: Two or more events overlap in time

**Detection Algorithm**:
```python
def detect_double_bookings(events):
    """
    Find all overlapping events.

    Algorithm: O(n²) brute force for small calendars
    For large calendars: Use interval tree O(n log n)
    """
    conflicts = []

    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            if events_overlap(events[i], events[j]):
                conflicts.append({
                    'type': 'double_booking',
                    'severity': 'critical',
                    'events': [events[i], events[j]],
                    'overlap_minutes': calculate_overlap(events[i], events[j])
                })

    return conflicts

def events_overlap(event1, event2):
    """Check if two events overlap."""
    return (event1['start'] < event2['end'] and
            event2['start'] < event1['end'])
```

**Resolution Strategies**:
- Decline one event
- Reschedule to next available slot
- Delegate attendance
- Request meeting recording

### 2. Buffer Violations (High/Medium)

**Definition**: Insufficient time between consecutive events

**Recommended Buffers**:
- Between meetings: 15 minutes minimum
- Before important meetings: 30 minutes (prep time)
- After long meetings (90+ min): 15-30 minutes (recovery)
- Between locations: 30-60 minutes (travel time)

**Detection Algorithm**:
```python
def detect_buffer_violations(events, min_buffer=15):
    """
    Check for insufficient buffer time.

    Severity levels:
    - Critical: <5 minutes (back-to-back)
    - High: 5-10 minutes
    - Medium: 10-15 minutes
    """
    violations = []
    sorted_events = sorted(events, key=lambda e: e['start'])

    for i in range(len(sorted_events) - 1):
        current_end = sorted_events[i]['end']
        next_start = sorted_events[i + 1]['start']

        buffer_minutes = (next_start - current_end).total_seconds() / 60

        if 0 <= buffer_minutes < min_buffer:
            severity = (
                'critical' if buffer_minutes < 5 else
                'high' if buffer_minutes < 10 else
                'medium'
            )

            violations.append({
                'type': 'buffer_violation',
                'severity': severity,
                'events': [sorted_events[i], sorted_events[i + 1]],
                'buffer_minutes': buffer_minutes,
                'shortfall': min_buffer - buffer_minutes
            })

    return violations
```

**Resolution Strategies**:
- Shorten first meeting by X minutes
- Start second meeting X minutes later
- Make one meeting async
- Combine related meetings

### 3. Timezone Conflicts (Medium)

**Definition**: Events scheduled in inappropriate timezones or unusual hours

**Detection Patterns**:
```python
def detect_timezone_issues(events):
    """
    Identify timezone-related scheduling issues.

    Red flags:
    - Events before 7am or after 9pm local time
    - Cross-timezone meetings at inconvenient times
    - Timezone mismatches in event data
    """
    issues = []

    for event in events:
        event_time = parse_datetime(event['start'])
        hour = event_time.hour

        # Flag unusual hours
        if hour < 7:
            issues.append({
                'type': 'early_morning',
                'severity': 'medium',
                'event': event,
                'hour': hour,
                'message': f'Event at {hour}:00 (before normal work hours)'
            })

        elif hour >= 21:
            issues.append({
                'type': 'late_night',
                'severity': 'medium',
                'event': event,
                'hour': hour,
                'message': f'Event at {hour}:00 (after normal work hours)'
            })

        # Check multi-timezone meetings
        if has_international_attendees(event):
            if not is_timezone_friendly(event):
                issues.append({
                    'type': 'timezone_unfriendly',
                    'severity': 'medium',
                    'event': event,
                    'message': 'Meeting time may be inconvenient for some attendees'
                })

    return issues
```

### 4. Travel Time Conflicts (High)

**Definition**: Insufficient time to travel between physical locations

**Detection Algorithm**:
```python
def detect_travel_conflicts(events):
    """
    Identify impossible travel between locations.

    Travel time estimates:
    - Same building: 5 minutes
    - Same campus: 15 minutes
    - Same city: 30-60 minutes
    - Different cities: 2+ hours
    """
    conflicts = []
    sorted_events = sorted(events, key=lambda e: e['start'])

    for i in range(len(sorted_events) - 1):
        current = sorted_events[i]
        next_event = sorted_events[i + 1]

        # Skip virtual meetings
        if is_virtual(current) or is_virtual(next_event):
            continue

        # Check if locations differ
        if locations_differ(current, next_event):
            time_available = (
                (next_event['start'] - current['end']).total_seconds() / 60
            )
            required_time = estimate_travel_time(
                current['location'],
                next_event['location']
            )

            if time_available < required_time:
                conflicts.append({
                    'type': 'travel_conflict',
                    'severity': 'high',
                    'events': [current, next_event],
                    'time_available': time_available,
                    'time_required': required_time,
                    'shortfall': required_time - time_available
                })

    return conflicts

def is_virtual(event):
    """Check if meeting is virtual."""
    location = event.get('location', '').lower()
    virtual_keywords = ['zoom', 'meet', 'teams', 'webex', 'virtual', 'http']
    return any(kw in location for kw in virtual_keywords)
```

### 5. Priority Conflicts (Low)

**Definition**: High-priority events conflicting with other commitments

```python
def detect_priority_conflicts(events):
    """
    Flag when high-priority events conflict.

    Priority indicators:
    - Event marked as "high priority"
    - Client meetings
    - Executive meetings
    - Recurring 1:1s with manager
    """
    conflicts = []

    high_priority = [e for e in events if is_high_priority(e)]

    for hp_event in high_priority:
        overlapping = find_overlapping_events(hp_event, events)
        if overlapping:
            conflicts.append({
                'type': 'priority_conflict',
                'severity': 'low',
                'high_priority_event': hp_event,
                'conflicting_events': overlapping,
                'recommendation': 'Reschedule conflicting events to protect high-priority time'
            })

    return conflicts
```

---

## Resolution Strategies

### Strategy Matrix

| Conflict Type | Automatic Fix | User Action Required | Prevention |
|---------------|--------------|---------------------|-----------|
| Double Booking | Decline lower priority | Choose which to attend | Enable conflict warnings |
| Buffer Violation | Suggest reschedule | Adjust times | Add default buffer settings |
| Timezone Issue | Flag for review | Confirm timezone | Multi-timezone checking |
| Travel Conflict | Make one virtual | Reschedule or adjust location | Location-aware scheduling |
| Priority Conflict | Flag for user | Protect high-priority time | Priority-based booking rules |

### Automatic Resolution Engine

```python
def suggest_resolution(conflict):
    """
    Generate actionable resolution suggestions.

    Returns ranked list of solutions by feasibility.
    """
    suggestions = []

    if conflict['type'] == 'double_booking':
        suggestions = [
            {
                'action': 'decline_lower_priority',
                'description': f"Decline {identify_lower_priority(conflict)}",
                'effort': 'low',
                'impact': 'high'
            },
            {
                'action': 'reschedule',
                'description': f"Reschedule to {find_next_slot(conflict)}",
                'effort': 'medium',
                'impact': 'high'
            },
            {
                'action': 'delegate',
                'description': 'Delegate attendance to team member',
                'effort': 'medium',
                'impact': 'medium'
            }
        ]

    elif conflict['type'] == 'buffer_violation':
        shortfall = conflict['shortfall']
        suggestions = [
            {
                'action': 'shorten_first',
                'description': f"End first meeting {shortfall} min earlier",
                'effort': 'low',
                'impact': 'high'
            },
            {
                'action': 'delay_second',
                'description': f"Start second meeting {shortfall} min later",
                'effort': 'medium',
                'impact': 'high'
            },
            {
                'action': 'make_async',
                'description': 'Convert one meeting to email update',
                'effort': 'low',
                'impact': 'high'
            }
        ]

    # Rank by effort/impact ratio
    suggestions.sort(key=lambda s: (s['effort'], -impact_score(s['impact'])))

    return suggestions
```

---

## Conflict Prevention Rules

### Proactive Rules

**Rule 1: Buffer Time Enforcement**
```python
# Automatically add buffer to all meetings
def add_default_buffers(events):
    """
    Add 15-minute buffer after each meeting.

    Implementation: Shorten meeting by 5 minutes OR
    add 15-minute "buffer" event after
    """
    for event in events:
        if event['category'] == 'meeting':
            # Option A: Shorten meeting
            event['end'] = event['end'] - timedelta(minutes=5)

            # Option B: Add buffer block
            create_buffer_event(
                start=event['end'],
                duration=15,
                title='Buffer Time'
            )
```

**Rule 2: Meeting Window Restrictions**
```python
# Only allow meetings during designated windows
MEETING_WINDOWS = {
    'monday': [('10:00', '12:00'), ('14:00', '16:00')],
    'tuesday': [('10:00', '12:00'), ('14:00', '16:00')],
    'wednesday': [('14:00', '16:00')],  # Deep work day
    'thursday': [('10:00', '12:00'), ('14:00', '16:00')],
    'friday': [('10:00', '11:30')]  # Light Friday
}

def validate_meeting_time(event):
    """Check if meeting falls within allowed windows."""
    day = event['start'].strftime('%A').lower()
    hour = event['start'].hour

    windows = MEETING_WINDOWS.get(day, [])

    for window_start, window_end in windows:
        if is_within_window(event, window_start, window_end):
            return True

    return False  # Outside allowed windows
```

**Rule 3: Focus Time Protection**
```python
# Protect morning focus blocks
PROTECTED_BLOCKS = [
    {'days': ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'],
     'start': '08:00',
     'end': '10:00',
     'type': 'focus_time'}
]

def is_protected_time(event_time):
    """Check if time falls within protected block."""
    for block in PROTECTED_BLOCKS:
        if event_time.strftime('%A').lower() in block['days']:
            if is_within_time_range(event_time, block['start'], block['end']):
                return True
    return False
```

**Rule 4: No Lunch Meetings**
```python
# Enforce lunch break
LUNCH_BREAK = {'start': '12:00', 'end': '13:00'}

def validate_no_lunch_meeting(event):
    """Prevent meetings during lunch."""
    event_start_hour = event['start'].hour
    event_end_hour = event['end'].hour

    if 12 <= event_start_hour < 13 or 12 < event_end_hour <= 13:
        return False  # Conflicts with lunch

    return True
```

---

## Quality Checklist

- [ ] All conflict types detected
- [ ] Severity levels assigned accurately
- [ ] Resolution suggestions are actionable
- [ ] Prevention rules can be enforced
- [ ] Timezone handling is correct
- [ ] Virtual vs in-person distinguished
- [ ] Travel time estimates realistic
- [ ] Priority conflicts identified
- [ ] User notifications are clear
- [ ] False positives minimized

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: Conflict detection, buffer validation, travel planning, schedule optimization
