# navstokgap: what survives refinement, from Newton's action to the $SU(3)$ mass gap

**Website:** <https://arivero.github.io/navstokgap/> lists every result by
track, with the Markdown source and the typeset PDF for each. Rebuild it with
`make site`.

**Goal (2026-09-26).** One paper comparing what survives refinement in
Newton's action problem, in pure $SU(3)$ Yang--Mills theory, and in QCD
with zero and nonzero quark masses. The two proof goals are **the
necessity of a positive action scale in Newton's Galileo comparison**,
from independently justified premises, and **the continuum existence and
mass gap of pure $SU(3)$ Yang--Mills** in four dimensions. The pion is a
benchmark for which symmetries a mechanism preserves. The
[working note](notes/three-continuum-limits.md) sets out the comparison;
[STATE](research/STATE.md) is the live queue.

## The organizing idea: local insertion laws

A limit is built by inserting one new variable at a time and asking how
the old observations and the dynamics are recovered.

- [Inserting a point, subdividing a cell](notes/refinement-composition-and-limit.md)
  ([PDF](out/papers/refinement-composition-and-limit.pdf)): eliminating an
  inserted Newtonian time changes the discrete action by
  $-F^2uv(u+v)/(8M)$, a cubic counterterm restores exact composition, and a
  summable-defect theorem gives the limit over arbitrary partitions,
  $\|Q_\pi-U_T\|\le F^2T|\pi|^2/(24M\hbar)$. Two-dimensional Yang--Mills
  subdivides exactly by heat-kernel convolution.
- [Series and parallel](notes/series-parallel-gauge-refinement.md)
  ([PDF](out/papers/series-parallel-gauge-refinement.pdf)): halving one
  lattice direction factors exactly into series moves, which close in
  every dimension, and parallel insertions in the $\binom{D-1}{2}$
  transverse planes, which carry the whole renormalization problem (none
  in $D=2$, one in $D=3$, three in $D=4$). The free-field defect is exact
  and equals the error of Migdal's bond moving. For compact $U(1)$ in
  three dimensions one step is proved to equal the free step up to an
  extensive error of density $e^{-\pi^2/(8\lambda_3a)}$, which explains
  why its lattice gap (Göpfert--Mack) disappears in the fixed-coupling
  continuum limit (Gross). The $SU(2)$ midpoint's curvature term is explicit.

## Open problems, stated for the next agents

Each item is a theorem-sized step with its hypotheses written in the
linked note.

1. **The $SU(2)$ cube at order $t$.** Show that the $O(\lambda_3a)$
   curvature and commutator terms of one parallel insertion reduce to a
   coupling shift plus operators irrelevant on smooth fields (Hypothesis
   P($\alpha$) of the series/parallel note, §4), then do $SU(3)$.
2. **A full mid-plane and iteration.** Prove P($\alpha$) for a whole
   non-abelian mid-plane by a small-field cluster expansion, stable under
   iteration, giving three-dimensional ultraviolet control in the
   insertion language; compare Balaban's 1985 ultraviolet stability.
3. **The four-dimensional logarithm.** Extract the one-loop running
   $g_0^{-2}(2a)=g_0^{-2}(a)-2b_0\log2$ from the three parallel insertions
   of each directional halving.
4. **From ultraviolet control to a gap.** On the fixed-$\lambda_3$
   trajectory, prove $E=C_3\hbar c\lambda_3$ with $0<C_3<\infty$. The
   compact $U(1)$ comparison shows the mechanism must come from the
   non-abelian terms.
5. **Newton's record.** A universal action unit already follows from
   classical radiation thermodynamics, and back-action indeterminacy is
   impossible with Liouville dynamics, product preparations and Bayesian
   records ([unit and indeterminacy](notes/necessity-unit-and-indeterminacy.md)).
   Find a physically justified premise that denies one of those three and
   makes the unit a floor on records
   ([the Planck paper](notes/planck-gap-paper.md) holds the conditional
   bounds).

## The Newton component

[The cost of a mark](notes/planck-gap-paper.md)
([PDF](out/papers/planck-gap-paper.pdf)) is the developed synthesis. With
canonical quantum kinematics supplied, every instrument obeys
$\frac s8\sum_j\Delta(\hat D_j)+\frac J2\sum_j\Delta(\hat X_j)\ge\hbar\arcsin(1-2\epsilon)$,
pairing Newton's sagitta $s$ with the impulse a record leaves undetermined
and his impulse $J$ with the displacement; Newton's inscribed polygon
differs from the parabola by the pure phase $F^2\sum_j\tau_j^3/(24m\hbar)$;
and the *Opticks* holds a measured least length and a period-times-momentum
invariant under refraction. The independent necessity of $\hbar>0$ is
open problem 5.

## The Yang--Mills map

[The position note](notes/mass-gap-position.md)
([PDF](out/papers/mass-gap-position.pdf)) and the
[conditional theorem](notes/mass-gap-conditional-theorem.md) hold what is
proved (finite-lattice and volume-uniform strong-coupling gaps), what is
imported, and the open blocking and mixing estimates (H1, H2), with
construction and nontriviality explicit.

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
