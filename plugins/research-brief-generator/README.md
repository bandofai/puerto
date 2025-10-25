# Research Brief Generator

**Professional research brief generation with multi-source data gathering, comparative analysis, and decision frameworks.**

Automates comprehensive research projects from planning through final deliverable generation, producing executive-ready reports with proper citations and data-driven recommendations.

---

## Overview

The Research Brief Generator transforms complex research tasks into systematic, multi-agent workflows that deliver professional-quality research briefs. Whether you're comparing products, evaluating technologies, assessing vendors, or conducting strategic analysis, this plugin provides the frameworks and agents to conduct thorough, objective research that drives confident decision-making.

### What This Plugin Does

- **Research Planning**: Defines scope, methodology, evaluation criteria, and sources
- **Multi-Source Data Collection**: Gathers information from official docs, expert reviews, user feedback using WebFetch
- **Comparative Analysis**: Creates comparison matrices, SWOT analyses, pros/cons, weighted scoring
- **Decision Support**: Applies decision frameworks to generate data-driven recommendations
- **Professional Reports**: Produces executive-ready research briefs with full citations
- **Source Attribution**: Maintains complete bibliography with credibility assessment

### Key Features

- **4 Specialized Agents**: research-planner, data-gatherer, comparative-analyzer, brief-writer
- **Comprehensive Skill**: research-methodology with proven frameworks and best practices
- **Template Library**: Research plans, comparison matrices, and brief templates
- **Multiple Frameworks**: SWOT, weighted scoring, cost-benefit, decision matrices, PESTLE
- **Citation Standards**: Proper source attribution and bibliography generation
- **WebFetch Integration**: Automated web research and data extraction
- **Quality Standards**: Objectivity, completeness, transparency, evidence-based analysis

---

## Use Cases

### Product/Service Comparison

**Scenario**: Choose between 3-5 competing products or services

**Example**: "Compare Salesforce, HubSpot, and Pipedrive CRMs for a 50-person sales team"

**Deliverables**:
- Feature comparison matrix
- Pricing comparison and TCO analysis
- Pros/cons for each option
- User review sentiment analysis
- Weighted scoring with recommendation

---

### Technology Evaluation

**Scenario**: Assess technical solutions or architectures

**Example**: "Evaluate cloud hosting platforms (AWS, Azure, GCP) for our application"

**Deliverables**:
- Technical capability comparison
- Architecture assessment
- Performance benchmarks
- Security and compliance analysis
- Total cost of ownership
- Implementation complexity

---

### Vendor Selection

**Scenario**: Choose service providers or partners

**Example**: "Select a managed security services provider for our enterprise"

**Deliverables**:
- Vendor comparison matrix
- Service offering analysis
- Company stability assessment
- Client reference insights
- Risk assessment
- Contract comparison

---

### Market Research

**Scenario**: Understand market landscape and opportunities

**Example**: "Analyze the conversational AI market to identify partnership opportunities"

**Deliverables**:
- Market overview and size
- Competitive landscape
- Trend analysis
- Customer segment analysis
- Strategic recommendations

---

### Strategic Decisions

**Scenario**: High-level strategic choices

**Example**: "Should we build, buy, or partner for our analytics capability?"

**Deliverables**:
- PESTLE analysis
- SWOT for each option
- Risk assessment
- Scenario analysis
- Strategic recommendation

---

## Plugin Structure

```
research-brief-generator/
├── .claude-plugin/
│   └── plugin.json                    # Plugin metadata
├── agents/
│   ├── research-planner.md            # Defines research scope and methodology
│   ├── data-gatherer.md               # Multi-source data collection with WebFetch
│   ├── comparative-analyzer.md        # Analysis and comparison frameworks
│   └── brief-writer.md                # Professional report generation
├── skills/
│   └── research-methodology/
│       └── SKILL.md                   # Comprehensive research frameworks and best practices
├── templates/
│   ├── research-plan-template.json    # Research planning structure
│   ├── comparison-matrix-template.json # Feature comparison format
│   └── research-brief-template.md     # Final report template
├── data/                              # Sample data (user-created during research)
└── README.md                          # This file
```

---

## Agents

### 1. research-planner

**Model**: Sonnet
**Tools**: Read, Write, Grep, Glob

**Purpose**: Strategic research design and planning

**Responsibilities**:
- Clarify research objectives and decision context
- Define scope (in-scope, out-of-scope, constraints)
- Select appropriate research frameworks (SWOT, weighted scoring, etc.)
- Identify information sources for each alternative
- Establish evaluation criteria with weights
- Design decision-making methodology
- Create structured research plan document

**When to Use**: First step of any research project to establish foundation

**Output**: Comprehensive research plan saved to `~/.claude/research-projects/[id]/research-plan.json`

---

### 2. data-gatherer

**Model**: Sonnet
**Tools**: Read, Write, WebFetch, Grep, Glob

**Purpose**: Multi-source data collection specialist

**Responsibilities**:
- Load research plan and extract requirements
- Systematically fetch data from identified sources using WebFetch
- Collect official documentation, technical specs, pricing
- Gather expert reviews and user feedback
- Extract relevant information for each evaluation criterion
- Assess source credibility and currency
- Handle conflicting information appropriately
- Document data gaps and quality
- Create structured data files with proper citations
- Generate complete bibliography

**When to Use**: After research plan is complete, to gather all needed data

**Output**: Structured data files in `data/structured/`, raw data in `data/raw/`, bibliography in `sources/`

---

### 3. comparative-analyzer

**Model**: Sonnet
**Tools**: Read, Write, Grep, Glob

**Purpose**: Deep comparative analysis and framework application

**Responsibilities**:
- Create side-by-side feature comparison matrices
- Perform detailed pros/cons analysis for each alternative
- Apply weighted scoring methodology
- Conduct SWOT analysis
- Build decision matrices
- Perform cost-benefit analysis
- Generate scenario analyses
- Identify key insights and trade-offs
- Synthesize findings into actionable comparisons

**When to Use**: After data collection, to analyze and compare alternatives

**Output**: Analysis files in `analysis/` - comparison matrices, pros/cons, scoring, SWOT, decision matrix

---

### 4. brief-writer

**Model**: Sonnet
**Tools**: Read, Write, Grep, Glob

**Purpose**: Professional research brief generation

**Responsibilities**:
- Synthesize all research and analysis into coherent narrative
- Write executive summary (1-page decision document)
- Create comprehensive research brief
- Generate one-page summary for quick reference
- Prepare presentation-ready slides
- Ensure proper citations throughout
- Maintain professional tone and formatting
- Make complex information accessible
- Provide clear, justified recommendations
- Include implementation guidance

**When to Use**: Final step after analysis is complete

**Output**: Multiple brief formats in `brief/` - full brief, one-pager, presentation slides

---

## Research Methodology Skill

The `research-methodology` skill is the knowledge foundation for all agents, containing:

### Part 1: Research Design & Planning
- SMART research objectives
- Scoping frameworks
- Methodology selection

### Part 2: Source Evaluation & Data Collection
- Credibility hierarchy (Tier 1-4 sources)
- CRAAP test (Currency, Relevance, Authority, Accuracy, Purpose)
- Multi-source triangulation
- Handling conflicting information

### Part 3: Comparative Analysis Frameworks
- Feature comparison matrices
- SWOT analysis
- Weighted decision matrices
- Pros/cons analysis
- Cost-benefit analysis
- Risk assessment

### Part 4: Decision-Making Frameworks
- Must-have / nice-to-have categorization
- Elimination decision processes
- Scenario-based decision making
- Confidence assessment

### Part 5: Citation & Attribution Standards
- Citation formats
- Quote attribution
- Bibliography standards

### Part 6: Research Quality Standards
- Objectivity principles
- Completeness standards
- Accuracy requirements
- Transparency standards

### Part 7: Professional Report Writing
- Executive summary principles
- Narrative flow
- Clarity and accessibility
- Visual communication

### Part 8: Common Research Frameworks
- PESTLE analysis
- Porter's Five Forces
- Pugh Matrix
- Additional frameworks

### Part 9: Research Ethics & Best Practices
- Ethical principles
- Avoiding common cognitive biases
- Quality checklist

---

## Workflow

### Standard Research Project Workflow

```
1. @research-planner
   ↓ Creates research plan
   ↓ Defines scope, criteria, sources
   ↓ Saves: research-plan.json

2. @data-gatherer
   ↓ Loads research plan
   ↓ Fetches data from sources (WebFetch)
   ↓ Structures data for analysis
   ↓ Saves: data/structured/*, sources/bibliography.md

3. @comparative-analyzer
   ↓ Loads research plan + data
   ↓ Creates comparison matrices
   ↓ Performs SWOT, pros/cons, scoring
   ↓ Applies decision framework
   ↓ Saves: analysis/* (matrices, scoring, SWOT)

4. @brief-writer
   ↓ Loads plan + data + analysis
   ↓ Synthesizes into narrative
   ↓ Writes executive summary
   ↓ Creates full research brief
   ↓ Saves: brief/* (full, one-page, presentation)

5. Final Deliverable
   ↓ Professional research brief
   ↓ Clear recommendation
   ↓ Supporting evidence
   ↓ Full citations
```

### Agent Invocation Pattern

**Option 1: Sequential Manual Invocation**
```
@research-planner I need to compare CRM platforms for our sales team
[Wait for plan]

@data-gatherer Execute data gathering for research-[id]
[Wait for data collection]

@comparative-analyzer Analyze data for research-[id]
[Wait for analysis]

@brief-writer Generate research brief for research-[id]
[Receive final brief]
```

**Option 2: Orchestrated Workflow**
```
@orchestrator-planner I need to compare CRM platforms. Create a plan using:
- research-planner for scope
- data-gatherer for data
- comparative-analyzer for analysis
- brief-writer for final brief
```

---

## Getting Started

### Installation

1. **Clone or download** this plugin to your Claude Code plugins directory:
   ```bash
   # User-level (recommended)
   ~/.claude/plugins/research-brief-generator/

   # Or project-level
   .claude/plugins/research-brief-generator/
   ```

2. **Verify structure**:
   ```bash
   research-brief-generator/
   ├── .claude-plugin/plugin.json
   ├── agents/
   ├── skills/research-methodology/
   └── templates/
   ```

3. **Restart Claude Code** or reload plugins

### Quick Start Example

**Simple Product Comparison**:

```
@research-planner I need to compare Notion, Coda, and Airtable for our team's project management needs. Key criteria: ease of use, collaboration features, pricing, and integrations. Budget is $500/month max.
```

The research-planner will create a structured plan, then guide you through the workflow with the other agents.

---

## Usage Examples

### Example 1: E-commerce Platform Comparison

**Goal**: Choose between Shopify, WooCommerce, and BigCommerce for new online store

**Workflow**:

1. **Planning**:
```
@research-planner Compare Shopify, WooCommerce, and BigCommerce for launching an online apparel store with 200 SKUs. Key criteria: ease of use, payment options, inventory management, mobile experience, SEO, pricing (budget $300/month), and scalability to 10k monthly orders.
```

2. **Data Collection**:
```
@data-gatherer Execute data gathering for research-20250115-143022. Focus on official feature lists, pricing tiers, user reviews from Trustpilot and G2, and expert reviews from ecommerce blogs.
```

3. **Analysis**:
```
@comparative-analyzer Analyze data for research-20250115-143022. Create feature matrix, pros/cons, weighted scoring using criteria from plan, and cost-benefit analysis including transaction fees.
```

4. **Brief Generation**:
```
@brief-writer Generate comprehensive research brief for research-20250115-143022. Include one-page summary and presentation slides for stakeholder review.
```

**Result**: Professional brief with recommendation, implementation roadmap, and full justification.

---

### Example 2: Cloud Infrastructure Decision

**Goal**: Evaluate AWS, Azure, and GCP for hosting a SaaS application

**Workflow**:

1. **Planning**:
```
@research-planner Evaluate AWS, Azure, and Google Cloud Platform for hosting our multi-tenant SaaS application. Requirements: Kubernetes support, global availability, strong security/compliance (SOC2, GDPR), scalability to 100k users, managed database options. Key criteria: technical capabilities, pricing/TCO, support quality, vendor lock-in risk, and integration with our existing tools.
```

2. **Data Collection**:
```
@data-gatherer Collect data for research-[id]. Sources: official documentation for each platform, TechCrunch/Ars Technica reviews, G2 reviews from DevOps teams, technical comparison sites, and TCO calculators.
```

3. **Analysis**:
```
@comparative-analyzer Analyze cloud platforms for research-[id]. Create technical capability matrix, TCO analysis over 3 years, SWOT for each platform, and scenario analysis for different growth trajectories.
```

4. **Brief Generation**:
```
@brief-writer Create research brief for research-[id]. Target audience: CTO and engineering leadership. Include technical appendix with architecture considerations.
```

---

### Example 3: Marketing Automation Tool Selection

**Goal**: Select between HubSpot, Marketo, and ActiveCampaign

**Workflow**:

1. **Single Orchestrated Request**:
```
@orchestrator-planner Create and execute a research project to select a marketing automation platform. Alternatives: HubSpot, Marketo, ActiveCampaign. Use research-planner for methodology, data-gatherer for source collection, comparative-analyzer for analysis, and brief-writer for final deliverable. Key criteria: email automation, lead scoring, CRM integration, analytics, ease of use, and pricing for 5,000 contacts.
```

The orchestrator will coordinate all four agents sequentially and deliver the final brief.

---

## Templates

### Research Plan Template

**File**: `templates/research-plan-template.json`

Comprehensive structure for research planning including:
- Research objective and context
- Alternatives with initial notes
- Scope definition (in/out, constraints)
- Methodology and frameworks
- Source strategy by alternative
- Evaluation criteria with weights
- Decision framework
- Deliverables checklist
- Timeline and success criteria

**Usage**: Referenced by research-planner agent; customize for your domain

---

### Comparison Matrix Template

**File**: `templates/comparison-matrix-template.json`

Structure for feature-by-feature comparison:
- Alternative metadata
- Comparison categories with weights
- Feature-level details with status symbols
- Winner identification per feature
- Analysis and insights
- Unique capabilities and gaps
- Visualization guidance

**Usage**: Referenced by comparative-analyzer; guides matrix creation

---

### Research Brief Template

**File**: `templates/research-brief-template.md`

Professional report structure:
- Executive summary (1-page)
- Objective and scope
- Methodology
- Alternatives overview
- Comparative analysis
- Key findings and insights
- Recommendation with rationale
- Implementation considerations
- Appendices (scoring, SWOT, bibliography)

**Usage**: Referenced by brief-writer; ensures consistent formatting

---

## Configuration & Customization

### Customizing Evaluation Criteria

Edit the research plan template to add domain-specific criteria:

```json
{
  "category": "Your Category",
  "weight": 0.15,
  "criteria": [
    {
      "name": "Your specific criterion",
      "weight": 0.10,
      "description": "What this measures",
      "scale": "1-5 or custom",
      "type": "must-have|important|nice-to-have"
    }
  ]
}
```

### Adding Research Frameworks

Extend the research-methodology skill with domain-specific frameworks:

1. Add new section to `skills/research-methodology/SKILL.md`
2. Document when to use the framework
3. Provide template/structure
4. Include example application

### Customizing Source Strategy

In research plan, specify domain-specific sources:

```json
{
  "sources": {
    "by_alternative": {
      "alt1": {
        "official_sources": ["Your domain-specific official sources"],
        "review_sources": ["Industry-specific review platforms"],
        "technical_sources": ["Domain technical resources"]
      }
    }
  }
}
```

---

## Best Practices

### For Research Planning

1. **Be Specific**: "Compare CRMs for 50-person sales team" not "Research CRMs"
2. **Define Constraints**: Budget, timeline, must-have requirements
3. **Weight Appropriately**: Most important criteria should have highest weights
4. **Distinguish Must-Haves**: Separate deal-breakers from nice-to-haves

### For Data Collection

1. **Multiple Sources**: Use official + expert + user perspectives
2. **Verify Credibility**: Apply CRAAP test to sources
3. **Note Currency**: Data age matters, especially for technology
4. **Document Gaps**: Explicitly note missing information
5. **Cite Everything**: URL and date for all claims

### For Analysis

1. **Apply Consistently**: Same criteria to all alternatives
2. **Show Your Work**: Document scoring rationale
3. **Acknowledge Trade-offs**: No perfect choice; be honest about compromises
4. **Stay Objective**: Let data drive conclusions, not preferences
5. **Test Sensitivity**: Ensure recommendation is robust to weight changes

### For Brief Writing

1. **Lead with Recommendation**: Executive summary should enable decision
2. **Support with Evidence**: Every claim needs a citation
3. **Write Clearly**: Assume intelligent but non-expert reader
4. **Be Comprehensive**: Cover all alternatives fairly
5. **Provide Action Steps**: What to do next

---

## Data Management

### Research Project Structure

Each research project creates:

```
~/.claude/research-projects/research-YYYYMMDD-HHMMSS/
├── research-plan.json              # Research plan
├── data/
│   ├── raw/                        # Raw data from sources
│   │   ├── alt1-official.json
│   │   ├── alt1-reviews.json
│   │   └── ...
│   └── structured/                 # Structured summaries
│       ├── alt1-summary.json
│       ├── alt2-summary.json
│       └── ...
├── sources/
│   └── bibliography.md             # Complete bibliography
├── analysis/
│   ├── comparison-matrix.md        # Feature comparison
│   ├── pros-cons.md                # Strengths/weaknesses
│   ├── weighted-scores.md          # Scoring analysis
│   ├── swot.md                     # SWOT analysis
│   ├── decision-matrix.md          # Decision framework
│   ├── cost-benefit.md             # TCO/ROI (if applicable)
│   └── SUMMARY.md                  # Analysis summary
└── brief/
    ├── research-brief-full.md      # Comprehensive brief
    ├── research-brief-1-page.md    # Executive summary
    ├── research-brief-presentation.md # Slide deck
    └── brief-metadata.json         # Brief metadata
```

### Accessing Research Data

**List all research projects**:
```bash
ls -lt ~/.claude/research-projects/
```

**View a research plan**:
```bash
cat ~/.claude/research-projects/research-20250115-143022/research-plan.json
```

**Read the final brief**:
```bash
cat ~/.claude/research-projects/research-20250115-143022/brief/research-brief-full.md
```

### Exporting Research

**Copy brief for sharing**:
```bash
cp ~/.claude/research-projects/research-[id]/brief/research-brief-full.md ~/Desktop/
```

**Archive completed research**:
```bash
tar -czf research-[id].tar.gz ~/.claude/research-projects/research-[id]/
```

---

## Advanced Usage

### Custom Decision Frameworks

Beyond weighted scoring, implement custom frameworks:

**RICE Prioritization** (Reach, Impact, Confidence, Effort):
1. Modify research plan to include RICE criteria
2. Update comparative-analyzer to calculate RICE scores
3. Brief-writer presents RICE-based recommendation

**Kano Model** (Must-be, One-dimensional, Attractive):
1. Categorize features by Kano model
2. Analyze user satisfaction impact
3. Recommend based on maximum satisfaction

### Multi-Stage Research

For complex decisions, conduct research in stages:

**Stage 1: Broad Scan**
- Research 5-10 alternatives
- Lightweight analysis
- Eliminate clearly unsuitable options

**Stage 2: Deep Dive**
- Research top 3 from Stage 1
- Comprehensive analysis
- Final recommendation

### Periodic Re-Research

Markets evolve; revisit decisions:

**Annual Review**:
```
@research-planner Review our 2024 CRM selection. Re-evaluate Salesforce vs current alternatives given our growth to 100 people. Has the landscape changed?
```

### Integration with Decision-Making Processes

**RFP Response**:
Use comparative-analyzer output to create RFP comparison matrices

**Board Presentations**:
Use brief-writer presentation format for board decks

**Procurement**:
Use TCO analysis and decision matrix for procurement justification

---

## Troubleshooting

### Issue: WebFetch Fails for Source

**Solution**:
- Check URL is accessible
- Try alternative sources
- Document unavailability in data gaps
- Proceed with available sources

### Issue: Conflicting Data Between Sources

**Solution**:
- Note conflict explicitly in data collection
- Assess source credibility (prefer Tier 1)
- Seek additional sources as tiebreaker
- Document uncertainty in analysis

### Issue: Unclear Recommendation (Close Scores)

**Solution**:
- Perform sensitivity analysis
- Consider scenario-based recommendations
- Suggest pilot/POC for top options
- Acknowledge uncertainty honestly
- Provide decision criteria for choosing

### Issue: Data Gaps for Key Criteria

**Solution**:
- Document gap explicitly
- Note impact on decision confidence
- Recommend how to fill gap (vendor demo, trial, etc.)
- Proceed with available data if gap is acceptable
- Lower confidence rating appropriately

---

## Tips for Quality Research

### 1. Start with Clear Objectives

Bad: "Research project management tools"
Good: "Compare Asana, Monday.com, and ClickUp for a 20-person product team managing 5 concurrent projects, with focus on Gantt charts, time tracking, and budget under $400/month"

### 2. Use Multiple Source Types

- ✅ Official docs + Expert reviews + User reviews
- ❌ Only official marketing materials

### 3. Balance Criteria Weights

- ✅ Top 3 criteria = 60-70% of weight
- ❌ All criteria weighted equally (undermines prioritization)

### 4. Document Your Reasoning

- ✅ "Scored 4/5 because [evidence] from [source]"
- ❌ "4/5" with no justification

### 5. Acknowledge Limitations

- ✅ "Limited long-term reliability data; product launched 3 months ago"
- ❌ Ignore gaps and uncertainties

### 6. Stay Objective

- ✅ Present all alternatives fairly
- ❌ Cherry-pick data to support preferred option

### 7. Make Recommendations Actionable

- ✅ "Choose Shopify. Next steps: 1) Start 14-day trial, 2) Configure payment gateway, 3) Import 50 SKUs as test"
- ❌ "Shopify is probably best"

---

## Integration with Other Plugins

### Orchestrator Plugin

Use orchestrator-planner to coordinate the full research workflow:

```
@orchestrator-planner Execute complete research project comparing [alternatives] using research-brief-generator agents
```

### Skill Library

Research methodology skill is referenced by:
- Other analysis-focused agents
- Strategic planning agents
- Decision support systems

---

## Version History

**Version 1.0** (2025-01)
- Initial release
- 4 agents: research-planner, data-gatherer, comparative-analyzer, brief-writer
- Comprehensive research-methodology skill
- 3 templates: research plan, comparison matrix, research brief
- Multiple decision frameworks (SWOT, weighted scoring, cost-benefit)
- WebFetch integration for multi-source data collection
- Citation and bibliography standards

---

## Roadmap

**Planned Enhancements**:
- Additional research frameworks (RICE, Kano, AHP)
- Industry-specific templates (SaaS comparison, hardware evaluation)
- Quantitative analysis extensions (statistical significance)
- Visualization generation (charts, graphs)
- PDF export capability
- Integration with external data sources (APIs)

---

## Contributing

To contribute improvements:

1. **Add domain-specific criteria**: Edit templates with your industry's key factors
2. **Extend frameworks**: Add new analysis methods to research-methodology skill
3. **Improve templates**: Enhance brief structure for specific use cases
4. **Share best practices**: Document lessons learned in your domain

---

## Support & Feedback

For issues, questions, or suggestions:
- Review existing research projects for examples
- Consult research-methodology skill for frameworks
- Check troubleshooting section above

---

## License

MIT License - See plugin.json for details

---

## Acknowledgments

**Research Frameworks**: Based on established methodologies from:
- Academic research best practices
- Management consulting frameworks (McKinsey, BCG, Bain)
- Technology analyst approaches (Gartner, Forrester)
- Evidence-based decision-making literature

**Design Philosophy**: Skill-aware agents that leverage comprehensive frameworks for consistent, high-quality research output.

---

## Quick Reference

**Typical Research Project Timeline**:
- Planning: 30-60 minutes
- Data Collection: 2-4 hours (depends on alternatives and sources)
- Analysis: 1-2 hours
- Brief Writing: 1 hour
- **Total**: Half day to full day for comprehensive research

**When to Use This Plugin**:
- ✅ Comparing 2+ alternatives (products, services, vendors)
- ✅ Making decisions with $10k+ impact
- ✅ Strategic choices requiring stakeholder buy-in
- ✅ Situations needing documented justification
- ❌ Simple/obvious decisions
- ❌ Single-option validation (use other analysis tools)

**Key Success Factors**:
1. Clear objectives and constraints
2. Multiple credible sources per alternative
3. Appropriate criteria with weights
4. Objective, evidence-based analysis
5. Honest acknowledgment of limitations
6. Actionable recommendations

---

**Research Brief Generator** - Turning complex decisions into clear, confident choices through systematic research and analysis.
