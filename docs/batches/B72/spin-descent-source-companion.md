# B72 — classical spin Hamiltonian and moment descent

## Result and bounded question

The bounded audit finds a direct method match for the model in
`notes/hamiltonian-moment-descent.md`: classical spins on fixed-norm spheres
carry a Lie–Poisson bracket, and Hamilton evolution is obtained by taking the
Poisson bracket with the Hamiltonian. This supports the note's use of a
reversible Hamiltonian flow as hidden-measure dynamics, but not evolution on
the retained first/cross-moment quotient.

## Source and coverage

Primary source: *Hamiltonian Dynamics of Classical Spins*, `Physics` 8(1),
article 23 (2026), DOI `10.3390/physics8010023`,
<https://doi.org/10.3390/physics8010023> (publisher page:
<https://www.mdpi.com/2624-8174/8/1/23>). One discovery query was used.
The bounded route covers the opening Poisson-algebra/Hamilton-equation
discussion and displayed classical-spin equations, at most four article
pages. This is a method match, not a full-paper audit.

## Source-to-model match

The source presents classical spin components with antisymmetric Poisson
relations and derives time derivatives from the Hamiltonian. In the note's
normalization, `{u_i,u_j}=S_A^{-1} epsilon_ijk u_k` (and similarly for `v`);
therefore `H=J u_z v_z` gives cross-precession rates `J/S_A` and `J/S_B`.
`S_A,S_B` have action units and `J` energy units, so rates have inverse-time
units. Any overall sign convention is fixed internally by the note's stated
`dot f={f,H}` convention, rather than imported as a source quotation.

The method supports preservation of sphere Casimirs and an invertible
Hamiltonian flow. Completeness on `S^2 x S^2` follows from the note's smooth
vector field on a compact phase space; that is the note's deduction.

## Proof review and operational consequence

The two preparations in (3) have equal `E[u]`, `E[v]`, and `E[u v^T]`, and
equal microscopic energy. Yet
`d E[u_x v_z]/dt = -(J/S_A) E[u_y v_z^2]`, whose initial values are
`-J/S_A` and `0`. The product effect in (5) consequently separates their
later states. This written derivation establishes failure of a single-valued
quotient evolution; it does not claim every interaction behaves so.

B69 supplies the inherited boundary: minimal/separable composites and
restricted effects need not expose all hidden events. B70 presumes an
interaction already acting on the fixed locally tomographic operational state
space. This model fails that premise before B70 applies. A repair must either
restrict preparations/effects stably under interactions or enlarge retained
moments; finite capacity and action units choose neither.

## Limits and literature status

The source matches the Lie–Poisson/Hamiltonian method only. It establishes
neither the particular quotient counterexample nor a universal obstruction,
nonzero action parameter, or novelty. Coverage is one primary source with
selected pages, not an exhaustive prior-art search.

## Coordinator primary recheck and access boundary

Authors: Slobodan Radošević, Sonja Gombar, Milica Rutonjski, Petar Mali,
Milan Pantić and Milica Pavkov-Hrvojević. Publisher HTML/DOI returned 429
and XML returned 403 during review. The same work is available as
[arXiv:2503.16308v2](https://arxiv.org/html/2503.16308v2), dated
24 December 2025; this is the coordinator's checked version.
Selected §§V.1–V.2 give the sphere variables and Poisson algebra (69)–(75),
product phase space (77) and many-spin bracket/dynamics discussion. These
HTML passages were read; no full-paper or PDF visual-read claim is made.
The source uses normalized spins; the note supplies S_A,S_B and derives its
own component equations. The source's quantization prescription is not used.

Search accounting: one worker query plus two coordinator queries to verify
the DOI and find the preprint after access failed. This exceeded the initial
two-query total target by one; work stopped at the same paper. The worker's
unnamed page coverage remains reported; the above section anchors are checked.
