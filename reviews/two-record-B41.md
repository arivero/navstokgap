# R10/B41: two-record proof and prior-art review

C076–C077 are accepted as mechanical consequences of bounded-error
differentiation, 2026-09-10. The core finite-difference inequality and optimized
equal-error constants are established prior art, explicitly matched in
Seeber–Haimovich v2 §4. The [B41 audit](../references/batches/B41.md) records
worker coverage and the coordinator's additional reading separately.

## Written proof checks

1. Propagate/intersect twice gives exactly the jointly compatible phase set
   because the force class concatenates freely. Empty records are excluded.
2. Backwards integration gives the positive weight $(s-t_1)/\delta$ and
   its integral $\delta/2$. Noise enters as $m(e_2-e_1)/\delta$.
3. The adverse signs $e_1=+\varepsilon_1,e_2=-\varepsilon_2$, and positive
   force on both final intervals attain both terminal error bounds together.
   Any earlier allowed force supplies a trajectory with the prescribed initial
   state; the claimed worst case varies records as well as motions.
4. A conditional compatible set lies inside the displayed error rectangle.
   The area upper bound is four times the half-width product, not that product
   itself. Neither is a positive lower bound for all possible estimators.
5. Equal-error balancing gives the stated optimum only when timing permits.
   Substitution of $b=\delta_*$ yields $4\sqrt{mF\varepsilon}$ and
   $7\varepsilon$; the two sample times fit a fixed horizon for sufficiently
   small error. Both coordinates, their diameters and action product close.

All verification is written algebra and proof review. Records are an ideal
information interface, not a completed bounded-resource apparatus. The next
lower-bound problem must preserve the shared initial state and accessible
records when constructing indistinguishable alternatives.

## Source review

One sequential Luna-low worker used two queries and three passage selections.
Coordinator verified arXiv v2 metadata and HTML: signal/noise definitions,
the §6.2 lower-bound statements, and an additional §4 reading. Lemma 4.3
contains the equal-error estimate with the same constants; Theorem 4.1 gives
its optimized timing. This upgrades the worker's scaling-level match to an
exact prior-art match. No source formula was imported from a PDF image.

Corrected the companion's $v''$ typo to $q''$ and supplied a versioned full-text
URL instead of an abstract link labelled HTML. Proposition 6.5's quasi-exactness
condition prevents importing its stronger constant into our fixed-difference
problem. R11 must prove the appropriate lower bound for its own information class.
