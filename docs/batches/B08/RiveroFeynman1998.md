# Rivero: a short derivation of Feynman formula

> Source: [arXiv:quant-ph/9803035v1](https://arxiv.org/abs/quant-ph/9803035v1); stable local research copy `.build/m05/Rivero_FeynmanFormula_1998.pdf`.
> Metadata: Alejandro Rivero, *A short derivation of Feynman formula*, arXiv:quant-ph/9803035v1, submitted 14 March 1998.
> Extraction: all three pages extracted with `pdftotext -layout` and checked visually. SHA-256 `f4ac9355052c93c724c55c0354b080b6851cd6185eb4d84bbfdc60d51617349b`.

## Result used

Rivero proposes an oscillatory finite-dimensional representation in equations (2)--(4), then a time-discretized two-regulator expression in (5), a still-unspecified control transformation in (6), proportional control in (7)--(9), and an invariance statement in (10). This is provenance for the regulator question, not a proof of the draft's normalized free-kernel map.

## Selected coverage

- Printed p. 1, equations (1)--(4): a formal gradient-delta representation and a "halved" oscillatory amplitude whose modulus square is intended to recover a critical-point weight.
- Printed p. 2, equations (5)--(9): the exponent contains the time step (\epsilon'\) multiplying the discrete Lagrangian sum; (\epsilon) and (\epsilon') are the two regulators. Equation (6) is expressly left unspecified, while (7) sets the controlled phase coefficient (h).
- Printed p. 3, equations (10)--(11) and final discussion: proposed control invariance and tangent-groupoid motivation.

The PDF title page was regenerated with an August 2018 date, but the versioned arXiv identifier supplies the 1998 submission date. Rivero suppresses normalization constants in the passage from the amplitude to its modulus square; the draft's ((2\pi\epsilon)^{-d/2}), determinant, and Fourier convention must therefore be checked independently.

## Evidence boundary

Audited 2026-09-07. This batch reuses the original documented in
`docs/Rivero_FeynmanFormula_1998.md`. Rights: arXiv research copy; redistribution
permission unresolved, so original bytes stay in ignored `.build/`.

Reading level: full-read of this three-page working draft. The source supports the existence and intended interpretation of the two regulators. It does not establish convergence, dimensional consistency under a physical Lagrangian, or the running-bare-mass formula.
