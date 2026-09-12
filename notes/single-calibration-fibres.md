# One uncertain calibration leaves an exact receiver curve

Keeping three supplied constraints exact and allowing the fourth to vary
leaves a one-dimensional common-record receiver family. Its leading direction
is the corresponding column of the inverse calibration-response matrix.
Thus the location of the uncertainty matters: its canonical effects are read
from that column, rather than from the number of missing constraints.

R32, completed with an explicit pulse subfamily, 2026-09-12. Retain R30's fixed pulse design, nonzero c,
small fixed apparatus box, full exact final record and receiver energy ball
Z={H_s<=E_max}, E_max>0. Receiver energy is not supplied. Coordinates use
R30's fixed component units, with canonical conversion factors L_* and P_*.
Write C=(q_1,q_2,q_3,H_app) and C_*=C(eta_c). Only component j has report
error epsilon; all others equal C_* exactly. For apparatus-energy uncertainty
j=4, epsilon is measured in the fixed energy unit. Sections 1–3 prove the curve and conditional canonical bound for any R30
design. Section 4 supplies an explicit admissible pulse selection making all
four column tests positive; an arbitrary fixed design retains its own test.

## 1. Construct the fibre through the exact coupled reference

Use R31's exact reference Y_lambda=G_lambda(0,eta_c), with
a_lambda=S^{-1}Y_lambda, and its inverse apparatus chart eta_lambda(w,a).
Define

$$T_\lambda(w)=\frac{C(\eta_\lambda(w,a_\lambda))-C_*}{\lambda}.$$

The numerator vanishes at lambda=0 for every w, and at w=0 for every
lambda. R30's smooth divided-map argument gives

$$T_\lambda(0)=0,\qquad T_0(w)=Lw,\qquad
D_wT_\lambda(0)=J_\lambda=L+O(\lambda). \tag{1}$$

Indeed T_lambda=D_lambda(w,a_lambda)-D_lambda(0,a_lambda), and
a_lambda tends to eta_c. This cancellation includes the displacement of
the nominal coupled apparatus; replacing Y_lambda by a free record would
change the reference preparation.

Since L is invertible, the parameter-dependent inverse theorem yields fixed
positive s_0 and lambda_0 and a smooth family

$$w_{\lambda,j}(s)=T_\lambda^{-1}(s e_j),\quad |s|\le s_0,
\quad w_{\lambda,j}(0)=0. \tag{2}$$

Here the inverse is on a neighbourhood of zero contained in the interior of
Z. Choose a smaller common neighbourhood first and then a fixed coupling
ceiling, so its compensating apparatus remains inside the original box.
The derivative is invertible uniformly near (lambda,w)=(0,0); the usual
contraction proof supplies a common image neighbourhood, making s_0
independent of lambda. These restrictions shrink the constructed family,
not the physical preparation box.

Every member has exactly the same ten final apparatus coordinates and

$$C(\eta_\lambda(w_{\lambda,j}(s),a_\lambda))
=C_*+\lambda s e_j. \tag{3}$$

Consequently the allowed common-record segment includes every

$$|s|\le s_\epsilon:=\min\{s_0,\epsilon/\lambda\}. \tag{4}$$

This is an exact nonlinear construction with all apparatus reaction retained.
At positive epsilon it proves full receiver-state ambiguity for each of the
four choices j. At epsilon=0 R30 recovers the unique reference state.

## 2. Which canonical quantities move?

Differentiation gives the explicit test

$$\partial_s w_{\lambda,j}(0)=J_\lambda^{-1}e_j
=d_j+O(\lambda),\qquad d_j=L^{-1}e_j. \tag{5}$$

For j=4 this is the unique vector annihilated by A_1,A_2,A_3 and normalized
by -Kc B_1(d_4)=1, with the fixed output-unit factors of R30 understood.
The response in position is L_*(d_j)_x; in momentum it is P_*(d_j)_P.
The nonzero vector d_j guarantees state ambiguity. A positive product of
canonical risks follows when both displayed canonical components are nonzero.

Under this additional test, reduce s_0 and lambda_0 so each of the two
canonical derivatives keeps its sign and has magnitude at least half its
limiting magnitude. The endpoints s=+/-s_epsilon then have separations at
least L_*|(d_j)_x|s_epsilon and P_*|(d_j)_P|s_epsilon. Every estimator on
the admitted class therefore obeys

$$\epsilon_x\epsilon_P\ge
\frac{L_*P_*}{4}|(d_j)_x(d_j)_P|\,s_\epsilon^2. \tag{6}$$

R31's feasible-estimator upper bound remains valid with three zero
tolerances. Together with bounded-domain zero estimates, (6) gives optimal
canonical product order min{1,(epsilon/lambda)^2}, up to fixed positive
action-unit constants, whenever the two-component test holds. A vanishing
leading component requires examining the exact derivative or higher-order
curve; it does not establish that the corresponding observable is recovered.

## 3. A positive risk product can live on a curve

At fixed positive epsilon, weak coupling retains this whole local curve
segment. Unlike R31's four-error construction, it does not fill an energy
ball. R30's derivative margin makes T_lambda a smooth injective local
diffeomorphism on the receiver domain. Its intersection with a coordinate
line is locally one-dimensional. The canonical projection of each smooth
curve patch has zero planar area even when both coordinate diameters are
positive. Thus positive worst-case position and momentum errors do not
require a positive symplectic area of compatible states.

The scale in (6) is set by calibration tolerance, pulse response and the
admitted preparation neighbourhood. Improved supplied precision at fixed
coupling closes it. Section 4 evaluates all four columns for an explicitly selected R30
subfamily; positivity for arbitrary admissible pulse designs remains a
separate question.

## 4. An explicit pulse subfamily makes all four canonical products positive

Choose the first three nominal pulse times to be tau, 2 tau, 3 tau, with
0<3 tau<T and tau sufficiently small. Then choose disjoint nonnegative smooth
pulses with sufficiently small positive widths, and fix those widths. This is
an explicit additional selection within R30's admissible designs; its rank
conditions alone were not a test of individual inverse entries. For this
selection every d_j has nonzero x and P components. Thus (6) holds for each
of the four single uncertain constraints, including apparatus energy.

Here is a written small-time proof, using physical receiver coordinates to
make the scalings transparent. Put alpha=a/mu+d/nu and
beta=(ad-g^2)/(mu nu). The free receiver output satisfies

$$x^{(4)}+\alpha\ddot x+\beta x=0.$$

Since g>0, the jet (x(0),xdot(0),xddot(0),x'''(0)) determines the full
receiver state: P=mu xdot, y=(mu xddot+a x)/g, and
Q=(mu nu x'''+a nu xdot)/g. For fixed positive tau use coordinates

$$b=(x(0),\tau\dot x(0),\tau^2\ddot x(0)/2,
                   \tau^3x'''(0)/6).$$

In these coordinates the four functionals

$$\mathcal H_\tau x=(x(\tau),x(2\tau),x(3\tau),\tau\dot x(\tau))$$

converge, with matrix error O(tau squared), to evaluation of
p(u)=b_0+b_1 u+b_2 u^2+b_3 u^3 at u=1,2,3 and p'(1).
To verify the error despite the scaled coordinates, set X(u)=x(tau u).
Its equation is X''''+alpha tau^2 X''+beta tau^4 X=0, with initial
jet (b_0,b_1,2b_2,6b_3). Integrating this equation on the fixed interval
[0,3] gives the asserted uniform linear-map error. This is a Taylor/ODE
estimate, not a numerical check.

The limiting Hermite map is invertible: its homogeneous cubic has zeros
at 1,2,3 and a double zero at 1, so is zero. Its inverse columns are:

| j | Cardinal polynomial p_j(u) | p_j(0) | p'_j(0) |
| --- | --- | --- | --- |
| 1 | (u-2)(u-3)(3u-1)/4 | -3/2 | 23/4 |
| 2 | -(u-1)^2(u-3) | 3 | -7 |
| 3 | (u-1)^2(u-2)/4 | -1/2 | 5/4 |
| 4 | (u-1)(u-2)(u-3)/2 | -3 | 11/2 |

Direct substitution verifies the four interpolation conditions for each
column; differentiating the displayed products gives the last column.
Continuity of inversion gives initial x and P components
p_j(0)+O(tau squared) and (mu/tau)(p'_j(0)+O(tau squared)) for
H_tau^{-1}e_j. Every displayed leading coefficient is nonzero.

To transfer to L, write I_j=integral f_j(s_0+v_0 t) dt>0. In the
narrow-pulse limit its rows are nonzero multiples of the H_tau rows, with
multipliers

$$\sigma_j=-K I_j j\tau/M_j\ (j=1,2,3),\qquad
\sigma_4=-Kc I_1/\tau.$$

Normalize by these factors before taking the width limit; no lower bound
on pulse integrals in that auxiliary limit is needed. In physical input and
output units the inverse column has limiting canonical components

$$ (d_j)_x=\sigma_j^{-1}[p_j(0)+O(\tau^2)],\qquad
(d_j)_P=\frac{\mu}{\tau\sigma_j}[p'_j(0)+O(\tau^2)]. \tag{7}$$

These formulae describe the zero-width limit at fixed tau; for actual pulses
there are additional errors tending to zero after row normalization as widths
decrease. Here is the finite-width estimate. For fixed tau, let e(t) be the row
mapping b to x(t), and place each pulse support within h of j tau, with
h<tau/4. The normalized position row is the positive weighted average of
(t/(j tau))e(t); the normalized fourth row is the average of tau e'(t)
under pulse 1. By the mean-value bound their distances from e(j tau) and
tau e'(tau) are at most h times, respectively,
sup ||(t e(t))'||/(j tau) and tau sup ||e''(t)|| over these supports.
These constants are finite at the chosen tau. Thus the normalized four-row
matrix N satisfies ||N-H_tau||<=C_tau h in b coordinates.
If ||H_tau^{-1}|| C_tau h<1/2, the inverse identity gives
||N^{-1}-H_tau^{-1}||<=2||H_tau^{-1}||^2 C_tau h.
Choose h still smaller so this is below half the smallest absolute entry
in the first two rows of H_tau^{-1}. All eight entries then stay nonzero;
these rows recover x and tau P/mu. This also proves the required uniform
operator estimate independently of the pulse amplitudes or integrals.
Select tau first, then positive widths so all eight entries remain
nonzero. Conversion to R30's fixed component units multiplies inverse entries
by fixed nonzero factors and preserves this conclusion. Formula (6) uses the
dimensionless entries and the factors L_* and P_* as before.

The first two times are exactly R29's construction. Invertibility of H_tau
makes the third row nonzero on their three-row kernel, as R30 requires.
The first three position rows are independent. Analytic observability then
selects a fourth disjoint time completing the ordinary four-position signal
matrix. Choose all four widths small enough to preserve both determinants
and the eight inverse-entry margins. After this choice all pulses, tau,
masses and c stay fixed. R30 selects its small fixed apparatus box for this
design; R32 shrinks only the constructed curve and coupling ceiling thereafter.

For any other already fixed R30 design, the exact algebraic criterion is
that both cofactors cof_{j,1}(L) and cof_{j,2}(L) are nonzero, since
(L^{-1})_{i,j}=cof_{j,i}(L)/det L in the ordering (x,P,y,Q).
The construction above proves simultaneous feasibility, not positivity for
every R30 design. It introduces no shrinking-pulse physical limit into the
risk theorem. At fixed design its optimal product order remains
min(1,(epsilon/lambda)^2), with action units and preparation-dependent constants.

C121 accepts this pulse-selection result after the [B64 review](../reviews/pulse-column-B64.md).
The interpolation methods and bounded source coverage are recorded in
[B64](../references/batches/B64.md); exact model matches and novelty remain unassessed.
