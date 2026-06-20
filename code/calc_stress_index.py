"""
calc_stress_index.py
Compute normalized climate stress index s(t) from Gol-e-Zard Cave speleothem proxies
(Carolin et al., 2019, PNAS) following the methodology described in the Supplementary Information.

Reference:
Carolin, S. A. et al. Precise timing of abrupt increase in dust activity in the Middle East
coincident with 4.2 ka social change. Proceedings of the National Academy of Sciences 116, 67–72 (2019).

Parameters are consistent with the SI of this study:
- Background Mg/Ca mean: 0.87 mmol/mol
- Peak Mg/Ca value: 1.55 mmol/mol
- Temporal aggregation: 50-year time slices
- Chronology: converted from ka BP (before 1950 CE) to BCE
"""

import numpy as np
import pandas as pd

# --------------------------
# 1. Load raw proxy data
# --------------------------
# Input file contains columns: ka_BP, Mg_Ca_mmolmol, delta_18O_permil
input_path = "../data/raw_proxy_carolin2019.csv"
df = pd.read_csv(input_path)

# --------------------------
# 2. Convert chronology: ka BP → BCE
# --------------------------
# Conversion rule: BCE = 1950 - (ka_BP * 1000)
df["year_BCE"] = (1950 - df["ka_BP"] * 1000).round().astype(int)

# --------------------------
# 3. Min-max normalization of Mg/Ca to s(t) ∈ [0, 1]
# --------------------------
baseline_mgca = 0.87   # pre-event background mean (mmol/mol)
peak_mgca = 1.55       # maximum value during the 4.2 ka event (mmol/mol)

df["s_t"] = (df["Mg_Ca_mmolmol"] - baseline_mgca) / (peak_mgca - baseline_mgca)

# Clip values to [0, 1] to handle minor noise outside the baseline-peak range
df["s_t"] = df["s_t"].clip(lower=0, upper=1)

# --------------------------
# 4. Aggregate into 50-year time slices
# --------------------------
# Define 50-year bins spanning 2500–1900 BCE
bin_edges = np.arange(2525, 1875, -50)  # right-aligned bin edges
bin_labels = (bin_edges[:-1] - 25).astype(int)  # midpoint of each 50-year window

df["time_slice"] = pd.cut(
    df["year_BCE"],
    bins=bin_edges,
    labels=bin_labels,
    right=True,
    include_lowest=True
)

# Compute mean s(t) per time slice
s_t_aggregated = (
    df.groupby("time_slice", observed=True)
    .agg(s_t_normalized=("s_t", "mean"))
    .reset_index()
    .rename(columns={"time_slice": "year_BCE"})
)

# Assign climate phase labels
def assign_phase(year, s_val):
    if year > 2310:
        return "pre-event baseline"
    elif 2310 >= year > 2220:
        return "rising phase"
    elif 2220 >= year >= 2160:
        return "peak aridity"
    elif 2160 > year >= 2020:
        return "declining phase"
    else:
        return "post-event recovery"

s_t_aggregated["climate_phase"] = s_t_aggregated.apply(
    lambda row: assign_phase(row["year_BCE"], row["s_t_normalized"]), axis=1
)

# Add key node annotations
s_t_aggregated["note"] = ""
peak_row = s_t_aggregated.loc[s_t_aggregated["year_BCE"] == 2190, "note"]
if not peak_row.empty:
    s_t_aggregated.loc[s_t_aggregated["year_BCE"] == 2190, "note"] = "climatic peak of the 4.2 ka event"

# --------------------------
# 5. Export final s(t) time series
# --------------------------
output_path = "../data/stress_index_timeseries.csv"
s_t_aggregated.to_csv(output_path, index=False, float_format="%.3f")

print(f"Computation complete. Output saved to {output_path}")
print(f"Total time slices: {len(s_t_aggregated)}")
print(f"Peak s(t) = {s_t_aggregated['s_t_normalized'].max():.3f} at ~{s_t_aggregated.loc[s_t_aggregated['s_t_normalized'].idxmax(), 'year_BCE']} BCE")