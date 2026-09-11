# B47 source companion: fixed-coupling nonlinear calibration

## Result and bounded coverage

The bounded audit supports the *assumption route* used by R16: a finite-time
smooth Hamiltonian flow has a differentiable dependence on initial data and
parameters, so the stated `C^1` expansion of the four-record map can be
checked by differentiating the equations and applying finite-time variation of
constants. It does **not** supply the model-specific `O(lambda^3)` constants,
the invertible matrix `A`, or a global inverse theorem. Once those estimates
are established on a convex compact neighbourhood, the written lower-Lipschitz
argument gives injectivity and the minimum-residual error bound. This is not a
claim that pointwise rank alone gives global invertibility.

## Primary passages

1. **Sideris, *Ordinary Differential Equations and Dynamical Systems*, 2013,
   DOI 10.2991/978-94-6239-021-8, ch. 6.1, Theorem 6.1, printed pp. 89--90
   (one-based PDF pp. 96--97), and Corollary 6.1, printed p. 92.** The theorem states that
   for a `C^1` vector field the local solution is `C^1` in initial data and
   gives the variational equation for `D_p x`; the corollary extends the
   regularity with the vector field. Source: [author-hosted book](https://web.math.ucsb.edu/~sideris/pdffiles/BookPublishedComplete.pdf).
   This is the direct source precedent for
   differentiating the finite-time Hamilton equations and propagating a
   compact-domain derivative bound. The same book's Theorem 6.2 / Corollary
   6.3 (PDF pp. 98--99) gives continuous, respectively `C^k`, dependence on a
   parameter under the stated hypotheses; this supports treating preparation
   coordinates as finite parameters, subject to a common existence interval.
   Evidence level: passage (web PDF text opened; no claim made beyond the
   named theorem scope).

2. **Theurel, “Incompatible observables in classical physics: A closer look
   at measurement in Hamiltonian mechanics,” arXiv:2104.02064v2, PDF pp. 5--7,
   cached `.build/b36/theurel-2104.02064v2.pdf`, inherited B37 coverage.**
   These pages give the trapped Gaussian preparation, impulsive Hamiltonian
   coupling, stable pointer momentum, and the preparation-dependent precision /
   disturbance relations (Eqs. (8)--(22)). They are an interaction and
   preparation precedent, not an exact finite-duration autonomous four-record
   calibration and not evidence for a fixed-coupling global inverse. Evidence
   level: inherited passage digest; the worker confirmed it did not reopen or
   render Theurel in B47.

## Query and route record

One new search query was used (2026-09-11): `smooth dependence solutions
ordinary differential equations initial conditions theorem continuous
 differentiable dependence primary source PDF`. It led to the Sideris primary
 PDF, which was opened at the chapter-6 passage above. Theurel was reused from
B37, so no second new query was needed. Search results were discovery only;
the substantive statement above is anchored to the opened PDF passage and the
inherited B37 digest.

## Audit implications for R16

The source-backed premise is smooth finite-time dependence. The stronger R16
statement remains a project derivation requiring: a common compact energy
neighbourhood, cutoff margins, uniform `C^1` estimates, and a fixed positive
singular-value margin for `A`. Exact calibration removes known systematic
nonlinearity; it does not make an uncertain Hamiltonian or an inaccessible
record exact. The product limit is therefore conditional on the preparation
and record-error sequence contracting.

Suggested next ambiguity test: hold a **fixed positive incoming probe-width**
box (rather than letting `b` contract), retain exact final four-record access,
and use the full nonlinear map to test whether two receiver states can be
paired with distinct admissible incoming probe momenta giving the same record.
An implicit-function construction with margins would quantify the residual
state ambiguity and identify precisely what lower-width premise is needed.

## Coordinator review and coverage correction

Reopened Sideris, verified title/2013/DOI, and read Theorem 6.1 and its
variational equation, with proof route and corollaries in the chapter text.
Printed p. 89 is zero-based PDF index 95, not one-based page 95. Corollary
6.1 is printed p. 92 (PDF 99); Theorem 6.2 and Corollary 6.3 are pp. 92–93
(PDF 99–100). The screenshot request timed out; this check is text-level.
Theurel was inherited, not freshly visually inspected. Multiple theorem and
corollary selections exceed two short passages despite being grouped as one
chapter reading. The one query targets an assumption precedent, not an
exhaustive exact-result search. Novelty remains unassessed.
