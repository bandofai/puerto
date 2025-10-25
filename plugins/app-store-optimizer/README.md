# App Store Optimizer Plugin

ASO (App Store Optimization) specialist for maximizing app visibility, downloads, and conversion through keyword research, metadata optimization, creative assets, review management, and competitive analysis.

## Overview

The App Store Optimizer plugin provides agents for data-driven ASO using proven strategies for both Apple App Store and Google Play Store, focusing on organic discovery and conversion optimization.

## Agents

### 1. keyword-researcher (Sonnet, WebSearch, Skill-Aware)
Conducts keyword research to identify high-traffic, low-competition keywords for app discovery.

**Use for**: Keyword discovery, search volume analysis, competitor keyword analysis, keyword difficulty assessment

**Example**:
```
Use keyword-researcher for fitness tracking app.
App category: Health & Fitness
Core features: Step counting, workout tracking, calorie counting
Target markets: US, UK, Canada
Research:
- High-volume keywords (search volume, competition)
- Long-tail opportunities (specific use cases)
- Competitor keywords (apps ranking for similar terms)
- Localized keywords per market
Output: 50+ keywords with volume, difficulty, relevance scores
```

### 2. listing-optimizer (Sonnet, Skill-Aware)
Optimizes app title, subtitle, description, and promotional text for keywords and conversion.

**Use for**: App Store/Play Store metadata, keyword placement, compelling copy, localization

**Example**:
```
Use listing-optimizer for productivity app.
Keywords: task management, to-do list, project planning, team collaboration
Constraints:
- App Store: 30-char title, 30-char subtitle
- Play Store: 30-char title, 80-char short description
Requirements:
- Primary keyword in title
- Secondary keywords in subtitle/short description
- Compelling value proposition
- Call-to-action in description
- Social proof (users, ratings)
Output: Optimized metadata for both stores
```

### 3. creative-optimizer (Sonnet, Skill-Aware)
Optimizes app icon, screenshots, and preview videos for maximum conversion.

**Use for**: Icon design guidance, screenshot messaging, preview video scripts, A/B testing recommendations

**Example**:
```
Use creative-optimizer for e-commerce app.
Assets:
- App icon: Design principles for recognition and tappability
- Screenshots (10 required): Feature highlights, benefit-focused messaging
- Preview video (30 seconds): Hook, problem, solution, CTA
Optimization:
- First 3 screenshots critical (visible without scroll)
- Text overlays with value props
- Social proof (ratings, user count)
- Localization for each market
A/B test ideas: Different value props, screenshot order, icon variations
```

### 4. review-manager (Sonnet, Skill-Aware)
Manages app reviews: response strategies, sentiment analysis, feature request extraction, reputation management.

**Use for**: Review responses, negative review mitigation, review solicitation, feedback analysis

**Example**:
```
Use review-manager for app with 4.2 rating.
Issues in recent reviews:
- Crash on iOS 17 (20% of negative reviews)
- Missing dark mode (15%)
- Slow performance (10%)
- Price complaints (5%)
Tasks:
- Draft responses to negative reviews (empathetic, solution-focused)
- Identify bug reports vs feature requests
- Prioritize issues by frequency
- Create review solicitation strategy (in-app prompts)
- Monitor competitor reviews for opportunities
```

## Skills

### aso-strategy
Comprehensive ASO best practices and optimization frameworks:
- **Keyword Research**: Search volume tools, keyword difficulty, long-tail strategy, competitor analysis
- **App Store Algorithm**: Keyword relevance, download velocity, rating/reviews, retention
- **Metadata Optimization**: Title (30 chars), subtitle (30 chars), keyword field (100 chars iOS), description (4000 chars)
- **Creative Assets**: Icon design, screenshot messaging, preview video structure
- **Conversion Optimization**: Value proposition, social proof, credibility indicators
- **Localization**: 40+ languages, cultural adaptation, keyword translation
- **A/B Testing**: Title variants, icon tests, screenshot experiments, statistical significance
- **Review Management**: Response templates, sentiment analysis, review velocity
- **Competitor Analysis**: Keyword overlap, positioning, feature gaps

## Templates

### app-store-listing-template.md
Complete app store listing: Title, subtitle, description, promotional text, keyword field (iOS), short description (Android), what's new, support URL, marketing URL.

### keyword-research-template.md
Keyword research framework: Target keywords with search volume, competition, relevance scores, seasonal trends, localization variants, keyword clusters.

### screenshot-specifications.md
Screenshot best practices: Dimensions (6.7", 6.5", 5.5" iOS / phone, tablet Android), messaging hierarchy, text overlay guidelines, localization requirements, A/B test ideas.

### review-response-playbook.md
Review response templates: Positive reviews (thank you), negative reviews (empathy, solution, update), bug reports (acknowledge, timeline), feature requests (consider, roadmap).

## Workflows

### Complete ASO Optimization
```
1. Keyword research
Use keyword-researcher to identify 50+ target keywords

2. Metadata optimization
Use listing-optimizer to optimize title, subtitle, description with keywords

3. Creative optimization
Use creative-optimizer to design icon, screenshots, preview video

4. Review management
Use review-manager to respond to reviews and improve rating

5. Monitor & iterate
Track rankings, downloads, conversion rate; A/B test variations
```

### App Launch ASO
```
Pre-launch (4 weeks before):
- keyword-researcher: Build keyword list
- listing-optimizer: Draft metadata variants for A/B testing
- creative-optimizer: Create icon and screenshot variations

Launch week:
- Submit app with optimized metadata
- Monitor keyword rankings daily
- Solicit initial reviews from beta users

Post-launch (ongoing):
- review-manager: Respond to all reviews within 48 hours
- A/B test metadata and creatives monthly
- Update keywords based on performance data
```

## Requirements Met

✅ Role: ASO (App Store Optimization) specialist
✅ Keyword research: keyword-researcher with search volume and competition analysis
✅ App title/description optimization: listing-optimizer with keyword placement
✅ Screenshot and preview optimization: creative-optimizer with conversion best practices
✅ Review management strategy: review-manager with response playbooks
✅ Competitor analysis: Covered in keyword-researcher and aso-strategy skill
✅ Tools: ASO tools (WebSearch for research), analytics, research capabilities

## Key Features

✓ **Keyword Research**: Search volume, competition, relevance scoring
✓ **Metadata Optimization**: Title, subtitle, description with keyword density
✓ **Creative Assets**: Icon, screenshots, preview videos
✓ **Localization**: 40+ languages with cultural adaptation
✓ **A/B Testing**: Statistical testing for metadata and creatives
✓ **Review Management**: Response playbooks, sentiment analysis
✓ **Competitor Analysis**: Keyword overlap, positioning gaps
✓ **Conversion Optimization**: First impression, social proof, CTAs

## ASO Fundamentals

### App Store Search Algorithm Factors
1. **Title keywords** (highest weight)
2. **Download velocity** (growth rate matters)
3. **Ratings & reviews** (quality and quantity)
4. **Keyword field** (iOS only, 100 characters)
5. **Retention rate** (Day 1, Day 7, Day 30)
6. **Update frequency** (signals active development)

### Conversion Optimization
- **App icon**: Unique, recognizable, simple (works at 512px and 60px)
- **First 3 screenshots**: Visible without scrolling, most important
- **Value proposition**: Clear benefit in 3 seconds or less
- **Social proof**: Ratings count, featured badges, user testimonials
- **Credibility**: Press mentions, awards, user count

### Platform Differences

**Apple App Store**:
- 30-char title, 30-char subtitle
- 100-char keyword field (comma-separated, no spaces)
- 10 screenshots (max), 3 preview videos
- A/B testing via App Store Product Page Optimization

**Google Play Store**:
- 30-char title, 80-char short description, 4000-char long description
- No separate keyword field (uses description)
- 8 screenshots (max), 1 preview video (up front)
- A/B testing via Google Play Experiments

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 1 comprehensive aso-strategy skill
- ✅ 4 professional templates for listings, keywords, screenshots, reviews
- ✅ Complete README with platform-specific workflows

## ASO Metrics to Track

- **Impressions**: How often app appears in search
- **Conversion rate**: Impressions → Downloads (3-5% good, 10%+ excellent)
- **Keyword rankings**: Position for target keywords
- **Download velocity**: Daily/weekly downloads
- **Rating**: Average star rating (4.5+ ideal)
- **Review volume**: New reviews per day
- **Retention**: D1, D7, D30 retention rates

Closes #77
