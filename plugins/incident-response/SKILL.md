# Incident Response Skill

Expert knowledge for security incident detection, analysis, containment, eradication, recovery, and post-incident activities following NIST IR Framework and MITRE ATT&CK.

## Overview

This skill provides comprehensive patterns, methodologies, and best practices for conducting professional security incident response operations aligned with industry standards (NIST 800-61r2, MITRE ATT&CK, SANS Incident Handler's Handbook).

## Core Framework: NIST Incident Response Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│                    PREPARATION                               │
│  • IR Plan  • Tools  • Training  • Communications           │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│             DETECTION & ANALYSIS                             │
│  • Alerts  • SIEM  • IOCs  • Threat Intel  • Classification│
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│            CONTAINMENT, ERADICATION & RECOVERY               │
│  • Isolate  • Remediate  • Restore  • Validate             │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│              POST-INCIDENT ACTIVITY                          │
│  • Lessons Learned  • Report  • IOC Sharing  • Improve     │
└─────────────────────────────────────────────────────────────┘
```

## Incident Severity Classification

### SEV-1: Critical (P1)
**Impact:** Active data breach, ransomware encryption, complete system compromise
**Response Time:** Immediate (< 15 minutes)
**Escalation:** C-level, legal, PR, external IR team
**Resources:** Full IR team, external forensics if needed

**Indicators:**
- Active data exfiltration detected
- Ransomware encryption in progress
- Critical infrastructure compromise (domain controllers, firewalls)
- Public data breach notification required
- Nation-state APT activity confirmed

**Example Scenarios:**
- Ransomware spreading across network
- Payment card data exfiltration
- Compromised CEO credentials used for wire fraud
- Database dump posted on dark web

### SEV-2: High (P2)
**Impact:** Confirmed breach, significant system compromise, malware infection
**Response Time:** < 1 hour
**Escalation:** IR team lead, security management, affected business units
**Resources:** Core IR team, specialists as needed

**Indicators:**
- Confirmed malware infection
- Unauthorized access to sensitive systems
- Privilege escalation detected
- Data staging for exfiltration
- Multiple compromised accounts

**Example Scenarios:**
- Phishing campaign targeting executives
- Malware infection on file servers
- Compromised service account with elevated privileges
- Insider threat detected

### SEV-3: Medium (P3)
**Impact:** Suspicious activity, potential compromise, contained threat
**Response Time:** < 4 hours
**Escalation:** Security operations, system owners
**Resources:** SOC analyst, system administrators

**Indicators:**
- Anomalous login patterns
- Failed intrusion attempts
- Suspicious network traffic
- Policy violations
- Vulnerability exploitation attempts

**Example Scenarios:**
- Brute force attack on web application
- Suspicious email attachment opened
- Unauthorized software installation
- Potential account compromise

### SEV-4: Low (P4)
**Impact:** Policy violation, security event requiring investigation
**Response Time:** Next business day
**Escalation:** SOC monitoring
**Resources:** Standard security monitoring

**Indicators:**
- Minor policy violations
- False positive alerts requiring validation
- Low-risk security events
- Informational alerts

## MITRE ATT&CK Framework Integration

### Tactic-to-Technique Mapping

#### TA0001: Initial Access
Common techniques:
- **T1566**: Phishing (Spearphishing Attachment, Link, Service)
- **T1190**: Exploit Public-Facing Application
- **T1133**: External Remote Services
- **T1078**: Valid Accounts

**Detection:**
- Email gateway logs
- Web application firewall alerts
- VPN/RDP authentication logs
- Failed login attempts

**Response:**
- Isolate affected accounts
- Block malicious domains/IPs
- Patch vulnerable applications
- Reset compromised credentials

#### TA0002: Execution
Common techniques:
- **T1059**: Command and Scripting Interpreter (PowerShell, Bash, Python)
- **T1047**: Windows Management Instrumentation
- **T1053**: Scheduled Task/Job
- **T1204**: User Execution

**Detection:**
- EDR process execution logs
- PowerShell logging
- Script execution monitoring
- Scheduled task creation

**Response:**
- Kill malicious processes
- Remove scheduled tasks
- Block script execution
- Collect process memory dumps

#### TA0003: Persistence
Common techniques:
- **T1136**: Create Account
- **T1543**: Create/Modify System Process
- **T1547**: Boot/Logon Autostart Execution
- **T1098**: Account Manipulation

**Detection:**
- Account creation logs
- Registry modifications
- Startup folder monitoring
- Service creation events

**Response:**
- Remove unauthorized accounts
- Delete persistence mechanisms
- Restore registry keys
- Document all changes

#### TA0004: Privilege Escalation
Common techniques:
- **T1068**: Exploitation for Privilege Escalation
- **T1134**: Access Token Manipulation
- **T1078**: Valid Accounts (with elevated privileges)
- **T1055**: Process Injection

**Detection:**
- UAC bypass attempts
- Token manipulation events
- Suspicious process ancestry
- Privilege changes

**Response:**
- Terminate escalated processes
- Patch vulnerabilities
- Review account permissions
- Implement least privilege

#### TA0005: Defense Evasion
Common techniques:
- **T1070**: Indicator Removal (Clear logs, File deletion)
- **T1112**: Modify Registry
- **T1562**: Impair Defenses (Disable AV, Logging)
- **T1027**: Obfuscated Files or Information

**Detection:**
- Log clearing events
- Security tool tampering
- File system monitoring
- Registry monitoring

**Response:**
- Restore deleted logs from backups
- Re-enable security controls
- Collect forensic evidence
- Implement write-once logging

#### TA0006: Credential Access
Common techniques:
- **T1003**: OS Credential Dumping (LSASS, SAM)
- **T1110**: Brute Force
- **T1555**: Credentials from Password Stores
- **T1056**: Input Capture (Keylogging)

**Detection:**
- LSASS access attempts
- Failed login spikes
- Credential dumping tools
- Keyboard hooking

**Response:**
- Force password resets
- Enable MFA
- Isolate compromised systems
- Hunt for lateral movement

#### TA0007: Discovery
Common techniques:
- **T1087**: Account Discovery
- **T1083**: File and Directory Discovery
- **T1018**: Remote System Discovery
- **T1016**: System Network Configuration Discovery

**Detection:**
- Network scanning
- Reconnaissance commands
- Enumeration scripts
- Port scanning

**Response:**
- Monitor for lateral movement
- Segment network
- Block reconnaissance tools
- Enhance detection rules

#### TA0008: Lateral Movement
Common techniques:
- **T1021**: Remote Services (RDP, SMB, SSH, WinRM)
- **T1570**: Lateral Tool Transfer
- **T1550**: Use Alternate Authentication Material
- **T1080**: Taint Shared Content

**Detection:**
- Abnormal remote connections
- File transfers between hosts
- Pass-the-hash detection
- SMB/RDP session monitoring

**Response:**
- Isolate affected systems
- Block lateral movement paths
- Reset domain credentials
- Implement network segmentation

#### TA0009: Collection
Common techniques:
- **T1005**: Data from Local System
- **T1039**: Data from Network Shared Drive
- **T1114**: Email Collection
- **T1113**: Screen Capture

**Detection:**
- Large file access patterns
- Data staging activities
- Email export operations
- Screenshot tools

**Response:**
- Identify collected data
- Block data staging locations
- Preserve evidence
- Assess data sensitivity

#### TA0010: Exfiltration
Common techniques:
- **T1041**: Exfiltration Over C2 Channel
- **T1048**: Exfiltration Over Alternative Protocol
- **T1567**: Exfiltration Over Web Service
- **T1029**: Scheduled Transfer

**Detection:**
- Unusual outbound traffic
- Large data transfers
- Cloud storage uploads
- DNS tunneling

**Response:**
- Block exfiltration channels
- Capture network traffic
- Identify stolen data
- Notify affected parties

#### TA0011: Command and Control
Common techniques:
- **T1071**: Application Layer Protocol (HTTP, DNS, Mail)
- **T1573**: Encrypted Channel
- **T1095**: Non-Application Layer Protocol
- **T1572**: Protocol Tunneling

**Detection:**
- Beaconing traffic
- Unknown domain connections
- Encrypted traffic to suspicious IPs
- DNS anomalies

**Response:**
- Block C2 infrastructure
- Sinkhole malicious domains
- Capture C2 communications
- Identify all infected hosts

#### TA0040: Impact
Common techniques:
- **T1486**: Data Encrypted for Impact (Ransomware)
- **T1485**: Data Destruction
- **T1490**: Inhibit System Recovery
- **T1491**: Defacement

**Detection:**
- Mass file encryption
- Backup deletion
- Shadow copy removal
- Website defacement

**Response:**
- Isolate infected systems immediately
- Preserve evidence
- Initiate recovery procedures
- Assess data loss

## Evidence Collection & Chain of Custody

### Evidence Types

**1. Volatile Evidence (Order of Volatility)**
Priority order for collection:
1. CPU registers, cache
2. Routing tables, ARP cache, process tables, kernel statistics
3. Memory (RAM)
4. Temporary file systems
5. Disk
6. Remote logging data
7. Physical configuration, network topology
8. Archival media

**Collection Commands:**
```bash
# Memory capture
# Linux
sudo lime-util --format raw --output memory.raw

# Windows (with FTK Imager or WinPmem)
winpmem.exe -o memory.raw

# Process list
# Linux
ps aux > process_list.txt
netstat -antp > network_connections.txt
lsof > open_files.txt

# Windows
tasklist /v > process_list.txt
netstat -ano > network_connections.txt

# Network connections
ss -tunap > network_state.txt
arp -a > arp_cache.txt

# Logged-in users
w > logged_users.txt
last > login_history.txt
```

**2. Non-Volatile Evidence**
```bash
# Disk imaging
# Linux
sudo dd if=/dev/sda of=/mnt/evidence/disk.img bs=64K conv=noerror,sync
sudo dcfldd if=/dev/sda of=/mnt/evidence/disk.img hash=md5,sha256 hashlog=hash.txt

# Create hash
md5sum disk.img > disk.img.md5
sha256sum disk.img > disk.img.sha256

# File system timeline
fls -r -m / /dev/sda1 > filesystem_timeline.txt

# Collect logs
tar czf logs_$(date +%Y%m%d_%H%M%S).tar.gz /var/log/

# Windows Event Logs
wevtutil epl Security Security.evtx
wevtutil epl System System.evtx
wevtutil epl Application Application.evtx
```

### Chain of Custody Documentation

**Evidence Log Template:**
```
EVIDENCE COLLECTION LOG
=======================
Case Number: INC-2025-0001
Incident: Suspected ransomware infection
Date/Time: 2025-01-15 14:30:00 UTC
Collected By: John Smith
Witness: Jane Doe

ITEM 1:
-------
Description: Memory dump from web-server-01
Source: 192.168.1.100 (web-server-01.corp.local)
Collection Method: WinPmem physical memory acquisition
File: web-server-01_memory_20250115_1430.raw
Size: 16,384 MB
MD5: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
SHA256: 1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
Storage Location: Evidence locker #3, drive EVI-001
Notes: System was in active infection state during collection

CHAIN OF CUSTODY:
Date/Time       | Transferred From  | Transferred To    | Purpose          | Signature
----------------|-------------------|-------------------|------------------|----------
2025-01-15 14:30| John Smith       | Evidence Locker   | Secure storage   | J.Smith
2025-01-15 16:00| Evidence Locker  | Forensic Lab      | Analysis         | M.Jones
```

### Evidence Handling Best Practices

**DO:**
- Use write-blockers for disk imaging
- Calculate cryptographic hashes immediately
- Document everything (photos, notes, timestamps)
- Maintain strict chain of custody
- Store evidence in secure, access-controlled location
- Create working copies for analysis
- Label evidence clearly and consistently
- Get legal guidance before collection

**DON'T:**
- Analyze original evidence (always use copies)
- Turn off systems before memory capture
- Trust system timestamps (may be altered)
- Collect evidence without proper authorization
- Break chain of custody
- Use untrusted tools
- Modify evidence
- Share evidence without proper authorization

## Forensic Analysis Methodologies

### Timeline Analysis

**Purpose:** Reconstruct incident chronology from multiple data sources

**Process:**
```bash
# 1. Collect timestamped events
# File system timeline (MAC times)
fls -r -m / /mnt/evidence/disk.img > fs_timeline.txt

# Windows Registry timeline
regripper -r /mnt/evidence/SYSTEM -p timeline > registry_timeline.txt

# Log analysis
# Parse web logs
cat access.log | awk '{print $4, $1, $7}' > web_timeline.txt

# Parse authentication logs
grep -E "sshd|login|sudo" /var/log/auth.log > auth_timeline.txt

# 2. Normalize timestamps to UTC
# 3. Merge all timelines
# 4. Filter to incident timeframe
# 5. Identify key events:
#    - Initial compromise
#    - Lateral movement
#    - Data access
#    - Exfiltration
#    - Persistence establishment

# Super timeline with Plaso/log2timeline
log2timeline.py --storage-file timeline.plaso disk.img
psort.py -o dynamic -w timeline.csv timeline.plaso
```

### Indicator of Compromise (IOC) Identification

**Network IOCs:**
```bash
# Extract unique IPs from network logs
cat network.log | awk '{print $5}' | sort -u > unique_ips.txt

# Check against threat intelligence
while read ip; do
  curl -s "https://otx.alienvault.com/api/v1/indicators/IPv4/$ip/general" | jq .
done < unique_ips.txt

# DNS queries to suspicious domains
grep -E "\.tk$|\.ml$|\.ga$" dns.log

# Port scan detection
netstat -an | grep SYN_SENT | wc -l
```

**File IOCs:**
```bash
# File hash calculation
find /suspect/directory -type f -exec md5sum {} \; > file_hashes.txt

# VirusTotal lookup
curl --request GET \
  --url "https://www.virustotal.com/api/v3/files/$FILE_HASH" \
  --header "x-apikey: $VT_API_KEY"

# YARA scanning
yara -r /usr/share/yara-rules/ /suspect/directory

# Check for common malware paths
find / -name "*.tmp.exe" -o -name "~*.exe" -o -path "*/AppData/Roaming/*.exe"
```

**Registry IOCs (Windows):**
```bash
# Persistence locations
reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\Run"
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce"

# Recent documents
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs"

# USB history
reg query "HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR"
```

### Memory Forensics

```bash
# Using Volatility 3
vol3 -f memory.raw windows.info          # System info
vol3 -f memory.raw windows.pslist        # Process list
vol3 -f memory.raw windows.pstree        # Process tree
vol3 -f memory.raw windows.cmdline       # Command lines
vol3 -f memory.raw windows.netscan       # Network connections
vol3 -f memory.raw windows.malfind       # Malware detection
vol3 -f memory.raw windows.dlllist       # Loaded DLLs
vol3 -f memory.raw windows.handles       # Open handles
vol3 -f memory.raw windows.registry.printkey --key "Software\Microsoft\Windows\CurrentVersion\Run"

# Extract suspicious process
vol3 -f memory.raw windows.memmap --pid 1234 --dump

# Scan for malware signatures
vol3 -f memory.raw windows.vadyarascan --yara-file malware_rules.yar

# Linux memory analysis
vol3 -f memory.raw linux.bash            # Bash history
vol3 -f memory.raw linux.pslist          # Processes
vol3 -f memory.raw linux.lsof            # Open files
```

### Log Analysis

**Web Server Logs:**
```bash
# Find SQL injection attempts
grep -iE "union.*select|concat\(|0x[0-9a-f]+" access.log

# Command injection
grep -iE "\||;|`|\$\(|&&" access.log

# Directory traversal
grep -E "\.\./|\.\.\\\\" access.log

# Top attacking IPs
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -20

# Failed authentication attempts
grep "401\|403" access.log | wc -l

# Large POST requests (potential data exfiltration)
awk '$6 == "POST" && $10 > 1000000 {print $0}' access.log
```

**Authentication Logs:**
```bash
# Failed SSH logins
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c

# Successful logins from unusual IPs
grep "Accepted" /var/log/auth.log | grep -v "192.168.1."

# Sudo usage
grep "sudo" /var/log/auth.log | grep -v "session"

# Account creation/modification
grep -E "useradd|usermod|passwd" /var/log/auth.log
```

**Windows Event Logs:**
```powershell
# Failed logons (Event ID 4625)
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4625} | Select-Object TimeCreated, Message

# Successful logons (Event ID 4624)
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4624} | Where-Object {$_.Properties[8].Value -eq 10}

# Account creation (Event ID 4720)
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4720}

# Service installation (Event ID 7045)
Get-WinEvent -FilterHashtable @{LogName='System'; ID=7045}

# PowerShell execution (Event ID 4104)
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational'; ID=4104}
```

## Incident Response Playbooks

### Playbook 1: Ransomware Infection

**Severity:** SEV-1 (Critical)
**Detection Triggers:**
- Mass file encryption detected
- Ransom note files (.txt, .html)
- Backup deletion attempts
- Shadow copy removal
- Unknown encryption processes

**Immediate Actions (0-15 minutes):**
```bash
# 1. ISOLATE infected systems immediately
# Disconnect network (don't power off - preserves memory)
# Physical: Unplug network cable
# Virtual: Disable network adapter
# Network: Block at switch/firewall

# 2. IDENTIFY scope
# Check for other infected systems
# Review file server access logs
# Check backup integrity

# 3. PRESERVE evidence
# Capture memory
sudo lime-util --format raw --output infected_host_memory.raw

# Screenshot ransom note
# Document file extensions (.encrypted, .locked, etc.)

# 4. ALERT stakeholders
# IR team
# Management (C-level)
# Legal
# PR (if public facing)
# Law enforcement (FBI IC3)

# 5. ENGAGE external help if needed
# Ransomware negotiation firm
# Professional IR team
# Forensics specialists
```

**Containment (15-60 minutes):**
```bash
# 1. Network segmentation
# Isolate affected network segments
# Block SMB/RDP between segments
iptables -A INPUT -p tcp --dport 445 -j DROP
iptables -A INPUT -p tcp --dport 3389 -j DROP

# 2. Disable compromised accounts
# AD: Disable user accounts
Get-ADUser -Filter {Enabled -eq $true} | Disable-ADAccount

# Force password reset
# Revoke authentication tokens

# 3. Check backups
# Verify backup integrity (disconnected backups)
# Test restore capability
# Ensure backups are offline/air-gapped

# 4. Kill encryption processes
# Identify ransomware process
ps aux | grep -iE "encrypt|ransom|lock"
kill -9 <PID>

# Windows
tasklist | findstr /i "encrypt ransom lock"
taskkill /F /PID <PID>
```

**Eradication (1-4 hours):**
```bash
# 1. Identify ransomware variant
# Upload sample to:
#   - https://id-ransomware.malwarehunterteam.com/
#   - https://www.nomoreransom.org/crypto-sheriff.php

# 2. Check for decryptor
# https://www.nomoreransom.org/en/decryption-tools.html

# 3. Remove malware
# Boot from clean media
# Scan with multiple AV engines
# Manual removal if needed

# 4. Rebuild vs restore decision
# Rebuild from known-good images (preferred)
# Or: Clean existing systems (higher risk)

# 5. Patch vulnerabilities
# Update all systems
# Close attack vector (patch exploited vulnerability)
```

**Recovery (4-24 hours):**
```bash
# 1. Restore from backups
# Restore to point before infection
# Verify data integrity
rsync -av --checksum /mnt/backup/data/ /restored/data/

# 2. Validate restoration
# Check file integrity
# Test applications
# Verify no reinfection

# 3. Gradual network reconnection
# Monitor for reinfection signs
# Incremental restoration

# 4. Enhanced monitoring
# Deploy EDR if not present
# Increase logging verbosity
# 24/7 SOC monitoring
```

**Post-Incident (24-72 hours):**
```bash
# 1. Root cause analysis
# How did ransomware enter?
# Why did it spread?
# Why didn't detection work?

# 2. Lessons learned meeting
# What worked well?
# What needs improvement?
# Action items with owners

# 3. Improve defenses
# Implement offline backups
# Network segmentation
# Email filtering
# MFA enforcement
# Application whitelisting

# 4. Documentation
# Incident report
# Timeline
# IOCs
# Recommendations
```

### Playbook 2: Data Breach / Exfiltration

**Severity:** SEV-1 (Critical)
**Detection Triggers:**
- Large outbound data transfers
- Database dump activity
- Sensitive data access outside normal hours
- Data staging in unusual locations
- Alerts from DLP system

**Immediate Actions (0-15 minutes):**
```bash
# 1. CONFIRM the breach
# Review DLP alerts
# Check data access logs
# Verify exfiltration occurred

# 2. BLOCK ongoing exfiltration
# Block destination IPs/domains
iptables -A OUTPUT -d $MALICIOUS_IP -j DROP

# Block user/service account
# Disable compromised credentials

# 3. CAPTURE evidence
# Network traffic capture
tcpdump -i eth0 -w exfiltration_capture.pcap host $MALICIOUS_IP

# Process list and network connections
netstat -antp > network_state.txt
ps auxf > process_tree.txt

# 4. NOTIFY
# Legal team (attorney-client privilege)
# Privacy officer
# Compliance team
# DO NOT notify affected individuals yet (legal guidance required)
```

**Analysis (15-120 minutes):**
```bash
# 1. Identify WHAT was exfiltrated
# Review accessed files
find / -type f -mtime -7 -user $COMPROMISED_USER

# Database query logs
# File server access logs
# Email sent items

# 2. Identify HOW MUCH data
# Analyze network traffic
# File sizes
# Database row counts

# 3. Identify WHEN
# Timeline analysis
# First access to last exfiltration

# 4. Identify WHERE it went
# IP address geolocation
# Domain registration
# Cloud storage services
# Pastebin, GitHub, etc.

# 5. Classify data sensitivity
# PII (Personally Identifiable Information)
# PHI (Protected Health Information)
# PCI (Payment Card Information)
# Trade secrets
# Credentials
```

**Containment:**
```bash
# 1. Isolate affected systems
# Prevent further access

# 2. Revoke credentials
# Force password resets
# Revoke API keys
# Rotate database credentials

# 3. Block exfiltration channels
# Firewall rules
# Proxy blocking
# DNS sinkholing

# 4. Notify external parties
# Cloud providers (if data stored there)
# Law enforcement
# Cyber insurance
```

**Legal/Regulatory (Parallel Track):**
```bash
# 1. Breach notification requirements
# GDPR: 72 hours to notify supervisory authority
# CCPA: Notify California AG if >500 CA residents affected
# HIPAA: 60 days to notify HHS, affected individuals
# State laws: Vary by state

# 2. Document for regulators
# What data was accessed
# Number of individuals affected
# Steps taken to mitigate
# Contact information for inquiries

# 3. Prepare notification letters
# Draft with legal review
# Include:
#   - What happened
#   - What data was involved
#   - What we're doing about it
#   - What affected individuals should do
#   - Contact information for questions
```

### Playbook 3: DDoS Attack

**Severity:** SEV-2 (High) to SEV-1 (Critical depending on impact)
**Detection Triggers:**
- Website/service unavailable
- Bandwidth saturation
- Server resource exhaustion
- Firewall connection table full

**Immediate Actions (0-5 minutes):**
```bash
# 1. CONFIRM DDoS vs legitimate traffic spike
# Check traffic patterns
netstat -an | grep :80 | wc -l
ss -s  # Socket statistics

# Review web server access logs
tail -f /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -rn

# 2. NOTIFY
# Network team
# Cloud/hosting provider
# DDoS mitigation service (Cloudflare, Akamai, AWS Shield)

# 3. CAPTURE traffic sample
tcpdump -i eth0 -c 10000 -w ddos_sample.pcap
```

**Mitigation:**
```bash
# 1. Enable DDoS protection service
# Cloudflare: Enable "Under Attack" mode
# AWS: AWS Shield Standard/Advanced
# On-prem: Redirect traffic through scrubbing center

# 2. Rate limiting (temporary)
# Nginx
limit_req_zone $binary_remote_addr zone=ddos:10m rate=10r/s;
limit_req zone=ddos burst=20;

# iptables
iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j DROP

# 3. Block attack sources
# GeoIP blocking (if attack from specific countries)
# ASN blocking
# IP reputation blocking

# 4. Traffic scrubbing
# Route traffic through DDoS mitigation service
# Keep origin server IPs secret
```

**Analysis:**
```bash
# Identify attack type
# 1. Volumetric (flood)
#    - UDP flood
#    - ICMP flood
#    - DNS amplification

# 2. Protocol attacks
#    - SYN flood
#    - ACK flood
#    - Fragmented packets

# 3. Application layer (Layer 7)
#    - HTTP flood
#    - Slowloris
#    - RUDY (R-U-Dead-Yet)

# Check for botnet signatures
# Analyze user agents
# Request patterns
# TLS fingerprints
```

### Playbook 4: Insider Threat

**Severity:** SEV-2 (High) to SEV-1 (Critical)
**Detection Triggers:**
- Unusual data access by employee
- Off-hours system access
- Data download to personal devices
- Accessing systems/data outside role
- Disgruntled employee behavior

**Immediate Actions (0-30 minutes):**
```bash
# 1. VALIDATE the alert
# Review user activity logs
# Confirm unauthorized access
# Assess intent (malicious vs policy violation)

# 2. CONSULT legal/HR
# Insider threats have legal/employment implications
# Get guidance before taking action
# Consider:
#   - Employment law
#   - Union agreements
#   - Privacy rights

# 3. PRESERVE evidence
# DO NOT alert the user yet
# Enable detailed logging
# Monitor ongoing activity

# 4. ASSESS current risk
# Is data being exfiltrated now?
# Is sabotage occurring?
# Is there immediate danger?
```

**Covert Monitoring (If legally approved):**
```bash
# 1. Enhanced logging (without user knowledge)
# Capture screen activity
# Keystroke logging (only if legally permissible)
# File access auditing
# Email monitoring

# 2. Network monitoring
# Packet capture for user's traffic
tcpdump -i eth0 host $USER_IP -w insider_traffic.pcap

# 3. Endpoint monitoring
# Process execution
# File operations
# USB device usage
# Cloud upload activity
```

**Containment (With legal/HR approval):**
```bash
# 1. Limit access (gracefully)
# Reduce privileges without alerting user
# "System maintenance" excuse if needed

# 2. Prevent data destruction
# Backup user's files
# Shadow copy of workstation
# Preserve email

# 3. When ready to act (coordinated with HR/legal)
# Disable account
# Revoke physical access
# Remote wipe mobile devices
# Collect company property
```

**Investigation:**
```bash
# 1. Timeline of activity
# When did suspicious behavior start?
# What triggered it? (Negative review, termination notice?)

# 2. Data inventory
# What data did user access?
# What was downloaded/copied?
# Where did it go?

# 3. Co-conspirators
# Did user share data with others?
# Were other accounts used?

# 4. Impact assessment
# Competitive harm
# Regulatory implications
# Trade secret theft
```

## Communication Protocols During Incidents

### Internal Communication

**Incident Response Team Structure:**
```
Incident Commander (IC)
├── Technical Lead (Forensics, Containment)
├── Communications Lead (Stakeholder updates)
├── Legal Lead (Regulatory, Law enforcement)
└── Business Lead (Business impact, Recovery)
```

**Communication Channels:**
- **Primary:** Dedicated Slack/Teams channel: `#incident-response-active`
- **Backup:** Conference bridge: 1-800-XXX-XXXX, PIN: XXXX
- **Emergency:** Direct phone tree

**Update Frequency:**
- SEV-1: Every 30 minutes
- SEV-2: Every 2 hours
- SEV-3: Daily
- SEV-4: As needed

**Status Report Template:**
```
INCIDENT STATUS UPDATE #5
Time: 2025-01-15 16:00 UTC
Incident: INC-2025-0001 - Ransomware
Severity: SEV-1
Status: Containment Phase

CURRENT SITUATION:
- 15 servers confirmed infected
- 3 servers isolated and offline
- 12 servers in remediation
- No new infections in last 30 minutes

ACTIONS TAKEN:
- Network segmentation implemented
- Disabled compromised accounts (23 accounts)
- Engaged external forensics team (CrowdStrike)
- Backup integrity verified

NEXT STEPS:
- Complete isolation of remaining infected systems (ETA: 17:00 UTC)
- Begin restoration from backups (ETA: 18:00 UTC)
- Deploy EDR to all systems (ETA: Tomorrow 09:00 UTC)

BLOCKERS:
- None

NEXT UPDATE: 16:30 UTC
```

### External Communication

**Law Enforcement Notification:**
When to notify:
- Ransomware (FBI Internet Crime Complaint Center - IC3)
- Nation-state APT
- Child exploitation material discovered
- Criminal activity

**FBI IC3:** https://ic3.gov/
**FBI Cyber Division:** (Local field office)
**Secret Service:** (Financial crimes)
**Local Police:** (Physical security incidents)

**Regulatory Notification:**
```
# GDPR (EU)
Supervisory Authority: Within 72 hours of becoming aware
Data Subjects: Without undue delay

# HIPAA (US Healthcare)
HHS: Within 60 days (if >500 individuals)
Media: Same timeline (if >500 in jurisdiction)
Individuals: Within 60 days

# PCI DSS (Payment Cards)
Card Brands: Immediately upon detection
Acquirer/Bank: Per contract terms

# State Breach Laws (US)
Varies by state - typically:
- Without unreasonable delay
- After law enforcement clearance (if requested)
```

**Customer/Public Notification:**
```
Template for breach notification:

Subject: Important Security Notice - [Company Name]

Dear [Customer Name],

We are writing to inform you of a data security incident that may have
affected your personal information.

WHAT HAPPENED:
On [Date], we discovered that [brief description]. We immediately began
an investigation with the assistance of leading cybersecurity experts.

WHAT INFORMATION WAS INVOLVED:
The information that may have been accessed includes: [specific data types]

WHAT WE ARE DOING:
We have [steps taken to secure systems]. We are also [additional measures].

WHAT YOU CAN DO:
[Specific recommendations]:
- Monitor your accounts for suspicious activity
- Consider placing a fraud alert or credit freeze
- Be alert for phishing attempts

FOR MORE INFORMATION:
We have established a dedicated helpline: 1-800-XXX-XXXX
Available Monday-Friday, 8am-8pm EST
Or visit: www.company.com/security-notice

We sincerely apologize for this incident and any inconvenience.

Sincerely,
[Name]
[Title]
```

## Legal and Regulatory Requirements

### Data Retention for Incidents

**Preserve evidence for:**
- **Litigation:** Statute of limitations varies (2-10 years)
- **Regulatory:** Often 7 years
- **Cyber insurance:** Per policy (typically 3-5 years)
- **Internal policy:** Minimum 1 year recommended

**What to preserve:**
- Forensic disk images
- Memory dumps
- Log files
- Network captures
- Email correspondence
- Incident reports
- Chain of custody documentation
- Legal holds

**Storage requirements:**
- Write-once media (WORM)
- Encrypted at rest
- Access-controlled
- Geographically distributed backups
- Regular integrity verification

### Legal Holds

**When to implement:**
- Anticipated litigation
- Regulatory investigation
- Law enforcement request
- Insurance claim

**Scope:**
- All documents related to incident
- Communications between IR team
- Email from/to affected individuals
- System logs
- Forensic evidence

**Process:**
```bash
# 1. Legal team issues hold notice
# 2. Identify custodians (people with relevant data)
# 3. Preserve data in place
# 4. Copy data to secure storage
# 5. Document preservation actions
# 6. Ongoing monitoring until released
```

## Threat Intelligence Integration

### IOC Sharing

**Where to share:**
- **ISAC (Information Sharing and Analysis Centers):**
  - FS-ISAC (Financial Services)
  - H-ISAC (Healthcare)
  - MS-ISAC (State/Local Government)
  - Auto-ISAC (Automotive)

- **STIX/TAXII feeds**
- **MISP (Malware Information Sharing Platform)**
- **AlienVault OTX**
- **VirusTotal**

**IOC Formats:**
```bash
# STIX 2.1 Format
{
  "type": "indicator",
  "spec_version": "2.1",
  "id": "indicator--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
  "created": "2025-01-15T14:30:00.000Z",
  "modified": "2025-01-15T14:30:00.000Z",
  "name": "Malicious IP from ransomware campaign",
  "pattern": "[ipv4-addr:value = '203.0.113.42']",
  "pattern_type": "stix",
  "valid_from": "2025-01-15T14:30:00.000Z",
  "indicator_types": ["malicious-activity"],
  "kill_chain_phases": [{
    "kill_chain_name": "mitre-attack",
    "phase_name": "command-and-control"
  }]
}

# OpenIOC Format
<ioc>
  <short_description>Ransomware C2 IP</short_description>
  <definition>
    <Indicator operator="OR">
      <IndicatorItem>
        <Context type="network">Network/IP</Context>
        <Content>203.0.113.42</Content>
      </IndicatorItem>
    </Indicator>
  </definition>
</ioc>

# YARA Rule
rule ransomware_sample_2025 {
    meta:
        description = "Detects XYZ ransomware variant"
        author = "IR Team"
        date = "2025-01-15"
        hash = "abc123..."
    strings:
        $ransom_note = "YOUR FILES HAVE BEEN ENCRYPTED"
        $extension = ".encrypted" wide ascii
        $c2 = "203.0.113.42" wide ascii
    condition:
        2 of them
}
```

### Threat Intelligence Enrichment

```bash
# IP reputation lookup
curl -s "https://otx.alienvault.com/api/v1/indicators/IPv4/$IP/general" | jq .

# Domain reputation
curl -s "https://otx.alienvault.com/api/v1/indicators/domain/$DOMAIN/general" | jq .

# File hash lookup (VirusTotal)
curl --request GET \
  --url "https://www.virustotal.com/api/v3/files/$FILE_HASH" \
  --header "x-apikey: $VT_API_KEY" | jq .

# Threat intelligence platform query (ThreatConnect, MISP, etc.)
# Check if IOC is known malicious
# Get associated campaigns, threat actors
# Identify TTPs
```

## Performance Metrics

**Mean Time to Detect (MTTD):**
```
MTTD = Time of Detection - Time of Initial Compromise
Goal: < 24 hours
Industry Average: ~200 days
```

**Mean Time to Respond (MTTR):**
```
MTTR = Time of Containment - Time of Detection
Goal: < 1 hour for SEV-1
```

**Mean Time to Recover (MTTR):**
```
MTTR = Time Systems Fully Restored - Time of Detection
Goal: < 24 hours for SEV-1
```

**False Positive Rate:**
```
FPR = False Positives / (False Positives + True Positives)
Goal: < 10%
```

## Post-Incident Review Template

```markdown
# Post-Incident Review: [Incident ID]

## Executive Summary
- **Incident:** [Brief description]
- **Severity:** SEV-X
- **Duration:** [Date/time started] to [Date/time resolved]
- **Impact:** [Business impact, data loss, downtime]
- **Root Cause:** [Primary cause]

## Timeline
| Time (UTC) | Event |
|------------|-------|
| 2025-01-15 10:00 | Initial compromise via phishing email |
| 2025-01-15 10:15 | Malware executed, establishes persistence |
| 2025-01-15 14:30 | Detection: EDR alerts on suspicious process |
| 2025-01-15 14:35 | IR team engaged |
| 2025-01-15 15:00 | Containment: Infected system isolated |
| 2025-01-15 16:00 | Eradication: Malware removed |
| 2025-01-15 18:00 | Recovery: System restored from backup |
| 2025-01-16 09:00 | Monitoring: Enhanced logging in place |

## What Went Well
1. EDR detected the threat within 4 hours
2. IR team responded quickly (5 minute response time)
3. Backups were available and clean
4. Clear communication with stakeholders

## What Went Wrong
1. Phishing email bypassed email gateway
2. User opened malicious attachment despite training
3. No MFA on compromised account
4. Detection took 4 hours (could be faster)
5. Incomplete inventory of affected systems initially

## Root Cause Analysis
**Primary Cause:** Spear phishing email with malicious macro
**Contributing Factors:**
- Email gateway did not detect malicious attachment
- User clicked despite security awareness training
- No MFA enabled on account
- Insufficient email security controls

## Lessons Learned
1. **Email Security:** Need advanced threat protection (ATP)
2. **User Training:** More frequent, realistic phishing simulations
3. **MFA:** Enforce MFA for all users, no exceptions
4. **Detection:** Tune EDR for faster detection
5. **Asset Inventory:** Maintain better CMDB for complete scope identification

## Action Items
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| Implement ATP email protection | Security Team | 2025-02-01 | In Progress |
| Deploy MFA to all users | IT Team | 2025-01-30 | In Progress |
| Conduct phishing simulation | HR/Security | 2025-02-15 | Not Started |
| Tune EDR detection rules | SOC Team | 2025-01-25 | In Progress |
| Update asset inventory | IT Team | 2025-01-31 | Not Started |

## IOCs
**IP Addresses:**
- 203.0.113.42 (C2 server)
- 198.51.100.15 (Data staging)

**Domains:**
- evil-domain.tk
- malicious-site.ml

**File Hashes (SHA256):**
- a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a7b8c9d0e1f2

**MITRE ATT&CK Techniques:**
- T1566.001 (Phishing: Spearphishing Attachment)
- T1204.002 (User Execution: Malicious File)
- T1059.003 (Command and Scripting Interpreter: Windows Command Shell)
- T1547.001 (Boot or Logon Autostart Execution: Registry Run Keys)

## Recommendations
1. **Short-term (0-30 days):**
   - Deploy MFA
   - Implement ATP email protection
   - Conduct emergency phishing simulation

2. **Medium-term (30-90 days):**
   - Review and update security awareness training
   - Enhance EDR detection capabilities
   - Implement application whitelisting

3. **Long-term (90+ days):**
   - Deploy SOAR platform for automation
   - Implement zero-trust architecture
   - Regular tabletop exercises
```

## Tools & Resources

### Essential IR Tools

**Network Analysis:**
- Wireshark / tcpdump
- Zeek (formerly Bro)
- NetworkMiner
- Nmap

**Forensics:**
- Volatility (Memory forensics)
- Autopsy / The Sleuth Kit
- FTK Imager
- X-Ways Forensics

**Malware Analysis:**
- IDA Pro / Ghidra
- Cuckoo Sandbox
- Any.run
- Joe Sandbox

**SIEM/Log Analysis:**
- Splunk
- Elastic Stack (ELK)
- Graylog
- Chronicle

**Threat Intelligence:**
- MISP
- OpenCTI
- ThreatConnect
- AlienVault OTX

### Reference Materials

**Frameworks:**
- NIST SP 800-61r2: Computer Security Incident Handling Guide
- SANS Incident Handler's Handbook
- MITRE ATT&CK: https://attack.mitre.org/
- Cyber Kill Chain (Lockheed Martin)

**Training & Certifications:**
- GCIH (GIAC Certified Incident Handler)
- GCFA (GIAC Certified Forensic Analyst)
- CISM (Certified Information Security Manager)
- CISSP (Certified Information Systems Security Professional)

**Communities:**
- FIRST (Forum of Incident Response and Security Teams)
- SANS Internet Storm Center
- r/netsec, r/AskNetsec
- InfoSec Twitter community

## Best Practices

1. **Preparation is Key**
   - Develop and test IR plans regularly
   - Conduct tabletop exercises quarterly
   - Maintain updated runbooks
   - Build relationships before incidents (law enforcement, PR, legal)

2. **Speed Matters**
   - Faster detection = less damage
   - Pre-authorized actions reduce decision delays
   - Automation where possible

3. **Document Everything**
   - Assume you'll be testifying
   - Chain of custody is critical
   - Screenshots, timestamps, commands executed

4. **Preserve Evidence**
   - Don't destroy evidence while investigating
   - Work from copies, not originals
   - Hash everything

5. **Communication**
   - Clear, concise, regular updates
   - Know your audience (technical vs executive)
   - Single source of truth for status

6. **Learn and Improve**
   - Every incident is a learning opportunity
   - Conduct post-incident reviews
   - Implement lessons learned
   - Share knowledge with community

7. **Legal First**
   - Engage legal counsel early
   - Understand notification requirements
   - Preserve attorney-client privilege
   - Don't promise what you can't deliver

8. **Assume Breach**
   - Hunt proactively
   - Trust but verify
   - Defense in depth
   - Zero trust architecture
