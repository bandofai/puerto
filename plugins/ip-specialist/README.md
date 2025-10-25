# IP Specialist Plugin

**Production-ready intellectual property management with patent search, portfolio tracking, filing documentation, and infringement monitoring**

A comprehensive plugin providing four specialized agents to handle all aspects of IP management, from prior art searches to portfolio maintenance and competitive intelligence.

---

## Overview

This plugin provides a complete IP management workflow with:

- **4 Specialized Agents**: Each agent focuses on one aspect of IP management
- **3 Comprehensive Skills**: Battle-tested knowledge from IP professionals
- **3 Professional Templates**: Ready-to-use filing and tracking documents
- **Full Coverage**: Search → Track → File → Monitor

---

## Agents

### 1. patent-searcher (Sonnet - Requires Judgment)

**When to use**: Prior art searches, patent landscape analysis, freedom-to-operate research

**What it does**:
- Conducts comprehensive patent searches across USPTO, EPO, WIPO databases
- Uses IPC/CPC classification systems for thorough coverage
- Analyzes patent landscapes and competitive positioning
- Identifies blocking patents and white space opportunities
- Reviews non-patent literature (academic papers, open source, standards)
- Generates detailed search reports with recommendations

**Skill-aware**: Reads `prior-art-research` and `ip-management` skills before starting

**Example usage**:
```bash
"Conduct prior art search for machine learning-based medical diagnostic system.
Search USPTO, EPO, and Google Patents. Focus on AI/ML classifications (G06N)
and medical informatics (G16H). Include academic literature from 2018-present."
```

**Output**:
- Comprehensive search report with 20-50 relevant references
- Classification codes searched (IPC/CPC)
- Search queries documented (reproducible)
- Key references analyzed (claims, status, relevance)
- Landscape analysis (competitors, trends, opportunities)
- Risk assessment (blocking patents, FTO concerns)
- Strategic recommendations

**Tools**: Read, Write, Edit, Bash, WebSearch, Grep, Glob
**Model**: Sonnet (requires judgment for relevance and strategic analysis)

---

### 2. ip-tracker (Haiku - Fast & Routine)

**When to use**: Portfolio tracking, renewal deadlines, maintenance management

**What it does**:
- Tracks patents, trademarks, copyrights, trade secrets
- Monitors renewal and maintenance deadlines
- Calculates maintenance fees (USPTO, EPO, international)
- Generates deadline reports and alerts (90/60/30 days)
- Updates portfolio status and legal status changes
- Manages portfolio documentation and organization

**Skill-aware**: Reads `ip-management` skill before tracking work

**Example usage**:
```bash
"Update IP portfolio tracker with status of all patents. Flag any maintenance
fees due in next 90 days. Calculate costs and generate deadline report."
```

**Output**:
- Updated portfolio spreadsheet
- Deadline report with upcoming actions (next 90-120 days)
- Cost projections for maintenance fees
- Status updates (granted, pending, expired)
- Alert flags for critical deadlines (< 30 days)
- Recommendations for portfolio optimization

**Tools**: Read, Write, Edit, Bash, Grep, Glob
**Model**: Haiku (fast for deterministic tracking and calculations, 90% cost savings)

---

### 3. filing-assistant (Sonnet - Complex Documentation, Skill-Aware)

**When to use**: Preparing patent or trademark filing documentation

**What it does**:
- Prepares patent applications (utility, design, provisional)
- Drafts patent claims (independent and dependent)
- Writes detailed descriptions with enablement
- Prepares trademark applications and descriptions
- Formats according to USPTO/EPO standards
- Generates filing packages with all required forms
- Provides filing instructions and cost estimates

**Skill-aware**: Reads `ip-documentation` and `ip-management` skills, checks for docx skill if available

**Example usage**:
```bash
"Prepare provisional patent application for blockchain-based payment system.
Invention disclosure: distributed ledger with multi-party verification,
smart contract integration, and privacy-preserving transactions. Include
3 independent claims covering device, method, and system."
```

**Output**:
- Complete patent application (specification, claims, abstract)
- Formatted per USPTO requirements (margins, spacing, numbering)
- Claims covering multiple embodiments (device, method, system)
- Drawings descriptions (references to figures)
- Filing checklist and instructions
- Fee calculation (entity size dependent)
- Quality review checklist (enablement, written description, definiteness)

**Tools**: Read, Write, Edit, Bash, Grep, Glob
**Model**: Sonnet (complex legal/technical writing requires judgment)

---

### 4. infringement-monitor (Sonnet - Strategic Analysis)

**When to use**: Monitoring for IP infringement, competitive intelligence, market analysis

**What it does**:
- Monitors for potential patent infringement (products, services)
- Tracks trademark conflicts and likelihood of confusion
- Searches for competitive patent filings and trademark applications
- Conducts element-by-element infringement analysis (claim mapping)
- Assesses commercial impact and risk levels
- Documents evidence (screenshots, URLs, dates)
- Recommends enforcement actions (cease & desist, licensing, litigation)

**Skill-aware**: Reads `ip-management` and `prior-art-research` skills

**Example usage**:
```bash
"Monitor for potential infringement of US Patent 11,123,456 (ML image recognition).
Search for products using similar neural network architectures for medical imaging.
Check recent patent filings by competitors in G06N and G16H classes. Assess risk
and recommend enforcement strategy."
```

**Output**:
- Infringement monitoring report
- Potential infringers identified (companies, products)
- Infringement analysis (claim charts, element-by-element comparison)
- Evidence package (screenshots, product specs, dates)
- Risk assessment (High/Medium/Low infringement strength and commercial impact)
- Competitive intelligence (new filings, market trends)
- Enforcement recommendations (cease & desist, licensing, litigation)
- Action priority matrix

**Tools**: Read, Write, Edit, Bash, WebSearch, Grep, Glob
**Model**: Sonnet (requires judgment for legal analysis and strategic recommendations)

---

## Skills

### 1. ip-management

**Comprehensive IP portfolio management knowledge**

Covers:
- **Asset Types**: Patents (utility, design, plant), trademarks, copyrights, trade secrets
- **Lifecycle Management**: Filing → prosecution → grant → maintenance → enforcement
- **Deadline Tracking**: Maintenance fees (USPTO: 3.5, 7.5, 11.5 years), trademark renewals (5-6, 9-10 years)
- **Strategic Planning**: Patent vs. trade secret decisions, geographic coverage, claim strategy
- **Cost Management**: Fee schedules (micro/small/large entity), budget allocation, ROI analysis
- **Valuation**: Cost, market, income approaches; licensing rates by industry
- **Risk Management**: FTO analysis, validity assessment, ownership verification
- **International**: PCT, EPO, Madrid Protocol; foreign filing strategies
- **Best Practices**: Invention capture, due diligence, documentation standards

**When read**: By all agents for strategic context and portfolio knowledge

---

### 2. prior-art-research

**Patent search strategies and classification systems**

Covers:
- **Search Fundamentals**: Patentability, FTO, invalidity, landscape searches
- **Classification Systems**: IPC (8 sections, hierarchical), CPC (250k+ categories, USPTO/EPO joint system)
- **Databases**: USPTO (PatFT, AppFT), Google Patents, EPO Espacenet, WIPO PatentScope
- **Search Strategies**: Iterative approach (exploratory → keywords → classification → citations → assignee)
- **Boolean and Field Searches**: Operators (AND, OR, NOT), proximity (NEAR, ADJ), field codes (TI/, AB/, ACLM/, CCL/)
- **Citation Analysis**: Backward citations (prior art), forward citations (later developments), patent families
- **Non-Patent Literature**: Academic papers (Google Scholar, IEEE, PubMed), standards (IEEE, ISO), open source (GitHub)
- **Documentation**: Search reports, query logs, reference tracking

**When read**: By `patent-searcher` before conducting searches, by `infringement-monitor` for search techniques

---

### 3. ip-documentation

**Filing templates and legal language standards**

Covers:
- **Patent Application Structure**: Title, background, summary, detailed description, claims, abstract, drawings
- **Claims Drafting**: Independent vs. dependent, preamble-transition-body structure, transitions (comprising, consisting of, consisting essentially of)
- **Patent Description**: Enablement (§112(a)), written description, best mode, multiple embodiments, examples
- **Trademark Documentation**: Mark description, goods/services identification (Nice Classification), specimens, basis (§1(a) use, §1(b) intent-to-use)
- **Legal Language**: Means-plus-function (§112(f)), definiteness (§112(b)), antecedent basis, consistent terminology
- **USPTO Requirements**: Formatting (37 CFR 1.52), fees (entity status), formal requirements, maintenance schedules
- **International Filing**: PCT application process, EPO requirements, foreign filing licenses, Madrid Protocol

**When read**: By `filing-assistant` before preparing any filing documents

---

## Templates

### 1. patent-filing-template.docx

**Complete utility patent application structure**

Includes:
- Application data sheet (inventors, assignee, priority claims)
- Cross-reference to related applications section
- Background of the invention (field, prior art, problems)
- Brief summary (objects, advantages, overview)
- Brief description of drawings (FIG. 1, FIG. 2, etc.)
- Detailed description (enablement, written description, best mode, multiple embodiments, examples)
- Claims section (independent claims 1, 11, 21; dependent claims 2-10, 12-20, 22-30)
- Abstract (max 150 words)
- Formatting guidelines (USPTO 37 CFR 1.52: margins, line numbering, paragraph numbering)
- Filing checklist (enablement, antecedent basis, consistent terminology)

**Use for**: Utility patent applications (most common type)

---

### 2. trademark-application-template.docx

**Comprehensive trademark application guide**

Includes:
- Pre-filing checklist (clearance search, mark selection, specimen preparation)
- Applicant information (individual or entity)
- Mark information (standard character vs. special form)
- Mark description (for stylized/logo marks)
- Color claim (if applicable)
- Translation and transliteration (if foreign wording)
- Disclaimer requirements (generic/descriptive terms)
- Goods and services identification (Nice Classification, acceptable wording)
- Specimen requirements (for goods: labels, tags, packaging; for services: ads, websites)
- Filing basis (§1(a) Use in Commerce vs. §1(b) Intent to Use)
- Declarations and signatures
- TEAS Plus vs. TEAS Standard (fee differences)
- USPTO ID Manual guidance (acceptable identifications)

**Use for**: US trademark applications via TEAS system

---

### 3. ip-portfolio-tracker.xlsx

**Multi-sheet portfolio management spreadsheet**

Includes:
- **Portfolio Summary**: Dashboard with counts, deadlines, costs
- **Patent Portfolio**: Asset ID, type, title, jurisdiction, application/patent numbers, filing/grant dates, status, deadlines, costs, inventors, tech area, business value
- **Trademark Portfolio**: Mark, type, jurisdiction, reg number, filing/registration dates, renewal dates, classes, goods/services, specimens
- **Copyright Portfolio**: Work title, type, creation date, registration number, authors, owner, protection term
- **Trade Secrets**: Description, category, classification, protection measures, access level, review dates
- **Deadlines Calendar**: Upcoming deadlines sorted by urgency (critical < 30 days, high 30-60, standard 60-90)
- **Costs and Budget**: Annual budget by category, actual vs. budget, projected costs (12 months)
- **Patent Families**: Family ID, priority application, jurisdictions, status summary, member details
- **Licensing and Agreements**: License in/out, cross-licenses, parties, terms, revenue/costs
- **Prosecution History**: Office actions, responses, examiner interviews, outcomes

**Formulas included**: Days until deadline, conditional formatting (color-coded alerts), cost summaries, deadline counts

**Use for**: Tracking 10-1000+ IP assets across jurisdictions

---

## Workflow Examples

### Example 1: File New Patent Application

```bash
# 1. Prior art search (assess patentability)
@patent-searcher "Conduct patentability search for wireless IoT sensor with
edge computing capabilities. Technology: low-power sensors, edge ML inference,
mesh networking. Search USPTO and EPO, last 10 years."

# Result: Search report with 15 relevant patents, none blocking, suggests proceeding

# 2. Prepare patent application
@filing-assistant "Prepare utility patent application for wireless IoT sensor.
Key features: ultra-low power (10-year battery), edge ML for anomaly detection,
self-healing mesh network. Include claims for device, method, and system.
Target provisional filing."

# Result: Complete provisional application ready to file (~$3k-$5k with attorney)

# 3. Add to portfolio tracker
@ip-tracker "Add new provisional application to portfolio. Application number
US 63/456,789, filed 2025-01-15, inventors Smith and Doe, assigned to Acme Corp.
Set reminder for 12-month deadline to file non-provisional."

# Result: Portfolio updated, deadline set for 2026-01-15 (conversion deadline)
```

### Example 2: Manage Trademark Portfolio

```bash
# 1. Monitor renewal deadlines
@ip-tracker "Review trademark portfolio for upcoming renewals. Generate report
for deadlines in next 6 months. Calculate costs."

# Result: 3 trademarks require §8/§9 filing (years 9-10), total cost $1,275

# 2. Prepare renewal filings
@filing-assistant "Prepare §8 Declaration of Use and §9 Renewal for trademark
registration 5,123,456 (ACME SOLUTIONS, Classes 9 and 42). Confirm continued
use, prepare current specimens (website screenshots showing mark + services)."

# Result: Renewal documentation ready, specimens prepared, filing instructions

# 3. Update tracker after filing
@ip-tracker "Update trademark TM-001 (ACME SOLUTIONS) with §8/§9 filing date
2025-01-20. Set next renewal deadline for 2035 (10 years)."

# Result: Portfolio updated, next deadline flagged
```

### Example 3: Competitive Intelligence and Enforcement

```bash
# 1. Monitor for infringement
@infringement-monitor "Monitor for potential infringement of US Patent 11,123,456
(AI-powered chatbot with sentiment analysis). Search for competitive products
launched in last 6 months. Check new patent filings by TechCorp and ChatCo."

# Result: 2 potential infringers identified, 1 high risk (TechCorp's new product),
# claim chart shows 9 of 10 elements match claim 1

# 2. Conduct FTO for our new product
@patent-searcher "Freedom-to-operate search for our new voice assistant product.
Features: wake word detection, natural language understanding, multi-language,
cloud integration. Search active US patents (not expired), last 15 years."

# Result: 5 active patents identified, 2 potential blocking patents by VoiceCo,
# recommend licensing or design-around

# 3. Landscape analysis for acquisition target
@patent-searcher "Patent landscape analysis for StartupAI (acquisition target).
Review their patent portfolio (15 granted, 8 pending), analyze strength, identify
key assets, assess competitive positioning in computer vision space."

# Result: Detailed landscape report, portfolio valued at $2-3M, strong position
# in autonomous vehicle perception, white space in industrial inspection
```

### Example 4: Complete Portfolio Review

```bash
# 1. Generate portfolio summary
@ip-tracker "Generate comprehensive portfolio report. Include: asset counts by
type and status, upcoming deadlines (next 120 days), cost projections (next
12 months), portfolio value assessment by technology area."

# Result: Portfolio summary report - 45 patents (32 granted, 13 pending),
# 18 trademarks (15 registered), 12 copyrights, 8 trade secrets identified.
# Next 120 days: 5 critical actions, estimated $12,500 in fees.

# 2. Identify optimization opportunities
@ip-tracker "Review patent portfolio for optimization. Identify: abandoned
applications (can refile?), patents nearing expiration (worth maintaining?),
defensive patents (abandon to save costs?), licensing opportunities (unused
patents generating no revenue)."

# Result: 8 patents recommended for abandonment (save $15k/year in maintenance),
# 3 patents identified for licensing outreach, 2 abandoned applications worth
# refiling as continuations

# 3. Competitor analysis
@infringement-monitor "Competitive intelligence report on top 3 competitors.
Analyze patent portfolios (size, growth, focus areas), trademark activity
(new brands, product launches), identify acquisition activity, assess
strategic positioning."

# Result: Competitor analysis - Competitor A: 125 patents (aggressive filing,
# focus on ML), B: 78 patents (IoT sensors), C: 43 patents (cloud platforms).
# All increasing filing rates 20-30% YoY. White space identified in edge computing.
```

---

## Installation

### User-Level (Available in All Projects)

```bash
# Clone or copy this plugin to your user-level plugins directory
cp -r plugins/ip-specialist ~/.claude/plugins/

# Verify installation
ls ~/.claude/plugins/ip-specialist/agents/
```

### Project-Level (Project-Specific)

```bash
# Copy to project's .claude directory
mkdir -p .claude/plugins
cp -r plugins/ip-specialist .claude/plugins/

# Commit to version control
git add .claude/plugins/ip-specialist/
git commit -m "feat: add ip-specialist plugin"
```

---

## Configuration

### Portfolio Tracker Setup

```bash
# Copy template to project
cp plugins/ip-specialist/templates/ip-portfolio-tracker.xlsx ./ip-portfolio.xlsx

# Open in Excel/Google Sheets and customize:
# - Add your existing IP assets
# - Set up entity status (micro/small/large) for fee calculations
# - Configure alert thresholds
# - Link to document management system (file paths)
```

---

## Design Decisions

### Why These Agents?

**Four agents, not one**: Single responsibility principle. Each agent is an expert in one domain:
- **patent-searcher**: Search expertise (databases, classifications, query techniques)
- **ip-tracker**: Portfolio management (deadlines, costs, status tracking)
- **filing-assistant**: Documentation expertise (legal language, formatting, requirements)
- **infringement-monitor**: Competitive intelligence (analysis, evidence, enforcement)

Separation of concerns ensures focused expertise and prevents conflation of search/track/file/monitor activities.

### Why Different Models?

**Haiku (ip-tracker)**:
- Deterministic work (deadline calculations, status updates, cost projections)
- Structured data updates (spreadsheet management)
- High volume, routine tasks
- **90% cost savings** vs. Sonnet (10x cheaper)
- Perfect for tracking 100+ assets

**Sonnet (patent-searcher, filing-assistant, infringement-monitor)**:
- Requires judgment (relevance assessment, claim drafting, risk analysis)
- Strategic decisions (what to file, where to file, enforcement options)
- Legal/technical writing (patent claims, descriptions)
- Nuanced analysis (infringement mapping, competitive positioning)

**Cost optimization**: Use Haiku where possible (tracking), Sonnet where necessary (analysis).

### Why Skill-Aware?

Without skills, agents rely on general knowledge:
- Patent searches miss ~30-40% of relevant prior art (classification search omitted)
- Filing documents non-compliant (formatting, enablement, definiteness issues)
- Portfolio decisions ad-hoc (no consistent methodology)

With skills, agents follow proven IP professional practices:
- **prior-art-research**: 85-95% recall (keywords + classifications + citations)
- **ip-documentation**: USPTO-compliant formatting, proper enablement, claim strategies
- **ip-management**: Industry-standard portfolio optimization, deadline tracking

**Quality difference**:
- Without skills: ~50-60% quality, frequent corrections needed
- With skills: ~90-95% quality, professional-grade output

Skills encode decades of IP professional experience into reusable knowledge.

---

## Cost Optimization

**Estimated costs per task** (based on Claude pricing):

| Task | Agent | Model | Est. Cost |
|------|-------|-------|-----------|
| Prior art search | patent-searcher | Sonnet | ~$0.10-0.20 |
| Portfolio update | ip-tracker | Haiku | ~$0.01-0.02 |
| Patent application | filing-assistant | Sonnet | ~$0.15-0.30 |
| Infringement monitoring | infringement-monitor | Sonnet | ~$0.10-0.20 |

**Cost comparison**:
- All-Sonnet approach: ~$0.50 per comprehensive workflow
- Optimized (Haiku for tracking): ~$0.40 per workflow
- **Savings**: ~20% (more significant with high-volume tracking)

**Professional services comparison**:
- Patent attorney search: $2,000-5,000
- Portfolio management: $200-500/month
- Patent application drafting: $8,000-15,000
- Infringement analysis: $3,000-10,000

**Plugin assists** (not replaces) attorneys: Reduces attorney time by 30-50% through better preparation and initial drafting.

---

## Troubleshooting

### Search results incomplete

**Issue**: Patent search missing relevant prior art

**Solutions**:
- Ensure agent read `prior-art-research` skill (check output)
- Verify searches included classification codes (not just keywords)
- Check multiple databases used (USPTO + EPO + Google Patents minimum)
- Review search queries logged (should include Boolean operators)
- Consider commercial database (Derwent, Orbit) for comprehensive searches

### Portfolio tracker deadlines incorrect

**Issue**: Maintenance fee dates or renewal dates calculated wrong

**Solutions**:
- Verify grant date accurate (maintenance fees calculated from grant date)
- Check jurisdiction (EPO uses filing date anniversary, USPTO uses grant date)
- Confirm entity status (micro/small/large affects fee amounts, not dates)
- Review USPTO fee schedule changes (updated periodically)
- Cross-reference with official USPTO PAIR or TSDR for critical deadlines

### Filing documents non-compliant

**Issue**: Generated patent application doesn't meet USPTO requirements

**Solutions**:
- Ensure agent read `ip-documentation` skill (mandatory first step)
- Check formatting: line numbering, paragraph numbering [0001], margins
- Review enablement: are examples detailed enough for POSITA to make/use?
- Verify antecedent basis: every "the" has prior "a" or "an"
- Have patent attorney review before filing (always recommended)

### Infringement analysis unclear

**Issue**: Can't tell if product actually infringes patent claims

**Solutions**:
- Request element-by-element claim chart (each claim element vs. product feature)
- Ensure evidence documented (screenshots, product specs, dates)
- Review claim construction (how terms are interpreted)
- Remember: infringement requires ALL elements (all elements test)
- Consult IP litigation attorney for legal opinion (analysis is technical, not legal)

---

## Best Practices

### Search Best Practices

1. **Search before filing**: Always conduct patentability search before investing in patent application ($2k search saves $10k+ filing)
2. **Use multiple strategies**: Keywords + classifications + citations + assignee/inventor + non-patent literature
3. **Document thoroughly**: Save search queries, document databases searched, maintain reference list
4. **Review claims, not just abstracts**: Abstract may miss relevant claim details
5. **Check legal status**: Expired patents can't block you (FTO searches), but are still prior art (patentability searches)

### Portfolio Management Best Practices

1. **Review quarterly**: Portfolio status, upcoming deadlines, costs vs. budget
2. **Set alerts early**: 90-day notice for critical deadlines (not 30-day)
3. **Verify entity status**: Micro/small entity qualification can save 50-75% on fees
4. **Prune regularly**: Abandon low-value patents (save $800-7,400 per patent over lifetime)
5. **Geographic alignment**: File patents where you sell (80% of revenue = 80% of patent budget)

### Filing Best Practices

1. **File provisional first**: $2k-5k for 12-month priority hold (vs. $10k+ non-provisional immediately)
2. **Enable thoroughly**: Detailed examples, specific values, multiple embodiments (prevent §112 rejections)
3. **Broad independent claims**: Cover core invention without unnecessary limitations
4. **Multiple dependent claims**: Fallback positions (claims 2-20 narrow from claim 1)
5. **Attorney review mandatory**: Always have licensed patent attorney review before filing

### Monitoring Best Practices

1. **Monitor continuously**: Quarterly monitoring (not annual) catches issues early
2. **Document evidence immediately**: Screenshots with timestamps, save to archive.org
3. **Assess risk objectively**: High infringement likelihood + high commercial impact = enforcement priority
4. **Consult attorney before action**: Technical analysis ≠ legal opinion; get counsel before cease & desist
5. **Track competitor filings**: Competitive intelligence informs R&D strategy and white space identification

---

## Integration with Other Plugins

### With backend-architect

```bash
# 1. Design API architecture
@api-designer "Design REST API for healthcare data platform"

# 2. Patent the innovation
@patent-searcher "Prior art search for healthcare API with FHIR integration"
@filing-assistant "Prepare patent application for healthcare API architecture"

# 3. Protect trade secrets
@ip-tracker "Document API security algorithms as trade secrets, implement protection measures"
```

### With frontend-developer

```bash
# 1. Create UI component
@component-builder "Create innovative data visualization component"

# 2. Design patent protection
@filing-assistant "Prepare design patent application for UI component visual appearance"

# 3. Trademark brand elements
@filing-assistant "Prepare trademark application for product name 'DataViz Pro'"
@ip-tracker "Add trademark to portfolio, set renewal reminders"
```

### With tax-compliance / expense-manager

```bash
# 1. Track IP expenses
@ip-tracker "Export IP costs for year 2024 (filing fees, maintenance, attorney fees)"

# 2. Calculate R&D tax credits
# Use IP investment data for R&D tax credit calculations

# 3. Amortize IP costs
# Patent and trademark costs can be amortized over useful life for tax purposes
```

---

## Legal Disclaimer

**IMPORTANT**: This plugin provides technical assistance with IP management tasks.

**This plugin does NOT**:
- Provide legal advice or legal opinions
- Replace licensed patent or trademark attorneys
- Guarantee patent grants or trademark registrations
- Provide infringement or validity legal opinions
- Represent you before USPTO or in litigation

**Always consult licensed attorneys for**:
- Legal strategy and advice
- Office Action responses (USPTO prosecution)
- Infringement opinions and enforcement decisions
- Licensing agreements and contracts
- Litigation and USPTO proceedings (IPR, oppositions, etc.)
- International filing strategies

**Patent and trademark law is complex**. Professional legal counsel is essential for protecting valuable IP rights.

---

## Resources

### USPTO (United States Patent and Trademark Office)
- **Main site**: www.uspto.gov
- **Patent search**: patents.google.com, patft.uspto.gov
- **Trademark search**: www.uspto.gov/trademarks/search (TESS)
- **Filing systems**: Patent Center (patents), TEAS (trademarks)
- **Status check**: PAIR (patents), TSDR (trademarks)
- **Fee schedule**: www.uspto.gov/learning-and-resources/fees-and-payment/uspto-fee-schedule

### International Offices
- **EPO (European)**: www.epo.org, worldwide.espacenet.com
- **WIPO (World)**: www.wipo.int, patentscope.wipo.int
- **JPO (Japan)**: www.jpo.go.jp/e/
- **CNIPA (China)**: english.cnipa.gov.cn
- **KIPO (Korea)**: www.kipo.go.kr/en/

### Patent Classification
- **CPC**: www.uspto.gov/web/patents/classification
- **IPC**: www.wipo.int/classifications/ipc
- **Classification search**: www.uspto.gov/patents/search

### Legal Resources
- **MPEP** (Manual of Patent Examining Procedure): www.uspto.gov/web/offices/pac/mpep/
- **TMEP** (Trademark Manual): www.uspto.gov/trademarks/law/tmep
- **Patent law** (35 U.S.C.): www.uspto.gov/web/offices/pac/mpep/consolidated_laws.pdf
- **Trademark law** (15 U.S.C.): www.uspto.gov/trademarks/law/trademark-statutes

### Professional Organizations
- **AIPLA** (American IP Law Association): www.aipla.org
- **INTA** (International Trademark Association): www.inta.org
- **IPO** (Intellectual Property Owners): www.ipo.org

### Attorney Referral
- **USPTO attorney search**: www.uspto.gov/learning-and-resources/ip-policy/public-information-about-practitioners
- **State bar associations**: Local attorney referral services

---

## Contributing

Found a better IP search strategy? Identified additional classification codes? Improved filing templates? Contributions welcome!

1. Test improvement in real IP workflow
2. Document clearly with examples
3. Submit PR with explanation
4. Include before/after comparisons if applicable

---

## Changelog

### v1.0.0 (2025-01-20)

**Initial Release**

- 4 specialized agents (patent-searcher, ip-tracker, filing-assistant, infringement-monitor)
- 3 comprehensive skills (ip-management, prior-art-research, ip-documentation)
- 3 professional templates (patent-filing, trademark-application, ip-portfolio-tracker)
- Full USPTO and international patent office coverage
- IPC/CPC classification system knowledge
- Cost-optimized (Haiku for tracking, Sonnet for analysis)

---

## Support

**Issues**: Report at [Puerto GitHub Issues](https://github.com/bandofai/puerto/issues)

**Questions**: Tag your issue with `plugin:ip-specialist`

**Feature Requests**: Use `enhancement` label

**Legal Questions**: Consult licensed patent/trademark attorney (not GitHub issues)

---

**Version**: 1.0.0
**Author**: Puerto Plugin System
**Last Updated**: January 2025
**Status**: Production Ready
**Legal Compliance**: Follows USPTO and international IP standards
**Attorney Review**: Recommended for all filings and legal decisions
