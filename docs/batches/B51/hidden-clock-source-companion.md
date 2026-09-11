# B51 source companion: hidden-clock ambiguity

## Result and bounded coverage

One primary source gives a close conceptual precedent for R20's common-record
family: parameter/state changes can be exactly input-output equivalent, and
non-identifiability is characterized by transformations preserving dynamics
and readout. It does not contain R20's Hamiltonian apparatus, fixed-energy
shell, finite eight-record map, pulse determinant, or risk-product bound.

## Primary source and reading

Eduardo D. Sontag, “Dynamic compensation, parameter identifiability, and
equivariances,” *PLoS Computational Biology* 13(4), e1005447 (2017), DOI
10.1371/journal.pcbi.1005447. Open primary full text:
https://pmc.ncbi.nlm.nih.gov/articles/PMC5398758/.

Four selected page-equivalents/passages were read: article metadata and
abstract (HTML lines 33–35, 100–110); system/parameterized-flow setup and
input-output equivalence (lines 116–148); equivariance definition and its
invariance implication (lines 149–170); and Lie-derivative identifiability
plus observability/separation (lines 173–205, 399–406). This is passage-level
coverage, not a full-article read.

## Claim-by-claim audit

**R20 / proposed C096 (hidden clock common-record family): partial conceptual
match only.** Sontag defines a parameterized initialized ODE and response, and
calls parameters structurally unidentifiable when distinct parameter/state
choices yield the same input-output response. An equivariance map preserving
the readout and intertwining vector fields is a sufficient certificate of
such equality. This supports treating hidden clock coordinates as augmented
parameters and searching for a record-preserving fibre. R20 instead proves a
finite-time, fixed-design, exact-record family by an implicit equation on the
receiver energy shell; no source theorem establishes that construction.

**R20 pulse determinant/transversality: no match.** The source's elementary
observables/Lie-derivative rank language is related to sensitivity and
separation, but it neither derives the four-pulse determinant asymptotic
`det A ~ D (r epsilon)^10` nor the positive transverse energy derivative from
clock speed. Those remain model-derived written calculations.

**R20 risk product: no match.** The source discusses exact identifiability and
state separation, not minimax endpoint risks, preparation margins, canonical
error products, or an action-unit lower bound. Equation (9)'s positive product
is therefore a derived consequence of the constructed common-record curve,
not an established literature result.

## Search and stopping record

Query 1 (2026-09-11): `primary source unknown clock offset calibration dynamical
system state identifiability observability energy shell implicit function level
set`.

The search located Sontag's open-access primary article. Query 2 was not used:
the one-source and four-selected-page budget was already sufficient. Search
results were discovery leads; only the cited Sontag passages count as evidence.
No exhaustive prior-art or novelty conclusion is claimed, and no numerical or
symbolic verification was performed.

## Source-to-model idea for R21

Treat the hidden initial clock momentum as a parameter of the finite-time
record map and compute a finite set of output sensitivities (or Lie-derivative
analogues) at the revealed clock position. Test whether the resulting map is
one-to-one locally after imposing the energy shell. A nontrivial
record-preserving equivariance would predict residual ambiguity; a full-rank
augmented sensitivity would support local recovery, while neither settles
global shell recovery.

## Coordinator source review

Verified metadata, Systems and equivalence equations (1)–(4), Definition 1,
Proposition 1 and the Observability passage in the primary HTML/MathML.
The source's equality ranges over all inputs and times; R20 concerns eight
records at one fixed time. Equivariance is therefore a comparison method,
not an asserted symmetry of R20's interacting Hamiltonian. Initial clock
momentum is a parameter of the preparation, while the clock momentum evolves
during interaction. The worker's four HTML selections are passage coverage,
not a verified PDF page count. No additional discovery query was used.
