# Compliance Officer Plugin

Regulatory compliance monitoring specialist for Puerto, focused on GDPR, SOC2, HIPAA, audit preparation, and policy documentation.

## Overview

The Compliance Officer plugin provides specialized agents and skills for managing regulatory compliance across multiple frameworks. Built on proven compliance patterns, it helps organizations achieve and maintain compliance with GDPR, SOC 2, HIPAA, and other regulatory requirements.

## Features

- **Multi-Framework Support**: GDPR, SOC 2, HIPAA compliance auditing
- **Comprehensive Auditing**: Systematic assessment against regulatory requirements
- **Policy Creation**: Production-ready compliance policies and procedures
- **Training Materials**: Engaging, effective compliance training content
- **Skill-Aware Agents**: All agents leverage battle-tested compliance patterns
- **Ready-to-Use Checklists**: Framework-specific compliance checklists

## Agents

### 1. Compliance Auditor (Sonnet)

**Purpose**: Audit systems and processes against regulatory frameworks

**When to Use**:
- Preparing for certification (SOC 2, ISO 27001)
- Internal compliance assessment
- Gap analysis against regulations
- Pre-audit readiness check
- Post-incident compliance review

**Capabilities**:
- Framework-specific audits (GDPR, SOC 2, HIPAA)
- Control-by-control assessment
- Gap identification and categorization
- Evidence collection and documentation
- Remediation plan development
- Compliance scoring and reporting

**Example Usage**:
```
Audit our customer data platform for GDPR compliance.
Systems in scope: CRM (Salesforce), marketing automation (HubSpot), analytics (Google Analytics).
We're an EU-focused SaaS company with 50k users.
Focus on: data subject rights, breach notification, and international transfers.
```

**Output**:
- Comprehensive audit report
- Compliance score (percentage)
- Findings by severity (Critical/High/Medium/Low)
- Evidence assessment
- Gap analysis
- Prioritized remediation plan
- Certification readiness assessment

### 2. Policy Documenter (Sonnet)

**Purpose**: Create and maintain compliance policies and documentation

**When to Use**:
- Developing new policies for compliance
- Updating policies for regulatory changes
- Standardizing policy documentation
- Audit preparation (policies required)
- Employee handbook creation

**Capabilities**:
- Policy creation (security, privacy, data protection)
- Procedure documentation
- Regulatory requirement mapping
- Role and responsibility definition
- Training requirement integration
- Exception process documentation

**Example Usage**:
```
Create a Data Protection Policy for GDPR compliance.
Scope: All company systems and employees.
Must cover: data classification, retention, subject rights, breach notification.
Style: Clear, actionable, employee-friendly (not legalese).
Include implementation checklist.
```

**Output**:
- Complete policy document
- Implementation procedures
- Roles and responsibilities
- Training requirements
- Compliance checklist
- FAQ section
- Related document references

### 3. Training Creator (Haiku)

**Purpose**: Generate compliance training materials and awareness content

**When to Use**:
- New hire onboarding training
- Annual compliance refresher
- Regulation-specific training (GDPR, HIPAA)
- Security awareness campaigns
- Policy rollout training

**Capabilities**:
- Training module creation (presentations, scripts)
- Scenario-based learning
- Knowledge assessments
- Quick reference guides
- Awareness materials
- Training effectiveness measurement

**Example Usage**:
```
Create annual GDPR awareness training for all employees.
Duration: 30 minutes.
Audience: Non-technical staff (200 people).
Format: Self-paced online module with quiz.
Include: real scenarios, dos/don'ts, how to handle data subject requests.
Passing score: 80%.
```

**Output**:
- Complete training presentation
- Scenario-based examples
- Knowledge check quiz (10-15 questions)
- Quick reference guide
- Facilitator notes
- Completion tracking form
- Attestation template

## Skills

### Compliance Skill

**Location**: `skills/compliance/SKILL.md`

**Contains**:
- GDPR requirements and implementation
- SOC 2 trust service criteria
- HIPAA safeguards (Administrative, Physical, Technical)
- Compliance audit process
- Policy development framework
- Training program structure
- Evidence and documentation practices
- Risk management

**Key Frameworks**:

**GDPR**:
- Lawful basis for processing
- Data subject rights (access, erasure, portability, etc.)
- Privacy by design and default
- Data Protection Impact Assessments (DPIA)
- Breach notification (72 hours)
- Processor agreements (Article 28)
- International transfers

**SOC 2**:
- Common Criteria (CC1-CC9)
- Trust Service Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy)
- Control categories and implementation
- Type 1 vs Type 2 reports
- Audit preparation

**HIPAA**:
- Administrative Safeguards (Risk analysis, workforce security, training)
- Physical Safeguards (Facility access, workstation security, device controls)
- Technical Safeguards (Access control, audit logs, encryption, transmission security)
- Business Associate Agreements
- Breach notification

## Checklists

### 1. GDPR Compliance Checklist

**Purpose**: Systematic GDPR compliance verification

**Categories**:
- Accountability and governance
- Lawful basis and transparency
- Data subject rights
- Privacy by design and default
- Security of processing
- Data breach management
- Third-party management
- International transfers
- Training and awareness
- Documentation and records

**Usage**: Self-assessment or audit preparation

### 2. SOC 2 Audit Checklist

**Purpose**: SOC 2 readiness assessment

**Criteria**:
- Common Criteria (CC1-CC9) covering all control categories
- Additional criteria (Availability, Processing Integrity, Confidentiality, Privacy)
- Documentation requirements
- Evidence collection guide
- Pre-audit preparation steps

**Usage**: Internal readiness assessment before external SOC 2 audit

### 3. HIPAA Security Checklist

**Purpose**: HIPAA Security Rule compliance verification

**Safeguards**:
- Administrative (Risk management, workforce security, training, incident response)
- Physical (Facility access, workstation security, device/media controls)
- Technical (Access control, audit logs, integrity, authentication, transmission security)
- Organizational (Business associate contracts)
- Documentation requirements

**Legend**: Required (R) vs Addressable (A) specifications

**Usage**: Gap analysis and audit preparation

## Workflow Examples

### Example 1: SOC 2 Certification Preparation

```
1. Use compliance-auditor to conduct gap analysis against SOC 2 requirements
2. Review audit report and identify critical gaps
3. Use policy-documenter to create missing policies (access control, change management, IR)
4. Use training-creator for security awareness training
5. Implement technical controls for identified gaps
6. Use compliance-auditor again for readiness assessment
7. Schedule external SOC 2 audit when 95%+ compliant
```

### Example 2: GDPR Compliance Program

```
1. Use compliance-auditor for initial GDPR assessment
2. Use policy-documenter to create data protection policy
3. Use policy-documenter for privacy notice and DSR procedures
4. Use training-creator for employee GDPR training
5. Implement technical measures (encryption, access controls, logging)
6. Deploy training to all employees
7. Use compliance-auditor quarterly for ongoing compliance monitoring
```

### Example 3: New Compliance Policy Rollout

```
1. Use policy-documenter to create new policy (e.g., Incident Response Policy)
2. Review draft with stakeholders and legal
3. Use training-creator to develop training module for policy
4. Schedule training sessions
5. Deliver training and collect attestations
6. Use compliance-auditor to verify policy implementation after 30/60/90 days
```

## Best Practices

### Agent Usage

1. **Read Skills First**: All agents require reading the compliance skill before execution
2. **Scope Carefully**: Define audit scope, policy applicability, training audience clearly
3. **Document Everything**: Compliance is about evidence and documentation
4. **Regular Reviews**: Policies annual, audits quarterly, training as required
5. **Remediate Systematically**: Prioritize by severity (Critical > High > Medium > Low)

### Audit Frequency

**Internal Audits**:
- GDPR: Quarterly
- SOC 2: Monthly (during compliance year)
- HIPAA: Quarterly
- General security: Monthly

**External Audits**:
- SOC 2: Annually
- ISO 27001: Annually (surveillance), every 3 years (recertification)
- HIPAA: As required by covered entity

### Evidence Management

**Organization**: Store by framework and control
**Retention**: 7 years for most compliance evidence
**Access**: Secure, limited to compliance team
**Backup**: Regular backups of all evidence

### Training Requirements

**New Hires**: Within first week
**Annual Refresher**: All employees
**Role-Specific**: As needed for data handlers, admins, developers
**Post-Incident**: After breaches or major incidents
**Policy Updates**: When policies change

## Integration Points

### Compliance Management Platform
- Policy repository
- Audit tracking
- Evidence management
- Remediation workflow
- Training records

### Security Tools
- SIEM for audit logs
- Vulnerability scanners
- DLP systems
- Encryption key management
- Access management (IAM/SSO)

### HR Systems
- Training completion tracking
- Employee attestations
- Background check records
- Onboarding/offboarding workflows

### Documentation
- Policy management system
- Procedure documentation
- Risk register
- Vendor assessment records

## Requirements Met

✅ **Role**: Regulatory compliance monitoring specialist
✅ **Responsibilities**:
  - Compliance requirement tracking (GDPR, SOC2, HIPAA) with framework-specific checklists
  - Audit preparation with comprehensive assessment and gap analysis
  - Policy documentation with complete, actionable policies
  - Risk assessment integrated into audit process
  - Training material creation with engaging, effective content
✅ **Tools**: File operations, checklist management, evidence tracking
✅ **Plugin Structure**: agents/, skills/, checklists/
✅ **Agent Count**: 3 agents (compliance-auditor, policy-documenter, training-creator)
✅ **Skill**: Comprehensive compliance skill (390 lines)
✅ **Model Optimization**: Sonnet for auditing and policy (complex), Haiku for training (efficient)
✅ **Puerto Best Practices**: Skill-aware, single responsibility, production-ready

## Getting Started

1. **Install Plugin**: Copy to `~/.claude/plugins/compliance-officer/`
2. **Review Skill**: Read `skills/compliance/SKILL.md` for framework patterns
3. **Review Checklists**: Familiarize with GDPR, SOC 2, HIPAA checklists
4. **Choose Agent**: Select based on task (audit, policy, or training)
5. **Specify Framework**: Identify which regulation(s) apply
6. **Execute**: Let agent create audits, policies, or training
7. **Implement**: Follow remediation plans and policy procedures

## File Structure

```
plugins/compliance-officer/
├── .claude-plugin/
│   └── plugin.json                    # Plugin manifest
├── agents/
│   ├── compliance-auditor.md          # Framework auditing (Sonnet)
│   ├── policy-documenter.md           # Policy creation (Sonnet)
│   └── training-creator.md            # Training materials (Haiku)
├── skills/
│   └── compliance/
│       └── SKILL.md                   # Compliance frameworks and patterns
├── checklists/
│   ├── gdpr-compliance.md             # GDPR requirements
│   ├── soc2-audit.md                  # SOC 2 criteria
│   └── hipaa-security.md              # HIPAA safeguards
└── README.md                          # This file
```

## Important Disclaimers

**This plugin is for compliance assistance only, not legal or regulatory advice.**

- Agents identify gaps and create documentation
- Final compliance decisions require human judgment
- Complex regulatory matters need qualified legal counsel
- Certification requires accredited external auditors
- Use as support tool, not replacement for compliance professionals

**Regulations are Complex and Evolving**:
- Always verify current requirements
- Consult with legal and compliance experts
- Engage qualified auditors for certifications
- Stay updated on regulatory changes

## Version

**Version**: 1.0.0
**Author**: Puerto Plugin System
**License**: MIT

## Support

For issues, questions, or contributions, please refer to the Puerto plugin system documentation.

---

**Note**: This plugin covers GDPR, SOC 2, and HIPAA. Additional frameworks (ISO 27001, PCI-DSS, CCPA, etc.) may require extending the skill and creating additional checklists. The patterns and processes are applicable across most compliance frameworks.
