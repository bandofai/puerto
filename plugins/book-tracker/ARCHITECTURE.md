# Book Reading Tracker - Plugin Architecture

## Overview

The Book Reading Tracker plugin is a comprehensive reading management system built on Puerto's plugin architecture. It provides six specialized agents, two skills, and Python tools for complete book tracking, progress monitoring, and reading analytics.

## Architecture Pattern

**Pattern**: Multi-Agent Specialist System with Shared Skills

```
User Request
    ↓
Automatic Agent Selection (based on description triggers)
    ↓
Agent reads reading-management skill (MANDATORY)
    ↓
Agent executes using Python tools
    ↓
Updates shared data store (~/.reading-tracker/)
    ↓
Returns formatted results
```

## Component Breakdown

### 1. Agents (6 total)

#### reading-list-manager (Sonnet)
**Responsibility**: Library management
**Tools**: Read, Write, Python
**Triggers**: "add book", "import", "search books", "export"
**Key Operations**:
- Initialize library structure
- Add/remove/update books
- Import from Goodreads/LibraryThing CSV
- Search and filter books
- Export to JSON/CSV/Markdown
- Enrich metadata from APIs

**Model Choice**: Sonnet - Needs judgment for metadata normalization and smart searching

#### progress-tracker (Haiku)
**Responsibility**: Reading progress
**Tools**: Read, Write, Python
**Triggers**: "read pages", "progress", "started reading", "finished book"
**Key Operations**:
- Log reading sessions
- Calculate reading pace
- Estimate completion dates
- Track reading streaks
- Multi-book concurrent tracking
- Progress visualization

**Model Choice**: Haiku - Deterministic calculations, fast response for frequent updates

#### notes-organizer (Sonnet)
**Responsibility**: Notes and highlights
**Tools**: Read, Write, Python
**Triggers**: "add note", "quote", "highlight", "search notes"
**Key Operations**:
- Create notes/quotes/highlights
- Tag-based organization
- Cross-book note linking
- Search all notes
- Export to Markdown/PDF
- Theme-based compilation

**Model Choice**: Sonnet - Needs understanding of context and relationships between notes

#### reading-analyst (Sonnet)
**Responsibility**: Analytics and insights
**Tools**: Read, Write, Python
**Triggers**: "reading report", "statistics", "analyze", "trends"
**Key Operations**:
- Generate period reports (monthly/yearly)
- Genre distribution analysis
- Author diversity metrics
- Reading pace trends
- Top books/authors
- Visualization (text-based charts)

**Model Choice**: Sonnet - Requires analytical reasoning and pattern recognition

#### recommendation-engine (Sonnet)
**Responsibility**: Book recommendations
**Tools**: Read, Write, Python
**Triggers**: "recommend", "suggest books", "what to read"
**Key Operations**:
- Similar book suggestions
- Author expansion
- Genre exploration
- Diversity recommendations
- Community data integration
- Personalized recommendations

**Model Choice**: Sonnet - Needs sophisticated reasoning for recommendation algorithms

#### goal-tracker (Haiku)
**Responsibility**: Reading goals
**Tools**: Read, Write, Python
**Triggers**: "set goal", "reading challenge", "goal progress", "on track"
**Key Operations**:
- Set annual reading goals
- Track progress vs. targets
- Milestone management
- Pace analysis
- Adjustment recommendations
- Achievement celebration

**Model Choice**: Haiku - Straightforward calculations and progress tracking

### 2. Skills (2 total)

#### reading-management
**Location**: `skills/reading-management/SKILL.md`
**Purpose**: Comprehensive data structure standards and patterns
**Contents**:
- Book/Progress/Note/Goal schemas
- Directory structure standards
- List management workflows
- Progress calculation algorithms
- Note organization strategies
- Analytics computation patterns
- API integration guidelines
- Error handling patterns

**Usage**: MANDATORY first read for all agents

#### book-api-integration (Future)
**Location**: `skills/book-api-integration/SKILL.md`
**Purpose**: External API integration patterns
**Contents**:
- Goodreads API patterns
- LibraryThing API patterns
- Open Library usage
- Rate limiting strategies
- Caching best practices
- Response normalization

### 3. Python Tools

#### book_api_client.py
**Purpose**: Unified API client with caching and rate limiting
**Features**:
- Open Library integration (no key required)
- Goodreads support (with API key)
- LibraryThing support (with API key)
- File-based response caching (30-day TTL)
- Automatic rate limiting (configurable)
- ISBN lookup and book search
- Response normalization to standard schema

**Key Classes**:
- `RateLimiter`: Decorator for rate-limiting functions
- `APICache`: File-based cache with TTL
- `BookAPIClient`: Main client interface

#### analytics_engine.py (Future)
**Purpose**: Statistical analysis and visualization
**Features**:
- Time-series analysis
- Distribution calculations
- Trend detection
- Reading pace algorithms
- Goal projection models
- Text-based chart generation

#### recommendation_system.py (Future)
**Purpose**: ML-based recommendations
**Features**:
- Collaborative filtering
- Content-based recommendations
- Hybrid strategies
- Diversity optimization
- Explanation generation

## Data Architecture

### Storage Strategy: Local-First

**Location Priority**:
1. Project-level: `.reading-tracker/` (if .git exists)
2. User-level: `~/.reading-tracker/` (global)

**Directory Structure**:
```
.reading-tracker/
├── library.json              # Main book database
├── progress.json             # Reading sessions and progress
├── goals.json               # Reading goals and challenges
├── recommendations.json     # Cached recommendations
├── config.json             # User preferences and API keys
├── notes/                  # Notes by book
│   └── {book-id}/
│       └── notes.json
├── analytics/              # Generated reports
│   ├── monthly/
│   └── yearly/
└── .cache/                 # API response cache
    └── *.json
```

### Data Flow

**Add Book Flow**:
```
User: "Add The Pragmatic Programmer"
    ↓
reading-list-manager activates
    ↓
Reads reading-management skill
    ↓
Executes Python: add_book()
    ↓
Optionally: book_api_client.fetch_by_isbn()
    ↓
Updates library.json
    ↓
Returns confirmation with book details
```

**Progress Update Flow**:
```
User: "Read pages 1-45 of Pragmatic Programmer"
    ↓
progress-tracker activates
    ↓
Reads reading-management skill
    ↓
Executes Python: log_session()
    ↓
Calculates: percentage, pace, estimate
    ↓
Updates progress.json
    ↓
Returns progress summary with streak
```

**Generate Report Flow**:
```
User: "Generate January reading report"
    ↓
reading-analyst activates
    ↓
Reads reading-management skill
    ↓
Executes Python: generate_report()
    ↓
Loads library.json and progress.json
    ↓
Calculates statistics and trends
    ↓
Saves to analytics/monthly/2025-01.md
    ↓
Returns formatted report with visualizations
```

## Integration Points

### External APIs

**Open Library** (no key required):
- ISBN lookups
- Book search
- Cover images
- Basic metadata

**Goodreads** (requires API key):
- Enhanced metadata
- Community ratings
- Reading lists import
- Recommendations

**LibraryThing** (requires API key):
- Library import
- Enhanced metadata
- Series information
- Tag data

### Import/Export Formats

**Import**:
- Goodreads CSV export
- LibraryThing JSON
- Custom JSON schema
- ISBN lists (plain text)

**Export**:
- JSON (full data export)
- CSV (spreadsheet-compatible)
- Markdown (human-readable)
- PDF (formatted reports - future)

## Workflow Patterns

### Complete Book Lifecycle

```
1. Discovery: @recommendation-engine suggest
2. Add: @reading-list-manager add to to-read
3. Start: @reading-list-manager move to reading
4. Progress: @progress-tracker log sessions
5. Notes: @notes-organizer capture insights
6. Complete: @reading-list-manager mark completed
7. Rate: @reading-list-manager rate book
8. Analyze: @reading-analyst update statistics
9. Discover next: @recommendation-engine what next
```

### Monthly Review Workflow

```
1. @reading-analyst generate monthly report
2. @goal-tracker check goal progress
3. @notes-organizer export monthly highlights
4. @recommendation-engine suggest next month focus
```

### Research Reading Workflow

```
1. @reading-list-manager create collection
2. @reading-list-manager add books to collection
3. @notes-organizer tag notes by theme
4. @notes-organizer link related notes
5. @notes-organizer search notes by keyword
6. @notes-organizer export collection summary
```

## Performance Characteristics

### Agent Response Times

- **reading-list-manager**: ~2-5s (with API calls: +3-10s)
- **progress-tracker**: ~0.5-1s (Haiku, simple calculations)
- **notes-organizer**: ~1-3s (depends on note count)
- **reading-analyst**: ~2-5s (depends on library size)
- **recommendation-engine**: ~2-4s (algorithm complexity)
- **goal-tracker**: ~0.5-1s (Haiku, straightforward math)

### Scalability

**Library Size**:
- Small (< 100 books): All operations fast
- Medium (100-1000 books): Noticeable delay in analytics
- Large (1000+ books): Consider pagination/indexing

**Notes**:
- Organized by book directory (scales well)
- Search may slow with 10,000+ notes
- Consider full-text search engine for large collections

### Caching Strategy

**API Responses**: 30-day TTL
**Benefits**:
- Reduced API calls (respect rate limits)
- Faster metadata enrichment
- Offline capability for cached data

## Security & Privacy

### Data Privacy
- All data stored locally
- No telemetry or external tracking
- API keys encrypted in config
- Optional: user-managed backup

### API Key Management
```json
{
  "apis": {
    "goodreads_key": "YOUR_KEY",
    "librarything_key": "YOUR_KEY"
  }
}
```

Or environment variables:
```bash
export GOODREADS_API_KEY=your_key
export LIBRARYTHING_API_KEY=your_key
```

## Error Handling

### Validation Errors
- Book data validation before save
- Progress bounds checking
- Status transition validation

### Recovery Patterns
- Automatic backups before destructive operations
- Transaction-like updates
- Restore from backup on corruption

### API Failures
- Graceful degradation (continue without metadata)
- Retry logic with exponential backoff
- Cache fallback

## Testing Strategy

### Agent Testing
```bash
# Initialize library
@reading-list-manager "Initialize library"

# Add test book
@reading-list-manager "Add test book: Title by Author, ISBN 123"

# Log progress
@progress-tracker "Read pages 1-10 of test book"

# Verify data
cat ~/.reading-tracker/library.json | jq '.books'
```

### Data Integrity Tests
- Validate JSON structure
- Check referential integrity
- Verify calculations

## Future Enhancements

### Planned Features
1. **Mobile app sync** (self-hosted server)
2. **Audiobook tracking** (time-based instead of pages)
3. **OCR for quotes** (photograph physical book pages)
4. **Advanced ML recommendations** (collaborative filtering)
5. **Social features** (optional sharing with friends)
6. **Reading clubs** (shared lists and discussions)
7. **Multi-language support** (UI translations)
8. **Advanced visualizations** (actual charts, not text-based)

### Technical Improvements
1. **SQLite database** (for large libraries)
2. **Full-text search** (for notes)
3. **Incremental backups** (version control for data)
4. **Plugin webhooks** (integrate with other services)
5. **Performance optimization** (lazy loading, indexing)

## Development Guidelines

### Adding New Features
1. Determine if it fits existing agent or needs new one
2. Update reading-management skill with patterns
3. Implement in agent using Python
4. Add tests
5. Update README with usage examples

### Modifying Data Schema
1. Update reading-management skill first
2. Implement migration script
3. Version bump in data files
4. Test with existing data

### Integration with Other Plugins
- Orchestrator: Multi-step book operations
- Subagent Creator: Generate custom reading agents
- Future: Calendar sync for reading time blocking

---

**Architecture Version**: 1.0.0
**Last Updated**: 2025-01-22
**Status**: Production Ready
