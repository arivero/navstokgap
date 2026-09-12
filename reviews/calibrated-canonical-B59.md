# R28 review: both canonical coordinates remain ambiguous

C112–C113 are accepted as checked derivations for the fixed pulse design in
[R28](../notes/calibrated-canonical-ambiguity.md), 2026-09-12.

1. R25's apparatus inverse applies about eta_c, whose calibrated displacement
   lies within b/4 of the original box centre. The compensator differs from
   eta_c by O(lambda times receiver displacement), leaving a b/2 boundary
   margin on the chosen compact receiver neighbourhood at small coupling.
2. Integrating the exact probe equations gives the t-weighted first-pulse
   functional with coefficient -K/M_1 in the calibration residual. The clock
   impulse has sign -lambda Kc integral f'_1 x. Matching its final momentum
   and taking initial energy variation v_0 delta p_s gives -Kc integral h xdot
   after integration by parts. Other free probe positions and all probe
   momenta vanish at eta_c; they supply no first-order energy term. Receiver
   and clock reactions affect the next order, not these coefficients.
3. Both numerators vanish identically at lambda=0 for every w. Their integral
   coupling-derivative formulas prove joint smoothness, rather than merely a
   pointwise limit. A small signed coupling neighbourhood is an analytic
   extension; admitted physical couplings remain positive.
4. At a small fixed positive tau the backward free internal displacement has
   x=gY tau squared/(2mu)+O(tau fourth) and P=-gY tau+O(tau cubed). This checks
   both signs and nonzero canonical components directly from the receiver
   generator. Narrow positive smooth pulses preserve rank and a nearby kernel
   vector. The width is fixed before weak coupling. R06's explicit four-row
   observability argument allows three further disjoint pulses retaining the
   original signal rank. The conclusion is existential in pulse design.
5. On the two-dimensional kernel plane, the positive receiver quadratic form
   supplies a shell point energy-orthogonal to the canonical kernel direction.
   The energy derivative is independent of the two pulse rows because it
   evaluates to 2E on that shell point. Adding ell(v)=1 gives an invertible
   four-row derivative. The note now states the augmented map and a uniform
   inverse-derivative perturbation bound of 1/2, including its self-map radius.
6. Compactness and joint smoothness preserve box, cutoff, positive-speed and
   endpoint margins and canonical derivative signs on one fixed rectangle.
   Integration gives actual finite endpoint separations in both coordinates;
   all ten final apparatus records and both initial energies agree exactly.
   The deterministic triangle inequality yields each half-separation bound
   and their action-valued product. No projected area or exact minimax constant
   follows from this curve construction.

[B59](../references/batches/B59.md) separates the inherited analytic methods
from these model calculations. Coordinator checked Freire's primary pp. 1–3:
p. 1 states the smooth inverse theorem; pp. 2–3 give the self-map and strict
Lipschitz perturbation mechanism. The worker's flagged joint regularity,
observability, margin and uniform-sign obligations are discharged above and
in the revised note. One Luna-low worker, no descendants. No numerical or
symbolic verification scripts ran. Novelty remains unassessed.
