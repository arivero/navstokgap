# B58: calibrated-displacement ambiguity source companion

## Result and bounded coverage

The Borsuk–Ulam theorem is directly verified in a Princeton University course
source: every continuous map `f:S^n -> R^n` has an `x` with `f(x)=f(-x)`.
This exactly supports the topological step (3)–(4) of R27 for `n=10`, once
`Psi` is a continuous chart and the complete record map is continuous. The
theorem supplies existence of an equal-record antipodal pair; it supplies no
mechanical dynamics, energy-shell chart, derivative estimate, receiver-state
separation, or risk bound. Those remain model-derived and conditional on R25's
uniform flow estimates and the displayed R27 margin assumptions.

## Primary source

Sanjeev Arora (lecturer), Nir Ailon and Iannis Tourlakis (scribes), Princeton
University, *Lecture 13: Topological Non-Constructive Methods*, COS 598B
(Spring 2002), PDF p. 1. Evidence level: passage. The definition of `S^n`
as the boundary of the unit ball and its antipodal operation appear at PDF p.
1, lines 5–9 in the text extraction; Theorem 1 states:
“For every continuous map `f : S^n -> R^n`, there exists `x in S^n` such that
`f(x)=f(-x)`.” The same page explicitly identifies `x` and `-x` as antipodal
points. The source also gives the equivalent odd-map-zero formulation (p. 1,
lines 18–23), but R27 needs the equal-image formulation directly.

URL: https://www.cs.princeton.edu/courses/archive/spr05/cos598B/lec13.pdf

## Audit of the R27 application

With the stated eleven free chart coordinates, a radius-`r` parameter sphere is
`S^10`; composing the chart with the ten-component final record map gives a
continuous `S^10 -> R^10` map. Thus Borsuk–Ulam yields an exact common record,
not merely a rank-loss or infinitesimal coincidence. The calibrated coordinate
`q_1=c` is fixed in the chart, so antipodality acts on parameters and does not
invoke the rejected physical sign involution.

The separation and risk conclusions require separate checking. In particular,
the estimate `||D_eta F_lambda-I|| <= C lambda` and receiver derivative bound
must be established uniformly on the unconstrained convex box from R25; they
are not consequences of Borsuk–Ulam. The chart's solved energy coordinates are
nonlinear, so the lower bound from the eleven free-coordinate projection should
be stated as an inequality justified by those coordinates being components of
the full initial state, with fixed scaling. The resulting positive risk is a
full receiver-state Euclidean risk; the theorem does not force separation in
both `x` and `P`, and it does not imply an action scale or canonical error
product.

## Source-to-model suggestion

Retain Borsuk–Ulam only for the exact common-record existence step. For R28,
add a separate argument or constraint forcing the equal-record pair to differ
in both measured canonical coordinates; test whether the uniform derivative
estimate and chart margins survive that restriction.

Coverage: one web search query and two source opens (Princeton PDF plus a
Chicago-hosted corroborating exposition), with the theorem passage read; no
full-source read and no broad novelty search. Exact prior-art coverage and
novelty are unassessed.
