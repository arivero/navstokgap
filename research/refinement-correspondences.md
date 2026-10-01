# Newton–Yang–Mills correspondence test

2026-10-01. An exact formula in each theory is not automatically an exact
identification between the theories. The classifications below keep the
objects and the map explicit. Sources retain their stated reading levels;
this document introduces no new physical premise.

## 1. Exact common composition at the Gaussian/semigroup level

The Newton free kernel and a group heat kernel each obey Chapman–Kolmogorov:
K_(t1+t2)(x,z)=∫K_t1(x,y)K_t2(y,z)dy. For gauge variables the integral is
normalized Haar convolution, k_t1*k_t2=k_(t1+t2). In a linear Gaussian model,
integrating an inserted variable gives a Schur complement; variances in
series add and precisions in parallel add. These are exact common
composition laws, with different state spaces and normalizations.

Sources: [refinement composition](../notes/refinement-composition-and-limit.md),
[series/parallel](../notes/series-parallel-gauge-refinement.md),
[Gaussian blocking](../notes/gaussian-blocking-coupling.md).
Boundary: Newton's deterministic trajectory insertion is not itself a heat
semigroup or a measure on gauge connections. Compact-group series closure
does not close the interacting transverse-plane integral in D>2.

## 2. Gaussian records versus parallel gauge faces: exact algebra, structural transfer

For a Gaussian quantum position instrument, forgetting y gives
ρ(x,x′)↦ρ(x,x′)exp[−(x−x′)²/(8σ²)]. Its Wigner transform is exactly momentum
convolution with v=ℏ²/(4σ²). Two simultaneous records satisfy
σ_eff^−2=σ1^−2+σ2^−2 and v_eff=v1+v2. Abelian Gaussian parallel-face weights
multiply, so their inverse heat times add. Thus the precision algebra is
exactly the same algebra, after naming the covariance/precision variables.

Source: [Newton record move](../notes/newton-record-parallel-move.md), §1–2,
and the gauge Gaussian calculation in [series/parallel](../notes/series-parallel-gauge-refinement.md).
Boundary: a trace over a quantum pointer is a completely positive channel;
a gauge mid-plane marginal is a Euclidean integral with nonabelian generated
interactions. No constructed functor identifies these full objects. The
Wigner representation may be signed, and ℏ is already supplied. Call the
physical comparison a structural analogy, not a derivation of either goal.

## 3. Additive cut action versus generated interactions: structural only

For constant force, Kτ=F²τ³/(24m) and insertion at fraction s gives
Kτ−Ksτ−K(1−s)τ=3s(1−s)Kτ. The general Dirichlet action decomposes into
orthogonal Schauder-hat costs. This is an exact nonnegative additive measure
on cuts of the specified classical path.

Eliminating gauge variables gives S_eff(U)=−log∫exp[−S(U,V)]dV, up to
normalization. Connected cumulants generate terms supported on multiple
plaquettes; they need not be nonnegative or a finitely additive cut measure.
Sources: [cut measure](../notes/cut-measure-newton.md),
[4D composition](../notes/four-dimensional-composition.md),
[small-field dressing](../notes/su2-midplane-small-field.md), §36.
The common question is the price of eliminating variables. There is no
proved identification of the cut measure with all generated gauge couplings.

## 4. Universality versus dimensional transmutation: distinct mechanisms

Independent mass composition in the Brownian model yields mD=κ; compatible
interacting rotation generators give a common action coefficient. Neither
argument forces κ>0. Four-dimensional perturbative running instead has
d(1/g²)/d log μ=2b0+… and supplies a matched scale of the form
Λ≈a^−1 exp[−1/(2b0g²)], with further matching corrections.

Sources: [stochastic route](../notes/stochastic-route-velocitas-ultima.md),
[rotation composition](../notes/rotation-composition-universality.md),
[parallel logarithm](../notes/four-dimensional-parallel-log.md),
[UV/IR](../notes/uv-halving-ir-confinement.md).
The Newton coefficient has action units and may be zero. Λ has inverse-length
units, and a physical positive gap needs a surviving positive coefficient
and observable weight as well as a continuum construction. These are
structurally useful scale questions, not the same selection theorem.

## 5. Zero action versus zero gap: structural diagnostic

The classical zero-action branch is an admissible law under several Newton
consistency premises. A gauge zero gap is a statement about a reconstructed
Hamiltonian's spectral edge after volume/cutoff limits; a vanishing lattice
gap can also be the correct scaling of a positive physical gap.
Sources: [fifth postulate](../notes/principia-fifth-postulate.md),
[three continuum limits](../notes/three-continuum-limits.md),
[lattice obligations](../notes/mass-gap-obligations-lattice.md).
The common diagnostic is “which hypothesis excludes zero?” The zero objects
and their limits differ. Goldstone protection in the pion comparison supplies
an additional symmetry mechanism, not an action-normalization statement.

## 6. Valley lifting: a conditional mechanical implication

In the x²y² matrix-mechanical model a supplied transverse phase-space-area
floor bounds excursions along the valley at fixed energy. The operator
uncertainty argument supplies quantum confinement in the corresponding
Schrödinger model. Sources: [low-dimensional gap](../notes/low-dimensional-mass-gap.md),
[action-floor model](../notes/action-floor-yang-mills-gap.md).
This is a useful model-level conditional connection. Semiclassical phase-space
counting does not prove a four-dimensional gauge gap. In D=4 a mass/energy
gap and c alone do not reconstruct an action unit.

## 7. Tangent groupoid and “all zoomings”: exact ingredients, open synthesis

The tangent groupoid relates pair-groupoid arrows at nonzero scale to tangent
vectors at zero. Time-graded trajectory refinement and the harmonic
arbitrary-partition construction have their own exact composition laws.
Quantum diffusive paths and Newton's ballistic ultimate-velocity fibre have
different scaling. Sources: [groupoid trajectories](../notes/tangent-groupoid-trajectories.md),
[refinement §§3c–3d](../notes/refinement-composition-and-limit.md).
A gauge double-groupoid organizing parallel moves is proposed, not proved.
Use the language when it names state, composition and topology. The rhetorical
claim that all these limits are one mechanism adds no theorem and should be
omitted from the main narrative.

## Consequence for the book

Keep exact insertion and state retention in the common opening part. Give
Newton recording and gauge effective-action construction separate technical
parts. Reunite them through explicitly scoped scale and spectral questions
in the final part. This is the structure adopted in [the book map](book-map.md).
