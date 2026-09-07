# B10 review: collision action relaxation

## Verdict

The three draft claims are mathematically sound for the explicitly stated
refreshed iid bath: B10 can be accepted as a proof/source-audited derivation,
with C022 and C023 labelled derived consequences rather than imported
theorems, and C024 labelled a model counterexample to universality. The
literature contains an exact affine-map/constant-rate model match and an exact
Maxwell-kernel lag-covariance specialization, but no selected source derives
the full preparation-time relaxation or the bath-scaling countermodel.

## Proof and assumption audit

1. **Collision map and bounds.** With `m` the tracer mass and `M` the bath
   mass, `a=(m-M)/(m+M)` and `b=2M/(m+M)`. For `m>=M>0`, `0<=a<1`, `b=1-a`,
   so `V'=aV+bW` is a convex update. Direct expansion verifies momentum and
   kinetic-energy conservation. The bath departure bound in the draft,
   `|W'| <= (3m-M)w/(m+M) < 3w`, is correct. It is only a reservoir-frame
   speed statement, not a relativistic invariant.
2. **Invariant law and uniqueness.** The series
   `b sum_{j>=0} a^j W_j` converges absolutely and remains in `[-w,w]`.
   Coupling with a common Poisson clock and bath gives difference `a^{N_t}`;
   its mean is `exp[-nu(1-a)t]`. This proves uniqueness of the invariant law
   on the bounded interval, including `a=0` (one collision erases the state).
   No detailed balance is used.
3. **Moments and lag covariance.** Independence and centering give
   `S*=b^2 s^2/(1-a^2)=M s^2/m`; conditioning on the future bath gives
   `E[V(t+r)|V(t)]=exp(-gamma r)V(t)`, hence the stationary covariance. The
   double integral for displacement and `H*=(m+M)s^2/nu` follow with the
   correct action units.
4. **Preparation-time relaxation.** The generator identities
   `Lv=-gamma v` and `L(v^2)=-beta v^2+nu b^2 s^2` give
   `S(t)=S*+(S0-S*)exp(-beta t)`. Since the future conditional mean is linear,
   the integrated lag covariance is exactly `2mS(t)/gamma`. The centered
   initial law is required for the displayed closed variance ODE. The
   conditional-covariance identity itself remains valid with nonzero mean.
5. **Finite window.** The formula in Eq. (window) follows by ordering the two
   time variables. It has the stated small-window and long-window limits. At
   fixed `Delta`, the approach to stationarity is proportional to
   `exp(-beta t)` (with a Delta-dependent coefficient), so “at rate beta” is
   correct but not a uniform-in-Delta assertion.
6. **Scaling countermodel.** Replacing each bath velocity by `epsilon W`,
   `0<epsilon<=1`, preserves all stated stochastic and collision premises and
   scales every variance/action quantity by `epsilon^2`. This disproves
   universality from those premises alone; it does not disprove universality
   after an independently specified spatial encounter law or thermodynamic
   constraint.

## Literature comparison

- Barkai, arXiv:cond-mat/0303255v1, pp. 1, 4–5: exact elastic affine map,
  unchanged bath, molecular chaos, uniform rate and Poisson collision count.
- Barbier--Trizac, arXiv:1203.6759v3, pp. 1, 19: stationary covariance and
  Green–Kubo integral; for Maxwell kernel, exponential lag decay. Their model
  may have acceleration and velocity-dependent collision kernels, so only the
  field-free `nu=0` specialization transfers.
- Ben-Naim--Krapivsky, arXiv:cond-mat/0301238v1, pp. 1, 6: contrast showing
  that a changing collision clock produces aging/algebraic physical-time
  correlations even when collision-number decay is exponential.

Exact source matches are confined to the model ingredients above. The affine
stationary law, moment constants, finite-window expression and rescaling
countermodel are elementary derivations under B10's added bounded/refreshed
assumptions.

## Checks and unresolved obligation

`python scripts/collision_action_checks.py` passes all 15 symbolic identities.
Rendered-page checks covered the affine map/master equation (Barkai p. 4),
the autocorrelation equations (Ben-Naim--Krapivsky p. 6), and the integrated
Maxwell covariance (Barbier--Trizac p. 19). The remaining bounded task is to
derive a spatial encounter rate, including its relative-speed incoming bias,
and retest whether it supplies a mass/rate universality condition.

## Coordinator integration

All three PDF hashes and version watermarks were checked. Barkai (2) is on
p. 3, added by the coordinator; (3)–(8) are on p. 4 and (9)–(12) on p. 5.
Barbier–Trizac's verified p. 19 contains (89)–(98). The worker read seven
pages, with eight pages of combined coverage. Formula images were checked
independently and all 15 identities pass. The user's renewed cut-point focus
makes this a supporting diagnostic; A03 now precedes the spatial-clock task.
