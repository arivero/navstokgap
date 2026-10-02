# Provisional book architecture

Based on the maintained notes, 2026-10-01; chapters are proposed, not written.
The test question is: **what survives refinement, and under what conditions
can a positive physical scale survive with it?** The repository establishes
several exact insertion laws, conditional scale bounds and informative
closures. It has not established either main necessity/existence-and-gap goal.
The [reading paths](dependencies.md) organize the established inputs and
their open extensions.

## Choosing a spine

| Organization | Strength | Cost | Decision |
| --- | --- | --- | --- |
| Refinement first | Exact local composition gives a shared mathematical entry; makes loss of state and generated interactions visible | Can conceal the different Newton and gauge premises | Preferred, with separate case-study parts and an explicit analogy audit |
| Supplied versus generated scales | Cleanly separates action calibration from dimensional transmutation | Pushes the local constructions too far back | Use as the recurring chapter question |
| Two independent case studies | Most honest about distinct mathematics | Duplicates cuts, composition and limiting-order discussions | Retain separate technical parts after common foundations |
| The recurring zero branch | Organizes decisive countermodels | Makes the book read as a collection of failures | Use as a diagnostic, not the narrative spine |

The preferred reading is foundations → Newton records → gauge refinement
→ physical scales and unfinished exits. An exact identity on one side is
never promoted to a proof on the other. [Correspondences](refinement-correspondences.md)
explains where a common equation exists and where the comparison is structural.

## Part I. What a refinement must preserve

### 1. Two questions and one discipline of limits

Introduce Newton's positive action necessity and the pure SU(3) continuum
existence/gap target, with physical time, cutoff, volume, preparation and
observable weight kept separate. The pion illustrates protection of a zero
threshold by symmetry. Sources: [three continuum limits](../notes/three-continuum-limits.md),
[official targets](../notes/millennium-problem-definitions.md),
[lattice obligations](../notes/mass-gap-obligations-lattice.md).
Purpose: formulate the actual endpoints without identifying a sampling gap,
a finite-box gap or a supplied action constant with either endpoint.

### 2. Insert a variable, then eliminate it

Start with the exact constant-force cut and gauge heat-kernel convolution.
Explain compatibility under every admissible partition, the sufficient
summable-defect criterion, and the harmonic construction beyond a finite
Cauchy estimate. Sources: [refinement composition](../notes/refinement-composition-and-limit.md),
[cut consistency](../notes/cut-point-consistency.md),
[zero spacing](../notes/zero-spacing-any-action.md).
Purpose: exact local composition and stated limiting hypotheses, without a
positive scale being inferred from consistency alone.

### 3. The state at a cut

Position alone generally loses momentum; eliminating another body can leave
memory even after position and momentum are retained. Telegraph bridges give
a constructive alternative to scalar convolution rigidity. Sources:
[classical cut state](../notes/classical-cut-state.md),
[reachable composition](../notes/reachable-cut-composition.md),
[three-body memory](../notes/three-body-cut-memory.md),
[telegraph bridge](../notes/telegraph-return-bridge.md).
Purpose: identify the closure data before taking a continuum limit.

## Part II. Newton's cell, and the price of its record

### 4. A shrinking area with an exact action

Derive the inertial–parabola area, distinguish its matched-endpoint chord
lens, and show how the cut measure decomposes the Dirichlet action into
orthogonal hats. The polygon's scalar phase uses the same functional with
a supplied phase unit. Sources: [insertion action](../notes/newton-insertion-action.md),
[cut measure](../notes/cut-measure-newton.md),
[polygon phase](../notes/polygon-lift-phase.md).
Purpose: additive finite action bookkeeping; the geometry itself reaches zero.

### 5. From Gaussian marks to general disturbance

Present the sharp invariant Gaussian benchmark first, then arbitrary pointer
recoil and arbitrary-instrument disturbance/Bures bounds. Explain which
resources belong to the body, apparatus and comparison states, and why a
known preparation can escape a preparation-independent cell floor. Sources:
[mark cost](../notes/mark-cost-and-statistical-floor.md),
[probabilistic bound](../notes/planck-gap-probabilistic.md),
[recoil](../notes/record-costs-recoil.md),
[disturbance](../notes/record-costs-disturbance.md),
[path length](../notes/record-distance-path-length.md).
Purpose: strongest current information/disturbance theorem, with its quantum
input and preparation dependence visible. The early bounded-support model
belongs in a correction box.

### 6. A unit, a floor, and the zero branch

Separate dimensional availability, radiation calibration, composition
universality, quantum role and positivity. Newton-compatible deformations
and covariant state restrictions expose alternatives to joint determinacy;
Leibniz continuity becomes a precise but family-dependent record criterion.
Sources: [fifth postulate](../notes/principia-fifth-postulate.md),
[unit and indeterminacy](../notes/necessity-unit-and-indeterminacy.md),
[dimensional selection](../notes/action-unit-dimensional-selection.md),
[rotation composition](../notes/rotation-composition-universality.md),
[Leibniz records](../notes/leibniz-continuity-records.md).
Purpose: universality and consistency can retain the common zero branch.

### 7. Can a physical apparatus keep the restriction?

Use the two-pointer escape and exact Gaussian posteriors as reference cases,
then physical feedback, adaptive records, nonlinear generators and weak
copies. Finish at coherence memory in the supplied quantum free-evolution
reference: positive tails permit phase reconstruction but fail uniform
stability in the stated local-data metric. Sources:
[indeterminacy routes](../notes/newton-indeterminacy-routes.md),
[recording closure](../notes/sed-closure-under-recording.md),
[SED calibration](../notes/sed-zeta-radiation-link.md).
Purpose: a concrete physical history law remains missing; a covariance ceiling
or a stationary bath alone does not discharge it.

## Part III. Gauge refinement and the generated action

### 8. Solved lower-dimensional tests

Explain exact two-dimensional subdivision, compact-group Lévy alternatives,
and why three-dimensional U(1) monopole suppression disappears under its
fixed-coupling continuum trajectory while the same total-variation budget
fails in four dimensions. Sources: [zero spacing](../notes/zero-spacing-any-action.md),
[Villain refinement](../notes/villain-monopole-refinement.md),
[halving atlas](../notes/halving-atlas.md).
Purpose: dimension and group change what survives; a solved regulator limit
does not automatically produce a nontrivial physical spectrum.

### 9. Series closes; parallel creates interactions

Factor directional halving into exact series moves and an interacting
mid-plane integral. Develop the exact SU(2) midpoint character and general
group/cut identities, including centre torsion at thirds for SU(3). Sources:
[series/parallel](../notes/series-parallel-gauge-refinement.md),
[SU(2) midpoint](../notes/su2-midpoint-exact.md),
[centre cuts](../notes/sun-midpoint-centre.md),
[order-t calculation](../notes/su2-midplane-order-t.md).
Purpose: isolate the nonlinear RG obligation; traces and one-loop coefficients
are not the full normalized matrix or group-integral comparison.

### 10. Retain the barrier and normalize the clusters

Organize the large small-field notebook by logical dependency: convexity and
rarity, response contacts, weak recoupling, marked connected sets, exact
dressing, and moving Gaussian sources. Sources:
[small-field notebook](../notes/su2-midplane-small-field.md), especially
§§24–37; [large-field action cost](../notes/large-field-action-lower-bound.md)
as a scoped supporting input.
Purpose: (116) and (112) in their weak strip, then the quadratic source test
for part of (113). Full nonlinear comparison, physical recoupling and stable
iteration remain the chapter's explicit open exit.

### 11. The four-dimensional logarithm

Compose Gaussian block maps before contracting generated vertices. Explain
tree-level scale invariance, the conditional one-loop logarithm and the
continuum-subtracted matching problem at arbitrary block depth. Sources:
[Gaussian blocking](../notes/gaussian-blocking-coupling.md),
[parallel logarithm](../notes/four-dimensional-parallel-log.md),
[4D composition](../notes/four-dimensional-composition.md),
[UV/IR ladder](../notes/uv-halving-ir-confinement.md).
Purpose: depth-uniform nonlinear matching and remainder control, rather than
an assumption that a formal running coupling is already a constructive RG.

## Part IV. Which scales can survive?

### 12. A rigorous strong side and a difficult arrival

State the Wilson transfer bound, the continuous-time finite-volume
Hamiltonian bound and Yarotsky's existential volume-uniform theorem
with their own normalizations, then the existential target box.
The October 2 KS numerical uniform threshold is withdrawn.
Explain why blocking
without coupling flow, global Agmon suppression, conjugate flow and physical
crossover certification do not bridge the weak trajectory. Sources:
[Wilson gap](../notes/wilson-strong-coupling-explicit.md),
[KS gap](../notes/kogut-susskind-strong-coupling-explicit.md),
[target box](../notes/strong-coupling-target-box.md),
[reasons to stop](../notes/reasons-to-stop-as-research.md),
[mass-gap position](../notes/mass-gap-position.md).
Purpose: a physical positive gap needs controlled arrival and construction;
all-bare-coupling T2′ is an optional stronger statement.

### 13. Spectral weight, valleys and the ultraviolet bridge

Contrast trial-state/moment upper bounds with lower-gap criteria from a
complete observable frame. Develop the matrix-model valley mechanism and
the torus/Feshbach test, retaining the UV dressing obstruction. The displayed
cutoff calculation uses SU(2); corresponding SU(3) operator estimates remain
an additional transfer obligation. Sources:
[moments](../notes/moment-hierarchy-upper-bounds.md),
[susceptibility](../notes/susceptibility-gap.md),
[low-dimensional gap](../notes/low-dimensional-mass-gap.md),
[Feshbach](../notes/weak-coupling-feshbach-reduction.md),
[torus valley](../notes/torus-valley-potential.md),
[UV Schur error](../notes/schur-error-ultraviolet.md).
Purpose: distinguish finite positive spectral weight and an upper energy
scale from a volume/cutoff-uniform positive lower edge.

### 14. What the comparison has earned

Return to the two independent proof goals. Tabulate exact correspondences,
structural analogies and the still-open physical premises, using
[three continuum limits](../notes/three-continuum-limits.md),
[Newton record/parallel move](../notes/newton-record-parallel-move.md),
[action floor and matrix gap](../notes/action-floor-yang-mills-gap.md),
[tangent groupoid](../notes/tangent-groupoid-trajectories.md).
Purpose: explain why RG appears through elimination without claiming that
its appearance selects positive action or proves a continuum mass gap.

## Material outside the main spine

| Placement | Material and reason |
| --- | --- |
| Historical excursus accompanying chapters 4–6 | Edition-local Newton, Galileo and ancient division passages; the Book I scholion is part of the argument's premises, not proof of a modern theorem |
| Apparatus appendix | Calibration/clock/preparation/recovery sequence, routed through conservative-harmonic-receiver; preserve individual designs and counterexamples |
| Technical appendix | SU(3) constants, exact character expansions, explicit threshold calculations, reachable-set and minimax formulas |
| Correction boxes | Bounded-support quantum mark failure; local/global Agmon; sharp-flux Gaussian nonclosure; torus holonomy; bare Feshbach UV |
| Supporting model boxes | Ising Hermitian transfer, finite-depth spin gap, checkerboard composition, classical mechanical interference |
| Research-history appendix | Old operational reconstruction, collision transport, discrete-substrate conversations, old programme branches and orphan snapshots |
| Forward-looking side note | Pion symmetry benchmark and speculative groupoid construction; neither adds a third active proof goal |

No source note is merged or replaced. [Synthesis opportunities](synthesis-opportunities.md)
identifies where a future chapter-sized synthesis would genuinely improve
retrieval rather than duplicate an existing compilation.
