# 🔄 Process Flow — AS-IS vs TO-BE

**Project:** Global Healthcare Crisis Analysis  
**Version:** 1.0

---

## Current State (AS-IS) — Healthcare Access in Low-Income Countries

```
Patient experiences symptoms
        │
        ▼
Seeks nearest health facility
        │
        ├──── [If facility exists] ────────────────────────────────┐
        │                                                           │
        ├──── [If no facility within 10km] ──► Delays seeking care │
                       │                               │
                       ▼                               ▼
              Condition worsens              Reaches facility late
                       │                               │
                       └───────────────────────────────┘
                                       │
                                       ▼
                          Facility Assessment
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                   │
                    ▼                  ▼                   ▼
              No doctor          No medicine          Cannot pay
            available           in stock              for care
                    │                  │                   │
                    └──────────────────┼───────────────────┘
                                       │
                                       ▼
                     Patient turns away / receives inadequate care
                                       │
                                       ▼
                          Preventable death or disability
```

### AS-IS Pain Points

| Pain Point | Regions Affected | Impact |
|------------|-----------------|--------|
| Average travel time to nearest clinic > 2 hours | Sub-Saharan Africa, Rural South Asia | 40% delay in care |
| Stock-outs of essential medicines | Sub-Saharan Africa | 35% of facilities |
| User fees preventing access | All LMIC | 800M people avoid care due to cost |
| Shortage of trained staff | Africa, South Asia | 57 countries face critical shortages |
| Paper-based health records | Global (low-income) | 60% duplication, misdiagnosis |

---

## Future State (TO-BE) — Proposed Redesigned Process

```
Patient experiences symptoms
        │
        ▼
Community Health Worker (CHW) receives alert
(via mobile health app / SMS triage)
        │
        ▼
CHW performs initial assessment within 30 minutes
        │
        ├──── [Minor condition] ──► CHW provides treatment on-site
        │                                        │
        ├──── [Moderate condition] ──► Mobile clinic dispatched
        │                                        │
        └──── [Severe condition] ──► Fast-track referral to hub hospital
                                                 │
                                                 ▼
                                    Facility with:
                                    ✅ Stocked medications
                                    ✅ Trained staff (telemedicine backup)
                                    ✅ Electronic Health Records
                                    ✅ Zero user fees (subsidized)
                                                 │
                                                 ▼
                                    Treatment provided
                                                 │
                                                 ▼
                                    Follow-up scheduled via SMS
                                                 │
                                                 ▼
                                    Health outcome recorded in EHR
                                    (feeds national surveillance system)
```

### TO-BE Improvements

| Improvement | Current State | Target State | How |
|-------------|--------------|-------------|-----|
| Time to first care | 2–5 hours | < 30 minutes | CHW network + mobile clinics |
| Medicine availability | 65% in-stock | 95% in-stock | AI-based supply chain |
| Financial barriers | 800M unable to pay | Universal coverage | UHC legislation + subsidy |
| Staff availability | 0.2/1000 (Africa) | 1.0/1000 | Training + retention incentives |
| Data quality | Paper-based | Digital EHR | National health information systems |

---

## Process Improvement Metrics

| KPI | AS-IS Baseline | TO-BE Target | Measurement Method |
|-----|---------------|-------------|-------------------|
| Average time to care | 180 minutes | 30 minutes | Mobile health app tracking |
| Preventable death rate | 94.6/1000 births | < 25/1000 | UNICEF annual census |
| Medicine stock-out rate | 35% | < 5% | Supply chain audits |
| Patient financial hardship | 30% of patients | < 5% | Household health surveys |
| Healthcare access index | 31.6 (Africa avg) | 65+ | IHME HAQ annual scoring |
