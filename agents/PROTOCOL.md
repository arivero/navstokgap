# Bounded agent work and handoff

The repository state is the authority for continuity. Agent role cards describe
work, not persistent processes or auto-starting Codex configurations. The user
requested smaller agents for minor bibliography/transcription tasks. Model names
are preferences, not a claim about future availability: use the available
equivalent or report the mismatch. Do not silently choose a larger paid model.

## Dispatch

Coordinator: pass a concrete task ID, paths to AGENTS/PROGRAMME/role instructions,
the exact question and allowed write paths. For Luna/Sol overrides use a bounded
context rather than a full conversation fork. Require workers to read applicable
skills themselves. Workers do not edit shared indexes, task state, claims, papers
or other workers' files; return proposed integration changes in the handoff.

The initial concurrency budget is one coordinator plus at most two source workers.
This leaves room for a bounded independent reviewer when useful. These are
cost-control choices, not assertions about mathematical independence.

## Evidence levels

`metadata` means identifier/title verified; `abstract` means abstract read;
`passage` means a named section/page/folio read; `full-read` means all specified
text read; `proof-audited` means the proof and imported assumptions were checked.
These labels are not interchangeable. Search snippets are leads, not quotations
from a full source. Do not label a whole collected manuscript fully read after
searching selected words.

## Return format

Save `research/handoffs/<task-id>.md` containing:

- Task, model/role, date, input revisions or paths and output paths.
- Searches/open routes attempted, identifiers and edition choices.
- Exact reading coverage, extraction defects and uncertain mathematical symbols.
- Findings with source anchors; claims NOT established by the source.
- Tests/validation performed, unresolved dependencies and suggested next task.

For sources use `references/SOURCE_POLICY.md`. No access-control bypass, external
publication or correspondence. Mark unavailable sources and stop at the task's
budget; a lawful source stub is a valid output.

## Acceptance

Coordinator checks metadata and at least every passage used for a substantive
claim. Formula transcriptions need visual verification against the source.
Translations and editorial expansions must be labeled. Only reviewed material
enters the shared bibliography or supports an accepted claim. Agreement between
models is not a proof or independent historical evidence.

If the session ends unexpectedly, a future coordinator may reclaim an active task
after checking for live workers and existing outputs. Preserve partial artifacts
and state their incompleteness; do not blindly restart downloads or overwrite them.
