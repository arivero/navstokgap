# Finite operational closure does not select quantum composition

A classical random orientation, observed only through affine directional
responses, has a ball of operational states, distinguishability capacity two
and continuous reversible connections between all pure states. Its natural
classical composites retain these exact operational descriptions but fail
purification and Hardy's subspace requirement. Thus finite capacity and
reversible local closure leave a substantive composition premise to select.

Q01 second milestone, 2026-09-13. This is an operational countermodel with
classical hidden variables and stipulated measurement restrictions. It is not
a derivation of those restrictions from an apparatus Hamiltonian. All state
and response coordinates are dimensionless; no action constant is introduced.
The standard restricted-classical and minimal-composite constructions are
matched in [B69](../references/batches/B69.md); the explicit checks below
are derived applications with no novelty assertion.

## 1. One orientation and its allowed experiments

The hidden state is u on the unit sphere in R^3. Preparations are all Borel
probability measures mu on that sphere. A measurement is a finite family

$$e_i(u)=a_i+b_i\cdot u,\qquad a_i\ge |b_i|,\qquad
\sum_i a_i=1,\quad\sum_i b_i=0. \tag{1}$$

These nonnegative functions sum to one. Their probabilities depend exactly
on r=integral u dmu. Every vector in the closed unit ball is achievable by
mixing two opposite orientations. Conversely the directional binary tests
(1+/-n dot u)/2 determine all components of r. Thus operational equivalence
is equality of r, and the operational state space is exactly the ball.

Its pure states are the unit sphere. If a measurement distinguishes k states
r_i perfectly, then 1=a_i+b_i dot r_i<=2a_i for each successful outcome.
Summing a_i gives k<=2. Opposite unit vectors attain two. The normalized
ball has affine dimension three; its unnormalized cone has dimension four.

Allowed reversible transformations are rotations u -> R u, R in SO(3).
They descend exactly to r -> R r. Rotation paths connect any two pure states
continuously and reversibly. Convex mixtures, compositions of rotations and
measurement probabilities remain closed on r. This is a preparation/evolution/
terminal-measurement model; unrestricted invasive instruments are not silently
included in the allowed operations.

The restricted effects are a physical premise of the example. If all hidden
orientation events became measurable, the operational state description
would instead distinguish the underlying probability measures.

## 2. Classical composites and local tomography

For n components take all joint probability measures on (S^2)^n. Allowed
measurements are products of local tests (1), their random mixtures and
coarse-grainings. Transformations are local rotations, permutations of
components and their random mixtures; preparations can be classically
correlated. These operations preserve the specified class exactly.

Put v(u)=(1,u). All observable probabilities depend on the tensor

$$z=\int v(u_1)\otimes\cdots\otimes v(u_n)\,d\mu. \tag{2}$$

Products of local effects span the tensor coordinates, so they determine z.
The operational composite is the convex hull of product ball states, the
minimal state tensor product. It has unnormalized linear dimension 4^n.
Here tensor coordinates are merely moments of classical random variables.

The distinguishability capacity is exactly 2^n. For each product outcome,
its largest probability is bounded by 2^n times its value at the product
of zero vectors, since each local factor is at most twice its constant term.
This bound survives mixing and coarse-graining. If one test distinguishes k
states, each successful effect has value at least 2^{-n} at that reference
state; normalization gives k<=2^n. Products of opposite-pole tests attain
2^n. Thus both capacity and linear dimension multiply under composition.

## 3. Where purification fails

Every pure state of this composite is a product of pure local states.
Indeed the product-pure set is compact in finite-dimensional tensor space,
and its convex hull is (2). Every point has a finite convex representation;
an extreme point must itself be a product-pure point. Such points are extreme
because a pure unit-vector marginal forces that local orientation with
probability one, successively for every component.

Every marginal of a pure composite is therefore pure. The mixed local state
r=0, for example, has no purification by any number of these components.
CDP's existence clause already fails, before essential uniqueness is tested.
This makes the missing resource the allowed pure composite states, rather
than the continuity of local reversible motion.

## 4. An explicit failure of Hardy's subspace requirement

Consider two components and measure each along a fixed unit axis n. Coarse-
grain to the event that the two signs agree. Its hidden response is

$$e_{\rm same}(u,v)=\tfrac12[1+(n\cdot u)(n\cdot v)]. \tag{3}$$

A preparation supported on this event with probability one must have
(n dot u)(n dot v)=1 almost surely. Since both factors lie in [-1,1], the
only hidden configurations are (n,n) and (-n,-n). The resulting operational
face is a line segment with two pure states and capacity two. The full
two-component system has four perfectly distinguishable pole configurations;
this face retains two of them and excludes the other two exactly.

An elementary capacity-two system in section 1 is a three-dimensional ball,
not this segment. Consequently this constrained subsystem does not behave
like that elementary system: Hardy's subspace axiom fails. The example can
satisfy local continuity and multiplicative capacity/dimension while failing
another essential member of the axiom package. It challenges neither complete
reconstruction theorem.

## 5. Decision and action-scale boundary

Retain finite operational closure as a useful requirement, but reject it
together with local reversible continuity as a sufficient selector of quantum
composition. The decisive next quantum premise concerns which globally pure
states and subspaces must be physically available. The example's measurement
restriction is explicit and still needs physical motivation; adding a
classical hidden apparatus without changing the allowed operational composites
does not supply purification.

All rotations can be parametrized by a chosen classical clock without an
action unit in (1)–(3). The model establishes no action floor. The remaining
quantum task is to justify a composite/subspace principle independently of
the intended answer, followed separately by the mechanical phase/action map.
Additional single-system continuity examples would leave that decision
unchanged and are parked.
