"""
Conflict Multiplier Model Numerical Simulation (Corrected)
Corresponds to Section S3 of the Supplementary Information
Core dynamical system:
  dW/dt = r - Γ · s(t) · W
  dγ/dt = α · s(t) · W - β · γ

Fixes to original version:
1. Replaced step-function s(t) with empirically derived gradual climate stress series
2. Corrected antagonistic investment from instantaneous product to cumulative state variable
3. Calibrated to match observed ~60 yr conflict lag and ~120 yr collapse lag
4. Aligned x-axis to absolute Year BCE, consistent with main text Figure 1
5. 600 DPI resolution, Nature Portfolio color-blind friendly palette

Dependencies: Python 3.8+, numpy, scipy, matplotlib
Repository path: code/conflict_multiplier_simulation.py
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import os

# ==============================================================
# 1. EMPIRICAL CLIMATE STRESS TIME SERIES
# ==============================================================
# Data from stress_index_timeseries.csv
year_bce_stress = np.array([2500, 2450, 2400, 2350, 2300, 2250, 2200,
                            2150, 2100, 2050, 2000, 1950, 1900])
s_t_empirical = np.array([0.05, 0.20, 0.10, 0.08, 0.35, 0.70, 1.00,
                          0.90, 0.75, 0.40, 0.15, 0.08, 0.05])

# Convert to relative time: t=0 at 2300 BCE (crisis onset)
t_empirical = 2300 - year_bce_stress
t_fine = np.linspace(-200, 450, 651)  # 2500 BCE to 1850 BCE, 1-yr resolution
year_bce_fine = 2300 - t_fine

# Interpolate stress to fine time grid
s_fine = np.interp(t_fine, t_empirical, s_t_empirical)

# ==============================================================
# 2. MODEL PARAMETERS (calibrated to Sumerian archaeological record)
# ==============================================================
r = 0.004          # Linear growth rate of effective output, per year
Gamma = 0.0125     # Conflict multiplier (resilience decay coefficient)
alpha = 0.018      # Antagonism growth driver coefficient
beta = 0.0082      # Antagonism natural decay rate
W0 = 0.2           # Initial resilience at 2500 BCE
gamma0 = 0.05      # Initial antagonistic investment at 2500 BCE

# ==============================================================
# 3. DYNAMICAL MODEL DEFINITION
# ==============================================================
def conflict_multiplier_system(y, t, r, Gamma, alpha, beta, t_grid, s_grid):
    """
    Full 2-variable conflict multiplier system
    State vector: y = [W, gamma]
    """
    W, gamma = y
    s_val = np.interp(t, t_grid, s_grid)
    dW_dt = r - Gamma * s_val * W
    dgamma_dt = alpha * s_val * W - beta * gamma
    return [dW_dt, dgamma_dt]

# Solve ODE system
y0 = [W0, gamma0]
solution = odeint(conflict_multiplier_system, y0, t_fine,
                  args=(r, Gamma, alpha, beta, t_fine, s_fine))
W_sim = solution[:, 0]
gamma_sim = solution[:, 1]

# ==============================================================
# 4. NORMALIZE ALL INDICES TO [0, 1] (consistent with empirical data)
# ==============================================================
s_norm = s_fine  # Already min-max normalized
gamma_norm = (gamma_sim - gamma_sim.min()) / (gamma_sim.max() - gamma_sim.min())
W_norm = (W_sim - W_sim.min()) / (W_sim.max() - W_sim.min())

# ==============================================================
# 5. CALCULATE KEY TIME POINTS AND LAGS
# ==============================================================
# Climate stress peak
peak_s_idx = np.argmax(s_norm)
peak_s_year = year_bce_fine[peak_s_idx]

# Antagonistic investment peak (lags stress peak)
peak_gamma_idx = np.argmax(gamma_norm)
peak_gamma_year = year_bce_fine[peak_gamma_idx]
lag_gamma_yr = peak_gamma_idx - peak_s_idx

# System resilience trough (post-stress minimum)
post_peak_mask = np.arange(len(t_fine)) >= peak_s_idx
trough_W_idx_local = np.argmin(W_norm[post_peak_mask])
trough_W_idx = np.where(post_peak_mask)[0][trough_W_idx_local]
trough_W_year = year_bce_fine[trough_W_idx]
lag_W_yr = trough_W_idx - peak_s_idx

# Print summary
print("=" * 65)
print("SIMULATION RESULTS")
print("=" * 65)
print(f"Climate stress peak:         {int(peak_s_year)} BCE")
print(f"Antagonistic investment peak: {int(peak_gamma_year)} BCE")
print(f"  → Lag after stress peak:   {int(lag_gamma_yr)} years")
print(f"System resilience trough:    {int(trough_W_year)} BCE")
print(f"  → Lag after stress peak:   {int(lag_W_yr)} years")
print("=" * 65)

# ==============================================================
# 6. PUBLICATION-QUALITY VISUALIZATION (npj Complexity compliant)
# ==============================================================
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 10
plt.rcParams["axes.linewidth"] = 0.8
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

fig, axes = plt.subplots(3, 1, figsize=(7, 8), sharex=True, dpi=600)

# ---------- Panel (a): Climatic Stress Index ----------
ax0 = axes[0]
ax0.plot(year_bce_fine, s_norm, color="#0072B2", linewidth=1.5)
ax0.fill_between(year_bce_fine, 0, s_norm, color="#0072B2", alpha=0.15)

# Peak annotation
ax0.scatter(peak_s_year, s_norm[peak_s_idx], color="#D55E00", marker="v", s=45, zorder=5)
ax0.axvline(peak_s_year, color="gray", linestyle="--", linewidth=0.8)
ax0.text(peak_s_year - 75, s_norm[peak_s_idx] + 0.04,
         f"Peak Aridity\n({int(peak_s_year)} BCE)", fontsize=9, va="bottom")

# Sustained stress period shading
ax0.axvspan(2250, 2050, color="lightgray", alpha=0.3)

ax0.set_ylabel("Climatic Stress Index, $s(t)$")
ax0.set_ylim(0, 1.1)
ax0.text(0.02, 0.88, "(a)", transform=ax0.transAxes, fontweight="bold", fontsize=12)
ax0.text(0.5, 0.92, "ACT I: STRESS ONSET", transform=ax0.transAxes,
         fontweight="bold", fontsize=10, ha="center")

# ---------- Panel (b): Antagonistic Investment Index ----------
ax1 = axes[1]
ax1.plot(year_bce_fine, gamma_norm, color="#D55E00", linewidth=1.5)

# Peak annotation
ax1.scatter(peak_gamma_year, gamma_norm[peak_gamma_idx], color="#D55E00", marker="^", s=45, zorder=5)
ax1.axvline(peak_s_year, color="gray", linestyle="--", linewidth=0.8)
ax1.axvline(peak_gamma_year, color="gray", linestyle="--", linewidth=0.8)

# Lag arrow
y_arrow_b = 0.72
ax1.annotate("", xy=(peak_gamma_year, y_arrow_b), xytext=(peak_s_year, y_arrow_b),
             arrowprops=dict(arrowstyle="<->", color="black", linewidth=0.8))
ax1.text((peak_s_year + peak_gamma_year)/2, y_arrow_b + 0.03,
         f"Lag ~{int(lag_gamma_yr)} yrs", fontsize=9, ha="center")

ax1.set_ylabel("Antagonistic Investment Index, $\Gamma(t)$")
ax1.set_ylim(0, 1.1)
ax1.text(0.02, 0.88, "(b)", transform=ax1.transAxes, fontweight="bold", fontsize=12)
ax1.text(0.5, 0.92, "ACT II: MALADAPTIVE RESPONSE", transform=ax1.transAxes,
         fontweight="bold", fontsize=10, ha="center")

# ---------- Panel (c): Systemic Resilience Index ----------
ax2 = axes[2]
ax2.plot(year_bce_fine, W_norm, color="#009E73", linewidth=1.5)
ax2.fill_between(year_bce_fine, 0, W_norm, color="#009E73", alpha=0.15)

# Trough annotation
ax2.scatter(trough_W_year, W_norm[trough_W_idx], color="black", marker="o", s=45, zorder=5)
ax2.axvline(peak_s_year, color="gray", linestyle="--", linewidth=0.8)
ax2.axvline(trough_W_year, color="gray", linestyle="--", linewidth=0.8)

# Lag arrow
y_arrow_c = 0.18
ax2.annotate("", xy=(trough_W_year, y_arrow_c), xytext=(peak_s_year, y_arrow_c),
             arrowprops=dict(arrowstyle="<->", color="black", linewidth=0.8))
ax2.text((peak_s_year + trough_W_year)/2, y_arrow_c + 0.03,
         f"Lag ~{int(lag_W_yr)} yrs", fontsize=9, ha="center")

ax2.set_ylabel("Systemic Resilience Index, $W(t)$")
ax2.set_xlabel("Year (BCE)")
ax2.set_ylim(0, 1.1)
ax2.set_xlim(2500, 1850)
ax2.set_xticks(np.arange(2500, 1800, -100))
ax2.text(0.02, 0.88, "(c)", transform=ax2.transAxes, fontweight="bold", fontsize=12)
ax2.text(0.5, 0.92, "ACT III: SYSTEMIC COLLAPSE", transform=ax2.transAxes,
         fontweight="bold", fontsize=10, ha="center")

# Overall figure title
fig.suptitle("Figure 1. Three-phase dynamics of the 4.2 ka event in Sumer (model simulation)",
             fontsize=12, fontweight="bold", y=0.98)

plt.tight_layout(rect=[0, 0, 1, 0.96])

# ==============================================================
# 7. SAVE OUTPUTS
# ==============================================================
os.makedirs("../figures", exist_ok=True)
plt.savefig("../figures/conflict_multiplier_simulation.png", dpi=600, bbox_inches="tight")
plt.savefig("../figures/conflict_multiplier_simulation.svg", format="svg", bbox_inches="tight")
print("\n✅ Figures saved to ../figures/ (600 DPI PNG + vector SVG)")

os.makedirs("../data", exist_ok=True)
results_array = np.column_stack((year_bce_fine, t_fine, s_norm, gamma_norm, W_norm))
csv_header = "year_BCE,years_after_onset,s_t_normalized,gamma_t_normalized,W_t_normalized"
np.savetxt("../data/conflict_multiplier_simulation_results.csv",
           results_array, delimiter=",", header=csv_header, comments="", fmt="%.4f")
print("✅ Simulation results saved to ../data/")

plt.show()
