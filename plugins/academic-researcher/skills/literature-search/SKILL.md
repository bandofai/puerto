# Literature Search Skill

**Expert patterns for academic database search, systematic reviews, and citation analysis**

## Core Principles

1. **Comprehensive Coverage**: Search multiple databases for complete literature coverage
2. **Systematic Approach**: Document search strategy for reproducibility
3. **Quality Assessment**: Evaluate source credibility and relevance
4. **Citation Management**: Track sources meticulously from the start
5. **Iterative Refinement**: Refine search based on results

---

## Search Strategy Development

### PICO Framework (Clinical Research)

Use PICO to structure clinical/healthcare research questions:

**P**opulation: Who is the patient/population?
- Age group, gender, ethnicity
- Medical condition or characteristic
- Setting (hospital, community, etc.)

**I**ntervention: What intervention/exposure?
- Treatment, diagnostic test, exposure
- Specific details (dose, duration, method)

**C**omparison: What is the alternative?
- Standard care, placebo, alternative treatment
- No intervention

**O**utcome: What outcomes are measured?
- Primary outcomes
- Secondary outcomes
- Timeframe

**Example**:
```
P: Adults aged 65+ with Type 2 diabetes
I: Continuous glucose monitoring
C: Standard finger-stick monitoring
O: HbA1c levels, hypoglycemic events (6 months)

Search terms:
  Population: "older adults" OR "elderly" OR "aged" AND "type 2 diabetes" OR "T2D"
  Intervention: "continuous glucose monitoring" OR "CGM"
  Comparison: "self-monitoring blood glucose" OR "SMBG" OR "finger-stick"
  Outcome: "HbA1c" OR "glycemic control" OR "hypoglycemia"
```

### Concept Mapping

For general research, map out main concepts and related terms:

```
Main Concept: Machine Learning Bias
  ├─ Synonyms: algorithmic bias, AI fairness, model bias
  ├─ Related: fairness, discrimination, equity
  ├─ Specific types: selection bias, measurement bias, sampling bias
  └─ Applications: healthcare, hiring, criminal justice

Boolean Search:
("machine learning" OR "artificial intelligence" OR "AI" OR "deep learning")
AND
("bias" OR "fairness" OR "discrimination" OR "equity")
AND
("healthcare" OR "medical" OR "clinical")
```

---

## Boolean Operators

### AND - Narrows Search

Requires ALL terms to be present:
```
machine learning AND healthcare
  → Results must contain BOTH terms
  → Reduces number of results
  → Increases specificity
```

### OR - Broadens Search

Requires ANY term to be present:
```
("machine learning" OR "deep learning" OR "AI")
  → Results contain at least ONE term
  → Increases number of results
  → Captures synonyms and variations
```

### NOT - Excludes Terms

Removes results with specific term:
```
climate NOT "climate change"
  → Results about climate but excludes climate change
  → Use cautiously (may exclude relevant papers)
```

### Parentheses - Groups Terms

Controls order of operations:
```
(machine learning OR AI) AND (bias OR fairness) AND healthcare
  → Evaluates OR operations first, then AND
```

### Quotation Marks - Exact Phrase

Searches for exact phrase:
```
"machine learning"
  → Both words together in that order
  → More precise than: machine AND learning
```

---

## Google Scholar Search via WebSearch

### Basic Search Syntax

```bash
# Basic keyword search
WebSearch: "machine learning bias healthcare" site:scholar.google.com

# Author search
WebSearch: author:"Smith J" machine learning site:scholar.google.com

# Title search
WebSearch: intitle:"algorithmic fairness" site:scholar.google.com

# Source/journal search
WebSearch: source:"Nature" machine learning site:scholar.google.com

# Date range
WebSearch: "machine learning" after:2020 before:2024 site:scholar.google.com

# Highly cited papers
WebSearch: "machine learning" cited by:100 site:scholar.google.com
```

### Advanced Operators

**intitle:** - Search in title only
```
intitle:"systematic review" machine learning
  → Papers with "systematic review" in title
```

**author:** - Search by author
```
author:"hinton" deep learning
  → Papers by author with "hinton" in name
```

**source:** - Search in specific journal
```
source:"Nature Machine Intelligence" fairness
  → Papers published in that journal
```

**after:YYYY** - Papers after year
```
"machine learning" after:2020
  → Only papers from 2020 onwards
```

**before:YYYY** - Papers before year
```
"machine learning" before:2020
  → Only papers before 2020
```

### Citation Analysis

**Find highly cited papers**:
```
"machine learning" cited by:500
  → Papers cited at least 500 times
```

**Citation tracking**:
1. Find seminal paper
2. Check "Cited by X" link
3. Identify papers that cite it (forward citation)
4. Check references (backward citation)

---

## PubMed Search via WebSearch

### MeSH Terms (Medical Subject Headings)

```bash
# Search with MeSH terms
WebSearch: "diabetes mellitus"[MeSH] AND "machine learning" site:pubmed.ncbi.nlm.nih.gov

# Search in specific fields
WebSearch: "bias"[Title] AND "prediction model"[Abstract] site:pubmed.ncbi.nlm.nih.gov

# Limit to specific publication types
WebSearch: "systematic review"[PT] machine learning site:pubmed.ncbi.nlm.nih.gov
```

### Field Tags

- **[Title]** - Search in title
- **[Abstract]** - Search in abstract
- **[Author]** - Search by author name
- **[MeSH]** - MeSH controlled vocabulary
- **[PT]** - Publication type (Review, Clinical Trial, etc.)

### Filters

```
Publication date: Use after:YYYY in WebSearch query
Article type: Include [PT] tag (e.g., "systematic review"[PT])
Species: Add "humans"[MeSH] to limit to human studies
Language: Add "english"[Language]
```

---

## Systematic Review Protocol (PRISMA)

### Phase 1: Protocol Development

**Define Research Question**:
```
PICO format:
P: Population of interest
I: Intervention/exposure
C: Comparison
O: Outcomes

Example:
Among adults with depression (P), does cognitive behavioral therapy (I)
compared to medication (C) reduce symptom severity (O)?
```

**Develop Search Strategy**:
```
1. Identify key concepts from PICO
2. Generate synonyms and related terms
3. Construct Boolean search strings
4. Test and refine searches
5. Document final search strategy
```

**Define Inclusion Criteria**:
```
Study design: RCTs, cohort studies, case-control
Population: Age range, condition, setting
Intervention: Specific interventions
Outcome: Required outcome measures
Language: English, other languages
Date: Publication date range
```

**Define Exclusion Criteria**:
```
Study design: Case reports, editorials, opinion pieces
Population: Animal studies, pediatric (if adult focus)
Intervention: Not relevant interventions
Outcomes: Lacks required outcomes
Quality: High risk of bias
```

### Phase 2: Search Execution

**Database Selection** (minimum 3):
```
Primary: Google Scholar (broad coverage)
Medical: PubMed/MEDLINE
Preprints: arXiv, bioRxiv, SSRN
Citation indexes: Web of Science, Scopus
Specialized: IEEE Xplore (engineering), PsycINFO (psychology)
```

**Search Documentation**:
```markdown
## Search Strategy

### Database: Google Scholar
**Date searched**: 2024-01-20
**Search string**: ("machine learning" OR "artificial intelligence") AND
                  "bias" AND ("healthcare" OR "medical")
**Filters**: Year 2019-2024, English
**Results**: 1,247 papers

### Database: PubMed
**Date searched**: 2024-01-20
**Search string**: (machine learning[Title/Abstract] OR artificial
                  intelligence[Title/Abstract]) AND bias[Title/Abstract]
                  AND (healthcare OR medical)
**Filters**: Humans, English, 2019-2024
**Results**: 342 papers
```

### Phase 3: Screening

**Title/Abstract Screening**:
```
1. Export all search results
2. Remove duplicates
3. Screen titles for relevance
4. Screen abstracts of potentially relevant papers
5. Document reasons for exclusion
6. Calculate inter-rater reliability (if multiple reviewers)
```

**Full-Text Screening**:
```
1. Obtain full-text of included abstracts
2. Apply inclusion/exclusion criteria thoroughly
3. Document reasons for exclusion
4. Resolve disagreements through discussion
5. Final included studies list
```

**PRISMA Flow Diagram**:
```
Identification:
  Records identified through database searching: n = 1,589
  Additional records through other sources: n = 12

Screening:
  Records after duplicates removed: n = 1,245
  Records screened: n = 1,245
  Records excluded: n = 1,089

Eligibility:
  Full-text articles assessed: n = 156
  Full-text articles excluded (with reasons): n = 98
    - Wrong population: 23
    - Wrong intervention: 31
    - Wrong outcome: 18
    - Wrong study design: 26

Included:
  Studies included in synthesis: n = 58
```

### Phase 4: Data Extraction

**Standardized Form**:
```markdown
## Study ID: [Author Year]

### Study Characteristics
- Authors:
- Year:
- Country:
- Study design:
- Sample size:
- Setting:

### Participants
- Population:
- Age (mean ± SD):
- Gender (% female):
- Inclusion criteria:
- Exclusion criteria:

### Intervention
- Intervention description:
- Control/comparison:
- Duration:
- Delivery method:

### Outcomes
- Primary outcome:
- Secondary outcomes:
- Measurement tools:
- Follow-up period:

### Results
- Primary outcome results:
- Effect size:
- Statistical significance:
- Secondary outcomes:

### Quality Assessment
- Risk of bias:
- Limitations:
- Funding source:
```

### Phase 5: Quality Assessment

**RCTs - Cochrane Risk of Bias Tool**:
```
Domains:
1. Random sequence generation
2. Allocation concealment
3. Blinding of participants/personnel
4. Blinding of outcome assessment
5. Incomplete outcome data
6. Selective reporting
7. Other bias

Rating: Low / Unclear / High risk
```

**Observational - Newcastle-Ottawa Scale**:
```
Selection (max 4 stars):
  - Representativeness of exposed cohort
  - Selection of non-exposed cohort
  - Ascertainment of exposure
  - Outcome not present at start

Comparability (max 2 stars):
  - Comparability on basis of design/analysis

Outcome (max 3 stars):
  - Assessment of outcome
  - Follow-up length adequate
  - Adequacy of follow-up

Quality: Good (7-9), Fair (4-6), Poor (0-3)
```

---

## Citation Analysis Techniques

### Backward Citation Chaining

Find what a paper cites:
```
1. Identify key paper on your topic
2. Review its reference list
3. Identify seminal/foundational works
4. Track down highly relevant references
5. Repeat for newly found papers
```

### Forward Citation Chaining

Find who cites a paper:
```
1. Identify seminal paper
2. Use "Cited by" in Google Scholar
3. Review papers that cite it
4. Identify recent developments
5. Find review papers
```

### Citation Metrics

**H-Index**: Author has h papers with ≥h citations each
- Higher h-index = more prolific and cited author

**Impact Factor**: Average citations per paper in journal
- Higher IF = more prestigious journal (generally)

**Citation Count**: Total times paper cited
- >100 citations = highly influential (field-dependent)
- >1000 citations = seminal work

**Citations per Year**: Citation count ÷ years since publication
- Identifies rising papers with growing impact

---

## Search Quality Assessment

### PRESS Checklist (Peer Review of Electronic Search Strategies)

Translation of concepts:
- [ ] All key concepts translated to search terms
- [ ] Synonyms and related terms included
- [ ] Spelling variations considered

Boolean operators:
- [ ] AND used to combine concepts
- [ ] OR used within concepts for synonyms
- [ ] NOT used appropriately (if at all)
- [ ] Parentheses group terms correctly

Subject headings:
- [ ] MeSH terms used (PubMed)
- [ ] Subject headings exploded appropriately
- [ ] Free-text terms supplement headings

Limits and filters:
- [ ] Date ranges specified
- [ ] Language limits appropriate
- [ ] Publication type filters justified
- [ ] Study design filters documented

---

## Source Quality Indicators

### Journal Quality

**Peer-Reviewed**: Most important indicator
- Published in peer-reviewed journal
- Undergone expert review process

**Impact Factor**: Journal prestige
- Higher IF generally better (but field-dependent)
- Check Journal Citation Reports

**Indexing**: Journal recognition
- Indexed in PubMed/MEDLINE
- Listed in major databases

**Open Access**: Accessibility
- Legitimate OA journals (PLOS, BMC, etc.)
- Beware predatory OA journals

### Predatory Journal Warning Signs

- ❌ Guaranteed rapid publication
- ❌ Minimal peer review
- ❌ Unknown editorial board
- ❌ Poor website quality
- ❌ Spam email solicitations
- ❌ Unclear publishing fees
- ❌ Not indexed in major databases

Check: Directory of Open Access Journals (DOAJ), Think Check Submit

### Paper Quality Indicators

**Strong Indicators**:
- ✅ High citation count (field-adjusted)
- ✅ Published in high-IF journal
- ✅ Clear methodology
- ✅ Adequate sample size
- ✅ Appropriate statistics
- ✅ Transparent reporting
- ✅ Funded by reputable source
- ✅ Author credentials strong

**Weak Indicators**:
- ❌ Very low/no citations (if not recent)
- ❌ Predatory journal
- ❌ Unclear methods
- ❌ Very small sample
- ❌ Missing data/statistics
- ❌ Conflicts of interest
- ❌ Retracted or corrected

---

## Grey Literature Sources

### Why Include Grey Literature

**Advantages**:
- Reduces publication bias
- Captures recent research
- Includes technical reports
- Provides context

**Disadvantages**:
- Not peer-reviewed (usually)
- Harder to locate
- Variable quality
- May lack detail

### Sources

**Dissertations and Theses**:
- ProQuest Dissertations & Theses
- EThOS (UK)
- DART-Europe
- Institutional repositories

**Conference Proceedings**:
- IEEE Xplore
- ACM Digital Library
- Conference websites
- ResearchGate

**Preprints**:
- arXiv (physics, CS, math)
- bioRxiv (biology)
- medRxiv (medicine)
- SSRN (social sciences)

**Technical Reports**:
- Government websites
- Think tank publications
- NGO reports
- Industry white papers

**Clinical Trial Registries**:
- ClinicalTrials.gov
- WHO ICTRP
- EU Clinical Trials Register

---

## Search Documentation Template

```markdown
# Literature Search Documentation

## Search Objective
[What are you searching for and why?]

## Databases Searched
1. Google Scholar
2. PubMed/MEDLINE
3. [Additional databases]

## Search Terms

### Concept 1: [Main concept]
- Term 1: [keyword]
- Term 2: [synonym]
- Term 3: [related term]

### Concept 2: [Secondary concept]
- Term 1: [keyword]
- Term 2: [synonym]

### Boolean Search String
```
([Concept 1 terms] OR [synonyms])
AND
([Concept 2 terms] OR [synonyms])
AND
[filters]
```

## Search Filters
- Date range: YYYY-YYYY
- Language: English
- Publication type: [Peer-reviewed articles]
- Study design: [If applicable]

## Search Results

| Database | Date | Search String | Results | Relevant |
|----------|------|---------------|---------|----------|
| Google Scholar | 2024-01-20 | [String] | 1,247 | 58 |
| PubMed | 2024-01-20 | [String] | 342 | 32 |

## Inclusion Criteria
- [Criterion 1]
- [Criterion 2]

## Exclusion Criteria
- [Criterion 1]
- [Criterion 2]

## Search Limitations
- [Any limitations to acknowledge]

## Reviewer
[Name, Date]
```

---

## Best Practices Checklist

### Before Searching

- [ ] Research question clearly defined
- [ ] Key concepts identified
- [ ] Synonyms and related terms listed
- [ ] Inclusion/exclusion criteria set
- [ ] Database selection justified
- [ ] Search strategy documented

### During Searching

- [ ] Multiple databases searched (minimum 3)
- [ ] Boolean operators used correctly
- [ ] Search strings tested and refined
- [ ] Results tracked systematically
- [ ] Date of each search recorded
- [ ] Search strings saved/documented

### After Searching

- [ ] Results exported with full citations
- [ ] Duplicates identified and removed
- [ ] Results organized by relevance
- [ ] Preliminary screening completed
- [ ] Full-text access verified
- [ ] Citation manager updated
- [ ] Search limitations acknowledged

### Quality Assurance

- [ ] Peer review of search strategy (PRESS)
- [ ] Test search retrieves known key papers
- [ ] Coverage adequate (not too narrow)
- [ ] Results manageable (not too broad)
- [ ] High-quality sources prioritized
- [ ] Predatory journals excluded

---

## Common Pitfalls to Avoid

**Too Broad**:
- ❌ "machine learning" → 1,000,000+ results
- ✅ "machine learning" AND "bias" AND "healthcare" after:2020 → 1,200 results

**Too Narrow**:
- ❌ Only one database, very specific terms
- ✅ Multiple databases, synonyms included

**Missing Synonyms**:
- ❌ Only "machine learning"
- ✅ "machine learning" OR "deep learning" OR "AI" OR "neural networks"

**Poor Boolean Logic**:
- ❌ machine learning AND bias OR healthcare (incorrect grouping)
- ✅ "machine learning" AND "bias" AND "healthcare"

**Not Documenting**:
- ❌ Random searches, no record
- ✅ Systematic documentation of all searches

**Ignoring Grey Literature**:
- ❌ Only peer-reviewed journals
- ✅ Include preprints, theses, conference papers

**No Quality Filter**:
- ❌ Include all results regardless of quality
- ✅ Assess source credibility and study quality

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: Academic research, systematic reviews, literature searches
