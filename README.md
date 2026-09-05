# Navier–Stokes and Yang–Mills assessment

Initial orientation: 2026-09-05. This repository is for assessing arguments about
the Navier–Stokes and Yang–Mills existence and mass gap Millennium problems.
The first comparison milestone is complete. The next discussion concerns a more
complicated toy model to be supplied by the user; work on the Millennium problems
themselves is outside the present scope.

## First milestone

- [Exact definitions](notes/millennium-problem-definitions.md): equations, assumptions and official targets.
- [Comparison and bridges](notes/comparison-and-bridges.md): scaling, geometric and parabolic connections, and distinctions between spectral gaps.
- [Source catalogue](docs/README.md): five local PDFs with reading notes and checksums.
- [Milestone review](reviews/first-milestone.md): verification scope and remaining limitations.

## Mathematical scope

See [the problem definitions](notes/millennium-problem-definitions.md) for the
equations, admissibility conditions, alternatives A–D and quantum mass gap requirement.

- Navier–Stokes: retain the exact alternatives A–D in Fefferman's statement,
  including dimension, domain, initial data, forcing and solution class.
- Yang–Mills: retain quantum existence on four-dimensional spacetime for every
  compact simple gauge group and a positive physical mass gap. Classical field
  regularity, a finite lattice gap or an auxiliary stochastic-flow gap alone
  does not establish this result.
- Connections are initially comparisons, not asserted reductions. Each proposed
  transfer must identify the objects, hypotheses and conclusion it preserves.

The common analytic concern is control across scales and limits: nonlinear
interactions can defeat estimates available at a fixed resolution. The tasks
differ: fluid regularity concerns evolution from smooth data; quantum existence
concerns a field theory, and its mass gap concerns the spectrum above the vacuum.
Yang–Mills heat flow and stochastic quantisation offer a concrete place to compare
parabolic methods, but their auxiliary time must be distinguished from physical
time. Results in lower dimension must keep that qualification.

## Proposed tools

| Tool | Purpose | When to introduce |
| --- | --- | --- |
| Primary-source browsing, PDF extraction, BibTeX | Exact theorem statements, versions and page references | Initial source dossier |
| Git and Markdown | Durable assumptions, claims, dependencies and objections | Now |
| Python with symbolic and scientific libraries | Check algebra, scaling and small reproducible experiments | A concrete calculation needs it |
| Exact arithmetic or interval arithmetic | Certify a bounded computational claim with explicit error control | Numerical evidence becomes part of an argument |
| Lean 4 and mathlib | Check selected formal statements and their proofs | A useful lemma and formalisation feasibility are identified |
| LaTeX and a document build | Produce a coherent assessment for review | Notes mature into a report |

Lean review must inspect the statement and transitive axioms, not just compilation.
Any unproved assumptions remain visible. Numerical experiments need an identified
mathematical question, reproducible parameters and a statement of what they cannot
establish. A larger computation is justified by a specific question, not by the
reputation of the problems.

Local executable discovery on 2026-09-05 found `python3`, `pdftotext`, `pandoc`
and `git` on PATH. It did not find `julia`, `sage`, `lean`, `lake` or `latexmk`.
This is not a complete software inventory; Python packages were not inspected.
No software was installed during this orientation.

## Proposed agent roles

These are roles to activate for bounded tasks, not agents launched for this note.
The session currently permits the coordinator plus three simultaneous subagents;
roles can therefore run in stages.

| Role | Reviewable output |
| --- | --- |
| Coordinator | Shared definitions, dependencies and an assessment that resolves disagreements |
| Navier–Stokes analyst | Exact PDE claims, norm estimates and the first unsupported regularity step |
| Yang–Mills analyst | Construction, axioms, gauge invariance and continuum/infinite-volume/gap obligations |
| Adversarial reviewer | Attempts to break an argument through examples, missing hypotheses and limit failures |
| Source auditor | Verified theorem citations and a comparison between cited and used hypotheses |
| Computational/formal checker | Reproducible calculations or checked lemmas, with their scope and assumptions |

Use independent first readings for substantive claims. Agreement among agents of
the same model is not independent mathematical verification. An objection should
identify an equation, hypothesis or counterexample; final acceptance should rest
on evidence, with external specialist review for substantive new claims.

## Suggested growth of the repository

Create directories when they acquire actual content:

```text
docs/          Source catalogue, originals and checked reading notes
notes/         Problem statements, common notation and comparisons
claims/        Claims, assumptions, dependencies, status and objections
experiments/   Reproducible scripts and outputs
formal/        Selected formal lemmas and pinned toolchain
reviews/       Independent assessments and resolved or outstanding objections
```

The first substantive deliverable is linked above. When the user's toy model arrives,
identify its own mathematical target and compare its structures with the documented
bridges before assessing any argument about it.
Use statuses such as sourced theorem, checked derivation, conditional claim,
heuristic, numerical evidence and refuted claim. Do not count one as another.

## Sources consulted

- [Fefferman, official Navier–Stokes problem description](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf), especially pp. 1–2.
- [Jaffe and Witten, official Yang–Mills problem description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf), especially pp. 5–8.
- [Chandra, Chevyrev, Hairer and Shen, Stochastic quantisation of Yang–Mills–Higgs in 3D](https://arxiv.org/abs/2201.03487). Consulted abstract for the scope of the parabolic connection; this is not a four-dimensional mass gap result.
- [Lean reference: axioms](https://lean-lang.org/doc/reference/latest/Axioms/), for transitive axiom auditing.
- [OpenAI, GPT-6 Astra release](https://openai.com/index/gpt-6-astra/).
- [OpenAI, Ten advances in mathematics and theoretical computer science, 2026-08-01](https://openai.com/index/ten-advances-in-mathematics/).

The OpenAI pages report mathematical research advances and formal certificates.
They were read as release context, not as audited mathematical proofs. They do
not establish whether either Millennium problem was attempted internally.
