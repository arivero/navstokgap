# Restart state

Updated: 2026-09-13. **G03 interacting-gap milestone complete (C124/B68).**
The [synthesis](../notes/action-scale-obstructions.md) consolidates the classical
obstructions; [Q01](../notes/quantum-exclusion-premises.md) identifies the
operational exclusion premises and remaining mechanical action step. The
[Ising proof](../notes/interacting-ising-gap.md) supplies an interacting gap
uniform in finite volume at bounded coupling and fixed per-site clock.

## Current ordered work

This is the single priority list for autonomous sessions. Apply
[STRATEGY](STRATEGY.md), inspect the selected TASKS entry and relevant source
capsule, and carry one bounded decision to completion. Explicit user directions
select their own task.

1. **Q01 — selected next quantum decision.** Use B67's premise map to define
   an exact finite-capacity operational description closed under reversible
   transformations and composition. Test which independent physical premise
   enforces that closure or purification in the mechanical class. Hardy's
   moving-ball example motivates this question; trajectory continuity alone
   does not settle it. Stop at one explicit model/countermodel and premise
   decision, not a full reconstruction-proof audit. See [Q01 handoff](handoffs/Q01.md).
2. **K01 — supporting alternative if context independence is decisive.**
   Test whether local measurement descriptions extend to one common
   system-plus-apparatus state, using I007 and the exact operational class
   selected in Q01. Select only if this changes Q01's exclusion premise;
   otherwise reassess the gap track after the Q01 milestone.

After each milestone, replace this list with the next actual choices. An open
umbrella task does not reserve all subsequent sessions.

## Consolidated findings and parked work

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
  explicit interacting chain give relaxation-gap control. G03 is complete:
  bounded coupling and a clock floor yield a uniform finite-volume bound.
  General-graph variants are parked for a named operator/limit dependency;
  a physical Hamiltonian and continuum transfer remain open.
- A19, A14, R02, M03 and historical H11 remain supporting work. Select them
  when they decide a named main-track premise or the user requests them.

The [ledger](../claims/LEDGER.md) owns acceptance and literature status. P04
promoted no new claim; G03 adds C124 with written proof review and bounded B68
literature coverage, including the unresolved source-image boundary. The [dated state history](STATE-history-2026-09-12.md)
and task handoffs preserve the earlier milestones; their old next-task text
is historical. User-supplied bibliography and source originals remain intact.

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
