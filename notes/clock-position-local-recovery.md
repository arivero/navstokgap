# A known clock position permits stable local recovery

Revealing the initial clock position removes R20's common-record phase
ambiguity on a fixed local preparation patch. Eight final pointer records,
known zero incoming probe momenta and exact receiver energy jointly determine
the receiver, incoming probe positions and unknown initial clock momentum.
A uniform inverse estimate gives a canonical reconstruction-error product
that closes with final record error at fixed positive coupling.

R21, 2026-09-11. This is a local-domain result for the fixed pulse design and
transverse shell point constructed in [R20](hidden-clock-ambiguity.md).
The location of the preparation patch and exact initial receiver energy are
supplied information. Global recovery on the entire energy shell is open.
Literature coverage is recorded separately in [B52](../references/batches/B52.md).

## 1. Augment the record by the supplied energy

Retain R20's Hamiltonian, masses, observation time T, cutoff margins, fixed
pulse design, E>0 and shell point z_*. Fix the revealed initial clock position
at s_0. Incoming probe momenta are fixed and known at zero; the four incoming
positions q and the initial clock speed v=p_s(0)/M_c are unknown. The free
receiver energy is H_s(z)=z^T Gz/2 and A_v means A_{s_0,v}. The exact scaled
record map, smoothly extended to lambda=0, is

$$F_\lambda(z,q,v)=\left(\frac{\pi(T)}{\lambda},q(T)\right),\qquad
F_0(z,q,v)=(-A_v z,q). \tag{1}$$

Fix positive component units, including a speed unit V_* and energy unit E_*.
All norms and derivatives below are in these dimensionless coordinates;
physical formulas for the derivative kernel are unchanged by conjugation
with those unit matrices. Set w=(z,q,v), w_*=(z_*,0,v_0), and

$$\mathcal G_\lambda(w)=\big(F_\lambda(w),H_s(z)/E_*\big). \tag{2}$$

There are nine unknown coordinates and nine augmented outputs. Energy is a
known preparation constraint, not an additional measured pointer output.
R19's integrated equations and R20's clock-derivative extension give
smoothness in (lambda,w) and C1 convergence to G_0 on a common compact
neighbourhood with strict pulse and cutoff margins. The pulse design remains
fixed throughout this argument; only coupling and record errors vary.

## 2. The energy-speed derivative supplies the missing rank

At w_* the physical block derivative has the form

$$J=D\mathcal G_0(w_*)=
\begin{pmatrix}
-A_0&0&-(\partial_v A)_0z_*\\
0&I&0\\
z_*^T G/E_*&0&0
\end{pmatrix}. \tag{3}$$

To test its kernel, the first two rows give

$$dq=0,\qquad dz=Bz_*\,dv,\qquad B=-A_0^{-1}(\partial_v A)_0.$$

The last row then gives

$$0=\frac{\tau}{E_*}dv,\qquad \tau=z_*^T GBz_*>0. \tag{4}$$

R20 establishes both invertibility of A_0 and positivity of tau for this
fixed design and selected shell point. Hence dv=0, dz=0, and J is invertible.
The condition is quantitative only after units and the design are fixed.
No inference that tau is nonzero everywhere on the shell is used.

## 3. One fixed neighbourhood and a uniform inverse bound

Let gamma=1/||J^{-1}||>0 in the fixed component sup norms. Continuity of
D G_0 gives a closed convex ball U about w_*, small enough that

$$\sup_{w\in U}||D\mathcal G_0(w)-J||\le\gamma/4.$$

Choose U inside the physical speed, position and cutoff margins. Uniform
C1 convergence then gives lambda_0>0 with

$$\sup_{w\in U}||D\mathcal G_\lambda(w)-J||\le\gamma/2
\quad(0\le\lambda\le\lambda_0). \tag{5}$$

For any w,w' in U, integrate D G_lambda-J along their straight segment:

$$||\mathcal G_\lambda(w)-\mathcal G_\lambda(w')||
\ge \frac{\gamma}{2}||w-w'||. \tag{6}$$

This gives injectivity and a Lipschitz inverse on the image, with the same
U and constant for all these couplings. The extension at lambda=0 is an
analytic tool: unscaled zero-coupling pointer records carry no receiver
signal. Physical reconstruction uses 0<lambda<=lambda_0.

Choose a closed receiver ball Z_* about z_*, a fixed positive incoming
position box Q_* about zero, and a fixed positive speed interval V about
v_0, whose Cartesian product is contained in U. The physical preparation is

$$\mathcal K=(Z_*\cap\{H_s=E\})\times Q_*\times V. \tag{7}$$

It is compact, has a receiver shell patch of positive relative interior,
and has independent positive apparatus widths. All these sets stay fixed as
record errors decrease. For two points in K the energy outputs agree, so
(6) is already a lower Lipschitz estimate for their eight scaled records.
Segments used in the proof lie in U; they need not lie on the energy shell.
This is what promotes the pointwise rank calculation to a uniform local
preparation-domain recovery statement.

## 4. Record stability and the action-valued error product

Let final pointer momentum and position record errors in the fixed units
be bounded by rho_pi and rho_q, respectively. In (1) the combined error is

$$\delta=\max(\rho_\pi/\lambda,\rho_q).$$

Choose any minimum-residual fit of the scaled record on K; compactness gives
existence even when the noisy record lies outside the exact image. The true
state has residual at most delta, so the fitted and true exact records differ
by at most 2 delta. Their energy components agree exactly. Equation (6) gives

$$||\widehat w-w||\le4\delta/\gamma. \tag{8}$$

Taking worst-case initial receiver coordinate errors over K and the allowed
record errors, with physical canonical units L_*,P_*, yields

$$0\le\mathcal H_{\rm rec}:=\epsilon_x\epsilon_P
\le\frac{16L_*P_*}{\gamma^2}
       \max(\rho_\pi/\lambda,\rho_q)^2. \tag{9}$$

This product has units ML^2/T, without a 2 pi normalization. The initial
clock-momentum error is at most 4 M_c V_* delta/gamma. At fixed positive
lambda, fixed apparatus and fixed local preparation, both receiver risks
and the clock-momentum risk vanish uniformly as record errors vanish.
A joint limit also closes whenever rho_pi/lambda and rho_q tend to zero.
The constants may deteriorate as tau approaches zero or the pulse design
changes; no uniform assertion over such families follows.

## 5. The next test is global clock-speed ambiguity

R20's source capsule borrows the observation-map viewpoint from Sontag and
the smooth-flow premise from Sideris. Here the model-specific Schur complement
(4), followed by segment integration, decides recovery. The result settles
local uniqueness with exact energy and revealed clock position; it does not
select a positive universal action scale.

For R22, retain the revealed offset and compare two unknown speeds across the
whole receiver shell. At zero coupling, equality of scaled momentum records
requires z'=A_{v'}^{-1}A_v z. Determine whether this transform preserves H_s
for some nonzero z and v' different from v in a stated speed interval; then
test persistence or exclusion at positive coupling with eight records and
fixed preparation margins. A sign change or zero of the constrained
energy-speed derivative is a diagnostic, not by itself an exact ambiguous
pair. This distinguishes genuine global branches from local conditioning.
