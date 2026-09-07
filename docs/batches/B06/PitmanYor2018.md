# Pitman and Yor, *A guide to Brownian motion and related stochastic processes*

> Source: https://arxiv.org/abs/1802.09679v1
> Metadata: Jim Pitman and Marc Yor, 2018, arXiv:1802.09679v1, 27 February 2018.
> Extraction: `pdftotext -layout`; page anchors below are printed pages. Formula layout was checked against the PDF for the cited equations.

## Source digest

Pitman and Yor state the standard Brownian transition density
\[
p_t(x,y)=(2\pi t)^{-1/2}\exp[-(y-x)^2/(2t)]
\]
and identify its Chapman–Kolmogorov identity with addition of independent Gaussian increments (printed pp. 12–13, eqs. (20)–(25)). They give the finite-dimensional Markov product formula (eq. (20) and the display following it), so conditioning on endpoints can be handled by products of transition densities.

For a bridge from \(x\) to \(y\) over \([0,T]\), §3.4, printed p. 10, constructs
\[
B^{x,y,T}_u=x+B_u-(u/T)B_T+(u/T)(y-x),
\]
using independence of the centered Gaussian bridge component and \(B_T\). The standard bridge is centered Gaussian with covariance \(s(1-t)\) for \(s\le t\) (printed p. 6, eqs. (4)–(5)); hence its one-time variance is \(u(T-u)/T\) after scaling.

The source supports the stochastic/heat-kernel setting, not the project’s action notation. Replacing Brownian variance \(t\) by \(\kappa t/m\) is a direct scaling. The finite-dimensional concentration as \(\kappa\to0\) is a derived Chebyshev/union-bound consequence, not a theorem quoted from this source.

## Relevant transcription anchors

Coordinator correction, 2026-09-07: (4)–(5) are on printed **p. 6**, not p. 5.
On p. 10 the second equality of the bridge display omits `/T` from the
deterministic interpolation; the preceding equality is correct. The manuscript
derives it independently. Coordinator visually checked pp. 10 and 13 and read
pp. 6, 10, 12–14.

Stable original: `.build/cone-refinement/PitmanYor2018.pdf`, retrieved 2026-09-07.
SHA-256: `44dd2ce290403125d26ba5ae1ecfbcffff2495a30c74ed2eb2cbee425fe8548b`.
Rights: linked arXiv research copy; redistribution permission has not been
established, so original bytes stay outside the published repository.

- Printed p. 12–13, eqs. (20)–(25): transition kernels, Chapman–Kolmogorov, finite-dimensional products, and normalized Brownian density.
- Printed p. 10, §3.4: endpoint bridge construction and linear mean.
- Printed p. 6, eqs. (4)–(5): centered Gaussian standard bridge and covariance.
- Printed p. 16, eqs. (31)–(32): Brownian generator and heat equation; this supports the heat-kernel interpretation but not the project’s mass/action rescaling verbatim.
