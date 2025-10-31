# Email Copywriting Skill

**Production-tested patterns for high-converting email copy, subject lines, and CTAs**

This skill provides comprehensive best practices for writing email marketing copy that drives opens, clicks, and conversions based on proven patterns from successful campaigns.

---

## Table of Contents

1. [Subject Line Best Practices](#subject-line-best-practices)
2. [Preview Text Optimization](#preview-text-optimization)
3. [Email Body Copywriting](#email-body-copywriting)
4. [Call-to-Action (CTA) Mastery](#call-to-action-cta-mastery)
5. [Personalization Strategies](#personalization-strategies)
6. [Copywriting Frameworks](#copywriting-frameworks)
7. [Email Types and Templates](#email-types-and-templates)
8. [Deliverability Best Practices](#deliverability-best-practices)
9. [Mobile Optimization](#mobile-optimization)
10. [Testing and Optimization](#testing-and-optimization)

---

## Subject Line Best Practices

### Length Guidelines

**Optimal length**: 30-50 characters (6-10 words)
- Mobile preview shows ~30-40 characters
- Desktop shows ~60-70 characters
- Front-load important words

**Examples**:
```
✅ "Your exclusive 20% discount expires tonight"  (47 chars)
✅ "New arrivals you'll love, {{first_name}}"     (37 chars + personalization)
✅ "Your cart misses you (+ 15% off inside)"      (42 chars)

❌ "We wanted to reach out to let you know about our amazing new product launch that we think you'll really enjoy" (too long, gets cut off)
```

### Proven Subject Line Formulas

**1. Benefit-Focused**
```
"Get [benefit] in [timeframe]"
"[Number] ways to [achieve goal]"
"How to [solve problem] without [pain point]"

Examples:
- "Get 50% more leads in 30 days"
- "7 ways to boost email open rates"
- "How to grow revenue without increasing ad spend"
```

**2. Curiosity-Driven**
```
"The [surprising thing] about [topic]"
"Why [unexpected statement]"
"You won't believe [intriguing claim]"

Examples:
- "The surprising truth about email marketing"
- "Why top performers send fewer emails"
- "You won't believe these conversion rates"
```

**3. Urgency-Based**
```
"[Time limit] to [benefit]"
"Last chance: [offer]"
"Only [number] left for [product]"

Examples:
- "48 hours to claim your bonus"
- "Last chance: Free shipping ends tonight"
- "Only 5 spots left for our masterclass"
```

**4. Question-Based**
```
"Are you making this [mistake]?"
"What's your [metric/goal]?"
"Ready to [achieve outcome]?"

Examples:
- "Are you making this email mistake?"
- "What's your email conversion rate?"
- "Ready to 3x your productivity?"
```

**5. Social Proof**
```
"[Number] customers already [action]"
"Join [number] [people] who [benefit]"
"How [person/company] achieved [result]"

Examples:
- "10,000 marketers already upgraded"
- "Join 50K+ entrepreneurs who trust us"
- "How Shopify increased sales by 127%"
```

**6. Personalized**
```
"{{first_name}}, [benefit/question]"
"Your [personalized content] is ready"
"Based on your [behavior], you'll love this"

Examples:
- "Sarah, your custom report is ready"
- "Your abandoned cart is waiting (+ surprise inside)"
- "Based on your last purchase, you'll love these"
```

**7. News/Update**
```
"Introducing: [new feature/product]"
"[Product] just got better"
"What's new in [month/quarter]"

Examples:
- "Introducing: AI-powered analytics"
- "Your dashboard just got 10x faster"
- "What's new in our Spring collection"
```

### Subject Line Power Words

**Urgency**: Now, Today, Urgent, Hurry, Fast, Quick, Limited, Ending, Last chance, Expires
**Exclusivity**: Exclusive, Members only, VIP, Private, Invitation, Select, Premium
**Curiosity**: Secret, Revealed, Discover, Unlock, Hidden, Surprising, Shocking
**Value**: Free, Bonus, Extra, Save, Discount, Deal, Offer, Gift
**Action**: Get, Grab, Claim, Download, Join, Start, Try, Learn

### Subject Line Red Flags (Spam Triggers)

**Avoid or minimize**:
- ❌ ALL CAPS
- ❌ Excessive punctuation!!! ???
- ❌ Spammy words: FREE!!!, Guarantee, Act now, Click here, Winner
- ❌ Multiple currencies: $$$, €€€
- ❌ RE: or FWD: (when not reply/forward)
- ❌ Excessive emojis (>2)

**Use sparingly**:
- ⚠️ Free (combine with other words: "Free guide to...")
- ⚠️ Discount/Sale (be specific: "20% off" not "HUGE SALE")
- ⚠️ Emojis (1-2 max, must be relevant)

---

## Preview Text Optimization

### What is Preview Text?

The 40-100 character snippet shown after subject line in inbox. Critical for open rates.

### Best Practices

**1. Complement, Don't Repeat**
```
✅ Subject: "Your exclusive 20% discount inside"
   Preview: "Plus free shipping on orders over $50 | Shop now"

❌ Subject: "Your exclusive 20% discount inside"
   Preview: "You have an exclusive 20% discount" (redundant)
```

**2. Add Context or Urgency**
```
✅ Subject: "New arrivals are here"
   Preview: "Shop the collection before it sells out | Limited quantities"

✅ Subject: "{{first_name}}, your report is ready"
   Preview: "See how you compare to industry benchmarks | 5-min read"
```

**3. Include CTA Preview**
```
✅ Subject: "Time to upgrade your plan?"
   Preview: "Get 30% off annual plans this week only | View plans →"
```

**4. Avoid Default Text**
```
❌ "View this email in browser" (wasted preview space)
❌ "If you can't see this email..." (assumes failure)
❌ Company boilerplate text
```

### Implementation

```html
<!-- Preheader text (hidden in email, shown in preview) -->
<div style="display:none;font-size:1px;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;">
    Your compelling preview text goes here. Add extra spaces or invisible characters to fill preview pane if needed.
    ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌
</div>
```

---

## Email Body Copywriting

### The AIDA Framework

**Attention** → **Interest** → **Desire** → **Action**

```
[ATTENTION] Subject line + Hero section
↓
[INTEREST] Hook them in first 2 sentences
↓
[DESIRE] Benefits, social proof, urgency
↓
[ACTION] Clear, compelling CTA
```

### Opening Lines

**First 2 sentences are critical** - Most readers decide whether to continue here.

**Strong Opening Patterns**:

1. **Question Hook**
   ```
   "What if you could double your email revenue without sending more emails?

   Our top customers are doing exactly that with this one strategy."
   ```

2. **Problem Statement**
   ```
   "Your email list is growing, but your revenue isn't.

   You're not alone—78% of marketers face this exact challenge."
   ```

3. **Benefit Delivery**
   ```
   "In the next 5 minutes, you'll discover the exact template that generated
   $2.4M in revenue for our clients last quarter."
   ```

4. **Surprise/Curiosity**
   ```
   "We analyzed 10,000 email campaigns and found something shocking:

   Shorter emails don't always perform better. Here's what actually works..."
   ```

5. **Direct Value**
   ```
   "Your personalized report is ready, {{first_name}}.

   Here's how your performance compares to industry leaders:"
   ```

### Body Copy Best Practices

**1. Scannable Structure**
```
✅ Short paragraphs (2-3 sentences max)
✅ Bullet points for lists
✅ Subheadings to break sections
✅ White space between sections
✅ Bold for emphasis (sparingly)

❌ Long text blocks
❌ Dense paragraphs
❌ Wall of text
```

**2. Benefit-Focused Language**
```
✅ "You'll save 10 hours per week"
✅ "Increase your conversion rate by 35%"
✅ "Get results in 24 hours"

❌ "Our platform has advanced features"
❌ "We offer comprehensive solutions"
❌ "Industry-leading technology"
```

**3. Show, Don't Just Tell**
```
✅ "Sarah increased her email revenue from $10K to $47K in 60 days using this strategy."

❌ "Our strategy can significantly improve your results."
```

**4. Conversational Tone**
```
✅ "You're probably wondering..."
✅ "Here's the thing..."
✅ "Let me show you..."
✅ "Quick question..."

❌ "Pursuant to our previous communication..."
❌ "We are pleased to announce..."
❌ Overly formal corporate speak
```

**5. Second Person ("You")**
```
✅ "You'll get instant access to..."
✅ "Your business will benefit from..."

❌ "Users will receive..."
❌ "Customers can access..."
```

### Reading Level

**Target: 8th grade reading level or lower**

Tools: Hemingway Editor, Grammarly, Readable.com

**Simple is better**:
```
✅ "Use this template to write better emails"
❌ "Utilize this template to optimize your email communication efficacy"

✅ "Get started in 5 minutes"
❌ "Commence implementation in a minimal timeframe"
```

---

## Call-to-Action (CTA) Mastery

### CTA Best Practices

**1. Action-Oriented Verbs**
```
✅ Start, Get, Download, Claim, Join, Discover, Learn, Try, Shop, See
❌ Click here, Submit, Enter, Go
```

**2. Benefit-Focused**
```
✅ "Get My Free Guide"
✅ "Start Saving 10 Hours/Week"
✅ "See My Personalized Plan"
✅ "Claim My 20% Discount"

❌ "Click Here"
❌ "Submit"
❌ "Learn More" (vague)
```

**3. Create Urgency**
```
✅ "Claim Your Spot (Only 5 Left)"
✅ "Get 20% Off - Expires Tonight"
✅ "Download Now - Limited Time"
```

**4. Remove Friction**
```
✅ "Start Free Trial (No Credit Card)"
✅ "Get Instant Access"
✅ "Download Free Guide (No Signup)"
```

**5. Make it Personal**
```
✅ "Show Me My Results"
✅ "Get My Custom Plan"
✅ "Calculate My Savings"
```

### CTA Placement

**Primary CTA**: Above the fold + repeat 2-3 times in longer emails
**Secondary CTA**: Different, lower-commitment action

```
[Hero Section]
→ Primary CTA Button

[Body Content]
→ Benefits, social proof

[Mid-Email]
→ Primary CTA (repeated)

[Additional Content]
→ More details, FAQ

[Footer Area]
→ Primary CTA (final push)
→ Secondary CTA (lower commitment)
```

### Button Design

**Size**: Minimum 44px height (mobile touch target)
**Color**: High contrast with background
**Text**: 2-5 words, action-oriented
**Spacing**: Generous white space around button

```html
<!-- Good CTA Button -->
<table role="presentation" cellspacing="0" cellpadding="0">
  <tr>
    <td align="center" style="border-radius: 4px; background-color: #FF6B6B;">
      <a href="{{link}}" target="_blank" style="
        display: inline-block;
        padding: 16px 32px;
        font-family: Arial, sans-serif;
        font-size: 18px;
        color: #ffffff;
        text-decoration: none;
        font-weight: bold;
      ">
        Get Started Free
      </a>
    </td>
  </tr>
</table>
```

### CTA Copy Formulas

**1. [Verb] + [Benefit]**
```
"Download Free Guide"
"Start Saving Time"
"Get 20% Off"
```

**2. [Verb] + [Possessive] + [Benefit]**
```
"Claim My Discount"
"See My Results"
"Get My Free Trial"
```

**3. [Verb] + [Urgency]**
```
"Join Now - Limited Spots"
"Shop Sale - Ends Tonight"
"Register Today"
```

**4. [Result-Oriented]**
```
"Yes, I Want Better Results"
"Show Me How to Save Time"
"I'm Ready to Grow"
```

---

## Personalization Strategies

### Personalization Tokens

**Basic**:
```
{{first_name}}
{{last_name}}
{{email}}
{{company}}
```

**Behavioral**:
```
{{last_purchase_product}}
{{last_purchase_date}}
{{cart_items}}
{{browsing_history}}
{{download_name}}
```

**Segmentation**:
```
{{industry}}
{{company_size}}
{{location}}
{{job_title}}
{{signup_date}}
```

### Personalization Best Practices

**1. Always Use Fallbacks**
```
✅ "Hi {{first_name|there}},"
✅ "Hey {{first_name|friend}},"

❌ "Hi {{first_name}}," (could show "Hi ," if missing)
```

**2. Natural Integration**
```
✅ "Based on your interest in {{topic}}, you might like..."
✅ "Since you downloaded {{resource}}, here's the next step..."

❌ "Hello {{first_name}} {{last_name}} from {{company}} in {{city}}, {{state}}"
(over-personalization feels creepy)
```

**3. Dynamic Content Blocks**
```
IF {{location}} = "New York"
  → Show NYC event invitation

IF {{last_purchase}} < 30 days ago
  → Show product tips
ELSE
  → Show new product recommendations
```

**4. Behavioral Triggers**
```
{{cart_items}} abandoned
  → "You left {{product_name}} in your cart"

{{download_name}} downloaded
  → "Here's how to use {{resource_name}}"

{{webinar_name}} registered
  → "Your {{webinar_name}} starts in 24 hours"
```

---

## Copywriting Frameworks

### 1. PAS (Problem-Agitate-Solution)

```
[PROBLEM]
"Your email open rates are stuck at 15%."

[AGITATE]
"While your competitors are seeing 30%+ opens and generating 2x more revenue
from the same list size. Every day you wait, you're leaving money on the table."

[SOLUTION]
"Our proven subject line framework has helped 5,000+ marketers double their
open rates in 30 days. Here's how it works..."

[CTA]
"Get the Framework Free →"
```

### 2. BAB (Before-After-Bridge)

```
[BEFORE]
"You're spending 10+ hours per week manually segmenting email lists."

[AFTER]
"Imagine having your entire list automatically segmented based on behavior,
giving you back those 10 hours while increasing engagement by 40%."

[BRIDGE]
"Our AI-powered segmentation does exactly that. Set it up once, and it runs
on autopilot forever."

[CTA]
"Start Free Trial →"
```

### 3. FAB (Features-Advantages-Benefits)

```
[FEATURE]
"Our platform includes AI-powered send time optimization."

[ADVANTAGE]
"It analyzes when each subscriber is most likely to open emails."

[BENEFIT]
"So your emails land at the perfect moment, boosting your open rates by 35%
without any extra work from you."

[CTA]
"See It In Action →"
```

### 4. The 4 Ps (Problem-Promise-Proof-Push)

```
[PROBLEM]
"Cart abandonment is costing you 70% of potential sales."

[PROMISE]
"Recover 30-40% of abandoned carts on autopilot."

[PROOF]
"Over 2,000 Shopify stores use our abandoned cart sequences to generate an
average of $15K additional monthly revenue. Here's how Sarah from Austin
recovered $47K in just 60 days..."
[Include case study, testimonial, or data]

[PUSH]
"Start recovering lost revenue today."
[CTA] "Install Free App →"
```

### 5. PASTOR Framework

```
[PROBLEM]
Identify the pain point

[AMPLIFY]
Make it vivid and real

[STORY]
Share relatable story or case study

[TRANSFORMATION]
Show the after state

[OFFER]
Present your solution

[RESPONSE]
Clear call-to-action
```

---

## Email Types and Templates

### 1. Welcome Email

**Purpose**: Set expectations, deliver quick win, build relationship

**Template**:
```
Subject: Welcome to [Company] - Here's what's next

Hi {{first_name}},

Welcome! We're excited to have you.

Here's what you can expect from us:
✓ [Benefit 1]
✓ [Benefit 2]
✓ [Benefit 3]

To get you started, here's [quick win/resource]:
→ [Link to valuable content]

[Optional: What to do next]
The best way to get results fast is to [action].

[CTA Button]

Questions? Just reply to this email.

Cheers,
[Name/Team]
```

### 2. Promotional Email

**Purpose**: Drive sales with clear offer

**Template**:
```
Subject: [Specific discount]% off [product] - [Time limit]

{{first_name}}, we have something special for you.

[BENEFIT-FOCUSED OPENING]
Get [benefit] with [specific discount] off [product].

Here's what you get:
• [Benefit 1]
• [Benefit 2]
• [Benefit 3]

[SOCIAL PROOF]
"[Testimonial]" - [Customer Name]

[URGENCY]
This offer expires [specific time/date].

[CTA Button: "Shop Now & Save [X]%"]

[Trust signals: Free shipping, money-back guarantee, etc.]
```

### 3. Newsletter/Content Email

**Purpose**: Provide value, build engagement, subtle promotion

**Template**:
```
Subject: [Intriguing content headline]

Hi {{first_name}},

[HOOK - Interesting insight or question]

This week's insights:

1. [Tip/Article 1 with brief description]
   → [Read more link]

2. [Tip/Article 2 with brief description]
   → [Read more link]

3. [Resource/Tool recommendation]
   → [Check it out link]

[FEATURED CONTENT]
📌 Don't miss: [Main article title]
[2-3 sentence description creating curiosity]
→ [Read full article]

[SOFT CTA - Related product/service]
P.S. If you enjoyed this, you might like [product/service].
[Learn more link]
```

### 4. Cart Abandonment

**Purpose**: Recover lost sales

**Template**:
```
Subject: You left something behind ({{product_name}})

Hi {{first_name}},

You left these items in your cart:

[Product Image]
{{product_name}}
{{price}}

[REMOVE OBJECTION]
• Free shipping on orders over $50
• 30-day money-back guarantee
• Secure checkout

[OPTIONAL INCENTIVE - Email 2 or 3]
Complete your order now and get 15% off with code: COMEBACK15

[CTA Button: "Complete My Order"]

Questions? We're here to help: [support email/chat link]
```

### 5. Re-engagement

**Purpose**: Win back inactive subscribers

**Template**:
```
Subject: We miss you, {{first_name}}

{{first_name}}, we noticed you haven't [action] in a while.

We miss having you around!

[WHAT THEY'RE MISSING]
Here's what's new since you last visited:
• [Update 1]
• [Update 2]
• [Update 3]

[INCENTIVE]
To welcome you back, here's [special offer/resource].

[CTA: "Yes, I Want Back In"]

[ALTERNATIVE CTA]
Not interested? [Update your preferences] or [unsubscribe].

We only want to send emails you love.
```

---

## Deliverability Best Practices

### Spam Score Reduction

**Avoid Spam Triggers**:
```
❌ FREE!!! (all caps with excessive punctuation)
❌ Click here now!!!
❌ Act now or lose out forever
❌ Guarantee, winner, congratulations (when not genuine)
❌ Viagra, pills, drugs, casino (unless relevant business)
❌ $$$, €€€ (excessive currency symbols)
❌ ALL CAPS SUBJECT LINES
```

**Better Alternatives**:
```
✅ "Free guide to email marketing"
✅ "Start your free trial"
✅ "Limited-time offer: 20% off"
✅ "Get started today"
```

### Text-to-Image Ratio

**Target: 60:40 text to images** (or higher text ratio)

- Too many images = spam filter flag
- Image-only emails = accessibility issues
- Always include alt text for images

### Email Authentication

Ensure these are configured:
- SPF (Sender Policy Framework)
- DKIM (DomainKeys Identified Mail)
- DMARC (Domain-based Message Authentication)

### List Hygiene

- Remove hard bounces immediately
- Remove inactive subscribers (180-365 days no engagement)
- Double opt-in for new subscribers
- Easy unsubscribe process

---

## Mobile Optimization

**70%+ of emails are opened on mobile** - Mobile-first design is critical.

### Mobile Copywriting

**1. Front-Load Important Info**
```
✅ "20% off ends tonight - Shop now"
❌ "As a valued customer, we wanted to let you know about our special
    promotional offer that gives you 20% off..."
```

**2. Shorter Subject Lines**
```
✅ 30-40 characters for mobile
✅ Put key info first
```

**3. Shorter Paragraphs**
```
✅ 1-2 sentences per paragraph on mobile
✅ Plenty of white space
```

**4. Prominent CTAs**
```
✅ Minimum 44px touch target
✅ Full-width buttons work well on mobile
✅ Plenty of padding around tappable elements
```

**5. Scannable Content**
```
✅ Bullet points
✅ Emojis as visual breaks (sparingly)
✅ Short sentences
✅ Clear hierarchy (headlines, subheads)
```

---

## Testing and Optimization

### What to Test

**High-Impact Elements**:
1. Subject lines (highest impact on opens)
2. Preview text
3. CTA copy and design
4. Email length
5. Personalization
6. Send time
7. From name

**Testing Priority**:
```
1. Subject line variations (test first)
2. Primary CTA copy
3. Email structure (short vs. long)
4. Personalization effectiveness
5. Visual elements
```

### Subject Line Testing

**Test These Variables**:
```
✅ Length (short vs. long)
✅ Personalization (with vs. without name)
✅ Emoji (with vs. without)
✅ Question vs. statement
✅ Benefit vs. curiosity vs. urgency
✅ Numbers/statistics
```

**Example Test**:
```
Control: "New arrivals just dropped"
Variant A: "{{first_name}}, new arrivals you'll love"
Variant B: "20% off new arrivals - 48 hours only"
Variant C: "Which new arrival is your favorite? 🛍️"
```

### Copy Testing Best Practices

- Test ONE variable at a time
- Sufficient sample size (1,000+ per variant minimum)
- Run for full week to account for day-of-week variations
- Statistical significance (95% confidence)
- Document learnings for future campaigns

---

## Quick Reference Checklist

**Before Sending Every Email**:

**Subject Line**:
- [ ] 30-50 characters
- [ ] Front-loaded with key info
- [ ] No excessive caps or punctuation
- [ ] Personalization (if appropriate)
- [ ] Creates curiosity, urgency, or clear benefit
- [ ] Tested variants ready (A/B test)

**Preview Text**:
- [ ] Complements subject line
- [ ] 40-100 characters
- [ ] Not redundant with subject
- [ ] Adds context or urgency

**Body Copy**:
- [ ] Strong opening hook (first 2 sentences)
- [ ] Benefit-focused (not feature-focused)
- [ ] Scannable (short paragraphs, bullets, white space)
- [ ] 8th grade reading level or lower
- [ ] Conversational tone
- [ ] Personalization tokens have fallbacks
- [ ] Mobile-optimized (short paragraphs)

**CTA**:
- [ ] Action-oriented verb
- [ ] Benefit-focused
- [ ] Stands out visually
- [ ] Minimum 44px touch target
- [ ] Repeated 2-3 times in longer emails
- [ ] Low friction (addresses objections)

**Technical**:
- [ ] Plain text version included
- [ ] All images have alt text
- [ ] Links tested and working
- [ ] Personalization tokens tested
- [ ] Mobile preview checked
- [ ] Spam score checked (<5/10)
- [ ] Unsubscribe link present
- [ ] Physical address included (CAN-SPAM)

**Deliverability**:
- [ ] Text-to-image ratio > 60:40
- [ ] No spam trigger words (excessive)
- [ ] Proper HTML structure
- [ ] From name recognizable
- [ ] Reply-to address functional

---

## Performance Benchmarks

### Email Metrics by Industry

**Average Open Rates**:
- B2B: 15-25%
- B2C Retail: 18-25%
- SaaS: 20-25%
- Non-profit: 20-28%

**Average Click Rates**:
- B2B: 2-4%
- B2C Retail: 2-3%
- SaaS: 3-5%
- Non-profit: 2-4%

**Average Conversion Rates**:
- Promotional: 1-3%
- Cart Abandonment: 4-8%
- Welcome Series: 3-7%

### What Good Looks Like

**Excellent Performance**:
- Open rate: >30%
- Click rate: >5%
- Click-to-open rate: >15%
- Unsubscribe rate: <0.5%
- Spam complaints: <0.1%

---

## Resources

### Copywriting References
- "Everybody Writes" by Ann Handley
- "The Copywriter's Handbook" by Robert Bly
- Copyhackers.com tutorials
- Swipe files from top brands

### Email Testing Tools
- Litmus (email preview and testing)
- Email on Acid (rendering tests)
- Mail Tester (spam score)
- Hemingway Editor (readability)
- Grammarly (grammar and clarity)

### Inspiration Sources
- Really Good Emails (reallygoodemails.com)
- Milled (milled.com)
- Competitor emails (subscribe to competitors)
- Industry leaders' campaigns

---

**This skill should be read before creating any email campaign to ensure best practices are followed.**
