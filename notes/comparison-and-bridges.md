# Navier–Stokes and Yang–Mills: comparison and bridges

The two problems share questions about nonlinear fields, scaling, constraints and
uniform estimates. This comparison derives their scaling and dissipation
identities, distinguishes regularity from relaxation and spectral separation,
and specifies what each proposed bridge must transport.

First substantive milestone, 2026-09-05; exposition revised 2026-09-06.

The [definitions](millennium-problem-definitions.md) preserve the official targets;
the [source catalogue](../docs/README.md) provides PDFs and reading scope. Below,
“derived” means an elementary calculation under the stated hypotheses, “cited”
means a result imported from a named source, and “proposed” means a comparison
whose transfer obligations remain to be specified. Source companions record the
versions and passages used.

## 1. Exact targets and unlike meanings of existence

| Feature | Navier–Stokes | Yang–Mills |
| --- | --- | --- |
| Setting | Three spatial dimensions, forward time; whole space or spatially periodic | Four-dimensional quantum spacetime |
| Quantifier | Any admissible initial velocity for A/B; an admissible counterexample for C/D | Every compact simple gauge group |
| External force | Zero for A/B; admissible smooth forcing permitted for C/D | Pure gauge-theory target |
| Required object | Global smooth velocity and pressure, with the specified admissibility | Nontrivial quantum theory with the required axiomatic properties |
| Required extra control | Whole-space energy uniformly bounded in time | Positive, finite lower edge of nonvacuum energy |
| Accepted alternative | Prove one of A–D | Construct the theory and prove its mass gap |

Sources: [F, pp. 1–2](../docs/Fefferman_NavierStokes.pdf) and
[JW, §§3–5](../docs/JaffeWitten_YangMills.pdf).
Fefferman's existence alternatives A/B specify zero forcing; breakdown
alternatives C/D permit admissible forcing. These quantifiers and forcing
hypotheses determine the exact target.

The required evidence concerns smooth deterministic evolution for the fluid and
quantum correlations, reconstruction and spectrum for the gauge theory. Each
bridge must identify which object it transports and how it supplies the target's
remaining structure.

## 2. Equations and the several time variables

Let $x$ denote fluid position and $t$ fluid time. For a smooth unforced fluid,
pressure elimination on whole space with suitable decay, or the standard periodic
pressure convention, gives

$$
\partial_tu=\nu\Delta u-\mathbb P((u\cdot\nabla)u),
\qquad \nabla\cdot u=0,
$$

where $\mathbb P$ is the orthogonal projection onto divergence-free fields.
This pressure-eliminated representation supports the calculations below.

For gauge fields use $y\in\mathbb R^d$, a Lie-algebra-valued connection $A$, an
invariant positive inner product, curvature

$$
F_{ij}=\partial_iA_j-\partial_jA_i+[A_i,A_j],
\qquad D_i=\partial_i+[A_i,\,\cdot\,].
$$

The Euclidean Yang–Mills action in our normalisation is

$$
S(A)=\frac12\int|F_A|^2\,d^dy.
$$

Coupling factors can be restored; this convention fixes the gradient identities
below. Gauge heat flow has the form

$$
\partial_sA=-D_A^*F_A.
$$

It is degenerate along gauge directions. A gauge term yields a parabolic
representative.
[L, equations (1.1)–(1.2), (2.2)–(2.4)](../docs/Luscher_WilsonFlow_1006.4518v3.pdf)
provides the concrete flow and gauge modification. The parameter $s$ is auxiliary.

| Parameter | Meaning | Generator or operation |
| --- | --- | --- |
| $t$ | Fluid evolution time | Nonlinear Navier–Stokes evolution |
| $\tau$ | Quantum real time | Unitary evolution $e^{-i\tau H}$ |
| $r$ | Euclidean physical-time separation | Semigroup $e^{-rH}$, when reconstruction applies |
| $s$ | Gauge heat-flow or Langevin time | Auxiliary deterministic or stochastic evolution |

In a stochastic construction in $d=4$, the noise lives over $(s,y)$: an auxiliary
time and four Euclidean coordinates. The fluid has three spatial coordinates
and its physical evolution time.

## 3. Scaling: a precise common language, unequal criticalities

The following calculations are derived for smooth fields on whole space.
For periodic fields the rescaling changes the box size along with the field.

For fixed viscosity the unforced fluid scaling is

$$
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t).
$$

Each term of the velocity equation gains $\lambda^3$. Changing variables in a
spatial integral gives, in spatial dimension $d$,

$$
\|u_\lambda(t)\|_{L^q}=\lambda^{1-d/q}
\|u(\lambda^2t)\|_{L^q},\qquad
E(u_\lambda(t))=\lambda^{2-d}E(u(\lambda^2t)),
\quad E(u)=\tfrac12\|u\|_2^2.
$$

In $d=3$, the $L^3$ norm is invariant, whereas energy scales as $\lambda^{-1}$.
Concentrating a profile can therefore increase pointwise size while decreasing its
energy. This is the energy-supercritical scaling that a regularity estimate must
address. For a fixed smooth profile also
$\|\nabla u_\lambda\|_2^2=\lambda\|\nabla u\|_2^2$ in three dimensions.

For a connection put $A_\lambda(y)=\lambda A(\lambda y)$. Both the derivative
and commutator contributions give

$$
F_{A_\lambda}(y)=\lambda^2F_A(\lambda y),\qquad
S(A_\lambda)=\lambda^{4-d}S(A).
$$

Thus the classical Euclidean action is scale-invariant in $d=4$: action-critical
in four Euclidean dimensions, alongside the fluid's energy-supercritical scaling
in three spatial dimensions. The effect of quantisation on scaling is a further
question.

Proposed use: identify the norms or observables controlled at each scale, then
derive estimates connecting the relevant solution spaces, measures or spectra.

## 4. Dissipation and curvature: useful structure with different roles

For smooth unforced fluid solutions with vanishing boundary terms, integration by
parts gives

$$
\frac{dE}{dt}=-\nu\|\nabla u\|_2^2,
\qquad
\langle u,(u\cdot\nabla)u\rangle=0.
$$

The cancellation follows by integrating
$u\cdot\nabla(|u|^2/2)$ and using $\nabla\cdot u=0$. The pressure term vanishes
under the same hypotheses. For smooth gauge heat flow the first variation is

$$
\delta S(A)[a]=\langle D_A^*F_A,a\rangle,
\qquad \frac{dS}{ds}=-\|D_A^*F_A\|_2^2.
$$

Both identities hold under the stated regularity and boundary assumptions.
Here $E$ is quadratic in velocity; $S$ is quadratic in curvature, which contains
derivatives and commutators. Navier–Stokes combines viscous diffusion and
energy-conserving advection. For comparison, ordinary $L^2$ gradient descent of
kinetic energy would give $\partial_tu=-u$.

The model distinction is essential. [T, Theorem 1.5 and p. 10](../docs/Tao_AveragedNS_1402.0290v3.pdf)
supplies a cited example with averaged nonlinearity, energy cancellation and
finite-time blowup. A regularity argument must therefore exploit structure
beyond the properties shared with that averaged equation.

There is also a geometric analogy. With $u^\flat$ the velocity one-form,
$\omega=*du^\flat$ is vorticity in three Euclidean dimensions, while gauge
curvature is $F=dA+A\wedge A$. The unforced vorticity equation, obtained by taking
the curl, is

$$
\partial_t\omega+(u\cdot\nabla)\omega
=(\omega\cdot\nabla)u+\nu\Delta\omega.
$$

The stretching term makes nonlinear derivative amplification explicit. Curvature
likewise exposes derivatives and self-interaction, with the additional
nonabelian term $A\wedge A$. A map between the two descriptions must account for
that term and respect the resulting dynamics.

Projection restricts the fluid to a physical incompressibility constraint; a
gauge transformation changes the representative of a gauge orbit. This gives
two analytic tasks to compare: constrained evolution and evolution modulo
redundancy.

## 5. Stochastic quantisation: a concrete but conditional bridge

The schematic auxiliary equation is

$$
\partial_sA=-D_A^*F_A+\text{gauge term}+\text{noise}
+\text{renormalisation terms}.
$$

This schematic display identifies the terms a precise SPDE construction must define.
[C, §1.2, Theorem 1.6, Remark 1.9 and §4](../docs/Chevyrev_StochasticYM_2202.13359v2.pdf)
describes rigorous finite-volume dynamics in dimensions two and three. The solution
framework allows a cemetery state for possible explosion. Invariant measures
and infinite volume appear as further questions in that 2022 review.

The proposed connection is through methods for singular parabolic equations. A
route from auxiliary dynamics to the Millennium target would still have to supply:

1. A well-defined process and an appropriate invariant law.
2. Identification of that law with the intended gauge theory.
3. The required continuum and infinite-volume control, with correct observables.
4. Quantum reconstruction with the required axioms.
5. A gap for the reconstructed physical Hamiltonian.

In this chain, stationarity, reflection positivity and the physical spectral
bound each have their own proof obligation.

## 6. Three different gaps

### 6.1 A finite-box fluid decay rate

Derived diagnostic: take the standard unforced periodic fluid on a box of side
$L$, with periodic pressure and zero mean velocity. Fourier modes have wavevectors
$k=2\pi n/L$. Therefore

$$
\|\nabla u\|_2^2\geq(2\pi/L)^2\|u\|_2^2,
\qquad
E(t)\leq E(0)e^{-2\nu(2\pi/L)^2t}
$$

for as long as the solution is smooth. The Stokes decay-rate gap is
$\gamma_L=\nu(2\pi/L)^2$. It vanishes when $L\to\infty$; constants are zero
modes unless the mean is removed. Whole-space heat flow supplies a useful
comparison: globally smooth evolution with nonzero decay rates accumulating at
zero. The displayed fluid estimate controls low-frequency decay; regularity
also requires control of high-frequency concentration.

### 6.2 An auxiliary mixing gap

Derived distinction: suppose an auxiliary Markov generator $\mathcal L$ has
invariant law $\mu$ and an $L^2(\mu)$ relaxation bound. Replacing it by
$c\mathcal L$, for any $c>0$, keeps $\mu$ invariant because
$\int c\mathcal Lf\,d\mu=0$, while multiplying its relaxation rate by $c$.
Equivalently its semigroup is $P_{cs}$.

The sampling clock can therefore rescale a mixing gap while preserving
equilibrium correlations. Extracting a physical mass requires a physical-time
operator identification. A reversible diffusion conjugate to a Schrödinger-type
operator still requires that identification with the field-theory Hamiltonian.

### 6.3 The quantum gap and physical correlations

Derived spectral consequence: assume a self-adjoint physical $H\geq0$, a unique
vacuum $\Omega$, and a gap $m>0$. Let $\psi$ be a well-defined state orthogonal
to $\Omega$, for example one created by a suitably smeared centred observable.
The spectral theorem gives

$$
\langle\psi,e^{-rH}\psi\rangle
=\int_{[m,\infty)}e^{-rE}\,d\rho_\psi(E)
\leq e^{-mr}\|\psi\|^2,\quad r\geq0.
$$

This is decay in Euclidean physical-time separation $r$, as distinct from
auxiliary relaxation time $s$. An observable constrains the energies to which
it couples. Proving a full spectral gap requires a decay bound for a class of
observables that detects all states under consideration.

In units $\hbar=c=1$, mass has inverse-length units. A fluid decay rate has
inverse-time units, with $\nu$ carrying length-squared/time. Equating their numerical
values requires a physically justified conversion.

## 7. Bridge assessment

| Bridge | Status here | Legitimate use | Missing ingredient for a transfer |
| --- | --- | --- | --- |
| Scaling and control across scales | Derived comparison | Identify what a bound actually controls | Estimates with correct exponents and uniform constants |
| Energy/action monotonicity | Derived identities for smooth fields | Separate conservative transport from dissipation | Coercivity in the needed topology and continuation/limit arguments |
| Vorticity/curvature | Geometric analogy with explicit formulae | Expose derivatives and self-interactions | A map respecting fields, dynamics and observables |
| Constraint/gauge handling | Analytic analogy | Track admissible variables and representatives | Proof that the constraints or quotients correspond |
| Gauge heat flow | Cited auxiliary construction | Compare parabolic smoothing mechanisms | Quantum measure construction and physical spectral information |
| Stochastic quantisation | Cited lower-dimensional results; conditional route | Relate auxiliary dynamics to candidate field laws | Invariant law, reconstruction and all required limits |
| Spectral gap/correlation decay | Derived implication for physical $H$ | Interpret suitable Euclidean correlations | Reconstruction and control of a spectrally sufficient class |
| Finite-box or mixing gap as mass gap | Additional structure required | Identify the operator governing a measured rate | Physical operator identification and survival of limits |

For any regularised spectral calculation use a cutoff label $a$ and box size $L$.
The statement $m_{a,L}>0$ at each fixed pair is weaker than a positive bound in
physical units along a justified continuum and infinite-volume construction.
For example, a dimensionless lattice gap may scale as $a m$ and tend to zero
while a physical $m$ stays positive. Conversely a box-induced gap can disappear.
The construction must specify the order of limits and justify any interchange.

## 8. Applying the comparison

For each toy model, specify its variables and symmetries, its trajectory or state
space, its clock and generator, its scale transformation and its limiting
procedures. Then state the desired estimate and identify which structures it
shares with the companion field problem.

The present [mechanics programme](../research/PROGRAMME.md) starts with
action variations and operational resolution, then moves to operator spectra.
This comparison supplies the transfer questions for that sequence. Its proposed
bridges remain conditional on the listed constructions and estimates; the
Millennium targets remain the full problems in the official definitions.
