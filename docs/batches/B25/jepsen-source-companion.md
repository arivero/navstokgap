# B25: the spatial two-speed receiver

Balakrishnan, Bena and Van den Broeck give the exact tagged covariance
$C(t)=c^2e^{-2nct}$ for a symmetric two-speed equal-mass hard-point gas
(PDF pp. 7–8, equations (11)–(12)). Its integral gives $D=c/(2n)$.
The repository uses $u=c$, $\rho=n$ and action normalization $H_*=2mD$.

## Source and reading coverage

- V. Balakrishnan, I. Bena, C. Van den Broeck, *Velocity Correlations,
  Diffusion and Stochasticity in a One-Dimensional System*, Physical Review E
  65, 031102 (2002), DOI 10.1103/PhysRevE.65.031102.
- [Versioned source](https://arxiv.org/abs/cond-mat/0109025v1), submitted
  3 September 2001. Coordinator verified the arXiv metadata.
- PDF route: https://arxiv.org/pdf/cond-mat/0109025 .
  Cache: `.build/b25/balakrishnan_bena_vandenbroeck_2001.pdf`.
- SHA-256: `6c8f7c34c0ae46811d68a94926e82cd4886311b90835ad98f45d0a962bcc09b3`.
  The original remains ignored; redistribution rights were not assessed.
- Full `pdftotext -layout` extraction: `.build/b25/source.txt`.
  Full extraction is distinct from full reading.
- One Luna-low worker used two discovery searches and reported passages
  across pp. 3–18, including pp. 3–8, 13 and 17–18. This exceeded the
  assigned five-page scope; exact per-page reading depth was not reported.
- Coordinator read p. 4 and pp. 16–19 text, and visually checked pp. 7–8
  and 19. These passages support the accepted covariance and interpretation.

## Preparation and tagged path

Page 4 starts with uniformly distributed positions in a finite interval,
independent velocities and an initially specified tag at zero. Equal masses
exchange velocities on collision. The thermodynamic limit sends interval
length and particle numbers to infinity at fixed densities. Homogeneity
uses equal left/right density and symmetric velocity law (pp. 6–7);
section III specifies stationary velocity preparation. Equation (11), p. 7,
assigns equal probabilities to the two velocities.

On p. 17 the source describes a tag initially at either speed alternating
between free trajectories, and identifies its velocity with a dichotomic
Markov process. Page 19 distinguishes its ordinary ballistic atom from the
Bessel-weighted atom at zero for a tag initially at rest. The wording on
p. 16 about an extra Bessel factor requires this initial-state distinction.
Coordinator corrected the worker's overbroad recollision qualification
against the p. 19 image.

The worker also reported the general diffusion formula (29), p. 13,
$D=\langle|U|\rangle/(2n)$. The accepted two-speed result instead follows
directly by integrating the visually checked covariance (12).

## Source-to-task use

A12 defines the infinite Poisson Palm preparation directly. Its ordered-gap
proof derives independent reversal waits of rate $\rho u$, then
$H_*=mu/\rho$, in the existing collision manuscript. This is an established
model with an explicit proof and action-normalized consequences. The gas has
finite energy density and an infinite total reservoir; its infinite-volume
description precedes the long-window limit.

A13 changes spacing correlations at fixed mass, speed and density. Independent
spatial gaps supply the exact Markov clock; the next proof should identify
which weaker preparation assumptions retain a positive plateau.
