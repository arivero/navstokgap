# Reversible interaction excludes the minimal orientation composite

C125 cannot retain its separable operational state space and admit a continuous
reversible interaction beyond local rotations. This is an application of
Theorem 1 of de la Torre, Masanes, Short and Müller, not a new reconstruction
theorem. Their Theorem 2 selects quantum composition for identical qubits with
local tomography and operational closure. The remaining physical question is
why a mechanical interaction must descend reversibly to this restricted
operational description. No action scale follows from this source audit.

Q01 third milestone, 2026-09-13. [B70](../references/batches/B70.md) records
selected primary passages and the unaudited proof dependencies.

## Assumptions already present in C125

The local state coordinate r lies in the unit ball in R^3. Write

$$\rho(r)=\tfrac12(I+r\cdot\sigma),\qquad E=aI+b\cdot\sigma.$$

Then tr(E rho)=a+b dot r. The local effect constraints in C125 are precisely
positivity and normalization of qubit effects. This is an invertible change
of coordinates, with dimensionless Pauli matrices; no global positive cone
or entangled preparation has been assumed. For n components the same tensor
basis maps C125's moment coordinates to Hermitian matrices. Its joint hidden
measures map exactly to convex mixtures of product density matrices.

| Source hypothesis (PDF pp. 1–2) | C125 and the proposed extension |
| --- | --- |
| Local qubit states and effects | Ball and affine directional effects already supply these |
| Local tomography and product preparations/tests | Already supplied by tensor moments and product tests |
| All local unitary conjugations | Already supplied by SO(3) rotations on each ball |
| Connected linear reversible group larger than the local group | New operational interaction requirement; affine mixture compatibility extends the maps linearly to the unnormalized span |
| Identical systems, spectator extension and relabelling | Arbitrary n and permutations already supplied; any new gate must remain admissible under these operations |
| Ancilla preparation, joint evolution, measurement and discard | Must be imposed when claiming the full quantum measurement/channel conclusion; C125 specified terminal tests |

An interaction of hidden orientations is not automatically an interaction on
these moments. Two hidden preparations with the same moment tensor must remain
operationally equivalent after evolution; the induced map must also have an
allowed inverse. These are the precise descent and reversibility requirements.

## The source theorem and the exclusion

Theorem 1 assumes a connected linear group containing local unitaries and
valid probabilities for every product preparation followed by a group element
and a product test. If that group is larger than the local group, its action
on a pair with fixed product spectators contains an entangling unitary or its
partial-transpose conjugate (source p. 2).

The first branch takes some pure product preparation to an entangled state,
which is outside C125's minimal composite. In the second branch choose a
product input whose partial transpose is a product input entangled by the
unitary. The output is a partial transpose of a pure entangled two-qubit
state. In Schmidt coordinates its eigenvalues include the opposite pair
plus/minus s_1 s_2, with both Schmidt coefficients positive. It is therefore
not positive semidefinite and cannot be a separable density matrix either.
Product spectators do not change either obstruction. These are direct
applications of the source's two branches; neither requires initially
admitting entangled states as a hypothesis.

For larger admissible composites, Theorem 2 uses interchangeable copies and
three-system consistency to exclude the partial-transpose alternative. The
source then invokes entangling-gate universality and operational closure to
obtain all quantum preparations, measurements and completely positive
trace-preserving maps. Positivity of all resulting tests excludes further
states/effects. The broad conclusion includes these closure assumptions and
applies to finite numbers of identical qubits, not arbitrary local state spaces.

## Decision, evidence and remaining physical premise

Accept the source-backed exclusion of a reversible interacting extension
*preserving C125's minimal state space*. C125 itself remains a valid model
with local dynamics. Adding interaction as a premise is substantive: it
changes the allowed composite, rather than repairing a coordinate choice.
Theorem 1's technical Lie-algebra proof and the imported gate-universality
results were not independently audited. This milestone checks their statements,
the hypothesis map and the conditional consequence; it claims no novelty.

The source fixes probability structure. It supplies no mechanical Hamiltonian,
no identification of its transformation parameter with physical time/energy,
and no universal action normalization. G03's stochastic relaxation interaction
also supplies no reversible operational gate of this kind.

This completes the selected Q01 dependency decision. Full proof auditing and
a mechanical justification of exact reversible descent remain supporting
work. After comparing this third Q01 milestone with the gap track, select
G04's operator-identification test: construct G03's finite-volume Hermitian
representative and isolate the extra clock/action and physical-Hamiltonian
identifications. Stop at that transfer decision, rather than another coupling
variant. STATE owns the queue.
