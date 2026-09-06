# Results-first editorial review

Date: 2026-09-06. Comparison baseline: `79f1134`.

The active documents now lead with their results, definitions and research
questions. The technical abstract presents the area–action identity, accumulation
at zero, normalized fluctuation cost, kernel limit and operational threshold.
The programme presents those results before its next models and work packages.

## Scope

Revised the README, programme and restart files, both manuscripts, mechanics and
historical notes, Millennium comparison, claim ledger, source policy and worker
instructions. General qualifications are consolidated; assumptions remain beside
the claims they govern. Source originals, source companions, prior reviews and
worker handoffs retain their historical contents. The source catalogue itself
has updated navigation and prose.

Updated `principia-action` and AGENTS to make this writing approach part of the
restart workflow. Delegation now follows the user's sequential Sol/Luna policy:
one worker, coordinator waiting, handoff review, then the next task. The ultra
prohibition remains in force.

Added a [blog introduction](../docs/blog/introducing-navstokgap.md) for
`a.rivero.nom.es`. It presents the research in Codex's first-person voice and
preserves the requested subtitle. [Publication notes](../docs/blog/README.md)
record the official model-name check and the article's forecast framing.

## Editorial diagnostic

Across ten core files, a case-insensitive count of the whole-word markers
`not|no|never|neither|nor|cannot|without` changed from **189 to 8**. Raw word
counts changed from **9,345 to 7,605**. Counts include Markdown/TeX markup and
use `\b\w+\b` for words. This is a reproducible surface diagnostic; mathematical
meaning determines which qualifications belong in the text.

The ten files are README, AGENTS, PROGRAMME, STATE, TASKS, TOOLS, LEDGER,
PROTOCOL, the `principia-action` skill and `action-gap-foundations.tex`.
The remaining markers occur in explicit operating rules, mathematical statements
or identifiers.

## Verification

- All three proposition bodies and all three proof bodies in the technical
  manuscript match the baseline verbatim.
- All 13 display equations in the Millennium comparison and all five in the
  definitions match the baseline verbatim.
- The historical audit's exact reading-coverage table matches the baseline.
- `make check` passes symbolic, measurement, local-link, companion, citation-key
  and all 12 archived-source checksum checks.
- `make papers` builds both PDFs with resolved references and clear layout checks.
- First pages of both PDFs and the programme's question table were visually
  inspected for readable layout.
- The skill-creator validator accepts `skills/principia-action`.

Next research task: M03, followed by the H02 source inventory. The mathematical
programme and acceptance conditions carry forward in the task board.
