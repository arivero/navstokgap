# B30 source companion: mechanical dilation audit

## Result and coverage

The two-source bounded audit supports the geometric classification of A16’s
dilation as conformally symplectic scaling. It supplies no direct prior-art
match for the exact external-potential map, covariance-action scaling, closure
zero-infimum proposition, or Kepler/softened/harmonic coupling examples.

Search budget: two queries, two primary pages. Primary reading was the HTML
record of Rastelli and Santoprete, arXiv:2408.15191, §§1.2, 2, 4 and 5
(including Proposition 4.7 and Theorem 5.4), and Sloan, arXiv:2407.13792,
§§I–II introductory passages. Evidence labels are metadata/abstract/passage;
equation extraction in the HTML is occasionally elided, so no omitted formula
is transcribed as evidence.

Rastelli–Santoprete explicitly frame positive scaling actions on exact
symplectic manifolds, define conformally symplectic maps, and state that scaled
cotangent lifts are conformally symplectic (Proposition 4.7). Their simple
mechanical and Newtonian n-body applications establish related prior art for
scaling geometry. Sloan describes mechanical dynamical-similarity reductions
that remove a scaling direction and retain a contact/Herglotz description.
Neither source addresses A16’s admissibility class or action lower bound.

## Proof/literature separation

Proof status in the repository: the Hamilton equations, flow conjugacy,
`F_a^*omega=a omega`, degree-one action scaling, covariance pushforward and
conditional zero-infimum proposition are written derivations in
`notes/action-scale-dilation.md`. They require the stated smooth domain,
finite moments, invariant pushforward preparation, and closure along arbitrarily small
positive `a`. No model at `a=0` is used.

Literature status: related conformal-symplectic scaling is established prior
art. The combined covariance estimator and action-selection obstruction have
no direct match in the bounded passages. Coupling substitutions and the
force-bound obstruction are derived model consequences, with no direct source
match found. This audit does not establish novelty beyond the searched scope.

The source-to-model bridge is: conformally symplectic scaling motivates a
written fixed-force test of small-radius circles, checking whether a uniform
force/acceleration ceiling removes the contraction family while preserving a
well-defined preparation and action observable.

## Coordinator verification

Verified the titles/authors and the conformally symplectic statement in
[Rastelli–Santoprete v1, Definition 4.6 and Proposition 4.7](https://arxiv.org/html/2408.15191v1#S4.SS1),
and the contact/Herglotz context in
[Sloan v1](https://arxiv.org/html/2407.13792v1).
The source's fixed-Hamiltonian scaling symmetry and A16's map between
potentials are separate constructions. No source equation is imported into
A16's proof. The worker's “two pages” means two HTML documents and the named
passages, not two PDF pages. The closure hypothesis needs arbitrarily small
admitted values of a, rather than every small a; the note states the weaker
sufficient condition correctly. Proof acceptance is in the coordinator review.
