# Incident Response Plugin

Professional security incident detection, analysis, containment, eradication, and recovery following NIST IR Framework and MITRE ATT&CK methodology.

## Overview

The Incident Response plugin provides specialized agents and comprehensive skills for conducting professional security incident response operations aligned with industry standards (NIST 800-61r2, MITRE ATT&CK, SANS Incident Handler's Handbook).

### Key Features

- **NIST IR Framework Compliance** - Full incident response lifecycle
- **MITRE ATT&CK Integration** - Tactic and technique classification
- **Forensic Analysis** - Timeline reconstruction, IOC identification
- **Chain of Custody** - Evidence preservation and documentation
- **Playbook Library** - Ransomware, data breach, DDoS, insider threat
- **Recovery Planning** - System restoration and hardening
- **Post-Incident Activities** - Lessons learned and continuous improvement

## Installation

```bash
/plugin install incident-response@puerto
```

## Quick Start

### 1. Detect Incident
```
Analyze security alert: suspicious PowerShell execution on web-server-01
```

### 2. Coordinate Response
```
Coordinate response for incident INC-20250115-143000
```

### 3. Conduct Forensics
```
Analyze forensics for incident INC-20250115-143000
```

### 4. Plan Recovery
```
Plan recovery for incident INC-20250115-143000
```

## Components

### Agents

#### 1. incident-detector (Sonnet)
**PROACTIVELY use for security incident detection**

**Capabilities:**
- MITRE ATT&CK classification (all 14 tactics, 180+ techniques)
- Severity assessment (SEV-1 to SEV-4)
- IOC extraction (IPs, domains, hashes, processes)
- Initial timeline creation
- Incident report generation

**Tools:** Read, Write, Bash, Grep

---

#### 2. response-coordinator (Sonnet)
**PROACTIVELY use for incident response coordination**

**Capabilities:**
- Playbook selection and activation
- IR team assembly and coordination
- Containment strategy execution
- Eradication coordination
- Stakeholder communication management

**Tools:** Read, Write, Edit, Bash

---

#### 3. forensic-analyzer (Sonnet)
**PROACTIVELY use for forensic investigation**

**Capabilities:**
- Timeline reconstruction from multiple sources
- IOC identification and enrichment
- Root cause analysis (5 Whys methodology)
- Evidence preservation (READ-ONLY for integrity)
- Comprehensive forensic reports

**Tools:** Read, Grep, Bash

---

#### 4. recovery-planner (Sonnet)
**PROACTIVELY use for recovery planning**

**Capabilities:**
- System restoration planning (rebuild vs clean)
- Staged rollout strategy
- Hardening recommendations
- Post-incident activity planning
- Lessons learned facilitation

**Tools:** Read, Write, Edit, Bash

---

### Skills

#### incident-response

Comprehensive knowledge covering:

**NIST IR Framework:**
- Preparation
- Detection & Analysis
- Containment, Eradication & Recovery
- Post-Incident Activity

**MITRE ATT&CK:**
- All 14 tactics (TA0001 through TA0043)
- 180+ techniques mapped
- Detection and response guidance for each

**Severity Classification:**
- SEV-1: Critical (< 15 min response)
- SEV-2: High (< 1 hour response)
- SEV-3: Medium (< 4 hours response)
- SEV-4: Low (next business day)

**Incident Playbooks:**
- Ransomware infection
- Data breach / exfiltration
- DDoS attack
- Insider threat
- Phishing campaign
- Malware infection

**Evidence & Forensics:**
- Chain of custody procedures
- Timeline analysis methodologies
- IOC identification and enrichment
- Memory forensics
- Log analysis
- Root cause analysis

**Legal & Regulatory:**
- GDPR (72 hour notification)
- HIPAA (60 day reporting)
- PCI DSS (immediate notification)
- State breach laws (varies)

## Usage Example: Ransomware Response

```
Step 1: Detection
> Analyze ransomware infection: mass file encryption, ransom notes found

Response:
INCIDENT: INC-20250115-143000
SEVERITY: SEV-1 (Critical)
MITRE: TA0040 - Impact (T1486 - Data Encrypted for Impact)

IOCs Identified:
- Process: ransomware.exe
- Extension: .encrypted
- Ransom note: README_DECRYPT.txt
- C2 IP: 203.0.113.42

IMMEDIATE ACTIONS:
1. ISOLATE infected systems (DO NOT power off)
2. Alert C-level, legal, law enforcement
3. Engage @response-coordinator
4. Check backup integrity

────────────────────────────────────────

Step 2: Response Coordination
> Coordinate response for INC-20250115-143000

Response:
PLAYBOOK: Ransomware Response (SEV-1)
TEAM ASSEMBLED:
- Incident Commander: [Assigned]
- Technical Lead: @forensic-analyzer
- Communications Lead: [Assigned]

CONTAINMENT (In Progress):
✓ 15 systems isolated from network
✓ 23 compromised accounts disabled
✓ Malicious IPs blocked at firewall
○ Evidence preservation ongoing

Next: Execute eradication once containment validated

────────────────────────────────────────

Step 3: Forensic Analysis
> Analyze forensics for INC-20250115-143000

Response:
FORENSIC ANALYSIS COMPLETE

Attack Timeline:
1. Initial compromise: 2025-01-15 10:00 UTC (phishing email)
2. Execution: 10:15 UTC (macro executed malware.exe)
3. Persistence: 10:20 UTC (registry key added)
4. Lateral movement: 10:30-13:00 UTC (spread to 15 systems)
5. Encryption: 14:30 UTC (ransomware deployed)
6. Detection: 14:35 UTC (user report)

Dwell Time: 4 hours 35 minutes

Root Cause: Unpatched email gateway allowed malicious attachment

Eradication Targets:
- Remove: C:\Users\victim\AppData\malware.exe
- Delete: HKLM\...\Run\WindowsUpdate (persistence)
- Reset: All user credentials

────────────────────────────────────────

Step 4: Recovery Planning
> Plan recovery for INC-20250115-143000

Response:
RECOVERY PLAN COMPLETE

Approach: REBUILD from clean images (SEV-1 best practice)

Timeline:
- Phase 1 (Foundation): 0-4 hours - Core infrastructure
- Phase 2 (Critical): 4-8 hours - P1 critical systems
- Phase 3 (Full): 8-24 hours - All systems
- Phase 4 (Validation): 24-72 hours - Monitoring for reinfection

Hardening Measures:
Immediate (0-7 days):
- Patch email gateway (CVE-2025-XXXX)
- Deploy MFA to all accounts
- Enhanced email security (ATP)
- Application whitelisting

Short-term (7-30 days):
- EDR deployment on all endpoints
- Network segmentation
- Backup improvements (3-2-1 strategy)

Medium-term (30-90 days):
- Zero-trust architecture
- Security awareness training
- Purple team exercises

Ready for Incident Commander approval
```

## Severity Matrix

| Level | Response | Escalation | Examples |
|-------|----------|------------|----------|
| **SEV-1** | < 15 min | C-level, Legal, PR, External IR | Ransomware, Data breach, Critical infrastructure |
| **SEV-2** | < 1 hour | IR lead, Security management | Malware infection, Unauthorized access |
| **SEV-3** | < 4 hours | SOC, System owners | Suspicious activity, Policy violations |
| **SEV-4** | Next day | SOC monitoring | Minor violations, False positives |

## MITRE ATT&CK Coverage

All 14 tactics with detection and response guidance:

- **TA0001: Initial Access** - Phishing, Exploits, External Services
- **TA0002: Execution** - Scripts, Tasks, User Execution
- **TA0003: Persistence** - Autostart, Accounts, Services
- **TA0004: Privilege Escalation** - Exploits, Token Manipulation
- **TA0005: Defense Evasion** - Log Clearing, Disabling Security
- **TA0006: Credential Access** - Credential Dumping, Brute Force
- **TA0007: Discovery** - Account/System Discovery, Reconnaissance
- **TA0008: Lateral Movement** - Remote Services, File Transfer
- **TA0009: Collection** - Data from Local/Network, Screen Capture
- **TA0010: Exfiltration** - C2 Channel, Alternative Protocols
- **TA0011: Command & Control** - Application/Encrypted Protocols
- **TA0040: Impact** - Ransomware, Data Destruction, Defacement

## Regulatory Compliance

### GDPR (EU)
- **72 hours** to notify supervisory authority (from awareness)
- Notify data subjects if high risk
- Document in breach register

**Applicability:** EU residents' personal data

### HIPAA (US Healthcare)
- **60 days** to report to HHS (if >500 individuals affected)
- Individual notification within 60 days
- Annual report for smaller breaches

**Applicability:** Protected Health Information (PHI)

### PCI DSS (Payment Cards)
- **Immediate** notification to acquiring bank and card brands
- Forensic investigation report required
- Remediation and validation

**Applicability:** Payment card data

### State Breach Laws (US)
- Varies by state (typically "without unreasonable delay")
- Some states require attorney general notification
- Notify affected residents

**Applicability:** State residents' personal information

## Best Practices

### Preparation
- Maintain updated incident response plan
- Conduct quarterly tabletop exercises
- Test backup restoration monthly
- Keep emergency contact lists current
- Pre-authorize common response actions

### Detection & Analysis
- Deploy comprehensive logging (SIEM/EDR)
- Enable threat intelligence feeds
- Tune alert thresholds to reduce false positives
- Practice proactive threat hunting
- Establish baseline behavior

### Containment
- **Isolate, don't power off** (preserves memory evidence)
- Document all actions with timestamps
- Preserve evidence with chain of custody
- Communicate status regularly
- Engage external experts when needed

### Eradication
- Identify and remediate root cause first
- Patch all exploited vulnerabilities
- Remove all persistence mechanisms
- **Consider rebuild over cleaning** (especially SEV-1)
- Validate environment is clean

### Recovery
- **Staged rollout** - never restore all systems simultaneously
- Monitor continuously for 72+ hours for reinfection
- Enhanced security posture before reconnection
- Validate backup integrity before restoration
- Document all recovery steps

### Post-Incident
- Conduct **blameless** lessons learned session
- Implement improvement action items
- Share IOCs with security community
- Update incident response playbooks
- Measure effectiveness (MTTD, MTTR metrics)

## Performance Metrics

Track incident response effectiveness:

**Detection Metrics:**
- **Mean Time to Detect (MTTD):** Goal < 24 hours
- **False Positive Rate:** Goal < 10%

**Response Metrics:**
- **Mean Time to Respond (MTTR):** Goal < 1 hour for SEV-1
- **Containment Time:** Goal < 4 hours

**Recovery Metrics:**
- **Mean Time to Recover:** Goal < 24 hours for critical systems
- **Backup Success Rate:** Goal 100%

**Program Metrics:**
- **Security Awareness:** Phishing click rate < 5%
- **Patch Compliance:** > 95% within 30 days
- **MFA Adoption:** 100% target

## Resources

### Official Standards
- **NIST SP 800-61r2:** Computer Security Incident Handling Guide
  https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf
- **MITRE ATT&CK:** https://attack.mitre.org/
- **SANS Incident Handler's Handbook**
  https://www.sans.org/white-papers/33901/

### Training & Certifications
- **GCIH:** GIAC Certified Incident Handler
- **GCFA:** GIAC Certified Forensic Analyst
- **CISM:** Certified Information Security Manager
- **CISSP:** Certified Information Systems Security Professional

### Communities
- **FIRST:** Forum of Incident Response and Security Teams (https://www.first.org/)
- **SANS Internet Storm Center:** https://isc.sans.edu/
- **Reddit:** r/netsec, r/AskNetsec

### Tools
**Forensics:**
- Volatility (memory forensics)
- Autopsy/Sleuth Kit (disk forensics)
- Wireshark (network forensics)

**Detection:**
- Splunk/ELK (SIEM)
- CrowdStrike/Carbon Black (EDR)
- Suricata/Snort (IDS)

**Threat Intelligence:**
- MISP, OpenCTI
- AlienVault OTX
- VirusTotal

## Contributing

Found an issue or have improvements? Please open an issue on the Puerto repository.

## License

MIT

---

**Need Help?**

Ask the agents:
- "How do I respond to a ransomware attack?"
- "Analyze this security incident: [description]"
- "Create recovery plan for incident INC-XXXXX"
- "What are the GDPR notification requirements?"

**Emergency Response:**
- Engage @incident-detector first for triage and classification
- Escalate per severity (SEV-1 = immediate C-level notification)
- Document everything with timestamps
- Preserve evidence with chain of custody
- Follow your organization's incident response plan
