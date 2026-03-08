# 👥 Stakeholder Analysis

**Project:** Global Healthcare Crisis Analysis  
**Version:** 1.0  
**Date:** March 2026

---

## 1. Stakeholder Identification

| # | Stakeholder | Type | Role in Project |
|---|-------------|------|----------------|
| 1 | World Health Organization (WHO) | External | Data source, policy endorsement |
| 2 | World Bank | External | Funding data, economic context |
| 3 | National Health Ministries | External | Primary audience for recommendations |
| 4 | NGOs (MSF, UNICEF, Red Cross) | External | Implementation partners |
| 5 | Healthcare Investors / Philanthropists | External | Funding recommendations |
| 6 | Academic Researchers | External | Peer review & validation |
| 7 | Project Sponsor | Internal | Budget approval, strategic direction |
| 8 | Business Analyst (You) | Internal | Analysis, reporting, recommendations |
| 9 | Data Engineer | Internal | Data pipeline, dataset quality |
| 10 | Communications Team | Internal | Presentation of findings |

---

## 2. Power / Interest Grid

```
HIGH POWER
    │
    │   ● National Health Ministries        ● WHO / World Bank
    │     (Manage closely)                    (Keep satisfied)
    │
    │   ● Project Sponsor                   ● Healthcare Investors
    │
    │─────────────────────────────────────────────────────────
    │
    │   ● Data Engineer                     ● Academic Researchers
    │     (Keep informed)                     (Monitor)
    │
    │   ● Communications Team               ● General Public
    │
LOW POWER
    └───────────────────────────────────────────────────────
         LOW INTEREST                    HIGH INTEREST
```

### Quadrant Strategies

| Quadrant | Strategy | Stakeholders |
|----------|----------|--------------|
| High Power, High Interest | **Manage Closely** — Frequent updates, involve in decisions | WHO, World Bank, National Ministries |
| High Power, Low Interest | **Keep Satisfied** — Regular summaries, no detail overload | Project Sponsor, Investors |
| Low Power, High Interest | **Keep Informed** — Share findings, invite feedback | Researchers, NGOs, Data Team |
| Low Power, Low Interest | **Monitor** — Minimal engagement | General public, media |

---

## 3. RACI Matrix

| Activity | BA (You) | Data Engineer | Project Sponsor | WHO/World Bank | NGOs |
|----------|----------|--------------|----------------|----------------|------|
| Define project scope | **R/A** | C | A | I | I |
| Data collection | R | **R/A** | I | C | I |
| Data cleaning & EDA | **R/A** | C | I | — | — |
| Statistical analysis | **R/A** | C | I | — | — |
| Visualization creation | **R/A** | — | I | — | — |
| Recommendations | **R/A** | I | A | C | C |
| Executive report | **R** | I | A | I | — |
| Stakeholder presentation | **R** | — | A | I | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## 4. Stakeholder Engagement Plan

### WHO / World Bank
- **Engagement level:** High
- **Communication method:** Formal reports, quarterly briefings
- **Key interest:** Policy alignment, data accuracy
- **Concerns:** Data credibility, political sensitivity

### National Health Ministries
- **Engagement level:** High
- **Communication method:** Country-specific briefings
- **Key interest:** Actionable recommendations, resource allocation
- **Concerns:** Sovereignty, feasibility within budget constraints

### NGOs (MSF, UNICEF)
- **Engagement level:** Medium-High
- **Communication method:** Partnership workshops
- **Key interest:** Ground-level implementation guidance
- **Concerns:** Speed of deployment, logistics in low-resource settings

### Healthcare Investors / Philanthropists
- **Engagement level:** Medium
- **Communication method:** Executive summary, investment brief
- **Key interest:** ROI of health investment, impact measurement
- **Concerns:** Risk, accountability, measurable outcomes

---

## 5. Communication Plan

| Stakeholder | Frequency | Format | Channel |
|-------------|-----------|--------|---------|
| Project Sponsor | Weekly | Status update (1 page) | Email |
| WHO / World Bank | Monthly | Formal report | Secure portal |
| National Ministries | Per milestone | Presentation deck | Video call |
| NGOs | Bi-monthly | Workshop summary | Email / Slack |
| Data Team | Daily | Stand-up | Slack |
| Investors | Quarterly | Executive brief | Meeting |

---

## 6. Risk Register — Stakeholder Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Ministries reject recommendations | Medium | High | Involve them early in BR review |
| Data disputed by WHO | Low | High | Document all assumptions clearly |
| Investor disengages | Medium | Medium | Tie findings to ROI metrics |
| Internal scope creep from sponsor | High | Medium | Strict change control process |
