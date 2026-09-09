# B27: the relativistic Kepler angular-momentum threshold

## Finding

For the one-particle Hamiltonian

\[
H(r,p_r;L)=\sqrt{m^2c^4+c^2(p_r^2+L^2/r^2)}-\frac{k}{r},
\qquad r>0,\quad k>0,
\]

the collision-free bound radial well exists exactly when \(|L|>k/c\). Its
bottom is the circular orbit

\[
E_{\min}(L)=mc^2\sqrt{1-\left(\frac{k}{c|L|}\right)^2}.
\]

This threshold and the endpoint behavior are standard in Boyer's explicit
classification: his \(\alpha\) is this companion's \(k\), and he takes the
orientation with \(L>0\). ArXiv PDF p. 6, Eqs. (19)--(20), gives the radial
turning polynomial and its two roots; pp. 9--10, Eqs. (37)--(42), separates
\(L>\alpha/c\), \(L=\alpha/c\), and \(L<\alpha/c\), calls the first regime's
bound trajectories two-turning-point rosettes, and states that the latter two
regimes reach the centre in finite time. This is a standard benchmark, not a
novelty claim.

## Written derivation and endpoint

At a radial turning point set \(x=1/r\). The effective radial energy is

\[
F_L(x)=\sqrt{m^2c^4+c^2L^2x^2}-kx,\qquad x>0.
\]

If \(|L|>k/c\), then \(F_L(0)=mc^2\) and \(F_L(x)\to+\infty\) as
\(x\to\infty\). Its unique critical point satisfies

\[
\frac{c^2L^2x}{\sqrt{m^2c^4+c^2L^2x^2}}=k,
\]

and substitution gives the stated minimum. Hence energies
\(E_{\min}(L)<E<mc^2\) have two positive turning radii; equality is the
circular orbit. This is also obtained by making the square root in Boyer's
p. 6 Eq. (20) vanish.

At the endpoint \(|L|=k/c\),

\[
F_L(x)=\sqrt{m^2c^4+k^2x^2}-kx\downarrow0
\quad (x\to\infty),
\]

so the infimum occurs only at the excluded singular boundary \(r=0\): there
is no collision-free radial well. For \(|L|<k/c\), \(F_L(x)\to-\infty\).
Boyer's p. 9 Eq. (38) treats equality separately, while p. 10 and Eqs.
(41)--(42) verify finite-time arrival at the centre for both equality and the
subcritical regime. Thus the strict inequality matters.

The dimensions are \([k]=\mathrm{energy}\,\mathrm{length}\), so \(k/c\) has
units of action/angular momentum. It is positive because the externally
specified coupling \(k\) and limiting speed \(c\) are positive; it is not
dynamically selected or universal across potentials or couplings.

## Model boundary

This is special-relativistic kinetic energy plus a prescribed static
\(-k/r\) potential about a fixed centre. It can model a test particle in an
external Coulomb field under the stated approximation. It is not a
relativistically closed two-body theory: centre recoil, field degrees of
freedom, retardation, radiation, and self-force are absent. Accordingly the
threshold establishes a one-body external-potential benchmark, not a general
relativistic Kepler theorem and not an action-selection mechanism.

## Source and reading coverage

- **Timothy H. Boyer**, *Unfamiliar trajectories for a relativistic particle
  in a Kepler or Coulomb potential*, *American Journal of Physics* **72**
  (2004), 992--997. DOI: `10.1119/1.1737396`; arXiv:
  `physics/0405090v1`. **metadata, abstract, passage**.
  Open source: <https://arxiv.org/abs/physics/0405090v1>.
- Exactly four pages of the arXiv PDF were read: internal pp. **5, 6, 9, and
  10**. Equations (14)--(20) and (37)--(42), plus their surrounding prose,
  were extracted with `pdftotext -layout`. No other PDF pages were read.
- Local retrieval (ignored build path):
  `.build/b27/Boyer_UnfamiliarTrajectories_physics0405090.pdf`.
  SHA-256:
  `7ebbf94fa5adc6c8b22852d9ac86a41343995ab08e2cefb0a255e8c6e8c7ee3b`.
- Three discovery queries were used: `site:arxiv.org relativistic classical
  Coulomb orbit angular momentum Ze^2/c minimum energy sqrt 1`; `classical
  relativistic Kepler problem L > k/c minimum energy paper`; and `Sommerfeld
  relativistic Kepler Hamiltonian angular momentum k/c plunge orbit equation`.
  Search snippets and experimental HTML were routing aids, not counted as PDF
  pages and not used as substitutes for the passages above.
- Extraction is clean for the displayed equations on the listed pages. The
  source uses both \(E\) for total relativistic energy and a rest-energy-shifted
  energy in nearby prose; this companion uses \(E\) only for the Hamiltonian
  value displayed at the top.

## Proposed verified BibTeX

```bibtex
@article{Boyer2004UnfamiliarTrajectories,
  author = {Boyer, Timothy H.},
  title = {Unfamiliar trajectories for a relativistic particle in a Kepler or Coulomb potential},
  journal = {American Journal of Physics},
  volume = {72},
  pages = {992--997},
  year = {2004},
  doi = {10.1119/1.1737396},
  eprint = {physics/0405090},
  archivePrefix = {arXiv}
}
```

## Source-to-goal next test

Use \(k/c\) as a positive classical survival-threshold benchmark, then test
the programme's universality gate: vary the supplied coupling \(k\) across otherwise identical
one-body models. The threshold scales with \(k\) and vanishes as \(k\to0\), so
any proposed universal positive action scale must add a premise that fixes or
replaces this coupling-dependent quantity rather than merely appeal to finite
propagation speed and central binding.
