# Incident Management Skill

Incident assessment methodologies, severity classification, triage systems, resource allocation, and emergency documentation requirements.

## Incident Assessment Framework

### Initial Assessment Methodology

**METHANE Report Format** (Standard emergency assessment):

```
M - Major Incident Declared? (Yes/No)
E - Exact Location (Address, floor, coordinates)
T - Type of Incident (Fire, medical, hazmat, etc.)
H - Hazards (Present and potential)
A - Access (Best routes, restrictions)
N - Number of Casualties (Dead, injured, unaccounted)
E - Emergency Services (Required and on scene)
```

**Example METHANE Report**:
```
M: YES - Major incident declared
E: 123 Main Street, Building A, 3rd floor east wing
T: Fire with smoke, possible structural damage
H: Heavy smoke, potential collapse, hazmat in adjacent lab
A: North entrance accessible, south blocked by fire
N: 2 injured (minor), 15 evacuated safely, 3 unaccounted
E: Fire dept on scene, EMS requested, police notified
```

### Incident Severity Classification

**SEVERITY MATRIX**:

```markdown
│               │ LOW IMPACT   │ MEDIUM IMPACT    │ HIGH IMPACT      │ CATASTROPHIC     │
│───────────────│──────────────│──────────────────│──────────────────│──────────────────│
│ HIGH          │ MEDIUM       │ HIGH             │ CRITICAL         │ CRITICAL         │
│ LIKELIHOOD    │ Priority 2   │ Priority 1       │ Priority 1       │ Priority 1       │
│               │ 4-hour resp. │ 1-hour response  │ Immediate        │ Immediate        │
│───────────────│──────────────│──────────────────│──────────────────│──────────────────│
│ MEDIUM        │ LOW          │ MEDIUM           │ HIGH             │ CRITICAL         │
│ LIKELIHOOD    │ Priority 3   │ Priority 2       │ Priority 1       │ Priority 1       │
│               │ 24-hr resp.  │ 4-hour response  │ 1-hour response  │ Immediate        │
│───────────────│──────────────│──────────────────│──────────────────│──────────────────│
│ LOW           │ LOW          │ LOW              │ MEDIUM           │ HIGH             │
│ LIKELIHOOD    │ Priority 4   │ Priority 3       │ Priority 2       │ Priority 1       │
│               │ Monitor      │ 24-hr response   │ 4-hour response  │ 1-hour response  │
```

**IMPACT ASSESSMENT CRITERIA**:

**LOW IMPACT**:
- No injuries or minor first aid only
- Minimal property damage (<$10K)
- No operational disruption
- Localized to single room/area
- No media attention
- Resolved in <1 hour

**MEDIUM IMPACT**:
- Minor injuries requiring medical attention
- Moderate property damage ($10K-$100K)
- Limited operational disruption (<4 hours)
- Affects single department/floor
- Potential local media attention
- Resolved in 1-8 hours

**HIGH IMPACT**:
- Serious injuries, hospitalization
- Major property damage ($100K-$1M)
- Significant operational disruption (4-24 hours)
- Affects multiple departments/building
- Certain local/regional media attention
- External agency response required
- Resolved in 8-48 hours

**CATASTROPHIC IMPACT**:
- Fatalities or life-threatening injuries
- Severe property damage (>$1M)
- Extended operational disruption (>24 hours)
- Affects entire facility/organization
- National media attention
- Extended external agency involvement
- Resolution days to weeks

**LIKELIHOOD ASSESSMENT**:
- **HIGH**: Occurs frequently (monthly), known risk
- **MEDIUM**: Occurs occasionally (yearly), identified risk
- **LOW**: Rare occurrence, theoretical risk

### 5-Step Incident Assessment Process

**STEP 1: DETECT & VERIFY** (0-5 minutes)
```markdown
□ Incident reported
□ Source verified (not false alarm)
□ Initial information gathered:
  - What happened?
  - Where exactly?
  - When (time)?
  - Who is affected?
  - How many involved?
□ Scene safety confirmed for assessment
□ Documentation initiated (incident number assigned)
```

**STEP 2: ASSESS & CLASSIFY** (5-15 minutes)
```markdown
□ METHANE report completed
□ Severity classification determined (Low/Medium/High/Critical)
□ Impact categories assessed:
  ☑ Life safety (injuries, fatalities, missing persons)
  ☑ Property (damage extent, value)
  ☑ Environment (contamination, hazmat)
  ☑ Operations (business disruption)
  ☑ Reputation (media, stakeholder impact)
  ☑ Legal/Regulatory (compliance, liability)
□ Trends identified (getting worse/stable/improving)
□ Resource requirements estimated
```

**STEP 3: ACTIVATE RESPONSE** (15-30 minutes)
```markdown
□ Response level determined:
  Level 1: Local response (security/facilities)
  Level 2: Departmental response (add management)
  Level 3: Full ICS activation (crisis team)
  Level 4: External resources (fire/police/EMS)
  Level 5: Multi-agency coordination

□ Appropriate personnel notified
□ ICS structure activated (if Level 3+)
□ Command post established
□ Safety officer assigned
□ Initial actions directed
```

**STEP 4: MONITOR & REASSESS** (Ongoing)
```markdown
□ Situation status updates every 15-30 min
□ Severity re-evaluated as information available
□ Response effectiveness monitored
□ Resource adequacy assessed
□ Escalation triggers watched
□ Documentation maintained
□ Stakeholder notifications sent
```

**STEP 5: TRANSITION & DOCUMENT** (Post-incident)
```markdown
□ Incident contained/resolved
□ Demobilization plan executed
□ Resources released appropriately
□ Final incident report completed
□ Lessons learned documented
□ Follow-up actions assigned
□ After-action review scheduled
```

## Triage Methodologies

### Medical Triage - START Method

**START Triage** (Simple Triage And Rapid Treatment):

Used for mass casualty incidents to quickly categorize victims.

**TRIAGE CATEGORIES**:

**GREEN - MINOR** (Walking Wounded):
- Can walk
- Delayed treatment (hours)
- "Walking wounded area"

**YELLOW - DELAYED** (Urgent):
- Cannot walk but breathing
- Respiratory rate <30/min
- Radial pulse present
- Follows commands
- Treatment within 1-2 hours

**RED - IMMEDIATE** (Critical):
- Not walking
- Airway compromised OR
- Respiratory rate >30/min OR
- No radial pulse OR
- Doesn't follow commands
- Treatment within minutes

**BLACK - DECEASED/EXPECTANT**:
- Not breathing after airway opened
- Or injuries incompatible with life
- Expectant (if resources limited)

**START Triage Algorithm**:
```
START
  ↓
Can patient walk?
  ├─ YES → GREEN (Minor)
  └─ NO ↓
Open airway
  ↓
Breathing?
  ├─ NO → BLACK (Deceased)
  └─ YES ↓
Respiratory rate?
  ├─ >30/min → RED (Immediate)
  └─ <30/min ↓
Radial pulse present?
  ├─ NO → RED (Immediate)
  └─ YES ↓
Mental status (follows commands)?
  ├─ NO → RED (Immediate)
  └─ YES → YELLOW (Delayed)
```

**Triage Tagging**:
- Physical tag attached to patient
- Color-coded (Red/Yellow/Green/Black)
- Include: Name, injuries, treatments given, time triaged
- Don't remove tag

### Operational Triage

**For non-medical incidents** (fire, hazmat, security):

**PRIORITY 1 - IMMEDIATE**:
- Life safety threatened
- Rapidly deteriorating situation
- Imminent hazard
- Response: Immediate action, all available resources

**PRIORITY 2 - URGENT**:
- Significant hazard, not immediately life-threatening
- Situation stable but could deteriorate
- Response: Rapid deployment, adequate resources

**PRIORITY 3 - NON-URGENT**:
- Hazard contained
- No immediate threat
- Response: Scheduled, standard resources

**PRIORITY 4 - ROUTINE**:
- No active hazard
- Follow-up/documentation only
- Response: As available

### Resource Triage

When resources are limited, prioritize allocation:

**ALLOCATION MATRIX**:
```markdown
CRITICAL RESOURCES (Life safety equipment, medical, rescue):
1. Immediate life-saving interventions
2. Prevent escalation to life-threatening
3. Reduce suffering
4. Protect responders
5. Property protection

HUMAN RESOURCES (Personnel):
1. Critical specialized skills (medical, hazmat, rescue)
2. Incident command positions
3. Essential operations
4. Support functions
5. Recovery activities

EQUIPMENT/SUPPLIES:
1. Life safety equipment
2. Personal protective equipment
3. Communication equipment
4. Containment/mitigation
5. Recovery/restoration
```

## Incident Documentation Requirements

### Incident Report Structure

**INCIDENT REPORT FORM**:

```markdown
INCIDENT IDENTIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Incident Number: [Auto-generated]
Date: [YYYY-MM-DD]
Time Discovered: [HH:MM]
Time Reported: [HH:MM]
Location: [Building, floor, room]
Reported By: [Name, contact]
Initial Responder: [Name, title]

INCIDENT CLASSIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type: [ ] Fire  [ ] Medical  [ ] Security  [ ] Hazmat
      [ ] Natural Disaster  [ ] Infrastructure  [ ] Other: ___

Severity: [ ] Low  [ ] Medium  [ ] High  [ ] Critical

Status: [ ] Ongoing  [ ] Contained  [ ] Resolved

INCIDENT DESCRIPTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
What happened: [Detailed narrative]

Cause (if known): [Root cause or suspected cause]

Discovered how: [Detection method - alarm, observation, report]

IMPACT ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Injuries/Fatalities:
- Number injured: [X]
- Severity: [ ] Minor  [ ] Serious  [ ] Critical  [ ] Fatal
- Description: [Details]
- Medical response: [Treatment provided, hospital transport]

Property Damage:
- Estimated cost: $[Amount]
- Description: [What was damaged]
- Affected area: [Size/scope]

Environmental Impact:
[ ] None  [ ] Spill/Release  [ ] Contamination
Description: [Details if applicable]

Operational Impact:
- Business interruption: [Duration]
- Services affected: [Which services]
- Personnel affected: [Number, which departments]
- Estimated financial impact: $[Amount]

PERSONNEL INVOLVED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Injured/Affected:
1. Name: [Name], Injury: [Description], Status: [Treatment/location]
2. [Continue for each person]

Witnesses:
1. Name: [Name], Contact: [Phone/email], Statement: [Attached/below]
2. [Continue for each witness]

RESPONSE ACTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Immediate Actions Taken:
- [Action 1 - by whom, at what time]
- [Action 2]
- [Action 3]

Resources Deployed:
- Internal: [Security, facilities, medical, management]
- External: [Fire dept, police, EMS, agencies]

ICS Activated: [ ] Yes  [ ] No
If yes:
- Incident Commander: [Name]
- Operations: [Name]
- Planning: [Name]
- Logistics: [Name]
- Finance/Admin: [Name]

NOTIFICATIONS MADE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Internal:
- [ ] Senior Management (Name: ___, Time: ___)
- [ ] Department Head (Name: ___, Time: ___)
- [ ] HR (Name: ___, Time: ___)
- [ ] Legal (Name: ___, Time: ___)
- [ ] Public Relations (Name: ___, Time: ___)

External:
- [ ] 911/Emergency Services (Time: ___)
- [ ] Regulatory Agency: [Which, Time: ___]
- [ ] Insurance (Time: ___)
- [ ] Media (If yes, method: ___)

DOCUMENTATION ATTACHMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [ ] Photos (Quantity: ___)
- [ ] Videos (Quantity: ___)
- [ ] Witness statements (Quantity: ___)
- [ ] Medical records
- [ ] Police/Fire reports
- [ ] Safety data sheets (hazmat)
- [ ] Incident action plans
- [ ] Communication logs
- [ ] Other: [Specify]

CURRENT STATUS & NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Current Status: [Ongoing/Contained/Resolved]

Ongoing Actions:
- [Action and responsible party]
- [Action and responsible party]

Investigation:
Required: [ ] Yes  [ ] No
If yes:
- Lead investigator: [Name]
- Start date: [Date]
- Expected completion: [Date]

Regulatory Reporting:
Required: [ ] Yes  [ ] No
If yes:
- Agency: [Which]
- Deadline: [Date]
- Responsible: [Name]

Follow-up Required:
- [ ] Corrective actions identified
- [ ] Equipment inspection/repair
- [ ] Training needed
- [ ] Policy/procedure review
- [ ] After-action review scheduled

REPORT INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Prepared by: [Name, Title]
Date prepared: [YYYY-MM-DD]
Report version: [1.0, 2.0, Final]
Distribution: [Who receives this report]
Confidentiality: [ ] Public  [ ] Internal  [ ] Confidential

APPROVALS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reviewed by:
- Emergency Manager: [Name, Signature, Date]
- Department Head: [Name, Signature, Date]
- Legal (if required): [Name, Signature, Date]
```

### Incident Action Plan (IAP)

**For Level 3+ incidents lasting >1 operational period**:

```markdown
INCIDENT ACTION PLAN
Incident Name: [Descriptive name]
Operational Period: [Date/time start] to [Date/time end]

1. SITUATION SUMMARY
Current Situation:
- [Brief description of incident status]
- [Key developments since last period]

Weather/Environmental Factors:
- [Conditions affecting response]

Safety Issues:
- [Known hazards]
- [Protective measures required]

2. INCIDENT OBJECTIVES
Priority 1: [Primary objective - usually life safety]
Priority 2: [Secondary objective - stabilization/containment]
Priority 3: [Tertiary objective - property protection]
Priority 4: [Additional objectives]

Measurable targets for this operational period:
- [Specific, measurable goal]
- [Specific, measurable goal]

3. ORGANIZATION
Incident Commander: [Name]
└─ Safety Officer: [Name]
└─ Public Information Officer: [Name]
└─ Operations Section Chief: [Name]
   └─ [Branches/Divisions/Groups]
└─ Planning Section Chief: [Name]
└─ Logistics Section Chief: [Name]
└─ Finance/Admin Section Chief: [Name]

4. ASSIGNMENTS
Operations Section:
- Branch/Division: [Name]
  Task: [Specific assignment]
  Resources: [Personnel, equipment]
  Location: [Where]
  Time: [Start-end]

- Branch/Division: [Name]
  [Continue for each assignment]

5. SUPPORT & LOGISTICS
Communications:
- Primary: [Radio channel/phone]
- Backup: [Alternative]

Medical Support:
- On-scene: [EMS unit location]
- Transport: [Hospital designation]

Facilities:
- Incident Command Post: [Location]
- Staging Area: [Location]
- Base: [Location if established]

6. SAFETY MESSAGE
Key safety considerations for this operational period:
- [Specific hazard and mitigation]
- [Specific hazard and mitigation]

Required PPE: [List]

Weather concerns: [Forecast impact on operations]

7. NEXT OPERATIONAL PERIOD
Expected transition: [Date/time]
Planning meeting: [Date/time, location]
Tactics meeting: [Date/time, location]

Prepared by: [Planning Section Chief, Date/time]
Approved by: [Incident Commander, Date/time]
```

### Communication Log

**All incident communications must be logged**:

```markdown
COMMUNICATION LOG
Incident: [Number/Name]
Date: [Date]

Time  | From      | To        | Method | Message Summary                    | Action
------|-----------|-----------|--------|------------------------------------|---------
14:32 | Security  | 911       | Phone  | Fire reported Bldg A, 3rd floor   | FD dispatched
14:33 | Security  | Emerg Mgr | Radio  | Fire alarm activated, evacuation  | ICS activation
14:35 | Emerg Mgr | CEO       | Phone  | Briefing on fire incident         | Monitoring
14:40 | Fire Dept | IC        | Radio  | On scene, requesting utilities off| Facilities notified
14:42 | IC        | All Staff | Email  | Evacuation in progress, status    | Info disseminated
```

### Resource Tracking

**Track all resources deployed**:

```markdown
RESOURCE STATUS TRACKING

Resource Type: [Personnel, Equipment, Facility]
Resource Name/ID: [Specific identification]

Check-In Time: [HH:MM]
Check-In Location: [Where]
Checked In By: [Name]

Assignment:
- Assigned to: [Division/Branch/Group]
- Assignment: [Specific task]
- Location: [Where working]
- Supervisor: [Name]

Status Updates:
- [Time]: [Status - available, assigned, out of service]
- [Time]: [Status]

Check-Out Time: [HH:MM]
Check-Out Location: [Where]
Checked Out By: [Name]

Total Time: [Hours]

Notes: [Damage, issues, maintenance needed]
```

## Resource Allocation

### Resource Categorization

**PERSONNEL**:
```markdown
IMMEDIATE RESPONSE:
- First responders (security, facilities, medical)
- Incident Commander
- Safety Officer
- Operations personnel

SPECIALIZED SKILLS:
- Hazmat technicians
- Search and rescue
- Medical personnel
- Technical experts
- Heavy equipment operators

SUPPORT:
- Logistics (supplies, food, facilities)
- Communications
- Documentation
- Relief personnel
```

**EQUIPMENT**:
```markdown
LIFE SAFETY:
- Personal protective equipment (PPE)
- Rescue equipment
- Medical equipment
- Detection equipment (gas, radiation)
- Communication equipment

OPERATIONAL:
- Fire suppression
- Containment equipment
- Decontamination
- Generators
- Lighting

SUPPORT:
- Vehicles
- Computers/technology
- Office supplies
- Food/water
- Temporary facilities
```

**FACILITIES**:
```markdown
COMMAND & CONTROL:
- Incident Command Post
- Emergency Operations Center
- Staging areas

SUPPORT:
- Medical treatment area
- Decontamination area
- Rest/rehab area
- Assembly points

LOGISTICS:
- Supply storage
- Equipment cache
- Fueling location
```

### Resource Request Process

**REQUEST WORKFLOW**:
```
Supervisor identifies need
    ↓
Request to Operations Section Chief
    ↓
Operations evaluates request
    ↓
If approved → Request to Logistics Section Chief
    ↓
Logistics sources resource
    ↓
Resource delivered to Staging
    ↓
Assigned to requestor
    ↓
Check-in at assignment
    ↓
[Use during operational period]
    ↓
Release from assignment
    ↓
Return to Staging or check out
```

**RESOURCE REQUEST FORM**:
```markdown
Request Number: [Auto-generated]
Date/Time: [Timestamp]
Requested By: [Name, Position]
Assignment: [Division/Branch/Group]

RESOURCE REQUESTED:
Type: [ ] Personnel  [ ] Equipment  [ ] Facility
Description: [Specific resource needed]
Quantity: [Number]
Qualifications/Specifications: [Details]

JUSTIFICATION:
Purpose: [Why needed]
Priority: [ ] Immediate  [ ] Urgent  [ ] Routine
Duration: [How long needed]

APPROVED BY:
Operations: [Name, Signature, Date/Time]
Logistics: [Name, Signature, Date/Time]

STATUS:
[ ] Pending
[ ] Sourcing
[ ] Ordered
[ ] In Transit
[ ] Delivered
[ ] Assigned
[ ] Not Available

Delivery Location: [Where]
ETA: [Expected time]
Delivered By: [Name]
Delivered Time: [Actual time]

Notes: [Any special instructions]
```

### Mutual Aid Agreements

**Requesting External Resources**:
```markdown
WHEN TO REQUEST MUTUAL AID:
- Local resources insufficient
- Specialized capabilities needed
- Extended incident duration
- Multiple simultaneous incidents

REQUEST PROCESS:
1. Incident Commander authorizes request
2. Contact mutual aid partner agency
3. Specify: Resource type, quantity, capabilities, duration
4. Confirm: Availability, response time, cost
5. Provide: Incident location, contact, assignment
6. Track: Check-in, deployment, check-out
7. Document: Usage, costs, performance

MUTUAL AID COORDINATION:
- Unified command structure
- Clear communication protocols
- Compatible equipment/systems
- Credentialing verification
- Cost tracking/reimbursement
- Safety briefings
- After-action coordination
```

## Post-Incident Activities

### Demobilization Planning

**Demobilization triggers**:
- Incident objectives met
- All hazards mitigated
- No further immediate threat
- Operations transitioned to recovery

**Demobilization process**:
```markdown
1. Demobilization plan developed (Planning Section)
2. Resources released in order:
   - Non-essential first
   - Specialized resources
   - Support functions
   - Command staff last
3. Each resource:
   - Checked out
   - Debriefed
   - Equipment inspected
   - Time recorded
   - Documentation collected
4. Facilities restored/closed
5. Final incident briefing
6. Command transferred or terminated
```

### After-Action Review (AAR)

**Scheduled within 72 hours of incident resolution**:

```markdown
AAR MEETING AGENDA

1. INCIDENT OVERVIEW (10 min)
   - Timeline recap
   - Final statistics (injuries, damage, cost)
   - Duration and scope

2. WHAT WENT WELL (20 min)
   - Effective actions
   - Successful procedures
   - Individual/team performance
   - Equipment that performed well
   - Communication successes

3. WHAT NEEDS IMPROVEMENT (30 min)
   - Challenges encountered
   - Procedural gaps
   - Communication issues
   - Resource shortfalls
   - Training deficiencies
   - Equipment failures

4. LESSONS LEARNED (20 min)
   - Key takeaways
   - Unexpected situations
   - Innovative solutions
   - Best practices identified

5. ACTION ITEMS (20 min)
   - Corrective actions needed
   - Responsible party assigned
   - Timeline for completion
   - Resource requirements
   - Follow-up review date

6. DOCUMENTATION (10 min)
   - Final report responsibility
   - Required attachments
   - Distribution list
   - Retention requirements
```

**AAR REPORT CONTENTS**:
- Executive summary
- Incident overview
- Timeline
- Response actions
- Strengths
- Areas for improvement
- Recommendations
- Action plan
- Appendices (photos, logs, forms)

---

*This skill provides comprehensive incident management frameworks for assessment, triage, resource allocation, and documentation of emergency incidents.*
