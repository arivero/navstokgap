# Restart state

Updated: 2026-09-06. Milestone complete: persistent research programme and first paper drafts.

## What a fresh agent should know

- User cost constraint: never select `ultra`, including through subagent
  inheritance. Explicitly choose a supported non-ultra effort and announce/record
  model plus effort for each dispatch. See `agents/PROTOCOL.md`. This rule was
  added after the first milestone; it does not relabel historical dispatches.
- Actual project: Newtonian trajectories, action scales and mechanisms for gaps.
  The Millennium comparison is completed preparation, not permission to attempt
  either Millennium problem in this repository now.
- Desired outcomes: a justified quantum reconstruction and/or a gap-producing toy
  model. These are research targets, not results already established.
- Existing result: constant-force chord/curve action identity and a family of
  arbitrarily small nonzero action differences. See claim C001/C002 and the note.
- Technical continuation: three proved control/conditional propositions in
  `papers/action-gap-foundations.tex`, internally reviewed in R01. They do NOT
  prove the existence of a new action field, force a positive Planck constant,
  or establish a universal action/mass gap.
- History: later English Principia openings have been read. A complete Classical
  Scholia corpus audit has NOT been completed. No evidence yet establishes that
  doubts about shrinking areas delayed the 1687 edition.
- The user added Newton Project NATP00385. Its title is *Unarranged fragments,
  mostly relating to the dispute with Leibniz*. It is not itself a catalogue entry
  for the six Book III Classical Scholia. Normalized text hides deletions.

## Reading order and continuation

1. `AGENTS.md` and `research/PROGRAMME.md`.
2. `research/TASKS.md`; select one ready task with its dependencies satisfied.
3. `claims/LEDGER.md`, then only the routed notes/sources and applicable skills.
4. Run `make check` and, for manuscript edits, `make papers`.
5. Record exact files, commands/results, unresolved questions and next task here
   before ending. Workers return a handoff; only the coordinator updates this file.

Product-level goals, running terminal IDs and chat summaries are not durable task
state. Do not assume an earlier tool process or subagent is still running. Inspect
`git status --short` before modifying anything; preserve unrelated user changes.

## Completed integration and next action

- P00/M01/R01 complete: programme, role cards, claims/ideas separation, two
  LaTeX/PDF drafts and internal mathematical review.
- B01 complete as a bounded Luna search: six primary leads; coordinator checked
  metadata/abstracts and Wootters's opening discussion, integrated shared BibTeX.
  Reconstruction proofs remain unaudited. Start Q01 with Hardy and
  Chiribella–D'Ariano–Perinotti when that task is selected.
- H01 complete as a focused Sol audit: official NATP00385 normalized/diplomatic/XML
  originals with checksums and companions. The shelf-folio versus internal-label
  concordance is uncertain. No full manuscript or facsimile reading is claimed.
- Next bounded mathematical task: M03 (oscillator Hessian versus energy gap;
  free line versus circle). Independent source task: H02 (Classical Scholia
  six-entry corpus/access inventory), with saved seeds in `references/batches/`.
- No live worker or long-running process is needed to resume. Role files are
  task instructions, not a background autonomous service.

## Reproduction and limitations

`make check` and `make papers` pass. Python syntax compilation and the skill
validator pass. Both LaTeX builds resolve references and have no overfull-box
warnings. Representative PDF pages were visually inspected; this is not a
page-by-page publication proofread. Source checksum verification covers all
registered originals, including the three new Newton representations.

No scientific software installation was required: Python/SymPy/Matplotlib,
Pandoc, pdfLaTeX and BibTeX were present. Lean remains a deferred F01 feasibility
task with an explicit theorem target; there is no formal certificate.

The first full build exposed BibTeX's refusal to write an absolute output path.
The build now runs BibTeX inside its dedicated `.build/<paper>/` directory with
the repository on `BIBINPUTS`. Do not disable TeX security settings to work around it.

## Prior milestones

- `31908fb`: official Millennium statements and comparison.
- `2cb1554`: Principia source dossier, constant-force calculation and reusable skill.

- This milestone is recorded by the commit titled `Establish restartable action-gap research programme and papers`.
  Use `git log -1 --format='%h %s' --grep='Establish restartable action-gap'`
  to resolve it; the state file deliberately does not contain a self-referential
  commit hash. Detailed integration record: `research/handoffs/P00.md`.
