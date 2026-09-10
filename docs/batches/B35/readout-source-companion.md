# B35 readout source companion

## Scope and coverage

Bounded audit of `notes/classical-readout-refinement.md` (R05), completed 2026-09-10. Two discovery query families, two primary sources, and two bounded HTML readings were used. No source originals were downloaded or added to tracked documents. Reading was limited to the passages named below.

## Queries

1. `classical measurement Hamiltonian pointer model measurement error disturbance primary source`
2. `"Measurement theory in classical mechanics" von Neumann model Hamiltonian 2020`

Search results were discovery only. Theorem/source claims below use the opened primary pages.

## Primary sources

1. So Katagiri, “Measurement theory in classical mechanics,” *Progress of Theoretical and Experimental Physics* 2020(6), 063A02, DOI [10.1093/ptep/ptaa065](https://doi.org/10.1093/ptep/ptaa065), arXiv: [1911.07563](https://arxiv.org/abs/1911.07563). Version metadata and abstract: arXiv abstract page. Passage read: arXiv HTML §5, lines 203–241 (von Neumann model in classical/KvN formalism), including equations (5.1)–(5.12). Level: passage. The passage gives the model Hamiltonian (H=xP), Liouvillian, pointer shift (X\to X+x), target momentum translation (p\to p-P), and explicitly says the interaction is nontrivial.

2. David Theurel, “Incompatible observables in classical physics: A closer look at measurement in Hamiltonian mechanics,” *Physical Review E* 110, 024124 (2024), DOI [10.1103/PhysRevE.110.024124](https://doi.org/10.1103/PhysRevE.110.024124). APS abstract page read: title/author/date/DOI and abstract, lines 71–92 of the opened page. Level: abstract. It studies joint Hamiltonian evolution of an object and finite-temperature apparatus and reports an apparatus-specific precision–disturbance scale, while explicitly saying it is not universal and vanishes only in an unreachable zero-temperature limit in that model. Full article was access restricted; no equation-level claim is taken from it.

## Findings and per-result classification

* **Canonical probe shears and exact pointer/back-reaction formulas.** Katagiri §5 is a close prior model for the source-side structure: (H=xP) shifts the pointer by the target coordinate and translates target momentum by the pointer momentum. The two R05 shears (G_x=\alpha x\pi), (G_P=\beta P\rho) are a classical canonical, two-channel specialization/generalization with separate gains and a second readout. Classification: **derived consequence / specialization**, not an exact literature match. The source uses KvN operators to represent classical mechanics; R05 uses ordinary symplectic phase-space variables and rectangular preparations. Quantum operator commutators, projection, and \(\hbar\) are not premises of R05.

* **Accuracy–disturbance products and quiet preparations.** Katagiri establishes interaction-induced pointer shift and momentum translation, but does not establish R05’s support-width products (s_qt_q), (s_rt_r), their units, or their infimum under width scaling. Theurel’s abstract supports the relevance of apparatus preparation and a possible apparatus-specific positive scale, but its finite-temperature/built-apparatus premise is different. Classification: **candidate contribution (bounded coverage)** for the exact rectangular support countertest; **unmatched** as a universal claim. R05 correctly treats the zero-width limit as an ideal singular preparation and the finite-width infimum as a model-family statement.

* **Inverse observation amplification and finite-horizon \(\delta^4\) preparation.** Neither source studies the R04 sampled three-body map, its (B_\delta^{-1}=O(\delta^{-3})) conditioning, or the (N=O(\delta^{-1})) accumulated-disturbance estimate. Classification: **candidate contribution**, with prior-art coverage limited to generic classical measurement interaction. The written proof is internally sound provided the R04 block bound, compact-shell flow bound, fixed gains, and uniform rectangular support assumptions are retained.

* **No action floor from ideal readout alone.** The sources do not establish a universal positive action constant. Theurel’s abstract points in the opposite methodological direction: any positive scale is apparatus-specific in the stated model. Classification: **derived consequence of R05’s explicit model**, not a source theorem; its scope must remain restricted to externally switched impulsive instruments and scalable preparations.

## Written proof check

The Hamilton equations for (G_x=\alpha x\pi) give (q^+=q+\alpha x) and (P^+=P-\alpha\pi); those for (G_P=\beta P\rho) give (r^+=r+\beta P^+) and (x^+=x+\beta\rho). Thus the stated errors and disturbances follow directly, including the (-\alpha\pi) contribution to the second momentum readout. The products have action units because position times momentum is action, while \(\alpha\) is dimensionless and \(\beta\) has units (T/M).

With widths (O(\eta^p)), the exact R04 error identity multiplies the probe terms by (B_\delta^{-1}=O(\eta^{-3})), giving hidden-state error (O(\eta^{p-3})). Setting (p=4) gives (O(\eta)). There are (O(\eta^{-1})) kicks, each (O(\eta^4)), so the accumulated trajectory displacement is (O(\eta^3)). The table’s probe kinetic-energy estimate is (O(\eta^8)) per probe times (O(\eta^{-1})), hence (O(\eta^7)), under fixed positive probe masses. No numerical or symbolic verification was run.

The conclusion requires the stated changing preparation and apparatus schedule. It does not apply to a fixed apparatus, a fixed nonzero noise floor, finite-duration passive couplings, or a preparation class with a uniform lower width/resource bound. The source literature therefore leaves R06’s finite-duration resource question open.

## Proposed BibTeX

```bibtex
@article{Katagiri2020Measurement,
  author = {So Katagiri},
  title = {Measurement theory in classical mechanics},
  journal = {Progress of Theoretical and Experimental Physics},
  year = {2020}, volume = {2020}, number = {6}, pages = {063A02},
  doi = {10.1093/ptep/ptaa065}, eprint = {1911.07563}, archivePrefix = {arXiv}
}
@article{Theurel2024Incompatible,
  author = {David Theurel},
  title = {Incompatible observables in classical physics: A closer look at measurement in Hamiltonian mechanics},
  journal = {Physical Review E}, year = {2024}, volume = {110}, pages = {024124},
  doi = {10.1103/PhysRevE.110.024124}
}
```

## Source-to-model test

Impose one finite apparatus class with a nonzero lower bound on pointer phase-space width or preparation energy, while retaining the two-shear map. Recompute the support products and the (B_\delta^{-1}) propagated error symbolically in the written derivation: determine whether the imposed bound yields a positive action-valued resource floor, or only a divergent observation cost as \(\delta\to0\). This directly separates Theurel’s apparatus-specific scale premise from R05’s scalable quiet-preparation countertest.

## Coordinator verification and acceptance classification

On 2026-09-10 the coordinator opened the arXiv abstract and rendered HTML
[version 2, section 5](https://arxiv.org/html/1911.07563#S5), equations
(5.1)–(5.12), and the APS abstract. The arXiv metadata verifies the journal
identifier above. The worker's rendered line numbers are not durable anchors:
in the coordinator view section 5 occupied lines 235–273. An attempted v3
HTML route returned 404; the verified version is v2, dated 21 June 2020.

There is a sign inconsistency between the derivative expression (5.3) and its
simplification (5.4) as rendered. We use the interaction Hamiltonian and the
explicit state translations (5.7)–(5.10) as the precedent; R05's signs are
derived independently from Hamilton's equations. No source Liouvillian sign
convention or uncertainty theorem is imported into the proof.

Final classification: C066–C067 are **derived consequences of the stated
canonical model and linear-flow estimates, with novelty unassessed**. The
worker's candidate-contribution labels record lack of a match in its small
coverage, not evidence for novelty. A lower preparation-energy bound alone
need not impose a position-momentum width product; R06 must derive that link
from an explicit confined or thermal apparatus before using it. Theurel is
abstract-level motivation only. His full assumptions and proof remain a
bounded passage-reading task for R06. No universal quantum identification or
fixed-resource realization has been accepted.
