# Final clock momentum restores global receiver recovery

Yes: adding the clock's final momentum to the eight final pointer coordinates
restores uniform global recovery on the full receiver energy shell for
sufficiently small fixed positive coupling. It determines the unknown initial
clock speed, receiver state and incoming probe positions together. The proof
also works on a bounded receiver energy ball: exact initial energy is no longer
needed as reconstruction data.

R23, 2026-09-11. Retain R19's fixed apparatus, revealed initial clock position
s_0, known zero incoming probe momenta and known observation time T. Unknown
receiver state z lies in a compact convex neighbourhood Z of the energy ball;
incoming positions q occupy a fixed positive box, and speed v a fixed small
positive interval V about v_0. Choose these domains with common strict pulse
and cutoff margins and uniformly invertible free signal matrices A_v. All
apparatus masses, pulse geometry and preparation widths remain fixed.
The added datum is p_s(T), persistent after all pulses. Literature coverage
is in [B54](../references/batches/B54.md).

## 1. Include the clock reaction in the record map

Use fixed component units, including speed unit V_* and clock momentum unit
M_c V_*. The physical expression for the nine scaled records is

$$\mathcal F_\lambda(z,q,v)=
 \left(\frac{\pi(T)}{\lambda},q(T),\frac{p_s(T)}{M_c}\right).$$

All norm statements below are in the corresponding dimensionless coordinates.
R19's finite-time variational estimates, extended to v, give

$$\mathcal F_\lambda=L+R_\lambda,\qquad
L(z,q,v)=(-A_vz,q,v),\qquad
\|R_\lambda\|_{C^1}\le C\lambda. \tag{1}$$

For the new block, the exact equation in the linear cutoff region is

$$p_s(T)=M_cv-\lambda K\sum_j\int_0^T f'_j(s(t))x(t)q_j(t)\,dt. \tag{2}$$

The integrand and its initial-data derivatives are uniformly bounded on the
common compact finite-time domain. Thus the correction and its derivatives
are O(lambda); no unaffected-clock approximation is made. The same argument
gives the first two blocks as in R19. Smoothness supplies a uniform C1
remainder on the entire convex domain, not just on the shell. After the
clock leaves every pulse, its momentum is constant and can be stored as a
record. Final probe positions still refer to the specified time T.

## 2. A global inverse bound for the nonlinear leading map

Choose alpha>0 with ||A_v h||>=alpha||h|| throughout V, and let

$$D=\sup_{v\in V,z\in Z}\|(\partial_v A_v)z\|<\infty.$$

For w=(z,q,v), w'=(z',q',v') set d=||L(w)-L(w')|| in the product sup norm.
The last two blocks give ||q-q'||<=d and |v-v'|<=d. The first gives

$$\alpha\|z-z'\|
 \le\|A_vz-A_{v'}z'\|+\|(A_{v'}-A_v)z'\|
 \le(1+D)d.$$

Here the speed segment stays in V and z' stays in Z. Consequently

$$\|L(w)-L(w')\|\ge\beta\|w-w'\|,\qquad
\beta=\min\left(1,\frac{\alpha}{1+D}\right)>0. \tag{3}$$

This directly handles the v-dependent signal matrix; L need not be linear.
Integrating the derivative of R along the segment in the convex preparation
domain yields

$$\|\mathcal F_\lambda(w)-\mathcal F_\lambda(w')\|
 \ge(\beta-C\lambda)\|w-w'\|
 \ge\frac\beta2\|w-w'\| \tag{4}$$

for all 0<lambda<=lambda_0 after choosing C lambda_0<=beta/2. Hence the
nine exact records uniquely determine all nine unknowns globally on this
domain. In particular they exclude R22's distinct-speed equal-record pairs.
The proof uses the whole bounded receiver domain; neither a known local
receiver patch nor the equation H_s=E supplies the missing rank.

The physical role is simple: the last record constrains speed; with speed
constrained, the first four signals constrain receiver state, and final
positions constrain incoming pointer positions. Equation (2) is calibrated
jointly rather than substituting p_s(T)/M_c as an exact initial speed.

## 3. Finite precision and action products

Suppose final pointer momentum, position and clock-momentum errors have
dimensionless sup bounds rho_pi,rho_q,rho_c in the declared units. Then

$$\delta=\max(\rho_\pi/\lambda,\rho_q,\rho_c).$$

Choose a minimum-residual fit on the compact admitted domain (either the
energy shell times apparatus boxes or a closed energy ball times those boxes).
The true state is a competitor, so the fitted and true exact record vectors
differ by at most 2 delta. Equation (4) gives

$$\|\widehat w-w\|\le4\delta/\beta,\qquad
\epsilon_x\epsilon_P\le\frac{16L_*P_*}{\beta^2}\delta^2. \tag{5}$$

Here L_*,P_* are fixed receiver canonical units and epsilon_x,epsilon_P are
worst initial-coordinate errors. The product has action units without a
2 pi factor. Initial clock momentum error is at most 4 M_c V_* delta/beta.
At fixed positive coupling all errors close uniformly as the three record
precisions improve, with positive preparation widths unchanged. A joint
coupling/precision limit also closes if rho_pi/lambda, rho_q and rho_c tend
to zero. The bounded receiver disturbance need not vanish.

This settles which resource caused the preceding global ambiguity: an
unobserved clock speed. Arbitrarily precise joint access to the nine final
records and exact model calibration are still supplied resources. The added
momentum is a mechanical stored variable; implementing its readout with another
apparatus is a separate measurement-composition question.

## 4. Next test

R24 should hide initial clock position as well, add its final position at T,
and test the full ten-coordinate apparatus record. Its leading clock map is
(s,v)->(s+vT,v), suggesting a global inverse on fixed small clock boxes.
Then consolidate the clock results by comparing which preparation data are
supplied and which persistent or time-stamped records replace them.
