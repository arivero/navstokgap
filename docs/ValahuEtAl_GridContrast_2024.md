# Valahu et al. — measured grid-state contrasts of a trapped ion

The three grids contain the real characteristic-function measurements
used in Fig. 2A of *Quantum-enhanced multiparameter sensing in a single
mode*. Each CSV records a row ID, two displacement coordinates and
the signed fluorescence contrast. The authors measured the upper-right
quadrant. Other quadrants are filled using symmetries. The separately
reconstructed density matrices and Wigner functions involve a further
fit.
[Paper, Fig. 2A and Methods](https://doi.org/10.1126/sciadv.adw9757)
and [supplement, Fig. S.1](https://arxiv.org/pdf/2412.04865#page=14)
(passages).

Christophe H. Valahu, Matthew P. Stafford, Zixin Huang, Vassili G.
Matsos, Maverick J. Millican, Teerawat Chalermpusitarak, Nicolas C.
Menicucci, Joshua Combes, Ben Q. Baragiola and Ting Rei Tan deposited
the data on 18 December 2024. The paper appeared in *Science Advances*
**11**, eadw9757 (2025). [Versioned dataset and licence](https://zenodo.org/records/14512034)
(metadata).

The [local ZIP](ValahuEtAl_GridContrast_2024.zip) packages
the three original grid CSVs under their deposited filenames.
The other files in the deposit concern number–phase states and
metrological estimators. The grid files were retrieved on 18 November
2026 and matched individually to the MD5 digests published by Zenodo.
The CSV bytes are unchanged. Valahu and colleagues license the data
under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Reading coverage

The axis and diagonal comparison uses row IDs 1200, 1210, 1690 and 1700 in
`grid_chis_delta_061.csv`, `grid_chis_delta_037.csv` and
`grid_chis_delta_030.csv`. They give the origin, two axes and their
vector sum at the same tabulated coordinate in the measured quadrant.
Rows 1455 and 1550 provide two further measured contrasts at fractional
multiples of that coordinate for the impulse test.
The four-column release gives point estimates. The corresponding trial
counts, covariances and an independent mechanical calibration of
probe disturbance are additional inputs to a confidence-qualified
trajectory test. The [mechanical comparison](../notes/newton-insertion-action.md#three-measured-contrasts-of-a-trapped-ion)
uses only these entries.
