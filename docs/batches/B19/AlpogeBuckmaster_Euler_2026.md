# Blowup for the Euler equations with smooth forcing

> Source: [author-hosted PDF](https://cims.nyu.edu/~tristanb/euler.pdf); [local PDF](AlpogeBuckmaster_Euler_2026.pdf).
> Metadata: attributed to Levent Alpöge and Tristan Buckmaster by the [released statement](Buckmaster_Statement_2026-09-08.md) and by reference [1] of the [Boussinesq preprint](AlpogeBuckmaster_Boussinesq_2026.md). The PDF itself carries no author byline and no acknowledgments section. Preprint, 112 pages, no arXiv identifier at retrieval.
> Extraction: `pdftotext -layout`; selective reading notes. Downloaded 2026-09-08 from the author's institutional page.

## Source digest

Cited result, Theorem 1.1 (PDF p. 2). For every $r_0>0$ and $z_0\in\mathbb R$ there exist $T_*>0$,
$0<R<r_0/2$, a divergence-free axisymmetric $u_0\in C_c^\infty(T_R;\mathbb R^3)$ with nonzero swirl and
zero meridional velocity, and an axisymmetric force $f\in C^\infty(\mathbb R^3\times[0,T_*];\mathbb R^3)$
supported in the fixed solid torus $T_R$, such that the forced incompressible Euler equations have a
solution $(u,p)\in C^\infty(\mathbb R^3\times[0,T_*))$ with, writing $\Gamma=ru^\varphi$ and
$\omega=\operatorname{curl}u$,

$$\sup_{t<T_*}\big(\|\Gamma(t)\|_\infty+\|u^r(t)\|_\infty+\|u^z(t)\|_\infty\big)<\infty,\qquad
\lim_{t\uparrow T_*}\|\nabla\Gamma(t)\|_\infty=\lim_{t\uparrow T_*}\|\omega(t)\|_\infty=\infty,$$

together with $\int_0^{T_*}\|\omega(t)\|_\infty\,dt=\infty$, which is the Beale–Kato–Majda quantity.
Uniqueness holds before blowup in a finite-energy, locally space–time Lipschitz class with bounded
spatial gradients, and the competing solution need not be axisymmetric.

The amplification mechanism, §1.2 p. 2. Circulation transports the swirl; its square generates azimuthal
vorticity through the fixed axial derivative; the resulting meridional velocity amplifies the circulation
gradient. Each localized oscillation is transported by the exact nonlinear flow of the preceding fields,
and each addition returns the principal azimuthal-vorticity amplitude at its material centre to zero
before the next layer grows. Higher-order corrections make the physical force increments summable
together with all mixed space–time derivatives.

## Source-facing notes

The Boussinesq companion's local two-field calculation runs on an affine background with a constant
elliptic symbol. For Euler the symbol and the buoyancy coefficient vary across the support, so the
amplitudes depend on material position and the transporting velocity includes all preceding
corrections (§1.2, p. 2). That dependence is the stated source of the length difference between the two
papers.

Presentation. The author of the [statement](Buckmaster_Statement_2026-09-08.md) describes this writeup
as machine-generated text that had not yet been rewritten, and apologises for its state. Read it as a
preliminary release. Sections 7–12 use a private notation for rate lists and moments (the `a@X` entries)
introduced at p. 27 and never cross-checked here.

Review scope: title page, abstract, §1.1–§1.3 pp. 1–3, Theorem 1.1, the closing proof of Theorem 1.1 at
p. 112 and the reference list. The construction in §§2–13 is read for structure only; no proof audit is
claimed.
