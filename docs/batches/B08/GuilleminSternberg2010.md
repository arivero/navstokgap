# Guillemin and Sternberg: exact quadratic stationary phase

> Source: [Victor Guillemin's MIT-hosted PDF](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf); stable local research copy `.build/b08/GuilleminSternberg_SemiclassicalAnalysis.pdf`.
> Metadata: Victor Guillemin and Shlomo Sternberg, *Semi-classical analysis*, 13 January 2010.
> Extraction: `pdftotext -layout`; the three selected pages and equation (14.7) were checked visually. SHA-256 `7a93a81009fcfe4637377e632fb9595b2015874e5ce5d78287bc19fd126d0d27`.

## Result used

For a real nonsingular symmetric matrix (A), the notes derive the exact Fourier identity for a quadratic oscillatory integral, including the determinant, signature phase, and inverse quadratic form. With (A>0), (t=1/\epsilon), a translation by (q_*), and the notes' unitary Fourier convention, equation (14.7) gives exactly the Fourier factors used in the draft.

## Selected coverage

- Printed p. 463, equations (14.5)--(14.6): (n)-dimensional Fresnel integral, determinant magnitude, and signature phase, extended from diagonal to arbitrary nondegenerate quadratic forms by an orthogonal change of coordinates.
- Printed p. 464, equation (14.7): exact Fourier formula for (f\in\mathcal S(\mathbb R^n)), a nonsingular symmetric (A), and (t>0); proof by diagonalization and density of product functions.
- Printed p. 465: substitution (t=\hbar^{-1}), the Fourier-side factor, and its Taylor expansion.

The source allows indefinite nonsingular (A), using (|\det A|) and (e^{i\pi\operatorname{sgn}A/4}). The draft deliberately assumes SPD (A), so these reduce to (\det A) and (e^{i\pi d/4}).

## Evidence boundary

Retrieved and audited 2026-09-07. Rights: author-hosted research copy with
redistribution permission unresolved; original bytes stay in ignored `.build/`.
Coordinator independently verified the title/date and (14.7) visually and read
pp. 463–465. On p. 464 an intermediate one-dimensional rewritten display omits
the signature in its phase; the general formula (14.7) retains it correctly.
The project's positive-definite specialization agrees with both displays.

Reading level: passage, three printed pages. The exact amplitude formula is an established match. Taking its limit by dominated convergence and identifying ( |O(q_*)|^2/\det A) with the pullback distribution (\delta^{(d)}(\nabla F)) are elementary consequences, not statements quoted from these pages.
