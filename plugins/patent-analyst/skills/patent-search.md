# Patent Search Skill

Comprehensive patterns for patent database searching, prior art identification, and patent classification systems.

## Patent Database Overview

### Major Patent Databases

**USPTO (United States Patent and Trademark Office)**
- US patents and applications
- Full-text search from 1976
- Image search for older patents
- Public PAIR for status tracking
- PatFT (granted patents)
- AppFT (published applications)

**EPO (European Patent Office) - Espacenet**
- Global patent coverage (140+ million documents)
- Advanced search capabilities
- Patent family information
- Legal status tracking
- Machine translations

**WIPO (World Intellectual Property Organization) - PATENTSCOPE**
- International PCT applications
- National patents from 60+ offices
- Translated documents
- Sequence listings for biotech

**Google Patents**
- User-friendly interface
- Global coverage
- Prior art finder
- Citation analysis
- PDF downloads

## Patent Classification Systems

### CPC (Cooperative Patent Classification)

**Structure**:
```
Section (A-H, Y): Broadest level
Class: 2-digit number
Subclass: 1-3 letters
Group: Main group (1-3 digits)
Subgroup: Detail level (2+ digits after /)
```

**Example**: H04L 29/06
- H: Electricity
- 04: Electric communication technique
- L: Transmission of digital information
- 29: Arrangements, apparatus, circuits or systems
- 06: Characterized by protocol

**Common Sections**:
- A: Human Necessities
- B: Performing Operations, Transporting
- C: Chemistry, Metallurgy
- D: Textiles, Paper
- E: Fixed Constructions
- F: Mechanical Engineering, Lighting, Heating
- G: Physics
- H: Electricity
- Y: General tagging for new technologies

### IPC (International Patent Classification)

Similar structure to CPC, international standard
- Used by patent offices worldwide
- More general than CPC
- 70,000+ classification entries

### US Classification System (Legacy)

Historical system, replaced by CPC in 2015
- Still relevant for pre-2015 searches
- Class/Subclass structure
- More than 450 classes

## Boolean Search Strategies

### Basic Operators

**AND**: Narrow search (both terms required)
```
"machine learning" AND "drug discovery"
```

**OR**: Broaden search (either term)
```
"artificial intelligence" OR "machine learning" OR "neural network"
```

**NOT**: Exclude terms
```
"battery" NOT "lithium"
```

**NEAR**: Proximity search (terms within X words)
```
"quantum" NEAR3 "computing"  # Within 3 words
```

**SAME**: Same field/paragraph
```
"blockchain" SAME "supply chain"
```

### Advanced Search Techniques

**Phrase Search**:
```
"natural language processing"
```

**Wildcard Search**:
```
nano*  # nanotechnology, nanomaterial, nanoparticle
pharmac?  # pharmaceutic, pharmacology
```

**Truncation**:
```
comput$  # compute, computer, computing, computational
```

**Field-Specific Search**:
```
TTL=(machine learning)  # Title
ABST=(neural network)   # Abstract
CLMS=(classification)   # Claims
ISD=2020$              # Issue date 2020
AN=(IBM)               # Assignee
IN=(Smith)             # Inventor
```

## Search Strategy Development

### Step 1: Define Search Objective

**Types of Searches**:
1. **Novelty Search**: Is invention new?
2. **Validity Search**: Find prior art to challenge patent
3. **Freedom to Operate**: Will product infringe?
4. **State of the Art**: What exists in technology area?
5. **Competitor Intelligence**: What is competitor filing?

### Step 2: Identify Key Concepts

**Concept Mapping**:
```
Core Concept: Autonomous vehicles
  ├─ Related Terms: self-driving, driverless, automated driving
  ├─ Technical Components: LIDAR, sensors, computer vision
  ├─ Applications: passenger transport, delivery, trucking
  └─ Related Technologies: machine learning, GPS, obstacle detection
```

**Synonym Development**:
- Technical synonyms
- Acronyms and abbreviations
- Different language variations
- Historical terminology
- Emerging terminology

### Step 3: Select Classification Codes

**Finding Relevant Classes**:
1. Search for known relevant patents
2. Review their classification codes
3. Browse classification scheme
4. Use classification search tools
5. Check definition files

**Example Classification Research**:
```
Topic: Autonomous vehicles
Primary CPC: B60W 30/00 (Purposes of road vehicle drive control systems)
Secondary CPC: G05D 1/00 (Control of position/direction/altitude)
Related CPC: G06N (Computing arrangements based on specific models)
```

### Step 4: Construct Search Query

**Layered Approach**:

**Layer 1 - Broad Catch-All**:
```
CPC=(B60W30/* OR G05D1/*) AND ("autonomous" OR "self-driving" OR "driverless")
```

**Layer 2 - Technical Features**:
```
(LIDAR OR "laser radar" OR "light detection") AND (navigation OR "path planning")
```

**Layer 3 - Specific Innovations**:
```
("machine learning" OR "neural network") AND ("obstacle detection" OR "object recognition")
```

**Combined Query**:
```
(CPC=(B60W30/* OR G05D1/*) AND
  (("autonomous" OR "self-driving") AND
   (LIDAR OR "laser radar") AND
   ("obstacle detection" OR "path planning")))
NOT ("remote control" OR "toy vehicle")
ISD>=20150101  # Patents from 2015 onwards
```

## Database-Specific Search Syntax

### USPTO PatFT/AppFT

**Field Codes**:
```
TTL/        Title
ABST/       Abstract
ACLM/       Claims (all)
ICLM/       Independent claims
SPEC/       Specification (full text)
ISD/        Issue date
APD/        Application date
AN/         Assignee name
IN/         Inventor name
CCL/        Current CPC classification
ICL/        International classification
REF/        Referenced patents
```

**Example Search**:
```
TTL/("machine learning" OR "artificial intelligence") AND
CCL/(G06N3/08 OR G06N20/*) AND
ISD/20200101->20241231
```

### EPO Espacenet

**Advanced Search Fields**:
```
ti = Title
ab = Abstract
cl = Claims
pa = Applicant
in = Inventor
pn = Publication number
pd = Publication date
pr = Priority date
ic = IPC class
cpc = CPC class
```

**Example Search**:
```
(ti,ab)=(quantum computing) and
cpc=(G06N10/*) and
pd>=20200101
```

### WIPO PATENTSCOPE

**Search Fields**:
```
EN_TI:      English title
EN_AB:      English abstract
EN_CLMS:    English claims
IC:         IPC classification
CPC:        CPC classification
DP:         Publication date
PA:         Applicant
```

**Example Search**:
```
EN_TI:("CRISPR" OR "gene editing") AND
IC:C12N15/* AND
DP:[20200101 TO 20241231]
```

### Google Patents

**Operators**:
```
intitle:    In title
assignee:   Assignee name
inventor:   Inventor name
before:     Before date
after:      After date
```

**Example Search**:
```
intitle:blockchain assignee:IBM after:priority:20200101
```

## Prior Art Searching

### Patent Prior Art

**Citation Analysis**:
1. **Backward Citations**: Patents cited by target patent
2. **Forward Citations**: Patents citing target patent
3. **Patent Families**: Related applications worldwide

**Search Strategy**:
```
1. Identify key patents in technology area
2. Review all cited references
3. Analyze forward citations
4. Check patent families for variations
5. Review related applications by same inventors
```

### Non-Patent Literature (NPL)

**Sources**:
- Academic journals and papers
- Conference proceedings
- Technical standards
- Product documentation
- Technical blogs and websites
- GitHub repositories
- ArXiv preprints
- Dissertations and theses

**Search Platforms**:
- Google Scholar
- IEEE Xplore
- ACM Digital Library
- PubMed (medical/biotech)
- ArXiv (preprints)
- Technical documentation sites

### Search Documentation

**Record Keeping**:
```markdown
# Search Log

**Date**: 2025-02-15
**Searcher**: [Name]
**Objective**: Novelty search for AI-powered drug discovery

## Search Strategy

### Databases Searched
- USPTO PatFT: 2015-2024
- EPO Espacenet: Global coverage
- Google Patents: Validation

### Keywords
Primary: "drug discovery", "artificial intelligence", "machine learning"
Secondary: "pharmaceutical", "compound screening", "molecule generation"
Synonyms: "medicinal chemistry", "lead optimization", "QSAR"

### Classification Codes
- G16C 20/70 (Molecular design, e.g. drug design)
- G06N 3/08 (Neural networks)
- G16H 70/40 (ICT for drug development)

### Search Queries

Query 1 (USPTO):
TTL/(("drug discovery" OR "pharmaceutical") AND
     ("artificial intelligence" OR "machine learning")) AND
CCL/(G16C20/* OR G06N3/08)
Results: 145 patents

Query 2 (EPO):
(ti,ab)=("AI" AND "drug" AND "discovery") AND
cpc=(G16C20/70 OR G06N*)
Results: 287 patents

[Continue with additional queries...]

## Results Summary
- Total patents found: 432
- Relevant patents: 67
- Highly relevant: 12
- Key competitors: Pfizer (15), Novartis (8), IBM (6)
```

## Search Quality Indicators

### Completeness Checklist

- [ ] Multiple databases searched (minimum 2-3)
- [ ] Appropriate classification codes used
- [ ] Comprehensive keyword variations included
- [ ] Date range appropriate for technology
- [ ] Forward and backward citations checked
- [ ] Patent families reviewed
- [ ] Non-patent literature searched
- [ ] Competitor patents reviewed
- [ ] Search documented with queries
- [ ] Results properly categorized

### Relevance Ranking

**High Relevance**:
- Directly covers claimed invention
- Same technical field
- Same technical problem solved
- Similar technical solution

**Medium Relevance**:
- Related technical field
- Similar problem, different solution
- Different problem, similar solution
- Relevant background technology

**Low Relevance**:
- Different technical field
- Tangentially related
- Background only
- Different application domain

## Common Search Pitfalls

**Avoid**:
1. **Too narrow**: Missing relevant prior art
   - Solution: Use OR operators, synonyms, wildcards

2. **Too broad**: Overwhelming irrelevant results
   - Solution: Add technical specifics, classification codes

3. **Wrong classification**: Missing key patents
   - Solution: Research classifications thoroughly

4. **Date limitations**: Missing relevant prior art
   - Solution: Search full patent database history

5. **Language barriers**: Missing foreign patents
   - Solution: Use international databases, machine translation

6. **Missing NPL**: Incomplete prior art
   - Solution: Search academic and technical literature

7. **Ignoring patent families**: Missing related disclosures
   - Solution: Review all family members

8. **Poor documentation**: Search not reproducible
   - Solution: Document all queries, databases, dates

## Search Output Format

### Search Report Structure

```markdown
# Patent Search Report

## Executive Summary
- Search objective
- Key findings
- Relevant patents identified
- Prior art assessment

## Search Methodology
### Databases
- USPTO: [Date range]
- EPO: [Date range]
- WIPO: [Date range]
- Google Patents: [Date range]

### Search Strategy
- Keywords and synonyms
- Classification codes
- Boolean operators used
- Search iterations

## Results

### Highly Relevant Patents
1. [Patent Number] - [Title]
   - Assignee: [Company]
   - Filing Date: [Date]
   - Relevance: [Why relevant]
   - Key Claims: [Summary]

### Patent Landscape
- Total patents found: X
- Relevant patents: Y
- Date range: [Earliest-Latest]
- Key assignees: [List]
- Technology trends: [Analysis]

## Prior Art Analysis
- Blocking patents identified
- Related technologies
- White space opportunities
- Recommendation

## Appendix
- Complete search queries
- Full patent list
- Classification definitions
```

## Best Practices

### Iterative Searching
1. Start broad, then narrow
2. Review initial results
3. Identify new keywords from relevant patents
4. Adjust classification codes
5. Refine and repeat

### Quality Over Quantity
- Focus on highly relevant results
- Document why patents are relevant
- Rank by importance to objective
- Don't be distracted by volume

### Stay Current
- Set up alerts for new publications
- Monitor key competitors
- Track technology trends
- Review recent filings regularly

### Collaboration
- Discuss findings with technical experts
- Validate relevance with inventors
- Get legal review for critical searches
- Share search strategies with team
