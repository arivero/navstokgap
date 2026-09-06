# Technical continuation: where the maintained proofs live

The complete derivations are in
[`papers/action-gap-foundations.tex`](../papers/action-gap-foundations.tex),
with its [human-readable PDF](../out/papers/action-gap-foundations.pdf).
This note is a routing summary, not a second independently maintained proof.

- Propositions 1–2: the constant-force family and a general nonzero second
  variation give arbitrarily small absolute action differences.
- Section 3: Jacobi fields solve the linearized equations; arbitrary off-shell
  fluctuations need not. A normalized Dirichlet eigenvalue bound does not
  discretize action values.
- Section 4: the free quantum kernel tends to a delta in the short-time limit;
  its first correction is proportional to the second derivative of delta.
- Proposition 3: with specified quantum states, independent copy count $N$,
  equal priors and ideal binary measurements, the first-lobe action threshold is
  $2\hbar\arccos([4p(1-p)]^{1/(2N)})$. It vanishes as $N$ grows for fixed
  $1/2<p<1$, but the perfect-discrimination endpoint $p=1$ must be kept separate.
- Section 6: a free relativistic particle with fixed endpoints and a strict speed
  margin still has arbitrarily small positive action differences.

These are control/conditional results. They do not derive the quantum state space,
Born rule, positive $\hbar$, the physical implementation of a two-arm chord
comparison, or a mass gap. Algebra checks supplement the written proofs; no
formal certificate or novelty claim is made.
