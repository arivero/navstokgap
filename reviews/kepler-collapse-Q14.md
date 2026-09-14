# Q14 review: the Coulomb collapse thresholds are C052's plunge condition with the angular action measured in $\hbar$

**Result.** The remark in Section 6 of
[`action-unit-dimensional-selection.md`](../notes/action-unit-dimensional-selection.md)
is correct and understates the correspondence. The classical energy identity
of C052 is the symbol of the radial Klein--Gordon equation, and its
$1/r^2$ coefficient $c^2\ell^2-k^2$ is what the quantum collapse conditions
test. The Klein--Gordon threshold $Z\alpha=l+1/2$ is the classical plunge
condition $|L|>k/c$ with $|L|=\hbar(l+1/2)$; the Dirac threshold
$Z\alpha=|\kappa|=j+1/2$ is the same condition with $|L|=\hbar|\kappa|$. In
addition, C052's circular-orbit energy at $|L|=\hbar|\kappa|$ equals every
Dirac level with zero radial quantum number, and quantizing C052's radial
action gives Sommerfeld's formula, which is the full Dirac spectrum. The
only quantum input is the unit in which the angular action is measured at
the plunge boundary. No new theorem is claimed; this is the Sommerfeld--Dirac
coincidence of 1916 and 1928 in the repository's own notation.

Task: bounded mathematical and primary-source audit of the Section 6 remark,
requested by the user on 2026-09-14 in order to understand how the quantum
wave-equation thresholds arise from the classical arguments of this
repository. Role: coordinator, Claude Fable 5.1, no worker. Budget used:
three web queries and six fetches, two of them blocked by publisher walls;
two open arXiv PDFs read at passage level; nothing downloaded into `docs/`.
Inputs: the Q14 note, the C052 note and B27 companion. This file is the only
output besides the remark replacement in the note and the handoff update.

## 1. The classical identity is the symbol of the Klein--Gordon radial equation

C052 uses $H=\sqrt{m^2c^4+c^2(p_r^2+\ell^2/r^2)}-k/r$ with fixed $m,c,k>0$
and $\ell=|L|$. Squaring $E+k/r$ gives the energy identity recorded there:

$$c^2p_r^2=E^2-m^2c^4+\frac{2Ek}{r}+\frac{k^2-c^2\ell^2}{r^2}.\tag{C}$$

The stationary Klein--Gordon equation with minimal coupling to $V=-k/r$ is
$(E+k/r)^2\psi=(m^2c^4-\hbar^2c^2\nabla^2)\psi$. With
$\psi=r^{-1}u(r)Y_{lm}$ the radial equation is

$$\hbar^2c^2u''+\Big[E^2-m^2c^4+\frac{2Ek}{r}
 +\frac{k^2-\hbar^2c^2\,l(l+1)}{r^2}\Big]u=0.\tag{KG}$$

Term by term, (KG) is (C) under $c^2p_r^2\mapsto-\hbar^2c^2\,d^2/dr^2$ and
$c^2\ell^2\mapsto\hbar^2c^2\,l(l+1)$. The attractive $k^2/r^2$ term is the
same classical expression in both: it comes from squaring the minimally
coupled energy, before any quantum rule is applied. Set
$Z\alpha:=k/(\hbar c)$; for $k=Ze^2/(4\pi\epsilon_0)$ this is $Z$ times the
fine-structure constant, and $k/c=Z\alpha\hbar$ is the action unit of the
Q14 note.

## 2. The indicial equation restores the classical form with $\ell=\hbar(l+1/2)$

Near $r=0$ the $1/r^2$ term dominates (KG). Substituting $u\sim r^{\sigma}$
gives the indicial equation $\sigma(\sigma-1)=l(l+1)-(Z\alpha)^2$, that is

$$\Big(\sigma-\tfrac12\Big)^2=\Big(l+\tfrac12\Big)^2-(Z\alpha)^2.$$

Both exponents are real exactly when $l+1/2\ge Z\alpha$, which is
$\hbar(l+1/2)\ge k/c$. C052's regular domain is $\ell>k/c$. The two
conditions coincide under $\ell=\hbar(l+1/2)$; the half arises because the
Frobenius equation completes $l(l+1)$ to the square $(l+1/2)^2-1/4$, the
same shift as Langer's modification. Beyond the threshold
$\sigma=1/2\pm i\nu$, so $u\sim r^{1/2}\cos(\nu\ln r+\varphi)$: both
solutions are square-integrable at the origin ($|u|^2\sim r$), regularity
selects nothing, and the energies obtained from the regular-solution
condition become complex. This is the quantum fall to the centre, and it
sits at the classical plunge boundary.

The Klein--Gordon levels themselves are

$$E_{n_r,l}=mc^2\Big[1+\frac{(Z\alpha)^2}
 {\big(n_r+\tfrac12+\sqrt{(l+1/2)^2-(Z\alpha)^2}\big)^2}\Big]^{-1/2},$$

Suslov's Eq. (28) and, for $l=0$, Bouaziz's Eq. (7). Compared with the
classical Sommerfeld formula of Section 4 below, both quantum numbers
acquire a half: $n_r\mapsto n_r+1/2$ and $n_\varphi\mapsto l+1/2$. The
threshold therefore transfers exactly, while the circular energies do not.

## 3. The Dirac thresholds and the $n_r=0$ levels are C052 at $\ell=\hbar|\kappa|$

For the radial Dirac system the indicial exponent is
$s=\sqrt{\kappa^2-(Z\alpha)^2}$ with $|\kappa|=j+1/2$; Suslov's Eqs.
(29)--(32) give the same content through the Langer form
$C=(\nu+1/2)^2$ with $\nu=\sqrt{(j+1/2)^2-(Z\alpha)^2}$. The exponent is
real exactly when $|\kappa|\ge Z\alpha$, which is C052's condition with
$\ell=\hbar|\kappa|$. For the ground state $\kappa=-1$ the threshold is
$Z\alpha=1$.

The Dirac levels are (Suslov (31)--(32))

$$E_{n_r,j}=mc^2\Big[1+\frac{(Z\alpha)^2}
 {\big(n_r+\sqrt{(j+1/2)^2-(Z\alpha)^2}\big)^2}\Big]^{-1/2}.$$

At $n_r=0$ this reduces to $mc^2\sqrt{1-(Z\alpha)^2/(j+1/2)^2}$. C052's
circular-orbit energy is $E_{\min}(\ell)=mc^2\sqrt{1-k^2/(c^2\ell^2)}$, and
$k/(c\ell)=Z\alpha\hbar/\ell$. At $\ell=\hbar(j+1/2)$ the two expressions
are identical. Every Dirac level with zero radial quantum number
($1s_{1/2}$, $2p_{3/2}$, $3d_{5/2}$, and so on) is the energy of the
classical circular orbit with angular action $\hbar|\kappa|$. The Dirac
ground state is the classical circle at $\ell=\hbar$, and its collapse at
$Z\alpha=1$ is the classical plunge boundary reached at $Z=1/\alpha$.

## 4. Sommerfeld's formula from C052's radial action

In the regular domain of C052 write (C) as
$c^2p_r^2=-A+2B/r-C/r^2$ with $A=m^2c^4-E^2>0$ for a bound orbit,
$B=Ek$ and $C=c^2\ell^2-k^2>0$. The radial action over one libration is

$$J_r=\frac{1}{2\pi}\oint p_r\,dr
 =\frac1{\pi c}\int_{r_1}^{r_2}\sqrt{-A+2B/r-C/r^2}\,dr,$$

with turning radii $r_1<r_2$ the roots of $-Ar^2+2Br-C=0$, so that
$r_1+r_2=2B/A$ and $r_1r_2=C/A$. Since
$-Ar^2+2Br-C=A(r_2-r)(r-r_1)$, the integral reduces to
$\sqrt A\int_{r_1}^{r_2}\sqrt{(r_2-r)(r-r_1)}\,dr/r$. For $0<a<b$,

$$\int_a^b\frac{\sqrt{(b-x)(x-a)}}{x}\,dx=\frac{\pi}{2}(a+b)-\pi\sqrt{ab}.$$

Two checks fix this evaluation: at $a=b$ both sides vanish, and as
$a\downarrow0$ the left side is $b\int_0^1\sqrt{(1-t)/t}\,dt
=b\,\Gamma(1/2)\Gamma(3/2)/\Gamma(2)=\pi b/2$, matching the right side.
Hence

$$J_r=\frac1c\Big[\frac{Ek}{\sqrt{m^2c^4-E^2}}-\sqrt{c^2\ell^2-k^2}\Big],$$

which is Sommerfeld's generic integral (Suslov Eqs. (5)--(6)). At the
circular orbit $B^2=AC$ and $J_r=0$; at the threshold $C=0$ the inner
turning radius reaches the centre. Imposing $J_r=n_r\hbar$ and
$\ell=n_\varphi\hbar$ gives
$Ek/(\hbar c\sqrt{m^2c^4-E^2})=n_r+\sqrt{n_\varphi^2-(Z\alpha)^2}=:N$, so

$$E=mc^2\Big[1+\frac{(Z\alpha)^2}{N^2}\Big]^{-1/2},$$

Sommerfeld's 1916 fine-structure formula. It coincides with the Dirac
spectrum of Section 3 under $n_\varphi\leftrightarrow j+1/2=|\kappa|$. The
nonrelativistic check is the same integral with $A=2m|E|$, $B=mk$,
$C=\ell^2$, giving $J_r+\ell=k\sqrt{m/(2|E|)}$ and the Kepler--Bohr
levels.

## 5. What is derived and what is supplied

Derived from C052 with one rule, angular action in units of $\hbar$: the
Klein--Gordon threshold ($\ell=\hbar(l+1/2)$), the Dirac threshold
($\ell=\hbar|\kappa|$), the Dirac $n_r=0$ levels as circular orbits, and
with radial action quantization the full Dirac spectrum. Supplied and
unexplained here: the wave equations themselves, spin, which half-integer
multiples occur ($l+1/2$ for a scalar, $|\kappa|$ for a spinor), the extra
$n_r+1/2$ of the scalar spectrum, and radiative corrections. The mechanism
of the coincidence is the symbol relation (C)--(KG) together with the
Frobenius completion of the centrifugal term, which reproduces the
classical plunge structure exactly because the collapse is decided by the
$1/r^2$ coefficient alone.

Planck's constant enters once, as the unit of the angular action at the
plunge boundary: threshold $\Leftrightarrow\ell_{\min}/\hbar=Z\alpha$,
which is Q14's $k_e/c=\alpha\hbar$ read at $Z=1$. The factor $1/\alpha$
of the note's item 5 is therefore the statement that the Dirac ground state
reaches the classical boundary at $Z=1/\alpha\approx137$; for hydrogen the
classical boundary lies at $\ell=\alpha\hbar$, a factor $\alpha$ below the
actual ground-state angular action. Zeldovich and Popov's abstract records
that a finite nuclear size moves the Dirac critical charge to
$Z_c\approx170$, where the $1s_{1/2}$ level reaches the lower continuum;
this is the quantum counterpart of C053, where a softened core removes the
classical threshold. That parallel is an observation, not a claim.

## 6. Primary-literature comparison and exact coverage

1. Sergei K. Suslov, "The 'Sommerfeld Puzzle' and Its Extensions,"
   [arXiv:2401.07485](https://arxiv.org/abs/2401.07485) (2024), 18 pages.
   Reading level: **passage**, pp. 1--3 and 5--7, Eqs. (1)--(6) and
   (26)--(32). Abstract: "The exact agreement between the Sommerfeld (1916)
   and Dirac (1928) results for the energy levels of the relativistic
   hydrogen atom (the so-called 'Sommerfeld puzzle') is analyzed and
   extended." Page 1: "In 1916 Arnold Sommerfeld applied the quantization
   rules of the 'old' quantum theory to the relativistic hydrogen atom.
   Exact solution was obtained by C. G. Darwin and W. Gordon only in 1928
   after discovery of the Dirac equation: The new answer was precisely the
   'old' Sommerfeld formula!" Eqs. (5)--(6) state the generic integral of
   Section 4; Eq. (27) gives $\nu=-1/2+\sqrt{(l+1/2)^2-\mu^2}$ and Eq.
   (28) the scalar spectrum; Eqs. (31)--(32) give the Dirac spectrum with
   $\nu=\sqrt{(j+1/2)^2-\mu^2}$, $\mu=Ze^2/(\hbar c)$.
2. Djamil Bouaziz, "Klein-Gordon Equation with Coulomb Potential in the
   Presence of a Minimal Length,"
   [arXiv:1311.7405](https://arxiv.org/abs/1311.7405) (2013), 9 pages.
   Reading level: **passage**, pp. 3--4, Eqs. (3)--(7), the ordinary
   Klein--Gordon Coulomb problem at $l=0$ in momentum space. Eq. (5)
   defines $\mu=\sqrt{1/4-Z^2e^4/(\hbar^2c^2)}$; p. 4: "In the case
   $Z>68$, the parameter $\mu$ becomes imaginary and thus the spectral
   condition (7) fails. In order to obtain a discrete spectrum, the
   potential must be regularized by introducing a cutoff at short
   distances." $Z=68$ is $Z\alpha\approx0.496$; the sentence "When $Z<68$,
   the general solution is a linear combination" reads as $Z>68$ in
   context. Eq. (7), $1/2-w+\mu=-n$ with $w=ZEe^2/(\hbar c\epsilon)$ and
   $\epsilon=\sqrt{m^2c^4-E^2}$, is Section 2's level formula at $l=0$.
3. L. C. Biedenharn, "The 'Sommerfeld Puzzle' revisited and resolved,"
   *Foundations of Physics* **13** (1983), 13--34, DOI
   [10.1007/BF01889408](https://doi.org/10.1007/BF01889408). Reading
   level: **record only**; Springer and PhilPapers refused the fetch and
   the Semantic Scholar record carries no abstract. Cited for the name and
   date of the coincidence; its resolution through a hidden symmetry is
   reported by secondary summaries and was not inspected.
4. Ya. B. Zeldovich and V. S. Popov, "Electronic structure of superheavy
   atoms," *Soviet Physics Uspekhi* **14** (1972), 673--694, DOI
   [10.1070/PU1972v014n06ABEH004735](https://doi.org/10.1070/PU1972v014n06ABEH004735).
   Reading level: **abstract**: "$Z_c\approx170$ is the critical value of
   the nuclear charge, at which the energy of the ground state of the
   $1S_{1/2}$ electron reaches the limit of the lower continuum of the
   solutions of the Dirac equation."
5. Records not inspected: A. Sommerfeld, *Annalen der Physik* **356**
   (1916), 1--94, DOI 10.1002/andp.19163561702 (Wiley refused the fetch;
   cited through Suslov's reference [27]); Landau and Lifshitz, *The
   Classical Theory of Fields* §39 and *Quantum Mechanics* §35, the
   standard treatments of the classical Coulomb fall and the quantum fall
   to the centre.

Queries: "Biedenharn 1983 Sommerfeld puzzle revisited and resolved
Foundations of Physics Dirac Coulomb"; "Klein-Gordon equation Coulomb
potential critical coupling $Z\alpha=1/2$ $(l+1/2)^2$ fall to the center";
and the B27 queries already recorded. Coverage is bounded; the
correspondence is established textbook material and no novelty is
asserted.

## Verdict and remaining dependency

Accept the Section 6 remark as audited at passage level for the scalar and
spinor thresholds and for the Dirac $n_r=0$ levels, with the Biedenharn and
Sommerfeld records unread. The remark in the note is replaced by the
audited statement with a link here. Proof status: elementary written
derivations above, using C052's identity and two standard radial
equations. Literature status: exact match with the Sommerfeld--Dirac
coincidence; the scalar threshold is standard. Q14 remains exploratory
with no ledger promotion; if promoted, the claim would read "C052's
threshold and circular energies coincide with the Dirac Coulomb thresholds
and zero-radial-node levels under $\ell=\hbar|\kappa|$," with the
literature match recorded as exact.

The remaining dependency is unchanged from Q14: the physical premise that
fixes the ground-state angular action at $\hbar$ rather than at the
classical unit $\alpha\hbar$. The audit sharpens its form: the classical
model already contains the collapse structure, and the quantum theory
contributes the unit of angular action at the boundary.
