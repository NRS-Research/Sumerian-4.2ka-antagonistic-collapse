\---



\## Computation of \\(s\_{\\text{obs}}\\) Values for Table S2a



\### Universal Formula



\\\[

s\_{\\text{obs}} = \\frac{\\text{Mg/Ca} - 0.87}{1.722 - 0.87}

\\]



\- Denominator fixed: \\(1.722 - 0.87 = 0.852\\)

\- Truncation rule: if result < 0, set to 0.000 (baseline condition)



\---



\### Point-by-Point Calculation



\#### 1. Background Start (depth 47.0 mm, mu\_yrBP 4349, BCE 2400)

\- Mg/Ca = 0.893

\- Numerator = 0.893 − 0.87 = 0.023

\- \\(s\_{\\text{obs}} = 0.023 / 0.852 = 0.02700\\)

\- Positive, no truncation → \*\*0.027\*\*



\#### 2. Plateau Onset (depth 41.5 mm, mu\_yrBP 4263, BCE 2310)

\- Mg/Ca = 1.533

\- Numerator = 1.533 − 0.87 = 0.663

\- \\(s\_{\\text{obs}} = 0.663 / 0.852 = 0.77817\\)

\- → \*\*0.778\*\*



\#### 3. First Peak (depth 39.0 mm, mu\_yrBP 4162, BCE 2190)

\- Mg/Ca = 1.543

\- Numerator = 1.543 − 0.87 = 0.673

\- \\(s\_{\\text{obs}} = 0.673 / 0.852 = 0.78991\\)

\- → \*\*0.790\*\*



\#### 4. Trough (depth 38.0 mm, mu\_yrBP 4138, BCE 2210)

\- Mg/Ca = 1.248

\- Numerator = 1.248 − 0.87 = 0.378

\- \\(s\_{\\text{obs}} = 0.378 / 0.852 = 0.44366\\)

\- → \*\*0.444\*\*



\#### 5. Second Peak (depth 36.0 mm, mu\_yrBP 4022, BCE 2070)

\- Mg/Ca = 1.722

\- Numerator = 1.722 − 0.87 = 0.852

\- \\(s\_{\\text{obs}} = 0.852 / 0.852 = 1.000\\)

\- → \*\*1.000\*\*



\#### 6. Plateau Termination (depth 35.25 mm, mu\_yrBP 3970, BCE 2020)

\- Mg/Ca = 1.569

\- Numerator = 1.569 − 0.87 = 0.699

\- \\(s\_{\\text{obs}} = 0.699 / 0.852 = 0.82042\\)

\- → \*\*0.820\*\*



\#### 7. Background Return (depth 35.0 mm, mu\_yrBP 3954, BCE 2004)

\- Mg/Ca = 0.826

\- Numerator = 0.826 − 0.87 = −0.044

\- \\(s\_{\\text{obs}} = −0.044 / 0.852 = −0.05164\\)

\- Negative → truncated to \*\*0.000\*\*

\---



\### Corrected Table S2a (Final Version)



| Anchor Point | depth (mm) | mu\_yrBP | BCE | Mg/Ca (mmol mol⁻¹) | \\(s\_{\\text{obs}}\\) (corrected) |

|-------------|------------|---------|-----|--------------------|-------------------------------|

| Background start | 47.0 | 4349 | 2400 | 0.893 | 0.027 |

| Plateau onset | 41.5 | 4263 | 2310 | 1.533 | 0.778 |

| First peak | 39.0 | 4162 | 2190 | 1.543 | 0.790 |

| Trough | 38.0 | 4138 | 2210 | 1.248 | 0.444 |

| Second peak | 36.0 | 4022 | 2070 | \*\*1.722\*\* | \*\*1.000\*\* |

| Plateau termination | 35.25 | 3970 | 2020 | 1.569 | 0.820 |

| Background return | 35.0 | 3954 | 2004 | 0.826 | 0.000 |



\---

