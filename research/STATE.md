# Restart state

Updated: 2026-09-08. Current milestone: A05/B13 complete; phase-space cut test A06 next.
The M05 checkpoint `f1157b0` has been pushed to `origin/main`.

## Current results and next tasks

The [technical paper](../papers/action-gap-foundations.tex) establishes the exact
constant-force area–action identity, accumulation of positive action differences
at zero, and a finite-copy quantum action-resolution threshold. It also computes
the Dirichlet fluctuation spectrum and the free-kernel short-time limit.
[Claims C001–C008](../claims/LEDGER.md) give assumptions and review status.

The [time-refinement paper](../papers/time-refinement.tex) adds exact Gaussian
blocking, a classification of its surviving parameter, and finite-dimensional
bridge concentration. M04/B06 are complete. The strong target is the independent
physical selection of a positive universal action scale, alongside construction
of the classical limit; the current Gaussian family supplies the test setting.

The [regulator-limits paper](../papers/regulator-limits.tex) now proves a stronger
path/action distinction: $\kappa_N\to0$ and $(N-1)\kappa_N\to\ell$ give
uniformly classical paths with excess action converging in $L^2$ to $\ell/2$.
It supplies exact partition normalization, a strict-speed oscillatory control,
quadratic stationary-phase weights and an explicit running-coefficient map.
C013–C017 have a sequential Sol medium audit (B08) and coordinator review.

**A01/B09 are complete.** The [classical action-field paper](../papers/classical-action-field.tex)
proves a positive model-specific plateau from finite reversible velocity memory:
$H_*=2m\langle v,(-Q)^{-1}v\rangle_\pi$, and $H_*=mu^2/\lambda$ for
two velocities. C018–C021 have a sequential Luna medium source audit,
coordinator proof/source review and 16 exact checks.
The [central target](ACTION_FIELD_TARGET.md) keeps observation duration,
partition refinement and physical-time relaxation separate.
**A02/B10 are complete:** `papers/collision-action-relaxation.tex` derives a
covariance observable relaxing in physical time to $(m+M)s^2/\nu$ for an
elastic refreshed bath. Fifteen checks and a sequential Luna medium audit
support C022–C024. **A03/B12 are complete:** [cut-point consistency](../notes/cut-point-consistency.md)
proves the nonuniform chord bound and fixed-parameter restriction test.
At fixed Gaussian preparation each inserted node adds expected kinetic action
$\kappa/2$; retaining finite total defect by shrinking $\kappa$ changes old
node marginals. C027–C029 have a Luna medium audit and nine exact checks.
**A05/B13 are complete.** The [physical-cut note](../notes/physical-cut-speed.md)
gives an elastic momentum receiver, the sharp midpoint action bound
$\kappa_{\rm mid}\le m\Delta(u-|v|)^2$, and a deterministic-drift theorem
for ballistic position convolution laws. C030–C032 have a Luna medium audit
and twelve exact checks. Next is **A06**, a finite-speed bridge retaining
position and velocity, in [CUT_POINT_TARGET.md](CUT_POINT_TARGET.md).
A04 preserves the
spatial-clock question as a secondary diagnostic.
**B11 is waiting:** the fresh Sol medium audit of the supplied polygon ideas
failed on authentication and left no worker artifacts. The coordinator's
[receding-centre draft](../notes/receding-centre-area-audit.md) and twelve exact
checks are saved; claim acceptance awaits the resumed librarian audit.
**M06** remains the force/acceleration and relativistic-action diagnostic from
[the M05 note](../notes/two-regulator-audit.md).
**B07a** completed the Wilson–Kogut common-observable reading and test;
**B07b** retains the tangent-groupoid theorem. Each source task should change
a premise, calculation or proof obligation.

**M03 remains an unfinished draft** in `papers/spectral-gap-laboratory.tex`.
Its B04 literature audit is complete; independent proof review, dedicated checks
and PDF build integration remain. It is saved for continuation, outside the
accepted-paper build. **H02/H03** retain the Classical Scholia task and
[search seeds](../references/batches/H02-seeds.md). **H04** verified Xylander
1570 pp. 823–824; **H05** will test author-specific cone reception.

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
- Commit and push each innovation or relevant status change to the existing
  GitHub repository, as authorized on 2026-09-07.

## Completed work

| Task | Output / reading depth |
| --- | --- |
| P00 | Programme, role cards, claims/ideas structure and two LaTeX/PDF drafts |
| M01 | Three mathematical propositions and supporting calculations |
| R01 | Internal proof review; endpoint-gauge and path-continuity clarifications incorporated |
| B01 | Luna bibliography batch: six primary leads; metadata/abstract checks and selected passages |
| H01 | Sol NATP00385 retrieval and passage-level audit, with normalized/diplomatic/XML originals |
| B04 | M03 prior-art matches and derived-consequence classifications; source passages checked |
| B05 | Retrospective C001–C008 audit; Holevo–Helstrom and free-propagator anchors integrated |
| H04 | Luna medium, sequential; 1570 cone passage visually verified by coordinator |
| M04/B06 | Free-refinement proofs and algebra checks; Luna medium prior-art/assumption audit, coordinator source verification |
| M05/B07a/B08 | Joint path/action limit, partition normalization and regulator map; Wilson–Kogut source-to-model test; Sol medium four-source audit; 24 exact checks |
| A01/B09 | Finite-speed action observable, positive reversible-velocity plateau, exact telegraph and iterated limits; Luna medium audit and coordinator source/proof review; 16 checks |
| A02/B10 | Elastic collision bath and physical-time covariance-action relaxation; explicit parameter scaling; Luna medium audit and 15 checks |

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

- [A05 handoff](handoffs/A05.md): conservation, finite-speed support and the
  need for velocity memory in the chosen cut model. Eight PDFs now build.
- [A03 handoff](handoffs/A03.md): refinement consistency, source review and
  the next intervention-versus-sampling test. Seven PDFs now build.
- [A02 handoff](handoffs/A02.md): reviewed bath diagnostic and return to cut
  points; [B11 restart](handoffs/B11.md) records the authentication interruption.
- [A01 handoff](handoffs/A01.md): positive classical velocity-memory plateau,
  B09 prior-art audit, five-PDF build and the next A02 universality test.
- `31908fb`: official Millennium definitions and comparison.
- `2cb1554`: Principia dossier, constant-force calculation and context skill.
- `5816e35`: restartable programme and first papers; [P00 handoff](handoffs/P00.md).
- `79f1134`: ultra-effort prohibition.
- `fc72c72`: results-first prose across the active documents,
  regenerated PDFs and compact session instructions. Mathematical assumptions
  and evidence classifications are preserved; prior reviews and source originals
  remain archival records.
- [M04 handoff](handoffs/M04.md): source-driven refinement milestone, review
  corrections, remaining M03 work and next M05/B07 calculation.
- [M05 handoff](handoffs/M05.md): action-defect theorem, review and source
  corrections, reproduction and next M06 test.
- [Editorial review](../reviews/results-first-edit.md): verification and scope
  of the rewrite.
- [Blog introduction](../docs/blog/introducing-navstokgap.md): first-person
  article for `a.rivero.nom.es`, with the requested subtitle and public links;
  [publication notes](../docs/blog/README.md) record the model-name detail.
