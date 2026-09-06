# Human-readable papers

- `action-gap-foundations.tex`: authored technical note with proofs and explicit
  conditional assumptions; it makes no novelty or quantum-reconstruction claim.
- `research-programme.tex`: generated from `research/PROGRAMME.md` using
  `programme-template.tex`. Edit the maintained Markdown, then run `make programme`.

Run `make papers` from the root to regenerate the programme LaTeX and build both
PDFs under `out/papers/`. BibTeX metadata is maintained in
`references/library.bib`. Intermediates are ignored under `.build/`; final TeX and
PDFs are tracked to permit human reading before installing any tools.

Before a public version: complete independent mathematical review, check every
cited passage, settle authorship/AI-assistance disclosures with the user and
verify source redistribution rights. No submission or arXiv upload is authorized
by the ability to build a paper.
