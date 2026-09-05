# Sources for the first comparison

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

PDF byte identity is recorded in [SHA256SUMS](SHA256SUMS); verify from the repository
root with `sha256sum -c docs/SHA256SUMS`.
