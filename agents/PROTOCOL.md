# Bounded agent work and handoff

Each agent receives a concrete question and produces a reviewable artifact.
The coordinator maintains shared state and integrates the results. Role cards
describe the intended work; the task board records its current status.

## Dispatch and cost

Never select `ultra`: the user prohibited it to conserve tokens
(2026-09-06). Explicitly request a supported effort for every worker, reviewer and
descendant. Use fresh or limited context when a full-history fork prevents an
override. Announce task ID, model and effort before dispatch.

Use low/medium for routine sources and higher permitted effort when the task
requires substantial reasoning. A model substitution that raises cost requires
user direction. The concurrency budget is one coordinator and one active
subagent across the entire team (user instruction, 2026-09-06). Delegate smaller
tasks to Sol or Luna in sequence. The coordinator waits for the worker to finish,
then reviews its handoff before continuing or dispatching another. Run review
agents sequentially, and pass this limit to every descendant.

Pass the question, input paths, applicable skills, allowed output paths and a
finite source/page budget. The coordinator owns shared indexes, claim acceptance,
paper integration and commits. Workers return changes to these shared artifacts
as proposals in their handoffs.

## Evidence and writing

Lead each output with findings and source anchors. Use the following reading
labels consistently:

| Level | Work completed |
| --- | --- |
| metadata | Title and identifier verified |
| abstract | Abstract read |
| passage | Named section, page or folio read |
| full-read | Entire specified text read |
| proof-audited | Proof and imported assumptions checked |

Treat search snippets as discovery leads. Record the coverage and extraction
limits once, alongside the findings they affect. Follow AGENTS.md's writing rule.

## Handoff

Save `research/handoffs/<task-id>.md` with:

- Task, role, requested model/effort, date, inputs and outputs.
- Effective model/effort when independently reported.
- Source routes, identifiers, edition choices and exact reading coverage.
- Findings with anchors, extraction defects and unresolved dependencies.
- Checks performed and the next bounded task.

Use lawful routes and `references/SOURCE_POLICY.md`. A source stub
recording an access failure is a valid outcome at the task's stopping point.
External publication, correspondence and paid services require user direction.

## Acceptance and restart

The coordinator verifies metadata and every passage supporting a substantive
claim. Formula transcription includes visual source checking; translations and
editorial expansions carry labels. Mathematical acceptance rests on the argument,
its assumptions and tests.

After interruption, check live workers and existing outputs before reclaiming a
task. Preserve partial artifacts, record their coverage and resume from the
remaining work.
