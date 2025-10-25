# Legal Review Skill

**Production-tested patterns for contract analysis, risk identification, and legal review**

This skill codifies best practices from legal and compliance teams reviewing commercial contracts.

---

## Core Principles

1. **Thoroughness**: Read every word, every clause, every exhibit
2. **Risk Focus**: Identify and quantify exposure points
3. **Business Alignment**: Balance legal protection with commercial objectives
4. **Specificity**: Cite exact language, provide concrete recommendations
5. **Prioritization**: Distinguish deal-breakers from nice-to-haves

---

## Contract Analysis Framework

### Essential Clauses Checklist

Every contract review must analyze these core provisions:

**1. Parties and Definitions**
- Legal entity names correct
- Addresses accurate
- Defined terms consistent
- No circular definitions

**2. Scope of Work/Services**
- Deliverables clearly specified
- Performance standards defined
- Acceptance criteria explicit
- Timelines realistic

**3. Payment Terms**
- Amount and currency clear
- Payment schedule defined
- Method specified
- Late payment consequences
- Taxes and expenses allocated

**4. Term and Termination**
- Initial term duration
- Renewal mechanism (auto/manual)
- Notice period for non-renewal
- Termination for convenience
- Termination for cause
- Effect of termination
- Survival clauses

**5. Intellectual Property**
- Work product ownership
- License grants and scope
- Pre-existing IP treatment
- Derivative works
- Moral rights
- Patent/trademark usage

**6. Confidentiality**
- Definition of confidential info
- Duration of obligations
- Permitted disclosures
- Return/destruction requirements
- Exclusions from confidentiality

**7. Representations and Warranties**
- Authority to enter contract
- Ownership of assets/IP
- Compliance with laws
- No conflicts
- Product/service warranties
- Warranty duration and remedies

**8. Indemnification**
- Who indemnifies whom
- Scope (IP, breach, third-party claims)
- Process (notice, defense, settlement)
- Limitations or caps
- Insurance requirements

**9. Limitation of Liability**
- Cap amount ($ or % of fees)
- Excluded damages (consequential, etc.)
- Exceptions to cap (willful misconduct, IP, confidentiality)
- Reasonableness vs. contract value

**10. Dispute Resolution**
- Governing law (jurisdiction)
- Venue for disputes
- Dispute process (negotiation → mediation → arbitration/litigation)
- Attorney fees provision
- Injunctive relief preservation

**11. General Provisions**
- Assignment restrictions
- Force majeure
- Notices (address, method)
- Entire agreement
- Amendment process
- Severability
- Waiver
- Counterparts

---

## Risk Identification Patterns

### Financial Exposure Risks

**Unlimited Liability** 🚨 CRITICAL
```
❌ Problematic: "Party A shall indemnify Party B for any and all claims..."
✅ Better: "Party A shall indemnify Party B up to the amount paid under this Agreement in the 12 months preceding the claim..."
```

**Uncapped Indemnification** 🚨 CRITICAL
```
❌ Problematic: Indemnification with no dollar limit
✅ Better: Indemnification capped at 2x annual contract value, except for IP infringement, gross negligence, or willful misconduct
```

**Payment Without Acceptance** ⚠️ HIGH
```
❌ Problematic: "Payment due upon delivery"
✅ Better: "Payment due 30 days after acceptance or 45 days after delivery, whichever is earlier"
```

**Automatic Price Increases** ⚠️ MEDIUM
```
❌ Problematic: "Prices may increase at vendor's discretion"
✅ Better: "Prices fixed for initial term; subsequent increases limited to CPI or 5%, whichever is less, with 90 days notice"
```

### Liability and Risk Allocation

**One-Sided Indemnification** ⚠️ HIGH
```
❌ Problematic: Only we indemnify, they don't
✅ Better: Mutual indemnification for IP infringement and breach of contract
```

**Broad Consequential Damages** 🚨 CRITICAL
```
❌ Problematic: Party liable for lost profits, business interruption, etc.
✅ Better: "Neither party liable for consequential, incidental, or punitive damages, except for breach of confidentiality or IP infringement"
```

**Warranty of Results** ⚠️ HIGH
```
❌ Problematic: "Vendor guarantees [specific business outcome]"
✅ Better: "Vendor represents that services will be performed in professional manner consistent with industry standards"
```

### Operational and Compliance Risks

**Exclusive Relationship** ⚠️ MEDIUM
```
❌ Problematic: "Customer shall not engage any competitor of Vendor"
✅ Better: Avoid exclusivity or limit scope/duration narrowly with carve-outs
```

**Overly Broad Non-Compete** 🚨 CRITICAL
```
❌ Problematic: "No competing products for 5 years worldwide"
✅ Better: No non-compete, or very narrow scope/geography/duration if essential
```

**Unfavorable Data Terms** ⚠️ HIGH
```
❌ Problematic: "Vendor owns all data"
✅ Better: "Customer retains all ownership of Customer Data; Vendor has license only to provide services"
```

**Audit Rights Imbalance** ⚠️ MEDIUM
```
❌ Problematic: They can audit us anytime; we have no audit rights
✅ Better: Mutual audit rights with reasonable notice and frequency limits
```

### Termination and Exit Risks

**Termination for Convenience Imbalance** ⚠️ HIGH
```
❌ Problematic: They can terminate anytime; we cannot
✅ Better: Mutual termination for convenience with equal notice period
```

**No Termination for Breach** 🚨 CRITICAL
```
❌ Problematic: Cannot terminate even if they materially breach
✅ Better: "Either party may terminate if other party materially breaches and fails to cure within 30 days of notice"
```

**Inadequate Data Return** ⚠️ MEDIUM
```
❌ Problematic: No provision for return of data upon termination
✅ Better: "Within 30 days of termination, Vendor shall return or destroy all Customer Data in format reasonably requested by Customer"
```

**Auto-Renewal Without Notice** ⚠️ MEDIUM
```
❌ Problematic: "Auto-renews for successive 1-year terms"
✅ Better: "Auto-renews unless either party gives 60 days written notice of non-renewal before end of term"
```

---

## Amendment Strategy Framework

### Negotiation Hierarchy

**Tier 1: Must Have** (Deal-breakers)
- Liability cap appropriate to contract value
- Mutual termination rights
- IP ownership protection
- Regulatory compliance provisions
- Data protection adequate for regulations

**Tier 2: Should Have** (Strongly preferred)
- Mutual indemnification
- Balanced warranties
- Reasonable payment terms
- Fair renewal/termination notice
- Audit rights

**Tier 3: Nice to Have** (Negotiable)
- Most favored customer pricing
- SLA credits
- Preferred venue for disputes
- Specific insurance amounts
- Extended payment terms

### Standard Amendment Language

**Liability Cap Template**:
```
"Except for [EXCEPTIONS: breach of confidentiality, IP infringement, gross negligence, willful misconduct], neither party's aggregate liability arising out of or related to this Agreement shall exceed [OPTION 1: the total amounts paid or payable under this Agreement in the 12 months preceding the claim] [OPTION 2: $[SPECIFIC AMOUNT]]."
```

**Mutual Indemnification Template**:
```
"Each party (the "Indemnifying Party") shall defend, indemnify, and hold harmless the other party from and against any third-party claims, damages, and costs (including reasonable attorneys' fees) arising from: (a) the Indemnifying Party's breach of this Agreement; (b) the Indemnifying Party's infringement of third-party intellectual property rights; or (c) the Indemnifying Party's gross negligence or willful misconduct."
```

**Termination for Convenience Template**:
```
"Either party may terminate this Agreement for convenience upon [60/90] days' prior written notice to the other party. Upon termination for convenience, Customer shall pay for all services rendered through the termination date."
```

**Data Protection Template**:
```
"Customer retains all right, title, and interest in Customer Data. Vendor shall: (a) use Customer Data only to provide services under this Agreement; (b) implement appropriate technical and organizational measures to protect Customer Data; (c) not disclose Customer Data to third parties without Customer consent; and (d) upon termination, return or destroy all Customer Data as directed by Customer."
```

---

## Contract Type Specific Patterns

### Software as a Service (SaaS) Agreements

**Critical Provisions**:
- Service levels and availability (uptime %, credits)
- Data security and privacy (SOC 2, encryption)
- Data ownership and portability
- Subprocessor disclosure and approval
- Escrow for source code (if material)
- Integration support and APIs

**Common Issues**:
- Vendor owns all usage data
- No SLA or unenforceable SLA
- Weak data security commitments
- Cannot export data in usable format
- Vendor can change features/pricing at will

### Master Service Agreements (MSA)

**Critical Provisions**:
- SOW process and requirements
- Resource qualifications
- Acceptance criteria
- Change order process
- Staff continuity or replacement
- Ownership of work product

**Common Issues**:
- Vague scope allowing vendor discretion
- No acceptance testing
- All changes billable at vendor discretion
- Vendor owns deliverables
- No recourse for poor performance

### Non-Disclosure Agreements (NDA)

**Critical Provisions**:
- Mutual vs. one-way confidentiality
- Definition of confidential information
- Duration (2-5 years typical)
- Carve-outs (public, already known, independently developed)
- Return/destruction obligation
- No implied license

**Common Issues**:
- One-way when should be mutual
- Overly broad definition (all information shared)
- Perpetual duration
- Insufficient carve-outs
- Residuals clause too broad

### Professional Services Agreements

**Critical Provisions**:
- Deliverables and milestones
- Acceptance criteria
- Resource qualifications and key personnel
- Work product ownership
- Subcontracting limitations
- Expenses (what's reimbursable)

**Common Issues**:
- Time and materials with no cap
- Acceptance based solely on delivery
- Vendor can substitute resources freely
- Vendor owns work product
- Unlimited expense reimbursement

---

## Red Flags and Warning Signs

### Language That Signals Problems

**"At Vendor's sole discretion"**
→ Gives vendor unilateral control; push for mutual agreement or defined criteria

**"Without limitation"**
→ Creates open-ended obligation; add reasonable limitations

**"Any and all"**
→ Overly broad; specify what's actually covered

**"As is" / "With all faults"**
→ Disclaimer of warranties; unacceptable for purchased products/services

**"Irrevocable"**
→ Cannot be changed; avoid or limit duration/scope

**"Exclusive"**
→ Prevents alternatives; avoid or narrow significantly

**"Perpetual"**
→ Forever; limit to specific duration or tie to contract term

**"Unlimited liability"**
→ No cap on exposure; absolutely must add cap

### Structural Red Flags

- Contract heavily favors one party throughout
- Multiple conflicting or inconsistent provisions
- Important terms left to "good faith" or future agreement
- Key definitions missing or circular
- References to exhibits that don't exist
- Handwritten changes not initialed
- Execution date before negotiation complete
- No severability clause (entire contract void if one provision invalid)

---

## Review Process Best Practices

### Initial Review (30 minutes)

1. **Identify contract type** and purpose
2. **Skim for red flags**: Unlimited, exclusive, irrevocable, perpetual
3. **Check essentials present**: Parties, term, payment, termination, liability, dispute resolution
4. **Note overall balance**: Does it heavily favor one party?
5. **Flag immediate concerns** for deep dive

### Detailed Analysis (2-4 hours)

1. **Read every word** carefully, including exhibits
2. **Analyze each essential clause** against checklist
3. **Extract all obligations** for both parties
4. **Identify all risks** and quantify exposure
5. **Compare to standard forms** (ours and industry)
6. **Note missing protections**
7. **Check internal consistency** (definitions, cross-references)
8. **Document findings** with section/page references

### Amendment Development (1-2 hours)

1. **Prioritize issues**: Must have, should have, nice to have
2. **Draft specific language** (not just concepts)
3. **Provide multiple versions**: Preferred, fallback, minimum
4. **Explain rationale** for each change
5. **Anticipate objections** and prepare responses
6. **Identify trade-offs** and concessions we can make

---

## Risk Scoring Methodology

### Severity Levels

**🔴 Critical**:
- Unlimited financial exposure
- Regulatory violation
- Loss of critical IP
- No termination rights
- Unacceptable operational constraints

**🟠 High**:
- Financial exposure >$100k or >10% of contract value
- One-sided liability allocation
- Inadequate IP protection
- Unfair termination provisions
- Significant operational constraints

**🟡 Medium**:
- Financial exposure $10k-$100k or 2-10% of contract value
- Imbalanced but not one-sided terms
- Moderate operational impact
- Missing standard protections

**🟢 Low**:
- Financial exposure <$10k or <2% of contract value
- Minor imbalances
- Low operational impact
- Clarification issues only

### Priority Matrix

| Severity | Likelihood High | Likelihood Medium | Likelihood Low |
|----------|----------------|-------------------|----------------|
| Critical | P1 - Must Fix | P1 - Must Fix | P2 - Should Fix |
| High | P1 - Must Fix | P2 - Should Fix | P2 - Should Fix |
| Medium | P2 - Should Fix | P3 - Monitor | P3 - Monitor |
| Low | P3 - Monitor | P3 - Monitor | Accept |

---

## Common Mistakes to Avoid

❌ **Skimming instead of reading thoroughly**
→ Critical issues often in "boilerplate" sections

❌ **Assuming standard language is favorable**
→ Many "standard" clauses heavily favor drafter

❌ **Focusing only on business terms**
→ Legal terms create most risk exposure

❌ **Not quantifying financial exposure**
→ Cannot assess risk without numbers

❌ **Accepting "this is our standard form"**
→ Everything is negotiable to some degree

❌ **Negotiating without fallback positions**
→ Need 3 versions: ideal, acceptable, minimum

❌ **Making only vague requests**
→ Must provide specific proposed language

❌ **Not considering relationship impact**
→ Balance legal protection with commercial reality

---

## Summary Checklist

### Analysis Complete When:
- [ ] Entire contract read word-for-word
- [ ] All essential clauses analyzed
- [ ] All obligations extracted
- [ ] All risks identified and quantified
- [ ] Missing protections noted
- [ ] Inconsistencies documented
- [ ] Overall assessment provided

### Risk Assessment Complete When:
- [ ] Risks categorized by type
- [ ] Severity rated (Critical/High/Medium/Low)
- [ ] Likelihood assessed
- [ ] Financial exposure quantified
- [ ] Priority assigned (P1/P2/P3)
- [ ] Mitigation strategies proposed

### Amendments Complete When:
- [ ] Specific language drafted (not concepts)
- [ ] Multiple versions provided
- [ ] Rationale explained
- [ ] Priorities clear (must/should/nice)
- [ ] Trade-offs identified
- [ ] Negotiation strategy included

---

**Version**: 1.0
**Last Updated**: January 2025
**Application**: Commercial contracts (B2B focus)
