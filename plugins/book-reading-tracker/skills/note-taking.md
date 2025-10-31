# Note-Taking Skill

Comprehensive patterns for book notes, highlights, quotes, and annotation management.

## Note Data Structure

```json
{
  "id": "unique-note-id",
  "bookId": "unique-book-id",
  "bookTitle": "Book Title",
  "author": "Author Name",
  "type": "note|highlight|quote|question|summary",
  "content": "The actual note or quote text",
  "pageNumber": 127,
  "chapter": "Chapter 5: The Discovery",
  "location": "kindle-location-1234",
  "tags": ["theme:identity", "character:protagonist", "literary-device:metaphor"],
  "themes": ["Identity", "Transformation"],
  "dateCreated": "2025-02-15T14:30:00Z",
  "dateModified": "2025-02-15T15:00:00Z",
  "context": "Additional context about why this is noteworthy",
  "relatedNotes": ["note-id-1", "note-id-2"]
}
```

## Note Types

### 1. Highlights
- Direct text from the book
- Preserve exact wording
- Include page/location reference
- May include brief commentary

### 2. Quotes
- Memorable passages
- Exact quotation with citation
- Use quotation marks
- Include page number for citation

### 3. Notes
- Personal thoughts and reactions
- Analysis and interpretation
- Questions raised by the text
- Connections to other books/ideas

### 4. Summaries
- Chapter summaries
- Section overviews
- Plot point recaps
- Key concept summaries

### 5. Questions
- Unanswered questions
- Discussion prompts
- Areas for further research
- Interpretive questions

## Organization Patterns

### By Book Structure
```
Book Title
├── Front Matter
│   └── Notes on introduction
├── Part 1: Beginning
│   ├── Chapter 1
│   │   ├── Page 10: Highlight
│   │   ├── Page 15: Note
│   │   └── Page 20: Quote
│   └── Chapter 2
│       └── Page 35: Summary
└── Part 2: Development
    └── ...
```

### By Theme
```
Themes
├── Identity
│   ├── Book A, p. 45
│   ├── Book B, p. 112
│   └── Book C, p. 67
├── Power Dynamics
│   ├── Book A, p. 89
│   └── Book D, p. 23
└── Redemption
    └── ...
```

### By Tag System
- **Themes**: `theme:identity`, `theme:power`, `theme:love`
- **Characters**: `character:protagonist`, `character:antagonist`
- **Literary Devices**: `device:metaphor`, `device:foreshadowing`
- **Topics**: `topic:politics`, `topic:technology`
- **Quality**: `brilliant`, `profound`, `confusing`

## Citation Formats

### Standard Citation
```
"Quote text here." (Author Last Name, Page Number)
Example: "It was the best of times..." (Dickens, 1)
```

### Full Citation
```
Author Last Name, First Name. Book Title. Publisher, Year. Page Number.
Example: Dickens, Charles. A Tale of Two Cities. Penguin, 1859. p. 1.
```

### Kindle Location
```
"Quote text here." (Author, Location 1234)
```

## Highlight Compilation

### By Color Code (if using physical books)
- **Yellow**: Important concepts
- **Blue**: Beautiful prose
- **Green**: Questions/confusion
- **Pink**: Favorite passages

### By Priority
- **High**: Essential to understanding
- **Medium**: Interesting but supplementary
- **Low**: Nice to have

## Note-Taking Best Practices

### During Reading
1. **Mark immediately**: Note insights as they occur
2. **Brief is better**: Short notes while reading, expand later
3. **Page references**: Always include page/location
4. **Context matters**: Note what prompted the thought
5. **Flag for follow-up**: Mark notes needing expansion

### After Reading
1. **Review and organize**: Consolidate notes by theme
2. **Expand abbreviated notes**: Add full thoughts
3. **Create summaries**: Chapter and book-level
4. **Link related ideas**: Connect notes across books
5. **Tag thoroughly**: Apply consistent tag system

## Search and Retrieval

### Search Strategies
- Full-text search across all notes
- Filter by book, author, or date
- Search by tag or theme
- Find notes in date range
- Search within specific book

### Common Searches
- "Show all notes about [theme]"
- "Find quotes from [author]"
- "Notes from books read in [year]"
- "Highlights about [topic]"
- "Questions from [book title]"

## Export Formats

### Markdown Export
```markdown
# Book Title by Author Name

## Chapter 1: Title

### Page 10
**Highlight:** "Quote text here"

**Note:** My thoughts on this passage...

### Page 15
**Question:** Why did the character...?
```

### PDF Export
- Formatted with book metadata
- Organized by chapter
- Includes citations
- Table of contents
- Tag index

### JSON Export
- Complete data structure
- Machine-readable
- Portable format
- Preserves relationships

## Note Linking

### Cross-Reference Patterns
- Link notes with similar themes
- Connect character development across chapters
- Link foreshadowing to outcomes
- Connect to notes from other books

### Reference Format
```
Related to: [Book Title, p. XX] - [Brief description]
See also: [Note ID] about [theme]
Contrasts with: [Book Title] where author says...
```

## Review and Maintenance

### Regular Review
- Weekly: Review recent notes
- Monthly: Organize and tag
- Quarterly: Update themes
- Annually: Archive and export

### Quality Control
- Verify page references
- Complete abbreviated notes
- Fix typos in quotes
- Update tags
- Remove duplicates

## Analysis Patterns

### Thematic Analysis
- Collect all notes on a theme
- Compare across books
- Track theme development
- Identify patterns

### Character Analysis
- Compile character mentions
- Track development arc
- Note key quotes
- Analyze motivations

### Writing Style Analysis
- Collect stylistic examples
- Note literary devices
- Track language patterns
- Study narrative techniques

## Annotation Guidelines

### What to Note
- Key arguments or thesis statements
- Memorable quotes
- Passages that move you emotionally
- Confusing sections (for clarification)
- Connections to other readings
- Questions for further thought
- Examples and evidence
- Beautiful or powerful language

### What to Avoid
- Over-highlighting (diminishes usefulness)
- Vague notes without context
- Incomplete citations
- Unsorted accumulation
- Duplicate entries
