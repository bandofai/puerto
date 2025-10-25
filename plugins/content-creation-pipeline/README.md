# Content Creation Pipeline Plugin

Complete content planning and publishing workflow specialist with idea capture, calendar planning, draft tracking, multi-platform posting, and performance analytics.

## Overview

Transform your content creation from chaotic inspiration to systematic production with a complete pipeline covering idea capture through performance optimization. This plugin provides specialized agents and comprehensive workflows for managing content across blogs, social media, newsletters, and more.

## What's Included

### Agents

#### 1. idea-inbox (Haiku)
**Purpose**: Capture and organize content ideas from any source.

A fast, efficient agent that:
- Captures ideas from voice memos, notes, conversations, articles
- Categorizes by content type (blog, social, video, newsletter)
- Tags for discoverability and filtering
- Tracks status through the pipeline (inbox → published)
- Provides search and filtering capabilities
- Integrates with content scheduler

**Activation**: Use `@idea-inbox` or let it activate when capturing content ideas.

**Example Usage**:
```
@idea-inbox I just had an idea while walking: create a tutorial about
JavaScript closures for beginners. I keep seeing questions about this.
Could work as blog post and Twitter thread.
```

#### 2. content-scheduler (Haiku)
**Purpose**: Plan content calendar and manage multi-platform publishing.

A strategic planning agent that:
- Creates and maintains content calendar
- Schedules posts across multiple platforms
- Generates platform-specific publishing checklists
- Manages milestones (outline, draft, review, publish)
- Optimizes posting times by platform
- Suggests content repurposing opportunities
- Tracks publishing status per platform

**Activation**: Use `@content-scheduler` or let it activate for calendar planning.

**Example Usage**:
```
@content-scheduler Schedule the closures tutorial for next Tuesday,
with blog post at 9am, Twitter thread at 10am, and LinkedIn post at 11am.
```

#### 3. performance-tracker (Sonnet)
**Purpose**: Analyze content performance and provide optimization insights.

An analytical agent that:
- Tracks metrics across all platforms (views, engagement, clicks)
- Compares performance against benchmarks
- Calculates performance scores (0-10)
- Identifies success patterns and improvement opportunities
- Generates comprehensive performance reports
- Recommends repurposing strategies for top content
- Updates benchmarks from historical data
- Provides actionable optimization suggestions

**Activation**: Use `@performance-tracker` or let it activate for analytics requests.

**Example Usage**:
```
@performance-tracker Analyze the performance of the async/await tutorial
published last week. What worked well and what should I optimize?
```

### Skill: content-pipeline

Comprehensive workflow patterns covering:
- **Idea Capture**: From inspiration to structured ideas
- **Calendar Planning**: Strategic scheduling and timing
- **Draft Tracking**: Status management through pipeline stages
- **Multi-Platform Publishing**: Platform-specific optimization
- **Performance Analytics**: Metrics, benchmarks, and insights
- **Content Repurposing**: Maximize ROI from top content
- **Batching Strategies**: Efficient production workflows
- **Evergreen Libraries**: Building reusable content assets
- **Engagement Tactics**: Community building and feedback loops
- **Anti-Patterns**: Common pitfalls to avoid

### Templates

#### 1. ideas-database.json
Example structure for the content ideas database with:
- Complete idea objects with all metadata
- Status tracking through pipeline
- Tag indexing for search
- Statistics and metrics
- Example ideas across different types

#### 2. content-calendar.json
Example content calendar structure with:
- Scheduled posts with platform breakdown
- Milestone tracking (outline, draft, review)
- Asset requirements and checklists
- SEO planning per post
- Promotion strategies
- Upcoming milestones view

#### 3. performance-metrics.json
Example performance tracking with:
- Platform-specific metrics (blog, Twitter, LinkedIn)
- Aggregate performance data
- Benchmark comparisons
- Performance scoring
- Insights and recommendations
- Trend analysis
- Top performers identification

## The Content Pipeline

### Complete Workflow

```
1. IDEA CAPTURE (idea-inbox)
   Voice memo, note, conversation
   ↓
   Structured idea with metadata
   ↓
   Status: inbox → backlog

2. CALENDAR PLANNING (content-scheduler)
   Review backlog ideas
   ↓
   Schedule on calendar
   ↓
   Status: backlog → scheduled
   ↓
   Generate checklists

3. CONTENT CREATION (manual or with writing agents)
   Create outline
   ↓
   Write draft
   ↓
   Edit and refine
   ↓
   Status: scheduled → outline → draft → editing → ready

4. MULTI-PLATFORM PUBLISHING (content-scheduler)
   Publish on blog (primary)
   ↓
   Cross-post to social media
   ↓
   Feature in newsletter
   ↓
   Status: ready → published

5. PERFORMANCE TRACKING (performance-tracker)
   Wait 7 days for metrics stabilization
   ↓
   Gather platform analytics
   ↓
   Calculate performance score
   ↓
   Generate insights report
   ↓
   Identify repurposing opportunities
   ↓
   Status: published → archived
   ↓
   Inform future content strategy
```

### Status Progression

| Status | Description | Typical Duration | Agent |
|--------|-------------|------------------|-------|
| **inbox** | Just captured, needs review | 0-2 days | idea-inbox |
| **backlog** | Reviewed, ready for scheduling | Ongoing | idea-inbox |
| **scheduled** | On calendar, publish date set | 1-4 weeks | content-scheduler |
| **outline** | Structure created | 1 day | Manual/writing agent |
| **draft** | First version written | 1-2 days | Manual/writing agent |
| **editing** | Being revised | 1 day | Manual/editing agent |
| **ready** | Final version, ready to publish | 0-7 days | Manual |
| **published** | Live on platforms | Ongoing | content-scheduler |
| **archived** | Performance tracked, completed | Permanent | performance-tracker |

## Installation

```bash
/plugin install content-creation-pipeline@puerto
```

After installation:
1. Restart Claude Code to activate agents
2. Initialize your content database (agents do this automatically)
3. Start capturing ideas with `@idea-inbox`

## File Structure

```
content-creation-pipeline/
├── .claude-plugin/
│   └── plugin.json              # Plugin metadata
├── agents/
│   ├── idea-inbox.md            # Idea capture agent (Haiku)
│   ├── content-scheduler.md     # Calendar planning agent (Haiku)
│   └── performance-tracker.md   # Analytics agent (Sonnet)
├── skills/
│   └── content-pipeline/
│       └── SKILL.md             # Comprehensive workflow patterns
├── templates/
│   ├── ideas-database.json      # Example idea database
│   ├── content-calendar.json    # Example calendar structure
│   └── performance-metrics.json # Example performance tracking
└── README.md                    # This file
```

## Data Storage

All content data is stored in `.claude/content/`:

```
.claude/content/
├── ideas.json                   # Central idea database
├── calendar.json                # Content calendar
├── metrics.json                 # Performance metrics
├── inbox/                       # Voice memos, quick captures
├── checklists/                  # Platform-specific checklists
├── analytics/                   # Raw analytics data
└── reports/                     # Performance reports
```

This keeps all content workflow data organized and accessible.

## Usage Examples

### Scenario 1: Capture Voice Memo Idea

**You**:
```
I just recorded a voice memo about my experience debugging a tricky
async bug. The key insight was using console.trace() to track the
call stack. This could make a good quick tip post for Twitter and
maybe expand into a blog post about debugging techniques.
```

**idea-inbox activates**:
```
Captured: idea-2025-01-22-001

Title: Using console.trace() for Async Debugging
Type: social (can expand to blog)
Platforms: twitter, blog
Status: inbox
Priority: medium

Core insight: console.trace() helps track async call stacks when
debugging complex promise chains or async/await code.

Tags: #javascript #debugging #async #tips

Next step: Review and move to backlog when ready
Use: @content-scheduler to plan publication
```

### Scenario 2: Schedule Content

**You**:
```
@content-scheduler Schedule the console.trace debugging tip for
Friday at 10am on Twitter, and if it performs well, I'll expand
it into a full blog post next week.
```

**content-scheduler responds**:
```
Scheduled: post-2025-01-26-001

Title: Using console.trace() for Async Debugging
Publish Date: 2025-01-26 10:00 UTC
Type: social

Platforms:
  - Twitter: 2025-01-26 10:00 (single tweet)

Milestones:
  - Draft due: 2025-01-25 (tomorrow)
  - Final due: 2025-01-26 08:00

Checklist created:
  - twitter: .claude/content/checklists/post-2025-01-26-001-twitter.md

Next: Create tweet by tomorrow
```

### Scenario 3: View Calendar

**You**:
```
@content-scheduler Show me what's scheduled for this week
```

**content-scheduler responds**:
```
=== Content Calendar: 2025-01-22 to 2025-01-28 ===

2025-01-25 - 10 VS Code Extensions That Save Time [blog]
  - Blog: 09:00
  - Twitter: 10:00 (thread)
  - dev.to: 14:00

2025-01-26 - Using console.trace() for Async Debugging [social]
  - Twitter: 10:00

Total: 2 posts scheduled
Platforms: Blog (1), Twitter (2), dev.to (1)
```

### Scenario 4: Analyze Performance

**You**:
```
@performance-tracker Analyze the async/await tutorial I published last week.
How did it perform?
```

**performance-tracker responds**:
```
=== Performance Report: Async/Await Tutorial ===

Published: 2025-01-15
Tracking Period: 7 days

Overall Performance: 8.5/10 (Excellent)

Total Reach: 25,950
Total Engagement: 1,897 (7.3%)
Total Clicks: 515

Platform Breakdown:
  Blog: 1,250 views | 4:32 avg time | 45 shares
  Twitter: 15,200 impressions | 6.4% engagement
  LinkedIn: 8,500 impressions | 4.6% engagement

Benchmarks:
  vs Average Views: 1.4x 📈
  vs Average Engagement: 1.8x 📈
  vs Average Shares: 2.1x 📈

Key Insights:
  ✓ Strong Twitter performance (6.4% vs 4.8% avg)
  ✓ Above-average blog engagement (4:32 vs 3:45)
  ✓ Content resonated with technical audience

Repurposing Recommendations (High Priority):
  1. Create "Advanced Async Patterns" follow-up
  2. Extract code examples into Twitter thread
  3. Submit to dev.to and Medium for additional reach
  4. Create YouTube video walkthrough

Next Steps:
  - Respond to remaining comments (12 on blog)
  - Plan follow-up content on advanced patterns
  - Update benchmarks with this post's data

Full report: .claude/content/reports/post-2025-01-15-001-report.md
```

### Scenario 5: Find Top Performers

**You**:
```
@performance-tracker Show me my top performing content from last month
```

**performance-tracker responds**:
```
=== Top Performing Content (Last 30 Days) ===

1. [8.5] Async/Await Tutorial for JavaScript Beginners
   Reach: 25,950 | Engagement: 1,897 (7.3%)
   Tags: javascript, tutorial, async, beginners

2. [7.8] 10 Productivity Tips for Remote Developers
   Reach: 18,400 | Engagement: 1,205 (6.5%)
   Tags: productivity, remote, career

3. [7.2] Building a REST API with Node.js
   Reach: 14,200 | Engagement: 892 (6.3%)
   Tags: nodejs, api, tutorial

=== Common Success Factors ===

Top Tags:
  javascript: 3 posts (avg score 7.8)
  tutorial: 2 posts (avg score 8.1)
  career: 1 post (avg score 7.8)

Best Platforms (avg engagement):
  blog: 5.2%
  twitter: 6.1%
  linkedin: 4.3%

Insights:
  - Tutorial content performs 20% better than average
  - Technical topics (JavaScript) get high engagement
  - Twitter threads drive most blog traffic
```

## Advanced Usage

### Content Batching

Create multiple pieces in focused sessions:

```
@idea-inbox I want to batch-create 4 tutorial ideas around JavaScript:
1. Array methods deep dive
2. Object destructuring patterns
3. Template literals beyond basics
4. Error handling best practices
```

idea-inbox will create 4 separate ideas, all tagged "javascript" and "tutorial", ready for batch scheduling.

### Content Series Planning

```
@content-scheduler I want to create a 4-week series on React hooks.
Schedule:
- Week 1: useState basics
- Week 2: useEffect patterns
- Week 3: Custom hooks
- Week 4: Performance optimization

Each week: Blog post Tuesday 9am, Twitter thread Wednesday 10am
```

content-scheduler will create 4 calendar entries with consistent timing, tagged as a series.

### Performance Comparison

```
@performance-tracker Compare the performance of all my JavaScript
tutorials from the last 3 months. Which topics resonate most?
```

performance-tracker will analyze patterns across similar content and identify winning topics/formats.

### Repurposing Pipeline

```
@performance-tracker The async/await tutorial scored 8.5. Give me a
complete repurposing plan to maximize its reach.
```

performance-tracker will suggest:
- Twitter thread (extract key points)
- YouTube video (code walkthrough)
- Newsletter feature (with commentary)
- dev.to/Medium cross-posting
- Instagram carousel (visual summary)
- Follow-up advanced content

## Best Practices

### Daily Workflow

**Morning** (5 minutes):
```
1. Check calendar for today's posts
2. Review any pending milestones
3. Capture any overnight ideas
```

**Evening** (10 minutes):
```
1. Process inbox ideas (categorize, tag)
2. Update draft statuses
3. Engage with published content comments
```

### Weekly Review (30 minutes)

```
1. @idea-inbox "Show me all inbox ideas"
   - Promote best to backlog
   - Archive unclear ideas

2. @content-scheduler "Show next 2 weeks"
   - Ensure all slots filled
   - Generate missing checklists

3. @performance-tracker "Analyze last week's posts"
   - Review performance
   - Note patterns
   - Plan repurposing
```

### Monthly Planning (1 hour)

```
1. Review performance trends
2. Identify top-performing topics/formats
3. Plan next month's content themes
4. Update benchmarks
5. Set growth goals
6. Audit tool/workflow efficiency
```

## Publishing Checklists

The content-scheduler generates platform-specific checklists automatically. Here are the standards:

### Blog Post Checklist
- [ ] SEO title (50-60 characters)
- [ ] Meta description (150-160 characters)
- [ ] Cover image (1200x630px)
- [ ] Headings (H2/H3 structure)
- [ ] Internal links (2-3 related posts)
- [ ] Images with alt text
- [ ] Code syntax highlighting
- [ ] Reading time estimate
- [ ] Social share buttons
- [ ] Newsletter CTA
- [ ] Preview on mobile and desktop

### Twitter Thread Checklist
- [ ] Hook tweet (compelling first tweet)
- [ ] Thread outline (7-10 tweets)
- [ ] Each tweet under 280 characters
- [ ] Images prepared (1-4 per tweet)
- [ ] Hashtags (2-3 max)
- [ ] Link to blog in final tweet
- [ ] Schedule or post
- [ ] Engage with early replies

### LinkedIn Post Checklist
- [ ] Professional headline
- [ ] First 2 lines compelling (preview)
- [ ] Paragraph breaks for readability
- [ ] Hashtags (3-5 relevant)
- [ ] Professional tone
- [ ] Call-to-action
- [ ] Tag relevant people/companies
- [ ] Share in relevant groups

### Newsletter Checklist
- [ ] Subject line (40-50 characters)
- [ ] Preview text optimized
- [ ] Mobile-first design
- [ ] Scannable format (bullets, bold)
- [ ] One primary CTA
- [ ] All links tested
- [ ] Unsubscribe link present
- [ ] Test email to yourself
- [ ] Schedule send time

## Performance Benchmarks

Target metrics by platform:

### Blog
- **Views**: 500+ (new), 2,000+ (established)
- **Time on page**: 3+ minutes
- **Bounce rate**: <50%
- **Shares**: 20+ per post

### Twitter
- **Impressions**: 5,000+ per thread
- **Engagement rate**: 2-5% (good), 5%+ (excellent)
- **Link clicks**: 100+ to blog
- **Thread completion**: 60%+

### LinkedIn
- **Impressions**: 3,000+ per post
- **Engagement rate**: 1-3%
- **Comments**: 10+ (quality discussions)
- **Shares**: 15+

### Newsletter
- **Open rate**: 20-30% (good), 30%+ (great)
- **Click rate**: 2-5% (decent), 5%+ (excellent)
- **Unsubscribe**: <0.5% per send
- **Reply rate**: >1% (high engagement)

## Troubleshooting

### Agents Not Finding Data

**Issue**: Agent can't find ideas.json or calendar.json

**Solution**: Agents create these automatically. Just use them:
```
@idea-inbox Capture this idea: [your idea]
```
The agent will initialize the database if it doesn't exist.

### Performance Tracking Seems Off

**Issue**: Metrics don't match platform analytics

**Solution**:
1. Wait 7 days after publish (metrics stabilize)
2. Manually update with accurate data
3. Benchmarks update monthly from historical data

### Calendar Conflicts

**Issue**: Too many posts scheduled for one day

**Solution**:
```
@content-scheduler Show calendar for [date]
```
Review and reschedule as needed. Agent suggests optimal slots.

### Ideas Getting Lost

**Issue**: Can't find old ideas

**Solution**: Use tags and search:
```
@idea-inbox Search for ideas tagged "javascript"
@idea-inbox Show all high priority ideas in backlog
```

## Integration with Other Plugins

### With subagent-creator

Create custom content writing agents:
```
@ultimate-subagent-creator Create an agent that writes blog post
outlines following my content-pipeline skill patterns
```

### With orchestrator

Coordinate complex content workflows:
```
@orchestrator-planner Plan a content workflow: research topic,
create outline, write draft, generate social posts, schedule everything
```

## Future Enhancements

Planned features:
- **AI-assisted idea enrichment**: Generate titles/tags automatically
- **Social media auto-posting**: Direct integration with platform APIs
- **Analytics auto-import**: Pull metrics from Google Analytics, Twitter API
- **Content A/B testing**: Test titles, publish times, formats
- **Collaboration features**: Team workflows, approval processes
- **Content library**: Searchable archive of all published content
- **Template system**: Reusable post structures and formats

## Contributing

This plugin is part of the Puerto marketplace. See main repository for contribution guidelines.

## Support

For issues or questions:
- Review the [content-pipeline skill](skills/content-pipeline/SKILL.md) for comprehensive workflows
- Check agent files for specific capabilities
- Refer to templates for data structure examples

## License

MIT License - See main repository for details

---

**Transform content chaos into systematic excellence. From idea to performance insights, every step optimized.**
