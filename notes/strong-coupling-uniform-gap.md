# The strong-coupling gap of the Kogut--Susskind Hamiltonian is uniform in the volume

Statement T2 of [the obligations map](mass-gap-obligations-lattice.md)
holds in Hamiltonian form: for every compact connected gauge group $G$
and every lattice size, the Kogut--Susskind Hamiltonian at coupling
$g\ge g_0(G)$ has a non-degenerate ground state and a gap
$$\Delta_{a,L}\ \ge\ \gamma\,\frac{g^2}{2}\,C_2(R_{\min})\,\frac{\hbar c}{a},$$
with $\gamma>0$ independent of the lattice size, and the physical
(gauge-invariant) gap is at least as large. The proof is a hypothesis check
against Yarotsky's Theorem 1 on relatively bounded perturbations of
classical lattice systems (Commun. Math. Phys. 261 (2006) 799, Sections 1
and Theorem 1 read at passage level): the electric term is a classical
Hamiltonian in the Peter--Weyl partition with a product ground state and
unit local gap after normalization, and the magnetic term is a bounded,
translation-invariant, finite-range perturbation whose normalized size is
$\beta(g)=48N^2/[g^4(N^2-1)]$ for $SU(N)$, so the theorem's smallness
condition $\beta\le\beta_*(3,\Lambda_0)$ is the strong-coupling condition
$g^4\ge48N^2/[(N^2-1)\beta_*]$. The same theorem gives the infinite-volume
ground state and exponential clustering at these couplings. The constants
$\beta_*$ and $\gamma$ are existential in Yarotsky's statement, so
$g_0$ is a well-defined but not numerically explicit threshold. The
result does not distinguish abelian from non-abelian groups; that
distinction is T2$'$, and the rest of the problem is the descent of $g_0$
to zero along the scaling curve. No claim is promoted.

## 1. The Hamiltonian in Yarotsky's normalization

Notation as in [the obligations map](mass-gap-obligations-lattice.md) §1:
periodic cubic lattice $\Lambda=(\mathbb Z/N_s\mathbb Z)^3$, links
$\mathcal E$, plaquettes $\mathcal P$, $\mathcal H=L^2(G^{\mathcal E})$,
and
$$H=\frac{\hbar c}{a}\Big[\frac{g^2}{2}\sum_{\ell}(-\Delta_\ell)
+\frac{2}{g^2}\sum_{p}\big(N-\operatorname{Re}\operatorname{tr}U_p\big)\Big].$$
Let $C_2\equiv C_2(R_{\min})$ be the smallest nonzero Casimir eigenvalue
of $-\Delta$ on $L^2(G)$; for $SU(N)$ with
$\operatorname{tr}T^aT^b=\tfrac12\delta^{ab}$, $C_2=(N^2-1)/(2N)$. Divide
by the unit $\varepsilon_0=(g^2/2)C_2\,\hbar c/a$:
$$\frac{H}{\varepsilon_0}=\sum_{x\in\Lambda}h_x+\sum_{x\in\Lambda}\phi_x,\qquad
h_x=\frac1{C_2}\sum_{i=1}^3(-\Delta_{(x,x+e_i)}),\qquad
\phi_x=\frac{4}{g^4C_2}\sum_{i<j}\big(N-\operatorname{Re}\operatorname{tr}U_{p(x,i,j)}\big),$$
where $p(x,i,j)$ is the plaquette with corner $x$ spanned by $e_i,e_j$.
Every link belongs to exactly one $h_x$ and every plaquette to exactly one
$\phi_x$, so the two sums reproduce $H/\varepsilon_0$.

## 2. Hypothesis check

Yarotsky's setting (Section 1 of the paper): a lattice $\mathbb Z^\nu$,
site spaces $\mathcal H_x$ possibly infinite-dimensional with a preferred
vector $\Omega_x$, translation-invariant interactions of finite range
$\Lambda_0$, a classical part $H_0=\sum_xh_x$ where $h_x$ is a function of
a product partition of unity containing the projection onto $\Omega_x$
and satisfies $h_x\Omega=0$, $h_x\ge1$ on the orthogonal complement of the
product vector, and a perturbation $\sum_x\phi_x$ with each $\phi_x$ a
symmetric form on $\mathcal H_{\Lambda_0+x}$ obeying
$|\phi_x(v,v)|\le\alpha\|h_x^{1/2}v\|^2+\beta\|v\|^2$ with $\alpha<1$.
Theorem 1 there: there are $\alpha_*,\beta_*>0$ depending only on $\nu$
and $\Lambda_0$ such that if $\alpha\le\alpha_*$ and $\beta\le\beta_*$,
then for periodic cubic volumes $H_\Lambda$ has a non-degenerate ground
state with a gap $\gamma>0$ independent of $\Lambda$, the ground states
have a weak$^*$ thermodynamic limit, and that limit has exponentially
decaying correlations.

1. *Lattice and site spaces.* $\nu=3$; $\mathcal H_x=L^2(G)^{\otimes3}$,
   the three links leaving $x$; $\Omega_x$ the constant function. Then
   $\mathcal H_\Lambda=\bigotimes_x\mathcal H_x=L^2(G^{\mathcal E})$ and
   $\Omega_{\Lambda,0}$ is the constant function on $G^{\mathcal E}$.
2. *Partition and classicality.* On each link, Peter--Weyl gives the
   orthogonal partition of unity by isotypic projections $P_R$, $R$
   ranging over irreducible representations, with $P_{\rm triv}$ the
   projection onto constants. $-\Delta_\ell=\sum_RC_2(R)P_R$ is a function
   of this partition, so $h_x$ is a function of the product partition on
   $\mathcal H_x$, and $h_x$ is self-adjoint and unbounded, as allowed.
3. *Local ground state and gap.* $h_x\Omega_x=0$. On the orthogonal
   complement of $\Omega_x$ in $\mathcal H_x$ at least one of the three
   links carries a nontrivial representation, so
   $h_x\ge C_2(R_{\min})/C_2=1$ there: condition (1) of the paper holds
   with the range $\Lambda_0=\{0\}$ for $h_x$, which may be enlarged to the
   common range below.
4. *Perturbation.* $\phi_x$ is multiplication by a continuous function on
   the twelve links of the three plaquettes at $x$, whose sites lie in
   $\Lambda_0+x$ with $\Lambda_0=\{0,1\}^3$; it is symmetric, bounded, and
   $0\le N-\operatorname{Re}\operatorname{tr}U_p\le2N$ gives
   $$|\phi_x(v,v)|\le\beta\|v\|^2,\qquad
   \beta=\frac{4}{g^4C_2}\cdot3\cdot2N=\frac{24N}{g^4C_2}
   =\frac{48N^2}{g^4(N^2-1)}\ \ (SU(N)),$$
   so condition (2) holds with $\alpha=0$ and this $\beta$.
5. *Translation invariance and periodicity.* $h_x$ and $\phi_x$ are
   translates of $h_0$ and $\phi_0$, and the lattice is a periodic cube,
   the case in which the paper states Theorem 1.

**Theorem (T2, Hamiltonian form).** Let $\beta_*=\beta_*(3,\{0,1\}^3)$ and
$\gamma$ be the constants of Yarotsky's Theorem 1 for this range. For
every $g$ with $48N^2/[g^4(N^2-1)]\le\beta_*$, that is
$g\ge g_0(N)=\big(48N^2/[(N^2-1)\beta_*]\big)^{1/4}$, and every $N_s\ge2$:
$H$ has a non-degenerate ground state, and
$$\Delta_{a,L}\ \ge\ \gamma\,\varepsilon_0=\gamma\,\frac{g^2}{2}\,\frac{N^2-1}{2N}\,\frac{\hbar c}{a}.$$
The physical gap obeys $\Delta^{\rm phys}_{a,L}\ge\Delta_{a,L}$ by Theorem 1(3)
of the obligations map. The ground states have a thermodynamic limit
$\omega$ with exponentially decaying correlations of local observables.

*Proof.* Items 1--5 are the hypotheses of Yarotsky's Theorem 1 with
$\alpha=0\le\alpha_*$ and $\beta\le\beta_*$; its conclusions 1--3 are the
statements, after multiplying the normalized gap $\gamma$ by
$\varepsilon_0$. The inheritance by the physical sector is the positivity
argument already written for T1. $\square$

For a general compact connected $G$ the same holds with
$C_2=C_2(R_{\min})$ and the bound $N-\operatorname{Re}\operatorname{tr}U_p\le2\dim$
in place of $2N$; the threshold is $g_0^4=24\dim/(C_2\beta_*)$.

## 3. What the theorem does and does not give

- *Uniformity.* $\gamma$ depends only on $\nu=3$ and $\Lambda_0=\{0,1\}^3$,
  so the bound holds for every lattice size at once. The extensive Kato
  bound of the obligations map §3 is replaced by a local one, which is
  exactly what the cluster structure of the perturbation provides.
- *Large $N$.* $\beta\to48/g^4$ as $N\to\infty$, so $g_0(N)$ is bounded in
  $N$: the strong-coupling gap is uniform in the rank at fixed bare $g$ in
  this convention. In the 't Hooft normalization $\lambda=g^2N$ the
  threshold reads $\lambda\ge g_0^2N$, growing with $N$.
- *Scale.* The gap is measured in $\hbar c/a$ and is proportional to
  $g^2$: a supplied cutoff scale, as the dimensional census of
  [G07](low-dimensional-mass-gap.md) §4 requires at fixed $g$. Nothing
  here survives $a\to0$ at fixed $g$, and T3 asks for the behaviour along
  $g(a)\to0$, outside the theorem's range.
- *Abelian case.* $U(1)$ satisfies every hypothesis with
  $C_2(R_{\min})=1$ (charge one) and $\dim=1$, so it too is gapped uniformly
  in volume at strong coupling. The theorem is blind to the property that
  distinguishes the groups; that property enters only in T2$'$, where the
  abelian gap closes (Guth; Fröhlich--Spencer) and the non-abelian one is
  conjectured to persist.
- *Explicitness.* $\beta_*$ and $\gamma$ exist by the theorem and are not
  given as numbers in its statement. Extracted from the proof
  ([threshold note](strong-coupling-threshold-explicit.md)), the
  time-discretized expansion gives $\beta_*\simeq e^{-465}$ and
  $g_0^2\simeq10^{101}$ for $SU(3)$; the continuous-time expansion of
  [the Kogut--Susskind note](kogut-susskind-strong-coupling-explicit.md)
  gives $g_0^2=388$ rigorously ($79$ in the adjacent-growth class) with
  $\gamma\to4$. The descent problem
  does not depend on that number, only on the structure of the expansion.
- *Relation to the small-volume end.* Yarotsky's expansion is in the
  electric basis, where the ground state at $g=\infty$ is the constant
  function. At weak coupling the ground state concentrates near
  $U_p=1$ and the good variables are the constant modes of
  [G07](low-dimensional-mass-gap.md) §3.3, with gap
  $\delta_1g^{2/3}\hbar c/L$ in the continuum small box. The two
  expansions use different bases and different small parameters
  ($g^{-4}$ and $g^{2/3}$); T2$'$ is the statement that the gap does not
  close between them.

## 4. Consequence for STATE

T2 is closed in Hamiltonian form as a corollary of an established
theorem, with the threshold $g_0(N)=(48N^2/[(N^2-1)\beta_*])^{1/4}$. The
obligations table moves T2 to "established"; the open items are T2$'$,
T3 and T4. The next theorem-sized target on the lattice route is a
weak-coupling counterpart: a variational upper bound and, if possible, a
lower bound on the Kogut--Susskind gap at small $g$ on a lattice whose
side is small against $\hbar c/\Lambda$, using the constant-mode ground
state of C133 as the trial state, to connect the lattice gap
$\Delta_{a,L}$ with the continuum small-volume corner and to locate the
regime where neither expansion applies.
