# Action-field selection: the central target

The target is to derive, from explicitly classical physical premises, an
action-valued field that approaches a positive universal constant. The eventual
identification of that constant with $\hbar$ must follow from its role in the
derived dynamics. This is now the central task; spectrum examples and action
defects serve as tests of its premises.

**R05/B35 completed:** [the classical readout test](../notes/classical-readout-refinement.md)
adds physical probe back-reaction to R04's receiver-memory reconstruction.
Quiet scalable preparations close the instrument's action products while
preserving asymptotically accurate recovery. **R06/B37 completed:**
[finite-duration autonomous readout](../notes/autonomous-finite-readout.md)
retains fixed finite mass and pulse widths, with delayed exact records and
shrinking preparation widths; C068–C069 close its accuracy–disturbance product.
**R07/B38 completed:** bounded unresolved force gives a delayed prediction
region. **R08/B39 completed:** exact cut composition and observed-position
fibres quantify its information dependence; area can close without momentum
recovery. **R09/B40 complete:** finite-precision records yield an exact area
and uniform joint precision/delay closure. **R10/B41 complete:** two records
give full-state reconstruction with an explicitly vanishing action-error product.
**R11/B42 complete:** exact minimax risks survive dense noisy records at fixed
tolerance. **R12 is next:** the composition law of these worst-case scales,
compared with A08's variance universality. See
[R11](../notes/indistinguishable-phase-bound.md) and
[I006](../ideas/I006-discovery-by-connecting-results.md). C066–C067 concern
ideal impulses and growing probe supply. A19 remains the supporting test.

## Variables and proof obligations

Supporting priority after A18/B32: **A19**, test peak excitation rather than
a pointwise speed floor, retaining the force ceiling. A18 gives a sharp
canonical action bound for closed regular trajectories; turning-point stops
motivate the weaker premise. See [A18](../notes/closed-orbit-force-action.md).

Earlier priority after A17/B31: **A18**, extend the positive circular-action
bound from force ceiling plus speed floor to closed regular trajectories.
A17's fixed-potential small-circle family isolates lower excitation as a
separate physical premise. See [A17](../notes/fixed-force-small-circles.md).

Earlier priority after A15/B29: **A16**, test dilation closure for the
canonical covariance estimator and its orbit/preparation class. A15 gives a
constant-in-time bound-orbit estimator whose value remains prepared. See
[the A15 note](../notes/bound-orbit-action-observable.md).

Earlier transport priority after A13/B26: **A14**, independent stationary renewal
streams with fixed mean gap and variable gap variance. A13's ordered streams
close the response at A12's mechanical scales and mean rate. Derive the Palm
residual law and determine which quantitative fluctuation premise survives
near-ordered preparations.

The preceding priority after A12/B25 was **A13**, change spacing correlations at fixed
mass, speed and density. A12 derives $\lambda=\rho u$ and plateau $mu/\rho$
from independent Poisson gaps; A13 tests that preparation premise.

The preceding priority after A11/B24 was **A12**, choose a bounded-velocity receiver
and its invariant preparation. A11 derives a positive periodic-chain limit
from extensive mode energy, but its common hard-speed condition closes the
response uniformly in the window. The next model must address that preparation
constraint together with the low-frequency weights. G02 supplies the calibrated
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
