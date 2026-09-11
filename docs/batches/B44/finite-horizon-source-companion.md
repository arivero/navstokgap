# B44 source companion: finite-horizon minimax phase recovery

## Scope and result

This is a bounded R13 librarian audit dated 2026-09-11. The audit asks whether
the exact known-initial-state finite-horizon radii in
`notes/finite-horizon-minimax.md` have a direct literature match: the scaled
momentum radius
\(V(s)=s\) for \(s\le\sqrt2\),
\(V(s)=\sqrt{2s^2+4}-s\) for \(\sqrt2\le s\le4\), and \(V(s)=2\) thereafter;
the position radius \(\min(s^2/2,1)\); and the blind-delay and composition
consequences. Coverage is bounded and does not establish novelty.

## Sources and exact coverage

1. Richard Seeber and Hernan Haimovich, “Optimal Robust Exact Differentiation
   via Linear Adaptive Techniques,” *Automatica* 148 (2023) 110725,
   arXiv:2111.12638v2 (2 August 2022), versioned HTML:
   https://arxiv.org/html/2111.12638v2 . Reused B42 source; the audit reread
   two named passages. **Passage 1 (proof-level):** §3.1, Proposition 3.1
   and its proof, HTML lines 231–257, constructs opposite bounded-curvature
   signals with a common admissible noisy record and gives the sharp long-time
   derivative lower bound. **Passage 2 (proof-level):** §4, Lemma 4.3 and
   Theorem 4.1 with proof, HTML lines 339–350 and 364–379, gives the matching
   finite-difference upper bound at its optimized differencing interval.
   These passages support the long-time pair and the record-limited value
   \(2\sqrt{mF\varepsilon}\), but do not state R13's three finite-horizon
   regimes law. The prepared pair itself already has zero initial position and velocity.

2. Stewart D. Johnson, “Computing Minimum Time Paths With Bounded
   Acceleration,” arXiv:1310.5905v1 (22 October 2013), metadata and abstract:
   https://arxiv.org/abs/1310.5905v1 . **Passage 3 (abstract-level):** the
   abstract states that bounded-acceleration trajectories with prescribed
   initial and terminal position/velocity are treated and reduced to a
   finite parameter search. This is a reachable-trajectory precedent, not a
   noisy-history minimax recovery theorem; no equation or proof in the paper
   was used to support an R13 formula.

## Findings and boundaries

No exact source match was found within the two-query budget for the piecewise
function \(V(s)\), the position radius, or the blind-delay formulas. The R13
piecewise law is therefore recorded as a derived consequence of the bounded
curvature central-fibre argument in the note. The bang-bang constructions,
the equality of the position and momentum extremizer, and the aggregate versus
constituent composition formulas are likewise model derivations. Seeber–
Haimovich supplies the established long-time pair and asymptotic sharp
derivative scale only. The acceleration-planning source supplies geometric
reachable-set context under a different endpoint/time-optimal objective.

The finite-horizon proof issue to preserve is the pathwise position strip
\(|x(t)|\le1\) over the whole observed interval, not merely the endpoint
constraint. Any literature comparison must also preserve known initial
position and velocity, continuous access to every noisy position record, and
the distinction between separate scalar minimax risks and their product.

## Source-to-model suggestion

Use bounded-acceleration reachable-set terminology to recast the central fibre
as a terminal slice of a path-constrained reachable tube. The decisive check
for R14 is whether a shared apparatus error constraint changes that tube from
the Cartesian product used in R12/R13; retain the bang-bang/path-strip proof
as the acceptance test rather than importing a time-optimal endpoint result.

## Coverage and limits

Two discovery queries, two primary sources, and four named passages were used
(including the two reread Seeber passages). Search snippets and the second
source's abstract were used only as bounded discovery/context evidence. No
exhaustive prior-art search or novelty assertion is justified. No numerical or
symbolic verification script was created or run.

## Coordinator corrections and verification

Verified the versioned differentiation HTML, Proposition 3.1 (10)–(12),
Theorem 4.1 (17), (19), and Lemma 4.3 (18). Proposition 3.1 constructs
the zero-initial-state pair at a later time; its risk uses a supremum over
future times. R13 proves the fixed-horizon transient separately. The optimal
differencing interval is 2 sqrt(N/L); preparation from zero takes 4 sqrt(N/L).
These times have different meanings.

The second source is by Stewart D. Johnson, not the worker's initial
O'Connor attribution; verified arXiv v1 metadata and abstract. It contributes
context only. Count the selected proposition/proof, lemma/proof, theorem/proof
and Johnson abstract as four passages across two sources. The worker grouped
the lemma and theorem together as one numbered entry. It reports two search
queries but did not save their exact strings, so search reproducibility is
limited. No additional coordinator search sweep was performed.
