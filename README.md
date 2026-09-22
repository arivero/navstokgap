# navstokgap: the Planck gap in Newton's comparison, and the Yang--Mills mass gap

**Website:** <https://arivero.github.io/navstokgap/> lists every result by
track, with the Markdown source and the typeset PDF for each. Rebuild it with
`make site`.

The active goal, set on 2026-09-17, is to establish the Planck gap with
Newton-age arguments and their modern equivalents. Galileo's comparison of
the inertial line with the falling parabola, whose area Newton takes to
zero in Lemmas X and XI, acquires a floor of order $\hbar$ once it has to
be recorded. The $SU(3)$ Yang--Mills mass gap, the goal from 2026-09-16,
is paused with its map intact.

## Read the current result

[The cost of a mark: Newton's vanishing sagitta and a floor of order $\hbar$](notes/planck-gap-paper.md)
([PDF](out/papers/planck-gap-paper.pdf)) is the synthesis:

- Newton's limit has no geometric floor, and a recorded comparison has one.
- For every instrument,
  $\frac s8\sum_j\Delta(\hat D_j)+\frac J2\sum_j\Delta(\hat X_j)\ge(1-2\epsilon)\hbar$:
  Newton's sagitta $s$ is paired with the impulse a record leaves
  undetermined, and his impulse $J$ with the displacement.
- For uncorrelated Gaussian marks the floor takes the sharp form
  $\tau\Delta E\ge24z_{1-\epsilon}^2\hbar$, from the conjugacy of a mark's
  error and the impulse it delivers.
- Newton's inscribed polygon differs from the parabola by the pure phase
  $F^2\sum_j\tau_j^3/(24m\hbar)$, the parabolic segments of the chords
  converted by $\hbar$, whatever the state of the body.
- Newton's *Opticks* holds a measured least length, a posited least
  impulse and a disposition whose period times momentum is invariant under
  refraction; its Prop. XII denies the premise that would join them to a
  floor.

[STATE](research/STATE.md) lists every result with the note that proves it.

## The paused mass-gap track

[The position note](notes/mass-gap-position.md)
([PDF](out/papers/mass-gap-position.pdf)) is the synthesis: what is
proved, what is imported, what has been ruled out, and what remains.
Its full working queue as of 2026-09-18 is STATE at commit 6bc52cb. In
short, the
conjecture decomposes into six named statements, of which the
finite-lattice gap and the volume-uniform strong-coupling gap are proved
here; the clause $m<\infty$ is reduced to the existence of the theory
plus the nontriviality of one flowed correlator; and the clause $m>0$
remains, with real-space blocking and expansion around the free theory
both closed off by explicit computation.

## Earlier consolidated result

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
