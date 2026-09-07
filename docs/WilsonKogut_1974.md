# The renormalization group and the epsilon expansion

Wilson and Kogut compare cutoff theories at a common physical correlation
length. Their section 12 supplies a concrete design rule for the toy model:
choose a reference observable and specify which coefficients run to preserve it.

- Kenneth G. Wilson and John Kogut, *Physics Reports* 12 (1974), 75–199.
- DOI: [10.1016/0370-1573(74)90023-4](https://doi.org/10.1016/0370-1573(74)90023-4).
- [INSPIRE 81239](https://inspirehep.net/literature/81239): metadata verified
  through the record/API, 2026-09-07; no open-file link listed there.
- [Institutional PDF](https://theory.tifr.res.in/~tridib/ReferenceMaterial/WilsonKogut.pdf)
  retrieved 2026-09-07 into ignored `.build/m05/WilsonKogut1974.pdf`.
- Extraction: `pdftotext -layout`; scanning/OCR affects mathematical symbols.
- Rights: institutional research copy; redistribution permission unresolved,
  so original bytes remain outside the published repository.

## Selected reading and digest

Coverage on 2026-09-07: passage reading of the trajectory setup in §12.1,
printed pp. 161–165, and §12.2, pp. 166–168. The parameter is an auxiliary RG
flow parameter, distinct from physical time. Formulae and the scale comparison
on printed p. 167 (PDF page 93), and Fig. 12.7 on p. 166, were visually
checked. The source uses an
assumed simple flow topology to illustrate the renormalization construction.

On p. 167, choose a renormalized mass $\mu_R$ and a cutoff-dependent bare
interaction with dimensionless correlation length $\xi=\Lambda_0/\mu_R$.
Rescaled trajectories meet the surface $\xi=1$ at points $Q_{\Lambda_0}$;
their comparison then uses the same physical correlation length. In the
depicted topology these points approach a reference renormalized interaction.
The renormalized mass remains a free parameter. Page 168 describes the
backward-extension requirement for a renormalized trajectory to remain in the
allowed interaction space.

The construction accompanying Fig. 12.7 is the operational match we identify
for Rivero's invocation of Wilson–Kogut. The text search for “triangle” found
no occurrence; that name comes from Rivero's account.

## Source-to-model consequence

[M05](../papers/regulator-limits.tex) fixes an interior-time bridge variance
as its reference observable and explicitly runs the bare kinetic coefficient
to preserve it. This imports the common-scale comparison principle; the
positive action scale enters through the reference condition.

Stable-original SHA-256:
`770dc5bbceddf6fefed4f240aff5dd495ec1a3beea04d0c6dd771d5df8c926b6`.
