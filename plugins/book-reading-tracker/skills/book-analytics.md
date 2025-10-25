# Book Analytics Skill

Comprehensive patterns for reading analytics, insights generation, and visualization.

## Key Metrics

### Reading Volume
- **Books per month**: Total completed / months
- **Books per year**: Annual reading count
- **Pages per month**: Total pages / months
- **Pages per year**: Annual page count
- **Reading streak**: Consecutive days with reading activity

### Reading Pace
- **Average reading speed**: Pages per day/hour
- **Average book duration**: Days from start to completion
- **Books in progress**: Current concurrent reads
- **Completion rate**: Completed / (Completed + Abandoned)

### Content Metrics
- **Average book length**: Mean pages per book
- **Genre distribution**: Percentage by genre
- **Format distribution**: Physical/eBook/Audiobook %
- **Language distribution**: Books by language
- **Publication era**: Vintage vs. contemporary ratio

## Analytics Queries

### Time-Based Analysis
```python
# Books per month in current year
def books_per_month(year):
    books = get_completed_books(year)
    monthly_counts = defaultdict(int)
    for book in books:
        month = book['dateCompleted'].month
        monthly_counts[month] += 1
    return monthly_counts

# Year-over-year comparison
def yoy_comparison(year1, year2):
    count1 = len(get_completed_books(year1))
    count2 = len(get_completed_books(year2))
    change = ((count2 - count1) / count1) * 100
    return {"year1": count1, "year2": count2, "change_pct": change}
```

### Genre Analysis
```python
# Genre distribution
def genre_distribution(books):
    genre_counts = defaultdict(int)
    for book in books:
        for genre in book.get('genre', []):
            genre_counts[genre] += 1
    total = len(books)
    return {genre: (count/total)*100
            for genre, count in genre_counts.items()}

# Genre diversity score (Shannon entropy)
def genre_diversity(books):
    dist = genre_distribution(books)
    return -sum(p * log(p) for p in dist.values() if p > 0)
```

### Author Analysis
```python
# Author frequency
def top_authors(books, limit=10):
    author_counts = defaultdict(int)
    for book in books:
        author_counts[book['author']] += 1
    return sorted(author_counts.items(),
                  key=lambda x: x[1],
                  reverse=True)[:limit]

# Author diversity
def unique_authors(books):
    return len(set(book['author'] for book in books))
```

### Reading Pace Analysis
```python
# Average reading speed
def avg_reading_speed(books):
    speeds = []
    for book in books:
        if 'dateStarted' in book and 'dateCompleted' in book:
            days = (book['dateCompleted'] - book['dateStarted']).days
            if days > 0:
                pages_per_day = book['pages'] / days
                speeds.append(pages_per_day)
    return sum(speeds) / len(speeds) if speeds else 0

# Reading pace trend
def reading_pace_trend(books):
    # Group by month and calculate average pace
    monthly_pace = defaultdict(list)
    for book in books:
        if 'dateStarted' in book and 'dateCompleted' in book:
            month = book['dateCompleted'].strftime('%Y-%m')
            days = (book['dateCompleted'] - book['dateStarted']).days
            if days > 0:
                pace = book['pages'] / days
                monthly_pace[month].append(pace)
    return {month: sum(paces)/len(paces)
            for month, paces in monthly_pace.items()}
```

## Reading Goal Tracking

### Goal Types
1. **Quantity goals**: Number of books per year
2. **Page goals**: Total pages per year
3. **Genre goals**: Read X books in Y genres
4. **Author goals**: Read X new authors
5. **Challenge goals**: Reading challenges (e.g., around the world)

### Goal Progress Calculation
```python
def goal_progress(goal_books, completed_books, current_date, year):
    # Current progress
    progress_pct = (completed_books / goal_books) * 100

    # Expected progress based on date
    days_elapsed = (current_date - datetime(year, 1, 1)).days
    days_in_year = 365 + (1 if is_leap_year(year) else 0)
    expected_pct = (days_elapsed / days_in_year) * 100
    expected_books = (goal_books * expected_pct) / 100

    # On track status
    on_track = completed_books >= expected_books

    # Projection
    books_per_day = completed_books / days_elapsed
    projected_total = books_per_day * days_in_year

    return {
        "progress": progress_pct,
        "onTrack": on_track,
        "expected": expected_books,
        "projection": projected_total,
        "booksAhead": completed_books - expected_books
    }
```

## Visualization Patterns

### Books per Month Chart
```
Jan |██████ 6
Feb |████ 4
Mar |█████████ 9
Apr |███████ 7
May |█████ 5
Jun |██████ 6
```

### Genre Distribution Pie Chart
```
Fiction (40%)     ████████
Non-Fiction (30%) ██████
Science (20%)     ████
History (10%)     ██
```

### Reading Pace Trend Line
```
Pages/Day
50 |     *
40 |   *   *
30 | *       *
20 |           *
10 |_____________
   J F M A M J
```

### Goal Progress Bar
```
Annual Goal: 50 books
Current: 32 books (64%)
[████████████████████░░░░░░░░░░]
On track: ✓ (+2 books ahead)
```

## Report Templates

### Monthly Reading Summary
```markdown
# Reading Summary - February 2025

## Books Completed: 4
- Book Title 1 by Author A (Rating: 4.5/5)
- Book Title 2 by Author B (Rating: 4/5)
- Book Title 3 by Author C (Rating: 5/5)
- Book Title 4 by Author D (Rating: 3.5/5)

## Statistics
- Total pages: 1,280
- Average rating: 4.25/5
- Average pages per book: 320
- Reading pace: 46 pages/day

## Top Genres
1. Fiction (50%)
2. Science Fiction (25%)
3. History (25%)

## Goal Progress
- Annual goal: 50 books
- Progress: 12/50 (24%)
- Status: On track (+1 book ahead)
```

### Annual Reading Review
```markdown
# 2025 Reading Review

## Overview
- Books completed: 52
- Pages read: 18,200
- Average rating: 4.2/5
- Favorite genre: Science Fiction

## Monthly Breakdown
- Peak month: March (9 books)
- Slowest month: December (2 books)
- Average: 4.3 books/month

## Top 10 Books of the Year
1. Book Title (5/5)
2. Book Title (5/5)
...

## Author Statistics
- Unique authors: 45
- Most read author: Author Name (4 books)
- New discoveries: 38 authors

## Genre Distribution
- Fiction: 40%
- Non-fiction: 30%
- Science: 20%
- History: 10%

## Reading Pace
- Average: 35 pages/day
- Fastest book: Title (5 days)
- Longest duration: Title (45 days)

## Goals Achieved
✓ Read 50 books (achieved: 52)
✓ Explore 5 new genres
✓ Read 10 classics
```

## Insights Generation

### Pattern Recognition
- **Reading slumps**: Months with below-average completion
- **Peak periods**: Months with above-average completion
- **Genre shifts**: Changes in genre preferences over time
- **Length preferences**: Trending toward longer/shorter books

### Recommendations
- "Based on your reading pace, you're on track to complete X books this year"
- "You haven't read [genre] in 3 months - time to diversify?"
- "Your reading pace increased 20% this quarter"
- "You're behind goal by X books - need to average Y books/month"

### Comparative Analysis
- Compare current year to previous years
- Compare to reading goals
- Compare to community averages (if available)
- Compare reading patterns across seasons

## Advanced Analytics

### Reading Velocity Trends
```python
def velocity_analysis(books):
    # Calculate 30-day rolling average
    sessions = get_reading_sessions(books)
    daily_pages = defaultdict(int)
    for session in sessions:
        date = session['date']
        daily_pages[date] += session['pages']

    # 30-day moving average
    dates = sorted(daily_pages.keys())
    moving_avg = []
    for i in range(len(dates)):
        window = dates[max(0, i-29):i+1]
        avg = sum(daily_pages[d] for d in window) / len(window)
        moving_avg.append((dates[i], avg))

    return moving_avg
```

### Correlation Analysis
- Book length vs. rating
- Genre vs. completion time
- Publication year vs. rating
- Reading speed vs. enjoyment

### Predictive Analytics
- Projected annual total based on current pace
- Estimated time to complete current books
- Genre preference evolution
- Reading pattern seasonality

## Data Quality Metrics

### Completeness Score
- Percentage of books with complete metadata
- Percentage with ratings
- Percentage with notes
- Percentage with dates

### Update Frequency
- Days since last book completed
- Days since last progress update
- Average update interval
