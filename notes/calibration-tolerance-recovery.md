# Calibration tolerance sets the recovery crossover

On R30's same fixed apparatus box, receiver reconstruction errors are bounded
by a constant times (final-record error + calibration error)/coupling. With
exact final records this rate has a matching canonical lower bound, up to
fixed constants. At any fixed positive calibration tolerance, sufficiently
weak coupling makes one complete record compatible with the entire bounded
receiver domain. The coordinate minimax risks then equal their no-record values.

R31, 2026-09-12. Retain [R30](three-calibration-global-recovery.md)'s fixed
nonzero c, pulses, small positive apparatus box about eta_c and receiver ball
Z={H_s<=E_max}, E_max>0. All norms are its fixed component norms; calibration
outputs C=(q_1,q_2,q_3,H_app) use fixed length and energy units. Instead of
imposing C=C_* exactly, supply a reported vector C_obs with
||C(eta)-C_obs||<=epsilon. Final record error is bounded by delta. These
are deterministic support bounds, not stochastic variance assumptions.
The physical unknowns range over the original box times Z, and initial pulse
couplings vanish. Source coverage is in [B62](../references/batches/B62.md).

## 1. A two-data inverse estimate

Use R30's inverse apparatus chart eta_lambda(w,a), a=S^{-1}Y, and
D_lambda=[C(eta_lambda(w,a))-C(a)]/lambda. Its uniform receiver inverse
margin holds independently of whether the supplied constraints are exact.
For two initial preparations write C_1=C(eta), C_2=C(eta'), with records Y,Y'.
Insert their actual constraints into the R30 comparison to obtain

$$\|w-w'\|\le 2\|L^{-1}\|
\left[\frac{\|C_1-C_2\|}{\lambda}
 +(M_C/\lambda+M_D)\|S^{-1}\|\|Y-Y'\|\right]
\le\frac K\lambda(\|C_1-C_2\|+\|Y-Y'\|). \tag{1}$$

K is fixed over the bounded preparation and small coupling interval. Thus
calibration precision and final-record precision are separate data resources,
both amplified by the same sufficient inverse estimate.

Choose any preparation in the compact box times Z consistent with both
reported error bounds. It exists because the true preparation is consistent;
a deterministic choice can be made by sequential coordinate minimization
on this compact feasible set. Comparing it with the true preparation gives

$$\|\widehat w-w\|\le\frac{2K}{\lambda}(\epsilon+\delta),\qquad
\epsilon_x\epsilon_P\le4L_*P_*K^2
                    ((\epsilon+\delta)/\lambda)^2. \tag{2}$$

At fixed positive coupling both precisions tending to zero suffice. A joint
weak-coupling limit is controlled when (epsilon+delta)/lambda tends to zero.
The bound also applies componentwise with epsilon the largest of four
calibration tolerances. The lower construction below permits the same positive
epsilon in each component; setting some tolerances exactly zero is a different
preparation restriction.

## 2. An exact common-record ball within the tolerance

Take nominal receiver w=0 and nominal apparatus eta_c, and let
Y_lambda=G_lambda(0,eta_c), C_obs=C(eta_c)=C_*.
R25's preconditioned contraction on R30's enlarged chart gives a smooth
compensator for every w in Z, with

$$G_\lambda(w,\eta_\lambda(w))=Y_\lambda,\qquad
\|\eta_\lambda(w)-\eta_c\|\le B\lambda\|w\|. \tag{3}$$

For completeness, differentiate the chart identity at fixed a:

$$D_w\eta_\lambda=-(D_\eta F_\lambda)^{-1}D_wF_\lambda.$$

The inverse norm is at most 2 and ||D_wF_lambda||<=L lambda on the
enlarged chart. At a=S^{-1}Y_lambda the chart takes w=0 to eta_c.
Integrating along the segment from 0 to w proves (3) with B=2L;
this argument does not require the nominal apparatus displacement to vanish.

Let R_Z=max_Z||w||>0 and M bound ||DC|| on the apparatus chart, increasing
M if necessary so M>0. Reduce the fixed coupling ceiling until
B lambda_* R_Z <= rho/2, with rho the unchanged R30 preparation half-width.
The full compensator then stays inside that box with half its margin.
Reduce the ceiling also to keep the actual first displacement bounded away
from zero, for example within half the fixed nominal |c| in its units.

For

$$t=\min\{1,\epsilon/(MB\lambda R_Z)\}, \tag{4}$$

every w in tZ satisfies

$$\|C(\eta_\lambda(w))-C_*\|\le MB\lambda\|w\|\le\epsilon.$$

These are exact full final records, with the same reported calibrations and
apparatus energy. The receiver domain is a ball, so its dilation tZ remains
admissible; no exact receiver energy was supplied in R30. Complete nonlinear
reaction and free apparatus drift are included in (3). The compensating
correlations select points from the admitted product domain; no prior
correlation restriction or probability distribution is imposed.

## 3. Canonical minimax bounds and exact saturation

For an estimator of (x,P) from (Y_obs,C_obs), define epsilon_x and epsilon_P
as its separate worst-case absolute errors over all initial states in the
fixed product domain and all reported data satisfying the error bounds.
R_x and R_P are the respective infima over estimators. The optimal product
below is the infimum of epsilon_x epsilon_P over joint canonical estimators;
the same constructions attain both asserted coordinate upper bounds.

Completing the receiver energy square, put k_x=a-g^2/d>0 and

$$X_E=\sqrt{2E_{\max}/k_x},\qquad P_E=\sqrt{2\mu E_{\max}}.$$

The canonical projection of Z is k_x x^2+P^2/mu<=2E_max. Its dilated copy
tZ in the common record has coordinate extrema +/-tX_E and +/-tP_E.
Consequently every global estimator has

$$\epsilon_x\ge tX_E,\quad\epsilon_P\ge tP_E,\quad
\epsilon_x\epsilon_P\ge t^2X_EP_E. \tag{5}$$

For exact final records, (2), together with the constant-zero estimator and
coordinatewise selection of the better guaranteed estimate, bounds the
optimal coordinate risks above by
min(X_E,2L_*K epsilon/lambda) and min(P_E,2P_*K epsilon/lambda).
Thus on this fixed class the optimal canonical risk product has order

$$\min\{1,(\epsilon/\lambda)^2\}, \tag{6}$$

up to positive constants with action units that depend on the fixed apparatus
and energy bound. This comparison concerns epsilon>0 and 0<lambda<=lambda_*;
at epsilon=0 and exact final records R30 gives zero risk.

If epsilon>=MB lambda R_Z, then t=1 and the constant-zero estimator attains
both lower bounds exactly. The minimax coordinate risks and optimal product are

$$R_x=X_E,\qquad R_P=P_E,\qquad
\inf_{(\widehat x,\widehat P)}\epsilon_x\epsilon_P
=X_EP_E=2E_{\max}\sqrt{\mu/k_x}. \tag{7}$$

The canonical projection of this one compatible receiver set is then the full
ellipse, of area pi X_E P_E. Both area and product have action units; their
different factors reflect different observables. The displayed threshold is
sufficient for saturation, not a claimed sharp transition constant.

## 4. Meaning and next test

Finite calibration tolerance restores a genuine identical-record ambiguity,
not merely an ill-conditioned reconstruction formula. Weak coupling hides
the receiver once its signal lies within the allowed initial calibration
variation. The limiting risk is set by E_max and mechanical parameters; it
is not a universal positive action scale. At fixed coupling improved supplied
precision still closes the product.

R32 should test whether four calibration tolerances are equivalent resources:
keep q_1,q_2,q_3 exact and allow only apparatus-energy tolerance, then exchange
which single constraint is uncertain. Identify actual canonical fibres, since
the max-tolerance upper bound alone cannot decide their geometry.
