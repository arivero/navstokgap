# Pitman and Yor: Brownian motion and bridges

> Source: [arXiv:1802.09679v1](https://arxiv.org/abs/1802.09679v1); stable local research copy `.build/cone-refinement/PitmanYor2018.pdf`.
> Metadata: Jim Pitman and Marc Yor, *A guide to Brownian motion and related stochastic processes* (2018), arXiv:1802.09679v1.
> Extraction: `pdftotext -layout`; formulas on the four selected pages were checked visually against the PDF. SHA-256 `44dd2ce290403125d26ba5ae1ecfbcffff2495a30c74ed2eb2cbee425fe8548b`.

## Result used

The source gives the continuous standard Brownian bridge and its covariance, an endpoint-bridge construction, and the Markov finite-dimensional density/Chapman--Kolmogorov formulas. After the direct variance rescaling (B^T\mapsto\sqrt{\kappa/m}B^T), these facts support the common-bridge coupling and identify the partition-node Gaussian law in the draft. They do not state the draft's chi-square action law or the joint (d\kappa\) limit; those are derived in the draft.

## Selected coverage

- Printed p. 6 (PDF p. 7), equations (4)--(5): the standard bridge is a continuous centered Gaussian process with covariance (s(1-t)) for (s\leq t\) on ([0,1]).
- Printed p. 10 (PDF p. 11), section 3.4: bridge from (x) to (y) over ([0,T]). The first displayed expression is correct; its following rewritten expression visibly omits `/T` in the deterministic interpolation term.
- Printed pp. 12--13 (PDF pp. 13--14), equations (20)--(25): Markov finite-dimensional products, Chapman--Kolmogorov composition, and the Brownian Gaussian transition density.

At dispatch the earlier B06 companion contained two stale references to printed
p. 5 before its explicit correction to p. 6. The coordinator corrected those
remaining references during integration and visually verified p. 6 again.

## Evidence boundary

Audited 2026-09-07. This batch reuses the original documented by B06.
Rights: arXiv research copy; redistribution permission unresolved, so the
original stays in ignored `.build/`.

Reading level: passage, four printed pages. The continuous covariance and Markov-product ingredients are cited from the source. Scaling by (\kappa/m), the arbitrary-partition precision matrix, whitening, and the simultaneous uniform-path/(L^2)-action limit are project derivations.
