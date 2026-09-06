# Tooling decisions and reproduction

Inspected 2026-09-05: Python 3.12.3, SymPy 1.14.0, Matplotlib 3.10.9,
pdfTeX (TeX Live 2023/Debian), BibTeX 0.99d, Pandoc and Poppler extraction tools
are available. Lean/Lake and latexmk were not on PATH. No new system software is
needed for this milestone; no global configuration was changed.

## Use now

From the repository root:

```sh
make check
make papers
make figures
```

`make check` validates exact algebra, elementary numerical cross-checks, source
checksums, companion presence and local Markdown links. It does not prove general
ODE existence, audit scanned formulae or certify a new physical theory.
`make papers` builds LaTeX/BibTeX with no shell escape, keeps intermediates under
`.build/`, checks unresolved citations/references, and copies PDFs to `out/papers/`.
`make figures` regenerates the existing constant-force illustration.

Python dependencies are pinned at the two directly used library versions in
`requirements.txt`; this is not a full transitive lock or a bit-for-bit container.
On another machine use a project-local virtual environment if needed:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
make check PYTHON=.venv/bin/python
```

LaTeX needs an article-class TeX distribution with amsmath, amsthm, amssymb,
geometry, hyperref, booktabs and longtable plus BibTeX. Pandoc is used to produce
the programme's checked-in LaTeX from its maintained Markdown; the technical
paper is authored directly in LaTeX. PDF builds need not be byte-identical because
TeX embeds metadata; correctness checks concern content and successful resolution.

## Introduce only with a concrete task

| Tool | Decision and trigger |
| --- | --- |
| Lean 4 + mathlib | Defer installation to F01, a bounded proof feasibility task with an accepted statement and pinned versions |
| Interval arithmetic | Add when a theorem depends on a numeric inequality requiring certified error bounds |
| SciPy / numerical ODEs | Add for a named experiment; numerical trajectories cannot settle universal existence |
| OCR | Use only for selected unreadable scans; mark uncertainty and visually verify mathematical passages |
| arXiv/INSPIRE APIs | Use public read-only search for bounded batches; record version, query and retrieval date; no API key required for basic discovery |
| Large simulations, symbolic suites, cloud provers | Not justified by the current finite-dimensional control calculations |

## Formalisation gate

See `formal/README.md`. Use the official
[Lean installation guide](https://lean-lang.org/install/manual/) when the task is
activated, not an unpinned shell installer copied into a proof script. Audit the
meaning of the theorem statement and transitive assumptions with `#print axioms`;
compilation alone cannot detect that the wrong theorem was formalised. The official
[proof-validation guidance](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)
distinguishes these checks. No Lean certificate exists in this milestone.

## Small-agent economy

Give Luna metadata lookup, bounded primary-source discovery and uncomplicated
transcription. Give Sol equation collation, extraction review and small symbolic
or formal tasks. Reserve central model selection, circularity audits and theorem
acceptance for coordinator/reviewer attention. These are workload assignments,
not guarantees of model capability. Prefer a reviewed two-page source digest to
an unreviewed corpus dump.
