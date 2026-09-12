# B59: calibrated canonical ambiguity

## Result and bounded coverage

The bounded audit finds method support for the smooth-flow, contraction, and
implicit-function steps used by R28/C112--C113. It finds no source that
establishes the calibrated Hamiltonian apparatus, the two scaled residual
limits, the pulse-kernel construction, or the deterministic canonical
risk-product bound. Those are model-derived consequences whose proof depends
on the displayed equations and margins. Prior-art novelty is unassessed.

Worker coverage was zero discovery queries and no fresh source opening. Freire
pp. 1--3, Sideris, and the fixed-point chapter were read here only through
the inherited B54/B50--B56/B48 companions; the three-page Freire route is
therefore inherited worker evidence. Coordinator subsequently opened Freire
and checked pp. 1–3, including the smooth inverse statement on p. 1 and
the perturbation and local inverse statements on p. 3. No exhaustive
literature search or full-source read is claimed.

## Source routes and evidence

**Alberto Freire**, *Inverse Function Theorem and Surfaces in R^n*,
University of Tennessee lecture notes,
<https://web.math.utk.edu/~afreire/teaching/m447f16/InverseFunctionTheorem.pdf>.
Evidence level: passage, pp. 1--3, inherited through B54 (not freshly opened
by the worker; coordinator checked pp. 1–3 directly). Pages
1--2 treat `f(x)=Ax+phi(x)` with invertible `A` and Lipschitz `phi`; a strict
bound `||A^-1|| Lip(phi)<1` gives a contraction and a Lipschitz inverse.
Proposition 1 on p. 3 states the corresponding global homeomorphism and
inverse estimate. The inverse-function discussion on p. 3 gives a local
bi-Lipschitz conclusion when the derivative is invertible and the remainder
has a sufficiently small Lipschitz constant. This supports generic inverse
and perturbation methods only.

**Thomas C. Sideris**, *Ordinary Differential Equations and Dynamical
Systems*, Chapter 6, printed pp. 89--90, 92--93 (PDF pp. 96--97, 99--100).
Evidence level: passage inherited from B50/B55/B56. Smooth dependence of a
finite-time ODE flow on initial data and parameters supports the regularity
assumed for `G_lambda`; it does not supply R28's common flow domain, cutoff
margins, or uniform estimates.

**Frankfurt-hosted lecture chapter**, *Fixed point theorems*, Theorems
1.4--1.5 and Corollary 1.7, PDF pp. 4--5. Evidence level: passage inherited
from B48/B56. Banach contraction and parameter perturbation estimates support
an apparatus compensator once the self-map and strict contraction have been
proved. They do not establish the Hamiltonian energy adjustment or its
derivative.

## Claim-by-claim audit

**C112 (exact common-record canonical curve): method-supported,
model-derived.** Sideris and Freire support smooth finite-time dependence and
the implicit/inverse continuation pattern. The compensator estimate (1),
smooth divisibility in (3), the Hamiltonian signs and coefficients, and the
uniform preparation-box margin are all specific to R28 and require direct
written verification. At `lambda=0`, the claimed derivative rows are
`dH_s`, `A`, and `B`; their independence follows only after the pulse design
and the stated receiver dynamics have been checked. The four-equation IFT
also requires a jointly smooth extension in `(lambda,w)` at zero, not merely
pointwise divisibility of each numerator.

**C113 (positive deterministic canonical risk product): model-derived,
conditional on C112.** Once two admissible endpoints have the same complete
record and both canonical separations in (9), the triangle-inequality bounds
in (10) are elementary and source-independent. Freire does not establish a
minimax estimator, a product normalization, or a positive universal action
floor. The stated constant remains dependent on energy, preparation, coupling
range, masses, and fixed pulse design.

## Proof issues and source-to-model next test

The main proof obligations are to write an explicit jointly smooth quotient
for `U_lambda,V_lambda`, prove the pulse rank and nonzero canonical kernel
direction for one fixed positive smooth pulse, and verify that all exact
energy and record equations remain inside the cutoff and clock-speed margins
on the compact IFT rectangle. The phrase “analytic observability spans all
four dimensions” needs either a direct rank argument for the selected pulse
times or a clearly stated inherited lemma. The endpoint integration in (9)
also needs the derivative-sign neighborhood to be uniform in `lambda`.

Source-to-model suggestion: formulate the complete constrained residual map
as a single augmented map and state its joint `C^1` norm and invertible
reference derivative explicitly. Then apply Freire's perturbation margin to
the augmented map, while separately retaining the model calculation of the
three limiting rows. This tests whether the zero-coupling quotient and the
finite-coupling curve share one uniform neighborhood.
