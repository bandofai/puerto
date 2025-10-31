# Book Reading Tracker Plugin

A comprehensive reading management system for Claude Code that helps you track books, monitor progress, capture insights, and analyze your reading habits.

## Overview

The Book Reading Tracker plugin provides intelligent agents, skills, and tools for managing your reading journey. From discovering new books to analyzing reading patterns, this plugin transforms how you engage with literature.

## What's Included

### Agents

#### 1. reading-list-manager
Manages your reading lists across different states (to-read, reading, completed, abandoned).

**Key Features:**
- Add/remove books with rich metadata
- Move books between reading states
- Search and filter by genre, author, year
- Bulk operations for list management
- Import from Goodreads/LibraryThing
- Export to various formats

**Activation**: Automatically activates for reading list operations, or use `@reading-list-manager`.

#### 2. progress-tracker
Tracks reading progress with detailed metrics and visualizations.

**Key Features:**
- Page/percentage progress tracking
- Reading session logging
- Estimated completion dates
- Reading pace analysis
- Daily/weekly progress reports
- Reading streaks tracking

**Activation**: Automatically activates for progress updates, or use `@progress-tracker`.

#### 3. notes-organizer
Organizes reading notes, quotes, and highlights with intelligent retrieval.

**Key Features:**
- Chapter-by-chapter notes
- Quote extraction with context
- Highlight compilation by theme
- Tag-based organization
- Search across all notes
- Export to Markdown/PDF

**Activation**: Automatically activates for note-taking operations, or use `@notes-organizer`.

#### 4. reading-analyst
Analyzes reading patterns and generates insights.

**Key Features:**
- Books per month/year statistics
- Genre distribution analysis
- Author diversity metrics
- Reading pace trends
- Completion rate tracking
- Time investment analysis

**Activation**: Use `@reading-analyst` for analytics and reports.

#### 5. recommendation-engine
Suggests books based on reading history and preferences.

**Key Features:**
- Personalized recommendations
- Similar book discovery
- Author expansion suggestions
- Genre exploration paths
- Community recommendations (via APIs)
- Reading challenge ideas

**Activation**: Use `@recommendation-engine` for book suggestions.

#### 6. goal-tracker
Monitors reading goals and annual challenges.

**Key Features:**
- Annual reading challenges
- Custom goal setting (pages, books, genres)
- Progress visualization
- Goal adjustment strategies
- Achievement milestones
- Motivation insights

**Activation**: Use `@goal-tracker` for goal management.

### Skills

#### 1. reading-management
Comprehensive patterns for book tracking, including:
- Data structure standards for books/progress
- List management workflows
- Progress calculation methods
- Note organization strategies
- Analytics computation patterns
- API integration guidelines

Main Claude and all agents read this skill for consistent data handling.

#### 2. book-api-integration
Patterns for integrating with external book services:
- Goodreads API authentication and queries
- LibraryThing API usage
- Open Library API for metadata
- ISBN lookups and resolution
- Rate limiting and caching strategies
- Error handling for API failures

### Python Tools

#### 1. book_api_client.py
Unified client for book APIs with caching and rate limiting.

**Features:**
- Goodreads API integration
- LibraryThing integration
- Open Library fallback
- Local caching layer
- Automatic retry logic
- Response normalization

#### 2. analytics_engine.py
Statistical analysis and visualization for reading data.

**Features:**
- Time-series analysis
- Distribution calculations
- Trend detection
- Reading pace algorithms
- Goal projection models
- Export to charts/graphs

#### 3. recommendation_system.py
Machine learning-based recommendation engine.

**Features:**
- Collaborative filtering
- Content-based recommendations
- Hybrid recommendation strategies
- Diversity optimization
- Explanation generation

## Installation

```bash
/plugin install book-tracker@puerto
```

**Prerequisites:**
- Python 3.9+
- pip or uv package manager
- Optional: Goodreads API key
- Optional: LibraryThing API key

After installation, restart Claude Code to activate all agents and skills.

## Quick Start

### Initial Setup

```bash
# Initialize reading library
@reading-list-manager "Initialize new reading library"

# Set reading goals
@goal-tracker "Set annual goal of 50 books"

# Import from Goodreads (optional)
@reading-list-manager "Import from Goodreads CSV export"
```

### Daily Usage

**Add a book:**
```
@reading-list-manager Add "The Pragmatic Programmer" by Andy Hunt to reading list
```

**Update progress:**
```
@progress-tracker I read pages 45-82 of "The Pragmatic Programmer"
```

**Add notes:**
```
@notes-organizer Add note to "The Pragmatic Programmer" chapter 2: "DRY principle is fundamental"
```

**Check progress:**
```
@goal-tracker Show my reading goal progress
```

**Get recommendations:**
```
@recommendation-engine Suggest books similar to "The Pragmatic Programmer"
```

### Weekly Reviews

```
@reading-analyst Generate weekly reading report
@progress-tracker Show reading pace trends
@goal-tracker Am I on track for my annual goal?
```

### Monthly Analytics

```
@reading-analyst Complete monthly reading analysis
@reading-analyst Genre distribution for this month
@recommendation-engine Based on this month, what should I read next?
```

## Data Structure

All reading data is stored in `~/.reading-tracker/` or `.reading-tracker/` (project-specific).

### Directory Layout

```
.reading-tracker/
├── library.json              # Main book database
├── progress.json             # Reading progress tracking
├── notes/                    # Reading notes organized by book
│   ├── {book-id}/
│   │   ├── highlights.md
│   │   ├── notes.md
│   │   └── quotes.md
├── analytics/                # Generated reports and statistics
│   ├── monthly/
│   └── yearly/
├── goals.json               # Reading goals and challenges
├── recommendations.json     # Cached recommendations
└── config.json             # User preferences and API keys
```

### Core Data Models

#### Book Entry

```json
{
  "id": "book-uuid-12345",
  "isbn": "978-0135957059",
  "title": "The Pragmatic Programmer",
  "subtitle": "Your Journey to Mastery",
  "authors": ["Andy Hunt", "Dave Thomas"],
  "publisher": "Addison-Wesley",
  "published_year": 2019,
  "edition": "20th Anniversary Edition",
  "pages": 352,
  "language": "en",
  "genres": ["Programming", "Software Engineering", "Computer Science"],
  "tags": ["technical", "reference", "career"],
  "cover_url": "https://...",
  "description": "...",
  "status": "reading",
  "date_added": "2025-01-15T10:00:00Z",
  "date_started": "2025-01-20T08:00:00Z",
  "date_completed": null,
  "rating": null,
  "format": "physical",
  "owned": true,
  "source": "purchased",
  "metadata": {
    "goodreads_id": "12345",
    "library_thing_id": "67890"
  }
}
```

#### Progress Entry

```json
{
  "book_id": "book-uuid-12345",
  "sessions": [
    {
      "date": "2025-01-20T20:00:00Z",
      "start_page": 1,
      "end_page": 45,
      "duration_minutes": 60,
      "location": "home",
      "notes": "Great intro chapter"
    }
  ],
  "current_page": 45,
  "total_pages": 352,
  "percentage": 12.8,
  "pages_per_day_avg": 15.0,
  "estimated_completion": "2025-02-15",
  "reading_streak_days": 5,
  "last_updated": "2025-01-20T21:00:00Z"
}
```

#### Note Entry

```json
{
  "id": "note-uuid-67890",
  "book_id": "book-uuid-12345",
  "type": "note|quote|highlight",
  "content": "DRY principle: Don't Repeat Yourself",
  "context": "Chapter 2: A Pragmatic Approach",
  "page": 30,
  "location": "section 2.3",
  "tags": ["principle", "best-practice"],
  "created": "2025-01-20T20:30:00Z",
  "modified": "2025-01-20T20:30:00Z",
  "linked_notes": [],
  "importance": "high"
}
```

#### Goal Entry

```json
{
  "id": "goal-2025",
  "year": 2025,
  "type": "annual_challenge",
  "target_books": 50,
  "target_pages": null,
  "target_genres": ["fiction", "non-fiction"],
  "constraints": {
    "min_fiction": 10,
    "min_non_fiction": 10,
    "diversify_authors": true
  },
  "progress": {
    "books_completed": 5,
    "pages_read": 1250,
    "on_track": true,
    "pace": "ahead"
  },
  "milestones": [
    {
      "at_books": 10,
      "name": "First Quarter",
      "achieved": false,
      "projected_date": "2025-03-15"
    }
  ]
}
```

## Workflows

### Complete Book Lifecycle

```bash
# 1. Discover and add book
@recommendation-engine "Suggest books about software architecture"
@reading-list-manager "Add 'Clean Architecture' to to-read list"

# 2. Start reading
@reading-list-manager "Move 'Clean Architecture' to currently reading"
@progress-tracker "Started 'Clean Architecture' today"

# 3. Track progress
@progress-tracker "Read pages 1-50 of 'Clean Architecture', took 1.5 hours"
@notes-organizer "Add highlight from page 23: 'Architecture is about intent'"

# 4. Continue reading
@progress-tracker "Read pages 51-100 yesterday"
@notes-organizer "Chapter 3 notes: SOLID principles review"

# 5. Complete book
@progress-tracker "Finished 'Clean Architecture' today!"
@reading-list-manager "Mark 'Clean Architecture' as completed, rating 5/5"
@notes-organizer "Export all notes for 'Clean Architecture' to markdown"

# 6. Review and discover next
@reading-analyst "How did 'Clean Architecture' affect my reading stats?"
@recommendation-engine "What should I read next after 'Clean Architecture'?"
```

### Monthly Review Workflow

```bash
# Generate comprehensive monthly report
@reading-analyst "Generate January 2025 reading report"
# Output includes:
# - Books completed
# - Pages read
# - Reading time invested
# - Genre distribution
# - Top authors
# - Reading pace trends
# - Notable quotes/insights

# Check goal progress
@goal-tracker "How am I tracking against my annual goal?"

# Plan next month
@recommendation-engine "Based on January reading, suggest February focus areas"
```

### Research Reading Workflow

For academic or research reading with heavy note-taking:

```bash
# 1. Create research project
@notes-organizer "Create research collection: 'Software Architecture Patterns'"

# 2. Add books to collection
@reading-list-manager "Add multiple books to 'Software Architecture Patterns' collection"

# 3. Read with detailed notes
@notes-organizer "Add note to 'Clean Architecture' page 45: Connection to DDD concepts"
@notes-organizer "Link note from 'Clean Architecture' p45 to 'DDD' p120"

# 4. Extract insights
@notes-organizer "Search all notes in 'Software Architecture Patterns' for 'microservices'"
@notes-organizer "Generate summary of key themes across all books in collection"

# 5. Export research
@notes-organizer "Export 'Software Architecture Patterns' collection to research paper format"
```

## API Integration

### Goodreads Setup

1. Get API key from [Goodreads Developers](https://www.goodreads.com/api)
2. Configure:

```bash
@reading-list-manager "Configure Goodreads API key: YOUR_KEY_HERE"
```

Or set environment variable:
```bash
export GOODREADS_API_KEY=your_key_here
```

**Available Operations:**
- Import reading lists
- Sync reading progress
- Fetch book metadata
- Get community recommendations
- Import reviews and ratings

### LibraryThing Setup

1. Get API key from [LibraryThing APIs](https://www.librarything.com/services/)
2. Configure:

```bash
@reading-list-manager "Configure LibraryThing API key: YOUR_KEY_HERE"
```

**Available Operations:**
- Import library
- Fetch enhanced metadata
- Get series information
- Community recommendations
- Tag cloud data

### Open Library (No API Key Required)

Automatic fallback for:
- ISBN lookups
- Cover images
- Basic metadata
- Author information
- Edition data

## Analytics Features

### Reading Statistics

**Time-based:**
- Books per month/quarter/year
- Pages per day/week/month
- Reading time investment
- Completion rates
- Streak tracking

**Content-based:**
- Genre distribution (pie chart)
- Author diversity score
- Language breakdown
- Publication year trends
- Fiction vs non-fiction ratio

**Behavior-based:**
- Reading pace trends
- Preferred reading times
- Average book length
- Re-reading frequency
- Abandonment rate

### Visualizations

Generated as markdown tables and charts:

```
@reading-analyst "Visualize my 2024 reading journey"
```

Output includes:
- Monthly books completed bar chart
- Genre distribution pie chart
- Reading pace line graph
- Goal progress timeline
- Author frequency cloud

### Predictive Analytics

```
@reading-analyst "Project if I'll hit my annual goal"
@progress-tracker "When will I finish my current book?"
@goal-tracker "Suggest pace adjustments to meet goal"
```

## Recommendation System

### Recommendation Types

**Similar Books:**
Based on genre, author, themes, and ratings.

```
@recommendation-engine "Books similar to 'Sapiens'"
```

**Author Expansion:**
Discover more from favorite authors.

```
@recommendation-engine "More books by Yuval Noah Harari"
```

**Genre Exploration:**
Branch into new genres based on preferences.

```
@recommendation-engine "Non-fiction like my current reads but in new genres"
```

**Community Picks:**
Leverages Goodreads/LibraryThing data.

```
@recommendation-engine "Trending books in software engineering"
```

**Diversity Goals:**
Helps diversify reading across authors, perspectives, genres.

```
@recommendation-engine "Suggest books to diversify my reading this quarter"
```

### Recommendation Quality

The system considers:
- Reading history and ratings
- Genre preferences and exploration appetite
- Author diversity
- Reading pace and book length
- Current reading goals
- Community ratings and trends
- Personal note patterns (what themes you highlight)

## Commands Summary

### Reading List Management
```bash
@reading-list-manager "Add [book] to [list]"
@reading-list-manager "Move [book] to [status]"
@reading-list-manager "Search books by [genre/author/tag]"
@reading-list-manager "Import from Goodreads CSV"
@reading-list-manager "Export reading list to JSON/CSV"
```

### Progress Tracking
```bash
@progress-tracker "Read pages X-Y of [book]"
@progress-tracker "Started/finished [book] today"
@progress-tracker "Show current reading progress"
@progress-tracker "Reading pace for [book]"
@progress-tracker "When will I finish [book]?"
```

### Notes & Highlights
```bash
@notes-organizer "Add note to [book] page X: [content]"
@notes-organizer "Add quote from [book]: [quote]"
@notes-organizer "Search notes for [keyword]"
@notes-organizer "Export notes for [book]"
@notes-organizer "Link notes across books"
```

### Analytics
```bash
@reading-analyst "Generate [period] reading report"
@reading-analyst "Show genre distribution"
@reading-analyst "Reading trends for [year]"
@reading-analyst "Top authors/genres"
@reading-analyst "Reading pace analysis"
```

### Recommendations
```bash
@recommendation-engine "Suggest books like [book]"
@recommendation-engine "What should I read next?"
@recommendation-engine "Recommendations based on [genre/author]"
@recommendation-engine "Trending books in [category]"
@recommendation-engine "Help me diversify my reading"
```

### Goal Tracking
```bash
@goal-tracker "Set goal of [N] books for [year]"
@goal-tracker "Show goal progress"
@goal-tracker "Am I on track?"
@goal-tracker "Adjust goal to [new target]"
@goal-tracker "Reading challenge milestones"
```

## Configuration

### Global Settings

Configure in `~/.reading-tracker/config.json`:

```json
{
  "default_reading_goal": 50,
  "preferred_format": "physical",
  "timezone": "America/Los_Angeles",
  "analytics": {
    "include_abandoned": false,
    "group_series_as_one": true,
    "count_rereads": true
  },
  "apis": {
    "goodreads_key": "YOUR_KEY",
    "librarything_key": "YOUR_KEY",
    "rate_limit_per_minute": 30
  },
  "preferences": {
    "auto_fetch_metadata": true,
    "auto_fetch_covers": true,
    "prompt_for_notes_on_completion": true,
    "streak_reminder": true
  }
}
```

### Project-Specific Reading

For book clubs or shared reading lists:

Create `.reading-tracker/config.json` in project root:

```json
{
  "mode": "shared",
  "club_name": "Tech Book Club",
  "members": ["alice", "bob", "charlie"],
  "shared_notes": true,
  "sync_progress": false
}
```

## Advanced Features

### Collections & Series

```bash
@reading-list-manager "Create collection 'Software Architecture Books'"
@reading-list-manager "Add books to collection"
@reading-list-manager "Track series reading order"
```

### Reading Challenges

```bash
@goal-tracker "Create challenge: Read 12 classics in 12 months"
@goal-tracker "Create challenge: 5 books from each continent"
@goal-tracker "Create challenge: Read in 3 different languages"
```

### Book Clubs

```bash
@reading-list-manager "Create book club schedule for 2025"
@notes-organizer "Enable shared notes for book club members"
@progress-tracker "Compare reading pace with club members"
```

### Import/Export

**Supported Formats:**
- Goodreads CSV export
- LibraryThing JSON
- Calibre database
- ISBN lists (plain text)
- Custom JSON schema

**Export Options:**
- CSV for spreadsheets
- JSON for backup
- Markdown for reading logs
- PDF for reading reports

## Troubleshooting

### API Rate Limits

**Issue**: "Rate limit exceeded" when fetching book data

**Solution**:
- Wait a few minutes
- Enable caching in config
- Add API keys for higher limits

### Missing Metadata

**Issue**: Book metadata incomplete or missing

**Solution**:
```bash
@reading-list-manager "Manually update metadata for [book]"
# Or try different APIs
@reading-list-manager "Fetch metadata from LibraryThing for [book]"
```

### Progress Not Saving

**Issue**: Reading progress not persisting

**Solution**:
- Check `~/.reading-tracker/` permissions
- Verify progress.json is not corrupted
- Use `@progress-tracker "Rebuild progress database"`

### Analytics Not Generating

**Issue**: Analytics reports show errors

**Solution**:
- Ensure Python dependencies installed
- Check `analytics_engine.py` logs
- Verify data format in library.json

## Performance Notes

- **Local-first**: All data stored locally, APIs only for enrichment
- **Caching**: API responses cached for 30 days
- **Lazy loading**: Large libraries loaded on-demand
- **Offline support**: Full functionality without internet (except API features)

## Privacy & Data

- **No telemetry**: Your reading data stays local
- **API keys**: Stored encrypted in config
- **Backups**: Recommended to backup `~/.reading-tracker/` regularly
- **Sharing**: Optional sync features, disabled by default

## Future Enhancements

Planned features:
- Mobile app sync (via self-hosted server)
- Audiobook tracking integration
- Reading time estimation improvements
- Social features (optional sharing)
- Advanced ML recommendations
- Multi-language support
- OCR for physical book quotes

## Contributing

This plugin is part of the Puerto marketplace. See main repository for contribution guidelines.

## Links

- [Goodreads API Documentation](https://www.goodreads.com/api)
- [LibraryThing APIs](https://www.librarything.com/services/)
- [Open Library API](https://openlibrary.org/developers/api)

## License

MIT License - See main repository for details

---

**Transform your reading journey into data-driven insights. Every book, every page, every insight tracked and analyzed.**
