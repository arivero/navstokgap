# Extending the Córdoba–Martínez-Zoroa IPM blow-up to uniformly space-time smooth forcing

> Source: [author-hosted PDF](https://cims.nyu.edu/~tristanb/ipm.pdf); [local PDF](AlpogeBuckmasterCoiculescu_IPM_2026.pdf).
> Metadata: Levent Alpöge (Anthropic PBC / alpoge@fas.harvard.edu), Tristan Buckmaster (Courant, NYU), Matei P. Coiculescu (Courant, NYU); preprint, 57 pages, no arXiv identifier at retrieval.
> Extraction: `pdftotext -layout`; selective reading notes. Downloaded 2026-09-08 from the author's institutional page.

## Source digest

Cited result, Theorem 2.1 (PDF p. 3). There exist an odd, zero-mean initial density
$\rho_{\rm in}\in C^\infty(\mathbb T^2)$ and an odd, zero-mean force
$F\in C^\infty([0,1]\times\mathbb T^2)$ such that the forced IPM equation
$\partial_t\rho+u_T(\rho)\cdot\nabla\rho=F$ has a solution with
$\rho\in C^\infty([0,T]\times\mathbb T^2)$ for every $T<1$, with
$\rho(t)\to\rho_*$ in $C^\eta(\mathbb T^2)$ for every $0\le\eta<1$, and with

$$\lim_{t\uparrow1}\|\nabla\rho(t)\|_{L^\infty}=\lim_{t\uparrow1}\|D_xu_T(\rho(t))\|_{L^\infty}=\infty.$$

The velocity $u_T$ is the periodic zero-order Darcy multiplier fixed in equation (1), p. 3.

The refinement mechanism is stated on pp. 3–4. A single plane wave $\vartheta=A\sin(k\cdot x)$ is an
exact unforced steady state, because the Darcy multiplier vector is perpendicular to $k$. Localizing
that wave destroys stationarity, and **the nonlinear residual is then taken as the force**. Levels are
indexed by frequency $q$; the parent of level $q+1$ is the complete preceding density after a smoothing
Fourier cutoff, $P_{q+1}=S_{\mu_{q+1}}\rho^{(q)}$. Amplitude is tied to the oscillation parameter in a
frequency-dependent way, so the level amplitude stays small while its gradient grows. Infinitely many
levels are placed inside the finite interval $[0,1)$.

## Source-facing notes

The forced problem is what is solved here. Alternatives A and B of the Millennium statement require
$f=0$; this construction lives on the side that permits forcing ([local definitions](../../../notes/millennium-problem-definitions.md)).

Attribution stated by the authors, pp. 2–3: the multiscale induction, transported phase, finite
asymptotic velocity expansion and phase-harmonic cancellation are due to Córdoba and
Martínez-Zoroa [1]. New here are Fourier-space truncations avoiding derivative loss, a mixed
space–time induction giving a space–time smooth force, transport of packets by Fourier-truncated
rather than jet-truncated velocity, and an exact series avoiding a nonconstructive nonlinear limit.

AI-use statement, p. 3: the introduction (apart from the literature review paragraph) was written by
the listed authors; the remainder was written with Claude and Codex under the authors' direction.

Announcement of the companion results, pp. 2–3: Boussinesq and Euler are said to be formally verified
in Lean, and the PDF prints the identifying artifact hashes as the literal unfilled placeholders
`[BOUSSINESQ SHA-256]`, `[EULER SHA-256]`. No Lean artifact accompanies the release.

Review scope: title page, abstract, introduction pp. 1–4, Theorem 2.1 and the strategy subsection,
reference list. The 50-page construction is read for structure only; no proof audit is claimed.
