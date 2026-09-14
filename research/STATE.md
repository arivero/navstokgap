# Restart state

Updated: 2026-09-14. **Q13 shared-readiness constraint completed.**
User direction now prioritizes publication development; C128/B74 remains accepted.
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

1. **Publication author completion — waiting for author input.** P07's
   [decision sheet](../reviews/publication-readiness-P07.md) recommends the
   elastic-gas draft first and the spin draft second. Both have revised
   explanations and PDF-inclusive review bundles. Author names, affiliations,
   destination/article type and submission direction remain. Further autonomous
   polishing is parked unless a reader report or concrete venue requirement
   identifies a change.
2. **Physical selection mechanism — next autonomous research.**
   [Q12](../notes/local-detector-coincidences.md) gives the all-gate coincidence
   bound for independent monotone receivers of fixed fractions of a common
   pulse, with a sharp efficiency/balance trade-off. Explicit routing,
   correlated-readiness and gate-selection countermodels identify its boundary.
   Q08--Q12 establish why fringes and discrete events alone leave source and
   apparatus premises open. These constructions remain exploratory.
   [Q13](../notes/shared-readiness-chsh.md) applies established CHSH to arbitrary
   shared readiness: independent settings and conditional locality give the
   all-gate bound 2; the supplied singlet predicts 2 sqrt(2). The dimensionless
   witness leaves the absolute action normalization free. No new claim.
   **Next autonomous construction switches to the gap track below.**
   Further single-splitter, thermal and shared-release tuning is parked.
   Q03--Q07 scale/topology/normalization variants remain parked; their
   [prior mechanism summary](handoffs/Q12-prior-state.md) retains the results.
   Existing uncommitted Q02 radiation work remains separate and untouched.
3. **Gap track — selected physical Hamiltonian construction.** Specify a local
   quantum spin Hamiltonian obtained by finite-depth local unitary conjugation
   of independent spins. Derive its interacting ground state, gap and size
   dependence with energy units explicit. This tests a direct Hamiltonian
   mechanism rather than another sampling-clock parent. Quantum structure and
   the energy-to-time action factor remain supplied inputs. Stop at that
   construction; continuum and arbitrary-perturbation claims are separate.

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
