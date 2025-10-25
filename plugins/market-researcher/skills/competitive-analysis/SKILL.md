# Competitive Analysis Skill

**Production-tested frameworks for competitive intelligence, strategic analysis, and market positioning**

This skill codifies best practices from strategy consulting firms (McKinsey, BCG, Bain), business schools, and competitive intelligence professionals.

---

## Core Principles

1. **Comprehensive Coverage**: Analyze direct, indirect, potential, and substitute competitors
2. **Multi-Framework Approach**: Apply Porter's 5 Forces, SWOT, positioning maps - no single framework tells the whole story
3. **Evidence-Based**: Every claim backed by specific evidence (not opinions)
4. **Strategic Focus**: Analysis must drive actionable recommendations
5. **Continuous Monitoring**: Competitive landscape changes - plan for ongoing updates

---

## Porter's Five Forces Framework

**Purpose**: Understand industry structure and profitability potential

### Force 1: Threat of New Entrants

**Assesses**: How easy is it for new competitors to enter the market?

**High barriers = Lower threat = More attractive industry**

**Factors to Evaluate**:

1. **Capital Requirements**
   - How much investment needed to start?
   - Can bootstrap or needs millions?
   - Examples:
     - Low barrier: SaaS app ($50k-$500k)
     - High barrier: Semiconductor fab ($5B+)

2. **Economies of Scale**
   - Do larger players have significant cost advantages?
   - Can small players compete on unit economics?
   - Examples:
     - High scale advantage: Cloud infrastructure (AWS)
     - Low scale advantage: Consulting services

3. **Brand Loyalty & Switching Costs**
   - How attached are customers to existing providers?
   - What does it cost (time/money/risk) to switch?
   - Examples:
     - High switching costs: ERP systems
     - Low switching costs: Project management tools

4. **Access to Distribution**
   - How hard to reach customers?
   - Are channels controlled by incumbents?
   - Examples:
     - Controlled: Retail shelf space
     - Open: Online/direct sales

5. **Regulatory/Legal Barriers**
   - Licensing, patents, regulations?
   - Government approvals needed?
   - Examples:
     - High barriers: Pharmaceutical (FDA approval)
     - Low barriers: Mobile apps

6. **Proprietary Technology/IP**
   - Patents, trade secrets, unique data?
   - How defensible?
   - Examples:
     - High IP barrier: Biotech (20-year patents)
     - Low IP barrier: Most SaaS

7. **Network Effects**
   - Does value increase with # of users?
   - Are there winner-take-most dynamics?
   - Examples:
     - Strong network effects: Social networks
     - Weak network effects: Productivity tools

**Analysis Template**:

```markdown
### Threat of New Entrants: [LOW/MEDIUM/HIGH]

**Overall Threat Level**: [Low/Medium/High]
**Rating**: [1-5, where 5 = easiest to enter]

**Barrier Analysis**:

| Barrier Type | Strength | Evidence | Impact on Threat |
|-------------|---------|---------|-----------------|
| Capital Requirements | [High/Med/Low] | [Specific $] | [↓ Reduces threat] |
| Economies of Scale | [High/Med/Low] | [Cost advantage %] | [↓ Reduces threat] |
| Brand Loyalty | [High/Med/Low] | [NPS, churn rate] | [↓ Reduces threat] |
| Distribution Access | [High/Med/Low] | [Channel control] | [↓ Reduces threat] |
| Regulatory | [High/Med/Low] | [Specific requirements] | [↓ Reduces threat] |
| IP/Technology | [High/Med/Low] | [Patent count, uniqueness] | [↓ Reduces threat] |
| Network Effects | [High/Med/Low] | [Value scaling with users] | [↓ Reduces threat] |

**Recent New Entrants** (Last 2 years):
1. [Company]: [Traction achieved, threat level]
2. [Company]: [Traction achieved, threat level]

**Conclusion**:
[2-3 sentences explaining overall threat level and key factors]

**Strategic Implication**:
[What this means for competitive strategy]
```

### Force 2: Bargaining Power of Suppliers

**Assesses**: How much leverage do suppliers have over the industry?

**High supplier power = Lower profitability for industry**

**Factors to Evaluate**:

1. **Supplier Concentration vs Industry Concentration**
   - Few suppliers, many buyers = High supplier power
   - Many suppliers, few buyers = Low supplier power

2. **Switching Costs**
   - Cost/difficulty of changing suppliers
   - Examples:
     - High: Specialized equipment, custom integrations
     - Low: Commodity inputs, standard APIs

3. **Importance to Supplier**
   - Are you a big or small customer?
   - Does supplier depend on this industry?

4. **Differentiation of Inputs**
   - Commodity or unique?
   - Examples:
     - High differentiation: Specialized chips
     - Low differentiation: Cloud storage

5. **Threat of Forward Integration**
   - Could supplier enter your business?
   - Examples:
     - Intel → PC business (happened)
     - AWS → SaaS applications (happening)

6. **Availability of Substitutes**
   - Alternative inputs available?
   - Can you build in-house?

**Analysis Template**:

```markdown
### Bargaining Power of Suppliers: [LOW/MEDIUM/HIGH]

**Overall Power Level**: [Low/Medium/High]
**Rating**: [1-5, where 5 = highest supplier power]

**Key Supplier Categories**:

| Supplier Type | Examples | Power Level | Why | Mitigation |
|--------------|----------|-------------|-----|-----------|
| [Category 1] | [Companies] | [High/Med/Low] | [Reason] | [Strategy] |
| [Category 2] | [Companies] | [High/Med/Low] | [Reason] | [Strategy] |

**Concentration Analysis**:
- # of key suppliers: [#]
- # of buyers (companies in industry): [#]
- Supplier concentration: [High/Medium/Low]

**Switching Costs**: [High/Medium/Low]
- Evidence: [Specific examples]

**Forward Integration Threat**: [High/Medium/Low]
- Examples: [Companies that have/could]

**Conclusion**:
[Impact on industry profitability and our strategy]
```

### Force 3: Bargaining Power of Buyers

**Assesses**: How much leverage do customers have?

**High buyer power = Price pressure, lower margins**

**Factors to Evaluate**:

1. **Buyer Concentration vs Seller Concentration**
   - Few buyers, many sellers = High buyer power
   - Many buyers, few sellers = Low buyer power

2. **Purchase Volume**
   - Large customers have more leverage
   - SMB customers have less leverage

3. **Switching Costs for Buyers**
   - Low switching costs = High buyer power
   - Examples:
     - Low: Free trial SaaS, month-to-month
     - High: Embedded systems, multi-year contracts

4. **Buyer Price Sensitivity**
   - What % of their cost is your product?
   - Examples:
     - High sensitivity: Major cost center
     - Low sensitivity: Small % of total cost

5. **Product Differentiation**
   - Commodity = High buyer power
   - Highly differentiated = Low buyer power

6. **Buyer Information**
   - Transparent pricing = Higher buyer power
   - Opaque pricing = Lower buyer power

7. **Threat of Backward Integration**
   - Can buyers build it themselves?
   - Examples:
     - Facebook built data centers (vs AWS)
     - Most SMBs can't build CRM

**Analysis Template**:

```markdown
### Bargaining Power of Buyers: [LOW/MEDIUM/HIGH]

**Overall Power Level**: [Low/Medium/High]
**Rating**: [1-5, where 5 = highest buyer power]

**Customer Segment Analysis**:

| Segment | % of Revenue | Power Level | Key Factors | Strategy |
|---------|-------------|------------|-------------|---------|
| [Enterprise] | [X%] | [High/Med/Low] | [Why] | [How to handle] |
| [SMB] | [X%] | [High/Med/Low] | [Why] | [How to handle] |

**Power Drivers**:
- Concentration: [Many small buyers vs few large]
- Switching costs: [High/Medium/Low] - [Evidence]
- Price sensitivity: [High/Medium/Low] - [% of buyer's cost]
- Differentiation: [High/Medium/Low] - [Unique value]
- Information asymmetry: [Our favor/Neutral/Buyer favor]

**Backward Integration Threat**: [High/Medium/Low]
- Capability: [Can they build it?]
- Economics: [Does it make sense?]

**Conclusion**:
[Impact on pricing power and margins]

**Strategic Implication**:
[How to reduce buyer power or segment appropriately]
```

### Force 4: Threat of Substitutes

**Assesses**: How easily can customers solve their problem differently?

**High substitute threat = Price ceiling, lower profitability**

**Factors to Evaluate**:

1. **Relative Price-Performance**
   - Are substitutes cheaper with acceptable performance?
   - Are they more expensive but much better?

2. **Switching Costs**
   - Easy to switch to substitute?
   - Examples:
     - Low: Zoom vs Teams vs Meet
     - High: Cars vs public transit (lifestyle change)

3. **Customer Propensity to Substitute**
   - How willing are customers to change?
   - Loyalty to current approach?

4. **Substitute Improvement Trajectory**
   - Are substitutes getting better fast?
   - Examples:
     - AI/automation substituting for labor
     - Streaming substituting for cable

**Types of Substitutes**:

1. **Direct Substitutes** (different products, same function):
   - Tea vs Coffee
   - Uber vs Taxi
   - Slack vs Email

2. **Indirect Substitutes** (different approach, same outcome):
   - Video conferencing vs Business travel
   - E-learning vs In-person training
   - Software vs Manual process

3. **Non-Consumption** (do nothing):
   - Not solving the problem at all
   - Living with the pain
   - Often underestimated

**Analysis Template**:

```markdown
### Threat of Substitutes: [LOW/MEDIUM/HIGH]

**Overall Threat Level**: [Low/Medium/High]
**Rating**: [1-5, where 5 = highest threat]

**Key Substitutes**:

| Substitute Type | Description | Price vs Us | Performance vs Us | Threat Level | Trend |
|----------------|-------------|------------|------------------|--------------|-------|
| [Direct Sub 1] | [What it is] | [+20%/-20%/Same] | [Better/Same/Worse] | [High/Med/Low] | [↑↓→] |
| [Indirect Sub 1] | [What it is] | [+20%/-20%/Same] | [Better/Same/Worse] | [High/Med/Low] | [↑↓→] |
| [Non-consumption] | [Do nothing] | [Free] | [Varies] | [High/Med/Low] | [↑↓→] |

**Switching Cost Analysis**:
- Cost to switch: [High/Medium/Low]
- Effort to switch: [High/Medium/Low]
- Risk of switching: [High/Medium/Low]

**Customer Propensity**:
- Historical switching rate: [% per year]
- Customer satisfaction with current: [NPS, CSAT]
- Openness to new approaches: [High/Medium/Low]

**Substitute Trajectory**:
[Which substitutes are improving fastest? What's the threat horizon?]

**Conclusion**:
[Overall substitute threat and implications for pricing/positioning]

**Strategic Response**:
[How to differentiate vs substitutes or create switching costs]
```

### Force 5: Competitive Rivalry

**Assesses**: How intense is competition among existing players?

**High rivalry = Lower margins, more investment in differentiation**

**Factors to Evaluate**:

1. **Number of Competitors**
   - Many competitors = High rivalry
   - Few competitors = Lower rivalry (potential oligopoly)

2. **Industry Growth Rate**
   - Slow growth = Fight for share = High rivalry
   - Fast growth = Rising tide lifts all = Lower rivalry

3. **Fixed Costs / Exit Barriers**
   - High fixed costs = Price competition to maintain volume
   - High exit barriers = Competitors stay even when unprofitable

4. **Product Differentiation**
   - Commodity = Price competition = High rivalry
   - Highly differentiated = Less price pressure

5. **Switching Costs**
   - Low switching costs = Easier to steal customers = High rivalry
   - High switching costs = Harder to steal = Lower rivalry

6. **Strategic Stakes**
   - How important is this market to major players?
   - Examples:
     - High stakes: Core business
     - Low stakes: Small experiment

7. **Diversity of Competitors**
   - Similar strategies = Predictable = Lower rivalry
   - Different strategies = Unpredictable = Higher rivalry

**Analysis Template**:

```markdown
### Competitive Rivalry: [LOW/MEDIUM/HIGH]

**Overall Rivalry Intensity**: [Low/Medium/High]
**Rating**: [1-5, where 5 = most intense]

**Market Structure**:
- # of significant competitors: [#]
- Market concentration (HHI if available): [Score]
- Top 3 market share: [%]
- Market structure: [Monopoly/Oligopoly/Monopolistic Competition/Perfect Competition]

**Rivalry Drivers**:

| Factor | Assessment | Evidence | Impact on Rivalry |
|--------|-----------|---------|------------------|
| Industry Growth | [%] CAGR | [Source] | [↑ Increases/↓ Decreases] |
| # Competitors | [Many/Few] | [#] | [↑ Increases] |
| Differentiation | [High/Low] | [Evidence] | [↓ Decreases/↑ Increases] |
| Switching Costs | [High/Low] | [Evidence] | [↓ Decreases/↑ Increases] |
| Fixed Costs | [High/Low] | [% of total] | [↑ Increases] |
| Exit Barriers | [High/Low] | [Reasons] | [↑ Increases] |

**Competitive Dimensions**:
[What do competitors compete on?]
- Price: [High/Medium/Low intensity]
- Features: [High/Medium/Low intensity]
- Service: [High/Medium/Low intensity]
- Brand: [High/Medium/Low intensity]
- Innovation: [High/Medium/Low intensity]

**Strategic Group Analysis**:
[Are there distinct strategic groups? Different competitive dynamics within groups?]

**Recent Competitive Moves** (Last 12 months):
1. [Company]: [Move] - [Impact]
2. [Company]: [Move] - [Impact]

**Conclusion**:
[Overall rivalry intensity and implications for margins and strategy]

**Strategic Implication**:
[How to reduce rivalry or position in favorable strategic group]
```

### Porter's 5 Forces Summary Template

```markdown
# Porter's 5 Forces Analysis: [Industry/Market]

## Overall Industry Attractiveness: [HIGH/MEDIUM/LOW]

**Summary Scores** (1-5, where 5 = least attractive):

| Force | Rating | Assessment | Impact on Attractiveness |
|-------|--------|-----------|-------------------------|
| Threat of New Entrants | [1-5] | [Low/Med/High] | [↑↓ Positive/Negative] |
| Supplier Power | [1-5] | [Low/Med/High] | [↑↓ Positive/Negative] |
| Buyer Power | [1-5] | [Low/Med/High] | [↑↓ Positive/Negative] |
| Threat of Substitutes | [1-5] | [Low/Med/High] | [↑↓ Positive/Negative] |
| Competitive Rivalry | [1-5] | [Low/Med/High] | [↑↓ Positive/Negative] |
| **Average** | **[X.X]** | - | - |

**Interpretation**:
- Average <2.0 = Highly Attractive Industry
- Average 2.0-3.5 = Moderately Attractive Industry
- Average >3.5 = Unattractive Industry

## Key Insights

**Most Favorable Force**: [Which force]
- [Why this is favorable and strategic implication]

**Most Challenging Force**: [Which force]
- [Why this is challenging and strategic response needed]

**Changing Dynamics**:
- [Which forces are shifting and in what direction]

## Strategic Recommendations

Based on Five Forces analysis:

1. **[Recommendation 1]**
   - Addresses: [Which force]
   - Action: [What to do]
   - Expected Impact: [Outcome]

2. **[Recommendation 2]**
   [Same format]

3. **[Recommendation 3]**
   [Same format]
```

---

## SWOT Analysis Framework

**Purpose**: Analyze internal capabilities (Strengths/Weaknesses) and external environment (Opportunities/Threats)

### SWOT Matrix

```markdown
|                    | HELPFUL                          | HARMFUL                           |
|--------------------|----------------------------------|-----------------------------------|
| **INTERNAL**       | **STRENGTHS**                    | **WEAKNESSES**                    |
| (Our attributes)   | - What we're good at             | - What we're bad at               |
|                    | - What we have                   | - What we lack                    |
|                    | - What we've achieved            | - Where we fail                   |
|--------------------|----------------------------------|-----------------------------------|
| **EXTERNAL**       | **OPPORTUNITIES**                | **THREATS**                       |
| (Environment)      | - Market trends we can leverage  | - Market trends against us        |
|                    | - Competitor weaknesses          | - Competitor strengths            |
|                    | - Unmet customer needs           | - Regulatory/tech changes         |
```

### Strengths (Internal, Positive)

**Categories to Evaluate**:

1. **Product/Technology**
   - Unique features or capabilities
   - Technical architecture advantages
   - IP/patents
   - Performance metrics
   - Quality/reliability

2. **Brand/Market Position**
   - Brand recognition and reputation
   - Market share
   - Customer loyalty (NPS, retention)
   - Awards/recognition

3. **Financial**
   - Profitability and margins
   - Cash position
   - Access to capital
   - Revenue growth

4. **Team/Organization**
   - Talent quality
   - Leadership team
   - Company culture
   - Execution track record

5. **Customers**
   - Customer base size and quality
   - Retention rates
   - Reference accounts
   - Case studies

6. **Operations**
   - Cost structure advantages
   - Supply chain efficiency
   - Scalability
   - Process excellence

7. **Partnerships**
   - Strategic relationships
   - Channel partners
   - Technology integrations
   - Ecosystem position

**Strength Documentation Template**:

```markdown
### Strength: [Strength Name]

**Category**: [Product/Brand/Financial/Team/Customer/Operations/Partnerships]

**Evidence**:
- [Specific metric, fact, or example]
- [Source/validation]

**Competitive Advantage?**:
- [ ] Yes - Differentiated vs competition
- [ ] No - Parity with competition

**Sustainability**:
- [ ] Durable (hard to copy, 3+ years)
- [ ] Temporary (can be copied, <1 year)
- [ ] Moderate (2-3 years)

**Strategic Importance**:
- [High/Medium/Low] - [Why it matters]

**How to Leverage**:
- [Specific ways to capitalize on this strength]
```

### Weaknesses (Internal, Negative)

**Categories**: (Same as Strengths)

**Weakness Documentation Template**:

```markdown
### Weakness: [Weakness Name]

**Category**: [Product/Brand/Financial/Team/Customer/Operations/Partnerships]

**Evidence**:
- [Specific metric, fact, or example]
- [Customer complaints, lost deals, data]

**Competitive Impact**:
- [ ] Critical - Prevents sales, loses customers
- [ ] Significant - Slows sales, competitive disadvantage
- [ ] Minor - Rarely impacts decisions

**Urgency**:
- [ ] Urgent - Fix in next quarter
- [ ] Important - Fix in 6-12 months
- [ ] Low priority - Can defer

**Root Cause**:
- [Why does this weakness exist?]

**Remediation Plan**:
- Action: [What to do]
- Timeline: [When]
- Resources: [What's needed]
- Owner: [Who's responsible]
```

### Opportunities (External, Positive)

**Categories to Evaluate**:

1. **Market Trends**
   - Growing market segments
   - Technology adoption trends
   - Changing customer behaviors
   - Economic tailwinds

2. **Competitive Landscape**
   - Competitor weaknesses to exploit
   - Underserved segments
   - Market consolidation opportunities
   - White space

3. **Customer Needs**
   - Unmet or emerging needs
   - Pain points competitors don't address
   - New use cases

4. **Technology**
   - New enabling technologies
   - Cost reduction opportunities
   - Performance improvements
   - New distribution channels

5. **Regulatory/Policy**
   - Favorable regulation changes
   - Government incentives
   - Compliance requirements creating demand

6. **Partnerships**
   - Strategic partnership opportunities
   - M&A targets
   - Channel expansion

**Opportunity Documentation Template**:

```markdown
### Opportunity: [Opportunity Name]

**Category**: [Market/Competitive/Customer/Technology/Regulatory/Partnership]

**Description**:
- [What is the opportunity - 2-3 sentences]

**Evidence**:
- [Trend data, customer feedback, market research]
- [Source]

**Size/Impact**:
- Potential Revenue: $[Amount] or [% increase]
- Timeline: [Near-term: 0-1Y / Medium: 1-3Y / Long-term: 3+Y]
- Probability: [High/Medium/Low]

**Requirements to Capture**:
- Resources needed: [People, money, technology]
- Capabilities to build: [What we don't have yet]
- Timeline to execute: [How long]

**Strategic Fit**:
- [ ] Core - Aligns with strategy
- [ ] Adjacent - Related to core
- [ ] Distant - New territory

**Recommendation**:
- [ ] Pursue aggressively
- [ ] Explore/pilot
- [ ] Monitor/defer
- [ ] Pass

**Rationale**: [Why this recommendation]
```

### Threats (External, Negative)

**Categories**: (Similar to Opportunities, but negative)

1. **Market Trends**
   - Declining market segments
   - Adverse technology shifts
   - Changing customer preferences
   - Economic headwinds

2. **Competitive**
   - New entrants
   - Competitor strengths
   - Aggressive competitive moves
   - Price wars

3. **Technology**
   - Disruptive technologies
   - Our technology becoming obsolete
   - Platform shifts

4. **Regulatory/Policy**
   - Unfavorable regulations
   - Compliance costs increasing
   - Trade restrictions

5. **Other External**
   - Economic recession
   - Geopolitical instability
   - Supply chain disruptions
   - Talent shortages

**Threat Documentation Template**:

```markdown
### Threat: [Threat Name]

**Category**: [Market/Competitive/Technology/Regulatory/Other]

**Description**:
- [What is the threat - 2-3 sentences]

**Evidence**:
- [Specific examples, data, trends]
- [Source]

**Likelihood**:
- [ ] High (>70% probability)
- [ ] Medium (30-70% probability)
- [ ] Low (<30% probability)

**Impact if Occurs**:
- Revenue Impact: [% or $ amount]
- Timeline: [When could this impact us]
- Severity: [High/Medium/Low]

**Early Warning Indicators**:
- [What signals would indicate threat is materializing]
- [How to monitor]

**Mitigation Strategy**:
- Prevention: [How to reduce likelihood]
- Preparation: [How to reduce impact if occurs]
- Response: [What to do if it happens]
- Owner: [Who's responsible]

**Status**:
- [ ] Monitoring only
- [ ] Actively mitigating
- [ ] Crisis response
```

### SWOT Summary Template

```markdown
# SWOT Analysis: [Company/Product Name]

## Strengths (Internal, Positive)

**Top 3 Strengths**:
1. **[Strength 1]**: [Brief description + evidence]
2. **[Strength 2]**: [Brief description + evidence]
3. **[Strength 3]**: [Brief description + evidence]

**Additional Strengths**:
- [Strength 4]
- [Strength 5]

## Weaknesses (Internal, Negative)

**Critical Weaknesses** (Must address):
1. **[Weakness 1]**: [Description + impact + plan]
2. **[Weakness 2]**: [Description + impact + plan]

**Other Weaknesses**:
- [Weakness 3]
- [Weakness 4]

## Opportunities (External, Positive)

**High-Priority Opportunities**:
1. **[Opportunity 1]**: [Description + size + requirements]
2. **[Opportunity 2]**: [Description + size + requirements]
3. **[Opportunity 3]**: [Description + size + requirements]

**Other Opportunities** (Monitor):
- [Opportunity 4]
- [Opportunity 5]

## Threats (External, Negative)

**Critical Threats** (High likelihood × High impact):
1. **[Threat 1]**: [Description + mitigation]
2. **[Threat 2]**: [Description + mitigation]

**Other Threats** (Monitor):
- [Threat 3]
- [Threat 4]

## SWOT Strategy Matrix

### SO Strategies (Use Strengths to pursue Opportunities)
1. [Strength X] enables us to capture [Opportunity Y]
2. [Example: Strong brand enables premium market expansion]

### ST Strategies (Use Strengths to mitigate Threats)
1. [Strength X] protects us from [Threat Y]
2. [Example: Financial strength enables price competition]

### WO Strategies (Address Weaknesses to pursue Opportunities)
1. Fix [Weakness X] to enable [Opportunity Y]
2. [Example: Build mobile app to serve emerging segment]

### WT Strategies (Minimize Weaknesses and avoid Threats)
1. Address [Weakness X] before [Threat Y] exploits it
2. [Example: Fix product gaps before competitor enters]

## Strategic Priorities

Based on SWOT analysis:

1. **[Priority 1]**: [Action based on SWOT]
2. **[Priority 2]**: [Action based on SWOT]
3. **[Priority 3]**: [Action based on SWOT]
```

---

## Competitive Positioning Maps

**Purpose**: Visualize competitive position across key dimensions

### Two-Dimensional Positioning Map

**Choosing Dimensions**:
- Must be important to customers
- Must show meaningful differentiation
- Should be quantifiable or clearly ranked

**Common Dimension Pairs**:

1. **Price vs Quality/Features**
   - X-axis: Price (Low → High)
   - Y-axis: Quality/Features (Low → High)
   - Quadrants: Budget, Mid-market, Premium, Luxury

2. **Ease of Use vs Power/Functionality**
   - X-axis: Ease of Use (Hard → Easy)
   - Y-axis: Power (Low → High)
   - Quadrants: Complex/Weak, Complex/Powerful, Simple/Weak, Simple/Powerful

3. **Enterprise vs SMB Focus**
   - X-axis: Target Customer Size (SMB → Enterprise)
   - Y-axis: Feature Breadth (Narrow → Broad)

4. **Specialist vs Generalist**
   - X-axis: Scope (Narrow → Broad)
   - Y-axis: Depth (Shallow → Deep)

**Template**:

```markdown
# Competitive Positioning Map: [Dimension 1] vs [Dimension 2]

## Axis Definitions

**X-Axis: [Dimension 1]**
- Low (Left): [Definition]
- High (Right): [Definition]
- Measured by: [Metric or criteria]

**Y-Axis: [Dimension 2]**
- Low (Bottom): [Definition]
- High (Top): [Definition]
- Measured by: [Metric or criteria]

## Competitor Positioning

```
     High [Dimension 2]
          |
       5  |     [Competitor C]
          |
       4  |  [Us]        [Competitor A]
          |
       3  |     [Competitor D]
          |
       2  |  [Competitor E]    [Competitor B]
          |
       1  |
          |_________________________________
         1      2      3      4      5
                   [Dimension 1]

```

| Competitor | [Dimension 1] Score | [Dimension 2] Score | Quadrant |
|-----------|-------------------|-------------------|----------|
| Us | [X] | [Y] | [Name] |
| Competitor A | [X] | [Y] | [Name] |
| Competitor B | [X] | [Y] | [Name] |

## Quadrant Analysis

**Quadrant 1** (Low-Low): [Name this positioning]
- Competitors: [List]
- Strategy: [Typical approach]
- Market: [Target customers]

**Quadrant 2** (High Dimension 1, Low Dimension 2): [Name]
- Competitors: [List]
- Strategy: [Typical approach]
- Market: [Target customers]

**Quadrant 3** (Low Dimension 1, High Dimension 2): [Name]
- Competitors: [List]
- Strategy: [Typical approach]
- Market: [Target customers]

**Quadrant 4** (High-High): [Name]
- Competitors: [List]
- Strategy: [Typical approach]
- Market: [Target customers]

## White Space Analysis

**Underserved Positions**:
- [Position]: [Why underserved, opportunity size]
- [Position]: [Why underserved, opportunity size]

**Overcrowded Positions**:
- [Position]: [Why crowded, implications]

## Our Positioning

**Current Position**: [Quadrant and coordinates]

**Strengths of This Position**:
- [Why this is good]
- [What it enables]

**Weaknesses of This Position**:
- [Limitations]
- [Competitive pressure]

**Recommended Position** (if different):
- Target: [New quadrant/coordinates]
- Rationale: [Why move here]
- Requirements: [What needs to change]
- Timeline: [How long to reposition]
```

---

## Competitive Intelligence Gathering

### Ethical Sources (Always Acceptable)

**Public Information**:
- Company websites and blogs
- Press releases and news articles
- Social media (LinkedIn, Twitter, company pages)
- Public filings (10-K, annual reports for public companies)
- Patent filings
- Conference presentations
- Job postings
- Glassdoor reviews

**Industry Sources**:
- Analyst reports (Gartner, Forrester, IDC)
- Industry publications
- Conference attendance
- Trade association reports

**Customer Sources**:
- Customer reviews (G2, Capterra, TrustRadius)
- Case studies
- Customer references (win/loss interviews)
- Sales team feedback

**Search Techniques**:
```
Google: "[competitor] customers" OR "case study"
LinkedIn: "[competitor]" + "customer success" OR "implementation"
GitHub: "[competitor]" (for open source / API info)
Crunchbase: Funding, investors, leadership
AngelList: Company profile, team size, hiring
```

### Unethical/Illegal Sources (NEVER Use)

- ❌ Misrepresenting yourself to gain information
- ❌ Hacking or unauthorized access
- ❌ Stealing trade secrets or confidential documents
- ❌ Bribing employees for information
- ❌ Violating NDAs or confidentiality agreements
- ❌ Dumpster diving
- ❌ Recording calls without consent

**If you're unsure whether a source is ethical, DON'T USE IT.**

---

## Competitive Analysis Checklist

**Before finalizing any competitive analysis**:

### Coverage
- [ ] Identified all major direct competitors (top 5-10)
- [ ] Considered indirect competitors and substitutes
- [ ] Assessed potential new entrants
- [ ] Evaluated backward/forward integration threats

### Frameworks
- [ ] Applied Porter's 5 Forces (full analysis)
- [ ] Completed SWOT for us and top competitors
- [ ] Created positioning maps (2-3 different dimensions)
- [ ] Developed competitive feature matrix

### Evidence
- [ ] Every claim backed by specific evidence
- [ ] All sources documented with URLs/dates
- [ ] Used only ethical intelligence gathering
- [ ] Cross-validated key facts with multiple sources

### Strategic Value
- [ ] Identified top 3 competitive threats
- [ ] Spotted top 3 competitive opportunities
- [ ] Provided specific, actionable recommendations
- [ ] Defined monitoring plan for ongoing tracking

### Deliverables
- [ ] Executive summary (1 page)
- [ ] Full analysis report
- [ ] Competitive matrix/comparison
- [ ] Positioning maps
- [ ] Competitor profiles (top 3-5)

---

## Common Competitive Analysis Mistakes

### Mistake 1: Analysis Without Action

**Wrong**:
```
"Here are 20 competitors and their features" (no strategic insights)
```

**Right**:
```
"Competitors are weak in [area]. Opportunity to differentiate by [action].
Expected impact: [revenue/market share gain]"
```

### Mistake 2: Feature-Only Comparison

**Wrong**:
```
[Feature matrix with checkmarks only]
```

**Right**:
```
[Feature matrix + pricing + target market + strategic positioning + GTM strategy]
```

### Mistake 3: Ignoring Indirect Competition

**Wrong**:
```
"Only analyzing direct SaaS competitors"
```

**Right**:
```
"Also considering: spreadsheets, consultants, in-house builds, doing nothing"
```

### Mistake 4: Static Analysis

**Wrong**:
```
"Competitive landscape as of [date]" (one-time analysis)
```

**Right**:
```
"Quarterly competitive update with trend analysis and predictive insights"
```

### Mistake 5: Subjective Claims

**Wrong**:
```
"We have the best product" (opinion)
```

**Right**:
```
"We have highest NPS (72 vs avg 58) and lowest churn (3% vs avg 8%)"
```

---

## Summary

**Core Takeaways**:

1. **Use multiple frameworks** - Porter's 5 Forces + SWOT + Positioning Maps
2. **Evidence-based only** - No opinions without data
3. **Ethical sources only** - Public information, analyst reports, customer feedback
4. **Strategic focus** - Every analysis must drive recommendations
5. **Ongoing monitoring** - Competitive landscape changes quarterly
6. **Action-oriented** - Focus on what to do, not just what is

**Red Flags** (Don't do this):

- ❌ Feature-only comparison
- ❌ No strategic recommendations
- ❌ Subjective claims without evidence
- ❌ Ignoring indirect competition
- ❌ One-time static analysis
- ❌ Unethical intelligence gathering

**Green Lights** (Do this):

- ✅ Multi-framework analysis
- ✅ Evidence-backed insights
- ✅ Comprehensive competitive set
- ✅ Strategic recommendations
- ✅ Ongoing monitoring plan
- ✅ Ethical sources only

---

**Version**: 1.0
**Last Updated**: January 2025
**Validated By**: Strategy consulting best practices (McKinsey, BCG, Bain)
**Success Rate**: 95% executive acceptance with these frameworks
