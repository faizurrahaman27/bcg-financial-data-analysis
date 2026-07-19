# 📊 Financial Analysis Report
## Apple, Microsoft, and Tesla (2023–2025)

**Prepared by:** Senior Financial Data Analyst  
**Data Source:** SEC 10-K Filings (Standardized)  
**Tools:** Python, Pandas, Matplotlib  
**Date:** July 2026

---

## Table of Contents

1. [Methodology & Data Overview](#1-methodology--data-overview)
2. [Individual Company Analysis](#2-individual-company-analysis)
   - 2.1 [Apple](#21-apple--mature-giant-steady-cash-flow)
   - 2.2 [Microsoft](#22-microsoft--the-growth-engine)
   - 2.3 [Tesla](#23-tesla--profitability-collapse)
3. [Comparative Analysis](#3-comparative-analysis)
4. [Key Trends, Findings & Anomalies](#4-key-trends-findings--anomalies)
5. [Executive-Level Insights](#5-executive-level-insights)
6. [Recommended Visualizations](#6-recommended-visualizations)
7. [Executive Summary](#7-executive-summary)
8. [Conclusions & Recommendations](#8-conclusions--recommendations)
9. [Appendix](#9-appendix)

---

## 1. Methodology & Data Overview

### Analytical Approach

This analysis employs a structured, data-driven methodology using Python and Pandas to evaluate the financial health of three major technology companies: Apple, Microsoft, and Tesla. The dataset was extracted from SEC 10-K filings and standardized for comparative analysis.

**Key Metrics Analyzed:**
- **Revenue & Revenue Growth %** — Top-line performance trajectory
- **Net Income & Net Income Growth %** — Bottom-line profitability
- **Net Margin** — Operational efficiency (Net Income / Revenue)
- **Total Assets & Asset Growth** — Capital deployment and scale
- **Total Liabilities** — Financial obligations
- **Debt Ratio** — Leverage and financial risk (Total Liabilities / Total Assets)
- **Operating Cash Flow** — Cash generation capability (limited data)
- **CAGR (Compound Annual Growth Rate)** — Normalized growth measurement

**Formulas Used:**
- CAGR = ((End Value / Start Value)^(1/Years) - 1) × 100
- Net Margin = (Net Income / Revenue) × 100
- Debt Ratio = Total Liabilities / Total Assets
- Shareholders' Equity = Total Assets - Total Liabilities

### Dataset Overview

| Column | Description | Data Type | Completeness |
|--------|-------------|-----------|-------------|
| Company | Company name (Apple, Microsoft, Tesla) | String | 100% |
| Year | Fiscal year (2023–2025) | Integer | 100% |
| Revenue | Annual revenue (in millions USD) | Integer | 100% |
| Net Income | Annual net income (in millions USD) | Integer | 100% |
| Total Assets | Total assets (in millions USD) | Integer | 100% |
| Total Liabilities | Total liabilities (in millions USD) | Integer | 100% |
| Operating Cash Flow | Operating cash flow (in millions USD) | Float | 33% (Tesla only) |
| Revenue Growth % | Year-over-year revenue growth | Float | 67% |
| Net Income Growth % | Year-over-year net income growth | Float | 67% |
| Debt Ratio | Leverage ratio | Float | 100% |

> ⚠️ **Data Quality Notes:** Operating Cash Flow data is **missing** for Apple and Microsoft. Growth percentages are unavailable for 2023 as the base year. All monetary values are in **millions of USD**.

---

## 2. Individual Company Analysis

### 2.1 Apple — Mature Giant, Steady Cash Flow

| Metric | 2023 | 2024 | 2025 | 2-Year Change |
|--------|------|------|------|---------------|
| Revenue | $383,300M | $391,000M | $416,200M | +8.58% |
| Net Income | $97,000M | $93,700M | $112,000M | +15.46% |
| Net Margin | 25.31% | 23.96% | 26.91% | +1.60pp |
| Total Assets | $352,600M | $365,000M | $359,200M | +1.87% |
| Total Liabilities | $290,400M | $308,000M | $285,500M | -1.69% |
| Debt Ratio | 82.36% | 84.38% | 79.48% | Improving |
| Revenue Growth % | — | +2.01% | +6.45% | — |
| Net Income Growth % | — | -3.40% | +19.53% | — |

**Revenue Trend:** Apple's revenue grew at a modest **4.20% CAGR**. Growth accelerated from 2.01% YoY in 2024 to 6.45% in 2025, suggesting a late-cycle recovery.

**Profitability Trend:** Net income dipped in 2024 (-3.40% YoY) but rebounded sharply in 2025 (+19.53% YoY). Net margin recovered to **26.91%**.

**Asset & Liability Trends:** Apple's asset base is virtually flat (+1.87%). Liabilities declined in 2025, improving the equity cushion. The debt ratio improved from 84.38% to 79.48%.

**Overall Assessment:** Apple is a stable, mature, and highly profitable company. It is not a growth story but a cash-generation machine with elite margins and disciplined capital allocation.

---

### 2.2 Microsoft — The Growth Engine

| Metric | 2023 | 2024 | 2025 | 2-Year Change |
|--------|------|------|------|---------------|
| Revenue | $211,915M | $245,122M | $281,724M | +32.94% |
| Net Income | $72,361M | $88,136M | $101,832M | +40.73% |
| Net Margin | 34.15% | 35.96% | 36.15% | +2.00pp |
| Total Assets | $411,976M | $512,163M | $619,003M | +50.25% |
| Total Liabilities | $205,753M | $243,686M | $275,524M | +33.91% |
| Debt Ratio | 49.94% | 47.58% | 44.51% | Improving |
| Revenue Growth % | — | +15.67% | +14.93% | — |
| Net Income Growth % | — | +21.80% | +15.54% | — |

**Revenue Trend:** Microsoft achieved an exceptional **15.30% revenue CAGR** — the highest in the cohort. Growth remained consistently strong at 15.67% (2024) and 14.93% (2025).

**Profitability Trend:** Net income grew at an **18.63% CAGR**. Net margin expanded steadily to **36.15%** — the highest in the peer group.

**Asset & Liability Trends:** Assets surged **50.25%** to $619B. Liabilities grew at a slower pace than assets, resulting in a declining debt ratio (49.94% → 44.51%).

**Overall Assessment:** Microsoft is in a clear expansion phase with best-in-class growth, profitability, and balance sheet quality.

---

### 2.3 Tesla — Profitability Collapse

| Metric | 2023 | 2024 | 2025 | 2-Year Change |
|--------|------|------|------|---------------|
| Revenue | $96,773M | $97,690M | $94,827M | -2.01% |
| Net Income | $14,974M | $7,153M | $3,855M | -74.26% |
| Net Margin | 15.47% | 7.32% | 4.07% | -11.40pp |
| Total Assets | $106,618M | $122,070M | $137,806M | +29.25% |
| Total Liabilities | $43,009M | $48,390M | $54,941M | +27.74% |
| Debt Ratio | 40.34% | 39.64% | 39.87% | Stable |
| Operating Cash Flow | $13,256M | $14,923M | $14,747M | Stable |
| Revenue Growth % | — | +0.95% | -2.93% | — |
| Net Income Growth % | — | -52.23% | -46.11% | — |

**Revenue Trend:** Revenue is **contracting**. It was flat in 2024 (+0.95%) and declined in 2025 (-2.93%). The 2-year CAGR is **-1.01%**.

**Profitability Trend:** Net income collapsed **74.26%** over two years. Net margin fell from 15.47% to 4.07% — a staggering 11.4 percentage point decline.

**Asset & Liability Trends:** Assets grew **29.25%**, but this expansion is completely decoupled from revenue and profit performance. This signals **declining capital efficiency**.

**Overall Assessment:** Tesla is in a crisis phase. Asset expansion without revenue or profit growth is a critical red flag.

---

## 3. Comparative Analysis

### 3.1 2025 Financial Snapshot

| Metric | Apple | Microsoft | Tesla |
|--------|-------|-----------|-------|
| Revenue | $416.2B | $281.7B | $94.8B |
| Net Income | $112.0B | $101.8B | $3.9B |
| Net Margin | 26.91% | **36.15%** | 4.07% |
| Total Assets | $359.2B | **$619.0B** | $137.8B |
| Shareholders' Equity | $73.7B | **$343.5B** | $82.9B |
| Debt Ratio | 79.48% | **44.51%** | 39.87% |

### 3.2 Rankings Summary

| Category | Leader | Runner-Up | Laggard |
|----------|--------|-----------|---------|
| Highest Revenue | Apple ($416.2B) | Microsoft ($281.7B) | Tesla ($94.8B) |
| Highest Profitability (Margin) | Microsoft (36.15%) | Apple (26.91%) | Tesla (4.07%) |
| Fastest Revenue Growth (CAGR) | Microsoft (15.30%) | Apple (4.20%) | Tesla (-1.01%) |
| Fastest Profit Growth (CAGR) | Microsoft (18.63%) | Apple (7.45%) | Tesla (-49.26%) |
| Strongest Balance Sheet (Equity) | Microsoft ($343.5B) | Tesla ($82.9B) | Apple ($73.7B) |
| Lowest Leverage | Tesla (39.87%) | Microsoft (44.51%) | Apple (79.48%) |
| **Overall Financial Strength** | **Microsoft** | Apple | Tesla |

---

## 4. Key Trends, Findings & Anomalies

### 4.1 Key Trends

1. **Microsoft is the clear growth leader** — revenue CAGR of 15.30% is ~3.6× Apple's and vastly outpaces Tesla's decline.
2. **Tesla's profitability is in freefall** — net income collapsed 74.26% over two years with sustained double-digit negative growth rates.
3. **All three companies improved or stabilized debt ratios in 2025** — a positive trend for balance sheet health.
4. **Asset growth is diverging from performance** — Microsoft and Tesla both expanded assets aggressively, but only Microsoft converted that into revenue and profit growth.

### 4.2 Positive Findings

✓ Microsoft demonstrates the strongest all-around performance: revenue growth, profitability expansion, asset growth, and balance sheet improvement.  
✓ Apple's 2025 net income recovery (+19.53% YoY) shows resilience.  
✓ Microsoft's net margin of 36.15% is the benchmark for the peer group.  
✓ Tesla's operating cash flow remains positive (~$14.7B) despite the earnings collapse.  
✓ Apple's liabilities declined in 2025, improving the equity position.

### 4.3 Negative Findings

✗ Tesla's net income declined 74.26% over two years — a critical red flag.  
✗ Tesla's revenue contracted in 2025 (-2.93% YoY) after near-flat 2024.  
✗ Apple's revenue growth slowed to 2.01% in 2024 before recovering in 2025.  
✗ Apple's debt ratio of 79.48% is the highest among the three companies.  
✗ Missing OCF data for Apple and Microsoft limits cash flow analysis.  
✗ Tesla's asset growth (+29.25%) is not translating to revenue or profit growth.

### 4.4 Anomalies & Unusual Values

1. **Tesla Net Income Collapse:** -52.23% in 2024 and -46.11% in 2025. This is not a one-off event; it is sustained deterioration.
2. **Apple's 2024 Net Income Dip:** -3.40% YoY decline despite +2.01% revenue growth. The 2025 rebound suggests 2024 was an anomaly.
3. **Tesla Asset Growth Without Revenue Growth:** Assets grew 29.25% while revenue fell 2.01%. This implies declining asset turnover.
4. **Microsoft's Accelerated Asset Growth:** Assets surged from $412B to $619B (+50.25%) in two years, likely driven by AI/cloud investments and acquisitions.
5. **Apple's High Debt Ratio:** 79.48% in 2025, down from 84.38% in 2024. While improving, it remains notably higher than peers.

### 4.5 Business Implications

- Microsoft is capturing market share and investing aggressively in AI/cloud.
- Apple is in a mature phase — growth is modest but margins remain elite.
- Tesla faces a profitability crisis; its business model is under severe stress.
- Investors should weigh Microsoft's growth vs. Apple's stability vs. Tesla's risk.

---

## 5. Executive-Level Insights

1. **Microsoft leads in revenue growth momentum** with a 15.30% CAGR (2023–2025), outpacing Apple (4.20%) and reversing Tesla's negative trajectory (-1.01%).
2. **Microsoft also dominates profitability expansion**, delivering an 18.63% net income CAGR while Tesla's collapsed 74.26% over the same period.
3. **Apple's net margin recovered to 26.91% in 2025** after a 2024 dip, but Microsoft's 36.15% margin is now the benchmark for the peer group.
4. **Tesla's net margin eroded from 15.47% (2023) to 4.07% (2025)** — an 11.4 percentage point decline that signals severe margin compression.
5. **Microsoft's asset base surged 50.25% in two years** (to $619B), reflecting aggressive capital deployment in AI, cloud, and strategic acquisitions.
6. **Apple's asset base grew only 1.87% over two years**, indicating a mature, capital-light model focused on shareholder returns rather than expansion.
7. **Tesla's asset growth of 29.25% is decoupled from revenue and profit performance**, suggesting declining capital efficiency and potential overcapacity.
8. **All three companies improved or stabilized their debt ratios in 2025**; Microsoft's fell to 44.51%, the most conservative leverage profile in the set.
9. **Apple's debt ratio of 79.48% remains the highest**, though it improved from 84.38% in 2024 — a structural feature of its capital return strategy.
10. **Tesla's operating cash flow held steady at ~$14.7B despite earnings collapse**, indicating non-cash charges or working capital dynamics are masking underlying cash health.
11. **Missing operating cash flow data for Apple and Microsoft** limits the ability to assess free cash flow generation and capital allocation quality.
12. **The dataset reveals a clear divergence**: Microsoft is in an expansion phase, Apple is in a stabilization phase, and Tesla is in a restructuring or crisis phase.

---

## 6. Recommended Visualizations

| Metric | Chart Type | Rationale |
|--------|-----------|-----------|
| Revenue Trend (Time Series) | Line Chart | Best for showing progression over time; easy to spot inflection points. |
| Net Income Trend | Combo Chart (Line + Column) | Line for trend + column for absolute values; highlights magnitude + change. |
| Revenue Growth % (YoY) | Clustered Bar Chart | Side-by-side bars make YoY deltas instantly readable. |
| Net Margin Comparison | Horizontal Bar Chart | Ideal for ranking a single metric across companies. |
| Total Assets vs Liabilities | Stacked Area Chart | Shows composition and trend of the balance sheet. |
| Debt Ratio Trend | Line Chart (with target line) | Single-metric time series; target line (e.g., 50%) adds context. |
| Revenue vs Net Income (with Margin as Bubble Size) | Scatter Plot (Bubble Chart) | Bubble size = margin; reveals efficiency trade-offs at a glance. |
| 2-Year CAGR Comparison | Radar/Spider Chart | Multi-dimensional comparison in one visual; good for executive decks. |
| Operating Cash Flow | Waterfall Chart | Shows contribution of OCF to net income; missing data flagged. |
| Financial Health Scorecard | KPI Cards + Conditional Formatting | KPI cards for latest values; conditional color coding (RAG) for instant status. |

**Design Notes:**
- Use a consistent color palette: Apple (gray), Microsoft (blue), Tesla (red).
- Add data labels directly on charts to eliminate the need for legends.
- Include a "Data Quality" panel flagging missing OCF for Apple/Microsoft.
- Use drill-through from company-level KPIs to year-level detail pages.
- Add a "Red Flag" conditional formatting rule for negative growth rates.

---

## 7. Executive Summary

This analysis evaluates the annual financial performance of **Apple, Microsoft, and Tesla** using standardized data extracted from SEC 10-K filings for fiscal years 2023 through 2025. The dataset encompasses revenue, net income, total assets, total liabilities, operating cash flow, growth rates, and debt ratios. The findings reveal three distinctly different strategic trajectories across the peer group.

**Microsoft** emerges as the unequivocal growth leader. Over the two-year period, Microsoft achieved a revenue CAGR of **15.30%** and a net income CAGR of **18.63%**, the highest among all three companies. Its asset base expanded by **50.25%** to $619 billion, reflecting aggressive capital deployment in cloud infrastructure, artificial intelligence, and strategic acquisitions. Importantly, this growth was accompanied by balance sheet strengthening: the debt ratio declined from 49.94% to **44.51%**, demonstrating that Microsoft is scaling efficiently without overleveraging. Net margin improved steadily from 34.15% to **36.15%**, establishing Microsoft as the most profitable operator in the cohort on a margin basis.

**Apple** presents a contrasting profile of maturity and stability. Revenue grew at a modest **4.20% CAGR**, consistent with a business operating at global scale with limited new market penetration. Net income rebounded strongly in 2025 (+19.53% YoY) after a slight contraction in 2024, lifting the net margin to **26.91%**. Apple's asset base grew only 1.87% over two years, indicating disciplined capital allocation and a focus on shareholder returns rather than expansion. However, Apple's debt ratio of **79.48%** remains the highest in the group, though it improved from 84.38% in 2024. This elevated leverage is a known structural feature of Apple's capital strategy, which relies heavily on debt to fund share buybacks and dividends.

**Tesla's** financial trajectory is the most concerning. Revenue contracted by **2.01%** over two years, with a negative CAGR of -1.01%. More alarming is the collapse in profitability: net income fell **74.26%** from $14.97 billion to $3.86 billion, and the net margin eroded from 15.47% to just **4.07%**. This sustained deterioration — spanning both 2024 and 2025 — suggests systemic margin compression rather than a one-time event. Tesla's asset base grew 29.25% during this period, but this capital expansion has not translated into revenue or profit growth, signaling declining capital efficiency. Notably, Tesla is the only company in the dataset with operating cash flow data, which remained stable at approximately $14.7 billion, suggesting non-cash charges may be contributing to the earnings decline.

From a comparative standpoint, Microsoft holds the strongest balance sheet (lowest debt ratio, highest equity base of $343.5 billion), the fastest growth, and the highest profitability. Apple offers stability and elite margins but limited growth momentum. Tesla faces a profitability crisis that demands immediate strategic attention. **Missing operating cash flow data for Apple and Microsoft is a material limitation** that should be addressed in future data collection cycles to enable a complete cash flow analysis.

---

## 8. Conclusions & Recommendations

### 8.1 Microsoft — Recommendation: Overweight / Strong Buy

**Rationale:** Microsoft demonstrates the strongest all-around performance: highest revenue CAGR (15.30%), highest net income CAGR (18.63%), best-in-class net margin trajectory (34.15% → 36.15%), and the strongest balance sheet (debt ratio fell to 44.51%, equity of $343.5B).

**Action Items:**
- Monitor capex intensity and return on invested capital (ROIC).
- Watch for signs of margin compression as scale increases.
- Assess whether asset growth translates to sustainable revenue streams.
- Obtain missing OCF data to validate cash conversion quality.

### 8.2 Apple — Recommendation: Market Weight / Hold

**Rationale:** Apple is a stable, mature business with elite margins (26.91%). The strong 2025 net income recovery (+19.53% YoY) shows resilience. Revenue growth of 4.20% CAGR is modest but predictable.

**Action Items:**
- Evaluate whether the 2025 profit rebound is sustainable or cyclical.
- Assess capital return program sustainability under high leverage.
- Monitor for new product cycle catalysts (AI, services expansion).
- Obtain OCF data to evaluate free cash flow and dividend coverage.

### 8.3 Tesla — Recommendation: Underweight / Caution

**Rationale:** Tesla's net income collapsed 74.26% over two years — a critical red flag. Revenue contracted (-2.01% over 2 years) amid asset expansion. Net margin fell from 15.47% to 4.07%.

**Action Items:**
- Investigate root causes: pricing strategy, cost structure, competition.
- Analyze whether OCF stability (~$14.7B) masks underlying cash burn.
- Evaluate if asset expansion will eventually pay off.
- Consider position sizing reduction until profitability stabilizes.

### 8.4 Cross-Portfolio Insights

- **Diversification:** Overweight Microsoft (growth), hold Apple (stability), underweight Tesla (turnaround risk).
- **Data Quality Gap:** Prioritize completing OCF data for Apple and Microsoft.
- **Sector Dynamics:** Microsoft's outperformance reflects AI/cloud tailwinds. Apple's modest growth reflects hardware saturation. Tesla's struggles reflect EV market maturation.
- **Monitoring Framework:** Track revenue growth, net margin, debt ratio, asset turnover, and ROE quarterly.
- **Risk Flags:** Alert on debt ratio > 85%, net margin decline > 5pp YoY, or revenue decline for two consecutive periods.

---

## 9. Appendix

### 9.1 Python Code Snippets

```python
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('financial_analysis_standardized.csv')

# CAGR calculation
def calculate_cagr(start, end, years):
    return ((end / start) ** (1 / years) - 1) * 100

# Net Margin
df['Net Margin'] = (df['Net Income'] / df['Revenue']) * 100

# Shareholders' Equity
df['Equity'] = df['Total Assets'] - df['Total Liabilities']
```

### 9.2 Data Quality Flag

> ⚠️ **Limitations:**
> - Operating Cash Flow data is **missing** for Apple and Microsoft.
> - Growth percentages are unavailable for 2023 (base year).
> - All monetary values are in **millions of USD**.
> - The dataset covers only 3 years; longer time series would improve trend reliability.

### 9.3 Computed Metrics Summary

| Company | Revenue 2025 | Net Income 2025 | Net Margin 2025 | Assets 2025 | Equity 2025 | Debt Ratio 2025 | Rev CAGR | NI CAGR |
|---------|-------------|----------------|----------------|------------|------------|----------------|----------|---------|
| Apple | $416,200M | $112,000M | 26.91% | $359,200M | $73,700M | 79.48% | 4.20% | 7.45% |
| Microsoft | $281,724M | $101,832M | 36.15% | $619,003M | $343,479M | 44.51% | 15.30% | 18.63% |
| Tesla | $94,827M | $3,855M | 4.07% | $137,806M | $82,865M | 39.87% | -1.01% | -49.26% |

---

*Report generated using Python, Pandas, and Matplotlib. All conclusions are based solely on the provided dataset. No external data was used.*

**End of Report**
