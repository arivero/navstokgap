# State

Updated 2026-09-27. Read this page and the
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
   Next: those estimates for $SU(2)$, then a mid-plane, then iteration.
   The [zero-spacing note](../notes/zero-spacing-any-action.md) extends it
   to any action and dimension: all 2D limits (Lévy exponents), and the
   conditional per-volume error budget, with the strict 4D threshold $c>2/b_0$.
2. **Newton necessity.** [Routes and conditional theorem](../notes/newton-indeterminacy-routes.md): Gaussian record closure yields the disturbance floor with $h_*=2\zeta$; the radiation unit is explicit.
   Next: physically justify closure under recording and $2\zeta=\gamma h_{\rm rad}$; hidden-background and deterministic-inflexion premises leave both open.
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
