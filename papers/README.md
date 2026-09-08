# Papers

- `action-gap-foundations.tex`: area–action identity, variation propositions,
  Jacobi operator, free kernel and quantum finite-copy threshold.
- [time-refinement.tex](time-refinement.tex): exact Gaussian blocking, surviving
  action parameter, conditioned classical-path limit and oscillatory counterpart;
  [PDF](../out/papers/time-refinement.pdf). Literature/assumption audit B06.
- [regulator-limits.tex](regulator-limits.tex): arbitrary-partition normalization,
  finite action defect in a classical-path limit, speed control, stationary phase
  and a two-regulator scaling map; [PDF](../out/papers/regulator-limits.pdf).
  Per-result source/proof audit B08 and 24 exact finite checks.
- [classical-action-field.tex](classical-action-field.tex): positive action
  plateau from finite reversible velocity memory, exact telegraph example and
  limit-order test; [PDF](../out/papers/classical-action-field.pdf).
  B09 source audit, coordinator proof review and 16 exact checks.
- [collision-action-relaxation.tex](collision-action-relaxation.tex): physical-time
  action relaxation in an elastic refreshed bath, with explicit scale inputs;
  [PDF](../out/papers/collision-action-relaxation.pdf). B10 audit and 15 checks.
- [cut-point-consistency.tex](cut-point-consistency.tex): generated from
  [the maintained note](../notes/cut-point-consistency.md); arbitrary cuts,
  fixed-parameter bridge consistency and one-node action cost.
  [PDF](../out/papers/cut-point-consistency.pdf), B12 audit and nine checks.
- [physical-cut-speed.tex](physical-cut-speed.tex): generated from
  [the maintained note](../notes/physical-cut-speed.md); elastic midpoint cuts,
  sharp finite-speed variance bound and ballistic convolution theorem.
  [PDF](../out/papers/physical-cut-speed.pdf), B13 audit and twelve checks.
- [telegraph-return-bridge.tex](telegraph-return-bridge.tex): generated from
  [the maintained note](../notes/telegraph-return-bridge.md); conditional
  count/simplex construction, midpoint atom and consistent polygon-action limit.
  [PDF](../out/papers/telegraph-return-bridge.pdf), B14 audit, 12 symbolic checks
  and 45 rational partition cases.
- [composition-universality.tex](composition-universality.tex): generated
  from [the composition note](../notes/composition-universality.md); conditional
  mass universality, positive reference and preparation tests.
  [PDF](../out/papers/composition-universality.pdf), B16 and five algebra checks.
- `research-programme.tex`: generated from `research/PROGRAMME.md` using
  `programme-template.tex`. Edit the Markdown and run `make programme`.

Run `make papers` from the root to regenerate the programme and build all ten
PDFs in `out/papers/`. Bibliographic metadata lives in
`references/library.bib`; build intermediates live in `.build/`.
The tracked TeX/PDF pairs provide readable outputs and editable source.

`spectral-gap-laboratory.tex` is the preserved M03 working draft. Its B04
literature audit is complete; proof review, dedicated checks and build integration
are pending. It is outside the accepted-paper build.

The current technical draft has written proofs and internal review R01.
Publication preparation includes specialist review, citation checking,
authorship/AI-assistance disclosure and source redistribution checks.
Public submission requires user direction.
