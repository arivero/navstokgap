# R13/B44 written proof and source review

C082–C083 are accepted as derived consequences in the stated bounded-force,
known-initial-state, complete bounded-error record model. Literature novelty
remains unassessed. Review date: 2026-09-11.

## Mathematical acceptance

The central-fibre minimax proof applies to the weak-star compact force ball
intersected with closed pointwise position constraints. Scaling maps it to
zero initial position/velocity, unit acceleration and unit position band.
The rearrangement lower bound on endpoint position at fixed velocity uses
only the acceleration integral and decreasing time weight. Combining it with
v<=s and the final-v-interval position-band inequality gives the three-branch
lower envelope of upper bounds. The negative/positive bang path stays inside the full strip:
its minimum is -h^2, with h increasing from zero to one on the transient.
The constant-force and delayed prepared paths cover both remaining regimes.
Junction values match at sqrt(2) and 4. All extremizers attain the separate
position bound too, justifying the blind-delay support sum, rather than
assuming arbitrary phase-radius products are attainable jointly.

R12's product theorem and proportional force/error lift require no long-time
assumption. Substituting finite-horizon radii is therefore valid. The position
loss criterion follows from the exact difference of a minimum of sums and a
sum of minima, including equality cases. For the example, aggregate squared
scaled time is 17/2 and momentum factor squared is 34; multiplying gives
sqrt(714)-17. Since 714>26^2, aggregate momentum exceeds 9 in the chosen
units. The early action product and fixed-T precision limit have correct
action units. No computational numerical or symbolic verification was used.

## Source acceptance

One sequential gpt-5.6-luna worker at low effort supplied B44. Coordinator
then read the two primary sources at the named passages. Corrected Johnson's
author metadata, the source's already-zero initial pair, and the distinction
between its future-supremum risk and R13's fixed horizon. The 2 sqrt(N/L)
differencing interval is not the 4 sqrt(N/L) preparation horizon. B44 records
four selected passages when the lemma and theorem are counted separately;
exact search strings were not saved. Johnson's abstract is context only.
No precise transient or composition theorem match was obtained in this bounded
coverage. The preserved worker handoff is followed by the coordinator-corrected
[source companion](../docs/batches/B44/finite-horizon-source-companion.md).

Next: R14's explicitly shared two-constituent apparatus error constraint.
