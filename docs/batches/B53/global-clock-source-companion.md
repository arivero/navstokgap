# B53 source companion: global clock-speed ambiguity

## Result and bounded coverage

The source distinguishes local from global identifiability and, separately,
structural from at-a-point identifiability. Its Hessian discussion diagnoses
approximate uncertainty; rank loss alone supplies no exact output collision.
This is a methodological precedent for R22/C100–C101, rather than a theorem
about the Hamiltonian clock apparatus.

## Primary source and exact passages

Tom Quaiser, Anna Dittrich, Fred Schaper and Martin Mönnigmann, “A simple work flow for biologically inspired model reduction—application to early JAK-STAT signaling,” *BMC Systems Biology* **5**, article **30** (2011), DOI **10.1186/1752-0509-5-30**. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3050741/.

One query was used (2026-09-11): `site:pmc.ncbi.nlm.nih.gov structural identifiability local global multiple parameters same output equivalence`. Three selected HTML passages were read (passage-level, not full-read):

1. Lines 134--142: smooth state/parameter/input/output model and the point that outputs over a finite observation interval are fixed by initial conditions and input.
2. Lines 180--190: definition of global versus local (at-a-point) structural identifiability; equality of outputs implies equality of the parameter under the relevant quantifier. The same passage explains that a small Hessian eigenvalue corresponds to a long uncertainty direction, with parameters far apart having almost the same objective value.
3. Lines 244--246 and 301--313: application-level examples where tiny eigenvalues and large coefficient-of-variation lower bounds diagnose non-identifiable parameters. These are numerical/data-analysis examples, not exact dynamical counterexamples, and are used only to illustrate the diagnostic distinction.

## Claim-by-claim audit

**C100 (actual distinct-speed equal-energy finite-record pair): no exact source match.** R22's written argument is stronger and different: it constructs a fixed pulse design, two fixed distinct speeds, a continuous equal-energy shell path, opposite endpoint signs of the energy mismatch, and an intermediate point with exactly identical eight records. The source's output map is a general smooth ODE response and gives definitions/diagnostics; it neither has an energy shell nor a finite eight-coordinate Hamiltonian record map, nor proves the intermediate-value construction. The pair and its positive-coordinate separation remain model-derived.

**C101 (positive-coupling persistence and risk product): no source match.** The source does not prove persistence of an exact equal-output branch under coupling, uniform preparation margins, canonical coordinate separation, minimax risks, or an error-product lower bound. R22's contraction/implicit continuation and continuity argument, followed by the two-point estimator bound, must be checked as a written proof. The source's Hessian/eigenvalue discussion concerns approximate fit and variance, not exact common records or a preparation-dependent action-unit product.

**Local versus global scope.** The source makes the logical boundary explicit: local recovery on one patch does not imply global recovery over the shell. R21's local inverse therefore remains compatible with R22's separate global equal-record pair. The source does not assert that every locally identifiable system has a remote collision; it only supplies the quantifier distinction and a standard sensitivity diagnostic.

## Source-to-model idea for R23

Treat the final clock momentum as an additional output coordinate in the record map. Re-run the global question on the same full shell: test whether the augmented map is locally invertible on the R21 patch and whether a distinct-speed equal-record branch can still cross the energy shell. A final momentum record that is persistent after the pulses may remove the R22 collision, but this is a model-specific global injectivity question; local Jacobian rank alone cannot settle it.

## Coverage and stopping

Coordinator correction: the worker's Raue/2010/volume-4 attribution was wrong.
Verified all four authors, year, volume, article number and DOI at PMC and the
[publisher](https://link.springer.com/article/10.1186/1752-0509-5-30).
Re-read Methods / System class and Identifiability in the primary HTML, using
its text and MathML extraction after an intermittent browser challenge.
The definitions distinguish local/global parameter alternatives from
fixed-reference/all-reference identifiability. The Gaussian Hessian diagnostic
is not imported into R22's exact pair proof. Application examples remain
worker-only coverage; coordinator acceptance uses the definitions.

The query, one primary source, and three selected passage groups exhaust the assigned budget. Search snippets were discovery leads; only the named lines count as evidence. Novelty is unassessed. No numerical or symbolic verification script was created or run.
