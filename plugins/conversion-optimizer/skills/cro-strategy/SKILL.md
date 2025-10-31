# CRO Strategy Skill

Comprehensive patterns and best practices for Conversion Rate Optimization (CRO).

## CRO Fundamentals

### Core Metrics

**Conversion Rate**:
- Formula: (Conversions / Visitors) × 100
- Benchmark: 2-5% average, 10%+ excellent
- Segmentation: By source, device, campaign

**Bounce Rate**:
- Formula: (Single-page sessions / Total sessions) × 100
- Landing page: 40-60% typical, <40% good
- Content page: 60-80% typical

**Exit Rate**:
- Formula: (Exits from page / Page views) × 100
- Identifies abandonment points
- Different from bounce rate (bounce = first page only)

**Average Session Duration**:
- Engagement indicator
- Context-dependent (product page vs. blog)
- Correlate with conversion

**Pages Per Session**:
- User engagement depth
- Funnel progression indicator
- Higher typically better for content, not always for e-commerce

### Key Performance Indicators

- **Micro-conversions**: Newsletter signup, video view, file download
- **Macro-conversions**: Purchase, demo request, account creation
- **Revenue per visitor**: Total revenue / Total visitors
- **Cart abandonment**: (Carts created - Purchases) / Carts created × 100
- **Form completion rate**: (Completions / Starts) × 100
- **Click-through rate**: (Clicks / Impressions) × 100

---

## Funnel Analysis Methodologies

### Funnel Stages

**Awareness**: Traffic acquisition
**Interest**: Content engagement
**Desire**: Product exploration
**Action**: Conversion
**Post-conversion**: Retention, advocacy

### Drop-off Analysis

**Identify leaks**:
1. Map complete user journey
2. Calculate conversion rate each stage
3. Identify biggest drop-offs
4. Prioritize by impact (traffic × drop-off %)

**Common drop-off points**:
- Landing to product page: Unclear value prop
- Product to cart: Pricing concerns, lack of trust
- Cart to checkout: Unexpected costs, complex process
- Checkout to purchase: Payment issues, security concerns

### Funnel Visualization

**Metrics to track**:
- Unique visitors each stage
- Conversion rate each stage
- Time between stages
- Common paths and deviations

**Tools**:
- Google Analytics (Funnel Visualization, Goal Flow)
- Hotjar (Funnels)
- Mixpanel (Funnels)
- Amplitude (Behavioral Cohorts)

---

## A/B Testing Best Practices

### Hypothesis Formation

**Framework**: "If [change], then [expected outcome] because [reasoning]"

**Example**: "If we change CTA button from 'Submit' to 'Get My Free Trial', then conversion will increase by 15% because it's more specific and communicates value."

**Good hypotheses**:
- Based on data (analytics, user research)
- Specific and measurable
- One variable at a time
- Aligned with user psychology

### Test Design

**Elements to test**:
- Headlines and copy
- Call-to-action (text, color, size, placement)
- Images and videos
- Form fields (number, order, labels)
- Layout and hierarchy
- Trust signals (testimonials, badges)
- Pricing presentation
- Navigation

**Test types**:
- **A/B test**: Two versions
- **Multivariate test**: Multiple elements simultaneously
- **Split URL test**: Different pages entirely
- **Multi-page test**: Funnel optimization

### Sample Size and Duration

**Sample size calculation**:
- Baseline conversion rate
- Minimum detectable effect (MDE)
- Statistical significance (95% typical)
- Statistical power (80% typical)

**Calculator formula**:
```
n = 2 × (Zα + Zβ)² × p × (1-p) / (MDE)²
Where:
- Zα = 1.96 (for 95% confidence)
- Zβ = 0.84 (for 80% power)
- p = baseline conversion rate
- MDE = minimum detectable effect
```

**Duration considerations**:
- Run full weeks (account for weekly patterns)
- Minimum 7-14 days
- Wait for statistical significance
- Don't stop early (peeking problem)

### Statistical Significance

**P-value**: Probability results occurred by chance
- p < 0.05: Statistically significant (95% confidence)
- p < 0.01: Highly significant (99% confidence)

**Confidence intervals**: Range of likely true values
- Overlapping CIs: Not significantly different
- Non-overlapping: Significantly different

**Common mistakes**:
- Stopping test too early
- Multiple testing without correction
- Ignoring segment differences
- Declaring winner without significance
- Not accounting for seasonality

### Winner Implementation

**Validation**:
1. Verify statistical significance
2. Check consistency across segments
3. Confirm tracking is accurate
4. Monitor for novelty effect

**Rollout**:
- Gradual (10% → 50% → 100%)
- Monitor key metrics
- Keep control data for comparison
- Document learnings

---

## User Journey Mapping

### Journey Mapping Process

**Steps**:
1. **Define personas**: Who are your users?
2. **Identify touchpoints**: Where do they interact?
3. **Map current state**: What's happening now?
4. **Identify pain points**: Where do they struggle?
5. **Design future state**: How should it work?

### Touchpoint Analysis

**For each touchpoint**:
- **Goal**: What user wants to accomplish
- **Actions**: What they do
- **Emotions**: How they feel
- **Pain points**: What frustrates them
- **Opportunities**: How to improve

**Example touchpoint**:
- **Touchpoint**: Product page
- **Goal**: Understand product value and decide to buy
- **Actions**: Read description, view images, check price, read reviews
- **Emotions**: Curious → Interested → Uncertain → Confident/Skeptical
- **Pain points**: Unclear features, missing info, concerns about quality
- **Opportunities**: Better images, comparison table, video demo, guarantee

### Heatmap Analysis

**Types of heatmaps**:
- **Click maps**: Where users click
- **Scroll maps**: How far users scroll
- **Move maps**: Mouse movement (attention proxy)
- **Attention maps**: Time on page areas

**Insights from heatmaps**:
- Are CTAs being clicked?
- Do users see key content? (scroll depth)
- Are they confused? (rage clicks, erratic movement)
- What elements attract attention?

**Tools**: Hotjar, Crazy Egg, Microsoft Clarity, Lucky Orange

### Session Recording Analysis

**What to look for**:
- **Confusion**: Back-and-forth, hesitation
- **Rage clicks**: Repeated clicking
- **Dead ends**: Navigation issues
- **Form struggles**: Field errors, abandonment
- **Device issues**: Mobile usability problems

---

## Landing Page Optimization Patterns

### Above-the-Fold Elements

**Headline**:
- Clear value proposition
- Specific, not generic
- Address user pain point
- 6-12 words ideal

**Subheadline**:
- Expand on headline
- Include key benefit
- 10-20 words

**Hero image/video**:
- Show product in use
- Relevant to target audience
- High quality, fast loading
- Consider video (increase engagement by 86%)

**Call-to-action**:
- Above the fold
- Contrasting color
- Action-oriented (not "Submit")
- Visible without scrolling

### Social Proof

**Types**:
- **Customer testimonials**: Specific, authentic, with photo
- **Case studies**: Detailed success stories
- **Reviews and ratings**: Star ratings, review count
- **Client logos**: Recognizable brands
- **Social media followers**: Large following
- **Press mentions**: Media coverage
- **Awards and certifications**: Industry recognition
- **User count**: "Join 50,000+ users"

**Best practices**:
- Specific results over vague praise
- Include names and photos (credibility)
- Video testimonials (most powerful)
- Place near relevant features/CTAs
- Use real customers (never fake)

### Value Proposition

**Components**:
1. **Headline**: Main benefit
2. **Subheadline**: How you deliver it
3. **3-5 bullet points**: Key benefits
4. **Visual**: Product or benefit representation

**Formula**: "We help [target audience] [achieve goal] by [unique approach]"

**Example**: "We help small businesses double their conversion rate by identifying and fixing their top 5 funnel leaks in 30 days."

### Trust Signals

**Security indicators**:
- SSL certificate (HTTPS)
- Security badges (Norton, McAfee)
- Payment icons (Visa, PayPal)
- Privacy policy link
- Money-back guarantee
- Free trial (removes risk)

**Credibility indicators**:
- Professional design
- Error-free copy
- Contact information visible
- About page with team
- Physical address
- Phone number

---

## CTA Design and Placement

### CTA Copy

**Action-oriented verbs**:
- Get, Start, Download, Try, Join, Claim, Discover
- NOT: Submit, Click here, Learn more

**Value-focused**:
- "Get My Free Trial" > "Submit"
- "Start Saving Money" > "Sign Up"
- "Download Your Guide" > "Download"
- "Claim Your Discount" > "Click Here"

**First-person**:
- "Start My Free Trial" > "Start Free Trial"
- Studies show 90% increase in conversions

**Urgency**:
- "Get Instant Access"
- "Start Today"
- "Claim Your Spot"

### CTA Design

**Size**:
- Large enough to see (minimum 47-57px height)
- Thumb-friendly on mobile (44x44px minimum)
- Proportional to importance

**Color**:
- Contrasting with page (stands out)
- Consistent with action (green = go, red = stop/sale)
- A/B test (orange/red often high-converting)

**Shape**:
- Rounded corners (more clickable feel)
- Button vs. link (button typically 45% higher CTR)
- Adequate padding and white space

**Placement**:
- Above the fold
- Multiple placements (top, middle, bottom)
- In context (near relevant information)
- Sticky/floating (always visible)

### Number of CTAs

**Single CTA**:
- Best for focused conversion
- Remove distractions
- One clear action

**Multiple CTAs**:
- Same CTA repeated (long pages)
- Primary and secondary (e.g., "Buy" and "Learn More")
- Keep primary prominent

---

## Form Optimization

### Field Reduction

**Principle**: Only ask for essential information

**Impact**:
- Removing one field: 10% increase typical
- 3 fields vs. 10 fields: 120% increase
- Each field: 5-10% drop in completion

**Essential vs. Nice-to-have**:
- **Essential**: Email, password (signup)
- **Often unnecessary**: Phone, company size, middle name
- Ask later (progressive profiling)

**Multi-step forms**:
- Break long forms into steps
- Show progress indicator
- Start with easiest fields
- 5-7 fields per step ideal

### Progressive Disclosure

**Technique**: Show fields conditionally based on previous answers

**Benefits**:
- Reduces cognitive load
- Form appears shorter
- Relevant fields only
- Higher completion rates

**Example**:
1. "Are you a business or individual?" → Radio buttons
2. If business → Show "Company name" and "# employees"
3. If individual → Show "Occupation"

### Field Labels and Hints

**Labels**:
- Above field (not inside as placeholder)
- Clear and concise
- No jargon

**Placeholders**:
- Examples ("john@example.com")
- Format hints ("MM/DD/YYYY")
- NOT as labels (accessibility issue)

**Help text**:
- Why you need it ("We'll never share your email")
- Format requirements ("8-20 characters")
- Inline validation messages

### Error Handling

**Best practices**:
- Inline validation (real-time)
- Specific error messages ("Email must include @")
- NOT generic ("Invalid input")
- Red color for errors
- Keep entered data (don't clear)
- Focus on first error field

### Autofill and Autocomplete

**Enable browser autofill**:
- Use standard field names (email, tel, postal-code)
- Autocomplete attribute
- Reduces friction significantly

**Smart defaults**:
- Country (based on IP)
- Phone format (based on country)
- Common selections

---

## Psychology Principles

### Scarcity

**Principle**: People value items more when they're scarce

**Applications**:
- Limited quantity: "Only 3 left in stock"
- Limited time: "Sale ends in 24 hours"
- Exclusive access: "Available to first 100 customers"
- Seasonal: "Limited edition"

**Best practices**:
- Be honest (fake scarcity backfires)
- Use countdown timers
- Update in real-time
- Clear end date/quantity

### Urgency

**Principle**: People act faster when there's a deadline

**Applications**:
- Time-limited offers: "Expires tonight at midnight"
- Cart timers: "Complete purchase in 15 minutes"
- Event registration: "Early bird ends Friday"
- Seasonal: "Cyber Monday only"

**Techniques**:
- Countdown timers (visual urgency)
- Dynamic copy ("Offer ends in X hours")
- Urgent CTAs ("Claim Now", "Get Instant Access")

### Reciprocity

**Principle**: People feel obligated to give back when they receive

**Applications**:
- Free trials: Give value first
- Free tools/calculators: Useful resources
- Free shipping: Remove friction
- Bonus content: Ebooks, guides, templates
- Samples: Free taste before buying

**Best practices**:
- Give genuinely valuable content
- No strings attached (don't require much info)
- Relevant to your paid offering
- Exceed expectations

### Social Proof

**Principle**: People follow others' actions

**Types** (in order of power):
1. Testimonials with specific results
2. Case studies with data
3. Reviews and ratings (volume matters)
4. Expert endorsements
5. Celebrity endorsements
6. Wisdom of crowds ("Join 1M users")
7. Friends' actions ("Your friend bought this")

### Loss Aversion

**Principle**: People prefer avoiding losses over acquiring gains

**Applications**:
- "Don't miss out" > "Get access"
- "Avoid losing $500" > "Save $500"
- Risk reversal: Money-back guarantee
- Free trial: No commitment
- Before/after: Show the loss without product

### Authority

**Principle**: People trust and follow experts

**Applications**:
- Credentials: MD, PhD, CPA
- Awards: Industry recognition
- Press mentions: As seen in...
- Certifications: Certified by...
- Data and research: Studies show...

---

## Page Speed Optimization Impact

### Speed and Conversion Correlation

**Research findings**:
- 1 second delay: 7% reduction in conversions
- 2 second delay: 87% of users abandon
- 3 seconds: 40% bounce rate
- 5 seconds: 90% bounce rate

**Google benchmarks**:
- 0-2 seconds: Excellent
- 2-3 seconds: Good
- 3-5 seconds: Poor
- 5+ seconds: Very poor

### Speed Optimization Tactics

**Critical rendering path**:
- Minimize render-blocking resources
- Inline critical CSS
- Defer non-critical JavaScript
- Lazy load images below fold

**Resource optimization**:
- Image compression (WebP format)
- Minify CSS/JS
- Enable gzip/brotli compression
- Use CDN
- Reduce HTTP requests

**Perceived performance**:
- Skeleton screens (loading placeholder)
- Progressive loading (content first, then enhancements)
- Optimistic UI (assume success)
- Instant feedback (button state change)

### Core Web Vitals

**LCP (Largest Contentful Paint)**:
- Goal: <2.5 seconds
- Optimize large images
- Reduce server response time
- Use preload for key resources

**FID (First Input Delay)**:
- Goal: <100ms
- Minimize JavaScript execution
- Break up long tasks
- Use web workers

**CLS (Cumulative Layout Shift)**:
- Goal: <0.1
- Include size attributes on images/videos
- Don't insert content above existing
- Use transform animations (not width/height)

---

## Mobile Optimization

### Mobile-Specific Considerations

**Touch targets**:
- Minimum 44x44px (Apple guideline)
- 48x48dp (Android guideline)
- Adequate spacing (prevent mis-taps)
- Larger for primary CTAs

**Thumb zone**:
- Easy reach: Bottom center/corners
- Stretch reach: Top corners
- Place primary actions in easy reach

**Text readability**:
- Minimum 16px font size
- Line height 1.5x font size
- Adequate contrast (4.5:1 minimum)
- Short line length (50-75 characters)

### Mobile Forms

**Optimization**:
- Large input fields (minimum 44px height)
- Appropriate keyboards (type="email", "tel", "number")
- Auto-zoom disabled on focus
- Vertical layout (one column)
- Minimal required fields
- Auto-advance (credit card fields)

### Mobile Page Speed

**Critical**:
- 3G network consideration
- Image optimization (critical)
- Lazy loading (essential)
- Reduce payloads
- AMP pages (for content)

---

## CRO Testing Tools

### Google Optimize (Free/Sunset 2023)

**Note**: Sunsetted Sept 2023. Alternatives below.

### VWO (Visual Website Optimizer)

**Features**:
- A/B testing
- Multivariate testing
- Split URL testing
- Heatmaps
- Session recordings
- Form analytics
- Surveys

**Pricing**: $199+/month

### Optimizely

**Features**:
- A/B testing
- Multivariate testing
- Personalization
- Feature flags
- Recommendations
- Full stack (backend testing)

**Best for**: Enterprise
**Pricing**: Custom (typically $50k+/year)

### Convert.com

**Features**:
- A/B testing
- Split testing
- Multivariate testing
- GDPR compliant
- Privacy-focused
- No flicker

**Pricing**: $699+/month

### Microsoft Clarity (Free)

**Features**:
- Heatmaps
- Session recordings
- Rage clicks detection
- Dead clicks
- Excessive scrolling
- Quick back

**Best for**: Session analysis and heatmaps

### Hotjar

**Features**:
- Heatmaps
- Session recordings
- Surveys
- Feedback widgets
- Form analytics

**Pricing**: Free (basic), $39+/month

### AB Tasty

**Features**:
- A/B testing
- Personalization
- Recommendations
- Feature management
- Split testing

**Pricing**: Custom

---

## CRO Process Framework

### 1. Research Phase

**Quantitative data**:
- Google Analytics (traffic, behavior, conversions)
- Funnel analysis (drop-off points)
- Heatmaps (attention and interaction)
- Form analytics (field abandonment)

**Qualitative data**:
- User interviews (why they do/don't convert)
- Surveys (exit intent, on-page)
- Session recordings (observe behavior)
- User testing (task completion)
- Customer support tickets (pain points)

### 2. Hypothesis Generation

**Prioritization framework (ICE)**:
- **Impact**: How much will it improve conversion? (1-10)
- **Confidence**: How sure are we? (1-10)
- **Ease**: How easy to implement? (1-10)
- **Score**: (Impact × Confidence × Ease) / 3

**Alternative (PIE)**:
- **Potential**: How much improvement possible? (1-10)
- **Importance**: How valuable is the page? (1-10)
- **Ease**: How hard to implement? (1-10)

### 3. Test Design

**Create variations**:
- Control (current version)
- Variant(s) (changes based on hypothesis)
- Document changes clearly

**Set up tracking**:
- Goal conversions
- Micro-conversions
- Revenue (if applicable)
- Segment tracking

### 4. Run Test

**Validation**:
- QA all variants
- Test tracking
- Preview mode
- Cross-browser/device testing

**Monitoring**:
- Check daily (don't peak at results)
- Ensure even traffic split
- Watch for anomalies
- Document any issues

### 5. Analysis

**Statistical validation**:
- Confidence level (95%+)
- Statistical significance (p < 0.05)
- Sufficient sample size
- Consistent across segments

**Segment analysis**:
- Desktop vs. mobile
- New vs. returning
- Traffic source
- Geography
- Device type

### 6. Implementation

**Winner validated**:
- Implement changes permanently
- Document learnings
- Share with team
- Monitor post-test

**No clear winner**:
- Document learnings
- Generate new hypothesis
- Consider different approach
- Test again

### 7. Iteration

**Continuous improvement**:
- Always have test running
- Build on learnings
- Test new pages/funnels
- Refine over time

---

## Quick Reference: CRO Checklist

### Landing Page
- [ ] Clear, specific headline (value proposition)
- [ ] Compelling subheadline
- [ ] Relevant hero image/video
- [ ] CTA above the fold
- [ ] Social proof (testimonials, logos)
- [ ] Benefits-focused copy
- [ ] Trust signals (security badges, guarantee)
- [ ] Mobile-optimized
- [ ] Fast loading (<3 seconds)
- [ ] No navigation distractions (dedicated landing page)

### Forms
- [ ] Minimal required fields
- [ ] Clear labels (above fields)
- [ ] Helpful placeholder examples
- [ ] Inline validation
- [ ] Specific error messages
- [ ] Progress indicator (multi-step)
- [ ] Privacy reassurance
- [ ] Visible submit button
- [ ] Mobile-friendly inputs
- [ ] Autofill enabled

### CTAs
- [ ] Action-oriented copy
- [ ] Value-focused (not generic)
- [ ] Contrasting color
- [ ] Large enough to see/tap
- [ ] White space around
- [ ] Multiple placements (long pages)
- [ ] Consistent throughout

### A/B Testing
- [ ] Data-driven hypothesis
- [ ] One variable at a time
- [ ] Sufficient sample size calculated
- [ ] Run full weeks (7-14 days minimum)
- [ ] Statistical significance achieved
- [ ] Segment analysis completed
- [ ] Winner validated before implementation

---

**Version**: 1.0
**Last Updated**: January 2025
**Research Sources**: ConversionXL, CXL Institute, VWO, Optimizely, Nielsen Norman Group
