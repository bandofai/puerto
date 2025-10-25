# Email Automation Workflow Template

**Use this template to design and document automated email workflows, drip campaigns, and trigger-based sequences.**

---

## Workflow Overview

**Workflow Name**: {{workflow_name}}

**Workflow Type**: {{type}}
- [ ] Welcome Series (Onboarding)
- [ ] Abandoned Cart Recovery
- [ ] Browse Abandonment
- [ ] Post-Purchase Nurture
- [ ] Lead Nurture (Educational Drip)
- [ ] Re-engagement / Win-back
- [ ] Trial Nurture (SaaS)
- [ ] Event-Based Triggered
- [ ] Birthday/Anniversary
- [ ] Custom: {{custom_type}}

**Business Goal**: {{goal}}
(e.g., Activate new users, recover lost revenue, build loyalty, move leads to sales-qualified)

**Target Audience**: {{audience_description}}

**Expected Impact**:
- Primary Metric: {{metric}} (Target: {{target}})
- Estimated Conversion Rate: {{conversion_rate}}%
- Estimated Revenue Impact: {{revenue_estimate}}

---

## Entry Criteria (Triggers)

### Primary Trigger

**Trigger Event**: {{trigger_event}}

Examples:
- User signs up for email list
- Account created
- Product added to cart (no purchase within 3 hours)
- Purchase completed
- Trial started
- No login for 30 days
- Birthday is tomorrow

### Additional Entry Conditions

Users must meet ALL of these conditions to enter workflow:

- [ ] {{condition_1}}
- [ ] {{condition_2}}
- [ ] {{condition_3}}
- [ ] Email subscribed = true
- [ ] Not currently in conflicting workflow

### Re-Entry Rules

**Can users enter this workflow multiple times?** {{yes/no}}

**If YES, under what conditions?**
- [ ] Completed previous instance of workflow
- [ ] Minimum {{X}} days since last entry
- [ ] Different product/category than previous entry
- [ ] Other: {{specify}}

**If NO, how to handle re-triggers?**
- [ ] Ignore subsequent triggers
- [ ] Update data but don't re-enter
- [ ] Exit current instance and restart

---

## Exit Criteria

Users will exit the workflow when ANY of these conditions are met:

- [ ] **Goal achieved**: {{goal_description}} (e.g., Made purchase, activated account, attended webinar)
- [ ] **Unsubscribed**: User opts out of emails
- [ ] **Time elapsed**: {{X}} days have passed since workflow entry
- [ ] **Negative action**: {{action}} (e.g., Spam complaint, account deleted)
- [ ] **Entered conflicting workflow**: {{workflow_name}}
- [ ] **Custom condition**: {{specify}}

---

## Workflow Sequence

### Email 1: {{email_1_name}}

**Timing**: {{timing}}
- [ ] Immediate (upon trigger)
- [ ] {{X}} hours after trigger
- [ ] {{X}} days after trigger
- [ ] Next {{day}} at {{time}}
- [ ] Optimal send time per subscriber

**Subject Line**: {{subject_line}}

**Preview Text**: {{preview_text}}

**Content Summary**:
{{brief_description_of_email_content}}

**Key Elements**:
- **Main Message**: {{main_message}}
- **Value Proposition**: {{value_prop}}
- **Social Proof**: {{testimonial_or_stats}}
- **Primary CTA**: {{cta_text}} → {{destination}}
- **Secondary CTA** (optional): {{cta_text}} → {{destination}}

**Personalization**:
- {{token_1}}: {{usage_description_1}}
- {{token_2}}: {{usage_description_2}}
- {{token_3}}: {{usage_description_3}}

**Goals / Success Metrics**:
- Open Rate Target: {{percentage}}%
- Click Rate Target: {{percentage}}%
- Specific Action: {{action}}

**File Location**: `emails/{{workflow_slug}}/email-1-{{slug}}.html`

---

### Conditional Split 1 (Optional)

**Decision Point**: After Email 1, check condition

**Condition**: {{condition_to_check}}

Examples:
- Opened Email 1?
- Clicked primary CTA?
- Made purchase?
- Profile complete?
- Lead score > 50?

**IF {{condition}} is TRUE**:
→ Go to Email 2A: {{email_2a_name}}

**IF {{condition}} is FALSE**:
→ Go to Email 2B: {{email_2b_name}}

**Default Path** (if data unavailable):
→ Go to Email 2B

---

### Email 2: {{email_2_name}}

**Timing**: {{timing}} after Email 1
- [ ] {{X}} hours later
- [ ] {{X}} days later
- [ ] Immediate (if condition met)
- [ ] Next {{day}} at {{time}}

**Subject Line**: {{subject_line}}

**Preview Text**: {{preview_text}}

**Content Summary**:
{{brief_description}}

**Key Elements**:
- **Main Message**: {{main_message}}
- **Value Proposition**: {{value_prop}}
- **Social Proof**: {{testimonial_or_stats}}
- **Primary CTA**: {{cta_text}} → {{destination}}

**Personalization**:
- {{token_1}}: {{usage_description}}
- {{token_2}}: {{usage_description}}

**Goals / Success Metrics**:
- Open Rate Target: {{percentage}}%
- Click Rate Target: {{percentage}}%
- Specific Action: {{action}}

**File Location**: `emails/{{workflow_slug}}/email-2-{{slug}}.html`

---

### Email 3: {{email_3_name}}

**Timing**: {{timing}} after Email 2

**Subject Line**: {{subject_line}}

**Preview Text**: {{preview_text}}

**Content Summary**:
{{brief_description}}

**Key Elements**:
- **Main Message**: {{main_message}}
- **Value Proposition**: {{value_prop}}
- **Social Proof**: {{testimonial_or_stats}}
- **Primary CTA**: {{cta_text}} → {{destination}}

**Personalization**:
- {{token_1}}: {{usage_description}}
- {{token_2}}: {{usage_description}}

**Goals / Success Metrics**:
- Open Rate Target: {{percentage}}%
- Click Rate Target: {{percentage}}%
- Specific Action: {{action}}

**File Location**: `emails/{{workflow_slug}}/email-3-{{slug}}.html`

---

### Email 4: {{email_4_name}} (Optional)

**Timing**: {{timing}} after Email 3

**Subject Line**: {{subject_line}}

**Preview Text**: {{preview_text}}

**Content Summary**:
{{brief_description}}

**Key Elements**:
- **Main Message**: {{main_message}}
- **Value Proposition**: {{value_prop}}
- **Social Proof**: {{testimonial_or_stats}}
- **Primary CTA**: {{cta_text}} → {{destination}}

**Goals / Success Metrics**:
- Open Rate Target: {{percentage}}%
- Click Rate Target: {{percentage}}%
- Specific Action: {{action}}

**File Location**: `emails/{{workflow_slug}}/email-4-{{slug}}.html`

---

## Workflow Diagram

Visual representation of email sequence flow:

```
[Trigger Event]
     |
     v
[Entry Conditions Check]
     |
     v
[Email 1: {{email_1_name}}]
     |
  Wait {{time}}
     |
     v
[Condition Check: {{condition}}?]
     |
     +----------+----------+
     |                     |
  [TRUE]              [FALSE]
     |                     |
     v                     v
[Email 2A]           [Email 2B]
     |                     |
  Wait {{time}}         Wait {{time}}
     |                     |
     +----------+----------+
                |
                v
         [Email 3]
                |
             Wait {{time}}
                |
                v
       [Goal Achieved?]
                |
         +------+------+
         |             |
      [YES]          [NO]
         |             |
         v             v
      [Exit]      [Email 4]
                       |
                       v
                    [Exit]
```

Or alternative paths:

```
[Trigger]
    |
    v
[Email 1] ─(Opened?)─┬─(Yes)──> [Email 2A - Deep Dive]
                     |              |
                     |           Wait 3d
                     |              |
                     |              v
                     |          [Email 3A]
                     |              |
                     └─(No)───> [Email 2B - Different Angle]
                                    |
                                 Wait 3d
                                    |
                                    v
                                [Email 3B]
                                    |
                                    +────────┬────────+
                                             v
                                       [Email 4 - Final Push]
                                             |
                                             v
                                          [Exit]
```

---

## Timing Schedule

| Email | Timing | Delay from Previous | Day Since Entry |
|-------|--------|---------------------|-----------------|
| Email 1 | {{timing_1}} | Immediate | Day 0 |
| Email 2 | {{timing_2}} | {{delay_2}} | Day {{day_2}} |
| Email 3 | {{timing_3}} | {{delay_3}} | Day {{day_3}} |
| Email 4 | {{timing_4}} | {{delay_4}} | Day {{day_4}} |

**Total Workflow Duration**: {{total_days}} days

**Average Time to Conversion**: {{avg_days}} days (estimated)

---

## Personalization Rules

Customize email content based on user attributes or behavior:

| Element | Personalization Token | Fallback Value | Notes |
|---------|----------------------|----------------|-------|
| Subject Line | {{first_name}} | "there" | Use if available |
| Greeting | {{first_name}} | "friend" | Always personalize greeting |
| Product Name | {{product_name}} | "this item" | For cart/browse abandonment |
| Company Name | {{company}} | N/A | B2B only |
| Discount Code | {{discount_code}} | Generate unique code | Track usage |
| Send Time | {{optimal_send_time}} | 10am local time | If platform supports |

**Dynamic Content Blocks**:

```
IF {{segment}} = "VIP":
    Show exclusive early access offer
ELSE IF {{segment}} = "New Customer":
    Show onboarding resources
ELSE:
    Show standard offer
```

---

## Success Metrics

### Primary Goal

**Goal Description**: {{goal}}

**How to Measure**: {{measurement_method}}

**Target**: {{target_value}}

**Tracking Method**:
- [ ] Conversion pixel on thank-you page
- [ ] UTM parameters in all links
- [ ] Goal tracking in email platform
- [ ] CRM integration for attribution

### Secondary Metrics

| Metric | Target | Actual | Notes |
|--------|--------|--------|-------|
| Workflow Completion Rate | {{percentage}}% | TBD | % who receive all emails |
| Overall Open Rate | {{percentage}}% | TBD | Average across all emails |
| Overall Click Rate | {{percentage}}% | TBD | Average across all emails |
| Conversion Rate | {{percentage}}% | TBD | % who achieve goal |
| Time to Conversion | {{days}} days | TBD | Average days from entry to goal |
| Revenue per Entry | ${{amount}} | TBD | For e-commerce workflows |
| Unsubscribe Rate | <{{percentage}}% | TBD | Should remain low |
| Spam Complaint Rate | <0.1% | TBD | Critical to monitor |

### Engagement Metrics by Email

| Email | Open Rate Target | Click Rate Target | Conversion Rate Target |
|-------|------------------|-------------------|------------------------|
| Email 1 | {{percentage}}% | {{percentage}}% | {{percentage}}% |
| Email 2 | {{percentage}}% | {{percentage}}% | {{percentage}}% |
| Email 3 | {{percentage}}% | {{percentage}}% | {{percentage}}% |
| Email 4 | {{percentage}}% | {{percentage}}% | {{percentage}}% |

---

## Implementation Checklist

### Pre-Launch

**Workflow Configuration**:
- [ ] Entry trigger configured and tested
- [ ] Entry conditions verified
- [ ] Exit conditions configured
- [ ] Re-entry rules set appropriately
- [ ] Workflow does not conflict with other automations
- [ ] Goal tracking implemented
- [ ] Time zone handling configured

**Email Content**:
- [ ] All emails written and approved by stakeholders
- [ ] Subject lines optimized (30-50 characters)
- [ ] Preview text optimized (40-100 characters)
- [ ] Personalization tokens mapped with fallbacks
- [ ] All links tested and working
- [ ] UTM parameters added to all links (utm_source, utm_medium, utm_campaign)
- [ ] Mobile preview checked for all emails
- [ ] Dark mode compatibility verified
- [ ] Images optimized and hosted externally
- [ ] Alt text added to all images
- [ ] Spam score checked (<5/10 for all emails)
- [ ] Unsubscribe link present in all emails
- [ ] Plain text version created for all emails
- [ ] Legal compliance verified (CAN-SPAM, GDPR)

**Technical Setup**:
- [ ] Conditional logic tested (all branches)
- [ ] Default paths configured for edge cases
- [ ] Timing delays verified
- [ ] Send time optimization configured
- [ ] Platform-specific settings configured (suppression lists, etc.)

**Testing**:
- [ ] Test emails sent to internal team
- [ ] All workflow paths tested end-to-end
- [ ] Personalization rendering verified
- [ ] Mobile rendering tested on actual devices
- [ ] Trigger events tested to ensure workflow starts correctly
- [ ] Exit conditions tested
- [ ] No duplicate sends verified

**Analytics**:
- [ ] Analytics dashboard created
- [ ] Conversion tracking tested
- [ ] Attribution model defined
- [ ] Reporting schedule set

### Launch Plan

**Soft Launch** (Recommended):
- [ ] Launch to 10% of eligible audience
- [ ] Monitor for 3-7 days
- [ ] Check for errors, broken links, or issues
- [ ] Review initial performance metrics
- [ ] Make adjustments if needed

**Full Launch**:
- [ ] Scale to 50% of audience
- [ ] Monitor for 1 week
- [ ] If performance meets targets, scale to 100%
- [ ] Continue monitoring weekly

---

## Monitoring Plan

### Daily Monitoring (First 2 Weeks)

- [ ] Check workflow entry rate (users entering)
- [ ] Monitor for errors or failures
- [ ] Check email send volume by sequence position
- [ ] Review spam complaints immediately
- [ ] Check for broken links or technical issues

### Weekly Monitoring (Ongoing)

- [ ] Review overall open and click rates
- [ ] Check conversion rate against target
- [ ] Analyze drop-off points (where do users exit?)
- [ ] Review unsubscribe rate
- [ ] Check goal achievement rate
- [ ] Compare performance to benchmarks

### Monthly Monitoring

- [ ] Calculate ROI (revenue vs. cost)
- [ ] Review email performance trends over time
- [ ] Identify optimization opportunities
- [ ] Update workflow based on learnings
- [ ] A/B test improvements

---

## Optimization Opportunities

### A/B Tests to Run

**Priority 1: Email 1 Subject Line** (Affects entire workflow)
- Control: {{subject_line_control}}
- Variant: {{subject_line_variant}}
- Success Metric: Open rate
- Sample Size: {{sample_size}} per variant
- Duration: {{duration}} days

**Priority 2: Email Timing**
- Control: Email 2 sent {{X}} days after Email 1
- Variant: Email 2 sent {{Y}} days after Email 1
- Success Metric: Overall conversion rate
- Sample Size: {{sample_size}} per variant
- Duration: {{duration}} days

**Priority 3: CTA Copy**
- Control: {{cta_control}}
- Variant: {{cta_variant}}
- Success Metric: Click-through rate
- Sample Size: {{sample_size}} per variant
- Duration: {{duration}} days

### Future Enhancements

- [ ] {{enhancement_1}}
- [ ] {{enhancement_2}}
- [ ] {{enhancement_3}}
- [ ] Add dynamic content blocks for personalization
- [ ] Implement predictive send time optimization
- [ ] Create additional branches based on engagement level
- [ ] Integrate with CRM for lead scoring

---

## Results and Learnings

### Performance Summary (To be completed after running)

**Date Range**: {{start_date}} to {{end_date}}

**Total Entries**: {{total_entries}}

**Overall Results**:
- Workflow Completion Rate: {{percentage}}%
- Average Open Rate: {{percentage}}%
- Average Click Rate: {{percentage}}%
- Conversion Rate: {{percentage}}%
- Total Conversions: {{count}}
- Revenue Generated: ${{amount}}
- ROI: {{multiplier}}x

**Email Performance**:

| Email | Sent | Opens | Clicks | Conversions | Open Rate | Click Rate | Conv Rate |
|-------|------|-------|--------|-------------|-----------|------------|-----------|
| Email 1 | {{sent_1}} | {{opens_1}} | {{clicks_1}} | {{conv_1}} | {{or_1}}% | {{cr_1}}% | {{cvr_1}}% |
| Email 2 | {{sent_2}} | {{opens_2}} | {{clicks_2}} | {{conv_2}} | {{or_2}}% | {{cr_2}}% | {{cvr_2}}% |
| Email 3 | {{sent_3}} | {{opens_3}} | {{clicks_3}} | {{conv_3}} | {{or_3}}% | {{cr_3}}% | {{cvr_3}}% |
| Email 4 | {{sent_4}} | {{opens_4}} | {{clicks_4}} | {{conv_4}} | {{or_4}}% | {{cr_4}}% | {{cvr_4}}% |

### Key Learnings

**What Worked**:
1. {{learning_1}}
2. {{learning_2}}
3. {{learning_3}}

**What Didn't Work**:
1. {{learning_1}}
2. {{learning_2}}
3. {{learning_3}}

**Surprising Insights**:
1. {{insight_1}}
2. {{insight_2}}
3. {{insight_3}}

### Recommended Changes

Based on performance data:

1. **{{change_1}}**: {{rationale}}
2. **{{change_2}}**: {{rationale}}
3. **{{change_3}}**: {{rationale}}

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | {{date}} | Initial workflow creation | {{author}} |
| 1.1 | {{date}} | {{changes}} | {{author}} |
| 2.0 | {{date}} | Major revision based on performance data | {{author}} |

---

## Notes

**Additional Context**:
{{any_additional_notes_or_context}}

**Stakeholders**:
- Owner: {{owner_name}}
- Approver: {{approver_name}}
- Implementer: {{implementer_name}}
- Analyst: {{analyst_name}}

**Related Workflows**:
- {{related_workflow_1}}
- {{related_workflow_2}}

**References**:
- Campaign brief: {{link}}
- Design files: {{link}}
- Original requirement: {{link}}
