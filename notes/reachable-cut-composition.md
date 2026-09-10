# Reachable information across a classical cut

An unobserved cut preserves the bounded-force endpoint region exactly when
position and momentum cross the cut jointly. An exact phase-state observation
replaces the hidden horizon by the remaining time. A position observation leaves
an explicitly calculable momentum interval and a larger terminal area.

R08, 2026-09-10. C072–C073 accepted by [written review](../reviews/cut-composition-B39.md);
[B39 literature audit](../references/batches/B39.md) records derived
specializations with novelty unassessed. This continues [R07](causal-force-information.md) with the same mass,
force class and total horizon. The areas below use ordinary canonical measure
$dq\,dp$, with action units $ML^2/T$ and no $2\pi$ normalization.

## 1. Fixed experiment and exact composition

Let $m,F,T>0$, $\dot q=p/m$, $\dot p=f$, and allow every measurable input
$|f|\le F$ on $[0,T]$, with known initial state $x_0=(q_0,p_0)$.
No probability law is imposed. Define $S_t(q,p)=(q+tp/m,p)$ and

$$K_t=\left\{\left(\frac1m\int_0^t(t-s)f(s)ds,
\int_0^tf(s)ds\right):|f|\le F\right\}.$$

For $t>0$, R07 proves that $K_t$ is the lens

$$|d|\le1,\quad |z-d/2|\le(1-d^2)/4,
\qquad d=\frac{v}{Ft},\quad z=\frac{mu}{Ft^2},$$

with area $A(t)=2F^2t^3/(3m)$. Set $K_0=\{0\}$.
For a cut $a\in(0,T)$ and $b=T-a$, exact reachability gives

$$\boxed{K_T=S_bK_a+K_b.}$$

Here $+$ is Minkowski addition. Splitting each force integral at $a$ proves
one inclusion. Conversely, any two admissible segment inputs concatenate into
an admissible full input and realize their sheared sum. The rectangular input
class (no cross-time constraints beyond the pointwise ceiling) is the premise
used in this converse. The same argument proves composition for any finite
partition and any initial set by union over its states.

Thus eliminating an unobserved node leaves $S_Tx_0+K_T$ unchanged on every
mesh. Its area stays $A(T)$ at fixed $F,m,T$ even as the mesh tends to zero.
Adding the segment areas would be incorrect: $A(a)+A(b)<A(T)$; the sheared
Minkowski sum retains the joint alternatives.

## 2. What discarding the joint state loses

Replacing $K_a$ by its marginal rectangle

$$B_a=[-Fa^2/(2m),Fa^2/(2m)]\times[-Fa,Fa]$$

strictly enlarges the propagated endpoint set $S_bB_a+K_b$.
For example take the spurious corner $(-Fa^2/(2m),Fa)$ and future input
$+F$. Its terminal momentum increment is $FT$, while its position increment
is $F(-a^2/2+ab+b^2/2)/m$. Every genuine force with impulse $FT$ equals
$F$ almost everywhere, and therefore has position increment $FT^2/(2m)$.
The discrepancy is $Fa^2/m>0$. This proves strict enlargement for every
interior cut without a numerical test.

Position alone is not a closed state: the same cut position can admit different
momenta, which produce different future positions under the same future force.
It can still be used in an exact description if its compatible momentum fibre
or equivalent history is retained. The failure concerns deleting that data.

## 3. Observed cuts and exact conditional area

Observations here are ideal, exact, non-disturbing records available for the
terminal prediction. They change the observer's information; no recording
apparatus or propagation law is inferred. The underlying force class stays fixed.

If the full cut state $x_a$ is observed and reachable, its conditional terminal
set is $S_bx_a+K_b$: any admissible future can follow an admitted past.
Its area is exactly $A(b)$, independently of the observed value. The separate
coordinate minimax errors are $Fb^2/(2m)$ and $Fb$ as in R07.

If only $q_a$ is observed, put

$$\zeta=\frac{m(q_a-q_0-p_0a/m)}{Fa^2}\in[-1/2,1/2].$$

Solving the two lens inequalities at fixed $z=\zeta$ gives the exact fibre

$$p_a\in I_\zeta=p_0+Fa[d_-,d_+],\qquad
 d_-=1-\sqrt{2-4\zeta},\quad d_+=-1+\sqrt{2+4\zeta}.$$

Indeed the upper lens boundary is $1/2-(d-1)^2/4$, giving the lower
endpoint; the lower boundary is $(d+1)^2/4-1/2$, giving the upper endpoint.
Both endpoints lie in $[-1,1]$, and all intermediate points are reachable.
The interval width is

$$D(\zeta)=Fa\,[\sqrt{2-4\zeta}+\sqrt{2+4\zeta}-2].$$

The conditional terminal set and its area are

$$\boxed{E_\zeta=\{(q_a+bp/m,p):p\in I_\zeta\}+K_b,\qquad
|E_\zeta|=\frac{2F^2b^3}{3m}+\frac{Fb^2}{m}D(\zeta).}$$

For the area proof apply the determinant-one shear $(q,p)\mapsto(q-bp/m,p)$.
The added segment becomes vertical of length $D$. Every nonempty vertical
section of the sheared convex lens is an interval, so addition increases its
length by $D$. Its horizontal projection has width $Fb^2/m$, since
$u-bv/m=-m^{-1}\int_0^bsf(s)ds$ ranges between $\pm Fb^2/(2m)$.
Integration of the sections proves the formula, including $D=0$.

Consequently a central position record $\zeta=0$ leaves width
$2(\sqrt2-1)Fa$; an extreme position $|\zeta|=1/2$ determines momentum
exactly and leaves area $A(b)$. For every interior $\zeta$ and $b>0$, the
position-conditioned area is strictly greater than the phase-conditioned area.
Every conditional set is a subset of the original endpoint set by construction.

## 4. Refinement and the scale-selection obligation

Unobserved refinement keeps $A(T)$ fixed because it supplies no new record.
With successively available exact phase records whose latest time approaches
$T$, the residual area is $A(b)\to0$. Even a single exact position record at
$a=T-b$ gives

$$|E_\zeta|\le\frac{2F^2b^3}{3m}
 +2(\sqrt2-1)\frac{F^2ab^2}{m}\longrightarrow0$$

uniformly over its admissible value. The width bound follows from concavity
and symmetry of the two square roots. This area closure does not imply
momentum recovery: at $\zeta=0$, $D\to2(\sqrt2-1)FT$.
Area alone can vanish by collapse of one coordinate while the other stays
uncertain. No individual trajectory receives a positive action lower bound.

The next bounded test, R09, replaces exact cut positions by a deterministic
error interval of half-width $\varepsilon$. Derive the terminal set and its
area as $b,\varepsilon\to0$, keeping the force class fixed; test which
information or apparatus premise could prevent closure. This follows the
source-inspired compatibility question in the [ancient-cut note](ancient-cuts-provenance.md).
