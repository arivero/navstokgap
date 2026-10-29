---
name: poormanrag
description: Retrieve proofs, countermodels, corrections and unexpected connections across the navstokgap corpus before a bounded research step. Use concise keyword searches and targeted reading, not an exhaustive reread or literature audit.
---

# Repository retrieval

Before each bounded research unit or change of mechanism, use
[STATE](../../research/STATE.md), relevant entries in the dated
[LLM map](../../LLM.md) and the full-read [catalog](../../notes/index.md).
Consult [dependency paths](../../research/dependencies.md) and the
[obstruction map](../../research/obstructions.md) for relevant chains
and failed routes; [note-index.json](../../research/note-index.json) gives
thematic metadata and typed links. Reuse unchanged material already read;
search for later corrections instead of rereading whole maps each time.

Resolve a former filename through the canonical entry's `keys` in
[note-index.json](../../research/note-index.json) or the existing
`NOTE_REDIRECTS` in `scripts/build_site.py`; read the destination argument
rather than treating a deleted filename as lost mathematics. Include the old
slug, a scientific synonym and a structural dependency in retrieval. Typed
`uses`, `corrects`, `obstructs` and `continues` relations support recall across
models without retaining duplicate prose. Check a correcting relation before
reusing an older source or manuscript.

Form a small direct query from the mechanism, model, result IDs and likely
failure modes. Search both catalog and **full corpus**, including source
companions and manuscripts:

```sh
rg -n -i 'mechanism|synonym|operator|claim-id' notes/index.md
rg -l -i 'mechanism|synonym|operator|claim-id|counterexample' notes ideas references research claims papers docs --glob '*.md' --glob '*.bib' --glob '*.tex' --glob '*.txt'
```

Replace the examples with the actual terms. Inspect filenames before
selecting targeted passages with `rg -n` and `sed`; narrow a noisy query
rather than silently discarding the end of its results. Follow result IDs,
the original argument and any correction or superseding note. Catalog
priority chooses reading order, not eligibility: a low-priority or older
note can contain the needed counterexample.

For **serendipitous recall**, also ask what the calculation shares with a
different model or track: a lost state, a closure operation, a limit order,
a conserved quantity, an observable or a failure mode. Search one compact
combination of that structural motif and a contrasting context across the
same corpus. For example, a cusp-history question can probe cuts and
memory; the resulting three-body receiver supplies a concrete hidden-state
comparison, but does not realize cusp branching. Inspect one promising
off-spine hit when it might change a premise, proof, countertest or
analogy; follow its corrections as needed. If no useful hit appears,
return to the calculation without manufacturing a connection or a tour of
unrelated notes.

Carry forward only what is needed: the proved statement and hypotheses,
the relevant countermodel or correction, and the estimate or test for the
current unit. Cite the maintained proof or held source passage and retain
its reading level; catalog summaries and metadata are leads, not evidence.
Do not create search reports, routine review artifacts, embedding services
or numerical verification scripts.

After a useful result, update the note and both catalog entries. Preserve
retrieval priority, proof status, role, value, limitations and correction
links; read a new entry in full and a material change with its surrounding
argument. A `surprising` flag expresses research judgment, not novelty.
This repository-local skill is activated by [AGENTS.md](../../AGENTS.md);
it adds no external-action or publication authority.
