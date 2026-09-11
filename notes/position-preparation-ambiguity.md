# Unknown probe positions can hide the receiver after momentum calibration

Revealing all four incoming probe momenta does not suffice for reconstruction
in an admissible fixed design of R06's apparatus. Unknown incoming positions
have a full-rank effect on the four final momenta at order lambda squared.
Clock reaction supplies the leading diagonal response for sufficiently narrow,
fixed pulses. Exact nonlinear compensation then hides a two-dimensional
receiver energy-shell patch and gives positive preparation-dependent canonical
reconstruction risks.

R18, 2026-09-11. This is an existence result within R06's pulse-design class;
invertibility of R06's signal matrix alone does not assert the response rank
for every pulse design. Choose the design first, then fix sufficiently small
lambda>0 and position half-width b>0. The information is the four initial
and four final probe momenta. The receiver shell and the full apparatus box
remain Cartesian supports. We use the admissible slice with nominal initial
clock data and zero incoming probe momenta; those clock data are not added as
records. All norms use R16's fixed component units. Literature coverage is in
[B49](../references/batches/B49.md).

## 1. The position response includes receiver and clock reaction

Write G_lambda(z,q) for final momenta on this slice, F_lambda(z)=G_lambda(z,0),
and f_j(t)=f_j(s_0+vt); a prime on f denotes its spatial derivative.
Let e_P inject a force into the receiver P equation, and put

$$h(t)=e_x\Phi_t e_P,\qquad h(0)=0,\quad h'(0)=1/\mu.$$

At zero coupling the initial probe position q_k stays constant. Differentiating
the receiver and clock equations with respect to q_k, the first-order
position variations are

$$\partial_{q_k}x(t)=-\lambda K\int_0^t h(t-u)f_k(u)\,du+O(\lambda^2),$$
$$\partial_{q_k}s(t)=-\frac{\lambda K}{M_c}
 \int_0^t(t-u)f'_k(u)x^0(u)\,du+O(\lambda^2).$$

The integrated record equation is -lambda K integral f_j(s)x dt. Hence

$$D_qG_\lambda(z,q)=\lambda^2 B(z)+O(\lambda^3),$$
$$B_{jk}(z)=K^2\int_0^T f_j(t)\int_0^t h(t-u)f_k(u)\,du\,dt
 +\frac{K^2}{M_c}\int_0^T f'_j(t)x^0(t)
   \int_0^t(t-u)f'_k(u)x^0(u)\,du\,dt. \tag{1}$$

These formulas are in physical position/momentum coordinates; fixed component
units conjugate B by invertible diagonal scalings. Each B entry has units
momentum/length. Smooth finite-time flow dependence and fixed cutoff margins
make the remainders uniform for z near a shell point and ||q||<=b_0.
At lambda=0, the receiver and clock paths do not depend on q, so the leading
matrix is independent of q. Taylor expansion in lambda of the variational
equations proves the stated uniform remainder; no computational checks are
used. In particular the clock term cannot be discarded at this order.

## 2. A fixed pulse design with invertible response

Order the four pulse supports in time. Equation (1) is lower triangular:
a later pulse k cannot affect record j before j's support ends. To prove
nonzero diagonal entries choose a smooth nonnegative nonzero bump phi supported
in (-1,1), and set

$$f_j(s_0+vt)=\phi((t-t_j)/\delta).$$

Here delta>0 is a design duration. At the shell point
z_*=(0,0,sqrt(2E/d),0), the analytic history x^0(t) is not identically zero,
since its second derivative at zero is g sqrt(2E/d)/mu>0. Its zeros are isolated.
R06 supplies four distinct times with independent evaluation rows. Perturbing
those times within their open invertibility neighbourhood avoids all zeros
of this history. Thus choose t_j with x_j=x^0(t_j) nonzero and independent rows.

For small delta, supports are disjoint and interior, and the signal matrix
A remains invertible after row normalization by K delta integral phi.
The receiver contribution to B_jj is O(delta^3), since h(t-u)=O(delta).
The clock contribution, after t=t_j+delta r and u=t_j+delta s, is

$$\frac{K^2x_j^2\delta}{M_cv^2}
 \int\phi'(r)\int_{s<r}(r-s)\phi'(s)\,ds\,dr+O(\delta^2)
 =-\frac{K^2x_j^2\delta}{M_cv^2}\int\phi(r)^2\,dr+O(\delta^2).$$

For the identity, the inner integral equals integral from -infinity to r
of phi(s) ds; integration by parts gives minus integral phi squared.
Smoothness of x^0 supplies the O(delta^2) remainder. Consequently every
B_jj(z_*) is negative for sufficiently small positive delta, and
B_*=B(z_*) is invertible. Choose one such delta once. Pulse derivatives,
conditioning constants and force bounds may depend on this design. Neither
delta nor M_c varies in the subsequent preparation or coupling limits;
reducing lambda_0 meets R06's uniform force and cutoff requirements.

## 3. Exact compensation with an interior position margin

In dimensionless component units, reduce the receiver neighbourhood and
lambda_0 so that, for ||q||<=b_0,

$$\|I-(\lambda^2B_*)^{-1}D_qG_\lambda(w,q)\|\le\tfrac12.$$

This follows from (1), continuity of B(w), and fixed invertibility of B_*.
R16 gives ||D_zF_lambda||<=L lambda. Choose a constant C>0 such that
||B_*^{-1}||L<=C. Set Y_*=F_lambda(z_*). For

$$\|w-z_*\|\le\frac{\lambda b}{4C},\qquad 0<b\le b_0,$$

the map

$$T_w(q)=q-(\lambda^2B_*)^{-1}(G_\lambda(w,q)-Y_*)$$

contracts the closed ball ||q||<=b/2 into itself: its derivative norm is at
most 1/2 and ||T_w(0)||<=C||w-z_*||/lambda<=b/4.
It has a unique fixed point there, with exact records G_lambda(w,q(w))=Y_*
and ||q(w)||<=2C||w-z_*||/lambda<=b/2. The four initial momenta also agree
exactly, at zero. Thus all eight observed values coincide on the constructed
fibre. Positive box margins, shell energy and apparatus upper resource bounds
are preserved, including the full clock reaction.

## 4. Canonical reconstruction risks and limits

Use R17's exact shell chart w(x,P), fixed units L_*,P_*, and constants r_0,C_0
with ||w(x,P)-z_*||<=C_0 max(|x|/L_*,|P|/P_*). Choose r_0 small enough for
section 3's receiver neighbourhood. Put

$$r=\min\left(r_0,\frac{\lambda b}{4CC_0}\right)>0.$$

The common augmented record admits every |x|<=L_*r, |P|<=P_*r. For every
estimator based on the eight momenta, the worst errors over the admitted
shell/box product therefore satisfy

$$\epsilon_x\ge L_*r,\qquad\epsilon_P\ge P_*r,\qquad
\mathcal H_{\rm rec}=\epsilon_x\epsilon_P\ge L_*P_*r^2.$$

The compatible receiver fibre has projected canonical area at least
4L_*P_*r^2. The product and area have units ML^2/T, with no 2 pi factor.
These are deterministic reconstruction bounds, not disturbance bounds.
At fixed coupling the displayed bound closes as b squared; at fixed b it
closes as lambda squared. This last statement concerns the lower bound only,
and does not prove that the full information risks vanish with lambda.
Unlike R17's momentum compensation, position compensation must pass through
two interaction factors, which accounts for the radius proportional to lambda b.
Positivity still comes from the preparation support and limited record access;
no preparation-independent universal action scale has been selected.

## 5. Next test

R19 should reveal the initial clock position and momentum as well as incoming probe momenta,
and add the four final probe positions while leaving their initial positions
unknown. Test whether the resulting eight final records jointly recover the
receiver and four unknown initial probe positions at fixed small coupling.
A uniform injectivity argument, rather than a rank count alone, should decide
whether reading both pointer coordinates removes this ambiguity.
