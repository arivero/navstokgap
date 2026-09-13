# B70 — reversible interaction and quantum composition

## Finding

The primary result is de la Torre, Masanes, Short and Müller, “Deriving
quantum theory from its local structure and reversibility,” arXiv:1110.5482v1
[quant-ph], submitted 25 October 2011 (printed PDF metadata: 10 September
2018), https://arxiv.org/abs/1110.5482 and PDF
https://arxiv.org/pdf/1110.5482. The paper’s Theorem 2 (PDF p. 2) states:
in any locally tomographic theory of identical qubits, any continuous
reversible interaction implies that allowed states, measurements and
transformations are identical to quantum theory. Theorem 1 (PDF p. 2) is the
technical reduction: for a connected reversible group containing all local
unitaries and preserving probabilities for product preparations and product
effects, any nonlocal element yields either an entangling unitary action or
its partial-transpose variant on a pair (with spectator state sigma).

## Exact scope and qualifications

The theorem is about *locally quantum* systems represented by Hermitian
matrices: each local system is a qubit, with all three Pauli fiducial
measurements and the Bloch ball (PDF p. 1). C125's affine ball/effects have
this representation via rho=(I+r.sigma)/2, and its tensor moments provide the
Hermitian coordinates. Local tomography means joint states
are fixed by all products of those local fiducial measurements (p. 1). The
connected group G contains the full local unitary group
`ad_U1 tensor ... tensor ad_Un`, hence all local SO(3) rotations, and every
G must make every product-state/product-effect probability lie in [0,1]
(Theorem 1, p. 2). “Continuous reversible interaction” means a reversible
transformation connected to the identity, so it can be implemented
continuously in time (pp. 1–2). Identical-system closure lets the interaction
be permuted to any pair (Theorem 2 proof, p. 2).

The conclusion forces the full quantum state cone/effects and CPTP
transformations only after these hypotheses and operational ancilla/discard
closure. The authors explicitly say the proof does not easily generalize to
higher dimensions or discrete transformations and leave broader
locally-tomographic representation as an open question (p. 4). The argument
also excludes the partial-transpose branch by using three qubits and positivity
of local measurement probabilities (p. 2).

## Map to C125 / Q01

C125 supplies the local ball, local SO(3) rotations, tensor-coordinate local
tomography, and arbitrary-copy/permutation closure. The missing premise is an
admissible connected nonlocal reversible interaction preserving product-state /
product-effect probabilities. Theorem 1 is the direct obstruction to retaining
C125's minimal separable composite: any such interaction must contain an
entangling unitary or a partial-transpose branch. Theorem 2 then uses the
identical-system closure to exclude the latter and force quantum states and
measurements. Its final CPTP/instrument conclusion additionally uses ancilla
preparation, joint evolution and discard closure, outside C125's terminal
scope.

Source-to-model capsule: theorem/setup (pp. 1–2) -> add connected reversible
nonlocal dynamics to C125 -> test preservation of product-effect positivity ->
Theorem 1 obstructs the minimal composite, while Theorem 2 plus identical-copy
closure selects quantum composition; ancilla/discard closure remains needed
for the broad CPTP statement. This is a dependency result, not an
independently verified physical mechanism or effective interaction setting.

## Coverage and limits

Evidence level: metadata, abstract and passage. I read the arXiv v1 PDF pp. 1–2
(setup, Theorems 1–2 and Theorem 2 proof) and p. 4 (conclusion/limitations),
using pdftotext extraction. Theorem 1's proof and universality steps remain
unaudited; I did not audit later versions.
Discovery count: one web discovery query; one primary paper selected. No
numerical or symbolic verification was performed.

## Coordinator verification

Coordinator checked arXiv version metadata and source pp. 1–2 plus the p. 3
coordinate setup; rendered p. 2 and visually checked both theorem statements.
The initial worker mapping was corrected: Hermitian coordinates and arbitrary
copies/permutations already occur in C125. See the written B70 review for the
conditional minimal-composite exclusion and operational-closure qualification.
The printed September 2018 date is distinct from the October 2011 submission.
