# Stakeholder Communication Skill

Emergency notification systems, communication chains, status update templates, family reunification, and stakeholder management during emergencies.

## Emergency Notification Systems

### Multi-Channel Notification Strategy

**Channel Hierarchy** (Deploy in this order):
```markdown
1. PRIMARY: Mass notification system (SMS/Email/App)
   - Fastest reach
   - Documented delivery
   - Two-way capability

2. SECONDARY: Building systems
   - Fire alarm / PA system
   - Digital signage
   - Desktop alerts

3. TERTIARY: Phone tree
   - Voice calls
   - Human contact
   - For those without email/mobile

4. BACKUP: Social media
   - Twitter/X
   - Facebook
   - LinkedIn
   - Company website

5. TRADITIONAL: Media
   - Local news
   - Radio
   - TV
```

### Mass Notification System Requirements

**Essential Features**:
- [ ] Multi-channel delivery (SMS, email, voice, app)
- [ ] Geofencing / location-based targeting
- [ ] Opt-in/opt-out management
- [ ] Two-way communication capability
- [ ] Template library
- [ ] Contact list management
- [ ] Delivery confirmation tracking
- [ ] Mobile app with push notifications
- [ ] API for integration
- [ ] 99.9%+ uptime guarantee
- [ ] Redundant infrastructure
- [ ] Emergency override capability

**Message Delivery Tracking**:
```json
{
  "message_id": "EMERG-2025-001",
  "sent": "2025-01-15T14:30:00Z",
  "total_recipients": 1250,
  "delivered": {
    "sms": 1200,
    "email": 1150,
    "voice": 950,
    "app_push": 1100
  },
  "failed": {
    "sms": 50,
    "email": 100,
    "voice": 300,
    "app_push": 150
  },
  "opened": {
    "email": 890,
    "app_push": 980
  },
  "responded": 450,
  "delivery_rate": 96.0
}
```

### Notification Message Templates

**Alert Message Structure**:
```
[ALERT LEVEL] [EMERGENCY TYPE]

WHAT: [One sentence description]
WHERE: [Location/affected area]
WHEN: [Time/duration]
ACTION: [What recipient should do immediately]

Additional details: [Link to webpage]
Updates: [How/where/when updates will be provided]

Issued: [Time] by [Authority]
Message ID: [Tracking number]
```

**Alert Levels**:

**LEVEL 1 - INFORMATIONAL** (Green):
```
INFORMATIONAL: Scheduled Fire Drill

WHAT: Fire evacuation drill will be conducted
WHERE: All buildings
WHEN: Today at 2:00 PM, duration 30 minutes
ACTION: Participate in drill, evacuate to assigned assembly points

This is a drill. Normal operations will resume by 2:30 PM.

Details: emergency.company.com/drill-2025-01
Updates: No further alerts unless drill extended

Issued: 1:45 PM by Emergency Management
Message ID: INFO-2025-015
```

**LEVEL 2 - ADVISORY** (Yellow):
```
ADVISORY: Severe Weather Watch

WHAT: Severe thunderstorm watch issued for our area
WHERE: All locations in [County]
WHEN: 4:00 PM - 10:00 PM today
ACTION: Monitor weather, be prepared to shelter if warning issued

Stay indoors if possible. Shelter locations: [Building A Lobby, Building B Cafeteria]

Details: emergency.company.com/weather
Updates: Will notify immediately if upgraded to WARNING

Issued: 2:15 PM by Emergency Management
Message ID: ADV-2025-042
```

**LEVEL 3 - WARNING** (Orange):
```
WARNING: Shelter-in-Place Order

WHAT: Hazardous materials incident reported nearby
WHERE: 2-mile radius including our facility
WHEN: Effective immediately, estimated 2-4 hours
ACTION: GO INSIDE NOW. Close all windows and doors. Turn off HVAC.

Move to interior rooms. Do not leave building.
Monitor emergency.company.com for updates every 30 min.

Details: emergency.company.com/shelter
Updates: Next update by 3:00 PM or when situation changes

Issued: 1:30 PM by Emergency Management
Message ID: WARN-2025-008
```

**LEVEL 4 - EMERGENCY** (Red):
```
EMERGENCY: Evacuate Immediately

WHAT: Fire alarm activated - possible fire in Building A
WHERE: Building A - ALL FLOORS
WHEN: NOW
ACTION: EVACUATE IMMEDIATELY to Assembly Point B

Use stairs only. Do not use elevators.
Do not return to building for any reason.
Report to Assembly Point B for accountability.

This is NOT a drill.

Details: emergency.company.com/active
Updates: Continuous via app and website

Issued: 2:47 PM by Emergency Management
Message ID: EMERG-2025-001
```

### Phone Tree Structure

**Design Principles**:
- Each person calls 3-5 people (span of control)
- Multiple layers for redundancy
- Backup contacts for each position
- 24/7 contact information
- Regular testing (quarterly)

**Phone Tree Example**:
```
Emergency Coordinator
├── Branch 1 Leader (Dept A, B, C)
│   ├── Dept A Manager
│   │   ├── Team Lead 1 → 5 employees
│   │   ├── Team Lead 2 → 5 employees
│   │   └── Team Lead 3 → 5 employees
│   ├── Dept B Manager
│   │   ├── Team Lead 1 → 5 employees
│   │   └── Team Lead 2 → 5 employees
│   └── Dept C Manager
│       └── Team Lead 1 → 5 employees
├── Branch 2 Leader (Dept D, E, F)
│   └── [Similar structure]
└── Branch 3 Leader (Remote/Field)
    └── [Similar structure]
```

**Phone Tree Protocol**:
```markdown
WHEN YOU RECEIVE THE CALL:
1. Listen carefully to message
2. Write down key information
3. Ask questions if unclear
4. Confirm you understand
5. Immediately call your assigned contacts
6. If you reach voicemail:
   - Leave detailed message
   - Try alternate number
   - Try text/email
7. If you cannot reach someone after 3 attempts:
   - Note it
   - Call their backup
   - Report to your caller
8. Once all contacts made, call back to confirm completion
9. Estimated time: Should complete within 30 minutes
```

**Phone Tree Message Script**:
```
"This is [Your Name] with an emergency notification.

[EMERGENCY TYPE] has occurred at [LOCATION].

ACTION REQUIRED: [Specific action - evacuate, shelter, stay home, etc.]

TIMING: [When to take action]

ADDITIONAL INFO: Check [emergency website/hotline] for updates.

Do you understand and can you repeat back the action required?

[Confirm understanding]

Now please call your assigned contacts immediately and relay this message.

Thank you."
```

## Communication Chain of Command

### Organizational Communication Structure

```
┌─────────────────────────────────────────────────┐
│         INCIDENT COMMANDER                      │
│    (Overall authority & communication approval) │
└────────────┬────────────────────────────────────┘
             │
    ┌────────┴────────┐
    ▼                 ▼
┌─────────────┐  ┌──────────────────────┐
│   SAFETY    │  │ PUBLIC INFORMATION   │
│   OFFICER   │  │      OFFICER         │
└─────────────┘  └──────┬───────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
    INTERNAL       EXTERNAL         MEDIA
    COMMS          COMMS           RELATIONS
        │               │               │
        ▼               ▼               ▼
    Employees      Families         Press
    Management     Customers        Social Media
                   Partners
                   Community
```

### Role-Specific Communication Responsibilities

**Incident Commander**:
```markdown
APPROVES:
- All external communications
- Major announcements
- Policy decisions
- Resource allocation announcements

COMMUNICATES WITH:
- Senior leadership
- Government officials
- Key stakeholders (direct)
- Public (through PIO)
```

**Public Information Officer (PIO)**:
```markdown
RESPONSIBILITIES:
- Develops all external messages
- Manages media relations
- Coordinates social media
- Monitors public perception
- Provides talking points
- Conducts press briefings

MUST COORDINATE WITH:
- Incident Commander (approval)
- Legal (review)
- HR (employee impact)
- Safety (technical accuracy)

COMMUNICATION OUTPUTS:
- Press releases
- Media advisories
- Social media posts
- Website updates
- Talking points
- Q&A documents
```

**Safety Officer**:
```markdown
RESPONSIBILITIES:
- Safety-related communications
- Hazard warnings
- Protective action recommendations
- Incident safety briefings

COMMUNICATES:
- Safety concerns to IC
- Hazards to all personnel
- Protective measures to public (through PIO)
```

**HR Representative**:
```markdown
RESPONSIBILITIES:
- Employee notifications
- Family notifications (if applicable)
- Benefits/support information
- Return-to-work communication
- Employee hotline management

COMMUNICATES WITH:
- All employees
- Families (critical incidents)
- Employee assistance programs
- Unions (if applicable)
```

**Department Managers**:
```markdown
RESPONSIBILITIES:
- Relay emergency notifications
- Account for their personnel
- Provide status updates
- Answer employee questions (using approved talking points)
- Monitor employee wellbeing

RECEIVE FROM:
- Emergency notifications
- Status updates
- Talking points
- Return-to-work instructions

REPORT TO:
- Personnel accountability
- Department status
- Employee concerns
- Resource needs
```

## Status Update Templates

### Update Frequency Standards

**Active Emergency Phase**:
- First update: Within 1 hour of incident
- Subsequent updates: Every 2-4 hours or when status changes
- Minimum: Every 6 hours even if no change

**Stabilization Phase**:
- Updates: Every 6-12 hours
- Daily summary updates
- As significant developments occur

**Recovery Phase**:
- Daily updates for first week
- Then every 2-3 days
- Weekly until full resolution

### Initial Notification Template

**Subject**: EMERGENCY ALERT: [Emergency Type] - [Date/Time]

```markdown
EMERGENCY NOTIFICATION

INCIDENT: [Emergency type and brief description]

TIME: [When incident occurred]

LOCATION: [Specific location]

STATUS: [Current situation - contained, ongoing, resolved]

IMPACT:
- Injuries: [Number and severity, or "None reported"]
- Damage: [Description]
- Operations: [Impact on business/services]
- Affected personnel: [Number]

IMMEDIATE ACTIONS TAKEN:
- [Action 1]
- [Action 2]
- [Action 3]

CURRENT ACTIONS:
- [Ongoing response activities]

PERSONNEL INSTRUCTIONS:
[What employees/stakeholders should do]

NEXT UPDATE: [When to expect next communication]

CONTACT INFORMATION:
Emergency Hotline: [Number]
Email: [Address]
Website: [URL]

Issued by: [Name/Title]
Time: [Timestamp]
```

### Ongoing Update Template

**Subject**: UPDATE #[X]: [Emergency Type] - [Current Status]

```markdown
EMERGENCY UPDATE #[X]

INCIDENT: [Emergency type]
UPDATE TIME: [Timestamp]
INCIDENT TIME: [Original time] (Duration: [X hours])

CURRENT STATUS: [Summary of current situation]

CHANGES SINCE LAST UPDATE:
- [What has changed]
- [New developments]
- [Updated information]

CURRENT SITUATION:
- Injuries/Impact: [Updated numbers/status]
- Response activities: [What's being done now]
- Containment: [Progress made]
- Timeline: [Expected duration]

PERSONNEL STATUS:
- Accounted for: [Number/percentage]
- Affected: [Number and status]
- Relocated: [If applicable]

OPERATIONS IMPACT:
- [Affected facilities/services]
- [Expected resumption timeline]
- [Alternative arrangements]

WHAT YOU NEED TO DO:
[Current instructions for stakeholders]

RESOURCES AVAILABLE:
- Employee assistance: [Contact]
- Facility updates: [Where to check]
- Questions: [Who to contact]

NEXT UPDATE: [When]

APPRECIATION:
[Acknowledge responders, cooperation, etc.]

Issued by: [Name/Title]
Time: [Timestamp]
Update: [X of estimated Y]
```

### Resolution/All-Clear Template

**Subject**: ALL CLEAR: [Emergency Type] Resolved - Normal Operations Resume

```markdown
ALL CLEAR NOTIFICATION

INCIDENT: [Emergency type]
STATUS: RESOLVED
RESOLUTION TIME: [Timestamp]
TOTAL DURATION: [X hours/days]

FINAL STATUS:
- Situation: Fully resolved
- Safety: Area/facility declared safe
- Impact: [Final summary]
- All personnel accounted for: [Confirm]

OPERATIONS:
- Normal operations resume: [Date/time]
- Affected areas accessible: [Date/time]
- Any restrictions: [If applicable]

INCIDENT SUMMARY:
- What happened: [Brief description]
- Response actions: [What was done]
- Outcome: [Results]

FOLLOW-UP ACTIONS:
- Investigation: [If applicable]
- Repairs/remediation: [Timeline]
- Lessons learned review: [Scheduled]
- Support services: [Available resources]

APPRECIATION:
[Thank responders, employees, partners for cooperation]

RESOURCES:
- Post-incident support: [EAP, counseling, etc.]
- Questions: [Contact information]
- Detailed report: [When available]

RETURN TO NORMAL:
[Specific instructions for resuming operations]

Issued by: [Name/Title]
Time: [Timestamp]
Final update in series of: [Total updates sent]
```

### Family Notification Template (Critical Incident)

**Subject**: URGENT: Family Notification - [Incident Type]

```markdown
Dear [Family Member Name],

We are reaching out to inform you about an incident involving [Employee Name]
that occurred at [Location] on [Date] at approximately [Time].

INCIDENT INFORMATION:
[Brief, factual description of what happened]

[EMPLOYEE NAME]'S STATUS:
[Specific information about the individual]
- Current location: [Hospital, home, etc.]
- Condition: [As much as can be shared]
- Medical care: [Being provided if applicable]

WHAT WE ARE DOING:
- [Support being provided]
- [Company representative assigned]
- [Resources available]

WHAT YOU CAN DO:
- Contact: [Company representative name and number - available 24/7]
- Visit: [If applicable and appropriate]
- Information: [Where to get updates]

SUPPORT AVAILABLE:
- Company representative: [Name, phone - available 24/7]
- Employee assistance program: [Contact information]
- [Other resources]

We understand this is difficult news. Please know that [employee name]'s
wellbeing is our top priority. We are here to support both [him/her] and
your family in every way possible.

Please contact [representative name] at [number] immediately. [He/She] is
available 24/7 and will be your primary point of contact.

Additional updates will be provided as the situation develops.

Sincerely,

[Name]
[Title]
[Contact Information]

Sent: [Timestamp]
```

## Family Reunification Communication

### Reunification Center Operations

**Setup Communication**:
```markdown
REUNIFICATION CENTER ESTABLISHED

LOCATION: [Full address]
OPEN: [Date/time] - [Expected closing time]
HOURS: [Schedule]

WHO SHOULD COME:
- Family members seeking information about employees/affected persons
- Individuals seeking reunification with family members

WHAT TO BRING:
- Photo identification
- Information about person you're seeking (name, description, last known location)

SERVICES AVAILABLE:
- Personnel accounting status
- Reunification with employees/family
- Information about incident
- Support services
- Refreshments
- Childcare (if applicable)

ALTERNATIVE CONTACT:
If unable to come in person:
- Hotline: [Number]
- Email: [Address]
- Website: [URL for status check]

UPDATES:
[How often center information will be updated]

Map and directions: [Link]

For immediate emergencies: Call 911
For urgent questions: [24/7 hotline]
```

**Status Inquiry Response Template**:
```markdown
Thank you for contacting us about [Person's Name].

CURRENT STATUS: [Choose one:]

□ SAFE AND ACCOUNTED FOR
  [Person] has been accounted for and is safe.
  [He/She] is currently [location/status].
  Reunification: [Process to reunify]

□ SAFE - UNAVAILABLE FOR CONTACT
  [Person] has been accounted for and is safe.
  [He/She] is currently unable to be contacted because [reason].
  Expected contact: [Timeframe]

□ SAFE - RECEIVING MEDICAL ATTENTION
  [Person] has been accounted for.
  [He/She] is receiving medical attention at [Hospital/Location].
  Condition: [What can be shared]
  Contact: [Hospital contact for family]

□ SEARCHING
  We are actively working to locate [Person].
  Last known location: [If known]
  Expected update: [Timeframe]
  Please contact us if you hear from [him/her].

□ INFORMATION NEEDED
  We need additional information to locate [Person].
  Please provide: [Specific details needed]

NEXT STEPS: [What the inquirer should do]

CONTACT INFORMATION:
Your name: [Confirmed]
Your phone: [Confirmed]
Relationship: [Confirmed]
Best time to reach you: [Confirmed]

We will contact you:
- Immediately when status changes
- At scheduled update times: [Times]
- [Other conditions]

Questions or concerns: Contact [Name] at [Number] (24/7)

Thank you,
[Reunification Center Team]
Updated: [Timestamp]
```

### Hotline Management

**Hotline Script for Call Operators**:

**OPENING**:
```
"Emergency Information Hotline, this is [Your Name].
How can I help you today?"

[Listen to inquiry]

"Let me help you with that. To better assist you, I need to ask a few questions."
```

**INFORMATION GATHERING**:
```markdown
1. "May I have your full name please?"
   [Record: Caller name]

2. "What is your relationship to the person you're inquiring about?"
   [Record: Relationship]

3. "What is the full name of the person you're asking about?"
   [Record: Person of interest]

4. "Do you know where [Person] was when the incident occurred?"
   [Record: Last known location]

5. "When did you last have contact with [Person]?"
   [Record: Last contact time]

6. "What is the best number to reach you?"
   [Record: Callback number]

7. "Are you calling from a safe location?"
   [Record: Caller safety]
```

**INFORMATION PROVIDING**:
```markdown
CHECK DATABASE/STATUS BOARD

IF PERSON FOUND:
"Good news - [Person] has been accounted for and is [status].
[Additional details as appropriate and authorized to share]

Would you like information about [reunification center/hospital visit/contact method]?"

IF PERSON NOT YET LOCATED:
"We are actively working to account for everyone. [Person] has not yet been
located, but that doesn't necessarily mean anything is wrong. Many people
evacuate to different locations or are unable to check in immediately.

We will continue searching and will contact you immediately when we have
information.

Can I confirm your contact information? [Verify]

We will call you:
- As soon as we locate [Person]
- With general updates every [X hours]
- If we need additional information

Is there anything else I can help you with right now?"
```

**CLOSING**:
```
"Thank you for calling. We will be in touch as soon as we have information.

Your reference number is: [Number]
Keep this for your records.

Is there anything else you need right now?

[If no] Thank you for your patience. We'll speak with you soon."
```

**DIFFICULT CALLS**:
```markdown
EMOTIONAL/DISTRESSED CALLER:
"I understand this is very stressful. Let me do everything I can to help you."
[Remain calm, speak slowly, be empathetic]
[Offer to connect with counselor/support if available]

ANGRY CALLER:
"I understand your frustration. Let me see what information I can provide."
[Don't take it personally, stay professional]
[Focus on what you CAN do, not what you can't]

MEDIA CALLING:
"All media inquiries should be directed to our Public Information Officer.
The number is [PIO number]. They will be able to assist you."
[Don't provide any information]
[Don't confirm or deny anything]
[Log the call]

REPEAT CALLER (No new info):
"I know you're anxious for information. We have your contact information and
will reach out immediately when status changes. Calling repeatedly won't make
us locate [Person] faster, but it does tie up lines for others who may need
to reach us. We WILL call you as promised. Thank you for understanding."
```

## Stakeholder-Specific Communication Strategies

### Employees

**Communication Priorities**:
1. Safety and wellbeing
2. Incident status
3. Their role/expectations
4. Support available
5. Operational impact
6. Return to work

**Channels**:
- Mass notification (immediate)
- All-hands meeting (within hours)
- Email updates (regular)
- Intranet/employee portal
- Manager cascade (for details)
- Employee hotline (for questions)

**Key Messages**:
```markdown
IMMEDIATELY:
"Your safety is our priority. [Action required]."

ONGOING:
"Here's what we know, what we're doing, and what we need from you."

RESOLUTION:
"Thank you for your patience and cooperation. Here's what happens next."
```

### Families

**Communication Priorities**:
1. Status of their family member
2. How to make contact
3. Support available
4. How to get updates

**Channels**:
- Direct phone call (critical incidents)
- Email (non-critical updates)
- Reunification center
- Family hotline
- Family portal/website

**Tone**: Empathetic, clear, supportive, timely

### Customers/Clients

**Communication Priorities**:
1. Impact on service/products
2. Alternative arrangements
3. Timeline for restoration
4. How to get help

**Channels**:
- Email
- Website banner
- Social media
- Account managers (key clients)
- Customer service hotline update

**Key Messages**:
```markdown
TRANSPARENCY:
"Here's what happened and how it affects you."

ASSURANCE:
"Here's what we're doing to minimize impact."

GUIDANCE:
"Here's what you can do / alternative options."

COMMITMENT:
"Here's when we expect to be back to normal."
```

### Partners/Vendors

**Communication Priorities**:
1. Impact on partnership/supply chain
2. Alternative arrangements needed
3. Expected duration
4. How to coordinate

**Channels**:
- Direct email/call to key contacts
- Partner portal update
- Partner hotline

### Media

**Communication Priorities**:
1. Factual incident information
2. Actions being taken
3. Impact assessment
4. Spokesperson availability

**Channels**:
- Press release
- Media advisory
- Press conference (major incidents)
- Social media
- Website media center

**Response Timeframe**:
- Initial response: Within 6 hours
- Full statement: Within 24 hours
- Ongoing updates: Daily or as situation changes

### Regulatory Agencies

**Communication Priorities**:
1. Compliance notification
2. Technical details
3. Corrective actions
4. Investigation cooperation

**Channels**:
- Official notification (as required by regulation)
- Direct contact with agency
- Written report
- Follow-up meetings

**Tone**: Professional, cooperative, detailed, compliant

## Communication Best Practices

### DO's:
- Communicate early and often
- Be honest and transparent
- Use multiple channels
- Confirm message receipt
- Provide specific actions
- Set expectations for next update
- Show empathy
- Acknowledge uncertainty when appropriate
- Keep messaging consistent
- Document all communications

### DON'Ts:
- Don't delay notification hoping for more info
- Don't speculate or guess
- Don't minimize the situation
- Don't blame others
- Don't provide unverified information
- Don't go silent after initial notification
- Don't use jargon
- Don't make promises you can't keep
- Don't forget to update when situation changes
- Don't neglect internal stakeholders

### Message Principles:

**CLEAR**:
- Use simple language
- Short sentences
- Active voice
- Specific actions

**CONCISE**:
- Essential information only
- Bullets, not paragraphs
- One message, one topic

**CREDIBLE**:
- Facts, not speculation
- Source attribution
- Honest about unknowns
- Consistent across channels

**COMPASSIONATE**:
- Acknowledge impact
- Express concern
- Offer support
- Respect dignity

---

*This skill provides comprehensive stakeholder communication frameworks for effective emergency notification, status updates, and family reunification during crisis situations.*
