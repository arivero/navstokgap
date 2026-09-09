# Relativistic Kepler: a singular-core angular-action threshold

Regular bound motion in the fixed potential $-k/r$ exists exactly for
$|L|>k/c$. Replacing it by $-k/\sqrt{r^2+a^2}$, with any fixed $a>0$,
admits regular bound circles for every $|L|>0$. Thus the positive infimum
uses the singular core as well as finite speed and binding.

## Object and physical premises

Use planar canonical coordinates $(r,\theta,p_r,L)$, $r>0$, and
$H=\sqrt{m^2c^4+c^2(p_r^2+L^2/r^2)}+V(r)$, with fixed $m,c,k>0$.
Energy includes rest energy. A regular bound orbit is a complete Hamiltonian
trajectory whose radius remains in a compact subset of $(0,\infty)$.
The angular action is $I_\theta=|L|$: the angular canonical cycle has
$(2\pi)^{-1}|\int_0^{2\pi}L\,d\theta|=|L|$. This cycle normalization does
not require a closed spatial rosette. Define
$g_\theta=\inf\{|L|:\text{a regular bound orbit exists}\}$.
Its units are action, since $[k]=\text{energy}\times\text{length}$.
This is an admissibility threshold, not a spacing of adjacent action values.

The potential is external and static; recoil, radiation and field dynamics
are excluded from this one-body model. Hamilton's velocity always has
magnitude less than $c$ at finite momentum.

## Singular potential: domain and proof

Set $\ell=|L|$ and $x=1/r$. The turning-point energy is
$F_\ell(x)=\sqrt{m^2c^4+c^2\ell^2x^2}-kx$.
For $\ell>0$ its second derivative is strictly positive, its derivative at
zero is $-k$, and its derivative at infinity tends to $c\ell-k$.
Consequently a finite minimum exists exactly for $\ell>k/c$, with

$$
E_{\min}=mc^2\sqrt{1-k^2/(c^2\ell^2)},\qquad
r_0=\frac{\ell\sqrt{c^2\ell^2-k^2}}{mkc}.
$$

For each such $\ell$, the complete bound domain has
$E_{\min}\le E<mc^2$. Equality gives the circle; strict inequality gives
two turning radii. Indeed $F_\ell(0)=mc^2$ and $F_\ell(x)\to\infty$ at
large $x$, so the allowed interval $F_\ell(x)\le E$ is compact and separated
from zero. Energy bounds the momentum there; the smooth Hamiltonian vector
field therefore extends for all time. For $E\ge mc^2$ the outer radius is
unbounded. For $E<E_{\min}$ there are no states.

At $\ell=k/c$, $F_\ell(x)$ decreases to zero without attaining it.
For $\ell<k/c$ it decreases to minus infinity (also directly for $\ell=0$).
There is no radial well in either case. For any allowed orbit with
$E<mc^2$, the single outer turning point leads to a plunge. The energy
identity and inward radial velocity are

$$
c^2p_r^2=E^2-m^2c^4+\frac{2Ek}{r}
 +\frac{k^2-c^2\ell^2}{r^2},\qquad
\dot r=\frac{c^2p_r}{E+k/r}.
$$

For $\ell<k/c$, $|\dot r|\to c\sqrt{k^2-c^2\ell^2}/k>0$ at the centre.
At equality the allowed energy satisfies $E>0$, and
$|\dot r|\sim c\sqrt{2E/k}\sqrt r$. Both give finite arrival time by
integrating $dr/|\dot r|$. A collision continuation is outside the domain.
Hence $g_\theta=k/c$, with the infimum excluded and all larger angular
actions admitted continuously. At fixed $k$ it closes as $c\to\infty$;
at fixed $c$ it closes as $k\downarrow0$. These are limits of thresholds
for positive couplings; at $k=0$ there are no nonstationary bound orbits. At fixed $\ell,k,m$,
$r_0\to\ell^2/(mk)$ and $E_{\min}-mc^2\to-mk^2/(2\ell^2)$ in the
Newtonian limit.

Boyer's equations (19)--(20), (37)--(42), mapped by $\alpha=k$, supply the
established classification; [B27](../references/batches/B27.md) records the
passage audit. The compactness and endpoint-time arguments above state the
precise domain used here.

## Softened core: the threshold closes at fixed coupling

Fix $a>0$ and take $V_a(r)=-k/\sqrt{r^2+a^2}$. For every $\ell>0$ the
turning-point energy

$$
U_{a,\ell}(r)=\sqrt{m^2c^4+c^2\ell^2/r^2}
             -\frac{k}{\sqrt{r^2+a^2}}
$$

tends to infinity as $r\downarrow0$. At large radius,
$U_{a,\ell}(r)=mc^2-k/r+\ell^2/(2mr^2)+O(r^{-3})$,
so it takes values below its limit $mc^2$. It therefore attains a global
minimum at a finite positive radius. At that minimum $p_r=0$ and
$U'_{a,\ell}=0$, giving a complete circular Hamiltonian trajectory.
Every energy strictly between the minimum and $mc^2$ also has compact
allowed radial components. These give regular bound trajectories by the
same continuation argument. Thus $g_\theta(a)=0$ for every $a>0$ even at
fixed $m,k,c$. This existence argument needs neither uniqueness of the
minimum nor a small-velocity approximation.

For each fixed subcritical $0<\ell<k/c$, minimizing radii approach zero as
$a\downarrow0$. To see this, write $r=ay$ and choose a fixed large $y$ with
$c\ell/y<k/\sqrt{1+y^2}$. Then $aU_{a,\ell}(ay)$ tends to a negative
constant, so the minimum tends to minus infinity. On $r\ge\delta>0$,
$U_{a,\ell}\ge mc^2-k/\delta$ uniformly in $a$, forcing the minimizer below
any such $\delta$. These circles leave the regular domain of the singular
model in the limit. In particular $\lim_{a\downarrow0}g_\theta(a)=0$,
whereas the singular model has $g_\theta=k/c$.

## Next observable test

A15 should compare orbital action with a finite-window fluctuation in a
specified bound preparation. M07 identifies which singular-core premise
supports a positive angular threshold; it supplies no universal action value
or attraction law for a physical-time field. Proof and literature status are
recorded separately in the claim ledger and the follow-up audit.
