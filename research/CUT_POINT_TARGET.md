# Cut-point refinement: the central selection test

The immediate question is which independently stated physical condition forces
an action-valued remainder to survive as the cut points become dense. The user
reaffirmed this focus on 2026-09-07. Collision-bath relaxation is a diagnostic
for this problem, rather than a replacement for it.

Use partitions $\pi_N=\{0=t_0^{(N)}<\cdots<t_N^{(N)}=T\}$ with mesh
$|\pi_N|\to0$ in a fixed mechanical experiment. Keep physical time, cut index
and fluctuation parameter separate. State whether cuts sample one trajectory,
define impulsive approximations, or introduce new random degrees of freedom.

**R03/B33 completed:** [the cut-state test](../notes/classical-cut-state.md)
separates exact phase-state composition from independent position-conditioned
resets, whose terminal refinement limit freezes motion. **R04/B34 completed:**
[the three-body test](../notes/three-body-cut-memory.md) retains tagged momentum
and derives the receiver memory and two-time recovery map. **R05/B35** closes
the quiet-preparation test with scalable impulsive probes. **R06/B37** supplies
[four finite-duration autonomous records](../notes/autonomous-finite-readout.md)
at fixed mass and observation latency, with exact record access and increasingly
concentrated preparation. Refining reported samples needs no extra probes.
**R07 is next:** require causal new information and a justified precision
restriction, then test for a resource or action lower bound. A19 supports it.

## A03: completed calculation

**Renewed priority, 2026-09-09:** [I005](../ideas/I005-classical-cuts-and-relations.md)
and R03 ask what relational data must survive a cut. Compare composing full
dynamics before eliminating interface variables with composing the reduced
segments. Fix the experiment and preparation; identify ordinary classical
memory before proposing an unavoidable action-valued remainder.

[The reviewed note](../notes/cut-point-consistency.md) and B12 complete the
five tests below. Chord errors vanish on arbitrary shrinking meshes. Exact
Gaussian restriction consistency fixes $\kappa$, whereas the finite-defect
scaling changes the retained-node distribution. At fixed $\kappa$, each inserted
node contributes mean kinetic action $\kappa/2$, and $2D_\pi/(N-1)$ estimates
that parameter in mean square. C027–C029 record the precise hypotheses.

After the 2026-09-08 review, A03/A05/A06 are closed as the chosen structural
tests. The main next task is A08 composition in
[ACTION_FIELD_TARGET.md](ACTION_FIELD_TARGET.md). Preserve the separate
Gaussian node estimator, finite-window variance coefficient and long-window
plateau; transferring the C028 estimator to bounded-speed fixed-duration paths
does not preserve its positive limit. A07 remains a supporting force test.

1. Derive the constant-force chord action error for arbitrary nonuniform
   partitions; identify the mesh and force controls responsible for its limit.
2. Compare geometric approximation with the fluctuating-node families of
   [M05](../papers/regulator-limits.tex). The latter retain action defect
   $\ell/2$ when $(N-1)\kappa_N\to\ell$, while paths converge uniformly.
3. Test refinement consistency: inserting cuts into the same experiment must
   preserve its coarse observables. Determine whether a positive-defect
   sequence satisfies this or changes the experiment at each refinement.
4. Define any local action field, its endpoint convention and its observation
   window. Test additivity and units before identifying a surviving value with
   a universal action constant.
5. Test deterministic and reduced-noise families against the proposed physical
   condition; then commission a bounded prior-art and assumption audit.

The [constant-force note](../notes/principia-constant-force-action.md), §4,
supplies the equal-partition vanishing-error baseline. A01 separates duration
from refinement. A02 supplies a physical-time relaxation mechanism whose
plateau comes from bath energy and a clock. M06 retains the force-control test;
a spatial collision clock is a secondary A04 diagnostic.

## A05: completed physical-cut test

[The physical-cut note](../notes/physical-cut-speed.md) implements equal-mass
elastic reversal with a momentum receiver. It proves the sharp midpoint bound
$\kappa_{\rm mid}\le m\Delta(u-|v|)^2$ and that ballistic position-only
convolution laws are deterministic. C030–C032 and B13 close this chosen test.

Specify whether a cut is a coordinate observation or an executed interaction.
For one concrete interaction, derive its conditional node law and momentum/
energy bookkeeping. Compare its coarse marginals across successive insertions,
and test a hard speed ceiling. The fixed Gaussian law is a reference model;
its parameter is supplied and its support has no strict speed ceiling. The
research obligation is a classical mechanism selecting a positive consistent
fluctuation law, followed by universality of its action parameter.

## A06: completed velocity-resolved return bridge

[The return-bridge note](../notes/telegraph-return-bridge.md) and B14 close
this test with an explicit count/simplex path law, midpoint atom, right-continuous
velocity convention and exact cut restriction. The polygon action error vanishes
at rate bounded by switch count times mesh; its mean has an explicit Bessel bound.
The endpoint-window protocol at a forced jump is distinct from exact conditioning.

Construct the telegraph bridge on $(X,V)$ at fixed $u<c$ and reversal rate.
Start with fixed initial velocity and an attainable terminal position/velocity.
Separate atomic endpoints from the interior density before conditioning.
Derive the midpoint law, sum over the midpoint velocity, and verify that
inserting another cut preserves the old joint marginals. Compare with an
independent midpoint-reset rule. Track the initial/bath premises setting the
reversal rate and scale, and distinguish the microscopic coefficient from
A01's long-duration plateau. These steps are complete in C033–C034.

## A07: finite-duration turns under force control

On the line take $X\in W^{2,\infty}([0,T])$ with $X(0)=X(T)=0$,
$\dot X(0)=u$, $\dot X(T)=-u$, $0<u<c$, $|\dot X|\le u$ and
$|\ddot X|\le a$, where $a>0$ is a specified classical acceleration ceiling.
Completed in [the bounded-turn note](../notes/bounded-acceleration-return.md),
C043–C044 and B21: $T_{\min}=2u/a$, $S_{K,\min}=mu^3/(3a)$ and
uniform sharp polygon error $ma^2T|\pi|^2/24$. The original task was to
find the sharp feasible duration and the infimum of
$(m/2)\int_0^T\dot X^2dt$, with an attaining path when feasible.
Then study sampled-polygon action convergence and vary $u,a,m$ within the
physical premises. Distinguish an endpoint-conditioned bound from a universal
action scale. Repeat the scaling interpretation when the fixed input is force
$F_{\max}=ma$ rather than acceleration. This joins M06's force-control question
to the central cut-point test. Commission one bounded librarian audit covering
the optimal-control inequality and its mechanics interpretation before acceptance.

## The supplied polygon proposal

The user supplied a Claude-attributed proposal on 2026-09-07. Its operational
area threshold is a comparison axiom, distinct from the main goal of deriving
positive action under independently classical premises. Audit its passage from
minimum cell size to an exact action lattice before reusing its quantization
claims. Preserve the useful distinction between polygon error and swept area.

## Newton: passage and conjecture

Lemma I, Lemmas X–XI and the closing Scholium provide arguments about limiting
ratios; Proposition I supplies the central-force polygon. The
[source-grounded note](../notes/principia-constant-force-action.md) separates
these passages from modern action calculations. Newton's possible suspicion
of a surviving action scale remains a historical hypothesis for H02/H03's
dated manuscript and Classical Scholia evidence.
