# HIPAA Security Checklist

## Administrative Safeguards (45 CFR § 164.308)

### Security Management Process (Required)

**Risk Analysis (R)**
- [ ] Risk analysis conducted and documented
- [ ] All systems with ePHI identified
- [ ] Threats and vulnerabilities assessed
- [ ] Impact of threats determined
- [ ] Risk levels assigned

**Risk Management (R)**
- [ ] Risk mitigation measures implemented
- [ ] Residual risks documented and accepted
- [ ] Risk management ongoing

**Sanction Policy (R)**
- [ ] Sanctions for policy violations defined
- [ ] Enforcement process documented
- [ ] Violations tracked and sanctions applied

**Information System Activity Review (R)**
- [ ] Audit logs reviewed regularly
- [ ] Security incident tracking
- [ ] Review frequency defined (at least quarterly)
- [ ] Review findings documented

### Assigned Security Responsibility (Required)

- [ ] Security Officer designated
- [ ] Security Officer responsibilities documented
- [ ] Security Officer has appropriate authority

### Workforce Security (Required)

**Authorization and Supervision (A)**
- [ ] Workforce authorization process
- [ ] Access appropriate to role
- [ ] Supervision procedures for unauthorized access

**Workforce Clearance Procedure (A)**
- [ ] Clearance procedure for ePHI access
- [ ] Background checks where appropriate

**Termination Procedures (A)**
- [ ] Access termination process
- [ ] Deactivation within 24 hours
- [ ] Equipment return procedures
- [ ] Exit interviews

### Information Access Management (Required)

**Isolating Healthcare Clearinghouse Functions (R if applicable)**
- [ ] Electronic ePHI separated from other functions

**Access Authorization (A)**
- [ ] Authorization process for ePHI access
- [ ] Access based on role and minimum necessary
- [ ] Access requests documented and approved

**Access Establishment and Modification (A)**
- [ ] Access provisioning procedures
- [ ] Access modification process
- [ ] Regular access reviews (quarterly/semi-annual)

### Security Awareness and Training (Required)

**Security Reminders (A)**
- [ ] Periodic security updates and reminders
- [ ] Security tips and newsletters

**Protection from Malicious Software (A)**
- [ ] Anti-malware training
- [ ] Procedures for detecting and reporting malware

**Log-in Monitoring (A)**
- [ ] Procedures for monitoring login attempts
- [ ] Failed login alerts

**Password Management (A)**
- [ ] Password creation procedures
- [ ] Password change procedures
- [ ] Password complexity requirements
- [ ] No password sharing policy

### Security Incident Procedures (Required)

**Response and Reporting (R)**
- [ ] Incident identification procedures
- [ ] Incident reporting mechanism
- [ ] Incident response procedures
- [ ] Incident documentation and analysis
- [ ] Mitigation procedures

### Contingency Plan (Required)

**Data Backup Plan (R)**
- [ ] Data backup procedures documented
- [ ] Daily backups of ePHI
- [ ] Backups stored securely offsite
- [ ] Backup restoration tested regularly

**Disaster Recovery Plan (R)**
- [ ] DRP documented
- [ ] Recovery procedures for ePHI
- [ ] Emergency mode operations
- [ ] DRP tested annually

**Emergency Mode Operation Plan (R)**
- [ ] Procedures to continue operations during emergency
- [ ] Critical functions identified
- [ ] Emergency access to ePHI

**Testing and Revision Procedure (A)**
- [ ] Contingency plan tested annually
- [ ] Test results documented
- [ ] Plan updated based on test results

**Applications and Data Criticality Analysis (A)**
- [ ] Critical applications identified
- [ ] Data criticality determined
- [ ] Priorities for recovery

### Evaluation (Required)

- [ ] Technical and non-technical evaluations conducted
- [ ] Evaluation based on risk analysis
- [ ] Evaluation frequency defined (at least annual)
- [ ] Evaluation findings documented
- [ ] Corrective actions tracked

### Business Associate Contracts (Required)

- [ ] Business Associate Agreements (BAAs) with all vendors handling ePHI
- [ ] BAAs include required provisions (45 CFR § 164.314)
- [ ] Subcontractor BAAs required
- [ ] BAA compliance monitored

## Physical Safeguards (45 CFR § 164.310)

### Facility Access Controls (Required)

**Contingency Operations (A)**
- [ ] Facility access during emergencies
- [ ] Physical security maintained during contingency

**Facility Security Plan (A)**
- [ ] Physical security measures documented
- [ ] Building access controls
- [ ] Visitor access procedures

**Access Control and Validation Procedures (A)**
- [ ] Procedures to control physical access
- [ ] Badge/access card system
- [ ] Visitor logs maintained

**Maintenance Records (A)**
- [ ] Facility modification records
- [ ] Physical security repairs documented

### Workstation Use (Required)

- [ ] Workstation use policies defined
- [ ] Physical security for workstations
- [ ] Screen privacy protections
- [ ] Unattended workstation procedures (lock, timeout)

### Workstation Security (Required)

- [ ] Physical restrictions on workstation access
- [ ] Workstation positioning (public view minimized)
- [ ] Physical security locks where appropriate

### Device and Media Controls (Required)

**Disposal (R)**
- [ ] ePHI disposal procedures
- [ ] Media sanitization before disposal/reuse
- [ ] Certificate of destruction for disposed media

**Media Re-use (R)**
- [ ] Procedures for media re-use
- [ ] ePHI removal before re-use
- [ ] Verification of removal

**Accountability (A)**
- [ ] Hardware and electronic media inventory
- [ ] Media movement tracking
- [ ] Accountability for media location

**Data Backup and Storage (A)**
- [ ] Backup media security
- [ ] Offsite storage procedures
- [ ] Backup media inventory

## Technical Safeguards (45 CFR § 164.312)

### Access Control (Required)

**Unique User Identification (R)**
- [ ] Unique user ID for each user
- [ ] No shared accounts
- [ ] User ID associated with individual

**Emergency Access Procedure (R)**
- [ ] Procedures for emergency access to ePHI
- [ ] Break-glass accounts or procedures
- [ ] Emergency access logged and reviewed

**Automatic Logoff (A)**
- [ ] Session timeouts configured
- [ ] Timeout period defined (typically 15-30 min)

**Encryption and Decryption (A)**
- [ ] ePHI encrypted at rest
- [ ] ePHI encrypted in transit
- [ ] Encryption standard: AES-256 or equivalent
- [ ] TLS 1.2+ for transmission

### Audit Controls (Required)

- [ ] Audit logging enabled for ePHI systems
- [ ] Logs capture: user ID, timestamp, action, data accessed
- [ ] Logs protected from tampering
- [ ] Logs reviewed regularly
- [ ] Log retention period defined (typically 6 years)

### Integrity (Required)

**Mechanism to Authenticate ePHI (A)**
- [ ] Methods to verify ePHI not altered/destroyed
- [ ] Checksums or digital signatures
- [ ] Version control for documents

### Person or Entity Authentication (Required)

- [ ] User authentication required
- [ ] Multi-factor authentication (MFA) for remote access
- [ ] MFA for privileged accounts (strongly recommended)
- [ ] Strong authentication mechanisms

### Transmission Security (Required)

**Integrity Controls (A)**
- [ ] Measures to ensure transmitted ePHI not altered
- [ ] Transmission integrity verification

**Encryption (A)**
- [ ] Encryption for ePHI transmitted over networks
- [ ] TLS 1.2+ for web transmission
- [ ] VPN for remote access
- [ ] Secure email (encrypted) for ePHI

## Organizational Requirements (45 CFR § 164.314)

### Business Associate Contracts

- [ ] BAAs with all business associates
- [ ] Required provisions included
- [ ] Subcontractor flow-down requirements
- [ ] BAA breach notification provisions

### Group Health Plans

- [ ] Plan documents amended if required
- [ ] Adequate firewalls between plan and sponsor

## Policies, Procedures, and Documentation (45 CFR § 164.316)

### Policies and Procedures

- [ ] Written policies and procedures
- [ ] Policies implement required standards
- [ ] Policies reviewed and updated as needed (at least annually)

### Documentation

- [ ] Policies and procedures documented
- [ ] Actions and activities documented
- [ ] Documentation retained for 6 years
- [ ] Documentation available to workforce
- [ ] Changes documented and dated

## Privacy Rule Integration

- [ ] Privacy Officer designated
- [ ] Privacy policies documented
- [ ] Notice of Privacy Practices (NPP) provided
- [ ] Patient rights processes (access, amendment, etc.)
- [ ] Minimum necessary standard applied
- [ ] Authorization for marketing/research
- [ ] Breach notification process (Privacy & Security Rules)

## Compliance Status

**HIPAA Security Readiness**: [Not Started / In Progress / Mostly Compliant / Fully Compliant]

**Safeguards Status**:
- Administrative: [X]% complete
- Physical: [X]% complete
- Technical: [X]% complete

**Critical Gaps**:
1. [Gap]
2. [Gap]
3. [Gap]

**Risk Level**: [High / Medium / Low]

**Next Steps**:
1. [Action with deadline]
2. [Action with deadline]
3. [Action with deadline]

**Next Review Date**: [Date]

---

**Legend**:
- (R) = Required implementation specification
- (A) = Addressable implementation specification (must implement OR document reason for not implementing and alternative)
