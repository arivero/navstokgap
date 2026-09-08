# B19 coverage: forced multiscale blowup, September 2026

Retrieval, extraction and reading limits for the four originals of batch
[B19](../../../references/batches/B19.md). The programme reading is in the batch file;
this page records what was fetched and how far it was read.

## Retrieval

All four PDFs were downloaded on 2026-09-08 with `curl` from the author's institutional
page at `https://cims.nyu.edu/~tristanb/`. None carried an arXiv identifier, a DOI or a
journal record at retrieval, and none appeared in the author's own publications listing.
The files are therefore archived here as bytes, with checksums registered in
[`docs/SHA256SUMS`](../../SHA256SUMS), because the hosting page can change without notice.

| Local original | Source URL | Pages | SHA-256 |
| --- | --- | --- | --- |
| [IPM](AlpogeBuckmasterCoiculescu_IPM_2026.pdf) | `~tristanb/ipm.pdf` | 57 | `b3ebdbb8…c72a12` |
| [Boussinesq](AlpogeBuckmaster_Boussinesq_2026.pdf) | `~tristanb/boussinesq.pdf` | 76 | `895a628d…a4a21b` |
| [Euler](AlpogeBuckmaster_Euler_2026.pdf) | `~tristanb/euler.pdf` | 112 | `97ef408b…0ae8d8` |
| [Statement](Buckmaster_Statement_2026-09-08.pdf) | `~tristanb/statement.pdf` | 4 | `8d772394…621f9d` |

Extraction used `pdftotext -layout`, the method already recorded for the Millennium
comparison sources. The Euler text uses a private rate-list notation from p. 27 onward
that was not decoded here.

## Reading coverage

| Original | Read | Not read |
| --- | --- | --- |
| IPM | Title, abstract, introduction pp. 1–4, Theorem 2.1, strategy p. 4, references | Construction and appendix, pp. 5–56 |
| Boussinesq | Title, contents, §1.1–§1.2 pp. 1–5, §2 p. 7, Lemma 3.1 and §3.1–§3.2 pp. 8–9, acknowledgments and references p. 76 | Estimates, §§3.3–10, pp. 10–75 |
| Euler | Title, abstract, §1.1–§1.3 pp. 1–3, Theorem 1.1, closing proof p. 112, references | Construction, §§2–13, pp. 3–111 |
| Statement | Full text, pp. 1–4 | — |

Theorem statements were transcribed from the PDFs and checked against the abstracts.
No proof was audited. Nothing in these papers is entered in the claim ledger.

## Verified source facts

- The IPM paper lists a third author, Matei P. Coiculescu, who does not appear on the
  Boussinesq paper or in the press coverage.
- The IPM paper announces Lean verification of the Boussinesq and Euler results and prints
  the identifying artifact hashes as the unfilled placeholders `[BOUSSINESQ SHA-256]`,
  `[EULER SHA-256]` on p. 3. No Lean artifact is published with any of the three papers.
- The Euler PDF carries no author byline and no acknowledgments section; its text ends at
  the reference list. Authorship rests on the statement and on reference [1] of the
  Boussinesq paper.
- The Boussinesq §2 dating, 2026-08-15 for the result and 2026-08-22 for Lean verification,
  agrees with the statement's account.

## Access limits and open retrieval

The Córdoba–Martínez-Zoroa IPM original, arXiv:2410.22920v3, and the
Córdoba–Laín-Sanclemente–Martínez-Zoroa Boussinesq paper, Adv. Math. 480 (2025) 110480,
are the load-bearing prior sources for the programme and are catalogued in
[`library.bib`](../../../references/library.bib) from their arXiv and DOI records only.
Neither was downloaded or read in this batch; both remain open retrieval tasks.

Tao's commentary of 2026-09-07 was read online at
`https://terrytao.wordpress.com/2026/09/07/finite-time-blowup-with-smooth-forcing-term-for-the-incompressible-porous-medium-boussinesq-and-incompressible-euler-equations/`
and is cited for its assessment only; it was not archived.

The claimed hypodissipative Navier–Stokes result and the reported internal OpenAI
forced-Navier–Stokes proof have no public artifact and are outside the citable record.
