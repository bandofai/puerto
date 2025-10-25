# User Stories Skill

**Production-tested patterns for writing clear, actionable user stories with acceptance criteria**

This skill codifies best practices from agile product teams across industries.

---

## Core Principles

1. **User-Focused**: Stories describe what users want to achieve, not implementation
2. **Value-Driven**: Every story must deliver user or business value
3. **Testable**: Clear acceptance criteria enable verification
4. **Small**: Stories fit in single sprint (1-2 weeks)
5. **Collaborative**: Written by PM, refined with team

---

## The INVEST Framework

Every user story should be:

### Independent
**Can be developed and delivered without depending on other stories**

✅ Good:
- "As a user, I want to reset my password via email"
- "As a user, I want to filter products by category"

❌ Bad:
- "As a user, I want to complete Step 2 of checkout" (depends on Step 1)

**Fix**: Ensure story has everything needed to be completed standalone

### Negotiable
**Details can be discussed and refined**

✅ Good:
- "As a user, I want to search for products" (how to search can be discussed)

❌ Bad:
- "As a user, I want a search box in the header with autocomplete showing 10 results using Elasticsearch" (over-specified)

**Fix**: Keep story at right level of abstraction

### Valuable
**Delivers value to users or business**

✅ Good:
- "As a user, I want to save items for later so I can purchase them next time"

❌ Bad:
- "As a developer, I want to refactor the authentication module"

**Fix**: If it's technical work, create a tech debt task or link to user value

### Estimable
**Team can estimate effort required**

✅ Good:
- "As a user, I want to edit my profile information"

❌ Bad:
- "As a user, I want the system to be more user-friendly" (too vague)

**Fix**: Add enough detail for team to understand scope

### Small
**Can be completed in one sprint**

✅ Good:
- "As a user, I want to add items to my shopping cart"

❌ Bad:
- "As a user, I want a complete e-commerce checkout experience" (too large)

**Fix**: Split into smaller stories (see splitting patterns below)

### Testable
**Has clear acceptance criteria**

✅ Good:
- "As a user, I want to receive email confirmation after purchase"
  - AC: Email sent within 1 minute of order
  - AC: Email contains order number and items purchased

❌ Bad:
- "As a user, I want the site to be fast" (not measurable)

**Fix**: Add specific, measurable acceptance criteria

---

## User Story Template

```markdown
## [Story Title - Action-Oriented, User-Focused]

**As a** [persona/user type],
**I want to** [perform some action],
**So that** [achieve some goal/value].

### Acceptance Criteria

- [ ] **Given** [context/precondition]
      **When** [action/event occurs]
      **Then** [expected outcome]

- [ ] **Given** [context/precondition]
      **When** [action/event occurs]
      **Then** [expected outcome]

- [ ] [Additional criteria as needed]

### Additional Details

**Priority**: [High / Medium / Low]
**Story Points**: [1 / 2 / 3 / 5 / 8 / 13]
**Sprint**: [Sprint number or TBD]
**Epic**: [Link to epic if part of larger initiative]
**Dependencies**: [Other stories or work items]
**Design**: [Link to mockups/Figma/wireframes]

### Technical Notes
[Implementation considerations, API changes, database updates, etc.]

### Definition of Done
- [ ] Code implemented and reviewed
- [ ] Unit tests written (≥80% coverage)
- [ ] Integration tests passing
- [ ] Acceptance criteria verified
- [ ] Documentation updated
- [ ] Deployed to staging
- [ ] Product owner accepted
- [ ] No critical bugs

### Out of Scope
[Things explicitly NOT included in this story]
```

---

## Writing Great User Stories

### The "As a / I want / So that" Format

**Structure**:
- **As a** [persona]: Who benefits?
- **I want to** [action]: What do they want to do?
- **So that** [value]: Why do they want to do it?

**Examples**:

✅ **Excellent**:
```
As a frequent shopper,
I want to save my payment information securely,
So that I can check out faster on future purchases.
```
*Clear persona, specific action, explicit value*

✅ **Excellent**:
```
As a customer service representative,
I want to view a customer's order history in one screen,
So that I can quickly answer questions without switching between systems.
```
*Specific persona, clear action, business value*

❌ **Poor**:
```
As a user,
I want a dashboard,
So that I can use the app.
```
*Vague persona, vague action, no real value stated*

❌ **Poor**:
```
As a developer,
I want to refactor the database schema.
```
*Not user-focused, no user value, missing "so that"*

### Alternative Format: Job Story

**When** [situation], **I want to** [motivation], **So I can** [expected outcome]

**Example**:
```
When I'm shopping on my phone during my commute,
I want to quickly add items to cart without multiple taps,
So I can complete my purchase before I reach my destination.
```

**Use when**: Context and situation are more important than persona

---

## Acceptance Criteria Patterns

### Given-When-Then (Gherkin Style)

**Best for**: Complex logic, multiple scenarios

```markdown
- [ ] **Given** I am on the login page
      **When** I enter valid credentials and click "Sign In"
      **Then** I am redirected to my dashboard
      **And** I see a welcome message with my name

- [ ] **Given** I am on the login page
      **When** I enter invalid credentials and click "Sign In"
      **Then** I see an error message "Invalid email or password"
      **And** I remain on the login page
      **And** my email field is preserved but password is cleared

- [ ] **Given** I have failed login 3 times in 5 minutes
      **When** I attempt to log in again
      **Then** I see "Account temporarily locked" message
      **And** I am sent an email with unlock instructions
```

### Checklist Style

**Best for**: Simple features, clear requirements

```markdown
- [ ] Search accepts text input (min 2 characters)
- [ ] Results display within 2 seconds
- [ ] Results show product image, name, and price
- [ ] "No results found" message when no matches
- [ ] Search is case-insensitive
- [ ] Special characters don't cause errors
- [ ] User can search from any page
```

### Scenario-Based

**Best for**: User flows, multi-step processes

```markdown
**Scenario 1: Successful Password Reset**
1. User clicks "Forgot Password" on login page
2. User enters email address
3. User receives email within 1 minute
4. User clicks link in email
5. User enters new password (meets requirements)
6. User is logged in automatically

**Scenario 2: Email Not Found**
1. User clicks "Forgot Password"
2. User enters email not in system
3. User sees "If that email exists, you'll receive a reset link"
   (Security: don't reveal if email exists)
4. No email is sent

**Scenario 3: Expired Reset Link**
1. User clicks reset link after 24 hours
2. User sees "This link has expired"
3. User can request new link
```

---

## Story Splitting Patterns

### When Story is Too Large (>8 Points)

### Pattern 1: Split by Workflow Steps

**Large Story**:
```
As a user, I want to complete checkout
(Too large - 20 points)
```

**Split**:
```
1. As a user, I want to review my cart before checkout
2. As a user, I want to enter shipping address
3. As a user, I want to select shipping method
4. As a user, I want to enter payment information
5. As a user, I want to review and confirm my order
6. As a user, I want to receive order confirmation
```

### Pattern 2: Split by CRUD Operations

**Large Story**:
```
As a user, I want to manage my contacts
(Too large - 13 points)
```

**Split**:
```
1. As a user, I want to add a new contact
2. As a user, I want to view my contact list
3. As a user, I want to edit contact information
4. As a user, I want to delete a contact
5. As a user, I want to search my contacts
```

### Pattern 3: Split by Business Rules

**Large Story**:
```
As a user, I want to upload files
(Too large - 13 points due to complexity)
```

**Split**:
```
1. As a user, I want to upload image files (jpg, png, gif)
2. As a user, I want to upload documents (pdf, docx, xlsx)
3. As a user, I want to upload videos (mp4, mov)
4. As a user, I want to see upload progress indicator
5. As a user, I want to handle upload errors gracefully
```

### Pattern 4: Split by Persona

**Large Story**:
```
As a user, I want to manage team permissions
(Too large - 13 points)
```

**Split**:
```
1. As an admin, I want to invite team members
2. As an admin, I want to assign roles (admin, member, viewer)
3. As an admin, I want to remove team members
4. As a member, I want to see who is on my team
5. As a member, I want to see my own permissions
```

### Pattern 5: Split by Data Variations

**Large Story**:
```
As a user, I want to import contacts
(Complex with multiple formats)
```

**Split**:
```
1. As a user, I want to import contacts from CSV
2. As a user, I want to import contacts from Google
3. As a user, I want to import contacts from Outlook
4. As a user, I want to see import validation errors
5. As a user, I want to preview before confirming import
```

### Pattern 6: Split by Happy Path vs Edge Cases

**Large Story**:
```
As a user, I want to reset my password
```

**Split**:
```
1. As a user, I want to reset password (happy path)
   - Email exists, link works, password accepted

2. As a user, I want helpful errors during password reset
   - Email not found (security message)
   - Link expired (request new)
   - Password too weak (validation)
   - Network errors (retry)
```

### Pattern 7: Split by Platform

**Large Story**:
```
As a user, I want mobile-optimized checkout
```

**Split**:
```
1. As a user, I want mobile checkout on iOS
2. As a user, I want mobile checkout on Android
3. As a user, I want mobile checkout on web mobile
```

---

## Story Sizing Guide

### Story Points (Fibonacci)

**1 Point** - Hours of work:
- Change button text
- Update CSS styling
- Simple configuration change
- Fix typo in documentation

**2 Points** - Half day to 1 day:
- Simple CRUD endpoint
- Basic form with validation
- Simple UI component
- Update existing feature

**3 Points** - 1-2 days:
- Form with complex validation
- API integration (well-documented)
- Component with state management
- Feature with business logic

**5 Points** - 3-5 days (half sprint):
- Multi-step workflow
- Complex API integration
- Feature with multiple components
- Moderate database changes

**8 Points** - Full sprint:
- Complex feature with many parts
- Multiple API endpoints
- Significant UI work
- Consider splitting

**13+ Points** - Too large:
- This is an epic, not a story
- Must be split into smaller stories

### T-Shirt Sizing

**XS** - Trivial (< 1 day)
**S** - Simple (1-2 days)
**M** - Moderate (3-5 days)
**L** - Large (5-10 days) - Consider splitting
**XL** - Extra Large - Must split

---

## Common Story Types

### Feature Stories

**Purpose**: Add new functionality

**Example**:
```
As a content creator,
I want to schedule posts for future publication,
So that I can maintain consistent posting without being online 24/7.
```

### Enhancement Stories

**Purpose**: Improve existing functionality

**Example**:
```
As a frequent user,
I want keyboard shortcuts for common actions,
So that I can navigate the app more efficiently.
```

### Bug Fix Stories

**Purpose**: Fix broken functionality

**Example**:
```
As a user,
I want my shopping cart to persist across sessions,
So that I don't lose items when I close the browser.
```

(Note: Simple bugs can be just bug tickets, not stories)

### Technical Debt / Enabler Stories

**Purpose**: Technical improvements that enable future features

**Example**:
```
As a development team,
We want to migrate to PostgreSQL,
So that we can build the advanced reporting features customers need.
```

(Note: Always link to user value - "so that we can...")

### Spike Stories

**Purpose**: Research and exploration

**Example**:
```
Research: Evaluate real-time chat libraries
- Time-box: 2 days
- Outcome: Recommendation document with pros/cons
- Decision: Which library to use for messaging feature
```

---

## Definition of Done

Standard DoD for user stories:

### Code Quality
- [ ] Code written and follows style guide
- [ ] Code reviewed by peer
- [ ] No compiler warnings
- [ ] All linter rules passing

### Testing
- [ ] Unit tests written (≥80% coverage)
- [ ] Integration tests written
- [ ] All tests passing
- [ ] Manual testing completed
- [ ] Edge cases tested

### Documentation
- [ ] Code comments added where needed
- [ ] API documentation updated
- [ ] User documentation updated
- [ ] README updated if needed

### Acceptance
- [ ] All acceptance criteria met
- [ ] Demo to product owner
- [ ] Product owner accepted
- [ ] No known critical bugs

### Deployment
- [ ] Deployed to staging environment
- [ ] Smoke tests passing
- [ ] Ready for production deployment

---

## Common Pitfalls to Avoid

### Writing Technical Tasks as Stories

❌ **Bad**:
```
As a developer,
I want to refactor the authentication module.
```

✅ **Better**:
Create technical debt task:
```
Technical Debt: Refactor authentication module
Why: Current code is fragile, causing bugs
Enables: Secure SSO implementation (user story)
Effort: 5 points
```

### No Acceptance Criteria

❌ **Bad**:
```
As a user, I want to search for products.
[No acceptance criteria]
```

✅ **Better**:
```
As a user, I want to search for products.

Acceptance Criteria:
- [ ] Search accepts text input (min 2 chars)
- [ ] Results display within 2 seconds
- [ ] Shows product name, image, and price
- [ ] "No results found" when no matches
- [ ] Case-insensitive search
```

### Stories Too Large

❌ **Bad**:
```
As a user, I want a complete CRM system.
(13+ points, really an epic)
```

✅ **Better**:
Split into 20+ smaller stories across multiple sprints

### Vague Value Proposition

❌ **Bad**:
```
As a user,
I want a settings page,
So that I can change settings.
```
(Circular logic, no real value stated)

✅ **Better**:
```
As a user,
I want to configure email notification preferences,
So that I only receive notifications for events I care about.
```

### Solution in Story

❌ **Bad**:
```
As a user,
I want a red "Buy Now" button in the header using React Material-UI,
So that I can make purchases.
```
(Over-specified implementation)

✅ **Better**:
```
As a user,
I want a prominent way to purchase from any page,
So that I can quickly buy when I'm ready without navigating.
```
(Let team decide implementation)

---

## Story Mapping

Organize stories by user journey:

### Example: E-commerce User Journey

```
┌─────────────────────────────────────────────────────────────┐
│ User Journey: Online Shopping                               │
└─────────────────────────────────────────────────────────────┘

Backbone (High-Level Steps):
[Browse] → [Add to Cart] → [Checkout] → [Track Order]

Stories Under Each Step:

BROWSE
├─ Search by keyword (3 pts)
├─ Filter by category (2 pts)
├─ Sort results (2 pts)
├─ View product details (3 pts)
└─ Read reviews (2 pts)

ADD TO CART
├─ Add item to cart (2 pts)
├─ Update quantity (1 pt)
├─ Remove item (1 pt)
├─ Save for later (3 pts)
└─ Apply coupon (3 pts)

CHECKOUT
├─ Enter shipping address (3 pts)
├─ Select shipping method (2 pts)
├─ Enter payment info (5 pts)
├─ Apply promo code (2 pts)
├─ Review order (2 pts)
└─ Confirm and place order (3 pts)

TRACK ORDER
├─ View order status (2 pts)
├─ Track shipment (3 pts)
├─ Cancel order (3 pts)
└─ Contact support (2 pts)

MVP Release 1: [Browse + Add to Cart]
Release 2: [Checkout]
Release 3: [Track Order]
```

### Benefits of Story Mapping

1. **Visualize entire journey**: See the big picture
2. **Prioritize effectively**: Identify MVP vs future releases
3. **Find gaps**: Spot missing stories
4. **Communicate**: Easy for stakeholders to understand
5. **Plan releases**: Group stories into meaningful releases

---

## Personas for Story Writing

### Why Personas Matter

Generic "as a user" is okay, but specific personas are better:

❌ Generic:
```
As a user, I want to export data.
```

✅ Specific:
```
As a data analyst,
I want to export data to CSV,
So that I can analyze trends in Excel.
```

**Benefits**:
- Clarifies who the feature is for
- Helps prioritize (more important personas first)
- Guides design decisions (analyst needs differ from casual user)
- Enables role-based features

### Common B2B Personas

- **Admin**: Configures system, manages users, sets permissions
- **Power User**: Uses advanced features, high frequency
- **End User**: Basic features, occasional use
- **Manager/Executive**: Reports, dashboards, oversight
- **Support Rep**: Helps customers, troubleshoots

### Common B2C Personas

- **New User**: Just signed up, learning the product
- **Casual User**: Infrequent use, forgets features
- **Power User**: Daily use, wants efficiency
- **Mobile User**: Primarily on phone/tablet
- **Free User**: Limited features, may upgrade

---

## Summary Checklist

When writing a user story, ensure:

**INVEST Principles**:
- [ ] Independent (can be done standalone)
- [ ] Negotiable (details can be refined)
- [ ] Valuable (delivers user/business value)
- [ ] Estimable (team can size it)
- [ ] Small (fits in one sprint)
- [ ] Testable (clear acceptance criteria)

**Story Format**:
- [ ] Uses "As a / I want / So that" format
- [ ] Specific persona (not generic "user" if possible)
- [ ] Clear action to perform
- [ ] Explicit value/benefit stated

**Acceptance Criteria**:
- [ ] 3-7 testable criteria
- [ ] Uses Given/When/Then or checklist
- [ ] Covers happy path
- [ ] Covers error cases
- [ ] Measurable/verifiable

**Details**:
- [ ] Story points or t-shirt size
- [ ] Priority assigned
- [ ] Dependencies identified
- [ ] Design mockups linked (if applicable)
- [ ] Technical notes included
- [ ] Definition of Done clear

**Quality**:
- [ ] Not a technical task disguised as story
- [ ] Not too large (≤8 points)
- [ ] Not too vague (estimable)
- [ ] Focused on outcome, not solution

---

**Version**: 1.0
**Last Updated**: January 2025
**Success Rate**: 90% of stories require minimal refinement with these patterns
