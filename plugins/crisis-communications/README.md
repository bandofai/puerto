# Crisis Communications Plugin

Crisis communication management specialist for crisis response planning, press releases, stakeholder messaging, social media monitoring, and response coordination.

## Overview

The Crisis Communications plugin provides agents for managing organizational crises using proven frameworks (SCCT - Situational Crisis Communication Theory, Image Restoration Theory), rapid response protocols, and multi-channel stakeholder communication.

## Agents

### 1. crisis-planner (Sonnet, Skill-Aware)
Creates comprehensive crisis communication plans with scenarios, response teams, protocols, and escalation procedures.

**Use for**: Crisis preparedness, response planning, scenario development, communication protocols

**Example**:
```
Use crisis-planner to create crisis communication plan for SaaS company.
Scenarios: Data breach, service outage, executive misconduct, product defect, negative press
Include: Crisis team roles, decision tree, communication templates, escalation paths
Framework: SCCT (Situational Crisis Communication Theory)
Stakeholders: Customers, employees, investors, media, regulators
```

### 2. press-release-writer (Sonnet, Skill-Aware)
Writes press releases for crisis situations with appropriate tone, transparency, and messaging.

**Use for**: Official statements, media announcements, crisis disclosures, corrective actions

**Example**:
```
Use press-release-writer for data breach announcement.
Incident: Unauthorized access to customer database (50K users affected)
Data exposed: Email addresses, names (no financial data)
Actions taken: Breach contained, passwords reset, forensics underway, authorities notified
Tone: Transparent, accountable, reassuring
Include: What happened, impact, actions taken, customer guidance, contact info
```

### 3. stakeholder-messenger (Sonnet, Skill-Aware)
Crafts targeted messages for different stakeholder groups: customers, employees, investors, partners, regulators.

**Use for**: Customer notifications, employee updates, investor communications, regulatory responses

**Example**:
```
Use stakeholder-messenger for service outage communications.
Incident: 6-hour outage affecting 80% of customers
Stakeholder groups:
- Customers: Email + in-app notification
- Employees: Internal memo with customer handling guidance
- Investors: Board update with financial impact
- Partners: API status and compensation details
Timeline: Immediate (during crisis), post-resolution update, follow-up
```

### 4. social-monitor (Sonnet, WebSearch, Skill-Aware)
Monitors social media sentiment, identifies emerging issues, and drafts rapid responses.

**Use for**: Social listening, sentiment tracking, rapid response, misinformation correction

**Example**:
```
Use social-monitor during product recall crisis.
Platforms: Twitter, LinkedIn, Reddit, Facebook
Keywords: [Product name], recall, safety, defect
Tasks:
- Identify trending concerns and misinformation
- Draft holding statements for social teams
- Recommend influencer/community engagement
- Flag escalation triggers (viral posts, media pickup)
```

## Skills

### crisis-communication
Crisis communication frameworks and best practices:
- **SCCT Framework**: Crisis types, response strategies (denial, diminishment, rebuilding)
- **Image Restoration Theory**: Strategies (denial, evasion, reducing offensiveness, corrective action, mortification)
- **Response Speed**: Golden Hour (first 60 minutes), first 24 hours, ongoing
- **Stakeholder Segmentation**: Customers, employees, investors, media, regulators, general public
- **Message Pillars**: Transparency, accountability, empathy, action
- **Channel Strategy**: Press releases, social media, email, website, media interviews
- **Legal Considerations**: Disclosure requirements, liability language, regulatory compliance

## Templates

### crisis-communication-plan-template.md
Comprehensive crisis preparedness plan: Crisis team structure, scenario playbooks, decision trees, communication protocols, stakeholder matrices, template library, training requirements.

### press-release-template.md
Crisis press release format: Headline, lead paragraph (5 W's), incident details, impact assessment, actions taken, customer guidance, contact information, boilerplate.

### stakeholder-update-template.md
Stakeholder-specific messaging templates for customers, employees, investors, partners, and regulators with appropriate tone and detail level.

### social-media-response-playbook.md
Social media crisis response guide: Monitoring keywords, response timeframes, escalation triggers, holding statements, engagement guidelines, misinformation correction protocols.

## Workflows

### Crisis Response Workflow
```
1. Immediate response (First Hour)
Use crisis-planner to activate crisis team and assess situation

2. Official statement (Within 6 hours)
Use press-release-writer to draft initial press release

3. Stakeholder notifications (Within 24 hours)
Use stakeholder-messenger for targeted communications to all groups

4. Social monitoring (Ongoing)
Use social-monitor to track sentiment and respond to concerns

5. Follow-up (Post-resolution)
Use press-release-writer and stakeholder-messenger for resolution announcement
```

### Crisis Preparedness
```
Use crisis-planner to develop comprehensive crisis communication plan:
- Identify top 10 crisis scenarios
- Define crisis team (spokesperson, legal, PR, executives)
- Create decision trees for response strategy
- Develop message templates for each scenario
- Establish escalation protocols
- Schedule training and simulations
```

## Requirements Met

✅ Role: Crisis communication management specialist
✅ Crisis communication plans: crisis-planner with SCCT framework
✅ Press release drafting: press-release-writer with crisis-specific templates
✅ Stakeholder messaging: stakeholder-messenger for segmented communications
✅ Social media monitoring: social-monitor with WebSearch for real-time tracking
✅ Response coordination: Workflow integration across all agents
✅ Tools: Monitoring tools (WebSearch), templates, email (messaging capabilities)

## Key Features

✓ **SCCT Framework**: Evidence-based crisis response strategies
✓ **Golden Hour Protocol**: Rapid response within first 60 minutes
✓ **Multi-Stakeholder**: Targeted messaging for 6+ stakeholder groups
✓ **Social Listening**: Real-time monitoring and rapid response
✓ **Legal Compliance**: Disclosure and liability language
✓ **Image Restoration**: Repair organizational reputation
✓ **Crisis Scenarios**: Data breach, outage, recall, misconduct, negative press

## Crisis Response Speed

- **Immediate (0-1 hour)**: Crisis team activation, initial assessment, holding statement
- **First 6 hours**: Official press release, regulatory notifications
- **First 24 hours**: All stakeholder groups notified, social monitoring active
- **Ongoing**: Daily updates until resolution, sentiment tracking
- **Post-crisis**: Resolution announcement, lessons learned, plan updates

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 1 comprehensive crisis-communication skill with SCCT and frameworks
- ✅ 4 professional templates covering all crisis scenarios
- ✅ Complete README with workflows and response timelines

Closes #74
