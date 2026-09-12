# B60: two-calibration branches

## Result and bounded coverage

This inherited-source audit finds method support for the smooth-flow,
contraction, and local inverse/continuation pattern used by R29/C114--C115.
It does not establish the new pulse-kernel coefficients, the rank of the
three calibrated rows, existence of two positive-coupling roots, or the
canonical global risk bound. Those statements remain model-derived and
conditional on the displayed R29 equations and margins. Exact prior-art
matches and novelty are unassessed.

Coverage is restricted to the inherited B59 companions: zero discovery
queries, zero fresh retrievals, and no fresh page claims. Freire pp. 1--3,
Sideris printed pp. 89--90 and 92--93 (PDF pp. 96--97, 99--100), and the
Frankfurt fixed-point chapter, Theorems 1.4--1.5 and Corollary 1.7 (PDF
pp. 4--5), are reported only at the inherited passage level. The coordinator
must verify any passage used for acceptance; no exhaustive literature search
or full-source read is claimed here.

## Inherited source routes

**Alberto Freire**, *Inverse Function Theorem and Surfaces in R^n*, University
of Tennessee lecture notes, pp. 1--3,
<https://web.math.utk.edu/~afreire/teaching/m447f16/InverseFunctionTheorem.pdf>.
The inherited reading treats contraction estimates for `f(x)=Ax+phi(x)` with
invertible `A`, a strict `||A^-1|| Lip(phi)<1` margin, and local inverse/
bi-Lipschitz consequences. This supports the abstract residual-map strategy,
not R29's four rows or physical normalization.

**Thomas C. Sideris**, *Ordinary Differential Equations and Dynamical
Systems*, Chapter 6, printed pp. 89--90, 92--93 (PDF pp. 96--97, 99--100).
The inherited passage supports smooth dependence of finite-time ODE flows on
initial data and parameters. It supplies no common-domain, cutoff, clock,
or uniform preparation-box estimate for this apparatus.

**Frankfurt-hosted lecture chapter**, *Fixed point theorems*, Theorems 1.4--1.5
and Corollary 1.7, PDF pp. 4--5. The inherited Banach contraction and parameter
perturbation estimates support a self-map argument once its contraction and
residual bounds have been proved. They do not derive Hamiltonian adjustments,
pulse responses, or action units.

## Claim-by-claim audit

**C114 (second calibration gives local recovery while two branches continue):
method-supported, model-derived.** The sources support applying smooth
parameter continuation or a contraction estimate to an augmented residual map
whose derivative is invertible at each zero-coupling root. They do not support
the R29 divided residual `W_lambda`, its limit `A_2`, the coefficient and sign
claims in the narrow-pulse expansion, nonzero canonical kernel coordinates,
rank preservation for positive-width pulses, or the claimed two-root
continuation. Joint smoothness in `(lambda,w)` and a uniform self-map margin
must be proved directly for the actual apparatus.

**C115 (positive global canonical risk despite local recovery):
model-derived, conditional on C114.** Once two distinct admissible roots have
one exact complete record and the stated preparation/energy constraints, the
coordinate triangle inequalities and product lower bound are elementary. The
inherited sources provide neither a minimax estimator nor a global ambiguity
theorem, and do not make the bound universal: its positivity and action units
depend on `E`, `c`, preparation margins, coupling range, and fixed pulse
geometry. Local inverse constants may depend on each fixed positive coupling.

## Open proof and source-to-model obligations

The next proof review should (i) verify the three-row pulse rank and the
nonzero `(x,P)` kernel direction for the selected smooth pulses, (ii) prove
joint quotient regularity and invertibility at both zero-coupling roots, and
(iii) check all exact record, energy, clock, and cutoff margins on one fixed
positive-coupling interval. For the next bounded audit, R30 should calibrate
`q_3=0` and compare the resulting four leading rows with true global inverse
control, explicitly testing whether rank against global recovery is sufficient
or whether a third calibration merely removes the current branches.
