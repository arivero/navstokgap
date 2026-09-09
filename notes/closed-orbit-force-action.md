# Closed trajectories: action from total turning and persistent excitation

Every regular closed Newtonian or special-relativistic trajectory with a
uniform speed floor and force ceiling has a positive canonical orbit-action
bound. The circular bound of C059 is sharp in this larger class. A18,
C060–C061; written proof and bounded B32 source review.

## Domain and action

Let $q:\mathbb R/T\mathbb Z\to\mathbb R^d$, $d\ge2$, be $C^2$, with
$v(t)=|\dot q(t)|\ge v_*>0$. In the relativistic case require $v(t)<c$,
and set $p=m\gamma\dot q$, $\gamma=(1-v^2/c^2)^{-1/2}$, $m>0$.
In the Newtonian case set $p=m\dot q$. Assume $|\dot p|\le F_{\max}$
for a fixed $F_{\max}>0$. Periodicity includes matching endpoint tangents.
Self-intersections are allowed. All assumptions concern one inertial frame.

Define the normalized canonical orbit action

$$J=\frac1{2\pi}\int_0^T p\cdot\dot q\,dt
  =\frac1{2\pi}\int_0^T P(v)v\,dt,$$

where $P(v)=m\gamma v$ or $mv$. This equals $(2\pi)^{-1}\oint p\cdot dq$
for a scalar-potential Hamiltonian with canonical momentum as specified.
For forces involving a vector potential, mechanical and canonical momentum
need separate treatment. The object here is orbit action, rather than an
arbitrary Hamilton-action difference or a general covariance determinant.

## Total-turning estimate

Write $n=\dot q/v$ for the unit tangent and
$\mathcal K=\int_0^T|\dot n|dt$ for total curvature. The classical Fenchel
theorem for a closed regular curve gives $\mathcal K\ge2\pi$. For arclength
$s$, $|\dot n|dt=|dn/ds|ds$, identifying this integral with the source's
total curvature. [B32](../references/batches/B32.md) verifies Milnor's
Theorem 3.4 and the smooth-curve identification.
Since $p=P(v)n$ and $n\cdot\dot n=0$,

$$|\dot p|^2=\dot P^2+P^2|\dot n|^2,
\qquad |\dot n|\le\frac{F_{\max}}{P(v)}
\le\frac{F_{\max}}{P_*},\quad P_*=P(v_*).$$

Integrating and then using monotonicity of $P(v)v$ proves

$$
T\ge\frac{P_*\mathcal K}{F_{\max}},\qquad
J\ge\frac{P_*^2v_*}{F_{\max}}\frac{\mathcal K}{2\pi}
\ge\frac{P_*^2v_*}{F_{\max}}.
$$

Thus the relativistic bound is
$m^2v_*^3/[F_{\max}(1-v_*^2/c^2)]$ and its Newtonian counterpart is
$m^2v_*^3/F_{\max}$. The units are action; $T$ retains units of time.
This extends C059 to noncentral forces and noncircular closed trajectories,
provided their momenta and force bounds satisfy the stated domain.

## Sharpness within smooth force-bounded mechanics

A circle at speed $v_*$ and radius $R_*=P_*v_*/F_{\max}$ has
$\mathcal K=2\pi$, $|\dot p|=F_{\max}$ and
$J=P_*R_*=P_*^2v_*/F_{\max}$. It can be realized by a smooth globally
force-bounded confining central potential, rather than only a prescribed force
along the orbit. Choose a smooth nondecreasing cutoff $\chi:[0,\infty)\to[0,1]$
equal to zero for $s\le1/4$ and to one for $s\ge1/2$, and set

$$V(r)=F_{\max}\int_0^r\chi(s/R_*)\,ds.$$

The potential is constant near the origin and linear at large radius, so its
Cartesian version is smooth and confining, with $|\nabla V|\le F_{\max}$.
At $r=R_*$ the circular force balance holds exactly. This realizes equality
in the claimed bound with a complete regular orbit and fixed model parameters.
It proves sharpness over the admissible model class, not attainability in
every preassigned potential.

## What the bound asks of the physical programme

Closedness supplies total turning. The force ceiling limits how quickly
momentum can turn. The speed floor turns that duration into an action cost.
These premises have separate roles. At fixed $m,F_{\max}$ the bound tends
to zero as $v_*\downarrow0$, consistently with C058's small circles.
The relativistic correction tends to the Newtonian value as $c\to\infty$.

A19 should test a weaker excitation premise suitable for oscillations that
stop at turning points: can a fixed peak momentum or kinetic excursion,
together with the force ceiling and periodicity, supply a positive action
bound? This would replace the pointwise speed floor by an observable excursion.
Its physical origin and any universal value remain a separate selection task.
