# B14 source companion: Cinque telegraph conditional probabilities

> Source: https://arxiv.org/pdf/2202.01904v1 (local cached PDF:
> `.build/b09/Cinque2022.pdf`)
> Metadata: Fabrizio Cinque, “A Note on the Conditional Probabilities of the
> Telegraph Process,” arXiv:2202.01904v1, 3 February 2022.
> SHA-256: `316edd890e42428d46cb88f8ae7ff10ca4fbd4bed86c2fde7180b24fc0be752b`
> Extraction: `pdftotext -layout`; pp. 3--4 formulas were also checked against
> rendered PDF images. The source PDF is already catalogued in B09; this
> companion records the additional B14 coverage.

## B14 reading coverage

Read pp. 1--4 (up to two additional pages were not needed). Page 1 defines
the integrated two-velocity process and the post-switch velocity convention in
(1.1)--(1.2); pp. 1--2 state finite-velocity endpoint atoms, the Markov
position/velocity pair, and the symmetric specialization. Page 3 Remark 2.1,
(2.4), gives the alternating switch-time representation and identifies the
odd alternating sum with time spent at the initial speed. Page 4 Theorem 2.1,
(2.6), gives the conditional density of the odd alternating sum. The rendered
formula was visually checked.

## Use in B14

Cinque supplies the telegraph occupation-time backbone and alternating switch
representation. B14 specializes it to equal rates, initial velocity `+u`, odd
count `2k+1`, and occupation time `T/2`; the `I_0` count weights, midpoint
atom, restriction consistency, and polygon-action estimate are project-derived
consequences. Cinque does not supply the zero-probability bridge version,
right-continuous midpoint protocol, or action estimate.

## Extraction and limits

The cached PDF and text hashes are respectively
`316edd890e42428d46cb88f8ae7ff10ca4fbd4bed86c2fde7180b24fc0be752b` and
`80754683e37d903f177ba51d426e3058741105712e0e8b922feb0f76776631d1`.
Raw extraction can lose fraction layout, so the substantive displayed formulas
were checked against the PDF render. No claim is made here about pages beyond
the stated pp. 1--4 coverage.

Coordinator independently checked the p. 4 PDF image and both hashes. At equal
rates the Mittag-Leffler denominator factor in (2.6) is
$E_{1,2k+2}^{k+1}(0)=1/(2k+1)!$, yielding the beta density used in the note.
The cached original remains in the ignored build area; this companion adds
selected reading rather than redistributing another PDF copy.

## Discovery-only source

Leonid Bogachev and Nikita Ratanov, *Occupation time distributions for the
telegraph process*, [arXiv:1007.3139v1](https://arxiv.org/abs/1007.3139v1)
(2010); journal DOI 10.1016/j.spa.2011.03.016 (2011).
Coordinator metadata/abstract reading on 2026-09-08 corrected the worker's
author attribution. The observable is occupation of a spatial half-line.
No PDF was downloaded and no theorem was imported; a further reading would
need to connect that observable to the bridge's midpoint before using it.
