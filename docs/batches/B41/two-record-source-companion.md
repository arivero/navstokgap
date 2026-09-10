# B41 source companion: two bounded-error position records

## Finding

Seeber–Haimovich provides a direct methodological precedent for R10's
precision/curvature competition and for R11's indistinguishable-trajectory
lower-bound strategy. Their result concerns causal signal differentiation;
R10 derives a mechanical two-position specialization and terminal phase-state
recovery. Estimator-specific worst-case attainment must remain separate from a
minimax statement with known initial state.

## Read coverage

- Richard Seeber and Hernan Haimovich, “Optimal Robust Exact Differentiation via
  Linear Adaptive Techniques,” *Automatica* 148 (2023) 110725,
  DOI [10.1016/j.automatica.2022.110725](https://doi.org/10.1016/j.automatica.2022.110725),
  [arXiv HTML](https://arxiv.org/abs/2111.12638).
- §2.1, lines 56–61: bounded second derivative and bounded measurable noise
  classes (**passage**).
- Definition 2.1, lines 70–78: causal dependence on the measured history
  (**passage**).
- §6.2, lines 585–595 and Proposition 6.5, lines 629–633: identical sampled
  records from pieced parabola arcs and a worst-case lower bound (**passage**).

Metadata and these passages were verified. Full proof audit and numerical
simulation were not undertaken.

## R10 connection

With `v=p/m=q'` and `|q''|<=F/m` almost everywhere,
the two-record finite difference has derivative error
`(eps1+eps2)/delta + F delta/(2m)`. Its equal-error optimum is proportional to
`sqrt(F eps/m)`; restoring momentum gives `2 sqrt(m F eps)`. The source's
§4 gives the same equal-error constants after unit conversion, as checked below.
The source treats available histories
and a generic noise amplitude, whereas R10 has exactly two position records and
known initial data.

## R11 connection and status

Use the source's alternating-parabola idea to build two force-bounded
trajectories with identical allowed records and shared initial state, then
apply the common-output/half-separation argument to terminal momentum. Matching
the resulting lower bound to R10's upper bound would establish minimax risk;
without that match, R10 remains only an exact worst case for its specified
finite-difference estimator. Literature status: established differentiation
precedent; R10/R11 mechanical specialization and any novelty remain
unassessed.

Search budget: two queries and three primary passages. No numerical or
symbolic verification was performed.

## Coordinator correction and exact match

Verified version: [arXiv v2, 2 August 2022](https://arxiv.org/html/2111.12638v2).
Section anchors control over the worker's extraction line numbers.
An additional coordinator reading of §4, Lemma 4.3 and Theorem 4.1, finds
the exact bound $2N/\delta+L\delta/2$, optimum $2\sqrt{N/L}$ and error
$2\sqrt{NL}$. Thus the constants as well as scaling are established prior art.
R10's mechanical units, unequal errors and delayed coordinate estimate are
derived consequences. Corrected the worker's velocity second derivative to
the position second derivative. Proposition 6.5 has a quasi-exactness premise;
its stronger bound is not a lower bound for every fixed finite difference.
