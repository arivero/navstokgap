# One-loop torus valleys: local confinement, periodicity and spectral limits

For a constant abelian $SU(2)$ background on $T^3_L$, the one-loop
zero-point energy defined by discarding the formal $m=0$ Fourier term in the
Poisson-summed expression (distinct from the physical $k=0$ oscillator) is
$$U(a)=\frac{2\hbar c}{\pi^2L}\Phi(La),\qquad
\Phi(b)=\sum_{m\in\mathbb Z^3\setminus\{0\}}
\frac{1-\cos(m\cdot b)}{|m|^4}.$$
Here $[a]=L^{-1}$. This nonnegative bounded periodic function has the
local expansion
$$U(a)=2\hbar c|a|+\frac{C_M}{3\pi^2}\hbar cL|a|^2
+O(\hbar cL^2|a|^3).$$
The first term is the four transverse zero-mode oscillators' energy;
the quadratic correction is useful input to a small-volume comparison.
The formula is exact for this specified one-loop prescription, not for
the interacting ground-state energy. A local Taylor expansion supplies
neither the global operator bound nor the nonzero-mode estimates in
[the Feshbach reduction](weak-coupling-feshbach-reduction.md).

The derivation below retains the frequency count, Fourier normalization
and symmetry argument. Weiss (*Phys. Rev. D* **24** (1981) 475, metadata)
and Lüscher (1983, abstract) are historical source leads, not independent
checks of this calculation. No novelty or full field-theory gap is claimed.

## 1. Frequencies in a constant abelian background

Let $a_i=\alpha_iT^3$, $i=1,2,3$, with $\vec\alpha\in\mathbb R^3$, and
write $a$ for $\vec\alpha$ when no confusion arises. Decompose the
adjoint fluctuation $\tilde A_i=\tilde A_i^3T^3+\tilde A_i^+T^++\tilde A_i^-T^-$.
The covariant derivative $D_j=\partial_j+[a_j,\cdot]$ acts on the neutral
component as $\partial_j$ and on the charged components as
$\partial_j\pm i\alpha_j$, so on the Fourier mode $e^{ik\cdot x}$,
$k\in(2\pi/L)\mathbb Z^3$, the charged components have covariant momentum
$k\pm a$. The quadratic form $\frac1{2g^2}\int|D_i\tilde A_j-D_j\tilde A_i|^2$
is, for a constant abelian background, the free transverse form with $k$
replaced by $k\pm a$ on the charged components, so after the usual
transverse gauge choice the frequencies are
$$\hbar\omega^{(0)}_k=\hbar c|k|\quad(\text{neutral, two polarizations}),$$
$$\hbar\omega^{(\pm)}_k=\hbar c|k\pm a|\quad(\text{charged, two polarizations each}),$$
away from shifted zero frequencies. At $k=0$ and $a\ne0$, the
background-covariant transverse condition $a\cdot\tilde A^{\pm}=0$
leaves two charged spatial polarizations; the neutral components are
the valley directions themselves: with $a=\alpha_1T^3$ along $x_1$ only, these are the
charged parts of $\tilde A_2,\tilde A_3$, four real oscillators of angular frequency $c|a|$, while the charged parts of $\tilde A_1$ are gauge
directions removed by Gauss's law. Enhanced zero modes at $a=0$ or
shifted momenta require their own treatment; this local oscillator count
is not a uniform projection across them.

**The $k=0$ term is C133.** The SU(2) matrix model of C133 with
$\vec x_1=\lambda\hat n$, $\vec x_2=\vec x_3=0$ has potential
$\tfrac12g^2(|\vec x_1\times\vec x_2|^2+|\vec x_1\times\vec x_3|^2+\cdots)$,
whose transverse Hessian at that point gives the components of
$\vec x_2,\vec x_3$ orthogonal to $\hat n$, four oscillators of
frequency $g|\lambda|/\sqrt m$; in the field-theory variables of
[G07](low-dimensional-mass-gap.md) Proposition 7 ($m=\hbar L^3/(g^2c)$, $g_B^2=\hbar cL^3/g^2$) this frequency is $c|a|$. The zero-point energy $4\cdot\tfrac12\hbar c|a|=2\hbar c|a|$ is the confining term of
G07 Theorem 6(1) and the floor of G08 Theorem 2 along the valley.

## 2. Poisson summation

The zero-point energy of the fluctuations relative to $a=0$, summing two
polarizations and both charges, is
$$U(a)=\frac{\hbar c}2\sum_{k\in(2\pi/L)\mathbb Z^3}\sum_{\rm pol=1,2}\big(|k+a|+|k-a|-2|k|\big) =\hbar c\sum_{k\in(2\pi/L)\mathbb Z^3}\big(|k+a|+|k-a|-2|k|\big),$$ where the $k=0$ term is $2\hbar c|a|$ and the neutral modes cancel.
The raw summands are nonnegative and of order $|a|^2/|k|$; their
unregularized sum diverges. Periodicity of a regulated sum alone does
not justify exchanging this sum and subtraction. We use the specific
Fourier finite-part prescription that discards the $m=0$ term below.
It restores periodicity by momentum reindexing and fixes the displayed
one-loop potential; a different prescription needs its own matching.
For $f(k)=|k|$ the distributional
Fourier transform is $\hat f(x)=\int|k|e^{-ik\cdot x}d^3k=-8\pi/|x|^4$ for
$x\ne0$ (the formula $\widehat{|k|^\alpha}=2^{\alpha+3}\pi^{3/2}\frac{\Gamma((3+\alpha)/2)}{\Gamma(-\alpha/2)}|x|^{-3-\alpha}$
at $\alpha=1$, with $\Gamma(-\tfrac12)=-2\sqrt\pi$), and
$$\sum_{k\in(2\pi/L)\mathbb Z^3}f(k+a)=\Big(\frac L{2\pi}\Big)^3\sum_{m\in\mathbb Z^3}\hat f(mL)\,e^{im\cdot La}$$
with the $m=0$ symbol a prescription-dependent subtraction, not a separately
evaluable distributional Fourier value. Hence
$$U(a)=\hbar c\Big(\frac L{2\pi}\Big)^3\sum_{m\ne0}\Big(-\frac{8\pi}{L^4|m|^4}\Big)\big(e^{im\cdot La}+e^{-im\cdot La}-2\big) =\frac{2\hbar c}{\pi^2L}\sum_{m\ne0}\frac{1-\cos(m\cdot La)}{|m|^4}=\frac{2\hbar c}{\pi^2L}\Phi(La).$$
Matching a lattice dispersion to this continuum one-loop expression
requires a separate cutoff estimate. No uniform relative
$O(a_{\rm lat}^2/L^2)$ error follows merely from the nonzero Fourier
indices.

Properties of $\Phi$: it is nonnegative, periodic with period $2\pi$ in
each component, invariant under the cubic group, bounded by
$2\sum'|m|^{-4}$, and zero exactly on $2\pi\mathbb Z^3$.

## 3. Expansion at the origin and the sign of the correction

$\Phi$ is not smooth at $0$. Its Laplacian is the periodic Green's
function $G(b)=\sum'_me^{im\cdot b}|m|^{-2}$, which has the Coulomb
singularity $2\pi^2/|b|$ at the origin (from $\int d^3m\,e^{im\cdot b}|m|^{-2}$)
and a finite remainder: $G(b)=2\pi^2/|b|+C_M+O(|b|^2)$, where $C_M$ is the
constant term of the periodic Coulomb Green's function of the cubic
lattice, the analytically continued Epstein sum $\sum'_m|m|^{-2}$.
Since $\Delta(\pi^2|b|)=2\pi^2/|b|$, the function $\Phi-\pi^2|b|$ has
Laplacian $C_M+O(|b|^2)$ near $0$, and the only quadratic form with cubic
symmetry and Laplacian $C_M$ is $\tfrac16C_M|b|^2$; so
$$\Phi(b)=\pi^2|b|+\tfrac16C_M|b|^2+O(|b|^3),\qquad
U(a)=2\hbar c|a|+\frac{C_M}{3\pi^2}\,\hbar cL|a|^2+O(\hbar cL^2|a|^3).$$ The linear term $2\hbar c|a|$ is the $k=0$ contribution of Section 1, so the nonzero modes contribute $$U_\perp(a)=U(a)-2\hbar c|a|=\frac{C_M}{3\pi^2}\hbar cL|a|^2+O(\hbar cL^2|a|^3),$$
with $C_M<0$ for the cubic lattice (lattice-sum tables; the sign is not
re-derived here and affects only the direction of a subleading
correction). In the rescaled variables $a=g^{2/3}\xi/L$ this is
$\frac{C_M}{3\pi^2}g^{4/3}|\xi|^2\,\hbar c/L$, of relative order $g^{2/3}$ to the zero-mode Hamiltonian $g^{2/3}h_3\,\hbar c/L$: the size that (H3) of the
formal local power counting suggests for the Feshbach reduction. The
coefficient is identified for this one-loop prescription, not for the
full compressed-operator gap hypothesis (H3).

## 3a. General constant backgrounds at quadratic order

The following extension is conditional: suppose a specified gauge-fixed
nonzero-mode determinant, including its longitudinal and ghost contributions,
defines a smooth even gauge-invariant one-loop function near the trivial
background and is matched to the same Fourier prescription as the abelian
calculation. An unfixed Hessian at a general noncommuting off-shell
background does not automatically have these properties. Under that
assumption its quadratic term is constrained by symmetry. It is
invariant under the constant gauge transformations, which rotate the
three colour vectors $\vec a_i$ simultaneously, under the cubic group
acting on the spatial index, and under $a\to-a$. The quadratic
invariants of $(\vec a_1,\vec a_2,\vec a_3)$ under $SO(3)_{\rm colour}$
are the bilinears $\vec a_i\cdot\vec a_j$, and the only cubic-invariant
symmetric form in the spatial indices is $\delta_{ij}$, so
$$U_\perp(a)=c\,\hbar cL\sum_{i=1}^3|\vec a_i|^2+O(\hbar cL^2|a|^3),$$
with a single pure number $c$, which the abelian valley
($\vec a_i=\alpha_i\hat e_3$, $\sum_i|\vec a_i|^2=|\alpha|^2$) determines:
$c=C_M/(3\pi^2)$. The Landau-level structure of non-commuting
backgrounds cannot change this quadratic invariant within the same
smooth one-loop prescription. The remainder is at least cubic in this
local estimate. This identifies a candidate coefficient for (H3);
symmetry does not establish a cutoff-uniform expansion, a global
relative bound or the gap of the compressed operator.

## 3b. The abelian theory in the same expansion

For compact $U(1)$ the constant modes commute, the quartic potential
vanishes, and the photons are neutral, so the one-loop potential of the
holonomy is identically zero: the constant-mode Hamiltonian is the free
Laplacian on the torus of holonomies, $H_0=\frac{e^2c}{2\hbar L^3}|p|^2$
with $a$ periodic of period $2\pi/L$, spectrum $e^2\hbar c|n|^2/(2L)$,
$n\in\mathbb Z^3$, gap $e^2\hbar c/(2L)$. The abelian small-volume gap is
linear in $e^2$, not $e^{2/3}$, because there is no commutator to confine
the holonomy and no charged mode to give it a potential; with $e$ fixed
by the absence of running, the $1/L$ decay is uncompensated and the
infinite-volume theory is gapless, in agreement with the Coulomb phase
of Guth and Fröhlich--Spencer. In the nonabelian matrix model, the $g^{2/3}$ scale comes from the
kinetic/quartic commutator balance. Running of the field-theory coupling
requires a general-background renormalization and matching calculation;
it cannot be read from the commuting-valley function $U$ alone.

## 4. Saturation and central holonomies

The full one-loop potential satisfies
$0\le U\le2\hbar c\max\Phi/(\pi^2L)=O(\hbar c/L)$, and its minima
are at $La\in2\pi\mathbb Z^3$. For $SU(2)$ with adjoint charges
$\pm1$, $La=2\pi e_i$ gives fundamental holonomy
$\exp(2\pi iT^3)=-1$. With strictly periodic gauge transformations these
are distinct central holonomy configurations. Strictly periodic $SU(2)$
gauge transformations identify covering shifts by $4\pi/L$ (and Weyl
reflection), so the infinitely many covering minima represent $2^3$
central holonomy triples. If transformations
periodic only up to the centre are instead gauged, the identification
and allowed sectors change. A configuration is not itself a quantum state.

When centre transformations are global symmetries, their characters on
three torus cycles label electric-flux sectors: $\mathbb Z_N^3$ gives
$8$ labels for $SU(2)$ and $27$ for $SU(3)$. The latter has three central
holonomies per direction. These labels and the one-loop barrier scale
$O(\hbar c/L)$ determine neither spectral splittings nor spectral
weights. Tunnelling and electric-flux interpretations require the
corresponding Hamiltonian, boundary conventions and estimates; they
are not derived by counting minima.

In the isolated matrix model, balancing kinetic and quartic terms gives
$La\sim g^{2/3}$ and the energy scale $g^{2/3}\hbar c/L$. Its linear
valley term is the local limit of $U$, whereas $U$ itself saturates and
is periodic. Crucially, $U_\perp=U-2\hbar c|a|$ is **not** bounded or
periodic on the covering space: the subtracted linear term grows.
The boundedness of $U$ therefore cannot establish a global perturbation
bound for $U_\perp$ relative to the confining matrix operator. Linear confinement may control
$|a|$ and allow some form bound; the small relative bound needed for a
gap comparison has not been supplied. Nor does
a local quadratic estimate control arbitrarily large $|\xi|$ after
$a=g^{2/3}\xi/L$.

Localization near one minimum and an expansion of the full field-theory
gap require the Feshbach hypotheses and a global treatment of the
holonomy domain. The informal comparison $g(L)^{2/3}\sim1$ marks the
loss of a small parameter; it proves no delocalization, sector
coalescence or crossover at a specified value of $z=\Delta L/(\hbar c)$.

## 5. Consequence for STATE

The explicit one-loop input is a periodic bounded $U$ with central
minima and a local correction
$U_\perp=(C_M/(3\pi^2))\hbar cL|a|^2+O(\hbar cL^2|a|^3)$.
The symmetry argument identifies its quadratic form under the stated
smooth-prescription assumption. Global (H3), nonzero-mode comparison,
$SU(3)$ matrix control, cutoff removal and physical spectral transport
remain separate. The abelian zero-mode benchmark has no such one-loop
valley potential; that contrast alone proves no nonabelian continuum gap.
