# Balaban constructions: source archive and reading notes

Retrieved 2026-10-27. **Eight PDFs are downloaded locally.** The linked
companions document selected passages and useful mechanisms. Thirteen older
journal papers have verified metadata but no downloaded full text. This is
a source collection with reading notes; no new construction or proof review
is claimed.

The PDFs and complete text extractions stay local, under this directory's
Git exclusions. The notes, bibliography and metadata are published. Each
companion records the local filename, source URL, version and PDF checksum.
Local registrations in `docs/SHA256SUMS` are separate from the notes-only
commit, so a fresh checkout does not require unpublished files.

## Start with these

| Source | Local PDF pages | Useful passages |
| --- | ---: | --- |
| [Balaban, ICM overview](Balaban_UltravioletStability_ICM1986_1987.md) | 4 | Printed pp. 1260–1262: finite gauge integrals, blocking, effective densities, historical ultraviolet-stability scope |
| [Dimock I: small fields](Dimock_BalabanI_1108.1335v2.md) | 52 | §§2.1, 2.4, 4.5 and Theorem 14: normalized block averaging, local inverses, localization, controlled RG step |
| [Dimock II: large fields](Dimock_BalabanII_1212.5562v2.md) | 94 | Introduction, Theorem 3.1, §§3.13–3.14: sums over region histories, boundaries, localization before the cluster expansion |
| [Dimock III: convergence](Dimock_BalabanIII_1304.0705v1.md) | 37 | §3.6: connected polymers, exponentiation, partition-function stability |
| [Dimock: covariant axial gauge](Dimock_CovariantAxialGauge_1410.2798v3.md) | 23 | Introduction: tree gauges, lattice covariance and block averaging in an Abelian model |
| [Dimock: scalar QED in three dimensions](Dimock_ScalarQED3_1502.02946v2.md) | 85 | §1.1: counterterms chosen by the RG flow, bounded-field and finite-volume scope |
| [Balaban et al.: block-spin algebra](BalabanEtAl_BlockSpinAlgebra_1609.00966v1.md) | 18 | Proposition 4: composition of background and critical fields, with fluctuation and domain-complement terms retained |
| [Balaban et al.: parabolic operators](BalabanEtAl_ParabolicOperators_1609.00971v1.md) | 64 | Introduction and Proposition 4.4: anisotropic blocks and bounds for analytic functions of covariance-related operators |

The last two papers concern weakly interacting bosons. Dimock's three-part
exposition uses scalar phi-four theory in three dimensions. These distinctions
matter when comparing the method with four-dimensional non-Abelian gauge
theory. The page counts describe the downloaded preprints, not journal editions.

## How the method works

Begin with a finite lattice integral. Choose coarse variables by averaging
fine variables over blocks. Integrate the remaining variables to obtain a
new density, preserving the partition function. In gauge theory the averaging
and gauge fixing must respect the gauge transformations. Balaban describes
this construction in his ICM overview, printed pp. 1260–1261.

Dimock's scalar presentation uses a normalized Gaussian averaging kernel
(I, §2.1). At each scale, split the integration into small-field and
large-field regions, and sum over all such choices (II, introduction).
This decomposition retains the full integration domain. Around the
background minimizer in a small-field region, analyze the Gaussian
fluctuations and the remaining interactions.

The central analytic work is localization. A fluctuation at one location
depends on Gaussian variables elsewhere through its covariance. Local
Green-function inverses and random-walk expansions control this dependence;
weakening parameters turn it into sums of local terms (I, §§2.4, 4.5;
II, §3.13). Connected sets of blocks, called polymers, organize the resulting
interactions. Cluster expansions and bounds on the large-field terms then
control their sums.

Separate the vacuum energy and other running parameters from the polymer
remainder, choose counterterms, and prove that another RG step preserves the
stated representation and bounds. Dimock I, Theorem 14, illustrates that
induction. Dimock III, §3.6, completes a scalar stability argument using
convergent connected-polymer sums. The constants and small-coupling hypotheses
belong to each theorem and must be retained when using it.

## Interesting points for this project

1. **Keep the effective density.** Our [refinement construction](../../notes/refinement-composition-and-limit.md)
   identifies a coarse-variable map and an integration law. The source
   calculations suggest tracking the generated interactions, normalization,
   boundary terms and region history as part of the state passed to the
   next refinement step.
2. **Distinguish composition from analytic control.** Proposition 4 of the
   block-spin algebra paper gives an explicit composition identity under
   its hypotheses. Its fluctuation integral and domain-complement term
   remain to be estimated. An algebraic insertion identity leaves those
   additional obligations.
3. **Localize before claiming independent local errors.** Dimock I, §4.5,
   and II, §3.13, explain why local dependence on the fluctuation field
   differs from local dependence on its independent Gaussian coordinates.
   This is relevant to our source-dependent and moving-background estimates.
4. **Separate the limits and operators.** Decay of a constrained fluctuation
   inverse and stability of a partition function do not establish the
   gap of the physical Hamiltonian. Our [conditional theorem](../../notes/mass-gap-conditional-theorem.md)
   retains continuum reconstruction, nontriviality and the spectral limit
   as separate obligations. The [threshold note](../../notes/small-field-step-gaussian.md#hard-conditioning-and-soft-constraint-decay)
   also records why sharpening the constants of its existing estimate
   does not reach the intended physical window.

These are proposed uses of the sources, not claims that their scalar,
Abelian or bosonic estimates apply unchanged to our SU(3) problem. No source
in this collection derives the necessity of a positive action constant.

## Older journal originals still needed

Crossref records were fetched individually on 2026-10-27. The
[structured catalog](catalog.json) preserves their titles, authors,
publication data and metadata URLs. Short descriptions below identify
the papers; they do not replace the full published titles.

| Paper | Journal volume, pages, year | DOI |
| --- | --- | --- |
| Regularity and decay of lattice Green functions | CMP 89, 571–597 (1983) | [BF01214744](https://doi.org/10.1007/BF01214744) |
| Propagators and renormalization transformations I | CMP 95, 17–40 (1984) | [BF01215753](https://doi.org/10.1007/BF01215753) |
| Propagators and renormalization transformations II | CMP 96, 223–250 (1984) | [BF01240221](https://doi.org/10.1007/BF01240221) |
| Averaging operations | CMP 98, 17–51 (1985) | [BF01211042](https://doi.org/10.1007/BF01211042) |
| Regular gauge configurations and gauge fixing | CMP 99, 75–102 (1985) | [BF01466594](https://doi.org/10.1007/BF01466594) |
| Propagators in a background field | CMP 99, 389–434 (1985) | [BF01240355](https://doi.org/10.1007/BF01240355) |
| Ultraviolet stability in three dimensions | CMP 102, 255–275 (1985) | [BF01229380](https://doi.org/10.1007/BF01229380) |
| Variational problem and background fields | CMP 102, 277–309 (1985) | [BF01229381](https://doi.org/10.1007/BF01229381) |
| Effective actions and coupling renormalization | CMP 109, 249–301 (1987) | [BF01215223](https://doi.org/10.1007/BF01215223) |
| RG approach II: cluster expansions | CMP 116, 1–22 (1988) | [BF01239022](https://doi.org/10.1007/BF01239022) |
| Convergent renormalization expansions | CMP 119, 243–285 (1988) | [BF01217741](https://doi.org/10.1007/BF01217741) |
| Large-field renormalization I | CMP 122, 175–202 (1989) | [BF01257412](https://doi.org/10.1007/BF01257412) |
| Large-field renormalization II | CMP 122, 355–392 (1989) | [BF01238433](https://doi.org/10.1007/BF01238433) |

Access attempts: a Springer PDF endpoint returned subscription HTML;
Project Euclid PDF endpoints returned an interstitial rather than a PDF.
The old Deep Blue URL for the three-dimensional stability paper returned
the library's application HTML. Its current public metadata API identified
the original bitstream, but content requests timed out or returned HTTP 500.
No HTML response was saved as an original PDF, and access controls were
not bypassed. The collection is incomplete for this older journal series.

## Relation to OpenAI's announcement

OpenAI's [October 26 announcement](https://openai.com/index/building-scientific-understanding-with-academic-communities/),
section “Existence of quantum chromodynamics and completions of the Standard
Model” (passage read), reports constructions of QCD and pure Yang–Mills
existence building on Balaban's approach. The release says the physics
group is preparing its own write-up and has deferred releasing the
AI-produced materials. The announcement does not claim a mass-gap proof.

For our programme, the announced existence construction is relevant to
the [T4 continuum obligation](../../notes/mass-gap-obligations-lattice.md#existing-estimates-and-examined-routes). Whether its
precise theory, axioms, limits and observables supply a compatible input
to our gap argument requires the actual construction. None of our open
estimates is marked proved on the strength of this announcement.
