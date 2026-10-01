---
name: poormanrag
description: Retrieve existing results, mechanisms, source support and route-closing corrections from the navstokgap repository before each research unit. Use keyword search and the notes catalog when the corpus exceeds context; this does not replace reading a proof or launch a literature audit.
---

# Poor man's repository retrieval

Use this workflow before every bounded research unit in this repository,
and again when changing track or mechanism. Paths below are relative to
the repository root, two directories above this file.

Read the live queue in [STATE](../../research/STATE.md). Recover relevant
entries in [LLM.md](../../LLM.md), the established-result map with a stated
snapshot date, and [notes/index.md](../../notes/index.md), the full-read
retrieval catalog. Later corrections in maintained notes take precedence
over an older map or an obsolete summary.
Use the [dependency paths](../../research/dependencies.md) and
[obstruction map](../../research/obstructions.md) for the minimal current
chain and the precise scope of a closed route. The structured counterpart
is [note-index.json](../../research/note-index.json).

Form a small query set from the proposed calculation: mechanism and
synonyms, model or operator, result IDs, and the likely failure modes.
Search catalog metadata for useful leads, then search the **full corpus**:

```sh
rg -n -i 'mechanism|synonym|operator|claim-id' notes/index.md
rg -l -i 'mechanism|synonym|operator|claim-id|counterexample' notes ideas references research claims papers docs --glob '*.md' --glob '*.bib' --glob '*.tex' --glob '*.txt'
```

Replace the example terms with the actual query. Inspect the filename
matches, then use `rg -n` and targeted reads to recover the load-bearing
derivation, assumptions, limit and correction. Expand synonyms or search
linked result IDs when a hit points to another note. A high catalog
priority chooses reading order; it never excludes lower-priority files
from the full-text search. Negative results deserve retrieval when they
close the proposed route. In particular, inspect both an old construction
and its correcting or superseding note before reusing it.

Carry a compact answer into the calculation: what is already proved,
under which premises; which mechanism remains available; which failed
route must be avoided; and which estimate the next unit will establish
or falsify. Cite the maintained proof or held source passage when using
a result. Catalog summaries, keyword matches and bibliography metadata
alone are not proof evidence. Respect source reading labels.

Keep retrieval bounded to the live calculation. Reuse unchanged sources
already held in context, adding a search for later corrections. No search
report, routine review artifact, embedding service or numerical verification
script is needed. Return to the proof as soon as its relevant dependencies
and obstructions are clear.

After a useful result, update its Markdown and JSON catalog entries along
with the maintained note. Preserve separate retrieval priority, proof status, research role and
value. A new entry requires a full read; material changes require reading
the changed argument and its relevant surroundings. Flag surprising
results as research judgment, without implying literature novelty. Keep
links to decisive corrections so future retrieval cannot revive a closed
route by reading only its attractive first version.

This repository-local skill is activated by [AGENTS.md](../../AGENTS.md).
It authorizes retrieval and catalog maintenance within the user's current
task; it adds no external-action permissions or publication authority.
