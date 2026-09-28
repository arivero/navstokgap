# State

Updated 2026-09-28. Read this page and the
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
- [The mass-gap position](../notes/mass-gap-position.md) and the
  sharpened [conditional assembly theorem](../notes/mass-gap-conditional-theorem.md)
  hold the pure-gauge map.  Its proved implication now separates
  scale-by-scale blocking transport (H1$_{\rm gap}$), uniform renormalized
  observable normalization (H1$_{\rm OS}$), one-box mixing (H2), and OS
  convergence/nontriviality (H3): together they imply a volume- and
  cutoff-independent lower bound.  All four remain open in the required
  weak/intermediate $SU(3)$ regime.  The same note gives the alternative
  persistent-soft-observable-weight condition for a zero threshold.
- [The working note, §5](../notes/three-continuum-limits.md) states the
  elementary spectral criteria for retaining a positive or zero
  threshold, including the need for surviving observable weight.
- [The completed $0+1$ proof](../notes/low-dimensional-mass-gap.md) now
  covers compact semisimple matrix mechanics, including $SU(3)$, and its
  $3+1$ constant-mode truncation has a gap proportional to
  $g^{2/3}\hbar c/L$.  The [torus-valley calculation](../notes/torus-valley-potential.md)
  now derives the matching $SU(3)$ Cartan root-sum one-loop potential and
  its $O(g^{4/3}\hbar c/L)$ nonzero-mode correction.  This is a small-box
  input only; its fibrewise Schur estimate and its transport through
  blocking remain open.  The $L^{-1}$ scaling marks the exact boundary
  before the full volume-uniform continuum problem.
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
   Diagonal entries and cube sectors are exact through spin 1 (Theorem 4 there); atlas cell 2 now has a [formal full-plane order-$t$ calculation](../notes/su2-midplane-order-t.md). Next: its normalized estimate (18) with winding control, then iteration; higher-spin sum control remains an alternative route.
   The [zero-spacing note](../notes/zero-spacing-any-action.md) extends it
   to any action and dimension: all 2D limits (Lévy exponents), and the
   conditional per-volume error budget, with the strict 4D threshold $c>2/b_0$.
   Atlas cell 4: [round 6 composition](../notes/four-dimensional-composition.md) gives the exact Gaussian kernel and sharp-blocking growth (unrefereed); next, bound its (14), the subtracted generated-vertex contractions, for finite endpoint matching and the conditional average rate.
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
3. **Spectral bridge:** the fibrewise relative-Schur estimate needed by
   the small-volume programme remains the valley-lifting task to connect
   to refinement.  The new [SU(3) Cartan root sum](../notes/torus-valley-potential.md)
   fixes the one-loop local coefficient but is not that estimate.  Its
   output must feed H1$_{\rm gap}$ and H1$_{\rm OS}$ of the
   [assembly theorem](../notes/mass-gap-conditional-theorem.md), then H2
   and OS reconstruction.  The [action-calibration bridge](../notes/uv-halving-ir-confinement.md)
   records exactly where $h_*=h_P/(2\pi)=\hbar_{\rm YM}$ is an added
   physical input rather than a mass-gap inference.  Use the pion
   benchmark where it tests the symmetry of a proposed mechanism; carry
   successful bounds toward reconstruction and the joint paper.

Attainment of the existing disturbance bounds and the Planck paper's
§11 historical/submission obligations remain open. Other mass-gap
[openings](../notes/mass-gap-openings.md) remain available; the proposed
curvature threshold conversion is still unverified.

## Constraints

No numerical or symbolic verification scripts. Build only the changed
note with `make paper NOTE=<slug>`. The user authorizes bounded Sol 6 or
Luna 6 workers for menial tasks with short returns; use them sparingly
and sequentially, never Astra subagents. Commit and push completed work.
