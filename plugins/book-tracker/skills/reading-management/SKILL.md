# Reading Management Skill

Comprehensive patterns and standards for book tracking, progress monitoring, and reading analytics.

## Data Structure Standards

### Book Entry Schema

```json
{
  "id": "uuid-v4",
  "isbn": "978-XXXXXXXXXX",
  "title": "Book Title",
  "subtitle": "Optional Subtitle",
  "authors": ["Author Name"],
  "publisher": "Publisher Name",
  "published_year": 2024,
  "edition": "First Edition",
  "pages": 350,
  "language": "en",
  "genres": ["Genre1", "Genre2"],
  "tags": ["tag1", "tag2"],
  "cover_url": "https://...",
  "description": "Book description...",
  "status": "to-read|reading|completed|abandoned",
  "date_added": "2025-01-20T10:00:00Z",
  "date_started": "2025-01-25T08:00:00Z",
  "date_completed": null,
  "rating": null,
  "format": "physical|ebook|audiobook",
  "owned": true,
  "source": "purchased|library|gift|manual",
  "metadata": {
    "goodreads_id": "12345",
    "librarything_id": "67890"
  }
}
```

**Field Validations:**
- `id`: UUID v4 format
- `isbn`: ISBN-10 or ISBN-13 (optional)
- `status`: Must be one of: to-read, reading, completed, abandoned
- `rating`: Integer 1-5 or null
- `pages`: Positive integer
- `date_*`: ISO 8601 format with Z suffix
- `authors`: Non-empty array

### Progress Entry Schema

```json
{
  "book_id": "uuid-v4",
  "sessions": [
    {
      "date": "2025-01-20T20:00:00Z",
      "start_page": 1,
      "end_page": 45,
      "pages_read": 45,
      "duration_minutes": 60,
      "location": "home",
      "notes": "Session notes"
    }
  ],
  "current_page": 45,
  "total_pages": 352,
  "percentage": 12.8,
  "pages_per_day_avg": 15.0,
  "estimated_completion": "2025-02-15T00:00:00Z",
  "reading_streak_days": 5,
  "last_updated": "2025-01-20T21:00:00Z"
}
```

**Calculation Rules:**
- `pages_read`: end_page - start_page + 1
- `percentage`: (current_page / total_pages) * 100
- `pages_per_day_avg`: total_pages_read / days_since_start
- `estimated_completion`: current_date + (pages_remaining / pages_per_day_avg)
- `reading_streak_days`: Count consecutive days with sessions

### Note Entry Schema

```json
{
  "id": "uuid-v4",
  "book_id": "uuid-v4",
  "type": "note|quote|highlight",
  "content": "Note content",
  "context": "Chapter 2: Introduction",
  "page": 30,
  "location": "Section 2.3",
  "chapter": "Chapter 2",
  "tags": ["principle", "important"],
  "importance": "low|medium|high",
  "created": "2025-01-20T20:30:00Z",
  "modified": "2025-01-20T20:30:00Z",
  "linked_notes": ["note-uuid-1", "note-uuid-2"]
}
```

**Note Types:**
- `note`: General observation or thought
- `quote`: Exact quote from text
- `highlight`: Important passage or concept

### Goal Entry Schema

```json
{
  "id": "goal-2025",
  "year": 2025,
  "type": "annual_challenge|custom",
  "target_books": 50,
  "target_pages": null,
  "target_genres": ["fiction", "non-fiction"],
  "constraints": {
    "min_fiction": 10,
    "min_non_fiction": 10,
    "diversify_authors": true,
    "max_rereads": 5
  },
  "progress": {
    "books_completed": 5,
    "pages_read": 1250,
    "on_track": true,
    "pace": "ahead|on_track|behind"
  },
  "milestones": [
    {
      "at_books": 10,
      "name": "First Quarter",
      "achieved": false,
      "achieved_date": null,
      "projected_date": "2025-03-15"
    }
  ],
  "created": "2025-01-01T00:00:00Z",
  "last_updated": "2025-01-20T10:00:00Z"
}
```

## Directory Structure

```
~/.reading-tracker/  (or .reading-tracker/ for project-level)
├── library.json              # Main book database
├── progress.json             # Reading progress tracking
├── goals.json               # Reading goals and challenges
├── recommendations.json     # Cached recommendations
├── config.json             # User preferences and API keys
├── notes/                  # Reading notes by book
│   └── {book-id}/
│       ├── notes.json      # Structured notes data
│       ├── highlights.md   # Exported highlights
│       └── quotes.md       # Exported quotes
└── analytics/              # Generated reports
    ├── monthly/
    │   └── 2025-01.md
    └── yearly/
        └── 2025.md
```

## List Management Workflows

### Add Book Workflow

```python
1. Generate UUID for book_id
2. Validate required fields (title, authors)
3. Set default values:
   - status: 'to-read'
   - date_added: current timestamp
   - owned: true
   - format: 'physical'
4. Optionally fetch metadata from APIs (if ISBN provided)
5. Add to library['books'][book_id]
6. Update library['metadata']['total_books']
7. Update library['metadata']['by_status'][status]
8. Save library.json
9. Return book_id and confirmation
```

### Change Status Workflow

```python
1. Load library
2. Validate book_id exists
3. Validate new status in allowed values
4. Update status counts:
   - Decrement old_status count
   - Increment new_status count
5. Set date fields:
   - to-read → reading: Set date_started
   - * → completed: Set date_completed
   - * → abandoned: Set date_abandoned
6. Update book['status']
7. Save library
8. Optionally trigger:
   - If completed: Prompt for rating
   - If completed: Update goal progress
   - If started: Initialize progress tracking
```

### Search Books Algorithm

```python
def search_books(filters):
    results = []

    for book in library['books'].values():
        # Apply each filter
        if filters.get('status') and book['status'] != filters['status']:
            continue

        if filters.get('query'):
            query_lower = filters['query'].lower()
            # Search in title, authors, description
            if not (
                query_lower in book['title'].lower() or
                any(query_lower in author.lower() for author in book['authors']) or
                (book.get('description') and query_lower in book['description'].lower())
            ):
                continue

        if filters.get('genre'):
            if filters['genre'] not in book.get('genres', []):
                continue

        if filters.get('author'):
            author_lower = filters['author'].lower()
            if not any(author_lower in a.lower() for a in book['authors']):
                continue

        if filters.get('tag'):
            if filters['tag'] not in book.get('tags', []):
                continue

        if filters.get('year'):
            if book.get('published_year') != filters['year']:
                continue

        if filters.get('rating'):
            if book.get('rating') != filters['rating']:
                continue

        results.append(book)

    # Sort by relevance/date
    results.sort(key=lambda b: b['date_added'], reverse=True)

    return results
```

## Progress Calculation Methods

### Reading Pace Algorithm

```python
def calculate_reading_pace(book_progress):
    sessions = book_progress['sessions']

    if not sessions:
        return {
            'pages_per_day': 0,
            'pages_per_hour': 0,
            'sessions_per_week': 0
        }

    # Get date range
    first_session = min(sessions, key=lambda s: s['date'])
    last_session = max(sessions, key=lambda s: s['date'])

    first_date = datetime.fromisoformat(first_session['date'].replace('Z', '+00:00'))
    last_date = datetime.fromisoformat(last_session['date'].replace('Z', '+00:00'))

    days_reading = max(1, (last_date - first_date).days + 1)

    # Total pages
    total_pages = sum(s['pages_read'] for s in sessions)

    # Pages per day
    pages_per_day = total_pages / days_reading

    # Pages per hour (for sessions with duration)
    sessions_with_time = [s for s in sessions if s.get('duration_minutes')]
    if sessions_with_time:
        total_minutes = sum(s['duration_minutes'] for s in sessions_with_time)
        pages_in_timed_sessions = sum(s['pages_read'] for s in sessions_with_time)
        pages_per_hour = (pages_in_timed_sessions / total_minutes) * 60
    else:
        pages_per_hour = 0

    # Sessions per week
    sessions_per_week = (len(sessions) / days_reading) * 7

    return {
        'pages_per_day': round(pages_per_day, 1),
        'pages_per_hour': round(pages_per_hour, 1),
        'sessions_per_week': round(sessions_per_week, 1)
    }
```

### Completion Estimate Algorithm

```python
def estimate_completion(book_progress, current_page, total_pages):
    if current_page >= total_pages:
        return None  # Already completed

    pages_remaining = total_pages - current_page

    # Method 1: Based on average pace
    pace = calculate_reading_pace(book_progress)
    if pace['pages_per_day'] > 0:
        days_remaining = pages_remaining / pace['pages_per_day']
        estimate_1 = datetime.now() + timedelta(days=days_remaining)
    else:
        estimate_1 = None

    # Method 2: Based on last 7 days
    recent_sessions = [
        s for s in book_progress['sessions']
        if (datetime.now() - datetime.fromisoformat(s['date'].replace('Z', '+00:00'))).days <= 7
    ]

    if recent_sessions:
        recent_pages = sum(s['pages_read'] for s in recent_sessions)
        recent_days = 7
        recent_pace = recent_pages / recent_days

        if recent_pace > 0:
            days_remaining_2 = pages_remaining / recent_pace
            estimate_2 = datetime.now() + timedelta(days=days_remaining_2)
        else:
            estimate_2 = None
    else:
        estimate_2 = None

    # Return the more conservative estimate (later date)
    if estimate_1 and estimate_2:
        return max(estimate_1, estimate_2)
    else:
        return estimate_1 or estimate_2
```

### Reading Streak Algorithm

```python
def calculate_reading_streak(sessions):
    if not sessions:
        return 0

    # Get unique dates (ignore time)
    reading_dates = set()
    for session in sessions:
        date = datetime.fromisoformat(session['date'].replace('Z', '+00:00')).date()
        reading_dates.add(date)

    # Sort dates descending
    sorted_dates = sorted(reading_dates, reverse=True)

    # Check if today or yesterday is included
    today = datetime.now().date()
    if sorted_dates[0] not in [today, today - timedelta(days=1)]:
        return 0  # Streak broken

    # Count consecutive days
    streak = 1
    expected_date = sorted_dates[0] - timedelta(days=1)

    for date in sorted_dates[1:]:
        if date == expected_date:
            streak += 1
            expected_date -= timedelta(days=1)
        elif date < expected_date:
            # Gap found, streak ends
            break

    return streak
```

## Note Organization Strategies

### Tagging Strategy

**Best Practices:**
- Use consistent tag naming (lowercase, hyphenated)
- Create tag taxonomy:
  - **Themes**: character-development, world-building, plot-twist
  - **Concepts**: philosophy, economics, psychology
  - **Techniques**: writing-style, narrative-structure
  - **Emotions**: inspiring, thought-provoking, suspenseful
  - **Meta**: to-revisit, to-research, quote-worthy

### Note Linking

```python
def link_notes(note_id_1, note_id_2, relationship='related'):
    """
    Link two notes across books
    Relationships: related, contradicts, expands, example-of
    """

    # Load both notes
    note1 = find_note_by_id(note_id_1)
    note2 = find_note_by_id(note_id_2)

    # Add bidirectional link
    note1['linked_notes'].append({
        'note_id': note_id_2,
        'relationship': relationship,
        'book_title': get_book_title(note2['book_id'])
    })

    note2['linked_notes'].append({
        'note_id': note_id_1,
        'relationship': relationship,
        'book_title': get_book_title(note1['book_id'])
    })

    # Save both
    save_note(note1)
    save_note(note2)
```

### Note Export Formats

**Markdown Export:**
```markdown
# Reading Notes: {Book Title}

**Authors**: {authors}
**Completed**: {date}
**Rating**: {rating}/5

## Chapter 1: Introduction

### 📝 Note (Page 5)

DRY principle is fundamental to good software design.

*Tags: principle, best-practice*

---

### 💬 Quote (Page 12)

> "Don't Repeat Yourself. Every piece of knowledge must have a single, unambiguous, authoritative representation within a system."

*Tags: quote-worthy, principle*

---
```

## Analytics Computation Patterns

### Genre Distribution

```python
def calculate_genre_distribution(books, period=None):
    """Calculate genre statistics"""

    # Filter by period if specified
    if period:
        books = filter_by_period(books, period)

    genre_counter = Counter()
    for book in books:
        for genre in book.get('genres', []):
            genre_counter[genre] += 1

    total_books = len(books)

    return [
        {
            'genre': genre,
            'count': count,
            'percentage': (count / total_books) * 100
        }
        for genre, count in genre_counter.most_common()
    ]
```

### Reading Trends

```python
def calculate_reading_trends(books, granularity='month'):
    """Calculate reading trends over time"""

    # Group by time period
    by_period = defaultdict(lambda: {
        'books': 0,
        'pages': 0,
        'avg_rating': 0,
        'ratings_count': 0
    })

    for book in books:
        if book['status'] != 'completed' or not book.get('date_completed'):
            continue

        date = datetime.fromisoformat(book['date_completed'].replace('Z', '+00:00'))

        if granularity == 'month':
            period_key = date.strftime('%Y-%m')
        elif granularity == 'quarter':
            quarter = (date.month - 1) // 3 + 1
            period_key = f"{date.year}-Q{quarter}"
        else:  # year
            period_key = str(date.year)

        period_data = by_period[period_key]
        period_data['books'] += 1
        period_data['pages'] += book.get('pages', 0)

        if book.get('rating'):
            period_data['avg_rating'] += book['rating']
            period_data['ratings_count'] += 1

    # Calculate averages
    for period, data in by_period.items():
        if data['ratings_count'] > 0:
            data['avg_rating'] = data['avg_rating'] / data['ratings_count']

    return dict(by_period)
```

### Diversity Metrics

```python
def calculate_diversity_metrics(books):
    """Calculate reading diversity"""

    completed = [b for b in books if b['status'] == 'completed']

    # Author diversity
    all_authors = []
    for book in completed:
        all_authors.extend(book.get('authors', []))

    unique_authors = len(set(all_authors))
    total_author_credits = len(all_authors)
    author_diversity = unique_authors / total_author_credits if total_author_credits > 0 else 0

    # Genre diversity (Shannon entropy)
    genre_counts = Counter()
    for book in completed:
        for genre in book.get('genres', []):
            genre_counts[genre] += 1

    total_genres = sum(genre_counts.values())
    genre_entropy = 0
    for count in genre_counts.values():
        p = count / total_genres
        genre_entropy -= p * math.log2(p)

    # Language diversity
    languages = Counter(b.get('language', 'en') for b in completed)

    # Publication year spread
    years = [b.get('published_year') for b in completed if b.get('published_year')]
    year_range = max(years) - min(years) if years else 0

    return {
        'author_diversity_score': round(author_diversity, 2),
        'unique_authors': unique_authors,
        'genre_diversity_entropy': round(genre_entropy, 2),
        'unique_genres': len(genre_counts),
        'languages': dict(languages),
        'year_range': year_range
    }
```

## API Integration Guidelines

### Rate Limiting Pattern

```python
import time
from functools import wraps

def rate_limit(calls_per_minute=30):
    """Decorator for rate limiting API calls"""

    min_interval = 60.0 / calls_per_minute
    last_called = [0.0]

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            left_to_wait = min_interval - elapsed

            if left_to_wait > 0:
                time.sleep(left_to_wait)

            result = func(*args, **kwargs)
            last_called[0] = time.time()

            return result

        return wrapper

    return decorator
```

### Caching Pattern

```python
import hashlib
import json
from pathlib import Path
from datetime import datetime, timedelta

class APICache:
    def __init__(self, cache_dir, ttl_days=30):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.ttl = timedelta(days=ttl_days)

    def _get_cache_key(self, endpoint, params):
        """Generate cache key from endpoint and params"""
        key_str = f"{endpoint}:{json.dumps(params, sort_keys=True)}"
        return hashlib.md5(key_str.encode()).hexdigest()

    def get(self, endpoint, params):
        """Get cached response if valid"""
        cache_key = self._get_cache_key(endpoint, params)
        cache_file = self.cache_dir / f"{cache_key}.json"

        if not cache_file.exists():
            return None

        # Check TTL
        mtime = datetime.fromtimestamp(cache_file.stat().st_mtime)
        if datetime.now() - mtime > self.ttl:
            cache_file.unlink()  # Expired, remove
            return None

        with open(cache_file, 'r') as f:
            return json.load(f)

    def set(self, endpoint, params, data):
        """Cache API response"""
        cache_key = self._get_cache_key(endpoint, params)
        cache_file = self.cache_dir / f"{cache_key}.json"

        with open(cache_file, 'w') as f:
            json.dump(data, f)
```

### Goodreads API Pattern

```python
@rate_limit(calls_per_minute=30)
def fetch_goodreads_book(isbn, api_key):
    """Fetch book data from Goodreads API"""

    import requests

    url = "https://www.goodreads.com/book/isbn_to_id"
    params = {'isbn': isbn, 'key': api_key}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        book_id = response.text.strip()

        # Fetch book details
        url2 = "https://www.goodreads.com/book/show.xml"
        params2 = {'id': book_id, 'key': api_key}

        response2 = requests.get(url2, params=params2, timeout=10)
        response2.raise_for_status()

        # Parse XML response
        # ... (parse and normalize to our schema)

        return normalized_book_data

    except requests.exceptions.RequestException as e:
        print(f"Goodreads API error: {e}")
        return None
```

## Error Handling Patterns

### Validation Errors

```python
class ValidationError(Exception):
    pass

def validate_book(book):
    """Validate book data structure"""

    errors = []

    # Required fields
    if not book.get('title'):
        errors.append("Title is required")

    if not book.get('authors') or len(book['authors']) == 0:
        errors.append("At least one author is required")

    # Field types
    if book.get('pages') and not isinstance(book['pages'], int):
        errors.append("Pages must be an integer")

    if book.get('rating') and (book['rating'] < 1 or book['rating'] > 5):
        errors.append("Rating must be between 1 and 5")

    # Status validation
    valid_statuses = ['to-read', 'reading', 'completed', 'abandoned']
    if book.get('status') and book['status'] not in valid_statuses:
        errors.append(f"Status must be one of: {', '.join(valid_statuses)}")

    if errors:
        raise ValidationError("; ".join(errors))
```

### Recovery Patterns

```python
def safe_save_library(library, library_path):
    """Save library with backup and recovery"""

    library_file = library_path / 'library.json'
    backup_file = library_path / 'library.backup.json'
    temp_file = library_path / 'library.temp.json'

    try:
        # Write to temp file first
        with open(temp_file, 'w') as f:
            json.dump(library, f, indent=2)

        # Validate temp file
        with open(temp_file, 'r') as f:
            json.load(f)  # Ensure it's valid JSON

        # Backup current file
        if library_file.exists():
            library_file.rename(backup_file)

        # Move temp to production
        temp_file.rename(library_file)

        print("✅ Library saved successfully")

    except Exception as e:
        print(f"❌ Error saving library: {e}")

        # Restore from backup if available
        if backup_file.exists():
            backup_file.rename(library_file)
            print("⚠️  Restored from backup")

        raise
```

## Best Practices

1. **Always validate data** before saving
2. **Use transactions** for multi-file updates
3. **Cache API responses** to respect rate limits
4. **Normalize dates** to UTC with Z suffix
5. **Generate UUIDs** for all entities
6. **Maintain referential integrity** between files
7. **Create backups** before destructive operations
8. **Provide clear error messages** with recovery steps
9. **Use consistent formatting** (2-space indent JSON)
10. **Log operations** for debugging and analytics

---

**This skill is read by all book-tracker agents to ensure consistent data handling and behavior.**
