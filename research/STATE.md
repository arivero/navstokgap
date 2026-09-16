# Restart state

Updated: 2026-09-16. **User direction: Galileo's inertial horizontal line
versus the falling parabola, and a mathematical necessity argument excluding
zero-action refinement. Quantum nature is the fact to explain, not an axiom
that supplies the desired answer.**

## Current ordered work

This is the single priority list for autonomous sessions. Apply
[STRATEGY](STRATEGY.md), inspect the selected TASKS entry and relevant source
capsule, and carry one bounded decision to completion. Explicit user directions
select their own task.

1. **Newton/Galileo area and minimum action — selected.** The anchor is the
   area between the inertial horizontal line and the falling parabola. With
   force F and horizontal speed v, its exact conversion is
   (3F/v) A = Delta t Delta E, where Delta E is gained vertical kinetic energy.
   The matched-endpoint chord lens is half that area and is a secondary
   comparison. **Kepler swept sectors/equal-area law are not this target.**
   **Target:** derive a mathematical consistency obstruction to zero-action
   refinement from explicit independently justified premises. Quantum nature
   motivates the problem; inserting hbar, uncertainty relations or a finite
   measurement budget does not solve it. Ordinary classical calculus admits
   vanishing defects, so name the added consistency requirement and show where
   that classical construction fails. The desired conclusion is necessity of
   a positive action scale, followed by universality and quantum identification.
   **N01 supporting result:** [the corrected derivation](../notes/newton-insertion-action.md)
   fixes the area/action factors and gives a closed controlled-force quantum
   comparison. Its supplied-hbar resolution bound is a benchmark, not the
   sought innovation. No mathematical necessity theorem was obtained.
   **Next ([N02](TASKS.md)):** construct and test one proposed non-quantum
   consistency principle for the joint time/position refinement of the Galileo
   comparison. State the cut state, composition and limits, then derive a
   contradiction at zero action or an explicit countermodel satisfying the
   proposed principle. C027--C029 and the deterministic full-state cut model
   are mandatory existing countertests; merely restating them is insufficient.
   The bounded deliverable is a tested new principle and exact obstruction or
   failure, not another audit queue or a measurement-resolution calculation.
   Reuse [I003's originating question](../ideas/I003-cut-paradox-arrow-obstruction.md)
   with its retained corrections. Swept-sector, orbital turning-event,
   quantum-readout and unrelated mechanism variants are supporting/parked
   unless they discharge a named dependency of this necessity argument.
2. **Publication author completion — waiting for author input.** P07's
   [decision sheet](../reviews/publication-readiness-P07.md) recommends the
   elastic-gas draft first and the spin draft second. Author details,
   destination/article type and submission direction remain. Further autonomous
   polishing is parked absent a concrete reader or venue requirement.
3. **Gap track — supporting.**
   [G05](../notes/finite-depth-spin-gap.md) constructs the standard cluster
   Hamiltonian with exact energy gap J uniform in chain length.
   [G07](../notes/low-dimensional-mass-gap.md) (user direction, 2026-09-16)
   makes the h > 0 / mass-gap analogy exact: both floors are unit multiples
   of the fixed constants (Theorem 1), both classical theories have an empty
   span and a similarity realizing zero, and every solved low-dimensional gap
   is either a supplied scale (box, lattice, mass term, 2D string tension,
   C124/C126's K, G05's J) or a generated one (Yang--Mills quantum
   mechanics, gap $\delta_1\hbar^{4/3}g^{2/3}m^{-2/3}$, vanishing when
   either commutator is removed; transmutation). Gate for further gap work:
   name whether a proposed gap is supplied or generated. G06 would be
   supplied; it returns for a named dependency of item 1 or explicit user
   selection. The analogy governs the structure-to-scale stage of item 1;
   its one consistency-forced scale (self-adjoint extension, regularization)
   is the mechanism N02 should look for, tested against C027 and C028--C029.
   [G08](../notes/action-floor-yang-mills-gap.md) closes the loop inside
   that model: a floor on transverse phase-space area produces the gap, the
   commutative model is inert under the floor, and a gap returns an action
   unit whenever the classical coupling is dimensionful (mechanics, $d=2,3$),
   failing at $d=4$. The phase-space form of the floor, a lower bound on the
   area of a closed transverse orbit, is the statement N02 should aim at.

See the [generator-audit handoff](handoffs/Q01-generator-audit.md) and
[finite-closure handoff](handoffs/Q01-finite-closure.md). C128
finishes the named repair decision: all-preparation exact closure needs
infinite observable dimension or changed model premises. This establishes
neither quantum structure nor distinguishability capacity. Both main tracks
still expose a physical dynamics premise; Q01's full reconstruction proof
and K01 remain supporting for a named acceptance/context question.

## Consolidated findings and parked work

- **Q01 theorem-proof sequence parked by user correction.** C129/B77 remains
  accepted. Equations (15)–(17) and the rest of the borrowed theorem are not
  scheduled. Return only for a concrete suspected error affecting a result in
  use, or explicit user direction; unaudited status alone is insufficient.

- C002/C056–C058: continuous variation, admissible contractions and fixed-potential
  small circles close candidate classical action scales in their stated classes.
- C035–C036/C060–C061: composition and orbit bounds are positive under explicit
  reference-preparation or excitation premises. Their physical origin remains open.
- R05–R33: preparation and record access control classical reconstruction.
  C116–C119 supply recovery/tolerance laws; C120–C123 expose direction-dependent
  risks. [R33](handoffs/R33.md) is **parked**, with accepted stages intact and
  curvature nonvanishing open. Return only for a named Q01/K01/G03 dependency,
  a substantive correction, or explicit user direction.
- C039–C040: the checkerboard limit supplies quantum consequences under chosen
  amplitudes, measurement rule and K>0. Necessity remains Q01's question.
- C041–C046 and C124: observable coverage, independent composition and an
  explicit interacting chain give relaxation-gap control. C126 constructs the local Hermitian parent;
  its energy normalization retains a supplied action constant. G03 is complete:
  bounded coupling and a clock floor yield a uniform finite-volume bound.
  General-graph variants are parked for a named operator/limit dependency;
  independent physical identification and continuum transfer remain open.
- A19, A14, R02, M03 and historical H11 remain supporting work. Select them
  when they decide a named main-track premise or the user requests them.

The [ledger](../claims/LEDGER.md) owns acceptance and literature status. P04
promoted no new claim; G03 adds C124 with written proof review and bounded B68
literature coverage, including the unresolved source-image boundary. C126
adds the reviewed finite-volume transfer and B71 parent-mapping audit. The [dated state history](STATE-history-2026-09-12.md)
and task handoffs preserve the earlier milestones; their old next-task text
is historical. [B73](handoffs/B73.md) adds the exact Lubetzky–Sly literature
match for C124, three archived publication routes and a supporting foundational
assessment.
C128 has a written orbit/atomic-separation proof and bounded B74 Koopman
framework audit. User-supplied bibliography and source originals remain intact.

## Constraints and validation

Preserve worktree changes. No numerical or symbolic verification scripts in
Python or a substitute language. Written proof and source review are the
mathematical checks; document/source tooling is allowed. Delegation follows
[the protocol](../agents/PROTOCOL.md): at most one Sol/Luna worker, sequential,
explicit supported effort, never ultra. Relevant checkpoints are committed
and pushed under the standing authorization.

Run `make check`, `make papers` and `git diff --check` after manuscript
integration. Review changed PDF pages and restore unrelated rebuilds only
after extracted-text equality. Record results in the handoff.
