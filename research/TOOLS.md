# Tooling and reproduction

The current toolchain supports exact calculations, source extraction and readable
papers. On 2026-09-05 it comprised Python 3.12.3, SymPy 1.14.0,
Matplotlib 3.10.9, pdfTeX (TeX Live 2023/Debian), BibTeX 0.99d,
Pandoc and Poppler.

## Commands

**Hard rule, 2026-09-09:** mathematical verification uses written derivations and source
review. Do not create or run Python numerical or symbolic spot-check scripts.
Prior scripts and outputs remain historical artifacts. Document builds, source
extraction, metadata, checksums and link validation remain permitted; a new
computational-verification workflow requires user direction.

From the repository root:

```sh
make check
make papers
make figures
```

| Command | Checks or output |
| --- | --- |
| `make check` | Source checksums, companions, local links and citation keys only |
| `make papers` | Regenerates programme/note LaTeX and accepted PDFs; checks unresolved references and layout overflow |
| `make figures` | Regenerates the constant-force illustration |

The manuscript supplies the analytic arguments; these commands verify their
computational and document artifacts. TeX runs with shell escape disabled,
intermediates in `.build/` and final PDFs in `out/papers/`.

The earlier mathematical scripts record past work and are excluded from
`make check`. M03's spectral manuscript awaits proof review and build integration.

## Dependencies

`requirements.txt` pins the directly used Python libraries, including NumPy
for A09b's finite Fourier-matrix convergence checks. For a
project-local environment:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
make check PYTHON=.venv/bin/python
```

LaTeX requires article class, lmodern, amsmath, amsthm, amssymb, geometry, hyperref,
booktabs, longtable and BibTeX. Pandoc generates the programme TeX from Markdown.
PDF metadata may vary between builds; validation concerns content and reference
resolution. A fully locked environment is a future reproducibility enhancement.

## Tool adoption

| Tool | Task that justifies it |
| --- | --- |
| Lean 4 + mathlib | F01: formalise the selected small-amplitude lemma with a pinned toolchain |
| Interval arithmetic or numerical ODEs | Requires new user direction; outside the current verification workflow |
| OCR | Recover selected scan passages, followed by visual equation checking |
| arXiv/INSPIRE APIs | Retrieve bounded source batches with queries, versions and dates recorded |
| Larger simulation or symbolic tools | Requires new user direction |

The existing stack suffices for this milestone. Lean/Lake and latexmk were absent
from the inspected PATH; F01 records the planned formalisation setup.

## Formalisation and agent workflow

Follow the official [Lean setup guide](https://lean-lang.org/install/manual/)
when F01 begins. Acceptance includes statement/definition review, a clean build
and transitive axiom inspection with `#print axioms`, following the
[proof-validation guidance](https://lean-lang.org/doc/reference/latest/ValidatingProofs/).
The [formalisation plan](../formal/README.md) gives the candidate theorem.

Use Luna for bounded metadata/search work and Sol for equation collation and
small calculations. The coordinator handles model selection, assumption tracking
and result acceptance. Apply the cost and effort rules in
[agents/PROTOCOL.md](../agents/PROTOCOL.md).
