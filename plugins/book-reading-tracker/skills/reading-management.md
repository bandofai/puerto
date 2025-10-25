# Reading Management Skill

Comprehensive patterns for reading list management, progress tracking, and book organization.

## Book Data Structure

```json
{
  "id": "unique-book-id",
  "title": "Book Title",
  "author": "Author Name",
  "isbn": "978-1234567890",
  "isbn13": "978-1234567890",
  "pages": 350,
  "publicationYear": 2023,
  "edition": "First Edition",
  "publisher": "Publisher Name",
  "genre": ["Fiction", "Science Fiction"],
  "language": "English",
  "format": "Hardcover|Paperback|eBook|Audiobook",
  "status": "to-read|reading|completed",
  "dateAdded": "2025-01-15",
  "dateStarted": "2025-02-01",
  "dateCompleted": "2025-02-20",
  "currentPage": 175,
  "rating": 4.5,
  "tags": ["space-opera", "dystopian"],
  "goodreadsId": "12345678",
  "coverUrl": "https://example.com/cover.jpg",
  "notes": "Brief personal note about the book"
}
```

## Reading States

### To-Read
- Books on wishlist
- Track date added
- Priority level (high/medium/low)
- Expected start date (optional)

### Reading
- Currently in progress
- Track start date
- Update current page regularly
- Multiple books can be in this state

### Completed
- Finished books
- Track completion date
- Reading duration calculation
- Rating and review

## Progress Tracking Patterns

### Progress Calculations
```python
# Completion percentage
completion_pct = (current_page / total_pages) * 100

# Pages remaining
pages_remaining = total_pages - current_page

# Reading pace (pages per day)
days_reading = (current_date - start_date).days
pages_per_day = current_page / days_reading

# Estimated completion date
days_to_complete = pages_remaining / pages_per_day
estimated_completion = current_date + timedelta(days=days_to_complete)
```

### Reading Session Tracking
```json
{
  "bookId": "unique-book-id",
  "sessionDate": "2025-02-10T20:00:00Z",
  "startPage": 100,
  "endPage": 125,
  "duration": 45,
  "notes": "Session notes"
}
```

## List Organization

### Filtering
- By status (to-read, reading, completed)
- By genre
- By author
- By publication year
- By rating
- By date added/started/completed
- By format (physical, eBook, audiobook)

### Sorting
- Alphabetically by title/author
- By date added (newest/oldest)
- By rating (highest/lowest)
- By pages (shortest/longest)
- By progress percentage
- By publication year

## Reading Goals

### Annual Reading Challenge
```json
{
  "year": 2025,
  "goalBooks": 50,
  "booksRead": 12,
  "progress": 24,
  "onTrack": true,
  "booksPerMonth": 4.17,
  "projectedTotal": 48
}
```

### Goal Tracking
- Books per year
- Pages per year
- Genres to explore
- Authors to read
- Series to complete

## Recommendation Algorithm

### Preference Analysis
1. **Genre frequency**: Most read genres
2. **Author frequency**: Favorite authors
3. **Rating patterns**: Highly rated characteristics
4. **Length preferences**: Average book length
5. **Publication trends**: Classic vs. contemporary

### Recommendation Scoring
```python
score = (
    genre_match * 0.3 +
    author_similarity * 0.2 +
    rating_correlation * 0.3 +
    length_match * 0.1 +
    recency_factor * 0.1
)
```

## Best Practices

### Data Entry
- Always capture ISBN for accuracy
- Use consistent genre naming
- Record format (physical/digital)
- Add publication year
- Include edition information

### Progress Updates
- Update after each reading session
- Track session duration for analytics
- Note page count accurately
- Record reading environment (optional)

### List Maintenance
- Archive completed books annually
- Review and update to-read list
- Remove books no longer interested in
- Maintain book cover images
- Keep metadata up-to-date

## Integration Patterns

### Goodreads API
- Search books by ISBN/title
- Fetch book metadata
- Get user reviews and ratings
- Import reading lists
- Export to Goodreads

### LibraryThing API
- Alternative book data source
- Library catalog integration
- Social reading features

### Export Formats
- CSV for spreadsheet analysis
- JSON for data portability
- Markdown for documentation
- PDF for printable lists
- HTML for web display

## Common Queries

### Statistics Queries
- Total books read this year
- Average books per month
- Most read genre
- Favorite authors
- Longest book read
- Average book rating
- Reading streak (consecutive days)

### List Queries
- Currently reading books
- Unfinished books (started but not completed)
- Highly rated books (4+ stars)
- Books added but not started
- Recently completed
- Overdue books (started > 60 days ago)
