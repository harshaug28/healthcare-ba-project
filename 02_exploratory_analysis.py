"""
=============================================================
 Global Healthcare Crisis — Data Analysis
 File: analysis/02_exploratory_analysis.py
 Author: Harsh Patel
 Description: Exploratory Data Analysis with visualizations
=============================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from scipy import stats
import warnings
import os

warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────
OUTPUT_DIR = "visualizations"
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams.update({
    "figure.facecolor": "#0f1117",
    "axes.facecolor": "#1a1d2e",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "text.color": "white",
    "grid.color": "#2e3250",
    "axes.titlecolor": "white",
    "font.family": "DejaVu Sans",
})

ACCENT = "#00d4ff"
COLORS = ["#00d4ff", "#ff6b6b", "#ffd93d", "#6bcb77", "#c77dff", "#ff9f43"]

# ─────────────────────────────────────────────
# 1. GENERATE REALISTIC SIMULATED DATASET
# ─────────────────────────────────────────────
np.random.seed(42)

countries = {
    "Sub-Saharan Africa": {
        "countries": ["Nigeria", "Ethiopia", "DRC", "Tanzania", "Kenya", "Ghana", "Uganda", "Mozambique"],
        "spend_range": (50, 200), "life_exp_range": (55, 68), "access_range": (20, 45),
        "u5_mortality_range": (50, 120), "malaria_rate": 0.8, "tb_rate": 0.6
    },
    "South Asia": {
        "countries": ["India", "Pakistan", "Bangladesh", "Nepal", "Sri Lanka", "Afghanistan"],
        "spend_range": (80, 350), "life_exp_range": (65, 76), "access_range": (45, 70),
        "u5_mortality_range": (25, 65), "malaria_rate": 0.2, "tb_rate": 0.4
    },
    "Latin America": {
        "countries": ["Brazil", "Mexico", "Colombia", "Argentina", "Peru", "Chile", "Bolivia"],
        "spend_range": (400, 1800), "life_exp_range": (70, 78), "access_range": (55, 80),
        "u5_mortality_range": (12, 30), "malaria_rate": 0.1, "tb_rate": 0.1
    },
    "Asia-Pacific": {
        "countries": ["China", "Indonesia", "Philippines", "Vietnam", "Thailand", "Malaysia"],
        "spend_range": (300, 2500), "life_exp_range": (70, 80), "access_range": (60, 85),
        "u5_mortality_range": (8, 25), "malaria_rate": 0.05, "tb_rate": 0.15
    },
    "Europe": {
        "countries": ["Germany", "France", "UK", "Italy", "Spain", "Poland", "Netherlands"],
        "spend_range": (2500, 6000), "life_exp_range": (77, 83), "access_range": (82, 95),
        "u5_mortality_range": (3, 8), "malaria_rate": 0.0, "tb_rate": 0.02
    },
    "North America": {
        "countries": ["USA", "Canada", "Mexico (North)"],
        "spend_range": (5000, 13000), "life_exp_range": (75, 83), "access_range": (80, 96),
        "u5_mortality_range": (4, 7), "malaria_rate": 0.0, "tb_rate": 0.01
    },
}

rows = []
for region, cfg in countries.items():
    for country in cfg["countries"]:
        spend = np.random.uniform(*cfg["spend_range"])
        life_exp = np.random.uniform(*cfg["life_exp_range"])
        access = np.random.uniform(*cfg["access_range"])
        u5_mort = np.random.uniform(*cfg["u5_mortality_range"])
        rows.append({
            "Country": country,
            "Region": region,
            "Health_Spend_Per_Capita_USD": round(spend, 1),
            "Life_Expectancy_Years": round(life_exp, 1),
            "Healthcare_Access_Index": round(access, 1),
            "Under5_Mortality_per1000": round(u5_mort, 1),
            "Malaria_Prevalence_pct": round(np.random.uniform(0, cfg["malaria_rate"] * 15), 2),
            "TB_Prevalence_per100k": round(np.random.uniform(5, cfg["tb_rate"] * 300), 1),
            "Physicians_per1000": round(np.random.uniform(0.1 if "Africa" in region else 0.5, 4.5), 2),
            "Hospital_Beds_per1000": round(np.random.uniform(0.3 if "Africa" in region else 1, 8), 1),
            "Vaccination_Coverage_pct": round(np.random.uniform(40 if "Africa" in region else 70, 99), 1),
            "GDP_per_Capita_USD": round(spend * np.random.uniform(6, 12), 0),
        })

df = pd.DataFrame(rows)
df.to_csv("data/global_health_data.csv", index=False)
print(f"✅ Dataset generated: {len(df)} countries across {df['Region'].nunique()} regions\n")
print(df.describe().round(2))


# ─────────────────────────────────────────────
# 2. FIGURE 1 — Healthcare Spending vs Life Expectancy
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#1a1d2e")

region_colors = dict(zip(df["Region"].unique(), COLORS))

for region, group in df.groupby("Region"):
    ax.scatter(
        group["Health_Spend_Per_Capita_USD"],
        group["Life_Expectancy_Years"],
        label=region, color=region_colors[region],
        s=100, alpha=0.85, edgecolors="white", linewidths=0.4, zorder=3
    )

# Trend line
x_vals = df["Health_Spend_Per_Capita_USD"]
y_vals = df["Life_Expectancy_Years"]
slope, intercept, r_val, p_val, _ = stats.linregress(np.log1p(x_vals), y_vals)
x_line = np.linspace(x_vals.min(), x_vals.max(), 300)
y_line = slope * np.log1p(x_line) + intercept
ax.plot(x_line, y_line, color="#ffffff", linewidth=1.5, linestyle="--", alpha=0.5, label=f"Trend (r={r_val:.2f})")

ax.set_title("Healthcare Spending vs. Life Expectancy by Country", fontsize=15, fontweight="bold", pad=15, color="white")
ax.set_xlabel("Health Spend Per Capita (USD) — Log Scale", fontsize=12)
ax.set_ylabel("Life Expectancy (Years)", fontsize=12)
ax.set_xscale("log")
ax.grid(True, alpha=0.3)
ax.legend(loc="lower right", fontsize=9, framealpha=0.3, facecolor="#1a1d2e", edgecolor="#444")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/spending_vs_outcomes.png", dpi=150, bbox_inches="tight")
plt.close()
print("✅ Chart saved: spending_vs_outcomes.png")


# ─────────────────────────────────────────────
# 3. FIGURE 2 — Under-5 Mortality by Region (Bar Chart)
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#1a1d2e")

region_mortality = df.groupby("Region")["Under5_Mortality_per1000"].mean().sort_values(ascending=False)

bars = ax.barh(region_mortality.index, region_mortality.values,
               color=COLORS[:len(region_mortality)], edgecolor="#0f1117", linewidth=0.5)

for bar, val in zip(bars, region_mortality.values):
    ax.text(val + 0.5, bar.get_y() + bar.get_height() / 2,
            f"{val:.1f}", va="center", ha="left", color="white", fontsize=10, fontweight="bold")

ax.set_title("Average Under-5 Mortality Rate by Region\n(per 1,000 live births)", fontsize=14, fontweight="bold", color="white", pad=12)
ax.set_xlabel("Deaths per 1,000 Live Births", fontsize=11)
ax.axvline(x=region_mortality.mean(), color="#ffd93d", linestyle="--", linewidth=1.5, label=f"Global Avg: {region_mortality.mean():.1f}")
ax.legend(fontsize=10, framealpha=0.3, facecolor="#1a1d2e", edgecolor="#444")
ax.grid(True, axis="x", alpha=0.3)
ax.set_xlim(0, region_mortality.max() * 1.15)

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/mortality_by_region.png", dpi=150, bbox_inches="tight")
plt.close()
print("✅ Chart saved: mortality_by_region.png")


# ─────────────────────────────────────────────
# 4. FIGURE 3 — Disease Burden Heatmap
# ─────────────────────────────────────────────
metrics = ["Healthcare_Access_Index", "Vaccination_Coverage_pct", "Physicians_per1000",
           "Hospital_Beds_per1000", "Life_Expectancy_Years"]
region_means = df.groupby("Region")[metrics].mean()

# Normalize 0–1 per column
normalized = (region_means - region_means.min()) / (region_means.max() - region_means.min())
normalized.columns = ["Access Index", "Vaccination %", "Physicians/1k", "Hospital Beds/1k", "Life Expectancy"]

fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor("#0f1117")

sns.heatmap(normalized, annot=region_means.round(1), fmt=".1f",
            cmap="RdYlGn", linewidths=0.5, linecolor="#0f1117",
            ax=ax, cbar_kws={"shrink": 0.8, "label": "Relative Score (0=worst, 1=best)"},
            annot_kws={"size": 10, "weight": "bold"})

ax.set_title("Global Healthcare System Performance by Region\n(Actual values shown, color = relative score)", 
             fontsize=13, fontweight="bold", color="white", pad=12)
ax.set_xlabel("")
ax.set_ylabel("")
ax.tick_params(colors="white")
plt.setp(ax.get_xticklabels(), rotation=30, ha="right", color="white")
plt.setp(ax.get_yticklabels(), rotation=0, color="white")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/disease_burden_heatmap.png", dpi=150, bbox_inches="tight")
plt.close()
print("✅ Chart saved: disease_burden_heatmap.png")


# ─────────────────────────────────────────────
# 5. FIGURE 4 — Healthcare Access Index Distribution
# ─────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.patch.set_facecolor("#0f1117")
for ax in axes:
    ax.set_facecolor("#1a1d2e")

# Left: Access Index by region (violin)
regions_ordered = df.groupby("Region")["Healthcare_Access_Index"].median().sort_values().index.tolist()
data_by_region = [df[df["Region"] == r]["Healthcare_Access_Index"].values for r in regions_ordered]

parts = axes[0].violinplot(data_by_region, positions=range(len(regions_ordered)), showmedians=True, showmeans=False)
for i, (pc, color) in enumerate(zip(parts["bodies"], COLORS)):
    pc.set_facecolor(color)
    pc.set_alpha(0.7)
parts["cmedians"].set_colors("white")
parts["cmins"].set_colors("white")
parts["cmaxes"].set_colors("white")
parts["cbars"].set_colors("white")

axes[0].set_xticks(range(len(regions_ordered)))
axes[0].set_xticklabels([r.replace(" ", "\n") for r in regions_ordered], fontsize=8, color="white")
axes[0].set_ylabel("Healthcare Access Index (0–100)", fontsize=10)
axes[0].set_title("Healthcare Access Distribution by Region", fontsize=12, fontweight="bold", color="white")
axes[0].axhline(y=50, color="#ffd93d", linestyle="--", linewidth=1, alpha=0.7, label="Access Threshold (50)")
axes[0].legend(fontsize=9, framealpha=0.3, facecolor="#1a1d2e", edgecolor="#444")
axes[0].grid(True, axis="y", alpha=0.3)

# Right: Correlation heatmap
corr_cols = ["Health_Spend_Per_Capita_USD", "Life_Expectancy_Years", 
             "Healthcare_Access_Index", "Under5_Mortality_per1000", "Vaccination_Coverage_pct"]
corr_labels = ["Spend/Capita", "Life Exp.", "Access Index", "Child Mortality", "Vaccination %"]
corr_matrix = df[corr_cols].corr()
corr_matrix.index = corr_labels
corr_matrix.columns = corr_labels

mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)
sns.heatmap(corr_matrix, ax=axes[1], annot=True, fmt=".2f", cmap="coolwarm",
            center=0, square=True, linewidths=0.5, linecolor="#0f1117",
            annot_kws={"size": 9}, cbar_kws={"shrink": 0.8})
axes[1].set_title("Key Metrics Correlation Matrix", fontsize=12, fontweight="bold", color="white")
plt.setp(axes[1].get_xticklabels(), rotation=30, ha="right", color="white", fontsize=9)
plt.setp(axes[1].get_yticklabels(), rotation=0, color="white", fontsize=9)

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/access_index_map.png", dpi=150, bbox_inches="tight")
plt.close()
print("✅ Chart saved: access_index_map.png")


# ─────────────────────────────────────────────
# 6. STATISTICAL SUMMARY
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("  STATISTICAL ANALYSIS RESULTS")
print("=" * 60)

corr_spend_life, p1 = stats.pearsonr(df["Health_Spend_Per_Capita_USD"], df["Life_Expectancy_Years"])
corr_access_mort, p2 = stats.pearsonr(df["Healthcare_Access_Index"], df["Under5_Mortality_per1000"])
corr_vacc_mort, p3 = stats.pearsonr(df["Vaccination_Coverage_pct"], df["Under5_Mortality_per1000"])

print(f"\n📊 Correlations:")
print(f"  Spend/Capita ↔ Life Expectancy:    r = {corr_spend_life:.3f}  (p={p1:.4f}) {'✅ Significant' if p1<0.05 else ''}")
print(f"  Access Index ↔ Child Mortality:    r = {corr_access_mort:.3f}  (p={p2:.4f}) {'✅ Significant' if p2<0.05 else ''}")
print(f"  Vaccination  ↔ Child Mortality:    r = {corr_vacc_mort:.3f}  (p={p3:.4f}) {'✅ Significant' if p3<0.05 else ''}")

print(f"\n📍 Countries Below Access Index 50 (Critical Zone):")
critical = df[df["Healthcare_Access_Index"] < 50][["Country", "Region", "Healthcare_Access_Index", "Life_Expectancy_Years"]].sort_values("Healthcare_Access_Index")
print(critical.to_string(index=False))

print(f"\n🌍 Regional Summary:")
summary = df.groupby("Region").agg(
    Countries=("Country", "count"),
    Avg_Spend=("Health_Spend_Per_Capita_USD", "mean"),
    Avg_Life_Exp=("Life_Expectancy_Years", "mean"),
    Avg_Access=("Healthcare_Access_Index", "mean"),
    Avg_Child_Mort=("Under5_Mortality_per1000", "mean"),
).round(1)
print(summary.to_string())

print("\n✅ All analysis complete. Check the 'visualizations/' folder for charts.")
