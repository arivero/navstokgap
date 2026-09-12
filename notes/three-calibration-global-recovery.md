# Three calibrated positions give uniform global receiver recovery

Three exact initial calibrations q_1=c nonzero, q_2=q_3=0, exact apparatus
energy H_0, and all ten final apparatus coordinates determine the entire
initial receiver state on a bounded convex domain. A fixed smooth pulse design
and a sufficiently small but fixed apparatus box about the calibrated centre
make the inverse uniform over that domain. Exact receiver energy is redundant.
The inverse amplifies record errors by at most a constant divided by coupling.

R30, 2026-09-12. Retain [R06](autonomous-finite-readout.md)'s Hamiltonian,
positive masses, coupled stable receiver, known T, smooth pulses and cutoff
margins. Use [R25](full-apparatus-preparation-ambiguity.md)'s free apparatus
shear S and full record G_lambda. Coordinates and norms below use fixed
positive component units; physical canonical units are L_* and P_*.
The receiver domain Z is a fixed compact convex energy ball H_s<=E_max,
with an open neighbourhood for derivatives. Its energy is not supplied.

Let eta_c have q_1=c, all other probe coordinates and momenta zero, and
clock (s_0,M_c v_0), v_0>0. Fix c first. The admitted apparatus states satisfy

$$\|\eta-\eta_c\|\le\rho,\qquad
q_1=c,\quad q_2=q_3=0,\quad
H_{\rm app}(\eta)=H_0=M_cv_0^2/2. \tag{1}$$

Here H_app is the free probe and clock kinetic energy, since the initial
interaction vanishes. The positive radius rho is chosen below, independently
of lambda. This is a box centred at eta_c, possibly smaller than R29's original
box. The theorem covers every state satisfying (1) in this box; it does not
assert recovery on the original larger box. All physical and record units,
pulse widths, masses, c, rho and T stay fixed in the precision limit.

## 1. Four independent leading rows

For free receiver motion x_w(t)=e_x Phi_t w at the nominal clock define

$$A_j(w)=\int_0^T t f_j(s_0+v_0t)x_w(t)\,dt,\qquad
B_1(w)=\int_0^T f_1(s_0+v_0t)\dot x_w(t)\,dt.$$

Choose the first two pulses as in [R29 §2](two-calibration-branches.md):
A_1,B_1,A_2 have rank three. Select a third time in a remaining open interval
where the output of their nonzero kernel vector is nonzero. Such a time
exists because the output is analytic and observable: its first four time
derivatives recover x,P,y,Q with nonzero diagonal coefficients
1,1/mu,g/mu,g/(mu nu). A sufficiently narrow positive third pulse therefore
makes A_3 nonzero on that kernel. All widths are fixed and positive.
The position rows A_1,A_2,A_3 are independent. To retain the additional R06
ordinary position-signal rank, make these choices first in the narrow-pulse
evaluation limit: the first three evaluation rows are independent, and analytic
observability selects a fourth disjoint time completing them. Then choose all
four positive widths sufficiently small to preserve both rank conditions.

In fixed output units the constant matrix

$$L=\begin{pmatrix}-K A_1/M_1\\-K A_2/M_2\\-K A_3/M_3\\-Kc B_1\end{pmatrix}
\tag{2}$$

is invertible. The nonzero displacement c is essential to its fourth row.
Pulse supports and the free nominal clock have strict endpoint margins.
After choosing pulses, reduce the apparatus neighbourhood and coupling to
preserve those margins, positive clock speed, bounded forces and linear cutoffs.

## 2. An inverse apparatus chart for every nearby record

Write F_lambda=S^{-1}G_lambda. On a fixed enlarged apparatus neighbourhood,
R25's smooth-flow estimates give

$$F_\lambda(w,\eta)=\eta+\lambda R_\lambda(w,\eta), \tag{3}$$

with R_lambda and the finitely many derivatives used below uniformly bounded
on a neighbourhood of Z, including small signed lambda. Fix a sufficiently
small radius r for this enlarged neighbourhood. For
||a-eta_c||<=r/2 and |lambda| sufficiently small, the map
eta -> a-lambda R_lambda(w,eta) is a contraction of the closed r-ball
about eta_c into itself, uniformly in w in Z. It defines the unique smooth
chart eta_lambda(w,a), with F_lambda(w,eta_lambda(w,a))=a and
eta_0(w,a)=a. Bounds on derivatives are uniform on a slightly smaller compact
product domain. All physical records use a=S^{-1}Y.

Choose rho<=r/8. Equation (3) and a further coupling restriction ensure that
all admitted records satisfy ||a-eta_c||<=r/4. The segment between any two
such a's stays inside the chart domain. The chart for counterfactual w may
leave the admitted rho-box; it remains in the enlarged smooth-flow domain.
This extension is what permits segment integration over the full convex Z.

## 3. A global margin for the exact constrained map

Set C(eta)=(q_1,q_2,q_3,H_app)(eta), in fixed output units. Define

$$D_\lambda(w,a)=
\frac{C(\eta_\lambda(w,a))-C(a)}{\lambda}. \tag{4}$$

The numerator vanishes identically at lambda=0 for every (w,a). Integrating
its coupling derivative from 0 to lambda gives a joint smooth extension,
including w and a derivatives. Subtracting C(a) is essential when the final
record varies; the divided constraint itself need not have a finite limit.

At a=eta_c the exact pointer drift identity and clock impulse calculation
in [R28 §1](calibrated-canonical-ambiguity.md) give

$$D_wD_0(w,\eta_c)=L \quad\hbox{for every }w\in Z. \tag{5}$$

Indeed each pointer row is -K A_j/M_j. Only q_1=c contributes to the
first-order clock energy variation. Integrating its f'_1 term by parts,
with pulse-free endpoints, gives -Kc B_1. Initial probe kinetic energy has
zero first derivative at eta_c. Receiver and clock reaction enter the exact
smooth remainder, rather than being discarded.

Uniform continuity on compact Z and invertibility of L allow r and then
the coupling ceiling to be reduced until, throughout the product chart,

$$\|L^{-1}(D_wD_\lambda(w,a)-L)\|\le\tfrac12. \tag{6}$$

This is a small-neighbourhood condition depending on c and the pulse design;
rho is chosen after it. Integrating along the receiver segment proves

$$\|w-w'\|\le2\|L^{-1}\|
\|D_\lambda(w,a)-D_\lambda(w',a)\|. \tag{7}$$

For two admitted preparations with the same record a, their C values equal
C_*=(c,0,0,H_0). Equations (4) and (7) force w=w'. The apparatus chart then
forces eta=eta'. Thus the full admitted preparation is globally recovered,
without a receiver energy-shell equation or a local branch label.

## 4. Record stability and the action-unit precision limit

For different admitted records a,a', their exact constraints imply

$$D_\lambda(w,a)=\frac{C_*-C(a)}{\lambda},\qquad
D_\lambda(w',a')=\frac{C_*-C(a')}{\lambda}.$$

Let M_C bound ||DC|| and M_D bound ||D_aD_lambda|| on the convex chart
record domain, uniformly in lambda. Apply (7) at a and insert the second
constraint to obtain

$$\|w-w'\|\le
2\|L^{-1}\|(M_C/\lambda+M_D)\|a-a'\|
\le\frac{K_z}{\lambda}\|Y-Y'\|,\quad0<\lambda\le\lambda_*. \tag{8}$$

The last constant includes ||S^{-1}|| and the fixed coupling ceiling.
The apparatus chart also gives
||eta-eta'||<=K_eta(||Y-Y'||+lambda||w-w'||), so its reconstruction is
stable on the same admitted class. Constants are independent of the actual
receiver state, preparation and small positive lambda.

For a measured record within delta of a true record, minimize record distance
over the compact admitted class (1) times Z. A minimizer exists, the true
state is a competitor, and its fitted record differs from the true one by
at most 2 delta. Therefore this deterministic estimator has

$$\epsilon_x\le2L_*K_z\delta/\lambda,\qquad
\epsilon_P\le2P_*K_z\delta/\lambda,\qquad
\epsilon_x\epsilon_P\le4L_*P_*K_z^2(\delta/\lambda)^2. \tag{9}$$

The product has action units ML^2/T, with no 2 pi factor. At fixed positive
coupling it tends to zero as final-record error tends to zero, while the
positive preparation width stays fixed. A joint weak-coupling limit is
controlled if delta/lambda tends to zero. These are upper bounds, not a
sharp conditioning or minimax claim. Supplied calibrations and apparatus
energy are exact; their errors require a separate stability analysis.

This settles a bounded-domain exclusion-of-zero test under the stated access
and preparation premises. It supplies no universal action parameter or quantum
identification. Source methods and their bounded coverage are recorded in
[B61](../references/batches/B61.md); novelty remains unassessed.

Next R31: allow errors in the three supplied calibrations and apparatus
energy. Determine which precision/coupling ratios suffice for recovery and
whether a fixed calibration tolerance restores an actual common-record
canonical ambiguity inside the same fixed box. Keep c bounded away from zero.
