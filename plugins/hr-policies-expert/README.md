# HR Policies Expert Plugin

**Expert guidance on HR policies, employment law, benefits, and compliance**

This plugin provides comprehensive HR policy expertise with a knowledge base covering employment law, company policies, benefits administration, and regulatory compliance. Get clear, compliant answers to policy questions with proper legal citations.

## Overview

The HR Policies Expert plugin serves as your organization's policy and compliance knowledge resource. Built on employment law fundamentals and HR best practices, it provides accurate guidance on policies, benefits, leave management, and compliance requirements.

**Important**: This plugin provides general guidance and should not be considered legal advice. Always consult qualified legal counsel for specific legal matters.

## Components

### Agent: `hr-policies-expert`

An HR policies and compliance expert that answers questions, reviews documents, and provides guidance on employment matters.

- **File**: `agents/hr-policies-expert.md`
- **Model**: Sonnet (requires domain expertise for policy/compliance)
- **Tools**: Read, Grep, Glob (read-only for security)
- **Pattern**: Read-Only Analyst
- **Skill-aware**: Always reads HR policies skill before responding

### Skill: HR Policies & Compliance

Comprehensive knowledge base covering HR policies, employment law, and compliance.

- **File**: `skills/hr-policies/SKILL.md`
- **Contains**:
  - Common HR policies (EEO, harassment, attendance, conduct, etc.)
  - Labor law fundamentals (FLSA, Title VII, ADA, ADEA, FMLA, COBRA, etc.)
  - Leave policies (PTO, sick leave, FMLA, parental leave, bereavement, etc.)
  - Benefits administration (health insurance, 401k, FSA, etc.)
  - Compliance requirements and checklists
  - Policy documentation standards
  - Question response frameworks
  - Leave management guidelines

## Features

### Core Capabilities

1. **Answer Policy Questions**
   - Company policy interpretation
   - Benefits eligibility and enrollment
   - Leave types and usage
   - Workplace policy guidance
   - Structured responses with citations

2. **Compliance Review**
   - Policy document review
   - Offer letter analysis
   - Job description compliance
   - Handbook review
   - Risk identification and mitigation

3. **Benefits Information**
   - Health insurance options
   - Retirement plan details
   - Enrollment periods and qualifying events
   - COBRA continuation
   - Other benefits (life, disability, FSA, etc.)

4. **Leave Management Guidance**
   - FMLA eligibility and process
   - PTO accrual and usage
   - Sick leave policies
   - Parental leave
   - Leave coordination
   - Intermittent leave tracking

5. **Employment Law Guidance**
   - FLSA (overtime, exemptions)
   - Title VII (discrimination)
   - ADA (disability accommodation)
   - ADEA (age discrimination)
   - FMLA (family/medical leave)
   - State and local law considerations

### Policy Coverage

**Leave Policies**:
- Paid Time Off (PTO)
- Sick Leave
- FMLA (Family and Medical Leave)
- Parental Leave
- Bereavement Leave
- Jury Duty and Voting Leave

**Workplace Policies**:
- Equal Employment Opportunity (EEO)
- Anti-Harassment and Anti-Discrimination
- Attendance and Punctuality
- Code of Conduct
- Drug and Alcohol Policy
- Social Media and Electronic Communications
- Discipline and Termination

**Benefits**:
- Health Insurance (medical, dental, vision)
- Retirement Plans (401k)
- Life and Disability Insurance
- Flexible Spending Accounts (FSA)
- Employee Assistance Program (EAP)
- Tuition Reimbursement

**Labor Laws**:
- Fair Labor Standards Act (FLSA)
- Title VII (Civil Rights Act)
- Americans with Disabilities Act (ADA)
- Age Discrimination in Employment Act (ADEA)
- Family and Medical Leave Act (FMLA)
- COBRA
- OSHA
- National Labor Relations Act (NLRA)

## Installation

### Option 1: Manual Installation (Project-Level)

```bash
# From your project root
cp -r plugins/hr-policies-expert .claude/plugins/

# Verify installation
ls .claude/plugins/hr-policies-expert/
```

### Option 2: User-Level Installation

```bash
# Install for all your projects
cp -r plugins/hr-policies-expert ~/.claude/plugins/

# Verify installation
ls ~/.claude/plugins/hr-policies-expert/
```

### Verify Installation

The agent will be automatically available in Claude Code. Verify by checking:

```bash
# List installed agents
ls .claude/plugins/hr-policies-expert/agents/
# Should show: hr-policies-expert.md

# List installed skills
ls .claude/plugins/hr-policies-expert/skills/
# Should show: hr-policies/
```

## Usage

### Automatic Activation

The agent activates automatically when you:
- Ask HR policy questions
- Request compliance review
- Need benefits information
- Ask about leave management
- Inquire about employment law

### Manual Invocation

You can explicitly invoke the agent:

```
@hr-policies-expert [your question or request]
```

### Example Requests

#### Policy Questions

**PTO/Vacation**:
```
"How much PTO do employees get?"
"Can I roll over unused vacation to next year?"
"Do we pay out PTO when someone leaves?"
```

**Leave Questions**:
```
"How do I request FMLA leave?"
"Am I eligible for parental leave?"
"What's the difference between sick leave and PTO?"
```

**Benefits Questions**:
```
"When can I enroll in health insurance?"
"How much does the company match for 401k?"
"What happens to my benefits if I go on leave?"
```

**Workplace Policy**:
```
"What's the remote work policy?"
"Is there a dress code?"
"How should I report harassment?"
```

#### Compliance Review

**Policy Review**:
```
"Review this anti-harassment policy for compliance"
"Can you check if our PTO policy meets state requirements?"
"Review our employee handbook for legal issues"
```

**Document Review**:
```
"Review this offer letter for compliance"
"Check this job description for ADA compliance"
"Analyze this separation agreement"
```

#### Employment Law

**Legal Questions**:
```
"What are the FLSA overtime requirements?"
"Explain ADA reasonable accommodation"
"What qualifies as FMLA-eligible leave?"
"Are we required to provide sick leave?"
```

#### Leave Management

**Leave Guidance**:
```
"How do I coordinate FMLA with short-term disability?"
"Can an employee take intermittent FMLA leave?"
"What's the process for requesting parental leave?"
```

## Best Practices

### For HR Teams

1. **Use as First Resource**
   - Check policy guidance before escalating
   - Review compliance checklists for documents
   - Reference for consistent answers

2. **Customize for Your Organization**
   - Add company-specific policies to project files
   - Update skill with your policy language
   - Include your specific processes and contacts

3. **Escalate Appropriately**
   - Complex legal questions → Legal counsel
   - Employment decisions → HR leadership
   - Discrimination/harassment → Immediate HR involvement

4. **Maintain Accuracy**
   - Review and update policies annually
   - Monitor law changes affecting policies
   - Seek legal review of significant changes

### For Managers

1. **Policy Clarification**
   - Use for quick policy references
   - Understand before communicating to team
   - Consistent application across team

2. **Don't**
   - Make policy exceptions without HR
   - Provide legal advice to employees
   - Promise anything outside written policy

3. **Escalate to HR**
   - Accommodation requests
   - Harassment complaints
   - Performance/discipline issues
   - Leave requests

### For Employees

1. **Self-Service**
   - Get quick answers to common questions
   - Understand your benefits and leave options
   - Know your rights and responsibilities

2. **Follow Up with HR**
   - For personal situation specifics
   - To request leave or accommodations
   - For benefits enrollment assistance
   - To report concerns

## Response Format

The agent provides structured, clear responses:

### Policy Question Response

```
### [Topic]

**Answer**: [Direct answer to question]

**Policy/Law Reference**: [Citation with section]

**Explanation**: [Context and reasoning]

**Example**: [Concrete example if helpful]

**Next Steps**:
- [Action 1]
- [Action 2]

**Questions?** [Contact information]

---

**Disclaimer**: This is general guidance. For specific situations, consult HR or legal counsel.
```

### Compliance Review Response

```
### Compliance Review: [Document Name]

**Overall Assessment**: [Compliant / Needs Revisions / Major Issues]

**Strengths**:
- ✅ [What's done well]

**Issues Found**:

**🔴 CRITICAL** (legal risk):
- [Issue with fix]

**🟡 IMPORTANT** (should address):
- [Issue with recommendation]

**🔵 SUGGESTIONS** (best practices):
- [Enhancement]

**Required Actions**:
1. [Priority actions]

**Recommendation**: [Final recommendation]

---

**Disclaimer**: General guidance only, not legal advice.
```

## File Structure

```
plugins/hr-policies-expert/
├── README.md                                    # This file
├── plugin.json                                  # Plugin metadata
├── agents/
│   └── hr-policies-expert.md                   # Main HR policy expert agent
└── skills/
    └── hr-policies/
        └── SKILL.md                            # Comprehensive HR knowledge base
```

## Skill Integration

The agent is **skill-aware**, meaning it MUST read the HR policies skill before answering any question. This ensures:

- **Accuracy**: Responses based on actual employment law and policies
- **Consistency**: Same answer for same question every time
- **Compliance**: Guidance aligned with legal requirements
- **Completeness**: All relevant context and citations provided
- **Quality**: Professional HR standard responses

The skill contains 10 parts:
1. Common HR Policies (EEO, harassment, attendance, conduct, etc.)
2. Leave Policies (PTO, FMLA, sick leave, parental leave, etc.)
3. Benefits Policies (health insurance, 401k, other benefits)
4. Labor Law Fundamentals (FLSA, Title VII, ADA, ADEA, FMLA, etc.)
5. Compliance Requirements (postings, notices, recordkeeping)
6. Policy Documentation Standards (writing and structure)
7. Answering Policy Questions (response framework)
8. Compliance Review Checklists
9. Leave Management Guidelines
10. Benefits Administration

## Customization

### Adding Company-Specific Policies

1. **Create company policy documents** in your project:
   ```bash
   mkdir -p .claude/hr-policies/
   # Add your policies as markdown files
   ```

2. **Agent will search for** company policies:
   ```bash
   # Looks for handbook, policies, etc.
   find . -name "*handbook*" -o -name "*policies*"
   ```

3. **Company policies take precedence** over general guidance in skill

### Extending the Skill

1. **Edit the skill** to add company-specific content:
   ```bash
   edit plugins/hr-policies-expert/skills/hr-policies/SKILL.md
   ```

2. **Add sections for**:
   - Your specific policies
   - Company processes
   - Internal contacts
   - Custom benefits

3. **Update regularly** as policies change

## Compliance Note

**Important Disclaimer**: This plugin provides general guidance on HR policies and employment law. It is NOT legal advice.

**Always**:
- Consult qualified legal counsel for specific legal matters
- Review policies with employment law attorney
- Stay current on federal, state, and local law changes
- Document employment decisions and compliance efforts

**Laws Vary By**:
- State
- Local jurisdiction
- Industry
- Company size
- Union status

The guidance provided may need to be adapted for your specific situation.

## Limitations

**What This Plugin Does**:
- ✅ Provides general policy guidance
- ✅ Cites employment laws and requirements
- ✅ Reviews documents for compliance issues
- ✅ Offers HR best practices
- ✅ Structures clear, actionable responses

**What This Plugin Does NOT Do**:
- ❌ Provide legal advice
- ❌ Make employment decisions
- ❌ Modify policies or documents
- ❌ Access HR systems or data
- ❌ Guarantee legal compliance
- ❌ Replace legal counsel review

**This is a knowledge tool**, not a decision-making system. HR professionals and legal counsel should review significant matters.

## Examples

### Example 1: FMLA Eligibility Question

**Request**:
```
"An employee is asking if they qualify for FMLA leave for surgery. How do I determine eligibility?"
```

**Response**:
```
### FMLA Eligibility Determination

**Answer**: FMLA eligibility requires meeting ALL four criteria. Here's how to verify:

**Eligibility Criteria** (must meet ALL):
1. ✅ Worked for company at least 12 months (doesn't have to be consecutive)
2. ✅ Worked at least 1,250 hours in the past 12 months
3. ✅ Company has 50+ employees within 75 miles of work location
4. ✅ Reason is FMLA-qualifying (own serious health condition requiring surgery is covered)

**How to Verify**:
- Check hire date in HRIS (must be 12+ months ago)
- Run hours report for last 12 months (must show 1,250+ hours)
- Confirm location has 50+ employees within 75 miles
- Verify surgery qualifies as serious health condition (will need medical certification)

**If Eligible**:
- Provide FMLA Eligibility Notice
- Send Rights and Responsibilities Notice
- Provide medical certification form
- Give employee 15 days to return certification

**If Not Eligible**:
- Provide written notice of ineligibility and reason
- Offer other leave options (company sick leave, disability, unpaid personal leave)

**Next Steps**:
1. Verify eligibility using criteria above
2. Notify employee in writing within 5 business days
3. If eligible, provide FMLA paperwork immediately
4. Track timeline for certification return (15 days)

**Questions?** Contact HR leadership or employment counsel for complex situations.

---

**Disclaimer**: This is general FMLA guidance. Verify specific circumstances and consult legal counsel for complex situations.
```

### Example 2: Offer Letter Compliance Review

**Request**:
```
"Review this offer letter before we send it to a candidate"
```

**Response**:
```
### Compliance Review: Offer Letter for [Position]

**Overall Assessment**: **Needs Revisions** - Critical at-will language missing

**Strengths**:
- ✅ Compensation clearly stated ($85,000/year)
- ✅ Start date specified (March 1, 2025)
- ✅ Exempt status noted
- ✅ Benefits overview included
- ✅ Professional, welcoming tone

**Issues Found**:

**🔴 CRITICAL** (legal risk, must fix):
- **Missing at-will employment disclaimer**
  - **Risk**: Without at-will language, offer could be interpreted as employment contract, significantly limiting termination rights
  - **Fix**: Add clearly stated at-will paragraph:
    "Employment with [Company] is at-will. This means either you or the company may end the employment relationship at any time, with or without cause or notice, except as required by law. No one other than the CEO has authority to modify this at-will relationship, and any modification must be in writing."

- **Promise of job security**: Letter states "we look forward to many successful years together"
  - **Risk**: Implies long-term employment commitment
  - **Fix**: Change to "we look forward to a successful working relationship"

**🟡 IMPORTANT** (should address):
- **Missing contingencies**: Offer appears unconditional
  - **Recommendation**: Add: "This offer is contingent upon:
    (1) Satisfactory completion of background check
    (2) Verification of eligibility to work in U.S. (Form I-9)
    (3) [Drug screening, if applicable]"

- **No integration clause**: Doesn't state that offer supersedes previous discussions
  - **Recommendation**: Add: "This letter and the Employee Handbook contain the complete terms of your employment. This offer supersedes any prior discussions, negotiations, or agreements."

**🔵 SUGGESTIONS** (best practices):
- Add acceptance deadline (e.g., "Please respond by [date]")
- Specify reporting relationship (reports to [Title])
- Reference employee handbook for additional policies
- Include HR contact for questions

**Required Actions**:
1. **Add at-will disclaimer** (critical - do not skip)
2. **Remove job security language**
3. **Add employment contingencies**
4. **Add integration clause**
5. **Have legal counsel review** revised version before sending

**Review Checklist**:
- ❌ At-will language included
- ✅ Compensation clearly stated
- ❌ Contingencies noted
- ❌ No promises of continued employment
- ✅ Benefits eligibility correct
- ❌ Integration clause included

**Recommendation**: **Revise and obtain legal review** before extending to candidate. The missing at-will language creates significant legal risk.

---

**Disclaimer**: This review provides general guidance. All offer letters should be reviewed by qualified employment counsel before use.
```

### Example 3: PTO Payout Question

**Request**:
```
"Do we have to pay out unused PTO when someone leaves?"
```

**Response**:
```
### PTO Payout on Termination

**Answer**: It depends on your state law and company policy. Some states require payout, others don't.

**State Law Requirements** (varies significantly):

**Must Pay Out** (examples):
- California: Accrued, unused PTO must be paid at final rate
- Massachusetts: Unused vacation must be paid (if policy doesn't say otherwise)
- Montana: Accrued vacation is earned wages, must be paid
- Others: Check your state's specific requirements

**Not Required** (examples):
- Most states: No legal requirement to pay if policy says no payout
- However: Company policy governs—if policy promises payout, must honor it

**Explanation**: PTO laws vary dramatically by state. Where no state law requires payout, company policy controls. But if policy promises payout OR is silent, paying may be required or expected.

**Your Company's Policy**:
[Check Employee Handbook Section X.X for your specific policy language]

**Best Practices**:
- **Clear policy language**: State explicitly whether PTO pays out or not
- **Consistent application**: Same treatment for all terminations (voluntary/involuntary)
- **State compliance**: California/Montana-style states require payout regardless of policy
- **Get legal review**: Have employment attorney review policy for your state(s)

**Next Steps**:
1. **Identify employee's work state**: State law where they work applies
2. **Check state PTO payout requirements**: Research or ask counsel
3. **Review company policy**: Does handbook address payout?
4. **Calculate payout if required**: Accrued balance × current rate
5. **Include in final paycheck**: Must follow state final pay timing too

**State Final Pay Requirements** (also vary):
- Immediate: CA (fired), CO, others
- Next regular payday: Many states
- Within specified days: Others

**Questions?** Contact employment counsel for your state's specific requirements. This is a common area where employers make costly mistakes.

---

**Important**: State law trumps company policy. Even if your policy says "no payout," states like California require it. Consult legal counsel for your jurisdiction.
```

## Performance and Quality

### Response Quality

All responses include:
- **Direct answer** upfront
- **Policy/law citations** with specific sections
- **Clear explanations** of reasoning
- **Concrete examples** when helpful
- **Actionable next steps**
- **Follow-up contact** information
- **Appropriate disclaimers**

### Accuracy Standards

- Based on actual employment law and regulations
- Cites specific statutes and requirements
- Notes state/local variations
- Includes recent law changes (as of January 2025)
- Disclaims when legal counsel needed

### Compliance Focus

All guidance emphasizes:
- Legal compliance first
- Risk mitigation
- Consistent application
- Documentation importance
- Professional practices

## Contributing

To improve this plugin:

1. **Share feedback** on accuracy and usefulness
2. **Suggest additions** to skill library
3. **Report errors** in policy or law information
4. **Contribute templates** for additional policies
5. **Submit improvements** via pull request

## Legal Disclaimer

**IMPORTANT DISCLAIMER**:

This plugin provides general information about HR policies and employment law. It is NOT legal advice and should not be relied upon as such.

Employment law is complex and varies by:
- Federal jurisdiction
- State law
- Local ordinances
- Industry-specific regulations
- Company size and structure
- Union agreements

**Always**:
- Consult qualified legal counsel for specific legal matters
- Verify current law (laws change frequently)
- Consider your specific circumstances
- Document compliance efforts
- Obtain legal review of policies

The creators and contributors of this plugin make no warranties about the accuracy, completeness, or suitability of the information provided. Use at your own risk.

## License

MIT License - free to use and customize for your organization

## Support

For questions or issues:
- Check this README first
- Review the HR policies skill documentation
- Open an issue in the repository
- Share your use case for assistance

## Changelog

### Version 1.0.0 (2025-01-19)

**Initial Release**:
- HR policies expert agent with comprehensive knowledge base
- HR policies skill covering employment law and compliance
- Policy question response framework
- Compliance review checklist approach
- 10-part comprehensive skill covering:
  - Common HR policies
  - Leave policies (PTO, FMLA, sick, parental, etc.)
  - Benefits policies
  - Labor law fundamentals (FLSA, Title VII, ADA, ADEA, etc.)
  - Compliance requirements
  - Policy documentation standards
  - Question response frameworks
  - Leave management guidelines
  - Benefits administration
- Read-only analyst pattern for security
- Structured response format with citations
- Appropriate legal disclaimers

## Acknowledgments

Built on employment law research and HR best practices from:
- Federal employment law statutes and regulations
- EEOC guidance and publications
- DOL wage and hour guidance
- SHRM (Society for Human Resource Management) resources
- Employment law expertise
- HR practitioner experience

---

**Your HR policy knowledge base, available anytime.**
