# README: Climate Stress Index s(t) for Mesopotamia (4.2 ka Event)

## Overview
This document describes the construction, source, and calculation rules of the normalized climate stress index `s(t)` for the Mesopotamia region during the 4.2 ka climate event. This dataset is provided as supplementary material for the associated research paper to support full reproducibility of the analysis.

---

## 1. Original Data Source
All raw proxy data underlying this index are digitized from the published peer-reviewed paper:
> Carolin, S. A., Walker, R. T., Day, C. C., Ersek, V., Sloan, R. A., Deed, M. W., Talebian, M., & Henderson, G. M. (2019). Precise timing of abrupt increase in dust activity in the Middle East coincident with 4.2 ka social change. *Proceedings of the National Academy of Sciences*, 116(1), 67–72.
> DOI: [10.1073/pnas.1808103115](https://doi.org/10.1073/pnas.1808103115)

Specifically, Mg/Ca and δ¹⁸O time series are extracted from **Figure 4A-i and Figure 4B-i** of the original paper, representing regional dust activity and stable isotope aridity proxies from the Gol-e-Zard Cave speleothem (Iran), respectively.

---

## 2. Proxy Selection Rationale
### Primary proxy: Mg/Ca ratio
The Mg/Ca ratio of speleothem calcite is adopted as the core proxy for `s(t)` construction, consistent with the original study’s core conclusions:
1. It directly records the flux of Mesopotamia-sourced dust, which exhibits clear threshold behavior in response to regional aridity, with abrupt onset and termination of high-dust intervals.
2. It provides high-precision chronological constraints for the start, duration, and end of the arid event, with an average U/Th dating uncertainty of ±31 years (1σ).

### Supplementary proxy: δ¹⁸O stable isotope
The δ¹⁸O record is used for qualitative cross-validation only:
1. It reflects gradual changes in regional precipitation amount and evaporation, confirming the long-term drying trend during the event.
2. It does not show an abrupt anomalous signal matching the dust event, so it is not used to define precise event boundaries or peak timing.

---

## 3. Key Chronological Node Note
### Peak aridity at ~2190 BCE
This study defines ~2190 BCE as the peak of the 4.2 ka arid event in Mesopotamia. **This node is a derived conclusion based on the original paper’s proxy records, and is not explicitly labeled as an "aridity peak" date in the original text.**

Supporting basis:
1. The main high-dust/arid interval documented in the original paper spans 4.26–3.97 ka BP (2310–2020 BCE), with a sustained high plateau of Mg/Ca values across the middle of the interval.
2. The δ¹⁸O aridity signal reaches its maximum within 4.2–4.1 ka BP (2250–2150 BCE).
3. The year 2190 BCE (4.14 ka BP) falls at the center of both the Mg/Ca high plateau and the δ¹⁸O peak window, and is consistent with independent regional deep-sea dust records within dating uncertainty.

All chronological conversions follow the formula:  
`Year (BCE) = (ka BP × 1000) − 1950`

---

## 4. Calculation Methodology
The index construction follows the quantification rules described in Section S2.1 of the paper’s Supplementary Information:
1. **Normalization**: Min-max normalization scaled to the [0, 1] interval, where:
   - Baseline value (s=0): Pre-event background mean of Mg/Ca = 0.87 mmol/mol (1σ = 0.18 mmol/mol), as reported in the original paper’s *Event Timing and Errors* subsection.
   - Peak value (s=1): Maximum Mg/Ca value during the main arid event = 1.55 mmol/mol, digitized from the original published record.
2. **Temporal aggregation**: All proxy values are aggregated into 50-year time slices, matching the typical ±30-year dating uncertainty of Bronze Age archaeological contexts. The analysis covers the period 2500–1900 BCE.
3. **Chronology conversion**: All dates are converted from the original ka BP scale to the BCE scale used in the main manuscript.

---

## 5. Citation Requirements
If you use this derived `s(t)` dataset in your own research, you are required to cite **both the original proxy source and the present paper**:
1. The original speleothem record: Carolin et al. (2019), as listed in Section 1 above.
2. The present study from which this derived index originates (full citation will be added upon formal publication).

---

## 6. Copyright Statement
- All original proxy data are copyrighted by the original authors and *Proceedings of the National Academy of Sciences* (PNAS).
- The derived normalized index, processing code, and documentation in this repository are provided exclusively for academic reproducibility and non-commercial research purposes.
- Derivative content in this repository is distributed under the CC-BY-NC 4.0 license; original source data remains subject to the original publisher’s terms of use.
