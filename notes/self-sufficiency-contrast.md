# The self-sufficiency contrast: where Newton's axioms leave motion undefined, the theory with $h>0$ defines it

The thesis in STATE says that Newton's mechanics is the large-action
regime of a theory with $h>0$, and that it needs $h$ because its own
axioms do not make a complete theory of motion. This note proves the
first piece of evidence for that claim as one theorem with four parts,
for Kepler's force. The classical flow of $V=-k/r$ is incomplete:
every zero-angular-momentum datum that moves inward, or is bound,
reaches the centre in finite time, with the explicit collision time
$t_c=\tfrac\pi2\sqrt{mr_0^3/2k}$ for fall from rest, and Newton's
axioms give no continuation there. The quantum Hamiltonian
$-\tfrac{h^2}{2m}\Delta-k/r$ is self-adjoint on the domain of the
Laplacian and generates a global unitary group for every state and
every $h>0$, by Kato's theorem, cited with its hypotheses. The same
contrast holds for the quartic between the fixed-$h$ unitary limit and
the classical-first construction that needs a branch rule. And the
classical trajectory is a derived object of the $h>0$ theory: for
quadratic forces the centroid of any state obeys Newton's equation
exactly at every $h$, and for Kepler's force a coherent state follows
the orbit in the large-action regime for finite times away from the
collision set, by Hepp's theorem, cited with its hypotheses and with
the one further localization hypothesis the singular potential needs.
Parts (a), (c) and the quadratic half of (d) are proved here; (b) and
the Kepler half of (d) rest on the cited theorems. Proposition 2 then
gives the gap the exercise is for: with finite $c$, the theories of
Kepler's force that define motion without an added rule are exactly
those with $h\ge k/(\alpha_cc)$, by the self-adjointness thresholds of
the relativistic Coulomb problem, cited; Newton's theory at $h=0$ and
every theory with $0<h<k/(\alpha_cc)$ are not self-sufficient. Written by Claude
Fable, 2026-10-01; proof status recorded in the final section.

Notation: $h$ is the reduced phase constant, $m>0$ the mass, $k>0$ the
force constant, $r=|x|$ in $\mathbb R^3$; the planar case is a remark.

## 1. Statement

**Theorem 1 (self-sufficiency contrast for Kepler's force).**

(a) *Classical incompleteness.* Let $L=x\times p$ be the angular
momentum. Every initial datum with $L=0$ whose radial velocity is
inward or zero, and every datum with $L=0$ and negative energy,
reaches $r=0$ at a finite time. For a body released from rest at
distance $r_0$ the collision time is
$$t_c=\frac\pi2\sqrt{\frac{m\,r_0^3}{2k}},\tag{1}$$
and in general $t_c\le\tfrac\pi2\sqrt{m r_{\max}^3/2k}$ with $r_{\max}$
the largest distance reached. The collision set
$\mathcal C=\{L=0,\ \dot r\le0\ \text{or}\ E<0\}$ is nonempty,
invariant under the flow while it exists, and of measure zero in phase
space. On $\mathcal C$ the vector field is unbounded at the endpoint
and Newton's axioms, the Laws together with the force law, define no
continuation: the flow of Kepler's force is not complete.

(b) *Quantum completeness.* For every $h>0$, $m>0$ and real $k$, the
operator
$$H_h=-\frac{h^2}{2m}\Delta-\frac kr\qquad\text{on }L^2(\mathbb R^3)\tag{2}$$
is self-adjoint on the domain $H^2(\mathbb R^3)$ of the Laplacian and
bounded below, and $U_h(t)=e^{-itH_h/h}$ is a strongly continuous
unitary group defined for every $t\in\mathbb R$ and every initial
state in $L^2(\mathbb R^3)$. This is Kato's theorem [@Kato1951;
metadata], whose hypothesis, that the potential is the sum of an
$L^2(\mathbb R^3)$ and a bounded function, is verified in §3.

(c) *The quartic contrast.* For $V=\lambda q^4$ on the line, Theorem
2(b) of the [1998-conjecture note](rivero-1998-conjecture-central-forces.md)
gives, for every $h>0$, the strong convergence of the time-sliced
operators to the unitary evolution $e^{-iTH_h/h}$ along every sequence
of partitions, with no extra datum; Theorem 1 there shows that the
halved classical-first construction at zero resolution has no limit on
a two-cell partition with three stationary paths, and Theorem 2(a)
there repairs it only by a branch rule chosen by hand. The fixed-$h$
construction exists for all data; the construction at zero needs a
rule the action does not supply.

(d) *The classical trajectory as a derived object.* (d1) For
$H=p^2/2m+V$ with $\deg V\le2$, the expectations $\langle q\rangle_t$,
$\langle p\rangle_t$ of every state with finite second moments obey
Newton's equations exactly for every $h>0$,
$$\frac{d}{dt}\langle q\rangle_t=\frac{\langle p\rangle_t}m,\qquad
\frac{d}{dt}\langle p\rangle_t=-V'(\langle q\rangle_t),\tag{3}$$
and a coherent state stays a Gaussian whose centroid is the classical
trajectory. (d2) For Kepler's force, let $z_0=(x_0,p_0)$ lie on a
classical orbit whose distance from the centre stays at least
$\rho_{\min}>0$ on $[0,T]$. Under Hepp's theorem, stated in §5 with its
hypotheses, applied to a smooth potential $V_\delta$ equal to $-k/r$
for $r\ge\delta$ with $0<\delta<\rho_{\min}$, the coherent state
$\varphi^h_{z_0}$ with $\sigma_h^2\propto h$ evolves under $H^{(\delta)}_h$
into a Gaussian centred on the Kepler orbit $z_t$ up to an $L^2$ error
tending to zero as $h\to0$, uniformly on $[0,T]$; and under the
localization hypothesis (L) of §5 the same holds for the Coulomb
evolution $U_h(t)$ itself.

*Conclusion.* The theory with $h>0$ defines motion for all data and
all times, by (b), and yields Newton's trajectories where they exist,
by (d), while Newton's axioms leave motion undefined on the collision
set, by (a), and the construction at zero needs a rule the axioms do
not contain, by (c).

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

For a general datum with $L=0$ and $\dot r\le0$: if $E<0$ then
$r\le r_{\max}=-k/E$ throughout, $|\dot r|^2=\tfrac{2k}m(1/r-1/r_{\max})$,
and the time to the centre is at most the fall time from rest at
$r_{\max}$, which is (1) with $r_{\max}$; if $E\ge0$ then
$|\dot r|\ge\sqrt{2k/(mr)}$ and the time is at most
$\int_0^{r_0}\sqrt{mr/2k}\,dr=\tfrac23\sqrt{m/2k}\,r_0^{3/2}$. If $L=0$,
$E<0$ and $\dot r>0$, the body reaches $r_{\max}$ at a finite time
and then falls as before. Invariance of $\mathcal C$ follows from the
conservation of $L$ and $E$; $L=0$ is the condition that $p$ be
parallel to $x$, two independent equations on the six-dimensional
phase space, so $\mathcal C$ has measure zero. At $r=0$ the force
$-kx/r^3$ is unbounded; no existence or uniqueness theorem applies
there, and the Laws, which presuppose a defined force, assign no
motion. A continuation through the centre (Levi-Civita or
Kustaanheimo–Stiefel regularization) is an added rule, in the same
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

Verification for $V=-k/r$: put $V_1=-\tfrac kr\mathbf 1_{r<1}$ and
$V_2=-\tfrac kr\mathbf 1_{r\ge1}$. Then $|V_2|\le|k|$, and
$$\int_{\mathbb R^3}|V_1|^2d^3x=k^2\int_0^1\frac{4\pi r^2}{r^2}\,dr=4\pi k^2<\infty.$$
So the hypothesis holds for every real $k$, and $H_h$ in (2) is
self-adjoint on $H^2(\mathbb R^3)$ for every $h>0$, $m>0$. Stone's
theorem then gives the unitary group $U_h(t)$ for all $t\in\mathbb R$,
strongly continuous, defined on every $\psi\in L^2$, with
$U_h(t)\psi\in H^2$ for $\psi\in H^2$. No initial datum and no time is
excluded; the states supported near $r=0$ evolve like all others.
$\square$

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
$M_t\Sigma_hM_t^{\sf T}$; in the large-action regime of §3c there,
masses scaled by $\lambda$ at fixed $h$ and widths, the position width
$s_t(h)$ tends to the initial $\sigma$ and the state is as localized on
its trajectory as it was prepared. $\square$

*(d2), Kepler's force.* Hepp's theorem [@Hepp1974; metadata; the
statement used is the one standardly quoted from it, the primary text
was not read in this session], in the form used here: let $W$ be a
real $C^\infty$ potential on $\mathbb R^3$ with bounded derivatives of
every order $\ge2$, so that $-\tfrac{h^2}{2m}\Delta+W$ is self-adjoint
and the classical flow $\Phi_t$ of $p^2/2m+W$ is complete; let
$\varphi^h_{z}$ be the coherent state at $z=(x,p)$ with position width
$\sigma_h$, $\sigma_h^2=hL_*/P_*$ for fixed $L_*,P_*$; and let
$\varphi^h_{z_t,M_t}$ be the Gaussian centred at $z_t=\Phi_t(z_0)$ with
covariance transported by the linearized flow $M_t=D\Phi_t(z_0)$. Then
for every $T>0$,
$$\sup_{|t|\le T}\big\|e^{-itH^{W}_h/h}\varphi^h_{z_0}
-e^{i\theta_t/h}\varphi^h_{z_t,M_t}\big\|_{L^2}\longrightarrow0
\qquad(h\to0),\tag{4}$$
with $\theta_t$ the classical action along the trajectory. Apply this
with $W=V_\delta$, a $C^\infty$ function equal to $-k/r$ for
$r\ge\delta$ and bounded with bounded derivatives inside the ball: for
$r\ge\delta$ all derivatives of $-k/r$ of order $\ge1$ are bounded by
constants times $\delta^{-2},\delta^{-3},\ldots$, so $V_\delta$
satisfies the hypothesis. Since the Kepler orbit through $z_0$ stays
at distance $\ge\rho_{\min}>\delta$ on $[0,T]$, it is also the orbit of
$V_\delta$, and (4) gives the first claim of (d2): under
$H^{(\delta)}_h$ the coherent state follows the Kepler orbit.

For the Coulomb evolution itself, Duhamel's formula on the common
domain gives
$$U_h(t)\varphi-U^{(\delta)}_h(t)\varphi
=-\frac ih\int_0^tU_h(t-s)\,(V-V_\delta)\,U^{(\delta)}_h(s)\varphi\,ds,$$
so that
$\|U_h(t)\varphi-U^{(\delta)}_h(t)\varphi\|\le\tfrac Th\sup_{s\le T}
\|(V-V_\delta)U^{(\delta)}_h(s)\varphi\|$, where $V-V_\delta$ is
supported in the ball $r<\delta$. **Hypothesis (L):** 
$\sup_{s\le T}\|(V-V_\delta)U^{(\delta)}_h(s)\varphi^h_{z_0}\|=o(h)$ as
$h\to0$. Under (L) the Coulomb and regularized evolutions of the
coherent state coincide in the limit and (4) transfers to $U_h$. The
hypothesis says that the evolved state carries negligible mass and
energy inside the ball the orbit never visits; for the Gaussian
$\varphi^h_{z_t,M_t}$ alone it holds with an exponentially small bound,
by Hardy's inequality $\|f/r\|\le2\|\nabla f\|$ in $\mathbb R^3$ and the
Gaussian tails, but the $o(1)$ remainder in (4) is an $L^2$ statement,
and (L) requires its energy-norm counterpart, which is not proved
here. $\square$

## 5b. Proposition 2: with finite $c$, self-sufficiency has a smallest $h$

The point of the exercise is a gap in the admissible values of $h$,
the elementary analogue of a spectrum $\{0\}\cup[m,\infty)$. Theorem 1
alone gives none: by (b) every $h>0$ makes the non-relativistic
Coulomb theory complete, and the ground-state energy $-mk^2/2h^2$
tends to $-\infty$ as $h\to0$ without any threshold. The threshold
appears when the speed of light is finite, through the known
self-adjointness limits of the relativistic Coulomb problem.

**Proposition 2 (smallest $h$ at finite $c$).** Let $c<\infty$ and
$\nu=k/(hc)$, the Coulomb coupling in units of $hc$.
(i) *Spin one half.* The Dirac--Coulomb operator
$c\,\alpha\cdot p+\beta mc^2-k/r$ on $L^2(\mathbb R^3)^4$ has a
distinguished self-adjoint extension, selected by finiteness of the
potential energy on its domain, for $\nu<1$ [@Schmincke1972;
@Wuest1975; @Nenciu1976; metadata], and is essentially self-adjoint
on $C_c^\infty(\mathbb R^3\setminus\{0\})^4$ for $\nu\le\sqrt3/2$;
for $\nu>1$ every self-adjoint realization requires a boundary
condition at the centre, an added rule in the sense of Theorem 1(a)
and (c).
(ii) *Spin zero.* For the Klein--Gordon equation with the Coulomb
potential the $s$-wave radial problem is regular at the origin iff
$\nu\le\tfrac12$ [@Case1950; metadata]; beyond it the solutions
oscillate without limit at the centre and a boundary condition must
be imposed.
(iii) Hence the theories of Kepler's force at finite $c$ that define
the motion without an added rule are exactly those with
$$h\ \ge\ h_{\min}=\frac{k}{\alpha_c\,c},\qquad
\alpha_c=1\ (\text{spin }\tfrac12),\quad\alpha_c=\tfrac12\ (\text{spin }0),\tag{5}$$
with the strict inequality in the spin-one-half case. Together with
Theorem 1(a), the set of values of $h$ at which a theory of Kepler's
force is self-sufficient is $[h_{\min},\infty)$: Newton's theory at
$h=0$ is incomplete, no theory with $0<h<h_{\min}$ is self-sufficient,
and every theory with $h\ge h_{\min}$ is. This is the gap. In the
non-relativistic limit $c\to\infty$, $h_{\min}\to0$ and the gap
closes, in agreement with Theorem 1(b).

*Proof.* (i) and (ii) are the cited theorems, read at the metadata
level and in their standard statements; the thresholds are stated as
they are standardly quoted, with the essential self-adjointness bound
$\sqrt3/2$ due to Weidmann, not separately cited here. (iii) is the
translation $\nu<\alpha_c\iff h>k/(\alpha_cc)$, together with Theorem
1(a) at $h=0$. $\square$

The unit $k/c$ is the one the
[necessity-unit note](necessity-unit-and-indeterminacy.md) isolated as
the unique mass-independent action built from $k_e$ and $c$, and the
[relativistic Kepler note](relativistic-kepler-threshold.md) found the
same threshold classically as $\ell>k/c$ for regular bound motion.
Proposition 2 places it where the thesis needs it: as the lower edge
of the set of self-sufficient theories. What it does not do is fix
$h$: any $h\ge h_{\min}$ is admissible, and the physical value exceeds
$h_{\min}$ by the inverse fine-structure ratio, which is the separate
calibration obligation.

## 6. What the theorem establishes and what it does not

The contrast is between two theories of the same force law. Newton's,
the Laws with $F=-kx/r^3$, assigns no motion to the collision set and,
for the quartic, cannot even be constructed at zero resolution without
a rule the action does not supply. The theory with $h>0$ assigns a
motion to every state for all time, by self-adjointness, and recovers
Newton's trajectories as the centroids of localized states, exactly for
quadratic forces and, in the large-action regime and away from
collisions, for Kepler's force under the cited theorem. The thesis in
STATE reads this as the sense in which Newton's mechanics needs $h$:
its only completion is the large-action regime of a theory that
contains $h$.

Not established here: the energy-norm localization (L) for the
Coulomb evolution; the planar operator beyond the standard form
construction; any statement that no completion of Newton's mechanics
without $h$ exists, which is the open obligation (ii) of STATE; and
anything about long times, where the Ehrenfest-type breakdown of (4)
is a separate matter. The theorem is evidence for the thesis, in the
form the thesis now has, and no more.

## 7. Consequence for STATE

Proposition 2 supplies the gap: the self-sufficient theories of
Kepler's force at finite $c$ have $h\ge k/(\alpha_cc)$, with Newton at
$h=0$ outside; it rests on cited thresholds and fixes no value of $h$.
Theorem 1 supplies the self-sufficiency contrast required by STATE's
obligation (iii): classical incompleteness with the explicit collision
time and collision set (proved), quantum completeness by Kato's theorem
(cited, hypothesis verified), the quartic contrast (proved in the
1998-conjecture note), and the classical trajectory as the derived
centroid, exact for quadratic forces (proved) and for Kepler's force
under Hepp's theorem and hypothesis (L) (cited). Next: prove (L) for
the Coulomb evolution of a coherent state, or replace Hepp's $L^2$
statement by an energy-norm one; then the open obligation (ii), that
no completion without $h$ exists. Proof status: written by Claude
Fable, 2026-10-01; parts (a), (c), (d1) proved, (b) and (d2) cited
with hypotheses; refereeing recorded in the status line when done.
