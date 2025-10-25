# Book Reading Tracker Plugin

Reading progress and book note management specialist for Puerto.

## Overview

The Book Reading Tracker plugin provides comprehensive tools for managing your reading life: tracking books across to-read/reading/completed states, monitoring progress, organizing notes and highlights, analyzing reading patterns, and getting personalized recommendations.

## Features

- **Reading List Management**: Organize books by status (to-read, reading, completed)
- **Progress Tracking**: Track pages read, completion percentage, and reading pace
- **Note Organization**: Capture and organize highlights, quotes, and personal notes
- **Reading Analytics**: Analyze reading patterns, genre distribution, and goal progress
- **Smart Recommendations**: Get personalized book suggestions based on your history
- **Goal Tracking**: Set and monitor annual reading challenges
- **Integration Ready**: Supports Goodreads and LibraryThing APIs

## Agents

### 1. reading-list-manager (Haiku)
Fast CRUD operations for reading list management.

**Capabilities:**
- Add/update/remove books
- Move books between states
- Search and filter lists
- Export reading lists
- Bulk operations

**Usage:**
```
@reading-list-manager Add "Project Hail Mary" by Andy Weir to my to-read list
@reading-list-manager Show all science fiction books in my completed list
@reading-list-manager Move "The Martian" to reading status
```

### 2. progress-tracker (Haiku)
Fast progress updates and completion calculations.

**Capabilities:**
- Update current page
- Calculate completion percentage
- Track reading sessions
- Monitor reading pace
- Generate progress reports

**Usage:**
```
@progress-tracker I'm on page 145 of "Project Hail Mary"
@progress-tracker How far along am I in my current books?
@progress-tracker Show my reading pace this week
```

### 3. note-organizer (Sonnet)
Intelligent note and highlight organization.

**Capabilities:**
- Organize notes by book/chapter/theme
- Compile highlights and quotes
- Tag and categorize notes
- Search across all notes
- Export notes in multiple formats

**Usage:**
```
@note-organizer Add this highlight from page 67: "Science is the process of proving yourself wrong as quickly as possible"
@note-organizer Show all my notes about leadership themes
@note-organizer Export my notes from "Atomic Habits" as Markdown
```

### 4. analytics-reporter (Sonnet)
Reading analytics and insights generation.

**Capabilities:**
- Books per month statistics
- Genre distribution analysis
- Reading pace trends
- Goal progress tracking
- Annual reading reviews

**Usage:**
```
@analytics-reporter Generate my monthly reading summary
@analytics-reporter How am I tracking against my annual goal?
@analytics-reporter Show me my genre distribution this year
```

### 5. recommendation-engine (Sonnet)
Personalized book recommendations based on history.

**Capabilities:**
- Analyze reading preferences
- Suggest similar books
- Discover new authors
- Genre exploration
- Track recommendation acceptance

**Usage:**
```
@recommendation-engine Suggest 5 books based on my recent reads
@recommendation-engine I loved "The Martian" - what should I read next?
@recommendation-engine Recommend something outside my usual genres
```

## Skills

### reading-management
Comprehensive reading list patterns, progress tracking, and book data structures.

### note-taking
Note organization patterns, highlight compilation, and annotation best practices.

### book-analytics
Reading analytics patterns, visualization techniques, and insight generation.

## Templates

### reading-list.json
Master reading list structure with books across all states, metadata, and reading goals.

### book-notes.json
Note and highlight storage with tagging, themes, and organization patterns.

### reading-sessions.json
Reading session tracking with duration, pages read, and statistics.

## Getting Started

### 1. Initialize Your Reading List
```
@reading-list-manager Create a new reading list for 2025
```

### 2. Add Books
```
@reading-list-manager Add these books to my to-read list:
- "Dune" by Frank Herbert
- "Foundation" by Isaac Asimov
- "Neuromancer" by William Gibson
```

### 3. Start Reading
```
@reading-list-manager Move "Dune" to reading status
@progress-tracker Started "Dune" today
```

### 4. Track Progress
```
@progress-tracker I'm on page 120 of "Dune"
@note-organizer Add note: "The ecology of Arrakis is fascinating"
```

### 5. Analyze Reading
```
@analytics-reporter Show my reading statistics this month
@recommendation-engine What should I read next?
```

## Reading Goal Example

Set an annual reading challenge:
```json
{
  "year": 2025,
  "goalBooks": 50,
  "goalPages": 15000,
  "genres": ["Read 5 classics", "Explore 3 new genres"]
}
```

Track progress throughout the year:
```
@analytics-reporter How am I tracking against my 2025 goal?
```

## Integration

### Goodreads API
- Search books by ISBN/title
- Import reading lists
- Sync progress
- Fetch book metadata

### LibraryThing API
- Alternative book data source
- Library catalog integration
- Social features

## Data Storage

All data is stored in JSON format:
- `data/reading-list.json`: Master reading list
- `data/notes/`: Book notes by book ID
- `data/sessions/`: Reading session logs
- `data/analytics/`: Generated reports

## Best Practices

1. **Update regularly**: Log progress after each reading session
2. **Capture notes immediately**: Note insights as they occur
3. **Use consistent tags**: Maintain a standard tag taxonomy
4. **Set realistic goals**: Base goals on past reading patterns
5. **Review periodically**: Monthly summaries help maintain momentum

## Tips

- Use ISBN for accurate book identification
- Record reading sessions with timestamps
- Tag notes with themes for easy retrieval
- Export notes periodically as backup
- Track reading environment for analytics

## Cost Optimization

- **Haiku agents** (reading-list-manager, progress-tracker): Fast, low-cost operations
- **Sonnet agents** (note-organizer, analytics-reporter, recommendation-engine): Higher-quality analysis and insights

Use Haiku agents for frequent updates, Sonnet for in-depth analysis.

## License

MIT
