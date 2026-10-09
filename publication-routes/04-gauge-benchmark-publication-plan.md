# Publication plan: three gauge-theory interface benchmarks

**Decision document, 2026-09-28.** This plan treats the B/D Gaussian benchmark, the C strong-coupling mixing certificate, and the A Maxwell-fibre benchmark as three different mathematical objects. It recommends independent theorem audits and literature searches before selecting article boundaries. The repository notes are proof-bearing research syntheses; their presence here does not by itself establish that a theorem, method, or application is new to the literature.

## 1. Executive recommendation

| Unit | Exact object currently in the repository | Publication disposition | First venue to assess |
|---|---|---|---|
| **B/D** | Massive complex Gaussian scalar on a four-dimensional lattice; finite-range Gaussian Markov blocking, cutoff-uniform covariance seminorm control, continuum OS reconstruction, and one-particle threshold \(\hbar c m\). The mass is supplied and the symmetry is global \(U(1)\). | A conditional standalone methods/benchmark paper only if the literature review establishes value in the assembled interface theorem, rather than in standard free-field facts. Otherwise retain as a technical appendix or repository benchmark. | *Journal of Mathematical Physics*; *Journal of Statistical Physics* if the finite-range/blocking result is the centre. *Communications in Mathematical Physics* is a stretch contingent on a demonstrable advance. |
| **C** | Four-dimensional periodic \(SU(3)\) Wilson Gibbs measures; a gauge-invariant Wilson-loop covariance estimate under a Dobrushin condition, with an open plaquette-interaction ball and explicit Wilson-coupling threshold \(g^2>24/\log(19/18)\). | Strongest independent article candidate. Submit only after a result-specific originality search and a theorem audit of the influence-matrix comparison and constants. State the regime as the explicit strong-coupling neighbourhood. | *Journal of Statistical Physics* or *Journal of Mathematical Physics*; *Annales Henri Poincaré* or *Communications in Mathematical Physics* only if the prior-art and technical contribution justify that level. |
| **A** | Periodic Gaussian \(U(1)\) Maxwell theory after the gauge quotient; exact harmonic/transverse split, nonconstant-mode lower bound \(\hbar c(2/a)\sin(\pi/N_s)\), and zero Feshbach off-diagonal. | Not recommended as a standalone paper on present evidence: the central calculation is an exact free-field decomposition. Keep as a focused benchmark or combine only if a broader, independently justified fibre-reduction framework supplies a real theorem-level contribution. | *Journal of Mathematical Physics* if the gauge-quotient/Feshbach formulation proves more than the standard torus spectrum; otherwise no journal submission. |

**Do not merge the three into one theorem paper by default.** The B/D scalar uses a supplied mass and a Gaussian Markov kernel; C is an interacting compact-group Gibbs measure in a strong-coupling region; A is a free gauge field with a physical quotient and an exactly reducing projection. Their common value is architectural: they instantiate distinct interfaces in the repository's H1/H2/A framework. A cross-benchmark perspective article is a later option only if it answers a sharply formulated question that cannot be answered by the separate theorem statements.

The article boundary for C should remain especially narrow. The Wilson-loop mixing ball is a one-box correlation/mixing certificate. Keep it distinct from the weak/intermediate-coupling scaling trajectory and from continuum OS construction; any larger manuscript must state additional hypotheses as hypotheses rather than folding them into the certificate.

## 2. What is repository synthesis, and what is established input?

This distinction should appear in each abstract, introduction, and theorem-proof map.

### B/D Gaussian blocking and OS reconstruction

**Established input already identified in the repository:** the positive finite-range decomposition of the massive lattice resolvent, cited to Brydges–Guadagni–Mitter (2004); standard Gaussian characteristic-function identities; covariance convergence for the massive free field; and the standard OS/Fock reconstruction of a free massive scalar field.

**Repository synthesis and derived statements:** the conditional-covariance identity is used to express a one-step blocking defect; finite range gives an exact zero beyond the fluctuation range; positivity of the covariance decomposition gives a telescoping, cutoff-uniform Weyl seminorm bound; these are then assembled with the continuum free-field limit into a concrete B/D/H3 benchmark. The Markov-kernel nature of the block operation, as distinct from deterministic link decimation, is part of the statement.

**Novelty test:** determine whether this exact interface-level combination, with the stated algebra, seminorm and constants, has appeared in finite-range decomposition, renormalization-group, or constructive-field-theory literature. Standardness of each ingredient does not decide whether the assembled theorem is useful or new. Describe it as an application/benchmark if that is what the search establishes; use a novelty claim only for an identified result not found in the reviewed sources.

### C strong-coupling mixing certificate

**Established input already identified:** Dobrushin uniqueness/comparison methods and covariance decay under a summable influence matrix; Wilson lattice gauge measures and their strong-coupling regimes; standard character/polymer-expansion results for lattice gauge theory. These lines of work are prior art, not claims of this repository.

**Repository synthesis and derived statements:** a link-conditional distribution is written explicitly for a gauge-invariant plaquette interaction; a mixed-oscillation seminorm controls total-variation influence; the four-dimensional link graph gives the row-sum bound \(18(e^{J}-1)\); Dobrushin comparison is expressed on the gauge-invariant Wilson-loop algebra; and the Wilson interaction is placed inside an explicit open local-interaction ball. The Wilson specialization yields the stated sufficient coupling condition.

**Novelty test:** look for prior Dobrushin or strong-mixing bounds for non-Abelian lattice gauge measures, especially Wilson loops, arbitrary local gauge-invariant plaquette interactions, and explicit four-dimensional constants. Distinguish a new gauge-invariant formulation or stability ball from a rederivation of known exponential clustering. The numerical radius is a sufficient certificate; do not call it a critical coupling or a phase boundary.

### A periodic Maxwell fibre benchmark

**Established input:** discrete Hodge decomposition on a periodic complex; Fourier diagonalization of the free lattice Maxwell operator; the two transverse polarizations; and the standard finite-volume photon spectrum with harmonic/holonomy modes separated from nonzero momentum modes.

**Repository synthesis and derived statements:** the physical configuration quotient is used before projection; the slow harmonic factor is retained; the exact lattice dispersion gives a finite-spacing nonconstant-mode bound; the transverse vacuum projection reduces the free Hamiltonian, making the Feshbach off-diagonal identically zero. This gives an exactly solvable reference case for the non-abelian fibre estimate.

**Novelty test:** establish whether the theorem's formulation as a gauge-invariant Feshbach benchmark and its cutoff comparison are genuinely absent from established lattice Maxwell/Hodge and Born–Oppenheimer/Feshbach treatments. If the search finds the same decomposition and estimate in standard form, cite it and retain the note as a benchmark rather than promoting it as an independent research article.

## 3. Required literature review before manuscript drafting

The current repository literature is a starting map, not a complete originality audit. Search primary papers and reviews, trace citations backward and forward, and log each source with the exact theorem or passage checked. Search exact mathematical phrases and equivalent formulations; terminology may differ from the repository's H1/H2/A labels.

### B/D search programme

1. Read the full finite-range decomposition theorem and hypotheses in Brydges–Guadagni–Mitter, *Journal of Statistical Physics* **115** (2004), 415–449; verify positivity, dimensional/mass assumptions, lattice conventions, volume dependence, and whether the cited version supplies the residual covariance used here.
2. Search finite-range decompositions of massive lattice Green functions, Gaussian RG/block-spin kernels, covariance interpolation, and scale-by-scale connected-correlation estimates. Include work that uses conditional expectation or random block kernels rather than deterministic decimation.
3. Check standard free scalar OS reconstruction, reflection positivity, lattice-to-continuum covariance limits, and the precise one-particle/field normalization. Establish which claims are classical facts and which require a proof specific to this normalization.
4. Search for cutoff-uniform seminorm or Weyl-algebra telescoping bounds in constructive QFT and RG literature. Compare the exact seminorm in (15) of [`u1-gaussian-blocking-os-benchmark.md`](../notes/u1-gaussian-blocking-os-benchmark.md), including its algebra and test-function class.
5. Search combinations such as “finite-range covariance decomposition + OS reconstruction”, “Gaussian covariance splitting + RG error”, and “block kernel + uniform spectral gap transport”. Record negative searches as bounded coverage, never as proof of priority.

### C search programme

1. Read Dobrushin's uniqueness/comparison theorem and the Dobrushin–Shlosman strong-mixing framework in the exact convention used for total variation, oscillation, and covariance prefactors. Check the finite-volume theorem and its infinite-volume limit separately.
2. Review lattice gauge-theory strong-coupling clustering and mass-gap results, including Osterwalder–Seiler character/cluster expansions and established Wilson-loop correlation estimates. Compare observable classes, dimensions, coupling normalization, constants, volume uniformity, and whether local interaction stability is covered.
3. Search specifically for Dobrushin influence matrices on link variables modulo gauge symmetry, gauge-invariant loop algebras, plaquette mixed-oscillation norms, and stability under arbitrary gauge-invariant plaquette perturbations. Include non-Abelian groups beyond \(SU(3)\), since a group-general theorem may predate the specialization.
4. Independently compare the threshold \(\beta<\tfrac14\log(19/18)\) with existing sufficient strong-coupling radii. Determine whether the contribution is the constant, the gauge-invariant observable statement, the open interaction ball, or a useful combination; do not equate a sufficient Dobrushin ball with the full strong-coupling phase.
5. Search articles, books, and review chapters under “strong mixing”, “complete analyticity”, “Dobrushin uniqueness”, “Wilson action”, “lattice gauge theory”, “gauge-invariant correlation decay”, and “uniform clustering”. Check cited sources at theorem level, not from abstracts alone.

### A search programme

1. Review discrete Hodge theory and the spectrum of compact/noncompact Maxwell theory on a periodic spatial lattice/torus, distinguishing harmonic holonomies, electric-flux sectors, gauge zero modes, and nonzero transverse oscillators.
2. Search lattice Maxwell Hamiltonians, torus photon spectra, Coulomb-gauge and gauge-quotient quantization, and exact finite-lattice dispersion bounds.
3. Review Feshbach maps, Born–Oppenheimer fibre projections, and adiabatic decoupling for gauge fields. Determine whether a zero Schur term from an exactly reducing free-field projection is already standard.
4. Verify how compact large gauge transformations act on the harmonic factor and whether the manuscript's Gaussian connection plus compact holonomy description is a single consistent regulator or a direct-product idealization that must be stated more narrowly.
5. Search for the exact comparison \(q_{a,\min}=(2/a)\sin(\pi/N_s)\) and its fixed-physical-volume limit in equivalent conventions; establish whether the bound and projection formulation contain any result beyond textbook Fourier analysis.

**Search record required for each candidate:** date, databases/indexes used, query strings, sources examined at full-text or theorem level, closest precedents, exact difference table, and remaining unsearched scope. A short search log belongs in the eventual manuscript's internal record; only necessary citations and a concise prior-work comparison belong in the submitted text.

## 4. Theorem-audit gates

No candidate moves from research note to submission draft until its proofs and hypotheses have been independently checked line by line. This is a theorem audit, not a re-running of forbidden numerical or symbolic checks.

### B/D audit

- **Model and scaling:** check the lattice covariance, complex-field normalization, factor of \(\hbar\), test-function pairing, and continuum limit dimensions. State finite/periodic-volume conventions consistently; do not infer volume-uniformity from an infinite-lattice decomposition without the corresponding finite-volume theorem.
- **Finite-range premise:** verify positivity of every \(\Gamma_{a,j}\), the residual covariance, exact range in the stated scale coordinates, and uniformity in cutoff and volume. Cite the precise theorem supporting each property.
- **Blocking identity:** derive the conditional covariance/tower identity for the stated observables and kernel; check the support-distance convention and the factor in the covariance sup-norm bound. Make explicit that this is random Gaussian integration, not deterministic blocking.
- **Weyl seminorm:** verify the characteristic-function identity, the connected-covariance estimate, positivity-based summability, and Cauchy–Schwarz over scales. Check extension from real tests to the claimed algebra and identify exactly which OS-continuity topology is used.
- **Continuum and reconstruction:** prove covariance convergence on the claimed test space, reflection positivity for the complex field, nontriviality/density of local vectors, and the Hamiltonian threshold with the chosen \(c,\hbar,m\) conventions. Distinguish the one-particle mass from a supplied input from a dynamically generated parameter.
- **Assembly interface:** map each B/D/H3 assertion to the corresponding hypothesis and conclusion of the conditional assembly theorem without changing the theorem's algebra, support, or uniformity assumptions.

### C audit

- **Conditional law and gauge covariance:** derive the conditional density from the finite-volume Gibbs measure; check orientation conventions, plaquette incidences, and covariance under vertex gauge transformations. Separate link-coordinate conditionals from the gauge-invariant observable conclusion.
- **Oscillation and total variation:** reprove the density comparison (including the total-variation convention), the mixed-oscillation bound, and the use of suprema over boundary conditions. Check whether an interaction term can involve a pair of links more than once and whether the definition handles orientation inversions.
- **Influence matrix:** verify the maximum of 18 neighbours for the specified periodic hypercubic link graph, small-volume identifications, row-sum condition, resolvent covariance inequality, and exponential-distance estimate. Check prefactors against the exact Dobrushin theorem cited.
- **Wilson specialization:** derive the staple trace bound, oscillation factor, \(\beta=6/g^2\) convention, and algebra from the influence condition to \(g^2>24/\log(19/18)\). Keep “sufficient condition” language attached to every threshold statement.
- **Perturbation ball:** establish that the seminorm is well-defined on gauge-invariant plaquette interactions, subadditive, invariant under adding constants and gauge transformations, and open in the stated topology. State whether the perturbations preserve reflection, translation, and orientation symmetries; do not silently require these if the theorem does not.
- **Observable algebra and uniformity:** verify that the covariance estimate applies to all claimed bounded Wilson-loop polynomials, with support/oscillation dependence explicit, and that constants are independent of periodic volume. State whether passage to infinite volume is a corollary and what boundary-condition control is needed.

### A audit

- **Complex and real structures:** ensure the Gaussian connection model, compact large-gauge identifications of harmonic holonomies, and induced physical inner product define one consistent finite regulator. If not, split the compact harmonic sector from the noncompact Gaussian transverse regulator explicitly.
- **Hodge quotient:** verify the finite periodic cochain decomposition, dimensions of harmonic and transverse subspaces, treatment of exact/longitudinal modes, and the physical Hilbert-space factorization after quotienting.
- **Hamiltonian:** derive the lattice Maxwell quadratic form and dispersion, polarization count at special momenta, normal-ordering convention, harmonic-sector Hamiltonian, and tensor-product decomposition.
- **Finite-volume bound:** verify the minimizing nonzero momentum for all allowed \(N_s\), including small lattices and even/odd sizes; verify the stated sine inequality's domain and continuum limit.
- **Feshbach statement:** confirm \(P\) is a physical projection, reduces the stated Hamiltonian, and that the resolvent domain and relative-Schur claim are correctly formulated. Make the zero off-diagonal conclusion follow from the exact tensor decomposition, not an informal mode argument.
- **Interpretation:** separate the lowest nonconstant oscillator energy from the full spectrum when harmonic modes are retained. Do not label it a gap above the global vacuum unless the harmonic sector's ground state and degeneracies have been checked.

A failed audit changes the statement first; it does not get patched with broader prose. Record any corrected conventions or counterexamples in the source note and then re-evaluate the publication unit.

## 5. Candidate manuscript outlines

These are deliberately modular. Draft only after the relevant literature and theorem-audit gates pass.

### C — preferred independent article

Provisional title: **Gauge-invariant Dobrushin mixing for four-dimensional \(SU(3)\) lattice gauge measures**

1. **Abstract:** finite-volume model, gauge-invariant loop algebra, sufficient influence condition, explicit Wilson ball, volume-uniform bound; state the coupling normalization and that the result concerns the strong-coupling region.
2. **Introduction and comparison:** explain why a gauge-invariant observable statement and perturbation stability are useful; identify exact prior results and differences without priority language beyond the reviewed search.
3. **Definitions and finite-volume setup:** links, plaquettes, gauge action, loop algebra, oscillation and mixed-oscillation norms.
4. **Conditional laws and influence estimate:** conditional density, total-variation lemma, graph degree and Dobrushin criterion.
5. **Main theorem:** covariance decay with explicit support and volume dependence; proof and infinite-volume corollary if justified.
6. **Wilson specialization:** explicit constants and open plaquette-interaction ball; examples and normalization table.
7. **Relation to established strong-coupling methods:** compare Dobrushin bounds with character/polymer expansions and state the precise niche of this certificate.
8. **Limits of the theorem as a research interface:** identify it as the H2 component at the stated couplings; distinguish it from scale transport and continuum construction in a concise scope paragraph.
9. **Appendices:** total-variation convention, graph/incidence calculation, and full constants audit.

### B/D — conditional methods paper

Provisional title: **Finite-range Gaussian blocking and a cutoff-uniform OS benchmark for the massive scalar field**

1. **Abstract and precise theorem:** model, finite-range input, Markov kernel, seminorm summability, continuum reconstruction.
2. **Prior work and contribution boundary:** finite-range decomposition, Gaussian RG and free-field OS results; say what is imported and what is the assembled estimate.
3. **Lattice model and scaling conventions.**
4. **Finite-range covariance decomposition and block kernel.**
5. **Exact bounded-observable covariance transport.**
6. **Weyl seminorm estimate and scale summability.**
7. **Continuum covariance, reflection positivity and OS/Fock reconstruction.**
8. **Interface interpretation and comparison with deterministic gauge blocking.**
9. **Appendix:** finite-volume formulation, test-function limits, and convention checks.

The paper proceeds only if Section 2 can articulate an independently meaningful result after crediting the finite-range and free-field literature. Otherwise the entire proof should remain available as an openly documented benchmark, not be stretched into a novelty claim.

### A — only after a positive novelty finding

Provisional title: **An exact gauge-quotient Feshbach split for periodic lattice Maxwell theory**

1. State the regulator and compactness convention unambiguously.
2. Prove the discrete Hodge decomposition and physical Hilbert-space split.
3. Diagonalize the nonconstant transverse Maxwell Hamiltonian.
4. Establish the finite-spacing lower bound and fixed-volume limit.
5. Prove the reducing projection and zero Feshbach off-diagonal.
6. Compare with existing torus Maxwell and Feshbach results.
7. Explain precisely which non-Abelian fibre estimate this benchmark calibrates.

If the literature audit identifies the result as standard, stop at the repository note. If a common A/B benchmark suite later becomes a paper, A can serve as a separate model section, not as evidence that the scalar and gauge theories share a theorem.

## 6. Staged preparation and release plan

1. **Freeze theorem statements.** Create a one-page theorem sheet per unit with model, assumptions, constants, observable algebra, limits, and exact conclusion. Reconcile notation with the conditional assembly theorem and source notes.
2. **Complete theorem audits.** Use the checklists above; ask a specialist in constructive field theory for C, and in lattice gauge/Maxwell quantization for A if the manuscript is considered. No candidate is “submission ready” on author self-review alone.
3. **Run the result-specific literature reviews.** Complete the source log, read closest sources at theorem level, build a comparison table, and obtain an independent bibliographic review. Bound every negative search claim by date and coverage.
4. **Select article boundaries.** Prioritize C. Make the B/D go/no-go decision after its originality audit. Retain A as an appendix/benchmark unless its audit finds a distinct theorem contribution. Do not combine C with either Gaussian benchmark just to increase article size.
5. **Draft and circulate.** Write C first with a theorem-first narrative and explicit prior-work comparison. Circulate to a specialist reader; resolve mathematical objections before venue styling. Draft B/D or A only if their go/no-go gates pass.
6. **Venue and policy pass.** Check current aims, article categories, length, data/source expectations, preprint policy, AI-use declaration policy, and exclusivity/submission rules on each target journal's official page immediately before submission. Select one primary and one fallback per accepted unit; the venue names in this plan are candidates, not editorial predictions.
7. **Prepare reproducible files.** Include editable source, the compiled PDF from that source, bibliography, figure licenses if any, and build instructions. Verify all citations, equations, hyperlinks, and redistribution rights for any archived source material. Keep working notes and internal search logs out of the submission unless they are intentionally cited supplements.
8. **Author approval and submission.** Obtain written approval of the final text, author order, declarations, and destination from all named authors. The repository plan itself authorizes neither external correspondence nor journal submission.

## 7. Authorship, attribution, and disclosure

- **Do not infer a byline from Git history, repository ownership, or the use of an AI agent.** The human project lead must determine the author list, order, affiliations, corresponding author, and each person's substantive contribution; every listed author must approve the final manuscript and take responsibility under the venue's rules.
- Attribute established inputs to their original sources at the point of use: finite-range decomposition, Dobrushin comparison, standard Wilson strong-coupling methods, discrete Hodge theory, and free Maxwell/OS reconstruction. Distinguish imported theorems from calculations and assembly performed in this repository. Do not cite the repository as prior published literature for its own theorem.
- Maintain source-level attribution in proof notes and manuscript references. Any theorem whose proof is adapted from a source should identify that source and the modifications; any specialist who only checks a draft should be credited in acknowledgements only with permission, not automatically listed as an author.
- Follow the chosen venue's current policies for AI-assisted research and writing. Describe assistance accurately where requested; do not present an AI system as a human author, invent a human contribution, or claim independent verification that did not occur. Any external reviewer or collaborator's role must be documented truthfully.
- The manuscript should include a contribution statement where required and a funding/conflict statement only on verified information. Leave author identity, institutional affiliation, funding, and acknowledgements unresolved until supplied and approved by the humans involved.

## 8. Readiness criteria

A unit can be recommended for submission only when all applicable boxes are checked:

- [ ] theorem statement is stable and each hypothesis is used where claimed;
- [ ] independent proof audit has no unresolved substantive objection;
- [ ] closest prior art has been read at the relevant theorem/passage level;
- [ ] repository synthesis and established literature are separated in the text;
- [ ] contribution and limitation language matches the precise model and regime;
- [ ] constants, units, gauge conventions, and limit order are audited;
- [ ] target venue and article category fit the actual contribution;
- [ ] all authors, attribution, affiliation, and required disclosures are approved;
- [ ] source, bibliography, compiled PDF, build instructions, and rights are checked;
- [ ] explicit author direction is obtained before external submission.

## 9. Repository map

- B/D theorem and proof: [`notes/u1-gaussian-blocking-os-benchmark.md`](../notes/u1-gaussian-blocking-os-benchmark.md).
- C theorem and proof: [`notes/gauge-invariant-dobrushin-certificate.md`](../notes/gauge-invariant-dobrushin-certificate.md); related Wilson uniqueness synthesis: [`notes/dobrushin-uniqueness-wilson.md`](../notes/dobrushin-uniqueness-wilson.md).
- A theorem and proof: [`notes/u1-maxwell-fibre-feshbach-benchmark.md`](../notes/u1-maxwell-fibre-feshbach-benchmark.md).
- Conditional assembly and interface definitions: [`notes/mass-gap-conditional-theorem.md`](../notes/mass-gap-conditional-theorem.md) and [`research/continuum-proof-assault-plan.md`](../research/continuum-proof-assault-plan.md).
- Existing bibliography: [`references/library.bib`](../references/library.bib).
