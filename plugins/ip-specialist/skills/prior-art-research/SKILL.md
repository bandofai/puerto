# Prior Art Research Skill

**Version**: 1.0.0
**Last Updated**: January 2025
**Purpose**: Comprehensive search strategies, patent classification systems, and database techniques for conducting thorough prior art searches and patent landscape analysis.

---

## Table of Contents

1. [Search Fundamentals](#search-fundamentals)
2. [Patent Classification Systems](#patent-classification-systems)
3. [Search Databases](#search-databases)
4. [Search Strategies](#search-strategies)
5. [Boolean and Field Searches](#boolean-and-field-searches)
6. [Citation Analysis](#citation-analysis)
7. [Non-Patent Literature](#non-patent-literature)
8. [Search Documentation](#search-documentation)

---

## Search Fundamentals

### Purpose of Prior Art Searches

**1. Patentability Search** (Before Filing)
- **Goal**: Assess novelty and non-obviousness of invention
- **Scope**: Broad, all relevant prior art
- **Depth**: Comprehensive (minimize risk of missing key references)
- **Outcome**: File/don't file decision, claim strategy

**2. Freedom-to-Operate (FTO) Search**
- **Goal**: Identify active patents that product may infringe
- **Scope**: Narrow, focused on product features
- **Depth**: Active patents only (not expired or pending)
- **Outcome**: Design-around, license, or launch decisions

**3. Invalidity Search**
- **Goal**: Find prior art to invalidate specific patent
- **Scope**: Extremely deep, all possible prior art sources
- **Depth**: Must find references patent examiner missed
- **Outcome**: Inter partes review, litigation defense, licensing leverage

**4. Landscape/State-of-the-Art Search**
- **Goal**: Understand technology domain and competitive positions
- **Scope**: Broad technology area, multiple years
- **Depth**: Patterns and trends, not individual claims
- **Outcome**: R&D strategy, white space identification, M&A targets

### Defining Search Scope

**Technology Understanding**:
1. **Core Innovation**: What is novel? What problem does it solve?
2. **Key Features**: Essential elements vs. optional variations
3. **Technical Field**: Primary technology area(s)
4. **Adjacent Technologies**: Related or enabling technologies
5. **Terminology**: Technical terms, synonyms, industry jargon

**Search Parameters**:

- **Time Period**:
  - Patentability: All time (but focus on last 20 years)
  - FTO: Active patents only (filed within last 20 years, not expired)
  - Landscape: Last 5-10 years for trends

- **Geographic Scope**:
  - US-only: USPTO databases
  - Worldwide: WIPO, EPO, Google Patents
  - Competitor jurisdictions: Where competitors file

- **Language**:
  - English: Most accessible
  - Machine translation: EPO, WIPO provide (quality varies)
  - Original language: May be necessary for nuanced searching

**Completeness vs. Cost Trade-off**:

- **Quick Search** (1-2 hours): Keyword search, top 20-30 results
  - Purpose: Initial assessment, early-stage decisions
  - Risk: May miss key references

- **Standard Search** (4-8 hours): Keywords + classifications + citations
  - Purpose: Patentability assessment, typical practice
  - Coverage: ~80-90% of relevant prior art

- **Comprehensive Search** (20-40 hours): All strategies, non-patent literature, foreign databases
  - Purpose: Invalidity search, high-stakes decisions
  - Coverage: 95%+ (no search is 100%)

### Prior Art Types

**Patent Prior Art**:
- **Utility Patents**: Most common, 20-year term
- **Design Patents**: Ornamental designs
- **Published Applications**: Not granted, but still prior art
- **Abandoned Applications**: May be prior art if published
- **Foreign Patents**: Count as prior art (worldwide novelty)

**Non-Patent Prior Art**:
- **Academic Papers**: Journal articles, conference proceedings
- **Books and Textbooks**: Technical manuals
- **Theses/Dissertations**: University research
- **Standards Documents**: IEEE, ISO, ANSI standards
- **Product Catalogs**: Commercial products (dated)
- **Websites**: Internet Archive (dated screenshots)
- **Trade Publications**: Industry magazines
- **Trade Shows**: Exhibition catalogs, demonstrations (dated)
- **Open Source**: Public code repositories (GitHub, SourceForge)

**Prior Art Dates**:

- **Effective Date**: When prior art becomes relevant
  - Patents: Filing date (or priority date)
  - Publications: Publication date
  - Sales/offers: Date of sale/offer
  - Public use: Date of public disclosure

- **Pre-AIA vs. AIA** (America Invents Act, March 16, 2013):
  - **Pre-AIA** (first-to-invent): Complex rules, US-only prior art for some categories
  - **AIA** (first-to-file): Simpler, worldwide prior art, filing date controls
  - **Critical**: Applications filed before March 16, 2013 use pre-AIA rules

---

## Patent Classification Systems

### Why Classifications Matter

**Search Efficiency**:
- Keywords miss synonyms and foreign language patents
- Classifications group similar inventions (across languages)
- Essential for comprehensive searches

**Coverage**:
- Keyword-only search: ~30-50% recall
- Classification-only search: ~50-70% recall
- **Combined keyword + classification: ~85-95% recall**

### IPC (International Patent Classification)

**Structure**: Hierarchical, 8 sections

**Sections** (Top Level):
- **A**: Human Necessities (agriculture, food, health)
- **B**: Performing Operations, Transporting (separating, shaping, printing)
- **C**: Chemistry, Metallurgy
- **D**: Textiles, Paper
- **E**: Fixed Constructions (building, mining)
- **F**: Mechanical Engineering, Lighting, Heating, Weapons
- **G**: Physics (instruments, computing, photography)
- **H**: Electricity (electronics, communication, electric power)

**Hierarchy Example**:
```
H04L 29/06
│││││ ││ ││
││││└ Subclass (two digits)
│││└─ Class (two digits)
││└── Section (one letter)
│└─── Subclass (one letter)
└──── Section (H = Electricity)

Full breakdown:
H     = Electricity
H04   = Electric Communication Technique
H04L  = Transmission of Digital Information (e.g., Telegraphic Communication)
H04L 29/06 = Characterized by a protocol
```

**Reading IPC Codes**:
- **Section**: Broad technology (A-H)
- **Class**: Narrower (2 digits)
- **Subclass**: More specific (letter)
- **Main Group**: Core technology (numbers before /)
- **Subgroup**: Detailed features (numbers after /)

**Using IPC**:
1. **Identify Candidate Classifications**: Browse IPC definitions (www.wipo.int/classifications/ipc)
2. **Search by Classification**: Find patents in that class
3. **Review Results**: Verify classification accuracy
4. **Expand or Narrow**: Adjust classification level as needed

### CPC (Cooperative Patent Classification)

**Joint System**: USPTO + EPO (2013)

**Advantages over IPC**:
- **More Granular**: 250,000+ categories vs. IPC's 70,000
- **More Current**: Updated frequently (IPC updated every 3 years)
- **Better Coverage**: Particularly for modern technologies (software, biotech)
- **Same Structure**: Based on IPC, so familiar hierarchy

**CPC-Specific Symbols**:
- **Y sections**: Cross-cutting themes (Y02 = Climate change, Y10 = Technical subjects covered by former USPC)
- **Additional notations**: More detailed than IPC

**Example CPC Code**:
```
H04L 63/1416
│││││ ││ ││││
│││││ ││ │││└─ Very specific feature
│││││ ││ ││└── Subgroup
│││││ ││ │└─── Subgroup
│││││ ││ └──── Main group
│││││ │└────── Subclass
│││││ └─────── Class
│││└└───────── Section
││└──────────── Class
│└───────────── Section
└────────────── Section (H = Electricity)

H04L 63/1416 = Network security, authentication, biometric authentication
```

**CPC vs. IPC Choice**:
- **Use CPC**: USPTO, EPO searches (more specific)
- **Use IPC**: WIPO, international searches (broader compatibility)
- **Use Both**: Maximum coverage

**Finding Classifications**:

1. **Classification Search Tools**:
   - USPTO CPC search: www.uspto.gov/web/patents/classification
   - EPO classification search: worldwide.espacenet.com
   - WIPO IPC search: www.wipo.int/classifications/ipc

2. **From Known Patents**:
   - Find similar patent → Note its classifications → Search those classes
   - Most reliable method (real-world classification example)

3. **Browse Hierarchies**:
   - Start broad (section) → narrow down (class → subclass → group)
   - Read definitions at each level

**Common Technology Classifications**:

**Software/Computing**:
- G06F (Digital computing, data processing)
- G06Q (Data processing for business, finance, management)
- G06N (Computer systems based on specific models - AI, neural networks)
- H04L (Transmission of digital information)

**Medical Devices**:
- A61B (Diagnosis, surgery, identification)
- A61F (Filters for blood vessels, prostheses, orthopedic devices)
- A61K (Pharmaceutical preparations)
- A61M (Devices for introducing media into body)

**Telecommunications**:
- H04W (Wireless communication networks)
- H04L (Digital transmission, packet switching)
- H04M (Telephonic communication)
- H04B (Transmission)

**Chemistry/Materials**:
- C07 (Organic chemistry)
- C08 (Organic macromolecular compounds, polymers)
- C12 (Biochemistry, microbiology, enzymology)

**Mechanical**:
- F16 (Engineering elements or units)
- F01 (Machines or engines in general)
- B23 (Machine tools, metalworking)

### US Classification (USPC) - Legacy

**Status**: Deprecated January 1, 2015 (replaced by CPC)

**Why Still Relevant**:
- Older patents (pre-2015) primarily classified in USPC
- Historical searches may require USPC
- Some patents have both USPC and CPC

**Structure**: Class/Subclass (e.g., 705/35)
- Flatter hierarchy than IPC/CPC
- ~450 classes, ~150,000 subclasses

**Conversion**: USPTO provides USPC-to-CPC concordance
- Use to translate old USPC searches to modern CPC

---

## Search Databases

### USPTO (United States Patent and Trademark Office)

**Coverage**: US patents and published applications

**Databases**:

1. **PatFT (Patent Full-Text and Image Database)**
   - **URL**: patft.uspto.gov
   - **Content**: Granted patents, 1976-present (full-text), 1790-1975 (images only)
   - **Search**: Boolean, field codes (title, abstract, claims, inventor, assignee)
   - **Limitations**: Basic interface, US patents only

2. **AppFT (Application Full-Text Database)**
   - **URL**: appft.uspto.gov
   - **Content**: Published applications, 2001-present
   - **Search**: Similar to PatFT
   - **Use**: Find pending applications (not yet granted)

3. **Patent Center** (formerly PAIR)
   - **URL**: patentcenter.uspto.gov
   - **Content**: Prosecution history (office actions, amendments, correspondence)
   - **Use**: Deep dive on specific patents, understand claim scope

**Strengths**:
- Official source (authoritative)
- Free access
- Full prosecution history available

**Weaknesses**:
- US patents only
- Clunky interface (dated)
- Limited export/analysis tools

### Google Patents

**Coverage**: Worldwide (USPTO, EPO, WIPO, and many national offices)

**URL**: patents.google.com

**Features**:
- **Natural Language Search**: "Machine learning image recognition" (no Boolean required)
- **PDF Download**: One-click full patent download
- **Citation Trees**: Visual forward/backward citation graphs
- **Prior Art Finder**: Automated prior art suggestions
- **Clean Interface**: Modern, fast, intuitive
- **Machine Translation**: Automatic translation for foreign patents

**Search Capabilities**:
- Keyword search (natural language or Boolean)
- Classification search (CPC, IPC)
- Inventor, assignee, filing date, etc.
- Combined searches

**Strengths**:
- Best user interface
- Worldwide coverage (100+ million documents)
- Fast and free
- Excellent for initial searches and citation analysis

**Weaknesses**:
- Not official source (use USPTO for legal certainty)
- Search syntax less powerful than specialized databases
- No prosecution history

**Best Practices**:
- Use for exploratory searches and citation analysis
- Verify key patents on official sources (USPTO, EPO)
- Export patent numbers, then search official databases

### EPO Espacenet

**Coverage**: Worldwide (140+ million documents, 110+ countries)

**URL**: worldwide.espacenet.com

**Features**:
- **Advanced Search**: Classifications, citations, legal status
- **Patent Families**: Related applications in different countries (INPADOC)
- **Legal Status**: Current status of patents (active, expired, pending)
- **Machine Translation**: Translate foreign patents to English
- **Batch Export**: Export search results

**Search Modes**:
1. **Quick Search**: Simple keyword search
2. **Advanced Search**: Field-specific (inventor, applicant, classification, date)
3. **Classification Search**: Browse IPC/CPC hierarchies
4. **Number Search**: Retrieve by patent/application number

**Strengths**:
- Official source (European Patent Office)
- Excellent international coverage
- Legal status information (invaluable for FTO)
- Advanced features (family search, legal status)

**Weaknesses**:
- Interface less intuitive than Google Patents
- Machine translation quality varies
- Export limitations (50 patents per batch)

**Best Use**:
- International searches (especially European and Asian patents)
- Legal status verification (FTO searches)
- Patent family analysis

### WIPO PatentScope

**Coverage**: Worldwide (100+ million documents, PCT applications, 70+ national collections)

**URL**: patentscope.wipo.int

**Features**:
- **PCT Applications**: International applications (only place to search comprehensively)
- **National Collections**: Many countries not in other databases
- **CLIR (Cross-Lingual Information Retrieval)**: Search in one language, find results in others
- **Advanced Search**: Boolean, field codes, classifications
- **Chemical Search**: Structure and sequence search (specialized)

**Strengths**:
- PCT applications (exclusive)
- Broadest international coverage
- Chemical structure search (unique)
- CLIR (language-agnostic search)

**Weaknesses**:
- Interface less modern
- Slower than Google Patents
- Export and analysis tools limited

**Best Use**:
- PCT application searches
- Searching countries not well-covered elsewhere (Africa, Middle East, Southeast Asia)
- Chemical/biotech searches (structure search)

### Commercial Databases

**When to Use**: High-stakes searches (invalidity, FTO, major investments)

**Major Providers**:

1. **Derwent Innovation (Clarivate)**
   - **Cost**: $20k-$100k+/year
   - **Features**: Enhanced abstracts, family grouping, citation analysis, alerts
   - **Best For**: Pharmaceutical, biotech, chemistry (strong coverage)

2. **Questel Orbit**
   - **Cost**: $15k-$80k+/year
   - **Features**: Advanced analytics, patent landscapes, legal status
   - **Best For**: Corporate IP departments, law firms

3. **PatBase (Minesoft)**
   - **Cost**: $10k-$50k+/year
   - **Features**: Sequence search, advanced export, custom alerts
   - **Best For**: Biotech, pharma (sequence search)

**Value Proposition**:
- More powerful search syntax
- Better analytics and visualization
- Enhanced data (legal status, patent families, standardized assignees)
- Saved searches and alerts
- Customer support

**ROI Consideration**:
- Cost ~$20k-$50k/year (typical corporate subscription)
- Value: Better search quality, time savings, reduced risk
- Break-even: If preventing one missed prior art reference (>$50k litigation savings)

---

## Search Strategies

### Iterative Search Process

**Phase 1: Exploratory (30 min - 1 hour)**
1. **Understand Technology**: Read disclosure, identify key terms
2. **Quick Keyword Search**: Google Patents, broad terms
3. **Review Top 10-20 Results**: Are they relevant? Identify patterns
4. **Refine Understanding**: Better terminology, related concepts

**Phase 2: Comprehensive Keyword (1-2 hours)**
1. **Develop Keyword List**: Primary terms + synonyms + related concepts
2. **Boolean Combinations**: AND, OR, NOT to create precise queries
3. **Multiple Databases**: Google Patents + Espacenet or PatentScope
4. **Filter by Date**: Relevant time period (e.g., last 20 years)
5. **Review 50-100 Results**: Mark relevant references

**Phase 3: Classification Search (1-2 hours)**
1. **Identify Classifications**: From relevant patents found in Phase 2
2. **Search by Classification**: CPC/IPC in USPTO, EPO, or Google Patents
3. **Combine with Keywords**: Classification AND keywords for precision
4. **Review Results**: Another 50-100 patents

**Phase 4: Citation Analysis (1-2 hours)**
1. **Key Patents**: Most relevant 5-10 patents from Phases 2-3
2. **Backward Citations**: What did they cite as prior art?
3. **Forward Citations**: Who cited them? (later developments)
4. **Iterate**: Review citations, then their citations (2-3 levels deep)

**Phase 5: Assignee/Inventor Search (30 min - 1 hour)**
1. **Key Players**: Identify leading companies/inventors from results
2. **Portfolio Search**: All patents by that assignee/inventor
3. **Review Recent Filings**: Last 5 years, same technology area

**Phase 6: Non-Patent Literature (1-3 hours, if needed)**
1. **Google Scholar**: Academic papers, technical publications
2. **IEEE Xplore**: Engineering publications
3. **Industry Sources**: Trade publications, product catalogs
4. **Websites/Archives**: Internet Archive for dated web content

**Total Time**: 6-10 hours for standard comprehensive search

### Keyword Development

**Core Terms**:
- Primary technical terms from invention
- Example: "machine learning", "neural network", "image recognition"

**Synonyms**:
- Different ways to say the same thing
- Example: "machine learning" = "ML" = "artificial intelligence" = "AI" = "deep learning"

**Related Concepts**:
- Adjacent or enabling technologies
- Example: "image recognition" → "computer vision", "object detection", "pattern recognition"

**Broader and Narrower Terms**:
- Broader: Encompassing category
  - Example: "vehicle" (broader than "car")
- Narrower: Specific implementations
  - Example: "convolutional neural network" (narrower than "neural network")

**Truncation and Wildcards**:
- **Truncation (*)**: Matches word variations
  - "comput*" → computer, computing, computation, compute
- **Wildcard (?)**: Replaces single character
  - "wom?n" → woman, women

**Building Keyword Combinations**:

**Method**: Combine using Boolean operators

Example for "Blockchain payment system":
```
(blockchain OR "distributed ledger" OR "block chain")
AND
(payment OR transaction OR transfer OR remittance)
AND
(system OR method OR process OR platform)
```

**Phrase Searching**:
- **Quotes**: Exact phrase
  - "machine learning" (must be adjacent)
- **Proximity (NEAR/n)**: Within n words
  - machine NEAR/5 learning (within 5 words)

### Classification Search Strategy

**Step 1: Identify Candidate Classifications**

**Method A**: From Known Patents
- Find 2-3 relevant patents from keyword search
- Note their classifications (both primary and secondary)
- Those classifications are likely relevant to your search

**Method B**: Browse Classification Hierarchy
- Start at broad level (section, class)
- Read definitions
- Drill down to more specific subclasses
- Identify most relevant groups

**Step 2: Validate Classification**

**Sample Search**:
- Search selected classification
- Review first 20-30 results
- **Good fit**: 70%+ are relevant → use this classification
- **Poor fit**: <50% relevant → try adjacent classifications

**Step 3: Search Multiple Related Classifications**

**Example** (for "Medical wearable sensor"):
- A61B 5/00 (Measuring for diagnostic purposes)
- A61B 5/024 (Heart rate monitoring)
- A61B 5/11 (Body movement sensing)
- G16H 40/67 (ICT for management of medical data)

**Combine**: (A61B 5/00 OR A61B 5/024 OR A61B 5/11 OR G16H 40/67) AND (wearable OR portable OR "body-worn")

**Step 4: Balance Recall and Precision**

- **High-level classification** (e.g., A61B 5/00): High recall (finds more), lower precision (more irrelevant)
- **Low-level classification** (e.g., A61B 5/024): Lower recall (finds fewer), high precision (more relevant)

**Strategy**: Search both levels, combine results

### Combined Keyword + Classification Search

**Optimal Approach**: Maximize both recall and precision

**Formula**:
```
(Classification1 OR Classification2 OR Classification3)
AND
(Keyword1 OR Keyword2 OR Keyword3)
AND
(Keyword4 OR Keyword5)
```

**Example** (Machine learning for medical diagnostics):
```
(CPC:(G06N 3/08 OR G06N 20/00 OR G16H 50/20))
AND
((machine ADJ learning) OR (neural ADJ network) OR (deep ADJ learning) OR AI)
AND
(medical OR diagnosis OR diagnostic OR patient OR disease)
```

**Result**: Patents that:
1. Are classified in ML or medical informatics classes
2. Mention ML keywords
3. Mention medical/diagnostic keywords

**Recall Improvement** (find more):
- Add more keyword synonyms
- Use broader classifications
- Use truncation (comput*)

**Precision Improvement** (reduce noise):
- Use narrower classifications
- Use phrase searching ("machine learning" not machine AND learning)
- Add more required terms (more ANDs)
- Exclude irrelevant terms (NOT)

---

## Boolean and Field Searches

### Boolean Operators

**AND**: Both terms required (narrows search)
```
machine AND learning
→ Documents with both "machine" and "learning"
```

**OR**: Either term (broadens search)
```
machine OR artificial
→ Documents with "machine" or "artificial" (or both)
```

**NOT**: Exclude terms (narrows search)
```
machine NOT ATM
→ Documents with "machine" but not "ATM"
```

**Parentheses**: Group operations (order of operations)
```
(machine OR artificial) AND learning
→ "machine learning" or "artificial learning"
```

**Nested Boolean**:
```
((machine OR artificial) AND (learning OR intelligence))
AND
(image OR video OR photo)
```

### Proximity Operators

**NEAR/n**: Terms within n words (order independent)
```
machine NEAR/5 learning
→ "machine learning", "learning machine systems", "machine-based deep learning"
```

**ADJ/n**: Terms within n words (order dependent)
```
machine ADJ/2 learning
→ "machine learning", "machine-based learning" (machine before learning)
```

**WITH**: Terms in same field (paragraph, sentence, abstract)
```
machine WITH learning WITH image
→ All three terms in same paragraph/field
```

**Database Differences**:
- Google Patents: Limited proximity (use phrase search with quotes)
- USPTO PatFT: NEAR/n, ADJ/n supported
- EPO/WIPO: Proximity varies by database

### Field Codes (USPTO PatFT)

**Common Fields**:

```
TI/: Title
AB/: Abstract
ACLM/: All Claims
SPEC/: Full specification (entire document)
IN/: Inventor name
AN/: Assignee (current)
AAN/: Assignee (at issuance)
ISD/: Issue date
APD/: Application date
CCL/: Current CPC classification
ICL/: International (IPC) classification
```

**Field Search Examples**:

**Title search**:
```
TI/(blockchain AND payment)
→ Patents with "blockchain" and "payment" in title
```

**Inventor search**:
```
IN/"Smith, John"
→ All patents invented by John Smith
```

**Assignee search**:
```
AN/Google
→ All patents currently assigned to Google (or subsidiaries)
```

**Date range**:
```
ISD/20200101->20231231
→ Issued between Jan 1, 2020 and Dec 31, 2023
```

**Classification + keyword**:
```
CCL/H04L63/08 AND TI/(authentication OR biometric)
→ Patents in H04L63/08 class with "authentication" or "biometric" in title
```

**Combining fields**:
```
(TI/blockchain OR AB/blockchain) AND ACLM/payment AND ISD/20180101->$
→ Title or abstract has "blockchain", claims have "payment", issued since 2018
```

### Advanced Search Techniques

**Truncation**:
```
comput*
→ computer, computing, computation, computed, compute
```

**Wildcards**:
```
wom?n → woman, women
behavio?r → behavior, behaviour (US/UK spelling)
```

**Phrase Search** (quotes):
```
"machine learning"
→ Exact phrase (adjacent words)
```

**Exclusion** (NOT):
```
apple NOT fruit
→ Patents about Apple (company) not apple (fruit)
```

**Must Include + Optional**:
```
+machine +learning image
→ Must have "machine" and "learning", optionally "image"
```

**Fuzzy Search** (some databases):
```
machine~
→ machine, machina, machines (approximate matching)
```

---

## Citation Analysis

### Citation Types

**Backward Citations** (References Cited):
- Prior art cited by patent during prosecution
- Listed on front page of granted patent
- **Sources**: Examiner-cited (from search), Applicant-cited (from disclosure)

**Forward Citations** (Cited By):
- Later patents that cite this patent as prior art
- Shows technological lineage and impact
- **High citation count**: Influential/foundational patent

### Citation Search Strategy

**Step 1: Find Key Patents** (from keyword/classification search)

**Step 2: Backward Citations**
- Review "References Cited" section
- **Examiner-cited**: Most relevant (examiner thought close prior art)
- **Applicant-cited**: Also important (applicant disclosed)
- **Non-patent literature**: Articles, books cited

**Step 3: Evaluate Cited References**
- Read abstracts of cited patents
- Identify most relevant (closest to your invention)
- Note any that disclose key features

**Step 4: Forward Citations**
- Who cited the key patents?
- Later developments in same technology
- Potential infringement targets (if they're citing your patent)

**Step 5: Iterate** (2-3 Levels Deep)
- Backward citations of backward citations
- Forward citations of forward citations
- Build citation network

### Citation Network Analysis

**Citation Tree** (Google Patents visualization):
- **Root**: Your key patent
- **Branches up**: Backward citations (prior art)
- **Branches down**: Forward citations (later developments)

**Patterns to Identify**:

**Foundational Patent**:
- High forward citation count (50+, 100+, 1000+ for major innovations)
- Many later patents cite it
- **Example**: Seminal machine learning or blockchain patents

**Patent Family**:
- Cluster of patents citing each other
- Same assignee, related technology
- Likely a patent portfolio around single invention

**Blocking Patent**:
- Cited by many later patents
- Broad claims covering technology area
- Potential FTO issue

**White Space**:
- Sparse citations in specific area
- Opportunity for new patents

**Tools for Citation Analysis**:
- **Google Patents**: Visual citation tree
- **Espacenet**: INPADOC family and citations
- **Lens.org**: Free citation analysis and patent families
- **Commercial**: Derwent Innovation, Orbit (advanced analytics)

---

## Non-Patent Literature

### Why Non-Patent Literature Matters

**Patents Miss**:
- Academic research (published before patent filing)
- Open-source projects (public code, no patent)
- Product documentation (manuals, catalogs)
- Standards (IEEE, ISO, ANSI)
- Websites and blogs (technical disclosures)

**Legal Significance**:
- Non-patent literature is prior art (just as valid as patents)
- Often earlier than patents (publication faster than patent grant)
- Can invalidate patents (if dated before patent priority)

### Academic Literature Search

**Google Scholar** (scholar.google.com):
- **Coverage**: Academic papers, theses, books, conference proceedings
- **Search**: Keyword search, author search, citation search
- **Date Filter**: Limit to relevant time period
- **Citation Count**: Indicator of influence
- **"Cited by"**: Forward citations (academic)

**IEEE Xplore** (ieeexplore.ieee.org):
- **Coverage**: Electrical engineering, computer science publications
- **Cost**: Subscription required (or pay-per-article)
- **Quality**: Peer-reviewed, high quality
- **Use For**: Software, hardware, telecommunications

**PubMed** (pubmed.ncbi.nlm.nih.gov):
- **Coverage**: Biomedical and life sciences literature
- **Free**: US government database
- **Use For**: Medical devices, pharmaceuticals, biotech

**ArXiv** (arxiv.org):
- **Coverage**: Pre-print server (physics, math, CS, biology)
- **Free**: Open access
- **Timeliness**: Earlier than journal publication
- **Use For**: Cutting-edge research (especially ML, AI)

### Technical Standards

**Standards Organizations**:
- **IEEE**: Institute of Electrical and Electronics Engineers
- **ISO**: International Organization for Standardization
- **ANSI**: American National Standards Institute
- **IETF**: Internet Engineering Task Force (RFCs)
- **3GPP**: 3rd Generation Partnership Project (telecom standards)

**Why Relevant**:
- Standards describe technical implementations (detailed specifications)
- Industry-wide adoption (public knowledge)
- Dated (clear priority date)
- Can be strong prior art (if predates patent)

**Access**:
- Some free (IETF RFCs)
- Some paid (IEEE, ISO standards)
- University libraries (often have subscriptions)

### Open Source and Code Repositories

**GitHub** (github.com):
- **Search**: Code search, repository search
- **Date**: Commit dates (timestamped)
- **Use**: Software prior art (especially algorithms, implementations)
- **Evidence**: README files, commit history, issue discussions

**SourceForge, GitLab, Bitbucket**:
- Alternative code repositories
- Similar search capabilities

**Stack Overflow**:
- Q&A site for programmers
- Technical discussions (dated)
- Can be prior art if discloses technical solution

### Internet Archive (Wayback Machine)

**Purpose**: Retrieve historical website content

**URL**: archive.org/web

**Use**:
- Prove public disclosure date
- Retrieve deleted web content
- Product pages, technical blogs, documentation

**Process**:
1. Enter URL of interest
2. Select date (snapshot from specific date)
3. Save screenshot/PDF (evidence of disclosure)

**Legal Value**:
- Admissible as evidence (courts accept Wayback Machine)
- Proves public accessibility on specific date
- Critical for websites/blogs as prior art

### Product Catalogs and Trade Publications

**Product Catalogs**:
- Manufacturer catalogs (printed or online)
- Technical specifications
- Dated (publication date = prior art date)

**Trade Publications**:
- Industry magazines (Electronics Weekly, Design News, etc.)
- Product announcements
- Technical articles
- Dated

**Trade Shows**:
- Exhibition catalogs
- Product demonstrations (if public, dated)
- Conference proceedings

**Access**:
- Historical archives (libraries, industry associations)
- Internet Archive
- Publisher websites

---

## Search Documentation

### Why Document Searches

**Legal Protection**:
- Good faith search (defense against willful infringement)
- Due diligence (if challenged)
- Opinion of counsel (reliance on documented search)

**Business Value**:
- Replicability (someone else can verify)
- Knowledge sharing (teach team)
- Audit trail (decision justification)

### What to Document

**Search Strategy**:
- **Keywords Used**: All terms, synonyms, Boolean combinations
- **Classifications Searched**: CPC, IPC codes
- **Databases**: Which databases searched
- **Date Ranges**: Time periods covered
- **Date Conducted**: When search performed

**Search Queries**:
- **Exact Syntax**: Copy-paste actual queries used
- **Number of Results**: Hits per query
- **Results Reviewed**: How many reviewed, how many relevant

**Key References Found**:
- **Patent Numbers**: All relevant patents
- **Relevance Rating**: High/medium/low relevance
- **Why Relevant**: Brief description of relevance
- **Status**: Active, expired, pending, abandoned

**Non-Patent Literature**:
- **Citations**: Full bibliographic information
- **Access Date**: When retrieved
- **Relevance**: Brief description

### Search Report Template

```markdown
# Prior Art Search Report

## Executive Summary
- **Search Date**: [Date]
- **Searcher**: [Name]
- **Invention**: [Brief description]
- **Purpose**: Patentability / FTO / Invalidity / Landscape
- **Conclusion**: [1-2 sentence summary]

## Search Strategy

### Keywords
**Primary Terms**:
- [Term 1], [Term 2], [Term 3]

**Synonyms**:
- [Term A] = [Synonym 1], [Synonym 2]

**Boolean Combinations**:
- Query 1: (term1 OR term2) AND (term3 OR term4)
- Query 2: ...

### Classifications
- **CPC**: [Code 1], [Code 2], [Code 3]
- **IPC**: [Code 1], [Code 2]

### Databases Searched
- Google Patents (worldwide, 1790-present)
- USPTO PatFT (US patents, 1976-present)
- EPO Espacenet (140M documents, worldwide)
- Google Scholar (academic literature, 2000-2025)

### Date Range
- Patents: All dates (focus on 2000-2025)
- Publications: 2000-2025

## Search Results

### Keyword Search Results
| Query | Database | Hits | Reviewed | Relevant |
|-------|----------|------|----------|----------|
| Query 1 | Google Patents | 1,245 | 100 | 12 |
| Query 2 | USPTO | 856 | 50 | 8 |
| ... | ... | ... | ... | ... |

### Classification Search Results
| Classification | Database | Hits | Reviewed | Relevant |
|----------------|----------|------|----------|----------|
| H04L 63/08 | Google Patents | 3,421 | 100 | 15 |
| ... | ... | ... | ... | ... |

### Citation Analysis
- Backward citations reviewed: 45 patents
- Forward citations reviewed: 28 patents
- Additional relevant references found: 7

### Non-Patent Literature
- Google Scholar: 25 papers reviewed, 5 relevant
- GitHub: 10 repositories reviewed, 2 relevant

## Key References

### Highly Relevant (Blocking or Close Prior Art)
1. **US 10,123,456** (Smith et al., Acme Corp.)
   - Filed: 2018-05-15, Granted: 2020-08-22
   - Status: Active (maintained)
   - Relevance: Discloses [feature X] and [feature Y], very similar to claims 1-5
   - Abstract: [Brief summary]
   - Key Claims: Claim 1 covers [description]

[Repeat for each highly relevant reference]

### Moderately Relevant
[Similar format, briefer]

### Background References
[List only, minimal detail]

## Analysis

### Patentability Assessment
- **Novelty**: [Analysis of whether invention is novel over prior art]
- **Non-Obviousness**: [Analysis of whether invention would be obvious to POSITA]
- **Recommendation**: File / Don't File / Modify Claims

### Freedom to Operate (if applicable)
- **Active Patents Identified**: [Number]
- **Risk Level**: High / Medium / Low
- **Blocking Patents**: [List if any]
- **Recommendation**: [Clear / Design-around / License / Challenge]

### Landscape Observations (if applicable)
- **Key Players**: [Assignees with most patents]
- **Technology Trends**: [Observations]
- **White Space**: [Opportunities]

## Appendices

### Appendix A: Search Queries (Full Text)
[Exact queries used, copy-paste]

### Appendix B: Reference List (Complete)
[All patents reviewed, even if not relevant]

### Appendix C: Non-Patent Literature (Full Citations)
[Bibliographic information]

---

**Report Prepared By**: [Name]
**Date**: [Date]
**Review**: [Attorney/Manager Review, if applicable]
```

### Search Query Log

**Maintain Separate Log** (for replicability):

```
Search Query Log
Date: 2025-01-15
Searcher: Jane Doe

Query 1:
Database: Google Patents
Query: (blockchain OR "distributed ledger") AND (payment OR transaction) AND (secure OR encryption)
Date Filter: 2015-2025
Results: 1,245 hits
Reviewed: First 100
Relevant: 12
Notes: Mostly cryptocurrency patents, narrowed to financial services

Query 2:
Database: USPTO PatFT
Query: CCL/(G06Q 20/38 OR G06Q 20/40) AND TI/(blockchain OR "distributed ledger")
Date Filter: 2015-2025
Results: 342 hits
Reviewed: All 342 (scanned abstracts)
Relevant: 28
Notes: Higher precision due to classification + title search

[Continue for all queries...]
```

### Reference Tracking Spreadsheet

**Columns**:
- Patent Number
- Title
- Assignee
- Inventors
- Filing Date
- Grant Date (if granted)
- Status (Active/Expired/Pending/Abandoned)
- CPC Classification(s)
- Relevance (High/Medium/Low)
- Key Features (brief description)
- Source (which query found it)
- Notes

**Use**:
- Track all patents reviewed
- Sort by relevance
- Share with team
- Attach to search report

---

## Conclusion

**Effective prior art searching requires**:

1. **Clear Scope**: Understand invention, define search boundaries
2. **Multiple Strategies**: Keywords + classifications + citations + non-patent literature
3. **Multiple Databases**: No single database has everything
4. **Iteration**: Refine search based on results
5. **Documentation**: Record strategy and results
6. **Analysis**: Evaluate relevance and legal impact

**A comprehensive search** (6-10 hours):
- 85-95% recall (finds most relevant prior art)
- Supports informed decisions (file or not, claim scope, FTO)
- Defensible (if challenged, documented good faith effort)

**Continuous learning**: Each search improves skills. Review granted patents to see what examiners find (learn from their search strategies).

---

**Resources**:
- USPTO Search Guide: www.uspto.gov/patents/search
- EPO Search Guide: www.epo.org/searching-for-patents
- WIPO Classification: www.wipo.int/classifications
- Google Patents: patents.google.com

---

**Version History**:
- v1.0.0 (January 2025): Initial comprehensive prior art research skill
