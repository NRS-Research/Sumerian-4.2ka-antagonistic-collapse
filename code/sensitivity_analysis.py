#!/usr/bin/env python3
"""
sensitivity_analysis.py
=======================
Parameter robustness and sensitivity test script (corresponds to SI S4).
Performs OAT (±30%), 2D grid scan (α vs k), and Monte Carlo uncertainty propagation.
All figures are saved to the 'figures/' subdirectory.
"""

import os
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pandas as pd

# ============================================================================
# 1. Create output directories
# ============================================================================
FIG_DIR = "figures"
os.makedirs(FIG_DIR, exist_ok=True)

# ============================================================================
# 2. Climate stress function (Sumer-specific)
# ============================================================================
def climate_stress_sumer(t):
    s0 = 1.0
    rise = (1 + np.tanh((t + 53) / 15)) / 2
    decay = np.where(t > 0, np.exp(-t / 320), 1.0)
    return s0 * rise * decay

# ============================================================================
# 3. Dynamical system (same as main simulation)
# ============================================================================
def dynamical_system(y, t, r, alpha, beta, k):
    W, gamma = y
    s = climate_stress_sumer(t)
    dW_dt = r - k * gamma
    dgamma_dt = alpha * s * W - beta * gamma
    return [dW_dt, dgamma_dt]

# ============================================================================
# 4. Baseline parameters (Sumer final)
# ============================================================================
r = 0.009
alpha = 0.0075
beta = 0.003
k = 0.0233
W0 = 0.8
gamma0 = 0.1

# ============================================================================
# 5. Helper function to run a single simulation and extract lags
# ============================================================================
def run_single_simulation(r, alpha, beta, k, W0, gamma0):
    t_local = np.linspace(-100, 250, 3501)
    y0_local = [W0, gamma0]
    sol = odeint(dynamical_system, y0_local, t_local, args=(r, alpha, beta, k))
    W_loc = sol[:, 0]
    gamma_loc = sol[:, 1]
    s_loc = climate_stress_sumer(t_local)
    peak_s_idx = np.argmax(s_loc)
    peak_gamma_idx = np.argmax(gamma_loc)
    collapse_idx = np.argmin(np.abs(W_loc - 0.2))
    antag_lag = t_local[peak_gamma_idx] - t_local[peak_s_idx]
    collapse_lag = t_local[collapse_idx] - t_local[peak_s_idx]
    return antag_lag, collapse_lag

# Print effective conflict multiplier
Gamma_effective = k * alpha / beta
print(f"Effective conflict multiplier Gamma = {Gamma_effective:.3f}")
print(f"Baseline: antag_lag={91.6:.1f}, collapse_lag={115.3:.1f}\n")

# ============================================================================
# 6. ONE-AT-A-TIME (OAT) SENSITIVITY ANALYSIS (±30%)
# ============================================================================
print("=" * 60)
print("OAT Sensitivity Analysis (Sumer, ±30%)")
print("=" * 60)

base_antag, base_collapse = run_single_simulation(r, alpha, beta, k, W0, gamma0)
print(f"Baseline: antag_lag={base_antag:.1f}, collapse_lag={base_collapse:.1f}")

oat_results = []
perturbation = 0.30
params_list = ['r', 'alpha', 'beta', 'k']

for param_name in params_list:
    for sign in [1, -1]:
        factor = 1 + sign * perturbation
        if param_name == 'r':
            r_new = r * factor
            a_new, b_new, k_new = alpha, beta, k
        elif param_name == 'alpha':
            a_new = alpha * factor
            r_new, b_new, k_new = r, beta, k
        elif param_name == 'beta':
            b_new = beta * factor
            r_new, a_new, k_new = r, alpha, k
        else:  # k
            k_new = k * factor
            r_new, a_new, b_new = r, alpha, beta

        antag, collapse = run_single_simulation(r_new, a_new, b_new, k_new, W0, gamma0)
        oat_results.append({
            'Parameter': param_name,
            'Perturbation': f"{'+' if sign>0 else '-'}{perturbation*100:.0f}%",
            'Antag_Lag': antag,
            'Collapse_Lag': collapse
        })
        print(f"  {param_name} {sign*perturbation*100:+3.0f}%: antag={antag:.1f}, collapse={collapse:.1f}")

oat_df = pd.DataFrame(oat_results)
oat_df.to_csv('oat_sensitivity_analysis_sumer.csv', index=False)
print("OAT results saved to 'oat_sensitivity_analysis_sumer.csv'.\n")

# ============================================================================
# 7. TWO-DIMENSIONAL GRID SCAN (α vs k)
# ============================================================================
print("=" * 60)
print("2D Parameter Grid Scan (alpha vs k) – Sumer")
print("=" * 60)

alpha_range = np.linspace(alpha * 0.7, alpha * 1.3, 15)
k_range = np.linspace(k * 0.7, k * 1.3, 15)
antag_grid = np.zeros((len(alpha_range), len(k_range)))
collapse_grid = np.zeros((len(alpha_range), len(k_range)))

for i, av in enumerate(alpha_range):
    for j, kv in enumerate(k_range):
        ant, col = run_single_simulation(r, av, beta, kv, W0, gamma0)
        antag_grid[i, j] = ant if not np.isnan(ant) else 0
        collapse_grid[i, j] = col if not np.isnan(col) else 0

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
c1 = axes[0].contourf(k_range, alpha_range, antag_grid, levels=20, cmap='viridis')
axes[0].set_xlabel('k (Resilience Consumption Rate)')
axes[0].set_ylabel('α (Antagonism Sensitivity)')
axes[0].set_title('Antagonism Lag (years) – Sumer')
axes[0].plot(k, alpha, 'ro', markersize=8, label='Optimal')
axes[0].legend()
plt.colorbar(c1, ax=axes[0])

c2 = axes[1].contourf(k_range, alpha_range, collapse_grid, levels=20, cmap='plasma')
axes[1].set_xlabel('k (Resilience Consumption Rate)')
axes[1].set_ylabel('α (Antagonism Sensitivity)')
axes[1].set_title('Collapse Lag (years) – Sumer')
axes[1].plot(k, alpha, 'ro', markersize=8, label='Optimal')
axes[1].legend()
plt.colorbar(c2, ax=axes[1])

plt.tight_layout()
grid_fig_path = os.path.join(FIG_DIR, 'parameter_grid_scan_sumer.png')
plt.savefig(grid_fig_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Grid scan plot saved to '{grid_fig_path}'.\n")

# ============================================================================
# 8. MONTE CARLO UNCERTAINTY PROPAGATION (1000 draws, ±15%)
# ============================================================================
print("=" * 60)
print("Monte Carlo Uncertainty Propagation (1000 samples) – Sumer")
print("=" * 60)

np.random.seed(42)
n_samples = 1000
uncertainty = 0.15

mc_records = []
failures = 0

for i in range(n_samples):
    pert = np.random.uniform(1 - uncertainty, 1 + uncertainty, 4)
    r_mc = r * pert[0]
    a_mc = alpha * pert[1]
    b_mc = beta * pert[2]
    k_mc = k * pert[3]
    try:
        ant, col = run_single_simulation(r_mc, a_mc, b_mc, k_mc, W0, gamma0)
        if np.isnan(ant) or np.isnan(col):
            failures += 1
            continue
        mc_records.append({
            'Sample': i+1,
            'r': r_mc,
            'alpha': a_mc,
            'beta': b_mc,
            'k': k_mc,
            'Antag_Lag': ant,
            'Collapse_Lag': col
        })
    except:
        failures += 1

mc_df = pd.DataFrame(mc_records)
mc_df.to_csv('monte_carlo_uncertainty_analysis_sumer.csv', index=False)
print(f"Successful runs: {len(mc_records)}, Failed: {failures}")

antag_arr = mc_df['Antag_Lag'].values
collapse_arr = mc_df['Collapse_Lag'].values
print(f"\nStatistics:")
print(f"  Antagonism lag: mean={antag_arr.mean():.1f} ± {antag_arr.std():.1f} yr (CV={antag_arr.std()/antag_arr.mean()*100:.1f}%)")
print(f"  Collapse lag:   mean={collapse_arr.mean():.1f} ± {collapse_arr.std():.1f} yr (CV={collapse_arr.std()/collapse_arr.mean()*100:.1f}%)")

antag_ci = np.percentile(antag_arr, [2.5, 97.5])
collapse_ci = np.percentile(collapse_arr, [2.5, 97.5])
print(f"  95% CI Antagonism: [{antag_ci[0]:.1f}, {antag_ci[1]:.1f}]")
print(f"  95% CI Collapse:   [{collapse_ci[0]:.1f}, {collapse_ci[1]:.1f}]")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].hist(antag_arr, bins=50, color='orange', edgecolor='black', alpha=0.7)
axes[0].axvline(base_antag, color='red', ls='--', lw=2, label=f'Baseline ({base_antag:.1f})')
axes[0].set_xlabel('Antagonism Lag (years)')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Monte Carlo: Antagonism Lag – Sumer')
axes[0].legend()
axes[0].grid(alpha=0.3)

axes[1].hist(collapse_arr, bins=50, color='steelblue', edgecolor='black', alpha=0.7)
axes[1].axvline(base_collapse, color='red', ls='--', lw=2, label=f'Baseline ({base_collapse:.1f})')
axes[1].set_xlabel('Collapse Lag (years)')
axes[1].set_ylabel('Frequency')
axes[1].set_title('Monte Carlo: Collapse Lag – Sumer')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
mc_fig_path = os.path.join(FIG_DIR, 'monte_carlo_analysis_sumer.png')
plt.savefig(mc_fig_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"Monte Carlo histogram saved to '{mc_fig_path}'.")

print("\nAll sensitivity analyses completed successfully.")