# B52: local inverse stability for the revealed-clock-position result

## Result and bounded coverage

The bounded audit found a close standard quantitative inverse-function precedent for C098: an invertible linear map plus a perturbation whose Lipschitz norm is smaller than the reciprocal inverse-operator norm gives a bi-Lipschitz inverse, with an explicit inverse Lipschitz constant. This supports the *form* of the derivative-closeness estimate used in R21. It does not establish the model-specific energy-speed Schur-complement sign, the eight-record Hamiltonian map, its uniform (C^1) convergence, or the canonical risk-product constant in C099. Literature novelty is unassessed.

## Primary source and exact reading

Alberto Freire, *Inverse Function Theorem and Surfaces in \(\mathbb R^n\)*, University of Tennessee lecture notes, PDF (date not stated on the retrieved document):
https://web.math.utk.edu/~afreire/teaching/m447f16/InverseFunctionTheorem.pdf

Passage-level reading of the four relevant PDF pages (pp. 1, 2, 3 and 5 of the 14-page PDF):

* pp. 1–3, “The inverse function theorem as an existence theorem” and Proposition 1 (p. 3): for (f(x)=Ax+\phi(x)), boundedly invertible (A), and \(\operatorname{Lip}(\phi)<\|A^{-1}\|^{-1}\), the contraction argument gives a homeomorphism onto the image with Lipschitz inverse. The displayed estimate gives \(\operatorname{Lip}(f^{-1})\le \|A^{-1}\|/(1-\lambda)\), where \(\lambda=\|A^{-1}\|\operatorname{Lip}(\phi)\).
* p. 3, “Inverse Function Theorem”: strong differentiability at a point with invertible derivative yields a local bi-Lipschitz homeomorphism; the proof obtains the result by making the Taylor remainder’s Lipschitz constant small relative to \(\|df(a)^{-1}\|^{-1}\).
* pp. 5–6, Corollary 2 (hypotheses on p. 5; conclusion and proof checked by the coordinator on p. 6): on a convex domain, \(f(x)=x+\phi(x)\) with \(\sup\|d\phi\|\le\lambda<1\) is a diffeomorphism onto its image. This is the direct segment-integration/derivative-closeness analogue of R21 Eq. (5)–(6), after conjugating by \(J\).

Evidence level: passage. The source is an institutional lecture note; no author date or DOI was established. No full-read or exhaustive prior-art claim is made.

## Claim-by-claim audit

**C098 (augmented energy/eight-record map has a uniform local lower Lipschitz bound): partial established-method match, model-derived result.** Freire’s perturbation proposition and Corollary 2 justify the general mechanism: on a convex fixed neighbourhood, if \(D\mathcal G_\lambda\) stays within a strict operator-norm margin of an invertible reference \(J\), then the map is injective there and its inverse is Lipschitz. The source’s hypotheses are a fixed linear reference and a globally small Lipschitz perturbation on the selected domain. R21 must still prove (and does in its draft) that (i) the augmented Jacobian (J) is invertible via the energy-speed Schur complement \(\tau>0\), (ii) the neighbourhood is convex and remains inside physical margins, and (iii) the required (C^1) convergence is uniform in \(0\le\lambda\le\lambda_0\). The source does not supply any of those Hamiltonian facts. The draft’s direct bound \(\|\mathcal G_\lambda(w)-\mathcal G_\lambda(w')\|\ge\gamma\|w-w'\|/2\) is therefore a derived application of a standard method, not an established theorem about this apparatus.

**C099 (minimum-residual recovery and canonical risk product): no exact literature match found in budget.** The source’s inverse Lipschitz estimate supports the intermediate residual-to-state step: if the true and fitted exact records differ by at most (2\delta), then a lower Lipschitz constant \(\gamma/2\) gives \(\|\widehat w-w\|\le4\delta/\gamma\). The factor 4 follows from R21’s residual convention, and the product bound \(16L_*P_*\max(\rho_\pi/\lambda,\rho_q)^2/\gamma^2\) is a model-derived consequence of coordinate-wise risk bounds and unit conversion. Freire does not discuss noisy records, minimum-residual estimators, canonical products, or action scales. Exact energy equality for the fitted candidate and compactness/existence of a minimizer remain R21 assumptions.

## Coverage and stopping point

One web query was used (2026-09-11), targeting a quantitative inverse-function theorem with a derivative/Lipschitz-closeness hypothesis. One primary institutional source was opened and the four named PDF pages above were inspected. Search-result snippets were discovery leads; only the named PDF passage counts as evidence. No second query, source, or numerical/symbolic verification was used. This is bounded coverage, not a novelty or exhaustiveness result.

## Source-to-model idea for R22

Reuse the source’s perturbation parameter \(\lambda=\|J^{-1}\|\operatorname{Lip}(\phi)\) as a diagnostic on the full energy shell: track the smallest local augmented singular margin (equivalently the largest inverse norm) as clock speed varies. A zero or loss of the strict margin identifies where the local R21 estimate can fail. Independently test whether an actual global common-record branch exists: local invertibility alone does not imply global injectivity. This separates conditioning loss from a genuine exact ambiguity.


## Coordinator correction

Verified the inverse estimate and Proposition 1 on pp. 1–3, and Corollary 2
on pp. 5–6, with visual inspection of p. 5. The worker listed pages 1,2,3,5;
its opening “pp. 1–4” and placement of Proposition 1 on pp. 1–2 were corrected.
The corollary continues onto p. 6, read separately by the coordinator. No
additional search query or source was used. The source contraction parameter
is distinct from the apparatus coupling despite the shared lambda notation.
