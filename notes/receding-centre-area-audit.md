# The surviving area is the matched-endpoint arc–chord defect

Draft coordinator derivation for B11 review, 2026-09-07. The supplied Sol
commentary correctly computes a factor of two for a fixed parabola. A genuine
central-force family distinguishes two comparisons: arc versus its inertial
tangent, and arc versus its matched-endpoint chord. The latter supplies the
stable connection to the existing action calculation.

## 1. Exact signed-area identity

Put $C_R=(0,R)$ and orient increasing $x$ to the right and $y$ toward the
centre. For a path starting at the origin, define its signed sectorial area

$$A_R[\gamma]=\frac12\int_\gamma[x\,dy-(y-R)\,dx]
=\frac R2\Delta x+\frac12\int_\gamma(x\,dy-y\,dx).$$

For two paths with the same endpoints, the term proportional to $R$ cancels
exactly. Their area difference is the signed area of the closed loop formed
by the first path and the reversed second. This cancellation holds for every
centre, before taking any limit.

For the perpendicular constant-force parabola $x=vt$, $y=Ft^2/(2m)$,
$0\le t\le\tau$, $F,v,m,\tau>0$, the finite part is

$$A_{\rm lens}=\frac{Fv\tau^3}{12m}.$$

Its straight chord from the origin has $\int(x\,dy-y\,dx)=0$, so this is
the exact arc-minus-chord area. The inertial tangent $(vt,0)$ happens also
to give that subtraction for the fixed parabola, since both have the same
horizontal endpoint. Their vertical endpoints differ.

The positive ordinary areas satisfy

$$A_{\rm tangent,arc}=\frac{Fv\tau^3}{6m}=2A_{\rm lens},\qquad
A_{\rm tangent,chord}=\frac{Fv\tau^3}{4m}=3A_{\rm lens},$$

and hence $A_{\rm tangent,arc}=A_{\rm tangent,chord}-A_{\rm lens}$.
The plus sign in the supplied geometrical explanation reverses this ordering.

## 2. A genuine receding central force

Use the explicit classical family

$$m\ddot q_R=\frac FR(C_R-q_R),\quad
q_R(0)=(0,0),\quad\dot q_R(0)=(v,0),\qquad
\omega_R^2=\frac{F}{mR}.$$

The force is central for every finite $R$ and tends to the uniform field on
bounded spatial sets. The exact solution is

$$x_R(t)=\frac v{\omega_R}\sin(\omega_Rt),\qquad
y_R(t)=R[1-\cos(\omega_Rt)].$$

On every fixed compact time interval it tends to the parabola, while

$$x_R(\tau)=v\tau-\frac{Fv\tau^3}{6mR}+O(R^{-2}).$$

Angular momentum about $C_R$ is $mRv$, so the actual arc and the inertial
tangent each have signed sectorial area $Rv\tau/2$. Their difference is
exactly zero for every $R$. In the finite-part decomposition the missing term
is

$$\frac R2[x_R(\tau)-v\tau]\longrightarrow-\frac{Fv\tau^3}{12m},$$

which cancels the parabola's finite part. Substituting the limiting parabola
before subtracting the divergent reference therefore changes this comparison.

Let $\operatorname{ch}_R$ instead join the actual arc endpoints. Then

$$A_R[q_R]-A_R[\operatorname{ch}_R]
=\frac{Rv}{2}\left[\tau-\frac{\sin(\omega_R\tau)}{\omega_R}\right]
\longrightarrow\frac{Fv\tau^3}{12m}.$$

Thus a genuine receding-centre construction recovers the lens when the chord
shares the arc endpoints. This is a precise reusable version of the supplied
geometrical idea. It does not require an identification of the arc and tangent
sector differences in a varying central-force family.

## 3. Action normalization

For the constant-force Lagrangian $L=m|\dot q|^2/2+Fy$, the existing
matched-endpoint calculation gives

$$S[q_{\rm chord}]-S[q_{\rm cl}]
=\frac F{2v}A_{\rm lens}
=\frac{F^2\tau^3}{24m}
=\frac{\tau\Delta E_\perp}{12},\qquad
\Delta E_\perp=\frac{F^2\tau^2}{2m}.$$

The supplied identity $6(F/v)A_{\rm lens}=\tau\Delta E_\perp$ is also
correct. It uses twice the matched-endpoint action difference before the
factor six. Numerical normalization should be fixed rather than absorbed into
an undefined threshold. $\Delta E_\perp$ is deterministic transverse work,
distinct from a quantum energy uncertainty. Comparing the actual path to its
inertial tangent changes the terminal point and loses endpoint-gauge invariance.

## 4. Threshold versus exact quantization

With $h=2\pi\hbar$ and equal angular steps $\Delta\phi=2\pi/N$, the
inequality $J\Delta\phi\ge h$ gives $J\ge N\hbar$. For any positive
integer $N$, $J=(N+1/2)\hbar$ satisfies every one of these $N$ cell bounds
and closes the angle at $2\pi$, while lying off the asserted action lattice.
An exact tiling assumption is therefore an extra premise in the supplied
Claude argument. A threshold on comparison-path defects also requires an
explicit map before being applied to orbital action-angle cells.

For the supplied Kepler spectrum write $E_N=-A/N^2$, $A>0$.
If $\omega_N=\hbar^{-1}dE_N/dN$ and $T_N=2\pi/\omega_N$, then

$$\frac{(E_{N+1}-E_N)T_N}{h}
=\frac{N(2N+1)}{2(N+1)^2}\longrightarrow1.$$

The finite difference approaches the frequency rule; the derivative relation
is exact. These algebraic checks assess the supplied conditional model and
leave its physical selection premise explicit.

## 5. Research use

Use the arc–chord construction in A03's nonuniform cut-point test. State the
refinement law, conserved endpoint data, action normalization and physical
condition proposed to exclude a vanishing remainder. Keep a supplied minimum
cell axiom as a separate comparison branch. Historical attribution follows the
Newton passage audit, not the modern calculation.
