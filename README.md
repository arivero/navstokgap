# Toward the Yang--Mills mass gap

The goal of this project, set on 2026-09-16, is a proof of the Yang--Mills
existence and mass-gap conjecture in the Jaffe--Witten formulation. Work
proceeds by theorems with explicit volume, cutoff and coupling dependence,
by lower-dimensional solved cases, and by the analogy with a positive
universal action scale, which the earlier phase of the project developed
through Newtonian trajectories and cut refinement.

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

[The position note](notes/mass-gap-position.md)
([PDF](out/papers/mass-gap-position.pdf)) is the synthesis: what is
proved, what is imported, what has been ruled out, and what remains.
[STATE](research/STATE.md) holds the working queue. In short, the
conjecture decomposes into six named statements, of which the
finite-lattice gap and the volume-uniform strong-coupling gap are proved
here; the clause $m<\infty$ is reduced to the existence of the theory
plus the nontriviality of one flowed correlator; and the clause $m>0$
remains, with real-space blocking and expansion around the free theory
both closed off by explicit computation.

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
