# Data Extraction Source Notes
## Overview
This document records the methodology, tools, and uncertainty assessment for digitizing raw proxy data from the published figure of Carolin et al. (2019).

## 1. Digitization Tool
- **Software**: WebPlotDigitizer v4.6
- **Source material**: Figure 4A-i (Mg/Ca ratio) and Figure 4B-i (δ¹⁸O record) from Carolin et al. (2019), PNAS, vol. 116, no. 1
- **Calibration method**: Axes were calibrated using the labeled tick marks on the original published figure; four corner anchor points were used to minimize geometric distortion.

## 2. Extraction Precision
### Temporal axis (x-axis, ka BP)
- Sampling resolution: ~10-year interval along the growth axis, matching the original record’s typical resolution during fast-growth periods.
- Digitization uncertainty: ±5 years for well-resolved segments; ±15 years for slow-growth, low-resolution segments.
- Alignment with original dating uncertainty: The original study reports an average U/Th dating uncertainty of ±31 years (1σ) for the stalagmite record. The total chronological uncertainty of the extracted dataset is consistent with the original published error range.

### Geochemical axis (y-axis)
- Mg/Ca ratio: Digitization precision ±0.03 mmol/mol
- δ¹⁸O: Digitization precision ±0.05‰
- Both values are well within the original analytical measurement errors reported in the paper’s Methods section.

## 3. Quality Control
1. All extracted data points were cross-checked against the published event boundaries (4.26 ka BP onset, 3.97 ka BP termination) to ensure chronological alignment.
2. The background mean value of extracted Mg/Ca matches the original reported 0.87 ± 0.18 mmol/mol (1σ) within digitization error.
3. Event threshold (1.4 mmol/mol, 3σ above baseline) is consistent with the original study’s definition.
