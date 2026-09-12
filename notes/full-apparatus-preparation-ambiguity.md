# Full final apparatus records can hide the entire receiver energy shell

Unknown incoming apparatus phase permits exact compensation of receiver changes
in R06, even when all ten final apparatus coordinates are recorded at known T.
A uniform contraction gives a common-record shell patch with an interior
preparation margin. At any fixed positive box width, sufficiently weak positive
coupling hides the whole shell behind one record: the coordinate minimax risks
then equal their no-record values exactly.

R25, 2026-09-12. Use [R06](autonomous-finite-readout.md)'s autonomous Hamiltonian,
fixed finite masses, smooth fixed pulses, cutoff margins and observation time.
The information includes the Hamiltonian and exact initial receiver energy E>0.
Every pair in the Cartesian product of that shell and the full initial apparatus
box is admissible; there is no known exact initial apparatus or total energy.
Risks below are deterministic worst-case errors for initial canonical (x,P).
They have no probability-density or accuracy–disturbance interpretation.

## 1. Invert the free apparatus shear

Write the physical initial apparatus state as
eta=(q_1,...,q_4,pi_1,...,pi_4,s,p_s), with centre
eta_*=(0,...,0,s_0,M_c v_0), v_0>0. Use fixed positive component length and
momentum units for both initial and final records; henceforth these coordinates
and all sup norms are dimensionless. The unknown box is
||eta-eta_*||<=b, 0<b<=b_0. The receiver domain Z is the convex energy ball
H_s<=E, or a fixed slightly larger ball when derivatives need a neighbourhood.

Let G_lambda(z,eta) be the ten unscaled final apparatus coordinates. At zero
coupling the receiver decouples and G_0=S eta. In physical coordinates the
invertible linear shear S is

$$(q_j,\pi_j,s,p_s)\longmapsto
(q_j+T\pi_j/M_j,\pi_j,s+Tp_s/M_c,p_s). \tag{1}$$

In dimensionless coordinates the coefficients include the corresponding fixed
momentum-to-length unit ratios. Set F_lambda=S^{-1}G_lambda. Uniform smooth
finite-time flow dependence on the common compact trajectory neighbourhood gives
constants C,L>0 and lambda_0>0, independent of b and lambda, such that

$$\|D_\eta F_\lambda-I\|\le C\lambda\le\tfrac12,
\qquad \|D_zF_\lambda\|\le L\lambda,
\quad 0\le\lambda\le\lambda_0. \tag{2}$$

Indeed F_0=eta, its two derivatives are I and zero, and their coupling
derivatives are bounded on this compact smooth-flow domain. R06's conserved
energy upper bound, bounded interaction and fixed T supply common existence
and trajectory bounds. Reduce b_0 and lambda_0 to preserve all cutoff and pulse
margins, including positive clock speed. Unknown initial probe momenta make
free probe positions drift; b_0 is chosen to cover that drift throughout T.
Equation (2) controls the complete interacting flow, including clock reaction.
No inverse signal matrix or pulse-rank assumption is needed for this ambiguity.

Fix any shell point z_* and the final record Y_*=G_lambda(z_*,eta_*).
For w in Z define on ||eta-eta_*||<=b/2

$$T_w(\eta)=\eta-F_\lambda(w,\eta)+F_\lambda(z_*,\eta_*).$$

If ||w-z_*||<=b/(4L lambda), (2) and the segment in Z imply

$$\|T_w(\eta_*)-\eta_*\|\le b/4,\qquad
\|T_w(\eta)-\eta_*\|\le b/4+\tfrac12\|\eta-\eta_*\|\le b/2.$$

Thus T_w is a self-mapping contraction with constant at most 1/2. Its unique
fixed point in that ball obeys

$$G_\lambda(w,\eta(w))=Y_*,\qquad
\|\eta(w)-\eta_*\|\le2L\lambda\|w-z_*\|\le b/2. \tag{3}$$

Equality holds for every final position and momentum, without dividing a
record by lambda. The prepared product support admits these correlated
choices of initial data; they need not have positive probability under a density.

## 2. A quantitative canonical patch at fixed coupling

Write the receiver energy as

$$H_s=\frac{P^2}{2\mu}+\frac{Q^2}{2\nu}
 +\frac{k_x}{2}x^2+\frac d2(y-gx/d)^2,
\qquad k_x=a-g^2/d>0.$$

At z_*=(0,0,sqrt(2E/d),0), use the exact shell chart

$$w(x,P)=\left(x,P,\frac gd x+
\sqrt{\frac{2E-k_xx^2-P^2/\mu}{d}},0\right). \tag{4}$$

Choose fixed canonical units L_*,P_* and r_0,C_0>0 so that the square
|x|<=L_*r_0, |P|<=P_*r_0 lies strictly inside the radicand domain and
||w(x,P)-z_*||<=C_0 max(|x|/L_*,|P|/P_*). These constants are independent of
b and lambda. With

$$r=\min\{r_0,b/(4LC_0\lambda)\}>0,$$

the common-record fibre contains this entire square at radius r. For any
estimator, taking the two endpoints of each compatible coordinate interval gives

$$\epsilon_x\ge L_*r,\qquad \epsilon_P\ge P_*r,\qquad
\epsilon_x\epsilon_P\ge L_*P_*r^2. \tag{5}$$

The projected compatible area is at least 4L_*P_*r^2. These are lower bounds,
not optimal constants in the general fixed-coupling regime.

## 3. Exact saturation at fixed preparation width

Let D=max_{H_s(w)=E}||w-z_*||>0 in the fixed receiver units. If

$$0<\lambda\le\min\{\lambda_0,b/(4LD)\}, \tag{6}$$

(3) applies to every point of the compact shell with the same Y_* and the
same b/2 preparation margin. Consequently the compatible receiver set at Y_*
is exactly the entire admitted shell. Its projection is exactly the ellipse

$$k_xx^2+P^2/\mu\le2E: \tag{7}$$

necessity follows from positive residual energy; sufficiency follows by
choosing Q=0 and y=gx/d plus a square root as in (4), including the boundary.
The coordinate extrema are X_E=sqrt(2E/k_x) and P_E=sqrt(2mu E).
Define each minimax risk as the infimum over estimators of the supremum over
the admitted shell times apparatus box. Common-record endpoints give lower
bounds X_E,P_E; the constant estimator (0,0) attains both bounds over the whole
admitted class. Therefore

$$R_x=X_E,\quad R_P=P_E,\quad
\inf_{(\widehat x,\widehat P)}\epsilon_x\epsilon_P
=X_EP_E=2E\sqrt{\mu/k_x}. \tag{8}$$

The common-record projected area is exactly pi X_E P_E. Products and areas
have units ML^2/T; the risk product has no 2 pi normalization. The ellipse
area is an ordinary area in the canonical plane, not an area assigned to the
three-dimensional shell. The effective stiffness k_x describes an energy
projection; sqrt(k_x/mu) is not asserted to be a normal-mode frequency.

At fixed b>0, the weak-coupling regime (6) loses all worst-case coordinate
advantage of the ten records. At fixed lambda>0, the patch lower bound closes
as b tends to zero; (6) cannot be maintained in that limit. Under joint limits
its validity requires the explicit ratio condition (6). The saturated value
is set by receiver energy, masses and stiffness; it closes under receiver
cooling and establishes no universal positive action scale. This result
advances the preparation/access test for exclusion of zero, leaving universal
scale selection and the quantum role open.

## 4. Source connection and next test

[B56](../references/batches/B56.md) audits inherited B48 contraction and
common-record methods and B50/B55 smooth-flow coverage. The free-shear
preconditioner, exact complete-record compensation and full-shell saturation
are model derivations; novelty is unassessed. Proof acceptance is recorded in
[the review](../reviews/full-apparatus-B56.md).

R26 should supply exact initial apparatus energy in addition to receiver
energy and all final apparatus records. Along the unique compensator eta(w),
test the extra scalar constraint H_app(eta(w))=H_app(eta_*), with the initial
interaction zero before all pulses. Determine an actual common-record shell
family and its preparation margins or a recovery bound. Conservation of total
energy constrains final receiver energy but does not alone settle that fibre.
