# Two ways to exclude a classical operational model

Hardy and Chiribella–D'Ariano–Perinotti (CDP) identify different extra
premises: reversible connectivity of pure states, and purification of mixed
states. Their classical alternatives are operational probability models.
Applying either reconstruction to mechanics first requires specifying which
preparations, transformations and measurements constitute a closed system
description. A dimensional action parameter then needs a dynamical bridge.

Q01 first milestone, 2026-09-13. This is a dependency audit of selected primary
passages, with source coverage in [B67](../references/batches/B67.md).
The full reconstruction proofs remain outside this milestone.

## Premise-to-use map

| Dependency | Hardy, version 4 | CDP, version 3 |
| --- | --- | --- |
| Operational class used here | Finite distinguishability capacity N and finite probability-coordinate count K; preparations, measurements, reversible transformations and composition | Finite-dimensional state/effect spaces defined through operational statistics; tests, transformations and composites |
| Additional premise | Any two pure states admit a continuous reversible connection within the system | Every state has a pure extension; fixed purifying systems give uniqueness up to their reversible transformations |
| Classical failure | A finite simplex has isolated pure states and reversible permutations | Pure states of the standard classical composite are products, whose marginals remain pure |
| Other assumptions retained | Probability, simplicity, subspace and composition axioms | Causality, perfect distinguishability, ideal compression, local distinguishability and pure conditioning |
| Action step | Match transformations to physical time, energy and mechanical action | The same dimensional identification is needed after state/composite reconstruction |

Hardy §1 states the axiom package; §§4 and 7 explain the classical failure.
CDP §II specifies finite statistical dimension, and §§III.1–III.2 locate the
classical-compatible principles and purification. These are conditional
reconstructions, not assumptions already supplied by the receiver model.
[Hardy](https://arxiv.org/html/quant-ph/0101012v4),
[CDP](https://arxiv.org/html/1011.6451v3).

## What the classical alternatives actually fail

For the finite simplex, a reversible affine map permutes its vertices. A
continuous path starting at one vertex cannot reach a different vertex while
remaining in that finite set. This is the elementary content of Hardy's
classical exclusion; the rest of his axiom package matters for selecting the
quantum alternative rather than merely rejecting the simplex.

For a classical joint probability table, a pure normalized state is concentrated
at one pair of labels. Summing over either label still gives a concentrated
state. A mixed marginal therefore has no pure classical extension. Already
the existence clause of purification fails; uniqueness adds an independent
requirement to the reconstruction. A correlated classical ensemble can encode
ignorance, but remains mixed globally. These are the standard elementary
classical comparisons identified in the source passages, not new no-go theorems.

## The Newtonian connection is closure during a transformation

Hardy §7 explicitly motivates continuity with a ball moving between the two
boxes representing a bit. Its intermediate positions exceed the two-state
description. This supports a more precise question than whether classical
motion is continuous: can the operational description be finite-capacity,
exact and closed under the entire reversible transformation?

Project inference: ordinary phase-space motion and a finite bit description
operate at different descriptive levels. A proposed classical derivation must
justify its measurement restrictions and transformation closure together.
Suppressing intermediate distinctions by coarse-graining alone does not prove
that the resulting transformations are reversible on the reduced states.
Likewise, calling a global mechanical microstate definite does not establish
CDP's operational pure extension of a locally mixed preparation. Its allowed
effects, composition and operational equivalence must be specified.

This preserves the useful physical motivation in Hardy while keeping the
ambient-model dependency visible. The paper's countably infinite extension is
not audited here; this finite-simplex comparison is not a rejection of every
continuous classical phase-space theory.

## What would supply the action unit?

The selected axioms concern probabilities, distinguishability, composition
and transformations. The outstanding project step is to relate their
transformation parameters to measured mechanical time and energy, and then
to a phase accumulated per unit action. The checkerboard model supplies this
relation through its chosen K, amplitudes and measurement rule; see
[the maintained comparison](checkerboard-dynamics.md). This audit identifies
that input rather than deriving a positive value or universal lower bound.

## Strategic consequence

Retain both reconstruction packages as candidate premises. The next quantum
decision is whether an independently motivated operational closure/composition
principle forces one of them for the admitted mechanical class. K01 is useful
only if its context/measurement assumptions decide that question. Further
receiver calibration coefficients do not currently resolve it.

The bounded Q01 passage milestone is complete. Under the current strategy,
G03's interacting size-uniform gap test is selected next; the deeper Q01
closure test remains an explicit eligible follow-up, not an automatic proof
audit of both papers.
