# B42 source companion: minimax indistinguishability

## Source and coverage

Richard Seeber and Hernan Haimovich, “Optimal Robust Exact Differentiation via Linear Adaptive Techniques,” *Automatica* 148 (2023) 110725, arXiv:2111.12638v2 (2 August 2022), [arXiv HTML v2](https://arxiv.org/html/2111.12638v2).

Three primary passages were read (bounded B41 route): §3.1 Proposition 3.1 and proof (HTML lines 231–257); §4 Lemma 4.3 and proof (364–372); and §4 Theorem 4.1 plus proof (339–350, 374–379). This is **passage** coverage, not a full proof audit. Numerical simulation material was not used.

## Exact matches and limits

Proposition 3.1 constructs opposite admissible signal/noise decompositions with the same causal input and derivative separation `4 sqrt(NL)`, forcing error `2 sqrt(NL)`. Setting `L=F/m` and `N=eps` gives the B42 momentum error `2 sqrt(mF eps)`. Its proof explicitly uses zero initial position and derivative, including a preparation arc. R11's force sequence is that same construction in mechanical units, followed by a blind-delay extension.

Lemma 4.3 and Theorem 4.1 establish the sharp finite-difference expression `2N/T+LT/2` and its optimum `2 sqrt(NL)`. Thus the square-root scaling and constant are established prior art; B42's convex-fibre minimax theorem, midpoint rule, and double-integrator specialization remain derived results.

## Research connection

Central-fibre worst-case radii provide a composition language for adversarial records. They should be compared with, but not identified with, variance composition: a variance addition law supplies no worst-case radius without extra distributional and preparation assumptions.

Coverage is bounded, not exhaustive; no novelty claim is made.

Coordinator correction: the source's $g_1\in\mathcal F_L^0$ in (10)–(12)
already enforces the shared exact initial data. The initial worker assessment
missed this direct match. The force pair and its zero-delay constant are
established prior art. The general scalar central-fibre lemma has no direct
source match in this bounded batch; it has a self-contained proof and its
novelty remains unassessed. Requested worker gpt-5.6-luna, low effort;
effective settings not independently reported.
