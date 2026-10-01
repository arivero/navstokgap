# State

Updated 2026-10-01 (evening). Read this page and the
[refinement note](../notes/refinement-composition-and-limit.md);
AGENTS.md governs. The [joint-paper plan](../notes/three-continuum-limits.md)
gives the wider comparison.
The [October 1 Claude handout](handoffs/HANDOFF-2026-10-01-CLAUDE-NEWTON.md)
gives the Newton/quantisation restart; the
[September 23 handout](handoffs/HANDOFF-2026-09-23.md) records earlier
reviews. This page carries the current direction.

## Goal

User direction, 2026-09-26: one eventual paper on what survives
refinement. The two main proof goals are **a positive action scale in
Newton's Galileo comparison, from independently justified physical
premises**, and **the continuum existence and mass gap of pure $SU(3)$
Yang--Mills**. QCD pions at zero and nonzero quark mass provide orientation
and inspiration; constructing fermionic QCD is outside the active queue.
The foundational reconstruction from classical limits is judged by its
use for those two goals; explaining the RG transformation itself is a
useful intermediate result (user, 2026-09-30).
**Thesis (user, 2026-10-01, restated at night).** The quantum theory
reduces to Newton's mechanics only under extra conditions: a record of
the preparation, or an imprecision action exceeding $h$ at one end of
the comparison, or the absence of crossing streams
([reachability note](../notes/zero-branch-reachability.md), Theorems 1,
2(ii), 5 and §§3b--3c). Newton's own construction, determinate bodies
with exact ultimate ratios, is the case these conditions exclude once
streams cross. The goal is to establish this as the consistency problem
of classical mechanics: it is the limit of the world's mechanics only
on a domain whose boundary is set by a constant, $h$, that the theory
does not contain, so it cannot state the conditions of its own
validity. The earlier strong form, that classical mechanics requires
$h>0$ to exist, is closed: a classical limit exists along recorded or
imprecise preparations. Proof obligations: (i) extend the necessity of
the conditions beyond quadratic forces, where it is exact, to the
smooth and Kepler cases now only cited; (ii) show that no condition
statable within classical mechanics replaces them, the coherence of
unrecorded launch points being non-classical (Theorem 5); (iii) carry
the threshold form, imprecision action compared with $h$, as the
surviving positive-scale statement into the paper; (iv) keep the
readout-law and Leibniz-continuity routes for the physical origin of
coherence. Deformation families (Moyal, Fisher, sheet realizations)
are continuous in the constant by construction and are admissible only
as checks, after stating which premise a calculation would establish
or exclude.
The latest direction is to build the limit from local insertion laws:
an intermediate Newtonian time, an edge or cell in gauge theory, and
their lower-dimensional counterparts. The modern leg remains primary; formal and textual
Principia work lives in the sibling `newtonlean` repository.

**Mid-term goal (user, 2026-09-27):** a collective understanding of the
halving of the lattice and what emerges in each case and dimension. The
[atlas of halving](../notes/halving-atlas.md) is the shared map; results
fill its cells (open cells in its §5).

## In hand

- [The Planck paper](../notes/planck-gap-paper.md) is the developed Newton
  component, with sharp conditional mark bounds, the general disturbance
  bound and polygon phase identities. It supplies their proof links.
  Positive quantum action is an input to those quantum results; the
  independent necessity argument remains open. All three September 23
  adversarial review batches are complete.
- [The mass-gap position](../notes/mass-gap-position.md) and
  [conditional theorem](../notes/mass-gap-conditional-theorem.md) hold
  the pure-gauge map: finite-lattice and strong-coupling results,
  with H1/H2 blocking and mixing estimates open. Continuum construction
  and nontriviality (T4) remain explicit obligations.
- [The working note, §5](../notes/three-continuum-limits.md) states the
  elementary spectral criteria for retaining a positive or zero
  threshold, including the need for surviving observable weight.
- [The refinement note](../notes/refinement-composition-and-limit.md)
  constructs the arbitrary-partition constant-force limit, gives exact
  two-dimensional gauge subdivision and a sufficient summable-error
  criterion, and distinguishes these from a surviving physical gap.
- [The corpus audit of 2026-10-01](../notes/corpus-audit-2026-10-01.md) scores every
  note for interest and correctness (Opus, reviewed by Fable): the spine
  holds; 24 notes, mostly closed mass-gap routes, still state withdrawn
  or inconsistent claims and await dated correction boxes.

## Next

1. **A local gauge refinement estimate.** The
   [series/parallel note](../notes/series-parallel-gauge-refinement.md)
   factors one directional halving exactly: series moves close in every
   dimension, and the parallel insertion $\Psi$ (Prop. 1) carries the
   renormalization in $\binom{D-1}{2}$ transverse planes. The free-field
   defect is exact (Prop. 2); for unperturbed $U(1)$ one step is proved (Thm 5:
   free-field step up to density $e^{-\pi^2/(8\lambda_3a)}$). $SU(2)$
   midpoint: exact structure and leading curvature term (Prop. 6); the
   finite-cube bound assumes full normalized Laplace estimates (Prop. 7).
   Measure level for $U(1)$: [monopole note](../notes/villain-monopole-refinement.md),
   TV distance $\le2(L/a)^3e^{-\pi^2/(6\lambda_3a)}$ in $D=3$; the route fails in
   $D=4$ (loop density per cell fixed by $g$). The $SU(2)$ midpoint character
   is exact for every spin ([closed form](../notes/su2-midpoint-exact.md)).
   [All-group cut identities and centre torsion](../notes/sun-midpoint-centre.md)
   are refereed (Round 5B A); its §5b displays the fundamental SU(3)
   trisection (5B B, written). Image-to-volume control remains open.
   Diagonal entries and cube sectors are exact through spin 1 (Theorem 4 there); §14 extends the barriered comparison to unequal layers (refereed by Claude). Cell 2: §§26--34 give response trees, decoupling and marked attachment norms. §35 gives (116) at all orders in the weak strip. [§36](../notes/su2-midplane-small-field.md#36-exact-dressed-activities-in-the-weak-recoupling-strip) gives exact dressed activities satisfying (112). [§37](../notes/su2-midplane-small-field.md#37-moving-means-with-a-fixed-barrier-an-exact-quadratic-source-test) gives a fixed moving-mean source radius and the subtracted barrier norm (177) in a centered quadratic model (Sol/Astra, refereed). Next gauge lemma: complex centered nonlinear bounds and the moving saddle's decaying source dependence; reject barrier differentiation, amplification on every good connector or assumed contact cancellation. Full (113), physical recoupling, group-integral comparison, $SU(3)$ constants and iteration remain open. Current research emphasis is Newton's action necessity and continuum existence.
   The [zero-spacing note](../notes/zero-spacing-any-action.md) extends it
   to any action and dimension: all 2D limits (Lévy exponents), and the
   conditional per-volume error budget, with the strict 4D threshold $c>2/b_0$.
   Atlas cell 4: [composition, §7](../notes/four-dimensional-composition.md) gives explicit vertices, finite one-step subtracted matching bounds and iteration hypotheses (Round 10, formal, unrefereed); next, prove depth-uniform (14) and remainder control. Theorems 1--4 are refereed by Claude.
2. **Newton gap and necessity.** [Which limits reach zero](../notes/zero-branch-reachability.md) (Fable, 2026-10-01; refereed by GPT-6.1 Sol via Codex, corrections applied): Galileo's comparison with Gaussian preparations and marks reaches the zero branch (Thm 1); for determinate preparations the complete record has an $h\to0$ limit only where signed cross amplitudes cancel, while smeared records converge to the classical branch sum (Thm 2), exactly for inertia with graded velocity inside its fold interval (Thm 3) and for a Kepler swarm whose windings overlap, where Hooke's anomaly record stays rigid (Thm 4). The invariant discontinuous at zero is the leading fringe visibility of crossing streams, a contrast, not a spectral gap, full when the record and preparation imprecision actions are small compared with $h$ (§§3b--3c); the thesis is the order of limits with the record limit first, and the second premise is an $h$-independent coherence length between the launch points of crossing streams (partial contrast $e^{-\Delta q_0^2/(8\sigma^2)}$, the same for every $h>0$), which remains a premise. Thm 5 (exact for quadratic forces): the same swarm attached as an incoherent mixture of coherent states with widths vanishing with $h$ has a complete record converging to Newton's branch-weighted density at every fixed time, so the gap requires the coherence premise (refereed ACCEPT by GPT-6.1 Sol via Codex, third pass, reports in `reviews/`). No universal late-time persistence and no positive Newtonian action scale are proved; a single body's packet has action spread of order $h$ and reaches the zero branch at any fixed time, so the thesis concerns swarms of $h$-independent extent. Next: defend the complete-records premise and move the paper's gap argument from the Gaussian parabola, which is immune, to the Kepler swarm.

GOAL MET: coherence-necessity theorem refereed ACCEPT

   (Session goal of 2026-10-01: Theorem 5 of the reachability note, refereed ACCEPT on its third pass, committed and pushed with both catalogs.) [Routes and conditional theorem](../notes/newton-indeterminacy-routes.md): Gaussian record closure yields the disturbance floor with $h_*=2\zeta$; the radiation unit is explicit.
   [Recording notebook](../notes/sed-closure-under-recording.md): Gaussian body--record limits and nonlinear/coherence countertests; §§8.22--8.23 realize score correction and Gaussian switching transport, with full-pointer and preparation-dependent-force obstructions. [Score-constrained ensembles](../notes/score-constrained-ensemble.md) gives the restricted action and reservoir-aware population momentum, a fixed-shape obstruction, and an exact positive non-Gaussian forward completion. Nonlinear recording generates a quartic tail outside its finite modes, with unread recoil energy retained (Sol/Astra, written, internally checked). Its §§6--8 (Fable; refereed by GPT-6.1 Sol via Codex, corrections applied): the two-sheet realization exists on every positive solution and for all forward time on that orbit, with exact mean cancellation of force and switch power (Props. 7--8); its controller is the field pair within this architecture and, after records, the record-dependent data of its family (Prop. 9, Cor. 10); branch controllers pass the two-unread-width test while the marginal-score replacement is refuted by the variance witness $\kappa^2\Delta t^2/m^2$ (Prop. 11); closure under coordinate copies holds at every $\kappa\ge0$ under a branch-dependent protocol (Prop. 12). Decision: composition closure selects no $\kappa$, so the apparatus-closure route to positivity is closed; $\kappa=0$ admits a preparation-independent body law and $\kappa>0$ none for all Gaussian preparations. Next Newton lemma: the premise that fails at $\kappa=0$, dependence of individual motion on the preparation's statistical state, through the terminal readout bound or the record reading of Leibniz continuity; reject further realizations of the field law offered as closure. Terminal access, phase reunion, positivity, universality and radiation calibration remain separate. [All zooming schedules, §§3c--3d](../notes/refinement-composition-and-limit.md#3c-all-refinement-sequences-and-two-microscopic-kick-orders) constructs the harmonic curve; refinement and complete-record continuity still admit zero action.
   [Shared-bath recording test](../notes/sed-closure-under-recording.md): sharp two-pointer posteriors survive at fixed cutoff; the premise that restores closure is a bound on every terminal readout, which at $\kappa=\hbar/2$ is Gaussian quantum measurement theory (refereed).
   Thermodynamic records give only $\eta\ge A_0e^{-W/k_BT}$
   ([no floor](../notes/thermodynamic-records-no-floor.md)). The statement to
   change is joint determinacy ([fifth postulate](../notes/principia-fifth-postulate.md)):
   Within SED, conditionally on its disputed Planck derivation and for
   resonant variables, $2\zeta=h_P/2\pi\approx0.297\,h_{\rm rad}$
   ([SED link](../notes/sed-zeta-radiation-link.md)); its scale identification retains those conditions.
   Newton's *velocitas ultima*; Laws independent of it, one action constant
   under covariance (Gutt), floor for $\hbar\ne0$; reviewed: the analogy is
   partial, since a commutative state restriction also floors.
   [Rivero 1998 test](../notes/rivero-1998-conjecture-central-forces.md): quartic interference, convergent fixed-$h$ refinement and angular/EBK consistency leave scale selection open.
   [Rotation composition](../notes/rotation-composition-universality.md): mechanical generator closure forces one constant per connected class; the common zero branch remains admissible.
   [Galileo two-path interference](../notes/galileo-two-path-interference.md): exact cubic-action error law; contrasting limits require averaging or calibrated control, with positive scale still supplied.
   [Cut measure](../notes/cut-measure-newton.md) (refereed): any cut sequence spends $K_\tau$ additively (Cameron--Martin energy of Schauder hats; the rod of *Zhuangzi* 33 spends $\frac67$); a floor bounds the number of exhibited cuts and supplies none.
   [Stochastic route](../notes/stochastic-route-velocitas-ultima.md) and
   cut-measure Prop. 6 are refereed (Round 5B A): continuous independent
   increments, mass composition and additive-noise testing give the
   conditional Planck mesh. Positivity and the physical noise law remain
   premises; Nelson supplies a separate mean-dynamics framework.
   [Leibniz continuity](../notes/leibniz-continuity-records.md) (refereed by Fable): the best verdict of Newton's comparison, $\Phi(-\frac12\sqrt{K_\tau/\kappa})$, is continuous in $F$ at zero iff $\kappa>0$, so Leibniz's 1687 law of continuity read on records selects the floor for motions; the geometric reading keeps the zero branch.
3. **Spectral bridge:** the H3 small-volume $SU(3)$ estimate in the
   [Feshbach note](../notes/weak-coupling-feshbach-reduction.md) remains
   the valley-lifting task to connect to the refinement construction.
   Use the pion benchmark where it tests the symmetry of a proposed
   mechanism; carry successful bounds toward reconstruction and the
   joint paper.

Attainment of the existing disturbance bounds and the Planck paper's
§11 historical/submission obligations remain open. Other mass-gap
[openings](../notes/mass-gap-openings.md) remain available; the proposed
curvature threshold conversion is still unverified.

## Constraints

No numerical or symbolic verification scripts. Build only changed notes
with `make paper NOTE=<slug>`. Concentrate mostly on Newton (user,
October 1); retain the gauge frontier for later bounded units. At most
one sequential bounded worker or referee when useful, under the current
user plan. The user requests removal of bulky Lean tools and generated
build files before the machine upgrade; inspect sister-repository sources
without reinstalling tools. Commit and push completed work.
