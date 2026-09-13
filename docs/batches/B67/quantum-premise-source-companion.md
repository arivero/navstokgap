# B67: quantum-premise dependency audit

## Result

Neither route derives quantum structure from Newtonian continuity or from
apparatus ignorance. Hardy excludes the finite classical simplex by adding a
specific continuous reversible-transformation axiom; Chiribella--D'Ariano--
Perinotti (CDP) exclude it by adding purification (with uniqueness), inside a
finite-dimensional operational-probabilistic theory. Both routes therefore
leave the project's dimensional action unit (and its identification with
\(\hbar\)) as an external, still-open premise.

## Bounded primary coverage

Only the specified versions were read, using their arXiv HTML renderings:

* L. Hardy, *Quantum Theory From Five Reasonable Axioms*,
  arXiv:quant-ph/0101012v4 (25 Sep 2001), §§1, 4, 6--7 (HTML anchors
  `S1`, `S4`, `S6`, `S7`). Page estimates from the worker are not accepted:
  HTML section anchors are the locators. Selected passages, not entire sections,
  were audited; no reconstruction proof audit.
* G. Chiribella, G. M. D'Ariano, P. Perinotti, *Informational derivation of
  quantum theory*, arXiv:1011.6451v3 (2011), §§III.1--III.2 and IV.2 (HTML
  anchors `S3`, `S4`). Coverage is selected passages, with no verified PDF
  page count or full proof audit. The coordinator additionally checked §II's
  finite-dimensional operational-state definition.

## Hardy: premise and classical comparison

Hardy defines a finite operational state description by \(N\), the maximum
number of distinguishable states, and \(K\), the number of real parameters
(§1, HTML `S1`, immediately before the five axioms). The five axioms are:
probabilities (limiting relative frequencies), simplicity (minimal \(K(N)\)),
subspaces, composite systems (\(N=N_A N_B\), \(K=K_A K_B\)), and continuity
(§1 `S1.I3`, repeated in §6). He explicitly states that the first four are
consistent with classical probability theory, while dropping the word
“continuous” in Axiom 5 gives classical probability with \(K=N\); quantum
theory has \(K=N^2\) (§1 `S1`, paragraphs after Axiom 5).

The exact Axiom 5 is: “There exists a continuous reversible transformation on
a system between any two pure states” (§6 `S7`, `Thmaxiom5`). In the classical
comparison (§4 `S4`, paragraph beginning “Note that the Axioms 1 to 4 are
satisfied”), pure states are finite in number, reversible transformations map
pure states to pure states, and hence no continuous path through pure states
can connect arbitrary distinct pure states. This is a finite simplex argument:
it is not a claim about continuous classical phase-space mechanics, whose pure
state set is not a finite simplex and is outside Hardy's finite \(N,K\) model
as used here.

**Dependency reading.** Continuity is an operational transformation premise,
not a consequence of a Newtonian trajectory's continuous time or position.
Hardy's result says which finite operational model is selected if all five
axioms hold; it supplies neither a physical mechanism enforcing Axiom 5 nor a
positive action quantity, units, phase law, or lower bound on classical action
differences.

## CDP: ambient class, purification, and classical comparison

CDP work in operational-probabilistic theories with systems, states,
transformations, tests and effects. Their five principles in §III.1 (`S3`) are
causality, perfect distinguishability, ideal compression, local
distinguishability, and pure conditioning. They state that all five are also
satisfied by classical information theory; in particular, classical pure
composite states are products, so conditioning one component leaves the other
pure (`S3`, discussion immediately after Axiom 5). Thus these principles do
not themselves exclude the classical finite simplex.

The additional purification postulate in §III.2 (`S3`/`Thmpostulate1`) requires
a pure extension of every state, unique up to reversible transformations of
a fixed purifying system. The introductory discussion (`S1`, paragraphs
around the purification principle) identifies this as a conservation-of-
information requirement and notes that the uniqueness clause is part of the
assumption. §IV.2 (`S4.SS2`) uses the postulate to derive consequences such as
reversible freedom between purifications; the paper's advertised selection of
quantum theory is conditional on this operational package and its finite
system framework.

**Dependency reading.** CDP's classical countermodel is standard finite
classical information theory, not continuous classical mechanics. Purification
is not epistemic ignorance of an apparatus: it asserts existence and essential
uniqueness of a pure extension plus reversible transformations. Nothing in the
audited passages derives purification from Newtonian continuity, mechanical
ignorance, or an apparatus model. No audited passage supplies an action
normalization, \(\hbar\), a phase/action map, or a positive universal action
gap.

## Decision and remaining step

Retain both as conditional operational reconstructions, with distinct
exclusion premises: Hardy = continuous reversible pure-state connectivity;
CDP = purification and uniqueness on top of five classical-compatible
principles. Reject the inference “classical continuity implies Hardy
continuity” and the inference “unknown apparatus state implies CDP
purification.” The next Q01 step must separately specify a physical premise
that selects one package (or another exclusion principle) for the project's
mechanical models. A further bridge must then introduce a dimensional positive
action constant and show how it enters phases/transformations; neither source
does this.

## Coordinator correction and additional passage

Hardy's Axiom 5 is in §7, not §6. His §1 also discusses a countably infinite
extension; the present exclusion map concerns the finite-system argument and
does not attribute a finite-only scope to the whole paper. In §7 Hardy
explicitly considers a ball moving between two boxes: intermediate physical
states lie outside the classical bit subspace. Thus there is a physical
continuity motivation, even though closure of the finite operational state
description during the transformation is an extra requirement. This nuance
qualifies the worker's opening contrast with Newtonian continuity.

For CDP the coordinator checked §II's finite-dimensional state/effect passage,
§I's five-principle summary, §III.1.5's classical pure-product statement and
§III.2's purification definition/postulate and adjacent interpretation.
Existence of a pure extension already fails for a mixed state in the standard
classical product-simplex model; uniqueness is further structure used by the
reconstruction, not needed for that elementary failure. Selected passage
coverage only, two primary routes, zero discovery queries. Requested worker
Luna low, effective settings unverified; no descendants.
