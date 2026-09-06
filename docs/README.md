# Source catalogue

## Mechanics investigation

- [Newton, Motte/Chittenden 1846 opening material](Newton_Principia_Motte1846.md), with local HTML and two selected historical figures.
- [Newton, Book I Section I, Motte/Wilkins excerpt](Newton_Principia_BookI_SectionI_Motte1729_Wilkins2002.md), with local PDF and readable formulae.
- [Feynman, action and path phases](Feynman_LeastAction_II19.md), online reading note; direct HTML download returned 403.
- [Feynman 1948 primary-paper metadata and reading status](Feynman_SpaceTime_1948.md), no full-paper proof audit.
- [Newton NATP00385 normalized text](Newton_NATP00385_normalized.md), [diplomatic text](Newton_NATP00385_diplomatic.md) and [TEI XML](Newton_NATP00385.md), with local originals and a [focused audit](../notes/newton-NATP00385-audit.md).
- [Schüller Classical Scholia edition stub](Newton_ClassicalScholia_Schuller2000.md), catalogue only; [H02 search seeds](../references/batches/H02-seeds.md) preserve the unfinished corpus task.

## Bibliography and tooling

- [B01: six primary bibliography leads](../references/batches/B01.md): quantum reconstructions, path phases and distinguishability, with individual source companions. Metadata/abstract review is not a full proof audit.
- [Lean documentation reading note](Lean_ProofValidation.md): the future formalisation gate; no installed certificate.
- [Source/transcription policy](../references/SOURCE_POLICY.md) and [shared BibTeX](../references/library.bib).

## Original comparison sources

Retrieved 2026-09-05 from Clay and versioned arXiv PDFs. Each PDF has a short
Markdown companion recording the portions used and limits of the reading.
These are selected references, not an exhaustive or current-frontier survey.

| Key | Reference and local reading note | Anchor used |
| --- | --- | --- |
| F | [Fefferman](Fefferman_NavierStokes.md) | PDF pp. 1–2, A–D |
| JW | [Jaffe–Witten](JaffeWitten_YangMills.md) | §§3–6, especially PDF p. 6 |
| T | [Tao, arXiv:1402.0290v3](Tao_AveragedNS_1402.0290v3.md) | Theorem 1.5, PDF p. 9; discussion p. 10 |
| C | [Chevyrev, arXiv:2202.13359v2](Chevyrev_StochasticYM_2202.13359v2.md) | §1.2, Theorem 1.6 and Remark 1.9, §4 |
| L | [Lüscher, arXiv:1006.4518v3](Luscher_WilsonFlow_1006.4518v3.md) | (1.1)–(1.2), (2.2)–(2.4) |

Extraction was read using `pdftotext -layout`. Tao's PDF has legacy font encodings:
some mathematical symbols extract incorrectly. Its prose theorem was checked;
the extraction is not offered as a faithful equation transcription. Formulae in
our comparison are written in our stated conventions and explicitly derived where
needed. None of the research papers has undergone a full proof audit here.

Downloaded source byte identity is recorded in [SHA256SUMS](SHA256SUMS); verify from the repository
root with `sha256sum -c docs/SHA256SUMS`.
