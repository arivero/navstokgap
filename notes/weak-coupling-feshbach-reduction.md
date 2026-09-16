# The weak-coupling gap in a small box reduces to three inequalities through the Schur complement

A lower bound $\Delta\ge\delta_1^{(3)}g^{2/3}(1-Cg^{2/3})\,\hbar c/L$ for the
torus Hamiltonian with a momentum cutoff follows from a proved
gap-transfer lemma and three inequalities about polynomial operators on
finitely many oscillators. The lemma: if $P$ is an orthogonal projection,
$D=\bar PH\bar P\ge\mu$ on $\operatorname{ran}\bar P$, and the
Schur-complement error $\eta=\sup_{E\le a_1}\|(D-E)^{-1/2}\bar PHP\|^2$
satisfies $a_1-\eta<\mu$, then the two lowest eigenvalues of $H$ obey
$a_0-\eta\le E_0\le a_0$ and $E_1\ge a_1-\eta$, so
$\operatorname{gap}(H)\ge\operatorname{gap}(PHP)-\eta$. Applied with $P$ the
projection onto the ground state of the nonzero momentum modes, the three
inequalities are: (H1) exciting any nonzero mode costs at least
$(2\pi\hbar c/L)(1-Cg^{2/3})$ in the presence of the constant modes and
the couplings; (H2) the coupling between the constant-mode sector and the
excited nonzero-mode sector has Schur error $\eta\le Cg^{4/3}\hbar c/L$,
which requires the projection to follow the constant mode (Section 3a)
and a gauge-invariant cutoff;
(H3) the effective constant-mode Hamiltonian $PHP$, which is C133's
operator plus the nonzero-mode zero-point energy as a function of the
constant modes, has gap $\ge\delta_1^{(3)}g^{2/3}(1-Cg^{2/3})\hbar c/L$. The
scaling analysis of the cubic and quartic couplings shows why each
inequality is expected with the stated powers, and identifies the
smallness parameter as $g^{2/3}$, Lüscher's expansion parameter. The
lemma is proved; the three inequalities are the open content of the
lower side of the small-volume corner. Units: $\hbar=c=1$ in this note,
energies in units of $\hbar c/L$ and $g$ dimensionless, as in
[G07](low-dimensional-mass-gap.md) Proposition 7. Nothing here is promoted.

## 1. The gap-transfer lemma

Let $H$ be self-adjoint, bounded below, with compact resolvent on a
Hilbert space $\mathcal H$, and $P$ an orthogonal projection with
$P\,D(H)\subset D(H)$; write $\bar P=1-P$, $A=PHP|_{\operatorname{ran}P}$,
$D=\bar PH\bar P|_{\operatorname{ran}\bar P}$, $B=PH\bar P$. Let
$a_0\le a_1\le\cdots$ be the eigenvalues of $A$ and $E_0\le E_1\le\cdots$
those of $H$.

**Lemma 1.** Suppose $D\ge\mu$ and, for some $\eta\ge0$,
$\|(D-E)^{-1/2}B^*\|^2\le\eta$ for all $E\le a_1$, with $a_1<\mu$. Then
$$a_0-\eta\le E_0\le a_0,\qquad E_1\ge a_1-\eta,\qquad
E_1-E_0\ \ge\ (a_1-a_0)-\eta .$$

*Proof.* For $E<\mu$, $D-E$ is invertible and the Schur complement of
$H-E$ with respect to the decomposition
$\operatorname{ran}P\oplus\operatorname{ran}\bar P$ is
$F(E)=A-E-B(D-E)^{-1}B^*$ on $\operatorname{ran}P$. The block
factorization
$$H-E=\begin{pmatrix}1&B(D-E)^{-1}\\0&1\end{pmatrix}
\begin{pmatrix}F(E)&0\\0&D-E\end{pmatrix}
\begin{pmatrix}1&0\\(D-E)^{-1}B^*&1\end{pmatrix}$$
is a congruence, so by Sylvester's law of inertia (the number of
negative eigenvalues, finite here because $H$ has compact resolvent and
$E<\mu\le\inf D$) the number of eigenvalues of $H$ below $E$ equals the
number of negative eigenvalues of $F(E)$, since $D-E>0$ contributes
none. The hypothesis gives $0\le B(D-E)^{-1}B^*\le\eta$, hence
$A-E-\eta\le F(E)\le A-E$ and, by min-max, the number of negative
eigenvalues of $F(E)$ lies between $\#\{k:a_k<E\}$ and $\#\{k:a_k<E+\eta\}$.
Taking $E$ slightly above $a_0$ shows $E_0\le a_0$; taking $E=a_0-\eta$
shows no eigenvalue of $H$ lies below $a_0-\eta$; taking $E=a_1-\eta$
shows at most one eigenvalue of $H$ lies below $a_1-\eta$, so
$E_1\ge a_1-\eta$. $\square$

The lemma transfers a gap from the compressed operator $PHP$ to $H$ at
the price $\eta$, which is the size of the coupling between
$\operatorname{ran}P$ and its complement measured against the energy
$D-E$ needed to leave $\operatorname{ran}P$. Everything below is the
choice of $P$ and the estimation of $a_1-a_0$, $\mu$ and $\eta$.

## 2. The cutoff torus Hamiltonian and the projection

On $T^3_L$ in temporal gauge, with $SU(2)$ for definiteness, momentum
cutoff $|k|\le\Lambda$ and the convention of G07 Proposition 7
($S=-\frac1{4g^2}\int F^aF^a$), decompose $A_i(x)=a_i+\tilde A_i(x)$ into
the constant mode and the nonzero modes $\tilde A_i(x)=L^{-3}\sum_{0<|k|\le\Lambda}\hat A_i(k)e^{ik\cdot x}$,
with conjugate momenta $p_i$ and $\tilde\Pi_i$. Then
$$H=H_0+H_\perp+W,$$
$$H_0=\frac{g^2}{2L^3}\sum_i|\vec p_i|^2+\frac{L^3}{2g^2}\sum_{i<j}|\vec a_i\times\vec a_j|^2,\qquad
H_\perp=\sum_{0<|k|\le\Lambda}\Big[\frac{g^2}{2}|\hat\Pi(k)|^2+\frac1{2g^2}|k\times\hat A(k)|^2\Big]$$
(in the normalization where the free part has frequencies $|k|$), and
$W$ collects every term of $\frac1{2g^2}\int|F_{ij}|^2$ that is neither
purely constant-mode nor quadratic in $\tilde A$ at $a=0$:
$$W=W_2+W_3+W_4,\quad
W_2=\frac1{g^2}\int\big(\partial_i\tilde A_j-\partial_j\tilde A_i\big)\cdot\big([a_i,\tilde A_j]-[a_j,\tilde A_i]\big)+\frac1{2g^2}\int\big|[a_i,\tilde A_j]-[a_j,\tilde A_i]\big|^2,$$
$$W_3=\frac1{g^2}\int\bar F_{ij}\cdot[\tilde A_i,\tilde A_j],\qquad
\bar F_{ij}=\partial_i\tilde A_j-\partial_j\tilde A_i+[a_i,\tilde A_j]-[a_j,\tilde A_i]+[a_i,a_j],$$
$$W_4=\frac1{2g^2}\int\big|[\tilde A_i,\tilde A_j]\big|^2 ,$$
where the purely constant part $\frac{L^3}{2g^2}|[a_i,a_j]|^2$ of
$\frac1{2g^2}\int|F|^2$ is in $H_0$ and $W_4$ is quartic in the nonzero modes.
The
Gauss constraint is imposed on states; the constant gauge
transformations act on $a_i$ by the adjoint action and on the nonzero
modes covariantly, and the nonconstant ones are fixed by keeping the
transverse nonzero modes, the standard small-volume gauge choice.

Let $\Omega_\perp$ be the ground state of $H_\perp$, the Gaussian vacuum
of the free transverse modes, with energy $E_\perp=\sum_k|k|$ (a constant
that cancels from gaps) and first excitation energy $\mu_\perp=2\pi/L$.
Set
$$P=1_{\text{const}}\otimes|\Omega_\perp\rangle\langle\Omega_\perp| .$$
$P$ commutes with the constant gauge transformations because
$\Omega_\perp$ is invariant under them, so Lemma 1 can be applied inside
the physical sector. The compression is
$$A=PHP=H_0+\langle\Omega_\perp,W\Omega_\perp\rangle(a)+E_\perp,$$
where $\langle\Omega_\perp,W_2\Omega_\perp\rangle(a)$ is a function of the
constant modes only (the Gaussian expectation of a quadratic form in
$\tilde A$ with $a$-dependent coefficients), $\langle W_3\rangle$ vanishes
(odd in $\tilde A$), and $\langle W_4\rangle$ is a constant. Thus $A$ is
C133's operator plus a potential $U(a)=\langle W_2\rangle(a)$, which is
the leading change of the nonzero-mode zero-point energy with the
constant background.

## 3. The three inequalities and their expected sizes

Rescale $\vec a_i=g^{2/3}L^{-1}\vec\xi_i$ and $\hat A(k)=g\,\hat A'(k)$ so that
$H_0=g^{2/3}L^{-1}h_3(\xi)$ with $h_3$ the unit operator of C133 and
$H_\perp$ is $g$-independent in the primed variables. Then, counting
powers of $g$ at fixed $L$ and at typical values $|\xi|=O(1)$,
$|\hat A'|=O(1)$:

| term | order in units of $1/L$ | role |
| --- | --- | --- |
| $H_0$ | $g^{2/3}$ | the gap to be transferred |
| $H_\perp$ excitations | $\ge2\pi$ | the energy $\mu$ of leaving $\operatorname{ran}P$ |
| $W_2$, linear in $a$ | $g^{2/3}$ | enters $U(a)$ and $B$ |
| $W_2$, quadratic in $a$ | $g^{4/3}$ | enters $U(a)$ |
| $W_3$, term with $\partial\tilde A$ | $g$ | enters $B$ |
| $W_3$, terms with $a$ | $g^{5/3}$, $g^{7/3}$ | enters $B$ |
| $W_4$ | $g^2$ | enters $A$ and $D$ |

With these sizes the three inequalities that Lemma 1 needs are:

> **(H1)** $D=\bar PH\bar P\ \ge\ E_\perp+\frac{2\pi}{L}(1-C_1g^{2/3})$ on
> $\operatorname{ran}\bar P$: any state with an excited nonzero mode costs
> at least one quantum $2\pi/L$ up to the shift produced by $W$ in a
> background $|a|\sim g^{2/3}/L$.

> **(H2)** $\eta=\sup_{E\le a_1}\|(D-E)^{-1/2}\bar PWP\|^2\ \le\ C_2\,g^{4/3}/L$.
> The leading contribution is the $W_2$ term linear in $a$ (order
> $g^{2/3}/L$, creating one or two nonzero quanta) squared and divided
> by $2\pi/L$; the $W_3$ term of order $g/L$ contributes $g^2/L$.

> **(H3)** $\operatorname{gap}(A)=\operatorname{gap}\big(H_0+U(a)\big)\ \ge\ \delta_1^{(3)}g^{2/3}(1-C_3g^{2/3})/L$.
> $U(a)$ is even in $a$ (charge conjugation), its linear term vanishes,
> and its quadratic term is of order $g^{4/3}/L$, a relatively bounded
> perturbation of $h_3$ in the rescaled variables.

Given (H1)--(H3), Lemma 1 with $\mu=E_\perp+\frac{2\pi}{L}(1-C_1g^{2/3})$
and $a_1-\eta<\mu$ (true for small $g$ since $a_1-a_0=O(g^{2/3}/L)$ and
$a_0-E_\perp=O(g^{2/3}/L)$) yields
$$\Delta\ \ge\ \delta_1^{(3)}\,g^{2/3}\,\frac{\hbar c}{L}\,\big(1-Cg^{2/3}\big),$$
restoring $\hbar c$. This is the lower side of the small-volume corner S,
matching the upper side obtained in
[the Polyakov-average note](polyakov-average-gap-bound.md) up to pure
numbers, and it is the leading term of Lüscher's expansion (abstract,
B78) as a two-sided bound.

## 3a. Correction: the projection must follow the constant mode, and the cutoff must be gauge invariant

The counting in the table is right for the sizes of the operators but
(H2) fails for the projection $P$ of Section 2 when the cutoff is a sharp
momentum cutoff. The term of $W_2$ linear in $a$ creates pairs of
nonzero quanta $(k,-k)$ from $\Omega_\perp$ with amplitude of order
$g^{2/3}|\xi|/L$ for every $k$, so
$\|\bar PW_2P\psi\|^2\sim(g^{4/3}/L^2)(\Lambda L)^3|\xi|^2$ and, after
dividing by the pair energy $2|k|$,
$$\eta\ \sim\ \frac{g^{4/3}}{L^2}\sum_{0<|k|\le\Lambda}\frac{|\xi|^2}{2|k|}
\ \sim\ \frac{g^{4/3}}{L}\,(\Lambda L)^2\,|\xi|^2 ,$$
quadratically divergent in the cutoff. This is the second-order energy
shift $-c\,|a|^2\Lambda^2L^3$ of the constant mode: a gauge-variant mass
term, which a sharp momentum cutoff produces and a gauge-invariant
regularization (the lattice, or any cutoff compatible with Gauss's law)
cancels, since no gauge-invariant function of constant modes is
quadratic in $a$. Two changes repair the reduction.

*Fibered projection.* $H_\perp+W_2$ is quadratic in $\tilde A$ at fixed
$a$, so it has, for $|a|$ small against $2\pi/L$, a Gaussian ground state
$\Omega_\perp(a)$ with frequencies $\omega_k(a)$, the spectrum of the
covariant transverse curl in the constant background (for
non-commuting $a_i$ the background carries a constant field strength and
the lowest shifted frequency is the Nielsen--Olesen mode,
$\omega^2=(2\pi/L)^2-c\,|[a,a]|$, still positive when
$g^{4/3}\ll(2\pi)^2$). Take
$$P=\int^\oplus da\;|\Omega_\perp(a)\rangle\langle\Omega_\perp(a)| ,$$
the Born--Oppenheimer projection. Then $W_2$ is absorbed exactly, the
compression is
$$A=PHP=H_0+U(a)+\text{(non-adiabatic terms)},\qquad
U(a)=\tfrac12\sum_k\big[\omega_k(a)-\omega_k(0)\big]+\text{const},$$
and $U(a)$ is the one-loop effective potential of the constant modes on
the torus: even in $a$, with no quadratic term for a gauge-invariant
cutoff, and with a quartic term $\propto|[a,a]|^2\log(\Lambda L)$ that
renormalizes $1/g^2$. In rescaled variables the finite part of $U$ is
$O(g^{4/3}/L)$ and the logarithm is $O(g^{4/3}\cdot g^{2}\log\Lambda L\,/L)$
relative to $H_0$'s $g^{2/3}/L$: (H3) holds with $g$ understood as the
renormalized coupling at the scale $L$, which is Lüscher's statement.
The non-adiabatic terms come from $p_i$ acting on $\Omega_\perp(a)$
(the Berry connection of the fibered vacuum) and are of relative order
$g^{4/3}$.

*Schur error.* With the fibered $P$, $\bar PWP$ contains only $W_3$,
$W_4$ and the non-adiabatic terms. $W_3$ creates three quanta with
amplitude of order $g/L$ per mode triple, and its second-order
contribution is the $a$-dependent part of a two-loop vacuum energy, whose
divergent part is $a$-independent and cancels from the gap; the finite
$a$-dependent part is of order $g^2/L$. (H2) is therefore expected in the
form $\eta\le C_2g^{4/3}(1+g^{2/3}\log\Lambda L)/L$, with a gauge-invariant
cutoff, and the constants $C_i$ grow with $\log(L/a)$ on a lattice: the
reduction holds at fixed cutoff, and the cutoff dependence is exactly the
running of the coupling.

The corrected list is: (H1) as before for $H_\perp(a)$; (H2) for the
fibered Schur error; (H3) for $h_3+U$ with $U$ the finite one-loop torus
potential. Lemma 1 is unchanged.

## 4. What the reduction shows

The smallness parameter is $g^{2/3}$ in every entry of the table, which
is the reason the small-volume expansion is a series in $g^{2/3}$. The
mechanism transferred is the zero-point confinement of C133: $A$ is that
operator plus a small even potential, and the nonzero modes enter only
through the price $\eta$ of leaving their vacuum. The reduction also
shows where the small-volume regime ends: (H1) fails when
$C_1g(L)^{2/3}$ reaches order one, that is when $\Delta_0(L)\sim2\pi/L$,
which is the crossover $z\simeq2$ of Lüscher--Münster in the variable
$z=\Delta L$. Beyond it, leaving the nonzero-mode vacuum is no longer
expensive compared with the constant-mode gap, no projection of the form
$P$ separates scales, and the argument gives nothing, which is the
statement of T2$'$'s difficulty in this language.

## 5. Consequence for STATE

The weak-coupling lower bound is now three inequalities on explicit
polynomial operators, with a proved transfer lemma. The next step on
the lower side is the fibered (H2): the non-adiabatic terms and the
$W_3$ Schur error against the nonzero-mode gap, on a lattice cutoff, with
the C133 ground state as weight; (H1) and (H3) are relatively bounded
perturbation statements, (H3) requiring the finite one-loop torus
potential. Their proof would close the small-volume corner
S from both sides and make the crossover statement the whole remaining
content of T2$'$ at fixed cutoff.
