# The spin interaction admits no exact finite observable repair

For C127's two-spin Hamiltonian and all Borel preparations, no finite-dimensional
space of bounded real observables containing the original terminal effects
closes under physical time evolution. The obstruction persists for arbitrarily
short time intervals. Thus finitely many extra expectation values cannot
repair this model's exact operational descent.

Q01 finite-repair decision, 2026-09-13. The proof below uses the
[Hamiltonian conventions and flow](hamiltonian-moment-descent.md). Literature
coverage is recorded separately in [B74](../references/batches/B74.md); no novelty claim is made.

## 1. Object and exact closure

Let X=S^2 times S^2, let all Borel probability measures on X be preparations,
and retain the affine local and product effects of C125. Fix J>0 (energy)
and S_A,S_B>0 (action), with Omega_A=J/S_A. The complete Hamiltonian flow
Phi_t of H=J u_z v_z defines the pullback U_t f=f composed with Phi_t.
All observables below are dimensionless; t is physical time, so Omega_A t
is dimensionless. There is no volume, continuum or statistical limit here.

A finite observable repair would be a finite-dimensional real subspace V
of bounded Borel functions on X, compared pointwise, containing 1 and the retained effects,
with U_t V contained in V for every t in an interval about zero. In particular,
V contains u_x and u_y because it contains (1+u_x)/2 and (1+u_y)/2.
The theorem also holds if closure is demanded only on a nonzero forward
interval. The case J=0 has static finite closure and is excluded explicitly.

## 2. An infinite independent time orbit

Set w=u_x+i u_y in the complexification of V. The flow equations give

$$U_t w=w\exp(i\Omega_A t v_z). \tag{1}$$

For any distinct times t_1,...,t_m in the chosen interval, suppose
sum_j c_j U_{t_j}w=0 as a function on X. Restrict to u=e_x and
v=(sqrt(1-z^2),0,z), with -1<z<1. Then

$$\sum_{j=1}^m c_j\exp(i\Omega_A t_j z)=0. \tag{2}$$

Differentiate this identity in z at zero for orders k=0,...,m-1.
The resulting equations are sum_j c_j(i Omega_A t_j)^k=0.
Their Vandermonde determinant is the product over j<l of
(i Omega_A t_l-i Omega_A t_j), which is nonzero. Hence every c_j=0.
There are arbitrarily many independent U_t w, contradicting finite dimension.
This proof requires no smoothness or differentiation of the added observables.

The infinitesimal hierarchy is the same obstruction: on smooth functions,
with Lf={f,H},

$$L^n w=(i\Omega_A)^n w v_z^n,\qquad n\geq0. \tag{3}$$

The functions w v_z^n are independent by the same restriction and polynomial
independence. Equation (1), rather than a formal truncated hierarchy, proves
the full finite-repair claim.

## 3. Why nonlinear updates of finite expectations do not evade the result

Take any finite real observables f_1,...,f_d, together with f_0=1. If the
expectation of g is determined by their expectations for every probability
measure, then g belongs to their real linear span. To see this, if g is outside
that span, finite-dimensional evaluation linear algebra supplies points x_j
and real weights a_j with sum_j a_j f_k(x_j)=0 for all k, but
sum_j a_j g(x_j) nonzero. Indeed, otherwise every linear relation among the
evaluation vectors (f_0(x),...,f_d(x)) would also annihilate g(x), defining a
linear functional on their span and expressing g as a combination of f_k.

Since sum_j a_j=0, the positive and negative weights have the same nonzero
mass M. Dividing the corresponding atomic measures by M gives two admitted
probability preparations with identical retained expectations and different
expectations of g. This proves the assertion by contradiction.

Apply this observation to g=U_t f_k. Even a nonlinear, single-valued update
of the finite expectation vector would force U_t f_k into the retained span.
Section 2 excludes this for a span containing the original effects and all
times in the interval. More generally a finite operational coordinate model
respecting probabilistic mixing is subject to this expectation argument;
arbitrary encodings of whole measures with no affine mixing rule are outside
its scope.

## 4. Strategic consequence

C128 closes the finite-repair alternative for this interaction and preparation
class. Exact closure requires infinitely many independent observables, or a
change in the admitted preparations, effects or dynamics. Infinite observable
dimension alone establishes neither an infinite perfectly distinguishable
capacity nor quantum structure. Finite accuracy and restricted preparations
are different premises requiring their own physical justification.

B70 therefore cannot be invoked for this hidden spin interaction by merely
adding finitely many moments. Both microscopic reversibility and finite local
operational descriptions remain compatible with failure of finite composite
closure. S_A,S_B still supply the mechanical action units; this obstruction
selects no universal positive action parameter. Park further hierarchy and
truncation variants unless a named physical restriction makes one decisive.
