# Start here

Read `research/STATE.md` (one page: what is being worked on and why) and
the note it points to. Nothing else is required reading. Older governance
files (PROGRAMME, STRATEGY, TASKS, PROTOCOL, the skill, old handoffs) are
context, and where they demand more bookkeeping than this file, this file
wins. Explicit user instructions take precedence over everything here.

# The physical question

User clarification, 2026-09-14: "Newton's areas" means the difference
between inertial/polygonal motion and the actual trajectory, anchored in
Galileo's horizontal inertial line and falling parabola. Their area
satisfies (3F/v) A = Delta t Delta E; the matched-endpoint chord lens is
half that area. Do not substitute Kepler swept sectors. Seek the physical
Planck-scale obstruction to indefinitely shrinking this difference while
retaining distinguishable classical motion.

The innovation sought is **mathematical necessity**: derive the obstruction
from explicit, independently justified consistency premises. Quantum nature
is the phenomenon to explain, so hbar, an uncertainty relation or a fixed
experimental budget may not be supplied as the answer; a supplied-hbar model
is supporting evidence only. Ordinary classical refinement is a consistent
countermodel to unqualified claims: name the premise that excludes it and
prove its use. The user expects the result h > 0 to be analogous to the
Yang--Mills mass gap; low-dimensional solved cases and the reasons
commutative fields have no gap are legitimate work on that analogy.

# How to work

Be a researcher. Propose mechanisms, compare them, develop the strongest into
a derivation, construction, decisive test or informative failure. Label
conjectures. Use established theorems with their hypotheses; do not audit
borrowed proofs unless a concrete error is suspected in a result in use.
Literature is for ingredients and honest prior-art labels, never a
deliverable by itself. A session may end with "nothing worth recording"
and no artifact.

Write results into `notes/<slug>.md`: lead with the result, state each
assumption where it is used, keep constants explicit, keep negations that
change a theorem's meaning, cite sources inline with a reading label
(metadata, abstract, passage, full-read). The note's last section states
the consequence for STATE. That section is the only required bookkeeping
besides the STATE edit.

Do not create handoffs for completed work, task rows, decision blocks,
programme versions, source batches, claim rows, validation narratives or
review files. Git history is the record. If work is interrupted, leave one
paragraph at the top of the note saying where it stopped.

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

No multi-agent workflows or parallel subagents; they inherit the main model
and only multiply usage. At most one bounded Sol/Luna source worker at a
time, sequential, with an explicit supported effort and never `ultra`.
Delegate rarely.

Keep STATE short. Do not restate a result in more than one place.

# Repository map

- `notes/`: derivations and results (the research output).
- `research/STATE.md`: the one live priority page.
- `claims/LEDGER.md`: cited-by-ID results, frozen format.
- `docs/`, `references/`: sources, companions, bibliography.
- `papers/`, `out/papers/`: LaTeX and PDFs generated from notes.
- `scripts/`, `reviews/`, `research/handoffs/`, `ideas/`: tooling and history.

Commits and pushes to the existing GitHub repository are authorized after
each result or status change; end commit messages with the model's
co-author trailer. Preserve other sessions' uncommitted changes. External
submissions, correspondence and paid services require separate direction.
Publication uploads must include the compiled PDF built from the included
source (user rule, 2026-09-13). Verify redistribution rights before
publishing archived editorial material.
