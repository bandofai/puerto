# Pipeline Analysis Skill

This skill contains comprehensive frameworks, methodologies, and best practices for sales pipeline analysis, forecasting, risk identification, and performance tracking. It is based on patterns from thousands of B2B sales scenarios across SaaS, Enterprise, and Mid-Market segments.

**Usage**: Read this entire skill before performing ANY pipeline analysis task to ensure consistent, professional quality.

---

## Table of Contents

1. [Pipeline Health Monitoring](#1-pipeline-health-monitoring)
2. [Deal Risk Identification](#2-deal-risk-identification)
3. [Forecasting Models](#3-forecasting-models)
4. [Win/Loss Analysis](#4-winloss-analysis)
5. [Performance Metrics Tracking](#5-performance-metrics-tracking)
6. [Data Analysis Techniques](#6-data-analysis-techniques)
7. [Report Templates & Formats](#7-report-templates--formats)
8. [Integration Patterns](#8-integration-patterns)

---

## 1. Pipeline Health Monitoring

### 1.1 Pipeline Coverage Metrics

**Pipeline Coverage Ratio** = Total Pipeline Value / Quota

**Recommended Coverage by Stage**:
- **Early Stage (Lead, Qualification)**: 5-10x quota
- **Mid Stage (Discovery, Demo)**: 3-5x quota
- **Late Stage (Proposal, Negotiation)**: 2-3x quota
- **Overall Pipeline**: 3-4x quota (weighted average)

**Why Coverage Matters**:
- Accounts for natural attrition (not all deals close)
- Provides buffer for slippage and push
- Indicates pipeline generation health

**Health Indicators**:
- 🟢 **GREEN**: Coverage >3.5x quota
- 🟡 **YELLOW**: Coverage 2.5-3.5x quota
- 🔴 **RED**: Coverage <2.5x quota

**Example Calculation**:
```
Quota: $1M
Current Pipeline: $2.8M
Coverage Ratio: 2.8x (YELLOW - below 3x target)

Action: Pipeline generation sprint needed
```

### 1.2 Pipeline Velocity

**Pipeline Velocity** = Average days a deal spends in each stage

**Benchmark Velocity by Stage** (B2B SaaS):
- Lead: 1-3 days
- Qualification: 3-7 days
- Discovery: 7-14 days
- Demo: 7-14 days
- Proposal: 14-21 days
- Negotiation: 14-30 days
- Contracting: 7-14 days

**Total Sales Cycle**: 60-120 days (depending on deal size and complexity)

**Velocity Trends**:
- **Accelerating**: Deals moving faster (good sign - engaged buyers)
- **Decelerating**: Deals slowing down (warning sign - lack of urgency)
- **Stalled**: Deals stuck >2x average days (risk of loss)

**Example Analysis**:
```
Stage: Proposal
Average Days: 28 days (Benchmark: 14-21 days)
Trend: +40% slower than benchmark

Diagnosis: Proposals sitting too long
Root Causes: Weak MEDDIC, no champion, competing priorities
Actions: Qualification coaching, champion identification
```

### 1.3 Stage Conversion Rates

**Conversion Rate** = (Deals advanced to next stage / Total deals in stage) × 100%

**Benchmark Conversion Rates** (B2B SaaS):
- Lead → Qualification: 30-40%
- Qualification → Discovery: 50-60%
- Discovery → Demo: 60-70%
- Demo → Proposal: 40-50%
- Proposal → Negotiation: 50-60%
- Negotiation → Closed-Won: 60-70%

**Overall Win Rate** (Lead → Closed-Won): 5-15%

**How to Use Conversion Rates**:
1. Identify weak stages (below benchmark)
2. Root cause analysis (why deals drop off)
3. Targeted coaching and process improvement
4. Forecast future pipeline based on historical conversion

**Example**:
```
Demo → Proposal Conversion: 25% (Benchmark: 40-50%)

Analysis:
- 40 demos conducted in Q1
- Only 10 advanced to proposal (25%)
- Expected: 16-20 proposals (40-50%)

Root Cause Investigation:
- Review demo quality (script, customization, engagement)
- Check qualification (are we demoing unqualified leads?)
- Analyze objections (what blockers emerge after demo?)

Action Plan:
- Demo training for reps
- Strengthen pre-demo qualification
- Objection handling playbook
```

### 1.4 Deal Aging Analysis

**Aging Categories**:
- **On Track**: Within average days for stage
- **Aging**: 1.5-2x average days for stage
- **Stale**: >2x average days for stage
- **Dead**: >3x average days (recommend disqualify)

**Aging Impact on Win Rate**:
- On Track Deals: 40-50% win rate
- Aging Deals: 20-30% win rate
- Stale Deals: 5-10% win rate
- Dead Deals: <5% win rate

**Stale Deal Protocol**:
1. Identify all stale deals (>2x average days)
2. Assign category:
   - **Revive**: High potential, need re-engagement plan
   - **Monitor**: Medium potential, wait for buyer timing
   - **Disqualify**: Low potential, clean up pipeline
3. Execute action plan within 7 days

**Example**:
```
Deal: Beta Industries
Stage: Proposal
Days in Stage: 42 days (Average: 18 days)
Category: STALE (2.3x average)

Historical Data: Stale proposals have 8% win rate

Action: Disqualify OR aggressive re-engagement
Decision Criteria:
- MEDDIC Score >70: Revive
- MEDDIC Score 50-70: Monitor
- MEDDIC Score <50: Disqualify
```

### 1.5 Pipeline Quality Indicators

**High-Quality Pipeline Characteristics**:
- Strong BANT/MEDDIC scores (>70)
- Economic Buyer engaged
- Champion identified
- Clear decision process and timeline
- Active engagement (meetings, responses)
- Aligned to ICP (Ideal Customer Profile)

**Quality Metrics**:

**Average Deal Size by Stage**:
- Track ACV (Annual Contract Value) by stage
- Flag unusually small deals (below minimum viable)
- Flag unusually large deals (may have longer cycles)

**Win Rate by Source**:
- Inbound vs. Outbound
- Marketing vs. Sales-sourced
- Channel partner vs. Direct
- Referral vs. Cold outreach

**Qualification Score Distribution**:
- What % of pipeline has MEDDIC >70?
- What % of pipeline has MEDDIC <50?
- Are we advancing unqualified deals?

**Champion/EB Engagement Levels**:
- % of deals with Economic Buyer engaged
- % of deals with Champion identified
- Correlation between engagement and win rate

**Example Quality Report**:
```
Pipeline Quality Assessment - Q1 2025

Total Pipeline: $4.2M (78 deals)

Quality Breakdown:
- High Quality (MEDDIC >70): $1.8M (43%) - 55% win rate
- Medium Quality (MEDDIC 50-70): $1.6M (38%) - 30% win rate
- Low Quality (MEDDIC <50): $0.8M (19%) - 10% win rate

Insights:
- 57% of pipeline has EB engaged (good)
- Only 34% has Champion identified (need improvement)
- Inbound deals have 2x win rate vs. Outbound

Actions:
- Champion identification training
- Focus on inbound pipeline generation
- Consider disqualifying low-quality deals (<50 MEDDIC)
```

### 1.6 Pipeline Health Scoring Framework

**Composite Health Score** (0-100):

**Formula**:
```
Health Score = (Coverage × 30) + (Velocity × 25) + (Conversion × 25) + (Quality × 20)

Where:
- Coverage = Pipeline/Quota ratio (capped at 1.0 for 4x)
- Velocity = 1 - (Avg Days / Benchmark Days) (capped at 0-1)
- Conversion = Avg stage conversion rate / Benchmark rate (capped at 1.0)
- Quality = % of pipeline with MEDDIC >70
```

**Health Score Interpretation**:
- 🟢 **80-100**: EXCELLENT - Healthy pipeline, on track to quota
- 🟡 **60-79**: GOOD - Adequate pipeline, some areas need attention
- 🟠 **40-59**: FAIR - Pipeline at risk, immediate action needed
- 🔴 **0-39**: POOR - Pipeline in crisis, major intervention required

**Example Calculation**:
```
Coverage: 3.2x quota → 0.80 (3.2/4.0)
Velocity: 45 days avg vs. 40 benchmark → 0.88 (1 - 0.125)
Conversion: 42% avg vs. 50% benchmark → 0.84 (42/50)
Quality: 48% pipeline MEDDIC >70 → 0.48

Health Score = (0.80 × 30) + (0.88 × 25) + (0.84 × 25) + (0.48 × 20)
             = 24 + 22 + 21 + 9.6
             = 76.6 (GOOD - Yellow)

Interpretation: Pipeline is adequate but quality needs improvement
Priority: Champion identification and qualification training
```

---

## 2. Deal Risk Identification

### 2.1 Risk Scoring Framework

**Risk Score** = Quantitative Signals (50%) + Qualitative Signals (50%)

**Risk Categories**:
- 🟢 **LOW RISK** (0-30): Strong deal, likely to close
- 🟡 **MEDIUM RISK** (31-60): Some concerns, monitor closely
- 🟠 **HIGH RISK** (61-80): Significant issues, intervention needed
- 🔴 **CRITICAL RISK** (81-100): Likely to slip or lose, urgent action

### 2.2 Quantitative Risk Signals (50 points)

**1. MEDDIC/BANT Score (20 points)**:
- MEDDIC >80: 0 points (low risk)
- MEDDIC 60-80: 10 points (medium risk)
- MEDDIC 40-60: 15 points (high risk)
- MEDDIC <40: 20 points (critical risk)

**2. Deal Aging (15 points)**:
- On track (<1.5x avg): 0 points
- Aging (1.5-2x avg): 8 points
- Stale (2-3x avg): 12 points
- Dead (>3x avg): 15 points

**3. Momentum (10 points)**:
- Accelerating (activity increasing): 0 points
- Steady (consistent activity): 3 points
- Slowing (activity decreasing): 7 points
- Stalled (no activity >14 days): 10 points

**4. Budget Alignment (5 points)**:
- Budget approved: 0 points
- Budget likely: 2 points
- Budget uncertain: 4 points
- No budget: 5 points

### 2.3 Qualitative Risk Signals (50 points)

**1. Economic Buyer Engagement (15 points)**:
- EB fully engaged: 0 points
- EB met, not engaged: 8 points
- EB identified, not met: 12 points
- EB unknown: 15 points

**2. Champion Status (15 points)**:
- Strong champion (active advocate): 0 points
- Weak champion (supportive but passive): 8 points
- Coach (helpful but not champion): 12 points
- No champion: 15 points

**3. Competition (10 points)**:
- No competition (sole vendor): 0 points
- Weak competition: 3 points
- Strong competition: 7 points
- Incumbent advantage: 10 points

**4. Decision Process (5 points)**:
- Clear process and timeline: 0 points
- Defined but vague timeline: 2 points
- Undefined process: 4 points
- No decision process: 5 points

**5. Proposal Response (5 points)**:
- Positive feedback: 0 points
- Neutral/no feedback: 3 points
- Negative feedback: 5 points
- No response >14 days: 5 points

### 2.4 Common Risk Patterns and Mitigation

**Risk Pattern 1: No Economic Buyer Access**
- **Impact**: 35% drop in win rate
- **Signals**: Only speaking to mid-level managers, budget authority unclear
- **Mitigation**:
  - Request EB meeting through champion
  - Create executive briefing for EB
  - Escalate to your VP/C-level for peer outreach
  - If no EB access after 30 days → disqualify

**Risk Pattern 2: Decision Date Keeps Slipping**
- **Impact**: 50% less likely to close (ever)
- **Signals**: Close date moved 2+ times, vague reasons ("timing", "priorities")
- **Mitigation**:
  - Identify true blocker (budget, authority, need, urgency)
  - Reset expectations with concrete next steps
  - Create urgency with business case/ROI
  - Consider moving to "Nurture" vs. active pipeline

**Risk Pattern 3: No Champion Identified**
- **Impact**: 40% drop in win rate
- **Signals**: No internal advocate, selling to committee
- **Mitigation**:
  - Identify potential champions (who benefits most?)
  - Provide champion with ammunition (ROI, case studies)
  - Build champion through value delivery (insights, tools)
  - If no champion after Discovery → high risk

**Risk Pattern 4: Poor MEDDIC/BANT Scores (<60)**
- **Impact**: 75% less likely to close
- **Signals**: Qualification gaps, unvalidated assumptions
- **Mitigation**:
  - Re-qualify the deal (MEDDIC deep dive)
  - Address gaps through targeted discovery
  - If gaps can't be closed → disqualify
  - Coach rep on qualification

**Risk Pattern 5: Long Silence Periods (>14 days)**
- **Impact**: 60% slip rate
- **Signals**: No response to emails/calls, ghosting
- **Mitigation**:
  - Multi-threaded outreach (contact multiple stakeholders)
  - Value-add touchpoint (not just "checking in")
  - Escalate to executive sponsor
  - If no response after 3 attempts → move to "Nurture"

**Risk Pattern 6: Procurement/Legal Delays**
- **Impact**: 20% slip rate, 30-60 day delays
- **Signals**: "Needs legal review", "procurement process"
- **Mitigation**:
  - Engage procurement early (before proposal)
  - Provide standard contract/MSA upfront
  - Identify non-negotiable terms early
  - Build procurement timeline into forecast

**Risk Pattern 7: Price Objections After Proposal**
- **Impact**: 45% loss rate if price is surprise
- **Signals**: "Too expensive", "Budget is lower"
- **Mitigation**:
  - Re-anchor on value and ROI
  - Explore multi-year or payment terms
  - Offer phased approach or lower tier
  - If budget truly insufficient → disqualify or stage reduction

**Risk Pattern 8: Multiple Proposal Revisions (>3)**
- **Impact**: 30% loss rate (decision fatigue, weak qualification)
- **Signals**: Constant changes to scope, pricing, terms
- **Mitigation**:
  - Identify true decision criteria
  - Set expectations ("this is our final proposal")
  - Walk away if requirements keep changing
  - Often indicates no real budget or authority

### 2.5 Risk Assessment Template

**For Each At-Risk Deal**:

```markdown
# Deal Risk Assessment: [Company Name]

## Risk Level: [LOW/MEDIUM/HIGH/CRITICAL]

## Deal Overview
- Amount: $XXX
- Stage: [Current Stage]
- Age: XX days (Avg: XX days)
- Close Date: YYYY-MM-DD (XX days out)
- Owner: [Rep Name]

## Risk Score: XX/100

### Quantitative Signals (XX/50)
- MEDDIC Score: XX/100 → XX points
- Deal Aging: XX days vs. XX avg → XX points
- Momentum: [Accelerating/Steady/Slowing/Stalled] → XX points
- Budget: [Approved/Likely/Uncertain/None] → XX points

### Qualitative Signals (XX/50)
- EB Engagement: [Status] → XX points
- Champion: [Status] → XX points
- Competition: [Status] → XX points
- Decision Process: [Status] → XX points
- Proposal Response: [Status] → XX points

## Historical Context
- Similar deals (MEDDIC XX-XX): XX% win rate
- Deals with [key risk pattern]: XX% win rate

## Recommended Actions
1. [Immediate action - this week]
2. [Short-term action - next 2 weeks]
3. [If no progress - disqualify or escalate]

## Forecast Impact
- Current Category: [Commit/Best Case/Pipeline/Omitted]
- Recommended Category: [Category] (XX% probability)
```

---

## 3. Forecasting Models

### 3.1 Forecast Categories

**Forecast Segmentation** (based on win probability):

**COMMIT** (90-100% confidence):
- Criteria:
  - Verbal or written commitment from EB
  - Contract in legal/procurement review
  - MEDDIC score >85
  - All steps completed, just awaiting signature
- Typical Stages: Negotiation (late), Contracting
- Historical Accuracy: 85-95% of Commit deals close

**BEST CASE** (70-89% confidence):
- Criteria:
  - Strong MEDDIC score (70-85)
  - Economic Buyer engaged
  - Champion identified
  - Proposal delivered with positive feedback
- Typical Stages: Proposal, Negotiation (early)
- Historical Accuracy: 65-75% of Best Case deals close

**PIPELINE** (30-69% confidence):
- Criteria:
  - Qualified opportunity (MEDDIC 50-70)
  - Active engagement
  - Discovery/Demo completed
  - Some risk or qualification gaps
- Typical Stages: Discovery, Demo, Proposal (early)
- Historical Accuracy: 30-50% of Pipeline deals close

**OMITTED** (<30% confidence):
- Criteria:
  - Weak qualification (MEDDIC <50)
  - Stale or stalled deals
  - Unresponsive buyer
  - Significant risks
- Action: Exclude from forecast, clean up or nurture
- Historical Accuracy: <20% of Omitted deals close

### 3.2 Forecast Calculation Methods

**Method 1: Stage-Based Probability**

Assign probability by stage:
- Lead: 5%
- Qualification: 10%
- Discovery: 20%
- Demo: 30%
- Proposal: 50%
- Negotiation: 75%
- Contracting: 90%

**Formula**: Weighted Forecast = Σ (Deal Value × Stage Probability)

**Example**:
```
Deal 1: $100K, Demo stage → $100K × 30% = $30K
Deal 2: $200K, Proposal stage → $200K × 50% = $100K
Deal 3: $150K, Negotiation stage → $150K × 75% = $112.5K

Weighted Forecast = $30K + $100K + $112.5K = $242.5K
```

**Pros**: Simple, consistent, easy to calculate
**Cons**: Doesn't account for deal quality, all deals treated same

**Method 2: MEDDIC/BANT-Enhanced Probability**

Adjust stage probability based on qualification score:

**Formula**: Adjusted Probability = Stage Probability × (MEDDIC Score / 70)

**Example**:
```
Deal 1: $100K, Demo (30%), MEDDIC 84
  Adjusted Probability = 30% × (84/70) = 36%
  Weighted Value = $100K × 36% = $36K

Deal 2: $200K, Proposal (50%), MEDDIC 56
  Adjusted Probability = 50% × (56/70) = 40%
  Weighted Value = $200K × 40% = $80K

Deal 3: $150K, Negotiation (75%), MEDDIC 91
  Adjusted Probability = 75% × (91/70) = 97% (cap at 95%)
  Weighted Value = $150K × 95% = $142.5K

Weighted Forecast = $36K + $80K + $142.5K = $258.5K
```

**Pros**: More accurate, accounts for deal quality
**Cons**: Requires MEDDIC data, more complex

**Method 3: AI/ML-Enhanced Probability**

Use historical data and machine learning to predict win probability:

**Inputs**:
- MEDDIC score
- Deal age and velocity
- Engagement metrics (meetings, emails, responses)
- Qualification source (inbound vs. outbound)
- Industry and deal size
- Rep performance history

**Output**: Win probability (0-100%)

**Pros**: Most accurate, learns from historical patterns
**Cons**: Requires significant historical data, complex implementation

**Recommended Approach**: Start with Method 2 (MEDDIC-Enhanced), evolve to Method 3 as data accumulates

### 3.3 Forecast Accuracy Tracking

**Measure Forecast Accuracy**:

**Formula**: Forecast Accuracy = (Actual Closed Revenue / Forecasted Revenue) × 100%

**Targets**:
- **Commit Forecast**: 90-95% accuracy
- **Best Case Forecast**: 70-80% accuracy
- **Pipeline Forecast**: 40-60% accuracy

**Track by**:
- Rep (who's accurate, who's sandbagging/overforecasting)
- Stage (which stages have best/worst accuracy)
- Segment (SMB vs. Mid-Market vs. Enterprise)
- Time period (monthly, quarterly)

**Example Accuracy Report**:
```
Q1 2025 Forecast Accuracy

Commit Forecast:
- Forecasted: $800K
- Actual: $720K
- Accuracy: 90% ✓ (Target: 90-95%)

Best Case Forecast:
- Forecasted: $1.2M
- Actual: $900K
- Accuracy: 75% ✓ (Target: 70-80%)

Pipeline Forecast:
- Forecasted: $2.5M
- Actual: $1.1M
- Accuracy: 44% ✓ (Target: 40-60%)

Insights:
- Rep A: 95% accuracy (excellent)
- Rep B: 65% accuracy (overforecasting, needs coaching)
- Negotiation stage: 88% accuracy (best)
- Demo stage: 42% accuracy (worst - qualification issue)
```

### 3.4 Slippage and Push Analysis

**Slippage** = Deals that didn't close on expected date

**Push** = Deals moved to future period

**Track**:
- % of deals that slip each period
- Average days slipped
- Reasons for slippage (procurement, budget, decision delay)
- Which deals slip most (stages, reps, deal types)

**Slippage Patterns**:
- **Early-stage slips** (Discovery, Demo): Usually qualification issues
- **Late-stage slips** (Proposal, Negotiation): Usually procurement, legal, budget timing
- **Repeat slips** (>2 times): High risk of never closing

**Example Slippage Report**:
```
Q1 Slippage Analysis

Total Deals Forecasted to Close: 45
Actually Closed: 32 (71%)
Slipped to Q2: 10 (22%)
Lost: 3 (7%)

Slippage Breakdown:
- Procurement delays: 4 deals (40%)
- Budget timing: 3 deals (30%)
- Decision pushed: 2 deals (20%)
- Legal review: 1 deal (10%)

Slippage by Rep:
- Rep A: 1/10 deals slipped (10% - excellent)
- Rep B: 4/12 deals slipped (33% - needs qualification coaching)
- Rep C: 5/15 deals slipped (33% - over-optimistic forecasting)

Actions:
- Earlier procurement engagement (reduce delays)
- Budget timing validation in qualification
- Forecast coaching for Rep B and C
```

### 3.5 Forecast Report Template

```markdown
# Sales Forecast: [Period]

**Generated**: YYYY-MM-DD
**Quota**: $X.XM
**Coverage**: X.Xx

## Executive Summary

[1-2 sentence summary: on track, at risk, key concerns]

## Forecast Breakdown

### Commit (90-100% confidence)
- **Forecasted Revenue**: $XXX (XX% of quota)
- **Deal Count**: XX deals
- **Top 5 Deals**: [List with amounts, close dates]
- **Risk**: [Any concerns even in Commit?]

### Best Case (70-89% confidence)
- **Forecasted Revenue**: $XXX (XX% of quota)
- **Deal Count**: XX deals
- **Top 5 Deals**: [List with amounts, close dates]
- **Upside**: [Which could move to Commit?]
- **Risk**: [Which could slip?]

### Pipeline (30-69% confidence)
- **Forecasted Revenue**: $XXX (XX% of quota)
- **Deal Count**: XX deals
- **Upside**: [Which could accelerate?]

### Total Forecast
- **Commit**: $XXX
- **Commit + Best Case**: $XXX (XX% of quota)
- **Commit + Best + Pipeline**: $XXX (XX% of quota)

## Forecast vs. Quota

- **Gap to Quota**: $XXX (need XX% more)
- **Path to Quota**: [What needs to happen?]
  - Move X deals from Best Case to Commit
  - Accelerate X deals from Pipeline to Best Case
  - Add $XXX new pipeline

## Changes from Last Week

**Moved UP** (more confident):
- [Deal Name]: Pipeline → Best Case (MEDDIC improved to 78)

**Moved DOWN** (less confident):
- [Deal Name]: Best Case → Pipeline (EB not engaged)

**NEW Deals** (added to forecast):
- [Deal Name]: $XXX, [Stage], [Category]

**Slipped Deals** (pushed to next period):
- [Deal Name]: $XXX (Reason: procurement delay)

**Lost Deals**:
- [Deal Name]: $XXX (Reason: lost to Competitor X)

## Forecast Accuracy (Historical)

- **Last Month**: XX% accuracy
- **Last Quarter**: XX% accuracy
- **Trend**: [Improving/Declining/Stable]

## Recommended Actions

1. [Immediate priority - this week]
2. [Short-term priority - next 2 weeks]
3. [Pipeline generation needs]
```

---

## 4. Win/Loss Analysis

### 4.1 Win/Loss Post-Mortem Framework

**Conduct Win/Loss Reviews** for:
- ✅ All deals >$50K (adjust threshold based on your business)
- ✅ All competitive losses (understand why competitor won)
- ✅ Surprising wins (we expected to lose but won)
- ✅ Surprising losses (we expected to win but lost)

**Timing**: Within 7 days of deal closing (win or loss)

**Information Sources**:
- Rep debrief (their perspective)
- Customer feedback (if possible - win or loss interview)
- CRM data (MEDDIC scores, activity timeline)
- Proposal and technical documentation
- Qualification and engagement history

### 4.2 Win Reasons

**Common Win Reasons** (rank by frequency):

1. **Product Fit** (40%):
   - Our solution best matched their requirements
   - Features they needed that competitors lacked
   - Technical superiority

2. **Value/ROI** (25%):
   - Best business case and ROI
   - Compelling cost savings or revenue impact
   - Fastest payback period

3. **Relationship/Trust** (15%):
   - Strong champion and EB relationships
   - Trusted brand or existing relationship
   - Sales process and responsiveness

4. **Services/Support** (10%):
   - Better implementation support
   - Superior customer success
   - Training and enablement

5. **Pricing** (10%):
   - Most competitive pricing
   - Flexible payment terms
   - Best value for money (not necessarily cheapest)

**Example Win Analysis**:
```
Win: Acme Manufacturing - $350K

Primary Win Reason: Product Fit (60%)
- Only vendor with real-time predictive maintenance
- Integration with their legacy SCADA system
- Proven results in manufacturing vertical

Secondary Win Reason: Value/ROI (30%)
- ROI analysis showed 14-month payback
- Projected $1.2M savings over 3 years
- Beat competitor ROI by 35%

Tertiary Win Reason: Relationship (10%)
- Strong champion in VP Operations
- Referenced by existing customer in same industry
- Responsive sales process

Key Success Factors:
- Early champion identification
- Customized demo with their data
- Compelling ROI analysis from sales-engineer
- Strong qualification (MEDDIC 87)

Replicability:
✅ Product fit (manufacturingtarget market)
✅ ROI-led sales approach
✅ Champion development strategy
✅ Industry-specific case studies
```

### 4.3 Loss Reasons

**Common Loss Reasons** (rank by frequency):

1. **Lost to Competitor** (35%):
   - Competitor had better product fit
   - Incumbent advantage (switching costs)
   - Competitor had stronger relationships
   - Outpriced by competitor

2. **No Decision** (30%):
   - Budget cut or frozen
   - Competing priorities changed
   - Lost champion or EB support
   - Decision fatigue (too complex)

3. **Price** (15%):
   - Too expensive vs. perceived value
   - Budget constraints
   - Cheaper alternative acceptable

4. **Timing** (10%):
   - Not urgent enough
   - Other initiatives took priority
   - Budget timing (fiscal year)

5. **Product Gaps** (10%):
   - Missing required features
   - Technical limitations
   - Integration challenges

**Example Loss Analysis**:
```
Loss: Beta Healthcare - $280K

Primary Loss Reason: Lost to Competitor (70%)
- Lost to Incumbent (Vendor X)
- Switching costs were barrier
- Their EB had existing relationship with Vendor X

Secondary Loss Reason: No Decision (20%)
- Decision timeline kept slipping
- Champion left company mid-process
- Competing IT priorities emerged

Contributing Factors (10%):
- Our pricing was 15% higher
- Missing one feature (HIPAA audit logs)

Root Cause Analysis:
❌ Weak qualification (MEDDIC was 54)
❌ No Economic Buyer access until late
❌ Didn't identify incumbent early enough
❌ No multi-threading (only 1 champion)

What We Could Have Done Differently:
1. Earlier discovery of incumbent and switching costs
2. Built business case for switch (ROI to overcome inertia)
3. Multi-threaded to reduce champion risk
4. Engaged EB earlier with executive sponsor
5. Should have disqualified after MEDDIC assessment

Lessons Learned:
- Always discover incumbent situation early
- Build switching cost mitigation into proposal
- Multi-thread to avoid champion risk
- Respect qualification - MEDDIC <60 = high loss rate
```

### 4.4 Competitive Intelligence

**Track Win/Loss by Competitor**:

```markdown
## Competitive Win/Loss Matrix

| Competitor | Wins | Losses | Win Rate | Notes |
|------------|------|--------|----------|-------|
| Competitor A | 12 | 8 | 60% | Strong in Enterprise, weak in SMB |
| Competitor B | 5 | 15 | 25% | Incumbent advantage, but aging product |
| Competitor C | 8 | 4 | 67% | Price leader, feature gaps |

## Competitive Battlecards (When We Win/Lose)

### vs. Competitor A
**When We Win**:
- Mid-Market and SMB deals (easier buying process)
- Modern tech stack requirements (our API > theirs)
- Speed of implementation (we're 2x faster)

**When We Lose**:
- Enterprise deals (their brand, established processes)
- Existing Comp A customers (high switching costs)
- Global requirements (we're not in APAC yet)

**Recommendations**:
- Target Mid-Market vs. Enterprise for now
- Build APAC presence for Enterprise expansion
- Emphasize modern API and faster implementation

### vs. Competitor B
**When We Win**:
- Almost always (86% win rate when head-to-head)
- Product superiority is clear
- Younger, more innovative company narrative

**When We Lose**:
- Only when incumbent (switching cost inertia)

**Recommendations**:
- Aggressively target Comp B customers for rip-replace
- Build switching ROI calculator
- Case studies of migrations from Comp B
```

### 4.5 Pattern Recognition and ICP Refinement

**Analyze Win Patterns** to identify your "sweet spot":

**What Deals Do We Win?**
- Company size: 200-1000 employees (Mid-Market)
- Industry: Manufacturing, Healthcare
- Use case: Predictive maintenance, compliance
- Budget range: $100K-$500K
- Decision maker: VP Operations, CTO
- Geography: North America
- Tech stack: Cloud-native, modern APIs

**What Deals Do We Lose?**
- Company size: <50 employees (too small) or >5000 (too complex)
- Industry: Financial Services (regulatory complexity)
- Use case: Custom integrations (not our strength)
- Budget range: <$50K (not enough value) or >$1M (out of our league)
- Decision maker: Procurement-led (price-focused)
- Geography: APAC (no local presence)
- Tech stack: Legacy on-prem (integration challenges)

**Updated ICP (Ideal Customer Profile)**:
```markdown
## Ideal Customer Profile (Based on Win/Loss Data)

**Firmographics**:
- Company Size: 200-1000 employees
- Industry: Manufacturing, Healthcare (avoid Financial Services)
- Geography: North America
- Tech Maturity: Cloud-native, modern stack

**Qualification Criteria**:
- Budget: $100K-$500K (sweet spot)
- Use Case: Predictive maintenance, compliance automation
- Decision Maker: VP Operations, CTO (avoid procurement-led)
- Timeline: 60-120 day sales cycle

**Red Flags (Consider Disqualifying)**:
- <50 employees or >5000 employees
- Financial Services industry
- Custom integration heavy
- <$50K budget or >$1M budget
- Procurement-led buying process
- APAC geography (until we have local presence)
- Legacy on-prem infrastructure
```

### 4.6 Win/Loss Report Template

```markdown
# Win/Loss Analysis: [Company Name]

## Deal Summary
- **Outcome**: [Won / Lost]
- **Amount**: $XXX
- **Close Date**: YYYY-MM-DD
- **Competitor**: [Competitor Name or "No Decision"]
- **Rep**: [Sales Rep Name]

## Deal Metrics
- **MEDDIC Score**: XX/100
- **Sales Cycle**: XX days
- **Stage Time**: [Breakdown by stage]
- **Engagement**: [High/Medium/Low]

## Primary Win/Loss Reason (XX%)
[Description]

## Secondary Reason (XX%)
[Description]

## Contributing Factors (XX%)
[Description]

## What Went Well ✅
1. [Success factor 1]
2. [Success factor 2]
3. [Success factor 3]

## What Could Have Been Better ❌
1. [Improvement area 1]
2. [Improvement area 2]
3. [Improvement area 3]

## Lessons Learned
1. [Lesson 1 - specific and actionable]
2. [Lesson 2]
3. [Lesson 3]

## Replicability (for Wins) / Avoidability (for Losses)
[Can we replicate this win? / Could we have avoided this loss?]

## Action Items
1. [Update battlecard / process / training]
2. [Share learning with team]
3. [Adjust ICP / qualification criteria]
```

---

## 5. Performance Metrics Tracking

### 5.1 Individual Rep Performance Metrics

**Core Metrics**:

**1. Quota Attainment** (most important):
- Formula: (Closed Revenue / Quota) × 100%
- Target: 100%+ (quota or above)
- Track: Monthly, Quarterly, Annual

**2. Pipeline Generation**:
- Formula: New pipeline added per period
- Target: 3-4x quota added per quarter
- Track: Monthly

**3. Win Rate**:
- Formula: (Closed-Won Deals / Total Closed Deals) × 100%
- Benchmark: 20-30% overall, 60-70% from Negotiation stage
- Track: By stage, by quarter

**4. Average Deal Size**:
- Formula: Total revenue / Number of deals
- Benchmark: Varies by segment (SMB: $20K, Mid-Market: $100K, Enterprise: $500K+)
- Track: Quarterly

**5. Sales Cycle Length**:
- Formula: Average days from Lead to Closed-Won
- Benchmark: 60-120 days (B2B SaaS)
- Track: Quarterly

**6. Activity Metrics**:
- Calls made, Meetings held, Proposals sent
- Correlation with success (more activity = more wins?)
- Track: Weekly

### 5.2 Rep Performance Tiers

**Tier 1: Top Performers** (>120% quota attainment):
- Characteristics: High win rate, strong qualification, efficient sales cycle
- Actions: Study and replicate their best practices
- Share their playbooks with team

**Tier 2: Core Performers** (80-120% quota attainment):
- Characteristics: Consistent, reliable, meeting expectations
- Actions: Coaching to move them to Tier 1
- Focus on 1-2 improvement areas

**Tier 3: Struggling Performers** (<80% quota attainment):
- Characteristics: Missing quota, low win rate or insufficient pipeline
- Actions: Intensive coaching, PIP if no improvement
- Diagnose root cause (skills, territory, motivation)

**Example Rep Performance Dashboard**:
```markdown
# Rep Performance Dashboard - Q1 2025

| Rep | Quota | Closed | Attainment | Pipeline | Win Rate | Avg Deal | Cycle |
|-----|-------|--------|------------|----------|----------|----------|-------|
| Rep A | $500K | $620K | 124% ⭐ | $1.8M | 32% | $95K | 68 days |
| Rep B | $500K | $510K | 102% ✓ | $1.5M | 28% | $88K | 75 days |
| Rep C | $500K | $390K | 78% ⚠️ | $1.2M | 22% | $72K | 95 days |

**Insights**:
- Rep A: Top performer - replicate qualification and closing skills
- Rep B: Solid - focus on pipeline generation for growth
- Rep C: Needs improvement - low win rate and long cycle (qualification issue)

**Actions**:
- Rep A: Shadow and document best practices
- Rep B: Pipeline generation training
- Rep C: Qualification coaching (MEDDIC deep dive), consider PIP if no improvement
```

### 5.3 Team Performance Metrics

**1. Overall Quota Attainment**:
- Team Total: (Total Closed Revenue / Total Quota) × 100%
- Target: 100%+

**2. Pipeline Coverage Ratio**:
- Team Pipeline: Total Pipeline / Total Quota
- Target: 3-4x

**3. Forecast Accuracy**:
- Commit Accuracy: Actual / Forecasted Commit
- Target: 90-95%

**4. Revenue by Segment**:
- SMB: XX%
- Mid-Market: XX%
- Enterprise: XX%

**5. Revenue by Product**:
- Product A: XX%
- Product B: XX%
- Services: XX%

**6. Revenue by Region**:
- North America: XX%
- EMEA: XX%
- APAC: XX%

### 5.4 Trend Analysis

**Compare Performance Over Time**:

**QoQ (Quarter over Quarter)**:
- Q1 2025 vs. Q4 2024
- Identify growth or decline
- Seasonal adjustments

**YoY (Year over Year)**:
- Q1 2025 vs. Q1 2024
- True growth (removes seasonality)
- Strategic progress

**Example Trend Analysis**:
```markdown
# Quarterly Trend Analysis

| Metric | Q1 2024 | Q2 2024 | Q3 2024 | Q4 2024 | Q1 2025 | YoY |
|--------|---------|---------|---------|---------|---------|-----|
| Revenue | $1.2M | $1.4M | $1.5M | $1.8M | $1.6M | +33% |
| Win Rate | 24% | 26% | 28% | 30% | 32% | +8pt |
| Avg Deal | $75K | $82K | $88K | $95K | $98K | +31% |
| Cycle | 95d | 89d | 82d | 75d | 72d | -24% |

**Insights**:
✅ Strong YoY growth (33% revenue increase)
✅ Win rate improving (better qualification)
✅ Deal size growing (moving up-market)
✅ Sales cycle shortening (more efficient)

**Seasonal Patterns**:
- Q4 is strongest quarter (year-end budget flush)
- Q1 is slower (new budgets, planning)
- Adjust expectations and quotas accordingly
```

### 5.5 Coaching Insights

**Identify Coaching Opportunities** based on data:

**Low Win Rate** → Qualification coaching
- Teach MEDDIC/BANT framework
- Role-play discovery calls
- Review lost deals together

**Long Sales Cycle** → Urgency and closing coaching
- Business case and ROI training
- Champion development
- Closing techniques

**Small Deal Size** → Up-market coaching
- Targeting larger accounts
- Value selling vs. feature selling
- Executive engagement

**Low Pipeline Generation** → Prospecting coaching
- Outbound cadences
- Messaging and positioning
- Lead qualification

**Example Coaching Plan**:
```markdown
# Coaching Plan: Rep C (Q1 2025)

## Performance Gaps
1. Win Rate: 22% (Target: 28%) - 6pt gap
2. Sales Cycle: 95 days (Target: 75 days) - 20 day gap
3. Quota Attainment: 78% (Target: 100%) - 22% gap

## Root Cause Diagnosis
- Reviewing lost deals: Poor qualification (MEDDIC avg: 52)
- Advancing unqualified deals → waste time, long cycles
- Not disqualifying weak opportunities

## Coaching Focus: Qualification
**Goal**: Improve MEDDIC scores to 70+ average

**Actions**:
1. **Training** (Week 1): MEDDIC framework deep dive
2. **Practice** (Week 2-3): Role-play qualification calls
3. **Application** (Week 4): Shadow on real qualification calls
4. **Review** (Ongoing): Weekly pipeline review with qualification lens

**Success Metrics** (90 days):
- MEDDIC scores 70+ on all new opportunities
- Win rate improves to 26%+
- Sales cycle shortens to 80 days or less
- Quota attainment reaches 90%+

**Check-in**: Weekly 1-on-1 to review progress
```

---

## 6. Data Analysis Techniques

### 6.1 Statistical Methods

**Cohort Analysis**:
- Group deals by creation period (e.g., "Q1 2024 cohort")
- Track their progress through pipeline stages
- Identify patterns (time to close, conversion rates, win rates)

**Example Cohort Analysis**:
```markdown
## Deal Cohort: Q1 2024 (Deals Created in Q1 2024)

| Cohort | Created | Qualified | Demo | Proposal | Closed-Won | Closed-Lost | Open |
|--------|---------|-----------|------|----------|------------|-------------|------|
| Q1 2024 | 120 | 48 (40%) | 29 (60%) | 18 (62%) | 12 (67%) | 6 (33%) | 0 |

**Insights**:
- Qualification rate: 40% (Lead → Qualified)
- Overall win rate: 10% (12/120) - industry benchmark
- Time to close: 110 days average
- Closed-Lost at Proposal stage: Pricing objections (4/6)

**Actions**:
- Improve qualification to 50%+ (reducing wasted effort)
- Address pricing objections earlier in process
```

**Regression Analysis**:
- Identify factors that predict wins
- Examples:
  - Does MEDDIC score predict win rate? (Yes: R² = 0.78)
  - Does number of meetings predict wins? (Yes: R² = 0.64)
  - Does deal size impact win rate? (No: R² = 0.12)

**Time-Series Forecasting**:
- Use historical data to predict future pipeline
- Seasonal adjustments (Q4 higher, Q1 lower)
- Trend projections (growth rate)

**Outlier Detection**:
- Identify unusual deals (very large, very fast, very slow)
- Investigate outliers (what's different?)
- Learn from positive outliers (replicate)
- Understand negative outliers (avoid)

### 6.2 Data Quality Standards

**Required CRM Fields** (for accurate analysis):
- Deal Amount (ACV)
- Stage
- Created Date
- Expected Close Date
- Owner (Sales Rep)
- Source (Inbound, Outbound, etc.)
- Industry
- Company Size

**Optional but Recommended**:
- MEDDIC/BANT scores
- Competitor (if known)
- Win/Loss reason (when closed)
- Engagement metrics (meetings, emails)

**Data Cleanliness Checks**:
- No missing values in required fields
- Close dates in future (for open deals)
- Stage progression logical (can't go backwards)
- Deal amounts reasonable (no $0 or $999M typos)
- Rep ownership accurate (not "Unassigned")

**Missing Data Handling**:
- **If minor (<10% missing)**: Proceed with caveats
- **If significant (>10% missing)**: Fix data before analysis
- **Document assumptions**: "Assuming average deal size for 12 deals with missing amounts"

### 6.3 Data Integration

**Combine data from multiple sources**:

**CRM Data** (Salesforce, HubSpot, etc.):
- Deal pipeline (amount, stage, dates)
- Account information (company size, industry)
- Activity data (calls, emails, meetings)

**Qualification Data** (from sales-lead-qualifier):
- BANT/MEDDIC scores
- Qualification notes
- Risk assessments

**Proposal Data** (from sales-proposal-writer):
- Proposal versions and dates
- Pricing and discounts
- Proposal status (sent, opened, responded)

**Technical Engagement** (from sales-engineer):
- Demo completion
- POC status
- ROI analysis

**Integration Pattern**:
1. Export CRM data (CSV or JSON)
2. Read qualification files from `./leads/`
3. Read proposal data from `./proposals/`
4. Read technical data from `./technical-docs/` and `./demos/`
5. Merge on Deal ID or Company Name
6. Perform integrated analysis

---

## 7. Report Templates & Formats

### 7.1 Executive Dashboard (Weekly)

**Purpose**: High-level snapshot for sales leadership

**Format**: 1-page, visual, quick to digest

**Template**:
```markdown
# Sales Executive Dashboard - Week of YYYY-MM-DD

## 🎯 Quota Progress

| Metric | This Week | This Month | This Quarter | Target |
|--------|-----------|------------|--------------|--------|
| Revenue Closed | $XXK | $XXK | $X.XM | $X.XM |
| Attainment | XX% | XX% | XX% | 100% |
| Deals Closed | X | XX | XX | XX |

## 📊 Pipeline Health

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Pipeline Value | $X.XM | $X.XM | 🟢/🟡/🔴 |
| Coverage Ratio | X.Xx | 3.5x | 🟢/🟡/🔴 |
| Weighted Forecast | $X.XM | $X.XM | 🟢/🟡/🔴 |

## 🚨 Top Risks (This Week)

1. **[Deal Name]** ($XXK) - [Risk description] - [Owner]
2. **[Deal Name]** ($XXK) - [Risk description] - [Owner]
3. **[Deal Name]** ($XXK) - [Risk description] - [Owner]

## 🚀 Top Opportunities (This Week)

1. **[Deal Name]** ($XXK) - [Opportunity description] - [Owner]
2. **[Deal Name]** ($XXK) - [Opportunity description] - [Owner]

## 📈 Trends

- **Pipeline Velocity**: [Faster/Slower] - XX days avg (was XX days)
- **Win Rate**: [Up/Down] - XX% (was XX%)
- **Forecast Accuracy**: XX% (Target: 90%)

## ⚡ Action Items

1. [Critical action - this week]
2. [Important action - next week]
```

### 7.2 Pipeline Health Report (Bi-weekly)

**Purpose**: Deep dive into pipeline quality and coverage

**Format**: 2-3 pages, analytical

**Template**:
```markdown
# Pipeline Health Report - YYYY-MM-DD

## Executive Summary

[2-3 sentences: Overall health, key concerns, recommendations]

## Pipeline Overview

**Total Pipeline**: $X.XM (XXX deals)
**Coverage Ratio**: X.Xx (Target: 3.5x)
**Health Score**: XX/100 ([Green/Yellow/Red])

## Breakdown by Stage

| Stage | Count | Value | Avg Deal Size | Avg Days | Conversion |
|-------|-------|-------|---------------|----------|------------|
| Qualification | XX | $XXM | $XXK | XX | XX% |
| Discovery | XX | $XXM | $XXK | XX | XX% |
| Demo | XX | $XXM | $XXK | XX | XX% |
| Proposal | XX | $XXM | $XXK | XX | XX% |
| Negotiation | XX | $XXM | $XXK | XX | XX% |

**Insights**:
- [Observation 1]
- [Observation 2]

## Pipeline Quality

**MEDDIC Score Distribution**:
- High Quality (>70): $X.XM (XX%)
- Medium Quality (50-70): $X.XM (XX%)
- Low Quality (<50): $X.XM (XX%)

**Economic Buyer Engagement**:
- EB Engaged: $X.XM (XX%)
- EB Identified, Not Engaged: $X.XM (XX%)
- EB Unknown: $X.XM (XX%)

**Insights**:
- [Quality observation]

## Aging Analysis

**Deal Age Distribution**:
- On Track: XX deals, $X.XM
- Aging: XX deals, $X.XM
- Stale: XX deals, $X.XM ⚠️
- Dead: XX deals, $X.XM 🚨

**Stale Deals Requiring Action** (>2x avg days):
1. [Deal Name] - XX days in [Stage] - [Owner]
2. [Deal Name] - XX days in [Stage] - [Owner]

## Velocity Trends

**Current Velocity**: XX days average
**Benchmark**: XX days
**Trend**: [Faster/Slower] by XX days vs. last month

**Bottleneck Stages**:
- [Stage]: XX days (XX% slower than benchmark)

## Recommended Actions

1. **Pipeline Generation**: [Need $XXK more to hit 3.5x coverage]
2. **Stale Deals**: [Disqualify or revive XX deals]
3. **Velocity**: [Address bottleneck in [Stage]]
4. **Quality**: [Improve qualification - XX% of pipeline has MEDDIC <50]
```

### 7.3 Forecast Report (Weekly/Monthly)

**See Section 3.5 for detailed template**

### 7.4 Deal Risk Assessment (On-Demand)

**See Section 2.5 for detailed template**

### 7.5 Win/Loss Analysis (Monthly/Quarterly)

**See Section 4.6 for detailed template**

### 7.6 Rep Performance Review (Quarterly)

**Purpose**: Individual rep performance evaluation

**Template**:
```markdown
# Performance Review: [Rep Name] - [Period]

## Summary

[1-2 paragraphs: Overall performance, strengths, areas for improvement]

## Quota Attainment

| Metric | Target | Actual | Attainment |
|--------|--------|--------|------------|
| Revenue | $XXX | $XXX | XX% |
| Deals Closed | XX | XX | XX% |

**Trend**: [Improving/Declining/Stable]

## Pipeline Metrics

| Metric | [Rep Name] | Team Avg | Benchmark |
|--------|------------|----------|-----------|
| Pipeline Generated | $XXX | $XXX | $XXX |
| Win Rate | XX% | XX% | XX% |
| Avg Deal Size | $XXK | $XXK | $XXK |
| Sales Cycle | XX days | XX days | XX days |

## Activity Metrics

| Metric | [Rep Name] | Team Avg |
|--------|------------|----------|
| Calls | XXX | XXX |
| Meetings | XXX | XXX |
| Proposals Sent | XXX | XXX |

## Strengths ✅

1. [Specific strength with evidence]
2. [Specific strength with evidence]

## Areas for Improvement 📈

1. [Specific improvement area with data]
   - **Evidence**: [Data point]
   - **Impact**: [What it costs]
   - **Coaching Plan**: [How to improve]

2. [Specific improvement area with data]
   - **Evidence**: [Data point]
   - **Impact**: [What it costs]
   - **Coaching Plan**: [How to improve]

## Goals for Next Quarter

1. [SMART goal 1]
2. [SMART goal 2]
3. [SMART goal 3]

## Support Needed

- [Resource or support needed from management]
```

---

## 8. Integration Patterns

### 8.1 Reading Data from sales-lead-qualifier

**File Location**: `./leads/{client-name}-qualification.json`

**Data Structure**:
```json
{
  "company": "Acme Corp",
  "framework": "MEDDIC",
  "scores": {
    "metrics": 12,
    "economic_buyer": 8,
    "decision_criteria": 15,
    "decision_process": 14,
    "identify_pain": 18,
    "champion": 4,
    "total": 71
  },
  "priority": "P2",
  "recommendation": "Qualified - proceed to demo"
}
```

**Usage in Pipeline Analysis**:
```python
# Read qualification data
qualification = read_json("./leads/acme-corp-qualification.json")

# Use in risk assessment
if qualification["scores"]["total"] < 60:
    risk_level = "HIGH"
elif qualification["scores"]["total"] < 75:
    risk_level = "MEDIUM"
else:
    risk_level = "LOW"

# Use in forecast probability
stage_probability = 0.50  # Proposal stage
meddic_adjustment = qualification["scores"]["total"] / 70
adjusted_probability = stage_probability * meddic_adjustment
```

### 8.2 Reading Data from sales-proposal-writer

**File Location**: `./proposals/{client-name}/`

**Files to Check**:
- `proposal-v1.0.md`, `proposal-v1.1.md` (version history)
- `pricing-{client-name}.md`
- `proposal-status.json`

**Data Structure** (proposal-status.json):
```json
{
  "company": "Acme Corp",
  "latest_version": "v1.1",
  "sent_date": "2025-01-12",
  "opened": true,
  "opened_date": "2025-01-13",
  "responded": false,
  "pricing": {
    "original": 250000,
    "current": 220000,
    "discount_pct": 12
  }
}
```

**Usage in Pipeline Analysis**:
```python
# Read proposal status
proposal = read_json("./proposals/acme-corp/proposal-status.json")

# Calculate days since sent
days_since_sent = days_between(proposal["sent_date"], today())

# Risk signal: >14 days with no response
if days_since_sent > 14 and not proposal["responded"]:
    risk_signals.append("Proposal silence >14 days")

# Risk signal: Discount + no response
if proposal["pricing"]["discount_pct"] > 10 and not proposal["responded"]:
    risk_signals.append("Discounted >10% with no response")
```

### 8.3 Reading Data from sales-engineer

**File Locations**:
- `./technical-docs/{client-name}-*.md`
- `./demos/{client-name}-*.md`
- `./roi/{client-name}-*.md`

**Signals to Extract**:
- Demo completed? (Yes/No)
- POC status? (Not started / In progress / Completed)
- ROI analysis delivered? (Yes/No)
- Technical objections? (List)

**Usage in Pipeline Analysis**:
```python
# Check for technical engagement files
demo_files = glob("./demos/acme-corp-*")
roi_files = glob("./roi/acme-corp-*")
poc_files = glob("./technical-docs/acme-corp-poc*")

# Positive signals
if len(demo_files) > 0:
    engagement_score += 10
if len(roi_files) > 0:
    engagement_score += 15
if len(poc_files) > 0 and "completed" in read_file(poc_files[0]):
    engagement_score += 20

# Win probability boost
# Historical data: POC + ROI = 82% win rate
if demo_completed and roi_delivered and poc_completed:
    win_probability = max(win_probability, 0.82)
```

### 8.4 CRM Data Export Formats

**Standard CSV Format**:
```csv
Deal ID,Company,Amount,Stage,Created Date,Close Date,Owner,Source,Industry,Company Size,MEDDIC Score
OPP-001,Acme Corp,250000,Proposal,2025-01-01,2025-03-31,Rep A,Inbound,Manufacturing,500,68
OPP-002,Beta Inc,180000,Demo,2025-01-15,2025-04-15,Rep B,Outbound,Healthcare,300,72
```

**Standard JSON Format**:
```json
{
  "deals": [
    {
      "deal_id": "OPP-001",
      "company": "Acme Corp",
      "amount": 250000,
      "stage": "Proposal",
      "created_date": "2025-01-01",
      "close_date": "2025-03-31",
      "owner": "Rep A",
      "source": "Inbound",
      "industry": "Manufacturing",
      "company_size": 500,
      "meddic_score": 68
    }
  ]
}
```

### 8.5 Data Output Locations

**Recommended Directory Structure**:
```
pipeline-data/
├── health-reports/
│   ├── 2025-01-19-weekly-health.md
│   └── 2025-01-15-pipeline-health.json
├── forecasts/
│   ├── 2025-Q1-forecast.md
│   └── 2025-Q1-commit-deals.json
├── risk-assessments/
│   ├── acme-corp-risk-assessment.md
│   └── critical-risks-2025-01-19.json
├── win-loss/
│   ├── 2024-Q4-win-loss-summary.md
│   └── competitor-analysis.json
└── performance/
    ├── rep-performance-2025-01.json
    └── team-metrics-2025-01.md
```

### 8.6 Handoff Protocols

**When to Notify Other Teams**:

**To Sales Ops**:
- Data quality issues found
- CRM field requirements
- New metrics or reports needed

**To Sales Enablement**:
- Rep performance gaps identified
- Training needs (qualification, closing, etc.)
- Best practices from top performers

**To Marketing**:
- Lead quality issues (source analysis)
- ICP refinement recommendations
- Win/loss insights for messaging

**To Product**:
- Feature gaps causing losses
- Competitive intelligence
- Customer use case patterns

**To Finance**:
- Forecast submissions (Commit/Best Case)
- Deal slippage explanations
- Quota attainment tracking

---

## Skill Version and Updates

**Version**: 1.0
**Last Updated**: 2025-01-19
**Based On**: 1000+ B2B deals across SaaS, Mid-Market, and Enterprise segments

**Updates**:
- This is the initial version
- Will be updated based on real-world usage and feedback
- Contributions welcome from sales-pipeline-analyst users

---

## Final Reminders

**Before Any Analysis**:
1. ✅ Read this entire skill (don't skip sections)
2. ✅ Verify data quality (completeness, freshness, accuracy)
3. ✅ Integrate data from all sources (CRM, qualification, proposal, technical)
4. ✅ Use appropriate methodology (documented in skill)
5. ✅ Provide actionable insights (not just metrics)
6. ✅ Format professionally (executive-ready)
7. ✅ Double-check calculations
8. ✅ Include generation date and data sources

**Quality Checklist**:
- [ ] Methodology clearly explained
- [ ] Data sources documented
- [ ] Metrics calculated correctly
- [ ] Context provided (vs. targets, benchmarks, historical)
- [ ] Actionable recommendations included
- [ ] Professional formatting
- [ ] No typos or errors
- [ ] Executive-friendly (clear, concise, visual)

You are now equipped with comprehensive pipeline analysis expertise. Use this skill to provide world-class insights that help sales teams win more, forecast accurately, and continuously improve.
