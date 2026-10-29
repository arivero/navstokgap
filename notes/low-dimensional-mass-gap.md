# Low-dimensional gauge gaps: matrix confinement, conditional floors and scales

With supplied physical $\hbar>0$, $m>0$ and $g>0$, the scalar
$H=-\hbar^2\Delta/(2m)+g^2x^2y^2/2$ and the bosonic $SU(2)$ model with at
least two matrices have compact resolvent and a simple positive ground state.
Their excitation gap is a positive finite number times
${E_*} =\hbar^{4/3}g^{2/3}m^{-2/3}$. The proof uses transverse oscillator
bounds, compactness and positivity improvement. The gauge-invariant sector
inherits a positive gap; its first excitation need not equal the unrestricted
one. These are quantum-mechanical spectral theorems, not construction of a
continuum Yang--Mills theory.

A supplied **classical** transverse orbit-area floor gives a different result:
it bounds energy sublevel sets and makes their phase-space volume finite.
It does not define a quantum Hamiltonian, discretize levels, or by itself give
a positive energy gap. The precise volume asymptotics, semiclassical estimates
and dimensional comparisons below retain their conditional status. In four
spacetime dimensions $1/g_{\rm cl}^2$ is already an action unit; its cancellation
from the classical field equations does not mean that the action has no
normalization. An action unit supplies neither an energy scale nor a gap there.

This treatment incorporates C131--C133 and the former G07/G08 comparison.
Borrowed spectral theorems, elementary proofs, conditional classical restrictions,
semiclassical estimates and open questions are labelled separately. Repository
reviews are internal written checks; no independent peer review or literature
novelty is claimed.

## 1. Observables, units and conventions

A gap is an energy difference of a specified self-adjoint operator. For an
isolated simple ground state it is $E_1-E_0$; a field-theoretic mass gap also
requires the physical state space, vacuum, continuum construction and limiting
order. A classical action floor instead takes an infimum of a specified action
observable over an admitted class. Neither is a statement about all possible
classical completions or instruments.

The [dimensional and similarity proofs](action-unit-dimensional-selection.md)
apply to any observable dimension $d_X$ (C131): if the floor depends only on the
fixed constants and $d_X$ is outside their dimension span, a finite positive
universal floor is impossible. Otherwise it is a dimensional monomial times a
function of dimensionless ratios. An admitted similarity scaling one positive
value arbitrarily close to zero gives zero infimum. These are necessary unit
and class tests, not sufficient positivity arguments.

In the mechanical model $g$ denotes its quartic coupling. For connection-valued
fields use $g_{\rm cl}$ with
$[1/g_{\rm cl}^2]=\mathrm{action}\,\mathrm{length}^{4-d}$; the dimensionless
four-dimensional coupling is $g_4^2=\hbar g_{\rm cl}^2$. The torus formula in
§3.4 retains $g$ for $g_4$ as explicitly stated there. Energy units are denoted
${E_*}$; they are unrelated to the dimensionless regulator $\epsilon=\hbar/S_0$,
time mesh or record resolution. Write $h_P=2\pi\hbar$ for Planck's constant.

## 2. The exact $\hbar$-scaling of spectra for homogeneous potentials

**Theorem 3.** Take $m,\lambda,\hbar>0$. Let $V\ge0$ be continuous on $\mathbb R^n$ and positively
homogeneous of degree $k>-2$, $V(sx)=s^kV(x)$, and let
$H=-\frac{\hbar^2}{2m}\Delta+\lambda V$ be the Friedrichs operator of its
form on $C_0^\infty$. With the unitary dilation
$(U_\ell\psi)(x)=\ell^{-n/2}\psi(x/\ell)$ and
$$\ell^{k+2}=\frac{\hbar^2}{m\lambda},\qquad
{E_*}=\frac{\hbar^2}{m\ell^2}
=\hbar^{\frac{2k}{k+2}}\,\lambda^{\frac{2}{k+2}}\,m^{-\frac{k}{k+2}},$$
one has $U_\ell^{-1}HU_\ell={E_*}\,(-\tfrac12\Delta+V)$. Every
spectral datum of $H$, in particular any gap, is ${E_*}$ times the
corresponding pure number of $-\tfrac12\Delta+V$.

*Proof.* $\Delta(U_\ell\psi)=\ell^{-2}U_\ell(\Delta\psi)$ and
$V\,U_\ell\psi=\ell^{k}U_\ell(V\psi)$ on $C_0^\infty$, which $U_\ell$
preserves; so $U_\ell^{-1}HU_\ell=\frac{\hbar^2}{m\ell^2}(-\tfrac12\Delta)
+\lambda\ell^kV$, and the choice of $\ell$ equates the two coefficients. The
identity passes to the Friedrichs extensions because $U_\ell$ maps the form
on the core to the transformed form. Unitary equivalence preserves spectra
and multiplicities. $\square$

**Proposition 4 (classical similarity).** For the classical Hamiltonian
$|p|^2/2m+\lambda V(x)$ with $V$ homogeneous of degree $k$, the map
$x\mapsto sx$, $t\mapsto s^{1-k/2}t$ carries solutions to solutions,
multiplies energies by $s^k$ and the action along a trajectory by
$s^{1+k/2}$ (Landau--Lifshitz, *Mechanics* §10; verified against the
equation of motion: $m\ddot x$ scales as $s/s^{2-k}=s^{k-1}$ and
$\lambda\nabla V$ as $s^{k-1}$). Hence for $k>0$ the range of the classical
Hamiltonian is $[0,\infty)$: the classical energy floor is zero, and the
classical action floor is zero by the similarity theorem cited in §1.

For $k>0$, any *proved* gap scales to zero as $\hbar\to0$ or
$\lambda\to0$; the dilation alone does not prove that a gap exists. The
oscillator ($k=2$), quartic model ($k=4$) and a box of supplied length give
units $\hbar\sqrt{\lambda/m}$, $\hbar^{4/3}\lambda^{1/3}m^{-2/3}$ and
$\hbar^2/(m\ell^2)$ respectively. The action-critical degree $k=-2$ is
excluded from the theorem and treated in §6. Its classical action is
scale invariant, while $m\lambda$ has action-squared units.

For the separately defined attractive Coulomb problem, the familiar energy
unit is $m\lambda^2/\hbar^2$; this singular negative potential does not
satisfy the theorem's $V\ge0$ continuity assumptions. Fixed-index hydrogenic
energies diverge negatively as $\hbar\to0$. Their accumulation at zero is
the *large principal-index* limit at fixed $\hbar$, not the same limit.

## 3. Quantum confinement of bosonic matrix valleys

### 3.1 The scalar model



**Theorem 5.** Let $H=-\frac{\hbar^2}{2m}\Delta+\frac{g^2}{2}x^2y^2$ on
$L^2(\mathbb R^2)$, defined as the Friedrichs operator of its form on
$C_0^\infty(\mathbb R^2)$.

1. As quadratic forms,
   $$H\ \ge\ \tfrac12K,\qquad
   K=-\frac{\hbar^2}{2m}\Delta+\frac{\hbar g}{2\sqrt m}\,(|x|+|y|).$$
2. $H$ has compact resolvent: its spectrum is a sequence
   $E_0<E_1<E_2<\cdots$ of eigenvalues of finite multiplicity tending to
   infinity.
3. $E_0$ is simple with a strictly positive eigenfunction, so
   $\Delta=E_1-E_0>0$, and $H-E_0$ satisfies the spectral-gap part of the Jaffe--Witten conditions
   with $0<m=\Delta<\infty$.
4. $E_n(\hbar,m,g)={E_*}\,e_n$ with $e_n$ the eigenvalues of
   $\tfrac12(-\Delta+x^2y^2)$ and
   $${E_*}=\hbar^{4/3}g^{2/3}m^{-2/3},\qquad
   \Delta=\delta_1\,\hbar^{4/3}g^{2/3}m^{-2/3},\quad\delta_1=e_1-e_0>0.$$
   Hence $\Delta\to0$ as $\hbar\to0$ and as $g\to0$. At $g=0$ the spectrum
   is $[0,\infty)$ with no eigenvalue. The classical Hamiltonian
   $|p|^2/2m+g^2x^2y^2/2$ has range $[0,\infty)$, and the motions
   $y=p_y=0$, $x(t)=x_0+p_xt/m$ escape to infinity along the valley with
   arbitrarily small energy.

*Proof.* **Oscillator bound.** For $\phi\in C_0^\infty(\mathbb R)$ and
$\mu,\nu>0$, with $\alpha=\sqrt{\nu/\mu}$, integration by parts gives
$\int|\phi'+\alpha y\phi|^2dy=\int|\phi'|^2+\alpha^2\int y^2|\phi|^2
-\alpha\int|\phi|^2$, so
$$\int\big(\mu|\phi'|^2+\nu y^2|\phi|^2\big)dy\ \ge\ \sqrt{\mu\nu}\int|\phi|^2dy .$$
With $\mu=\hbar^2/2m$ and $\nu=\tfrac12m\omega^2$ this is the zero-point
energy $\hbar\omega/2$ of the oscillator $-\frac{\hbar^2}{2m}\partial_y^2
+\frac12m\omega^2y^2$.

**Slicing.** Fix $x$ and apply the bound to $\phi=\psi(x,\cdot)$ with
$\nu=g^2x^2/2$, that is $m\omega_x^2=g^2x^2$, $\omega_x=g|x|/\sqrt m$,
$\sqrt{\mu\nu}=\hbar g|x|/(2\sqrt m)$. Integrating in $x$ (Fubini):
$$\int\Big[\frac{\hbar^2}{2m}|\partial_y\psi|^2+\frac{g^2}{2}x^2y^2|\psi|^2\Big]
\ \ge\ \int\frac{\hbar g|x|}{2\sqrt m}|\psi|^2,$$
and symmetrically with $x\leftrightarrow y$. Writing
$2q_H(\psi)=\int\frac{\hbar^2}{2m}|\nabla\psi|^2+\{\text{the $y$-slice}\}
+\{\text{the $x$-slice}\}$ and using the two slice bounds gives
$2q_H\ge q_K$ on $C_0^\infty$, which is Simon's display (5) with the
constants restored. The inequality extends to the form domain of $H$ by
density and shows $Q(H)\subset Q(K)$; the min-max values then satisfy
$\mu_n(H)\ge\tfrac12\mu_n(K)$.

**Compact resolvent.** Let $W\ge\gamma|x|$ be continuous with $\gamma>0$
and $K=-\frac{\hbar^2}{2m}\Delta+W$. On the unit form-ball
$\{q_K(\psi)+\|\psi\|^2\le1\}$ the mass outside the ball of radius $R$ is
at most $(\gamma R)^{-1}$ and the $H^1$ norm on the ball is bounded, so the
Rellich--Kondrachov theorem gives total boundedness in $L^2$; thus
$(K+1)^{-1/2}$ and $(K+1)^{-1}$ are compact (this is the case needed of
Reed--Simon IV, Theorem XIII.67). Here $W=\frac{\hbar g}{2\sqrt m}(|x|+|y|)
\ge\frac{\hbar g}{2\sqrt m}\sqrt{x^2+y^2}$. Since $\mu_n(H)\ge\tfrac12\mu_n(K)
\to\infty$, $H$ has compact resolvent as well (Reed--Simon IV, Theorem
XIII.16).

**Simplicity.** The Feynman--Kac formula
$(e^{-tH/\hbar}\psi)(x)=\mathbb E^x[\exp(-\hbar^{-1}\int_0^tV(b_s)ds)\psi(b_t)]$
with $V$ continuous and finite along paths shows that $e^{-tH/\hbar}$ is
positivity improving for every $t>0$, and Reed--Simon IV Theorem XIII.44
then gives a simple ground state with strictly positive eigenfunction.

**Scaling.** The unitary dilation with $\ell^6=\hbar^2/(mg^2)$ gives
$U_\ell^{-1}HU_\ell={E_*}\tfrac12(-\Delta+x^2y^2)$ directly,
fixing the stated dimensionless operator and all factors of two. At $g=0$ the Fourier
transform diagonalizes $-\hbar^2\Delta/2m$ as multiplication by
$\hbar^2|p|^2/2m$. The classical statements are direct: on the invariant set
$\{y=p_y=0\}$ Hamilton's equations reduce to free motion in $x$. $\square$

**Mechanism.** The valleys $\{xy=0\}$ are unbounded and the classical
phase-space volume below any positive energy is infinite, so a classical
particle escapes at arbitrarily low energy. The transverse zero-point
energy $\hbar\omega_x/2=\hbar g|x|/(2\sqrt m)$ grows linearly along a
valley and confines the quantum particle. That confining term is the
product of the two non-commutativities: $\hbar$ from $[x,p]=i\hbar$ and $g$
from the quartic coupling, which is the squared commutator of the gauge
potentials in Section 3.2. Removing either factor removes the gap, with the
exponents $4/3$ and $2/3$ of Theorem 5(4).

### 3.2 The SU(2) matrix model and its abelian valleys

Let $T^a=\sigma^a/2$, so $\operatorname{tr}T^aT^b=\tfrac12\delta^{ab}$ and
$[T^a,T^b]=i\epsilon^{abc}T^c$; let $X_i=x_i^aT^a$ with
$\vec x_i\in\mathbb R^3$, $i=1,\dots,D$. Then
$[X_i,X_j]=i(\vec x_i\times\vec x_j)^cT^c$ and
$-\operatorname{tr}[X_i,X_j]^2=\tfrac12|\vec x_i\times\vec x_j|^2$. The
Yang--Mills quantum-mechanical Hamiltonian is
$$H=-\frac{\hbar^2}{2m}\Delta_{\mathbb R^{3D}}
+\frac{g^2}{2}\sum_{i<j}|\vec x_i\times\vec x_j|^2
=-\frac{\hbar^2}{2m}\Delta_{\mathbb R^{3D}}-g^2\sum_{i<j}\operatorname{tr}[X_i,X_j]^2 ;$$
other trace or sum conventions multiply $g^2$ by a fixed number and every
energy by its cube root.

**Theorem 6.** For $D\ge2$:

1. For every ordered pair $i\neq j$, as forms,
   $-\frac{\hbar^2}{2m}\Delta_{\vec x_j}+\frac{g^2}{2}|\vec x_i\times\vec x_j|^2
   \ \ge\ \frac{\hbar g}{\sqrt m}|\vec x_i|$.
2. As forms on $L^2(\mathbb R^{3D})$,
   $$H\ \ge\ \tfrac12\Big[-\frac{\hbar^2}{2m}\Delta_{\mathbb R^{3D}}
   +\frac{\hbar g}{\sqrt m}\sum_{i=1}^D|\vec x_i|\Big].$$
3. $H$ has compact resolvent and a simple strictly positive ground state;
   its gap is $\Delta=\delta_1^{(D)}\,\hbar^{4/3}g^{2/3}m^{-2/3}>0$, with
   the same $\hbar\to0$ and $g\to0$ conclusions as Theorem 5.
4. The $SO(3)$ action $(U(R)\psi)(\vec x_1,\dots)=\psi(R^{-1}\vec x_1,\dots)$
   commutes with $H$; the invariant subspace, which Gauss's law selects in
   the constant-mode truncation of the gauge theory, reduces $H$, contains
   the ground state, and has gap $\Delta_{\rm inv}\ge\Delta>0$.
5. The potential vanishes exactly on the commuting configurations
   $\{\vec x_i=\lambda_i\hat n\}$, where all $X_i$ lie in one Cartan
   subalgebra. For $D=1$ there is no pair, $V\equiv0$, and
   $H=-\hbar^2\Delta_{\mathbb R^3}/2m$ has spectrum $[0,\infty)$.

*Proof.* (1) For fixed $\vec x_i\neq0$ choose an orthonormal frame of
$\mathbb R^3_{\vec x_j}$ with third axis along $\vec x_i$. Then
$|\vec x_i\times\vec x_j|^2=|\vec x_i|^2(u_1^2+u_2^2)$; drop the kinetic
term in $u_3$ and apply the oscillator bound in $u_1$ and in $u_2$ with
$\nu=g^2|\vec x_i|^2/2$, each giving $\hbar g|\vec x_i|/(2\sqrt m)$; the
complement $\vec x_i=0$ is a null set. Integrate over the remaining
variables. (2) Sum the pair inequalities over all $D(D-1)$ ordered pairs
with weight $w=1/(2(D-1))$: each kinetic term $T_j$ appears with total
weight $w(D-1)=\tfrac12$ and each unordered pair potential with weight
$2w=1/(D-1)\le1$. Then
$H=\sum_{i\ne j}w(T_j+V_{ij})+\tfrac12\sum_jT_j+(1-\tfrac1{D-1})\sum_{i<j}V_{ij}$,
where both remainders are nonnegative forms; dropping the potential
remainder and using (1) gives (2). (3) The bracket in (2) has
$W=\frac{\hbar g}{\sqrt m}\sum_i|\vec x_i|\ge\frac{\hbar g}{\sqrt m}|x|_{\mathbb R^{3D}}$,
so the compact-resolvent, simplicity and scaling steps of Theorem 5 apply
verbatim with $n=3D$, $k=4$. (4) $U(R)$ is unitary, preserves $C_0^\infty$,
commutes with each $\Delta_{\vec x_i}$ and preserves
$|\vec x_i\times\vec x_j|$; the Haar average $\int U(R)\,dR$ is the
orthogonal projection onto the invariant subspace and commutes with
$(H+1)^{-1}$, so the restriction is self-adjoint with compact resolvent. The
strictly positive simple ground state $\psi_0$ satisfies
$U(R)\psi_0=c(R)\psi_0$ with $c(R)>0$ and $|c(R)|=1$, hence is invariant, so
$E_0^{\rm inv}=E_0$ and $E_1^{\rm inv}\ge E_1$. (5) $\vec x_i\times\vec x_j=0$
for all pairs iff all nonzero vectors are parallel. $\square$

**The abelian and the two-dimensional cases.** Along the commuting
configurations the matrices commute and the potential is flat; writing
$\vec x_i=\lambda_i\hat n+\vec\xi_i$ with $\vec\xi_i\perp\hat n$, the
transverse curvature of the potential grows quadratically in $|\lambda|$,
which is what (1) exploits. An abelian gauge group has *only* commuting
configurations: its matrix model has $V\equiv0$ and the free spectrum
$[0,\infty)$. This is the gapless *free abelian matrix model*, not a theorem about every
commutative algebra or every abelian gauge theory. The free-field comparison
and compact abelian exceptions are treated in §5. The
temporal-gauge constant modes of a gauge theory in $d$ spacetime dimensions
are $D=d-1$ spatial components, so the zero-point mechanism needs $d\ge3$;
for $d=2$ the single matrix has no partner, in agreement with §5,
where two-dimensional Yang--Mills has no local excitations at all and its
discrete flux spectrum comes from the compact holonomy, a different
mechanism.

### 3.3 Conditional orbit-area bounds and state counting

For the same classical scalar Hamiltonian, freeze $x\ne0$ and let
$E_y=p_y^2/(2m)+m\omega_x^2y^2/2$, $\omega_x=g|x|/\sqrt m$.
The transverse oscillator ellipse has area

$$J_y=\oint p_y\,dy=\frac{2\pi E_y}{\omega_x}
 =\frac{2\pi\sqrt m E_y}{g|x|}.$$

Indeed its semiaxes are $\sqrt{2mE_y}$ and
$\sqrt{2E_y/(m\omega_x^2)}$. The frozen-oscillator identity is exact;
adiabatic conservation along a valley is only a leading-order reading when
$|\dot x/x|\ll\omega_x$, or $|x|\gg x_{\rm ad}(E)=(2E)^{1/4}g^{-1/2}$.
The original Landau--Lifshitz §49 comparison was metadata only; the bound
below requires no adiabatic approximation.

**Conditional sublevel bound (former G08 Theorem 2).** Supply an arbitrary
action coefficient $a_0>0$ and name the restriction $\mathsf F(a_0)$ on instantaneous admitted states by
$J_y\ge\pi a_0$ when $x\ne0$ and $J_x\ge\pi a_0$ when $y\ne0$.
Then

$$E_y\ge\frac{a_0g|x|}{2\sqrt m},\qquad
 |x|,|y|\le\frac{2\sqrt m E}{a_0g}.$$

This follows directly from the ellipse formula and $E_y\le E$; interchange
$x,y$ for the other bound. Momenta also satisfy $|p|\le\sqrt{2mE}$, so the
restricted sublevel set is bounded. Without the restriction,
$y=p_y=0$, $x(t)=x_0+p_xt/m$ escapes at any positive kinetic energy.
At $a_0=\hbar$, the numerical lower bound is the oscillator inequality
in Theorem 5. Its quantum proof, however, uses a Hilbert space, derivatives,
normalization and the canonical momentum operator, all additional structure.

The classical restriction alone has no discrete spectrum and need not be
invariant under the full coupled dynamics. It does not even force a positive
infimum of the instantaneous admitted energies: at $x=y=r>0$ choose
$p_x^2=p_y^2=a_0g\sqrt m\,r$. Both area bounds hold while
$H=a_0gr/\sqrt m+g^2r^4/2\to0$ as $r\downarrow0$. Thus the former claim
that a classical area floor itself proves a spectral gap is withdrawn.
A dynamical, invariant trajectory class would require a separate argument.

For the following count set $a_0=\hbar$ solely to compare with Theorem 5,
and define ${E_*} =\hbar^{4/3}g^{2/3}m^{-2/3}$ and
$X(E)=2\sqrt mE/(\hbar g)$. This comparison does not derive physical $\hbar$.

**Floor-admitted phase-space volume.**  Without the floor the phase-space
volume $|\{H_{\rm cl}\le E\}|$ is infinite for every $E>0$ (Simon, Ann. Phys. 146 (1983) 209--220, p. 210, passage
read). With the floor it is finite, and it can be computed with both
valleys included. Write $R=\sqrt{2E}/g$, so that the potential is
below $E$ exactly where $|xy|\le R$; the momenta at $(x,y)$ fill a disc
of area $2\pi m(E-\tfrac{g^2}{2}x^2y^2)$. By the conditional sublevel bound every admitted
state lies in the box $|x|,|y|\le X(E)$. For $X(E)^2\ge R$, that is
$E\ge{E_*}/2$, the box carries the volume
$$P(E)=\iint_{|x|,|y|\le X}2\pi m\Big(E-\frac{g^2}{2}x^2y^2\Big)_+dx\,dy
=8\pi m\,ER\Big[\frac89+\frac23\ln\frac{X^2}{R}\Big]:$$
in each quadrant the strip $0\le x\le R/X$, where the $y$-integral of
$E-\tfrac{g^2}2x^2y^2$ runs to $X$, contributes $\tfrac89ER$, and the
region $R/X\le x\le X$, where it runs to $R/x$ and equals
$\tfrac23ER/x$, contributes $\tfrac23ER\ln(X^2/R)$. Inside the box the
floor removes, at each $(x,p_x)$ with $x\ne0$, the ellipse
$E_y<\hbar\omega_x/2$ of area $\pi\hbar$ in the $(y,p_y)$ plane
(the area identity above), and at each $(y,p_y)$ with $y\ne0$ the ellipse
$E_x<\hbar\omega_y/2$ of the same area. The admitted volume
$V(E)=|\{H_{\rm cl}\le E\}\cap\mathsf F(\hbar)|$ therefore obeys
$0\le P-V\le2\cdot\pi\hbar\cdot2X\cdot2\sqrt{2mE}=16\sqrt2\,\pi mE^{3/2}/g$.
With $ER=\sqrt2E^{3/2}/g$ and $X^2/R=2\sqrt2\,(E/{E_*})^{3/2}$,
$$V(E)=\frac{8\sqrt2\,\pi m}{g}\,E^{3/2}\Big[\ln\frac E{E_*}+\theta(E)\Big],
\qquad\ln2-\frac{10}9\le\theta(E)\le\ln2+\frac89 .$$
Since $\sqrt R=x_{\rm ad}(E)$, the hyperbola $|xy|=R$ crosses the
diagonal at the adiabatic scale defined above. To leading order $V$ is
twice the one-valley integral of $(8\pi/3)\sqrt2\,mE^{3/2}/(g|x|)$,
the transverse ellipse area $2\pi(E-p_x^2/2m)/\omega_x$ integrated over
$|p_x|\le\sqrt{2mE}$, over $x_{\rm ad}(E)\le|x|\le X(E)$. A floor $\kappa h_P$ with any
$\kappa>0$ in place of $h_P/2$ replaces $X$ by $X/(2\kappa)$, leaves the
bound on $P-V$ unchanged (the excluded ellipses grow by $2\kappa$ as the
box shrinks by $1/(2\kappa)$) and shifts both bounds on $\theta$ by
$-\tfrac43\ln(2\kappa)$, so the coefficient of $E^{3/2}\ln E$ is
independent of the floor value.

*Comparison with the exact count.* For the operator
$-\Delta+|xy|^\alpha$, Simon proves the limit
$E^{-1-1/\alpha}(\ln E)^{-1}N(E)\to\pi^{-1}$ (J. Funct. Anal. 53
(1983) 84--98, Theorem 1.4 and the display after Theorem 1.5,
pp. 85--86, passage read). At $\alpha=2$ this is
$N(E)\simeq\pi^{-1}E^{3/2}\ln E$, the growth also stated in Ann. Phys.
146, p. 212, end of Section 2. The dilation $x\mapsto\ell x$ with
$\ell^6=\hbar^2/(mg^2)$ carries
$H=-\frac{\hbar^2}{2m}\Delta+\frac{g^2}{2}x^2y^2$ to
$\frac{E_*}2(-\Delta+x^2y^2)$, because both coefficients become
$\hbar^2/(2m\ell^2)=g^2\ell^4/2={E_*}/2$. Hence
$N_H(E)\simeq(2\sqrt2/\pi)(E/{E_*})^{3/2}\ln(E/{E_*})$, while
the floor count gives
$V(E)/h_P^2=(2\sqrt2/\pi)(E/{E_*})^{3/2}[\ln(E/{E_*})+\theta(E)]$.
The leading terms agree, constant included. The identification
$N\approx V/h_P^2$ is the Weyl heuristic, and the agreement is a comparison
of two computed leading terms; Simon's proof runs through a
Feynman--Kac lower bound and sliced-bread upper bounds. The leading coefficient is independent of the chosen positive floor
multiple. Agreement therefore cannot select its value or establish a
classical area restriction as the physical origin of the quantum count. Simon
(p. 86) calls a general geometric interpretation of the constant
$\pi^{-1}$ an open question; no search was run for later literature
that supplies one, and no novelty is claimed.

**Semiclassical channel levels.** With $J_y=(n+\tfrac12)h_P$ conserved, the valley
motion has effective Hamiltonian $p_x^2/2m+\kappa_n|x|$,
$\kappa_n=(n+\tfrac12)\hbar g/\sqrt m$, and Bohr--Sommerfeld
quantization $\oint p_x\,dx=(N+\tfrac12)h_P$ with
$\oint p_x\,dx=\tfrac{8\sqrt{2m}}{3}E^{3/2}/\kappa_n$ gives
$$E^{\rm BS}_{n,N}={E_*}\Big[\frac{3\pi(2n+1)(2N+1)}{16\sqrt2}\Big]^{2/3},
\qquad{E_*}=\hbar^{4/3}g^{2/3}m^{-2/3}.$$
The unit ${E_*}$ is the exact one of Theorem 5(4); the pure numbers are semiclassical estimates
of $e_n$ and are labelled as such. The estimate describes one channel,
the $x$-axis with its two half-valleys. The $y$-axis gives the same
levels, so counting both channels doubles every level, and the
coupling of the channels and of different $n$ near the origin, where
the adiabatic reading fails, is ignored. The quantization rules add a discrete set of positive approximate
channel levels. They are extra assumptions; they are not a spectral
consequence of the classical area restriction.
The splitting of the doublets and the simplicity of the ground state,
which the Jaffe--Witten conditions need, come from Theorem 5(3).
As a consistency check, each channel and each $n$ contribute
$\frac{4\sqrt2}{3\pi}(E/{E_*})^{3/2}/(n+\tfrac12)$ levels below $E$;
summed over both channels and over $n$ up to the adiabatic limit
$n_*\simeq2^{-1/4}(E/{E_*})^{3/4}$, where the turning point
$E/\kappa_n$ reaches $x_{\rm ad}(E)$, they give
$(2\sqrt2/\pi)(E/{E_*})^{3/2}\ln(E/{E_*})$ to leading order,
the same leading term as the volume count.

For $SU(2)$, each of the two frozen transverse oscillator directions
can instead be assigned area at least $\pi a_0$. Their sum gives
$E_\perp\ge a_0g|\vec x_i|/\sqrt m$ and the corresponding classical
sublevel bound $|\vec x_i|\le\sqrt m E/(a_0g)$. The quantum counterpart
is Theorem 6(1); imposing a classical restriction does not reproduce its
operator domain or state space. For an abelian matrix model, or $D=1$,
there is no transverse restoring oscillator: this restriction supplies no
valley confinement, and the quantum model is free.

### 3.4 Torus truncation and the uniformity problem

**Proposition 7.** For SU(2) Yang--Mills on a spatial torus of side $L$
with action $S=-\frac{\hbar}{4g^2}\int F^a_{\mu\nu}F^{a\mu\nu}\,d^3x\,c\,dt$
($g$ dimensionless, $[A]=$ length$^{-1}$), temporal gauge and the
constant-mode ansatz $A^a_i(x,t)=a^a_i(t)$, the Hamiltonian is
$$H_0=\frac{g^2c}{2\hbar L^3}\sum_{i=1}^3|\vec p_i|^2
+\frac{\hbar cL^3}{2g^2}\sum_{i<j}|\vec a_i\times\vec a_j|^2,\qquad
[a^a_i,p^b_j]=i\hbar\delta_{ij}\delta^{ab},$$
which is Theorem 6 with $D=3$, $m=\hbar L^3/(g^2c)$ and
$g_B^2=\hbar cL^3/g^2$. Its energy unit is
$${E_*}=\hbar^{4/3}g_B^{2/3}m^{-2/3}=\frac{g^{2/3}\,\hbar c}{L},$$
so the unrestricted zero-mode gap is $\delta_1^{(3)}g^{2/3}\hbar c/L$.
On the Gauss-invariant sector write instead
$\Delta_{0,\rm inv}(L)=\delta_{\rm inv}^{(3)}g^{2/3}\hbar c/L$,
where $\delta_{\rm inv}^{(3)}\ge\delta_1^{(3)}>0$; equality is not asserted.
Both truncation gaps decay as $1/L$ at fixed coupling.

*Proof.* With $F^a_{0i}=c^{-1}\dot a^a_i$ and $F^a_{ij}=(\vec a_i\times\vec
a_j)^a$ the Lagrangian is $\frac{\hbar L^3}{2g^2c}\sum|\dot{\vec a}_i|^2
-\frac{\hbar cL^3}{4g^2}\sum_{i,j}|\vec a_i\times\vec a_j|^2$; the Legendre
transform and $\tfrac14\sum_{i,j}=\tfrac12\sum_{i<j}$ give $H_0$, and the
exponent bookkeeping is $\hbar^{4/3+1/3-2/3}c^{1/3+2/3}L^{1-2}g^{-2/3+4/3}$.
$\square$

Lüscher's small-volume expansion (Nucl. Phys. B219 (1983) 233; abstract)
states that the torus spectrum is discrete and expands in powers of
$g^{2/3}$ with $g$ the renormalized coupling; Proposition 7 is the leading constant-mode model used in that
approximation, not a uniform error theorem for the full field Hamiltonian, and Lüscher--Münster (Nucl. Phys. B232 (1984) 445; abstract) carry
it to one loop for SU(2) and locate the crossover to large-volume behaviour
near $z=M(0^+)L\simeq2$. Jaffe and Witten write (p. 7 of the local PDF) that
"no present ideas point the direction to establish the existence of a mass
gap that is uniform in the volume". Proposition 7 shows the difficulty in
the solved sector: $\Delta_0(L)>0$ for every $L$ with
$\inf_L\Delta_0(L)=0$. Uniformity would need $g(L)^{2/3}/L$ bounded below,
outside the weak-coupling regime where the truncation is justified; the
compensation must come from the crossover regime, where the expansion no
longer applies. In the language of the dimensional theorem cited in §1, $L$ is a fixed apparatus
length that enters the monomial and makes the finite-volume floor
non-universal, and the uniformity requirement is exactly the demand that
the floor be independent of it.

The supersymmetric contrast identifies the mechanism once more: de Wit,
Lüscher and Nicolai (Nucl. Phys. B320 (1989) 135; abstract) prove that the
supersymmetric matrix-model Hamiltonians have continuous spectrum starting
at zero, through low-energy states along the same abelian valleys. The
fermionic zero-point energy cancels the bosonic $\hbar\omega/2$ per
transverse mode, so the confining term of Theorem 5 vanishes. The uncancelled bosonic transverse energy is the confinement mechanism
in Theorems 5--6. Its cancellation removes this argument in the cited
supersymmetric models.

The [Feshbach treatment](weak-coupling-feshbach-reduction.md) states the
separate complement, Schur and effective-gap estimates needed to transport
this truncation into a renormalized field theorem. The
[three-dimensional scaling problem](three-dimensional-gap-one-function.md)
uses $D=2$, with its own physical construction and order of limits.

## 4. Gap-to-action units and the field dimension

**Gap-to-action unit (C132a; former G08 Proposition 4).** Let the classical model with fixed constants $m$, $g$
(dimension vectors $d_m=(1,0,0)$, $d_g=(\tfrac12,-1,-1)$) be enlarged by
any fixed constants, and suppose the enlarged theory has a positive finite
gap $\Delta$ depending on the fixed constants only. Then the theory has
the action unit
$$A=\Delta^{3/4}\,m^{1/2}\,g^{-1/2},$$
and conversely an action unit $A$ gives the energy unit
$A^{4/3}g^{2/3}m^{-2/3}$.

*Proof.* Energy has dimension vector $(1,2,-2)$ and action $(1,2,-1)$. The
system $a\,d_m+b\,d_g+c\,(1,2,-2)=(1,2,-1)$ has the unique solution
$a=\tfrac12$, $b=-\tfrac12$, $c=\tfrac34$: the length and time components
give $-b+2c=2$, $-b-2c=-1$, hence $c=\tfrac34$, $b=-\tfrac12$, and the mass
component gives $a=\tfrac12$. So $m^{1/2}g^{-1/2}\Delta^{3/4}$ has action
dimension whatever the extra constants are. The converse energy monomial follows from Theorem 3 with $k=4$,
but dimensional permission does not establish any spectrum or positive gap. $\square$

A supplied positive finite gap gives this action unit, and a supplied action
unit gives an energy unit. These are equivalent *unit constructions*.
Theorem 5 supplies the additional spectral content
$\Delta=\delta_1{E_*}$, $0<\delta_1<\infty$, for the quantized model.

**Field dimension (C132b; Proposition 10 and former G08 Proposition 5).** Write the Euclidean Yang--Mills action with the gauge field
as a connection, $D=\partial+A$, $[A]={\rm length}^{-1}$, $x_0=ct$:
$$S_E=\frac1{4g_{\rm cl}^2}\int F^a_{\mu\nu}F^a_{\mu\nu}\,d^dx,\qquad
[1/g_{\rm cl}^2]={\rm action}\cdot{\rm length}^{4-d}.$$
The weight $e^{-S_E/\hbar}$ depends on the coupling through
$\lambda_d=\hbar g_{\rm cl}^2$, of dimension length$^{d-4}$; in $d=4$ the
repository writes $g^2=\hbar g_{\rm cl}^2$, a pure number (the trace-normalized action has the same dimension).
With the speed $c$ and a gap $\Delta$:

1. In $d=2$ and $d=3$ the pair $(1/g_{\rm cl}^2,c)$ contains neither an
   action unit nor an energy unit. Adjoining $\Delta$ gives exactly one
   action unit, adjoining $\hbar$ gives exactly one energy unit, and the
   same gap/action unit construction holds, without a positivity theorem.
2. In $d=4$, $1/g_{\rm cl}^2$ is itself an action unit. The constants
   $(1/g_{\rm cl}^2,c,\Delta)$ are dimensionally independent and their
   only action monomial is $1/g_{\rm cl}^2$, with $\Delta$ at exponent
   zero. The constants $(1/g_{\rm cl}^2,c,\hbar)$ contain no energy,
   length or time unit. So "gap $\Rightarrow$ action unit" holds
   trivially and "action unit $\Rightarrow$ gap" fails.

| $d$ | classical constants (with $c$ for Yang--Mills) | action unit with $\Delta$ adjoined | energy unit with $\hbar$ adjoined |
| --- | --- | --- | --- |
| 2 | $1/g_{\rm cl}^2\sim(1,4,-1)$ | $(1/g_{\rm cl}^2)^{1/3}c^{-2/3}\Delta^{2/3}$ | $\hbar^{3/2}g_{\rm cl}\,c=\hbar c\,\lambda_2^{1/2}$ |
| 3 | $1/g_{\rm cl}^2\sim(1,3,-1)$ | $(1/g_{\rm cl}^2)^{1/2}c^{-1/2}\Delta^{1/2}$ | $\hbar^2g_{\rm cl}^2\,c=\hbar c\,\lambda_3$ |
| 4 | $1/g_{\rm cl}^2\sim(1,2,-1)$, an action | $1/g_{\rm cl}^2$ itself; $\Delta$ enters with exponent $0$ | none: $\hbar g_{\rm cl}^2=g^2$ is a pure number |
| mechanics, $k=-2$ | $m$, $\lambda\sim(1,4,-2)$ | $\sqrt{m\lambda}$ already classical; $\Delta$ adds nothing | none: $2m\lambda/\hbar^2$ is a pure number |

*Proof.* Dimension vectors are over (mass, length, time); action is
$(1,2,-1)$, energy $(1,2,-2)$, $c\sim(0,1,-1)$. Solve
$a\,d_{1/g_{\rm cl}^2}+b\,d_c+c'\,(1,2,-2)=(1,2,-1)$. For $d=3$, adding the
length and time equations gives $2a=1$, then $c'=\tfrac12$, $b=-\tfrac12$;
for $d=2$ the sum gives $3a=1$, then $c'=\tfrac23$, $b=-\tfrac23$; for $d=4$
it gives $a=1$, then the mass equation gives $c'=0$ and the length equation
$b=0$. The determinants of the three dimension vectors are $-3$, $-2$, $-1$
for $d=2,3,4$, so each solution is unique. With $\hbar\sim(1,2,-1)$ in place
of $\Delta$ the determinants are $-2$ and $-1$ for $d=2,3$, and the displayed
energy monomials have vector $(1,2,-2)$ by direct addition. In $d=2,3$ the
pair $(1/g_{\rm cl}^2,c)$ alone fails: the mass and length equations fix
$a=1$ and $b=-2$ (respectively $b=-1$), and the time component is then $1$
(respectively $0$), never $-1$ or $-2$. In $d=4$, $1/g_{\rm cl}^2$ and
$\hbar$ have the same vector, so the span is that of $(1,2,-1)$ and
$(0,1,-1)$; $a(1,2,-1)+b(0,1,-1)=(1,2,-2)$ forces $a=1$ (mass), $b=0$
(length) and then $-1=-2$ (time), and the targets $(0,1,0)$ and $(0,0,1)$
fail at the time component in the same way. The $k=-2$ row is §6 below. $\square$

In $d=2,3$ the quantum theory in infinite volume has the constants
$(\hbar,c,\lambda_d)$, which are independent, so a gap that depends on them
alone is $\Delta=\kappa\,\hbar c\,\lambda_d^{1/(4-d)}$ with a pure number
$\kappa$ (the dimensional theorem cited in §1). The action unit of the table is then
$\kappa^{2/3}\hbar$ in $d=2$ and $\kappa^{1/2}\hbar$ in $d=3$: the gap returns
$\hbar$ up to a pure number.

Two facts fix the reading of the table. First, the overall factor
$1/g_{\rm cl}^2$ drops out of the classical field equations
$D_\mu F_{\mu\nu}=0$ in every dimension (the field normalization above), and the
dilation $A\mapsto sA(sx)$ maps solutions to solutions in every $d$ while
multiplying the action by $s^{4-d}$. The classical field equations are therefore dilation covariant in every
dimension; they supply no chosen solution length. The normalization
$1/g_{\rm cl}^2$ still converts solution geometry into action and energy. The difference between the
rows becomes physical through the quantum weight $e^{-S_E/\hbar}$, whose
coefficient $1/\lambda_d=1/(\hbar g_{\rm cl}^2)$ has dimension
length$^{4-d}$. In $d=2,3$ the weight carries a length and, with $c$, an
energy, and a gap is a pure number times that energy. In $d=4$ the weight
carries the pure number $1/g^2$ and no length. Second, $d=4$ is
action-critical in the sense of §6, and shares its row type with
the inverse-square potential: the classical constants own an action unit
and no energy unit. This is the dimensional reason the four-dimensional
problem is one-directional. A gap needs a length that the constants of the
weight do not contain; dimensional transmutation generates it from the
regulator (the field normalization above), and the unique action monomial formed using the classical coupling,
$c$ and that gap still equals the $1/g_{\rm cl}^2=\hbar/g^2$ already present. Along the continuum
trajectory of asymptotic freedom $g^2(a)\to0$, so this bare action unit grows
without bound in units of $\hbar$; the continuum theory keeps $\hbar$, $c$
and the transmuted scale, the dimensionless coupling having been traded for
that scale. The same normalization distinction applies to C132a: the trajectories of
$H_{\rm cl}$ depend on $g^2/m$ alone and $m$ normalizes the action, while an actual spectral gap additionally depends on the specified
quantization; the unit conversion itself does not.

## 5. Free fields, compact groups and the exact circle theory

 Let $H$
be the second quantization on Fock space of a one-particle operator
$\hbar\Omega$ with $\Omega\ge0$ the classical frequency operator. Then
$\operatorname{spec}(H)\setminus\{0\}$ has infimum
$\hbar\inf(\operatorname{spec}\Omega\setminus\{0\})$. In particular a free
quantum field has a gap if and only if its classical dispersion relation
has one.

*Proof.* On the $n$-particle sector $H$ acts as $\hbar\sum_{j\le n}\Omega_j$;
its spectrum is the closure of $n$-fold sums of spectral values of
$\hbar\Omega$, and the one-particle sector attains the infimum. $\square$

**Corollary 9 (Maxwell).** In a periodic box of side $L$, Coulomb gauge and
two transverse polarizations give $H=\sum_{k\ne0,\sigma}\hbar c|k|\,
n_{k\sigma}$ after normal ordering, $k\in(2\pi/L)\mathbb Z^3$: the gap is
$2\pi\hbar c/L$ and tends to zero as $L\to\infty$, where the spectrum is
$[0,\infty)$. A scale-covariant classical dispersion $\omega(sk)=s\omega(k)$
has infimum zero in infinite volume; a mass term gives
$\omega=\sqrt{c^2k^2+\mu^2c^4/\hbar^2}$ and the supplied gap $\mu c^2$, and
gauge invariance excludes the Maxwell mass term $A_\mu A^\mu$. The constant
modes are free ($k=0$, spectrum $[0,\infty)$ already at finite $L$) in the
non-compact theory; in compact $U(1)$ they live on a torus and contribute
energies proportional to $\hbar c/L$ as well. Free quantization therefore
generates no scale: this free compact finite-volume gap is $\hbar c/L$ times a
number.

**Compact abelian theories.** Compactness admits topological sectors
absent from noncompact free Maxwell theory. Osterwalder--Seiler's compact-group
strong-coupling construction, Polyakov's three-dimensional monopole mechanism,
Göpfert--Mack's all-coupling Villain gap, and the four-dimensional weak-coupling
Coulomb phase have different operators and limiting assumptions. Read levels
and precise references remain in [B78](../references/batches/B78.md).
The [Villain treatment](villain-monopole-refinement.md) retains the normalized
measure bounds and distinguishes the fixed-physical-coupling massless limit
from Göpfert--Mack's massive Gaussian scaling. A gapped lattice theory can
therefore have a massless continuum limit. The former Debye formula with a
dimensionless $\beta$ times $a^{-3}$ was not dimensionally a mass-squared
formula and is withdrawn in this normalization; use the canonical trajectory
and correlation bounds instead of that unchecked prefactor.

### The exact two-dimensional holonomy spectrum

**Proposition 11.** Pure Yang--Mills on a spatial circle of circumference
$L$, in temporal gauge with Gauss's law imposed, has as its only
gauge-invariant degree of freedom the holonomy $U\in G$ up to conjugation.
The physical Hilbert space is $L^2(G)^G$, the class functions, and with
$S=\frac1{2g_{\rm cl}^2}\int\operatorname{tr}F^2$ the Hamiltonian is
$H=\frac{g_{\rm cl}^2\hbar^2cL}{2}\,C$, where $C$ is the quadratic Casimir acting on
class functions. By Peter--Weyl the eigenfunctions are the characters
$\chi_R$ and
$$E_R=\frac{g_{\rm cl}^2\hbar^2cL}{2}\,C_2(R),\qquad
E_{\rm trivial}=0,\qquad
\text{gap}=\frac{g_{\rm cl}^2\hbar^2cL}{2}\,C_2(R_{\min})>0 ;$$
for $SU(N)$ with $\operatorname{tr}T^aT^b=\tfrac12\delta^{ab}$,
$C_2(\text{fund})=(N^2-1)/(2N)$, and for $U(1)$, $E_n=\frac{e^2\hbar^2cL}{2}n^2$
with $n\in\mathbb Z$ from compactness.

*Proof.* Gauss's law $D_xE=0$ makes the electric field covariantly
constant along the circle, so on class functions of the holonomy $E$ acts
as the left-invariant derivative and $\int_0^L\operatorname{tr}E^2\,dx$ as
$L$ times the Laplacian on the group; $H=\frac{g_{\rm cl}^2}{2}\int\operatorname{tr}E^2$
follows from $E=\dot A/g_{\rm cl}^2$, and restoring $\hbar,c$ uses $[g_{\rm cl}^2\hbar]=L^{-2}$
from §4. Characters diagonalize the Laplacian on class
functions with eigenvalue the Casimir. $\square$

The states are electric flux lines wrapping the circle, $E_R/L$ is a string
tension, and there are no propagating excitations: the theory has no local
degrees of freedom. The gap grows linearly with $L$ and diverges as
$L\to\infty$, so the Jaffe--Witten finiteness requirement $m<\infty$ fails
in infinite volume, where the finite-energy Hilbert space is the vacuum
alone. Abelian and non-abelian groups behave identically here; the
commutator plays no role in $d=2$ because there are no transverse spatial
directions, in agreement with $D=1$ in Theorem 6. Exact solvability on the
Euclidean side is Migdal's and Witten's (Commun. Math. Phys. 141 (1991)
153); rigorous constructions of the two-dimensional Yang--Mills measure are
Driver's, Gross--King--Sengupta's and Lévy's (B78).

## 6. Singular quantum mechanics: a scale is not a completion theorem

**Proposition 12 (two-dimensional delta potential).** For
$H=-\frac{\hbar^2}{2m}\Delta-\lambda\delta^2(\vec r)$ on $\mathbb R^2$,
$m\lambda/\hbar^2$ is dimensionless and the classical problem has no
energy scale. With a momentum cutoff $\hbar\Lambda$ the bound-state
condition is
$$1=\frac{m\lambda}{2\pi\hbar^2}\ln\Big(1+\frac{\hbar^2\Lambda^2}{2m|E_B|}\Big),
\qquad
|E_B|=\frac{\hbar^2\Lambda^2}{2m}\Big(e^{2\pi\hbar^2/(m\lambda)}-1\Big)^{-1}.$$
Removing the cutoff with $\lambda(\Lambda)$ chosen to keep $E_B$ fixed
defines the theory by the scale $E_B$ alone. The spectrum is
$\{E_B\}\cup[0,\infty)$.

*Proof.* In momentum space
$\tilde\psi(p)=\lambda\psi(0)/(p^2/2m+|E_B|)$, and
$\psi(0)=\int_{|p|<\hbar\Lambda}\tilde\psi\,d^2p/(2\pi\hbar)^2$ gives
$1=\frac{\lambda}{(2\pi\hbar)^2}\cdot2\pi\int_0^{\hbar\Lambda}
\frac{p\,dp}{p^2/2m+|E_B|}=\frac{m\lambda}{2\pi\hbar^2}\ln(1+\hbar^2\Lambda^2/2m|E_B|)$.
$\square$

This chosen nontrivial point interaction has an isolated bound state and
excitation threshold $|E_B|$ after shifting the ground energy to zero. Its
continuum is the escaping one-particle continuum, not a reconstructed field
spectrum. Specifying a nontrivial renormalized interaction supplies $E_B$;
well-defined quantum dynamics also permits the scale-free free operator.
Thus this example shows transmutation *within a selected interaction class*,
not that every consistent completion must introduce a scale.

**Proposition 13 (inverse-square domain and stability distinction).** In the
$s$ wave of $-\hbar^2\Delta/(2m)-\lambda/r^2$, put
$\gamma=2m\lambda/\hbar^2>0$. The reduced expression is
$-(\hbar^2/(2m))(u''+\gamma u/r^2)$ on $L^2(0,\infty)$.
For $0<\gamma\le1/4$, Hardy's inequality gives a nonnegative Friedrichs
extension with spectrum $[0,\infty)$ and no bound state. This names the
extension: non-essential self-adjointness does not by itself force a new
scale or the same spectrum for every boundary condition.

For $\gamma>1/4$, write $\nu=\sqrt{\gamma-1/4}$. The local indices are
$1/2\pm i\nu$, so a self-adjoint origin condition fixes their relative phase,
equivalently a length modulo discrete rescaling. The negative eigenvalues
form a two-sided geometric tower

$$E_n=-{E_*}^{\rm ext}\exp(-2\pi n/\nu),\qquad n\in\mathbb Z,
\qquad {E_*}^{\rm ext}>0.$$

They accumulate at zero as $n\to+\infty$ and are unbounded below as
$n\to-\infty$. There is no ground state or stable positive excitation gap
in this unregularized supercritical model. Keeping only the tower toward zero
would silently discard half the extension's spectrum. A short-distance
regularization that stabilizes it is an additional model.

The indices follow from $u=r^s$, $s(s-1)+\gamma=0$. The domain and full
tower statements are checked in
[Dereziński--Richard](https://arxiv.org/pdf/1604.03340), §§2.2--2.3 and
Theorem 5.5 (passages re-read during consolidation), already used for the
[singular-domain comparison](self-sufficiency-contrast.md). In the subcritical
range scale-preserving self-adjoint choices exist; at supercritical coupling
self-adjointness does not restore semiboundedness. The earlier inference
“well-defined dynamics forces a stable scale” is therefore withdrawn.

Classically $m\lambda$ has action-squared units and fall to the centre occurs
below angular momentum $\sqrt{2m\lambda}$. This action-critical dimensional
comparison with relativistic Coulomb thresholds survives; its domains,
quantum dynamics and admissibility premises are different. The remaining
Thorn, Camblong, Case and Essin--Griffiths leads retain B78's metadata-level
qualification and are not substituted for the domain theorem just read.

## 7. Consequence for STATE

The matrix gap is proved **after** quantum state/operator structure and
physical $\hbar$ are supplied. The classical orbit-area restriction gives a
bounded sublevel region and the displayed leading volume count; its Weyl
comparison and Bohr--Sommerfeld rules do not turn it into a classical derivation
of quantum spectral discreteness. The continuum problem adds control of the
nonzero modes, volume/cutoff limits and physical spectral weight. The exact
circle spectrum has global electric flux and no propagating local excitations.
These different mechanisms cannot be combined into a universal implication
“positive action implies mass gap”.

For comparison, constant-force motions at fixed $m,F$ admit
$x\mapsto sx$, $t\mapsto s^{1/2}t$, $v\mapsto s^{1/2}v$. Their Galileo
comparison $F^2\tau^3/(2m)$ scales by $s^{3/2}$ and area
$vF\tau^3/(6m)$ by $s^2$, giving zero infima when all such alternatives are
admitted. A supplied length gives $\sqrt{mF\ell_0^3}$; a supplied speed gives
$m^2c^3/F$; fixed charge and speed give $k_e/c$. Units do not by themselves
bound these observables. The [action-selection treatment](action-unit-dimensional-selection.md)
and [Newton insertion proof](newton-insertion-action.md) own those classical
arguments.

The former “similarity anomaly” route remains a question: can an independently
specified physical composition law exclude every zero-action completion?
Associativity, positivity and definability alone have supplied no such theorem;
scale-free formulation does not by itself establish similarity covariance.
Classical chords and zero/nonzero Gaussian families already compose. The
singular examples in §6 illustrate boundary choices and possible instability,
not a derivation of physical $\hbar$ from consistency.

Sources for the matrix theorem are Simon (Ann. Phys. **146** (1983) 209--220,
pp. 210--212, passage) and his counting theorem (J. Funct. Anal. **53** (1983)
84--98, pp. 85--86, passage). The finite-volume Lüscher/Lüscher--Münster and
supersymmetric de Wit--Lüscher--Nicolai comparisons were abstract-level reads;
Reed--Simon theorem numbers were corroborated through citing passages rather
than a full book audit. [B78](../references/batches/B78.md) and
[B79](../references/batches/B79.md) preserve those source boundaries. No new
research, independent review or priority claim follows from this consolidation.
