# Calibrated two-energy records still hide both canonical coordinates

A fixed smooth pulse design admits an exact common-record receiver curve with
nonzero variation in both initial x and P, despite a known nonzero q_1=c,
exact initial energies E,H_0, and all ten final apparatus coordinates at known
T. Its two endpoints give a positive canonical risk product, uniformly for
sufficiently weak positive coupling at fixed preparation width. The result is
an existence construction within R27's apparatus class; arbitrary pulse designs
require the rank test below.

R28, 2026-09-12. Retain [R06](autonomous-finite-readout.md)'s Hamiltonian,
K, positive masses, coupled receiver g>0, cutoff regions and endpoint pulse
margins. Retain [R27](calibrated-displacement-ambiguity.md)'s preparation:
H_s=E>0, H_app=H_0=M_c v_0^2/2, q_1=c nonzero, |c|/L_1<b/4, and every
remaining apparatus coordinate allowed in the fixed box of half-width b.
Choose the fixed pulse design as in section 2 before decreasing lambda.
All coordinate norms used for smoothness and margins use fixed component units.
The canonical errors below retain physical length and momentum units.

## 1. Two scaled constraints on the exact compensator

Let eta_c have q_1=c, all other probe coordinates and momenta zero, and clock
(s_0,M_c v_0). For a receiver shell point z_bar to be chosen below set
Y_lambda=G_lambda(z_bar,eta_c). R25's inverse-shear contraction, centred now
at eta_c, gives a smooth compensator eta_lambda(w) on a fixed neighbourhood
of z_bar with

$$G_\lambda(w,\eta_\lambda(w))=Y_\lambda,\qquad
\|\eta_\lambda(w)-\eta_c\|\le 2L\lambda\|w-z_{\rm bar}\|. \tag{1}$$

The chart may include an ambient receiver neighbourhood when taking
derivatives. Reducing lambda preserves a b/2 margin from the original box
boundary: eta_c is already within b/4 of its centre. Smoothness follows from
the invertible apparatus derivative and smooth finite-time flow. In particular
eta_0(w)=eta_c and eta_lambda(z_bar)=eta_c exactly.

Write h(t)=f_1(s_0+v_0t), x_w(t)=e_x Phi_t w and define linear functionals

$$A(w)=\int_0^T t h(t)x_w(t)\,dt,\qquad
B(w)=\int_0^T h(t)\dot x_w(t)\,dt. \tag{2}$$

On the compensator the additional calibration and energy conditions have
smooth extensions at lambda=0 after division by lambda:

$$U_\lambda(w)=\frac{q_1(\eta_\lambda(w))-c}{\lambda},\qquad
V_\lambda(w)=\frac{H_{\rm app}(\eta_\lambda(w))-H_0}{\lambda},$$
$$U_0(w)=-\frac K{M_1}A(w-z_{\rm bar}),\qquad
V_0(w)=-Kc B(w-z_{\rm bar}). \tag{3}$$

To verify signs and weights, Hamilton's equations give exactly
q_1(T)-T pi_1(T)/M_1=q_1(0)+(lambda K/M_1) integral t f_1(s(t))x(t) dt.
Matching the final record and differentiating at zero coupling gives U_0.
At eta_c only the first probe has a nonzero free displacement, so the first
clock impulse is -lambda Kc integral f'_1(s_0+v_0t)x_w(t) dt.
Matching final clock momentum requires initial momentum difference
+lambda Kc integral f'_1(x_w-x_bar) dt. Initial apparatus energy has first
variation v_0 times this difference; initial probe kinetic energies have zero
first variation. Integration by parts, with h zero at both endpoints, gives
V_0 in (3). Changes of the clock trajectory and receiver forcing enter only
higher orders in this first variation. Smooth divisibility follows by writing
each numerator as lambda times the integral of its coupling derivative.
Explicitly, for either smooth numerator N with N(0,w)=0, its extension is
integral from 0 to 1 of partial_lambda N(theta lambda,w) d theta. This is
jointly smooth in (lambda,w), including all receiver derivatives. The smooth
Hamiltonian flow also exists on a small signed coupling neighbourhood for
this analytic argument; physical states use only positive lambda.
Thus the three exact equations to solve are

$$H_s(w)=E,\qquad U_\lambda(w)=0,\qquad V_\lambda(w)=0. \tag{4}$$

## 2. A fixed pulse with a canonical direction in its kernel

There is a smooth nonnegative first pulse for which A,B are independent and
W=ker A intersect ker B contains a vector v with v_x v_P nonzero. Here v is
a receiver displacement per unit dimensionless curve parameter, not clock speed.

Choose a small time tau strictly between 0 and T. In the design limit of a
pulse concentrated near tau, writing I=integral h>0, the normalized rows
A/(tau I), B/I tend to e_x Phi_tau and e_x D Phi_tau, where D is the free
receiver generator. These rows specify x(tau) and P(tau)/mu and have rank two.
The vector

$$v^{(0)}=\Phi_{-\tau}(0,0,Y,0),\qquad Y>0 \tag{5}$$

lies in their kernel. The receiver equations give, by Taylor expansion,

$$v_x^{(0)}=\frac{gY}{2\mu}\tau^2+O(\tau^4),\qquad
v_P^{(0)}=-gY\tau+O(\tau^3). \tag{6}$$

Both are nonzero for sufficiently small fixed tau. Fix that tau. A sufficiently
narrow but positive smooth pulse width preserves rank two and a nearby kernel
vector with both components nonzero. For example, project v^(0) onto the
perturbed kernel using the continuous orthogonal projection in fixed units.
The positive mass and g>0 are used in (6); a decoupled receiver need not pass
this test. After this design choice, neither tau nor width varies with lambda.

The other three R06 pulses can retain an invertible four-momentum signal
matrix. The evaluation row at tau extends to a basis of four evaluation rows:
analytic observability spans all four dimensions even after excluding small
neighbourhoods of previously chosen times. Choose those times, then all four
positive widths sufficiently small with disjoint supports to preserve the
basis and the first pulse kernel property. There is therefore no conflict
between this construction and the original apparatus's calibrated readout rank.
Indeed, a vector annihilated by the evaluation rows on any remaining open
interval has analytic output identically zero. Its first four derivatives
at zero recover x,P,y,Q with nonzero diagonal coefficients
1,1/mu,g/mu,g/(mu nu), as shown in R06 section 2. Such a vector must vanish.

## 3. Continue a shell curve to positive coupling

Let H_s(w)=w^T J w/2 with J positive definite. The two-dimensional plane W
contains v above. Choose a nonzero z_bar in W with z_bar^T J v=0, and rescale
it so H_s(z_bar)=E. This is possible because J restricts to a positive
inner product on W. The rows

$$dH_s(z_{\rm bar}),\quad A,\quad B \tag{7}$$

are independent: A,B are independent and vanish on W, whereas
 dH_s(z_bar)[z_bar]=2E. Their common kernel is exactly span(v).
The nonzero constants K/M_1 and Kc in (3) preserve this rank.

Choose a linear parameter functional ell with ell(v)=1. Apply the implicit
function theorem to (4) and ell(w-z_bar)=t, at (lambda,t,w)=(0,0,z_bar).
The four by four w derivative is invertible by (7). It supplies a smooth
curve w_lambda(t) for |t|<=delta and 0<=lambda<=lambda_1, with delta,lambda_1
positive and fixed, such that

$$w_\lambda(0)=z_{\rm bar},\qquad
\partial_t w_0(0)=v. \tag{8}$$

For an explicit uniform neighbourhood, set
F_lambda(w)=(H_s(w)-E,U_lambda(w),V_lambda(w),ell(w-z_bar)), scaling each
output by a fixed positive unit. Let D_*=D_w F_0(z_bar). Joint smoothness
and invertibility allow a receiver ball of radius rho and a coupling interval
on which ||D_*^{-1}(D_w F_lambda-D_*)||<=1/2. Since F_lambda(z_bar)=0,
the map w -> w-D_*^{-1}(F_lambda(w)-(0,0,0,t)) is a contraction and maps
that ball to itself whenever ||D_*^{-1}(0,0,0,t)||<=rho/2. This supplies
one fixed positive t interval and the same joint smooth branch as the IFT.

For positive lambda every point has the exact two energies and calibrated
q_1=c, and (1) makes all ten final records exactly Y_lambda. Choose a compact
subrectangle of the implicit-function neighbourhood and reduce lambda_1 so
(1) leaves the b/2 box margin there. The same compact flow neighbourhood
preserves positive clock speed, linear cutoffs and pulse-free endpoints.
This proves actual admissible states, including all nonlinear reaction terms.

By continuity, shrink delta and lambda_1 once more so both canonical
derivatives keep the signs of v_x,v_P and magnitudes at least |v_x|/2,
|v_P|/2 throughout that rectangle. Integrating from -delta to delta gives

$$|w_\lambda(\delta)_x-w_\lambda(-\delta)_x|\ge\delta|v_x|,
\qquad
|w_\lambda(\delta)_P-w_\lambda(-\delta)_P|\ge\delta|v_P|. \tag{9}$$

## 4. Canonical risk, scope and next question

For any deterministic estimator from the complete record and supplied
calibration/energies, let epsilon_x,epsilon_P be its separate worst-case
absolute errors on the admitted constrained preparation class. Applying the
triangle inequality at the two common-record endpoints in (9) proves

$$\epsilon_x\ge\frac{\delta|v_x|}{2},\qquad
\epsilon_P\ge\frac{\delta|v_P|}{2},\qquad
\epsilon_x\epsilon_P\ge\frac{\delta^2|v_xv_P|}{4}>0. \tag{10}$$

The product has units ML^2/T with no 2 pi normalization. The same fixed bound
holds for all 0<lambda<=lambda_1 and hence for the liminf of the optimal risk
product as lambda decreases. Its constants depend on E,c,b, masses and pulse
design. No uniform assertion is made under cooling, shrinking preparation,
c tending to zero, or varying the design. A curve and its two endpoints do
not establish positive projected area or exact minimax constants. This
settles the existence branch of R28 and advances the exclusion-of-zero test
for this prepared information class; universal scale selection and quantum
identification remain open.

Source capsule: R25/B56's parameter-dependent compensator and inherited
smooth-flow/inverse methods -> divide the two residual constraints by coupling
-> test the rank on an actual receiver energy shell. R27/B58's topological
result motivated locating ambiguity in canonical coordinates; its theorem is
not used in this proof. [B59](../references/batches/B59.md) records the bounded
method audit; [review](../reviews/calibrated-canonical-B59.md) separates written
proof acceptance from literature status.

Next R29: reveal a second initial probe displacement q_2=0, retaining the
same two energies and full final record. Its additional scaled row is
integral t f_2(s_0+v_0t)x_w(t) dt. Test whether the resulting three linear
constraints plus receiver energy give a local inverse and whether distinct
global common-record pairs remain. An isolated solution is not by itself
global recovery.
