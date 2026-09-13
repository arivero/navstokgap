# Q01: finite observable repair of Hamiltonian descent

## Decision before calculation

2026-09-13. Target: Q01's exact finite operational closure dependency in B70
(action obligation 5). For C127's H=J u_z v_z, decide whether a finite real
observable space containing the terminal effects is invariant under all
physical times for every Borel preparation. Finite closure would retain the
repair; an infinite independent orbit rules it out in this class. Stop at
that proof and one bounded prior-literature audit. C127 exhibits only one
missing moment and therefore does not decide finite repair.

This finishes the named repair decision after the interaction/descent steps.
The other main track needs independently specified physical dynamics; another
G04 parent variant cannot supply it. After this step, consolidate Q01's
premise boundary rather than start another spin interaction or truncation.

Working source capsule: B72's classical spin Poisson dynamics supplies the
Hamiltonian flow; B67/Hardy section 7 motivates exact operational closure;
B70 assumes reversible action on the retained tensor state. The test is the
orbit of a retained transverse spin observable under that flow. S_A,S_B are
supplied action parameters, not a derived universal constant.

Audit budget: one sequential gpt-5.6-luna worker, low effort, no descendants;
at most two search queries and one primary paper's selected passages (up to
six pages). Review finite Koopman invariant-space precedent and the written
proof; no numerical/symbolic scripts. Effective settings reported only if
independently available.

## Result and acceptance

Entry HEAD was 06b6294; worktree was clean. [C128](../../notes/hamiltonian-finite-closure.md)
proves no finite real bounded observable span containing the retained effects
is invariant for C127 on any nonzero time interval. The orbit of u_x+i u_y
restricts to exponentials with arbitrarily many distinct frequencies;
a Vandermonde argument proves independence. A finite atomic separation lemma
shows nonlinear updates of finite expectations also force linear-span closure
when every Borel preparation is admitted. No regularity of added observables
is needed, and pointwise equality includes all Dirac preparations.

One sequential gpt-5.6-luna worker at requested low effort completed B74;
effective settings were not independently exposed. One query and one primary
paper, Brunton et al. (2016), selected HTML passages. Coordinator independently
rechecked metadata and the invariant-space prose around equations (9)–(10),
and reviewed both written arguments. The source supplies the established
framework; the spin specialization and expectation lemma are derived here.
No novelty claim, full-paper audit or numerical/symbolic scripts.
See the [B74 review](../../reviews/finite-closure-B74.md).

## Strategic consequence and queue

Finite enlargement is rejected for this interaction, retained effects and
all-preparation class. Exact closure requires infinite observable dimension
or changed model premises. Infinite dimension does not determine operational
capacity, force quantum structure or select a universal positive action scale.
The supplied S_A,S_B still set the mechanical action units.

Selected next: consolidate C125–C128/B70 into one physical-premise and
claim-to-source map, reusing completed audits. This concludes the spin repair
family rather than dispatching another hierarchy/truncation variant. Such
variants are parked pending a named independently justified physical
restriction. Gap-track physical identification remains supporting until
independent physical dynamics or a named limit dependency is supplied.
STATE and TASKS have been reconciled; the programme and synthesis integrate C128.

## Validation

`make check` passed 1471 local Markdown links, source companions, citation keys
and registered source hashes before the final handoff links were added.
`make papers` built all 17 papers with its reference/layout gates passing.
Visually reviewed synthesis page 5 and programme pages 1–4; the latter reflowed
with the updated premise paragraph. Fifteen unrelated PDFs were restored only
after extracted-text equality to entry HEAD. `git diff --check` passed.
The final `make check` passed 1473 local links and all source-integrity checks.
