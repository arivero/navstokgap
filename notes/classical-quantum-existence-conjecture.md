# The classical-to-quantum existence conjecture

**Conjecture and scope, 2026-10-27.** Every proof of consistency or
existence of classical mechanics contains a proof of consistency or
existence of quantum mechanics. We interpret this claim constructively:
the mechanical data and estimates that establish the classical theory
should suffice to construct a compatible quantum theory. The universal
claim remains open. For a specified class of smooth scalar potentials,
the [quantum-to-Newton construction](quantum-blocks-construct-newton.md)
already constructs both dynamics and a quantitative classical limit.
Its quantum existence argument uses additional operator theorems; we
have not shown that every classical existence argument supplies their
required hypotheses.

The immediate question is which classical refinement and stability
estimates permit such a construction. Existence of a quantum family for
arbitrary supplied positive action, physical necessity of positive action,
and uniqueness of a quantum completion are separate claims. No general
lifting theorem or independently necessary positive action scale is
proved here. The following formulation and comparison use the maintained
proofs cited below; they make no literature novelty claim.
The subsequent [Lipschitz-certificate lift](lipschitz-certificate-quantum-lift.md)
proves the bounded test in §6 for a specified one-dimensional action
class, using a named operator-theorem toolkit. The universal claim
remains open.

**Targeted advisor check (GPT-6.1 Sol, 2026-10-27): ACCEPT at the
stated scope.** The advisor read this formulation and the bounded
lifting proof. The latter uses the supplied global action and force
bound for quantum refinement, and the classical polygon certificate
for recovery of the classical flow. It does not derive quantum
existence from an arbitrary classical proof. This is an internal model
review, not independent peer review.

## 1. The meaning of containment

A proof may contain mathematical information that its author never
expresses in quantum terminology. Under the conjecture, a construction
of classical motion would also give enough control to construct quantum
evolution from the same mechanical data. A direct classical proof that
never mentions a Hilbert space therefore does not by itself refute this
interpretation. One must determine whether its assumptions and estimates
permit the quantum construction.

Literal textual inclusion would be a much stronger requirement on how
people write proofs. Conversely, appending an unrelated quantum existence
theorem to any classical proof would make containment uninformative. The
intended requirement is an explicit construction whose convergence uses
the classical data and estimates. Fix a named background analytic toolkit
before the test. Every model-dependent hypothesis needed to apply those
theorems must be supplied by the classical inputs or proved from them;
adding a new dynamical restriction would weaken the containment claim.

The word consistency also needs an identified object. Logical
consistency concerns the absence of contradictions in specified axioms.
Existence of a mathematical model can establish relative consistency
within the mathematical foundation used to construct it. Existence of
motion, uniqueness from initial data, continuous dependence, and
continuation for all time are different analytic properties. The present
programme addresses these analytic constructions and their relation to
quantum dynamics. It has not formulated a reduction between formal
arithmetical consistency statements for two axiomatic theories.

The quantum target requires a specified noncommutative quantization of
the mechanical observables, a self-adjoint Hamiltonian, a strongly
continuous unitary evolution, and a relation between that Hamiltonian and
the classical action. For the scalar example, the target uses the
Schrödinger position and momentum representation, with $Q=q$,
$P=-ih\,\partial_q$, the canonical relation $[Q,P]=ihI$ on Schwartz
space and its associated Weyl relations, and the Hamiltonian in (2).
Other action classes must specify the corresponding quantum structure
and correspondence conditions before the lifting test. These are
requirements on the constructed output; assuming them as additional
physical input would leave the conjecture unproved.

A Hilbert-space representation alone would admit a classical example.
For a complete Hamiltonian flow preserving phase volume, the operators
$(U(t)f)(z)=f(\Phi_{-t}(z))$ form a strongly continuous unitary group on
$L^2$ of phase space. Stone's theorem gives a self-adjoint generator;
multiplying it by any $h>0$ writes the same group as $e^{-itH_h/h}$.
Multiplication observables commute, and concentrating probability
packets recover the classical trajectory. This Koopman representation
would satisfy the weaker target without constructing the required
noncommutative quantum observables.

A normalizable vacuum, a spectral gap and relativistic field-theory
axioms are additional requirements. Free motion on the line has a quantum
Hamiltonian and unitary group, although its spectral bottom is not a
normalizable vacuum. A mechanical lifting result would not establish the
continuum existence or mass gap of four-dimensional Yang--Mills.

Throughout, $h$ has action units and denotes the reduced phase constant.
Identification with physical quantum mechanics would set $h=\hbar$;
ordinary Planck action is $h_P=2\pi\hbar$. The time mesh $|\pi|$ is an
independent parameter.

## 2. A testable lifting statement

Fix a class $\mathcal A$ of mechanical actions, their state spaces,
initial or boundary data, and finite refinement rules. A classical
existence certificate means explicit estimates sufficient to construct
the classical dynamics. For a polygon proof these may include a common
bounded region on each finite time interval, a stability estimate and a
force-balance residual tending to zero with the mesh. The admissible
certificates must be specified before testing a proposed lift; defining
them to include quantum convergence would assume the conclusion.

**Constructive lifting conjecture.** Fix the action class, certificate
schema, quantum target and named background analytic toolkit. One
construction procedure for that class takes any admissible mechanical
data and classical certificate as input and constructs a compatible
quantum family $Q_h$ for $h\in E\subset(0,\infty)$ with
$0\in\overline E$. Every model-dependent hypothesis used in the quantum
construction must be supplied by those inputs or proved from them.
The procedure must identify which certificate estimates control quantum
refinement and the recovery of the classical dynamics on the stated
preparations and observables. Additional dynamical restrictions cannot
be introduced to complete the proof.

The proposed interpretation requires a single construction procedure for
the chosen class, rather than a separate unexplained choice for each
certificate. A certificate schema must not exclude a counterexample
after the test begins. A theorem for one class would establish a bounded
lifting result; extending it to every classical existence proof remains
the universal conjecture.

Existence at one isolated $h>0$ cannot itself formulate an $h\to0$
limit. The lifting statement therefore requires a family indexed by
positive values accumulating at zero. Requiring every sufficiently small
positive $h$, or every $h>0$, strengthens that requirement. The current
smooth-potential example constructs the quantum theory for every $h>0$.
This family requirement makes the proposed lifting statement more
specific than a bare assertion that some quantum theory exists.

The word compatible requires an observable statement. In the current
example, fix $z_0$, a finite $T>0$, a time $t\in[0,T]$ and
$a\in C_c^\infty(T^*\mathbb R)$. For the specified coherent preparations
and partition vertices $t_j\to t$, the required limit is
$$
 \left\langle\psi_{h,\pi}(t_j),
       \operatorname{Op}_h^W(a)\psi_{h,\pi}(t_j)\right\rangle
 \longrightarrow a(\Phi_t(z_0)),
 \qquad h,|\pi|\longrightarrow0. \tag{1}
$$
Here $z_0$ is the initial canonical state, $\Phi_t$ the constructed
classical flow, $\psi_{h,\pi}(t_j)$ the state after the first $j$ quantum
cells, and $\operatorname{Op}_h^W$ Weyl quantization. Partitions containing
$t$ permit $t_j=t$. The limit holds along every joint schedule with
$h,|\pi|\to0$. A different action class may require different preparations,
observables and topologies while retaining its specified noncommutative
quantum target. Equation (1) does not require convergence of every quantum
state to a single classical point.

## 3. The smooth-potential instance

The [multiscale construction](quantum-blocks-construct-newton.md),
sections 1--5 (maintained proof read), assumes $m>0$ and
$V\in C^\infty(\mathbb R)$, with $V\ge0$ and bounded derivatives of
every order at least two. Set $L=\|V''\|_\infty$. Those hypotheses give
a globally Lipschitz classical force and define
$$
 H_h=-\frac{h^2}{2m}\frac{d^2}{dq^2}+V(q),\qquad h>0. \tag{2}
$$
The construction establishes a normalized Euclidean bridge law,
the self-adjoint Hamiltonian (2), and arbitrary-partition convergence
of real-time kick--drift products at each fixed $h$. Coherent packet
means form a Cauchy family as $h$ and the mesh vanish jointly, without
assuming the classical trajectory in advance. Their limit is the unique
Newton initial-value solution. The stated quantitative bound is
$$
 \sup_{0\le t\le T}\|z_{h,\pi}(t)-\Phi_t(z_0)\|_\omega
 \le G_T\big(C_\delta|\pi|+C_hh\big), \tag{3}
$$
with the weighted phase-space norm and constants defined in that proof,
equations (17) and (21). They are independent of the number of slices
and of $h\in(0,h_0]$ for fixed $h_0,T$. The sharper $O(h)$ mean term
uses the bounded third derivative already included in the hypotheses
and cancellation of the centered linear force term; packet widths
remain $O(\sqrt h)$. The
[groupoid formulation](groupoid-quantum-newton-states.md), sections 1--3
(maintained proof read), extends the comparison to smooth Weyl observables
and continuous sections of the established quantum/classical field.

The common-hypothesis result has the logical form
$$
 \mathcal H\ \Longrightarrow\
 \big[C\ \text{and}\ (\forall h>0)\,Q_h\
                   \text{ and the stated classical limit}\big]. \tag{4}
$$
$\mathcal H$ denotes the hypotheses just listed, $C$ the classical
existence and uniqueness conclusion, and $Q_h$ the specified quantum
existence conclusion. Equation (4) records a construction of both
theories from common data. It does not establish that the bare assertion
$C$, or every certificate proving $C$, supplies all information required
for $Q_h$.

The [direct polygon proof](balaban-ode-lesson.md), sections 1--3
(maintained proof read), constructs classical motion using stability,
residual bounds and Gronwall. Its hypotheses admit an arbitrary globally
Lipschitz acceleration. The quantum proof additionally specifies a
potential, a Hilbert-space realization and operator domains, and uses
self-adjointness and product convergence. In particular, positivity of
the potential is not needed for the direct classical polygon argument.
The quantum-to-classical comparison then uses the same Lipschitz
stability to control the packet means. The task is to determine which
of these quantum requirements follow from an appropriately specified
classical certificate and which require stronger assumptions.

The quartic extension of the packet construction also has a precise
boundary. It constructs the classical quartic trajectory from quantum
Hamiltonians whose potentials agree with the quartic on a sufficiently
large compact interval. Classical energy conservation prevents escape
from that interval. It does not prove the joint packet estimate for the
uncut quartic quantum Hamiltonian. The separate
[quartic vacuum construction](constructive-qft-one-time.md), sections
2--4 (maintained proof read), establishes its quantum existence and
bounded-cylinder reconstruction.

## 4. The 1998 proposal and phase information

Rivero's [1998 working draft](https://arxiv.org/html/quant-ph/9803035v1)
(full-read, sections 1--4, equations (1)--(10)) proposes
representing a classical variational distribution through oscillatory
functionals. It asks whether convergence of a controlled Feynman
functional is equivalent to existence of the proposed classical
functional-space distribution. The draft leaves its regulator-control
transformation unspecified and permits an arbitrary positive control
constant. This is a particular proposed convergence equivalence; the
claim about every classical existence proof is broader.

The [quartic and central-force tests](rivero-1998-conjecture-central-forces.md),
section 1 and Theorems 1--3 (maintained proof and corrections read),
identify the information that a lifting argument must preserve. At a
fixed finite partition, isolated nondegenerate stationary points $z_a$
of $S_\pi$ give, under the cutoffs and normalization stated there,
$$
 A_{h,\pi}(O)=\sum_a
 \frac{O(z_a)}{\sqrt{|\det S_\pi''(z_a)|}}
 e^{iS_\pi(z_a)/h+i\pi\sigma_a/4}+O_\pi(h). \tag{5}
$$
The signature $\sigma_a$ and the action differences determine relative
phases. The classical critical-point distribution, with weights
$1/|\det S_\pi''(z_a)|$, retains neither those phases nor a rule for
summing amplitudes. The action supplies candidate phases, but convergence
of trajectories alone does not bound the oscillatory sum. With several
branches, the squared amplitude retains interference terms. The quartic
test shows that the unqualified classical-first halved
functional can fail to converge even when the ordinary classical
initial-value problem is well posed. The draft's single-extremum
restriction must be preserved when applying its elementary argument.

The local determinant identity
$$
 \det S_\pi''=\det S_{yy}\,\det S_{\mathrm{eff}}'' \tag{6}
$$
holds when a stationary insertion $y=y_*(z)$ has invertible $S_{yy}$.
It relates the classical elimination weight to the square-root weight
in stationary phase. A possible lifting mechanism would transport these
weights, phases and remainders through refinement. Formula (6) by itself
does not control their infinite composition. The $O_\pi(h)$ remainder
in (5) is a fixed-partition statement and supplies no uniform mesh limit.

Classical endpoint composition also requires care. Hamilton's principal
action composes by stationary elimination on a chosen noncaustic branch.
A global minimum requires separate minimizing hypotheses. Quantum
propagators compose by integration over intermediate coordinates. These
kernel composition laws do not establish that the action is an ordinary
groupoid morphism. The [corrected groupoid formulation](groupoid-quantum-newton-states.md),
section 5 (maintained argument read), keeps geometric deformation, time
refinement and integration of fluctuations distinct.

## 5. Completeness and positive action

Classical incompleteness motivates a stronger physical question. For
attractive Kepler motion, some initial data reach a collision where the
original vector field gives no continuation, whereas the specified
Coulomb quantum Hamiltonian has global unitary dynamics for every
$h>0$. The [self-sufficiency theorem](self-sufficiency-contrast.md),
Theorem 1(a)--(b) and its dated scope corrections (maintained argument
read), establishes this contrast. It establishes neither a contradiction
in classical mechanics nor exclusion of all classical completions.

The [bounded-cusp theorem](newton-cusp-preparation-floor.md), sections
1--4 (maintained proof read), goes further under explicit assumptions.
Canonical covariance, weak closure of preparations and reversible
compatibility with a force that merges full point states imply a positive
covariance action floor. A classical model with a phase-space density
ceiling satisfies those same assumptions through an almost-everywhere
area-preserving flow. Its preparations give no weight to the exceptional
merging trajectories, and it admits no point preparations, so the
point-compatibility condition is vacuous in that model. The floor
therefore remains insufficient to identify quantum mechanics; record
closure and the identification with the phase constant require further
arguments.

Existence of a compatible family $Q_h$ for every $h>0$ leaves all those
positive values available and says nothing by itself about the physical
admissibility of the zero-action theory. Requiring positive action in
nature would need an independently justified condition that excludes
the classical alternative. Universality across systems and calibration
of one physical value are additional obligations. The constructive
lifting conjecture can be investigated before those stronger claims
are decided.

## 6. A bounded test

The test compares the direct polygon certificate with the quantum
product argument for a specified action class. Initially fix
$m>0$, $V\ge0$, the derivative bounds of section 3, the initial data and
a finite duration $T$. Specify the certificate fields as the classical
drift and kick rules, their common bounded region, stability and residual
estimates, with their domains of validity. Fix the allowed background
theorems on closed forms, self-adjoint generators and product limits.
Record explicitly which assumptions on $V$ the classical proof uses and
which it leaves unused.

Define the quantum finite factors from the same kinetic energy and
potential. For fixed $h>0$, a quantum Cauchy criterion is
$$
 \|U_{h,\pi}(T)\psi-U_{h,\sigma}(T)\psi\|_2
 \le r_{h,T,\psi}(|\pi|)+r_{h,T,\psi}(|\sigma|),
 \qquad r_{h,T,\psi}(s)\longrightarrow0. \tag{7}
$$
The subsequent [bounded lifting theorem](lipschitz-certificate-quantum-lift.md)
derives the operator-domain and product estimates from the supplied
conservative action and its global Lipschitz force bound, using the
named Nelson and graph-domain theorems. It actually allows $V\in
C^{1,1}$ without a lower bound. For graph-domain vectors it gives an
explicit $O(|\pi|)$ fixed-$h$ product estimate, and it uses the
classical polygon certificate together with packet-spread bounds to
prove an observable limit such as (1). Fixed-$h$ product convergence
and the joint classical limit remain different estimates; (7) need
not be uniform as $h\to0$.

That theorem concerns the delimited certificate class, rather than
every proof of classical existence. Likewise, nonuniqueness of a
quantum boundary condition does not refute a conjecture asking only
for existence of a compatible quantum theory.

For singular forces, the
[cusp-selection calculation](cusp-quantum-preparation-selection.md)
gives explicit Gaussian families with the same limiting incoming
trajectory and different outgoing branches; their superpositions give
mixtures. This reveals preparation information lost by the point-state
limit without establishing a universal positive action scale.

## 7. Consequence for STATE

The universal classical-to-quantum existence conjecture remains open.
The subsequent bounded theorem supplies one noncommutative construction
from the conservative global-Lipschitz certificate and the named
operator toolkit; the cusp examples show why singular continuations
require more information. Neither result changes the independent
action-necessity and Yang--Mills goals.
