# B70 librarian handoff

- Task: Q01 interaction-premise audit; bounded source audit for C125.
- Role/model/effort: requested Luna, low; one worker, no descendants. Date:
  2026-09-13. Outputs: `docs/batches/B70/interaction-source-companion.md` and
  the downloaded arXiv v1 PDF in `docs/batches/B70/`.
- Input context: `references/IDEA_BRIDGES.md`,
  `notes/classical-orientation-closure.md`, `research/handoffs/Q01-interaction.md`,
  plus AGENTS.md, agents/PROTOCOL.md, principia-action and bibliography skills.

## Source and coverage

Selected primary: G. de la Torre, L. Masanes, A. J. Short, M. P. Müller,
“Deriving quantum theory from its local structure and reversibility,” arXiv:
1110.5482v1 [quant-ph], submitted 25 Oct 2011; printed PDF metadata/date:
10 Sep 2018. Exact routes:
https://arxiv.org/abs/1110.5482 and https://arxiv.org/pdf/1110.5482.
Read PDF pages 1–2 and 4: local-quantum setup, Theorems 1 and 2, Theorem 2
proof, and conclusions/limitations. Evidence is passage level (not
proof-audited); extraction used pdftotext and PDF metadata/render layout.
One discovery query was used; one primary source was selected.

## Findings and dependency decision

Theorem 2 says identical qubits plus local tomography and any continuous
reversible interaction force states, measurements and transformations to be
those of quantum theory. Theorem 1 requires a connected linear reversible group
containing all local unitaries and product-state/product-effect probabilities
in [0,1]; a nonlocal element reduces to an entangling unitary or a
partial-transpose branch. The latter is ruled out by three-qubit positivity.

For C125, the local ball/effects are the qubit Bloch representation, tensor
moments give Hermitian coordinates, and copy/permutation closure is present.
The missing premise is an admissible connected nonlocal reversible group
preserving product-state/product-effect positivity. Theorem 1 obstructs the
minimal separable composite; Theorem 2's full conclusion additionally imports
the universality proof and ancilla/discard closure outside C125's terminal
scope. Retain interaction as Q01's dependency; do not claim independently
verified effective settings.

## Checks and continuation

Performed PDF metadata check and text-anchor check; no numerical/symbolic
scripts. No shared state, claims ledger, or task-board edits. Selected
continuation: coordinator may integrate this dependency map into Q01. Broader
higher-dimensional or discrete-interaction generalization is parked because
the source itself identifies it as open (p. 4).
