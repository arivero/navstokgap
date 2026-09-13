# B76 spin-publication positioning source companion

## Finding

The bounded search found close precedents for both ends of the P06 example,
but no exact match for their combination. Bacciagaluppi's account of the
Beltrametti--Bugajski construction gives the same kind of many-to-one classical
preparation quotient onto a finite-dimensional quantum state space; for a
qubit its pure-state phase space is the Bloch sphere. Cavalcanti, Menicucci and
Pienaar show that adding nonlinear transformations can split preparation
equivalence classes and require a rule distinguishing physical preparations.
Neither selected paper treats a smooth two-classical-spin Hamiltonian, the
specific equal-first/cross-moment pair, or the all-preparation theorem excluding
every finite expectation-coordinate repair. The existing B74 source remains a
method/terminology precedent for that last theorem, not a finished-example
match.

This is bounded evidence, not an exhaustive priority search. It supports
presenting the manuscript as a self-contained conceptual or pedagogical worked
example. The spin-specific finite-repair result can be described as the
distinctive element of the example, but not as a literature-certified novel
theorem.

## Selected papers and exact coverage

### Guido Bacciagaluppi (2004)

Guido Bacciagaluppi, “Classical Extensions, Classical Representations and
Bayesian Updating in Quantum Mechanics,” arXiv:quant-ph/0403055v1, submitted
7 March 2004; presented at *Quantum Theory: Reconsideration of Foundations 2*,
Växjö, June 2003. Source: <https://arxiv.org/abs/quant-ph/0403055>.

Evidence level: metadata and selected passage. PDF pp. 1--4 were read using
`pdftotext -layout`; PDF p. 4 was also visually checked. Page 1 identifies the
paper as partly a review of the Beltrametti--Bugajski formalism and says later
sections contain new updating results. Pages 2--3 define convex operational
states/effects, classical probability measures and a surjective affine
reduction map. Section 2.3, p. 4, maps all probability measures on the pure
quantum states many-to-one onto density operators, explicitly naming the Bloch
sphere as the finite-dimensional example and identifying different classical
preimages with different convex decompositions of one mixed state.

Match status: **exact structural precedent for the local state quotient**, but
the selected passage is a secondary account of the original
Beltrametti--Bugajski construction. It does not cover P06's minimal composite,
Hamiltonian descent failure or finite-closure theorem. The original 1995 paper,
“A classical extension of quantum mechanics,” *J. Phys. A* 28, 3329--3343,
appeared as a discovery lead, but its public mirror failed over both HTTPS and
HTTP; it was not read or counted in page coverage.

### Cavalcanti, Menicucci and Pienaar (2012)

Eric G. Cavalcanti, Nicolas C. Menicucci and Jacques L. Pienaar, “The
preparation problem in nonlinear extensions of quantum theory,”
arXiv:1206.2725v1 [quant-ph], submitted 13 June 2012, 5 pages. Source:
<https://arxiv.org/abs/1206.2725>.

Evidence level: metadata and selected passage. PDF pp. 1--4 were read using
`pdftotext -layout`; PDF p. 3 was visually checked. Page 1 states the claimed
split of preparation equivalence classes. Page 2 defines operational
equivalence relative to all admitted transformations and measurements and
notes that preparations equivalent under linear operations need not remain so
when nonlinear transformations are admitted. Page 3 formulates the
“preparation problem”: a state label can cease to determine evolution, so the
theory must distinguish preparation classes and specify which physical
procedures belong to them. Page 4 generalizes the argument to density
operators and decomposition-dependent outputs, then restates the required
formal and operational distinctions.

Match status: **close conceptual precedent**, not an exact model match. Its
setting is a quantum nonlinear box plus operational verifiability and
no-superluminal-signalling assumptions. P06 instead has linear pushforward of
hidden probability measures under a complete classical Hamiltonian flow, but
no induced map on a deliberately coarser finite quotient. Cavalcanti et al. do
not prove a Koopman-orbit or finite-expectation no-go result.

## Source-to-model lesson

Operational equivalence is relative to an admitted experiment set. In the
Cavalcanti et al. definition that set includes transformations followed by
measurements. Consequently P06 should call its two preparations equivalent
under the **initial terminal-effect quotient**, not unqualifiedly equivalent
in the expanded theory that already admits the Hamiltonian: precomposing the
terminal effect with that Hamiltonian refines the equivalence relation. This
distinction makes the example's lesson sharper: a proposed finite state space
must be stable under the physical transformations assigned to the theory.

## Bounded discovery and access record

Four discovery queries were used, exhausting the assigned budget:

1. `"classical spin" Koopman "finite-dimensional" invariant observables moment closure`
2. `"Beltrametti" "Bugajski" classical extension qubit Bloch ball preparation equivalence dynamics`
3. `"preparation equivalence" nonlinear dynamics operational state classical spin`
4. `"classical spin" "preparation problem" operational equivalence Hamiltonian`

Search snippets were discovery leads only. Two papers and eight substantive
PDF pages total were selected: Bacciagaluppi pp. 1--4 and Cavalcanti et al.
pp. 1--4. No further search was performed. Bacciagaluppi is a published source
paper whose selected section reviews the canonical extension; Cavalcanti et
al. is the one selected primary result paper. Thus the audit stayed below the
two-primary-paper ceiling.

Temporary originals and extracted/rendered pages are confined to ignored
`.build/b76/`. SHA-256:

- `bacciagaluppi-2004.pdf`:
  `36a402ea3e008ad583ab97c7b776b76be048b21b3c0ce33906c07f502162012b`
- `cavalcanti-menicucci-pienaar-2012.pdf`:
  `bdf423f0a361c2d2ae2d30bd8e6a4d5ec4dac0b4e803d6dc3b90a9e52836965b`

The arXiv records identify non-exclusive licences granted to arXiv for hosting;
no broader republication licence was established. The PDFs remain temporary
and are not proposed for publication or shared source indexes. The unavailable
1995 mirror produced no local file.
