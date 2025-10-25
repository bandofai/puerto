# Incident Response Plugin

Security incident response specialist for handling security breaches, coordinating response, performing forensic analysis, planning recovery, and documenting post-mortems.

## Overview

The Incident Response plugin provides agents for systematic security incident handling using NIST SP 800-61 (Incident Response Guide), SANS Incident Handler's Handbook, and industry-standard forensics and recovery practices.

## Agents

### 1. incident-detector (Sonnet, Skill-Aware)
Analyzes indicators of compromise (IOCs), classifies incidents, and determines severity levels.

**Use for**: Initial triage, incident classification, severity assessment, IOC analysis

**Example**:
```
Use incident-detector to analyze potential security incident.
Indicators:
- Unusual outbound traffic to known C2 server
- Multiple failed admin login attempts
- New scheduled task created on domain controller
- Sensitive file access by contractor account
Classification: Determine incident type (malware, unauthorized access, data exfiltration)
Severity: Use NIST framework (Low/Medium/High/Critical)
Output: Incident classification, severity, recommended response level
```

### 2. response-coordinator (Sonnet, Skill-Aware)
Coordinates incident response following NIST phases: Preparation, Detection & Analysis, Containment/Eradication/Recovery, Post-Incident Activity.

**Use for**: Response team coordination, action planning, timeline tracking, communication management

**Example**:
```
Use response-coordinator for ransomware incident.
Incident: Ransomware detected on 50 workstations, file encryption in progress
Response team: IR lead, IT ops, security analyst, legal, communications
Immediate actions:
- Isolate infected systems
- Identify patient zero and attack vector
- Preserve evidence for forensics
- Assess backup availability
- Notify stakeholders (CISO, legal, PR)
Timeline: Document all actions with timestamps
```

### 3. forensic-analyzer (Sonnet, Skill-Aware)
Performs digital forensics analysis: evidence collection, timeline reconstruction, attribution analysis.

**Use for**: Evidence preservation, log analysis, malware analysis, timeline creation, attribution

**Example**:
```
Use forensic-analyzer for data breach investigation.
Scope: Unauthorized database access, 100K customer records accessed
Evidence sources:
- Database logs (queries, connections)
- Web server logs (access patterns)
- Network logs (traffic to DB server)
- Authentication logs (compromised credentials?)
Analysis:
- Timeline of attacker activity
- Attack vector and initial access
- Data accessed/exfiltrated
- Persistence mechanisms
- Attribution indicators
Output: Forensic report with timeline, TTPs, IOCs
```

### 4. recovery-planner (Sonnet, Skill-Aware)
Develops recovery plans with system restoration, security hardening, and business continuity.

**Use for**: Recovery roadmap, system restoration, security improvements, business resumption

**Example**:
```
Use recovery-planner after malware eradication.
Incident: Malware removed, systems cleaned
Recovery needs:
- Restore 20 servers from clean backups
- Rebuild compromised domain controller
- Reset all AD passwords
- Patch vulnerabilities exploited
- Deploy EDR on all endpoints
- Resume business operations
Timeline: Phased recovery over 72 hours
Validation: Security testing before production
Business continuity: Interim workarounds, communication plan
```

## Skills

### incident-response
Comprehensive incident response frameworks and methodologies:
- **NIST SP 800-61**: 4-phase incident response lifecycle
- **SANS Incident Response**: 6-step process (Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned)
- **MITRE ATT&CK**: Tactics, techniques, and procedures (TTPs) framework
- **Incident Classification**: Malware, unauthorized access, data breach, DoS, insider threat
- **Severity Levels**: Critical/High/Medium/Low based on impact and scope
- **Evidence Handling**: Chain of custody, forensic soundness, legal admissibility
- **Communication**: Internal escalation, external notifications (law enforcement, regulators, customers)
- **Compliance**: GDPR breach notification (72 hours), state breach laws, PCI-DSS, HIPAA

## Templates

### incident-response-plan-template.md
Comprehensive IR plan: Team roles, contact list, incident classification matrix, response playbooks by incident type, escalation procedures, communication templates, tool inventory.

### forensic-analysis-report-template.md
Digital forensics report: Executive summary, incident timeline, evidence summary, analysis methodology, findings, indicators of compromise (IOCs), attacker TTPs, attribution analysis, recommendations.

### post-mortem-template.md
Blameless post-mortem: Incident summary, timeline, impact assessment, what went well, what went wrong, action items, preventive measures, lessons learned.

### recovery-plan-template.md
Recovery roadmap: System restoration sequence, security hardening steps, validation testing, business resumption plan, communication strategy, success criteria.

## Workflows

### Complete Incident Response Lifecycle
```
1. Detection & Triage
Use incident-detector to classify incident and determine severity

2. Response Coordination
Use response-coordinator to activate IR team and execute containment

3. Forensic Investigation
Use forensic-analyzer to collect evidence and analyze attack

4. Recovery & Hardening
Use recovery-planner to restore systems and prevent recurrence

5. Post-Mortem
Use response-coordinator to document lessons learned and update IR plan
```

### Data Breach Response
```
Phase 1: Immediate (0-24 hours)
- incident-detector: Classify breach, assess scope
- response-coordinator: Activate team, contain breach, preserve evidence

Phase 2: Investigation (24-72 hours)
- forensic-analyzer: Analyze logs, reconstruct timeline, identify data accessed

Phase 3: Notification (within 72 hours for GDPR)
- response-coordinator: Notify regulators, affected individuals, stakeholders

Phase 4: Recovery (Week 1-2)
- recovery-planner: Remediate vulnerabilities, restore security

Phase 5: Post-Mortem (Week 2-3)
- Document lessons, update IR plan, implement preventive controls
```

## Requirements Met

✅ Role: Security incident response specialist
✅ Incident detection: incident-detector with IOC analysis and severity classification
✅ Response coordination: response-coordinator with NIST/SANS frameworks
✅ Forensic analysis: forensic-analyzer with digital forensics and timeline reconstruction
✅ Recovery planning: recovery-planner with system restoration and hardening
✅ Post-mortem documentation: Covered in response-coordinator and templates
✅ Tools: Security tools (log analysis), logging (evidence), analysis (forensics)

## Key Features

✓ **NIST SP 800-61 Compliance**: Industry-standard IR framework
✓ **MITRE ATT&CK Integration**: TTPs-based threat analysis
✓ **Evidence Preservation**: Forensically sound evidence handling
✓ **Regulatory Compliance**: GDPR (72hr), state breach laws, PCI-DSS, HIPAA
✓ **Blameless Post-Mortems**: Learning-focused, not blame-focused
✓ **Severity Classification**: Risk-based prioritization
✓ **Chain of Custody**: Legal admissibility of evidence

## Incident Types Covered

- **Malware**: Ransomware, trojans, worms, rootkits
- **Unauthorized Access**: Credential compromise, privilege escalation
- **Data Breach**: Data exfiltration, unauthorized disclosure
- **DoS/DDoS**: Service disruption attacks
- **Insider Threat**: Malicious or negligent insiders
- **Web Application**: SQL injection, XSS, authentication bypass
- **Phishing**: Credential harvesting, business email compromise

## NIST Incident Response Phases

1. **Preparation**: IR plan, tools, training, contacts
2. **Detection & Analysis**: Monitoring, triage, classification, notification
3. **Containment, Eradication & Recovery**: Isolate, remove threat, restore operations
4. **Post-Incident Activity**: Lessons learned, plan updates, preventive measures

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 1 comprehensive incident-response skill with NIST/SANS frameworks
- ✅ 4 professional templates for IR plan, forensics, post-mortem, recovery
- ✅ Complete README with workflows and compliance requirements

## Important Notes

⚠️ **Legal Coordination**: Always involve legal counsel for breach response, especially for notification obligations.

⚠️ **Evidence Preservation**: Maintain chain of custody for potential legal proceedings.

⚠️ **Regulatory Timelines**: GDPR requires breach notification within 72 hours of awareness.

⚠️ **Security First**: This plugin provides guidance but requires qualified security professionals for actual incident response.

Closes #75
