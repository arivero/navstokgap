# Gauge spectral limits: finite lattices, coupling sets and the continuum target


The Hamiltonian route has distinct steps. T1 gives a unique physical
vacuum and positive gap on each finite lattice. T2 supplies an
existential volume-uniform strong-coupling gap for the Kogut--Susskind
operator; explicit Wilson-transfer estimates concern a different
operator. T2$'$ is the stronger all-coupling lower-bound property
$\liminf_{N_s\to\infty}\delta(g;N_s)>0$, not an equivalence to absence
of a bulk transition, and is not necessary at every bare coupling for a
continuum limit. T3 requires controlled physical gap scaling along the
weak-coupling trajectory, and T4 requires construction, nontriviality
and the axioms. Spectral transfer between finite lattices and the
specified limiting vacuum is an additional obligation. These latter
steps remain open. All energies below are measured using $\hbar c/a$;
volume and cutoff limits are separate.

## 1. The finite-lattice Hamiltonian

Let $G$ be a compact connected simple Lie group with Lie algebra basis
$T^a$ normalized by $\operatorname{tr}T^aT^b=\tfrac12\delta^{ab}$ in a
fixed faithful representation (for $SU(N)$ the fundamental). Let
$\Lambda=(a\mathbb Z/N_sa\mathbb Z)^3$ be the periodic spatial lattice with
spacing $a$, side $L=N_sa$, link set $\mathcal E$ and plaquette set
$\mathcal P$; $|\mathcal E|=3N_s^3$, $|\mathcal P|=3N_s^3$. The Hilbert space
is $\mathcal H=L^2(G^{\mathcal E},\mathrm{Haar}^{\otimes\mathcal E})$. On
the copy of $G$ attached to a link $\ell$, the electric field components
$E^a_\ell$ are $-i$ times the left-invariant vector fields, and
$\sum_a(E^a_\ell)^2=-\Delta_\ell$ is the Laplace--Beltrami operator of the
bi-invariant metric, whose eigenvalues on the Peter--Weyl blocks are the
quadratic Casimirs $C_2(R)$ with multiplicity $(\dim R)^2$. The
Kogut--Susskind Hamiltonian (Phys. Rev. D 11 (1975) 395, metadata) in the
convention used here is
$$H=\frac{\hbar c}{a}\Big[\frac{g^2}{2}\sum_{\ell\in\mathcal E}(-\Delta_\ell)
+\frac{2}{g^2}\sum_{p\in\mathcal P}\big(N-\operatorname{Re}\operatorname{tr}U_p\big)\Big]
=\frac{\hbar c}{a}\,\big[g^2K+g^{-2}V\big],$$
Here the plaquette trace constant $N$ is the faithful representation dimension (the colour $N$ for $SU(N)$), distinct from the number $N_s$ of sites per side. The scaled operators are $K=\tfrac12\sum_\ell(-\Delta_\ell)$ and $V=2\sum_p(N-\operatorname{Re}\operatorname{tr}U_p)$.
With $g$ dimensionless, $U_p$ the ordered product of the four link
variables around $p$, and $K$, $V$ the dimensionless electric and magnetic
operators. Other conventions rescale $g^2$ by a fixed number. The
dimensionless spectrum of $aH/(\hbar c)$ depends on $g$, $N_s$ and $G$ only:
$$\Delta_{a,L}=\frac{\hbar c}{a}\,\delta(g;N_s,G).$$

Gauge transformations $\gamma:\Lambda\to G$ act by
$(\mathcal V_\gamma\psi)(U)=\psi(\gamma_xU_\ell\gamma_y^{-1})$ for
$\ell=(x,y)$; they are unitary, commute with $H$ (the Laplacian is
bi-invariant and $\operatorname{tr}U_p$ is conjugation invariant) and
preserve positivity of functions. The physical space $\mathcal H_{\rm phys}$
is the joint fixed space (Gauss's law).

### SU(3) group factors

In this normalization $N=3$, $\dim SU(3)=8$,
$C_2(R_{\rm f})=4/3$, $C_2(\mathrm{adj})=3$ and
$Z(SU(3))=\mathbb Z_3$. The fundamental trace has
$\operatorname{tr}1=3$, so each magnetic plaquette term satisfies
$\|w_p\|\le12\hbar c/(ag^2)$. The
[strong-coupling proof](strong-coupling-uniform-gap.md),
[variational upper bounds](lattice-gap-upper-bounds.md),
[locality estimate](lieb-robinson-kogut-susskind.md) and
[vacuum identities](ground-state-measure-transfer.md) give their
specializations beside the corresponding hypotheses and proofs.
The [blocking comparison](blocking-criterion-monotone.md),
[central holonomies](torus-valley-potential.md#4-saturation-and-central-holonomies)
and [free colour-species cancellation](finiteness-half-flowed-susceptibility.md#the-bound-and-coupling-cancellation)
retain different geometries, sectors and approximation assumptions.

## 2. T1: every finite lattice has a gap above a unique physical ground state

**Theorem 1.** For every $a>0$, $N_s\ge2$, $g>0$ and $G$ as above:

1. $H$ is self-adjoint, bounded below, and has compact resolvent; its
   spectrum is a sequence $E_0<E_1<\cdots\to\infty$ of eigenvalues of
   finite multiplicity.
2. $E_0$ is simple with a strictly positive eigenfunction $\psi_0$, so
   $\Delta_{a,L}=E_1-E_0>0$.
3. $\psi_0\in\mathcal H_{\rm phys}$, $\mathcal H_{\rm phys}$ reduces $H$,
   and the physical gap satisfies $\Delta^{\rm phys}_{a,L}\ge\Delta_{a,L}>0$.

*Proof.* (1) $-\Delta_\ell$ is essentially self-adjoint on
$C^\infty(G)$, nonnegative, with compact resolvent, since $G$ is a compact
manifold and Peter--Weyl gives the eigenvalues $C_2(R)$ with finite
multiplicities and $C_2(R)\to\infty$ along any enumeration of irreducible
representations. $K=\tfrac12\sum_\ell(-\Delta_\ell)$ acts on the finite tensor
product with eigenvalues $\tfrac12\sum_\ell C_2(R_\ell)$; for each bound $E$ only
finitely many assignments $\ell\mapsto R_\ell$ have $\sum_\ell C_2(R_\ell)\le E$,
so $K$ has compact resolvent. $V$ is multiplication by a continuous
function with $0\le V\le4N|\mathcal P|$, hence bounded, and a bounded
perturbation of an operator with compact resolvent has compact resolvent
by the resolvent identity
$(H-z)^{-1}=(H_0-z)^{-1}[1+(g^{-2}V)(H_0-z)^{-1}]^{-1}$ for $z$ far in the
negative axis. Discreteness with finite multiplicities and
$E_n\to\infty$ follow, and $E_0$ is an eigenvalue.

(2) The heat kernel of $-\Delta$ on a compact connected Riemannian manifold
is strictly positive for $t>0$ (standard, from the strong maximum
principle or the Peter--Weyl expansion; metadata level), so the kernel of
$e^{-tK}$ on $G^{\mathcal E}$, a product of strictly positive kernels, is
strictly positive. With Brownian motion $X_t$ on $G^{\mathcal E}$ generated
by $-K$ (time rescaled by $g^2\hbar c/a$), the Feynman--Kac formula gives
$$(e^{-tH}\psi)(U)=\mathbb E^U\Big[\exp\Big(-\frac{\hbar c}{ag^2}\int_0^tV(X_s)\,ds\Big)\psi(X_t)\Big],$$
valid because $V$ is bounded and continuous. For $\psi\ge0$, $\psi\ne0$,
the weight is at least $e^{-t\hbar c\cdot4N|\mathcal P|/(ag^2)}>0$ and the law
of $X_t$ has a strictly positive density, so $(e^{-tH}\psi)(U)>0$ for
every $U$: $e^{-tH}$ is positivity improving. Reed--Simon IV, Theorem
XIII.44 (metadata; number corroborated as in B78) then gives that $E_0$ is
simple with $\psi_0>0$ almost everywhere, and $E_1>E_0$ because $E_1$ is
the next eigenvalue of a discrete spectrum.

(3) $\mathcal V_\gamma\psi_0$ is a normalized eigenfunction for $E_0$,
hence $\mathcal V_\gamma\psi_0=c(\gamma)\psi_0$ with $|c|=1$; both
functions are positive, so $c(\gamma)=1$ and $\psi_0\in\mathcal H_{\rm phys}$.
The projection $P=\int\prod_x d\gamma_x\,\mathcal V_\gamma$ onto
$\mathcal H_{\rm phys}$ commutes with $(H-z)^{-1}$, so $\mathcal H_{\rm phys}$
reduces $H$ and the restricted operator has compact resolvent, ground
state $\psi_0$, and next eigenvalue at least $E_1$. $\square$

Theorem 1 defines the object whose limits the conjecture is about. It
proves nothing about those limits: $\Delta_{a,L}$ is $\hbar c/a$ times a
number that may tend to zero as $N_s\to\infty$ or as $g\to0$.

## 3. T2: strong coupling, and why volume uniformity is the whole difficulty

At $g\to\infty$ the operator $g^2K$ dominates. Its ground state is the
constant function, with eigenvalue $0$, and its excitations are link
representations. Gauge invariance excludes a single excited link: the
lowest physical excitation of $K$ for a periodic $SU(N)$ lattice with
side at least four is a four-link plaquette loop in the fundamental representation,
with electric energy $4\cdot\tfrac12C_2(R_{\min})\,g^2\hbar c/a=2C_2(R_{\min})g^2\hbar c/a$;
for $SU(N)$, $C_2(\text{fund})=(N^2-1)/(2N)$. So the unperturbed physical
gap is
$$\gamma_{\rm phys}(g)=2C_2(R_{\min})\,g^2\,\frac{\hbar c}{a},$$
uniform in the side length under this restriction. At shorter periodic
sides winding cycles can be shorter; nonabelian networks can also branch.

**The naive bound fails.** The magnetic term satisfies
$0\le g^{-2}V\le4N|\mathcal P|g^{-2}$ in operator norm, so positivity and min–max give $\Delta^{\rm phys}\ge\gamma_{\rm phys}-\|g^{-2}V\|\hbar c/a
=(2C_2g^2-4N|\mathcal P|g^{-2})\hbar c/a$, positive only when
$g^4>2N|\mathcal P|/C_2$. The bound is extensive in the volume and useless
as $N_s\to\infty$. Volume uniformity therefore requires using that $V$ is a
sum of $|\mathcal P|$ terms each of norm at most $4N g^{-2}$ and each
acting on four links: locality, not smallness of the norm.

**What is established.** Osterwalder and Seiler (Ann. Phys. 110 (1978)
440; abstract, B78) prove for the Euclidean lattice theory with any
compact gauge group, at sufficiently strong coupling, reflection
positivity, the existence of the infinite-volume limit and Wilson's
confinement bound by a cluster expansion; exponential clustering of
gauge-invariant correlations uniform in the volume, that is a mass gap of
the transfer matrix in units of $1/a$, is the standard consequence of the
same expansion (not read at section level). Hamiltonian versions rest on
gap-stability theorems for local perturbations of commuting,
frustration-free Hamiltonians (Yarotsky, Commun. Math. Phys. 261 (2005)
799; Bravyi--Hastings--Michalakis, J. Math. Phys. 51 (2010) 093512; both
metadata): $g^2K$ is a sum of commuting link terms with a product ground
state and a uniform local gap, and $g^{-2}V$ is a sum of bounded local
terms. Yarotsky permits the infinite-dimensional local spaces and the relevant
bounded perturbation. The full hypothesis check, with existential
constants, is in [the strong-coupling note](strong-coupling-uniform-gap.md).
The finite-volume physical loop estimate above does not itself give a
volume-uniform threshold.

## 4. Coupling sets, finite volume and spectral limits

Define, for the Kogut--Susskind Hamiltonian of
this note, with gauge group
$G$, lattice spacing $a$ and $N_s$ sites per side,
$$c(g)=\liminf_{N_s\to\infty}\delta(g;N_s,G),\qquad
\mathcal G=\{g>0:\ c(g)>0\},\qquad
\Delta_{a,L}=\frac{\hbar c}{a}\delta(g;N_s,G),\quad L=aN_s.$$
Here $c(g)$ is a dimensionless lower-gap function; the constant $c$ in
$\hbar c/a$ is the speed of light. The volume limit is taken at fixed
$a$ and $g$. To retain the obligations map's convention, $\delta$ is
the gap on the **full link Hilbert space**. Its restriction to the
Gauss-law space has a gap $\delta^{\rm phys}\ge\delta$; closing of
$\delta$ need not even close $\delta^{\rm phys}$. An analogous gapped
set can be defined using $\delta^{\rm phys}$, but the two sets have not
been identified here.

T1 gives positivity at every finite volume; T2 gives
$[g_0(G),\infty)\subset\mathcal G$; and T2$'$, as an all-coupling
finite-volume lower-bound statement, is exactly
$\mathcal G=(0,\infty)$. Proposition 1 proves finite-volume continuity.
Proposition 2 identifies the slowest temporal correlation decay with
the spectral threshold **assuming a specified limiting vacuum theory**;
it does not identify that threshold with $c(g)$. Global openness and
closedness of $\mathcal G$ remain open. If openness is established,
closedness and the known nonemptiness would imply T2$'$ by connectedness.
This is a sufficient route to a lattice statement, not an equivalence
with the continuum mass-gap conjecture or with phase-transition absence.

### 4a. Finite-volume continuity

**Proposition 1.** For fixed $a$, $N_s\ge2$ and a nontrivial compact connected Lie group $G$,
the map $g\mapsto\delta(g;N_s,G)$ is continuous and strictly positive
on $(0,\infty)$, and locally piecewise real-analytic. The same holds
for the physical gap.

*Proof.* Write
$$h(g):=\frac{aH(g)}{\hbar c}=\frac{g^2}{2}K_0+\frac{2}{g^2}V_0,$$
with $K_0=\sum_\ell(-\Delta_\ell)\ge0$ having compact resolvent and
$V_0=\sum_p(N-\operatorname{Re}\operatorname{tr}U_p)$ bounded, with
$0\le V_0\le2N|\mathcal P|$ for $SU(N)$ in the fundamental
representation. For a general compact connected group, use the fixed
faithful representation and replace $N$ by its dimension. In a complex
neighbourhood of any $g>0$, this is a holomorphic family of type (A)
on the common domain $D(K_0)$. For real $g$ it is self-adjoint with compact
resolvent. The local analytic eigenvalue-branch theorem for a
self-adjoint analytic family (Kato/Rellich analytic perturbation theory,
standard theorem used here) supplies finitely many real-analytic
branches in an isolated spectral cluster. The ground branch is simple
by T1. In a neighbourhood of each $g$, the first excited eigenvalue is
the minimum of the finitely many branches in its cluster, hence
continuous. Distinct analytic branches have isolated crossings locally;
identically coincident branches do not affect this conclusion. Thus
the gap is locally piecewise analytic and continuous. T1 supplies its
strict positivity. The gauge projection reduces both $K_0$ and $V_0$, so
the same argument applies on the fixed physical subspace. $\square$

**Correction (2026-10-02).** The original min--max explanation did not
prove continuity: an infimum over subspaces of continuous functions
need not be continuous. The analytic-branch argument above replaces it;
no simplicity of the first excited eigenvalue is assumed.

Finite-volume positivity supplies no positive volume-uniform lower
bound. In particular $c(g)$ need not be continuous, and no regularity of
$\mathcal G$ follows just from Proposition 1.

### 4b. Spectral limits and surviving weight

If $c(g)=0$, then $\delta(g;N_s,G)\to0$ along a subsequence of volumes.
This is a statement about eigenvalues of different operators, not about
the spectrum of a constructed infinite-volume operator. To discuss
correlation length, first assume a limiting vacuum representation of
the local gauge-invariant observable algebra, with cyclic vacuum
$\Omega$, nonnegative dimensionless Hamiltonian $h_\infty$, and
$\ker h_\infty=\mathbb C\Omega$. The physical time generator is
$H_\infty=(\hbar c/a)h_\infty$. Existence of this representation and
convergence of the relevant correlators are extra hypotheses here.

For each bounded local gauge-invariant observable $A$, set
$A_0=A-\langle\Omega,A\Omega\rangle I$ and define its finite positive
spectral measure and temporal connected autocorrelation by
$$\mu_A(B)=\langle A_0\Omega,\mathbf1_B(h_\infty)A_0\Omega\rangle,
\qquad C_A(s)=\int_{[0,\infty)}e^{-s\lambda}\,d\mu_A(\lambda),
\quad s=\frac{ct_E}{a}.$$
For $\mu_A\ne0$ define $r_A=\inf\operatorname{supp}\mu_A$ and
$$r=\inf_{A:\mu_A\ne0}r_A,\qquad \xi_t=\frac{a}{r},$$
with $\xi_t=\infty$ when $r=0$. This takes the **slowest rate over all
local gauge-invariant observables**, rather than the rate of an
arbitrarily chosen observable. It is a temporal correlation length;
no equality with a spatial correlation length at fixed Hamiltonian
lattice spacing is asserted.

**Proposition 2 (conditional replacement).** In the vacuum
representation just specified, with a nonzero excited subspace,
$$m_{\rm lat}:=\inf\sigma(h_\infty|_{\Omega^\perp})=r,
\qquad \Delta_\infty=\frac{\hbar c}{a}m_{\rm lat}
=\frac{\hbar c}{\xi_t}.$$
For every nonzero $\mu_A$,
$-\lim_{s\to\infty}s^{-1}\log C_A(s)=r_A$.
These assertions concern the assumed limit theory; they make no claim
that $m_{\rm lat}=c(g)$.

*Proof.* Positivity of the spectral measure gives
$C_A(s)\le\mu_A([0,\infty))e^{-sr_A}$. For every $\varepsilon>0$,
the definition of support gives positive weight
$w_\varepsilon=\mu_A([r_A,r_A+\varepsilon])>0$, whence
$C_A(s)\ge w_\varepsilon e^{-s(r_A+\varepsilon)}$.
Taking logarithms, then $s\to\infty$ and
$\varepsilon\downarrow0$, proves the rate formula. Centered local
vectors are dense in $\Omega^\perp$ by cyclicity of $\Omega$ for the
local algebra. All their spectral supports lie above $m_{\rm lat}$,
so $r\ge m_{\rm lat}$. For every $\varepsilon>0$ the spectral projection
on $[m_{\rm lat},m_{\rm lat}+\varepsilon)$ in $\Omega^\perp$ is nonzero.
Density implies that it has nonzero action on some centered local
vector. That vector has $r_A<m_{\rm lat}+\varepsilon$, proving the
reverse inequality after $\varepsilon\downarrow0$. The physical-unit
identity follows from the definition of $H_\infty$. $\square$

An infimum of rates equal to zero need not be attained by a single
observable: $\xi_t=\infty$ need not mean that *one* observable has
slower-than-exponential decay. It can mean that there is no common
positive exponential rate for the entire local algebra.

**Why the original implication fails.** Even convergence of an
observable's spectral measures does not preserve their lowest support
points. With $\mathrm d_x$ denoting unit point mass at $x$, consider
$$\mu_n=(1-e^{-n})\mathrm d_1+e^{-n}\mathrm d_{1/n}.
$$
Its threshold tends to zero, but $\mu_n\Rightarrow\mathrm d_1$, whose
threshold is one. The soft mode loses all its observable weight. This
is a spectral-measure illustration, not a counterexample constructed
for the fixed Kogut--Susskind family. It identifies information that
finite-volume eigenvalues alone lack. Nonlocal sectors and the
full-space/physical-space distinction add further obstacles.

A valid sufficient implication is available **with surviving weight**.
Suppose centered finite-volume local spectral measures
$\mu_n\Rightarrow\mu_A$ in the representation above and, for every
$\eta>0$, there is $w_\eta>0$ with
$\mu_n([0,\eta/2])\ge w_\eta$ eventually. The closed-set inequality
gives $\mu_A([0,\eta/2])\ge w_\eta$. Uniqueness of the vacuum and
centering give $\mu_A(\{0\})=0$, so $\mu_A((0,\eta))>0$ and
$m_{\rm lat}=0$. These are precisely the extra convergence and weight
hypotheses of [three continuum limits, §5](three-continuum-limits.md)
(reading: passage). No such estimates are proved here for arbitrary $g$.

**Correction (2026-10-02): phase interpretation.** Vacuum coexistence
with small finite-volume tunnelling splittings and a gapless local
phase are possible scenarios, not an exhaustive consequence of
$c(g)=0$. Distinct infinite-volume ground states may persist throughout
a symmetry-broken interval, with a positive excitation gap in each
selected vacuum representation. A massless phase can likewise occupy
an interval. Neither every degeneracy nor every gapless coupling is
an isolated first- or second-order transition; neither an exponential
volume law for tunnelling nor transition order was proved by the
original argument.

**Corollary 3 (original equivalence withdrawn, 2026-10-02).** There is
no proved equivalence here between $\mathcal G=(0,\infty)$ and absence
of bulk phase transitions. T2$'$ means only the all-coupling lower-bound
property defined in the lead. Identifying it with phase behaviour needs
a limit theory, a specified vacuum/sector and spectral comparison.

*Precision, 2026-09-23, corrected 2026-10-02.* The
[openings note, §1](mass-gap-openings.md) (reading: passage) records
Wilson-action numerical evidence for first-order bulk transitions for
$SU(N\ge5)$, with source
[Rindlisbacher--Rummukainen--Salami](https://arxiv.org/abs/2306.14319).
It does not prove a hole in the $\mathcal G$ of this KS Hamiltonian:
the Euclidean Wilson operator differs, and the spectral comparison is
missing. Such intermediate-coupling lattice phenomena do not by
themselves obstruct a continuum limit along $g\to0$. All-coupling T2$'$
is stronger than the weak-trajectory gap and scaling control needed
for T3, together with continuum construction and nontriviality T4.

### 4c. What a second-order point could mean

**Correction (2026-10-02).** A divergent correlation length is a
necessary scaling signal for a continuum limit with a fixed nonzero
physical mass, not a proof that a continuum theory exists. The original
assertion that a second-order point automatically produces a continuum
limit, and the equivalence with uniqueness of the asymptotically free
limit, are withdrawn.

If a positive dimensionless local spectral mass $m_{\rm lat}(g)$ tends to zero
as $g\to g_*>0$, one can *choose* $a(g)=m_{\rm lat}(g)/M$ to keep the
inverse-length scale $M>0$ fixed. Then
$\Delta(g)=\hbar cM$ and $\xi_t/a=1/m_{\rm lat}\to\infty$.
This choice supplies scale matching only. Convergence of renormalized
correlators, positivity, axioms and nontriviality remain to be proved.
Moreover, diverging length alone does not specify transition order.

An asymptotically free trajectory instead approaches $g=0$ with
$a\Lambda_{\rm lat}(g)\to0$ as described in
§5 below.
A possible finite-$g_*$ scaling limit would be a different trajectory;
T2$'$ alone classifies neither continuum limits nor universality classes.
Numerically, the fundamental--adjoint plane of $SU(3)$ exhibits scalar
softening consistent with a critical endpoint and a $\phi^4$ continuum
interpretation ([Heller 1995](https://arxiv.org/abs/hep-lat/9508009),
reading: abstract). This is evidence for that interpretation, not a
constructed scalar continuum theory or a theorem for the Wilson axis.

### 4d. The abelian case: action, phase and transition order

The strong-coupling theorem applies to compact $U(1)$: in the
normalization $-\Delta$ has eigenvalues $n^2$, so
$C_2(R_{\min})=1$ and the defining representation has dimension one.
[The T2 note](strong-coupling-uniform-gap.md) (reading: full-read)
gives the KS bound
$$\delta(g;N_s,U(1))\ge\gamma\frac{g^2}{2},\qquad
g^4\ge\frac{24}{\beta_*},$$
with existential constants $\gamma,\beta_*>0$ independent of volume.
This proves a strong-coupling half-line is contained in $\mathcal G$,
not that $\mathcal G$ is exactly a half-line.

For four-dimensional Euclidean compact $U(1)$,
[Guth](https://doi.org/10.1103/PhysRevD.21.2291) proves a nonconfining
weak-coupling phase for the **Villain** action (reading: abstract);
[Fröhlich--Spencer](https://doi.org/10.1007/BF01213610) establishes a
massless Coulomb phase in the setting recorded in
[B78](../references/batches/B78.md) (reading: abstract). Those phase
results do not determine transition order or a continuously vanishing
confined-phase mass. They also do not establish the exact set
$\mathcal G_{U(1)}=(g_c,\infty)$ for the KS operator defined here;
that translation would need its own proof.

For the standard four-dimensional **Wilson** action, numerical evidence
supports a **weakly first-order** zero-temperature bulk transition
([Vettorazzo--de Forcrand 2004, §§2--3](https://arxiv.org/html/hep-lat/0409135v2),
reading: passage). This replaces the erroneous second-order assertion.
The Maxwell description belongs to the weak-coupling massless phase;
no Maxwell continuum construction at the transition endpoint is
established here. A massless phase over an interval also defeats the
original identification of every gapless coupling with a transition point.

The abelian comparison remains useful: group-independent strong-coupling
gap arguments alone do not supply weak-side control. The commutator
potential of [G07, §3](low-dimensional-mass-gap.md), the local-observable
restriction of [the upper-bound note, Proposition 6](lattice-gap-upper-bounds.md),
and the formal valley calculation of [the valley note, §3b](torus-valley-potential.md)
are distinct ingredients with distinct scopes. None is by itself a
proof of a nonabelian infinite-volume or continuum gap, or of the global
shape of either group's gapped set.

### 4e. Openness and closedness

For any subset of the connected interval $(0,\infty)$,
$$\mathcal G=(0,\infty)\quad\Longleftrightarrow\quad
\mathcal G\ne\varnothing\ \text{and}\ \mathcal G\text{ is open and closed}.$$
This is a topological fact, not a regularity theorem for $c(g)$.

| property | status | what it would take |
| --- | --- | --- |
| $\mathcal G\ne\varnothing$ | proved by T2: $[g_0,\infty)\subset\mathcal G$ | [strong-coupling theorem](strong-coupling-uniform-gap.md) |
| $\mathcal G$ open | unproved globally; $(g_0,\infty)$ is a known interior region | volume-uniform stability under changes of $g$ |
| $\mathcal G$ closed | unproved; sufficient for T2$'$ if openness holds | positivity at every finite limit point of gapped couplings, with control preventing lower bounds from collapsing |

**Correction (2026-10-02): later locality result.** The original text
left a Lieb--Robinson extension for the unbounded electric terms as the
next obstacle. [The later locality note, §§1--2](lieb-robinson-kogut-susskind.md)
(reading: full-read) treats the commuting on-link electric terms in the
interaction picture, leaving bounded finite-range plaquette interactions
with unchanged support and norm. This addresses the locality ingredient;
no numerical velocity or clustering-length estimate from that note is
needed here. Its §5 also explains why locality alone does not prove gap
stability: the cited stability route has additional hypotheses not
verified at general finite KS coupling, including frustration-freeness.
No universal assertion that every stability theorem requires that
hypothesis is intended.

Closedness alone is not T2$'$ without openness, and excluding the two
originally proposed scenarios would not establish either property.
Finite-volume analytic dependence provides neither estimate. Even a
proved T2$'$ would still leave continuum scaling, construction and
nontriviality to T3/T4.

## 5. T3: the scaling limit, as one asymptotic statement

Along the continuum curve the bare coupling runs with the cutoff. With
$b_0=11N/(48\pi^2)$ and $b_1=34N^2/(3(16\pi^2)^2)$ for $SU(N)$ (the
two-loop coefficients in the convention $\beta(g)=-b_0g^3-b_1g^5+\cdots$;
Gross--Wilczek, Politzer, abstract, B78), the lattice $\Lambda$ parameter
is defined by
$$a\Lambda_{\rm lat}(g)=(b_0g^2)^{-b_1/(2b_0^2)}\,e^{-1/(2b_0g^2)}\,[1+O(g^2)],$$
a dimensionless function that vanishes faster than any power of $g$.

For $SU(3)$, $b_0=11/(16\pi^2)\simeq0.06966$,
$b_1/(2b_0^2)=51/121\simeq0.4215$ and
$1/(2b_0)=8\pi^2/11\simeq7.180$. Thus
$$a\Lambda_{\rm lat}(g)=(b_0g^2)^{-51/121}
e^{-8\pi^2/(11g^2)}[1+O(g^2)].$$
Here $\Lambda_{\rm lat}$ has units of inverse length; the corresponding
energy scale is $\hbar c\Lambda_{\rm lat}$.

> **T3.** The limit $\displaystyle\frac{m}{\hbar c\,\Lambda_{\rm lat}}
> =\lim_{g\to0}\frac{\delta_\infty(g)}{a\Lambda_{\rm lat}(g)}$ exists and lies
> in $(0,\infty)$.

This is a proposed lattice-route scaling condition for a mass parameter $m$; identifying it with the gap of the reconstructed limit needs spectral transfer and surviving physical weight: the
dimensionless infinite-volume gap must vanish as $g\to0$ exactly like
$e^{-1/(2b_0g^2)}$ times the prescribed power, with a positive finite
prefactor. Any weaker vanishing gives $m=\infty$ in the continuum (the
theory is gapped only at the cutoff scale, as the compact abelian theory
in three dimensions is, G07 §4); any faster vanishing, or
$\delta_\infty=0$ at arbitrarily small $g$, gives $m=0$. T3 presupposes
$\delta_\infty>0$ on an interval $(0,g_1)$, which T2$'$ implies. The
order of limits is $N\to\infty$ at fixed $g$ first, then $g\to0$ with
$a=\Lambda_{\rm lat}^{-1}\,a\Lambda_{\rm lat}(g)$; Jaffe and Witten note
(p. 6, passage) that a gap uniform in the volume would also serve to
construct the infinite-volume limit, which is the reverse order.

**The conditional small-volume corner.** The weak-volume regime is
$L\Lambda_{\rm lat}\ll1$. Homogeneity of the constant-mode matrix
Hamiltonian gives the candidate scale $g(L)^{2/3}\hbar c/L$. The
[positive matrix gap](low-dimensional-mass-gap.md) is proved here for
$SU(2)$; an $SU(3)$ substitution supplies group constants, not the
missing matrix theorem. Even with that input, the
[Feshbach hypotheses](weak-coupling-feshbach-reduction.md) on nonzero
modes, gauge-compatible projection and uniform errors must be proved
before transferring the scale to the field theory. Lüscher's expansion
(*Nucl. Phys. B* **219** (1983) 233, abstract-level reading) is source
orientation, not a verification of those hypotheses here.

If small-volume comparison and continuum reconstruction hold in a declared
sector $\mathcal C$, the candidate sector gap obeys
$$z_{\mathcal C}(L)=\frac{\Delta_{\mathcal C}(L)L}{\hbar c}
=\delta_{1,\mathcal C}g(L)^{2/3}[1+O(g(L)^{2/3})]\quad(L\to0).$$
This is not automatically the full finite-box gap. The
[periodic holonomy countertest](torus-valley-potential.md#a-centre-odd-variational-countertest)
has a much smaller centre-sector splitting. The sector, physical observable
algebra and projection must match before transferring a local matrix spacing.
Separately, if the infinite-volume physical gap is a finite positive
energy $m$ and the finite-volume gaps converge to it, then
$z(L):=\Delta(L)L/(\hbar c)\sim mL/(\hbar c)$ as $L\to\infty$. Neither endpoint proves a
monotone interpolation, excludes intervening behavior or constructs
the continuum theory. Lüscher--Münster's crossover near $z\simeq2$
(*Nucl. Phys. B* **232** (1984) 445, abstract) remains a historical
orientation; the [one-loop valley calculation](torus-valley-potential.md)
does not establish that crossover as a spectral theorem.

## 6. T4: existence

The lattice route needs the continuum limit of the Euclidean lattice
theory with Osterwalder--Schrader reconstruction. Known: ultraviolet
stability of four-dimensional lattice Yang--Mills in a finite volume with
the cutoff removed (Balaban, Commun. Math. Phys. 122 (1989) 355 and the
series it belongs to; Magnen--Rivasseau--Sénéor, Commun. Math. Phys. 155
(1993) 325, with an infrared cutoff; both metadata). Open: the
infinite-volume limit, the axioms in infinite volume, and any spectral
information. Jaffe and Witten (p. 7, passage) write that a construction on
a compact space alone would be a major step and that no present ideas
give a gap uniform in the volume.

## 7. The list

| Statement | Content | Status |
| --- | --- | --- |
| T1 | finite lattice: unique physical ground state, gap $\Delta_{a,L}=(\hbar c/a)\delta(g;N_s,G)>0$ | proved (Theorem 1) |
| T2 | $\delta(g;N_s,G)\ge c(N)g^2$ for $g\ge g_0(N)$, uniformly in $N$ | established: Euclidean form (Osterwalder--Seiler); Hamiltonian form as a corollary of Yarotsky's theorem in [the strong-coupling note](strong-coupling-uniform-gap.md) |
| T2$'$ | $\delta_\infty(g)>0$ for all $g>0$ | open; the cited Euclidean U(1) phase does not by itself identify the KS gapped set |
| T3 | $\delta_\infty(g)/(a\Lambda_{\rm lat}(g))\to m/(\hbar c\Lambda_{\rm lat})\in(0,\infty)$ | open; spectral transfer to the reconstructed theory is also required |
| T4 | continuum infinite-volume theory with the axioms | selected ultraviolet-stability inputs; construction and axioms open |
| S | small-volume corner $z(L)=\delta_1g(L)^{2/3}[1+O(g^{2/3})]$ | C133 plus Lüscher's expansion |

T2$'$ is a stronger all-coupling route, not a necessary independent
condition for the continuum goal. T3 and T4 still require physical
spectral transfer, nontriviality and the stated limit order.

## Existing estimates and examined routes

For the $SU(3)$ Wilson transfer matrix, the separate sufficient bounds are
$g^2>24/\log(19/18)$ (integer $g^2>444$ sufficient) from
[Dobrushin](dobrushin-uniqueness-wilson.md), and
$g^2\ge6/\log(1+21/(500e^2))$ (integer $1059$ sufficient) from the
[all-representation polymer proof](wilson-strong-coupling-explicit.md).
Their physical lower rates in units $\hbar c/a$ are respectively
$$
 \log\frac1{18(e^{24/g^2}-1)},\qquad
 4\log\frac1{176(e^{6/g^2}-1)}.
$$
The latter rate additionally needs $g^2>6/\log(177/176)$ to be positive.
The leading-activity figure $176$, linearization $1056$ and sufficient integer
$1059$ are different statements. Neither criterion is a phase boundary.
For KS, the explicit volume-uniform $388$ threshold is withdrawn; the
[finite-volume correction](strong-coupling-uniform-gap.md#continuous-time-histories-and-the-corrected-overlap-criterion) is
$\delta^{\rm phys}\ge(8/3)g^2-12|\mathcal P|/g^2$ under its stated lattice
restrictions. The [Yarotsky application](strong-coupling-uniform-gap.md)
retains existential volume uniformity. These are distinct operators and bounds.

The following are failures of the specified routes, not an exhaustion theorem:

| route | why it closes |
| --- | --- |
| variational upper bounds, for $m>0$ | a spectral measure with all negative moments finite can have $m=0$ |
| expansion around the free theory | the bound reaches $m$ only at the confinement scale, where its coefficient is nonperturbative |
| blocking by projection | a surface-to-gap estimate worsens by $3M^2/8$ in the stated strong-coupling asymptotic; all-coupling monotonicity is not proved |
| conjugation by the flow | the spectrum is invariant; a changed local decomposition requires control of generated terms |
| flow before decimation | sup norms are bijection-invariant and spectra conjugation-invariant |
| Agmon estimate on the ground state | $\|\nabla V\|_\infty$ is extensive, so it bounds the global excess only |
| pointwise Gibbs domination | the comparison function bites only above the extensive threshold $V_*\simeq N|\mathcal P|$ |


The exact [magnetic-energy sum rule](ground-state-measure-transfer.md#common-setting-and-magnetic-identities) and
[ground-state transfer](ground-state-measure-transfer.md) remain useful
identities. A normalized isotropic Wilson estimate does not transfer verbatim
to the anisotropic KS ground state; projector convergence and matching of the
measure/observable are needed. A [flowed variational upper bound](finiteness-half-flowed-susceptibility.md)
requires a finite derivative expectation and nonzero physical susceptibility;
it is not by itself a positive lower gap.

The nonabelian matrix-model commutator valley, Gauss-law exclusion of a
c-number linear electric probe and the formal torus-holonomy potential have
different proof scopes ([matrix gap](low-dimensional-mass-gap.md),
[electric observables](lattice-gap-upper-bounds.md), [valley](torus-valley-potential.md)).
None fixes the shape of the KS gapped set or a four-dimensional continuum gap.

The [gauge atlas](halving-atlas.md) owns the refinement-depth map. A local
[action cost and background count](large-field-action-lower-bound.md) prove
no normalized rarity theorem. A [kernel tail](flow-conjugation-truncation.md#exact-continuum-variation-and-its-gauge-convention)
proves no Hamiltonian relative comparison. The
[signed operator test](large-field-operator-inequality.md) diagnoses one
localization/surface-loss construction, not every possible Hamiltonian method.
The [crossover comparison](mass-gap-openings.md#correlation-inequalities-and-the-transfer-they-require) retains what the
examined correlation and finite-certification tools would actually require.

## 8. Consequence for STATE

T2 in Hamiltonian form is now closed in
[the strong-coupling note](strong-coupling-uniform-gap.md) as a corollary
of Yarotsky's gap-stability theorem, with threshold
$g_0(N)=(48N^2/[(N^2-1)\beta_*])^{1/4}$; the unresolved task is to control the weak-coupling scaling trajectory and transfer the physical spectrum to the reconstructed theory. The
$d=3$ target of STATE keeps its place as the case where T3 has no
transmutation to perform.
