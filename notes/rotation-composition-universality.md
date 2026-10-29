# Composition and action normalization: reciprocal mechanics, rotations and spin phases

Interaction can constrain relative normalizations while leaving an absolute
action coefficient free. In the canonical product algebra the decisive
compatibility identity is
$$0=D[p_{ia},p_{jb}]=i(h_i-h_j)\partial_{ia}\partial_{jb}V.$$
Thus a Newton derivation and a nonzero mixed force derivative force equal
constituent constants on each connected interaction component. The common zero
branch remains admissible. Mechanical angular closure gives a separate
normalization test under faithful constituent observables; spatial covariance
alone permits unequal constants.

The hierarchy begins with reciprocal spring calibration and ends with the
extra phase premise on a spin sphere. Reciprocal forces fix inertia ratios.
A supplied phase constant $K>0$ makes global spin patching require
$2s/K\in\mathbb Z$. Neither the classical model, the algebraic equality nor
the phase ratio selects an absolute nonzero physical $\hbar$. Classical
fluctuation composition has its own probabilistic hypotheses and remains in
its [separate treatment](composition-universality.md).

These are conditional written proofs and established geometric comparisons,
not independent peer review or a claim of literature novelty. In the algebraic
sections $h$ denotes a reduced phase constant: quantum identification would
mean $h=\hbar$ and $h_P=2\pi\hbar$. $K$ in the phase section is supplied,
and equation labels M, A and P distinguish the three premise sets.

## Reciprocal mechanical calibration

### Measured response and reciprocal completion

Let two coordinates $x,y\in\mathbb R$ have the same length units and share
physical time $t$. Suppose their measured equations are

$$\ddot x=-\alpha(x-y),\qquad
\ddot y=\beta(x-y),\qquad \alpha,\beta>0. \tag{M1}$$

Both coefficients have units time$^{-2}$. Isolated free motion would leave
the sectors' positive inertias $m_1,m_2$ independently arbitrary. Now require
the specific mechanical completion

$$L=\tfrac12m_1\dot x^2+\tfrac12m_2\dot y^2
-\tfrac12k(x-y)^2,\qquad k>0. \tag{M2}$$

Here masses have mass units and $k$ has mass/time$^2$ units. This assumes a
diagonal constant kinetic energy and one reciprocal position-dependent
interaction. It is a physical model premise, not a consequence of observing
arbitrary coupled motion. Its forces are $F_1=-k(x-y)$ and $F_2=k(x-y)$.
The Euler--Lagrange equations agree with (M1) exactly when

$$m_1\alpha=m_2\beta=k,
\qquad \frac{m_2}{m_1}=\frac\alpha\beta. \tag{M3}$$

Thus fixed responses admit precisely the positive family
$(m_1,m_2,k)=m_1(1,\alpha/\beta,\alpha)$, with the entries interpreted
in their stated units. Coupling constrains relative normalization; equal
inertias follow only if the two acceleration responses are equal.

### Exchange currents and common scaling

Writing $r=x-y$, the conserved energy and total momentum are

$$H=\tfrac12m_1\dot x^2+\tfrac12m_2\dot y^2+\tfrac12kr^2,
\qquad P=m_1\dot x+m_2\dot y. \tag{M4}$$

Indeed $\dot T_1=-kr\dot x$, $\dot T_2=kr\dot y$, and
$\dot V=kr(\dot x-\dot y)$, so $\dot H=0$; the two forces give
$\dot P=0$. To display an exchange current, assign half the interaction
energy to each sector: $E_1=T_1+V/2$, $E_2=T_2+V/2$. Then

$$\dot E_1=-\tfrac{k}{2}r(\dot x+\dot y)=-\dot E_2. \tag{M5}$$

The half split is an accounting convention; conservation of $H$ is independent
of it. Generic initial data give nonzero exchange. Measuring power in an
independently calibrated energy unit would add information beyond (M1).

For every dimensionless $\eta>0$, replace
$(m_1,m_2,k)$ by $(\eta m_1,\eta m_2,\eta k)$. Equations (M1), all
coordinate histories with the same initial positions and velocities, and
their periods remain unchanged. $L,H,P,E_i$ and the currents in (M5) scale
by $\eta$. So does the trajectory action $S=\int L\,dt$ on any fixed
time interval. Independent rescaling of only one sector generally violates
(M3); common rescaling does not.

An on-shell positive action diagnostic makes this freedom visible without
cancellation in $S$. Set $M=m_1+m_2$, $\mu=m_1m_2/M$ and
$X=(m_1x+m_2y)/M$. Then

$$L=\tfrac12M\dot X^2+\tfrac12\mu\dot r^2-\tfrac12kr^2,
\qquad \omega^2=k/\mu=\alpha+\beta. \tag{M6}$$

In the stationary centre frame choose $r=A\cos(\omega t)$, $A>0$.
With $p_r=\mu\dot r$, its closed-orbit action is

$$I=\frac1{2\pi}\oint p_r\,dr
=\frac12\mu\omega A^2=\frac{E_{\rm rel}}\omega. \tag{M7}$$

The integral follows from $p_r\dot r=\mu A^2\omega^2\sin^2(\omega t)$
over one period. It has action units. Common rescaling sends $I$ to $\eta I$
at fixed trajectory. Even for fixed masses and spring, the admitted small
amplitudes $A\downarrow0$ send $I$ to zero. The full Lagrangian action over
this stationary-centre period is zero because the kinetic and potential
integrals coincide; (M7) must not be identified with that signed integral.

The relative frequency is strictly positive for this fixed two-body model.
The full system also has a free centre coordinate, so it has a zero-frequency
mode. This is a finite-dimensional classical frequency statement, with no
volume or continuum claim and no quantum energy gap.

### Connected networks and the cycle test

The relative mechanism extends to a finite connected undirected graph of
scalar coordinates, all measured in the same length and time units. On every
edge $\{i,j\}$ suppose both directed responses $a_{ij},a_{ji}>0$ are known:

$$\ddot q_i=-\sum_{j\sim i}a_{ij}(q_i-q_j). \tag{M8}$$

Seek only the mechanical class

$$L=\tfrac12\sum_i m_i\dot q_i^2
-\tfrac12\sum_{\{i,j\}}k_{ij}(q_i-q_j)^2,
\qquad m_i>0,\quad k_{ij}=k_{ji}>0. \tag{M9}$$

Comparison of coefficients requires
$m_i a_{ij}=m_j a_{ji}=k_{ij}$. Hence the necessary cycle condition is

$$\prod_{\ell=0}^{s-1}
\frac{a_{i_\ell i_{\ell+1}}}{a_{i_{\ell+1}i_\ell}}=1,
\qquad i_s=i_0. \tag{M10}$$

It is sufficient as well: choose any $m_0>0$, transport masses along a
spanning tree using $m_j/m_i=a_{ij}/a_{ji}$, and apply (M10) on each
remaining edge's fundamental cycle. This makes its transported ratio agree
with the edge ratio. All masses are positive and define the required springs.
Any two solutions have the same mass ratio along every edge; connectivity
makes their quotient one common constant. A disconnected graph instead
retains one constant per connected component.

For a concrete failed test take a triangle with $a_{12}=2\gamma$ and all
other directed edge coefficients $\gamma>0$. The cycle $1\to2\to3\to1$
has product 2. The required ratios would give $m_2=2m_1$, $m_3=m_2$,
and $m_1=m_3$, a contradiction. Such responses cannot have completion (M9).
This rejects that diagonal-inertia reciprocal-spring model; it does not
exclude completions with additional variables or a different kinetic form.

## Constituent algebras and the meaning of rotations

Take finitely many labelled bodies, $i=1,\ldots,N$, with masses $m_i>0$,
three spatial coordinates and three momenta. Assume an associative unital
complex algebra with self-adjoint generators satisfying

$$
[q_{ia},q_{jb}]=[p_{ia},p_{jb}]=0,\qquad
[q_{ia},p_{jb}]=i\delta_{ij}\delta_{ab}h_i1,
\quad a,b\in\{x,y,z\}. \tag{A1}
$$

The scalars $h_i\in\mathbb R$ remain fixed when the body is put in a
composite. Distinct constituent algebras commute. Assume also that the
normally ordered monomials $q^\alpha p^\beta$ are linearly independent:
we retain the full tensor product of canonical polynomial algebras,
including its commutative factors when some $h_i=0$. This is the
precise independence used in coefficient comparisons. Statistical
independence of states is unnecessary; entangled states are allowed.
For unbounded operator realizations all displayed identities are on a
common invariant dense domain representing these polynomials faithfully.

Define, with $\epsilon_{xyz}=1$,

$$
L_{ia}=\sum_{b,c}\epsilon_{abc}q_{ib}p_{ic},\qquad
L_a=\sum_iL_{ia}. \tag{A2}
$$

Each term in (A2) has unambiguous ordering because $q_{ib}$ and $p_{ic}$
commute for $b\ne c$. The additivity and mechanical normalization in
(A2) are hypotheses. Independently rescaling each body's momentum would
change its measured quantity of motion and these hypotheses.

Three distinct requirements can now be stated precisely.

- **Spatial covariance:** the map $q_i\mapsto Rq_i$, $p_i\mapsto Rp_i$
  is an algebra automorphism for every $R\in SO(A3)$.
- **Mechanical closure:** for one real $h$,
  $[L_a,L_b]=ih\sum_c\epsilon_{abc}L_c$ on the full algebra.
- **Mechanical generator identification:** for $h\ne0$, the generator
  $K_a=L_a/h$ satisfies
  $[K_a,q_{ib}]=i\sum_c\epsilon_{abc}q_{ic}$ and
  $[K_a,p_{ib}]=i\sum_c\epsilon_{abc}p_{ic}$ for every body.

The last convention gives
$U(\theta)=\exp(-i\theta K_a)$ and
$U(\theta)^\dagger q_{ib}U(\theta)
=q_{ib}-\theta\sum_c\epsilon_{abc}q_{ic}+O(\theta^2)$,
the usual active rotation of the vector's components about axis $a$.
Integration to a group representation additionally needs a strongly
continuous unitary action with these generators. Lie commutator
identities alone leave those domain and integrability obligations open.
For $h\ne0$, such an action is a representation of $SU(A2)$; descent to
$SO(A3)$ additionally requires a full $2\pi$ rotation to act as the identity.

The orbit-phase premise $e^{iL\theta/h_i}$ yields (A1) only after an additional
canonical observable/quantization prescription. A single orbit's angular
descent condition by itself supplies neither the tensor algebra nor its
mechanical generator identification. The present theorem begins at that
explicit algebraic extension.

## Mechanical closure forces a shared constant

**Theorem 1.** Under (A1)--(A2) and the monomial independence hypothesis,
mechanical closure holds for a scalar $h$ if and only if $h_i=h$ for
all $i$. It suffices to impose the single identity
$[L_x,L_y]=ihL_z$. For $h\ne0$, mechanical generator identification
is also equivalent to $h_i=h$ for all $i$.

*Proof.* The product rule for commutators gives

$$
[L_{ia},q_{jb}]=i\delta_{ij}h_i\sum_c\epsilon_{abc}q_{ic},\qquad
[L_{ia},p_{jb}]=i\delta_{ij}h_i\sum_c\epsilon_{abc}p_{ic}. \tag{A3}
$$

For example, writing $L_{ix}=q_{iy}p_{iz}-q_{iz}p_{iy}$ and
$L_{iy}=q_{iz}p_{ix}-q_{ix}p_{iz}$, their commutator has exactly the
surviving terms

$$
-i h_i q_{iy}p_{ix}+i h_i q_{ix}p_{iy}=ih_iL_{iz}.
$$

Different bodies commute, so closure of the sum is equivalent to

$$
\sum_i(h_i-h)L_{iz}=0. \tag{A4}
$$

The monomial $q_{ix}p_{iy}$ in (A4) occurs only in $L_{iz}$, with
coefficient $h_i-h$. Independence makes that coefficient zero for
each $i$, including a constituent with $h_i=0$. Conversely, equal
constants give closure in all three directions by the same calculation.

For generator identification, (A3) gives, for example,
$[L_x,q_{iy}]=ih_iq_{iz}$, whereas the required action is
$ihq_{iz}$. Independence makes $q_{iz}\ne0$, hence $h_i=h$.
The converse follows directly from (A3). $\square$

A restricted observable space needs the corresponding separation
hypothesis in place of monomial independence: each relation
$\sum_i c_iL_{ia}=0$ must force every $c_i=0$. Compression to a subspace
where all orbital $L_i$ vanish makes closure vacuous for arbitrary
$h_i$. A single orbit, expectation value or rigidly constrained
configuration can likewise lose the necessary separation. The theorem
uses observable identities valid for all admitted preparations and
configurations, with the constituents still individually accessible.

**Transitivity.** Form a graph whose vertices are bodies or species with
persistent constants $h_i$. Put an edge between two vertices when their
full pair algebra is admitted and its mechanical sum is required to
have one closure constant. Theorem 1 gives equality on each edge and
therefore throughout each connected component. Connectedness gives one
constant for the whole class, without assuming that every pair interacts
directly. Disconnected components remain unrelated unless a common
composite or generator condition links them. A context-dependent $h_i$
would require a further preparation-equivalence premise before this
argument could compare contexts.

**Role of three dimensions.** A single planar rotation generator has
$[L_z,L_z]=0$, which tests no normalization. In three dimensions the
non-abelian bracket in (A4) compares the mechanical sums internally.
Requiring the correct action on each $q_i,p_i$ already compares
normalizations in two dimensions by (A3). Three dimensions strengthen
the closure test; generator identification itself needs only one
nontrivial rotation plane.

## Rotation covariance and interaction compatibility

### Covariance with unequal constants

For arbitrary $h_i$, each scalar canonical block in (A1) is rotation
invariant. An explicit associative realization on polynomials is

$$
f*g=\mu\exp\left[\frac i2\sum_i h_i P_i\right] (f\otimes g),\qquad
P_i=\sum_a\left(\partial_{q_{ia}}\otimes\partial_{p_{ia}}
-\partial_{p_{ia}}\otimes\partial_{q_{ia}}\right). \tag{A5}
$$

The exponential terminates on polynomials. The constant derivative
operators commute, so either association of three factors gives the
same exponential of the sum over their three pairings. Each $P_i$ is
invariant under simultaneous spatial rotations. Thus (A5) supplies
covariance for every tuple $(h_1,\ldots,h_N)$.

If all $h_i\ne0$, define

$$
K_a=\sum_i L_{ia}/h_i.
$$

Equations (A3) give $[K_a,K_b]=i\epsilon_{abc}K_c$ (summed $c$)
and the correct rotations of all constituent observables. Concretely,
on $L^2(\mathbb R^{3N})$, $p_i=-ih_i\nabla_i$ yields
$\mathbf K=-i\sum_i\mathbf q_i\times\nabla_i$, which integrates to
simultaneous scalar rotations for arbitrary nonzero $h_i$. The
identification $K_a=L_a/h$ adds exactly the normalization tested in
Theorem 1. With some zero factors, spatial covariance still holds as
an automorphism; commutators with their central observables vanish,
so their rotations require an outer derivation.

### Central interactions and conservation

For classical Newton dynamics about a fixed inertial origin,
$\dot q_i=p_i/m_i$ and $\dot p_i=\sum_{j\ne i}F_{ij}$, the strong central
form of the Third Law is
$F_{ji}=-F_{ij}$ with $F_{ij}$ parallel to $q_i-q_j$. It gives

$$
\dot{\mathbf L}
=\sum_{i<j}(q_i-q_j)\times F_{ij}=0. \tag{A6}
$$

Equal and opposite forces together with centrality do the work here.
Equation (A6) uses neither a commutator nor an action constant. Transferring
this conservation law to the deformed observable algebra needs a
specified evolution law.

**Theorem 2 (conservation propagates equality along interacting pairs).**
Assume (A1), faithful configuration observables on open sets, and a
Hamiltonian

$$
H=\sum_i\frac{p_i^2}{2m_i}+\sum_{i<j}V_{ij}(r_{ij}),\qquad
r_{ij}=|q_i-q_j|. \tag{A7}
$$

Assume commutator differentiation
$[p_{ia},V]=-ih_i\partial_{q_{ia}}V$ on a common domain. This holds
algebraically for polynomial potentials, or on a smooth domain away
from collisions for the coordinate realization. Give time evolution
one fixed nonzero action normalization $h_t$,
$\dot A=[A,H]/(ih_t)$. Require conservation of the mechanical sum
for every admitted pair interaction, with other pair couplings
independently switchable off. For each tested edge require
$V_{ij}'(r_{ij})\ne0$ on some open set allowing
$q_i\times q_j\ne0$. Then conservation forces $h_i=h_j$ on that
edge, and therefore one value per connected interaction component.

*Proof.* The kinetic energies commute with each $L_i$. For one pair,
$\nabla_j V_{ij}=-\nabla_i V_{ij}$, and centrality gives
$(q_i-q_j)\times\nabla_i V_{ij}=0$. Consequently

$$
[\mathbf L,V_{ij}]
=i(h_i-h_j)q_i\times\nabla_i V_{ij}
=+i(h_i-h_j)\frac{V_{ij}'(r_{ij})}{r_{ij}}q_i\times q_j. \tag{A8}
$$

The configuration factor is a nonzero observable on the stated open
set. Conservation, equivalent to $[\mathbf L,H]=0$, forces $h_i=h_j$.
When constants agree on every interacting edge, (A8) proves the converse
conservation statement as well. $\square$

One central harmonic interaction suffices as a polynomial test:
$V_{ij}=k_{ij}|q_i-q_j|^2/2$, $k_{ij}>0$, gives the exact defect
$+ik_{ij}(h_i-h_j)q_i\times q_j$ (the displayed sign includes the earlier correction). This permits full configuration
variation and keeps every step inside the polynomial algebra.
Restriction to collinear configurations or to a pair's fixed
centre-of-mass frame would remove this particular torque test;
conservation about arbitrary fixed origins restores its stated scope.
An external central potential for each isolated body gives no such
exchange test and allows different constants.

Theorem 2 compares the $h_i$ but leaves their common value relative to
$h_t$ undetermined. Demanding the full Newton equations with the
physical Hamiltonian (A7) gives the stronger identities

$$
\dot q_i=\frac{h_i}{h_t}\frac{p_i}{m_i},\qquad
\dot p_i=-\frac{h_i}{h_t}\nabla_i V. \tag{A9}
$$

Requiring $\dot q_i=p_i/m_i$ for unrestricted momenta forces
$h_i=h_t$. This route already assumes a nonzero inner-commutator
clock. Alternatively, assigning each body its own denominator and
retaining all Newton equations must respect the shared product:
for any derivation $D$ with $Dp_{ia}=-\partial_{ia}V$,

$$
0=D[p_{ia},p_{jb}]
=i(h_i-h_j)\partial_{ia}\partial_{jb}V,\qquad i\ne j. \tag{A10}
$$

A nonzero mixed force derivative again equates the constants. This
is the main dynamical result of the note under the displayed derivation premise: it
needs no centrality and no angular momentum, and it holds for every
interacting pair. Equation
(A10) follows by applying the Leibniz rule to the zero cross commutator;
it exposes the compatibility obligation of separate denominators.
The common zero branch satisfies (A10) and supports ordinary classical
Hamiltonian evolution by a Poisson derivation.

## The common zero branch and angular representations

**Corollary (universality and positivity).** Theorem 1 forces a common
real value, with $h=0$ allowed. If one constituent has an independently
established $h_i\ne0$, connected composition propagates its nonzero value
to the entire component. The positivity input lies in that reference
constituent. Theorem 2 likewise permits all $h_i=0$; its commutator
clock then gives trivial evolution. Classical nontrivial dynamics uses
the Poisson bracket instead.

For the common family (A5), all real $h$ give associative algebras.
At $h=0$ the product is ordinary multiplication. Spatial rotations
remain non-abelian: their derivations are
$D_a f=\{f,L_a\}_{\rm P}$, and classical angular momenta obey
$\{L_a,L_b\}_{\rm P}=\epsilon_{abc}L_c$. The Poisson algebra supplies
the rotation structure while the multiplication algebra is commutative.
For polynomial observables the common Moyal family has

$$
\lim_{h\to0}\frac{[f,g]_{*_h}}{ih}=\{f,g\}_{\rm P}. \tag{A11}
$$

Requiring a nontrivial rotation to be implemented specifically by
$\exp(-i\theta L_a/h)$ selects $h\ne0$ in the premise. Its formula
requires division by $h$; classical rotations remain perfectly defined
by their derivations at zero. A strongly continuous unitary rotation
representation alone also leaves this choice open: pullback rotates
classical phase-space functions in $L^2$ using differential generators,
while measured classical angular momenta act by multiplication.

For $h\ne0$, supply self-adjoint angular generators integrating to a
unitary $SU(A2)$ representation. Its irreducible sectors have

$$
J^2=h^2j(j+1),\qquad J_z=hm,\qquad
j\in\{0,\tfrac12,1,\tfrac32,\ldots\},\quad
m=-j,-j+1,\ldots,j. \tag{A12}
$$

Here $J$ denotes total angular momentum, including any supplied
internal spin. To recall the dimensionless argument, put $K=J/h$ and
$K_\pm=K_x\pm iK_y$. Then
$[K_z,K_\pm]=\pm K_\pm$ and
$K_\mp K_\pm=K^2-K_z^2\mp K_z$. In an irreducible unitary sector,
positivity bounds the ladder above and below. Its highest weight $j$
has $K^2=j(j+1)$; the lowest weight is $-j$, so $2j$ is a nonnegative
integer. A full rotation acts by $e^{-2\pi im}=(-1)^{2j}$;
$SO(A3)$ descent retains integer $j$.

For ordinary scalar orbital wavefunctions, $L=q\times(-ih\nabla)$
has integer orbital labels and spherical harmonics. The canonical
angular algebra and this orbital spectrum are standard; see
[Tong, *Quantum Mechanics*, §§4.1.1--4.1.2](https://www.damtp.cam.ac.uk/user/tong/qm/qmhtml/S4.html)
(passage, commutator and spherical-harmonic derivations read).
Half-integer spin requires additional internal degrees of freedom or
an explicitly different state space. The central-force orbital
construction supplies no such degrees of freedom by itself.
If independent spin observables commute with the orbital variables,
requiring $J=L+S$ to rotate those variables still gives (A3), hence the
same orbital universality result. Requiring it also to rotate each
nontrivial spin algebra fixes the spin normalization in the same way.

Equation (A12) supplies dimensionless spectral ratios. The Casimir is
discrete; its factor $j(j+1)$ is integer for integer $j$ and can be
fractional for half-integer $j$. Conditional on fixed $|h|>0$, the
smallest nonzero $J^2$ among all integer sectors is $2h^2$, and among
all $SU(A2)$ sectors it is $3h^2/4$. A chosen representation can omit
these sectors; the scalar sector $j=0$ always remains an allowed
representation. Both spectral factors leave the dimensional value of $h$ free.

More explicitly, rescaling $J\mapsto\lambda J$, $h\mapsto\lambda h$
for $\lambda>0$ preserves the generators $K$, all rotation matrices,
and the integer/half-integer labels. A measured nonzero magnitude
$\ell$ and a known $j>0$ would fix
$|h|=\ell/\sqrt{j(j+1)}$, using that dimensional measurement as input.
With only $\ell$ fixed, unbounded $j$ allows values tending to zero.
Several specified component and Casimir eigenvalues can further
constrain $j$ and their ratios; this constitutes additional spectral
data. The scale freedom of the representation conditions alone remains.

## Relation to fluctuation composition and dimensional selection

The [classical composition note, §§1--3](composition-universality.md)
(full-read) concerns a fluctuation coefficient $\kappa(m)\ge0$ and
independent displacement variances. Its whole-body premise is

$$
\kappa(m_1+m_2)
=\frac{m_1\kappa(m_1)+m_2\kappa(m_2)}{m_1+m_2}.
$$

For all positive masses, $f(m)=m\kappa(m)$ is additive and nonnegative,
hence linear; $\kappa(m)=K\ge0$. A reference constituent then supplies
$K=m_0u_0^2/\lambda_0>0$ under the stated nonzero-speed and finite-rate
premises. The rotation theorem replaces this mass-additivity premise
with mechanical generator identification and separation of constituent
observables. A connected species graph suffices, and arbitrary positive
masses need not be admitted. Both arguments propagate a coefficient;
each obtains positivity only with additional input. Identifying $K$
with the phase constant $h$ remains another physical obligation.

There is an exact parallel in centre and relative variables. Set
$M=m_1+m_2$, $\mu=m_1m_2/M$,

$$
R=\frac{m_1q_1+m_2q_2}{M},\quad r=q_1-q_2,\quad
P=p_1+p_2,\quad p=\frac{m_2p_1-m_1p_2}{M}.
$$

Bilinearity in (A1) gives

$$
\begin{aligned}
{}[R_a,P_b]&=i\delta_{ab}\frac{m_1h_1+m_2h_2}{M},&
[r_a,p_b]&=i\delta_{ab}\frac{m_2h_1+m_1h_2}{M},\\
[R_a,p_b]&=i\delta_{ab}\frac{\mu}{M}(h_1-h_2),&
[r_a,P_b]&=i\delta_{ab}(h_1-h_2).
\end{aligned} \tag{A13}
$$

Thus canonical independence of the centre and relative algebras forces
$h_1=h_2$. The classical note has the corresponding covariance
$\operatorname{Cov}(\Delta R,\Delta r)=\Delta(\kappa_1-\kappa_2)/M$;
for its Gaussian preparations vanishing covariance gives statistical
independence. Equation (A13) concerns commuting observable algebras,
which can carry correlated or entangled states. The two independence
premises have distinct meanings despite their matching coefficients.

The [fifth-postulate note](principia-fifth-postulate.md) (full-read)
places these results as follows. Its Theorem B obtains a single Moyal
constant under full affine symplectic covariance. Applying that premise
to the combined phase space already includes transformations mixing
bodies, including (A13), whereas separate one-body covariance allows
one constant per factor as in (A5). Theorem 1 isolates a narrower
comparison using physical angular generators; it leaves general
star-product uniqueness to the stronger covariance theorem. Theorem A
retains the common zero and nonzero families under its Newton equations.
Theorems C and E give conditional disturbance and concentration bounds
once $|h|>0$ is supplied. Theorem D records action rescaling. The
Gaussian state restriction of B' supplies its own $\zeta$ in a
commutative algebra; spatial rotations and the present commutator
test leave a relation $2\zeta=|h|$ to an additional premise.

Finally, [the dimensional note, Theorem A](action-unit-dimensional-selection.md)
(full-read) applies to a universal floor $g(c)$ determined by fixed
constants $c_r$. If an action product exists, its form is

$$
g(c)=\left(\prod_r c_r^{a_r}\right)F(\pi_1,\ldots,\pi_s),\qquad
\sum_r a_r d_r=(1,2,-1). \tag{A14}
$$

It reduces to a pure number times the product when the fixed constants
have no independent dimensionless products. Rotation angles, group
structure constants, $j$ and $m$ are dimensionless and add no action
unit to (A14). When the fixed constants admit no action-dimensional
product, Theorem A allows only a zero or infinite universal floor;
dimensionless rotations preserve that conclusion. Treating $h$ as a new independent fixed constant makes
$|h|$ the supplied unit. Deriving a universal $|h|$ from pre-existing
constants instead requires dimensional homogeneity and the same
covariance argument as (A14); angular universality provides no value
for its dimensionless factor or proof of its positivity. For the
fixed $k_e=e^2/(4\pi\epsilon_0)$, $c$ and $G$ of that note, this would
read $|h|=Ck_e/c$. The rotation theorem leaves $C$ undetermined.
A coefficient and the infimum of a specified action observable also
need a proved relation before (A14) can be used as a floor statement.

## Global spin phases

### Classical patches and complete dynamics

Let the spin direction n lie on the unit sphere with polar coordinates
$(\theta,\phi)$. Supply $s>0$ with action units and define

$$\omega_s=s\sin\theta\,d\theta\wedge d\phi,
\qquad \int_{S^2}\omega_s=4\pi s. \tag{P1}$$

For any smooth real Hamiltonian H, define the vector field by
$\iota_{X_H}\omega_s=-dH$. Nondegeneracy gives a unique smooth vector field;
compactness gives its complete flow. Thus s may be any positive real value.
There is no globally defined one-form with derivative $\omega_s$, since the
integral of an exact two-form on the closed sphere would vanish.

Instead use regular north and south potentials

$$\alpha_N=s(1-\cos\theta)d\phi,\qquad
\alpha_S=-s(1+\cos\theta)d\phi. \tag{P2}$$

Each has derivative $\omega_s$. On a simply connected part of the overlap,

$$\alpha_N-\alpha_S=2s\,d\phi=d(2s\phi). \tag{P3}$$

The local actions $S_U=\int[\alpha_U(\dot n)-H(n)]dt$ differ by an endpoint
term. Their fixed-endpoint variations agree, yielding the same global
Hamiltonian equation. The azimuth is not single-valued on the entire overlap;
going around it changes $2s\phi$ by $4\pi s$. This constant ambiguity does
not change the equations. Classical variational consistency requires the
local derivatives to agree, not a globally single-valued real action value.

As a concrete clock, take $H=-\Omega s\cos\theta$, where $\Omega$ has inverse
time units. The equation gives $\dot\phi=\Omega$, $\dot\theta=0$. Multiplying
s and H by the same positive factor leaves this physical-time motion intact.

### The additional phase premise

Now supply $K>0$ with action units and ask for phase transport compatible
with the local factors $\exp(iS_U/K)$. On the overlap the transition phase,
up to convention for its inverse, is

$$g_{NS}(\phi)=\exp(i2s\phi/K).$$

This must be single-valued when $\phi$ advances by $2\pi$. Hence

$$\exp(i4\pi s/K)=1
\quad\Longleftrightarrow\quad \frac{2s}{K}\in\mathbb Z. \tag{P4}$$

The same condition follows by spanning a closed loop with a surface: two
spanning surfaces differ by an integer number of spheres, so their geometric
actions differ by $4\pi s$ times an integer. Equation (P4) makes the exponent
independent of this choice. For open paths the transport is a map between
endpoint phase fibres, rather than a gauge-independent scalar.

The extra premise is a U(P1) phase with curvature proportional to
$\omega_s/K$. Equation (P4) is its compatibility condition. The classical
symplectic form alone supplies no such phase, no interference rule and no K.
Prequantization also leaves further state-space and measurement choices open.

### Common scaling, local caps and coupled spheres

**Common rescaling.** If (s,H,K) satisfies the classical and phase conditions,
so does $(\eta s,\eta H,\eta K)$ for every $\eta>0$. Both the Hamiltonian
flow and the dimensionless phase remain unchanged. Thus even phase
consistency fixes a ratio rather than an absolute dimensional constant.

**Local contraction.** With H=0, the geometric action around a latitude
bounding a north-pole cap is

$$A(\theta_0)=2\pi s(1-\cos\theta_0)\longrightarrow0
\quad(\theta_0\downarrow0). \tag{P5}$$

These are trial loops, not nonconstant solutions for H=0. They test local
action resolution: quantization of the total sphere flux allows arbitrarily
small nonzero cap actions. It does not impose a minimum polygonal cell or
invalidate ordinary time subdivision. At fixed K and s>0, (P4) instead
restricts the allowed total sphere area, giving $s\ge K/2$ in that family.

**Two coupled spheres.** Take the product with form
$\omega_{s_1}\oplus\omega_{s_2}$ and any smooth interaction, for example
$H=J n_1\cdot n_2$ with J in energy units. It defines complete classical
dynamics for arbitrary $s_1,s_2>0$, including $s_2/s_1=\sqrt2$.
A common prequantization phase constant would require

$$2s_1/K=m_1,\qquad 2s_2/K=m_2,
\qquad m_1,m_2\in\mathbb Z_{>0}. \tag{P6}$$

Restriction to each sphere with the other held fixed proves these necessary
conditions; product transition functions make them sufficient for this
prequantization construction. Thus $s_2/s_1=m_2/m_1$ must be rational.
Classical coupling admits the irrational example, while a single-K phase
bundle excludes it. The exclusion comes from the added phase structure,
not from a failure of reciprocal Hamiltonian mechanics. Even a permitted
rational ratio leaves infinitely many choices obtained by K replaced by K/n.

## Source boundary for spin patching

F. Bonechi, A. S. Cattaneo and M. Zabzine, *Geometric quantization and
non-perturbative Poisson sigma model*, Advances in Theoretical and Mathematical
Physics **10**, 683--712 (2006),
[arXiv:math/0507223v3](https://arxiv.org/abs/math/0507223v3),
explicitly attributes its integrality condition to requirements on a path
integral. Coverage here: one discovery query and its arXiv abstract; no
full-proof or exact sphere-formula audit. The local potentials, variational
patching and tests (4)--(6) are written out above. The source was not read for the exact sphere formulas; those calculations
are the displayed written derivation, with no independent review or novelty
claim.

## Consequence for STATE

A connected reciprocal network fixes compatible mass ratios; canonical Newton
derivations or mechanical rotation closure equate constituent algebra constants;
a common spin phase imposes an integral ratio. These implications retain their
different premises. Their common scale freedom, the classical zero branch and
arbitrarily small local cap actions survive. Identification of a universal
nonzero physical $\hbar$ still needs independent physical preparation,
state/dynamics and calibration laws.
