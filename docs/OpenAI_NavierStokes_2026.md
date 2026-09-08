# OpenAI Navier–Stokes announcement: first-reading companion

Source: OpenAI, 8 September 2026,
[announcement](https://openai.com/index/navier-stokes-solution/).
Associated paper: OpenAI, *Finite time blowup for Navier–Stokes*, 165 pages,
[official PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf).

Coverage: announcement body, paper pp. 1–6 via web text extraction, official
Fefferman formulation pp. 1–2, formalization README and Comparator instructions.
Theorem 1.1 on PDF p. 1 was also visually checked against the downloaded original.
The theorem and physical explanation are reported from the authors; the full
argument and Lean build have not been independently audited here.

The main theorem concerns smooth compact forcing, initially zero velocity,
finite-energy velocity blowup, and alternatives C/D. The narrative motivates
careful separation of integral control and local concentration.

Repository use: [second blog entry](blog/after-the-navier-stokes-announcement.md).
Its proposed transfer is methodological: identify the controlled observable
and the missing uniform estimate. This reading adds no accepted mathematical
claim to our ledger. A dedicated proof/formalization audit needs its own task.

Source routes for continuation:

- [Official problem](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
- [Formalizations](https://github.com/openai/NavierStokesAndEuler).
- [Comparator instructions](https://github.com/openai/NavierStokesAndEuler/blob/main/ComparatorChallenges/README.md).

The PDF retrieval cache is `.build/openai-ns/navier-stokes.pdf`; redistribution
rights are unestablished, so the original remains outside tracked sources.
SHA-256: `8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81`.
