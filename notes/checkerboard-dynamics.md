# One action scale, two rules for composing paths

The same inverse-time parameter can generate a classical telegraph process or
a unitary Dirac evolution. The distinction lies in the rule for composing
path weights. We give an exactly normalized checkerboard step, its strong
wavepacket limit, and a measurement test that separates its corner amplitude
from a classical reversal probability. This completes A09b's mathematical
comparison and identifies the remaining physical selection question.

## 1. Objects and physical premises

Fix a mass $m>0$, propagation speed $c>0$, and action parameter $K>0$. Set
$\omega=mc^2/K$, with units of inverse time. A time step $\varepsilon>0$
has spatial length $c\varepsilon$. Components labelled $+$ and $-$ move right
and left. The classical comparison uses the same speed as a model parameter;
identifying it with the physical speed of light is an additional specialization.

Use Pauli matrices

$$
\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad (S_\varepsilon f)_\pm(x)=f_\pm(x\mp c\varepsilon).
$$

Classical states are nonnegative two-component probability densities or
measures, with total mass one. Coherent states belong to
$\mathcal H=L^2(\mathbb R;\mathbb C^2)$, with norm one and Born probabilities.
The common translation space makes a strong refinement limit well-defined.
At each fixed mesh the same formulas also define a walk on
$\ell^2(c\varepsilon\mathbb Z;\mathbb C^2)$.

C035–C036 supply a candidate positive classical plateau within a specified
composition/preparation class. Here $K$ is supplied, and equating it to that
plateau is a comparison hypothesis. Complex linear superposition, the squared
norm measurement rule, and the chosen mass-mixing generator specify the
coherent model. The calculation locates their use rather than deriving them
from classical composition.

## 2. Classical transitions and coherent corners

The classical step is $S_\varepsilon P_\varepsilon$, where

$$
P_\varepsilon=(1-\lambda\varepsilon)I+
\lambda\varepsilon\sigma_x,\qquad 0\le\lambda\varepsilon\le1.
$$

Its entries are probabilities and its columns sum to one. On smooth densities
its first-order generator is
$A_\lambda=-c\sigma_z\partial_x+\lambda(\sigma_x-I)$.
Thus the continuum component equations describe the classical telegraph
process with flip rate $\lambda$. Their sum satisfies
$\rho_{tt}+2\lambda\rho_t=c^2\rho_{xx}$.

The coherent step instead is

$$
C_\varepsilon=\frac{I-i\omega\varepsilon\sigma_x}
 {\sqrt{1+\omega^2\varepsilon^2}},\qquad
U_\varepsilon=S_\varepsilon C_\varepsilon.
$$

**Exact normalization.** Since $\sigma_x^2=I$ and $\sigma_x$ is Hermitian,
$C_\varepsilon^\dagger C_\varepsilon=I$. Translation is unitary, so every
$U_\varepsilon$ preserves the wavepacket norm. Expanding a product of $n$
steps gives a path factor
$(1+\omega^2\varepsilon^2)^{-n/2}(-i\omega\varepsilon)^r$ for $r$ flips,
counting possible mixing before the first translation.

The fixed-first-step convention of Skopenkov–Ustinov, Definition 2, instead
has $n-1$ mixing opportunities and an initial overall phase $i$.
Its source components $(a_1,a_2)$ obey Proposition 5. The explicit change
of basis

$$
\psi=W\begin{pmatrix}a_1\\a_2\end{pmatrix},\qquad
W=\begin{pmatrix}0&1\\-i&0\end{pmatrix}
$$

turns that recurrence into $U_\varepsilon$ in natural units, after replacing
the source's $m\varepsilon$ by $\omega\varepsilon$ and its spatial step by
$c\varepsilon$. Indeed $W$ is unitary, swaps the two translation directions,
and takes the source coin
$\left(\begin{smallmatrix}1&r\\-r&1\end{smallmatrix}\right)/\sqrt{1+r^2}$
to $(I-ir\sigma_x)/\sqrt{1+r^2}$.
This is an established checkerboard construction in an explicitly matched
basis; [B18](../references/batches/B18.md) records the prior-art audit.

## 3. Strong continuum limit (C039)

For every fixed $T\ge0$ and $\psi\in\mathcal H$,

$$
U_{T/N}^{\,N}\psi\longrightarrow e^{-iTH_D/K}\psi
\quad\hbox{in }\mathcal H,\qquad
H_D=-iKc\sigma_z\partial_x+mc^2\sigma_x.
$$

**Proof.** Use the unitary Fourier transform with phase $e^{-ipx/K}$;
$p$ is momentum. The step multiplier is

$$
M_\varepsilon(p)=e^{-icp\varepsilon\sigma_z/K}
\frac{I-i\omega\varepsilon\sigma_x}{\sqrt{1+\omega^2\varepsilon^2}}
=I-\frac{i\varepsilon}{K}(cp\sigma_z+mc^2\sigma_x)
+O_p(\varepsilon^2).
$$

At fixed $p$, compare $M_\varepsilon$ with
$e^{-i\varepsilon H(p)/K}$, where $H(p)=cp\sigma_z+mc^2\sigma_x$.
Both matrices are unitary. A telescoping sum bounds the $N$-step difference
by $N O_p((T/N)^2)$, which tends to zero. Its norm is also bounded by two
for all $p,N$. Dominated convergence against $|\widehat\psi(p)|^2$ proves
the strong limit. The Hermitian multiplier $H(p)$ defines a self-adjoint
operator with domain $H^1(\mathbb R;\mathbb C^2)$, since

$$
H(p)^2=(c^2p^2+m^2c^4)I.
$$

Consequently the limiting evolution is unitary and each component solves
$\partial_t^2\psi-c^2\partial_x^2\psi+\omega^2\psi=0$ distributionally.
The spectrum has branches $\pm E_p$, where
$E_p=\sqrt{c^2p^2+m^2c^4}$. Their rest separation is $2mc^2$ in energy
units. This is a single-particle branch separation; the vacuum spectral
problem belongs to a field-theory construction.

This proof concerns fixed $L^2$ initial data. The source's light-cone
delta-function warning concerns the singular point-source kernel and its
undefined square. It leaves the wavepacket norm identity above intact.

## 4. Analytic continuation and the nonrelativistic limit

At the differential-equation level, put $\lambda=-i\omega$ and remove the
scalar phase: $f(t)=e^{i\omega t}\psi(t)$. Then
$f_t=A_{-i\omega}f$ gives
$\psi_t=-c\sigma_z\psi_x-i\omega\sigma_x\psi$.
The opposite continuation sign gives the unitarily equivalent opposite mass
sign. At finite mesh the continued stochastic coin is

$$
\widetilde P_\varepsilon=(1+i\omega\varepsilon)I
-i\omega\varepsilon\sigma_x.
$$

Its symmetric eigenvector has squared norm factor one, and its antisymmetric
eigenvector has factor $1+4\omega^2\varepsilon^2$. No scalar phase or common
normalization makes both factors one when $\omega\varepsilon\ne0$.
Our normalized coherent coin has the same generator after phase removal,
but differs at second order. This identifies precisely the continuum sense
of the analytic-continuation correspondence.

For the positive branch, subtract the rest energy before taking $c\to\infty$
at fixed $m,K,p$:

$$
E_p-mc^2=\frac{p^2}{m(\sqrt{1+p^2/(m^2c^2)}+1)}
\longrightarrow\frac{p^2}{2m}.
$$

In the scalar spectral representation of that branch, dominated convergence
of the unit-modulus multipliers gives strong convergence on $L^2(\mathbb R)$
to the free Schrödinger group with action scale $K$. This statement uses
branch selection and rest-phase removal, and takes the mesh limit first.
It is distinct from the source's point-source, large-time triple limit.

For the real process, $\lambda=mc^2/K$ instead gives Kac's diffusion scaling
$c^2/(2\lambda)=K/(2m)$, as in C021: its limit is the heat process.
Equal dimensional coefficients organize the comparison; the path-weight rule
decides which evolution results.

## 5. Observing every corner changes the limit (C040)

Perform an ideal projective direction measurement after each coherent step,
starting from a wavepacket with definite direction. Given the previous
direction, the next reversal has probability

$$
q_\varepsilon=\frac{\omega^2\varepsilon^2}
 {1+\omega^2\varepsilon^2}.
$$

**Proof and limit.** The off-diagonal coin amplitude is
$-i\omega\varepsilon/\sqrt{1+\omega^2\varepsilon^2}$; translations preserve
its component norm. Projection resets direction after every step. Hence the
conditional flip probability is $q_\varepsilon$ at each step, independently
of the preceding spatial profile. For $N=T/\varepsilon$,

$$
\Pr(\hbox{at least one flip})\le Nq_\varepsilon
\le\omega^2T\varepsilon\longrightarrow0.
$$

With probability tending to one the initially selected direction persists for
the whole interval. The observed walk has a ballistic fixed-$\omega$ limit.
The classical telegraph step instead has flip probability
$\lambda\varepsilon$ and a finite mean flip count $\lambda T$.
Thus $\lambda=\omega$ equates two coefficients with inverse-time units,
not their trajectory or measurement laws.

## 6. Next physical test

The classical positive plateau and the coherent action parameter now have an
exact algebraic comparison. The remaining obligation is an operational rule
for coherent composition that identifies their values across preparations.
Inserted observation cuts must be distinguished from actual repeated
measurements: Section 5 gives different limiting laws for these operations.
G01 next tests which velocity modes the plateau controls and whether that
control supplies a spectral lower bound.

## Sources and reproduction

Skopenkov and Ustinov, *Feynman checkers: towards algorithmic quantum theory*.

[Selected arXiv version](https://arxiv.org/abs/2007.12879v2), 28 February 2022:
Definition 2, Propositions 5–6, pp. 12–13; proof p. 31; singular-kernel
discussion p. 19. The [source companion](../docs/batches/B18/checkerboard-recurrence-source-companion.md)
records exact coverage and the older-source page tasks. C039 is a reconstruction
with an elementary wavepacket proof; C040 is a derived protocol consequence.

Run `python3 scripts/checkerboard_checks.py` for algebra, finite paths and
Fourier-mode convergence checks. The general limits rest on the proofs above.
