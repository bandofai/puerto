# Emergency Response Coordinator Plugin

Emergency response management specialist for incident assessment, protocol activation, stakeholder notification, and resource coordination using ICS (Incident Command System) standards.

## Overview

The Emergency Response Coordinator plugin provides agents for managing organizational emergencies using standardized ICS frameworks, rapid protocol activation, multi-channel stakeholder communications, and comprehensive resource management for incidents including fires, medical emergencies, security threats, natural disasters, and hazmat situations.

## Agents

### 1. incident-assessor (Sonnet, Skill-Aware)
Assesses emergency incidents for severity, scope, impact, and response level needed using METHANE reports and ICS standards.

**Use for**: Incident evaluation, severity classification, ICS activation decisions, resource needs assessment

**Example**:
```
Use incident-assessor for fire emergency.
Location: Building A, 3rd floor east wing
Reported: Smoke detected, fire alarm activated
Initial info: 2 minor injuries evacuated, 3 employees unaccounted for
Hazards: Heavy smoke, possible structural damage, hazmat lab adjacent
Request: METHANE report, severity classification, ICS activation recommendation, resource requirements
```

### 2. protocol-activator (Haiku - Fast Activation, Skill-Aware)
Activates appropriate emergency protocols based on incident type with rapid decision-making for urgent situations.

**Use for**: Emergency procedure activation, RACE protocol, RUN/HIDE/FIGHT, evacuation, shelter-in-place

**Example**:
```
Use protocol-activator for active threat incident.
Type: Security - armed intruder reported
Location: Building B, 2nd floor
Severity: Critical
Action needed: Activate RUN/HIDE/FIGHT protocol, lockdown procedures, mass notification message
Speed: Immediate activation required
```

### 3. stakeholder-notifier (Haiku - Fast Comms, Skill-Aware)
Sends emergency notifications using template-based rapid communication for employees, families, customers, media, and regulatory agencies.

**Use for**: Mass alerts, status updates, all-clear notifications, family reunification communication

**Example**:
```
Use stakeholder-notifier for medical emergency.
Incident: Employee cardiac arrest in cafeteria
Status: EMS on scene, patient transported to Memorial Hospital
Stakeholders:
- Employees: Brief notification, counseling resources available
- Family: Urgent notification with hospital details and company contact
- Management: Incident summary and follow-up actions
- HR: Employee assistance activation
Notification type: Initial alert
```

### 4. resource-coordinator (Sonnet, Skill-Aware)
Coordinates emergency resources including personnel, equipment, and facilities with allocation, tracking, and demobilization.

**Use for**: Resource allocation, staging area management, mutual aid requests, ICS resource tracking

**Example**:
```
Use resource-coordinator for extended fire incident.
Incident: Building fire, multi-hour response expected
ICS activated: IC, Operations, Planning, Logistics sections
Resources needed:
- Personnel: 12-hour shift rotation for 3 operational periods
- Equipment: Additional generators, lighting, communication gear
- Facilities: Incident command post, staging area, rest/rehab area
- External: Mutual aid from neighboring fire departments
Tasks: Resource inventory, allocation plan, staging management, demobilization planning
```

## Skills

### emergency-protocols
Emergency response procedures and ICS framework:
- **Emergency Types**: Fire, medical, security, natural disaster, hazmat, infrastructure, pandemic
- **ICS Structure**: Incident Commander, Command Staff (PIO, Safety, Liaison), General Staff (Operations, Planning, Logistics, Finance/Admin)
- **Response Procedures**: RACE (fire), CPR/First Aid, RUN/HIDE/FIGHT (active threat), Shelter-in-Place, Evacuation
- **Triage**: START method (Simple Triage And Rapid Treatment) for mass casualty
- **Emergency Kits**: Individual and facility requirements
- **Training**: Personnel requirements, drill frequency, exercise types

### stakeholder-communication
Emergency notification systems and communication strategies:
- **Notification Systems**: Mass notification (SMS/Email/App), phone trees, social media, emergency websites
- **Alert Levels**: Informational (Green), Advisory (Yellow), Warning (Orange), Emergency (Red)
- **Communication Chain**: ICS command structure, PIO role, approval processes
- **Templates**: Initial alerts, status updates, all-clear, family notifications, customer notices, media statements, regulatory reports
- **Channels**: Multi-channel strategy, backup systems, 24/7 hotlines
- **Family Reunification**: Reunification center operations, hotline management, status inquiry responses

### incident-management
Incident assessment, triage, and documentation:
- **Assessment Framework**: METHANE report format (Major incident, Exact location, Type, Hazards, Access, Number of casualties, Emergency services)
- **Severity Matrix**: Impact (Low/Medium/High/Catastrophic) × Likelihood (Low/Medium/High) = Priority
- **5-Step Process**: Detect & Verify, Assess & Classify, Activate Response, Monitor & Reassess, Transition & Document
- **Triage Methodologies**: START (medical), operational priority, resource allocation triage
- **Documentation**: Incident reports, action plans, communication logs, resource tracking, after-action reviews
- **Demobilization**: Release order, checkout procedures, external resource coordination

## Workflows

### Emergency Response Workflow
```
1. Incident Occurs
Immediate: Call 911 if life safety issue
Use incident-assessor to evaluate severity and scope

2. Protocol Activation (Within 5 minutes)
Use protocol-activator to activate appropriate emergency procedures
- Fire: RACE protocol, evacuation
- Medical: CPR/First Aid, AED deployment
- Security: RUN/HIDE/FIGHT, lockdown
- Natural Disaster: Shelter-in-place or evacuation
- Hazmat: Shelter-in-place, containment

3. Stakeholder Notification (Immediate)
Use stakeholder-notifier to send emergency alerts
- Employees: Mass notification with specific actions
- 911/Emergency Services: If not already called
- Management: Executive briefing
- Affected families: If serious injuries

4. Resource Coordination (Ongoing)
Use resource-coordinator to manage response resources
- Personnel: ICS positions, shift rotations
- Equipment: Staging, allocation, tracking
- Facilities: Command post, assembly points
- Mutual aid: If local resources insufficient

5. Ongoing Management
- Status updates every 15-30 minutes (stakeholder-notifier)
- Resource status reports every 1-2 hours (resource-coordinator)
- Incident reassessment as situation evolves (incident-assessor)
- Protocol adjustments as needed (protocol-activator)

6. All-Clear & Demobilization
Use stakeholder-notifier for all-clear notification
Use resource-coordinator for systematic demobilization
Schedule after-action review within 72 hours
```

### ICS Activation Workflow
```
Use incident-assessor to determine if ICS activation needed:

Level 1 (Local): Security/Facilities handle, no ICS
Level 2 (Departmental): Add management, simple command
Level 3 (Full ICS): Activate full ICS structure - Use this workflow:

1. Establish Command
- Incident Commander designated
- Command Post established
- Use resource-coordinator to set up ICP

2. Activate Command Staff
- Public Information Officer (stakeholder-notifier)
- Safety Officer (incident-assessor for hazards)
- Liaison Officer (if multi-agency)

3. Activate General Staff (as needed)
- Operations: Use protocol-activator for tactics
- Planning: Use incident-assessor for situation analysis
- Logistics: Use resource-coordinator for resources
- Finance/Admin: Cost tracking, procurement

4. Develop Incident Action Plan
Each operational period (typically 12 hours):
- Objectives for the period
- Organization assignments
- Resource allocations (resource-coordinator)
- Communication plan (stakeholder-notifier)
- Safety considerations (incident-assessor)

5. Execute Response
- Operations implements tactics (protocol-activator)
- Resources deployed (resource-coordinator)
- Stakeholders updated (stakeholder-notifier)
- Situation monitored (incident-assessor)

6. Demobilization
When objectives met:
- Use resource-coordinator for systematic release
- Use stakeholder-notifier for all-clear
- Document lessons learned
```

### Mass Casualty Incident
```
Use incident-assessor for initial assessment:
- Number of casualties
- Types of injuries
- Resources required
- Triage method (START)

Use protocol-activator to activate mass casualty protocol:
- Triage area setup
- Treatment area setup
- Transportation coordination
- Hospital notifications

Use stakeholder-notifier for emergency notifications:
- Immediate: 911, request multiple ambulances
- Internal: All personnel, request first aid certified to triage area
- Families: As casualties identified
- Media: Through PIO only

Use resource-coordinator to manage medical response:
- Personnel: Triage team, treatment team, transport coordinator
- Equipment: First aid supplies, AEDs, spine boards
- Facilities: Triage area (GREEN/YELLOW/RED/BLACK zones), treatment area
- External: EMS units, hospital capacity coordination
```

## Requirements Met

✅ Role: Emergency response coordinator specialist
✅ Emergency protocols: Comprehensive skill covering fire, medical, security, natural disasters, hazmat, ICS
✅ Incident assessment: incident-assessor with METHANE reports and severity classification
✅ Protocol activation: protocol-activator for rapid emergency procedure deployment
✅ Stakeholder communication: stakeholder-notifier with multi-channel notifications
✅ Resource coordination: resource-coordinator for personnel, equipment, facilities management
✅ Tools: Appropriate tool sets for each agent type (Read for skills, Write for reports, Bash for scripts)
✅ Models: Sonnet for assessment/coordination judgment, Haiku for fast activation/notification

## Key Features

✓ **ICS Standards**: Full Incident Command System framework
✓ **METHANE Reports**: Standardized incident assessment methodology
✓ **START Triage**: Medical triage for mass casualty incidents
✓ **Multi-Hazard**: Fire, medical, security, natural disasters, hazmat, infrastructure
✓ **Template-Based**: Rapid activation using proven protocols
✓ **Multi-Channel**: Mass notification, phone trees, email, social media, websites
✓ **Family Reunification**: Personnel accounting and family notification procedures
✓ **Resource Management**: Complete tracking from check-in to demobilization
✓ **Mutual Aid**: External resource coordination when local capacity exceeded
✓ **Compliance**: OSHA, NFPA, FEMA standards incorporated

## Emergency Response Levels

**Level 1 - Local Response**: Security/Facilities handle, no ICS
- Minor incidents, no injuries or minor only
- Limited property damage
- Resolved quickly with local resources

**Level 2 - Departmental Response**: Add management, simple command
- Medical attention required
- Moderate disruption
- Single department/building affected

**Level 3 - Full ICS Activation**: Complete crisis team
- Serious injuries or fatalities
- Major property damage
- Multi-department impact
- External agency involvement
- Activate all 4 agents in coordination

**Level 4 - External Resources**: Beyond local capacity
- Specialized capabilities needed
- Extended duration (>12 hours)
- Mutual aid requested

**Level 5 - Multi-Agency**: Catastrophic impact
- Regional response
- Multiple jurisdictions
- Unified command structure

## Response Speed Targets

- **Detection to Assessment**: <5 minutes (incident-assessor)
- **Protocol Activation**: <5 minutes from assessment (protocol-activator)
- **Initial Notifications**: Immediate for Priority 1 stakeholders (stakeholder-notifier)
- **ICS Setup**: <30 minutes for Level 3+ incidents (resource-coordinator)
- **First Status Update**: <1 hour from incident
- **Ongoing Updates**: Every 15-30 min active phase, every 2-4 hours stabilization

## Incident Types Supported

- **Fire**: RACE protocol, evacuation, fire extinguisher use (PASS method)
- **Medical**: CPR, AED, first aid, stroke (FAST), choking, severe bleeding
- **Security**: Active threat (RUN/HIDE/FIGHT), bomb threat, workplace violence
- **Natural Disasters**: Tornado, earthquake, severe weather, flood
- **Hazmat**: Chemical spill, gas leak, contamination, shelter-in-place
- **Infrastructure**: Power outage, structural damage, elevator entrapment
- **Pandemic**: Disease outbreak, quarantine, mass illness

## Documentation Provided

- Incident reports (complete with METHANE assessment)
- Incident Action Plans (for each operational period)
- Resource tracking logs (personnel, equipment, facilities)
- Communication logs (all notifications and updates)
- Family reunification records (personnel accounting)
- After-action reviews (lessons learned)
- Regulatory notifications (OSHA, EPA, etc. as required)

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 3 comprehensive skills (emergency-protocols, stakeholder-communication, incident-management)
- ✅ ICS framework implementation with all standard positions
- ✅ Multi-hazard coverage (fire, medical, security, natural disaster, hazmat)
- ✅ Template-based rapid response capability
- ✅ Complete resource management lifecycle
- ✅ Family reunification procedures
- ✅ Complete README with workflows and response timelines

Closes #98
