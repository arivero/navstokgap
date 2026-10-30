# Start here

Language models reading this repository cold should also read
[`LLM.md`](LLM.md) (served as `llms.txt` on the site): what is proved and
at what level, what is open, which errors were already caught, and the
verified prior art. This file says how to work here.

Read `research/STATE.md` for the current question and the maintained
argument it points to. These instructions, STATE and the catalog replace
the retired handoffs, task lists and programme versions. Explicit user
instructions take precedence over everything here.

[`notes/index.md`](notes/index.md) is the compact full-read retrieval
catalog. Its priorities measure relevance to the present programme;
proof status, research value and route closures are separate fields.
Use `LLM.md` for the established-result map and the maintained notes for
later results and corrections. The catalog is repository infrastructure;
`docs/` follows the website and source-archive rules.

# The scientific task

The user has suspended new research for substantive consolidation. Organize
maintained notes by question and dependency; integrate corrections, retain
independent proofs/countermodels/constants and delete superseded source notes.
Keep published URLs through the website redirect mechanism. Catalogs and commit
history supply provenance; create no new refactoring report or handoff.

The long-term open goals are Newton action necessity and continuum pure $SU(3)$
Yang–Mills existence with a finite positive physical gap. The pion is a symmetry
benchmark. Classical completion, conditional positive floors, quantum states/
dynamics/instruments and universality/calibration of physical $\hbar$ are
separate claims. Every gauge gap names its operator, units and limiting order.
A finite-box or auxiliary-clock rate is not automatically the physical gap.

Historical comparisons use the actual text, named edition and reading label.
Resemblance establishes no transmission. A modern phase interpretation supplies
no theorem that Newton derived quantum kinematics. Internal model review is not
independent peer review or evidence of literature novelty. Keep physical
$\hbar$, $h_P=2\pi\hbar$, $\epsilon=\hbar/S_0$, mesh and record regulators
explicit. No fluxional-time interpretation is an established result here.

# How to work

Be a researcher. Propose mechanisms, compare them, develop the strongest into
a derivation, construction, decisive test or informative failure. Label
conjectures. Use established theorems with their hypotheses; do not audit
borrowed proofs unless a concrete error is suspected in a result in use.
Literature is for ingredients and honest prior-art labels, never a
deliverable by itself. A session may end with "nothing worth recording"
and no artifact.

**Retrieval before every research step (user, 2026-10-01).** Before each
bounded proof unit, perform keyword retrieval across the whole repository
corpus, following the repository-local
[`poormanrag` skill](skills/poormanrag/SKILL.md) (read it on first use).
Use STATE, `LLM.md` and `notes/index.md`, then search full texts across
notes, references, research, claims, source companions and
manuscripts. Read relevant proofs and correcting/superseding notes;
carry their hypotheses and failed routes into the calculation. Repeat
when changing mechanism or track. Every worker advancing a proof
follows this rule; keep retrieval brief and create no search reports.

Maintain both the Markdown and JSON catalog entries whenever a note is added or materially
changed, after reading all its changed content and enough surrounding
argument to preserve scope. A new entry requires a full read. Keep its
summary greppable, its limitations explicit, and links to route-closing
corrections intact. Retrieval priority and a `surprising` flag express
research judgment and confer no literature novelty. Do not create a PDF
for the catalog.

Write results into `notes/<slug>.md`: lead with the result, state each
assumption where it is used, keep constants explicit, keep negations that
change a theorem's meaning, cite sources inline with a reading label
(metadata, abstract, passage, full-read). The note's last section states
the consequence for STATE. That section is the only required bookkeeping
besides the STATE edit.

Do not create handoffs for completed work, task rows, decision blocks,
programme versions, source batches, claim rows, validation narratives,
internal review files or score tables. Record completed work in one short
phrase in the existing catalog; integrate corrections and unique proof
content into their arguments. Preserve source passages and reading coverage
in existing companions. Git history retains former process records. If work
is interrupted, leave one paragraph at the top of the actual note saying
where it stopped; STATE is the only live status page.

`claims/LEDGER.md` is retained for the claims already in it. Add a row only
for a result another note will cite by ID, with the proof location and an
honest literature label in the same row; no review or librarian ritual is
required. Use `references/library.bib` for anything you cite by key.

# Cost rules

**No Python or other scripts for numerical or symbolic verification** (user
rule, 2026-09-09). Written derivations are the check. Document tooling
(pandoc, LaTeX, pdftotext, link checks, shell queries to citation APIs) is
allowed.

**No full paper rebuild.** Build only the note you changed:
`make paper NOTE=<slug>`. Never run `make papers` as a routine gate, never
inspect PDF pages as images, and never restore rebuilt PDFs by comparison.
`make check` (link and checksum integrity) is cheap and may be run.

No parallel subagents. Work alone under the current user direction; only
a necessary menial task may be delegated to 6.1 Terra. Preserve unrelated
uncommitted work. Attribute this continuation with “6.1 Sol Max” under
the user's latest correction.

Keep STATE short. Do not restate a result in more than one place.

# Repository map

- `notes/`: derivations and results (the research output).
- `research/STATE.md`: the one live priority page.
- `claims/LEDGER.md`: cited-by-ID results, frozen format.
- `docs/`, `references/`: sources, companions, bibliography.
- `papers/`, `out/papers/`: LaTeX and PDFs generated from notes.
- `scripts/`, `skills/`: tooling and repository retrieval.
- Former idea/task names are retrieval aliases in the maintained catalog.

Commits and pushes to the existing GitHub repository are authorized after
each result or status change; end commit messages with the model's
co-author trailer. Preserve other sessions' uncommitted changes. External
submissions, correspondence and paid services require separate direction.
Publication uploads must include the compiled PDF built from the included
source (user rule, 2026-09-13). Verify redistribution rights before
publishing archived editorial material.
