"""
Plotting Script for Climate Stress Index s(t)
Generates a publication-quality figure matching the style of the main text figures
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load final s(t) dataset
df = pd.read_csv("../data/stress_index_timeseries.csv")

# Set plot style (Nature/NPJ journal style)
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 10
plt.rcParams["axes.linewidth"] = 0.8

fig, ax = plt.subplots(figsize=(7, 3.5), dpi=300)

# Plot s(t) curve
ax.plot(df["year_BCE"], df["s_t_normalized"], color="#c0392b", linewidth=2, label="Climate stress index s(t)")

# Shade event period
ax.axvspan(2310, 2020, color="#fadbd8", alpha=0.4, label="Main 4.2 ka arid event")

# Mark key nodes
ax.scatter(2190, 1.0, color="#922b21", zorder=5, s=40)
ax.annotate("Peak aridity\n~2190 BCE", xy=(2190, 1.0), xytext=(2080, 0.85),
            arrowprops=dict(arrowstyle="->", color="black", linewidth=0.8), fontsize=9)

# Axes settings
ax.set_xlabel("Year (BCE)", fontsize=11)
ax.set_ylabel("Normalized climate stress s(t)", fontsize=11)
ax.set_xlim(2500, 1900)
ax.set_ylim(0, 1.1)
ax.invert_xaxis()  # Time flows left to right from older to younger
ax.legend(frameon=False, loc="upper left", fontsize=9)

# Ticks
ax.set_xticks(np.arange(2500, 1899, -100))
ax.grid(axis="y", linestyle="--", alpha=0.3)

plt.tight_layout()
plt.savefig("../figures/s_t_timeseries.png", dpi=300, bbox_inches="tight")
plt.savefig("../figures/s_t_timeseries.pdf", bbox_inches="tight")
print("Plot saved to ../figures/ directory")
