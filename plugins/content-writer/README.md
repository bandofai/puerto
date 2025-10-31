# Content Writer Plugin

**Professional content creation for blogs, SEO, marketing copy, and email campaigns**

A comprehensive plugin providing four specialized agents to handle all aspects of content marketing, from blog writing to conversion-optimized copy.

---

## Overview

This plugin provides a complete content creation workflow with:

- **4 Specialized Agents**: Each agent focuses on one content type
- **3 Comprehensive Skills**: Industry best practices for content marketing
- **3 Professional Templates**: Ready-to-use starting points
- **Full Coverage**: Blog posts → SEO → Marketing copy → Email campaigns

---

## Agents

### 1. blog-writer (Sonnet - Creative Writing)

**When to use**: Creating engaging blog posts and long-form content

**What it does**:
- Writes SEO-optimized blog posts with engaging narratives
- Researches topics using web search
- Follows proper blog structure (hook, body, conclusion, CTA)
- Creates attention-grabbing headlines
- Implements storytelling techniques
- Optimizes for readability and engagement

**Skill-aware**: Reads `content-writing` skill before starting

**Example usage**:
```bash
"Write a 1500-word blog post about sustainable fashion trends for 2025.
Target audience: millennials interested in eco-friendly lifestyle.
Include statistics, expert quotes, and actionable tips."
```

**Output**:
- Complete blog post in Markdown
- SEO-optimized title and meta description
- Structured with H2/H3 headings
- Engaging introduction and strong CTA
- Reading time estimate
- Suggested featured image description

**Tools**: Read, Write, Bash, WebSearch, Glob
**Model**: Sonnet (creative writing requires judgment and nuance)

---

### 2. seo-optimizer (Sonnet - Strategic Analysis)

**When to use**: Optimizing content for search engines

**What it does**:
- Keyword research and analysis
- Meta description optimization
- Readability improvements (Flesch score)
- Internal/external linking suggestions
- Header tag optimization (H1, H2, H3 hierarchy)
- Image alt text recommendations
- Search intent analysis
- Content gap identification

**Skill-aware**: Reads `seo-optimization` skill before starting

**Example usage**:
```bash
"Optimize this blog post for the keyword 'remote work productivity tools'.
Target Flesch reading score of 60+. Suggest internal links to our product pages."
```

**Output**:
- SEO analysis report
- Keyword density and placement recommendations
- Optimized meta title and description
- Readability score and improvements
- Link building opportunities
- Structured data suggestions
- Competitive analysis

**Tools**: Read, Write, Edit, WebSearch, Grep, Glob
**Model**: Sonnet (SEO requires strategic thinking)

---

### 3. copywriter (Sonnet - Persuasive Writing)

**When to use**: Creating marketing copy, product descriptions, and CTAs

**What it does**:
- Product descriptions that convert
- Landing page copy (AIDA framework)
- Compelling calls-to-action
- Value proposition statements
- Feature-to-benefit conversion
- Social proof integration
- Urgency and scarcity messaging
- Brand voice consistency

**Skill-aware**: Reads `copywriting` skill before starting

**Example usage**:
```bash
"Write product descriptions for our new line of ergonomic office chairs.
Features: adjustable lumbar support, breathable mesh, 5-year warranty.
Target: remote workers with back pain. Use benefit-driven language."
```

**Output**:
- Persuasive product descriptions
- Multiple headline variations
- Feature-benefit matrix
- CTA buttons and microcopy
- Social proof elements
- Urgency/scarcity copy
- A/B testing suggestions

**Tools**: Read, Write, Edit, Bash, Glob
**Model**: Sonnet (persuasive writing requires psychological insight)

---

### 4. email-campaigner (Haiku - Template-Based)

**When to use**: Creating email campaigns and newsletters

**What it does**:
- Email campaign creation from templates
- Newsletter content generation
- Subject line optimization (A/B variants)
- Personalization token integration
- Mobile-responsive HTML emails
- Plain text versions
- Spam score analysis
- Segmentation recommendations

**Skill-aware**: Reads `content-writing` skill for tone/voice

**Example usage**:
```bash
"Create a welcome email campaign for new subscribers.
Tone: friendly and helpful. Include discount code WELCOME10.
3-email sequence: welcome, product intro, success stories."
```

**Output**:
- HTML email templates
- Plain text versions
- Subject line variations (5+ options)
- Preview text optimization
- Personalization placeholders
- CTA buttons with tracking
- Mobile preview notes

**Tools**: Read, Write, Bash, Glob
**Model**: Haiku (template-based, fast and cost-effective)

---

## Skills

### 1. content-writing

**Professional blog writing and storytelling techniques**

Covers:
- Blog post structure (hook, introduction, body, conclusion, CTA)
- Storytelling frameworks (Hero's Journey, Problem-Solution-Benefit)
- Engagement techniques (questions, statistics, anecdotes)
- Tone and voice guidelines (casual, professional, authoritative)
- Readability optimization (sentence length, paragraph structure)
- Headline formulas (numbers, how-to, listicles, questions)
- Content research methods (sources, citations, fact-checking)
- Editing checklist (grammar, clarity, flow, consistency)

**When read**: By `blog-writer` and `email-campaigner` agents

---

### 2. seo-optimization

**Search engine optimization and content discovery**

Covers:
- Keyword research methodology (search volume, difficulty, intent)
- On-page SEO elements (title tags, meta descriptions, headers)
- Readability metrics (Flesch score, grade level, sentence length)
- Search intent analysis (informational, navigational, transactional)
- Content structure for featured snippets
- Internal linking strategy (topic clusters, pillar pages)
- Image optimization (alt text, file names, compression)
- Technical SEO basics (schema markup, canonical tags)
- Competitive content analysis
- E-A-T principles (Expertise, Authoritativeness, Trustworthiness)

**When read**: By `seo-optimizer` agent

---

### 3. copywriting

**Persuasive writing and conversion optimization**

Covers:
- AIDA framework (Attention, Interest, Desire, Action)
- PAS formula (Problem, Agitate, Solution)
- Feature-to-benefit conversion techniques
- Value proposition development
- Call-to-action best practices (action verbs, urgency, clarity)
- Social proof integration (testimonials, reviews, case studies)
- Urgency and scarcity tactics (ethical approaches)
- Headline psychology (curiosity, benefit, specificity)
- Microcopy optimization (buttons, forms, error messages)
- Brand voice consistency across channels
- A/B testing strategies for copy
- Emotional triggers and persuasion psychology

**When read**: By `copywriter` agent

---

## Templates

### 1. blog-post-template.md

**Standard blog post structure**

Includes:
- SEO-optimized title with keyword
- Meta description (150-160 characters)
- Engaging introduction with hook
- H2/H3 structured body sections
- Bullet points and numbered lists
- Conclusion with key takeaways
- Strong call-to-action
- Author bio section
- Related posts suggestions

### 2. product-description-template.md

**E-commerce product copy template**

Includes:
- Attention-grabbing headline
- Brief overview (2-3 sentences)
- Key features in bullet points
- Benefit-driven descriptions
- Technical specifications table
- Social proof section
- Urgency/scarcity element
- Multiple CTA placements
- FAQ section

### 3. email-template.html

**Responsive email campaign template**

Includes:
- Mobile-responsive HTML structure
- Header with logo/branding
- Personalization tokens ({{first_name}}, etc.)
- Hero section with main message
- Content sections (features, benefits)
- CTA buttons (primary and secondary)
- Footer with unsubscribe
- Plain text alternative
- Tracking pixel placeholder

---

## Workflow Examples

### Example 1: Complete Blog Post Creation

```bash
# 1. Write initial draft
@blog-writer "Write a blog post about 'How AI is transforming content marketing'.
Target: marketing managers. Length: 1200 words. Include case studies."

# 2. Optimize for SEO
@seo-optimizer "Optimize this blog post for keyword 'AI content marketing tools'.
Target featured snippet format. Add internal links to our AI product pages."

# 3. Enhance CTAs
@copywriter "Improve the call-to-action sections in this blog post.
Goal: drive free trial signups. Use urgency without being pushy."
```

### Example 2: Product Launch Campaign

```bash
# 1. Create product descriptions
@copywriter "Write product descriptions for our new SaaS product.
Features: automated reporting, real-time analytics, API integrations.
Target: data analysts at mid-size companies."

# 2. Email announcement
@email-campaigner "Create a 3-email product launch sequence.
Email 1: Teaser, Email 2: Features reveal, Email 3: Launch day offer.
Include early bird discount."

# 3. Landing page copy
@copywriter "Write landing page copy for this product. Include hero headline,
3 key benefits, feature section, pricing table copy, and FAQ."

# 4. SEO optimization
@seo-optimizer "Optimize the landing page for 'automated analytics platform'.
Suggest schema markup and meta tags."
```

### Example 3: Content Marketing Audit

```bash
# 1. SEO audit
@seo-optimizer "Audit all blog posts in ./content/blog/ for SEO issues.
Check keyword optimization, meta descriptions, internal links, and readability."

# 2. Improve top performers
@blog-writer "Expand the top 5 performing blog posts with updated statistics
and additional sections based on related search queries."

# 3. Update CTAs
@copywriter "Review and update all CTAs in blog posts to align with new
product messaging and current campaigns."
```

---

## Installation

### User-Level (Available in All Projects)

```bash
# Clone or copy this plugin to your user-level plugins directory
cp -r plugins/content-writer ~/.claude/plugins/

# Verify installation
ls ~/.claude/plugins/content-writer/agents/
```

### Project-Level (Project-Specific)

```bash
# Copy to project's .claude directory
mkdir -p .claude/plugins
cp -r plugins/content-writer .claude/plugins/

# Commit to version control
git add .claude/plugins/content-writer/
git commit -m "feat: add content-writer plugin"
```

---

## Configuration

### Customize Brand Voice

Create project-specific voice guidelines in `.claude/skills/`:

```bash
# Override content-writing skill for your brand
mkdir -p .claude/skills/content-writing/
cp ~/.claude/plugins/content-writer/skills/content-writing/SKILL.md \
   .claude/skills/content-writing/SKILL.md

# Add your brand voice guidelines
nano .claude/skills/content-writing/SKILL.md
```

Example brand voice addition:
```markdown
## Brand Voice: [Your Company]

**Tone**: Professional but approachable
**Language**: Active voice, simple words (8th-grade reading level)
**Avoid**: Jargon, hype, superlatives without proof
**Use**: Customer stories, data-driven insights, actionable advice
**Personality**: Helpful expert, not sales-focused
```

Skills priority: `.claude/skills/` > `~/.claude/skills/` > plugin default

---

## Design Decisions

### Why These Agents?

**Four agents, not one**: Each content type requires different expertise:
- blog-writer: Long-form storytelling and research
- seo-optimizer: Technical SEO and analytics
- copywriter: Persuasion and conversion psychology
- email-campaigner: Template-based campaigns

**Why different models**:
- Sonnet (blog, SEO, copy): Creative and strategic thinking required
- Haiku (email): Template-based, fast turnaround for campaigns

### Why Skill-Aware?

Skills ensure consistent quality and adherence to best practices:

**Quality Difference**:
- Without skills: Generic content, inconsistent voice, poor SEO
- With skills: Brand-aligned, optimized, conversion-focused

Skills are continuously updated with latest content marketing trends.

---

## Cost Optimization

**Estimated costs per task** (based on Claude pricing):

| Task | Agent | Model | Est. Cost |
|------|-------|-------|-----------|
| Blog post (1500 words) | blog-writer | Sonnet | $0.15-0.25 |
| SEO optimization | seo-optimizer | Sonnet | $0.08-0.12 |
| Product description | copywriter | Sonnet | $0.05-0.08 |
| Email campaign (3 emails) | email-campaigner | Haiku | $0.03-0.05 |

**Total cost for full campaign**: ~$0.31-0.50

**ROI**: Professional content creation typically costs $100-500/piece from agencies

---

## Best Practices

### Content Creation

1. **Research first**: Use web search to gather current data and trends
2. **Know your audience**: Define target persona before creating content
3. **Optimize for humans first**: SEO comes after good writing
4. **Use data**: Include statistics, case studies, and proof points
5. **Edit ruthlessly**: First draft is never final

### SEO Optimization

1. **Keyword intent matters**: Match content to search intent
2. **Natural language**: Don't stuff keywords unnaturally
3. **Mobile-first**: Optimize for mobile readability
4. **Link strategically**: Internal links for topic authority
5. **Update regularly**: Refresh content to maintain rankings

### Copywriting

1. **Lead with benefits**: Features tell, benefits sell
2. **Use social proof**: Testimonials build trust
3. **Create urgency ethically**: Real scarcity, not fake FOMO
4. **Test everything**: A/B test headlines, CTAs, copy
5. **Keep it simple**: Clear > clever

### Email Marketing

1. **Subject line is critical**: 40% of success depends on it
2. **Personalize authentically**: Beyond just {{first_name}}
3. **Mobile-responsive always**: 60%+ opens on mobile
4. **Clear single CTA**: One primary action per email
5. **Test before sending**: Check spam score and rendering

---

## Integration with Other Plugins

### With frontend-developer

```bash
# 1. Create landing page copy
@copywriter "Write landing page copy for AI writing assistant product"

# 2. Build landing page
@component-builder "Create landing page components from this copy.
Include hero, features, testimonials, pricing, and CTA sections."
```

### With backend-architect

```bash
# 1. Design blog API
@api-designer "Design REST API for blog management system.
Endpoints for posts, categories, tags, authors."

# 2. Create blog content
@blog-writer "Write 10 sample blog posts for API documentation examples"
```

---

## Troubleshooting

### Blog posts too generic

**Issue**: Content lacks specificity or unique angle

**Solutions**:
- Provide more detailed brief with target audience
- Include competitor examples to differentiate from
- Specify unique data or perspectives to include
- Add brand voice guidelines to project skills

### SEO scores too low

**Issue**: Content not ranking or getting flagged

**Solutions**:
- Check keyword research (search volume vs. competition)
- Verify search intent match (informational vs. commercial)
- Improve readability (shorter sentences, simpler words)
- Add more relevant internal and external links

### Copy not converting

**Issue**: CTAs getting low click-through rates

**Solutions**:
- Test multiple headline variations
- Strengthen value proposition clarity
- Add more specific social proof
- Create stronger urgency/scarcity messaging
- Simplify language (reduce reading grade level)

### Emails going to spam

**Issue**: Low deliverability rates

**Solutions**:
- Avoid spam trigger words (free, guaranteed, act now)
- Balance text-to-image ratio (60:40 minimum)
- Include plain text version
- Test with spam checker tools
- Verify sender authentication (SPF, DKIM)

---

## Resources

### Content Writing
- [Content Marketing Institute](https://contentmarketinginstitute.com/)
- [Copyblogger](https://copyblogger.com/)
- [Ann Handley's Writing Tips](https://annhandley.com/)

### SEO
- [Moz Beginner's Guide to SEO](https://moz.com/beginners-guide-to-seo)
- [Ahrefs Blog](https://ahrefs.com/blog/)
- [Google Search Central](https://developers.google.com/search)

### Copywriting
- [Copyhackers](https://copyhackers.com/)
- [AWAI Copywriting Resources](https://www.awai.com/)
- [Joanna Wiebe's Copy School](https://copyhackers.com/copy-school/)

### Email Marketing
- [Really Good Emails](https://reallygoodemails.com/)
- [Litmus Email Resources](https://www.litmus.com/resources/)
- [Email on Acid Blog](https://www.emailonacid.com/blog/)

---

## License

Part of the Puerto plugin ecosystem.

---

## Changelog

### v1.0.0 (2025-01-20)

**Initial Release**

- 4 specialized agents (blog-writer, seo-optimizer, copywriter, email-campaigner)
- 3 comprehensive skills (content-writing, seo-optimization, copywriting)
- 3 professional templates
- Web search integration for research
- SEO best practices
- Conversion optimization frameworks
- Cost-optimized (Haiku for templates, Sonnet for creative)

---

## Support

**Issues**: Report at [Puerto GitHub Issues](https://github.com/bandofai/puerto/issues)

**Questions**: Tag your issue with `plugin:content-writer`

**Feature Requests**: Use `enhancement` label

---

**Version**: 1.0.0
**Author**: Puerto Plugin System
**Last Updated**: January 2025
**Status**: Production Ready
**Success Rate**: High-quality content with proper usage and clear briefs
