# Legal Reviewer Plugin

Contract review and analysis specialist for Puerto, focused on risk identification, clause analysis, and amendment suggestions.

## Overview

The Legal Reviewer plugin provides specialized agents and skills for analyzing commercial contracts, identifying legal risks, and suggesting amendments. Built on proven legal review patterns, it helps teams make informed decisions about contracts while protecting their interests.

## Features

- **Comprehensive Contract Analysis**: Systematic review of all essential clauses and provisions
- **Risk Identification**: Multi-dimensional risk assessment with severity ratings and mitigation strategies
- **Amendment Drafting**: Specific proposed language with multiple fallback options
- **Skill-Aware Agents**: All agents leverage battle-tested legal review patterns
- **Production Templates**: Ready-to-use checklists, risk assessment frameworks, and amendment formats

## Agents

### 1. Contract Analyzer (Sonnet)

**Purpose**: Review contracts and identify key clauses, terms, and obligations

**When to Use**:
- Initial contract review
- Due diligence
- Contract comparison
- Obligation extraction
- Compliance verification

**Capabilities**:
- Systematic clause-by-clause analysis
- Key terms extraction
- Obligation identification
- Critical dates tracking
- Missing protections flagging
- Comparison to standards

**Example Usage**:
```
Analyze the attached SaaS agreement between our company (Acme Corp) and vendor (CloudServices Inc).
Focus on: data ownership, liability caps, termination rights, and SLA commitments.
Contract value: $250k/year, 3-year term.
```

**Output**:
- Comprehensive contract analysis
- Key clauses summary
- Obligations list with deadlines
- Issues by priority
- Missing standard clauses
- Favorable/unfavorable terms
- Recommendations

### 2. Risk Identifier (Sonnet)

**Purpose**: Identify legal risks, liabilities, and potential issues in contracts

**When to Use**:
- Risk assessment required
- High-value contracts
- Unfamiliar contract types
- Vendor due diligence
- Board/executive review preparation

**Capabilities**:
- Financial exposure quantification
- Liability risk identification
- Operational constraint analysis
- Compliance issue detection
- Ambiguous language flagging
- Severity rating (Critical/High/Medium/Low)
- Mitigation strategy development

**Example Usage**:
```
Identify all legal risks in the Professional Services Agreement with ABC Consulting.
Our risk tolerance: Medium (we can accept up to $500k exposure).
Key concerns: IP ownership, staff continuity, payment terms.
```

**Output**:
- Risk assessment by category
- Severity and likelihood ratings
- Financial exposure estimates
- Red flags and deal-breakers
- Mitigation strategies
- Prioritized action items
- Accept/negotiate/reject recommendation

### 3. Amendment Suggester (Sonnet)

**Purpose**: Suggest contract amendments and alternative language

**When to Use**:
- Preparing for contract negotiation
- Responding to vendor form agreements
- Addressing identified risks
- Improving unfavorable terms
- Standardizing contract language

**Capabilities**:
- Specific proposed language (not just concepts)
- Multiple versions (preferred, fallback, minimum)
- Negotiation strategy development
- Objection response preparation
- Bundling strategy
- Cover letter drafting

**Example Usage**:
```
Suggest amendments for the MSA with XYZ Corp to address:
1. Unlimited liability (add reasonable cap)
2. One-sided indemnification (make mutual)
3. No termination for convenience (add for both parties)
4. Vendor owns all IP (we need to own work product)
Priority: High - must negotiate before signing next week.
```

**Output**:
- Amendment proposal with exact language
- Multiple versions per amendment
- Rationale for each change
- Priority classification
- Negotiation playbook
- Bundling strategy
- Cover letter template

## Skills

### Legal Review Skill

**Location**: `skills/legal-review/SKILL.md`

**Contains**:
- Contract analysis framework
- Essential clauses checklist
- Risk identification patterns
- Amendment strategy framework
- Contract type specific guidance
- Red flags and warning signs
- Review process best practices
- Risk scoring methodology

**Key Patterns**:

**Essential Clauses**:
1. Parties and Definitions
2. Scope of Work/Services
3. Payment Terms
4. Term and Termination
5. Intellectual Property
6. Confidentiality
7. Representations and Warranties
8. Indemnification
9. Limitation of Liability
10. Dispute Resolution
11. General Provisions

**Risk Severity Levels**:
- 🔴 Critical: Unlimited liability, regulatory violation, no termination rights
- 🟠 High: >$100k exposure, one-sided terms, inadequate IP protection
- 🟡 Medium: $10k-$100k exposure, imbalanced terms, moderate constraints
- 🟢 Low: <$10k exposure, minor issues, clarifications only

**Amendment Tiers**:
- Tier 1 Must Have: Deal-breakers (liability caps, IP protection, regulatory compliance)
- Tier 2 Should Have: Strongly preferred (mutual indemnification, balanced terms)
- Tier 3 Nice to Have: Negotiable improvements (preferred venue, extended payment)

## Templates

### 1. Contract Review Checklist

**Purpose**: Systematic contract review workflow

**Sections**:
- Pre-review preparation
- Essential clauses review (11 categories)
- Risk assessment
- Red flags check
- Missing protections
- Final review

**Usage**: Step-by-step guide ensuring no critical clause is overlooked

### 2. Risk Assessment Template

**Purpose**: Structured legal risk documentation

**Components**:
- Risk categorization (Financial, Liability, Operational, Compliance)
- Severity and likelihood ratings
- Impact quantification
- Mitigation strategies
- Deal-breaker identification
- Financial exposure summary

**Usage**: Consistent risk reporting format for stakeholders

### 3. Amendment Proposal Template

**Purpose**: Professional amendment submission format

**Includes**:
- Amendment structure (issue, current language, proposed language)
- Multiple versions (preferred, fallback, minimum)
- Rationale and justification
- Bundling strategy
- Negotiation approach
- Cover letter

**Usage**: Formal negotiation package for counterparties

## Workflow Examples

### Example 1: SaaS Agreement Review

```
1. Use contract-analyzer for initial comprehensive review
2. Use risk-identifier to assess financial and liability exposure
3. Review vendor's SLA, data security, and IP provisions
4. Use amendment-suggester for data ownership, liability cap, and termination rights
5. Prepare negotiation package with 3 tiers of amendments
6. Submit to vendor with cover letter
```

### Example 2: High-Risk Contract Assessment

```
1. Use risk-identifier first to quickly flag critical issues
2. If critical risks found, escalate to legal team immediately
3. Use contract-analyzer for detailed clause review
4. Document all obligations and deadlines
5. Use amendment-suggester for must-fix items
6. Present to leadership with accept/negotiate/reject recommendation
```

### Example 3: Amendment Negotiation

```
1. Review vendor's initial response to our amendments
2. Use amendment-suggester to draft fallback positions
3. Prepare 3 versions: ideal, acceptable, walk-away
4. Identify concessions we can offer
5. Define non-negotiable items
6. Execute negotiation with prepared responses to objections
```

## Best Practices

### Agent Usage

1. **Read Skills First**: All agents require reading the legal review skill before execution
2. **Cite Specifics**: Always reference exact section numbers and page numbers
3. **Quantify Risk**: Provide dollar amounts or percentage of contract value for exposure
4. **Multiple Options**: Offer 3 versions of amendments (preferred, fallback, minimum)
5. **Business Context**: Balance legal protection with commercial objectives

### Risk Assessment

**Severity Calculation**:
- Critical: >$1M exposure OR unlimited liability OR regulatory violation
- High: $100k-$1M exposure OR significant operational impact
- Medium: $10k-$100k exposure OR moderate constraints
- Low: <$10k exposure OR minimal impact

**Priority Matrix**:
- P1 (Must Address): Critical/High severity + Medium/High likelihood
- P2 (Should Address): High/Medium severity + Low/Medium likelihood
- P3 (Monitor): Low severity OR Low likelihood

### Amendment Strategy

**Tier 1 (Must Have)**:
- Deal-breakers
- Cannot sign without
- Worth walking away over

**Tier 2 (Should Have)**:
- Strongly preferred
- Will negotiate hard
- May concede if necessary

**Tier 3 (Nice to Have)**:
- Improvements
- Willing to drop
- Negotiating chips

### Common Pitfalls

❌ **Skimming contracts**: Read every word
✅ **Thorough review**: Including all exhibits and referenced documents

❌ **Assuming standard is safe**: "Boilerplate" often favors drafter
✅ **Analyze everything**: No clause is too standard to review

❌ **Vague amendment requests**: "Make this more fair"
✅ **Specific language**: Exact proposed text with multiple versions

❌ **All-or-nothing negotiation**: "Accept all or we walk"
✅ **Tiered approach**: Must-have vs. nice-to-have with fallbacks

## Integration Points

### Legal Review Process
- Initial screening by business team
- Legal review for material contracts
- Risk escalation to leadership
- Negotiation tracking
- Final approval workflow

### Contract Management System
- Contract repository
- Obligation tracking
- Renewal notifications
- Compliance monitoring
- Amendment history

### Risk Management
- Risk register integration
- Financial exposure tracking
- Insurance requirement verification
- Audit trail maintenance

## Requirements Met

✅ **Role**: Contract review and analysis specialist
✅ **Responsibilities**:
  - Contract review with systematic clause analysis
  - Risk identification across all categories
  - Clause analysis with specific findings
  - Amendment suggestions with multiple versions
  - Comparison with templates and standards
✅ **Tools**: File operations, contract templates, risk frameworks
✅ **Plugin Structure**: agents/, skills/, templates/
✅ **Agent Count**: 3 agents (contract-analyzer, risk-identifier, amendment-suggester)
✅ **Skill**: Comprehensive legal-review skill (380 lines)
✅ **Model Optimization**: Sonnet for all agents (complex reasoning required)
✅ **Puerto Best Practices**: Skill-aware, single responsibility, production-ready

## Getting Started

1. **Install Plugin**: Copy to `~/.claude/plugins/legal-reviewer/`
2. **Review Skill**: Read `skills/legal-review/SKILL.md` for patterns
3. **Choose Agent**: Select based on task (analyze, assess risk, or amend)
4. **Provide Contract**: Share contract document or paste text
5. **Specify Context**: Business objectives, risk tolerance, concerns
6. **Execute**: Let agent create analysis, assessment, or amendments

## File Structure

```
plugins/legal-reviewer/
├── .claude-plugin/
│   └── plugin.json                    # Plugin manifest
├── agents/
│   ├── contract-analyzer.md           # Contract review (Sonnet)
│   ├── risk-identifier.md             # Risk assessment (Sonnet)
│   └── amendment-suggester.md         # Amendment drafting (Sonnet)
├── skills/
│   └── legal-review/
│       └── SKILL.md                   # Legal review patterns
├── templates/
│   ├── contract-review-checklist.md   # Review workflow
│   ├── risk-assessment-template.md    # Risk documentation
│   └── amendment-proposal.md          # Amendment format
└── README.md                          # This file
```

## Important Disclaimers

**This plugin is for contract review assistance only, not legal advice.**

- Agents identify issues and suggest language
- Final decisions require human judgment
- Complex matters need qualified legal counsel
- Regulatory compliance requires legal expertise
- Use as support tool, not replacement for attorneys

## Version

**Version**: 1.0.0
**Author**: Puerto Plugin System
**License**: MIT

## Support

For issues, questions, or contributions, please refer to the Puerto plugin system documentation.

---

**Note**: This plugin focuses on commercial B2B contracts (SaaS, MSA, PSA, NDA, etc.). Adapt patterns to your specific jurisdiction, industry, and contract types.
