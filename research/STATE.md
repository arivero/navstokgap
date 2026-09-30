# State

Updated 2026-09-30. Read this page and the
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
The foundational reconstruction from classical limits is judged by its
use for those two goals; explaining the RG transformation itself is a
useful intermediate result (user, 2026-09-30).
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
   Diagonal entries and cube sectors are exact through spin 1 (Theorem 4 there); §14 extends the barriered comparison to unequal layers (refereed by Claude). Cell 2: §§26--30 give finite response trees and barrier-preserving decoupling; §§31--34 give reference and marked attachment norms with retained barriers. [§35](../notes/su2-midplane-small-field.md#35-separately-marked-bad-components-at-arbitrary-order) now proves the all-order connected target (116) in the weak recoupling strip, with explicit rarity and fixed decay (166) (Sol/Astra, refereed). Next gauge lemma: dress the correlated insertion family in this strip, paying good connectors by decay; reject volume cost or assumed physical recoupling. Dressing (112), boundary sources (113), (116) at recoupling one, $SU(3)$ constants and iteration remain open. Current research emphasis is Newton's action necessity and continuum existence.
   The [zero-spacing note](../notes/zero-spacing-any-action.md) extends it
   to any action and dimension: all 2D limits (Lévy exponents), and the
   conditional per-volume error budget, with the strict 4D threshold $c>2/b_0$.
   Atlas cell 4: [composition, §7](../notes/four-dimensional-composition.md) gives explicit vertices, finite one-step subtracted matching bounds and iteration hypotheses (Round 10, formal, unrefereed); next, prove depth-uniform (14) and remainder control. Theorems 1--4 are refereed by Claude.
2. **Newton necessity.** [Routes and conditional theorem](../notes/newton-indeterminacy-routes.md): Gaussian record closure yields the disturbance floor with $h_*=2\zeta$; the radiation unit is explicit.
   [Physical feedback, §§8.11--8.14](../notes/sed-closure-under-recording.md#814-the-limiting-momentum-record-and-retained-controller-recoil) constructs the body--record law and limiting-record closure. §§8.15--8.18 give the nonlinear classical failure, its persistence under weak refinement and the score correction/unread-label excess. [Two-packet test, §8.19](../notes/sed-closure-under-recording.md#819-local-score-data-do-not-close-free-evolution) shows that identical local jets and Fisher data can give different terminal coordinate records; (123) closes this finite reference with a coherence datum (Sol/Astra, refereed). Next Newton lemma: a physical preparation-and-record history rule carrying this datum through separation and reunion and accounting for (117), (119); reject a local-only descriptor, imported quantum dynamics or an unexcluded zero branch. [All zooming schedules, §§3c--3d](../notes/refinement-composition-and-limit.md#3c-all-refinement-sequences-and-two-microscopic-kick-orders) constructs the harmonic curve and separates RG scale from action normalization. Continuity survives zero action; adaptive timing, universality and radiation calibration remain separate.
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
with `make paper NOTE=<slug>`. Keep alternation gauge → Newton; at most
one sequential bounded worker or referee when useful, under the current
user plan. The user requests removal of bulky Lean tools and generated
build files before the machine upgrade; inspect sister-repository sources
without reinstalling tools. Commit and push completed work.
