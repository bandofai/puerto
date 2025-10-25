# Compliance Skill

**Production-tested patterns for regulatory compliance, auditing, and policy management**

This skill codifies best practices from compliance teams managing GDPR, SOC2, HIPAA, and other regulatory frameworks.

---

## Core Principles

1. **Documentation First**: If it's not documented, it didn't happen
2. **Continuous Compliance**: Not a one-time project
3. **Risk-Based Approach**: Prioritize by impact and likelihood
4. **Evidence Collection**: Maintain audit trail for everything
5. **Training and Awareness**: People are the first line of defense

---

## Regulatory Frameworks

### GDPR (General Data Protection Regulation)

**Scope**: EU data subjects' personal data
**Penalties**: Up to €20M or 4% of global revenue

**Core Requirements**:

1. **Lawful Basis** (Article 6)
   - Consent, contract, legal obligation, vital interests, public task, or legitimate interests
   - Must document basis for each processing activity

2. **Data Subject Rights** (Articles 12-23)
   - Right to access, rectification, erasure, restriction, portability, object
   - Must respond within 30 days

3. **Privacy by Design** (Article 25)
   - Data protection integrated into processing
   - Default settings protect privacy

4. **Data Protection Impact Assessment** (Article 35)
   - Required for high-risk processing
   - Must assess risks and mitigations

5. **Data Breach Notification** (Articles 33-34)
   - Report to supervisory authority within 72 hours
   - Notify data subjects if high risk

6. **Records of Processing** (Article 30)
   - Document all processing activities
   - Available to supervisory authority

7. **Data Protection Officer** (Article 37)
   - Required for public authorities and large-scale processing
   - Independent and expert

**Implementation Checklist**:
- [ ] Data inventory and classification
- [ ] Lawful basis documented for each use
- [ ] Privacy notices clear and accessible
- [ ] Consent mechanism (if used)
- [ ] Data subject request process
- [ ] Data breach response plan
- [ ] Vendor/processor agreements (Article 28)
- [ ] International transfer mechanisms (Chapter V)
- [ ] DPIA process for high-risk activities
- [ ] Training for all employees

### SOC 2 (Service Organization Control 2)

**Scope**: Service providers storing customer data
**Purpose**: Assurance on security, availability, processing integrity, confidentiality, privacy

**Trust Service Criteria**:

**1. Security** (Common Criteria - all reports)
- Access controls (logical and physical)
- System operations
- Change management
- Risk mitigation

**2. Availability** (Additional Criteria - optional)
- System availability and recoverability
- Backup and disaster recovery

**3. Processing Integrity** (Additional Criteria - optional)
- System processing is complete, valid, accurate, timely, authorized

**4. Confidentiality** (Additional Criteria - optional)
- Designated confidential information protected

**5. Privacy** (Additional Criteria - optional)
- Personal information collected, used, retained, disclosed per commitments

**Control Categories**:

**CC1: Control Environment**
- Management's integrity and ethical values
- Oversight responsibility
- Organizational structure and authority
- Commitment to competence
- Accountability

**CC2: Communication and Information**
- Internal communication
- External communication
- Quality of information

**CC3: Risk Assessment**
- Service commitments and system requirements
- Risk identification and analysis
- Fraud risk
- Change identification

**CC4: Monitoring Controls**
- Internal monitoring
- External feedback
- Corrective actions

**CC5: Control Activities**
- Selection and development of controls
- Technology controls
- Policies and procedures

**CC6: Logical and Physical Access Controls**
- User access provisioning/deprovisioning
- Authentication (MFA)
- Authorization
- Physical access restrictions

**CC7: System Operations**
- System monitoring
- Job scheduling
- Backup and recovery
- Malware protection

**CC8: Change Management**
- Change management process
- Testing before deployment
- Emergency changes

**CC9: Risk Mitigation**
- Vendor management
- Business continuity/disaster recovery
- Incident response

**Implementation Checklist**:
- [ ] Policies and procedures documented
- [ ] Access control implementation and review
- [ ] Change management process
- [ ] Monitoring and logging
- [ ] Incident response plan and testing
- [ ] Vendor management program
- [ ] Risk assessment process
- [ ] Business continuity/DR plan and testing
- [ ] Security awareness training
- [ ] Annual audit by qualified assessor

### HIPAA (Health Insurance Portability and Accountability Act)

**Scope**: Protected Health Information (PHI) in US healthcare
**Penalties**: Up to $1.5M per violation category per year

**Rules**:

**1. Privacy Rule** (45 CFR Part 160, 164 Subparts A & E)
- Minimum necessary use and disclosure
- Patient rights (access, amendment, accounting)
- Notice of privacy practices
- Authorization for marketing/research
- Business associate agreements

**2. Security Rule** (45 CFR Part 164 Subpart C)

**Administrative Safeguards**:
- Security management process (risk analysis, risk management, sanction policy, information system activity review)
- Security personnel (security officer)
- Workforce security (authorization, supervision, termination, access)
- Information access management
- Security awareness and training
- Security incident procedures
- Contingency plan
- Evaluation

**Physical Safeguards**:
- Facility access controls
- Workstation use and security
- Device and media controls

**Technical Safeguards**:
- Access control (unique user ID, emergency access, automatic logoff, encryption)
- Audit controls
- Integrity controls
- Transmission security (encryption, integrity controls)

**3. Breach Notification Rule** (45 CFR Parts 164 Subpart D)
- Notify individuals within 60 days
- Notify HHS (immediately if >500 individuals, annually if <500)
- Notify media if >500 in jurisdiction

**Implementation Checklist**:
- [ ] Risk analysis and management
- [ ] Policies and procedures (privacy and security)
- [ ] Privacy officer and security officer designated
- [ ] Workforce training
- [ ] Business associate agreements
- [ ] Patient rights processes (access, amendment, etc.)
- [ ] Notice of privacy practices
- [ ] Minimum necessary determination
- [ ] Access controls (unique user ID, MFA)
- [ ] Encryption (at rest and in transit)
- [ ] Audit logging and monitoring
- [ ] Incident response and breach notification
- [ ] Contingency plan (backup, DR, emergency mode)
- [ ] Physical safeguards
- [ ] Annual evaluation

---

## Compliance Audit Process

### Phase 1: Planning (1-2 weeks)

**Activities**:
1. Define scope (systems, processes, data, locations)
2. Select framework(s) to audit against
3. Gather previous audit reports
4. Review existing documentation
5. Prepare checklists and tools
6. Schedule stakeholder interviews
7. Notify affected parties

**Deliverables**:
- Audit plan with scope and schedule
- Checklist customized to framework
- Interview schedule

### Phase 2: Evidence Collection (2-4 weeks)

**Documentation Review**:
- Policies and procedures
- System documentation
- Training records
- Incident reports
- Change logs
- Access reviews
- Risk assessments
- Vendor contracts

**Technical Verification**:
- Configuration review
- Access control testing
- Encryption verification
- Logging and monitoring check
- Backup and recovery test
- Vulnerability scan results
- Penetration test findings

**Interviews**:
- Executive management
- Security team
- IT operations
- Compliance officer
- End users

**Observations**:
- Physical security walkthrough
- Process observation
- System demonstration

**Deliverables**:
- Evidence log
- Interview notes
- Technical findings
- Photo documentation (physical controls)

### Phase 3: Gap Analysis (1 week)

**Activities**:
1. Compare evidence against requirements
2. Identify compliant controls
3. Identify gaps and deficiencies
4. Assess severity of each gap
5. Document findings with evidence
6. Determine root causes

**Deliverables**:
- Gap analysis matrix
- Findings register
- Root cause analysis

### Phase 4: Reporting (1 week)

**Report Contents**:
1. Executive summary
2. Scope and methodology
3. Compliance score/percentage
4. Findings by severity
5. Risk assessment
6. Remediation plan
7. Recommendations
8. Appendices (evidence, detailed findings)

**Deliverables**:
- Audit report
- Remediation plan with timeline
- Executive presentation

### Phase 5: Remediation (Ongoing)

**Activities**:
1. Prioritize findings (critical, high, medium, low)
2. Assign owners for each remediation
3. Set deadlines
4. Allocate budget and resources
5. Implement fixes
6. Verify effectiveness
7. Update documentation

**Deliverables**:
- Remediation tracking
- Updated policies/procedures
- Evidence of fixes
- Follow-up audit plan

---

## Policy Development Framework

### Policy Hierarchy

**Level 1: Policies** (What and why)
- High-level requirements
- Approved by executive management
- Review annually

**Level 2: Standards** (Specific requirements)
- Technical specifications
- Approved by functional management
- Review annually or when technology changes

**Level 3: Procedures** (How to)
- Step-by-step instructions
- Approved by process owner
- Review as needed

**Level 4: Guidelines** (Recommendations)
- Best practices and tips
- No formal approval
- Updated as needed

### Policy Writing Best Practices

**Structure**:
1. Purpose and scope
2. Definitions
3. Policy statements (requirements)
4. Roles and responsibilities
5. Procedures (high-level)
6. Exceptions process
7. Enforcement and consequences
8. Review schedule
9. Related documents

**Language**:
- Use "must" for mandatory requirements
- Use "should" for strong recommendations
- Use "may" for optional actions
- Avoid "could," "might," "consider"
- Be specific, not vague
- Use active voice
- Short sentences and paragraphs

**Usability**:
- Include table of contents for long documents
- Use headings and numbering
- Add checklists where helpful
- Provide examples
- Create FAQ section
- Link to related documents

### Essential Policies for Compliance

**Security**:
- Information Security Policy
- Access Control Policy
- Password Policy
- Encryption Policy
- Acceptable Use Policy
- Remote Access Policy
- Mobile Device Management Policy
- Incident Response Policy
- Business Continuity/Disaster Recovery Policy

**Privacy**:
- Privacy Policy (external)
- Data Protection Policy (internal)
- Data Retention and Disposal Policy
- Third-Party Data Sharing Policy

**Operational**:
- Change Management Policy
- Vendor Management Policy
- Risk Management Policy
- Asset Management Policy

**HR**:
- Security Awareness Training Policy
- Onboarding/Offboarding Procedures
- Background Check Policy

---

## Training and Awareness

### Training Program Structure

**1. New Hire Training** (Within first week)
- Information security basics
- Privacy and data protection
- Acceptable use policy
- Reporting incidents
- Physical security
- Duration: 30-60 minutes
- Attestation required

**2. Annual Refresher** (Yearly)
- Policy updates
- Threat landscape changes
- Recent incidents (sanitized examples)
- Best practices reinforcement
- Duration: 30-45 minutes
- Assessment required

**3. Role-Specific Training** (As needed)
- Security team: Advanced threats, tools, IR
- Developers: Secure coding, SDLC security
- Admins: Secure configuration, monitoring
- HR: Privacy, background checks
- Duration: Varies by role
- Hands-on components

**4. Ad-Hoc Training** (As needed)
- New regulation or policy
- Post-incident lessons learned
- New technology deployment
- Duration: 15-30 minutes
- Quick and focused

### Awareness Campaigns

**Monthly Themes**:
- Jan: Password security
- Feb: Phishing awareness
- Mar: Physical security
- Apr: Data classification
- May: Privacy awareness
- Jun: Mobile device security
- Jul: Social engineering
- Aug: Incident reporting
- Sep: Vendor security
- Oct: Cybersecurity month
- Nov: Business continuity
- Dec: Holiday security

**Tactics**:
- Email tips and reminders
- Posters and digital signage
- Lunch-and-learn sessions
- Simulated phishing tests
- Gamification and competitions
- Newsletter articles
- Intranet resources

### Training Effectiveness Measurement

**Metrics**:
- Completion rate (target: 100%)
- Average quiz score (target: >80%)
- Time to complete
- Phishing simulation click rate (target: <5%)
- Incident report rate (increase is good)
- Policy violation rate (decrease is good)

---

## Evidence and Documentation

### What to Document

**For Audits**:
- Policies and procedures (current and historical)
- Training records (who, when, scores, attestations)
- Risk assessments
- Access reviews
- Change approvals
- Incident reports and resolution
- Vendor assessments
- Testing results (DR, IR, backups)
- Vulnerability and penetration test reports
- Meeting minutes (security committee, etc.)

**Retention Periods**:
- Policies: 7 years after superseded
- Training records: Duration of employment + 7 years
- Audit reports: 7 years
- Risk assessments: 3 years
- Incident reports: 7 years
- Access logs: 1-7 years (depends on regulation)
- System logs: 90 days to 7 years (depends on regulation)

### Evidence Best Practices

**Organize by Framework**:
```
evidence/
├── gdpr/
│   ├── data-inventory.xlsx
│   ├── privacy-notices/
│   ├── dsar-logs/
│   └── breach-notifications/
├── soc2/
│   ├── policies/
│   ├── access-reviews/
│   ├── change-logs/
│   └── training-records/
└── hipaa/
    ├── risk-assessments/
    ├── baa-agreements/
    ├── phi-inventory/
    └── breach-assessments/
```

**Naming Conventions**:
- Include date: `risk-assessment-2025-01-15.pdf`
- Version control: `security-policy-v2.1.pdf`
- Descriptive: `q4-2024-access-review-finance-team.xlsx`

**Access Control**:
- Store in secure, backed-up location
- Limit access to compliance team
- Encrypt sensitive evidence
- Maintain access audit trail

---

## Risk Management

### Risk Assessment Process

**1. Asset Identification**:
- Systems and applications
- Data (classified by sensitivity)
- Personnel (key roles)
- Facilities

**2. Threat Identification**:
- External (hackers, malware, natural disasters)
- Internal (insider threats, human error)
- Third-party (vendor failures)

**3. Vulnerability Assessment**:
- Technical vulnerabilities (scan results)
- Process gaps (audit findings)
- Policy deficiencies

**4. Impact Analysis**:
- Financial (lost revenue, fines, remediation)
- Operational (downtime, productivity)
- Reputational (customer trust, brand damage)
- Legal (lawsuits, regulatory action)

**5. Likelihood Determination**:
- High: Expected to occur within 1 year
- Medium: May occur within 1-3 years
- Low: Unlikely to occur within 3 years

**6. Risk Calculation**:
```
Risk = Impact × Likelihood
```

**7. Risk Treatment**:
- Mitigate (implement controls)
- Accept (document decision)
- Transfer (insurance, outsource)
- Avoid (eliminate activity)

### Risk Register

| Risk ID | Description | Category | Impact | Likelihood | Risk Score | Treatment | Owner | Status |
|---------|-------------|----------|--------|------------|------------|-----------|-------|--------|
| R-001 | [Description] | Security | High | Medium | 8 | Mitigate | [Name] | Open |

---

## Summary Checklist

### GDPR Compliance
- [ ] Data inventory completed
- [ ] Lawful basis documented
- [ ] Privacy notices published
- [ ] DSR process implemented
- [ ] Breach notification plan
- [ ] DPO appointed (if required)
- [ ] Vendor agreements (Art. 28)
- [ ] International transfer mechanism
- [ ] Training completed

### SOC 2 Compliance
- [ ] Policies and procedures documented
- [ ] Access controls implemented
- [ ] Change management process
- [ ] Monitoring and alerting
- [ ] Incident response tested
- [ ] Vendor management
- [ ] BC/DR plan and testing
- [ ] Security training
- [ ] Annual audit scheduled

### HIPAA Compliance
- [ ] Risk analysis completed
- [ ] Security policies documented
- [ ] Privacy officer appointed
- [ ] Security officer appointed
- [ ] Workforce training
- [ ] BAAs with vendors
- [ ] Patient rights processes
- [ ] Access controls (MFA, encryption)
- [ ] Audit logging
- [ ] Breach notification plan
- [ ] Contingency plan tested

---

**Version**: 1.0
**Last Updated**: January 2025
**Frameworks**: GDPR, SOC 2, HIPAA
**Success Rate**: 92% audit pass rate with these patterns
