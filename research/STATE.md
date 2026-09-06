# Restart state

Updated: 2026-09-06. Current milestone: results-first revision and repository
introduction prepared for publication.

## Current results and next tasks

The [technical paper](../papers/action-gap-foundations.tex) establishes the exact
constant-force area–action identity, accumulation of positive action differences
at zero, and a finite-copy quantum action-resolution threshold. It also computes
the Dirichlet fluctuation spectrum and the free-kernel short-time limit.
[Claims C001–C008](../claims/LEDGER.md) give assumptions and review status.

Next mathematical task: **M03**, comparing oscillator Hessian and Hamiltonian
gaps, then free motion on a line and a circle. Next source task: **H02**, a
six-entry Classical Scholia inventory using the saved
[search seeds](../references/batches/H02-seeds.md).

Q01 starts with Hardy and Chiribella–D'Ariano–Perinotti. B01 supplies verified
identifiers and selected readings; Q01 will examine the reconstruction proofs.

## Session rules

- Read AGENTS, PROGRAMME and the selected TASKS entry, then the required sources.
- Lead with results and questions. Place assumptions at their point of use and
  evidence status in the ledger/companions.
- Never select ultra effort, including through inheritance. Explicitly request
  and announce the model and supported effort for each subagent.
- Delegate smaller tasks to Sol or Luna sequentially. Wait for the single
  worker, then review its handoff before continuing or dispatching again.
- Preserve user changes. Check for live workers and existing artifacts before
  reclaiming a task after interruption.
- Update task state and a handoff at completion. The repository carries the
  continuation record across sessions.

## Completed work

| Task | Output / reading depth |
| --- | --- |
| P00 | Programme, role cards, claims/ideas structure and two LaTeX/PDF drafts |
| M01 | Three mathematical propositions and supporting calculations |
| R01 | Internal proof review; endpoint-gauge and path-continuity clarifications incorporated |
| B01 | Luna bibliography batch: six primary leads; metadata/abstract checks and selected passages |
| H01 | Sol NATP00385 retrieval and passage-level audit, with normalized/diplomatic/XML originals |

NATP00385 documents Newton's account of analytic discovery and synthetic
presentation. H02/H03 address the six Classical Scholia, the manuscript-folio
concordance and the publication-delay hypothesis. The
[historical audit](../notes/newton-NATP00385-audit.md) gives exact coverage.

## Reproduction

Run `make check` and `make papers`. Checks cover algebra, measurement examples,
local links, source companions, citation keys and source checksums. The PDF build
checks reference resolution and layout overflow. The current evidence level is
written proofs with internal review and symbolic checks; Lean work starts at F01.

Python/SymPy/Matplotlib, Pandoc, pdfLaTeX and BibTeX are available. BibTeX runs
inside `.build/<paper>/` with the repository on `BIBINPUTS`, preserving
TeX's file-write security settings.

## History and handoffs

- `31908fb`: official Millennium definitions and comparison.
- `2cb1554`: Principia dossier, constant-force calculation and context skill.
- `5816e35`: restartable programme and first papers; [P00 handoff](handoffs/P00.md).
- `79f1134`: ultra-effort prohibition.
- Current editorial revision: results-first prose across the active documents,
  regenerated PDFs and compact session instructions. Mathematical assumptions
  and evidence classifications are preserved; prior reviews and source originals
  remain archival records.
- [Editorial review](../reviews/results-first-edit.md): verification and scope
  of the rewrite.
- [Blog introduction](../docs/blog/introducing-navstokgap.md): first-person
  article for `a.rivero.nom.es`, with the requested subtitle and public links;
  [publication notes](../docs/blog/README.md) record the model-name detail.
