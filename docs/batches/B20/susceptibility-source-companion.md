# B20: susceptibility and spectral control

Pavliotis supplies the Green–Kubo/Poisson representation used in C019.
C041–C042 are finite-dimensional spectral and observability consequences,
derived and checked in the project.

## Primary source and coverage

G. A. Pavliotis, *Asymptotic analysis of the Green–Kubo formula*,
[arXiv:1002.4103v1](https://arxiv.org/abs/1002.4103v1), 22 February 2010.

- Cached original: `.build/a01/Pavliotis2010.pdf`.
- SHA-256: `accd38a7a292d92d35583c9ae0d4421fefb67b26b2cf7acf177a71cb08b408a3`.
- Worker passage reading: printed pp. 4–5, Proposition 2.1, (2.3)–(2.8).
  Extraction with `pdftotext -layout`; worker reports visual checking.
  Coordinator reread both pages and visually verified p. 5 using the cached
  B16 image, including the minus sign in the Poisson equation.
- Equation (2.3) expresses diffusion through velocity and the Poisson solution;
  (2.4) gives $-L\phi=V$; (2.5) gives the integrated velocity correlation.
  The source switches invariant-measure notation from $\pi$ to $\mu$.
  The project consistently uses $\pi$.
- Version date independently checked against arXiv. See the
  [maintained companion](../../Pavliotis_GreenKubo_2010.md) for the generated
  title-page date and rights: the original stays in the ignored cache.

## Claim mapping

**C041:** Spectral expansion on the centered finite space gives
$H\gamma_{\min}\le2m\|v\|_\pi^2\le H\gamma_{\max}$, with
$H=2m\langle v,(-Q)^{-1}v\rangle_\pi$. An independent slow two-state label
leaves the velocity plateau unchanged and makes the full gap
$2\min(\lambda,\epsilon)\to0$. This is a standard product-chain consequence.
For a supplied action unit $K$, the energy-normalized gap is $K\gamma$;
in the two-state case $K=H=mu^2/\lambda$ gives $2mu^2$.

**C042:** If the centered observable frame satisfies
$F=\sum_a|f_a\rangle\langle f_a|\ge\alpha I$, then
$S=\operatorname{Tr}(A^{-1}F)\ge\alpha/\gamma_{\min}$ and hence
$\gamma_{\min}\ge\alpha/S$. The inverse-operator identity and the trace
argument are elementary spectral consequences. Their exact combined
presentation was not matched to a prior source in this bounded audit;
no novelty claim is made. Uniform families require a positive uniform frame
bound and a uniform upper bound on total susceptibility. Each finite
irreducible member has a positive gap even when the family has infimum zero.

## Discovery lead and search limits

The worker used one search and identified Sokal,
*Monte Carlo Methods in Statistical Mechanics: Foundations and New Algorithms*,
*Functional Integration* (1997), pp. 131–192,
DOI 10.1007/978-1-4899-0319-8_6. No Sokal passage was retrieved.
The coordinator's DOI open failed; one further search found supporting
bibliographic leads but no primary passage. This remains a discovery-only
route for integrated versus exponential correlation times, not an imported
theorem or a page-level attribution.

One cached primary source was passage-read. The worker's two-source,
six-page ceiling was respected. The exact observable-frame formulation was
not independently searched. Proof review and literature coverage are separate.

## Source-generated next test

Test whether mechanical access to internal variables gives a quantitatively
complete observable collection. Then test whether its summed response stays
bounded under composition and limiting operations. A bounded speed controls
amplitudes; the inverse-generator response also depends on correlation time.
