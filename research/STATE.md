# State

Updated 2026-09-26. Read this page and the
[working note](../notes/three-continuum-limits.md); AGENTS.md governs.
The [September 23 handout](handoffs/HANDOFF-2026-09-23.md) records the
earlier results and reviews; this page carries the current direction.

## Goal

User direction, 2026-09-26: one eventual paper on what survives
refinement. The two main proof goals are **a positive action scale in
Newton's Galileo comparison, from independently justified physical
premises**, and **the continuum existence and mass gap of pure $SU(3)$
Yang--Mills**. QCD pions at zero and nonzero quark mass provide orientation
and inspiration; constructing fermionic QCD is outside the active queue.
The working note gives the limit orders, quantities, mechanisms and
paper architecture. The modern leg remains primary; formal and textual
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

## Next

1. **Constructive bridge:** the H3 small-volume $SU(3)$ estimate in the
   [Feshbach note](../notes/weak-coupling-feshbach-reduction.md), using
   transverse valley lifting with explicit constants and cutoff
   dependence. Stop at one estimate or its precise uncontrolled term.
2. **Newton necessity:** one explicit physical model of marks and
   composition that can justify a positive cost under refinement.
   The [working note, §7](../notes/three-continuum-limits.md) distinguishes
   this from assuming M3 or the canonical commutator, and states the
   separate universality and calibration obligations.
3. Use the pion benchmark only where it tests a proposed mechanism;
   carry successful estimates toward cutoff uniformity, reconstruction
   and the joint paper following the working note's plan.

Attainment of the existing disturbance bounds and the Planck paper's
§11 historical/submission obligations remain open. Other mass-gap
[openings](../notes/mass-gap-openings.md) remain available; the proposed
curvature threshold conversion is still unverified.

## Constraints

No numerical or symbolic verification scripts. Build only the changed
note with `make paper NOTE=<slug>`. The user authorizes bounded Sol 6 or
Luna 6 workers for menial tasks with short returns; use them sparingly
and sequentially, never Astra subagents. Commit and push completed work.
