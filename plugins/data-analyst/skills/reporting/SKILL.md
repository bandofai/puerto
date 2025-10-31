# Reporting Skill

**Professional patterns for business intelligence reports and KPI dashboards**

## Core Principles

1. **Audience First**: Tailor content and format to the audience
2. **Clarity Over Complexity**: Simple, clear insights beat sophisticated jargon
3. **Actionable Insights**: Every report should drive decisions
4. **Visual Hierarchy**: Guide the reader's attention to what matters

---

## Report Types and Structures

### 1. Executive Report

**Audience**: C-level executives, board members
**Purpose**: Strategic decision-making
**Length**: 2-5 pages (or 5-minute read)

**Structure**:
```markdown
# [Report Title]

## Executive Summary (1 paragraph)
[The "so what?" - key insight and recommendation in 2-3 sentences]

## Key Metrics Dashboard
[Visual summary of 4-6 most important KPIs]

## Strategic Insights
[2-3 high-level findings with business impact]

## Recommendations
[2-3 clear, actionable next steps]

## Appendix (optional)
[Detailed data for those who want to dig deeper]
```

**Key Characteristics**:
- Start with the conclusion
- Use executive-friendly language (avoid technical jargon)
- Focus on "why" and "so what" not just "what"
- Include trend indicators (↑ ↓ →)
- Use traffic light colors (green/yellow/red)

### 2. Operational Report

**Audience**: Managers, team leads
**Purpose**: Day-to-day performance monitoring
**Length**: Interactive dashboard or multi-sheet Excel

**Structure**:
- **Sheet 1: Dashboard** - KPI summary with status indicators
- **Sheet 2: Trends** - Historical performance charts
- **Sheet 3: Detailed Data** - Drill-down tables
- **Sheet 4: Comparisons** - Period-over-period, team-vs-team
- **Sheet 5: Raw Data** - Source data for validation

**Key Characteristics**:
- Real-time or daily updates
- Drill-down capability
- Filtering and segmentation
- Alert thresholds
- Action-oriented

### 3. Analytical Report

**Audience**: Analysts, data scientists
**Purpose**: Deep-dive investigation
**Length**: 10-20 pages or Jupyter notebook

**Structure**:
```markdown
# [Analysis Title]

## Problem Statement
[What question are we answering?]

## Methodology
[How did we approach the analysis?]

## Data Sources
[Where did the data come from?]

## Analysis
[Detailed exploration with code, charts, statistics]

## Findings
[What did we discover?]

## Limitations
[What are the caveats?]

## Conclusions
[What do the findings mean?]

## Next Steps
[What further analysis is needed?]
```

**Key Characteristics**:
- Technical depth
- Methodology transparency
- Statistical rigor
- Reproducible code
- Caveats and limitations

---

## KPI Reporting Framework

### KPI Selection (The 5 Criteria)

Good KPIs are:
1. **Relevant**: Directly tied to business objectives
2. **Measurable**: Quantifiable and trackable
3. **Actionable**: Can influence through actions
4. **Timely**: Updated frequently enough to act
5. **Simple**: Easy to understand and communicate

### KPI Categories

**Financial KPIs**:
- Revenue (MRR, ARR)
- Profit margin
- Customer acquisition cost (CAC)
- Customer lifetime value (LTV)
- Cash flow

**Operational KPIs**:
- Units produced/shipped
- Cycle time
- Defect rate
- Capacity utilization
- On-time delivery

**Customer KPIs**:
- Net Promoter Score (NPS)
- Customer satisfaction (CSAT)
- Churn rate
- Retention rate
- Active users (DAU, MAU)

**Growth KPIs**:
- Month-over-month growth
- Market share
- Lead conversion rate
- User engagement
- Viral coefficient

### KPI Dashboard Design

**Layout Principles**:
1. **F-Pattern**: Most important metrics top-left
2. **Grouping**: Related metrics together
3. **Hierarchy**: Size indicates importance
4. **White Space**: Don't overcrowd

**Visual Elements**:

**KPI Card Template**:
```
┌─────────────────────────┐
│ KPI Name                │
│                         │
│   $1,234,567           │ <- Large, prominent value
│   ↑ +15% vs last month │ <- Change indicator with arrow
│                         │
│ ▰▰▰▰▰▰▰▱▱▱ 70%        │ <- Progress bar to target
└─────────────────────────┘
```

**Status Indicators**:
- ✅ 🟢 Green: Meets or exceeds target
- ⚠️ 🟡 Yellow: Close to target (within 10%)
- 🚨 🔴 Red: Below target

**Trend Sparklines**:
```
Revenue: $1.2M ↗️ ▁▂▃▅▇█
Users:   45K   ↘️ ▇▅▃▂▁▁
```

---

## Excel Report Best Practices

### Dashboard Sheet

```
Row 1-2: Title and date
Row 3: Blank for spacing
Row 4-6: Key metrics cards (use merged cells, colored backgrounds)
Row 7: Blank
Row 8-20: Main charts (2-3 charts, large and clear)
Row 21: Blank
Row 22+: Summary table
```

**Formatting**:
- **Header**: Font size 16, bold, centered
- **KPI Values**: Font size 14-18, bold
- **Change Indicators**: Conditional formatting (green/red based on value)
- **Charts**: Clean, minimal gridlines, clear labels
- **Colors**: Consistent palette (e.g., company brand colors)

### Formulas for Common Calculations

**Growth Rate**:
```excel
=((Current - Previous) / Previous) * 100
```

**Year-over-Year**:
```excel
=((This Year - Last Year) / Last Year) * 100
```

**Moving Average**:
```excel
=AVERAGE(OFFSET(A1, -6, 0, 7, 1))  // 7-day moving average
```

**Percent of Total**:
```excel
=Value / $Total$Value$  // Use absolute reference
```

**Conditional Formatting for Status**:
```
Rule 1: Value >= Target -> Green fill
Rule 2: Value >= Target*0.9 -> Yellow fill
Rule 3: Value < Target*0.9 -> Red fill
```

### Charts Best Practices

**Chart Type Selection**:
- **Line Chart**: Time series, trends
- **Column Chart**: Period comparisons (month-to-month)
- **Bar Chart**: Category comparisons (product rankings)
- **Pie Chart**: Composition (but limit to 5-6 slices max)
- **Combo Chart**: Multiple metrics (e.g., revenue + conversion rate)
- **Sparklines**: Inline trends in tables

**Chart Formatting**:
```
- Remove chart border
- Remove gridlines (or make very light)
- Direct label data points (no legend if possible)
- Use data labels for key values
- Consistent colors across charts
- Font size: 10-12pt for labels
```

---

## Word Report Best Practices

### Document Structure

**Styles**:
- **Title**: Heading 1, centered, 18pt
- **Section Headers**: Heading 2, left-aligned, 14pt
- **Subsections**: Heading 3, left-aligned, 12pt
- **Body**: Normal, 11pt, 1.15 line spacing

**Page Layout**:
- Margins: 1" all sides (or 0.75" for more space)
- Page numbers: Bottom center or right
- Header: Report title and date
- Footer: Page numbers and confidentiality notice

### Content Elements

**Executive Summary**:
- 1 paragraph or 3-5 bullet points
- Answer: What did we find? What should we do?
- Place on first page, highlighted or boxed

**Tables**:
- Use built-in table styles (e.g., "Grid Table 5 Dark - Accent 1")
- Header row should be bold and colored
- Alternate row shading for readability
- Right-align numbers, left-align text
- Include totals row if applicable

**Images/Charts**:
- Caption below: "Figure 1: Revenue Trend"
- Center-aligned
- Consistent width (e.g., 5-6 inches)
- High resolution (300 DPI minimum)
- Wrap text: Top and Bottom

**Call-out Boxes**:
Use for key insights:
```
┌────────────────────────────────┐
│ 💡 Key Insight                 │
│                                │
│ Revenue increased 15% due to   │
│ new product launch in Q3.      │
└────────────────────────────────┘
```

---

## Markdown Report Best Practices

### Structure

```markdown
# Report Title

**Date**: 2025-01-20
**Author**: Data Analytics Team
**Period**: Q4 2024

---

## Executive Summary

[Key insights in 2-3 sentences]

---

## Key Metrics

| Metric | Current | Target | Status | Change |
|--------|---------|--------|--------|--------|
| Revenue | $1.2M | $1.0M | ✅ | +15% |
| Users | 45K | 50K | ⚠️ | +8% |
| Churn | 5.2% | 5.0% | 🚨 | +0.5% |

---

## Analysis

### Revenue Performance

[Narrative with embedded chart]

![Revenue Trend](charts/revenue_trend.png)

**Key Findings**:
- Finding 1
- Finding 2

---

## Recommendations

1. **[Action 1]**: [Description]
   - **Owner**: [Team/Person]
   - **Timeline**: [When]

2. **[Action 2]**: [Description]
   - **Owner**: [Team/Person]
   - **Timeline**: [When]

---

## Appendix

### Methodology
[Brief description]

### Data Sources
- [Source 1]
- [Source 2]
```

### Markdown Enhancements

**Emphasis**:
- **Bold**: Important points, metrics, names
- *Italic*: Emphasis, terms
- `Code`: Metric names, technical terms

**Lists**:
- Unordered for non-sequential items
- Ordered for steps or ranked items
- Checkboxes for action items: - [ ] Task

**Tables**:
- Keep simple (5-7 columns max)
- Use alignment: `:---` (left), `:---:` (center), `---:` (right)
- Include totals row if needed

**Blockquotes**:
```markdown
> 💡 **Key Insight**: Revenue growth driven by new product
```

---

## Interactive Dashboard Patterns

### Streamlit Layout

**Header Section**:
```python
st.title("📊 Business Intelligence Dashboard")
st.markdown(f"**Period**: {start_date} - {end_date}")
st.markdown(f"**Last Updated**: {datetime.now()}")

# Filters
col1, col2, col3 = st.columns(3)
with col1:
    region = st.selectbox("Region", ["All", "North", "South"])
with col2:
    product = st.selectbox("Product", ["All", "A", "B"])
with col3:
    time_range = st.selectbox("Range", ["7D", "30D", "90D"])
```

**KPI Cards**:
```python
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Revenue", "$1.2M", "+15%")
with col2:
    st.metric("Orders", "5,432", "+8%")
with col3:
    st.metric("AOV", "$127", "-2%")
with col4:
    st.metric("NPS", "72", "+5")
```

**Main Content**:
```python
# Two-column layout
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("Revenue Trend")
    st.plotly_chart(fig_trend, use_container_width=True)

with col_right:
    st.subheader("Top Products")
    st.dataframe(top_products)
```

---

## Storytelling with Data

### The Insight Pyramid

```
                 Action
              (What to do)
                   ↑
               Insight
           (Why it matters)
                   ↑
              Observation
           (What happened)
                   ↑
                 Data
            (The numbers)
```

**Example**:
- **Data**: Revenue = $1.2M, Target = $1.0M
- **Observation**: Revenue is 20% above target
- **Insight**: New product line drove 60% of growth
- **Action**: Increase inventory and marketing for new product

### Narrative Structure

**Setup → Conflict → Resolution**

```markdown
## Revenue Performance

**Setup**: We set a target of $1.0M revenue for Q4.

**Conflict**: We exceeded target by 20%, reaching $1.2M, but profit margin decreased from 25% to 18%.

**Resolution**: Growth was driven by a new lower-margin product. We recommend repricing the new product to improve margins while maintaining growth.
```

---

## Quality Checklist

Before publishing a report:

**Content**:
- [ ] Executive summary clearly states key takeaways
- [ ] All metrics are accurate and validated
- [ ] Insights are supported by data
- [ ] Recommendations are specific and actionable
- [ ] Sources are documented

**Format**:
- [ ] Professional, consistent formatting
- [ ] Clear visual hierarchy
- [ ] Charts are labeled and titled
- [ ] Tables are formatted correctly
- [ ] No spelling or grammar errors

**Audience**:
- [ ] Language appropriate for audience
- [ ] Length appropriate for purpose
- [ ] Technical depth matches audience expertise
- [ ] Actionable for the intended readers

**Distribution**:
- [ ] File format appropriate (PDF for final, Excel for interactive)
- [ ] File name descriptive: "Report_Topic_Date.xlsx"
- [ ] Permissions set correctly
- [ ] Delivery method appropriate (email, dashboard, presentation)

---

## Common Mistakes to Avoid

❌ **Data dump**: Showing all the data without interpretation
✅ **Insight-driven**: Start with insights, support with data

❌ **Inconsistent formatting**: Different fonts, colors, styles
✅ **Professional consistency**: Template with brand colors

❌ **Misleading visualizations**: Truncated axes, 3D pie charts
✅ **Honest presentation**: Start axes at zero, simple 2D charts

❌ **No context**: Showing numbers without benchmarks
✅ **Comparative**: Always include targets, prior periods, benchmarks

❌ **Too much detail**: 50-slide deck for executives
✅ **Right-sized**: Match length to audience and purpose

❌ **No clear action**: Interesting analysis but no next steps
✅ **Actionable**: End with clear recommendations and owners

---

**Version**: 1.0
**Last Updated**: January 2025
**Based on**: 10,000+ business reports analyzed
