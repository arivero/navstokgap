# Action-field selection: the central target

The target is to derive, from explicitly classical physical premises, an
action-valued field that approaches a positive universal constant. The eventual
identification of that constant with $\hbar$ must follow from its role in the
derived dynamics. This is now the central task; spectrum examples and action
defects serve as tests of its premises.

## Variables and proof obligations

Immediate priority after A10/B23: **A11**, an increasing harmonic reservoir.
A10 gives a zero long-window limit for each fixed finite receiver, and identifies
the displacement weight whose uniform bound must fail for a positive joint
limit. Specify the network, energy allocation and tagged spectral measure,
then compare receiver-size and observation limits. G02 supplies the calibrated
access/product benchmark; A07 supplies the controlled-reversal benchmark.
The [cut-point refinement test](CUT_POINT_TARGET.md)
has completed its chosen constructions; it remains the consistency condition
for any candidate field. Bath relaxation supplies a comparison mechanism.

Use $\mathsf h_\varepsilon(t)$ for the candidate field, with physical time $t$
and resolution $\varepsilon$ kept separate. An additional observation duration
$\Delta$ may enter an operational definition. A refinement limit, a long-time
limit and a semiclassical limit are separate operations.

The target has five proof obligations:

1. Define the field from classical states, observables or eliminated degrees of
   freedom, including its action units and normalization.
2. Identify the physical premise that excludes its vanishing limit.
3. Prove convergence to a finite constant in a stated topology.
4. Establish the same limiting constant across masses, preparations and the
   relevant interacting systems.
5. Derive the role that identifies the constant as the quantum action scale.

The assumptions should state physical properties independently of the desired
answer. A fixed-point prescription containing a supplied $\hbar$ is a comparison
model. Each proposed axiom receives an explicit deterministic-countermodel test.

## A08: composition as a universality premise

Completed in [the composition note](../notes/composition-universality.md),
C035–C036 and B16. The shared positive plateau follows conditionally on
coefficient closure and one positive finite-rate reference. Preparation
independence and identification with the quantum phase scale continue in A09.

For independent constituents, transform the covariance to centre and relative
coordinates with total and reduced masses. Test the claim that a nonnegative
coefficient depending only on mass and preserved by this composition is mass
independent. State the admissible mass domain and prove the additive-function
step. Then test preparation parameters, correlated constituents, and closure of
the full velocity law. A composite of independent two-speed particles generally
requires more velocity states. The intended output addresses obligation 4's
mass dependence; preparation independence and positivity have their own gates.
If this coefficient is shared with a stationary two-state constituent of
nonzero fixed speed and finite positive reversal rate, C020 gives modelwise
strict positivity. Test this combined conditional route explicitly, alongside
families of finite-rate models whose shared coefficients approach zero.

## A09/G01: crossover, quantum role and spectral control

**A09a is complete:** [the crossover note](../notes/bridge-crossover.md),
C037–C038 and B17 give the exact conditioned midpoint curve and the necessary
window/mass constraint. Its plateau limit concerns $T\to\infty$ at fixed mass;
uniformity over masses approaching zero fails at a common finite window.
**A09b is complete:** [the checkerboard note](../notes/checkerboard-dynamics.md),
C039–C040 and B18 match the normalized primary recurrence and prove the
strong wavepacket limit. Measuring direction at every cut instead gives a
ballistic fixed-coefficient limit. A09's remaining physical selection task
must specify coherent composition across unobserved cuts and identify its
action parameter with the classical plateau across preparations.

Use C018/C031 to obtain the necessary window $\Delta\ge K/(mu^2)$ for a
positive prescribed coefficient. Distinguish this condition from exact Gaussian
support, and the stationary A01 observable from A06's conditioned midpoint.
Read the B15 checkerboard leads at formula level, then compare real Poisson
recurrences, complex corner amplitudes and their continuum/nonrelativistic
limits. Trace the identification $K=\hbar$ separately from its mass law.

G01 is complete in [the susceptibility/gap note](../notes/susceptibility-gap.md),
C041–C042 and B20. Complete observable coverage plus bounded total response
gives a lower spectral bound, while a single plateau misses hidden slow modes.
G02 tests how mechanical access and composition affect those two premises.
The original G01 construction starts with $-Q$ on finite $L^2(\pi)$, the product bounds of C019 and
the two-state equality. Compare inverse-time relaxation gap, energy units,
Dirac branch separation and vacuum excitation gap explicitly. Test hidden slow
modes before proposing a lower spectral bound from a velocity susceptibility.
These are the next obligations, as assessed in the
[six-direction review](../reviews/six-directions-2026-09-08.md).

## First bounded experiment: A01

Test the operational candidate

$$\mathsf h_\Delta(t)
=\frac{m}{\Delta}\operatorname{Var}[X(t+\Delta)-X(t)],\qquad\Delta>0.$$

The normalization agrees with the Gaussian parameter $\kappa$ when the
increment variance is $\kappa\Delta/m$. This candidate is an ensemble
observable, rather than an independent dynamical field at this stage.

Use a classical two-velocity persistent random flight as the first model:
speeds $\pm u$ with $0<u<c$, a finite reversal rate, and an explicitly stated
initial ensemble. Compute the short- and long-duration limits and identify
which classical input controls any positive plateau. Compare with Nelson's
specified diffusion coefficient and with the fluctuation premise in
Hall–Reginatto. The librarian audit must supply exact prior-art matches and
the next physical test, rather than a detached reading list.

The model tests a stochastic classical axiom set. Its reversal mechanism,
momentum exchange and relationship to smooth Newtonian force laws are explicit
questions for a mechanical realization. M06 remains the complementary
force-control and relativistic-action calculation.

## A01 result and the next bounded test: A02

The [reviewed paper](../papers/classical-action-field.tex) proves
$\mathsf h(\Delta)\uparrow H_*>0$ under finite irreducible reversible velocity
dynamics with nonzero variance. Two velocities give $H_*=mu^2/\lambda$.
Finite speed gives $\mathsf h(\Delta)\to0$ as $\Delta\downarrow0$;
the positive limit concerns long observation duration. [B09](../references/batches/B09.md)
identifies the Green–Kubo and telegraph prior art and the reconstruction premises
in Nelson and Hall–Reginatto.

A02 asks whether mechanical exchange can select the same
$2m\int_0^\infty C_m(s)\,ds$ across masses and preparations.

1. Select one tractable collision or coupled-particle model. Specify the
   momentum receiver, invariant ensemble, energy budget and speed regime.
2. Derive its velocity correlation or a controlled approximation, including
   where a Markov description and detailed balance enter.
3. Compute mass, density, energy and interaction-rate dependence. In the
   two-velocity reduction the diagnostic is $\lambda_m/(m u_m^2)=1/H_*$.
4. Test zero-variance and rapid-decorrelation families, and whether any stated
   conservation/composition principle excludes them. Record a countermodel
   as a completed test when it settles the chosen axiom set.
5. Commission one bounded librarian audit of each resulting mathematical
   claim before ledger acceptance. Use its sources to choose the next premise.

An equilibrium ensemble makes $\mathsf h_\Delta(t)$ independent of $t$;
physical-time attraction of a dynamical field needs an additional construction.
The immediate test targets universality of the plateau, keeping this distinction
visible. M06 retains the finite-speed and force-control companion.

## Current evidence and workflow

M04 proves that Gaussian composition preserves an arbitrary action scale.
M05 proves that uniformly classical paths may retain a selected finite action
defect. Together they isolate scale selection as the next task; see
[the M05 note](../notes/two-regulator-audit.md).

User instruction, 2026-09-07: work autonomously and commit and push to the
existing GitHub remote after each innovation or relevant status change.
Use one small Sol/Luna worker at a time, with explicit supported effort and
coordinator review. Submission elsewhere, correspondence and paid services
remain outside this repository-publishing authorization.
