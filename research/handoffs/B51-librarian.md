# B51 librarian handoff

## Completed bounded audit

Read R20 (`notes/hidden-clock-ambiguity.md`) and the B50 source companion.
Audited one primary source within the authorized budget:

Eduardo D. Sontag, “Dynamic compensation, parameter identifiability, and
equivariances,” *PLoS Computational Biology* 13(4), e1005447 (2017), DOI
10.1371/journal.pcbi.1005447; https://pmc.ncbi.nlm.nih.gov/articles/PMC5398758/.

Used one web query (exact query and date are recorded in the companion), and
read four selected page-equivalents/passages: metadata/abstract; the
parameterized ODE and I/O-equivalence setup; equivariance/invariance; and
Lie-derivative identifiability plus observability. No second query, source, or
additional pages were used. Effective worker setting was Luna-low as
requested; no independent runtime metadata beyond that dispatch label is
available here.

## Findings

The source is a partial conceptual match: it formalizes exact I/O equivalence
under changed parameters/initial states and gives record-preserving
equivariances as certificates. This motivates treating hidden clock data as
augmented parameters and searching for a common-record fibre. It does not
match R20's Hamiltonian eight-pointer map, receiver energy-shell constraint,
pulse determinant/transversality calculation, or canonical minimax risk
product. Literature status is therefore “bounded partial precedent,” with
novelty unassessed.

The source-to-model suggestion for R21 is to augment the state with hidden
clock momentum and use a finite output-sensitivity/Lie-derivative map after
revealing clock position: test local injectivity under the energy-shell
constraint, while separating that from global shell recovery.

Full details and exact reading coverage are in
`docs/batches/B51/hidden-clock-source-companion.md`. No shared indexes,
claims, task state, commits, or numerical/symbolic scripts were changed.
