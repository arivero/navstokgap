# A gap is a scale the classical theory lacks: solved low-dimensional mass gaps and the positive-action question

The Yang--Mills mass gap and this programme's positive action floor are the
same kind of statement: the infimum of an observable over nontrivial states
is a positive finite multiple of a unit formed from the theory's fixed
constants, and it is zero or infinite whenever those constants admit no such
unit. Classical Yang--Mills in four dimensions carries no constant at all in
its field equations, and classical mechanics with a mass and a force carries
no action unit, so both classical floors are zero; the classical scale
covariance that realizes zero is the same similarity in both cases. Every
low-dimensional mass gap that can be solved in writing then falls into two
classes. A *supplied* gap is proportional to a constant written into the
definition: the box gap $2\pi\hbar c/L$ of a free field, the strong-coupling
lattice gap in units of $1/a$, a mass term, the string tension $g^2L$ of
two-dimensional Yang--Mills on a circle, and the repository's own Ising and
cluster gaps $Ka[1-\tanh 2b]$ and $J$. A *generated* gap arises from the
interplay of two structures that are each scale-free: in Yang--Mills quantum
mechanics the commutator potential and the canonical commutator produce
$\Delta=\delta_1\,\hbar^{4/3}g^{2/3}m^{-2/3}$, which vanishes if either
$\hbar$ or $g$ is removed, and this is the exact form of "commutative fields
have no gap" in zero space dimensions; in scale-invariant quantum mechanics a
scale is forced by the consistency requirement of defining the dynamics at
all. The dictionary in Section 7 records what this decides for the necessity
theorem sought in STATE item 1: the mass-gap problem takes the
non-commutative structure as given and asks for the scale, so the analogy
governs the second stage of the positive-action question and identifies the
consistency-forced scale as the only mechanism in the mass-gap story that
does not assume the structure it explains. This is G07, an exploratory
consolidation with written proofs; it promotes no ledger claim.

## 1. Two floors and one dimensional theorem

**The mass gap.** Jaffe and Witten require a self-adjoint $H\ge0$ with
$H\Omega=0$, $\operatorname{spec}(H)\cap(0,\Delta)=\varnothing$ for some
$\Delta>0$, and a finite supremum $m$ of such $\Delta$
([definitions](millennium-problem-definitions.md)). For a purely discrete
spectrum $E_0<E_1<\cdots$ the supremum is attained and equals $E_1-E_0$.

**The action floor.** [Q14](action-unit-dimensional-selection.md) defines,
for a model with fixed constants $c$, the attained set $\mathcal A(c)$ of an
action observable over admitted masses, preparations and solutions, and the
floor $g(c)=\inf\{A\in\mathcal A(c):A>0\}$. The programme's target is
$g(c)>0$ for the Galileo comparison, whose observable is
$\tau\Delta E=(3F/v)A_{\rm inertial,fall}=F^2\tau^3/(2m)$
([N01](newton-insertion-action.md) §1).

**Theorem 1 (floors are unit multiples).** Let a theory be specified by
fixed constants $c_1,\dots,c_r$ with dimension vectors $d_i\in\mathbb R^3$
over mass, length and time, and let $X$ be an observable with dimension
vector $d_X$ whose attained set $\mathcal X(c)\subset[0,\infty]$ is defined by
dimensionally homogeneous relations and whose floor
$\gamma(c)=\inf(\mathcal X(c)\cap(0,\infty))$ depends on the fixed constants
only. Then $\gamma(c)\in\{0,\infty\}$ for every $c$ when $d_X$ lies outside
the span of $d_1,\dots,d_r$, and $\gamma(c)=\Pi(c)F(\pi_1,\dots,\pi_s)$ with
$\Pi$ a monomial of dimension $d_X$ and $\pi_j$ the independent dimensionless
combinations otherwise.

*Proof.* This is Q14's Theorem A with $d_A$ replaced by $d_X$, and the proof
is the same three lines. A change of units $\lambda\in(0,\infty)^3$ carries
the model at $c$ to the model at $\lambda^{d_i}c_i$ and multiplies every
attained value by $\lambda^{d_X}$, so
$\gamma(\lambda^{d_1}c_1,\dots)=\lambda^{d_X}\gamma(c)$. If $d_X$ is outside
the span, choose $\lambda$ with $\lambda^{d_i}=1$ for all $i$ and
$\lambda^{d_X}\neq1$: then $\gamma(c)=\lambda^{d_X}\gamma(c)$, which forces
$\gamma(c)\in\{0,\infty\}$. If $d_X=\sum a_id_i$, then $\gamma/\Pi$ is
invariant under all unit changes and is therefore a function of the
dimensionless combinations. $\square$

**Corollary 2 (similarity forces zero).** If the admitted class at fixed
constants is preserved by a one-parameter family of transformations that
multiplies $X$ by every $s>0$, then $\gamma=0$ whenever some positive value
is attained. This is Q14's Theorem B for the observable $X$.

The two instances that motivate this note:

| | Mass gap of pure Yang--Mills | Action floor of the Galileo comparison |
| --- | --- | --- |
| Classical fixed constants | none in $D_A^*F_A=0$; $c$ alone | $m$, $F$ (or $m$, $g$) |
| $d_X$ in their span? | no: $c$ gives no mass | no: $(1,2,-1)\notin\operatorname{span}\{(1,0,0),(1,1,-2)\}$ |
| Classical similarity realizing zero | $A_s(x)=sA(sx)$: static energy $\mapsto sE$ in three space dimensions | $x\mapsto sx$, $t\mapsto s^{1/2}t$: $\tau\Delta E\mapsto s^{3/2}\tau\Delta E$ |
| Classical floor | $0$ | $0$ (C002, C027, C056--C058) |
| Quantum fixed constants | $\hbar$, $c$, dimensionless $g^2\hbar$: still no mass unit in $d=4$ | $\hbar$: action unit present |
| Where the scale must come from | the regularization scale, by transmutation (Section 4) | the constant $\hbar$ itself, whose necessity is the open question |

The classical Yang--Mills row is checked in Section 4; the Galileo row is
checked in Section 7. The table already states the analogy at the level of
Theorem 1: both classical theories have an empty span, both quantum theories
must obtain the missing unit from somewhere, and the two "somewheres" differ.

## 2. The exact $\hbar$-scaling of spectra for homogeneous potentials

**Theorem 3.** Let $V\ge0$ be continuous on $\mathbb R^n$ and positively
homogeneous of degree $k>-2$, $V(sx)=s^kV(x)$, and let
$H=-\frac{\hbar^2}{2m}\Delta+\lambda V$ be the Friedrichs operator of its
form on $C_0^\infty$. With the unitary dilation
$(U_\ell\psi)(x)=\ell^{-n/2}\psi(x/\ell)$ and
$$\ell^{k+2}=\frac{\hbar^2}{m\lambda},\qquad
\varepsilon=\frac{\hbar^2}{m\ell^2}
=\hbar^{\frac{2k}{k+2}}\,\lambda^{\frac{2}{k+2}}\,m^{-\frac{k}{k+2}},$$
one has $U_\ell^{-1}HU_\ell=\varepsilon\,(-\tfrac12\Delta+V)$. Every
spectral datum of $H$, in particular any gap, is $\varepsilon$ times the
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
classical action floor is zero by Corollary 2.

Three readings of Theorem 3 organize the rest of the note.

- For $k>0$ the exponent $2k/(k+2)$ is positive: the gap of $H$ is
  $\varepsilon\,\delta$ with $\delta$ a pure number and vanishes as
  $\hbar\to0$ and as $\lambda\to0$. A gap of a growing potential is a quantum
  effect and an interaction effect at once; at $\lambda=0$ the operator is
  $-\hbar^2\Delta/2m$ with spectrum $[0,\infty)$.
- The degree $k=-2$ is action-critical: the classical action is
  scale-invariant, $m\lambda$ has the dimension of action squared, the
  exponent of $\varepsilon$ has a pole, and the quantum problem depends on the
  single dimensionless number $2m\lambda/\hbar^2$ with no energy unit at all.
  This is the mechanical counterpart of the Yang--Mills scaling
  $S(A_s)=s^{4-d}S(A)$, which is critical at $d=4$
  ([comparison](comparison-and-bridges.md) §3). Section 6 treats it.
- Special cases of $\varepsilon$: $k=2$ gives $\hbar\sqrt{\lambda/m}$, the
  oscillator quantum up to a pure number; $k=4$ gives
  $\hbar^{4/3}\lambda^{1/3}m^{-2/3}$; $k\to\infty$ gives $\hbar^2/(m\ell^2)$
  with $\ell$ the box length, the particle-in-a-box unit; $k=-1$ gives
  $m\lambda^2/\hbar^2$, the Rydberg unit, whose *inverse* dependence on
  $\hbar$ means that the hydrogen level spacing diverges as $\hbar\to0$
  while the levels themselves crowd to zero from below. In each case the
  gap is the unique energy monomial in $(\hbar,m,\lambda)$, as Theorem 1
  requires.

## 3. Yang--Mills quantum mechanics: a solved gap that needs two commutators

The zero-momentum sector of Yang--Mills theory on a torus is a
finite-dimensional quantum-mechanical system whose potential is the squared
commutator of the constant gauge potentials. Its spectrum is purely discrete
for every positive $\hbar$ and coupling, although the classical energy range
is $[0,\infty)$ (Simon 1983; Lüscher 1983). The proof below is Simon's
first argument with every constant explicit, extended to the SU(2) model
with $D$ matrices and to its gauge-invariant sector.

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
   $\Delta=E_1-E_0>0$, and $H-E_0$ satisfies the Jaffe--Witten conditions
   with $0<m=\Delta<\infty$.
4. $E_n(\hbar,m,g)=\varepsilon\,e_n$ with $e_n$ the eigenvalues of
   $\tfrac12(-\Delta+x^2y^2)$ and
   $$\varepsilon=\hbar^{4/3}g^{2/3}m^{-2/3},\qquad
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

**Scaling.** Theorem 3 with $n=2$, $k=4$, $\lambda=g^2/2$:
$\varepsilon=\hbar^{4/3}(g^2/2)^{1/3}m^{-2/3}$, and absorbing the pure
number $2^{-1/3}$ into $e_n$ gives the displayed unit. At $g=0$ the Fourier
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
$[0,\infty)$. This is the exact zero-dimensional form of the statement that
commutative fields have no gap, and Section 4 gives the free-field form. The
temporal-gauge constant modes of a gauge theory in $d$ spacetime dimensions
are $D=d-1$ spatial components, so the zero-point mechanism needs $d\ge3$;
for $d=2$ the single matrix has no partner, in agreement with Section 5,
where two-dimensional Yang--Mills has no local excitations at all and its
discrete flux spectrum comes from the compact holonomy, a different
mechanism.

### 3.3 The finite-volume origin and the uniformity problem

**Proposition 7.** For SU(2) Yang--Mills on a spatial torus of side $L$
with action $S=-\frac{\hbar}{4g^2}\int F^a_{\mu\nu}F^{a\mu\nu}\,d^3x\,c\,dt$
($g$ dimensionless, $[A]=$ length$^{-1}$), temporal gauge and the
constant-mode ansatz $A^a_i(x,t)=a^a_i(t)$, the Hamiltonian is
$$H_0=\frac{g^2c}{2\hbar L^3}\sum_{i=1}^3|\vec p_i|^2
+\frac{\hbar cL^3}{2g^2}\sum_{i<j}|\vec a_i\times\vec a_j|^2,\qquad
[a^a_i,p^b_j]=i\hbar\delta_{ij}\delta^{ab},$$
which is Theorem 6 with $D=3$, $m=\hbar L^3/(g^2c)$ and
$g_B^2=\hbar cL^3/g^2$. Its energy unit is
$$\varepsilon=\hbar^{4/3}g_B^{2/3}m^{-2/3}=\frac{g^{2/3}\,\hbar c}{L},$$
so the zero-mode gap $\Delta_0(L)=\delta_1^{(3)}g^{2/3}\hbar c/L$ is positive
for every $L$ and decays as $1/L$ at fixed coupling.

*Proof.* With $F^a_{0i}=c^{-1}\dot a^a_i$ and $F^a_{ij}=(\vec a_i\times\vec
a_j)^a$ the Lagrangian is $\frac{\hbar L^3}{2g^2c}\sum|\dot{\vec a}_i|^2
-\frac{\hbar cL^3}{4g^2}\sum_{i,j}|\vec a_i\times\vec a_j|^2$; the Legendre
transform and $\tfrac14\sum_{i,j}=\tfrac12\sum_{i<j}$ give $H_0$, and the
exponent bookkeeping is $\hbar^{4/3+1/3-2/3}c^{1/3+2/3}L^{1-2}g^{-2/3+4/3}$.
$\square$

Lüscher's small-volume expansion (Nucl. Phys. B219 (1983) 233; abstract)
states that the torus spectrum is discrete and expands in powers of
$g^{2/3}$ with $g$ the renormalized coupling; Proposition 7 is its leading
term, and Lüscher--Münster (Nucl. Phys. B232 (1984) 445; abstract) carry
it to one loop for SU(2) and locate the crossover to large-volume behaviour
near $z=M(0^+)L\simeq2$. Jaffe and Witten write (p. 7 of the local PDF) that
"no present ideas point the direction to establish the existence of a mass
gap that is uniform in the volume". Proposition 7 shows the difficulty in
the solved sector: $\Delta_0(L)>0$ for every $L$ with
$\inf_L\Delta_0(L)=0$. Uniformity would need $g(L)^{2/3}/L$ bounded below,
outside the weak-coupling regime where the truncation is justified; the
compensation must come from the crossover regime, where the expansion no
longer applies. In the language of Theorem 1, $L$ is a fixed apparatus
length that enters the monomial and makes the finite-volume floor
non-universal, and the uniformity requirement is exactly the demand that
the floor be independent of it.

The supersymmetric contrast identifies the mechanism once more: de Wit,
Lüscher and Nicolai (Nucl. Phys. B320 (1989) 135; abstract) prove that the
supersymmetric matrix-model Hamiltonians have continuous spectrum starting
at zero, through low-energy states along the same abelian valleys. The
fermionic zero-point energy cancels the bosonic $\hbar\omega/2$ per
transverse mode, so the confining term of Theorem 5 vanishes. The gap of
Theorems 5--6 is exactly the uncancelled transverse zero-point energy.

## 4. Free and abelian fields have no gap; compact abelian gaps are supplied scales

**Proposition 8 (free fields inherit the classical dispersion).** Let $H$
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
generates no scale: every abelian finite-volume gap is $\hbar c/L$ times a
number.

**Proposition 10 (dimensional census of pure Yang--Mills).** With
$D=\partial+A$, $[A]=L^{-1}$, $[F]=L^{-2}$ and
$S=\frac1{g^2}\int\operatorname{tr}F^2\,d^dx$ of action dimension,
$[g^2]=(\text{action})^{-1}L^{d-4}$, so $g^2\hbar$ has dimension $L^{d-4}$.
The classical field equations $D_A^*F_A=0$ contain no constant, and the
static energy of $A_s(x)=sA(sx)$ in three space dimensions is $sE(A)$, so
the classical energy floor is zero. The quantum fixed constants are
$\hbar$, $c$ and $g$:

| $d$ | $g^2\hbar$ | Mass unit from $(\hbar,c,g)$ | Solved or expected gap |
| --- | --- | --- | --- |
| 2 | $L^{-2}$ | none; $g^2\hbar^2c$ is a string tension (energy/length) | $E_R=\tfrac12g^2\hbar^2cLC_2(R)$ on a circle, diverging with $L$ (Section 5) |
| 3 | $L^{-1}$ | $g^2\hbar^2/c$ | expected $m\propto g^2\hbar^2/c$ (Karabali--Nair, physics argument; lattice) |
| 4 | dimensionless | none | $m=a^{-1}F(g^2\hbar)$ with $F\to0$ along $g(a)$: transmutation |

By Theorem 1, a $d=4$ gap positive and finite must be a multiple of a mass
unit, and none exists among $(\hbar,c,g)$: the definition of the quantum
theory has to introduce a scale (cutoff $a$ or renormalization point), and
the continuum limit at fixed $m$ requires $F(g^2(a)\hbar)\to0$ along a curve,
which is dimensional transmutation stated as a dimensional necessity; the
one-loop form $m\propto a^{-1}\exp[-1/(2b_0g^2)]$ is the standard
asymptotic-freedom expression (Gross--Wilczek, Politzer 1973). In $d=3$ the
coupling itself carries the unit, and in $d=2$ it carries a tension but no
mass.

**Compact abelian theories.** Compactness of the gauge group supplies
topological excitations and, with them, gaps that are again supplied
scales. Osterwalder and Seiler (Ann. Phys. 110 (1978) 440) prove reflection
positivity, the strong-coupling infinite-volume limit and Wilson's
confinement bound for every compact group on the lattice; the
strong-coupling mass gap follows from their cluster expansion, in units of
$1/a$. Polyakov (Nucl. Phys. B120 (1977) 429) derives the photon
mass of three-dimensional compact $U(1)$ from monopoles, and Göpfert and
Mack (Commun. Math. Phys. 82 (1982) 545) prove the mass gap and confinement
of the three-dimensional Villain model for all couplings, with Debye mass
$m_D^2=(2\beta/a^3)e^{-\beta v(0)/2}$, $\beta=4\pi^2/e^2$ in lattice units:
a function of $e^2a$ with an essential singularity that vanishes as
$a\to0$ at fixed $e^2$.
Guth (Phys. Rev. D 21 (1980) 2291) and Fröhlich and Spencer (Commun. Math.
Phys. 83 (1982) 411) prove that four-dimensional compact $U(1)$ has a
massless Coulomb phase at weak coupling. The reading levels of these
citations are recorded in [B78](../references/batches/B78.md). The
dimensional reading is uniform: each gapped abelian case has its gap set by
an explicit scale in its definition, and the gap disappears when that scale
is removed at fixed coupling; the non-abelian cases in $d=3,4$ differ
because the coupling carries the unit or generates it by transmutation.

## 5. Two dimensions: an exactly solvable gap that is too large

**Proposition 11.** Pure Yang--Mills on a spatial circle of circumference
$L$, in temporal gauge with Gauss's law imposed, has as its only
gauge-invariant degree of freedom the holonomy $U\in G$ up to conjugation.
The physical Hilbert space is $L^2(G)^G$, the class functions, and with
$S=\frac1{2g^2}\int\operatorname{tr}F^2$ the Hamiltonian is
$H=\frac{g^2\hbar^2cL}{2}\,C$, where $C$ is the quadratic Casimir acting on
class functions. By Peter--Weyl the eigenfunctions are the characters
$\chi_R$ and
$$E_R=\frac{g^2\hbar^2cL}{2}\,C_2(R),\qquad
E_{\rm trivial}=0,\qquad
\text{gap}=\frac{g^2\hbar^2cL}{2}\,C_2(R_{\min})>0 ;$$
for $SU(N)$ with $\operatorname{tr}T^aT^b=\tfrac12\delta^{ab}$,
$C_2(\text{fund})=(N^2-1)/(2N)$, and for $U(1)$, $E_n=\frac{e^2\hbar^2cL}{2}n^2$
with $n\in\mathbb Z$ from compactness.

*Proof.* Gauss's law $D_xE=0$ makes the electric field covariantly
constant along the circle, so on class functions of the holonomy $E$ acts
as the left-invariant derivative and $\int_0^L\operatorname{tr}E^2\,dx$ as
$L$ times the Laplacian on the group; $H=\frac{g^2}{2}\int\operatorname{tr}E^2$
follows from $E=\dot A/g^2$, and restoring $\hbar,c$ uses $[g^2\hbar]=L^{-2}$
from Proposition 10. Characters diagonalize the Laplacian on class
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

## 6. Transmutation without a gap: the action-critical case in mechanics

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

The scale generated by quantization sits below the continuum threshold: the
excitation spectrum above the ground state is $[|E_B|,\infty)$, so the
one-particle problem does have an isolated ground state with spectral gap
$|E_B|$, but the "continuum" is the free particle escaping an unbounded
configuration space and every excitation energy above $|E_B|$ occurs. A
field-theoretic mass gap requires in addition that the vacuum be the ground
state and that all excitations be massive; transmutation supplies the scale
and confinement supplies the gap.

**Proposition 13 (inverse-square potential).** For $\ell=0$ the radial
equation of $-\frac{\hbar^2}{2m}\Delta-\lambda/r^2$ on $\mathbb R^3$ is
$-\frac{\hbar^2}{2m}u''-\frac{\lambda}{r^2}u=Eu$. For $2m\lambda/\hbar^2<1/4$
Hardy's inequality gives $H\ge0$, spectrum $[0,\infty)$ and no bound state.
For $2m\lambda/\hbar^2>1/4$ the operator is not essentially self-adjoint on
$C_0^\infty(\mathbb R^3\setminus0)$; each self-adjoint extension introduces
a length $r_0$ and the bound states form the geometric tower
$E_n=E_0e^{-2\pi n/\nu}$, $\nu=\sqrt{2m\lambda/\hbar^2-1/4}$, accumulating
at zero. Classically the fall to the centre occurs for angular momentum
below $\sqrt{2m\lambda}$, an action unit: $m\lambda$ has the dimension of
action squared.

This is the $k=-2$ case of Theorem 3. The classical theory owns an action
unit but no energy unit; the quantum theory depends on $2m\lambda/\hbar^2$
alone, and the definition of its dynamics forces a scale. C052's
relativistic Kepler plunge at $|L|<k/c$ is a competition of the same
$1/r^2$ type, so the classical action unit $k/c$ of Q14 is the mechanical
action-critical case, and C130 records its quantum version in the Dirac
thresholds. The lesson for necessity arguments is the hypothesis under
which "a scale is forced" is a theorem: the operator is symmetric, fails to
be essentially self-adjoint, and every self-adjoint extension carries a
scale. A consistency requirement, well-defined dynamics, forces the scale.
Sources for Section 6: Thorn, Camblong et al., Case, Essin and
Griffiths (B78).

## 7. The dictionary and what it decides for the positive-action question

### 7.1 Correspondences and non-correspondences

| | Mass gap | Positive action floor |
| --- | --- | --- |
| Object | physical Hamiltonian $H\ge0$ | action-defect observable on alternatives |
| Trivial state | vacuum $\Omega$, $H\Omega=0$ | inertial motion, zero defect |
| Statement | $\operatorname{spec}H\cap(0,m)=\varnothing$, $0<m<\infty$ | $\mathcal A(c)\cap(0,h)=\varnothing$, $0<h<\infty$ |
| Theorem 1 form | $m=$ (number) $\times$ mass unit of the fixed constants | $h=$ (number) $\times$ action unit of the fixed constants |
| Classical span | empty in $d=4$ | empty for $(m,F)$, $(m,g)$, $(G,c)$ |
| Classical similarity | $A_s(x)=sA(sx)$ | mechanical similarity of Proposition 4 |
| Classical countermodel | continuous classical energy range | C002, C027, C056--C058 |
| Free/commutative version | Proposition 8: no scale generated | ordinary calculus refinement: no scale generated |
| Generated gap | Theorems 5--6: two commutators, $\hbar^{4/3}g^{2/3}$ | none yet; C035--C036 need a supplied reference |
| Supplied gap | box, lattice, mass term, $d=2$ tension | C124/C126 ($K$), G05 ($J$), C060--C061 (speed floor) |
| Consistency-forced scale | regularization; Proposition 13 | the target of N02 |
| Assumed structure | gauge group, $\hbar$, quantum axioms | to be derived |

The last row is the non-correspondence that governs the rest. The mass-gap
problem states its non-commutative structure in the hypotheses and asks for
the scale. The necessity problem of STATE item 1 asks for the structure from
consistency premises, with quantum nature as the phenomenon to be explained.
The analogy is therefore exact for the second stage, from structure to
scale, where it says three things with proofs behind them: a positive floor
is a unit multiple and needs a unit (Theorem 1); the free or commutative
theory generates none (Propositions 8, Theorem 6(5)); and a generated scale
needs two scale-free ingredients that fail to commute, with the gap
vanishing when either is removed (Theorem 5). For the first stage, from
consistency to structure, the mass-gap story contains one mechanism that
does not presuppose the structure it explains: the scale forced by the
requirement that the dynamics be defined at all, which is the
self-adjoint-extension scale of Proposition 13 in quantum mechanics and the
regularization scale of Proposition 10 in field theory.

### 7.2 The commutative no-floor theorem for the Galileo comparison

**Proposition 14.** Let the admitted class be the constant-force motions
$q(t)=(vt,Ft^2/2m)$ with fixed constants $m,F$, all $v>0$, $\tau>0$
admitted, and let $X=\tau\Delta E=F^2\tau^3/(2m)$ or the area
$A=vF\tau^3/(6m)$. The similarity $x\mapsto sx$, $t\mapsto s^{1/2}t$,
$v\mapsto s^{1/2}v$ preserves the class and multiplies $X$ by $s^{3/2}$ and
$A$ by $s^2$; hence both floors are zero. The dimension vectors
$d_m=(1,0,0)$, $d_F=(1,1,-2)$ do not span $(1,2,-1)$, so Theorem 1 gives the
same conclusion without exhibiting the similarity.

*Proof.* $V=Fy$ is homogeneous of degree one, so Proposition 4 with $k=1$
gives $t\mapsto s^{1/2}t$ and action scaling $s^{3/2}$; the area is a
length squared. The span statement: $a(1,0,0)+b(1,1,-2)=(1,2,-1)$ forces
$b=2$ from the length component and then $-4\neq-1$ in time. $\square$

Which additions break the similarity? A fixed constant with action
dimension, that is $\hbar$, which is circular for the necessity argument. A
fixed constant whose dimension vector, with $d_m$ and $d_F$, spans action:
a fixed length $\ell_0$ gives $\sqrt{mF\ell_0^3}$; a fixed speed $c$ gives
$m^2c^3/F$; a fixed charge gives $k_e/c$ (Q14). Each of these is a supplied
unit, and the first two are mass-dependent, so they fail universality
(obligation 4 of the [action target](../research/ACTION_FIELD_TARGET.md))
unless a further premise ties them to $m$. Or a structure that is itself
scale-free but breaks the similarity when combined with the class: this is
what the two commutators do in Theorem 5 and what the definition problem
does in Proposition 13.

### 7.3 What the analogy transports to N02, labelled

The following is a conjecture shaped by Sections 3 and 6; it is stated so
that N02 can test it, and nothing below is claimed as proved.

**Conjecture (similarity anomaly).** Let alternatives compose under
concatenation with an action-defect observable that is additive and let the
composition rule be required to be consistent in a sense to be specified
(associative, positive, and defined for all admitted pairs). If the
composition rule is defined without a scale, then it is similarity-covariant
and the floor is zero (Corollary 2). A positive finite floor therefore
requires that the consistent definition of the composition itself carry a
scale, that is, an anomaly of the classical similarity: the similarity acts
on the alternatives but fails to act on the composed theory. Proposition 13
is the quantum-mechanical instance, where the composition is the
self-adjoint dynamics; Proposition 10 is the field-theoretic instance, where
it is the renormalized product of local operators.

What N02 would have to show is that the joint time/position refinement of
the Galileo comparison poses a definition problem of this type: a
composition of cut alternatives that is consistent only after a scale is
chosen. The existing countertests are the check: C027 composes constant-force
chords consistently at every mesh with no scale, and C028--C029 compose
Gaussian bridges consistently with a fixed but supplied $\kappa$. A
proposed principle that does not make one of these compositions
ill-defined at zero scale changes nothing, exactly as a classical Yang--Mills
argument that leaves $D_A^*F_A=0$ scale-covariant proves no gap.

What the analogy cannot deliver is the first stage itself. No theorem in
Sections 2--6 derives a commutator from a consistency premise; each takes
$[x,p]=i\hbar$ or the gauge group as given. The claim "h > 0 is analogous to
the mass gap" is exact and useful for the second stage and is a research
heuristic, recorded here as such, for the first.

## 8. Strategic consequence

Gap-track work now has a written gate: name whether a proposed gap is
supplied or generated, and for a generated gap name the two scale-free
structures whose product produces the unit. C124/C126 and G05 are supplied
gaps; G06's perturbed cluster chain would be as well, since $J$ remains an
input. The Yang--Mills quantum-mechanical gap is the first entry in the
programme whose scale is generated, and its exponents $4/3$ and $2/3$ are
forced by Theorem 1 once positivity is proved; its finite-volume version
exhibits the uniformity problem exactly. For STATE item 1 the consequence is
a sharpened target for N02: a consistency principle that makes the
zero-scale composition of cut alternatives ill-defined, tested against C027
and C028--C029. The dimensional table of Section 7.2 lists the units that a
supplied-constant route would have to justify, of which only $k_e/c$ is
mass-independent. No ledger claim is promoted; Theorems 5--6 and
Propositions 7, 11--13 are written proofs of established results with
explicit constants, and their sources are recorded with reading levels in
B78.
