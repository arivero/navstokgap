# Correlated calibration errors suppress the canonical response

For the calibration direction r=L e_y, the exact common-record receiver
curve approaches a hidden-coordinate line as coupling tends to zero.
Its position and momentum diameters are O(min(lambda,epsilon)), rather than
the order-one weak-coupling diameters obtained for the coordinate directions
in R32. The second coupling derivative is a homogeneous quadratic map: its tangent
at zero vanishes by signed-coupling symmetry. Explicit pulse integrals now
reduce the first possible canonical curvature to a two-component test.

R33, stages 1–2, 2026-09-12. Retain R32's selected fixed smooth pulses,
preparation box and receiver energy ball. Use fixed component units throughout;
e_y is the unit vector of the receiver's hidden position coordinate. The
physical canonical conversion factors remain L_* and P_*. The final record
is the exact coupled reference Y_lambda=G_lambda(0,eta_c). Statements below
concern its local compatible curve, not minimax risk over all final records.

## 1. Specify the correlated report

Keep C_* as the report and admit precisely

$$C(\eta)-C_* = \alpha r,\qquad |\alpha|\le\epsilon,
\qquad r=L e_y. \tag{1}$$

The scalar alpha and epsilon use this fixed normalization of r; rescaling r
requires the reciprocal rescaling of their units. Equivalently, any rank-three
linear map with kernel span(r) imposes three exact complementary constraints,
while a linear functional taking value one on r bounds the remaining scalar.
Thus (1) is a correlated line of calibration uncertainty, not four independent
error intervals. The direction, pulses and physical box stay fixed as lambda
varies. Apparatus and receiver energies are bounded as before; receiver energy
is not supplied exactly.

Use R32's divided exact calibration map T_lambda and inverse chart. A fixed
local interval supplies

$$w_\lambda(s)=T_\lambda^{-1}(s r),\qquad
|s|\le s_\epsilon:=\min(s_0,\epsilon/\lambda). \tag{2}$$

The corresponding apparatus has the same ten final coordinates and
C-C_*=lambda s r exactly. At zero coupling T_0=L, hence

$$w_0(s)=s e_y,\qquad w_\lambda(0)=0. \tag{3}$$

Take s_0 sufficiently small to lie strictly inside the receiver ball and
reduce only the coupling ceiling to keep the compensator in the fixed box.

## 2. Uniform canonical suppression on this fibre

Smooth inverse dependence on (lambda,s) and (3) imply, for a fixed K_1,

$$\|\partial_s w_\lambda(s)-e_y\|\le K_1\lambda,
\qquad \|w_\lambda(s)-s e_y\|\le K_1\lambda |s|. \tag{4}$$

The first bound follows by integrating the bounded mixed derivative
partial_lambda partial_s w from zero to lambda. Integrating in s proves the
second, including its factor |s| uniformly at the reference point.

Let R_x^loc and R_P^loc denote the optimal absolute errors when the receiver
is known to lie on the compact segment (2) and the data are this common
record and report. For a scalar coordinate the optimal error is half its
range, attained by the midpoint of its extrema. Equation (4) gives

$$R_x^{\rm loc}\le L_*K_1\lambda s_\epsilon,\qquad
R_P^{\rm loc}\le P_*K_1\lambda s_\epsilon,$$
$$R_x^{\rm loc}R_P^{\rm loc}\le L_*P_*K_1^2
\min(\lambda s_0,\epsilon)^2. \tag{5}$$

At fixed positive tolerance these conditional risks tend to zero in the
weak-coupling limit, although the receiver family retains a finite hidden-y
extent. This upper bound on a selected fibre is not a global estimator bound
for the full preparation class: other final records can have different
response directions.

## 3. The derivative that decides the surviving response

Define, using the exact apparatus chart and coupled reference a_lambda,

$$N(\lambda,w)=C(\eta_\lambda(w,a_\lambda))-C_*,\qquad
V(w)=\tfrac12\partial_\lambda^2N(0,w). \tag{6}$$

Since N(0,w)=0, N(lambda,0)=0 and partial_lambda N(0,w)=Lw,
smooth Taylor expansion gives T_lambda(w)=Lw+lambda V(w)+O(lambda^2),
with V(0)=0. Differentiating T_lambda(w_lambda(s))=s r yields

$$w_\lambda(s)=s e_y-\lambda L^{-1}V(s e_y)
                 +O(\lambda^2|s|). \tag{7}$$

The remainder is uniform on a smaller fixed s interval: Taylor-expand the
smooth inverse in lambda in the C^1 norm in s, then use w_lambda(0)=0.
Thus the first-order canonical coefficient is

$$b(s)=-\Pi_{x,P}L^{-1}V(s e_y),\qquad
b'(0)=-\Pi_{x,P}L^{-1}(D V(0))e_y. \tag{8}$$

The projection in (8) is in component units, before multiplication by L_*
and P_*. If both components of b'(0) are nonzero, uniform continuity of
their derivatives and (7) gives, after reducing s_0 and the coupling ceiling,

$$R_x^{\rm loc}R_P^{\rm loc}\ge
\frac{L_*P_*}{4}|b'_x(0)b'_P(0)|\lambda^2s_\epsilon^2. \tag{9}$$

Endpoint differences prove (9) just as in R32, now with an extra lambda in
each derivative. A zero coefficient calls for further terms, rather than
an assertion of exact constancy. Sections 4–5 evaluate (6)–(8) from the mechanical variational equations,
including the lambda-dependence of the reference record; both entries in (8)
vanish for this model. Equations (5) and (7) already establish canonical
suppression without assuming that this first coefficient is nonzero.

## 4. Mechanical symmetry cancels the proposed tangent coefficient

For the selected mechanics, both entries in (8) vanish exactly:
$D V(0)=0$. The first correction can instead bend the fibre quadratically
in s. This settles the tangent test posed in stage 1 without asserting exact
canonical constancy at positive coupling.

Work inside the fixed linear-cutoff neighbourhood supplied by R30, so that
X(x)=x and R(q_j)=q_j along all trajectories used here. Choose a smaller
symmetric receiver neighbourhood and signed coupling interval if necessary.
The receiver equations are linear with forcing -lambda K sum f_j(s)q_j
in the P equation; apparatus forces are -lambda K f_j(s)x and
-lambda K sum f'_j(s)xq_j. Consequently changing (lambda,z) to
(-lambda,-z), leaving the apparatus unchanged, maps solutions to solutions.
Uniqueness gives

$$G_{-\lambda}(-w,\eta)=G_\lambda(w,\eta),\qquad
Y_{-\lambda}=Y_\lambda.$$

The unique compensated preparation therefore obeys
$\eta_{-\lambda}(-w,a_{-\lambda})=\eta_\lambda(w,a_\lambda)$.
Thus N(-lambda,-w)=N(lambda,w), V(-w)=V(w), and D V(0)=0.
In particular J_lambda=D_w T_lambda(0) is even in lambda and
$J_\lambda=L+O(\lambda^2)$. The canonical tangent of the exact fibre at
s=0 is O(lambda squared), rather than the potentially nonzero order-lambda
term of stage 1. This is a symmetry of the signed parameter family; physical
couplings remain positive.

## 5. Explicit quadratic response from terminal variational equations

The following quadratures determine V for the actual fixed positive-width
pulses. All quantities in this section first use physical coordinates and
units. Apply the fixed input/output unit conversions before multiplying by
the component matrix L in (7). Write f_j(t)=f_j(s_0+v_0 t), with primes
meaning derivatives with respect to the clock position, and x_w(t)=e_x Phi_t w.
Use expansion coefficients u=u^(0)+lambda u^(1)+lambda squared u^(2)+...;
the second coefficient is half the second derivative.

On the common-record trajectory the first apparatus variations have zero
terminal values. Indeed the nominal receiver is zero at order zero, so
its reference apparatus record has no first coupling derivative. Integration
backwards from T gives, for all four probes,

$$u_j(t):=q_j^{(1)}(t)
=-\frac K{M_j}\int_t^T (r-t)f_j(r)x_w(r)\,dr,$$
$$k_j(t):=\pi_j^{(1)}(t)=K\int_t^T f_j(r)x_w(r)\,dr,$$
$$h(t):=s^{(1)}(t)
=-\frac{Kc}{M_c}\int_t^T(r-t)f'_1(r)x_w(r)\,dr,$$
$$\ell(t):=p_s^{(1)}(t)=Kc\int_t^T f'_1(r)x_w(r)\,dr. \tag{10}$$

These solve u_j''=-K f_j x_w/M_j and h''=-Kc f'_1 x_w/M_c
with both terminal position and momentum variations zero. Their initial
values are the first compensating preparation coefficients. In particular
v_0 ell(0)=-Kc B_1(w), by integration by parts and pulse-free endpoints,
recovering the fourth row of L with its sign.

The first receiver variation is independent of w:

$$z^{(1)}(t)=-Kc\int_0^t\Phi_{t-r}e_P f_1(r)\,dr,\qquad
z^{(1)}(0)=0. \tag{11}$$

Here e_P inserts a force in the canonical momentum equation. Equation (11)
holds also for the moving coupled reference. To display its contribution,
put xi(t)=e_x z^(1)(t). The reference's second apparatus coefficients at T
are

$$\bar q_j^{(2)}(T)=-\frac K{M_j}\int_0^T(T-t)f_j(t)\xi(t)dt,\qquad
\bar\pi_j^{(2)}(T)=-K\int_0^T f_j(t)\xi(t)dt,$$
$$\bar s^{(2)}(T)=-\frac{Kc}{M_c}\int_0^T(T-t)f'_1(t)\xi(t)dt,\qquad
\bar p_s^{(2)}(T)=-Kc\int_0^T f'_1(t)\xi(t)dt.$$

Thus a_lambda=eta_c+lambda squared a_2+O(lambda to the fourth), where a_2
is S^{-1} applied to this terminal coefficient vector; in particular
partial_lambda a(0)=0 and partial_lambda squared a(0)=2a_2. The initial
reference preparation remains eta_c; a_lambda is its preconditioned final
record, not its preparation. At second order subtract that reference trajectory.
The terminal apparatus differences are then zero and
the common terms involving x^(1) cancel. Writing Delta for this subtraction,
the remaining second-coefficient equations are

$$\Delta\ddot q_j^{(2)}=-\frac K{M_j}f'_j h x_w,$$
$$\Delta\dot p_s^{(2)}=-K\left(c f''_1 h x_w+
                  \sum_{j=1}^4 f'_j x_w u_j\right). \tag{12}$$

The reference preparation is eta_c at every lambda, so its second initial
coefficient is zero. Backward integration of (12), followed by expansion of
the initial kinetic energy, therefore gives the physical components of V:

$$V_j(w)=-\frac K{M_j}\int_0^T t f'_j(t)h(t)x_w(t)\,dt,
\qquad j=1,2,3,$$
$$V_4(w)=v_0 K\int_0^T\left(c f''_1 h x_w+
                 \sum_{j=1}^4 f'_j x_w u_j\right)dt
       +\frac{\ell(0)^2}{2M_c}
       +\sum_{j=1}^4\frac{k_j(0)^2}{2M_j}. \tag{13}$$

For example V_j has length units, and every term in V_4 has energy units.
The squared first-order momenta in (13) are necessary even though nominal
probe momenta vanish. Subtracting the moving reference before (12) is what
removes the w-independent forced-receiver terms; a free-reference calculation
would retain incorrect constants. Since x_w,h,u_j,k_j,ell are linear in w,
(13) makes V a homogeneous quadratic map, strengthening the parity argument.
In particular V(s e_y)=s squared V(e_y), with e_y interpreted in the fixed
receiver component units.

## 6. Curvature is the next nonvanishing test

Put beta=-Pi_(x,P) L^{-1}V(e_y) in component units. Equations (7) and (13)
yield, uniformly for |s|<=s_0,

$$\Pi_{x,P}w_\lambda(s)=\lambda s^2\beta
                              +O(\lambda^2|s|). \tag{14}$$

For S=s_epsilon there is a fixed constant K_2 such that

$$R_x^{\rm loc}R_P^{\rm loc}
\le L_*P_*K_2^2(\lambda S^2+\lambda^2 S)^2. \tag{15}$$

This follows by bounding each coordinate relative to its value zero at s=0;
half its range is at most its maximum absolute value. If both beta components
are nonzero and S/lambda is sufficiently large, comparison of s=0 with s=S
in (14) gives the conditional lower bound

$$R_x^{\rm loc}R_P^{\rm loc}
\ge\frac{L_*P_*}{16}|\beta_x\beta_P|\lambda^2 S^4. \tag{16}$$

For each coordinate the remainder is at most half its leading value in this
regime, and the radius is at least half the separation, explaining 1/16.
Explicitly, if each component remainder is bounded by M lambda squared |s|,
it suffices that S/lambda >= 2M/min(abs(beta_x),abs(beta_P)).
The two endpoints -S and S cancel the displayed quadratic term, so the
stage-1 endpoint test cannot establish (16). The beta nonvanishing condition
has not been established for R32's pulse family. When S is comparable to or
smaller than lambda, higher coupling terms can compete and (16) is not
asserted. At fixed positive tolerance, S=s_0 for sufficiently weak coupling.

The next bounded task is to evaluate the two projected quadratures beta for
an explicitly fixed admissible early-pulse design, with finite-width control.
If either vanishes, examine the next coupling coefficient. This step advances
the exclusion-of-zero test for a preparation-dependent conditional canonical
risk; it supplies neither global recovery nor a universal positive action.
