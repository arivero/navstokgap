# A conditional operational model of finite-dimensional quantum mechanics from one universal action constant

**Status — a complete model conditional on stated kinematic and operational
premises, not a derivation of those premises.**  This note makes workstream
E independent of the Yang--Mills programme.  It assembles a finite-degree-
of-freedom, nonrelativistic quantum model with canonical kinematics,
normal states, Born probabilities, unitary dynamics, composite systems and
quantum-limited Gaussian records.  It also records exactly what the model
does **not** derive: a positive action constant, the Weyl noncommutative
kinematics, the universality of that constant, or a relativistic quantum
field theory.

The distinction matters.  The record-cost and Gaussian-state results of
the repository can conditionally yield a positive record constant $h_*$.
They do not force a noncommutative observable algebra: a commutative
Gaussian state restriction has the same affine record floor.  Conversely,
the Moyal/Weyl construction supplies standard quantum kinematics once its
central action constant is given, but does not explain why nature chooses
its nonzero value.  A foundations model must display both inputs instead
of calling either one a proof of the other.

The construction is for $n<\infty$ canonical degrees of freedom.  Its
field-theoretic and relativistic extensions are stated as obligations in
Section 10, not silently assumed.

## 1. The target and the action calibration

Let $V=\mathbb R^{2n}$ carry the standard symplectic form
\[
 \sigma((q,p),(q',p'))=q\mathbin\cdot p'-p\mathbin\cdot q'. \tag{1}
\]
The target is a model $\mathsf Q_{\hbar}(V)$, for one $\hbar>0$, in which

1. canonical translations have the Weyl multiplier determined by
   $\sigma/\hbar$;
2. states give positive probabilities and regular irreducible kinematics
   are unitarily the Schrödinger ones;
3. closed systems evolve by self-adjoint Hamiltonians and measurements by
   completely positive instruments;
4. independent systems compose by tensor product with the *same*
   $\hbar$ when they are allowed to interact; and
5. a resolved position record of rms imprecision $s$ produces at least
   $\hbar^2/(4s^2)$ of unconditional momentum noise in an explicit
   quantum-limited model.

The empirical calibration which connects this model to the Planck and
record programmes is an added premise,
\[
 \boxed{\qquad h_*=\hbar=\frac{h_P}{2\pi}.\qquad}           \tag{2}
\]
Here $h_*$ is the conditional record constant of
[the Newton routes](newton-indeterminacy-routes.md), $h_P$ is Planck's
experimentally normalized constant, and $\hbar$ is the central action
constant in the model below.  The SED/radiation discussion provides one
conditional route to (2), but neither it nor dimensional analysis proves
(2).  The gauge-theory use of the same canonical $\hbar$ is described
separately in [the UV/IR note](uv-halving-ir-confinement.md) §3c; no
Yang--Mills mass-gap statement is used here.

## 2. The premises: what is assumed rather than derived

The model uses the following premises.  Their separation is intentional.

**F0 (positive calibrated action).**  A universal $\hbar>0$ is supplied,
with the empirical identification (2) if a numerical value is wanted.
The record programme may support this only after its own all-record
closure premise is justified.

**F1 (canonical projective kinematics).**  Each finite canonical system
has a regular, irreducible projective representation of phase-space
translations whose multiplier is
\[
 W(z)W(z')=e^{-i\sigma(z,z')/(2\hbar)}W(z+z'),
 \qquad W(z)^*=W(-z).                                        \tag{3}
\]
Regular means that $t\mapsto W(tz)$ is strongly continuous.  This is the
operational denial of classical joint determinacy.  Equivalently, one may
start from the associative, affine-symplectic-covariant Moyal product of
[the fifth-postulate note](principia-fifth-postulate.md) and require a
regular positive representation of its Weyl exponentials.

**F2 (positive state and effect calculus).**  Preparations are normal
positive states, and an effect is an operator $0\le E\le1$.  The
probability of its yes outcome is the state evaluated on $E$.  This is the
Born probability rule in $C^*$-algebraic form; it is not inferred from the
record floor.

**F3 (closed-system dynamics).**  A specified physical Hamiltonian is
self-adjoint and acts by $\rho\mapsto e^{-itH/\hbar}\rho e^{itH/\hbar}$.
For a particle, $H=P^2/(2m)+V(Q)$ is admitted only on a domain on which it
is self-adjoint.  This premise chooses the Schrödinger time law; the
existence of an action unit alone does not do so.

**F4 (operational closure of records).**  A measurement with outcomes
$r$ is a normal completely positive (CP), trace-nonincreasing map
$\mathcal I_r$ on states, with $\sum_r\mathcal I_r$ trace preserving.
Sequential records compose by composition of these maps, including the
physical memory of earlier outcomes.  This is the exact mathematical
closure missing from a prior-only classical posterior restriction.

**F5 (composition and interaction).**  Independent systems compose as
tensor products, their canonical phase spaces as symplectic direct sums,
and an allowed nonzero mixed interaction is required to have one
mechanical rotation/generator normalization.  The last clause is the
universality premise used in
[the rotation-composition result](rotation-composition-universality.md);
it rules out independent action constants in an interacting connected
class.

F1 is the specifically quantum premise.  F0 plus a classical state
restriction can reproduce part of the record phenomenology without F1.
Conversely, the larger Moyal/covariant algebraic family from which F1 is
selected retains a commutative $\hbar=0$ branch unless F0 excludes it.  A
physical foundation therefore needs both a nonzero selection principle and
a kinematic reason for the Weyl class.

## 3. The Weyl algebra and finite-system reconstruction

Define $\mathcal W_{\hbar}(V,\sigma)$ to be the unital $C^*$-algebra
generated by unitaries $W(z)$ obeying (3).  The phase in (3) is a
2-cocycle because bilinearity and antisymmetry of $\sigma$ give
\[
 e^{-i\sigma(z,z')/(2\hbar)}
 e^{-i\sigma(z+z',z'')/(2\hbar)}
 =e^{-i\sigma(z',z'')/(2\hbar)}
 e^{-i\sigma(z,z'+z'')/(2\hbar)}.                           \tag{4}
\]
Thus the product is associative before a representation is chosen.

For the standard Schrödinger representation on
$\mathcal H=L^2(\mathbb R^n,dq)$, set
\[
 (Q_j\psi)(q)=q_j\psi(q),\qquad
 (P_j\psi)(q)=-i\hbar\,\partial_{q_j}\psi(q),              \tag{5}
\]
on the usual dense domain, and
\[
 W(q_0,p_0)=\exp\!\left[\frac{i}{\hbar}(p_0\cdot Q-q_0\cdot P)\right]. \tag{6}
\]
The Baker--Campbell--Hausdorff formula applies because the commutator of
the two linear exponents is central, and proves (3).  Differentiating the
one-parameter groups gives
\[
 [Q_j,P_k]=i\hbar\delta_{jk}1.                              \tag{7}
\]

**Theorem 1 (finite canonical reconstruction).**  Under F1, every regular
irreducible representation of (3) for finite-dimensional nondegenerate
$(V,\sigma)$ is unitarily equivalent to (5)--(6).  Under F2, every normal
state is represented by a density operator $\rho\ge0$,
$\operatorname{Tr}\rho=1$, and every effect has probability
\[
 \Pr_\rho(E)=\operatorname{Tr}(\rho E).                     \tag{8}
\]

*Proof.*  The first statement is the Stone--von Neumann theorem applied
to the regular irreducible Weyl relations.  The second is the standard
normal-state duality for $B(\mathcal H)$: positivity and normalization
make a normal functional trace class, and applying it to an effect gives
a number in $[0,1]$.  Equation (8) is therefore the probability calculus
specified by F2. $\square$

This is a reconstruction **inside** F1--F2, not a derivation of those
premises.  It nevertheless eliminates an ambiguity often hidden in the
word “quantization”: for finite canonical systems, no inequivalent regular
irreducible realization remains after the multiplier is fixed.

## 4. Relation to the Moyal product and Newtonian mechanics

For suitable phase-space symbols, the Moyal product is
\[
 f*_\hbar g
 =f\exp\!\left[\frac{i\hbar}{2}
 \left(\overleftarrow\partial_q\overrightarrow\partial_p-
       \overleftarrow\partial_p\overrightarrow\partial_q\right)\right]g. \tag{9}
\]
The affine-symplectic associativity/covariance argument in
[the fifth-postulate note](principia-fifth-postulate.md) proves that this
is the unique product in its stated polynomial class, once F1's type of
kinematics is assumed.  Weyl exponentials obey exactly the multiplier
(3), so (9) and the Weyl model are two presentations of the same finite
canonical kinematics.

For $H=p^2/(2m)+V(q)$, the Heisenberg equation is
\[
 \dot A=\frac{i}{\hbar}[H,A].                               \tag{10}
\]
It gives $\dot Q=P/m$ and $\dot P=-V'(Q)$ exactly.  For a
quadratic $H$, the Moyal bracket is the Poisson bracket for every symbol,
so the complete observable evolution is the classical affine-symplectic
flow.  For nonquadratic $H$, the Wigner-symbol evolution is
\[
 \partial_t f=\{f,H\}_{\rm PB}+O(\hbar^2)                  \tag{11}
\]
where the expansion is meaningful only for a specified regular symbol
class.  Thus ordinary Newtonian mechanics is recovered exactly for the
quadratic cases used in the repository and semiclassically, not
unconditionally for arbitrary singular potentials.

The sign of $\hbar$ is physically redundant at this level: the
anti-symplectic reflection $(q,p)\mapsto(q,-p)$ and complex conjugation
carry $\mathsf Q_{\hbar}$ to $\mathsf Q_{-\hbar}$.  F0 fixes the convention
$\hbar>0$.

## 5. States, uncertainty, and the precise role of the record floor

For a state $\rho$, write
$\Delta_\rho A^2=\operatorname{Tr}\rho(A-\operatorname{Tr}\rho A)^2$.
Positivity of $\operatorname{Tr}(\rho X^*X)$ and (7) give Robertson's
bound
\[
 \Delta Q_j\,\Delta P_j\ge\frac{\hbar}{2}.                 \tag{12}
\]
For Gaussian states with covariance $\Sigma$ on $V$, positivity is
exactly the matrix condition
\[
 \Sigma+\frac{i\hbar}{2}\Omega\succeq0,                    \tag{13}
\]
where $\Omega$ is the coordinate matrix of $\sigma$.  In one degree of
freedom this says $\det\Sigma\ge\hbar^2/4$.  Hence the state-route
constant in the Newton programme is $\zeta=\hbar/2$ and its conditional
record constant is $h_*=2\zeta=\hbar$.

This implication does not reverse from an uncertainty-looking classical
condition alone.  The Gaussian restriction
$\sqrt{\det\Sigma}\ge\zeta$ on a *commutative* phase-space model is affine
symplectic and noise closed and yields the same affine statistical-speed
floor.  Theorem I of [the unit/indeterminacy note](necessity-unit-and-indeterminacy.md)
shows why a prior density ceiling is weaker still: unrestricted classical
instruments can recover arbitrarily concentrated posteriors.  Therefore:
\[
 \text{record floor}\not\Longrightarrow\text{Weyl algebra},
 \qquad
 \text{Weyl algebra}+\text{positive normal states}
 \Longrightarrow\text{(12)}.                                \tag{14}
\]
This is the required division of labour between the foundations model and
the physical programme selecting its action scale.

## 6. Records as CP instruments: an explicit quantum-limited model

F4 gives a mathematical meaning to “all retained records are admissible”.
A discrete instrument has a Kraus form
\[
 \mathcal I_r(\rho)=\sum_\ell M_{r\ell}\rho M_{r\ell}^*,
 \qquad \sum_{r,\ell}M_{r\ell}^*M_{r\ell}=1.                \tag{15}
\]
Its outcome probability is $\operatorname{Tr}\mathcal I_r(\rho)$ and its
conditional state is that output divided by the probability.  The dilation
of (15) by a unitary on system plus memory provides the physical retained
record; composition of instruments then preserves positivity by design.

For a sharp quantitative benchmark, take one particle and a Gaussian
position measurement of resolution $s>0$.  Its continuous Kraus density is
\[
 M_x=(2\pi s^2)^{-1/4}\exp\!\left[-\frac{(Q-x)^2}{4s^2}\right],
 \qquad \int_{\mathbb R}M_x^*M_x\,dx=1.                    \tag{16}
\]
The output density is the ideal position law convolved with a centered
Gaussian of variance $s^2$, so the added rms position imprecision is $s$.
Ignoring the outcome yields
\[
 \Phi_s(\rho)(q,q')=
 e^{-(q-q')^2/(8s^2)}\rho(q,q').                              \tag{17}
\]
Equivalently it is a random momentum translation with centered variance
$\hbar^2/(4s^2)$.  Therefore, for every input state with finite momentum
variance,
\[
 \operatorname{Var}_{\Phi_s(\rho)}(P)
 =\operatorname{Var}_{\rho}(P)+\frac{\hbar^2}{4s^2},
 \qquad
 s^2\!\left[\operatorname{Var}_{\Phi_s(\rho)}(P)-
 \operatorname{Var}_{\rho}(P)\right]=\frac{\hbar^2}{4}.    \tag{18}
\]

**Proposition 2 (a closed record model at the quantum limit).**  Equations
(15)--(18), together with tensor-product memories, define a sequentially
composable record model whose Gaussian position records attain the
noise--disturbance product $\hbar^2/4$.  In this model a later measurement
of a pointer's conjugate observable is another CP instrument on that
pointer; it cannot be treated as passive classical conditioning on a
pre-existing sharp joint $(q,p)$ value.

*Proof.*  The Gaussian integral gives the normalization in (16) and (17).
The latter is the characteristic function of a centered Gaussian random
momentum kick of variance $\hbar^2/(4s^2)$, proving (18).  Kraus maps are
CP, their tensor extensions are CP, and compositions of CP maps are CP.
The final assertion follows from (7) for the pointer pair. $\square$

This does not assert that every laboratory instrument is Gaussian or
minimal.  It supplies one complete, composition-closed model realizing
the constant that the classical record programme needs.  The harder
physical question is whether independent non-quantum premises compel this
instrument class or its all-instrument analogue.

## 7. Dynamics and the Schrödinger law

Under F3, Stone's theorem supplies a strongly continuous unitary group
$U_t=e^{-itH/\hbar}$ for self-adjoint $H$.  For a density state,
\[
 i\hbar\,\dot\rho=[H,\rho],
 \qquad \rho_t=U_t\rho_0U_t^*.                              \tag{19}
\]
For a pure state $\rho=|\psi\rangle\langle\psi|$, choosing its phase
continuously gives the Schrödinger equation
\[
 i\hbar\,\partial_t\psi=H\psi.                              \tag{20}
\]
The phase is physically immaterial at the density-operator level.  The
usual conservation laws follow when the corresponding self-adjoint
generator commutes with $H$ on a common invariant domain.

Equations (19)--(20) are not produced by an uncertainty relation alone.
They need F3, just as a classical stochastic covariance floor needs a
specified dynamical and readout law.  This avoids the false foundational
inference “positive action plus probability automatically gives
Schrödinger evolution.”

## 8. Composition and one universal constant

For two independent systems, use
\[
 \mathcal H_{12}=\mathcal H_1\otimes\mathcal H_2,
 \qquad W_{12}(z_1,z_2)=W_1(z_1)\otimes W_2(z_2),             \tag{21}
\]
which is the Weyl algebra of
$(V_1\oplus V_2,\sigma_1\oplus\sigma_2)$ when the two systems use the same
$\hbar$.  Product states are a special case of normal states; entangled
normal states are allowed.  Local instruments act as
$\mathcal I\otimes\operatorname{id}$, which makes no-signalling for
unconditioned local records immediate from trace preservation.

Abstractly, separate Moyal/Weyl factors can be written with constants
$\hbar_i$.  F5 removes that freedom for a connected interacting class:
the mechanical rotation/generator consistency result in
[the rotation note](rotation-composition-universality.md) proves that a
nonzero mixed interaction derivative forces $\hbar_i=\hbar_j$.  By a
connected interaction graph, all systems in the component share one
constant.  The theorem does not select its value and does not connect
components that never interact; those are physical universality premises,
not algebraic consequences.

## 9. The finite-model theorem and its exact status

**Theorem 3 (conditional finite nonrelativistic quantum model).**  Assume
F0--F5 for every system in an interacting connected class of finite
canonical degrees of freedom.  Then:

1. each irreducible regular one-system kinematics is the Schrödinger Weyl
   representation (5)--(7), unique up to unitary equivalence;
2. normal preparations and effects obey the Born rule (8), and Gaussian
   preparations obey (13) and the uncertainty bound (12);
3. every admitted closed Hamiltonian has unitary evolution (19), with
   pure-state equation (20);
4. records are sequentially composable CP instruments, and the explicit
   Gaussian position record obeys the exact quantum-limit identity (18);
5. composite interacting systems have the tensor-product rule (21) and a
   common $\hbar$; and
6. after the calibration (2), the common constant is the usual canonical
   Planck constant.

*Proof.*  Item 1 is Theorem 1.  Item 2 follows from F2, (7), and
positivity.  Item 3 is F3 plus Stone's theorem.  Item 4 is Proposition 2
and F4.  Item 5 is F5 and the rotation-composition result.  Item 6 is
substitution of F0's calibration. $\square$

The theorem is “full” only in its declared finite nonrelativistic domain:
it produces all standard structural layers of that model from an explicit
list of assumptions, with no unlabelled jump from a record floor to a
Hilbert space.  It is not a reconstruction of quantum theory from
classical mechanics alone.

## 10. What remains a physical foundations programme

The conditional model identifies four noninterchangeable open tasks.

1. **Select $\hbar>0$ physically.**  The radiation/record route must prove
   a composition-closed restriction on all terminal readouts, then justify
   the calibration (2).  A Gaussian bath or thermodynamic record cost alone
   does not yet do this.
2. **Derive or justify F1.**  A record floor has commutative realizations.
   A genuine derivation of quantum kinematics must explain the Weyl
   cocycle, complex amplitudes, and the exclusion of a positive joint
   phase-space state for all canonical observables.  This is the central
   foundations problem, not a corollary of Yang--Mills or the Clay problem.
3. **Extend the instrument premise.**  F4 is a complete operational
   calculus once assumed.  Showing that every physically realizable
   recording process is CP, or deriving CP from a deeper causal/local
   principle without assuming the Hilbert model, remains separate.
4. **Pass beyond finite nonrelativistic systems.**  Stone--von Neumann
   uniqueness fails for infinitely many degrees of freedom.  Relativistic
   locality, gauge constraints, inequivalent representations, particle
   creation, renormalization and gravity require additional axioms and
   construction.  No claim here settles them.

These tasks provide a clean order of attack: first make one
composition-closed physical readout class satisfy the record premise;
then seek a nonclassical kinematic principle selecting F1; only then
extend the finite model to fields.  The independent Yang--Mills programme
may use the calibrated $\hbar$ but neither supplies nor is supplied by
Theorem 3.

## 11. Consequence for STATE

The repository now has a precise candidate for the **target** of the
Newton/Planck foundations programme: not merely an action floor, but the
conditional operational model $\mathsf Q_{\hbar}$ of Theorem 3.  Its
mathematical assembly is complete under F0--F5.  Its physical foundation
is not complete: F0's universal positive scale, F1's noncommutative Weyl
kinematics, and F4's physical closure of records remain named premises.
This separation is a result, because it prevents a conditional record
floor or the independent Yang--Mills mechanism from being misreported as
a derivation of quantum mechanics.
