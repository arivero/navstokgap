# Kogut–Susskind strong coupling: stability, finite-volume bounds and history estimates

The Kogut–Susskind Hamiltonian has a volume-uniform strong-coupling gap by
Yarotsky's established local-perturbation theorem. For $SU(3)$ the theorem
also covers the translation-invariant, gauge-invariant few-link perturbations
and link-local electric deformations specified below. Its constants and the
location of the resulting target region are existential.

At a fixed volume the physical electric-loop gap has an explicit two-sided
min–max estimate. Continuous-time histories give additional conditional
overlap bounds and restricted shape counts. They supply **no explicit
volume-uniform KS threshold**: the old values $g^2=79,388$ and the associated
uniform rates were withdrawn because late roots, general shapes and
normalized true-vacuum correlations were not controlled. The corrections are
incorporated at each estimate below. Wilson-transfer thresholds concern a
different operator and remain in their [own proof](wilson-strong-coupling-explicit.md).

All gaps below are energies, with physical unit $\hbar c/a$. Positivity along
a weak-coupling scaling trajectory, cutoff removal and physical reconstruction
are separate obligations; positivity at every bare coupling is an optional
stronger property of a lattice action.

## Hamiltonian and the local stability theorem

On a periodic cubic spatial lattice $\Lambda=(\mathbb Z/N_s\mathbb Z)^3$,
with links $\mathcal E$ and plaquettes $\mathcal P$, use
$$H=\frac{\hbar c}{a}\left[\frac{g^2}{2}\sum_\ell(-\Delta_\ell)
 +\frac2{g^2}\sum_p(N-\operatorname{Re}\operatorname{tr}U_p)\right].$$
For $SU(N)$, $\operatorname{tr}T^aT^b=\delta^{ab}/2$ and
$C_2(R_{\min})=(N^2-1)/(2N)$. Write $\varepsilon_0=g^2C_2/2$ in
lattice energy units. Each site space $\mathcal H_x=L^2(G)^{\otimes3}$
contains its three outgoing links, with preferred constant vector
$\Omega_x$. The Peter–Weyl isotypic projections give a product partition
of unity, and
$$h_x=C_2^{-1}\sum_{i=1}^3(-\Delta_{(x,x+e_i)})$$
is a function of that partition, vanishes on $\Omega_x$ and is at least
one on its orthogonal complement.

Yarotsky, *CMP* **261** (2006) 799, §1 and Theorem 1 (**passage read**),
applies to these possibly infinite-dimensional site spaces and a
translation-invariant finite-range bounded perturbation. For range
$\Lambda_0$ there are positive $\beta_*(3,\Lambda_0)$ and $\gamma$ such
that a normalized local perturbation norm at most $\beta_*$ leaves a
simple ground state and gap at least $\gamma$, uniformly in periodic
volume. It also gives thermodynamic ground states and clustering for a
fixed consistent interaction. The bounded case uses relative coefficient
$\alpha=0$; no numerical value of $\beta_*$ is supplied by the statement.

Assign each of the three plaquettes $p(x,i,j)$, $i<j$, to $x$. After division
by $\varepsilon_0$, their positive potential has local norm at most
$$\beta(g)=\frac{24N}{g^4C_2}
 =\frac{48N^2}{g^4(N^2-1)}.$$
Its sites lie in $x+\{0,1\}^3$. Thus, for $N_s\ge2$ and
$\beta(g)\le\beta_*(3,\{0,1\}^3)$,
$$\Delta^{\rm phys}_{a,L}\ge\Delta_{a,L}
 \ge\gamma\frac{g^2C_2}{2}\frac{\hbar c}{a}.$$
This is a direct hypothesis check, not a new proof of the borrowed theorem.
For a compact connected group with a specified faithful unitary representation
of dimension $d_R$, the same sufficient estimate is
$g^4\ge24d_R/(C_2\beta_*)$. For the unperturbed elliptic Hamiltonian,
positivity improvement gives a unique positive ground state, and gauge
invariance of that vector follows from uniqueness and normalization
([finite-lattice proof](mass-gap-obligations-lattice.md)). The physical
subspace reduces $H$ and contains its ground state, proving gap inheritance.

The displayed sufficient $g_0$ is bounded as $N\to\infty$ at fixed $g$.
At fixed 't Hooft coupling $\lambda=g^2N$, its condition instead grows with
$N$. Neither fact transports this theorem to $g(a)\to0$.

## Bounded local perturbations and the existential target region

In units $\hbar c/a=1$ let
$$H=H_E'-g^{-2}\sum_pw_p-\sum_jd_j,\qquad
 w_p=\operatorname{tr}U_p+\operatorname{tr}U_p^\dagger,\quad \|w_p\|\le6.$$
Assume all of the following for $SU(3)$:

- $H_E'=\sum_{\ell,R}e'(R)P_R^\ell$ is link-local and translation
  invariant, $e'({\rm triv})=0$, and $e'(R)\ge\varepsilon'$ for every
  nontrivial $R$, where $\varepsilon'=(1-\eta_E)2g^2/3$, $0\le\eta_E<1$.
- Each $d_j$ is bounded, self-adjoint and gauge invariant, on a connected
  set of at most $q$ links. The family is translation covariant and
  $\sum_{j\ni\ell}\|d_j\|\le\eta$ for every link.
- $q\ge1$, $N_s\ge2q+1$, and $\Lambda_q=\{-q,\ldots,q\}^3$.

Let $n_x(j)$ count support links based at $x$ and distribute each term by
$$\delta_x=\sum_j\frac{n_x(j)}{|\operatorname{supp}d_j|}d_j.$$
Then $\sum_x\delta_x=\sum_jd_j$, $\|\delta_x\|\le3\eta$, and its
support lies in $x+\Lambda_q$: connectedness and at most $q$ links give
the stated radius. Dividing by $\varepsilon'$ gives an on-site electric
part with unit gap and local perturbation
$$\phi_x=-\frac1{\varepsilon'g^2}\sum_{i<j}w_{p(x,i,j)}
 -\frac{\delta_x}{\varepsilon'},\qquad
 \|\phi_x\|\le\frac1{1-\eta_E}
 \left(\frac{27}{g^4}+\frac{9\eta}{2g^2}\right).$$
The difference between 54 in the uncentered $SU(3)$ estimate above and 27
here comes from subtracting the magnetic scalar constant; both are sufficient
bounds with their specified ranges.

**Stability theorem.** With $\beta_q^*=\beta_*(3,\Lambda_q)$ and the
corresponding $\gamma_q>0$, the condition
$$\frac{27}{g^4}+\frac{9\eta}{2g^2}\le(1-\eta_E)\beta_q^*,
\quad\text{equivalently}\quad
 \eta\le\frac{2(1-\eta_E)\beta_q^*}{9}g^2-\frac6{g^2}$$
implies a simple gauge-invariant ground state and
$$\Delta^{\rm phys}_{a,L}\ge\Delta_{a,L}
 \ge\gamma_q(1-\eta_E)\frac{2g^2}{3}\frac{\hbar c}{a}.$$
Here $\eta$ is a numerical local norm in lattice energy units. The target
region opens at $g^4\ge27/[(1-\eta_E)\beta_q^*]$.

*Proof.* The preceding grouping verifies Yarotsky's hypotheses. A unique
normalized ground ray transforms under $SU(3)^\Lambda$ by a continuous
one-dimensional character. The Lie algebra is semisimple, so its derivative
vanishes; connectedness makes the character trivial. The ground state is
therefore physical even though general $d_j$ need not preserve positivity.
The reducing physical subspace inherits the lower bound. $\square$

The bound is uniform for a volume-dependent family satisfying the same
hypotheses. A thermodynamic state assertion additionally uses one consistent
infinite-lattice interaction, or the appropriate convergent family. The
borrowed theorem does not automatically cover nontranslation-invariant
perturbations, disconnected supports of unbounded diameter, or an arbitrary
nonlocal diagonal electric energy. Its range dependence is existential;
a $2^{-q}$ law is not part of this theorem.

## Physical electric loops and exact finite-volume bounds

For the unperturbed $SU(3)$ operator write $H=H_E-W+6P/g^2$, with
$P=3N_s^3$ and
$$E(\sigma)=\frac{g^2}{2}\sum_\ell C_2(r_\ell)
 \ge\varepsilon|S(\sigma)|,\quad \varepsilon=2g^2/3,
 \qquad \|W\|\le6P/g^2.$$
Gauss's law excludes a vertex with only one excited incident link.
Nonabelian invariant networks may branch; they need not be unions of flux
loops. Every nonempty finite graph of minimum degree at least two contains
a cycle. For $N_s\ge4$ its length is at least four. A plaquette character
realizes four fundamental links and is orthogonal to the electric vacuum,
so the physical electric gap is exactly $4\varepsilon$. Shorter periodic
lattices need separate winding counts; the unrestricted electric gap is
only $\varepsilon$.

Min–max bounds the shifts of each of the two lowest levels by $\|W\|$:
$$\left(\frac83g^2-\frac{12P}{g^2}\right)\frac{\hbar c}{a}
 \le\Delta^{\rm phys}_{a,L}\le
 \left(\frac83g^2+\frac{12P}{g^2}\right)\frac{\hbar c}{a}.$$
At each fixed volume the ratio to $g^2\hbar c/a$ tends to $8/3$.
The sufficient $g^4\ge9P$ gives lower coefficient $4/3$ but grows with
volume. It cannot establish a uniform threshold.

### The abelian comparison and a finite-volume bound

For $U(1)$ use $H_E=(g^2/2)\sum n_\ell^2$ and magnetic potential
$(2/g^2)\sum(1-\cos\theta_p)$. The same four-edge argument gives
$$\left(2g^2-\frac{4P}{g^2}\right)\frac{\hbar c}{a}
 \le\Delta^{\rm phys}_{a,L}\le
 \left(2g^2+\frac{4P}{g^2}\right)\frac{\hbar c}{a},\qquad N_s\ge4.$$
The local stability theorem also gives a volume-uniform strong-coupling
region for $U(1)$. The weak sides differ: $SU(3)$ has perturbative
$d g^2/d\log a=2b_0g^4+O(g^6)$, $b_0=11/(16\pi^2)$, whereas a pure
continuum photon has no such self-interaction. Guth, *PRD* **21** (1980)
2291, and Fröhlich–Spencer, *CMP* **83** (1982) 411, are the retained
metadata-level sources for the compact-lattice weak-coupling massless phase.
Running alone proves neither controlled arrival at the target region nor
continuum spectral transfer.

## Continuous-time histories and the corrected overlap criterion

This is an additional candidate expansion, not the proof of the stability
theorem. It also allows the more general diagonal physical $H_E'$ commuting
with exact-support projections $P_S$, with $E'(\sigma)\ge\varepsilon'|S|$.
Assume $N_s\ge\max(4,2q+1)$. Center the bounded $d_j$ in the electric
vacuum; scalar subtraction can at most double the quoted local norm $\eta$.
Without centering, remote vacuum insertions need not carry energy damping.

Duhamel's ordered expansion of $e^{-t(H_E'-W-D)}$ inserts plaquettes or
$d_j$ terms. Resolving $P_S$ between them gives histories
$S_0=S_n=\emptyset$ with insertion operators $X_k$, gaps
$x_k=\tau_{k+1}-\tau_k$ and
$$A(\gamma)=\sum_{k=1}^{n-1}|S_k|x_k,\qquad
 |w(\gamma)|\le\prod_k\|X_k\|e^{-\varepsilon'A(\gamma)}.$$
Amplitudes can have either sign. Labels within an exact support are already
summed in the operator norm. A plaquette changes only its four links and
has at most 16 next-support outcomes; a $q$-link insertion has at most $2^q$.
An irreducible physical history has $|S_k|\ge4$ between insertions.

Disjoint link factors and chronological interleavings motivate a hard-core
history gas, but a complete construction must still specify connected
components and insertion-endpoint compatibility. The following overlap
criterion is **conditional on such a factorizing gas and its majorant**.
For an established measure-space gas, the KP theorem used here is
Poghosyan–Ueltschi, [§2, Assumptions 1–2 and Theorem 2.1](https://arxiv.org/pdf/0811.4281)
(passage read), including its finite-volume/time integrability premise.

Set $a(\gamma)=n+\lambda A$, $\delta'=\varepsilon'-\lambda>0$.
The tilted majorant has insertion weights multiplied by $e$. Let
$T_\ell$ be the total excited duration and $r_\ell$ the number of maximal
excitation intervals on link $\ell$. Then
$$\sum_\ell T_\ell=A,\qquad
 \sum_\ell r_\ell\le\max(4,q)n.$$
An interval of length $x'$ in another history can overlap these intervals
under translations of total measure at most $T_\ell+r_\ell x'$.
The multiplicity $r_\ell$ is essential.

Let $Q'$ majorize the sum over **all** connected shapes reaching a test
link, including a sum over marked internal intervals, after integrating
$e^{-\delta'|S_k|x_k}$ on the positive orthant. Its length-marked version
is at most $Q'/(4\delta')$, since
$$\int_0^\infty e^{-\delta'|S|x}dx=\frac1{\delta'|S|},\qquad
 \int_0^\infty xe^{-\delta'|S|x}dx
 \le\frac1{4\delta'}\frac1{\delta'|S|}.$$
Therefore the overlap integral is at most
$$Q'A(\gamma)+\frac{Q'\max(4,q)}{4\delta'}n(\gamma),$$
and sufficient conditional inequalities are
$$Q'\le\lambda,\qquad Q'\le\frac{4\delta'}{\max(4,q)}.$$
For unperturbed plaquette histories this is $Q_\lambda\le\lambda,\delta$,
where explicitly
$$Q_\lambda=\sup_{\ell_0}\sum_{\text{shapes reaching }\ell_0}
 (n-1)h^n\prod_{k=1}^{n-1}(\delta|S_k|)^{-1},\qquad h=6e/g^2.$$
The old $Q_\lambda\le4\delta$ lost the endpoint multiplicity four.
Neither version proves that the actual all-root majorant is small.

## Restricted shape counts and their numerical status

Anchor the **first** insertion at the test link and require every later
insertion to touch the current support. For the unperturbed gas four initial
plaquettes give $F=4h=24e/g^2$. Later choices are at most
$4|S|\cdot16$, whose factor $|S|$ is canceled by the preceding time integral.
For the perturbed gas the same calculation gives
$$F'=24e/g^2+e\eta2^q,\qquad
 u'=\frac{384e/g^2+e\eta2^q}{\delta'},$$
$$B'_\lambda\le F'\sum_{m\ge1}m(u')^m
 =\frac{F'u'}{(1-u')^2}\le4F'u'\quad(u'\le1/2).$$
This is a valid restricted count. It includes repeated insertions. It omits
histories first reaching the test link later and pieces created remotely and
subsequently bridged; hence $B'_\lambda$ does not bound $Q'$.

For general connected insertion graphs, assign consecutive link intervals
to a spanning tree $T$. A surviving energy inequality is
$$\sum_{e\in T}|\tau_{i(e)}-\tau_{j(e)}|\le A(\gamma),\qquad
 e^{-\delta A}\le\prod_{e\in T}e^{-\delta|\tau_i-\tau_j|}.$$
Each insertion has at most eight predecessor/successor link slots. This does
not count the required root, interval marks and time-length multiplicities.
The former $u_{\rm gen}=24u$ also allowed only three child plaquettes per
parent link, excluding the repeated plaquette that creates and annihilates
a loop. Changing that factor to four would give a formal $32u$, still
without a proved marked count. Neither is a certified KP parameter.

For $\eta=\eta_E=0$, write $\lambda=\varepsilon(1-\theta)$,
$\delta=\varepsilon\theta$, $0<\theta<1$. Then
$$u=\frac{576e}{\theta g^4},\qquad
 g^4\ge\frac{1152e}{\theta},\quad
 g^8\ge\frac{82944e^2}{\theta\min(\theta,1-\theta)}$$
are sufficient for the displayed restricted $B_\lambda$ inequalities only.

| $\theta$ | sufficient integer $g^2$ for those restricted inequalities | candidate $4\lambda$, not a proved Hamiltonian rate |
| --- | --- | --- |
| $1/2$ | $80$ | $4g^2/3$ |
| $1/4$ | $112$ | $2g^2$ |
| $1/10$ | $177$ | $2.4g^2$ |

The former adjacent 79 rounds down: $79^2<2304e$. For the withdrawn formal
$24u$ alone, $24u=13824e/(\theta g^4)$ and $24u\le1/2$ requires
$g^4\ge27648e/\theta$. Integers 388, 549, 867 satisfy that **algebraic
condition** at the three listed $\theta$ values; the old middle 548 was
rounded down. None is a uniform gap threshold. The old additional
$g^8\ge1.47\times10^7/[\theta(1-\theta)]$ inherited the unproved count.

For the perturbed restricted count, $\theta=1/2$, $\eta_E=0.1$ give
$\lambda=\delta'=0.3g^2$. Requiring the formal $B'$ majorant to meet the
overlap conditions yields
$$e\eta2^q\le0.15g^2-384e/g^2,\qquad
 e\eta2^q\le0.6g^2/\max(4,q)-24e/g^2.$$

| $g^2$ | $q=4$ restricted $\eta$ | $q=8$ restricted $\eta$ | binding condition for $q=8$ |
| --- | --- | --- | --- |
| $100$ | $0.104$ | $0.00655$ | first |
| $200$ | $0.569$ | $0.0210$ | second |
| $400$ | $1.31$ | $0.0428$ | second |

Values are rounded down, in lattice energy units; the first insertion's
$2^q$ multiplicity is included. At large $g^2$, $\theta\le1/2$, the formal
slope is $4\theta(1-\eta_E)g^2/[3\max(4,q)e2^q]$. This is a property of
the restricted count, not the existential theorem's range dependence.
The former suggestion to divide tolerances by 24 at the same couplings
also fails algebraically: $24u'\le1/2$ would require
$e\eta2^q\le0.00625g^2-384e/g^2$, with no nonnegative solution unless
$g^4\ge61440e$. None of these tables locates the proved target region.

## From normalized true-vacuum correlations to a gap

Let $\psi_0>0$ be the normalized true finite-volume ground state and
$f_A=(A-\langle A\rangle_0)\psi_0$, for bounded gauge-invariant
multiplication observables, including whole-lattice supports. If
$$0\le\langle f_A,e^{-t(H-E_0)}f_A\rangle\le C_Ae^{-mt}
 \quad(t\ge0)$$
holds for every such $A$, then $\Delta^{\rm phys}\ge m\hbar c/a$ in
this dimensionless time convention. Indeed positive spectral mass below
$m-\zeta$ would contradict the exponential bound. The $f_A$ are dense in
the physical vacuum complement: truncate the gauge-invariant ratio
$f/\psi_0$ and then center. Bounded spectral projections extend their
vanishing from that dense set. Infinite volume additionally needs a named
vacuum GNS representation and dense observable domain.

This spectral lemma's hypothesis has not been proved by the history count.
For true-vacuum-centered $A$, the rank-one ground projection gives only
$$\frac{\langle\Omega_0,e^{-TH}A^*e^{-tH}Ae^{-TH}\Omega_0\rangle}
 {\langle\Omega_0,e^{-(2T+t)H}\Omega_0\rangle}
 \longrightarrow\langle\psi_0,A^*e^{-t(H-E_0)}A\psi_0\rangle.$$
A proof of decay needs a normalized connected insertion bound uniform in
boundary distance $T$ and volume. Individual four-link histories alone do
not show that each correlation cluster spans area at least $4t$. Thus
$m=4\lambda$, a uniform limiting coefficient four in electric-gap units,
and any asserted $O(g^{-4})$ relative correction remain unproved here.

## Time-discretized comparison and its missing activity bound

For the uncentered $SU(3)$ normalization the local perturbation is
$\beta\le54/g^4$. The earlier proof-extraction estimate assumed support
entropy $c^n$, $c=80e$, per-site activity $\rho^n$, and
$\sum_{n\ge1}(ce\rho)^n\le1$, hence $\rho\le1/(160e^2)$. It further
assumed
$$\rho_J=e^{-t_0},\qquad \rho_I=2et_0\beta e^{64t_0}.$$
The 64 is the proposed shadow volume $|\{0,1\}^3|^2$; the insertion
factor minimizes $2\alpha e^{t_0\beta/\alpha}$ at $\alpha=t_0\beta$.
Taking $t_0=7.1\ge\log160+2$ would require
$$\beta\le\frac{e^{-454.4}}{160e^2\,2e\cdot7.1},\qquad
 \log\beta\lesssim-465,\qquad
 \log g_0^2\simeq\tfrac12(\log54+465)\simeq234.5.$$
The resulting order $10^{102}$ is a **heuristic extraction**, not a numerical
conclusion of Yarotsky's theorem: conversion of full configuration weights
and multiplicities into the assumed support-site bound is missing. Nor is
$e^{64t_0}$ an unavoidable cost of all discretized methods. The alternative
illustrative coordination estimate $g^4\gtrsim54\cdot12e$, suggesting
$g^2$ of order 40–70, has no applicable Kirkwood–Thomas or Datta–Kennedy
constant proved here; those sources were read at metadata level only.

## Exact low-energy reductions and the physical scale

Suppose a specified scheme gives $H(a)$ and $H_{\rm eff}(2a)$ whose spectra,
with multiplicities and a common scalar shift, agree below $E_c(a)>E_0(a)$.
Then
$$\Delta(H(a))\ge\min\{\Delta(H_{\rm eff}(2a)),E_c(a)-E_0(a)\}.$$
If a finite sequence reaches the stability theorem at $a_s=2^sa_{\rm UV}$,
in the same full or physical sector at every step, iteration gives
$$\Delta(H(a_{\rm UV}))\ge\min\left\{
 \gamma_q(1-\eta_{E,s})\frac{2g_s^2}{3}\frac{\hbar c}{a_s},
 \min_{k<s}[E_c(a_k)-E_0(a_k)]\right\}.$$
Uniform positive physical margins and controlled $a_s$ are additional
hypotheses as $a_{\rm UV}\to0$; merely having finitely many positive margins
at each cutoff is insufficient. An actual generated interaction must satisfy
the theorem's locality and covariance premises. Reconstruction, nontrivial
spectral weight and the physical limit stay separate
([spectral obligations](mass-gap-obligations-lattice.md)).

The one-loop orientation
$n\simeq(g_{\rm weak}^{-2}-g_{\rm strong}^{-2})/0.0966$ gives about 21
doublings from $g^2=1/2$ to a hypothetical order-$10^2$ endpoint, or order
$10^3$ when the initial inverse coupling is 100. These are extrapolations;
the intermediate region and its corrections are uncontrolled. The
[small-volume Feshbach bridge](weak-coupling-feshbach-reduction.md) uses
a different basis and small parameter and retains its ultraviolet caveat.

## Consequence for STATE

The local stability theorem, exact finite-volume bounds, conditional history
criterion and restricted numerical tests now share one maintained treatment.
Only the first supplies volume uniformity. An explicit continuous-time
threshold requires the missing all-root count and normalized true-vacuum
correlation estimate; a physical continuum gap additionally requires
cutoff-uniform transport and reconstruction along the weak trajectory.
