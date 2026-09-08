# B17 crossover source companion

## Cinque (exact cached source)

> Source: https://arxiv.org/pdf/2202.01904v1
> Local cache: .build/b09/Cinque2022.pdf
> Metadata: Fabrizio Cinque, “A Note on the Conditional Probabilities of the Telegraph Process,” arXiv:2202.01904v1, 3 February 2022.
> SHA-256: 316edd890e42428d46cb88f8ae7ff10ca4fbd4bed86c2fde7180b24fc0be752b
> Extraction: pdftotext -layout; printed pp. 3–4 also checked against PDF rendering.

### Read coverage and use

Printed p. 3 Remark 2.1 and (2.4) identify the odd alternating switch-time sum with occupation time at the initial velocity. Printed p. 4 Theorem 2.1, (2.6), gives its conditional density for odd switch count. At equal rates the Mittag–Leffler denominator reduces to the factorial factor used in the C033 and C037 derivation. These are exact source matches.

The selected pages do not state the return bridge, midpoint split, beta parameters (k+1,k), midpoint atom, combined-sector factorial sum, action coefficient, or mass-universal finite-window implication. Those are project-derived consequences. No pages beyond 3–4 were used.

Coordinator reread both pages and visually checked p. 4, including the even-count
formula (2.5) as well as (2.6). Equal rates turn their Mittag-Leffler factors
into reciprocal factorials. Multiplication by the Poisson weights and the
position Jacobian gives the segment densities in the note. The original hash
was independently rechecked. Cached original rights/retrieval remain documented
in B09; this batch adds selected reading and keeps the PDF out of publication.

## Bogachev–Ratanov (abstract-level discovery check)

> Source: https://arxiv.org/abs/1007.3139v1
> Metadata: Leonid Bogachev and Nikita Ratanov, “Occupation time distributions for the telegraph process,” arXiv:1007.3139v1 (2010); journal DOI 10.1016/j.spa.2011.03.016 (2011).
> Coverage: abstract and online text route only; no local PDF downloaded.

The source studies occupation of the positive half-line and long-time arcsine-type limits. It is not a return-endpoint bridge and no theorem from it is used in C037/C038.

## DLMF (online special-function anchor)

> Source: https://dlmf.nist.gov/10.32.E1 (redirects to section 10.32)
> Metadata: NIST Digital Library of Mathematical Functions, section 10.32, integral representations, formula 10.32.1.
> Coverage: formula page opened 2026-09-08; no local cache required.

Formula 10.32.1 is the integral representation for the modified Bessel function I0(z). It supports the note’s normalized-exponential concentration argument. The subsequent ratio limit and l’Hôpital step are derived in the project note.

## Search limits

Two targeted searches and two primary openings were allowed and consumed. No exact match for the conditioned midpoint beta law or common-window mass conclusion was found. This is bounded coverage, not a novelty result.
