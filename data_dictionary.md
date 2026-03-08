# 📚 Data Dictionary

**File:** `data/global_health_data.csv`  
**Last Updated:** March 2026

---

## Column Definitions

| Column Name | Data Type | Unit | Description | Source |
|-------------|-----------|------|-------------|--------|
| `Country` | String | — | Country name | WHO/World Bank |
| `Region` | String | — | World region classification | World Bank |
| `Health_Spend_Per_Capita_USD` | Float | USD | Total health expenditure per person per year | World Bank |
| `Life_Expectancy_Years` | Float | Years | Average years of life at birth | WHO GHO |
| `Healthcare_Access_Index` | Float | Score (0–100) | Composite access score: proximity + affordability + quality | IHME HAQ Index |
| `Under5_Mortality_per1000` | Float | Per 1,000 births | Deaths of children under 5 per 1,000 live births | UNICEF |
| `Malaria_Prevalence_pct` | Float | Percentage | % of population affected by malaria | WHO |
| `TB_Prevalence_per100k` | Float | Per 100,000 | TB cases per 100,000 population | WHO |
| `Physicians_per1000` | Float | Per 1,000 people | Number of licensed physicians per 1,000 population | World Bank |
| `Hospital_Beds_per1000` | Float | Per 1,000 people | Number of hospital beds per 1,000 population | World Bank |
| `Vaccination_Coverage_pct` | Float | Percentage | % of eligible population vaccinated (DTP3 + Measles) | WHO/UNICEF |
| `GDP_per_Capita_USD` | Float | USD | Gross Domestic Product per person | World Bank |

---

## Notes

- **Healthcare_Access_Index** is modeled after the IHME Healthcare Access and Quality (HAQ) Index
- Data is simulated but calibrated to real-world distributions published by WHO and World Bank
- Values represent approximate figures as of 2022–2024 reporting periods
- "North America" in this dataset includes USA and Canada only (Mexico is classified under Latin America)

---

## Data Quality

| Dimension | Status |
|-----------|--------|
| Completeness | 100% — no missing values |
| Accuracy | Validated against WHO benchmark ranges |
| Consistency | All monetary values in USD 2023 |
| Timeliness | Represents 2022–2024 estimates |
