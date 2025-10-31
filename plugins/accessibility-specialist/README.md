# Accessibility Specialist Plugin

Digital accessibility specialist for WCAG compliance audits, accessibility testing, remediation recommendations, screen reader testing, and documentation following WCAG 2.1, Section 508, and ADA standards.

## Overview

Provides agents for comprehensive digital accessibility compliance using WCAG 2.1 Level AA standards, automated and manual testing, and remediation guidance.

## Agents

### 1. accessibility-auditor (Sonnet, Skill-Aware)
Conducts comprehensive accessibility audits using automated tools and manual testing against WCAG 2.1.

**Use for**: Full accessibility audits, compliance assessment, issue identification

**Example**:
```
Use accessibility-auditor for website accessibility audit.
Site: E-commerce platform (10 key pages)
Standard: WCAG 2.1 Level AA
Testing:
- Automated: axe DevTools, WAVE, Lighthouse
- Manual: Keyboard navigation, screen reader (NVDA/JAWS)
- Color contrast: All text meets 4.5:1 minimum
- Focus indicators: Visible on all interactive elements
Output: Audit report with violations by severity (Critical/High/Medium/Low)
```

### 2. wcag-checker (Sonnet, Skill-Aware)
Validates against specific WCAG success criteria with detailed compliance checking.

**Use for**: WCAG compliance verification, criterion-by-criterion assessment

**Example**:
```
Use wcag-checker for WCAG 2.1 Level AA compliance.
Success criteria to verify:
- 1.1.1 Non-text Content (Level A): All images have alt text
- 1.4.3 Contrast (Level AA): Text contrast ≥4.5:1, large text ≥3:1
- 2.1.1 Keyboard (Level A): All functionality available via keyboard
- 2.4.7 Focus Visible (Level AA): Keyboard focus indicator visible
- 4.1.2 Name, Role, Value (Level A): All controls have accessible names
Output: Pass/Fail for each criterion with evidence and examples
```

### 3. remediation-consultant (Sonnet, Skill-Aware)
Provides specific remediation recommendations with code examples and priority.

**Use for**: Fixing accessibility violations, implementation guidance, code examples

**Example**:
```
Use remediation-consultant for accessibility violations.
Violations found:
1. Missing alt text on 50 product images (WCAG 1.1.1, Critical)
2. Color contrast 3.2:1 on CTAs (WCAG 1.4.3, High)
3. Missing ARIA labels on icon buttons (WCAG 4.1.2, High)
4. Skip link not visible on focus (WCAG 2.4.1, Medium)
Remediation:
- Priority 1 (Critical): Add alt text with product names
- Priority 2 (High): Darken CTA colors to meet 4.5:1 contrast
- Priority 3 (High): Add aria-label to all icon-only buttons
- Priority 4 (Medium): Make skip link visible on keyboard focus
Include code examples for each fix
```

### 4. documentation-writer (Sonnet, Skill-Aware)
Creates accessibility statements, conformance reports, and documentation.

**Use for**: Accessibility statements, VPAT/ACR, compliance documentation

**Example**:
```
Use documentation-writer for accessibility statement.
Product: SaaS web application
Conformance level: WCAG 2.1 Level AA (partial)
Known issues:
- Video content lacks captions (WCAG 1.2.2) - remediation by Q2
- Some PDF documents not accessible (WCAG 1.3.1) - remediation in progress
Contact: accessibility@company.com
Include: Conformance statement, known limitations, remediation timeline, contact info
```

## Skills

### accessibility-standards
Complete accessibility standards and testing methodologies:
- **WCAG 2.1**: Web Content Accessibility Guidelines (A, AA, AAA levels)
- **Section 508**: US federal accessibility standard
- **ADA**: Americans with Disabilities Act requirements
- **ARIA**: Accessible Rich Internet Applications specification
- **Testing Tools**: axe DevTools, WAVE, Lighthouse, NVDA, JAWS, VoiceOver
- **Manual Testing**: Keyboard navigation, screen readers, zoom testing

## Templates

### accessibility-audit-template.md
Audit report: Executive summary, methodology, findings by WCAG criterion, severity classification, remediation recommendations, timeline.

### wcag-compliance-checklist.md
WCAG 2.1 checklist: All success criteria (A, AA, AAA) with pass/fail status, evidence, and notes for 13 guidelines across 4 principles (POUR).

### remediation-plan-template.md
Remediation plan: Prioritized violation list, code examples, implementation guidance, timeline, verification steps.

### accessibility-statement-template.md
Accessibility statement: Conformance level, known issues, remediation timeline, contact information, feedback mechanism.

## Workflows

```
1. Audit
Use accessibility-auditor for comprehensive testing

2. WCAG validation
Use wcag-checker for criterion-by-criterion compliance

3. Remediation
Use remediation-consultant for fix implementation

4. Documentation
Use documentation-writer for statements and reports
```

## Requirements Met

✅ Role: Digital accessibility specialist
✅ Accessibility audits: accessibility-auditor with automated + manual testing
✅ WCAG compliance: wcag-checker with 2.1 Level AA
✅ Remediation: remediation-consultant with code examples
✅ Screen reader testing: Covered in audits (NVDA, JAWS, VoiceOver)
✅ Documentation: documentation-writer for statements and VPATs

## Key Features

✓ **WCAG 2.1 Level AA**: Complete compliance framework
✓ **Automated + Manual**: Comprehensive testing approach
✓ **Screen Reader Testing**: NVDA, JAWS, VoiceOver
✓ **Code Examples**: Specific remediation guidance
✓ **Priority-Based**: Critical/High/Medium/Low severity
✓ **Standards**: WCAG, Section 508, ADA, ARIA

## WCAG 2.1 Principles (POUR)

**Perceivable**: Information must be presentable to users
- 1.1 Text Alternatives
- 1.2 Time-based Media
- 1.3 Adaptable
- 1.4 Distinguishable

**Operable**: UI components must be operable
- 2.1 Keyboard Accessible
- 2.2 Enough Time
- 2.3 Seizures
- 2.4 Navigable
- 2.5 Input Modalities

**Understandable**: Information must be understandable
- 3.1 Readable
- 3.2 Predictable
- 3.3 Input Assistance

**Robust**: Content must be robust for assistive technologies
- 4.1 Compatible

Closes #85
