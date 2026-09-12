# Two calibrated probe positions give local recovery and two global branches

A fixed smooth pulse design with q_1=c nonzero and q_2=0 has isolated,
locally recoverable preparations with identical complete final apparatus
records. Both exact initial energies E,H_0 are retained. The two receiver
states approach opposite shell points as coupling decreases and differ in
both canonical coordinates. Thus the second calibration removes the R28
curve locally but still permits global canonical ambiguity.

R29, 2026-09-12. Use R28's apparatus and fixed positive preparation box,
known T, exact model and the two energies. Choose the fixed pulses below
before decreasing coupling. The exact full-record compensator eta_lambda(w)
is centred at eta_c, with q_1=c and all other probe coordinates and momenta
zero. It is defined on a receiver neighbourhood containing both selected
shell points by the uniform R25 construction, for lambda small relative to
the fixed box width. Source coverage is in [B60](../references/batches/B60.md).

## 1. Three regular constraints after compensating the apparatus

Fix a receiver shell point z_bar, to be chosen in section 2, and set
Y_lambda=G_lambda(z_bar,eta_c). R28's smooth divided residuals U_lambda,
V_lambda impose q_1=c and H_app=H_0 on eta_lambda(w). Add

$$W_\lambda(w)=q_2(\eta_\lambda(w))/\lambda.$$

The exact pointer drift identity used in R28 gives the smooth zero-coupling
limit W_0(w)=-(K/M_2)A_2(w-z_bar), where

$$A_1(w)=\int_0^T t f_1(s_0+v_0t)x_w(t)\,dt,\qquad
B_1(w)=\int_0^T f_1(s_0+v_0t)\dot x_w(t)\,dt,$$
$$A_2(w)=\int_0^T t f_2(s_0+v_0t)x_w(t)\,dt.$$

The other limits are U_0=-(K/M_1)A_1(w-z_bar) and
V_0=-Kc B_1(w-z_bar). Smooth divisibility is joint in lambda and w:
each vanishing numerator N equals lambda times the integral of its coupling
derivative at theta lambda for 0<=theta<=1. The exact residual system is

$$\mathcal R_\lambda(w)=
 (H_s(w)-E,U_\lambda(w),V_\lambda(w),W_\lambda(w))=0. \tag{1}$$

All reaction terms are retained in this system.

## 2. Three pulse rows with a canonical one-dimensional kernel

Consider initially narrow-pulse evaluation rows x(tau), xdot(tau), x(2tau),
with tau>0 small and 2tau<T. The first two conditions say that the state at
tau is (0,0,Y,Q). Choose Q>0 fixed. Since

$$x(2\tau)=\frac g{2\mu}Y\tau^2+
                  \frac g{6\mu\nu}Q\tau^3+O(Y\tau^4+Q\tau^5),$$

the coefficient of Y is nonzero for small tau. There is a unique Y with
x(2tau)=0, and Y=-Q tau/(3nu)+O(tau cubed). Evolving this state backward
from tau gives the common-kernel vector v with

$$v_x=-\frac{gQ}{3\mu\nu}\tau^3+O(\tau^5),\qquad
v_P=\frac{5gQ}{6\nu}\tau^2+O(\tau^4). \tag{2}$$

Both are nonzero. The three evaluation rows have rank three: the third
restricts the two-dimensional kernel of the first two by its nonzero Y
coefficient. Fix such a tau. Positive smooth pulse widths sufficiently
small around tau and 2tau preserve rank and a nearby kernel vector with
v_x v_P nonzero for the actual rows A_1,B_1,A_2, after dividing each by
its positive integral and time factor as appropriate.

Two more disjoint pulses can complete the four ordinary position-signal rows
to an invertible R06 signal matrix. The two already chosen position rows
are independent, and analytic observability spans all four dimensions on any
remaining open interval. Fix all widths once. Force ceilings and cutoff
margins are then met by reducing the physical coupling bound.

Let J be the positive receiver energy matrix and set

$$z_{\rm bar}=\sqrt{\frac{2E}{v^T Jv}}v.$$

The three linear rows vanish on z_bar. Their kernel is its span. Therefore
at both +z_bar and -z_bar the four rows dH_s,A_1,B_1,A_2 are independent:
dH_s evaluated on the corresponding shell vector is 2E.

## 3. Continue both roots of the exact constrained record system

At lambda=0, (1) has roots +z_bar and -z_bar. Its derivative at each is
invertible. Smooth parameter continuation gives two exact roots

$$w_+(\lambda)=z_{\rm bar},\qquad
w_-(\lambda)=-z_{\rm bar}+O(\lambda). \tag{3}$$

The first is constant because eta_lambda(z_bar)=eta_c exactly. For the
second, precondition the residual derivative by its inverse at (0,-z_bar).
On a small fixed receiver ball and coupling interval it differs from identity
by at most one half. The residual at the centre is O(lambda), so shrinking
the coupling interval gives a self-mapping contraction on this ball. This
supplies a uniform branch, not merely formal first-order solutions.

R25's apparatus estimate is uniform between the two bounded receiver
neighbourhoods: ||eta_lambda(w)-eta_c||<=C lambda||w-z_bar||. Hence both
branches retain b/2 preparation margins for sufficiently small coupling.
Each has q_1=c, q_2=0, H_s=E, H_app=H_0 and exact complete record Y_lambda.
Endpoint pulse absence, clock positivity and linear cutoffs persist.

## 4. Local recovery and global risk have different quantifiers

At each positive fixed small coupling, form the augmented map from all
fourteen initial coordinates to the ten final records and four preparation
quantities (H_s,q_1,H_app,q_2). Its apparatus-to-record block is invertible
by R25. Eliminating that block leaves the derivative of (1), with its last
three rows multiplied by lambda. It is invertible at both branches by
section 3, since lambda>0.

In fixed units, continuity gives a convex neighbourhood about each branch
on which the augmented derivative differs from its value at the centre by
less than half its inverse margin. Segment integration gives a positive
lower Lipschitz bound there. Restricting to the known preparation values
then gives local recovery from the ten records, including local stability.
These neighbourhoods and constants may depend on the chosen positive
coupling. No uniform limit of their unscaled inverse margins is asserted.

Nevertheless the two neighbourhoods contain distinct preparations with one
common record. Every deterministic receiver estimator on the global admitted
class therefore satisfies

$$\epsilon_x\ge\tfrac12|(w_+-w_-)_x|,
\qquad\epsilon_P\ge\tfrac12|(w_+-w_-)_P|,$$
$$\epsilon_x\epsilon_P\ge
\tfrac14|(w_+-w_-)_x(w_+-w_-)_P|
\longrightarrow |(z_{\rm bar})_x(z_{\rm bar})_P|>0. \tag{4}$$

The limit concerns this lower bound; it has action units. Its constants
depend on E,c,b and fixed pulse geometry. This pair yields neither a positive
area nor an exact global minimax value. It is not generated by the broken
sign symmetry of the full calibrated apparatus: the second compensating
apparatus is obtained from the exact inverse record map.

Next R30: calibrate q_3=0 as well. Its divided residual adds A_3=integral
t f_3 x. Select it nonzero on the present one-dimensional kernel and test
uniform global recovery, rather than only disappearance of these two roots.
The resulting four leading linear constraints may make exact receiver
energy redundant; establish that on the stated full preparation domain.
