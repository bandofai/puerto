# Proposal Generation Skill

## Expert Knowledge Domain
Sales proposal creation, RFP responses, business development writing

## Table of Contents
1. [Proposal Structure](#proposal-structure)
2. [Template Patterns](#template-patterns)
3. [Client Customization](#client-customization)
4. [Value Proposition Frameworks](#value-proposition-frameworks)
5. [Case Study Selection](#case-study-selection)
6. [Terms & Conditions](#terms--conditions)

## Proposal Structure

### Standard Proposal Sections

```markdown
# Sales Proposal for {{CLIENT_NAME}}

## Executive Summary
- One-page overview of proposed solution
- Key benefits and ROI
- Total investment and timeline

## Understanding Your Needs
- Client's current challenges
- Business objectives
- Success criteria

## Proposed Solution
- Detailed approach
- Methodology
- Deliverables
- Timeline

## Why {{OUR_COMPANY}}
- Company background
- Relevant experience
- Differentiators

## Case Studies & Social Proof
- 2-3 relevant customer success stories
- Metrics and outcomes
- Testimonials

## Team & Resources
- Project team bios
- Resource allocation
- Support structure

## Investment & Pricing
- Detailed pricing breakdown
- Payment terms
- Optional add-ons

## Terms & Conditions
- Scope boundaries
- Assumptions
- Legal terms

## Next Steps
- Decision timeline
- Implementation timeline
- Contact information
```

### Winning Proposal Formula

**HOOK → UNDERSTAND → SOLVE → PROVE → CLOSE**

1. **HOOK** (Executive Summary)
   - Lead with the client's biggest pain point
   - Promise specific, measurable outcome
   - State investment range upfront

2. **UNDERSTAND** (Needs Analysis)
   - Demonstrate deep understanding of their business
   - Show you've done research
   - Reflect their language and priorities

3. **SOLVE** (Proposed Solution)
   - Present clear, actionable solution
   - Break into manageable phases
   - Link each element to a business outcome

4. **PROVE** (Social Proof)
   - Showcase similar client success
   - Include specific metrics (2x growth, 50% cost reduction)
   - Use testimonials strategically

5. **CLOSE** (Investment & Next Steps)
   - Clear, transparent pricing
   - Easy decision-making options
   - Obvious call-to-action

## Template Patterns

### Consulting Services Template

```markdown
# {{SERVICE_TYPE}} Proposal for {{CLIENT_NAME}}

**Prepared for:** {{CLIENT_CONTACT_NAME}}, {{CLIENT_TITLE}}
**Prepared by:** {{OUR_CONTACT_NAME}}, {{OUR_COMPANY}}
**Date:** {{DATE}}
**Valid through:** {{EXPIRATION_DATE}}

---

## Executive Summary

{{CLIENT_NAME}} is facing {{PRIMARY_CHALLENGE}}. This proposal outlines a {{DURATION}}-month engagement to {{DESIRED_OUTCOME}}, delivering {{KEY_METRICS}} improvement.

**Total Investment:** {{TOTAL_PRICE}}
**Expected ROI:** {{ROI_PERCENTAGE}} within {{TIMEFRAME}}

---

## Your Current Challenge

Based on our conversations, {{CLIENT_NAME}} is experiencing:

- {{PAIN_POINT_1}}
- {{PAIN_POINT_2}}
- {{PAIN_POINT_3}}

These challenges are resulting in {{BUSINESS_IMPACT}}.

---

## Our Proposed Approach

### Phase 1: {{PHASE_1_NAME}} ({{DURATION}})
{{PHASE_1_DESCRIPTION}}

**Deliverables:**
- {{DELIVERABLE_1}}
- {{DELIVERABLE_2}}

### Phase 2: {{PHASE_2_NAME}} ({{DURATION}})
{{PHASE_2_DESCRIPTION}}

**Deliverables:**
- {{DELIVERABLE_1}}
- {{DELIVERABLE_2}}

---

## Investment

| Phase | Duration | Investment |
|-------|----------|------------|
| Phase 1 | {{DURATION}} | {{PRICE}} |
| Phase 2 | {{DURATION}} | {{PRICE}} |
| **Total** | {{TOTAL_DURATION}} | **{{TOTAL_PRICE}}** |

**Payment Terms:** {{PAYMENT_SCHEDULE}}
```

### Software/Product Template

```markdown
# {{PRODUCT_NAME}} Proposal for {{CLIENT_NAME}}

## Solution Overview

{{PRODUCT_NAME}} helps {{CLIENT_TYPE}} achieve {{PRIMARY_BENEFIT}} through {{KEY_CAPABILITY}}.

## Pricing Tiers

### Starter: ${{PRICE}}/month
Perfect for {{USE_CASE}}

**Includes:**
- {{FEATURE_1}}
- {{FEATURE_2}}
- {{FEATURE_3}}

### Professional: ${{PRICE}}/month
Ideal for {{USE_CASE}}

**Everything in Starter, plus:**
- {{FEATURE_4}}
- {{FEATURE_5}}
- {{FEATURE_6}}

### Enterprise: Custom Pricing
For {{USE_CASE}}

**Everything in Professional, plus:**
- {{FEATURE_7}}
- {{FEATURE_8}}
- Dedicated support
- Custom integrations

## Implementation Timeline

Week 1-2: {{MILESTONE}}
Week 3-4: {{MILESTONE}}
Week 5+: {{MILESTONE}}
```

## Client Customization

### Research Checklist

Before customizing a proposal:

- [ ] Review client website and recent news
- [ ] Understand their industry and competitive landscape
- [ ] Identify their business model and revenue drivers
- [ ] Research key decision-makers (LinkedIn)
- [ ] Find their public challenges (earnings calls, interviews)
- [ ] Check for existing customer relationships in their industry
- [ ] Understand their tech stack and tools
- [ ] Research their company culture and values

### Personalization Techniques

1. **Use Their Language**
   ```
   Generic: "We'll improve your customer acquisition"
   Personalized: "We'll optimize your PLG motion to reduce CAC and improve activation rates"
   ```

2. **Reference Their Specific Situation**
   ```
   Generic: "Many companies face scaling challenges"
   Personalized: "Your recent Series B and 3x headcount growth in 2024 creates unique operational scaling challenges"
   ```

3. **Align with Their Goals**
   ```
   Generic: "We'll increase revenue"
   Personalized: "Supporting your stated goal of reaching $50M ARR by Q4 2026"
   ```

4. **Show Industry Expertise**
   ```
   Generic: "We understand your business"
   Personalized: "We've helped 15 B2B SaaS companies navigate the $10M to $50M ARR transition, addressing common challenges like negative unit economics during rapid expansion"
   ```

## Value Proposition Frameworks

### Feature → Benefit → Outcome

```
Feature: What we do
Benefit: What it means
Outcome: Business impact

Example:
Feature: "Weekly optimization sprints with dedicated analyst"
Benefit: "Continuous improvement without burdening your team"
Outcome: "15-20% improvement in conversion rates within first quarter"
```

### ROI Calculator

```python
def calculate_roi(current_state, improved_state, investment):
    """
    Calculate ROI for proposal

    Args:
        current_state: Current metric value (revenue, cost, etc.)
        improved_state: Projected metric after engagement
        investment: Total cost of proposed solution

    Returns:
        ROI percentage and payback period
    """
    gain = improved_state - current_state
    roi_percentage = ((gain - investment) / investment) * 100

    monthly_gain = gain / 12
    payback_months = investment / monthly_gain if monthly_gain > 0 else float('inf')

    return {
        "annual_gain": gain,
        "roi_percentage": round(roi_percentage, 1),
        "payback_months": round(payback_months, 1)
    }

# Example
roi = calculate_roi(
    current_state=1_000_000,  # $1M annual revenue
    improved_state=1_300_000,  # $1.3M projected
    investment=50_000          # $50K engagement cost
)
# Output: 500% ROI, 2-month payback
```

### Value Proposition Template

```markdown
For [TARGET_CUSTOMER]
Who [STATEMENT_OF_NEED]
Our [PRODUCT/SERVICE]
Is a [CATEGORY]
That [KEY_BENEFIT]
Unlike [PRIMARY_COMPETITOR]
Our solution [DIFFERENTIATOR]
```

Example:
```markdown
For mid-market B2B SaaS companies
Who are struggling to scale revenue operations efficiently
Our RevOps consulting engagement
Is a comprehensive operational transformation
That increases revenue per employee by 25% while reducing CAC
Unlike traditional management consulting
Our solution is led by former SaaS operators with hands-on implementation
```

## Case Study Selection

### Matching Criteria

Select case studies based on:

1. **Industry Similarity**
   - Same industry = highest relevance
   - Adjacent industry = good, explain parallels
   - Different industry = only if challenge is identical

2. **Company Size/Stage**
   - Similar revenue, team size
   - Similar growth stage (early-stage, scale-up, enterprise)
   - Similar market (B2B vs B2C)

3. **Challenge Similarity**
   - Exact same pain point
   - Comparable starting metrics
   - Similar constraints (budget, timeline, resources)

4. **Impressive Results**
   - Quantifiable outcomes (2x, 50%, $1M saved)
   - Time to value (results within X months)
   - Sustained impact (results maintained over time)

### Case Study Template

```markdown
## Case Study: {{CLIENT_NAME}}

**Industry:** {{INDUSTRY}}
**Company Size:** {{SIZE}}
**Challenge:** {{CHALLENGE_DESCRIPTION}}

### The Situation
{{CLIENT_NAME}}, a {{DESCRIPTION}}, was experiencing {{PROBLEM}}. This resulted in {{BUSINESS_IMPACT}}.

### Our Approach
We implemented a {{DURATION}} program focused on:
1. {{APPROACH_1}}
2. {{APPROACH_2}}
3. {{APPROACH_3}}

### Results
- **{{METRIC_1}}:** {{BEFORE}} → {{AFTER}} ({{IMPROVEMENT}}% improvement)
- **{{METRIC_2}}:** {{BEFORE}} → {{AFTER}} ({{IMPROVEMENT}}% improvement)
- **{{METRIC_3}}:** {{BEFORE}} → {{AFTER}} ({{IMPROVEMENT}}% improvement)

> "{{TESTIMONIAL_QUOTE}}"
> — {{NAME}}, {{TITLE}}, {{COMPANY}}

### Timeline to Value
Results achieved within {{TIMEFRAME}}, with initial improvements visible in {{EARLY_TIMEFRAME}}.
```

## Terms & Conditions

### Standard Terms Template

```markdown
## Terms & Conditions

### Scope
This proposal covers the services described in the "Proposed Solution" section. Any additional work outside this scope will require a separate agreement and pricing.

### Assumptions
This proposal assumes:
- {{ASSUMPTION_1}}
- {{ASSUMPTION_2}}
- {{ASSUMPTION_3}}

### Pricing Validity
Pricing in this proposal is valid until {{EXPIRATION_DATE}}. After this date, pricing may be subject to change.

### Payment Terms
- {{PERCENTAGE}}% due upon contract signing
- {{PERCENTAGE}}% due at {{MILESTONE}}
- {{PERCENTAGE}}% due upon completion

Invoices are payable within {{NET_DAYS}} days. Late payments may incur {{LATE_FEE}}% monthly fee.

### Confidentiality
Both parties agree to maintain confidentiality of proprietary information shared during this engagement.

### Intellectual Property
- Client retains ownership of all client-provided materials
- {{OUR_COMPANY}} retains ownership of methodologies and frameworks
- Deliverables are licensed to Client for use
- Work product ownership transfers upon final payment

### Cancellation
Either party may terminate with {{NOTICE_PERIOD}} days written notice. Client will be invoiced for work completed through termination date.

### Warranties
We warrant that services will be performed in a professional manner consistent with industry standards.

### Liability
Our liability is limited to the total fees paid for this engagement.

### Acceptance
This proposal is accepted when Client signs and returns, or issues a purchase order referencing this proposal.
```

### Flexible Terms Strategy

**Option Pricing**:
```markdown
## Pricing Options

### Option A: Fixed Fee
**Total: {{TOTAL_PRICE}}**
- Predictable budget
- Fixed scope
- {{PAYMENT_SCHEDULE}}

### Option B: Monthly Retainer
**{{MONTHLY_PRICE}}/month for {{DURATION}} months**
- Flexible scope adjustments
- Cancel with 30-day notice
- Includes {{HOURS}} hours/month

### Option C: Hourly (Not to Exceed)
**Hourly rate: {{HOURLY_RATE}}**
**Budget cap: {{MAX_BUDGET}}**
- Maximum flexibility
- Pay only for time used
- Detailed time tracking provided
```

## Best Practices

### Dos
✓ **Lead with value, not credentials**: Client cares about outcomes first
✓ **Be specific**: "30% improvement" beats "significant improvement"
✓ **Use client's language**: Mirror their terminology and priorities
✓ **Make pricing transparent**: Hidden costs destroy trust
✓ **Include social proof**: Case studies and testimonials are powerful
✓ **Provide options**: Give client agency in decision-making
✓ **Set clear next steps**: Make it easy to say yes

### Don'ts
✗ **Don't use generic templates**: Personalization wins
✗ **Don't bury the pricing**: Transparency builds trust
✗ **Don't over-promise**: Under-promise, over-deliver
✗ **Don't use jargon**: Write clearly for all stakeholders
✗ **Don't forget the timeline**: Clients need to plan
✗ **Don't skip proofreading**: Typos kill credibility
✗ **Don't make it hard to accept**: Simple signature, not complex process

### Proposal Checklist

Before sending:

- [ ] Personalized for this specific client
- [ ] All placeholders replaced
- [ ] Pricing calculations verified
- [ ] Case studies are relevant
- [ ] ROI clearly demonstrated
- [ ] Terms are fair and clear
- [ ] Proofread by fresh eyes
- [ ] Formatted professionally
- [ ] Easy to sign/accept
- [ ] Follow-up plan in place

## Integration Patterns

### With Pricing Calculator
```bash
# Get accurate pricing for proposal
@pricing-calculator calculate \
    --service "consulting" \
    --hours 200 \
    --rate 250 \
    --discount "volume"

# Returns: base, discount, final pricing
```

### With CRM Integration
```bash
# Fetch client information
@crm get-client --name "Acme Corp"

# Populate proposal template
@proposal-generator create \
    --template "consulting-services" \
    --client "Acme Corp" \
    --auto-populate true
```

## Templates Library

Create reusable templates for:

1. **By Service Type**
   - Consulting services
   - Software licensing
   - Product sales
   - Managed services
   - Training & workshops

2. **By Deal Size**
   - Small ($5K-$25K): Streamlined, 2-3 pages
   - Medium ($25K-$100K): Standard, 5-8 pages
   - Enterprise ($100K+): Comprehensive, 10-20 pages

3. **By Industry**
   - Technology/SaaS
   - Healthcare
   - Finance
   - Retail
   - Manufacturing

Remember: A winning proposal tells a compelling story of transformation from their current pain to desired future state.
