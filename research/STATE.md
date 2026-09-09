# Restart state

**Hard rule, 2026-09-09:** no creation or execution of Python numerical or
symbolic verification scripts, by coordinator or workers. Use written proofs
and source review. Historical check commands are inactive records. Document,
source, link and integrity tooling remains allowed; no language workaround.

Updated: 2026-09-09. Current milestone: M07/B28 complete.

## Current restart decision

Start **A15**, selecting an action observable for bound mechanics.
**M07/B28** integrated the known Kepler threshold and proved that any fixed
softened core admits arbitrarily small angular actions (C052–C053).
See [M07 handoff](handoffs/M07.md). Long-window displacement response is a transport observable; the
original bound-orbit target needs an explicit local/mesoscopic comparison.
Read [I004](../ideas/I004-bound-action-and-transport.md), the
[B27 source capsule](../references/batches/B27.md) and the
[repository review](../reviews/repository-review-2026-09-09.md).

**A14** remains a bounded renewal-preparation diagnostic. **R02** preserves and
audits the repaired I003 finite-propagation ideas. **A16** tests scale-changing
dilations against the proposed axioms. M06, G03, Q01 and the historical/source
queues remain live supporting tracks. No new claim ID was accepted in P03.

The hard-rule loophole in `make figures` is closed; it now refuses to execute
the legacy symbolic-check generator. Use `make check` and `make papers` for
document validation. See [P03 handoff](handoffs/P03.md).

## Milestone history

The following entries preserve the sequence of decisions. Their “next” tasks
are historical; the current restart decision above and TASKS govern dispatch.

**A13/B26 are complete.** Collision paper §6 compares ordered and Poisson
streams at fixed mass, speed, density and mean collision rate. The ordered
Palm tag is a stationary square wave; its displacement variance stays bounded,
giving $\mathsf h(\Delta)\le m/(3\rho^2\Delta)\to0$. C051 changes joint
position–velocity correlations, including mark independence. **A14** tests
stationary renewal streams with variable gap variance at fixed mean gap.
See [A13 handoff](handoffs/A13.md). One Luna-low audit; written verification only.

**A12/B25 are complete.** The collision paper derives a mechanical clock from
the two-speed Poisson hard-point gas: $\lambda=\rho u$, $H_*=mu/\rho$.
Every particle retains speed $u<c$. Independent spatial gaps supply the waiting
times; density and prepared speed supply the action value. C050 has a Luna-low
source audit and coordinator written proof/source review, with no numerical
scripts. **A13** holds mass, speed and density fixed and changes spacing
correlations. See [A12 handoff](handoffs/A12.md).

**A11/B24 are complete.** The existing receiver paper now contains the
periodic-chain limit $\Theta\sqrt{m/k}$, opposite iterated limits, a joint
window regime and the fixed-phase speed-ceiling obstruction C048–C049.
One Luna-low audit and coordinator proof/check review support the extension.
The A06/A09a return-bridge papers are consolidated, preserving their proofs
and source records; the paper review maps further A01–A09 opportunities.
A12 will specify a bounded-velocity receiver
and its preparation before attempting another plateau derivation.

**A10/B23 are complete.** The [conservative receiver note](../notes/conservative-harmonic-receiver.md)
derives the exact finite-network covariance and action observable from an
invariant fixed-energy preparation. Its long-window limit is zero at fixed
centre velocity; random centre velocity adds a ballistic term. C047 has
coordinator review, one Luna-low audit and 15 exact checks. **A11** next fixes
an increasing network, tagged spectral measure and energy allocation, then
compares receiver-size and window limits. See [A10 handoff](handoffs/A10.md).

**G02/B22 are complete.** The [expanded gap note](../notes/susceptibility-gap.md)
gives an injective-velocity fixed-plateau gap-closing family and a local-frame
product bound. C045–C046 have the saved Luna-low audit, coordinator source/proof
review and 14 grouped finite checks. **A10** now tests a finite conservative
harmonic receiver: derive its velocity correlation and action observable,
separate centre drift from internal modes, and identify the limit needed for
a preparation-independent positive plateau. See [G02 handoff](handoffs/G02.md).

**Restart tooling updated:** `skills/principia-action/SKILL.md` now routes work
through the five action-selection obligations. The new
`skills/navstokgap-bibliography/SKILL.md`, loaded by AGENTS on context recovery,
uses [source-idea cards](../references/IDEA_BRIDGES.md) to supply a concrete
next test. G02's saved Luna-low B22 audit has now been integrated. See the
[restart-skills handoff](handoffs/restart-skills-2026-09-08.md).

## Current results and next tasks

**A07/B21 are complete.** [The bounded-turn note](../notes/bounded-acceleration-return.md)
proves the sharp duration and kinetic-cost minimum and uniform quadratic
polygon-error bound. C043–C044 have one sequential Luna-low audit,
coordinator proof/source review and 27 finite checks. Fourteen PDFs now build.
**G02 is next:** weakened access to internal modes and composition. Mechanical
realization by a specified conservative receiver remains a separate step;
A09 retains preparation independence and coherent-action scale selection.

**G01/B20 are complete.** [The susceptibility/gap note](../notes/susceptibility-gap.md)
proves a lower gap bound from complete observable coverage and bounded total
response. A fixed positive velocity plateau can miss a closing internal-label
gap. C041–C042 have one sequential Luna-low audit, coordinator review and
20 finite checks. Thirteen PDFs now build. **A07 is next** to mechanically
realize finite-duration reversals and test force-dependent action bounds;
**G02** follows the observability criterion under weakened access/composition.
A09 retains the independent preparation and coherent-action selection tasks.

**A09b/B18 are complete.** [The checkerboard note](../notes/checkerboard-dynamics.md)
matches the primary recurrence in an explicit basis and proves its strong
Dirac wavepacket limit. Repeated direction measurements give a ballistic
fixed-coefficient cut limit, distinct from finite-rate telegraph motion.
C039–C040 have one sequential Luna-medium audit and addendum, coordinator
source/proof review, 28 exact checks and three Fourier-mode tests. Twelve PDFs
were built at that checkpoint. G01 then tested velocity susceptibility,
spectral products and hidden slow modes. Parent A09 retains preparation independence and the physical
identification of the classical plateau with the coherent action parameter.

**A09a/B17 are complete.** [The crossover note](../notes/bridge-crossover.md)
gives the exact count-conditioned beta midpoint law and the full action-valued
crossover $g(z)=zR(z)[1-R(z)]$, with cubic onset and limit one.
It proves the common-finite-window obstruction to positive universality across
arbitrarily small masses. C037–C038 have one sequential Luna-medium audit,
coordinator review, 29 exact checks and seven numerical comparisons.
This preceded A09b's direct checkerboard passages and the
real/complex two-component recurrence. The broader A09 task remains active;
preparation independence and quantum identification stay open.

**A08/B16 are complete.** [The composition note](../notes/composition-universality.md)
proves conditional mass universality and a positive-reference theorem:
composition plus one finite-rate, nonzero-speed telegraph constituent fixes a
common positive Green–Kubo plateau. C035–C036 have one Luna-low audit,
coordinator source/proof review and five dedicated algebra checks, alongside
P02's product-chain checks. Preparation independence and the quantum role
remain explicit A09 obligations. **A09 uses**
P02's existing crossover/midpoint/continuation calculations as drafts, followed
by G01. B11 and A07 retain their secondary tasks.

**The six-direction programme review is complete** (priority history).
[The critical review](../reviews/six-directions-2026-09-08.md) puts **A08**
composition first: mass additivity of the coefficient, its preparation domain,
correlations and full-law closure. **A09** follows with finite-speed crossover,
conditional bridge moments and real-versus-complex checkerboard dynamics.
**B15** (one Luna medium, coordinator review) verified the two remembered
1984 journal identifiers; full formula passages remain to be read. **G01**
gets the velocity-gap product and a slow-mode observability test. A07 remains
a supporting force-control calculation. The review changes priorities; C001–C034
retain their existing acceptance status, and prospective results await their
dedicated prior-art audits. See [selection target](ACTION_FIELD_TARGET.md).
An independent session then verified the A08/A09/G01 starting calculations
in [the six-direction checks note](../notes/composition-crossover-gap-checks.md):
product-chain composition, the cubic midpoint onset of the C033 bridge, the
slow-mode gap test and both continuation routes, with 28 exact checks.

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
and twelve exact checks. **A06/B14 are complete:** the
[return-bridge note](../notes/telegraph-return-bridge.md) constructs a
velocity-resolved bridge with midpoint atom $1/I_0(\lambda T)$ and exact
restriction consistency. Its polygon action error is bounded by
$mu^2N_T|\pi|/2$ and vanishes in mean and almost surely. C033–C034 have
a Luna medium audit, coordinator review, 12 symbolic checks and 45 rational
partition cases. **A07** replaces impulses by bounded-acceleration turns:
derive the sharp return-duration and kinetic-action bounds at prescribed
opposite endpoint velocities, then test their scaling.
See [CUT_POINT_TARGET.md](CUT_POINT_TARGET.md).
A04 preserves the
spatial-clock question as a secondary diagnostic.
**B11 is ready to resume:** the original Sol medium audit of the supplied polygon
ideas failed on authentication and left no worker artifacts; B12–B15 have since
run successfully. The coordinator's
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

Run `make check` and `make papers`. Checks cover local links, source companions, citation keys and source checksums. The PDF build
checks reference resolution and layout overflow. Current mathematical verification uses written proofs and source review;
symbolic checks are historical artifacts. Lean work starts at F01.

Python/SymPy/Matplotlib, Pandoc, pdfLaTeX and BibTeX are available. BibTeX runs
inside `.build/<paper>/` with the repository on `BIBINPUTS`, preserving
TeX's file-write security settings.

## History and handoffs

- [A09a handoff](handoffs/A09a.md): exact beta midpoint law, crossover limits,
  boundary-mean correction and common-window mass constraint; B17 audit.

- [A08 handoff](handoffs/A08.md): conditional shared positive plateau,
  product-state closure, preparation/correlation tests and B16 source review.

- [Six-direction review handoff](handoffs/P01-six-directions.md): A08/A09/G01
  priority, B15 metadata verification and preserved acceptance gates.
- [P02 checks handoff](handoffs/P02-six-direction-checks.md): exact verification
  and extension of those directions; sampler table and uncompiled Lean draft.
- [H06 handoff](handoffs/H06.md): pre-1901 primary sources in `docs/classics/`
  for retrieval context, with companions, checksums and BibTeX.
- [H07 handoff](handoffs/H07.md): second batch, least action across physics,
  Newton's Book III rules and scholium, and Planck's first value of h.
- [H08 handoff](handoffs/H08.md): the paradox of the cut from Democritus to
  Cavalieri, with Arabic and Chinese witnesses, and the I003 idea entry.
- [H09 handoff](handoffs/H09.md): the 1634 letter verified as no. 2992 of
  2 October, Guldin's Book IV pages, the Latin reception, and test 1 of I003.
- [I003 handoff](handoffs/I003-tests.md): rigidity of light-cone dynamics to
  first-order systems, the commutator scale, and the double-limit obstruction.

- [A06 handoff](handoffs/A06.md): exact return bridge, midpoint atom and
  endpoint-version choice; vanishing polygon error. Nine PDFs now build.

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
