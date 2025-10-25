# Skill: Access Management

Security-first access provisioning, lifecycle management, and compliance frameworks.

## Access Management Principles

### Least Privilege
- Grant minimum necessary access to perform job functions
- No "just in case" permissions
- Regular access reviews to prevent privilege creep
- Time-limited elevated access when possible

### Segregation of Duties
- No single person controls entire critical process
- Separate roles: requester, approver, provisioner, auditor
- Prevent conflicts: developers shouldn't have production DB admin
- SOX compliance requires documented separation

### Need-to-Know
- Access based on job requirements, not curiosity
- Data classification drives access decisions
- Document business justification for all access
- Regular validation that access is still required

## User Lifecycle Management

### Onboarding (New User)

#### Pre-Arrival Checklist
- [ ] Manager approves hire in HR system
- [ ] Department and role identified
- [ ] Start date confirmed
- [ ] Equipment ordered (laptop, monitors, etc.)
- [ ] Workspace prepared
- [ ] Accounts to be created identified

#### Day 1 Account Creation
**Standard Access for All Employees**:
- Email account (user@company.com)
- Network login (Active Directory/LDAP)
- File share access (department folder)
- Collaboration tools (Slack, Teams)
- HR system (view personal info, benefits)
- Time tracking system

**Role-Based Additional Access**:
| Role | Additional Systems |
|------|-------------------|
| Developer | GitHub, CI/CD, dev environments, code review tools |
| Sales | CRM, sales portal, demo environments |
| Support | Ticketing system, knowledge base, chat tools |
| Finance | Accounting system, payment processor, expense tool |
| HR | Full HR system, recruiting tools, background check |

#### Provisioning Process
1. Receive approved access request from HR or manager
2. Create user accounts in all required systems
3. Assign to appropriate groups based on department and role
4. Set initial password (must be changed on first login)
5. Configure MFA enrollment (required on first login)
6. Grant file share permissions
7. Add to distribution lists and groups
8. Send welcome email with credentials and setup instructions
9. Document all access granted in audit log
10. Schedule 30-day access review with manager

**Timeline**: Complete within 2 hours of start time on day 1

### Modification (Role Change, Transfer)

#### Triggers
- Promotion or role change
- Department transfer
- Project assignment requiring additional access
- Temporary duty assignment

#### Process
1. Receive approved change request from manager
2. Review current access permissions
3. Determine delta (add/remove permissions)
4. Remove old role-specific access
5. Add new role-specific access
6. Verify no conflicting permissions (SOX)
7. Update user attributes (department, title, manager)
8. Notify user and new manager of changes
9. Document all changes in audit log

**Important**: Don't just add permissions - remove old ones!

### Offboarding (Termination, Resignation)

#### Immediate Actions (Within 1 Hour of Notification)
1. Disable Active Directory/LDAP account (prevents login)
2. Disable email account (optional: forward to manager for 30 days)
3. Revoke VPN access
4. Disable remote access (RDP, SSH keys)
5. Reset passwords for shared accounts if user had access
6. Disable MFA tokens

#### Within 24 Hours
1. Remove from all systems (delete accounts)
2. Remove from all groups and distribution lists
3. Revoke cloud access (AWS, Azure, GCP)
4. Revoke application access
5. Return or wipe company devices
6. Transfer document ownership to manager
7. Remove from physical access (badge deactivation)

#### Within 1 Week
1. Archive user data per retention policy
2. Final access review and verification
3. Generate offboarding report for HR
4. Close offboarding ticket

**Exit Interview Access Questions**:
- Did you have access to any shared accounts? (passwords must be changed)
- Did you set up any personal accounts for work? (must be transferred)
- Do you have any work data on personal devices? (must be deleted)

## RBAC (Role-Based Access Control)

### Role Definitions

#### Standard User
- **Purpose**: General employee access
- **Access**: Email, file shares, collaboration tools, HR portal
- **Restrictions**: No admin rights, no sensitive data access

#### Power User
- **Purpose**: Advanced users needing local admin
- **Access**: Standard + local administrator rights
- **Restrictions**: No server access, no production access
- **Approval**: Manager + IT Director

#### Developer
- **Purpose**: Software development
- **Access**: Standard + code repos, dev environments, CI/CD, test databases
- **Restrictions**: No production access without approval
- **Approval**: Manager

#### Database Admin
- **Purpose**: Database administration
- **Access**: Standard + all database systems, backup tools
- **Restrictions**: Separate dev/prod roles (SOX), all actions logged
- **Approval**: Manager + IT Director + DBA Lead

#### System Admin
- **Purpose**: Server and infrastructure administration
- **Access**: Standard + server admin, network devices, virtualization
- **Restrictions**: Separate dev/prod roles, privileged access logged
- **Approval**: Manager + IT Director

#### Security Admin
- **Purpose**: Security tools and incident response
- **Access**: Standard + firewall, SIEM, antivirus, IDS/IPS
- **Restrictions**: Read-only to production systems, cannot approve own changes
- **Approval**: Manager + CISO

#### Executive
- **Purpose**: Senior leadership
- **Access**: Standard + executive systems, confidential data, strategic tools
- **Restrictions**: May have enhanced monitoring for compliance
- **Approval**: HR Director or above

### Permission Levels

#### Read
- View files, records, data
- No modification capability
- Suitable for: Reports, dashboards, reference data

#### Write
- Create new content
- Modify own content
- Delete own content
- Suitable for: Document creation, data entry

#### Contribute
- Create and modify any content
- Cannot delete others' content
- Suitable for: Collaborative workspaces

#### Admin
- Full control including user management
- Add/remove users from resource
- Change permissions
- Suitable for: Resource owners, team leads

#### Owner
- All admin rights plus:
- Transfer ownership
- Delete resource entirely
- Suitable for: Ultimate responsibility holder

## Access Request Validation

### Validation Checklist
- [ ] Request submitted by authorized person (manager, HR)
- [ ] User details complete (name, email, department, role, start date)
- [ ] Business justification provided
- [ ] Required approvals obtained
- [ ] Access level appropriate for role (least privilege)
- [ ] No policy violations (segregation of duties, conflicts)
- [ ] Temporary access has expiration date
- [ ] Compliance requirements met (SOX, HIPAA, PCI, GDPR)

### Approval Requirements

| Access Type | Required Approvers |
|-------------|-------------------|
| Standard user | Manager |
| Elevated access | Manager + IT Manager |
| Admin access | Manager + IT Director |
| Production DB | Manager + IT Director + DBA Lead |
| Financial systems (SOX) | Manager + IT Director + Finance Director |
| PHI/PII (HIPAA/GDPR) | Manager + Privacy Officer |
| Emergency access | On-call manager + post-review within 24h |

### Red Flags (Require Additional Scrutiny)
- Rushed request without proper justification
- Access beyond role requirements
- Conflicting roles (developer + production admin)
- Access to competitor-sensitive data before non-compete expires
- Contractor requesting permanent access
- Access request for terminated employee
- Bulk access requests without details

## Password Management

### Password Policies

#### Complexity Requirements
- Minimum 12 characters (14+ for privileged accounts)
- Mix of uppercase, lowercase, numbers, symbols
- No dictionary words
- No personal info (name, birthdate)
- No common patterns (Password123, Qwerty123)

#### Expiration and History
- Standard accounts: 90-day expiration
- Privileged accounts: 60-day expiration
- Cannot reuse last 12 passwords
- Cannot change password more than once per day (prevent cycling)

#### Password Reset Process
1. Verify user identity through secondary channel
   - Call user at phone number on file
   - Verify employee ID or ask security questions
   - Confirm manager name and department
2. Generate secure temporary password
   - Use password generator (12+ characters)
   - Or use pattern: `TempPass$(Get-Random)!`
3. Deliver password securely
   - Read over phone (not SMS, not email)
   - Use encrypted messaging if available
   - Never write down or email passwords
4. Set password to expire on first login
5. Log password reset event for security audit
6. Alert security team if suspicious timing or location

### Multi-Factor Authentication (MFA)

#### MFA Requirements
**Required for**:
- All remote access (VPN, RDP, SSH)
- Admin accounts (system, database, security)
- Access to sensitive data (financial, PHI, PII)
- Cloud services (AWS, Azure, GCP, Office 365)
- Privileged access management (PAM) systems

**Optional but recommended for**:
- Standard user accounts
- Email access
- Internal applications

#### MFA Methods (Strongest to Weakest)
1. **Hardware token** (YubiKey, RSA SecurID) - Most secure
2. **Authenticator app** (Google Authenticator, Microsoft Authenticator)
3. **Push notification** (Duo, Okta Verify)
4. **SMS code** - Least secure, avoid if possible due to SIM swapping risk

#### MFA Enrollment Process
1. User logs in with username/password
2. System prompts for MFA enrollment
3. User scans QR code with authenticator app
4. User enters test code to verify setup
5. Backup codes generated and saved by user
6. MFA now required for all future logins

### Privileged Access Management (PAM)

#### Just-in-Time (JIT) Access
- Temporary elevated privileges granted on-demand
- Approval workflow before granting
- Automatic expiration (1-8 hours typical)
- All actions logged and recorded
- Used for: Production access, admin tasks, emergency fixes

#### Break-Glass Accounts
- Emergency admin accounts for disaster recovery
- Stored in secure vault (physical safe or password manager)
- Only used when primary authentication systems are down
- Requires immediate notification to security team
- Password changed immediately after use
- All actions audited post-event

#### Privileged Session Recording
- All privileged sessions recorded (video + commands)
- Recordings stored for compliance (typically 1-7 years)
- Regular review of high-risk actions
- Alerts on suspicious activity (off-hours access, unusual commands)

## Access Review and Certification

### Quarterly Access Review

#### Process
1. Generate report of all user access by department
2. Send to department managers for review
3. Manager validates:
   - Is user still employed?
   - Is access still required for job function?
   - Is access level appropriate (no excessive permissions)?
4. Manager approves or requests removals
5. IT processes approved removals within 5 business days
6. Document review completion for compliance

#### Automated Checks
- **Stale accounts**: No login in 90+ days
- **Orphaned accounts**: User's manager left company
- **Excessive permissions**: User in more groups than peers
- **Conflicting roles**: Segregation of duties violations

### Annual Privileged Access Certification

#### Scope
- All accounts with admin privileges
- All accounts with access to sensitive data
- All service accounts
- All shared accounts

#### Review Questions
- Is privileged access still required?
- Is it used regularly (not dormant)?
- Are approvals up to date?
- Is MFA configured and working?
- Are all activities logged?
- Has there been any misuse?

### Continuous Monitoring

#### Real-Time Alerts
- Failed login attempts (5+ in 15 minutes)
- Login from unusual location
- Off-hours access to sensitive data
- Privilege escalation
- Account sharing detected (simultaneous logins from different IPs)
- Access to competitor data before non-compete expires

#### Weekly Reports
- New accounts created
- Accounts deleted
- Permission changes
- Password resets
- Failed access attempts
- Policy violations

## Compliance Requirements

### SOX (Sarbanes-Oxley)

#### Key Requirements
- Segregation of duties (developer ≠ production admin)
- All access changes logged and auditable
- Quarterly access reviews
- Password policies enforced
- Terminated users removed within 24 hours

#### Common Violations
- Single person has conflicting roles
- Shared accounts without accountability
- Access granted without approval
- No audit trail of access changes

### HIPAA (Protected Health Information)

#### Key Requirements
- Minimum necessary access (only PHI needed for job)
- Access logged and auditable
- MFA for remote access to PHI
- Terminated employees removed immediately
- Business Associate Agreements (BAA) for vendors
- Encryption of PHI at rest and in transit

#### PHI Access Roles
- **Direct Treatment**: Doctors, nurses (full PHI access)
- **Billing**: Billing staff (diagnosis, insurance info only)
- **IT Admin**: DBAs, sysadmins (minimal PHI exposure, all access logged)
- **Research**: De-identified data only (no names, dates, identifiers)

### PCI-DSS (Payment Card Industry)

#### Key Requirements
- No storage of full card numbers (PAN) except in secure vault
- No storage of CVV/CVV2 codes
- Encryption of cardholder data
- Quarterly access reviews for cardholder data environment (CDE)
- MFA for all access to CDE
- Unique credentials per person (no shared accounts)

#### Access Tiers
- **No access**: Default for all employees
- **CDE access**: Only for those with business need
- **Full card data**: Extremely limited (PCI administrator, key custodian)

### GDPR (Personal Data Protection)

#### Key Requirements
- Lawful basis for processing personal data
- Data subject access rights (view, correct, delete)
- Breach notification within 72 hours
- Data Protection Impact Assessment (DPIA) for high-risk processing
- Privacy by design and by default
- Documentation of all data processing activities

#### Data Subject Rights
- **Right to access**: User can request all data held about them
- **Right to rectification**: User can correct inaccurate data
- **Right to erasure**: User can request deletion ("right to be forgotten")
- **Right to portability**: User can receive data in machine-readable format
- **Right to object**: User can object to certain processing

## Audit Logging

### What to Log
- **Who**: Username and employee ID
- **What**: Action performed (create, read, update, delete, grant, revoke)
- **When**: Timestamp (UTC preferred)
- **Where**: System or resource affected
- **How**: Method (manual, automated, API, GUI)
- **Why**: Business justification or ticket number
- **Result**: Success or failure
- **Changes**: Before and after values for modifications

### Log Retention
- **Access logs**: 1 year minimum
- **Privileged access logs**: 7 years (SOX requirement)
- **PHI access logs**: 6 years (HIPAA requirement)
- **Financial system logs**: 7 years (SOX requirement)
- **Security incident logs**: Indefinite

### Audit Reports
- **Daily**: Failed login attempts, after-hours access
- **Weekly**: New accounts, deleted accounts, permission changes
- **Monthly**: Access reviews, policy violations
- **Quarterly**: Comprehensive access report for compliance
- **Annual**: Full audit for external auditors

## Emergency Access Procedures

### Emergency Access Request

#### Criteria for Emergency Access
- Production outage affecting business operations
- Security incident requiring immediate response
- Data loss requiring urgent recovery
- Time-sensitive business need (can't wait for normal approval)

#### Process
1. Requester submits emergency access request
   - Describe emergency situation
   - Specify required access
   - Specify duration needed
   - Provide on-call manager approval
2. IT grants temporary access immediately
3. Set automatic expiration (1-8 hours)
4. Enable enhanced logging/monitoring
5. Notify security team
6. Document in ticket with justification
7. Post-review within 24 hours:
   - Was emergency legitimate?
   - Was access used appropriately?
   - Document lessons learned

#### Emergency Access Audit
- Review all actions taken during emergency access
- Verify appropriate use
- Check for policy violations
- Document for compliance
- Follow up on any concerns

## Common Access Scenarios

### Scenario: Contractor Onboarding
- Time-limited access (contract end date)
- Restricted access (no internal systems)
- Separate email domain (contractor@external.com)
- Enhanced monitoring
- No admin privileges without exceptional approval
- Access review every 30 days
- Automatic expiration on contract end date
- Immediate offboarding on contract end

### Scenario: Shared Account Management
- Avoid shared accounts when possible (use service principals)
- If required:
  - Document all users with access
  - Change password quarterly or when user leaves
  - All activity logged and monitored
  - No shared accounts for admin access (use PAM instead)

### Scenario: API Keys and Service Accounts
- Generate unique API key per application/service
- No personal accounts for automated processes
- Rotate keys every 90 days
- Store in secure vault (AWS Secrets Manager, Azure Key Vault)
- Least privilege access
- Monitor for unusual activity
- Immediate revocation if compromised
