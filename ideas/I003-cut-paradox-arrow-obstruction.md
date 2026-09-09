# I003: the cut paradox, the arrow, and an obstruction to refining time and position together

Status: user-originated heuristic, recorded 2026-09-08 from three remarks made
during the H08 source session. Sources are collected in
[`docs/classics/`](../docs/classics/README.md) under batch H08.

## The remarks

1. Zeno's arrow looks like the Wick-rotated version of Democritus's cone: the
   cone asks whether adjacent spatial sections are equal or unequal, the arrow
   asks whether adjacent instants carry equal or unequal states of motion.
2. Somewhere deep there is an obstruction that does not allow mapping time to
   positions indefinitely as a double limit, and that forces the existence of a
   minimum action $h$.
3. Or at least of an $h$ that controls the convergence.

## What the repository already contains on each

- The cone: C032 proves that a position-only law with ballistic support and
  independent stationary increments is deterministic drift, so adjacent
  sections of such a law are equal; the P01 review keeps this as a modern
  analogy rather than a reception claim. The ancient answers are Chrysippus's
  “neither equal nor unequal” (Plutarch), the Mohist endpoint at which halving
  stops, Liu Hui's cutting until it cannot be cut, and the kalām atom.
- The arrow: Aristotle's diagnosis is that time is taken to be composed of
  nows (Physics VI.9). The C033 bridge has a midpoint atom, a state in which
  the body is exactly where its one-switch path puts it, and the finite-speed
  bridge retains velocity at every cut; al-Naẓẓām's leap is the discrete
  crossing of a divisible interval.
- The double limit: C021 shows that the mass-weighted second-moment coefficient
  has different iterated limits, rate first or duration first, and the
  crossover $\Delta_*=K/(mu^2)$ of the P02 note shows that a window-independent
  coefficient cannot exist below $\Delta_*$ at finite speed. Jacobson and
  Schulman's passage from $\Delta x\sim\Delta t$ to $(\Delta x)^2\sim\Delta t$
  (B15) is the same double limit in the checkerboard.

## The proposed reading

**Review, 2026-09-09:** retain the following as the originating heuristic.
The repaired [matrix note](../notes/i003-double-limit-rigidity.md) separates
finite propagation, probability conservation, a two-state commutator identity
and a specified resolution-noise model. Commuting random velocities can have
ballistic variance; positivity of evolution alone allows killing. R02 owns
the remaining theorem/source audit. The user's three remarks above are preserved.

The continuation that turns the telegraph process into the Dirac checkerboard
(A09) exchanges a Euclidean cut question for a Lorentzian one. Under it, the
cone dilemma about equal sections and the arrow dilemma about equal instants
are the same question. The obstruction in remark 2 is then the statement that
refining cuts in time and resolving positions cannot both be taken to zero
while a nonzero action coefficient survives; at finite speed the coefficient
vanishes below the crossover window, and the surviving constant is the plateau
above it. Remark 3 is the weaker and presently provable form: the coefficient
controls the rate at which the bridge's midpoint variance and the window
observable approach their limits, as in the cubic onset $H_*z^3/6$.

## Tests

Status 2026-09-08: test 1 is drafted in
[`notes/cut-paradox-two-faces.md`](../notes/cut-paradox-two-faces.md) with nine
checks. Tests 2 and 3, and the general form of test 1, are drafted in
[`notes/i003-double-limit-rigidity.md`](../notes/i003-double-limit-rigidity.md):
light-cone rigidity to first-order systems, the commutator scale, and the
rounding-model double limit; test 4 is listed there as prior art to audit.

1. State both paradoxes as restriction-consistency questions: adjacent
   sections of a solid under a slicing law, adjacent instants of a motion under
   a cut law. Check whether C032 and the C033 midpoint atom are the two
   Euclidean and Lorentzian faces of one statement under $\lambda\to i\omega$.
2. Formalize “mapping time to positions as a double limit”: mesh
   $|\pi|\to0$ and spatial resolution $\varepsilon\to0$ for a refinement
   law with speed bound $u$. Identify the obstruction with $\Delta_*$ and
   test whether it survives when the speed bound is removed (the Gaussian
   family admits the double limit, so finite speed is the source).
3. Decide between remark 2 and remark 3: positivity of the surviving
   coefficient needs the A08 composition premise and a nonzero-variance
   premise; convergence control needs only the plateau. Record which premises
   each version uses.
4. Prior-art audit: the ancient and medieval sources in H08, then the modern
   literature on the arrow and quantum measurement, before any claim ID.

Related: [I001](I001-action-field.md), [I002](I002-newton-polygon-threshold.md),
the [cut-point target](../research/CUT_POINT_TARGET.md) and the
[six-direction checks](../notes/composition-crossover-gap-checks.md).
