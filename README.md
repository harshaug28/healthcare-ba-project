# 🏥 Global Healthcare Crisis — Business Analysis Project

> **A comprehensive Business Analyst portfolio project** examining the world's most pressing healthcare challenges through data analysis, stakeholder mapping, and strategic recommendations.

---

## 📌 Project Overview

| Field | Details |
|-------|---------|
| **Project Title** | Global Healthcare Access & Mortality Analysis |
| **Domain** | Healthcare / Public Health |
| **Type** | Business Analysis + Data Analysis |
| **Status** | ✅ Complete |
| **Tools Used** | Python, Pandas, Matplotlib, Seaborn, Excel, Jupyter Notebook |

### Problem Statement

> *Millions of people around the world die from preventable diseases every year — not because cures don't exist, but because healthcare systems are underfunded, inaccessible, or inequitably distributed. This project investigates the root causes, patterns, and potential solutions through a business analyst lens.*

---

## 🎯 Business Objectives

1. Identify the **top causes of preventable deaths** globally
2. Analyze **healthcare spending vs. health outcomes** across countries
3. Map **regional disparities** in healthcare access
4. Develop **data-driven recommendations** for healthcare policymakers and NGOs
5. Build a **business case** for targeted investment in low-income regions

---

## 📂 Project Structure

```
healthcare-ba-project/
│
├── README.md                        ← You are here
│
├── data/
│   ├── global_health_data.csv       ← Simulated dataset (WHO-aligned)
│   ├── data_dictionary.md           ← Column definitions & sources
│   └── data_sources.md              ← References & data lineage
│
├── analysis/
│   ├── 01_data_cleaning.py          ← Data preprocessing script
│   ├── 02_exploratory_analysis.py   ← EDA with charts
│   ├── 03_statistical_analysis.py   ← Correlation & regression
│   └── healthcare_analysis.ipynb    ← Full Jupyter Notebook
│
├── docs/
│   ├── business_requirements.md     ← BRD (Business Requirements Document)
│   ├── stakeholder_analysis.md      ← Stakeholder map & RACI
│   ├── process_flow.md              ← AS-IS vs TO-BE process
│   └── gap_analysis.md              ← Current vs desired state
│
├── visualizations/
│   ├── mortality_by_region.png
│   ├── spending_vs_outcomes.png
│   ├── disease_burden_heatmap.png
│   └── access_index_map.png
│
└── reports/
    ├── executive_summary.md         ← 1-page summary for stakeholders
    └── full_analysis_report.md      ← Complete findings & recommendations
```

---

## 🔍 Key Findings

### 1. 💀 Top Preventable Causes of Death (Globally)
- **Lower respiratory infections** — 2.6M deaths/year
- **Diarrhoeal diseases** — 1.5M deaths/year (largely child deaths)
- **Malaria** — 619,000 deaths/year (90% in Sub-Saharan Africa)
- **Tuberculosis** — 1.6M deaths/year
- **Cardiovascular disease** — 17.9M deaths/year (fastest rising in LMICs)

### 2. 📊 Spending vs. Outcomes Gap
- The USA spends **$12,318 per capita** on healthcare yet ranks **#37** in outcomes (WHO)
- Sub-Saharan Africa spends **<$100 per capita** and carries **24% of global disease burden**
- Correlation between healthcare spending and life expectancy: **r = 0.74** (strong positive)

### 3. 🌍 Regional Disparities
| Region | Avg Life Expectancy | Health Spend/Capita | Access Index |
|--------|--------------------|--------------------|--------------|
| North America | 79.3 yrs | $9,200 | 90/100 |
| Europe | 78.1 yrs | $4,100 | 87/100 |
| Asia-Pacific | 73.6 yrs | $1,800 | 65/100 |
| Latin America | 72.4 yrs | $1,100 | 58/100 |
| Sub-Saharan Africa | 61.2 yrs | $87 | 32/100 |

---

## 📈 Data Analysis Summary

### Datasets Used
- **WHO Global Health Observatory** (GHO) — mortality, disease burden
- **World Bank Health Data** — spending, GDP, population
- **IHME Global Burden of Disease** — DALYs (Disability-Adjusted Life Years)
- **UNICEF** — child mortality and vaccination coverage

### Analysis Performed
| Analysis Type | Purpose | Tool |
|--------------|---------|------|
| Descriptive Stats | Understand distributions | Python/Pandas |
| Correlation Analysis | Spending ↔ Outcomes | Seaborn |
| Regression | Predict mortality from access | Scikit-learn |
| Heatmap | Disease burden by region | Matplotlib |
| Gap Analysis | Current vs. target state | Excel |

---

## 💡 Strategic Recommendations

### Short-Term (0–12 months)
1. **Redirect 15% of donor healthcare budgets** to top-5 preventable disease programs in Sub-Saharan Africa
2. **Standardize electronic health records (EHR)** in low-income countries to improve data quality

### Medium-Term (1–3 years)
3. **Establish regional healthcare hubs** for diagnostics and treatment across rural Africa and South Asia
4. **Public-Private Partnership (PPP) model** — engage pharma companies for subsidized essential medicines

### Long-Term (3–10 years)
5. **Universal Health Coverage (UHC) roadmap** — targeting countries below Access Index 50
6. **AI-powered early disease surveillance** systems in 50+ low-income nations

---

## 🛠️ How to Run the Analysis

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter openpyxl
```

### Run Analysis
```bash
# Clone the repo
git clone https://github.com/harshaug28/healthcare-ba-project.git
cd healthcare-ba-project

# Generate the dataset
python analysis/01_data_cleaning.py

# Run EDA
python analysis/02_exploratory_analysis.py

# Open full notebook
jupyter notebook analysis/healthcare_analysis.ipynb
```

---

## 📋 Business Analysis Artifacts

| Artifact | Description | Location |
|----------|-------------|----------|
| BRD | Business Requirements Document | `docs/business_requirements.md` |
| Stakeholder Analysis | Power/Interest grid + RACI | `docs/stakeholder_analysis.md` |
| Gap Analysis | AS-IS vs TO-BE | `docs/gap_analysis.md` |
| Process Flow | Current & proposed workflows | `docs/process_flow.md` |
| Executive Summary | C-suite ready summary | `reports/executive_summary.md` |

---

## 👤 Author

**Harsh Patel**  
Business Analyst | Data Analyst  
📧 harsh@example.com  
🔗 [LinkedIn](https://linkedin.com/in/harshaug28)  
🐙 [GitHub](https://github.com/harshaug28)

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- World Health Organization (WHO)
- World Bank Open Data
- Institute for Health Metrics and Evaluation (IHME)
- UNICEF Data

---

*⭐ If you find this project useful, please give it a star on GitHub!*
