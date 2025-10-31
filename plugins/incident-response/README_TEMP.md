# Incident Response Plugin

Professional security incident detection, analysis, containment, eradication, and recovery following NIST IR Framework and MITRE ATT&CK methodology.

## Overview

Specialized agents and comprehensive skills for conducting professional security incident response operations aligned with industry standards (NIST 800-61r2, MITRE ATT&CK, SANS).

### Key Features

- **NIST IR Framework** - Complete incident response lifecycle
- **MITRE ATT&CK** - Tactic and technique classification
- **Forensic Analysis** - Timeline reconstruction, IOC identification
- **Chain of Custody** - Evidence preservation and documentation
- **Playbooks** - Ransomware, data breach, DDoS, insider threat
- **Recovery Planning** - System restoration and hardening

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
- MITRE ATT&CK classification
- Severity assessment (SEV-1 to SEV-4)
- IOC extraction
- Initial timeline creation

**Tools:** Read, Write, Bash, Grep

---

#### 2. response-coordinator (Sonnet)
**PROACTIVELY use for incident response coordination**

**Capabilities:**
- Playbook activation
- IR team coordination
- Containment execution
- Stakeholder communications

**Tools:** Read, Write, Edit, Bash

---

#### 3. forensic-analyzer (Sonnet)
**PROACTIVELY use for forensic investigation**

**Capabilities:**
- Timeline reconstruction
- IOC identification
- Root cause analysis
- Evidence preservation (READ-ONLY)

**Tools:** Read, Grep, Bash

---

#### 4. recovery-planner (Sonnet)
**PROACTIVELY use for recovery planning**

**Capabilities:**
- System restoration planning
- Hardening recommendations
- Post-incident activities
- Lessons learned

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
- All 14 tactics
- 180+ techniques mapped
- Detection and response

**Severity Classification:**
- SEV-1: Critical (< 15 min)
- SEV-2: High (< 1 hour)
- SEV-3: Medium (< 4 hours)
- SEV-4: Low (next day)

**Incident Playbooks:**
- Ransomware infection
- Data breach / exfiltration
- DDoS attack
- Insider threat
- Phishing campaign

**Evidence & Forensics:**
- Chain of custody
- Timeline analysis
- IOC identification
- Memory forensics
- Log analysis

**Legal & Regulatory:**
- GDPR (72h notification)
- HIPAA (60 day)
- PCI DSS
- State breach laws

## Usage Example: Ransomware

```
Step 1: Detection
> Analyze ransomware infection: mass file encryption, ransom notes found

Response:
INCIDENT: INC-20250115-143000
SEVERITY: SEV-1 (Critical)
MITRE: TA0040 - Impact (T1486 Ransomware)

IOCs:
- Process: ransomware.exe
- Extension: .encrypted
- C2 IP: 203.0.113.42

ACTIONS:
1. ISOLATE infected systems
2. Alert C-level, legal
3. Engage @response-coordinator

Step 2: Coordination
> Coordinate response for INC-20250115-143000

Response:
PLAYBOOK: Ransomware (SEV-1)
TEAM: Assembled
CONTAINMENT:
✓ 15 systems isolated
✓ 23 accounts disabled
✓ IPs blocked

Step 3: Forensics
> Analyze forensics for INC-20250115-143000

Response:
TIMELINE:
10:00 - Phishing email
10:15 - Macro executed
14:30 - Encryption started

ROOT CAUSE:
Unpatched email gateway

ERADICATION TARGETS:
- Remove: malware.exe
- Reset: All credentials

Step 4: Recovery
> Plan recovery for INC-20250115-143000

Response:
APPROACH: Rebuild (SEV-1)
TIMELINE: 0-24 hours
HARDENING:
- Patch gateway
- Deploy MFA
- Email ATP
```

## Severity Matrix

| Level | Response | Escalation | Examples |
|-------|----------|------------|----------|
| **SEV-1** | < 15 min | C-level, Legal, External IR | Ransomware, Data breach |
| **SEV-2** | < 1 hour | IR lead, Security mgmt | Malware, Unauthorized access |
| **SEV-3** | < 4 hours | SOC, System owners | Suspicious activity |
| **SEV-4** | Next day | SOC monitoring | Minor violations |

## MITRE ATT&CK Coverage

All 14 tactics with detection and response:

- **TA0001:** Initial Access (Phishing, Exploits)
- **TA0002:** Execution (Scripts, Tasks)
- **TA0003:** Persistence (Autostart, Accounts)
- **TA0004:** Privilege Escalation
- **TA0005:** Defense Evasion
- **TA0006:** Credential Access
- **TA0007:** Discovery
- **TA0008:** Lateral Movement
- **TA0009:** Collection
- **TA0010:** Exfiltration
- **TA0011:** Command & Control
- **TA0040:** Impact

## Regulatory Compliance

**GDPR (EU):**
- 72 hours to notify authority
- Notify data subjects if high risk

**HIPAA (US Healthcare):**
- 60 days to report (>500 affected)
- Individual notification required

**PCI DSS (Payment Cards):**
- Immediate notification
- Forensic investigation required

**State Laws (US):**
- Varies by state
- Generally "without unreasonable delay"

## Best Practices

### Preparation
- Maintain updated IR plan
- Quarterly tabletop exercises
- Test backups monthly
- Keep contacts current

### Detection
- Deploy comprehensive logging
- Enable SIEM/EDR
- Tune alert thresholds
- Practice threat hunting

### Response
- Isolate, don't power off
- Document everything
- Preserve evidence
- Engage experts when needed

### Recovery
- Staged rollout (not all at once)
- Monitor 72h for reinfection
- Enhanced security posture
- Validate before restore

### Post-Incident
- Blameless lessons learned
- Implement improvements
- Share IOCs
- Measure MTTD/MTTR

## Resources

**Standards:**
- NIST SP 800-61r2
- MITRE ATT&CK: https://attack.mitre.org/
- SANS Incident Handbook

**Training:**
- GCIH, GCFA (GIAC)
- CISM, CISSP

**Communities:**
- FIRST (https://www.first.org/)
- SANS ISC (https://isc.sans.edu/)

**Tools:**
- Volatility (memory forensics)
- Autopsy (disk forensics)
- Wireshark (network)
- Splunk/ELK (SIEM)

## License

MIT
