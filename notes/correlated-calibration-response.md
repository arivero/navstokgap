# Correlated calibration errors suppress the canonical response

For the calibration direction r=L e_y, the exact common-record receiver
curve approaches a hidden-coordinate line as coupling tends to zero.
Its position and momentum diameters are O(min(lambda,epsilon)), rather than
the order-one weak-coupling diameters obtained for the coordinate directions
in R32. The first surviving canonical term is an explicit second coupling
derivative of the compensated calibration map.

R33, stage 1, 2026-09-12. Retain R32's selected fixed smooth pulses,
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
an assertion of exact constancy. The next stage evaluates (6)–(8) from the
mechanical variational equations, including the lambda-dependence of the
reference record. Equations (5) and (7) already establish canonical
suppression without assuming that this first coefficient is nonzero.
