# An exact gauge-quotient Feshbach split for periodic lattice Maxwell theory

**Manuscript A — full working draft.** Author and affiliation details are intentionally omitted pending approval. This is a focused benchmark article; the literature-positioning and specialist theorem audit remain to be completed before journal submission.

## Abstract

We give an exact finite-volume decomposition of the free Maxwell Hamiltonian on a periodic cubic spatial lattice. The physical configuration space is formed by quotienting lattice one-forms by exact forms and separating harmonic holonomies from coexact transverse modes. The nonconstant modes have the lattice dispersion
\[
q_a(k)=\frac2a\left(\sum_{i=1}^3\sin^2\frac{k_i a}{2}\right)^{1/2},
\]
so their least excitation costs \(\hbar c(2/a)\sin(\pi/N_s)\) on a torus of side \(L=N_sa\). Projection onto the transverse Fock vacuum reduces the Hamiltonian and has identically zero Feshbach off-diagonal. The calculation gives an exactly solvable reference for fibre-projection methods in interacting gauge systems, with the harmonic sector retained as a slow factor.

**Keywords:** lattice Maxwell theory; discrete Hodge decomposition; Feshbach map; gauge quotient; periodic boundary conditions.

## 1. Introduction

Projection methods separate low-energy variables from faster degrees of freedom. In a gauge theory, the projection must act on physical states, and a useful estimate must control both the energy of discarded modes and their coupling to the retained sector. The free periodic Maxwell field provides a precise reference case: gauge reduction, mode separation, dispersion, and the off-diagonal block can all be computed exactly.

The result is a finite-lattice statement. We describe the transverse excitation scale at fixed spatial size and identify why the Feshbach correction vanishes in this model. A nonzero correction in an interacting non-Abelian fibre problem requires additional estimates; it is not supplied by the free calculation.

## 2. The physical quotient and the mode split

Let \(\Lambda_{a,L}\) be the three-dimensional periodic cubic lattice with spacing \(a\), \(N_s\) sites per direction, and \(L=N_sa\). Denote real lattice cochains by \(C^q(\Lambda;\mathbb R)\), the coboundary by \(d\), and its adjoint in the translation-invariant lattice inner product by \(d^*\). A real lattice connection is a one-cochain \(A\), with gauge transformations \(A\mapsto A+d\chi\).

The discrete Hodge decomposition gives
\[
C^1/dC^0\simeq\mathcal H^1\oplus\mathcal T,\qquad
\mathcal T=\{A:d^*A=0,\ A\perp\mathcal H^1\},
\tag{1}
\]
where \(\mathcal H^1\) is the three-dimensional harmonic subspace. We use the quotient inner product and do not select a gauge-fixed representative. For a compact \(U(1)\) theory, large gauge transformations make the harmonic holonomies periodic. In the Gaussian regulator used below, this compact harmonic factor is retained separately from the noncompact transverse Gaussian factor; this convention makes the mode split explicit.

Canonical quantization yields
\[
\mathcal H_{\rm phys}=\mathcal H_{\rm harm}\otimes\mathcal F(\mathcal T_{\mathbb C}),
\tag{2}
\]
with \(\mathcal H_{\rm harm}=L^2(U(1)^3)\) when compact holonomies are retained. The transverse Hamiltonian, after normal ordering, is
\[
H_\perp=\sum_{k\ne0}\sum_{\lambda=1}^2
\hbar c\,q_a(k)\,a^*_{k,\lambda}a_{k,\lambda},
\tag{3}
\]
where
\[
k_i=\frac{2\pi n_i}{L},\quad n_i\in\{0,\ldots,N_s-1\},\qquad
q_a(k)=\frac2a\left(\sum_{i=1}^3\sin^2\frac{k_i a}{2}\right)^{1/2}.
\tag{4}
\]
The physical Hamiltonian has the tensor-sum form
\[
H_{a,L}=H_{\rm harm}\otimes1+1\otimes H_\perp.
\tag{5}
\]
The harmonic degrees of freedom are slow variables. Equation (5) follows because \(d\mathcal H^1=0\), while diagonalization of \(d^*d\) on \(\mathcal T\) gives (4).

## 3. The exact transverse threshold

The least nonzero lattice momentum has one component of magnitude \(2\pi/L\); consequently
\[
q_{a,\min}=\frac2a\sin\frac\pi{N_s}.
\tag{6}
\]
For \(N_s\ge2\), the sine argument lies in \((0,\pi/2]\), and \(\sin x\ge x(1-x^2/6)\) gives
\[
q_{a,\min}\ge\frac{2\pi}{L}\left(1-\frac{\pi^2}{6N_s^2}\right).
\tag{7}
\]
At fixed \(L\), \(q_{a,\min}\to2\pi/L\) as \(a\downarrow0\).

Let \(\Omega_\perp\) be the transverse Fock vacuum and define the physical projection
\[
P=1_{\rm harm}\otimes|\Omega_\perp\rangle\langle\Omega_\perp|,
\qquad \bar P=1-P.
\tag{8}
\]

**Theorem 1 (periodic Maxwell fibre estimate).** On the Hilbert space (2),
\[
\bar P H_{a,L}\bar P\ge
\bar P\bigl(H_{\rm harm}+\hbar c\,q_{a,\min}\bigr)\bar P,
\tag{9}
\]
and
\[
PH_{a,L}\bar P=0.
\tag{10}
\]
For every energy \(E\) in the resolvent set of the complementary block, the Feshbach term is therefore
\[
PH_{a,L}\bar P\,(\bar P H_{a,L}\bar P-E)^{-1}\,\bar P H_{a,L}P=0.
\tag{11}
\]

*Proof.* Every vector in \(\operatorname{ran}\bar P\) contains at least one transverse oscillator quantum. Each term in (3) is nonnegative and each nonzero momentum has frequency at least \(q_{a,\min}\); adding the independent harmonic Hamiltonian proves (9). The Hamiltonian (5) preserves transverse particle number and is a tensor sum, so \(P\) reduces it and (10) follows. Equation (11) is immediate. \(\square\)

## 4. Interpretation and use

The lower bound is a separation above the transverse vacuum fibre, not a statement about every possible degeneracy or energy in the retained harmonic sector. It is gauge invariant because both the quotient (1) and the projection (8) are defined after longitudinal modes have been removed.

The calculation isolates three data needed in a non-Abelian analogue: a gauge-covariant physical projection, a lower bound on the discarded fibre, and a relative estimate on the off-diagonal block. Here the first two are exact and the third vanishes. The model is useful as a calibration case for sign, normalization, and finite-volume conventions in Feshbach estimates.

## 5. Conclusion

For the periodic Gaussian Maxwell regulator, the nonconstant transverse sector has an explicit least energy and is exactly decoupled from the harmonic sector. This gives a clean finite-dimensional Fourier/Hodge benchmark for more difficult fibre reductions. A journal submission should compare this formulation with the established torus Maxwell spectrum and standard Feshbach theory, and should retain the regulator convention of Section 2.

## References for the submission pass

- The repository derivation and convention map: `notes/u1-maxwell-fibre-feshbach-benchmark.md`.
- Add primary references on discrete Hodge decomposition, canonical Maxwell theory on a torus, and Feshbach reduction after the result-specific literature review.
