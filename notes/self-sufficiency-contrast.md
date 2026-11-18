# Coulomb completion and its classical limit: domains, collisions and preparation

Newton's inverse-square force gives two different answers to the action
question for the same stationary planar preparation. Fix the mass, source,
energy and angular momentum. The mean inward force agrees exactly for the
Newtonian ellipse and infinitely many trial actions tending to zero. One
bounded radial observable distinguishes two of those actions and excludes
all sufficiently small ones for its specified value. The classical ellipse
satisfies the preparation even under arbitrarily fine time subdivision.
[Stationary Kepler preparations](#stationary-kepler-preparations).

For $V=-k/r$ in three dimensions, the inward radial classical flow reaches a
collision in finite time, whereas the nonrelativistic Coulomb Hamiltonian
$-h^2\Delta/(2m)-k/r$ on the specified Laplacian domain generates global
unitary motion for every supplied reduced action $h>0$. From rest at $r_0$,
the classical collision time is $t_c=(\pi/2)\sqrt{mr_0^3/(2k)}$. The
contrast diagnoses incomplete point-state dynamics; it does not exclude
classical continuations with an added collision or state rule.

Theorem 1 separates this global operator statement from classical-limit
recovery. Quadratic-force centroids obey Newton's equation exactly. For
Coulomb trajectories on fixed collision-free intervals, the stated Gaussian
preparations, smooth regularization and weighted localization/Hardy estimates
supply the singular-potential control and position/momentum centroid bounds
in §5. A norm approximation alone controls no singular multiplier.
The quartic comparison likewise separates an existing fixed-action unitary
limit from a classical branch rule.

The relativistic comparison in §5b has selection-dependent domains and
endpoints. Dirac's finite-potential-energy choice excludes critical equality;
the critical Schur form or specified cutoff limits include it. Strict-energy
Klein–Gordon construction has an open endpoint, while its radial principal
Friedrichs operator includes equality. A chosen radial branch is not a
construction of the full Klein–Gordon evolution. These are conditional
thresholds, not a necessity theorem for physical $\hbar$.

Notation: $h$ is a supplied reduced phase constant (quantum identification
$h=\hbar$, $h_P=2\pi\hbar$), $m>0$ the mass, $k>0$ the force constant and
$r=|x|$. Written model checks are internal; cited source theorems retain their
reading labels. Sections 5c and 5d use the regular planar form of §3.

## 1. Statement

**Theorem 1 (self-sufficiency contrast for Kepler's force).**

(a) *Classical incompleteness.* Let $L=x\times p$ be the angular
momentum. Every initial datum with $L=0$ whose radial velocity is
inward or zero, and every datum with $L=0$ and negative energy,
reaches $r=0$ at a finite time. For a body released from rest at
distance $r_0$ the collision time is
$$t_c=F(r_0):=\frac\pi2\sqrt{\frac{m\,r_0^3}{2k}}.\tag{1}$$
For bound data, $E<0$ with $R=-k/E$: $t_c\le F(R)$ if the radial
velocity is inward or zero, and $t_c\le2F(R)$ if it is outward; for
inward data with $E\ge0$, $t_c\le\tfrac23\sqrt{m/2k}\,r_0^{3/2}$. The
collision set, on the phase space $\{(x,p):x\neq0\}$,
$$\mathcal C=\{L=0\ \text{and}\ (\dot r\le0\ \text{or}\ E<0)\},$$
is nonempty, invariant under the flow while solutions exist, and of
measure zero. Along every solution in $\mathcal C$ the force magnitude
$k/r^2$ and the momentum $|p|\sim\sqrt{2mk/r}$ diverge as the centre is
approached, so there is no continuation as a solution of the original
vector field in phase space: the flow of Kepler's force is not
complete. Newton's axioms, the Laws with the force law, assign no
motion at the centre; any continuation is an added prescription
(regularization), and the theorem establishes incompleteness, not
that no classical completion is possible.

(b) *Quantum completeness.* For every $h>0$, $m>0$ and real $k$, the
operator
$$H_h=-\frac{h^2}{2m}\Delta-\frac kr\qquad\text{on }L^2(\mathbb R^3)\tag{2}$$
is self-adjoint on the domain $H^2(\mathbb R^3)$ of the Laplacian and
bounded below, and $U_h(t)=e^{-itH_h/h}$ is a strongly continuous
unitary group defined for every $t\in\mathbb R$ and every initial
state in $L^2(\mathbb R^3)$. This is Kato's theorem [@Kato1951;
metadata], whose hypothesis, that the potential is the sum of an
$L^2(\mathbb R^3)$ and a bounded function, is verified in §3.

(c) *The quartic contrast.* For $V=\lambda q^4$ on the line, $\lambda>0$,
Theorem 2(b) of the [1998-conjecture note](rivero-1998-conjecture-central-forces.md)
gives, for every $h>0$, the strong convergence of the time-sliced
operators to the unitary evolution $e^{-iTH_h/h}$ along every sequence
of partitions, with no extra datum; Theorem 1 there shows that the
unrestricted halved classical-first construction at zero resolution
has no limit on a two-cell partition with three stationary paths, and
Theorem 2(a) there exhibits one repair, a branch selection chosen by
hand. The contrast is between the fixed-$h$ construction, which exists
for all data, and that specific classical-first prescription, which
needs a datum the action does not supply; it says nothing against the
quartic Newtonian initial-value problem itself, which is globally well
posed.

(d) *The classical trajectory as a derived object.* (d1) For
$H=p^2/2m+V$ with $\deg V\le2$, the expectations $\langle q\rangle_t$,
$\langle p\rangle_t$ of every state with finite second moments obey
Newton's equations exactly for every $h>0$,
$$\frac{d}{dt}\langle q\rangle_t=\frac{\langle p\rangle_t}m,\qquad
\frac{d}{dt}\langle p\rangle_t=-V'(\langle q\rangle_t),\tag{3}$$
and a coherent state stays a Gaussian whose centroid is the classical
trajectory. (d2) For Kepler's force, let $z_0=(x_0,p_0)$ lie on a
classical orbit whose distance from the centre stays at least
$\rho_{\min}>0$ on $[0,T]$. Fix $0<\delta<\rho_{\min}$ and a real
$V_\delta\in C_b^\infty$ equal to $-k/r$ for $r\ge\delta$. For the
normalized coherent preparations of §5a, with width
$\ell_h=\sqrt{hL_*/P_*}$ and fixed $L_*,P_*>0$, the regularized and
Coulomb evolutions both satisfy the Gaussian norm approximation (4)
with error $O(\sqrt h)$, uniformly on $[0,T]$. Section 5a proves
$$\sup_{[0,T]}\|(V-V_\delta)U_h^{(\delta)}(t)\varphi_h\|_2
=O(h^{3/2})=o(h),\qquad\text{(L)}$$
and separately proves that the Coulomb position and momentum centroids
are $q_t+O(\sqrt h)$ and $p_t+O(\sqrt h)$. Here "large action" means
this fixed-scale limit $h\to0$ at fixed orbit. All constants depend on
the fixed interval, regularization and preparation; no uniformity in
$T$ or $\delta$ is claimed.

*Conclusion.* The theory with $h>0$ defines motion for all data and
all times, by (b), and yields Newton's trajectories where they exist,
exactly for quadratic forces and, under the fixed-data hypotheses of
§5a, for Kepler's force away from collisions, by (d), while Newton's axioms
leave motion undefined on the collision set, by (a), and the
unrestricted classical-first construction at zero needs a datum the
action does not supply, by (c).

## 2. Proof of (a)

Conservation of $L$ under a central force is Proposition I of Book I;
for $L=0$ the motion is on a line through the centre and
$E=\tfrac m2\dot r^2-k/r$ is conserved. Released from rest at $r_0$,
$E=-k/r_0$ and
$$\dot r^2=\frac{2k}m\Big(\frac1r-\frac1{r_0}\Big)=\frac{2k}{m}\,\frac{r_0-r}{r\,r_0},$$
with $\dot r<0$ for $t>0$ because the force points inward. Hence
$$t_c=\int_0^{r_0}\frac{dr}{|\dot r|}
=\sqrt{\frac{m r_0}{2k}}\int_0^{r_0}\sqrt{\frac{r}{r_0-r}}\,dr.$$
With $r=r_0\sin^2\theta$, $dr=2r_0\sin\theta\cos\theta\,d\theta$ and
$\sqrt{r/(r_0-r)}=\tan\theta$, the integral is
$2r_0\int_0^{\pi/2}\sin^2\theta\,d\theta=\pi r_0/2$, which gives (1).

For a bound datum with $L=0$, $E<0$ and $R=-k/E$: $r\le R$
throughout, $|\dot r|^2=\tfrac{2k}m(1/r-1/R)$, and the time from $r_0$
to the centre along the inward branch is
$I(r_0)=\sqrt{m/2k}\int_0^{r_0}\sqrt{rR/(R-r)}\,dr\le I(R)=F(R)$. If
the radial velocity is outward, the body first rises to $R$ in the
time $F(R)-I(r_0)$ and then falls in the time $F(R)$, so its collision
time is $2F(R)-I(r_0)\le2F(R)$, and it exceeds $F(R)$: one fall time
does not bound it. For inward data with $E\ge0$,
$|\dot r|\ge\sqrt{2k/(mr)}$ gives the time bound
$\int_0^{r_0}\sqrt{mr/2k}\,dr=\tfrac23\sqrt{m/2k}\,r_0^{3/2}$. Invariance
of $\mathcal C$: $L$ and $E$ are conserved; for $E<0$ the condition is
then automatic, and for $E\ge0$ the radial velocity cannot vanish, since
$\tfrac m2\dot r^2=E+k/r>0$, so its inward sign is preserved. The
condition $L=0$ is that $p$ be parallel to $x$, which for $x\neq0$
defines a four-dimensional subset of the six-dimensional phase space,
hence of Liouville measure zero; it is nonempty. As $r\to0$ along a
solution in $\mathcal C$, the force magnitude $k/r^2$ is unbounded and
$\tfrac m2\dot r^2=E+k/r$ gives $|p|\sim\sqrt{2mk/r}$, so the solution
leaves every compact subset of phase space in finite time and admits no
continuation as a solution of the vector field. A continuation through
the centre (Levi-Civita or Kustaanheimo–Stiefel regularization) is an
added prescription with an enlarged notion of solution, in the same
position as the branch rule of (c). $\square$

## 3. Proof of (b), with Kato's hypothesis verified

Kato's theorem [@Kato1951; metadata; the statement used is the one
standardly quoted from it, the primary text was not read in this
session]: let $V=V_1+V_2$ be real with $V_1\in L^2(\mathbb R^3)$ and
$V_2\in L^\infty(\mathbb R^3)$. Then for every $a>0$ the operator
$-a\Delta+V$ is self-adjoint on $H^2(\mathbb R^3)$ and bounded below.
The mechanism is the Sobolev bound
$\|u\|_\infty\le\epsilon\|\Delta u\|+C_\epsilon\|u\|$ for $u\in H^2(\mathbb R^3)$,
which makes $V_1$ relatively bounded with respect to $\Delta$ with
relative bound zero, so that the Kato--Rellich theorem applies for
every value of $a=h^2/2m$.

Verification for $V=-k/r$: fix a cutoff radius $R>0$ and put
$V_1=-\tfrac kr\mathbf 1_{r<R}$, $V_2=-\tfrac kr\mathbf 1_{r\ge R}$. Then
$|V_2|\le|k|/R$, and
$$\int_{\mathbb R^3}|V_1|^2d^3x=k^2\int_0^R\frac{4\pi r^2}{r^2}\,dr=4\pi k^2R<\infty.$$
So the hypothesis holds for every real $k$, and $H_h$ in (2) is
self-adjoint on $H^2(\mathbb R^3)$ for every $h>0$, $m>0$. Stone's
theorem then gives the unitary group $U_h(t)$ for all $t\in\mathbb R$,
strongly continuous, defined on every $\psi\in L^2$, with
$U_h(t)\psi\in H^2$ for $\psi\in H^2$; states outside the operator
domain have the mild unitary evolution, those inside satisfy the
Schrödinger equation. No initial datum and no time is excluded; the
states supported near $r=0$ evolve like all others. $\square$

*Planar remark.* In $\mathbb R^2$ the function $1/r$ is not square
integrable near the origin, and the operator-sense theorem does not
apply; the planar Coulomb Hamiltonian is defined in the form sense by
the KLMN theorem, since $1/r\in L^p_{\rm loc}(\mathbb R^2)$ for $p<2$
is form-bounded relative to $-\Delta$ with relative bound zero. The
planar Kepler problem used elsewhere in this repository therefore also
has a global unitary dynamics, by that standard route, which is not
reproved here.

## 4. Proof of (c)

The statements are Theorems 1, 2(a) and 2(b) of the
[1998-conjecture note](rivero-1998-conjecture-central-forces.md),
accepted on refereeing there (status line of that note). Theorem 2(b)
proves the product formula for $H_h=-\tfrac{h^2}{2m}d^2/dq^2+\lambda q^4$
at every $h>0$: essential self-adjointness, the strong limit of the
symmetric time slicing along any partition sequence, and the
composition $\|U_h(T)\|=1$. Theorem 1 proves that the halved
classical-first functional on the two-cell partition has, as the
resolution tends to zero, the oscillating value (4) there with no
limit, because the three stationary paths interfere; Theorem 2(a)
restores a limit only by restricting to a neighbourhood of one path,
a datum the action does not contain. Hence for the quartic the $h>0$
theory exists for all data without extra rules and the construction at
zero does not. $\square$

## 5. Proof of (d)

*(d1), quadratic forces.* By Theorem A(a) of the
[fifth-postulate note](principia-fifth-postulate.md), the Heisenberg
equations are Newton's second law as operator identities for every
real $h$: $\dot q=p/m$ and $\dot p=-V'(q)$. Taking expectations in a
state with finite second moments gives
$\tfrac{d}{dt}\langle q\rangle=\langle p\rangle/m$ and
$\tfrac{d}{dt}\langle p\rangle=-\langle V'(q)\rangle$; for
$\deg V\le2$ the function $V'$ is affine, so
$\langle V'(q)\rangle=V'(\langle q\rangle)$, which is (3). The centroid
therefore follows the classical trajectory through $(\langle q\rangle_0,
\langle p\rangle_0)$ for every $h>0$ and every such state, with no
approximation. For a coherent state the Wigner function is the
Gaussian transported by the affine flow (proof of Theorem 5 of the
[reachability note](zero-branch-reachability.md)), so the state stays
Gaussian with the classical trajectory as its centroid and covariance
$M_t\Sigma_hM_t^{\sf T}$. The width at time $t$ depends on the flow:
for free motion, scaling the mass by $\lambda$ at fixed $h$ and widths
sends $M_{12}=t/m\to0$ and the position width to the initial $\sigma$,
while for Hooke's force at fixed frequency the width
$s_t^2=\sigma^2\cos^2\omega t+h^2\sin^2\omega t/(4m^2\omega^2\sigma^2)$
tends to $\sigma^2\cos^2\omega t$; the centroid transport is exact in
every case. $\square$

### 5a. Kepler localization and moments (2026-10-02)

**Target and assumptions.** Fix $m,k,L_*,P_*>0$, an initial phase point
$z_0=(q_0,p_0)$, and $T<\infty$ such that its Kepler orbit
$z_t=(q_t,p_t)$ exists on $[0,T]$ and
$\rho_{\min}:=\min_{[0,T]}|q_t|>0$. Fix $0<\delta<\rho_{\min}$ and a real
$V_\delta\in C_b^\infty(\mathbb R^3)$ equal to $-k/r$ on $r\ge\delta$.
All these choices are independent of $h$. Put $\ell_h=\sqrt{hL_*/P_*}$,
choose $h_0>0$, and consider $0<h\le h_0$ with the normalized preparations
$$\varphi_h(x)=(2\pi\ell_h^2)^{-3/4}
\exp\left[-\frac{|x-q_0|^2}{4\ell_h^2}
          +\frac{i p_0\cdot(x-q_0)}h\right].$$
Both Hamiltonians have domain $H^2(\mathbb R^3)$. The conclusions to
prove are (L), its Duhamel transfer, and convergence of the two first
moments. Neither singular-multiplier control from an $L^2$ approximation
nor convergence of an unbounded observable is an assumption.

*Primary Hepp statement.* The published paper [@Hepp1974; passage,
§2, Theorem 2.1, p. 268; equations (2.15)--(2.20), pp. 269--270;
Theorem 2.3 and condition (R), p. 271] states Theorem 2.1 for one
degree of freedom: a real potential, $C^{2+\epsilon}$ near the classical
orbit, $\epsilon>0$, with $\int |V(x)|^2e^{-\eta x^2}dx<\infty$ for
some $0<\eta<\infty$, and any self-adjoint realization of the scaled
Hamiltonian. The limits are strong limits of Weyl operators, uniformly
on compact time intervals inside the orbit's existence interval.
Equation (2.20) gives the corresponding norm approximation on Gaussian
packets. For finitely many coordinates, Theorem 2.3 replaces the
integrability assumption by (R): a strongly continuous unitary
propagator $U_h(t,s)$ for all real $t,s$, with
$U_h(t,s)U_h(s,r)=U_h(t,r)$, $U_h(t,s)^*=U_h(s,t)$,
$U_h(t,t)=I$, and the strong derivative
$$\partial_s U_h(t,s)\psi=\frac ih U_h(t,s)H_h(s)\psi$$
on the sufficiently decaying Gaussian packets specified in (2.27),
with $H_h(s)\psi$ defined as a differential operator. Theorem 2.3
allows finitely many particles with vector and scalar potentials
locally $C^{2+\epsilon}$ along the orbit; here the vector potential is zero.

The three-dimensional $V_\delta$ satisfies (R) because it is bounded
and its Gaussian packets belong to $H^2$. The approximation is
$$\sup_{0\le t\le T}\|U_h^{(\delta)}(t)\varphi_h
-e^{iS_t/h}\varphi^h_{z_t,M_t}\|_2=O(\sqrt h),\tag{4}$$
where $S_t=\int_0^t(p_s\cdot\dot q_s-H_{\rm cl}(z_s))ds$ and the Gaussian
is obtained with the continuously lifted quadratic propagator of the
linearized flow $M_t$. Its translation convention uses
$p_t\cdot(x-q_t)$ in the phase. To see the rate in this smooth case,
expand $V_\delta$ through second order at $q_t$: the cubic remainder
has norm at most $B_3\ell_h^3\||y|^3g_t\|_2/6$ on the centered
quadratic Gaussian $g_t$. Duhamel divides this by $h$ and integrates
over $[0,T]$; the Gaussian moment is bounded on that fixed interval.
This is a direct specialization of Hepp's proof, not an estimate of
the singular multiplier on the unknown norm remainder.

**Centered Sobolev bound.** Let $u_h(t)=U_h^{(\delta)}(t)\varphi_h$ and
write exactly
$$u_h(t,x)=\ell_h^{-3/2}e^{i[S_t+p_t\cdot(x-q_t)]/h}a_h(t,y),
\qquad y=(x-q_t)/\ell_h.$$
Hamilton's equations cancel the constant and linear terms, so
$$i\partial_ta_h=G_h(t)a_h,\quad
G_h=-a_*\Delta_y+W_h(t,y),\quad a_*=\frac{P_*}{2mL_*},$$
$$W_h=\frac{V_\delta(q_t+\ell_h y)-V_\delta(q_t)
-\ell_h\nabla V_\delta(q_t)\cdot y}{h}.$$
Set $B_j=\sup_x\|\nabla^jV_\delta(x)\|$ (the Euclidean tensor norm),
$\ell_0=\sqrt{h_0L_*/P_*}$, and, for integer $s\ge1$,
$$b_s=\frac{L_*}{P_*}
\max_{2\le j\le\max(2,s)}\ell_0^{\,j-2}B_j.$$
Taylor's integral formula gives
$|\nabla_yW_h|\le b_s|y|$, and
$|\partial_y^\gamma W_h|\le b_s$ for $2\le|\gamma|\le s$.
All these constants are uniform for $0<h\le h_0$ and $0\le t\le T$.

With $D_y=-i\nabla_y$, define
$$E_s(a)=\sum_{|\alpha|+|\beta|\le s}\|y^\alpha D_y^\beta a\|_2^2,
\quad N_s=\binom{s+6}{6},\quad
c_s=a_*s(s+1)+b_s(2^s-1+2s).$$
The commutator of $y^\alpha D_y^\beta$ with the kinetic term has
norm bounded by $a_*s(s+1)\sqrt{E_s}$. For the potential term use
$$[D_y^\beta,W_h]=
\sum_{0<\gamma\le\beta}\binom{\beta}{\gamma}
(-i)^{|\gamma|}(\partial^\gamma W_h)D_y^{\beta-\gamma}.$$
When $|\gamma|=1$, the bound $b_s|y|$ increases the position degree
by one and decreases the derivative degree by one. Bounding
$|y|$ by $\sum_j|y_j|$ gives $3s b_s\sqrt{E_s}$.
The remaining binomial coefficients sum to at most $2^s-1-s$.
No term has degree larger than $s$. Thus
$$\frac{d}{dt}E_s(a_h)\le2c_s\sqrt{N_s}\,E_s(a_h),\qquad
E_s(a_h(t))\le E_s(a_0)e^{2c_s\sqrt{N_s}T},\tag{4a}$$
where $a_0=(2\pi)^{-3/4}e^{-|y|^2/4}$. For fixed $h$ the calculation
is justified on Schwartz packets: the integral equation for a bounded
smooth potential, with position and derivative cutoffs, gives the same
finite-seminorm energy estimates and propagation of Schwartz
regularity; letting the cutoffs tend to infinity proves (4a).
Equivalently, one first obtains these estimates for smooth truncated
data and passes by the $L^2$ evolution and lower semicontinuity.
The centered estimates, unlike the preliminary fixed-$h$ ones, have
the uniform constants displayed above.

For use below define
$$A_s(T)=3^{s/2}\sqrt{E_s(a_0)}e^{c_s\sqrt{N_s}T}.$$
Expanding $|y|^{2n}=(y_1^2+y_2^2+y_3^2)^n$ shows that both
$\||y|^na_h(t)\|_2$ and $\||y|^n\nabla_ya_h(t)\|_2$
are at most $A_{n+1}(T)$.

**Proof of (L).** Put
$r_c=(\delta+\rho_{\min})/2$ and $d=\rho_{\min}-r_c>0$.
Choose a smooth radial cutoff $\chi$ equal to one for $r\le\delta$,
zero for $r\ge r_c$, with $0\le\chi\le1$ and
$\|\nabla\chi\|_\infty\le2/(r_c-\delta)=2/d$.
On its support $|x-q_t|\ge d$, hence $|y|\ge d/\ell_h$.
The centered bounds imply, for every integer $n\ge1$,
$$\|\chi u_h(t)\|_2\le A_{n+1}(T)(\ell_h/d)^n,\qquad
\|\chi(\nabla-ip_t/h)u_h(t)\|_2
\le A_{n+1}(T)\ell_h^{n-1}/d^n.$$
Apply the three-dimensional Hardy inequality
$\|f/r\|_2\le2\|\nabla f\|_2$ to
$f=e^{-ip_t\cdot x/h}\chi u_h(t)$; the phase removes the potentially
large carrier momentum from the estimate. Since $V-V_\delta$ vanishes
outside $r<\delta$, this gives
$$\sup_{0\le t\le T}\|(V-V_\delta)u_h(t)\|_2
\le\frac{A_{n+1}(T)}{d^n}
\left[(4k/d+B_0)\ell_h^n+2k\ell_h^{n-1}\right].\tag{4b}$$
For $n=4$ the right side is $O(h^{3/2})=o(h)$, proving (L).
Choosing larger $n$ gives any prescribed power of $h$.
The dependence is explicit through $T$, $m$, $L_*/P_*$,
the preparation seminorms, $B_j(V_\delta)$, and the separation
$d=(\rho_{\min}-\delta)/2$. No uniformity as $T\to\infty$,
$\delta\to0$, or $\rho_{\min}-\delta\to0$ is claimed. A bounded family
of centered Schwartz preparations satisfies the same estimate with
its uniform $E_s(a_0)$ in place of the Gaussian value.
For the usual scaled regularization
$V_\delta(x)=-(k/\delta)v(x/\delta)$, with fixed smooth bounded $v$
equal to $1/|x|$ for $|x|\ge1$, the derivative dependence is
$B_j\le k\delta^{-j-1}\|\nabla^jv\|_\infty$. A radius $\delta$
alone cannot bound these constants for arbitrary regularizations.

On the common domain $H^2$, Duhamel now gives
$$U_h(t)\varphi_h-U_h^{(\delta)}(t)\varphi_h
=-\frac ih\int_0^tU_h(t-s)(V-V_\delta)u_h(s)\,ds.$$
Consequently the supremum of this norm is $O(h^{(n-3)/2})$ for every
$n\ge4$. In particular the two evolutions differ by $O(h^M)$ for
every fixed $M>0$, with an $M$-dependent constant. Equation (4)
therefore transfers to the Coulomb evolution.

**First moments.** Write $\psi_h=U_h\varphi_h$
and $p=-ih\nabla$. Its conserved form energy $e_h$ is bounded
independently of $h$: the initial kinetic energy is
$|p_0|^2/(2m)+3hP_*/(8mL_*)$, and the elementary spherical Gaussian
integral gives
$\langle\varphi_h,r^{-1}\varphi_h\rangle
=\operatorname{erf}(|q_0|/(\sqrt2\ell_h))/|q_0|\le1/|q_0|$.
Let $e_*=\sup_{0<h\le h_0}|e_h|<\infty$. Hardy and Young's inequality
give, with $X_h(t)=\|p\psi_h(t)\|_2$,
$$e_h\ge\frac{X_h(t)^2}{2m}-\frac{2k}{h}X_h(t)
\ge\frac{X_h(t)^2}{4m}-\frac{4mk^2}{h^2},\qquad
X_h(t)\le2\sqrt{m e_*}+\frac{4mk}{h}.\tag{4c}$$
The continuity equation, first with bounded position cutoffs and
then by passage to the limit, gives
$$\|x\psi_h(t)\|_2
\le\|x\varphi_h\|_2+\frac1m\int_0^tX_h(s)\,ds=O(1+h^{-1}).\tag{4d}$$
This also proves preservation of the position-moment domain on the
fixed interval. Energy conservation preserves the Coulomb form domain
$H^1$, so the momentum norm is finite as well.
For $u_h$ the centered bounds give
$\|(x-q_t)u_h(t)\|_2\le\ell_h A_1(T)$ and
$\|(p-p_t)u_h(t)\|_2\le(h/\ell_h)A_1(T)$.

For each self-adjoint coordinate or momentum component $B$ and the
two normalized states, symmetry on its domain yields
$$|\langle\psi_h,B\psi_h\rangle-\langle u_h,Bu_h\rangle|
\le\|\psi_h-u_h\|_2(\|B\psi_h\|_2+\|Bu_h\|_2).$$
Use (4b) with $n=6$: the norm difference is $O(h^{3/2})$, while
(4c)--(4d) bound the second factor by $O(h^{-1})$. Thus, uniformly
on $[0,T]$,
$$\langle x\rangle_{\psi_h(t)}=q_t+O(\sqrt h),\qquad
\langle p\rangle_{\psi_h(t)}=p_t+O(\sqrt h).\tag{4e}$$
These first-moment statements use derivatives of $V_\delta$ through
order seven via (4a). They establish the centroid assertion without
assuming moment convergence from a norm approximation. They give
neither long-time control nor convergence of higher moments. $\square$

## 5b. Proposition 2: action thresholds under specified selections

Theorem 1(b) gives no positive lower threshold: the non-relativistic
Coulomb evolution exists for every $h>0$. At finite $c$ a threshold
depends on which relativistic model, domain and selection premise are
required. Fix $m,k,c>0$ and $\nu=k/(hc)>0$. All statements concern an
ideal point Coulomb source. Rescale length by $\lambda_h=h/(mc)$ and
energy by $mc^2$; in the formulas for domains below, $x$ and $r$ denote
these dimensionless coordinates. This unitary rescaling leaves $\nu$
unchanged.

**Primary sources and their scope.** Schmincke's original example,
p. 348, applies his Theorems 2--3 to the strict range $|\nu|<1$ and
identifies the selected domain by finite potential energy
[@Schmincke1972; passage, pp. 345--348, GDZ text]. Wüst's theorem and
corollary require a real $C^1$ potential dominated by $\mu/r$ with
$\mu<1$, together with the specified bounded cutoff and convergence
conditions; the selected domain is
$D(D_{\min}^*)\cap D(r^{-1/2})$ [@Wuest1975; passage, pp. 93--95,
GDZ text]. Those results do not settle $\nu=1$. Nenciu constructs the
finite-kinetic-form-domain extension for a strict subcritical
Coulomb bound [@Nenciu1976; passage, introduction and Theorem 5.1,
pp. 246--247, author-posted text]; its poorly extracted formulas are
not used here to infer an endpoint.

The precise subcritical domain statement used below is Theorem 1.1
of Esteban--Lewin--Séré: for real $V=V_1+V_2+V_3$ with
$|V_1|\le\nu/r$, $0\le\nu<1$, $V_2\in L^3$ and $V_3\in L^\infty$,
there is a unique extension with
$H^1\subset D(D_V)\subset H^{1/2}$, also uniquely characterized by
$\int|\Psi|^2/r<\infty$ for every domain vector
[@EstebanLewinSere2019; passage, arXiv v7, Theorem 1.1, pp. 9--10].
Their §1.2 and Appendix A include essential self-adjointness at
$\nu=\sqrt3/2$. Their Theorem 1.11, building on Esteban--Loss
[@EstebanLoss2007; passage, Definition 3 and Theorem 4, pp. 3--4],
supplies a different critical domain and norm-resolvent cutoff limit.

For Klein--Gordon, Case's bibliographic identity is verified as
*Physical Review* **80**, 797--806 (1950), DOI
[10.1103/PhysRev.80.797](https://doi.org/10.1103/PhysRev.80.797)
[@Case1950; metadata/abstract]. Its original body was not accessible
in this revision, so it is not a proof input. We derive the radial
indices below directly and use separate read sources for the domains
and the evolution. Domain and spectral facts for the inverse-square
principal operator come from Dereziński--Richard
[@DerezinskiRichard2017; passage, §§2.2--2.3, equations (2.3)--(2.6),
Corollary 2.4 and Theorem 5.5]. The actual global Klein--Gordon
construction used here is Langer--Najman--Tretter
[@LangerNajmanTretter2008; passage, Example 8.3 and Theorems 8.5--8.6,
pp. 744--747]. These are distinct results.

**Proposition 2 (selection-dependent admissible sets).** The following
sets, including their endpoints, correspond to the premises in the
first column. An admissible set in one row is not an exclusion theorem
for other rows or other completions.

| Selection premise | Admissible $h$-set | Result supplied |
|---|---|---|
| Dirac minimal operator on $C_c^\infty(\mathbb R^3\setminus\{0\})^4$: require essential self-adjointness | $[2k/(\sqrt3c),\infty)$ | Unique closure, global unitary evolution |
| Dirac: require every operator-domain vector to have finite separate Coulomb potential energy | $(k/c,\infty)$ | Unique distinguished extension, global unitary evolution |
| Dirac: use that extension below critical coupling and the critical Schur-domain or specified cutoff-limit prescription at equality | $[k/c,\infty)$ | Global unitary evolution, including $h=k/c$ |
| Dirac: permit additional self-adjoint boundary conditions in singular channels | $(0,\infty)$ | Extensions exist; uniqueness is lost where the minimal operator is not essentially self-adjoint |
| Klein--Gordon: require strict coercivity of the conserved energy in the usual $H^1\oplus L^2$ topology, and use the charge-space generator below | $(2k/c,\infty)$ | A global charge-space evolution is constructed; the strict criterion excludes equality |
| Klein--Gordon $s$-wave principal radial operator: choose its Friedrichs extension | $[2k/c,\infty)$ | Principal radial operator and branch, including the no-log branch at equality; full critical evolution is not concluded |

*Dirac proof and domains.* In the scaled coordinates the expression is
$D_\nu=-i\alpha\cdot\nabla+\beta-\nu/r$. In a channel
$\kappa\in\mathbb Z\setminus\{0\}$ its reduced two-component radial
operator acts in $L^2((0,\infty),dr)^2$ as
$$d_{\nu,\kappa}=\begin{pmatrix}
1-\nu/r&-\partial_r+\kappa/r\\
\partial_r+\kappa/r&-1-\nu/r
\end{pmatrix}.$$
Its origin modes have exponents $\pm s_\kappa$,
$s_\kappa=\sqrt{\kappa^2-\nu^2}$. For real $s_\kappa>0$, the less
regular mode is locally square integrable precisely when
$s_\kappa<1/2$; for imaginary $s_\kappa$ both modes are locally
square integrable. At $s_\kappa=1/2$
its squared norm contains $\int dr/r$ and diverges. Infinity is
limit point. Taking $|\kappa|=1$ gives the inclusive essential
self-adjointness threshold $\nu\le\sqrt3/2$. The closure has domain
$H^1$ for strict inequality; at equality its domain is larger than
$H^1$ (Appendix A, Proposition A.1 of the cited source).

For $\sqrt3/2<\nu<1$, both modes are in radial $L^2$. A full spinor
contains the additional factor $1/r$, so its potential integral is
$\int_0^\epsilon(|u|^2+|v|^2)dr/r$. Finite potential energy excludes
the $r^{-s_1}$ coefficient and retains $r^{s_1}$, giving the unique
domain $D(D_{\min}^*)\cap D(r^{-1/2})$. At $\nu=1$ the modes are
constant and logarithmic. Both have divergent separate potential
energy. An extension domain must contain a nonzero boundary mode:
setting both coefficients to zero leaves the minimal, non-self-adjoint
domain. Thus no self-adjoint extension at equality has all domain
vectors of finite separate potential energy. For $\nu>1$ the lowest
channel has imaginary $s_1$ and the same integral diverges for every
nonzero boundary mode. This proves the open set in the second row.

The critical prescription instead uses the closed Schur form of
Esteban--Loss. For $0<\gamma<1$, define on
$C_c^\infty(\mathbb R^3,\mathbb C^2)$
$$b_\gamma[\phi]=\int_{\mathbb R^3}\left[
\frac{r}{1+\gamma r}|\sigma\cdot\nabla\phi|^2
+(2-\gamma-r^{-1})|\phi|^2\right]dx.$$
Their critical Hardy--Dirac inequality (7) verifies Assumption (A)
with $c(V)=0$ and $\Gamma=\sup V=0$. Let $\mathcal H_+$ be the
form domain of its closure, equivalently the completion in
$(b_\gamma[\phi]+\|\phi\|_2^2)^{1/2}$. Proposition 2 makes this domain
independent of $\gamma$ in the stated range. The closure defines the
combined form; its two integrals need not exist separately for a
completed vector. Definition 3 and Theorem 4 give the operator domain
$$\mathcal D_C=\{\Psi=(\phi,\chi)\in L^2(\mathbb R^3)^4:
\phi\in\mathcal H_+,\ D_1\Psi\in L^2\text{ in distributions}\}.$$
They prove self-adjointness and uniqueness under that form-domain
premise. The angular-channel formulation in Esteban--Lewin--Séré,
equations (1.28)--(1.31), admits $1/r$ spinor singularities and
excludes $(\log r)/r$ in both lowest channels.
Its combined operator energy is finite; its separate potential and
kinetic form energies need not be. Their Theorem 1.11, for
$V\ge-1/r$ and $\sup V<1$, reports
norm-resolvent convergence for $V_\epsilon=\max(V,-1/\epsilon)$ or
$V_\epsilon=(1-\epsilon)V$, as $\epsilon\downarrow0$. This establishes
the included endpoint under this changed selection premise.

**Source-formula clarification, 2026-10-02.** The literal compact
weighted-gradient formula printed in (1.32) of arXiv v7 is not used
as a domain definition here: it conflicts with the angular form
description just cited. For a nonzero constant spinor $\xi$, put
$$\phi(x)=\frac{e^{-r}}r\sigma\cdot\omega_x\xi,
\qquad \omega_x=x/r.$$
Its critical radial profile $\phi_1=e^{-r}\xi/r$ satisfies
$r\phi_1'+\phi_1=-e^{-r}\xi$, so the angular form norm in (1.29)
is finite. Logarithmic cutoffs of $r\phi_1$ have cost
$\int r|\eta_\epsilon'|^2dr=1/\log(1/\epsilon)$ on
$[\epsilon^2,\epsilon]$ and place it in the Schur-form closure.
But
$$\sigma\cdot\nabla(r\phi)=e^{-r}(2/r-1)\xi,$$
whose squared norm with weight $1/[r(1+r)]$ diverges like
$\int_0 dr/r$. Thus that compact rewrite cannot be taken literally
as equivalent to the angular norm. The source TeX and HTML confirm
that this is not a PDF extraction change. We use the original
Esteban--Loss form closure and the explicit angular conditions;
this calculation checks the problematic rewrite, not the full borrowed
theorems independently.

For arbitrary $\nu>0$, conjugation of the real radial system makes
its two deficiency indices equal. Every limit-circle channel therefore
admits self-adjoint boundary conditions; only finitely many channels
require them for a fixed $\nu$. Their direct sum gives a global
self-adjoint Dirac realization. Above critical coupling an origin
phase is additional data. Self-adjointness alone consequently gives
no positive lower bound on $h$.

*Klein--Gordon construction and domains.* In the scaled variables the
equation is $[(i\partial_t-V)^2+\Delta-1]\psi=0$, $V=-\nu/r$.
Hardy's inequality gives $\|Vf\|_2\le2\nu\|\nabla f\|_2$ for
$f\in H^1$. Langer--Najman--Tretter's Theorem 8.5 assumes
$H^1\subset D(V)$ and a decomposition $V=V_0+V_1$ with
$$\|V_0f\|_2\le a\|f\|_2+b\|(-\Delta+1)^{1/2}f\|_2,
\quad a+b<1,$$
and $V_1$ relatively compact. Pure Coulomb satisfies it with
$a=0$, $b=2\nu<1$, $V_1=0$. The theorem constructs the generator
$$A\binom{x}{y}=\binom{Vx+y}{(-\Delta+1)x+Vy}$$
in the charge space $\mathcal K=H^{1/2}\oplus H^{-1/2}$, with domain
$$D(A)=\{(x,y)\in\mathcal K:x\in H^1,\ y\in L^2,
\ Vx+y\in H^{1/2},\ (-\Delta+1)x+Vy\in H^{-1/2}\}.$$
The charge pairing is $[X,X']=\langle x,y'\rangle+\langle y,x'\rangle$,
using Sobolev duality. The group is strongly continuous and unitary
for this indefinite pairing. It gives global mild evolution on
$\mathcal K$ and classical evolution on $D(A)$. It is not a
probability-unitary group on scalar $L^2$. Theorem 8.6 gives the
corresponding strong Klein--Gordon solutions for
$\psi_0\in H^1$, $\psi_1\in H^{1/2}$ and
$(-\Delta-V^2)\psi_0\in H^{-1/2}$.
For the sign convention of the equation above use
$i\partial_tX=AX$, $y=(i\partial_t-V)\psi$, and $e^{-itA}$;
the source's group $e^{itA}$ also gives this evolution after reversing
the time parameter.

In physical units the conserved energy has spatial part
$$Q_\nu[f]=h^2c^2\|\nabla f\|_2^2+m^2c^4\|f\|_2^2
-k^2\|f/r\|_2^2
\ge(1-4\nu^2)h^2c^2\|\nabla f\|_2^2+m^2c^4\|f\|_2^2.$$
Sharpness of Hardy's constant, with dilations of its near-extremizers
to remove the mass term relative to the gradient, shows that strict
coercivity in the usual $H^1$ norm holds exactly for $\nu<1/2$.
At equality the combined form is nonnegative but loses that
coercivity; above it the spatial form is unbounded below. This
settles the fifth row's criterion, not the existence of all possible
Klein--Gordon completions.

For a stationary $s$-wave $\psi=e^{-iEt/h}u(r)/r$, direct substitution
gives the pencil
$$-h^2c^2u''+(m^2c^4-E^2)u-\frac{2Ek}{r}u-\frac{k^2}{r^2}u=0.$$
The indices are $1/2\pm s$, $s=\sqrt{1/4-\nu^2}$. The principal
operator $B_\nu=-\partial_r^2-\nu^2/r^2$ starts on
$C_c^\infty(0,\infty)$ in $L^2(dr)$, with maximal domain consisting
of $u,u'$ locally absolutely continuous and $B_\nu u\in L^2$.
For $0<\nu<1/2$ its Friedrichs domain sets the coefficient of
$r^{1/2-s}$ to zero. Both branches have finite $u(0)$ and are locally
$L^2$; those properties alone do not select it. At $\nu=1/2$ the
modes are $\sqrt r$ and $\sqrt r\log r$. The Friedrichs domain sets
the logarithmic coefficient to zero, admitting the endpoint for this
principal operator. It permits a nonzero $\sqrt r$ coefficient whose
separate kinetic integral diverges; the critical combined form is
finite: writing $u=\sqrt r\,v$ on $C_c^\infty(0,\infty)$ gives
$\int(|u'|^2-|u|^2/(4r^2))dr=\int r|v'|^2dr$. A logarithmic cutoff
near zero approximates a constant $v$ with vanishing form cost.
For $\nu>1/2$, $s=i\beta$, self-adjoint extensions require an
origin phase and all have a negative spectrum unbounded below
(Dereziński--Richard, Theorem 5.5(ii)). No semibounded Friedrichs
extension exists there. The lower-order $1/r$ term of the stationary
pencil does not change the indicial classification.

**Uncontrolled critical dynamical term.** The no-log radial selection
does not prove a global Klein--Gordon group at $\nu=1/2$. The critical
combined form does not bound $\|f/r\|_2$: a cutoff of $\sqrt r$ in
the radial form domain already has infinite separate kinetic and
inverse-square integrals. Thus the multiplier bound with relative
constant strictly below one fails. On the enlarged critical form
space, the mixed dynamical term $V\partial_t\psi$, or equivalently
the required control of $VQ_{1/2}^{-1/2}$, remains unbounded by the
estimates used here. A compatible phase space and generator domain
are still needed for a critical full evolution theorem. No such
theorem is asserted by the sixth row. $\square$

**Physical selection premises.** Dirac self-adjointness
ensures probability conservation, independently of the action-threshold
argument. It does not select among its extensions. Requiring each
separate energy to be finite is an additional regularity premise;
finite total energy does not entail it, as the critical domain shows.
The specified bounded-source and subcritical-coupling limits give
independent mathematical support for the critical Dirac prescription
once those preparations are chosen. They do not prove that all source
regularizations have that limit or that the ideal point source is
mandatory. Klein--Gordon energy stability supports semibounded
principal forms; Friedrichs closure and a particular topology are
additional choices, and charge conservation is not positive
probability conservation. A finite-size source introduces further
data and is outside these point-source thresholds.

The unit $k/c$ agrees with the
[necessity-unit note](necessity-unit-and-indeterminacy.md) and the
[relativistic Kepler threshold](action-unit-dimensional-selection.md#singular-and-softened-relativistic-coulomb-cores).
That dimensional agreement supplies neither a selection principle
nor the measured value of $h$. In particular there is no single
unqualified set $[h_{\min},\infty)$ shared by these models.

## Stationary Kepler preparations

**5c. 6.1 Sol Max, 2026-11-19.** In 1713 Lemma X, Corollary 4
identifies the initial force through displacement in a short time.
Proposition VI applies it along an orbit. Proposition XXXI asks for the
position on a given ellipse at an assigned time. The following comparison
uses a modern stationary ensemble. Newton's propositions specify the
motion of each member. [Lemma X and its revision](newton-insertion-action.md#lemma-x-and-the-measurement-of-initial-force)
and [Proposition XXXI, second edition](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00082#par286)
(passages).

Fix a particle mass $m$, a gravitational parameter $\mu=GM>0$ and a
positive signed angular momentum $J$ in a specified plane. The potential
is $-m\mu/r$. Set the length $R$, inverse time $\omega$, semimajor axis
$A$, energy $E$ and total Kepler action $I$ by

$$
 R=\frac{J^2}{m^2\mu},\qquad \omega=\sqrt{\frac{\mu}{R^3}},\qquad
 A=\frac94R,\qquad E=-\frac{m\mu}{2A},\qquad I=m\sqrt{\mu A}=\frac32J .
$$

Require stationarity and the sharp constants $E,J$. A classical
invariant probability is uniform in time on each of its ellipses.
Their orientations can have any distribution because the readout is
radial. The eccentricity satisfies $1-e^2=R/A$, so the periapsis
$A(1-e)>0$ makes Newton's short-time force limit regular along every
orbit in this preparation. In eccentric anomaly $u$ the radius is
$A(1-e\cos u)$ and uniform time has measure
$(1-e\cos u)\,du/(2\pi)$. These are the standard elliptic Kepler
relations. [JPL, chapter 7, equations (7-48)–(7-56)](https://spsweb.fltops.jpl.nasa.gov/portaldataops/mpg/MPG_Docs/MPG%20Book/Release/Chapter7-OrbitalMechanics.pdf)
(passage). They give

$$
 \overline{r^{-2}}=\frac{1}{A^{3/2}\sqrt R},\qquad
 r_{\mathrm{cl}}:=\overline r=\frac{3A-R}{2}=\frac{23R}{8}.
$$

Here and below the force observable is its *inward magnitude*
$m\mu/r^2$. On the classical orbit it is twice the mass times the
leading inward displacement from the inertial continuation, divided by
the squared time step. On a quantum state we use the expectation of the
same position function as a positive quadratic form.

Write $a>0$ for the trial reduced action ($h$ above, $h_P=2\pi a$).
Use the single-valued, spinless planar Schrödinger representation and
the Friedrichs Hamiltonian. Confinement of configuration space to the
plane is a model assumption. The regular bound states have
$J=ka$, $I=(n+k+\tfrac12)a$ for $k\ge1$ and radial index $n\ge0$.
At fixed $k$ each radial level is simple. The sharp inputs therefore
select one radial probability for each admissible action. The complete
list at our fixed $I/J$ is

$$
 k=2n+1,\qquad a_n=\frac{J}{2n+1},\qquad n=0,1,\ldots .
$$

This uses the exact [planar spectrum and radial eigenfunctions, Appendix A](https://arxiv.org/pdf/math-ph/0205031)
(passage, Parfitt and Portnoi), extending the [fixed-torus phase comparison](rivero-1998-conjecture-central-forces.md)
to the position law. In the standard radial moment formulas put
$\eta=I/a$, $L=k-1/2$ and $Z=m^2\mu/a^2$ in physical length units.
They give

$$
 \begin{aligned}
 \langle r^{-2}\rangle_a&=\frac{1}{A^{3/2}\sqrt R},\\
 \langle r\rangle_a&=r_{\mathrm{cl}}+\frac{a^2}{8m^2\mu},\\
 \langle r^2\rangle_a&=\frac A2
 \left(5A-3R+\frac{7a^2}{4m^2\mu}\right)\le\frac{45}{4}R^2 .
 \end{aligned}
$$

The last bound uses $a\le J$. The equality of mean force holds on the
entire sequence, down to the classical limiting value. The shift in the
mean radius uses planar angular momentum. In three dimensions fixing
$L^2=a^2\ell(\ell+1)$ removes this particular shift.
[Dehesa and Puertas-Centeno, equations (17), (26)](https://arxiv.org/pdf/2011.12242)
(passage, with $D=2$, $k>0$ here).

**One bounded readout.** Prescribe a radial bin width $\rho=R/1024$,
a maximum reading $B=1024R$, and a uniform time of reading in
$[1/\omega,2/\omega]$. Use these same length and time resolutions
for every $a$. Stationarity permits any independently fixed clock window
of positive duration. The observable and its mean reading are

$$
 F(r)=\rho\left\lfloor\frac{\min(r,B)}{\rho}\right\rfloor,\qquad
 M=\langle F(r)\rangle .
$$

For example, the exact reading specified at $a=J/3$ is
$\int_0^\infty F(Rs)p_1(s)\,ds$. With respect to $ds$ for $s=r/R$,
the cited eigenfunctions give the two densities

$$
 p_0(s)=\frac{(4/3)^4}{6}\,s^3 e^{-4s/3},\qquad
 p_1(s)=\frac{4^8}{9\cdot7!}\,s^7(7-4s)^2e^{-4s}.
$$

Since $(r-B)_+\le r^2/(4B)$, the loss from rounding and clipping obeys
$0\le\langle r\rangle_a-M\le\rho+\langle r^2\rangle_a/(4B)
\le61R/16384<R/250$. The disjoint readings can consequently be
specified by intervals, without resolving the individual radial nodes.

| Preparation at the same $E,J$ | Mean reading $M/R$ |
|---|---|
| $a=J$ | between $3-1/250$ and $3$ |
| $a=J/3$ | between $26/9-1/250$ and $26/9$ |
| Every $a=J/(2n+1)$ with $n\ge2$ | at most $23/8+1/200$ |
| Stationary Newtonian ellipses | at most $23/8$ |

Thus a reading in the second interval identifies $a=J/3$ within these
sharp preparations. The conic reproduces the exact mean force of that
state. Its different mean radius is the additional datum that matters.
The dimensional inputs are $m,\mu,J$, the energy chosen above, and the
fixed length and time windows. Here the reference action is $S_0=J$
and $\epsilon=a/J$. At fixed
$m,\mu,J$, scaling $a$ changes the allowed indices and the second line
of the moment formula. If instead $m,J,E,a$ are all multiplied by the
same positive number with $\mu$ fixed, then $H_a/a$, $R,A,\omega$ and
the entire sequence of radial readout laws in corresponding states are
unchanged. A radius and a clock alone therefore fix no mass normalization.

**Finite preparation tolerances.** Allow stationary states with joint
energy and angular momentum supported in $|E'-E|\le\zeta |E|$,
$|J'-J|\le\xi J$, with $0\le\zeta,\xi<1$. In each component
$A'\le A/(1-\zeta)$ and $R'\ge R(1-\xi)^2$. Different energy
components add by stationarity. The radial observable commutes with
angular momentum, so components of a degenerate energy with different
angular indices also add. Applying the first radial moment in each
component, and $F(r)\le r$, gives

$$
 a^2\ \ge\ 8m^2\mu
 \left[M-\frac12\left(\frac{3A}{1-\zeta}-R(1-\xi)^2\right)\right]_+ .
$$

For a classical stationary preparation the same upper bound on $M$
holds with $a=0$. At $\zeta=\xi=1/1024$ the classical upper bound
increases by less than $(27/(8\cdot1023)+1/1024)R$. Even the lower
end of the $J/3$ interval then forces $a>J/5$. This bound applies to
all trial actions admitting a state in the bands, including ones absent
from the sharp list.

**How much preparation information does the force give?** With just
the *mean* energy $E$ and sharp $J$, there is a classical stationary
ensemble giving exactly the $J/3$ binned mean. Compare a single-energy
ensemble to an equal mixture on $E(1-1/10)$ and $E(1+1/10)$. Both
have mean energy $E$. The second has mean radius
$r_{\mathrm{cl}}+3A/(2\cdot99)$. Its radii are below $5R$, so rounding
costs at most $R/1024$. Its reading lies above $26R/9$ and the
single-energy reading lies below $26R/9-R/250$. A convex combination
matches the specified $M$ exactly.

The mean inverse-square force distinguishes this mixture. For any
stationary bound ensemble at sharp $J$, let $x=|E'|/|E|$ and suppose
$\langle x\rangle=1$. In either model the force mean divided by the
sharp-energy force mean is $\langle x^{3/2}\rangle$. Indeed
$A'=A/x$ in the common inverse-square moment. Strict convexity makes
equality possible only at $x=1$ almost surely. More quantitatively,
$0<x\le A/R=9/4$ and $(x^{3/2})''\ge1/2$ there, so
$\operatorname{Var}(x)\le4(\langle x^{3/2}\rangle-1)$.
The two mean inputs, energy and force at fixed $J$, can thus enforce
the sharp-energy preparation in either theory. The Newtonian ellipse
satisfies both and survives every time refinement. A requirement on
its radial distribution is still missing.

## Three radial readings on a near-circular Kepler orbit

**5d. 6.1 Sol Max, 2026-11-19.** One inverse-square source also permits
a time-dependent comparison. Keep $m,\mu,J,R,\omega$ from §5c, and now
use a preparation near the circle $r=R$. The three times, in units
$\theta=\omega t$, are $2\pi/3,4\pi/3,2\pi$. At each time average a
single radial reading over the same distribution of clock offsets.
Each term is a one-time marginal of the same initial law.

For a classical ellipse of eccentricity $0<e<1$ and angular momentum
$J$, the semimajor axis is $R/(1-e^2)$. The condition $r>R$ is
$\cos u<e$ in eccentric anomaly. In mean anomaly $u-e\sin u$ this is
an **open arc** of length $W(e)$. The clock advances mean anomaly by
$v(e)$ between successive readings, where

$$
 W(e)=\pi+2\arcsin e+2e\sqrt{1-e^2},\qquad
 v(e)=\frac{2\pi}{3}(1-e^2)^{3/2}.
$$

The gaps between the three sampled phases on the circle are $v,v,2\pi-2v$.
The shortest closed arc containing all three has length $2v$. Since
$W'(e)=4\sqrt{1-e^2}$ and $v$ decreases, there is exactly one
$e_c\in(0,1)$ with $W(e_c)=2v(e_c)$. For $0<e\le e_c$ at most two
of the three readings can have $r>R$, including at equality. Above
$e_c$ some initial phase realizes all three. In particular $e_c>1/10$,
since $W(1/10)\le\pi+2/5<2v(1/10)$. On the circular orbit all three
strict inequalities fail. The same bound holds for any common clock
shift, hence for the average of shifted triples. This uses the Kepler
clock in §5c.

Here is an explicit pair with finite time and radius resolutions. Use
$d=10^{-8}$, $X=(r/R-1)/d$, $\delta=10^{-4}$ and the bounded reading
$f(X)=\max(0,\min(1,X/\delta))$. Its transition width in length is
$Rd\delta$. Take the clock offset uniform on $[-10^{-3},10^{-3}]$ in
$\theta$ units, a physical window $2\cdot10^{-3}/\omega$. Let $P$ be
the average of the three expectations of $f$. Compare
$a=Jd^2\tau$ for $\tau=1,1/3$. Both have integer angular index $J/a$.
Prescribe the same **real radial half-density**, including its signs,
in $L^2(dX)$. It is proportional to $\chi(dX)\phi(X)$, where

$$
 \phi=\frac1{\sqrt2}
 \left(\frac4{\sqrt{21}}\,|0\rangle-|3\rangle
                  +\sqrt{\frac5{21}}\,|6\rangle\right).
$$

Here $|j\rangle$ are the unit oscillator Hermite functions in $X$.
Take $0\le\chi\le1$, equal to one on $|y|\le1/32$ and zero on
$|y|\ge1/16$. On each transition use $1-10z^3+15z^4-6z^5$ with
$z=32|y|-1$. Thus $\|\chi'\|_\infty\le64$ and
$\|\chi''\|_\infty\le15360$. The angular factor is
$e^{i(J/a)\vartheta}/\sqrt{2\pi}$ in the polar angle $\vartheta$.
The two inputs agree in initial radial density, radial current (zero)
and angular momentum. Their radial momentum variances depend on $a$.
The coherent profile and oscillator sign observable are borrowed.
[Zaw and Scarani, equation (3) and figure 2](https://arxiv.org/pdf/2212.06017)
and [Zaw, Aw, Lasmar and Scarani, equation (D11)](https://arxiv.org/pdf/2204.10498)
(passages).

The following bound controls the transfer from that oscillator to the
actual Kepler flow. Subtract the circular energy
$E_c=-m\mu/(2R)$ and use energy unit $mR^2\omega^2d^2$. After absorbing
the radial Jacobian the exact equation on $X>-1/d$ is

$$
 i\tau\partial_\theta u=H_\tau u,\qquad
 H_\tau=\frac{\Pi_\tau^2}{2}
       +\frac{X^2}{2(1+dX)^2}-\frac{\tau^2d^2}{8(1+dX)^2},
 \qquad \Pi_\tau=-i\tau\partial_X .
$$

Let $G_\tau(\theta)$ be the whole-line oscillator evolution with
potential $X^2/2$, and put $Q=X$, $\Pi=-i\partial_X$.
The Heisenberg position is $Q\cos\theta+\tau\Pi\sin\theta$ and
the momentum is $-Q\sin\theta+\tau\Pi\cos\theta$. Each pair of
coefficients has Euclidean norm at most one. A rotated quadrature on
number indices $\le N$ raises the largest index by at most one and
has norm there at most $\sqrt{2N+1}$, by $Q^2+\Pi^2=2N_{\rm op}+1$.
It follows that $\|XG_\tau\phi\|,\|\Pi_\tau G_\tau\phi\|\le\sqrt{13}$
and $\|X^3G_\tau\phi\|\le\sqrt{13\cdot15\cdot17}<58$.

On the support of $\chi(dX)$ the potential differs from $X^2/2$
by at most $2d|X|^3+\tau^2d^2/4$. Compare the exact solution with
$\chi(dX)G_\tau\phi$ using Duhamel's formula. The kinetic commutator
costs at most $64\tau d\sqrt{13}+7680\tau^2d^2$ in the residual.
Initial normalization and the final cutoff each cost at most
$32\sqrt{13}\,d$ in norm by the bound on $\|XG_\tau\phi\|$. Extending the
half-line solution by zero, for $0\le\theta\le7$ this gives

$$
 \|u(\theta)-G_\tau(\theta)\phi\|
 \le 64\sqrt{13}\,d+
 7\big(116d/\tau+64\sqrt{13}\,d+7681\tau d^2\big)<5000d .
$$

For the sharp half-line oscillator observable the probability is
$1/2+C\cos(3\alpha)$, where $C=\sqrt7/(8\sqrt\pi)$ and
$\alpha=\arg(\cos\theta+i\tau\sin\theta)$. Indeed, parity leaves
only the $0,3$ and $3,6$ cross terms, whose half-line matrix elements
from (D11) above are $-1/(2\sqrt{3\pi})$ and
$-\sqrt5/(8\sqrt{3\pi})$. At the three central times its average is
$1/2+C$ for $\tau=1$ and $1/2+C/3$ for $\tau=1/3$.
The clock costs at most $9C\cdot10^{-3}$ since $|\alpha'|\le3$.
For the ramp, the rotated Hermite superposition has position density
at most $2\sqrt{13}$ by the one-dimensional Sobolev bound. The dilation
$|\cos\theta+i\tau\sin\theta|\ge1/3$ therefore costs at most
$6\sqrt{13}\,\delta$ in probability. Adding the Kepler comparison
error $10^4d$, each actual $P$ is within $7/1000$ of its respective
value. Thus the first action scores above $2/3+1/100$, and the
second below $2/3$, at the same fixed resolutions.

The classical comparison can use an independently stated energy
allowance. Require $\langle H-E_c\rangle\le20mR^2\omega^2d^2$ and
sharp $J$. Both quantum preparations satisfy it. On their support
$(1+dX)^{-2}\le(16/15)^2$, the unnormalized kinetic norm is
$\le\sqrt{13}+64d$, and $\|\chi(dX)\phi\|\ge1-32\sqrt{13}\,d$.
These bounds give $\langle H_\tau\rangle<20$. A classical initial
law with the same radial density and zero radial velocity also qualifies.
For every classical conic at this $J$,
$e^2=2(H-E_c)/(mR^2\omega^2)$. At most $4000d^2$ of any admissible
positive law can have $e>1/10$, including unbound trajectories.
The pointwise arc bound gives $P\le 2/3+4000d^2/3$ for the full law.
The specified coherent preparation supplies the excess. Classical
stationarity or Newton's short-time force prescription does not supply
its relative signs.

## 6. What the theorem establishes and what it does not

Theorem 1 compares an incomplete classical point-force flow with a
global non-relativistic Coulomb unitary evolution. Section 5a proves
the fixed-interval Kepler localization and both first-moment limits
under its stated regularization and coherent-preparation hypotheses.
Proposition 2 assigns endpoints to explicit selection criteria; it
does not derive those criteria from Newton's axioms.

The planar calculations use the form realization of §3 and its regular
bound states. Critical full Klein--Gordon dynamics under the no-log
prescription, long-time or shrinking-regularization estimates, and
necessity of a positive physical action remain open here.
Classical regularizations remain possible added prescriptions,
and Dirac self-adjoint extensions exist at every $h>0$ if boundary
data are allowed. Excluding those routes requires an independently
justified premise. The quartic Newtonian initial-value problem is
globally well posed; its contrast concerns the particular classical-first
time-slicing construction. These limitations are part of the statement,
not consequences to be inferred from a threshold formula.

## 7. Consequence for STATE

For the planar inverse-square source, Lemma X's mean force at fixed
$E,J$ agrees with every state on an exact sequence $a\downarrow0$.
At sharp inputs the bounded radial reading selects $J/3$. At the stated
finite tolerances it excludes every $a\le J/5$. The classical ellipse satisfies
the same conserved inputs and force law. The open question is which
independent principle about admissible central-force motion requires a
different radial law. The separate foundational note depends on that step.

The fixed-$T$, fixed-$\delta$ localization obligation (L) and the
Kepler centroid obligation are closed by the written derivation in
§5a. Replace the former unqualified action interval by Proposition 2's
selection-dependent sets: Dirac finite-potential selection $(k/c,\infty)$,
Dirac critical-form/cutoff selection $[k/c,\infty)$, and Klein--Gordon
strict-energy construction $(2k/c,\infty)$; its radial principal
Friedrichs endpoint is included, with full critical dynamics still open.
The October 1 referee acceptance applies to the original
Theorem 1 as then printed. The October 2 localization, moment proof
and replacement Proposition 2 are written, source-supported additions
by Codex and have not received independent verification or referee
acceptance.
