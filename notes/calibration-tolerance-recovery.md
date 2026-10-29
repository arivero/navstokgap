# Preparation, calibration and exact-record fibres of a classical apparatus

For the finite autonomous apparatus, exact final records can hide a whole
receiver shell when incoming apparatus phase is unknown. Two initial energies
and one or two probe-position calibrations still permit actual common-record
canonical alternatives in selected fixed designs. Three calibrated positions
and apparatus energy instead give global recovery on a sufficiently small
fixed box. Finite calibration tolerance restores ambiguity with matched
risk-product order $\min\{1,(\varepsilon/\lambda)^2\}$. The direction of
uncertainty matters: a correlated line can hide only an internal coordinate
at leading order, and its first canonical tangent cancels exactly.

These results consolidate C090–C093, C096–C101 and C106–C123 by their
common inverse construction. The apparatus and its smooth-flow estimates
are specified once in [the readout treatment](autonomous-finite-readout.md).
Historical written coordinator/model checks are internal checks, not external
peer review; literature novelty is unassessed. Distinct rank, topology and
energy hypotheses below must not be inferred from one another.

## Common apparatus chart and the meaning of risk

Use the receiver $z=(x,P,y,Q)$, energy $H_s=z^TGz/2$, clock and four probes
of the readout treatment. Put $k_x=a-g^2/d>0$. All norms use fixed component
units $L_*,P_*$ for the canonical receiver coordinates. Let $\eta$ be all ten
initial apparatus coordinates, $G_\lambda(z,\eta)$ their ten final coordinates
at known $T$, and $S$ the free apparatus shear

$$(q_j,\pi_j,s,p_s)\mapsto
(q_j+T\pi_j/M_j,\pi_j,s+Tp_s/M_c,p_s).$$

On convex compact receiver/apparatus enlargements with strict cutoff and
pulse margins, smooth finite-time flow gives

$$F_\lambda:=S^{-1}G_\lambda=\eta+\lambda R_\lambda(z,\eta),\qquad
\|D_\eta F_\lambda-I\|\le C\lambda\le\tfrac12,
\quad\|D_zF_\lambda\|\le L\lambda.$$

Derivatives of every finite order used below are bounded on smaller compact
domains, including a small signed coupling interval. At a prescribed record
$a=S^{-1}Y$, the map $\eta\mapsto a-\lambda R_\lambda(z,\eta)$ is a
contraction on an enlarged apparatus ball for $a$ near its centre. It defines
a unique smooth inverse apparatus chart $\eta_\lambda(z,a)$, with
$\eta_0(z,a)=a$. If $Y=G_\lambda(z_*,\eta_*)$, then

$$G_\lambda(w,\eta_\lambda(w))=Y,\qquad
\|\eta_\lambda(w)-\eta_*\|\le2L\lambda\|w-z_*\|.$$

Indeed $\eta\mapsto\eta-F_\lambda(w,\eta)+F_\lambda(z_*,\eta_*)$
contracts the radius-$b/2$ ball about $\eta_*$ into itself whenever
$\|w-z_*\|\le b/(4L\lambda)$. Its centre moves by at most $b/4$,
its derivative norm is at most $1/2$, and its fixed point has the displayed
bound. This includes exact nonlinear clock reaction. Counterfactual chart
values may leave a smaller physical box while remaining in the enlarged
smooth domain; segment proofs use this extension explicitly.

For a deterministic estimator let $\epsilon_x,\epsilon_P$ be separate global
worst-case errors. A common-record pair with coordinate separations
$\Delta x,\Delta P$ forces $\epsilon_x\ge|\Delta x|/2$ and
$\epsilon_P\ge|\Delta P|/2$. These need not be errors on the same motion.
A smooth curve may have positive coordinate-risk product but zero projected
planar area. All products here have action units $ML^2/T$, without a $2\pi$
factor, and are reconstruction risks, not accuracy–disturbance inequalities.
Correlated choices used in a lower bound select points from the admitted
Cartesian support; no probability law or positive probability for a fibre
is assumed.

## Incomplete records and preparation width

First retain only four final probe momenta. Unknown incoming probe momenta
$u$ have derivative $D_uG=I+O(\lambda)$, while $D_zG=O(\lambda)$.
The same contraction hides every shell point within $b/(4L\lambda)$ of
$z_*$. At $z_*=(0,0,\sqrt{2E/d},0)$ the exact shell chart is

$$w(x,P)=\left(x,P,\frac gd x+
 \sqrt{\frac{2E-k_xx^2-P^2/\mu}{d}},0\right).$$

Choose $r_0,C_0>0$ so its square $|x|\le L_*r_0$, $|P|\le P_*r_0$
has positive radicand and
$\|w-z_*\|\le C_0\max(|x|/L_*,|P|/P_*)$. Then one record hides the
whole square with

$$r=\min\{r_0,b/(4LC_0\lambda)\},\qquad
\epsilon_x\epsilon_P\ge L_*P_*r^2,\quad
\operatorname{area}_{x,P}\ge4L_*P_*r^2.$$

At fixed coupling the small-width rate is $b^2$, matching the calibrated
upper bound. At fixed width the displayed lower bound saturates as coupling
weakens. No exact total apparatus energy has yet been imposed.

If incoming momenta are revealed at zero but incoming positions $q$ remain
unknown, the response has two coupling factors. With
$h(t)=e_x\Phi_te_P$, $h(0)=0$, $h'(0)=1/\mu$, and
$f_j(t)=f_j(s_0+v_0t)$, its exact leading matrix is

$$D_qG_\lambda=\lambda^2B(z)+O(\lambda^3),$$
$$B_{jk}=K^2\int_0^T f_j(t)\int_0^t h(t-u)f_k(u)dudt
 +\frac{K^2}{M_c}\int_0^T f'_j(t)x^0(t)
   \int_0^t(t-u)f'_k(u)x^0(u)dudt.$$

It follows by differentiating receiver and clock equations in $q_k$:
$\partial_{q_k}x=-\lambda K\int_0^t h(t-u)f_k(u)du+O(\lambda^2)$
and $\partial_{q_k}s=-\lambda K M_c^{-1}\int_0^t(t-u)f'_k(u)x^0(u)du+
O(\lambda^2)$. In particular the clock term cannot be discarded.
Ordered disjoint pulses make $B$ lower triangular. Select independent signal
times avoiding the isolated zeros of the nonzero analytic history at $z_*$.
For $f_j(t)=\phi((t-t_j)/\delta)$, fixed smooth nonzero $\phi\ge0$,

$$B_{jj}=-\frac{K^2x^0(t_j)^2\delta}{M_cv_0^2}\int\phi^2
 +O(\delta^2).$$

The receiver term is $O(\delta^3)$. For the clock term substitute scaled
pulse variables: the inner integral of $(r-s)\phi'(s)$ is
$\int_{-\infty}^r\phi$, and integration by parts gives $-\int\phi^2$.
Choose sufficiently small positive $\delta$ once, making $B_*$ invertible.
Preconditioning by $(\lambda^2B_*)^{-1}$ gives a contraction when
$\|w-z_*\|\le\lambda b/(4C)$, with $C\ge\|B_*^{-1}\|L$.
The same shell square now has

$$r=\min\{r_0,\lambda b/(4CC_0)\},\qquad
\epsilon_x\epsilon_P\ge L_*P_*r^2,\quad
\operatorname{area}_{x,P}\ge4L_*P_*r^2.$$

This is a design-existence result, not a consequence of ordinary signal rank
for every pulse design. Its lower bound closes as $\lambda^2$ at fixed $b$;
that does not prove the full risk tends to zero. Complete final pointer
positions with known clock data instead give global recovery by
[the readout inverse](autonomous-finite-readout.md#complete-records-replace-clock-preparation-data).

## Full records, whole-shell saturation and exact energies

With the entire incoming apparatus box unknown, the common ten-record chart
at the start applies without any signal-rank assumption. On $H_s=E$ let
$D=\max\|w-z_*\|$. If

$$0<\lambda\le\min\{\lambda_0,b/(4LD)\},$$

one complete record hides the entire shell, with a $b/2$ box margin. Its
canonical projection is exactly $k_xx^2+P^2/\mu\le2E$: completing the
energy square proves necessity, and the shell chart with the remaining
energy in $y$ proves sufficiency. The constant estimator $(0,0)$ attains
both coordinate lower bounds, hence

$$R_x=\sqrt{2E/k_x},\quad R_P=\sqrt{2\mu E},\quad
\inf\epsilon_x\epsilon_P=2E\sqrt{\mu/k_x}.$$

The projected area is $\pi R_xR_P$. The stiffness $k_x$ is an energy
projection coefficient, not asserted to be a normal-mode stiffness. At fixed
$\lambda$ the local patch closes with $b$; the saturation condition cannot
then be kept as $b\to0$.

Supplying apparatus energy $H_0=M_cv_0^2/2$ removes many compensators, but
not all ambiguity. Prescribe terminal zero probes, clock position $s_0+v_0T$,
and

$$z(T)=r\Phi_Tz_*,\qquad
p_s(T)=\sqrt{2M_c[H_0+E(1-r^2)]}.$$

Backward exact flow has initial receiver $Z_\lambda(r)$ with $Z_0(r)=rz_*$.
The derivative of $H_s(Z_0(r))-E$ at $r=1$ is $2E>0$, so an implicit
$r_\lambda$ makes initial receiver energy exactly $E$. Endpoint interactions
vanish; total-energy conservation makes apparatus energy exactly $H_0$.
Terminal zero probes give initial probe phase $O(\lambda)$ and receiver/clock
reaction $O(\lambda^2)$, so
$r_\lambda=1+O(\lambda^2)$ and $Z_\lambda=z_*+O(\lambda^2)$.
At fixed positive box width both preparations fit within half its margin.

Inside the linear cutoff regions $(z,q,\pi)\mapsto(-z,-q,-\pi)$ leaves
the clock and equations invariant. Terminal zero probes therefore give the
same complete apparatus record for $Z_\lambda$ and $-Z_\lambda$, with both
energies equal. Global oddness of cutoffs is unnecessary. Choose
$z_*=(\sqrt{E/k_x},\sqrt{\mu E},(g/d)\sqrt{E/k_x},0)$. Then

$$\epsilon_x\epsilon_P\ge|(Z_\lambda)_x(Z_\lambda)_P|
 \longrightarrow E\sqrt{\mu/k_x}>0.$$

For small coupling the bound is at least one quarter of this limit.
This two-point construction asserts neither exact minimax saturation nor
positive area. Its positive scale closes with receiver energy.

## Clock fibres and local versus global recovery

Keep incoming momenta known at zero and only eight final pointer records.
Their scaled map is $(-A_cz,q)+O_{C^1}(\lambda)$. The implicit-function
theorem solves equal records as

$$z_0(c)=A_c^{-1}A_{c_0}z_*,\quad q_0(c)=0,\qquad
H_s(z_\lambda(c))=E.$$

Interior pulse support gives $\partial_sA=-AM/v$ by integration by parts.
Thus $\partial_sz_0=Mz_*/v_0$ and the offset derivative of energy is zero.
To obtain a transverse speed direction choose early pulses
$f_j(s)=\phi((s-s_0-v_0\epsilon a_j)/(v_0\epsilon\eta))$, with distinct
positive $a_j$ and fixed sufficiently small $\eta>0$. The moment matrix
$W_{jn}=\int\phi((u-a_j)/\eta)u^n/n!\,du$, $n=0,1,2,3$, is invertible
by its Vandermonde limit. With $r=v_0/v$,

$$\det A_{s_0,v}=D(r\epsilon)^{10}(1+O(\epsilon)),\quad D\ne0,
\qquad\operatorname{tr}(-A^{-1}\partial_vA)=10/v_0+O(\epsilon)>0.$$

The exponent is four time integrations plus derivative orders $0+1+2+3$;
the analytic expansion holds also with one speed derivative. Fix sufficiently
small positive $\epsilon$ once. Positive trace implies the symmetric energy
form of $B=-A^{-1}\partial_vA$ has a positive direction: its $G$-normalized
trace equals $\operatorname{tr}B$. Select a shell point in its open positive
set avoiding $P=0$ and $-ax+gy=0$. Then $z_*^TGBz_*>0$ and both canonical
entries of $Mz_*$ are nonzero. Solve energy for $v=v_\lambda(s)$:

$$v'_\lambda(s_0)=O(\lambda),\qquad
z'_\lambda(s_0)=Mz_*/v_0+O(\lambda).$$

On a fixed offset interval $|s-s_0|\le\sigma$ the two canonical derivatives
retain signs and magnitudes at least $k_x',k_P'>0$.
Speed/position compensations are $O(\lambda\sigma)$ and fit fixed positive
boxes. Its common-record endpoints imply
$\epsilon_x\epsilon_P\ge k_x'k_P'\sigma^2>0$. This curve has no implied
positive projected area. Revealing offset alone removes this family locally
through the transverse energy derivative, as proved in
[the local inverse](autonomous-finite-readout.md#energy-assisted-local-recovery-and-its-global-obstruction).

On the whole shell, two speed branches remain possible. Factor the early
pulse matrix before inversion, with $O$ having rows $e_xM^n$:

$$-A^{-1}\partial_vA=\frac1{v_0}O^{-1}\operatorname{diag}(1,2,3,4)O
 +O(\epsilon).$$

The factored analytic tail and its derivative are $O(\epsilon)$ after
removing the fixed moment matrix and powers of $r\epsilon$; a vanishing
determinant estimate alone would not justify this inverse limit. Its leading
map sends $z$ to
$(x,2P,3y-2ax/g,4Q-2a\nu P/(g\mu))/v_0$. At $Q=0$ its energy form is

$$v_0z^TGB^{(0)}z=g(x-y)(9x-5y)+2P^2/\mu.$$

Choose $L,p>0$ with $2p^2/\mu<4gL^2/5$. The normalized shell path through
$(L,p,rL,0)$, $0\le r\le7/5$, has opposite endpoint energy-response signs
and positive canonical coordinates. Fix the design and then a sufficiently
small speed separation $d_v>0$. At zero coupling equal records require
$z'=A_{v_0+d_v}^{-1}A_{v_0}z=z+d_vBz+O(d_v^2)$; the energy mismatch
changes sign along the path while both canonical separations exceed positive
$c_xd_v,c_Pd_v$. At positive coupling the invertible $(z',q')$ record
derivative continues this compact path uniformly with $O(\lambda)$ changes.
Endpoint signs and margins persist; intermediate value gives an actual
exact equal-energy, equal-record pair. For small coupling

$$\epsilon_x\epsilon_P\ge c_xc_Pd_v^2/16>0.$$

This is an actual pair, not an inference from a zero tangent. Reading final
clock momentum instead restores global recovery; reading its final position
also replaces initial offset. Those inverse theorems and their precision
constants are in the readout treatment.

## Calibration constraints reduce to receiver rank

Fix a nonzero initial displacement $q_1=c$, small enough to lie within one
quarter of the original apparatus box. Let $\eta_c$ have this displacement,
all other probe coordinates zero, and nominal clock phase. The inverse
apparatus chart centred there compensates any receiver in a bounded domain
for sufficiently small coupling relative to the box width.

Before using pulse rank, there is a design-independent full-state obstruction
under $H_s=E$, $H_{\rm app}=H_0$, $q_1=c$. Solve

$$p_s=\sqrt{2M_c(H_0-\sum_j\pi_j^2/(2M_j))},\qquad
 y=\frac gd x+\sqrt{(2E-k_xx^2-P^2/\mu-Q^2/\nu)/d}.$$

The free chart coordinates are $x,P,Q,q_2,q_3,q_4,\pi_1,\ldots,\pi_4,s$,
eleven in total. A fixed radius-$r$ Euclidean ball fits with strict radicands
and half-box margins. Its boundary $S^{10}$ maps continuously to the ten
final records. Borsuk–Ulam gives antipodal chart parameters with equal records.
Equal-record ambient estimates imply
$\|\Delta\eta\|_2\le2L\lambda\|\Delta z\|_2$. Since chart coordinates
are an orthogonal projection of fixed-unit initial coordinates,

$$R_z\ge\frac{r}{\sqrt{1+4L^2\lambda^2}}>0.$$

This is a dimensionless full receiver-state risk. Separation may be in $y,Q$;
it does not prove a canonical product. The chart antipodes do not reverse
$c$, so the broken sign involution is not being reused.

For canonical constructions set $Y_\lambda=G_\lambda(\bar z,\eta_c)$ and
write $\eta_\lambda(w)$ for its compensator. Define

$$A_j(w)=\int_0^Tt f_j(s_0+v_0t)x_w(t)dt,\qquad
B_1(w)=\int_0^Tf_1(s_0+v_0t)\dot x_w(t)dt.$$

Dividing calibration and energy residuals by coupling gives smooth limits

$$\frac{q_j(\eta_\lambda(w))-q_j(\eta_c)}\lambda
 \longrightarrow-\frac K{M_j}A_j(w-\bar z),\qquad
\frac{H_{\rm app}(\eta_\lambda(w))-H_0}\lambda
 \longrightarrow-KcB_1(w-\bar z).$$

The exact drift identity is
$q_j(T)-T\pi_j(T)/M_j=q_j(0)+(\lambda K/M_j)\int t f_j(s)xdt$.
Matching final clock momentum gives the initial clock-impulse difference;
its energy variation is $v_0$ times that impulse. Integration by parts turns
$\int f'_1xdt$ into $-\int f_1\dot xdt/v_0$, proving the energy row and
its sign. Initial zero probe momenta have no first-order kinetic-energy
variation. For every smooth numerator $N$ vanishing at zero coupling,
$N/\lambda=\int_0^1\partial_\lambda N(\theta\lambda,\cdot)d\theta$,
which proves joint smooth divisibility, including receiver derivatives.

With only $q_1=c$, a narrow fixed pulse near a small $\tau>0$ makes the
two rows $A_1,B_1$ approximate $x(\tau),\dot x(\tau)$ after nonzero
normalization. Their kernel contains a vector close to
$\Phi_{-\tau}(0,0,Y,0)$, with

$$v_x=gY\tau^2/(2\mu)+O(\tau^4),\qquad
v_P=-gY\tau+O(\tau^3),$$

both nonzero. In their two-dimensional kernel $W$, choose
$\bar z\ne0$ $G$-orthogonal to $v$, scaled to $H_s=E$. Then
$dH_s(\bar z),A_1,B_1$ have rank three and common kernel $\mathbb Rv$.
Adding a parameter functional $\ell(v)=1$ gives an invertible four-equation
implicit system. It continues an actual common-record shell curve
$w_\lambda(t)$, $|t|\le\delta$, with $w_\lambda(0)=\bar z$ and
$\partial_tw_0(0)=v$. One fixed compact parameter/coupling rectangle retains
half the two canonical derivative magnitudes and half-box apparatus margins.
Its endpoints therefore give

$$\epsilon_x\epsilon_P\ge\delta^2|v_xv_P|/4>0.$$

This pulse design can retain the ordinary four-signal matrix: analytic
observability completes the first evaluation row with three disjoint times.
The result is existence within the design class, not every pulse design.

Adding $q_2=0$ gives the third row $A_2$. Pulses near $\tau,2\tau$ have a
rank-three kernel obtained from state $(0,0,Y,Q)$ at $\tau$, with $Q>0$ and
$Y=-Q\tau/(3\nu)+O(\tau^3)$ to make $x(2\tau)=0$. Backward expansion gives

$$v_x=-gQ\tau^3/(3\mu\nu)+O(\tau^5),\qquad
v_P=5gQ\tau^2/(6\nu)+O(\tau^4).$$

Fix positive widths preserving both nonzero entries and rank. Scale $v$ to
$\bar z$ on the shell. At zero coupling the three linear constraints and
energy have two roots $\pm\bar z$, with invertible derivatives because
$dH_s(\pm\bar z)[\pm\bar z]=2E$. The exact compensated system continues
both roots as $w_+=\bar z$, $w_-=-\bar z+O(\lambda)$. They have the same
full record, energies and calibrations, with margins, and

$$\epsilon_x\epsilon_P\ge\tfrac14|(w_+-w_-)_x(w_+-w_-)_P|
 \longrightarrow|\bar z_x\bar z_P|>0.$$

Each root is locally stably recoverable at each fixed positive coupling:
eliminate the invertible apparatus-to-record derivative in the augmented
fourteen-coordinate map; its Schur derivative is the four-equation residual
derivative, with the three divided rows multiplied by $\lambda$. It remains
invertible. A sufficiently small convex neighbourhood gives a local lower
Lipschitz estimate. These neighbourhoods/constants need not be uniform as
$\lambda\to0$. Two local inverses do not give global recovery.

## Four exact supplied constraints give a global inverse

Take a bounded convex receiver energy ball $Z=\{H_s\le E_{\max}\}$ and
$C(\eta)=(q_1,q_2,q_3,H_{\rm app})$, with supplied
$C_*=(c,0,0,H_0)$. Choose the third pulse nonzero on the preceding
one-dimensional kernel, and a fourth completing the ordinary signal matrix.
Analytic observability on any remaining interval guarantees both choices;
choose positive widths preserving them. In fixed output units the matrix

$$L=\begin{pmatrix}-KA_1/M_1\\-KA_2/M_2\\-KA_3/M_3\\-KcB_1\end{pmatrix}$$

is invertible. Nonzero $c$ is essential. The physical apparatus box is now
centred at $\eta_c$ with sufficiently small fixed half-width $\rho>0$,
chosen after design. This may be smaller than the preceding two-branch box;
no recovery theorem on that original larger box is claimed.

For all nearby records use the enlarged inverse apparatus chart and define

$$D_\lambda(w,a)=
 [C(\eta_\lambda(w,a))-C(a)]/\lambda.$$

Subtracting $C(a)$ is necessary for joint smoothness when the record varies.
At $a=\eta_c$ its zero-coupling receiver derivative is exactly $L$ for
every $w\in Z$. Uniform continuity permits a chart radius and then coupling
ceiling such that

$$\|L^{-1}(D_wD_\lambda-L)\|\le\tfrac12.$$

Choose $\rho$ inside that chart (for example at most one eighth the enlarged
radius), so all physical records and their segments stay in its domain.
Receiver segment integration gives

$$\|w-w'\|\le2\|L^{-1}\|
 \|D_\lambda(w,a)-D_\lambda(w',a)\|.$$

For equal records and exact $C=C_*$ the right side is zero. This proves
uniform global recovery over the whole bounded domain, without supplying
receiver energy or a local branch label. For different records, bounds
$M_C\ge\|DC\|$, $M_D\ge\|D_aD_\lambda\|$ give

$$\|w-w'\|\le2\|L^{-1}\|(M_C/\lambda+M_D)
 \|S^{-1}\|\|Y-Y'\|\le K_z\|Y-Y'\|/\lambda.$$

The apparatus chart also bounds its own error by
$K_\eta(\|Y-Y'\|+\lambda\|w-w'\|)$.
Minimum-residual fitting on the compact admitted class with record error
$\delta$ yields
$\epsilon_x\epsilon_P\le4L_*P_*K_z^2(\delta/\lambda)^2$.
This is an upper bound with supplied exact calibration and exact model.

## Tolerances, exact ambiguity and matched crossover

Allow a reported $C_{\rm obs}$ with
$\|C(\eta)-C_{\rm obs}\|\le\varepsilon$, independently of final-record
error $\delta$. The same inverse comparison, using actual $C_1,C_2$, gives

$$\|w-w'\|\le\frac K\lambda
 (\|C_1-C_2\|+\|Y-Y'\|).$$

Choose any compact feasible preparation consistent with both data bands;
it exists because the true preparation is feasible (sequential coordinate
minimization makes a deterministic choice). Thus

$$\|\widehat w-w\|\le2K(\varepsilon+\delta)/\lambda,\qquad
\epsilon_x\epsilon_P\le4L_*P_*K^2
 ((\varepsilon+\delta)/\lambda)^2.$$

This covers separate component tolerances via their maximum. The matching
ball below allows positive tolerance in all four components; some exactly
known components require the directional test in the next section.

At the reference record $Y_\lambda=G_\lambda(0,\eta_c)$, differentiate the
inverse chart:
$D_w\eta_\lambda=-(D_\eta F_\lambda)^{-1}D_wF_\lambda$.
It follows that $\|\eta_\lambda(w)-\eta_c\|\le B\lambda\|w\|$,
$B=2L$. Set $R_Z=\max_Z\|w\|$ and $M_C>0$. Reduce the fixed coupling
ceiling until $B\lambda R_Z\le\rho/2$, also retaining actual $q_1$ away
from zero. Then the same complete record and reported $C_*$ hide the entire
dilated receiver ball $tZ$, where

$$t=\min\{1,\varepsilon/(M_CB\lambda R_Z)\}.$$

Indeed its calibration difference is at most $M_CB\lambda\|w\|$.
With $X_E=\sqrt{2E_{\max}/k_x}$ and $P_E=\sqrt{2\mu E_{\max}}$,
common-record coordinate endpoints force
$\epsilon_x\ge tX_E$, $\epsilon_P\ge tP_E$. For exact final records,
combine the feasible-estimator upper bound with the constant-zero estimator
in each coordinate. The optimal product has matched order

$$\min\{1,(\varepsilon/\lambda)^2\}$$

with fixed positive action-unit constants. At $\varepsilon=0$ exact recovery
holds. If $\varepsilon\ge M_CB\lambda R_Z$, the whole ball is hidden and
$R_x=X_E$, $R_P=P_E$, $\inf\epsilon_x\epsilon_P=X_EP_E$ exactly; its
projected ellipse has area $\pi X_EP_E$. This is a sufficient saturation
threshold, not a sharp crossover constant. At fixed coupling improved
calibration/record precision closes the product; at fixed positive tolerance
weak coupling saturates it. Receiver energy is not supplied here.

## One uncertain constraint and an explicit pulse design

Use the exact coupled reference above, $a_\lambda=S^{-1}Y_\lambda$, and

$$T_\lambda(w)=[C(\eta_\lambda(w,a_\lambda))-C_*]/\lambda.$$

It satisfies $T_\lambda(0)=0$, $T_0(w)=Lw$, and
$J_\lambda=D_wT_\lambda(0)=L+O(\lambda)$. The moving reference matters:
$T_\lambda=D_\lambda(w,a_\lambda)-D_\lambda(0,a_\lambda)$.
Uniform inverse-function estimates give a fixed interval and actual curve

$$w_{\lambda,j}(s)=T_\lambda^{-1}(se_j),\qquad
|s|\le S:=\min\{s_0,\varepsilon/\lambda\}.$$

It has exactly one uncertain calibration, $C-C_*=\lambda se_j$, all other
constraints exact, and one full final record. Its tangent is
$d_j+O(\lambda)$, $d_j=L^{-1}e_j$. If $(d_j)_x(d_j)_P\ne0$, a smaller
fixed neighbourhood preserves half both derivative magnitudes. Endpoints give

$$\epsilon_x\epsilon_P\ge
 \tfrac14L_*P_*|(d_j)_x(d_j)_P|S^2.$$

The preceding upper bound still holds with three zero tolerances, giving
matched order $\min\{1,(\varepsilon/\lambda)^2\}$. A zero leading entry
calls for higher-order analysis, not an assertion of recovery. Every smooth
projected curve patch has zero planar area despite positive coordinate risks.

All four column tests can hold in one fixed design. Choose pulse centres
$\tau,2\tau,3\tau$ with small fixed $\tau>0$. The output equation is
$x^{(4)}+\alpha x''+\beta x=0$, where
$\alpha=a/\mu+d/\nu$, $\beta=(ad-g^2)/(\mu\nu)$.
In scaled initial-jet coordinates
$(x,\tau\dot x,\tau^2\ddot x/2,\tau^3x^{(3)}/6)$,
$X(u)=x(\tau u)$ solves
$X^{(4)}+\alpha\tau^2X''+\beta\tau^4X=0$.
Integration on $[0,3]$ makes the map
$(x(\tau),x(2\tau),x(3\tau),\tau\dot x(\tau))$ an $O(\tau^2)$
perturbation of cubic Hermite interpolation. Its cardinal polynomials are

| Output | Cardinal polynomial | Initial value | Initial derivative |
| --- | --- | --- | --- |
| 1 | $(u-2)(u-3)(3u-1)/4$ | $-3/2$ | $23/4$ |
| 2 | $-(u-1)^2(u-3)$ | $3$ | $-7$ |
| 3 | $(u-1)^2(u-2)/4$ | $-1/2$ | $5/4$ |
| 4 | $(u-1)(u-2)(u-3)/2$ | $-3$ | $11/2$ |

A homogeneous cubic with roots $1,2,3$ and derivative zero at $1$ vanishes,
so this map is invertible. Substitution and differentiation verify the table.
Initial momentum is $\mu/\tau$ times the second entry. For pulse integrals
$I_j>0$, normalize calibration rows by
$\sigma_j=-KI_jj\tau/M_j$ ($j=1,2,3$) and
$\sigma_4=-KcI_1/\tau$. Their narrow-pulse limits are those Hermite rows.
With support half-width at most $h<\tau/4$, mean-value bounds on
$(te(t))'/(j\tau)$ and $\tau e''(t)$ give a normalized matrix error
$\|N-\mathcal H_\tau\|\le C_\tau h$. If
$\|\mathcal H_\tau^{-1}\|C_\tau h<1/2$, the inverse identity gives

$$\|N^{-1}-\mathcal H_\tau^{-1}\|
 \le2\|\mathcal H_\tau^{-1}\|^2C_\tau h.$$

Fix $h$ so this is below half the smallest of the eight nonzero canonical
entries. Both determinants and all column tests persist. Analytic
observability supplies a fourth disjoint ordinary signal pulse. The widths
are now positive and fixed; no shrinking-pulse physical limit enters the risk
theorem. For another design the exact tests are the two cofactors
$\operatorname{cof}_{j,1}(L),\operatorname{cof}_{j,2}(L)$ being nonzero.

## Correlated uncertainty and the corrected quadratic response

Instead admit the fixed calibration line
$C-C_*=\alpha r$, $|\alpha|\le\varepsilon$, $r=Le_y$, with this scalar
normalization. It is not four independent error intervals. Its local
reference-record curve is

$$w_\lambda(s)=T_\lambda^{-1}(sr),\quad |s|\le S,
\qquad w_0(s)=se_y,\quad w_\lambda(0)=0.$$

Bounded mixed derivatives give
$\|w_\lambda(s)-se_y\|\le K_1\lambda|s|$.
For this compact common-record segment alone, optimal scalar error is half
the coordinate range, so
$R_x^{\rm loc}R_P^{\rm loc}\le L_*P_*K_1^2\min(\lambda s_0,\varepsilon)^2$.
This is a conditional local-fibre estimate, not a global estimator bound.

Set $N(\lambda,w)=C(\eta_\lambda(w,a_\lambda))-C_*$ and
$V(w)=\tfrac12\partial_\lambda^2N(0,w)$. Smooth inverse expansion gives

$$w_\lambda(s)=se_y-\lambda L^{-1}V(se_y)+O(\lambda^2|s|).$$

The proposed nonzero tangent coefficient is actually zero. In the fixed
linear cutoff region coupling/receiver reversal gives
$G_{-\lambda}(-w,\eta)=G_\lambda(w,\eta)$ and
$Y_{-\lambda}=Y_\lambda$. Uniqueness of the inverse chart implies
$N(-\lambda,-w)=N(\lambda,w)$, hence $V$ is even and $DV(0)=0$.
Moreover $J_\lambda$ is even, so $J_\lambda=L+O(\lambda^2)$.
The canonical tangent at the reference is $O(\lambda^2)$.

For completeness the actual finite-width quadratic coefficient is determined
by terminal quadratures. In physical units put $x_w=e_x\Phi_tw$ and use
expansion coefficients $u=u^{(0)}+\lambda u^{(1)}+\lambda^2u^{(2)}+\cdots$.
The first apparatus variations, with zero terminal data, are

$$u_j(t)=-\frac K{M_j}\int_t^T(r-t)f_j(r)x_w(r)dr,
\quad k_j(t)=K\int_t^Tf_j(r)x_w(r)dr,$$
$$h(t)=-\frac{Kc}{M_c}\int_t^T(r-t)f'_1(r)x_w(r)dr,
\quad\ell(t)=Kc\int_t^Tf'_1(r)x_w(r)dr.$$

The first receiver variation is independent of $w$,
$z^{(1)}(t)=-Kc\int_0^t\Phi_{t-r}e_Pf_1(r)dr$. It also occurs in the
moving coupled reference. If $\xi=e_xz^{(1)}$, the reference's second
terminal coefficients are the integrals
$-K\int f_j\xi$, $-K\int(T-t)f_j\xi/M_j$ for probe momentum/position,
and $-Kc\int f'_1\xi$, $-Kc\int(T-t)f'_1\xi/M_c$ for the clock.
Thus $a_\lambda=\eta_c+\lambda^2a_2+O(\lambda^4)$, with $a_2$ the
inverse free shear applied to that vector. This is its final preconditioned
record; the reference's initial preparation stays exactly $\eta_c$.

Subtract the moving reference before second-order backward integration.
The common $x^{(1)}$ terms cancel, leaving

$$\Delta\ddot q_j^{(2)}=-Kf'_jh x_w/M_j,\qquad
\Delta\dot p_s^{(2)}=-K(c f''_1h x_w+\sum_j f'_jx_wu_j).$$

The resulting calibration coefficients are

$$V_j(w)=-\frac K{M_j}\int_0^Tt f'_j(t)h(t)x_w(t)dt\quad(j=1,2,3),$$
$$V_4(w)=v_0K\int_0^T(c f''_1h x_w+\sum_jf'_jx_wu_j)dt
 +\frac{\ell(0)^2}{2M_c}+\sum_j\frac{k_j(0)^2}{2M_j}.$$

The squared momenta are necessary initial kinetic-energy terms. Length/energy
units match the respective outputs; convert them to the fixed component
units before applying $L^{-1}$. All first variations in these integrals are
linear in $w$, so $V$ is homogeneous quadratic, not just even. A free-reference
calculation would retain incorrect constant forcing terms.

With $\beta=-\Pi_{x,P}L^{-1}V(e_y)$ this yields

$$\Pi_{x,P}w_\lambda(s)=\lambda s^2\beta+O(\lambda^2|s|),\qquad
R_x^{\rm loc}R_P^{\rm loc}
 \le L_*P_*K_2^2(\lambda S^2+\lambda^2S)^2.$$

If both $\beta$ entries are nonzero and each remainder is bounded by
$M\lambda^2|s|$, then $S/\lambda\ge2M/\min(|\beta_x|,|\beta_P|)$
permits comparison of $s=0$ with $s=S$, giving

$$R_x^{\rm loc}R_P^{\rm loc}\ge
 L_*P_*|\beta_x\beta_P|\lambda^2S^4/16.$$

Opposite endpoints cancel the quadratic term and cannot prove this bound.
Nonvanishing of both projected quadratures for the selected pulse family
remains unproved. For $S$ comparable to or smaller than coupling, higher
coupling terms may compete; the displayed lower bound is not asserted.

## Sources and consequence for STATE

The imported ingredients are smooth ODE dependence, contraction/inverse
methods, Borsuk–Ulam, observability and Hermite interpolation. Their bounded
source coverage and internal claim checks are retained in
[B48](../references/batches/B48.md)–[B66](../references/batches/B66.md),
with the detailed terminal-response capsules in
[B65](../references/batches/B65.md) and [B66](../references/batches/B66.md).
The constrained charts, exact compensators, pulse matrices and quadratures
above are the model derivations; no literature priority is claimed.

For STATE, positive preparation-relative risk, universal action selection,
and identification with physical $\hbar$ remain different claims. Whole-shell,
energy-constrained, local-curve and global-recovery hypotheses are explicit
here. Further calibration stages are parked by
[action-scale obstructions](action-unit-dimensional-selection.md#observables-and-the-admissible-class); the conditional
curvature test is retained without treating it as an active proof of necessity.
