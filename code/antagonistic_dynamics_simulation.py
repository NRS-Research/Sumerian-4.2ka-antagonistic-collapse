#!/usr/bin/env python3
"""
antagonistic_dynamics_simulation.py
====================================
Core numerical simulation of the conflict multiplier model (corresponds to SI S3).
Generates the 3-panel simulation plot (Fig. 1 equivalent) showing:
  (a) Climate stress index s(t)
  (b) Normalized antagonistic investment γ(t)
  (c) Systemic resilience W(t) with collapse threshold

Baseline parameters are set for the Sumerian core case.
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# ============================================================================
# 1. CLIMATE STRESS FUNCTION (Sumer-specific)
# ============================================================================
def climate_stress_sumer(t):
    """
    Normalized climate stress s(t) for Sumer.
    t = 0 corresponds to 2190 BCE (peak aridity).
    """
    s0 = 1.0
    rise = (1 + np.tanh((t + 53) / 15)) / 2
    decay = np.where(t > 0, np.exp(-t / 320), 1.0)
    return s0 * rise * decay

# ============================================================================
# 2. BIVARIATE DYNAMICS MODEL
# ============================================================================
def dynamical_system(y, t, r, alpha, beta, k):
    """Antagonistic dynamics model: dW/dt and dγ/dt."""
    W, gamma = y
    s = climate_stress_sumer(t)
    dW_dt = r - k * gamma
    dgamma_dt = alpha * s * W - beta * gamma
    return [dW_dt, dgamma_dt]

# ============================================================================
# 3. BASELINE PARAMETERS (Sumer final)
# ============================================================================
r = 0.009        # intrinsic growth rate (yr⁻¹)
alpha = 0.0075   # antagonism sensitivity
beta = 0.003     # antagonism decay rate (yr⁻¹)
k = 0.0233       # resilience consumption rate
W0 = 0.8         # pre-shock systemic resilience
gamma0 = 0.1     # pre-shock antagonistic investment

# Effective conflict multiplier
Gamma_effective = k * alpha / beta
print(f"Effective conflict multiplier Gamma = {Gamma_effective:.3f}")

# ============================================================================
# 4. SIMULATION
# ============================================================================
t = np.linspace(-100, 250, 3501)          # time axis (years relative to 2190 BCE)
year_bce = 2190 - t                       # convert to BCE
y0 = [W0, gamma0]

solution = odeint(dynamical_system, y0, t, args=(r, alpha, beta, k))
W_sim = solution[:, 0]
gamma_sim = solution[:, 1]
s_sim = climate_stress_sumer(t)

# Extract key timeline nodes
peak_s_idx = np.argmax(s_sim)
peak_gamma_idx = np.argmax(gamma_sim)
collapse_threshold = 0.2
collapse_idx = np.argmin(np.abs(W_sim - collapse_threshold))

lag_gamma = t[peak_gamma_idx] - t[peak_s_idx]
lag_collapse = t[collapse_idx] - t[peak_s_idx]

print(f"  Antagonism peak lag: {lag_gamma:.0f} years (~{2190 - t[peak_gamma_idx]:.0f} BCE)")
print(f"  Collapse lag:        {lag_collapse:.0f} years (~{2190 - t[collapse_idx]:.0f} BCE)")

# ============================================================================
# 5. GENERATE 3-PANEL FIGURE
# ============================================================================
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)
plt.subplots_adjust(hspace=0.3)

# Panel (a): Climate Stress Index s(t)
ax1.plot(year_bce, s_sim, color="#c0392b", linewidth=2)
ax1.axvline(2190, color="gray", linestyle="--", alpha=0.7)
ax1.text(2192, 0.9, "Peak Aridity\n~2190 BCE", va="top", fontsize=10)
ax1.set_ylabel("Climate Stress Index s(t)", fontsize=11)
ax1.set_ylim(0, 1.05)
ax1.set_title("Act I: Stress Onset (Sumer)", fontsize=12, fontweight="bold")
ax1.grid(alpha=0.2)

# Panel (b): Antagonistic Investment γ(t) (normalized)
gamma_norm = gamma_sim / gamma_sim.max()
ax2.plot(year_bce, gamma_norm, color="#e67e22", linewidth=2)
ax2.axvline(2190, color="gray", linestyle="-", alpha=0.7)
ax2.axvline(2190 - lag_gamma, color="gray", linestyle="--", alpha=0.7)
ax2.annotate(f"Lag ~{lag_gamma:.0f} yrs",
             xy=((2190 + (2190 - lag_gamma)) / 2, 0.5),
             ha="center", fontsize=10,
             arrowprops=dict(arrowstyle="<->", color="gray"))
ax2.text(2092, 0.9, f"Peak Conflict\n~{2190 - lag_gamma:.0f} BCE",
         va="top", fontsize=10)
ax2.set_ylabel("Antagonistic Investment γ(t) (Norm.)", fontsize=11)
ax2.set_ylim(0, 1.05)
ax2.set_title("Act II: Maladaptive Response", fontsize=12, fontweight="bold")
ax2.grid(alpha=0.2)

# Panel (c): Systemic Resilience W(t)
ax3.plot(year_bce, W_sim, color="#2980b9", linewidth=2)
ax3.axhline(y=collapse_threshold, color="red", linestyle=":", alpha=0.5, label="Collapse threshold")
ax3.axvline(2190, color="gray", linestyle="-", alpha=0.7)
ax3.axvline(2190 - lag_collapse, color="gray", linestyle="-", alpha=0.7)
ax3.annotate(f"Lag ~{lag_collapse:.0f} yrs",
             xy=((2190 + (2190 - lag_collapse)) / 2, 0.3),
             ha="center", fontsize=10,
             arrowprops=dict(arrowstyle="<->", color="gray"))
ax3.text(2052, 0.3, f"Collapse\n~{2190 - lag_collapse:.0f} BCE",
         va="top", fontsize=10)
ax3.set_ylabel("Systemic Resilience W(t)", fontsize=11)
ax3.set_xlabel("Year (BCE)", fontsize=11)
ax3.set_ylim(0, 1.05)
ax3.set_title("Act III: Systemic Collapse", fontsize=12, fontweight="bold")
ax3.legend(loc="upper right")
ax3.grid(alpha=0.2)
ax3.invert_xaxis()

plt.tight_layout()
plt.savefig("antagonistic_dynamics_simulation.png", dpi=600, bbox_inches="tight")
plt.close(fig)
print("\nFigure saved as 'antagonistic_dynamics_simulation.png'.")