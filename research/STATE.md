# State

Updated 2026-09-29. Read this page and the
[refinement note](../notes/refinement-composition-and-limit.md);
AGENTS.md governs. The [joint-paper plan](../notes/three-continuum-limits.md)
gives the wider comparison.
The [September 23 handout](handoffs/HANDOFF-2026-09-23.md) records the
earlier results and reviews; this page carries the current direction.

## Goal

User direction, 2026-09-26: one eventual paper on what survives
refinement. The two main proof goals are **a positive action scale in
Newton's Galileo comparison, from independently justified physical
premises**, and **the continuum existence and mass gap of pure $SU(3)$
Yang--Mills**. QCD pions at zero and nonzero quark mass provide orientation
and inspiration; constructing fermionic QCD is outside the active queue.
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
   Diagonal entries and cube sectors are exact through spin 1 (Theorem 4 there); §14 extends the barriered comparison to unequal layers (refereed by Claude). [Round 18 §18](../notes/su2-midplane-small-field.md#18-round-18-the-barrier-insertion-and-the-change-of-measure) tests the two routes from §17 (unrefereed). Cell 2 next: control the local barrier-weighted resolvent moment (72) and the moving-diffusion terms (73)--(75), uniformly in plane size and barrier approximation, to obtain the weighted $C\varepsilon^3/t$ kernel estimate; then full-integral comparison and perturbed-action stability. Fixed-frame equivalence and iteration remain open; higher-spin sum control remains an alternative route.
   The [zero-spacing note](../notes/zero-spacing-any-action.md) extends it
   to any action and dimension: all 2D limits (Lévy exponents), and the
   conditional per-volume error budget, with the strict 4D threshold $c>2/b_0$.
   Atlas cell 4: [composition, §7](../notes/four-dimensional-composition.md) gives explicit vertices, finite one-step subtracted matching bounds and iteration hypotheses (Round 10, formal, unrefereed); next, prove depth-uniform (14) and remainder control. Theorems 1--4 are refereed by Claude.
2. **Newton necessity.** [Routes and conditional theorem](../notes/newton-indeterminacy-routes.md): Gaussian record closure yields the disturbance floor with $h_*=2\zeta$; the radiation unit is explicit.
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

No numerical or symbolic verification scripts. Build only the changed
note with `make paper NOTE=<slug>`. The user authorizes bounded Sol 6 or
Luna 6 workers for menial tasks with short returns; use them sparingly
and sequentially, never Astra subagents. Commit and push completed work.
