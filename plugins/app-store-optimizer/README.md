# App Store Optimizer Plugin

**Comprehensive ASO (App Store Optimization) toolkit for maximizing app visibility, conversion, and user acquisition**

Drive organic installs through data-driven keyword research, optimized listings, conversion-focused creatives, and professional review management for both Apple App Store and Google Play Store.

## What This Plugin Does

The App Store Optimizer plugin provides a complete ASO workflow:

1. **Keyword Research**: Discover high-value keywords, analyze competition, and prioritize based on search volume and achievability
2. **Listing Optimization**: Craft conversion-focused titles, descriptions, and metadata optimized for each platform
3. **Creative Asset Optimization**: Design specifications for screenshots, icons, and videos that maximize conversion rates
4. **Review Management**: Monitor, respond to, and extract insights from user reviews to improve ratings and retention

## Quick Start

### Keyword Research
```bash
@keyword-researcher "Research keywords for a meal planning and calorie tracking app"
```

The agent will:
- Generate seed keywords from multiple categories
- Use WebSearch to discover related terms and search volumes
- Analyze top 10 competitors
- Score keywords by relevance, volume, competition, and difficulty
- Provide platform-specific recommendations for iOS and Android

**Output**: Prioritized keyword lists, competitor analysis, and metadata recommendations

---

### Listing Optimization
```bash
@listing-optimizer "Optimize app store listing for both iOS and Android using keyword research results"
```

The agent will:
- Read keyword research results
- Craft optimized titles (30 chars) and subtitles
- Write conversion-focused descriptions (iOS: conversion-first, Android: SEO + conversion)
- Create A/B test variations
- Provide localization guidance for top markets

**Output**: Complete metadata for both platforms, A/B test variants, and localization strategy

---

### Creative Optimization
```bash
@creative-optimizer "Create screenshot and icon specifications for fitness tracking app"
```

The agent will:
- Analyze competitor visual strategies
- Design screenshot specifications (hero, features, social proof, CTA)
- Provide icon design recommendations with differentiation strategy
- Write app preview video scripts
- Create A/B test variations for creatives

**Output**: Detailed design briefs, screenshot messaging, icon strategy, and video scripts

---

### Review Management
```bash
@review-manager "Process and respond to recent app store reviews"
```

The agent will:
- Categorize reviews by rating and type
- Generate personalized, professional responses
- Extract sentiment trends and insights
- Track feature requests and bug reports
- Monitor review metrics and competitor comparisons

**Output**: Response queue, sentiment analysis, feature request tracking, and bug reports

---

## Plugin Structure

```
plugins/app-store-optimizer/
├── README.md
├── skills/
│   └── aso-strategy/
│       └── SKILL.md                    # Comprehensive ASO methodology
├── agents/
│   ├── keyword-researcher.md           # Keyword discovery and analysis
│   ├── listing-optimizer.md            # Metadata optimization
│   ├── creative-optimizer.md           # Visual asset specifications
│   └── review-manager.md               # Review monitoring and response
└── [outputs created in ./aso/]
```

## Skills

### ASO Strategy Skill (`aso-strategy/SKILL.md`)

Comprehensive guide covering:

**Fundamentals**:
- ASO ranking factors and algorithms
- Apple App Store vs Google Play differences
- Visibility vs conversion optimization

**Keyword Research**:
- Seed keyword brainstorming (category, functional, problem-solving, competitor terms)
- Boolean search operators and advanced search techniques
- Search volume estimation and competition assessment
- Keyword scoring formulas (Priority = Volume × Relevance / Competition × Difficulty)

**Metadata Optimization**:
- Title and subtitle strategies (30 characters)
- Keyword field optimization (iOS: 100 chars, comma-separated, no duplicates)
- Description writing (iOS: conversion-focused, Android: SEO + conversion)
- First 250 characters critical on Android

**Visual Assets**:
- Screenshot strategy (hero value prop, features, social proof, CTA)
- Text overlay guidelines (40% max, high contrast, benefit-focused)
- Icon design principles (simple, bold, 1-3 colors, strong silhouette)
- App preview video structure (0-3 sec hook, features, CTA)

**Review Management**:
- Response strategies by rating (100% of 1-2 stars, 50-75% of 3 stars)
- Professional response templates
- Sentiment analysis and trend tracking
- Feature request and bug extraction

**A/B Testing**:
- iOS Product Page Optimization (PPO)
- Google Play Experiments
- What to test and how to measure

**Localization**:
- Top market prioritization
- Keyword research per locale (don't just translate)
- Cultural adaptation guidelines

**Competitive Analysis**:
- Metadata, visual, and keyword gap analysis
- Review mining for insights

## Agents

### 1. Keyword Researcher (`keyword-researcher.md`)

**Model**: Sonnet (needs strategic thinking)

**Tools**: Read, Write, Bash, WebSearch, Grep, Glob

**Key Capabilities**:
- Generates seed keywords across 5 categories
- Uses WebSearch to discover search terms, auto-complete suggestions, and competitor keywords
- Analyzes top 10 competitors for keyword strategies
- Scores keywords with priority formula
- Categorizes by intent (discovery, feature, competitor, branded)
- Provides platform-specific recommendations

**Outputs**:
- `./aso/keywords/keyword-research.md` - Full analysis
- `./aso/keywords/priority-keywords.md` - Top keywords by tier
- `./aso/keywords/competitor-analysis.md` - Gap analysis
- `./aso/keywords/metadata-recommendations.md` - Implementation guide

**When to Use**:
- New app launch
- Rebranding or repositioning
- Quarterly keyword strategy refresh
- Competitor analysis
- Entering new markets

---

### 2. Listing Optimizer (`listing-optimizer.md`)

**Model**: Sonnet (needs copywriting expertise)

**Tools**: Read, Write, Edit, Bash, Grep, Glob

**Key Capabilities**:
- Crafts titles and subtitles within character limits
- Writes conversion-focused descriptions (platform-specific strategies)
- Optimizes iOS keyword field (100 chars, algorithmic combinations)
- Integrates keywords naturally (no stuffing)
- Creates A/B test variations
- Provides localization guidance with cultural adaptation

**Outputs**:
- `./aso/listings/ios-metadata.md` - Complete iOS listing
- `./aso/listings/android-metadata.md` - Complete Android listing
- `./aso/listings/ab-test-variants.md` - Testing variations
- `./aso/listings/localization-guide.md` - Translation strategy

**When to Use**:
- Implementing keyword strategy
- Improving low conversion rates
- Launching new versions
- Expanding to new markets
- A/B testing metadata

---

### 3. Creative Optimizer (`creative-optimizer.md`)

**Model**: Sonnet (needs design strategy thinking)

**Tools**: Read, Write, Bash, Grep, Glob

**Key Capabilities**:
- Designs screenshot strategy (5-8 screenshots with specific purposes)
- Creates detailed screenshot specifications (messaging, layout, visual elements)
- Provides icon design briefs with competitor differentiation
- Writes app preview video scripts (hook, features, CTA structure)
- Generates A/B test variations for visual elements
- Includes localization considerations

**Outputs**:
- `./aso/creative/screenshot-specifications.md` - All screenshot designs
- `./aso/creative/icon-recommendations.md` - Icon design guide
- `./aso/creative/video-script.md` - Video production guide
- `./aso/creative/design-brief.md` - Overall creative direction
- `./aso/creative/ab-test-creative.md` - Visual testing variations

**When to Use**:
- Designing new app store assets
- Improving low product page conversion
- A/B testing screenshots or icon
- Refresh stale visuals
- Competitor analysis for visual strategy

---

### 4. Review Manager (`review-manager.md`)

**Model**: Haiku (fast response times, deterministic task)

**Tools**: Read, Write, Bash, Grep, Glob

**Key Capabilities**:
- Categorizes reviews by rating and type (bug, feature, praise, confusion)
- Generates personalized responses using templates
- Extracts sentiment trends over time
- Tracks feature requests with prioritization
- Documents bug reports for dev team
- Monitors review metrics and competitor comparisons

**Outputs**:
- `./aso/reviews/response-queue.md` - Ready-to-post responses
- `./aso/reviews/sentiment-analysis.md` - Trends and insights
- `./aso/reviews/feature-requests.md` - Product feedback
- `./aso/reviews/bug-tracker.md` - Technical issues

**When to Use**:
- Daily review monitoring
- After major updates
- Managing rating declines
- Extracting user feedback
- Competitive intelligence from reviews

---

## Complete ASO Workflow

### Phase 1: Research & Strategy (Week 1-2)

```bash
# Step 1: Keyword Research
@keyword-researcher "Research keywords for [app description]"

# Review outputs:
# - aso/keywords/keyword-research.md
# - aso/keywords/priority-keywords.md
# - aso/keywords/competitor-analysis.md

# Step 2: Competitive Analysis
@keyword-researcher "Deep dive competitor analysis for top 5 apps in [category]"
```

### Phase 2: Optimization (Week 2-3)

```bash
# Step 3: Listing Optimization
@listing-optimizer "Optimize metadata for iOS and Android using keyword research"

# Review outputs:
# - aso/listings/ios-metadata.md
# - aso/listings/android-metadata.md

# Step 4: Creative Assets
@creative-optimizer "Design screenshots and icon for [app] emphasizing [key value props]"

# Review outputs:
# - aso/creative/screenshot-specifications.md
# - aso/creative/icon-recommendations.md
# - aso/creative/video-script.md (if needed)
```

### Phase 3: Implementation (Week 3-4)

1. **Implement Metadata**:
   - Update titles, subtitles, descriptions in App Store Connect / Play Console
   - Implement keyword field (iOS)
   - Localize for top 5 markets

2. **Create Visual Assets**:
   - Design screenshots per specifications
   - Design/update icon
   - Produce video if applicable

3. **Set Up A/B Tests**:
   - iOS: Product Page Optimization (PPO)
   - Android: Google Play Experiments
   - Test one variable at a time

### Phase 4: Monitor & Iterate (Ongoing)

```bash
# Daily: Review Management
@review-manager "Process new reviews from past 24 hours"

# Weekly: Performance Monitoring
# - Track keyword rankings
# - Monitor conversion rates
# - Check A/B test results

# Monthly: Strategy Refresh
@keyword-researcher "Identify new keyword opportunities and trends"
@listing-optimizer "Optimize based on performance data"

# Quarterly: Major Refresh
# - Comprehensive competitor analysis
# - Creative asset refresh
# - Expand localization
```

---

## Best Practices

### Keyword Research
- Research 50+ keywords minimum
- Analyze top 10 competitors
- Focus on long-tail opportunities (lower competition, higher conversion)
- Balance head terms (volume) and niche terms (achievability)
- Localize keywords (don't just translate)

### Listing Optimization
- Stay within character limits (30 for title/subtitle, 100 for keywords)
- Never keyword stuff
- iOS description: pure conversion (not indexed)
- Android description: SEO + conversion (first 250 chars critical)
- A/B test title variations

### Creative Assets
- First screenshot is hero value proposition (not app UI)
- 40% text maximum in screenshots
- Icon must work at 120x120px
- Video hook in first 3 seconds
- Test screenshot order and messaging

### Review Management
- Respond to 100% of 1-2 star reviews within 24 hours
- Personalize every response (don't copy-paste)
- Extract feature requests for product team
- Track bug reports for dev team
- Monitor sentiment trends

### A/B Testing
- Test one variable at a time
- Run for minimum 2 weeks
- Need 300+ conversions per variant
- Monitor both conversion AND retention
- Document learnings for iteration

---

## Expected Impact

Following this ASO workflow typically results in:

**Visibility Improvements**:
- 50-200% increase in organic impressions (keyword optimization)
- Top 10 rankings for 5-15 targeted keywords
- Category ranking improvements

**Conversion Rate Improvements**:
- 15-40% lift from optimized screenshots
- 10-25% lift from optimized metadata
- 20-30% lift from icon updates

**Rating & Review Improvements**:
- 0.1-0.3 star rating increase (professional response strategy)
- 50-100% increase in review volume (smart prompting)
- Reduced negative review impact (fast response)

**Overall Download Impact**:
- 50-300% increase in organic installs (combined efforts)
- 30-50% reduction in cost-per-install (less paid acquisition needed)
- Higher quality users (better targeting = better fit)

---

## Tips for Success

1. **Start with Keyword Research**: Everything builds on keyword strategy
2. **Optimize for Both Platforms**: iOS and Android require different approaches
3. **Test Everything**: Use Product Page Optimization (iOS) and Experiments (Android)
4. **Monitor Continuously**: ASO is ongoing, not one-time
5. **Respond to Reviews**: 100% of 1-2 stars, builds trust with potential users
6. **Localize Properly**: Research local keywords, don't just translate
7. **Align with Product**: Use review insights to improve app, not just listings
8. **Be Patient**: ASO results compound over weeks/months

---

## Common Mistakes to Avoid

- ❌ Keyword stuffing in titles
- ❌ Ignoring platform differences (iOS vs Android)
- ❌ Using same description for both platforms
- ❌ Too much text in screenshots (>40-50%)
- ❌ Generic, feature-focused screenshots
- ❌ Copying competitor listings exactly
- ❌ Not responding to negative reviews
- ❌ Ending A/B tests too early
- ❌ Changing too many variables at once
- ❌ Ignoring localization opportunities

---

## Platform Differences

### Apple App Store
- 30-char title, 30-char subtitle
- 100-char keyword field (comma-separated, no spaces)
- Description NOT indexed for search (pure conversion focus)
- 10 screenshots max, 3 preview videos
- A/B testing via Product Page Optimization (PPO)

### Google Play Store
- 30-char title, 80-char short description
- NO separate keyword field (uses description text)
- Description IS indexed for search (SEO + conversion)
- 8 screenshots max, 1 preview video
- A/B testing via Google Play Experiments

---

## ASO Metrics to Track

- **Impressions**: How often app appears in search
- **Conversion rate**: Impressions → Downloads (3-5% good, 10%+ excellent)
- **Keyword rankings**: Position for target keywords
- **Download velocity**: Daily/weekly downloads
- **Rating**: Average star rating (4.5+ ideal)
- **Review volume**: New reviews per day
- **Retention**: D1, D7, D30 retention rates

---

## Integration with Other Plugins

**Works well with**:
- **Product Manager**: Feature requests from reviews inform product roadmap
- **Content Strategist**: Messaging consistency across app and marketing
- **Data Analyst**: Performance metrics and A/B test analysis
- **Copywriter**: Brand voice in descriptions and responses
- **Designer**: Visual asset production from specifications

---

## Support & Resources

**ASO Tools** (third-party, optional):
- App Annie / Sensor Tower: Market intelligence
- AppTweak / Mobile Action: Keyword tracking
- Storemaven: Product page optimization
- AppFollow: Review management

**Official Resources**:
- Apple: App Store Product Page Best Practices
- Google: Google Play Store Listing Best Practices
- WWDC: App Store Optimization sessions
- Google I/O: Play Store growth talks

**Community**:
- r/AppStoreOptimization
- ASO Stack: Community forum
- Mobile Dev Memo: Industry news

---

## Version

**Plugin Version**: 1.0
**Last Updated**: January 2025
**Compatibility**: iOS App Store, Google Play Store
**Success Rate**: 50-300% organic install increase in 3 months (following complete workflow)

---

## Questions?

This plugin provides the complete ASO toolkit. Each agent has detailed documentation on when and how to use it.

Start with `@keyword-researcher` to establish your keyword strategy, then proceed through listing optimization, creative design, and ongoing review management.

All agents read from the comprehensive `aso-strategy/SKILL.md` skill file to ensure best practices are followed.
