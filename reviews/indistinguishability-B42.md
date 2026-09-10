# R11/B42: connecting reachability to minimax recovery

C078–C079 are accepted by written proof review, 2026-09-10. The central-fibre
principle is a self-contained scalar optimal-recovery lemma; the explicit
prepared force pair is the Seeber–Haimovich Proposition 3.1 construction in
mechanical units. See [B42](../references/batches/B42.md) for bounded coverage.

## Proof checks

1. Convexity and central symmetry put the half-difference of any two compatible
   inputs back in the admissible set. Their observation difference lies in
   twice the error box. A scalar compatible image is a closed interval; its
   midpoint gives the upper bound. The symmetric central pair proves equality.
2. Integral images of the bounded-force ball are compact in the weak-star
   topology. Each continuous-history constraint is closed; their intersection
   remains compact. The result is scalar: simultaneous coordinate midpoints
   need not themselves form a reachable state, which the theorem does not require.
3. Two half-pulses prepare displacement $-Fd^2/(4m)=-\varepsilon$ and zero
   velocity. Positive force for time $d$ then reaches $+\varepsilon$ and
   momentum $Fd$. The preparation is monotone and the entire observed path
   stays in the error band. Both signs share the prescribed initial state.
4. Continuing opposite forces through delay $b$ adds $Fb$ to the momentum
   half-separation and $Fdb/m+Fb^2/(2m)$ to position. R10's bounds match both
   exactly. The time condition ensures the preparation starts after time zero.
5. The product concerns coordinate minimax risks, not a pathwise uncertainty
   product. Refining the same bounded-noise history cannot distinguish the
   pair. Precision/delay closure and the pair's optional speed ceiling follow
   directly from the displayed expressions.

No numerical or symbolic scripts were used. The lower bound arises from
bounded but otherwise arbitrary record errors; statistically independent
noise or a recording apparatus would introduce different assumptions.

## Source corrections and synthesis

One sequential Luna-low worker returned three passages within its two-query
budget. Coordinator read Proposition 3.1 and (10)–(12): the source explicitly
uses $g_1\in\mathcal F_L^0$, and therefore already includes shared zero
initial data and the preparation arc. Corrected the worker's contrary claim
and its factor-of-two wording. The source establishes the zero-delay core;
the finite-horizon positioning and blind-delay phase risks follow here.

The useful connection is now operational: force reachability, noisy-record
indistinguishability and exact recovery bounds use one common experiment.
The next connection to A08 must compare the actual observables. A worst-case
radius is not a variance, so a covariance composition formula cannot be
transferred merely because both products have action units.
