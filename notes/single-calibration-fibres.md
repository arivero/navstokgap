# One uncertain calibration leaves an exact receiver curve

Keeping three supplied constraints exact and allowing the fourth to vary
leaves a one-dimensional common-record receiver family. Its leading direction
is the corresponding column of the inverse calibration-response matrix.
Thus the location of the uncertainty matters: its canonical effects are read
from that column, rather than from the number of missing constraints.

R32, first stage, 2026-09-12. Retain R30's fixed pulse design, nonzero c,
small fixed apparatus box, full exact final record and receiver energy ball
Z={H_s<=E_max}, E_max>0. Receiver energy is not supplied. Coordinates use
R30's fixed component units, with canonical conversion factors L_* and P_*.
Write C=(q_1,q_2,q_3,H_app) and C_*=C(eta_c). Only component j has report
error epsilon; all others equal C_* exactly. For apparatus-energy uncertainty
j=4, epsilon is measured in the fixed energy unit. This note proves the
curve and a conditional canonical risk bound; evaluation of the actual
pulse-design columns is the next stage.

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
coupling closes it. The next calculation evaluates d_4 for the actual R30
pulse family, then compares the other columns; no design-generic canonical
positivity is assumed here.
