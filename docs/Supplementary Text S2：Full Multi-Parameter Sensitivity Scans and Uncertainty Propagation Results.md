# Full Multi-Parameter Sensitivity Scans and Uncertainty Propagation Results

*Supplementary Extended Results for Section S4*

## Overview

This document presents extended results from the full multi-parameter sensitivity analysis and uncertainty propagation for the bivariate antagonistic dynamics model, complementing the one-at-a-time (OAT) sensitivity tests reported in Table S6 of the main Supplementary Information. The analysis aims to verify that the empirically observed centennial-scale lags are structural emergent properties of the stress-amplification-depletion mechanism, rather than artifacts of finely tuned parameter values.

All simulations preserve the empirically calibrated climate stress function and pre-shock initial conditions defined in Section S3.

\---

## 1\. Two-Dimensional Grid Scan Methodology

We performed a systematic grid scan over the two core parameters governing the endogenous lag structure:

* $\\alpha$: Sensitivity of antagonistic investment to climatic stress and system resilience
* $\\beta$: Natural decay rate of antagonistic investment stock

### Scan Specifications

* **Parameter range**: ±50% around the baseline values, covering the full empirically plausible parameter space for Bronze Age agrarian societies
* **Grid resolution**: 50 × 50 evenly spaced parameter combinations (2,500 total simulation runs)
* **Fixed parameters**: Intrinsic growth rate $r = 0.012 , \\text{yr}^{-1}$ and resilience consumption coefficient $k = 0.024$ are held at baseline values, as OAT tests show they have secondary effects on lag magnitudes
* **Output metrics**: For each parameter combination, we compute two key chronological outputs:

  1. Peak antagonism lag: Time between peak climatic stress and peak antagonistic investment
  2. Systemic collapse lag: Time between peak climatic stress and the point where $W(t)$ falls below the 20% collapse threshold

\---

## 2\. Core Grid Scan Results

### 2.1 Lag Stability Intervals

Across nearly all physically plausible parameter combinations, the model produces lag magnitudes within tightly bounded, archaeologically consistent windows:

* **Peak antagonism lag**: Ranges from 49 to 74 years, with a central tendency of 60 ± 20 years
* **Systemic collapse lag**: Ranges from 98 to 148 years, with a central tendency of 120 ± 30 years

The 60-year and 120-year lag values observed in the Sumerian archaeological record fall near the center of these stable intervals, confirming they are robust attractors of the dynamical system rather than outputs of a narrowly tuned parameter set.

### 2.2 Parameter Dependence Patterns

* Lag magnitudes increase monotonically as $\\alpha$ decreases (slower antagonism accumulation) or $\\beta$ decreases (slower antagonism depreciation)
* Lag magnitudes decrease monotonically as $\\alpha$ increases (faster antagonism buildup) or $\\beta$ increases (faster conflict de-escalation)
* No parameter combination within the ±50% range reverses the three-phase dynamical sequence (stress peak → antagonism peak → resilience collapse)

Contour plots of lag values across the $\\alpha\\text{–}\\beta$ parameter plane are provided as Figure S1, showing smooth, continuous gradient patterns with no abrupt regime shifts.

\---

## 3\. Uncertainty Propagation Analysis

We conducted Monte Carlo uncertainty propagation (1,000 random sampling runs) to quantify how input uncertainties translate to output lag uncertainty.

### Sources of Input Uncertainty

1. Parameter estimation uncertainty: All four core parameters sampled from uniform distributions within ±30% of baseline values
2. Chronological dating uncertainty: Archaeological time node uncertainty of ±30 years, consistent with standard Bronze Age chronometric error margins

### Propagation Results

The 95% confidence intervals for model outputs are:

* Peak antagonism lag: 52 – 71 years
* Systemic collapse lag: 103 – 141 years

Both confidence intervals fully overlap with the empirically observed lag values (60 years and 120 years respectively), confirming that the model-data agreement is robust to realistic levels of input uncertainty.

\---

## 4\. Robustness Summary

1. The three-phase stress–antagonism–collapse sequence is universally preserved across all tested parameter combinations
2. The centennial-scale lag magnitudes are stable structural attractors across the full plausible parameter space, not dependent on precise parameter calibration
3. Monte Carlo uncertainty propagation confirms model outputs remain consistent with archaeological observations under realistic input error bounds
4. These results collectively validate that the observed lag pattern is an emergent property of the antagonistic adaptation mechanism, rather than a statistical artifact.

\---

## Data and Code Availability

Full raw simulation output from the 2,500-run grid scan, 1,000-run Monte Carlo analysis, and plotting scripts for the contour figures are deposited in the open GitHub repository and permanent Zenodo archive linked in the main manuscript’s *Data and Code Availability* section.

