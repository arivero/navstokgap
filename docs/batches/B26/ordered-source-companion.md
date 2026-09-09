# B26: ordered counterpropagating lattices

## Finding

The bounded ordered two-lattice preparation in `notes/ordered-beam-preparation.md`
was not matched in the bounded search. The sources located concern the standard
Jepsen mapping with independently random (or canonical) positions and velocities,
or finite-box effects; none studies two independently uniformly shifted,
counterpropagating equal-spacing lattices with the resulting deterministic
periodic tagged velocity. Thus the draft's zero long-window action response is
currently a derived consequence of its explicit correlated preparation, not a
reported literature result.

## Bounded source coverage

Two discovery queries were used (ordered/lattice Jepsen gas; lattice initial
conditions and equal spacing). Search snippets were treated only as discovery
leads. Two HTML source documents were opened; these are not two verified
PDF pages. The line ranges below are worker reports. Coordinator verified
metadata and abstracts at [0804.1866v2](https://arxiv.org/abs/0804.1866v2)
and [1209.1572v1](https://arxiv.org/abs/1209.1572v1). No source formula
enters the proof of C051:

* Sanjib Sabhapandit, Ioana Bena and Satya N. Majumdar, *Statistics of the
  total number of collisions and the ordering time in a freely expanding
  hard-point gas*, arXiv:0804.1866 (2008), abstract and pp.-equivalent HTML
  lines 17–20, 42–47, 44–46, 48–55. **abstract/passage**. It defines equal-mass
  hard-point collisions as velocity exchange and explicitly assumes positions
  and velocities drawn independently (lines 44–45), then studies free expansion
  and eventual fan ordering, not stationary ordered lattices.
* Anjan Roy, Onuttom Narayan, Abhishek Dhar and Sanjib Sabhapandit, *Tagged
  Particle Diffusion in One-Dimensional Gas with Hamiltonian Dynamics*,
  arXiv:1209.1572 (2012), abstract and pp.-equivalent HTML lines 9–18,
  26–28, 151–160. **abstract/passage**. The introduction attributes the
  equal-mass Jepsen tagged-diffusion result and its velocity-exchange mapping
  (lines 13–16); the finite-box calculation uses canonical uniformly ordered
  positions and independent Gaussian velocities (lines 26–28), unlike B26.

## Comparison and limits

The relevant distinction is preparation, not collision law. The standard
Jepsen results cited above exploit random independent data and produce a
diffusive tagged regime. B26 fixes each stream's spacing and randomizes only
two global phases. The Palm residual is uniform on one collision interval,
after which all waits equal that interval; the tagged velocity is therefore a
stationary square wave with period `2d`, rather than a Markov process with
exponential waits. A literature statement that “equal-mass hard-point gases
are Jepsen gases” does not establish the B26 covariance or its zero plateau.

## Verified metadata / BibTeX

```bibtex
@article{SabhapanditBenaMajumdar2008,
  author = {Sabhapandit, Sanjib and Bena, Ioana and Majumdar, Satya N.},
  title = {Statistics of the total number of collisions and the ordering time in a freely expanding hard-point gas},
  eprint = {0804.1866}, archivePrefix = {arXiv}, year = {2008}
}
@article{RoyNarayanDharSabhapandit2012,
  author = {Roy, Anjan and Narayan, Onuttom and Dhar, Abhishek and Sabhapandit, Sanjib},
  title = {Tagged Particle Diffusion in One-Dimensional Gas with Hamiltonian Dynamics},
  eprint = {1209.1572}, archivePrefix = {arXiv}, year = {2012}
}
```

## Source-to-model idea

Use the standard Jepsen velocity-exchange mapping as a control preparation:
compare independent gaps (Poisson clock, positive plateau) with fixed gaps and
random global phases (periodic cancellation, zero plateau), holding `m`, `u`
and `rho` fixed. The deciding premise is gap mixing/renewal, not equal-mass
elasticity alone. A useful next test is a stationary correlated gap process with
finite correlation length, to identify whether a positive plateau is restored
and which correlation assumptions are sufficient.
