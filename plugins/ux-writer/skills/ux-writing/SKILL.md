# UX Writing Skill

Expert patterns and best practices for creating effective interface copy, error messages, onboarding flows, and accessible content.

## Table of Contents
1. [Core Principles](#core-principles)
2. [Microcopy Patterns](#microcopy-patterns)
3. [Error Messages](#error-messages)
4. [Onboarding](#onboarding)
5. [Accessibility](#accessibility)
6. [Voice & Tone](#voice--tone)
7. [Content Patterns](#content-patterns)

## Core Principles

### Clarity Over Cleverness
**Priority**: Users must understand immediately, without thinking.

```
❌ "Oopsie daisy! Something went sideways."
✅ "We couldn't save your changes. Check your connection and try again."
```

**Rules**:
- Use simple, common words (8th-grade reading level)
- One idea per sentence
- Active voice over passive
- Specific over vague
- Front-load important information

### Brevity Without Loss
**Every word must earn its place.**

```
❌ "In order to proceed with the creation of your account, you'll need to provide us with your email address."
✅ "Enter your email to create your account."
```

**Techniques**:
- Remove filler words: "in order to" → "to", "utilize" → "use"
- Delete redundancy: "advance planning" → "planning"
- Use contractions when friendly: "You'll" not "You will"
- Cut adverbs: "very important" → "critical"

### User-Centered Language
**Write from the user's perspective, not the system's.**

```
System perspective (❌): "The system requires authentication"
User perspective (✅): "Sign in to continue"

System perspective (❌): "Invalid credentials provided"
User perspective (✅): "We don't recognize that email and password combination"
```

**Patterns**:
- Use "you/your" (not "the user")
- Focus on user goals, not system processes
- Explain benefits, not features
- Match user's mental model and vocabulary

### Consistency
**Same action = same label everywhere**

If you call it "Delete" in one place, don't call it "Remove" elsewhere (unless they're different actions).

**Consistency applies to**:
- Terminology (pick one word per concept)
- Capitalization (title case vs sentence case)
- Punctuation (periods in tooltips?)
- Tone (formal vs casual)
- Button patterns (verb-first)

## Microcopy Patterns

### Button Labels

**Rules**:
1. Start with verb (action word)
2. Be specific (what will happen)
3. Avoid generic labels when possible
4. Match button style to action

```
Primary buttons (main action):
✅ "Create account"
✅ "Save changes"
✅ "Continue to payment"
❌ "Submit"
❌ "OK"

Secondary buttons (alternate path):
✅ "Cancel"
✅ "Go back"
✅ "Skip for now"

Destructive buttons (dangerous):
✅ "Delete project"
✅ "Remove card"
✅ "Permanently delete"
❌ "Delete" (not specific enough)
```

**Loading states**:
```
❌ "Loading..."
✅ "Saving..." / "Creating account..." / "Processing payment..."
```

### Form Labels

**Best practices**:
- Use nouns or questions
- Place above field (not beside)
- Mark required/optional clearly
- Include helpful context

```
❌ "Name:" (colon unnecessary)
✅ "Full name"

❌ "Email *" (asterisk meaning unclear)
✅ "Email address (required)"
✅ "Phone number (optional)"

Question format (more conversational):
✅ "What's your email address?"
✅ "How should we contact you?"
```

### Placeholders

**Use for examples, not instructions**

```
❌ "Enter your email address" (That's what the label is for)
✅ "name@company.com"

❌ "YYYY-MM-DD" (too cryptic)
✅ "2024-01-15"

Good placeholders:
- Phone: "(555) 123-4567"
- URL: "https://example.com"
- Search: "Search products, orders, or customers"
```

**Warning**: Don't rely on placeholders alone—they disappear on input and fail accessibility.

### Tooltips

**When to use**:
- Add context (not repeat visible label)
- Explain consequences
- Show keyboard shortcuts
- Clarify unfamiliar terms

```
Visible label: "Auto-save"
Tooltip: "Changes save automatically every 30 seconds"

Visible label: "Private"
Tooltip: "Only you and people you invite can see this"

Icon button: [Heart icon]
Tooltip: "Add to favorites (⌘D)"
```

**Rules**:
- 1-2 sentences maximum
- Don't repeat the visible label
- Include keyboard shortcut if applicable
- Make dismissible/hoverable
- Don't put critical info in tooltips (many users won't see them)

### Empty States

**Framework**: Explain + Encourage + Action

```
Structure:
1. Headline: What's missing (positive frame)
2. Explanation: Why it matters / what goes here
3. Primary action: Fill this state
4. Secondary: Alternative or help

Example:
[Illustration]
"No projects yet"
"Projects help you organize tasks and collaborate with your team."
[Create your first project]
[Learn about projects]
```

**Tone**: Encouraging, never condescending
```
❌ "Nothing to see here"
❌ "This page is empty"
✅ "You haven't saved any items yet"
✅ "Your notifications will appear here"
```

### Notifications & Toasts

**Types**:
1. **Success**: Confirm action completed
2. **Info**: Helpful information
3. **Warning**: Something needs attention
4. **Error**: Action failed

```
Success (brief confirmation):
✅ "Project created"
✅ "Changes saved"
✅ "File uploaded"

Info (useful context):
✅ "New features are available. Refresh to see them."
✅ "You have 3 unsaved drafts"

Warning (needs action soon):
✅ "Your trial ends in 3 days. Upgrade to keep access."
✅ "You're viewing an old version of this file"

Error (action failed):
✅ "Couldn't upload file. Check your connection and try again."
```

**Rules**:
- Be concise (read in 2-3 seconds)
- Include an action when possible
- Use appropriate icon/color
- Don't auto-dismiss errors
- Limit frequency (max 1-2 toasts at once)

## Error Messages

### The 3-Part Formula
Every error message answers:
1. **What happened?** (The problem)
2. **Why?** (Reason - when helpful)
3. **How to fix?** (Solution)

```
Example:
"We couldn't save your document [what]. You're offline [why]. Your work is saved locally—reconnect to sync [how to fix]."
```

### Error Types

#### Validation Errors (User input issues)
```
❌ "Invalid email"
✅ "Please enter a valid email address (e.g., name@company.com)"

❌ "Password requirements not met"
✅ "Your password must be at least 8 characters with 1 number and 1 special character"

❌ "Field cannot be empty"
✅ "We need your phone number to send order updates"
```

#### System Errors (Technical failures)
```
❌ "Error 500: Internal server error"
✅ "Something went wrong on our end. We've been notified and are fixing it. Please try again in a few minutes."

❌ "Request timed out"
✅ "This is taking longer than expected. Your work is saved—try refreshing the page or come back in a few minutes."

❌ "Database connection failed"
✅ "We're having trouble connecting to our servers. Your data is safe. Please try again in a moment."
```

#### Permission Errors (Access issues)
```
❌ "403 Forbidden"
✅ "You don't have permission to edit this project. Contact the project owner to request access."

❌ "Unauthorized"
✅ "Your session has expired. Please sign in again to continue."
```

#### Not Found Errors
```
❌ "404 Not Found"
✅ "We can't find that page. It may have been moved or deleted. [Return to dashboard] or [Search for what you need]"

❌ "No results"
✅ "No results for 'project alpha'. Try a different search term or create a new project."
```

### Tone by Severity

**Minor errors** (user mistakes, validation):
- Friendly and helpful
- Light tone acceptable
- Focus on easy fix

```
"Oops! Your password needs at least one number. Almost there!"
```

**Moderate errors** (not found, permissions):
- Professional and clear
- Respectful tone
- Provide alternatives

```
"This file isn't available. It may have been deleted. Check your recent files or search for it."
```

**Critical errors** (system failures, data at risk):
- Calm and reassuring
- Transparent but not technical
- Emphasize safety

```
"We encountered a technical issue and couldn't process your payment. Your card has not been charged. We've been notified and are working on a fix. Please try again in 30 minutes or contact support if urgent."
```

### Error Prevention

**Better than good error messages is preventing errors:**

1. **Inline validation**: Show errors as users type (with debounce)
2. **Format hints**: "MM/DD/YYYY" next to date field
3. **Autocomplete**: Suggest valid values
4. **Disable invalid actions**: Gray out "Submit" until form valid
5. **Confirmation dialogs**: For destructive actions
6. **Smart defaults**: Pre-fill when possible

## Onboarding

### Onboarding Goals

1. **Time to value**: First meaningful action in < 2 min
2. **Time to success**: First win in < 5 min
3. **Time to competency**: Core workflow in < 10 min

### Progressive Disclosure

**Don't show everything at once.** Introduce features when needed.

```
❌ Bad: 20-step tutorial on first load
✅ Good: 3-step essential setup → Learn by doing → Contextual tips

❌ Bad: "Here are all 50 features!"
✅ Good: "Let's create your first project" → Reveal features in context
```

### Onboarding Patterns

#### Welcome Screen
```
Headline: Clear value proposition
"Welcome to [Product]! Let's get your workspace set up."

Subheadline: Process overview
"We'll help you connect your data, invite your team, and create your first report."

CTA: Start journey
[Get started]

Skip: Respectful exit
[Skip setup - I'll explore on my own]
```

#### Step Indicators
```
Show progress clearly:
- "Step 2 of 4" (numeric)
- [█████░░░] (visual bar)
- "Import data" → "Invite team" → "Create report" (named steps)

Each step:
- Headline: What we're doing
- Context: Why it matters (1 sentence)
- Estimate: "About 30 seconds"
- Action: Clear next step
```

#### Empty States (First Use)
```
[Friendly illustration]
"Your dashboard awaits"
"Dashboards help you track metrics at a glance. Create your first one to get started."
[Create dashboard] [See example]
```

#### Feature Tooltips (Coachmarks)
```
Guidelines:
- Trigger on first encounter (not on page load)
- Limit to 3-5 per session
- Always dismissible
- Point to specific element
- 1-2 sentences max

Example:
"Use Quick Add (⌘K) to create tasks from anywhere"
[Got it]
```

#### Success Moments
```
Celebrate completion:
"Excellent! Your workspace is ready. Here's what you can do now:"
✓ Create and assign tasks
✓ Track progress with dashboards
✓ Collaborate with your team
[Start working]

Micro-celebrations throughout:
✓ "Account connected"
✓ "Team invited"
✓ "First project created"
```

### Onboarding Copy Guidelines

**Headlines**:
- Action-oriented: "Let's connect your calendar"
- Benefit-focused: "Track your time automatically"
- User-centric: "You're almost ready to start"

**CTAs**:
- Specific: "Import contacts" not "Next"
- Show progress: "Continue (3 of 5)"
- Positive: "Continue" not "Don't skip"

**Skip options**:
- Respectful: "I'll do this later"
- Honest: "Skip (you can always invite later)"
- Easy return: "Remind me tomorrow"

## Accessibility

### Alt Text

**Decorative images**: `alt=""`
**Functional images**: Describe action, not appearance
**Informative images**: Describe content/data

```
Decorative:
alt="" (tells screen readers to skip)

Functional (button/link):
❌ alt="Blue arrow icon"
✅ alt="Next page"

Informative (chart):
❌ alt="Chart"
✅ alt="Line chart showing 40% revenue growth from Q1 to Q4 2024"
```

**Complex images**: Short alt + long description
```
<img alt="2024 sales distribution by region" src="chart.png">
<details>
  <summary>Chart data</summary>
  North America: 45%, Europe: 30%, Asia: 20%, Other: 5%
</details>
```

### ARIA Labels

**Use when visual label is missing or insufficient:**

```html
<!-- Icon-only button -->
<button aria-label="Close dialog">×</button>

<!-- Add context -->
<button aria-label="Search products">🔍</button>

<!-- Don't use if text is visible -->
❌ <button aria-label="Save">Save</button>
✅ <button>Save</button>
```

### Link Text

**Links should make sense out of context:**

```
❌ "Click here to download"
❌ "Read more"
❌ "Learn more about our privacy policy here"

✅ "Download 2024 annual report (PDF, 2.3 MB)"
✅ "Read our complete privacy policy"
✅ "Learn how we protect your data"
```

### Form Accessibility

```html
<!-- Always use <label> -->
<label for="email">Email address</label>
<input type="email" id="email" />

<!-- Add helpful instructions -->
<label for="password">Password</label>
<span id="pwd-hint">At least 8 characters with 1 number</span>
<input
  type="password"
  id="password"
  aria-describedby="pwd-hint"
/>

<!-- Associate errors -->
<input
  type="email"
  id="email"
  aria-invalid="true"
  aria-describedby="email-error"
/>
<span id="email-error" role="alert">
  Please enter a valid email like name@example.com
</span>
```

### Inclusive Language

**Avoid ableist terms:**
```
❌ "See the new features"
✅ "Check out the new features"

❌ "Blind spot"
✅ "Gap" or "Missing area"

❌ "Crazy fast" / "Insane performance"
✅ "Incredibly fast" / "Exceptional performance"

❌ "Dummy text" / "Sanity check"
✅ "Sample text" / "Verification" or "Test"
```

**Avoid directional language:**
```
❌ "Click the button on the right"
✅ "Click the Save button"

❌ "See the chart below"
✅ "The following chart shows..."
```

**Avoid color-only instructions:**
```
❌ "Click the green button"
✅ "Click the Confirm button"

❌ "Required fields are in red"
✅ "Required fields are marked with an asterisk (*)"
```

## Voice & Tone

### Voice (Consistent Personality)
Your product's voice is its personality—stays consistent across all copy.

Common voice attributes:
- **Professional**: Clear, respectful, competent
- **Friendly**: Warm, approachable, conversational
- **Helpful**: Supportive, instructive, empowering
- **Confident**: Assured, capable, trustworthy

### Tone (Emotional Context)
Tone changes based on the situation.

**Positive moments** (success, celebration):
- Enthusiastic and congratulatory
- "Excellent! Your account is all set up and ready to go."

**Neutral moments** (forms, settings):
- Clear and straightforward
- "Enter your billing information to complete your purchase."

**Negative moments** (errors, warnings):
- Calm and helpful (never blame user)
- "We couldn't process your payment. Please check your card details and try again."

**Urgent moments** (critical errors, deadlines):
- Direct and clear (no fluff)
- "Your session expires in 2 minutes. Save your work now."

### Tone Examples by Context

```
Welcome (enthusiastic):
"Welcome to TaskFlow! We're excited to help you get organized."

Form (neutral):
"Enter your company information"

Success (celebratory):
"You did it! Your team has been invited."

Error (calm and helpful):
"We couldn't save your changes. Check your connection and try again."

Warning (direct):
"This action cannot be undone. Delete 3 files?"

Help (supportive):
"Not sure where to start? We'll guide you through setting up your first project."
```

## Content Patterns

### Character Limits

**Know your constraints:**

- **Button**: 15-20 characters ideal, 30 max
- **Tooltip**: 60-80 characters (2 lines)
- **Notification**: 90-120 characters
- **Error message**: 120-150 characters
- **Alt text**: 125-150 characters
- **Meta description**: 150-160 characters
- **Tweet**: 280 characters

### Numbers and Dates

**Be specific and use user's format:**

```
❌ "about 2 weeks ago"
✅ "January 15, 2024" or "2 weeks ago (Jan 15)"

❌ "1234567 bytes"
✅ "1.2 MB"

❌ "97.3%"
✅ "97% uptime" or "Almost always online"
```

**Localization considerations:**
- Dates: US (01/15/2024) vs EU (15/01/2024)
- Use ISO 8601 for clarity: 2024-01-15
- Or spell out: January 15, 2024
- Times: 12-hour (3:00 PM) vs 24-hour (15:00)

### Capitalization

**Choose one and be consistent:**

**Title Case** (Each Major Word Capitalized):
- Headlines and page titles
- Navigation menu items
- Dialog titles

**Sentence case** (Only first word capitalized):
- Body text
- Form labels
- Button text (recommended)
- Error messages
- Tooltips

```
Title Case:
"Create New Project"
"Account Settings"

Sentence case:
"Create new project"
"Account settings"
```

**Recommendation**: Sentence case is more readable, scannable, and friendly. Use for most UI copy.

### Punctuation

**General rules:**

- **Periods**: Use in body text and multi-sentence messages. Skip in single-sentence tooltips, labels, and buttons.
- **Exclamation points**: Use sparingly for celebration. Max 1 per screen.
- **Question marks**: Use in questions (obviously). Don't use in buttons ("Delete?" → "Delete item")
- **Colons**: Usually unnecessary in form labels. "Email:" → "Email address"
- **Ellipsis (...)**: Use for loading states. "Saving..." → shows ongoing action

```
✅ Button: "Save changes" (no period)
✅ Tooltip: "This saves your work automatically" (no period if 1 sentence)
✅ Error: "We couldn't save your changes. Check your connection and try again." (periods in multi-sentence)
✅ Success: "Project created!" (exclamation for celebration)
```

### Contraction Use

**When to use contractions:**
- Friendly, conversational tone
- Onboarding and help text
- Success messages
- Chatbots and conversational UI

**When to avoid:**
- Formal business settings
- Legal or compliance text
- Serious errors or warnings
- When emphasizing words ("You will be charged")

```
Conversational:
"You're all set! We'll send a confirmation email."

Formal:
"You will be charged on the 1st of each month."
```

## UX Writing Checklist

Before publishing any copy, verify:

**Clarity**:
- [ ] Can a new user understand this immediately?
- [ ] Is it written in plain language (8th-grade level)?
- [ ] Are there any jargon or technical terms that need explanation?

**Brevity**:
- [ ] Is every word necessary?
- [ ] Can this be shorter without losing meaning?
- [ ] Have I removed filler words?

**User-centered**:
- [ ] Is it written from the user's perspective (not the system's)?
- [ ] Does it use "you/your" language?
- [ ] Does it focus on user benefits, not features?

**Consistency**:
- [ ] Does this match our existing terminology?
- [ ] Is capitalization consistent with our style?
- [ ] Does the tone match the context?

**Accessibility**:
- [ ] Do all images have appropriate alt text?
- [ ] Are links descriptive out of context?
- [ ] Is this understandable by screen readers?
- [ ] Have I avoided ableist language?
- [ ] Have I avoided color-only or direction-only instructions?

**Actionability**:
- [ ] Is the next step clear?
- [ ] Are CTAs specific and action-oriented?
- [ ] Have I provided a solution (for errors)?

**Scannability**:
- [ ] Can users skim and understand key points?
- [ ] Have I front-loaded important information?
- [ ] Is the structure clear (headlines, bullets)?

This skill provides the foundation for all UX writing decisions. Apply these patterns consistently to create interfaces that are clear, helpful, and accessible to all users.
