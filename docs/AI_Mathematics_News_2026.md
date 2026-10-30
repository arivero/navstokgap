# Machine-assisted mathematics, 2026: the news behind the working mandate

Updated 2026-10-30. This is a dated source record of claims, attribution and
reading coverage. **Passage** means the primary text was read for the stated
facts; **metadata** means a registry record only; **secondary** means a
press or reference summary whose primary text was not read here. Announcements
are not accepted mathematical claims in this repository.

## Yang–Mills shepherding: Gross chairs the committee

The [committee's October 2026 statement](https://www.kitp.ucsb.edu/sites/default/files/YM_working_group.pdf),
pp. 1–2, passage-read on 2026-10-30, says OpenAI asked David Gross on
16 October to take custody of the claimed existence proof and organize
its release. Gross chairs the group with Michael Douglas, Arthur Jaffe,
Igor Klebanov and Nikita Nekrasov. The committee's initial checks concern
the definitions and problem statement and alignment of the Lean
formalization with the informal argument; it plans releases with its assessment
after validation. This is a shepherding/review process, not a completed
independent certification.

The [OpenAI announcement of 26 October](https://openai.com/index/building-scientific-understanding-with-academic-communities/),
physics section, was also passage-read. The committee describes a claimed
continuum existence construction building on Bałaban's multiscale methods,
including fermionic couplings. It explicitly leaves confinement and the mass
gap open. The underlying proof and formalization have not been examined here.
This updates the source context without changing this repository's conditional
[spectral and construction obligations](../notes/mass-gap-obligations-lattice.md).

## The Millennium-scale events of September 2026

| Date | Event | Status | Reading |
| --- | --- | --- | --- |
| 2026-09-07/08 | Alpöge and Buckmaster release forced smooth blowup for IPM, Boussinesq and 3D Euler, extending Córdoba and Martínez-Zoroa's programme; Claude, Codex with GPT-5.6 Sol and later Astra were used; Lean verification of the Boussinesq and Euler results dated 2026-08-22 | Preprints on the author's page; artifact hashes left as placeholders in the IPM paper | passage, [B19 companion](batches/B19/forced-blowup-source-companion.md) |
| 2026-09-08 | OpenAI announces forced finite-time blowup for 3D Navier–Stokes, answering alternatives C/D of Fefferman's formulation, from about 10,000 concurrent agents, with a 165-page paper and Lean artifacts | Theorem 1.1 checked against the PDF; proof unaudited | passage, [companion](OpenAI_NavierStokes_2026.md) |
| 2026-09-08 to 13 | Priority dispute: Buckmaster and Alpöge say their Euler work reached OpenAI before the run; OpenAI's updated release (2026-09-10) says an investigation found their prompts could not have influenced the system; Córdoba: without the prior human programme the problem would not have been solved | Contested | secondary, [Wikipedia](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy) |
| 2026-09-11 | Clay Mathematics Institute: the problem "has apparently been settled"; the evaluation "is deliberately unhurried, but we will provide updates"; no claimant is named | Prize undecided | passage, [CMI](https://www.claymath.org/news/navier-stokes-announcement) |
| 2026-09-11 | Open letter "A Severe Misalignment of AI in Mathematics", 25 signatories in the record retrieved (Avila, Bhargava, Birkar, Deligne, Deng, Donaldson, Duminil-Copin, Figalli, Hairer, Huh, Kontsevich, Lindenstrauss, Lions, Maynard, McMullen, Mori, Ngô, Okounkov, Scholze, Smirnov, Tao, Viazovska, Villani, Werner, Zelmanov), against treating open problems as benchmarks at the expense of understanding | Published | metadata, [Zenodo 10.5281/zenodo.22737750](https://doi.org/10.5281/zenodo.22737750) |
| 2026-09-11 onward | Later reports count 27 to 28 signatories of the letter | Growing | secondary |
| 2026-09-15 | *Scientific American* (M. Bischoff) ranks the remaining problems for AI: Birch–Swinnerton-Dyer, Hodge and Riemann nearest; Yang–Mills with the mass gap and P versus NP furthest, "experts do not expect AI models to resolve these questions anytime soon" | Opinion survey | passage, [SciAm](https://www.scientificamerican.com/article/which-million-dollar-math-problem-could-ai-solve-next/) |
| 2026-09-21 | The **Advisory Group on Mathematics and Artificial Intelligence** (AGMAI), hosted at the Institute for Advanced Study, Princeton: Charles, De Lellis, Gowers, Hairer, Srivastava, Tillmann, Vakil, Witten, Wood. OpenAI approached members about an advisory board and they formed an independent, unpaid group instead, "to advise AI companies on their interactions with mathematical research and with the mathematical community, including the responsible presentation and release of mathematical results", with no decision-making power at any company. Its first task is advising OpenAI on releasing "a large number of significant results" from its internal model | Constituted | passage, [Tao's blog](https://terrytao.wordpress.com/2026/09/21/advisory-group-on-mathematics-and-artificial-intelligence/) |
| 2026-09-21 | OpenAI reports that an internal model resolved more than 100 further open problems in about 24 days | Unreleased; to be coordinated through AGMAI | secondary, [AI Weekly](https://aiweekly.co/alerts/openai-forms-math-advisory-group-amid-100-solved-problems-claim) |

## Other results of 2026 that bear on this repository

| Date | Result | System and people | Status | Reading |
| --- | --- | --- | --- | --- |
| 2026-08-10 | The proven proportion of zeta zeros on the critical line raised from 41.6% to 67.2% | Unreleased Claude research model; prompt by J. Sumner; validated by L. Alpöge and R. Furman; reviewed by B. Conrey and D. Goldston | Lean formalization passing the comparator tool; the post expects no route from it to the Riemann hypothesis | passage, [Anthropic](https://www.anthropic.com/research/riemann-zeta) |
| 2026-09 | Fermat's Last Theorem formalized in Lean end to end: 13 million lines, 30,300 theorems, 11 days, on Lean's three standard axioms | Internal model comparable to Claude Fable 5.1, about 6 billion output tokens; high-level direction from T. Peng | Complete; the authors call it longer than it needs to be | passage, [Anthropic](https://www.anthropic.com/research/formalizing-fermats-last-theorem) |
| 2026-07 | Proofs of the cycle double cover conjecture (GPT-5.6 Sol) and of Crouzeix's conjecture (GPT-5.6 Sol, S. Jin; reviewed by Greenbaum, Townsend, Crouzeix) | OpenAI models with named mathematicians | Expert expositions and reviews reported | secondary, [list](https://en.wikipedia.org/wiki/List_of_mathematical_discoveries_by_artificial_intelligence) |
| 2026-07-20 | Counterexample to the Jacobian conjecture in dimension 3 | Claude Fable 5; L. Alpöge, A. Mathew | Reported verified by several mathematicians; primary unread here | secondary, same list |
| 2026-08 | Sendov's conjecture for all degrees (GPT-5.6 Pro, L. Mazur; streamlined by T. Tao); twelve new Hadamard matrix orders and elliptic curves of rank at least 30 and 31 (Claude, Alpöge and coauthors); prime gaps at most 186 infinitely often (OpenAI, unverified) | Mixed | Lean or computer checks for most; the prime-gap bound unverified | secondary, same list |
| 2026-09 | Köthe conjecture disproved, with further counterexamples and proofs in combinatorics and probability | Epoch AI with GPT-6 Astra; T. Adamczewski and coauthors | Lean formalizations on GitHub | secondary, same list |
| 2026-09 | The roughly 25,000 cases of one inverse Galois problem identified, by mathematicians, amateurs, computation and AI-assisted search together | Community effort (SAIR challenge) | Press report | secondary, [SciAm](https://www.scientificamerican.com/article/mathematicians-use-ai-to-find-mysterious-symmetries-solving-decades-old-problem/) |

## Repository use

The held [Navier–Stokes companion](OpenAI_NavierStokes_2026.md) records the
forced alternatives and its bounded reading. The [exact problem comparison](../notes/comparison-and-bridges.md)
keeps fluid evolution, auxiliary relaxation and physical spectral energy
separate. Multiscale control is a shared methodological question, not an
operator identification or a proof that the remaining obligations reduce to
a fixed number of blocking steps. Source announcements do not lift the
current suspension of new research during consolidation.
