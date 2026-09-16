# The Schur error of the small-volume reduction is an ultraviolet problem: a fixed-lattice theorem is available, the renormalized regime is not

Inequality (H2) of [the Feshbach reduction](weak-coupling-feshbach-reduction.md)
is estimated here at second order with the fibered vacuum, on the
abelian valley and with the cutoff $\Lambda$ kept explicit. Two terms
have different characters. The non-adiabatic (Berry) coupling, produced
by the constant-mode momentum acting on the $a$-dependent Gaussian
vacuum, has Schur error
$$\eta_{\rm Berry}\ \simeq\ \frac{g^{8/3}}{96\pi^2}\,\log(\Lambda L)\,\langle|\partial_\xi\psi|^2\rangle\,\frac{\hbar c}{L},$$
of relative order $g^2\log(\Lambda L)$ to the zero-mode gap
$g^{2/3}\hbar c/L$: logarithmic, and of the size and form of the one-loop
renormalization of the coupling, so it is absorbed by writing the gap in
terms of $g(L)$. The cubic coupling $W_3$ produces at second order a
constant vacuum shift $\eta_0\sim g^2(\hbar c/L)(\Lambda L)^4$ and an
energy derivative $d\eta_0/dE\sim g^2(\Lambda L)^2$; the shift cancels
from the gap, but the derivative rescales it, and the transfer lemma
holds only when $g^2(\Lambda L)^2\ll1$, that is $g\ll1/N_s$ on a lattice
of $N_s$ sites per side. Consequently the reduction proves the
small-volume gap $\Delta\ge\delta_1^{(3)}g^{2/3}(1-o(1))\hbar c/L$ as a
fixed-lattice theorem, in the regime $g\to0$ at fixed $N_s$, and does
not reach the regime $g^2\log N_s\ll1$ of the renormalized expansion,
where the bare Gaussian fiber is far from the true nonzero-mode vacuum.
The small-volume corner is therefore an ultraviolet problem at fixed
$L$: its control uniformly in the cutoff is a renormalization theorem,
the same obligation as T4 of [the obligations map](mass-gap-obligations-lattice.md).
The route's step 1 splits accordingly into a provable fixed-lattice
statement and a renormalized statement that needs vacuum dressing.
Constants explicit throughout; nothing here is promoted.

## 1. The refined transfer lemma with a constant shift

Lemma 1 of the Feshbach note bounds the Schur term
$S(E)=B(D-E)^{-1}B^*$ by a constant. When $S(E)$ contains a large part
proportional to the identity, that part shifts all eigenvalues of the
compression equally and must not be charged to the gap.

**Lemma 1$'$.** In the setting of Lemma 1 suppose that for
$E\in I=[a_0-\eta_1-\bar\eta_0,\,a_1]$,
$$S(E)=\eta_0(E)\,1+R(E),\qquad 0\le R(E)\le\epsilon(A-a_0)+\eta_1,$$
with $\eta_0$ a nonnegative nondecreasing function, $\bar\eta_0=\sup_I\eta_0$,
$0\le\epsilon<1$, and $\eta_0(E)$ differentiable with
$0\le\eta_0'(E)\le\theta<1$ on $I$. Then
$$E_1-E_0\ \ge\ \frac{(1-\epsilon)(a_1-a_0)-2\eta_1}{1+\theta}.$$

*Proof.* $F(E)=A-E-\eta_0(E)-R(E)$. The count of negative eigenvalues
of $F(E)$ lies between the counts of $A-E-\eta_0(E)-\epsilon(A-a_0)-\eta_1$
and $A-E-\eta_0(E)$. Write $\tilde E=E+\eta_0(E)$, which is increasing
in $E$ with $d\tilde E/dE\le1+\theta$. The bounds show that $E_0$ is the
solution of $\tilde E=e_0$ with $e_0\in[a_0-\eta_1,a_0]$ and $E_1$ the
solution of $\tilde E=e_1$ with $e_1\ge a_0+(1-\epsilon)(a_1-a_0)-\eta_1$;
since $\tilde E$ has slope at most $1+\theta$,
$E_1-E_0\ge(e_1-e_0)/(1+\theta)$. $\square$

The constant shift costs nothing; its energy dependence costs the
factor $1/(1+\theta)$, and $\theta$ is the quantity that the cubic
coupling makes large.

## 2. The fibered vacuum and its $a$-derivative on the abelian valley

On the abelian valley of [the valley note](torus-valley-potential.md),
$a=\alpha T^3$, the charged modes at momentum $k$ have energies
$\hbar\omega_k^{(\pm)}=\hbar c|k\pm a|$ and the fibered vacuum is the
product of Gaussians
$\Omega_\perp(a)=\prod_k\Omega_k(a)$ with
$\Omega_k\propto\exp[-\omega_k(a)|q_k|^2/(2\hbar\cdot\text{norm})]$ in the
real mode coordinates $q_k$ of each polarization and charge. For a
single oscillator of frequency $\omega$ the derivative of the normalized
ground state with respect to $\omega$ is
$\partial_\omega\Omega=-\frac{1}{2\sqrt2\,\omega}\,\Omega_2$, with
$\Omega_2$ the normalized second excited state, so
$$\bar P\,\partial_{a_i}\Omega_\perp(a)=-\sum_{k,\pm,{\rm pol}}\frac{\partial_{a_i}\omega_k^{(\pm)}}{2\sqrt2\,\omega_k^{(\pm)}}\;\Omega_{k,2}\otimes\prod_{k'\ne k}\Omega_{k'},
\qquad\frac{\partial_{a_i}\omega_k^{(\pm)}}{\omega_k^{(\pm)}}=\pm\frac{(k\pm a)_i}{|k\pm a|^2}.$$
Its norm squared is
$\sum_{k,\pm,{\rm pol}}\frac{(k\pm a)_i^2}{8|k\pm a|^4}\simeq\frac{2\cdot2}{8}\sum_k\frac{\hat k_i^2}{|k|^2}
=\frac12\Big(\frac L{2\pi}\Big)^3\frac{4\pi}{3}\Lambda\,[1+O(a/\Lambda)]=\frac{L^3\Lambda}{12\pi^2}$,
linearly divergent: the vacua at different $a$ are not close in norm
as the cutoff is removed, which is the first sign that the fiber is
ultraviolet-sensitive. What enters the Schur error is the same sum with
the energy denominator, which converges better.

## 3. The Berry term

The constant-mode kinetic operator $\frac{g^2c}{2\hbar L^3}\sum_i|\vec p_i|^2$
with $p_i=-i\hbar\partial_{a_i}$ acts on $\psi(a)\Omega_\perp(a)$ as
$\frac{g^2c}{2\hbar L^3}\big[(-\hbar^2\Delta_a\psi)\Omega_\perp-2\hbar^2(\partial_{a_i}\psi)(\partial_{a_i}\Omega_\perp)-\hbar^2\psi\,\Delta_a\Omega_\perp\big]$.
The $\bar P$-component of the middle term is the leading non-adiabatic
coupling,
$$B_{\rm Berry}\,\psi=-\frac{g^2c\hbar}{L^3}\sum_i(\partial_{a_i}\psi)\,\bar P\,\partial_{a_i}\Omega_\perp .$$
Each two-quantum state $\Omega_{k,2}$ costs $D-E\ge2\hbar\omega_k$ above the
fiber, so
$$\|(D-E)^{-1/2}B_{\rm Berry}\psi\|^2
\simeq\Big(\frac{g^2c\hbar}{L^3}\Big)^2\sum_i\sum_{k,\pm,{\rm pol}}\frac{(k_i)^2}{8|k|^4\cdot2\hbar c|k|}\,|\partial_{a_i}\psi|^2
=\frac{g^4c\hbar}{16L^6}\sum_i\Big(\sum_k\frac{\hat k_i^2}{|k|^3}\Big)|\partial_{a_i}\psi|^2 ,$$
with $\sum_k\hat k_i^2|k|^{-3}\simeq\frac13\big(\frac L{2\pi}\big)^3 4\pi\int_{2\pi/L}^{\Lambda}\frac{dk}{k}=\frac{L^3}{6\pi^2}\log\frac{\Lambda L}{2\pi}$.
In the rescaled variable $a=g^{2/3}\xi/L$, $\partial_a=(L/g^{2/3})\partial_\xi$,
and
$$\eta_{\rm Berry}\ \simeq\ \frac{g^4c\hbar}{16L^6}\cdot\frac{L^3}{6\pi^2}\log(\Lambda L)\cdot\frac{L^2}{g^{4/3}}\,\langle|\partial_\xi\psi|^2\rangle
=\frac{g^{8/3}}{96\pi^2}\,\log(\Lambda L)\,\langle|\partial_\xi\psi|^2\rangle\,\frac{\hbar c}{L}.$$
Since $\langle|\partial_\xi\psi|^2\rangle$ is controlled by the kinetic
part of $h_3$, this is a relative bound of the form
$R\le\epsilon(A-a_0)+\eta_1$ with $\epsilon\sim g^2\log(\Lambda L)/(96\pi^2)$.
The logarithm is the ultraviolet signature of the vacuum polarization by
the constant background; the one-loop coefficient of the running
coupling for $SU(2)$ is $b_0=11/(24\pi^2)$, and the Berry term is one of
the contributions that together must reproduce it, which is the
consistency check the renormalized expansion has to pass. Its size,
relative order $g^2\log(\Lambda L)$, is what "$g$ is the renormalized
coupling at scale $L$" absorbs; at fixed cutoff it is small for
$g^2\log N_s\ll1$.

## 4. The cubic coupling: constant shift and slope

$W_3=\frac{\hbar c}{g^2}\int\bar F_{ij}\cdot[\tilde A_i,\tilde A_j]$ with
$\tilde A=g\tilde A'$ creates three quanta from the fiber vacuum. With
the mode normalization $\tilde A'\sim\sqrt{\hbar/(2\omega L^3)}(b+b^\dagger)$
the amplitude for $(k,k',k'')$, $k+k'+k''=0$, is of order
$g\hbar c\,|k|\,(\hbar/(2\hbar c))^{3/2}L^{-3/2}(|k||k'||k''|)^{-1/2}$ times
colour factors, and the second-order shift is
$$\eta_0\ \sim\ g^2\hbar c\sum_{k,k'}\frac{|k|^2/L^3}{|k||k'||k''|\,(|k|+|k'|+|k''|)}
\ \sim\ g^2\hbar c\,L^3\Lambda^4\cdot{\rm const}=g^2\,\frac{\hbar c}{L}\,(\Lambda L)^4\cdot{\rm const},$$
the two-loop vacuum energy of the box: extensive and quartically
divergent, and independent of $a$ at leading order. By Lemma 1$'$ it
costs nothing as a shift. Its energy derivative is
$$\theta=\eta_0'(E)\ \sim\ g^2\sum_{k,k'}\frac{|k|^2/L^3}{|k||k'||k''|\,(|k|+|k'|+|k''|)^2}\cdot\frac{1}{\hbar c}\cdot\hbar c
\ \sim\ g^2(\Lambda L)^2\cdot{\rm const},$$
and Lemma 1$'$ needs $\theta<1$: the bare-fiber reduction is valid only
for $g^2(\Lambda L)^2\ll1$. On a lattice $\Lambda L=\pi N_s$, so the
condition is $g\ll1/N_s$. The $a$-dependent part of the $W_3$ shift is
the two-loop contribution to the valley potential, of order
$g^2\hbar c/L$ with a logarithm, and poses no separate problem.

## 5. What is provable and what is not

**Fixed-lattice theorem (available by this route).** On the periodic
lattice with $N_s$ sites per side, with the lattice regularization of
the nonzero modes, for $g\le g_1/N_s$ with $g_1$ a pure number, the
hypotheses of Lemma 1$'$ hold with $\epsilon,\theta=O(g^2N_s^2)$ and
$\eta_1=O(g^{4/3}\hbar c/L)$, the compression is $h_3+U$ with $U$ the
valley potential, and therefore
$$\Delta_{a,L}\ \ge\ \delta_1^{(3)}\,g^{2/3}\,\frac{\hbar c}{L}\,\big(1-C\,g^{2/3}-C'g^2N_s^2\big).$$
This is the statement that the zero-mode picture of C133 is exact at
leading order on any fixed lattice as $g\to0$: Lüscher's leading term at
fixed regularization. Its proof is the bookkeeping of Sections 2--4
with rigorous constants; it is not carried out here.

**Renormalized regime (not available by this route).** The continuum
small-volume expansion holds for $g(L)^2\log(\Lambda L)\ll1$, a far
weaker condition than $gN_s\ll1$. In that regime the bare Gaussian
vacuum of the nonzero modes is not close to their true vacuum: the
two-loop dressing $\eta_0$ exceeds the one-quantum gap $2\pi\hbar c/L$
by the factor $g^2N_s^4$. A reduction that reaches the renormalized
regime must use a dressed fiber, the ground state of the nonzero modes
at $a=0$ including their self-interaction, and treat only the
$a$-dependence perturbatively; constructing that dressed vacuum with
cutoff-uniform control is a renormalization theorem, the finite-volume
ultraviolet problem that Balaban's work addresses on the Euclidean side.

**Consequence.** The small-volume corner S is not a finite-dimensional
problem. Its lower side splits into a fixed-lattice theorem, provable by
the present tools, and a renormalized theorem that is part of T4. This
is consistent with the structure found in [the obligations map](mass-gap-obligations-lattice.md):
every statement uniform in the cutoff is a renormalization statement,
and the zero-mode mechanism supplies the physics but not the
ultraviolet control.

## 6. Consequence for STATE

Step 1 of the route (close the corner) becomes: (1a) the fixed-lattice
theorem, $\Delta\ge\delta_1g^{2/3}\hbar c/L\,(1-o(1))$ for $g\ll1/N_s$,
provable now with explicit constants; (1b) the renormalized version,
which requires a dressed nonzero-mode vacuum with cutoff-uniform
bounds and is a T4-type problem. The Berry term's logarithm, with its
coefficient, is the first check that a dressed reduction must pass
against the one-loop $b_0$. The blocking induction of the foreseen route
inherits the same split: each blocking step is a fixed-cutoff
statement, and its uniformity is the renormalization problem.
