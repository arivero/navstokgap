# Inserting a point, subdividing a cell: how the limit is built

**Result and direction, 2026-09-26.** The user's insertion
$(t_0,t_1,t_2,t_3)\mapsto(t_0,t_1,t_2,t_{2.6},t_3)$ identifies the
right local question: after adding a variable, how are the old
observations and the dynamics recovered? For Galileo's constant force,
eliminating the new point gives an exact composition law and an explicit
action correction. A summable-defect lemma then constructs a limit
independent of the sequence of insertions. In $1+1$-dimensional pure
Yang--Mills, a heat-kernel convolution gives exact consistency under
inserting an edge. In $1+2$ and $1+3$ dimensions the corresponding
integration produces interactions among several boundary variables;
their control is the renormalization problem.

This is a constructive development of the
[joint-paper plan](three-continuum-limits.md). The elementary proofs
below assemble established ingredients, with no novelty claim. They
produce the constant-force limit and the exact two-dimensional
comparison, and specify sufficient estimates for further limits. The
positive action necessity and the four-dimensional $SU(3)$ gap remain
the two main goals; the pion remains a symmetry benchmark.

**Further result, 2026-09-29 (GPT-6.1 Sol; written, §3b checked by
GPT-6 Astra).**
For the end-kick harmonic polygon, §3b proves a finite Cauchy estimate
uniform over unequal partitions and observation times. A weighted
absolute-value norm supplies stability and telescoping insertion bounds
without assuming the limiting curve. A finite force-balance residual
tends to zero with the same mesh. This develops the specific norm
obstacle exposed by the sister Lean formalization; it supplies no action
floor or measurement law.

## 1. What an insertion has to preserve

Three operations occur at a new time $r$ between $s$ and $t$.

1. A classical calculation adds $q(r)$ and eliminates it by the equations
   of motion, or by stationary action with fixed endpoints.
2. A quantum propagator integrates over an unobserved intermediate
   coordinate: $K(t,s)=\int K(t,r)K(r,s)\,dq(r)$.
3. A physical mark introduces an apparatus and a record. Forgetting
   that record applies the mark's nonselective channel to the body.

Each is a precise composition question. In the third case the
nonselective channel must act as the identity on retained observables
if one is to recover the unmarked dynamics. Trace preservation alone
does not establish that. Thus inserting a variable in a calculation
and inserting an actual measurement have separate refinement laws.

For a gauge lattice, multiplying fine links along an old edge defines
the old holonomy, while integrating the other variables defines its
new probability law. Both the projection of variables and the law must
be specified. A choice of fine variables over a coarse configuration
also needs a conditional distribution; coarse data alone do not choose
that distribution.

## 2. Newton's one-point insertion, with all constants

Take transverse mass $M>0$, force $F$, and a cell of duration
$h=u+v$, split after $u>0$, with $v>0$. This is the symmetric impulsive
construction of the [polygon note](polygon-lift-phase.md), a modern
constant-force realization of the inscribed-chord comparison. It does
not assert that every historical force polygon used this update.

Write a kick and a free drift as

$$K_J(q,p)=(q,p+J),\qquad D_h(q,p)=(q+hp/M,p).$$

The cell map is

$$S_h=K_{Fh/2}D_hK_{Fh/2},\qquad
S_h(q,p)=\left(q+\frac{hp}{M}+\frac{Fh^2}{2M},p+Fh\right).$$

The input momentum is before the first half-kick and the output is
after the last. At a shared vertex the retained momentum is the one
between the two adjacent half-kicks; the incoming and outgoing chord
momenta depend on the partition.

**Proposition 1 (finite classical compatibility).**
$S_vS_u=S_{u+v}$ for every positive $u,v$.

*Proof.* The composed position increment is
$up/M+Fu^2/(2M)+v(p+Fu)/M+Fv^2/(2M)
=(u+v)p/M+F(u+v)^2/(2M)$; the impulses sum to $F(u+v)$.
$\square$

The insertion changes the old endpoint half-kicks as well. Relative to
the old two-kick cell, the impulse changes at times $0,u,h$ are

$$-\frac{Fv}{2},\qquad \frac{Fh}{2},\qquad -\frac{Fu}{2}.$$

Their total and their first time moment vanish. Consequently the old
endpoint position and momentum, with the convention just specified,
are preserved. Adding only the middle kick would describe a different
force history. The new chord slopes change, while retained positions
and the states between half-kicks agree.

The same result can be read directly from a discrete action. Put

$$L_h(x,y)=\frac{M(y-x)^2}{2h}+\frac{Fh}{2}(x+y).$$

**Proposition 2 (eliminating the new point).** For fixed endpoints
$x,y$, the unique minimizer of $L_u(x,z)+L_v(z,y)$ is

$$z_* =\frac{vx+uy}{h}-\frac{Fuv}{2M},$$

and

$$\min_z\{L_u(x,z)+L_v(z,y)\}
=L_h(x,y)-\frac{F^2uvh}{8M}. \tag{1}$$

*Proof.* With $\bar z=(vx+uy)/h$ and $w=z-\bar z$, completing the
square gives

$$L_u(x,z)+L_v(z,y)-L_h(x,y)
=\frac{Mh}{2uv}w^2+\frac{Fh}{2}w.$$

The minimum is at $w=-Fuv/(2M)$ and equals the displayed constant.
$\square$

That constant is independent of the endpoints, so its derivatives do
not change the classical endpoint momenta. It does change the action.
Define

$$\ell_h(x,y)=L_h(x,y)-\frac{F^2h^3}{24M}.$$

Since $h^3-u^3-v^3=3uvh$, equation (1) becomes the exact law

$$\min_z\{\ell_u(x,z)+\ell_v(z,y)\}=\ell_h(x,y). \tag{2}$$

This constructs the corrected endpoint action from finite insertion
compatibility. Two different orders of inserting several points agree:
the correction removed is always
$F^2(h^3-\sum_i h_i^3)/(24M)$. Equivalently, the two-step insertion
correction satisfies the associativity identity
$d(u,v)+d(u+v,w)=d(v,w)+d(u,v+w)$.

Among continuous corrections depending only on the cell duration, the
cubic correction is determined up to $E_{\rm ref}h$: subtracting two
solutions of the insertion equation gives the additive Cauchy equation.
This remaining freedom changes the zero of energy, leaving spectral
differences unchanged. Thus insertion consistency fixes a nontrivial part of
the action while retaining the expected energy-normalization freedom.

For the user's example, if $t_{2.6}$ lies at $3/5$ of the old cell,
then $u=3h/5$, $v=2h/5$. The insertion removes
$3F^2h^3/(100M)$, or $18/25$ of that cell's original cubic correction;
$7/25$ remains. These are exact fractions.

The geometric interpretation stays with Galileo's inertial line and
parabola. At horizontal speed $V$, the triangle between the old chord
and the two new chords has area $VFuvh/(4M)$ for $F,V>0$; multiplying
by $F/(2V)$ gives (1)'s action correction. It is the chord-segment
diagnostic of that comparison, not a Kepler swept sector.

## 3. Quantum composition, and the arbitrary-partition limit

Supply canonical quantum kinematics $[q,p]=i\hbar$, $\hbar>0$, and use
the unitary cell operator

$$Q_h=e^{iFhq/(2\hbar)}e^{-ihp^2/(2M\hbar)}e^{iFhq/(2\hbar)}.$$

Its coordinate kernel has phase $L_h/\hbar$ and free normalization
$(M/(2\pi i\hbar h))^{1/2}$, with the usual positive-time branch.
Completing the same square as in Proposition 2 in the oscillatory
Gaussian integral gives

$$Q_vQ_u=e^{-iF^2uvh/(8M\hbar)}Q_h.$$

The Gaussian normalization composes too: the intermediate integral
contributes $(2\pi i\hbar uv/(Mh))^{1/2}$. Hence

$$U_h=e^{-iF^2h^3/(24M\hbar)}Q_h,
\qquad U_vU_u=U_{u+v}. \tag{3}$$

This is the constant-force propagator, with generator
$p^2/(2M)-Fq$. The scalar correction is measurable as a relative phase
when histories are coherently compared. It cancels from the body-only
channel $\rho\mapsto Q_h\rho Q_h^\dagger$.

For $F\ne0$ this mechanical Hamiltonian on the line has spectrum
$\mathbb R$: unitary translations of $q$ shift it by arbitrary real
constants. The present limit is a unitary evolution over a finite
experiment. Its action-cost question concerns records of that
experiment; the field-theory vacuum spectral gap is a further kind of
statement.

The following finite-to-limit statement also covers situations with an
error instead of an exact scalar correction. It is an elementary
contractive form of a noncommutative sewing argument
([Feyel--de La Pradelle--Mokobodzki 2007](https://arxiv.org/abs/0706.0202),
abstract; the stronger telescoping hypothesis used here is stated and
proved below).

**Theorem 3 (summable insertion defects).** Let $Q(t,s)$ be bounded
operators on a fixed Banach space, $s<t$ in a finite interval, with
$\|Q(t,s)\|\le1$. Suppose for every $s<r<t$,

$$\|Q(t,s)-Q(t,r)Q(r,s)\|
\le C\bigl((t-s)^p-(r-s)^p-(t-r)^p\bigr),\qquad p>1. \tag{4}$$

For a finite partition $\pi$ of $[s,t]$, let $Q_\pi$ be the
chronological product. There exists a unique limit $U(t,s)$ as the
mesh tends to zero, independent of nesting, unequal cell lengths or
insertion order, and

$$\|Q_\pi-U(t,s)\|\le C\sum_{I\in\pi}|I|^p
\le C(t-s)|\pi|^{p-1}. \tag{5}$$

The limit is contractive and satisfies
$U(t,r)U(r,s)=U(t,s)$. If $Q(t,s)$ tends strongly to the identity as
$t\downarrow s$, so does $U(t,s)$.

*Proof.* One insertion changes the full product by at most (4), since
all operators before and after that cell are contractions. Successive
insertions telescope the potential $\sum_I|I|^p$, so for a refinement
$\pi'$,

$$\|Q_\pi-Q_{\pi'}\|
\le C\left(\sum_{I\in\pi}|I|^p-
\sum_{J\in\pi'}|J|^p\right).$$

Two arbitrary partitions have a common refinement, their union.
Their products differ by at most $C(t-s)$ times the sum of their
meshes to the power $p-1$. Completeness gives the limit; refining a
fixed $\pi$ proves (5). Joining partitions on $[s,r]$ and $[r,t]$
proves composition. The one-cell bound
$\|U(t,s)-Q(t,s)\|\le C(t-s)^p$ proves the final assertion.
$\square$

For constant force, $|e^{ix}-1|\le|x|$ gives (4) with
$p=3$ and $C=F^2/(24M\hbar)$. Thus, for duration $T$,

$$\|Q_\pi-U_T\|
\le\frac{F^2T}{24M\hbar}|\pi|^2. \tag{6}$$

This is a constructed arbitrary-partition limit. The analogous estimate
for a general nonlinear force needs a suitable domain and stability
norm; unbounded commutators need not satisfy (4) in operator norm.
The constant-force proof does not silently supply that extension.

Neither (2) nor (3) determines a universal action unit. The classical
composition is exact, and the quantum composition works at every
supplied $\hbar>0$. For the Newton necessity goal, the new question is
which independently justified physical record or optical law selects
the quantum composition structure and a common positive normalization.
Refinement of unobserved intermediate variables already works at fixed
$\hbar$; an action floor concerns the physical records, not a failure
of (6).

## 3b. Harmonic polygons: a finite refinement bound from a different norm

The sister repository's
[Proposition I realization graph](https://github.com/arivero/newtonlean/blob/381d5e9/research/PROP_I_REALIZATION.md)
and [HarmonicStability](https://github.com/arivero/newtonlean/blob/381d5e9/NewtonLimitDynamics/Polygon/HarmonicStability.lean)
(local full-read at commit `381d5e9`) separate finite stability from
convergence of force-generated polygons. The equal-cell quadratic
invariant is proved there; a norm inequality in the represented-fraction
arithmetic is a pending formalization step. The following written
argument uses a weighted sum of absolute values instead. It has not
been formalized in that repository and imports no trajectory or ODE
existence theorem.

Use its **end-kick** convention, distinct from §2's half-kicks. In one
coordinate, acceleration is $a(x)=-wx$, with $w\ge0$, and a cell of
duration $h$ first drifts and then applies the force at the new position:
$$A_h\binom{x}{v}
=\begin{pmatrix}1&h\\-wh&1-wh^2\end{pmatrix}\binom{x}{v}.
\tag{6a}$$
For several coordinates apply the same map to each coordinate pair.
Choose $\rho>0$ with $w\le\rho^2$ and define
$\|z\|_\rho=\rho\sum_i|x_i|+\sum_i|v_i|$. Let
$A_\pi=A_{h_n}\cdots A_{h_1}$ for a finite positive partition of
$[0,\tau]$, and assume $\rho|\pi|\le1$.

**Proposition 3b (finite harmonic refinement control).** Put
$B_\tau=e^{\rho\tau}$. Every such partition satisfies
$\|A_\pi\|_\rho\le B_\tau$. If $\pi'$ refines $\pi$, then
$$\|(A_{\pi'}-A_\pi)z\|_\rho
\le wB_\tau\left(\sum_{I\in\pi}|I|^2
                    -\sum_{J\in\pi'}|J|^2\right)\|z\|_\rho.
\tag{6b}$$
For any two admissible partitions of the same interval,
$$\|(A_\pi-A_\sigma)z\|_\rho
\le w\tau B_\tau(|\pi|+|\sigma|)\|z\|_\rho.
\tag{6c}$$
If $\rho\tau<1$, each occurrence of $B_\tau$ in these bounds may
instead be replaced by the rational expression $(1-\rho\tau)^{-1}$.
Thus on that window the proof uses only finite arithmetic, order and
absolute-value inequalities when the data are rational.

*Proof.* In scaled coordinates $(\rho x,v)$ the absolute column sums
of $A_h$ are $1+wh/\rho$ and $\rho h+|1-wh^2|$. Since
$wh^2\le1$, both are at most $1+\rho h$. The triangle inequality
therefore proves $\|A_h\|_\rho\le1+\rho h$. Multiplication gives
$\|A_\pi\|_\rho\le\prod_j(1+\rho h_j)\le e^{\rho\tau}$.
For $\rho\tau<1$, expand the finite product: its degree-$r$
elementary symmetric coefficient is at most $(\rho\tau)^r$.
The finite geometric sum is at most $(1-\rho\tau)^{-1}$. This
alternative bound applies to every subproduct too.

For a split $h+k$, direct multiplication gives
$$\begin{aligned}
\Delta x&=-whk(x+hv),\\
\Delta v&=whk\,v+w^2hk^2(x+hv),
\qquad\Delta=(A_kA_h-A_{h+k})z.
\end{aligned}\tag{6d}$$
The absolute column sums of the scaled difference matrix are
$$whk(1+wk/\rho),\qquad whk(1+\rho h+whk).$$
They are at most $2whk$: use $w\le\rho^2$ and
$\rho h+\rho k\le1$, which also gives
$\rho h+whk\le\rho h+\rho^2hk\le1$. Thus
$\|A_kA_h-A_{h+k}\|_\rho\le2whk$
$=w[(h+k)^2-h^2-k^2]$.
Multiplying by all the earlier and later cell maps costs at most
$B_\tau$; their combined duration is at most $\tau$. Successive
insertions telescope the sum of squared cell lengths, proving (6b).
For arbitrary $\pi,\sigma$ use their finite union as a common
refinement and $\sum h_j^2\le\tau|\pi|$, proving (6c).
$\square$

The estimate also controls the actual polygon between vertices.
At a time $t$ inside a cell, let $u$ be its elapsed duration and let
$\pi_t$ consist of the completed cells followed by $u$ (omit a zero
cell). The comparison state $z_\pi^\dagger(t)=A_{\pi_t}z_0$ has
exactly the polygon position; its velocity includes a partial kick
that the actual polygon has not yet received. For the actual state
$z_\pi(t)$, take the outgoing velocity at a completed vertex. Then
$$\|z_\pi^\dagger(t)-z_\pi(t)\|_\rho
=wu\sum_i|x_{\pi,i}(t)|
\le\frac{w}{\rho}|\pi|B_\tau\|z_0\|_\rho.
\tag{6e}$$
Apply (6c) to the two clipped partitions of $[0,t]$, then (6e) twice:
$$\sup_{0\le t\le\tau}\|z_\pi(t)-z_\sigma(t)\|_\rho
\le wB_\tau(\tau+\rho^{-1})(|\pi|+|\sigma|)\|z_0\|_\rho.
\tag{6f}$$
This is a finite uniform Cauchy estimate, including unequal schedules
and retained velocity. Completing the state space would construct a
limit; identifying its force law and its historical geometric enclosure
remain additional steps. No curve was supplied to prove (6b)--(6f).
The norm change supplies a concrete finite input to the graph's P3
obligation, rather than deducing P3 from an area invariant.

There is also a finite input to force identification. Define the
trapezoidal position sum, with no integral presumed,
$$T_\pi(t)=\sum_{j\text{ complete}}\frac{h_j}{2}(x_{j-1}+x_j)
             +\frac u2(x_{\rm last}+x_\pi(t)).$$
The same end-kick construction gives the exact identity
$$v_\pi^\dagger(t)-v_0+wT_\pi(t)
=-\frac w2\left[\sum_{j\text{ complete}}h_j^2v_{j-1}
                       +u^2v_{\rm last}\right].\tag{6g}$$
Indeed $x_j-x_{j-1}=h_jv_{j-1}$ and the kick is $-wh_jx_j$;
subtracting a trapezoid from $h_jx_j$ leaves
$h_j^2v_{j-1}/2$. The partial kick supplies the identical calculation
with $u$. Each departure velocity has absolute sum at most
$B_\tau\|z_0\|_\rho$, and
$\sum h_j^2+u^2\le t|\pi|$. For the actual velocity add the missing
partial kick $wu x_\pi(t)$ from (6e), obtaining
$$\|v_\pi(t)-v_0+wT_\pi(t)\|_1
\le wB_\tau(t/2+\rho^{-1})|\pi|\|z_0\|_\rho.
\tag{6h}$$
The position balance
$x_\pi(t)-x_0=\sum_{j\text{ complete}}h_jv_{j-1}+uv_{\rm last}$
is exact. At $t=0$ all sums are empty; at a completed vertex $u=0$,
so the identities retain the declared outgoing velocity. Thus the
candidate curve family is paired with a vanishing
finite force-balance residual, rather than only a stability estimate.
Passing these sums to a continuous force law and proving the relevant
geometric enclosure remain separate obligations.

**Astra's graph check (2026-09-29).** The printed-stage edges from
Lemma III Cor. 4 to Proposition I record a textual citation. They do
not supply convergence of the generated polygon family: the lemma's
given-curve approximation and the graph's P3 realization have different
inputs. The graph's attached
[sector_ratio_reconstruction](https://github.com/arivero/newtonlean/blob/381d5e9/NewtonLimitDynamics/Polygon/Enclosure.lean)
(local full-read) explicitly assumes lower and upper limits and a
geometric enclosure. Having that formal reference does not discharge
those hypotheses. This check concerns graph metadata and code; the
printed passages retain their existing repository attribution.
Astra checked (6b)--(6h), including the single $B_\tau$ factor
and the partial-cell sign in (6g). The finite estimate supplies P3's
Cauchy input and (6h) supplies force-consistency data; neither silently
closes the graph's limiting geometric or force-identification nodes.
This is an internal mathematical check, separate from Lean compilation.

The user's alternative (2026-09-29) is to obtain surviving quantities
by repeated block renormalization, without presupposing a limiting
physical curve. In this fixed harmonic model the Cauchy bound forces a
limit in the usual real-state completion. It does not establish that
the full body--apparatus state has the same completion when refinement
adds bath and memory variables. For that construction, specify the
retained observables and their blocking maps; §7's consistency estimate
is a distinct route to their limiting laws. A finite area identity
alone establishes neither kind of limit.

Here $w$ has units of inverse time squared and $\rho$ of inverse time;
the norm has velocity units, and every coefficient multiplying it in
(6b)--(6f) is dimensionless. At $w=0$ the insertion defect and all
partition discrepancies vanish exactly. For fixed $\tau,w,\rho$ the
bounds tend to zero with both meshes, independently of their nesting.
Mass enters only through $w$ if a spring force is written $-mw x$.
No action normalization appears. To use this mechanical bound for a
record, its discrepancy must still vanish after whitening by the
complete conditional record covariance, as tested in
[the recording note, §6.3](sed-closure-under-recording.md#63-ideas-supplied-by-the-current-lean-formalization).

## 4. Gauge refinement: geometry, marginalization and reflection

Take a finite oriented lattice $\Gamma$ and a refinement $\Gamma'$.
For an old edge represented by a path of fine edges, define

$$p_{\Gamma'\Gamma}(U)_e=U_{e_1}\cdots U_{e_k},$$

using inverses when an orientation reverses. These maps compose exactly
under further refinements and are gauge covariant: transformations at
the new interior vertices cancel in the product. Holonomies of old
loops are therefore represented exactly on the fine lattice.

For a probability measure the consistency equation is stronger:

$$p_{\Gamma'\Gamma*}\mu_{\Gamma'}=\mu_\Gamma. \tag{7}$$

At finite volume the left side can always be formed. Its effective
Boltzmann weight is the integral of the fine weight over the fibres of
$p$, with the Haar disintegration. This defines an effective action
up to a normalization constant. Equation (7) with a proposed coarse
action is a theorem to prove, not a consequence of having multiplied
the links correctly.

Uniformly halving a $D$-cube produces $2^D$ subcubes: four, eight or
sixteen for $D=2,3,4$. Local subdivisions and anisotropic spacetime
refinements are possible as well, provided neighbouring cells and the
projection maps remain compatible. The uniform grid is a convenient
sequence through a larger refinement problem.

**Time refinement alone versus a field continuum.** At fixed spatial
spacing $a_s$, a Hamiltonian lattice theory has the exact temporal law
$T_{a_s}(t)=e^{-tH_{a_s}/\hbar}$ and
$T_{a_s}(u+v)=T_{a_s}(v)T_{a_s}(u)$. Taking the time step to zero
leaves the spatial cutoff in place. Refining space adds degrees of
freedom and changes the Hilbert space, so Theorem 3 on one fixed space
cannot be applied without comparison maps. An isotropic Euclidean
refinement removes both cutoffs together; an anisotropic route must
also match electric and magnetic normalizations to recover the same
physical speed $c$. This is the additional task in the four-cube
comparison beyond inserting a time in mechanics.

One essential property can be carried exactly. Suppose a fine measure
is reflection positive, $p$ commutes with time reflection $\Theta$,
and every coarse positive-time observable pulls back to a fine
positive-time observable. Then its pushforward is reflection positive:

$$\int\overline{\Theta f}\,f\,d(p_*\mu)
=\int\overline{\Theta(f\circ p)}(f\circ p)\,d\mu\ge0. \tag{8}$$

The support condition on $p$ matters; a block straddling the reflection
plane cannot be assumed to have it. Equation (8) supplies positivity
for an exact blocking map with those properties. Subsequent truncation
of the effective action must preserve it separately.

## 5. The exactly soluble subdivision law in $1+1$ dimensions

Let $G=SU(3)$ with normalized Haar measure. Choose the group metric so
that $-\Delta_G\chi_R=C_2(R)\chi_R$ and
$C_2(\mathbf3)=4/3$. Let $\lambda_2>0$ have units of inverse area and
define the face kernel

$$k_A(U)=\sum_R d_R\chi_R(U)e^{-\lambda_2 A C_2(R)/2}.$$

It is the heat kernel at group heat-time $\lambda_2A$. Character
orthogonality gives the exact convolution identity

$$\int_G k_{A_1}(XU^{-1})k_{A_2}(UY)\,dU
=k_{A_1+A_2}(XY). \tag{9}$$

Indeed, integrating two characters contributes
$\delta_{RS}\chi_R(XY)/d_R$, so their heat exponents add and one
factor $d_R$ remains. When an interior edge splits a face, (9)
integrates out precisely that new edge. Splitting an edge alone uses
invariance of Haar measure under multiplication. These elementary moves
yield (7) for the heat-kernel surface measure with density
$Z^{-1}\prod_f k_{A_f}(U_{\partial f})$.

This is the established lattice-to-continuum construction of
two-dimensional Yang--Mills. Lévy proves subdivision consistency and
constructs continuum random holonomy, including the continuity needed
to extend beyond a nested set of graph edges
([Lévy, *Yang--Mills Measure on Compact Surfaces*, Theorem 1.6.1 and
§§2.5--2.10](https://arxiv.org/pdf/math/0101239), passage).

Here the counterpart of Newton's unequal-time insertion is division
into any two positive areas, $A=A_1+A_2$. The law already knows how
to remove the new variable. It also keeps its coupling parameter:
composition works for every $\lambda_2>0$.

**The spectrum must still be identified.** On a spatial circle of
circumference $L$, a Euclidean duration $t$ has area $Lct$. The
physical Hilbert space is $L^2(G)^G$, the class functions, and the
character expansion gives

$$E_R=\frac{\hbar c\lambda_2L}{2}C_2(R),\qquad
E_1-E_0=\frac23\hbar c\lambda_2L\quad\text{for }SU(3). \tag{10}$$

These are global electric-flux energies. Pure $1+1$-dimensional
Yang--Mills has no propagating transverse gluon, and (10) grows with
$L$. Thus the solved refinement limit supplies neither a finite
infinite-line glueball mass nor the four-dimensional spectrum. Its
value for this programme is the exact composition mechanism and a
spectral problem whose operator and boundary conditions are explicit.

There is a dimensional mass unit
$\hbar\sqrt{\lambda_2}/c$ and a string tension unit
$\hbar c\lambda_2$. The absence of local particle excitations has a
dynamical cause. This corrects the older dimensional claim in
[G07](low-dimensional-mass-gap.md) that no mass unit can be formed in
two dimensions.

**Other $1+1$ gap theories sharpen the comparison.** The Schwinger
model, $U(1)$ gauge theory with one massless charged Dirac fermion, has
an exactly soluble massive local boson
([Schwinger 1962](https://doi.org/10.1103/PhysRev.128.2425), abstract).
Its axial singlet symmetry is anomalous. With several massless
flavours, the spectrum instead includes a massive boson and
$N_f-1$ massless bosons
([Keegan 2015, §3](https://arxiv.org/pdf/1508.01685), passage).
Coleman's theorem also constrains continuous symmetry breaking under
its relativistic $1+1$ hypotheses
([Coleman 1973](https://doi.org/10.1007/BF01646487), metadata).
Thus lower dimension supplies exact theories with real spectral
content, but the four-dimensional pion's symmetry-breaking mechanism
must be checked afresh there. These examples serve the comparison;
they do not enlarge the main proof goals.

## 6. What changes in $1+2$ and $1+3$ dimensions

An interior link of a hypercubic $D$-dimensional lattice borders
$2(D-1)$ plaquettes. In $D=2$ the two-face convolution closes. In
$D=3$ or $4$, integrating a shared link couples four or six incident
plaquettes. The result generally depends on several boundary loops,
rather than on one coarse plaquette with one adjusted coefficient.

There is an exact local representation of this operation. Expand the
face weights in characters. For chosen incident representations, the
link integral is

$$P_{\rm inv}=\int_G\bigotimes_i R_i^{\sigma_i}(U)\,dU, \tag{11}$$

where a reversed orientation uses the dual representation. Haar
invariance and unitarity give $P_{\rm inv}^*=P_{\rm inv}$ and
$P_{\rm inv}^2=P_{\rm inv}$, with $\|P_{\rm inv}\|\le1$.
It is the orthogonal projector onto invariant tensors. In two
dimensions Schur orthogonality gives (9); in higher dimensions the
additional representation labels and invariant tensors carry the
boundary interaction. Formula (11) is an exact finite integration
identity, not a physical transfer-matrix gap.

The analogy with (1) is now precise. Newton's quadratic elimination
adds an endpoint-independent scalar; after the cubic correction, the
same cell law closes. Gauge-field elimination produces an entire
boundary-dependent effective interaction. A continuum argument must
control that interaction and the observables along with the coupling.

Use a dimensionally explicit convention

$$\frac{S_E}{\hbar}=\frac1{4\lambda_D}
\int F^a_{\mu\nu}F^a_{\mu\nu}\,d^Dx,
\qquad [\lambda_D]={\rm length}^{D-4}.$$

In the classical-coupling convention of G07,
$\lambda_D=\hbar g_{\rm cl,D}^2$. The dimensionless lattice coupling
is $g_{\rm lat}^2=\lambda_Da^{4-D}$; in $D=4$ it must also be run
with the cutoff.

| Spacetime | Refinement parameter at fixed physical coupling | Physical gap question |
| --- | --- | --- |
| $1+1$ | $\lambda_2a^2$ | Exact holonomy construction; circle flux spectrum (10) |
| $1+2$ | $\lambda_3a$ | $E_{\rm gap}=C_3\hbar c\lambda_3$, with $0<C_3<\infty$ to prove |
| $1+3$ | $g_0^2(a)$, dimensionless | $E_{\rm gap}=C_4\hbar c\Lambda$, with scale and positive finite $C_4$ to establish |

In $1+2$ dimensions the coupling supplies an inverse length, and the
ultraviolet problem is superrenormalizable. Dimensional analysis fixes
the unit in the table, conditional on constructing the theory; it does
not determine $C_3$ or its sign. At finite physical $L$, the form is
$E(L)=\hbar c\lambda_3 f(\lambda_3L)$, with the large-$L$ limit still
to control. The small-box constant-mode approximation is a distinct
limit from small lattice spacing at fixed box size.

**Source boundary in three dimensions.** Chandra, Chevyrev, Hairer and
Shen construct a renormalized stochastic Yang--Mills--Higgs flow on the
three-torus, locally in its auxiliary stochastic time, allowing possible
finite-time blow-up. Global survival and an invariant measure remain
open in that construction
([2024 paper, introduction](https://arxiv.org/pdf/2201.03487), passage).
It therefore does not establish a finite-volume OS quantum theory or
its physical gap. The earlier
[one-function note](three-dimensional-gap-one-function.md) overstated
this input; its dimensional reduction is conditional on existence.

The Karabali--Nair Hamiltonian approach supplies another mechanism, but
its current-variable kinetic scale must be distinguished from a proved
gap on the full physical Hilbert space
([Karabali--Nair 1996, eqs. (28)--(29)](https://arxiv.org/pdf/hep-th/9602155),
passage). Nair's 2026 treatment presents an outline of a proof and
identifies the gap as open
([*Towards a Proof of Mass Gap in 3d Yang--Mills Theory*](https://arxiv.org/abs/2608.10133),
abstract and introductory passage). The $1+2$ case is a genuine target
with simpler scaling, not a solved theorem to import wholesale.

In $1+3$ dimensions the leading coupling is marginal. Perturbatively,
one blocking step changes it by

$$g_0^{-2}(2a)=g_0^{-2}(a)-2b_0\log2+O(g_0^2(a)),
\qquad b_0=\frac{11}{16\pi^2}\quad(SU(3)).$$

The ultraviolet running sets the scale convention; the gap requires
control through the regime where that expansion no longer suffices.
This is the role of H1 in the existing
[mass-gap map](mass-gap-conditional-theorem.md), with construction and
nontriviality still explicit. The dimension table supplies a hierarchy
of constructive problems rather than an implication from one
dimension's gap to another's.

## 7. What estimate would construct the gauge limit?

Here is a probability counterpart of Theorem 3. Fix a finite physical
box and nested lattices $\Gamma_n$, $a_n=2^{-n}a_0$, with compatible
projections $p_{mn}$, $m>n$. Let $\mu_n$ be probability measures and
use total variation with convention
$\|\mu-\nu\|_{\rm TV}=\sup_A|\mu(A)-\nu(A)|$.

**Proposition 4 (summable consistency errors).** If

$$\|p_{n+1,n*}\mu_{n+1}-\mu_n\|_{\rm TV}\le e_n,
\qquad \sum_{n=0}^\infty e_n<\infty, \tag{12}$$

then $p_{mn*}\mu_m$ converges in total variation as $m\to\infty$
to a probability measure $\nu_n$. These limits are exactly consistent,
$p_{n+1,n*}\nu_{n+1}=\nu_n$, with

$$\|\nu_n-\mu_n\|_{\rm TV}\le\sum_{j\ge n}e_j.$$

*Proof.* Pushforward contracts total variation, so the difference of
the $m$-th and $(m+1)$-st projected measures is at most $e_m$.
The series is Cauchy in the space of finite measures. Limits preserve
normalization and commute with each fixed pushforward. $\square$

The consistent measures define a measure on the inverse limit of
these compact graph-configuration spaces. This is a measure on
generalized holonomies for the chosen graphs. Extending it to physical
continuum fields or all relevant paths, establishing Euclidean
covariance and OS regularity, and proving nontriviality need additional
estimates. A fixed-volume bound in (12) also needs a local version
uniform in the box to support $L\to\infty$.

For $e_n\le C a_n^\alpha$, $\alpha>0$, the tail is bounded by
$Ca_n^\alpha/(1-2^{-\alpha})$. The Newton estimate uses this kind of
summability. In a fixed $D$-dimensional volume, a per-cell contribution
of size $a^{D+\alpha}$ would sum to order $a^\alpha$; obtaining an
actual bound on normalized observables or measures from that power
counting is a separate step. Marginal terms with accumulated logarithms
must first be absorbed into running couplings and counterterms. A
geometrically shrinking cell by itself supplies no summable estimate.

Total variation in (12) is a sufficient, potentially overstrong norm.
A useful implementation can instead bound a separating class of
renormalized local observables and prove tightness in a suitable
topology. The topology, observables and constants must be named. In
higher dimensions unsmeared loop holonomies may themselves require
renormalization, so the bare graph projective limit alone is too weak
a target for the physical theory.

Finally, consistency of measures supplies no energy threshold. To
retain a positive physical gap, carry a uniform large-time bound

$$\langle O^*e^{-t(H-E_0)/\hbar}O\rangle_c
\le K_Oe^{-E_-t/\hbar},\qquad E_->0,$$

for a dense family of reconstructed local vectors, with surviving
finite-energy spectral weight. For the pion benchmark, the preserved
Ward identity and broken-symmetry residue instead require a soft
channel. The [spectral criteria](three-continuum-limits.md) state the
two limiting conclusions. Short-distance consistency and long-distance
spectral control are complementary parts of one construction.

## 8. Consequence for STATE and the final paper

The final paper should be organized around **local insertion laws,
their composition, and the quantity carried through the limit**. The
sequence is now concrete: the Newton action elimination (1), the
arbitrary-partition construction (4)--(6), exact surface subdivision
(9), and the higher-dimensional consistency estimate (12), followed
by the physical spectral or record-cost estimate. Pion physics tests
which symmetries those estimates preserve.

The next bounded field-theory task is **one $1+2$-dimensional blocking
step with its boundary interaction retained**. Start with a subdivided
finite cube and compatible reflection plane; specify its exact
boundary weight via (11), then choose a renormalized local observable
norm in which the difference from a proposed coarse weight can be
bounded. The deliverable is one explicit estimate, with dependence on
$a$, $\lambda_3$ and boundary data, or the exact term preventing that
estimate. Its purpose is to test summability, not to fit the answer to
a one-plaquette action. The small-volume H3 valley-lifting task remains
the separate spectral mechanism to connect to this construction.

For Newton, §3b now supplies finite uniform Cauchy and force-balance
bounds for harmonic end-kick polygons, using a norm that avoids the
sister formalization's pending quadratic norm inequality. Its graph
check separates that forward construction input from the cited
given-curve lemma. The next mathematical step is a limit/enclosure
construction carrying (6h); abandon a proposed identification if it
assumes the curve whose existence is at issue. The physical step is an
explicit refinement rule for
the **joint body and record**, deciding which old records are preserved
and what happens when the new one is forgotten. Test whether its
physical premises force a positive action cost and common scale, with
the unobserved composition (2)--(3) serving as the exact reference.
Assuming canonical quantum kinematics already puts it on the existing
conditional branch. The two goals are advanced by finding and
controlling these concrete maps, with the limit, the surviving scale
and the physical interpretation proved separately.
