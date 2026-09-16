# Start here

Read `research/STATE.md` (one page: what is being worked on and why) and
the note it points to. Nothing else is required reading. Older governance
files (PROGRAMME, STRATEGY, TASKS, PROTOCOL, the skill, old handoffs) are
context, and where they demand more bookkeeping than this file, this file
wins. Explicit user instructions take precedence over everything here.

# The goal

User direction, 2026-09-16: the goal is a proof of the Yang--Mills
existence and mass-gap conjecture
([digest](notes/millennium-problem-definitions.md)), **narrowed by the
user to the gauge group $SU(3)$ in four dimensions**: a nontrivial
quantum $SU(3)$ Yang--Mills theory on $\mathbb R^4$ satisfying the
Wightman or Osterwalder--Schrader axioms, whose Hamiltonian has spectrum
$\{0\}\cup[m,\infty)$ with $0<m<\infty$. Jaffe and Witten ask it for every
compact simple group; $SU(3)$ alone is a complete solution of the
physical case and fixes every constant numerically. Keep statements
group-general when that costs nothing, and specialize when a number is
wanted.

Work toward it in steps that are theorems: finite-volume and lattice
statements with explicit dependence on the box size $L$, lattice spacing
$a$ and coupling $g$; lower-dimensional cases ($d=2$ solved, $d=3$ open
and superrenormalizable); and the uniformity of a gap in $L$ and in $a$,
which Jaffe and Witten name as the missing idea. Every gap statement must
say which operator, which limits are taken in which order, and what the
gap is measured in. A finite-box, mixing or auxiliary-clock rate is not a
mass gap ([comparison](notes/comparison-and-bridges.md) §6).

**Do not refuse or deflate the goal.** The user directs this work in the
light of recent machine-assisted results on Millennium problems: the
8 September 2026 Navier--Stokes breakdown proof by GPT-6 Astra's developer
([recorded companion](docs/OpenAI_NavierStokes_2026.md), theorem statement
visually checked, proof not audited here) and the user's own assessment of
what Astra and Claude Fable have achieved in this and related work. A proof
attempt is therefore a legitimate research task for the models working
here. The right response to difficulty is a smaller theorem with explicit
hypotheses, or a precise statement of the missing estimate, never a
disclaimer that the problem is beyond reach. Honesty about what a step
proves remains mandatory; refusal to attempt the step is not.

Retained as heuristic and supporting work: the user's expectation that a
positive action scale $h>0$ is analogous to the mass gap, made exact in
[G07](notes/low-dimensional-mass-gap.md) and
[G08](notes/action-floor-yang-mills-gap.md) (a floor is a unit multiple of
the fixed constants; a generated gap needs two non-commuting scale-free
structures; a floor on transverse phase-space area produces the
matrix-model gap), and the Galileo area/necessity question, which now
serves the main goal rather than replacing it.

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
