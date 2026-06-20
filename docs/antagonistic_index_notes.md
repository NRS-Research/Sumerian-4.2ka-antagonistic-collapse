# Antagonistic Investment Index Γ(t) for Sumer: Construction Notes

## 1. Original Data Source
The conflict frequency data underlying this index are compiled from the authoritative epigraphic synthesis:
> Cooper, J. S. (1983). Reconstructing History from Ancient Inscriptions: The Lagash-Umma Border Conflict. *Sources from the Ancient Near East*, vol. 2, fasc. 1. Undena Publications, Malibu.

This work systematically collates and dates all surviving cuneiform inscriptions recording the long-running territorial conflict between the Sumerian city-states of Lagash and Umma, the most well-documented inter-city military conflict of the 3rd millennium BCE in Mesopotamia.

## 2. Index Construction Methodology
The quantification follows the uniform rules defined in Section S2.1 of the Supplementary Information:
1. **Event counting**: All recorded militarized conflicts (border raids, formal campaigns, treaty violations) are sorted chronologically based on the royal chronology established in the source.
2. **Temporal aggregation**: Conflict events are aggregated into 50-year time slices, matching the chronological resolution of the climate stress index and resilience index, and accommodating the ±30-year dating uncertainty of Bronze Age archaeological contexts.
3. **Normalization**: Min-max normalization to the [0, 1] interval, where 0 represents the pre-event baseline conflict frequency and 1 represents the recorded peak frequency of inter-city warfare.

## 3. Key Chronological Logic
- The peak of militarized conflict is placed at ~2130 BCE, centered in the 2150–2100 BCE slice.
- This peak lags ~60 years behind the 4.2 ka aridity peak (~2190 BCE), matching the characteristic timescale of antagonistic amplification described by the conflict multiplier model.
- Conflict frequency declines after ~2070 BCE, synchronous with the collapse of major Sumerian urban systems, reflecting the depletion of systemic resilience and reduction in the scale of competitive social units.

## 4. Limitations and Caveats
1. This index reflects relative change in conflict intensity rather than absolute warfare frequency, as surviving inscriptions are subject to preservation bias.
2. The chronology is based on conventional middle chronology for the Early Dynastic and Akkadian periods, consistent with the chronological framework used in the rest of the study.
3. The index is designed to validate the dynamical sequence of "climatic pressure → rising antagonism → resilience depletion"; exact numerical fitting is not the purpose of this analysis.
