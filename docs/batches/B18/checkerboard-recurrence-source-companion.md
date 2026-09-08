# Skopenkov–Ustinov, “Feynman checkers: towards algorithmic quantum theory”

**Result.** The selected primary source (arXiv:2007.12879v2, dated 28 February
2022; v1 was 2020; published
*Russian Mathematical Surveys* 77:3 (2022), 445–530, DOI
[10.1070/RM10025](https://doi.org/10.1070/RM10025)) gives the exact corner-weighted
checkerboard normalization and two-component recurrence needed for the A09b
recurrence gate. Definition 2 uses lattice step \(\varepsilon\), mass \(m\),
and amplitude weight \((1+m^2\varepsilon^2)^{(1-t/\varepsilon)/2}
i(-im\varepsilon)^{\mathrm{turns}}\). Proposition 5 is the numbered Dirac
recurrence (equations (3)–(4)); Proposition 6 gives exact finite-step
probability conservation. The continuum result is a propagator limit, but the
authors explicitly warn that its light-cone distributions have no ordinary
probabilistic square or global charge-conservation analogue.

## Source and coverage

- **Source:** M. B. Skopenkov and A. V. Ustinov, “Feynman checkers: towards
  algorithmic quantum theory,” arXiv:2007.12879v2 (explicitly selected, dated
  28 February 2022; v1 was 2020);
  publisher page: https://www.mathnet.ru/eng/rm10025.
- **Retrieved:** 2026-09-08 from https://arxiv.org/pdf/2007.12879v2.
- **Local original:** `.build/b18/Skopenkov_Ustinov_2007.12879v2.pdf` (cache;
  not a project-authored source file). Redistribution rights were not separately
  established; the PDF stays in the ignored cache, with versioned retrieval URL
  and hash for reproduction.
- **SHA-256:** `5c839f7ae32e5688e1245a58a9f9447841a749cf61009a049ae55b7e9f41d5ac`.
- **Extraction:** `pdftotext -layout`; equations and symbols visually checked
  in the rendered PDF pages listed below. Coverage is selected passage, not a
  full-paper read: PDF pages 12–14 and 17–19 (six selected pages; page
  numbers are the printed numbers in the PDF; PDF page 12 contains Definition
  2 and PDF page 13 contains Propositions 5–6). The arXiv abstract/metadata
  route was one targeted search; no historical original pages were inspected.
  Coordinator additionally checked pp. 12, 13, 19 and 31 visually, and verified
  the version date against arXiv and the English journal metadata against MathNet.

## Source digest and exact passages

### Definition and normalization (printed p. 12, Definition 2; PDF p. 12)

The lattice is \(\varepsilon\mathbb Z^2\), with steps \((\varepsilon,\varepsilon)\)
or \((-\varepsilon,\varepsilon)\). `turns(s)` counts interior points where
the successive step vectors are orthogonal (corners/reversals). For paths from
\((0,0)\) to \((x,t)\), first step \((\varepsilon,\varepsilon)\), the source
defines
\[
a(x,t,m,\varepsilon)=(1+m^2\varepsilon^2)^{(1-t/\varepsilon)/2}i
\sum_s(-im\varepsilon)^{\mathrm{turns}(s)},\qquad
P=|a|^2.
\]
The natural units are \(\hbar=c=1\), so \(m\varepsilon\) is dimensionless.
The stated physical interpretation is probability in the \(\varepsilon\times
\varepsilon\) square, conditional on the source's initial direction.

### Recurrence and exact conservation (printed p. 13, Propositions 5–6;
PDF p. 13)

Writing \(a_1=\operatorname{Re}a\), \(a_2=\operatorname{Im}a\), the source gives
\[
a_1(x,t+\varepsilon)=\frac{a_1(x+\varepsilon,t)+m\varepsilon a_2(x+\varepsilon,t)}
 {\sqrt{1+m^2\varepsilon^2}},
\]
\[
a_2(x,t+\varepsilon)=\frac{a_2(x-\varepsilon,t)-m\varepsilon a_1(x-\varepsilon,t)}
 {\sqrt{1+m^2\varepsilon^2}}.
\]
These are explicitly Proposition 5, titled “Dirac equation.” Proposition 6
states \(\sum_{x\in\varepsilon\mathbb Z}P(x,t,m,\varepsilon)=1\) for every
positive lattice time. Its proof is located at printed/PDF p. 31 (printed p. 30
is the dependency chart), and was not part of the visual page sample; the
extracted proof shows the sum-of-squares cancellation. Thus this is exact at
finite step, not only a limiting statement. The source's basis/order is
\((a_1,a_2)=(\Re a,\Im a)\),
with the first component receiving the right-shifted predecessor and the second
the left-shifted predecessor; the initial first-step convention fixes the phase.

### Continuum and non-relativistic statements (printed pp. 17–19; PDF pp. 17–19)

Corollary 5 (p. 17, equation (22)) gives the Feynman triple limit with
\(t\to\infty\), \(x/t\to0\), \(\varepsilon\to0\), under the sharp sequence
conditions \(1/t\to0\), \(x/t^{3/4}\to0\), and \(\varepsilon t^{1/2}\to0\). Its
right side is, up to \(e^{-imt}\), the free non-relativistic kernel (24),
\(\sqrt{m/(2\pi t)}\exp(imx^2/(2t)-i\pi/4)\). Corollary 6 (p. 18,
equation (23)) gives the uniform compact-subset \(\varepsilon\to0\) limit to
the Bessel-function spin-1/2 retarded propagator. The factor \(1/(2\varepsilon)\)
in (23) is explained as the length associated to one black lattice point and,
more deeply, by the Green-function normalization.

The caveat on printed p. 19 is material: the singular point-source continuum
retarded propagator has
generalized-function terms on \(t=\pm x\); squaring those delta terms is
ill-defined, so that point-source kernel has no direct probabilistic
interpretation and no global charge-conservation analogue. Regular \(L^2\)
wavepackets retain unitary norm conservation. Finite-step Proposition 6 must
not be silently promoted to a pointwise continuum probability statement.

## Source-to-model audit for the coordinator construction

The source directly supports the abstract two-component pattern, corner mixing,
and finite-step norm identity, but not the following dimensional generalization;
the latter is a derived coordinator construction. Let
\[
P_{\rm real}=(1-\lambda\varepsilon)I+\lambda\varepsilon\sigma_x,
\quad (Sf)_\pm(x)=f_\pm(x\mp c\varepsilon).
\]
For \(0\le\lambda\varepsilon\le1\), this is a real stochastic coin/shift:
its \(\ell^1\) probability is conserved, but it is generally not an
\(\ell^2\)-unitary quantum evolution. The source's complex corner weight is
therefore not a positive reversal probability.

With \(K>0\), \(\omega=mc^2/K\), use instead
\[
C=\frac{I-i\omega\varepsilon\sigma_x}{\sqrt{1+\omega^2\varepsilon^2}},
\qquad U=SC.
\]
Since \(\sigma_x=\sigma_x^\dagger\) and \(\sigma_x^2=I\), \(C^\dagger C=I\);
the translation shift \(S\) is unitary on \(L^2(\mathbb R;\mathbb C^2)\), hence
\(U\) is exactly unitary at every finite \(\varepsilon\). Expanding the stated
shift/order gives
\[
U=I-c\varepsilon\sigma_z\partial_x-i\omega\varepsilon\sigma_x+O(\varepsilon^2),
\]
so the formal continuum equation is
\[
iK\partial_t\psi=(-iKc\sigma_z\partial_x+mc^2\sigma_x)\psi.
\]
The basis/sign/order must be retained: reversing the shift flips the transport
sign. Applying the coin after the shift changes factor order only at
\(O(\varepsilon^2)\), leaving the first-order generator unchanged. A Fourier
matrix-product proof for fixed \(T\),
\(U_{T/N}^N\to\) the Dirac propagator, remains a coordinator derivation rather
than a statement read from this source.

The positive-energy branch has the derived dispersion
\(E_p=\sqrt{m^2c^4+p^2c^2}\), hence \(E_p-mc^2\to p^2/(2m)\) as \(c\to\infty\).
The real telegraph/Kac analogue gives heat coefficient \(D=K/(2m)\) only
after specifying the real reversal process and scaling; this source does not
select \(K\), nor does it supply the physical premise selecting complex
amplitudes over real probabilities. Analytic continuation requires a global
phase convention and is not exactly unitary for the real stochastic coin at
finite step.

### C040: ideal direction measurement after each step

Starting in a definite direction and performing an ideal projective direction
measurement after every $U_\varepsilon$ step gives the Born flip probability
\[
q=\frac{\omega^2\varepsilon^2}{1+\omega^2\varepsilon^2}.
\]
For $N=T/\varepsilon$ steps,
\[
\Pr(\text{at least one flip})\le Nq\le\omega^2T\varepsilon\to0.
\]
Thus fixed $\omega$ has a ballistic continuous-cut limit, distinct from the
finite-rate telegraph scaling $q=\lambda\varepsilon$. This is an elementary
measurement-protocol consequence of the audited coin, not a novelty claim.

## Status and remaining obligation

**Established by this bounded modern audit:** Definition 2 corner count and
normalization; Proposition 5 (not “Proposition 1”) recurrence; Proposition 6
finite-step probability conservation; continuum retarded-propagator and
non-relativistic-kernel statements with their caveat. **Derived consequences:**
the dimensional coin/shift construction, exact unitary check, Dirac expansion,
dispersion limit, and telegraph heat coefficient. **Open:** original Feynman /
Hibbs and 1984 Gaveau–Jacobson–Kac–Schulman/Jacobson–Schulman pages remain
uninspected; a physical premise selecting complex amplitudes and a positive
action parameter \(K\) is still required.
