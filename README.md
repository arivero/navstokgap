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

The user redirected the programme on 2026-09-12 after the calibration sequence
became too specialized. **Q01** is the next bounded quantum-premise audit, with
**K01** as a targeted measurement-compatibility test. **G03** is the following
gap milestone: replace independent-product control by an explicit interacting,
size-independent estimate. **R33's remaining curvature calculation is parked**;
its accepted results and open question are preserved.

[STATE](research/STATE.md) is the single current priority list.
[PROGRAMME](research/PROGRAMME.md) explains the questions;
[TASKS](research/TASKS.md) records scope and acceptance.
[STRATEGY](research/STRATEGY.md) requires follow-ups to state which main
conclusion they could change. The latest technical handoff does not by itself
choose the next research task.

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

Start with [AGENTS.md](AGENTS.md), STATE, PROGRAMME and the selected task.
Preserve user changes. Use written proofs and source review; the repository
prohibits numerical/symbolic verification scripts. Python remains allowed for
document builds, extraction and integrity tooling.

Run `make check` and `make papers`. Pandoc and LaTeX build the tracked papers;
checks cover local links, source companions, citation keys, checksums and PDF
reference/layout issues. See [TOOLS](research/TOOLS.md). Mathematical acceptance
rests on proofs and reviews, separately from document checks.

[The agent protocol](agents/PROTOCOL.md) permits one bounded Sol/Luna worker
at a time, followed by coordinator review; ultra effort is prohibited.
Commits and pushes have standing authorization. External publication and
correspondence require separate direction.
