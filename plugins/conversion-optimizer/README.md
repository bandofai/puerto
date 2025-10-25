# Conversion Rate Optimizer Plugin

CRO (Conversion Rate Optimization) specialist for analyzing conversion funnels, designing A/B tests, mapping user journeys, optimizing landing pages, and improving CTAs to maximize conversion rates.

## Overview

The Conversion Rate Optimizer plugin provides agents for data-driven conversion optimization using proven CRO frameworks, statistical testing methodologies, and user behavior analysis.

## Agents

### 1. funnel-analyzer (Sonnet, Skill-Aware)
Analyzes conversion funnels to identify drop-off points, calculate conversion rates, and recommend improvements.

**Use for**: Funnel analysis, drop-off identification, conversion rate calculation, bottleneck diagnosis

**Example**:
```
Use funnel-analyzer for e-commerce checkout funnel.
Funnel stages:
1. Product page (10,000 visits)
2. Add to cart (2,000 - 20% conversion)
3. Checkout started (1,500 - 75% conversion)
4. Payment info (900 - 60% conversion)
5. Order complete (720 - 80% conversion)

Analysis:
- Overall conversion: 7.2% (product → purchase)
- Biggest drop-off: Product → Cart (80% drop)
- Second issue: Checkout → Payment (40% drop)
Recommendations: Product page CTA optimization, checkout simplification
```

### 2. ab-test-designer (Sonnet, Skill-Aware)
Designs statistically rigorous A/B tests with hypotheses, success metrics, sample size calculations, and analysis plans.

**Use for**: A/B test planning, hypothesis development, sample size calculation, statistical analysis

**Example**:
```
Use ab-test-designer to improve signup conversion.
Current: 15% signup rate from landing page (5,000 visitors/week)
Hypothesis: Reducing form fields from 8 to 4 will increase signups by 25% (15% → 18.75%)
Test design:
- Variant A (control): 8 fields (name, email, company, role, phone, industry, size, country)
- Variant B: 4 fields (name, email, company, role)
- Success metric: Signup conversion rate
- Sample size: 3,200 visitors per variant (80% power, 95% confidence)
- Duration: 3 weeks
- Statistical test: Two-proportion z-test
```

### 3. journey-mapper (Sonnet, Skill-Aware)
Maps user journeys to visualize paths to conversion, identify friction points, and optimize touchpoints.

**Use for**: Customer journey mapping, touchpoint analysis, pain point identification, experience optimization

**Example**:
```
Use journey-mapper for SaaS free trial to paid conversion.
Journey stages:
1. Awareness: Google search → Blog post → CTA
2. Consideration: Landing page → Feature comparison → Pricing
3. Trial signup: Form → Email verification → Onboarding
4. Activation: First login → Setup wizard → First project created
5. Engagement: Daily use → Feature adoption → Value realization
6. Conversion: Upgrade prompt → Pricing selection → Payment → Paid user

For each stage:
- User actions, thoughts, emotions
- Touchpoints (website, email, in-app)
- Pain points and friction
- Optimization opportunities
```

### 4. landing-page-optimizer (Sonnet, Skill-Aware)
Optimizes landing pages for conversion using proven frameworks: clarity, relevance, value proposition, trust, urgency.

**Use for**: Landing page audits, headline optimization, CTA design, trust elements, page structure

**Example**:
```
Use landing-page-optimizer for PPC landing page.
Goal: Maximize demo requests for B2B SaaS
Current: 8% conversion rate
Audit:
- Headline: Clear value prop? Benefit-focused?
- Hero section: Compelling visual? Social proof?
- Value proposition: Unique? Specific? Quantified?
- Features: Benefit-oriented? Scannable?
- Social proof: Logos, testimonials, stats?
- Trust: Security badges, certifications?
- CTA: Clear, specific, contrasting? Above fold?
- Form: Minimal fields? Privacy assurance?
- Mobile: Responsive? Fast loading?
Recommendations: Prioritized list of improvements with expected impact
```

## Skills

### cro-strategy
Comprehensive conversion optimization frameworks and methodologies:
- **Funnel Analysis**: AARRR (Pirate Metrics), conversion rate calculation, drop-off analysis
- **A/B Testing**: Hypothesis formation, sample size (power analysis), statistical significance, Bayesian vs Frequentist
- **User Psychology**: Persuasion principles (Cialdini), cognitive biases, motivation (Fogg Behavior Model)
- **Landing Page Optimization**: Above-fold clarity, value proposition, F-pattern/Z-pattern layout
- **CTA Optimization**: Button copy, color, size, placement, urgency
- **Trust Building**: Social proof, testimonials, security badges, money-back guarantees
- **Urgency & Scarcity**: Countdown timers, limited availability, FOMO triggers
- **Form Optimization**: Field reduction, progressive disclosure, inline validation
- **Mobile CRO**: Thumb-friendly design, simplified navigation, fast loading
- **Personalization**: Dynamic content, behavioral targeting, segmentation

## Templates

### funnel-analysis-template.md
Funnel analysis framework: Stage definition, traffic volume per stage, conversion rates, drop-off analysis, benchmark comparison, improvement recommendations, prioritization matrix.

### ab-test-plan-template.md
A/B test documentation: Hypothesis, success metrics, variants description, sample size calculation, test duration, significance level, analysis plan, learnings documentation.

### user-journey-map-template.md
Journey mapping template: Stages (awareness → conversion), user actions/thoughts/emotions per stage, touchpoints, pain points, opportunities, quantitative data (drop-off rates).

### landing-page-checklist.md
Landing page optimization checklist: Headline (value prop), hero section, benefits vs features, social proof, trust elements, CTA optimization, form design, mobile optimization, page speed.

## Workflows

### Complete CRO Process
```
1. Analyze funnel
Use funnel-analyzer to identify biggest drop-off points

2. Map user journey
Use journey-mapper to understand user experience and pain points

3. Optimize landing pages
Use landing-page-optimizer to improve key conversion pages

4. Design A/B tests
Use ab-test-designer to validate improvements with statistical rigor

5. Iterate
Analyze results, implement winners, test next hypothesis
```

### Landing Page Optimization
```
1. Audit current page
Use landing-page-optimizer to identify issues

2. Prioritize improvements
Focus on high-impact, low-effort changes first

3. Create variants
Design improved version based on recommendations

4. A/B test
Use ab-test-designer to validate improvement statistically

5. Implement winner
Roll out winning variant to all traffic
```

## Requirements Met

✅ Role: CRO (Conversion Rate Optimization) specialist
✅ Conversion funnel analysis: funnel-analyzer with drop-off identification
✅ A/B test design and analysis: ab-test-designer with statistical rigor
✅ User journey mapping: journey-mapper with touchpoint and pain point analysis
✅ Landing page optimization: landing-page-optimizer with proven frameworks
✅ CTA optimization: Covered in landing-page-optimizer and cro-strategy skill
✅ Tools: Analytics, testing tools (guidance), data analysis

## Key Features

✓ **Funnel Analysis**: Identify and quantify conversion bottlenecks
✓ **A/B Testing**: Statistical sample size, significance testing
✓ **User Psychology**: Cialdini's persuasion, Fogg Behavior Model
✓ **Landing Page Best Practices**: Clarity, relevance, trust, urgency
✓ **CTA Optimization**: Copy, design, placement, color psychology
✓ **Form Optimization**: Field reduction, inline validation
✓ **Mobile CRO**: Touch-friendly, fast, simplified
✓ **Personalization**: Behavioral targeting, dynamic content

## CRO Fundamentals

### The 5 Principles of Conversion
1. **Clarity**: Instant understanding of what you offer
2. **Relevance**: Match visitor intent and expectations
3. **Value**: Clear, specific, quantified benefits
4. **Trust**: Credibility indicators, social proof, security
5. **Urgency**: Reason to act now (not later)

### A/B Testing Best Practices
- **One variable at a time**: Isolate what drives change
- **Statistical significance**: 95% confidence minimum
- **Sufficient sample size**: Power analysis for 80%+ power
- **Run full business cycles**: Account for weekly/monthly patterns
- **Document everything**: Hypothesis, results, learnings
- **Avoid peeking**: Wait for planned sample size before analysis

### Conversion Psychology (Cialdini's 6 Principles)
1. **Reciprocity**: Free trial, free content, free tools
2. **Commitment**: Small asks first, then bigger commitment
3. **Social Proof**: Testimonials, user counts, case studies
4. **Authority**: Expert endorsements, certifications, media mentions
5. **Liking**: Attractive design, friendly copy, relatability
6. **Scarcity**: Limited time offers, low stock, exclusivity

## CRO Metrics

- **Conversion Rate**: (Conversions / Visitors) × 100
- **Bounce Rate**: Visitors who leave without interaction
- **Time on Page**: Engagement indicator
- **Scroll Depth**: How far users scroll
- **Click-through Rate (CTR)**: Clicks on CTA / Page views
- **Form Abandonment**: Started but didn't complete
- **Revenue Per Visitor (RPV)**: Average revenue per visitor

## Conversion Benchmarks

- **E-commerce**: 2-3% (good), 5%+ (excellent)
- **SaaS free trial**: 15-25% (trial signup), 10-15% (trial → paid)
- **B2B lead gen**: 2-5% (demo request)
- **Email signup**: 10-15% (blog), 20-30% (gated content)
- **PPC landing page**: 5-10% (search), 2-5% (display)

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 1 comprehensive cro-strategy skill with frameworks
- ✅ 4 professional templates for funnel, A/B tests, journeys, landing pages
- ✅ Complete README with conversion benchmarks and best practices

## Common CRO Wins

### Quick Wins (High Impact, Low Effort)
- Reduce form fields (fewer = higher conversion)
- Add trust badges (security, guarantees, certifications)
- Improve CTA copy (specific action vs "Submit")
- Add social proof above fold (testimonials, user count)
- Fix mobile usability issues (thumb zone, tap targets)

### High-Impact Tests
- Value proposition clarity (headline test)
- Free trial length (7-day vs 14-day vs 30-day)
- Pricing display (monthly vs annual, tiered vs single)
- Checkout flow (one-page vs multi-step)
- CTA color/contrast (test against brand colors)

Closes #78
