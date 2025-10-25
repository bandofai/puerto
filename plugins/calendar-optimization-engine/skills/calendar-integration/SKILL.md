# Calendar Integration Skill

**Expert patterns for Google Calendar and Outlook API integration, authentication, and event management**

## Core Principles

1. **Authentication First**: Secure OAuth 2.0 flows for all calendar access
2. **Rate Limiting**: Respect API quotas and implement exponential backoff
3. **Data Normalization**: Standardize event formats across providers
4. **Error Handling**: Graceful degradation when APIs are unavailable
5. **Incremental Sync**: Efficient delta synchronization for large calendars

---

## Google Calendar API Integration

### Authentication

**OAuth 2.0 Flow**:

```python
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request

# Step 1: Create OAuth flow
flow = Flow.from_client_secrets_file(
    'credentials.json',
    scopes=['https://www.googleapis.com/auth/calendar.readonly'],
    redirect_uri='http://localhost:8080/oauth2callback'
)

# Step 2: Get authorization URL
auth_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true'
)

# Step 3: Exchange authorization code for tokens
flow.fetch_token(code=authorization_code)
credentials = flow.credentials

# Step 4: Save credentials for future use
with open('token.json', 'w') as token:
    token.write(credentials.to_json())
```

**Token Refresh**:

```python
def get_credentials():
    """Load and refresh credentials."""
    creds = None

    # Load saved credentials
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    # Refresh if expired
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        # Save refreshed credentials
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds
```

### Event Operations

**List Events**:

```python
from googleapiclient.discovery import build

def list_events(start_date, end_date, calendar_id='primary'):
    """
    Fetch events from Google Calendar.

    Args:
        start_date: ISO 8601 date string
        end_date: ISO 8601 date string
        calendar_id: Calendar ID (default: 'primary')

    Returns:
        List of events
    """
    service = build('calendar', 'v3', credentials=get_credentials())

    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=f'{start_date}T00:00:00Z',
        timeMax=f'{end_date}T23:59:59Z',
        singleEvents=True,  # Expand recurring events
        orderBy='startTime',
        maxResults=2500  # Max per request
    ).execute()

    return events_result.get('items', [])
```

**Create Event**:

```python
def create_event(summary, start_time, end_time, attendees=None, description=''):
    """
    Create new calendar event.

    Args:
        summary: Event title
        start_time: ISO 8601 datetime with timezone
        end_time: ISO 8601 datetime with timezone
        attendees: List of email addresses
        description: Event description

    Returns:
        Created event object
    """
    service = build('calendar', 'v3', credentials=get_credentials())

    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'America/New_York',
        },
        'attendees': [{'email': email} for email in (attendees or [])],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    created_event = service.events().insert(
        calendarId='primary',
        body=event
    ).execute()

    return created_event
```

**Update Event**:

```python
def update_event(event_id, updates):
    """
    Update existing event.

    Args:
        event_id: Google Calendar event ID
        updates: Dictionary of fields to update

    Returns:
        Updated event object
    """
    service = build('calendar', 'v3', credentials=get_credentials())

    # Fetch current event
    event = service.events().get(
        calendarId='primary',
        eventId=event_id
    ).execute()

    # Apply updates
    event.update(updates)

    # Save changes
    updated_event = service.events().update(
        calendarId='primary',
        eventId=event_id,
        body=event
    ).execute()

    return updated_event
```

**Delete Event**:

```python
def delete_event(event_id):
    """Delete calendar event."""
    service = build('calendar', 'v3', credentials=get_credentials())

    service.events().delete(
        calendarId='primary',
        eventId=event_id
    ).execute()
```

### Batch Operations

**Efficient Batch Requests**:

```python
from googleapiclient.http import BatchHttpRequest

def batch_operations(operations):
    """
    Execute multiple operations in single request.

    Args:
        operations: List of (method, event_id, body) tuples

    Example:
        operations = [
            ('get', 'event1', None),
            ('patch', 'event2', {'summary': 'Updated Title'}),
            ('delete', 'event3', None)
        ]
    """
    service = build('calendar', 'v3', credentials=get_credentials())

    def callback(request_id, response, exception):
        if exception:
            print(f'Request {request_id} failed: {exception}')
        else:
            print(f'Request {request_id} succeeded: {response}')

    batch = service.new_batch_http_request(callback=callback)

    for method, event_id, body in operations:
        if method == 'get':
            batch.add(service.events().get(
                calendarId='primary',
                eventId=event_id
            ))
        elif method == 'patch':
            batch.add(service.events().patch(
                calendarId='primary',
                eventId=event_id,
                body=body
            ))
        elif method == 'delete':
            batch.add(service.events().delete(
                calendarId='primary',
                eventId=event_id
            ))

    batch.execute()
```

---

## Outlook/Microsoft Graph API Integration

### Authentication

**OAuth 2.0 with Microsoft Identity**:

```python
import msal

# Configuration
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
TENANT_ID = 'common'
AUTHORITY = f'https://login.microsoftonline.com/{TENANT_ID}'
SCOPES = ['Calendars.ReadWrite']

# Create MSAL app
app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
    client_credential=CLIENT_SECRET
)

def get_access_token():
    """Get access token for Microsoft Graph."""
    # Try to get from cache first
    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
        if result:
            return result['access_token']

    # If not cached, get new token
    result = app.acquire_token_for_client(scopes=SCOPES)

    if 'access_token' in result:
        return result['access_token']
    else:
        raise Exception(f"Failed to get token: {result.get('error_description')}")
```

### Event Operations

**List Events**:

```python
import requests

def list_outlook_events(start_date, end_date):
    """
    Fetch events from Outlook calendar.

    Args:
        start_date: ISO 8601 date string
        end_date: ISO 8601 date string

    Returns:
        List of events
    """
    access_token = get_access_token()

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Microsoft Graph API endpoint
    url = 'https://graph.microsoft.com/v1.0/me/calendar/events'

    params = {
        '$filter': f"start/dateTime ge '{start_date}T00:00:00' and end/dateTime le '{end_date}T23:59:59'",
        '$orderby': 'start/dateTime',
        '$top': 1000
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json().get('value', [])
```

**Create Event**:

```python
def create_outlook_event(subject, start_time, end_time, attendees=None):
    """
    Create event in Outlook calendar.

    Args:
        subject: Event title
        start_time: ISO 8601 datetime
        end_time: ISO 8601 datetime
        attendees: List of email addresses

    Returns:
        Created event object
    """
    access_token = get_access_token()

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    event = {
        'subject': subject,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Eastern Standard Time'
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Eastern Standard Time'
        },
        'attendees': [
            {
                'emailAddress': {'address': email},
                'type': 'required'
            }
            for email in (attendees or [])
        ]
    }

    url = 'https://graph.microsoft.com/v1.0/me/calendar/events'
    response = requests.post(url, headers=headers, json=event)
    response.raise_for_status()

    return response.json()
```

---

## Data Normalization

### Standard Event Format

**Normalize events from any provider**:

```python
def normalize_event(event, provider='google'):
    """
    Convert provider-specific event to standard format.

    Standard Format:
    {
        'event_id': str,
        'provider': 'google' | 'outlook',
        'summary': str,
        'description': str,
        'start': ISO 8601 datetime with timezone,
        'end': ISO 8601 datetime with timezone,
        'timezone': str,
        'location': str,
        'attendees': List[dict],
        'recurrence': dict | None,
        'status': str,
        'visibility': str,
        'category': str,  # auto-classified
        'duration_minutes': int,
        'created_at': ISO 8601 datetime,
        'updated_at': ISO 8601 datetime
    }
    """
    if provider == 'google':
        return normalize_google_event(event)
    elif provider == 'outlook':
        return normalize_outlook_event(event)
    else:
        raise ValueError(f'Unknown provider: {provider}')

def normalize_google_event(event):
    """Normalize Google Calendar event."""
    from datetime import datetime
    from dateutil import parser

    # Parse times
    start = event['start'].get('dateTime', event['start'].get('date'))
    end = event['end'].get('dateTime', event['end'].get('date'))

    start_dt = parser.isoparse(start)
    end_dt = parser.isoparse(end)
    duration_minutes = int((end_dt - start_dt).total_seconds() / 60)

    normalized = {
        'event_id': event['id'],
        'provider': 'google',
        'summary': event.get('summary', 'No Title'),
        'description': event.get('description', ''),
        'start': start,
        'end': end,
        'timezone': event['start'].get('timeZone', 'UTC'),
        'location': event.get('location', ''),
        'attendees': [
            {
                'email': a.get('email'),
                'name': a.get('displayName', ''),
                'status': a.get('responseStatus', 'needsAction')
            }
            for a in event.get('attendees', [])
        ],
        'recurrence': event.get('recurrence'),
        'status': event.get('status', 'confirmed'),
        'visibility': event.get('visibility', 'default'),
        'category': auto_categorize_event(event),
        'duration_minutes': duration_minutes,
        'created_at': event.get('created'),
        'updated_at': event.get('updated')
    }

    return normalized

def normalize_outlook_event(event):
    """Normalize Outlook/Graph API event."""
    start = event['start']['dateTime']
    end = event['end']['dateTime']

    # Calculate duration
    from dateutil import parser
    start_dt = parser.isoparse(start)
    end_dt = parser.isoparse(end)
    duration_minutes = int((end_dt - start_dt).total_seconds() / 60)

    normalized = {
        'event_id': event['id'],
        'provider': 'outlook',
        'summary': event.get('subject', 'No Title'),
        'description': event.get('body', {}).get('content', ''),
        'start': start,
        'end': end,
        'timezone': event['start'].get('timeZone', 'UTC'),
        'location': event.get('location', {}).get('displayName', ''),
        'attendees': [
            {
                'email': a['emailAddress']['address'],
                'name': a['emailAddress'].get('name', ''),
                'status': a['status']['response']
            }
            for a in event.get('attendees', [])
        ],
        'recurrence': event.get('recurrence'),
        'status': event.get('status', 'confirmed'),
        'visibility': event.get('sensitivity', 'normal'),
        'category': auto_categorize_event(event),
        'duration_minutes': duration_minutes,
        'created_at': event.get('createdDateTime'),
        'updated_at': event.get('lastModifiedDateTime')
    }

    return normalized
```

### Auto-Categorization

```python
def auto_categorize_event(event):
    """
    Automatically categorize event based on metadata.

    Categories:
    - meeting: Group meetings
    - one_on_one: 1:1 meetings
    - focus_time: Blocked focus time
    - break: Lunch, breaks
    - learning: Training, courses
    - admin: Administrative tasks
    - personal: Personal appointments
    """
    summary = event.get('summary', '').lower()
    attendee_count = len(event.get('attendees', []))

    # Focus time
    if any(kw in summary for kw in ['focus', 'deep work', 'coding time', 'writing']):
        return 'focus_time'

    # Breaks
    if any(kw in summary for kw in ['lunch', 'break', 'coffee']):
        return 'break'

    # Learning
    if any(kw in summary for kw in ['training', 'course', 'learning', 'workshop']):
        return 'learning'

    # 1:1s
    if '1:1' in summary or '1-on-1' in summary or attendee_count == 2:
        return 'one_on_one'

    # Admin
    if any(kw in summary for kw in ['admin', 'expenses', 'planning', 'email']):
        return 'admin'

    # Personal
    if any(kw in summary for kw in ['doctor', 'dentist', 'personal', 'appointment']):
        return 'personal'

    # Default to meeting if has attendees
    if attendee_count > 0:
        return 'meeting'

    return 'other'
```

---

## Error Handling & Rate Limiting

### Exponential Backoff

```python
import time
from googleapiclient.errors import HttpError

def api_call_with_retry(api_function, *args, max_retries=5, **kwargs):
    """
    Execute API call with exponential backoff on rate limiting.

    Google Calendar quota: 1,000,000 queries/day
    Outlook quota: 10,000 requests/10 min
    """
    for retry in range(max_retries):
        try:
            return api_function(*args, **kwargs)

        except HttpError as e:
            if e.resp.status == 429:  # Rate limit exceeded
                wait_time = (2 ** retry) + (random.random() * 0.1)
                print(f'Rate limited. Waiting {wait_time:.1f}s before retry {retry + 1}/{max_retries}')
                time.sleep(wait_time)

            elif e.resp.status >= 500:  # Server error
                wait_time = (2 ** retry)
                print(f'Server error. Waiting {wait_time}s before retry {retry + 1}/{max_retries}')
                time.sleep(wait_time)

            else:
                # Client error, don't retry
                raise

        except Exception as e:
            print(f'Unexpected error: {e}')
            raise

    raise Exception(f'Max retries ({max_retries}) exceeded')
```

### Graceful Degradation

```python
def fetch_events_safe(start_date, end_date):
    """
    Fetch events with graceful degradation.

    Fallback strategy:
    1. Try Google Calendar API
    2. If fails, try cached data
    3. If no cache, return empty with error message
    """
    try:
        events = list_events(start_date, end_date)
        # Cache successful result
        cache_events(events, start_date, end_date)
        return events

    except Exception as e:
        print(f'API call failed: {e}')

        # Try cache
        cached = get_cached_events(start_date, end_date)
        if cached:
            print('Using cached events (may be stale)')
            return cached

        # No fallback available
        print('No cached data available')
        return []
```

---

## Incremental Sync

### Delta Synchronization

```python
def incremental_sync(sync_token=None):
    """
    Perform incremental sync using delta/sync tokens.

    Benefits:
    - Only fetch changed events
    - Reduces API calls
    - Faster synchronization

    Google Calendar uses syncToken
    Outlook uses deltaLink
    """
    service = build('calendar', 'v3', credentials=get_credentials())

    page_token = None
    all_events = []

    while True:
        if sync_token:
            # Incremental sync
            events = service.events().list(
                calendarId='primary',
                syncToken=sync_token
            ).execute()
        else:
            # Full sync
            events = service.events().list(
                calendarId='primary',
                pageToken=page_token
            ).execute()

        all_events.extend(events.get('items', []))

        page_token = events.get('nextPageToken')
        if not page_token:
            break

    # Save sync token for next incremental sync
    new_sync_token = events.get('nextSyncToken')

    return all_events, new_sync_token
```

---

## Best Practices

### 1. Authentication
- [ ] Use OAuth 2.0 (never API keys for user data)
- [ ] Store tokens securely (encrypted)
- [ ] Implement automatic token refresh
- [ ] Handle expired tokens gracefully
- [ ] Request minimum necessary scopes

### 2. API Calls
- [ ] Use batch operations when possible (50+ events)
- [ ] Implement exponential backoff for rate limiting
- [ ] Cache results to minimize API calls
- [ ] Use incremental sync for large calendars
- [ ] Respect quota limits

### 3. Data Handling
- [ ] Normalize all events to standard format
- [ ] Handle timezone conversions correctly (ISO 8601)
- [ ] Auto-categorize events for analytics
- [ ] Validate event data before creating
- [ ] Handle recurring events properly

### 4. Error Handling
- [ ] Catch and log all API errors
- [ ] Provide fallback to cached data
- [ ] Display clear error messages to users
- [ ] Implement retry logic for transient errors
- [ ] Monitor API health and quotas

### 5. Performance
- [ ] Use pagination for large result sets
- [ ] Implement local caching (1-hour TTL)
- [ ] Minimize API calls with batch operations
- [ ] Use webhooks for real-time updates (advanced)
- [ ] Optimize date range queries

---

## Common Patterns

### Pattern 1: Full Calendar Import

```python
def import_full_calendar(start_date, end_date):
    """Import all events in date range."""
    events = api_call_with_retry(list_events, start_date, end_date)
    normalized = [normalize_event(e, 'google') for e in events]

    # Save to local storage
    save_events(normalized)

    return normalized
```

### Pattern 2: Real-time Sync

```python
def setup_realtime_sync():
    """
    Set up real-time sync using webhooks (advanced).

    Google Calendar: Push notifications
    Outlook: Change notifications (webhooks)
    """
    # Register webhook
    # Process notifications
    # Update local data
    pass  # Implementation varies by provider
```

### Pattern 3: Multi-Calendar Aggregation

```python
def aggregate_calendars(calendar_ids):
    """Aggregate events from multiple calendars."""
    all_events = []

    for cal_id in calendar_ids:
        events = list_events(
            start_date='2025-01-01',
            end_date='2025-01-31',
            calendar_id=cal_id
        )
        all_events.extend(events)

    # Sort by start time
    all_events.sort(key=lambda e: e['start'])

    return all_events
```

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: Calendar import, event management, multi-provider integration
