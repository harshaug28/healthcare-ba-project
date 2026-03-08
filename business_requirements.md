# 📋 Business Requirements Document (BRD)

**Project:** Global Healthcare Crisis Analysis  
**Version:** 1.0  
**Date:** March 2026  
**Status:** Approved  
**Author:** Harsh Patel

---

## 1. Executive Summary

This document defines the business requirements for a data-driven analysis of the global healthcare crisis. The goal is to identify root causes of preventable deaths and healthcare inequity, and deliver actionable recommendations to policymakers, NGOs, and healthcare investors.

---

## 2. Business Context

### 2.1 Problem Background

Approximately **17 million people die from preventable causes annually** — diseases that are treatable or preventable with adequate healthcare infrastructure. This crisis is concentrated in:

- **Sub-Saharan Africa:** Carries 24% of global disease burden with only 3% of global health workers
- **South Asia:** Home to 40% of the world's poorest but has fewer than 0.5 physicians per 1,000 people in many areas
- **Rural communities globally:** 46% of the world's population lives in rural areas, yet they have access to only 23% of physicians

### 2.2 Business Drivers

| Driver | Description |
|--------|-------------|
| Humanitarian | Reducing preventable deaths is a moral imperative |
| Economic | Poor health costs developing nations 10–15% of GDP annually |
| SDG Alignment | UN Sustainable Development Goal 3: Good Health & Well-Being |
| Investment ROI | Every $1 invested in healthcare yields $4 in economic returns (WHO) |

---

## 3. Project Scope

### 3.1 In Scope

- Analysis of healthcare spending vs. outcomes in 37+ countries
- Regional disparity mapping across 6 major world regions
- Identification of top preventable causes of death
- Correlation analysis between healthcare investment and health outcomes
- Strategic recommendations for resource allocation

### 3.2 Out of Scope

- Country-level policy implementation
- Clinical or medical research
- Drug development analysis
- Mental health-specific analysis (separate project)

---

## 4. Business Requirements

### BR-01: Data Collection & Quality
**Priority:** High  
**Description:** Compile a reliable, multi-source dataset of global health indicators for a minimum of 30 countries spanning all major world regions.  
**Acceptance Criteria:** Dataset includes spending, life expectancy, access index, disease burden, and vaccination coverage for each country.

### BR-02: Regional Disparity Analysis
**Priority:** High  
**Description:** Quantify the gap in healthcare outcomes between high-income and low-income regions.  
**Acceptance Criteria:** Statistically significant difference demonstrated between top and bottom quartile regions.

### BR-03: Root Cause Identification
**Priority:** High  
**Description:** Identify the primary drivers of poor health outcomes in under-resourced regions.  
**Acceptance Criteria:** Top 5 preventable causes identified with supporting data; correlation analysis performed.

### BR-04: Predictive Insights
**Priority:** Medium  
**Description:** Build a model to identify which countries are most at risk and likely to benefit most from targeted investment.  
**Acceptance Criteria:** Countries ranked by criticality score with intervention priority tier (High/Medium/Low).

### BR-05: Visual Reporting
**Priority:** Medium  
**Description:** All findings must be communicated through clear, professional visualizations suitable for executive presentation.  
**Acceptance Criteria:** Minimum 4 publication-quality charts included in the report.

### BR-06: Recommendations Framework
**Priority:** High  
**Description:** Deliver actionable recommendations with timeline, resource estimates, and expected impact.  
**Acceptance Criteria:** Short/medium/long-term recommendations provided with measurable success KPIs.

---

## 5. Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-01 | System shall generate a clean dataset from simulated WHO/World Bank data | High |
| FR-02 | System shall produce scatter, bar, heatmap, and violin chart visualizations | High |
| FR-03 | System shall calculate Pearson correlation coefficients for key metric pairs | High |
| FR-04 | System shall flag countries below the critical Access Index threshold (<50) | Medium |
| FR-05 | System shall output a regional summary table for executive review | Medium |
| FR-06 | All code shall be documented and reproducible via command line | High |

---

## 6. Non-Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| NFR-01 | Code must run on Python 3.8+ | High |
| NFR-02 | Analysis shall complete in under 60 seconds | Medium |
| NFR-03 | All charts must be exported at minimum 150 DPI | Medium |
| NFR-04 | Project must be fully documented for GitHub publication | High |

---

## 7. Assumptions

- Data used is representative of real-world trends (validated against WHO/World Bank benchmarks)
- "Healthcare access index" is a composite score reflecting proximity, affordability, and quality
- Spending data reflects total public + private health expenditure per capita in USD

---

## 8. Constraints

- No access to raw WHO proprietary databases (simulated data used)
- Analysis covers only physical health (mental health excluded)
- No real-time data feed; analysis is point-in-time

---

## 9. Success Metrics (KPIs)

| KPI | Target |
|-----|--------|
| Number of countries analyzed | ≥ 30 |
| Statistical significance of key correlations | p < 0.05 |
| Regions covered | All 6 major world regions |
| Recommendations delivered | ≥ 6 (2 per time horizon) |
| Stakeholder satisfaction (presentation) | ≥ 4/5 |

---

## 10. Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Business Analyst | Harsh Patel | ✅ | March 2026 |
| Project Sponsor | [Sponsor Name] | Pending | |
| Data Lead | [Data Lead Name] | Pending | |
