# navstokgap: what survives refinement, from Newton's action to the $SU(3)$ mass gap

**Website:** <https://arivero.github.io/navstokgap/> opens with interactive
refinement sketches and a short introduction to the two questions.
The [research map](https://arivero.github.io/navstokgap/research.html) and
archive lead to every maintained scientific note; selected notes have a PDF.
Use `make opening` to rebuild the introduction, research map, assets and
sitemap; `make site` regenerates all website pages. The diagrams illustrate
refinement and do not supply a simulation or a proof.

The generated [sitemap](https://arivero.github.io/navstokgap/sitemap.xml)
lists the maintained website pages without invented update dates.
For [IndexNow](https://www.indexnow.org/documentation), use the public key
in `scripts/site/indexnow-key.txt` and its deployed file at
`https://arivero.github.io/navstokgap/<key>.txt` as `keyLocation`; submit
changed URLs only after their deployment. One participating endpoint
shares notifications with the others. Building the site sends no notifications.
Google sitemap submission uses a verified Search Console property; its
[former ping endpoint is retired](https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping).

**For language models:** [`LLM.md`](LLM.md), also served at
<https://arivero.github.io/navstokgap/llms.txt>, maps established results,
their scope, known errors and verified prior art. The maintained notes
carry later corrections; [the retrieval catalog](notes/index.md) helps
find the relevant proof.

**Goal (2026-09-26).** One paper comparing what survives refinement in
Newton's action problem, in pure $SU(3)$ Yang--Mills theory, and in QCD
with zero and nonzero quark masses. The two proof goals are **the
necessity of a positive action scale in Newton's Galileo comparison**,
from independently justified premises, and **the continuum existence and
mass gap of pure $SU(3)$ Yang--Mills** in four dimensions. The pion is a
benchmark for which symmetries a mechanism preserves. The
[working note](notes/three-continuum-limits.md) sets out the comparison;
[STATE](research/STATE.md) is the live queue.
Both main proof goals remain open. Current Newton record bounds assume
positive quantum action; classical-limit and completion results do not
derive its necessity. The [provisional book](research/book-map.md) organizes
the proofs and physical premises into proposed chapters.

## The organizing idea: local insertion laws

We compare laws for inserting one variable and eliminating it, then ask
which estimates let those local laws be iterated into a physical limit.

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

## Current proof obligations

STATE chooses the next bounded unit. The current obligations are:

1. **Newton's physical premise.** Justify the coherence or model-selection
   premise used by a necessity argument independently of its desired
   positive-action conclusion. Radiation, readout and continuity routes
   have distinct hypotheses ([unit and indeterminacy](notes/necessity-unit-and-indeterminacy.md),
   [reachability](notes/zero-branch-reachability.md),
   [Kepler selections](notes/self-sufficiency-contrast.md)).
2. **Nonlinear gauge refinement.** Extend the retained-barrier quadratic
   moving-source input to the nonlinear centered estimates, physical
   recoupling and stable iteration required by the
   [mid-plane proof](notes/su2-midplane-small-field.md). Its SU(2) results
   do not by themselves supply the SU(3) comparison.
3. **Uniform matching and the physical spectrum.** Prove the depth-uniform
   matching and remainder bounds in
   [four-dimensional composition](notes/four-dimensional-composition.md),
   and the blocking, mixing and reconstruction obligations in the
   [mass-gap map](notes/mass-gap-position.md). Formal running, a fixed-box
   bound and a continuum physical gap require different estimates.

## The Newton component

[The cost of a mark](notes/planck-gap-paper.md)
([PDF](out/papers/planck-gap-paper.pdf)) is the developed synthesis. With
canonical quantum kinematics supplied, every instrument obeys
$\frac s8\sum_j\Delta(\hat D_j)+\frac J2\sum_j\Delta(\hat X_j)\ge\hbar\arcsin(1-2\epsilon)$,
pairing Newton's sagitta $s$ with the impulse a record leaves undetermined
and his impulse $J$ with the displacement; Newton's inscribed polygon
differs from the parabola by the pure phase $F^2\sum_j\tau_j^3/(24m\hbar)$;
and the *Opticks* holds a measured least length and a period-times-momentum
invariant under refraction.

The [Kepler proof](notes/self-sufficiency-contrast.md) now controls the
singular multiplier and both centroids on fixed collision-free intervals.
Its relativistic thresholds depend on a selected point-source domain;
the critical Klein--Gordon radial branch does not establish full evolution.
The [coherence countercase](notes/zero-branch-reachability.md#4c-theorem-5-the-incoherent-attachment-reaches-zero)
recovers classical swarm records from incoherent packets for quadratic
forces. The paper and [joint synthesis](notes/three-continuum-limits.md)
state these boundaries in their openings. The new October 2 derivations
are unrefereed; independent positive-action necessity remains open.

## The Yang--Mills map

[The position note](notes/mass-gap-position.md)
([PDF](out/papers/mass-gap-position.pdf)) and the
[conditional theorem](notes/mass-gap-conditional-theorem.md) hold what is
proved (finite-lattice and volume-uniform strong-coupling gaps), what is
imported, and the open blocking and mixing estimates (H1, H2), with
construction and nontriviality explicit.
Wilson has explicit volume-uniform transfer bounds. The October 2
[KS correction](notes/kogut-susskind-strong-coupling-explicit.md)
withdraws its numerical uniform threshold; its surviving explicit bound
depends on volume. The
[existential uniform theorem](notes/strong-coupling-uniform-gap.md) and
[perturbed target region](notes/strong-coupling-target-box.md) retain their
own hypotheses. None of these fixed-cutoff results completes the continuum
construction or transfers a threshold between the two operators.

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

Start with [AGENTS.md](AGENTS.md), which names the required reading;
[STATE](research/STATE.md) gives the live queue. Results are notes in `notes/`, built one at a
time with `make paper NOTE=<slug>`; `make check` verifies links, source
companions, citation keys and checksums. Written proofs are the
mathematical check; the repository prohibits numerical or symbolic
verification scripts. PROGRAMME, STRATEGY, TASKS and the agent protocol
are historical context. Commits and pushes have standing authorization;
external publication and correspondence require separate direction.
