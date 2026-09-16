# Newtonian trajectories, quantum premises and gap mechanisms

This project asks which physical premises could force quantum structure with a
positive universal action parameter, and which dynamical estimates could produce
a gap that survives continuum and large-system limits. Newtonian trajectories
and cut refinement supply mechanical tests; the Yang–Mills comparison supplies
the companion field-theory question.

## Read the consolidated result

[Classical action scales: obstructions, conditional bounds and quantum premises](notes/action-scale-obstructions.md)
([PDF](out/papers/action-scale-obstructions.pdf)) brings the accepted results
into one argument:

- Continuous variation, admissible contractions and small excitation permit
  vanishing action in specified classical classes.
- Positive orbit and fluctuation bounds identify their supplied excitation or
  preparation inputs.
- Classical apparatus recovery and ambiguity depend on preparation, records
  and calibration; those error products have no established universal quantum role.
- Spectral control requires coverage of slow modes and bounds that survive the
  relevant limits. Independence currently supplies the product-system result.

The paper links its statements to the full proofs and inherited source audits.
It establishes no general impossibility theorem for classical reconstruction,
no new novelty claim and no Yang–Mills mass-gap result.

## Current research direction

The selected target is **Galileo's falling parabola versus inertial horizontal
motion**: their enclosed area converts to energy times time, and the research
asks what physical Planck-scale obstruction prevents indefinite refinement
into distinguishable classical alternatives. This is Newton's limiting-area
question, not Kepler's swept-area law. The matched-endpoint chord lens has a
different coefficient and is kept explicit.

[The N01 derivation](notes/newton-insertion-action.md)
([PDF](out/papers/newton-insertion-action.pdf)) gives the exact conversion and
a closed quantum comparison with a conditional resolution threshold. The
universal obstruction remains open. **The intended innovation is a mathematical
necessity theorem**, not a resolution limit obtained by assuming quantum
mechanics. The next construction must test an independently justified
consistency principle against zero-action refinement. Quantum-premise,
apparatus and gap results
support this target when they discharge a named dependency.

[STATE](research/STATE.md) is the one live priority page; PROGRAMME,
TASKS and STRATEGY are historical context.

## Supporting proofs and sources

| Topic | Entry point |
| --- | --- |
| Action selection and limiting variables | [Action target](research/ACTION_FIELD_TARGET.md) |
| Refinement, retained state and interventions | [Cut target](research/CUT_POINT_TARGET.md) |
| Mechanical contraction and its admissibility | [Dilation proof](notes/action-scale-dilation.md) |
| Positive orbit cost from excitation and force | [Closed-orbit bound](notes/closed-orbit-force-action.md) |
| Conditional mass universality | [Composition proof](notes/composition-universality.md) |
| Classical records and receiver preparation | [Technical receiver compilation](notes/conservative-harmonic-receiver.md) |
| Quantum consequences under supplied premises | [Checkerboard comparison](notes/checkerboard-dynamics.md) |
| Hidden modes and gap estimates | [Susceptibility proof](notes/susceptibility-gap.md) |
| Physical and auxiliary field-theory gaps | [Comparison](notes/comparison-and-bridges.md) |
| Acceptance and literature status | [Claim ledger](claims/LEDGER.md) |

[Papers](papers/README.md) indexes the maintained manuscripts and PDFs.
[Source ideas](references/IDEA_BRIDGES.md) connects named tasks to existing
companions. [Source catalogue](docs/README.md) and
[bibliography](references/library.bib) retain original evidence and metadata.
The [dated state history](research/STATE-history-2026-09-12.md) and handoffs
preserve earlier milestones; their old next-task wording is historical.

## Work and reproduce

Start with [AGENTS.md](AGENTS.md) and [STATE](research/STATE.md); that is
the whole required reading. Results are notes in `notes/`, built one at a
time with `make paper NOTE=<slug>`; `make check` verifies links, source
companions, citation keys and checksums. Written proofs are the
mathematical check; the repository prohibits numerical or symbolic
verification scripts. PROGRAMME, STRATEGY, TASKS and the agent protocol
are historical context. Commits and pushes have standing authorization;
external publication and correspondence require separate direction.
