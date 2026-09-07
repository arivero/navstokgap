# A short derivation of Feynman formula

Rivero proposes controlling a joint refinement limit by a finite scale, then
composing kernels over inserted positions. This supplies the next toy-model test.

- Author: Alejandro Rivero; arXiv:quant-ph/9803035v1, submitted 14 March 1998.
- [Primary record](https://arxiv.org/abs/quant-ph/9803035v1),
  [PDF](https://arxiv.org/pdf/quant-ph/9803035v1).
- Coverage: all three pages read on 2026-09-06; selected equations revisited
  2026-09-07. PDF extraction; the generated title-page date differs from the
  submission date, which supplies the bibliographic year.
- Anchors: p. 1, (1)–(4), finite-dimensional oscillatory proposal; p. 2,
  (5)–(9), two regulators and Wilson–Kogut control; p. 3, (10) and final
  paragraph, scale transformations and groupoid composition.
- Status: working proposal. The transformation in (6) is left unspecified;
  its convergence equivalence requires a separate proof.
- Rights: link to arXiv; any downloaded research copy stays in ignored `.build/`.

## Use in this project

M05 retrieved a stable copy on 2026-09-07:
`.build/m05/Rivero_FeynmanFormula_1998.pdf`, SHA-256
`f4ac9355052c93c724c55c0354b080b6851cd6185eb4d84bbfdc60d51617349b`.
Printed p. 2, equations (5)–(9), was visually checked. The exponent in (5)
contains the time step multiplying the Lagrangian sum. Track that factor
explicitly when interpreting the proposed proportionality of regulators.

Write the finite-dimensional blocking map first, including its normalization,
then track mesh size and action scale independently. The
[research note](../notes/cone-time-refinement.md) routes this reading into M04.
The completed [M05 audit](../papers/regulator-limits.tex) now supplies the
partition determinant, single-quadratic critical-point normalization and an
explicit running-coefficient map. Printed p. 1 was visually checked again
during coordinator review of B08.
