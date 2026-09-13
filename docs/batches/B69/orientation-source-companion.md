# B69 orientation-closure source companion

## Result and bounded question

The classical orientation construction in `notes/classical-orientation-closure.md`
is a valid GPT-style countermodel to the sufficiency of finite capacity and
continuous local reversibility, provided its restricted effects and product
measurements are treated as explicit operational premises. Janotta and
Hinrichsen's review confirms the relevant standard construction: the minimal
tensor product is the convex hull of product states (separable states), while
the choice of a composite tensor product is additional theory data. It does
not supply purification or entangled pure states. The bounded audit therefore
supports the note's decision and stops there.

## Source and selected coverage

P. Janotta and H. Hinrichsen, *Generalized Probability Theories: What
determines the structure of quantum theory?*, arXiv:1402.6562v3 (13 August
2014), topical review. The coordinator corrected the worker's version date.
Selected HTML passages: §§2.1, 2.8–2.9 (preparations/effects, normalization,
consistency and restricted effects); §3.1 (classical simplex); §4 (single
systems as restricted higher-dimensional classical models); §5.4–5.6
(marginals, minimal/maximal tensor products and restricted-effect caveat);
§7 discussion of multipartite quantum features. This is selected passage
coverage, not a full review or reconstruction audit.

## Source-to-model match

The review defines operational states and effects through probabilities and a
unit effect, with consistency (0\le e(\omega)\le1). It states that a theory
may restrict effects and that single-system nonclassical state spaces can be
represented as higher-dimensional classical systems with restricted effects
(§§2.9, 4). This matches the orientation note's sphere hidden variable plus
affine directional effects: the ball is an operational quotient, not the full
space of hidden probability measures. If unrestricted hidden events were
measurable, the quotient would disappear, exactly as the note qualifies.

For composites §5.1 describes the minimal tensor product as the boundary
constructed from convex combinations of product states (separable states), and
the maximal tensor product as the opposite boundary fixed by positivity on
product effects (§§5.5–5.6). It emphasizes that many tensor products lie between
these bounds and that restricted effect spaces make the maximal construction
more complicated. Hence the note's joint measures and product/coarse-grained
tests instantiate the minimal/separable side; local rotations and correlated
classical preparations do not add globally entangled pure states.

## Proof review of the note

For a local effect (a+b\cdot u), (a\ge |b|) implies its value is at most
(2a), while its value at the zero orientation is (a). For a product effect
on (n) components this gives (e(u_1,\ldots,u_n)\le2^n e(0,\ldots,0)).
If (k) outcomes perfectly distinguish (k) states, each has value one on
its designated state and therefore value at least (2^{-n}) at the reference
product state. Summing the normalized effects at that reference state proves
(k\le2^n); opposite-pole product tests attain (2^n). Mixing and
coarse-graining preserve the inequality. This is a written proof, not a
numerical check.

The pure-state claim is also sound: the composite is the finite-dimensional
compact convex hull of product ball states. An extreme point of that hull is a
product of local extreme points; conversely a product of pure local states is
extreme (a pure marginal forces the corresponding local orientation almost
surely, successively). Thus every pure composite has pure marginals, so the
local zero state has no purification in this composite, already violating
purification existence.

The Hardy-face test should be read narrowly. The equal-sign effect has value
one only on the two pole configurations, so its unit-probability face is a
line segment with capacity two, not the three-dimensional single-system ball.
It therefore fails the proposed subspace-isomorphism requirement while the
full composite has capacity four. This establishes a composition/subspace
failure, not a contradiction of Hardy's reconstruction theorem.

## Decision and limits

Retain finite capacity, local continuous reversibility, and multiplicative
capacity/dimension as insufficient to select quantum composition. The missing
premise is availability and operational accessibility of globally pure,
possibly entangled composites together with an appropriate subspace rule (or
purification principle). The review gives no mechanical derivation of that
premise and no action normalization or positive action floor. Coverage is one
primary review, at the requested bounded page/section scale; no novelty or
exhaustiveness claim is made.

## Coordinator recheck

The coordinator verified the v3 header date and read §4's restricted-classical
construction, §5.1's definition/extreme-product statement and §5.6's distinction
between state and effect restrictions. The worker's §5.5–5.6 attribution of
the minimal definition was corrected to §5.1. Broad worker section lists denote
selected passages, not full-section reading; exact discovery-query count was
not reported. One route was reopened without coordinator discovery queries.
Requested Luna low; effective settings unverified. The note uses its own
written moment and capacity derivation, not a source formula transcription.
Local effects are unrestricted on the operational ball but restricted relative
to hidden-orientation events; composite effects are explicitly restricted too.
