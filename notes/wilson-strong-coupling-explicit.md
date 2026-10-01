# An explicit strong-coupling gap for the Wilson transfer matrix: $SU(3)$ is gapped for $g^2\ge1059$, with $\Delta\ge(\hbar c/a)\,4\log[1/(176(e^{6/g^2}-1))]$

> **Correction (2026-10-02).** A referee report and the
> [corpus audit](corpus-audit-2026-10-01.md) §3c found the errors below;
> the text is corrected in place.
>
> - The former headline, $g^2\ge176$ with
>   $\Delta_W\ge(\hbar c/a)\,4\log(g^2/176)$, charged each plaquette its
>   leading fundamental coefficient $1/g^2$, and no argument here bounds
>   every polymer weight by that activity. It is kept only as the
>   leading-activity figure. The rigorous threshold of the same chain is
>   $g^2\ge1059$ (exactly $1058.6$); the former rigorous figure
>   $1056=6\times176$ linearized $e^{6/g^2}-1\simeq6/g^2$.
> - §1 bounded $\sum_{r\ne0}d_rc_r/c_0$, a sum of Fourier coefficients.
>   Polymer weights need the sup norm of $f/c_0-1$, which by positivity
>   of the $c_r$ equals $\sum_{r\ne0}d_r^2c_r/c_0=e^{\beta_W}/c_0-1$.
>   The bound $e^{\beta_W}-1$ survives with the new derivation.
> - §1 called $d_fc_f/c_0\simeq1/g^2$ the tube activity. Its own
>   Euler-characteristic formula gives $u=c_f/c_0\simeq1/(3g^2)=\beta_W/18$.
>   The factor $6$ between the two readings of the old table is $2d_f$
>   (the fundamental and its conjugate, and $|\chi_f|\le d_f$); the former
>   account of it is withdrawn. The $SU(N)$ formula holds for $N\ge3$.
> - The cluster size $4T$ was inferred from a single tube. §3 now proves
>   it for chains of polymers and for polymers carrying the observables,
>   on spatial tori with sides of at least $4$. The plaquette-animal bound
>   and the minimal polymer size $6$ now carry proofs (§2), and the decay
>   weight is written $d(\gamma)=\delta|\gamma|$ where the text had
>   $a(\gamma)=(1+\delta)|\gamma|$.
> - Withdrawn as unsupported: "$20e$ is the only constant with room" and
>   "a careful count would lower $176$ to about $10^2$". The weight
>   $a(\gamma)$ and the sup norm also have room (§3).
> - §5 placed the strong edge of the intermediate region at the heuristic
>   $176$; it now uses the rigorous figures. §4's anisotropic transfer
>   matrix now reads $e^{-a_tH_{\rm KS}/\hbar c}$.

**Later-note pointers.** [The Dobrushin note](dobrushin-uniqueness-wilson.md)
proves the lower rigorous threshold $g^2>444$ for the same operator,
with rate $\log(g^2/432)$; its comparison table quotes this note's former
$1056$. [Openings](mass-gap-openings.md) §2, Opening 1, reports a
curvature criterion that would give $g^2>32$ if its normalization
conversion, unchecked there, stands. The Kogut--Susskind explicit
threshold contrasted in §4 was withdrawn on 2026-10-02
([KS note](kogut-susskind-strong-coupling-explicit.md)).
[The bands note](confinement-scale-bands.md) §1 separates the
all-representation activity from the fundamental normalization, as the
correction above now does.

For the Wilson action of $SU(3)$, on every spatial torus whose sides
are at least $4$ lattice units, the Hamiltonian
$H_W=-(\hbar c/a)\log\mathcal T$ of the normalized transfer matrix has
a gap
$$\Delta_W\ \ge\ \frac{\hbar c}{a}\,4\log\frac{1}{176\,(e^{6/g^2}-1)}
\ =\ \frac{\hbar c}{a}\Big(4\log\frac{g^2}{1056}-\frac{12}{g^2}+O(g^{-4})\Big)
\qquad(g^2\ge1059),$$
uniformly in the volume. The threshold that Yarotsky's theorem supplies
for the Kogut--Susskind Hamiltonian is $g_0^2\sim10^{101}$
([threshold note](strong-coupling-threshold-explicit.md)). The Wilson
statement has an explicit threshold because the Euclidean character
expansion is a polymer gas of plaquette sets covering each of their
links at least twice, with no time discretization to pay for. Every
polymer weight is bounded by $\rho^{|\gamma|}$ with
$\rho=e^{\beta_W}-1=e^{6/g^2}-1$, a bound on the sup norm of the
normalized plaquette weight minus one. The Kotecký--Preiss criterion
holds for $20e^2\rho\le0.84$, that is $\rho\le5.684\times10^{-3}$, which
for this $\rho$ means $g^2\ge6/\log(1+0.84/20e^2)=1058.6$. Truncated
correlations in the time direction then decay at rate at least
$4\log(1/(176\rho))$ per lattice unit, because every time slab between
two observables holds at least four plaquettes of one polymer. Through
the transfer matrix $\mathcal T=e^{-aH_W/\hbar c}$, self-adjoint and
positive by link reflection positivity, the rate bounds the gap.

The former headline $g^2\ge176$, with
$\Delta_W\ge(\hbar c/a)\,4\log(g^2/176)$, is what the same chain gives
when each plaquette is charged its leading fundamental coefficient
$d_fc_f/c_0\simeq1/g^2$. Nothing here bounds every polymer by that
activity, so $176$ is a leading-activity figure. The rigorous $\rho$
exceeds the leading-order tube activity $u=c_f/c_0\simeq1/(3g^2)$ by
the factor $2d_f^2=18$. That factor, the plaquette-animal entropy $20e$
and the weight $a(\gamma)=|\gamma|$ in the criterion all have room. For
the same operator [the Dobrushin note](dobrushin-uniqueness-wilson.md)
gives the lower rigorous threshold $g^2>444$; the rate here is the
larger one for $g^2\gtrsim1.4\times10^3$. To leading order the gap of
$H_W$ grows like $\log g^2$ and that of $H_{\rm KS}$ like $g^2$, the two
Hamiltonians being different regularizations that agree only in the
continuum limit. Constants explicit; nothing promoted.

## 1. The polymer gas

Write the Wilson weight of a plaquette in characters,
$$f(U_p)=e^{\frac{\beta_W}{N}\operatorname{Re}\operatorname{tr}U_p}
=c_0(\beta_W)\Big[1+\sum_{r\ne0}d_r\frac{c_r}{c_0}\chi_r(U_p)\Big],
\qquad c_r=\frac1{d_r}\int f(U)\,\overline{\chi_r(U)}\,dU ,$$
with $\beta_W=2N/g^2$, and put $\phi(U)=f(U)/c_0-1$, $\phi_p=\phi(U_p)$. Expanding
$\prod_p(1+\phi_p)$ over sets $X$ of plaquettes and integrating over links,
a link lying in exactly one plaquette $p$ of $X$ integrates $\phi_p$
against Haar measure and gives $\int\phi\,dU=0$. Only sets covering each
of their links at least twice contribute: closed surfaces, possibly
branched (for $SU(3)$ three fundamentals can meet at a link, since
$f^{\otimes3}\ni1$), the smallest being the six faces of a cube (§2).
The polymers are the link-connected such sets, two polymers being
incompatible when they share a link, and
$$Z=c_0^{|\mathcal P|}\sum_{\text{compatible families}}\ \prod_\gamma w(\gamma),
\qquad w(\gamma)=\int\prod_{p\in\gamma}\phi_p\,dU .$$

*Surfaces and the tube activity.* Take a closed surface $S$ that is a
manifold (each link in exactly two of its plaquettes) and carries the
fundamental with a consistent orientation. The link integrals
$\int\chi_f(U_1h)\chi_f(h^{-1}U_2)\,dh=\chi_f(U_1U_2)/d_f$ give $d_f^{-1}$
per link, each vertex closes one index loop worth $d_f$, and each
plaquette brings $d_fc_f/c_0$ from the expansion, so the term is
$$d_f^{V-L+|S|}\Big(\frac{c_f}{c_0}\Big)^{|S|}=d_f^{\chi(S)}\,u^{|S|},
\qquad u=\frac{c_f}{c_0},$$
with $\chi(S)$ the Euler characteristic. The dimensions enter only
through $\chi(S)$, and the activity per plaquette along a tube is $u$.
For $SU(N)$ with $N\ge3$, the order-$\beta_W$ term of the expansion below
gives $d_fc_f=\beta_W/(2N)+O(\beta_W^2)$, and $c_0=1+O(\beta_W^2)$, so
$$u=\frac{\beta_W}{2N^2}\big(1+O(\beta_W)\big)=\frac{1}{Ng^2}\big(1+O(g^{-2})\big),
\qquad u=\frac{\beta_W}{18}+O(\beta_W^2)=\frac1{3g^2}+O(g^{-4})\quad(SU(3)),$$
the textbook strong-coupling parameter. The fundamental coefficient
$d_fc_f/c_0=1/g^2+O(g^{-4})$ is $d_f$ times larger.

**All representations, rigorously.** Put $x=\beta_W/N$ and expand
$$e^{x\operatorname{Re}\operatorname{tr}U}=\sum_{k\ge0}\frac{x^k}{k!}\,2^{-k}\sum_{j=0}^k\binom kj(\operatorname{tr}U)^j(\overline{\operatorname{tr}U})^{k-j}.$$
The integral $\int(\operatorname{tr}U)^j(\overline{\operatorname{tr}U})^{k-j}\overline{\chi_r(U)}\,dU$
is the multiplicity $m_r(j,k-j)\ge0$ of $r$ in
$f^{\otimes j}\otimes\bar f^{\otimes(k-j)}$, and counting dimensions,
$\sum_rd_r\,m_r(j,k-j)=N^k$. Hence $c_r\ge0$ for every $r$, and, every
term being nonnegative,
$$\sum_rd_r^2c_r=\sum_{k\ge0}\frac{x^k}{k!}\,2^{-k}\sum_{j=0}^k\binom kjN^k=e^{Nx}=e^{\beta_W}.$$
Since $|\chi_r|\le d_r$, the character series of $f$ converges
absolutely and uniformly, to $f$ by Peter--Weyl, and
$$\sup_U|\phi(U)|\ \le\ \sum_{r\ne0}d_r\frac{c_r}{c_0}\,\sup_U|\chi_r(U)|
=\sum_{r\ne0}d_r^2\frac{c_r}{c_0}=\frac{e^{\beta_W}}{c_0}-1,$$
with equality at $U=\mathbb 1$. Jensen's inequality with
$\int\operatorname{Re}\operatorname{tr}U\,dU=0$ gives $c_0\ge1$.
Therefore every polymer weight obeys
$$|w(\gamma)|\ \le\ \int\prod_{p\in\gamma}|\phi_p|\,dU\ \le\ \rho^{|\gamma|},
\qquad\rho=e^{\beta_W}-1=e^{2N/g^2}-1\ \simeq\ \frac{6}{g^2}\quad(SU(3)).$$
This one bound covers every representation, both orientations and the
branched polymers. Its leading term $2N/g^2$ is the sup norm
$2d_f\cdot d_fc_f/c_0$ of the fundamental and antifundamental terms.

## 2. Convergence: the Kotecký--Preiss criterion with numbers

*Adjacency.* In four dimensions a link lies in six plaquettes, and two
distinct plaquettes share at most one link, so a plaquette shares a
link with exactly $4\times5=20$ others (on $\mathbb Z^4$, or on a torus
with sides of at least $3$).

*Animals.* In a graph of maximal degree $D$, the connected sets of $n$
vertices containing a given vertex number at most
$\binom{Dn}{n-1}\le(eD)^{n-1}$. Order the neighbours of each vertex.
Breadth-first search inside a set $S$ from the given vertex, in that
order, assigns to each vertex of $S$ the subset of its $D$ neighbour
slots through which it discovers new vertices. The sequence of these
$n$ subsets in search order determines $S$, by replaying the search, and
their sizes add to $n-1$; such sequences correspond to $(n-1)$-element
subsets of the $Dn$ slots. Then
$\binom{Dn}{n-1}\le(Dn)^{n-1}/(n-1)!\le(eD)^{n-1}\big(\tfrac{n}{n-1}\big)^{n-1}e^{-1}\le(eD)^{n-1}$,
using $m!\ge e(m/e)^m$ (from $\log m!\ge\int_1^m\log t\,dt$) and
$(1+\tfrac1{n-1})^{n-1}\le e$. For plaquettes $D=20$: at most
$(20e)^{n-1}$ connected sets of $n$ plaquettes contain a given one.

*Minimal size.* A nonempty set $X$ of plaquettes covering each of its
links at least twice has $|X|\ge6$. Let $p\in X$ lie in the $(\mu,\nu)$
plane with corner at the origin, with sides $\ell_1$ and $\ell_3$ in
direction $\mu$ at $x_\nu=0$ and $x_\nu=1$, and $\ell_2$, $\ell_4$ in
direction $\nu$. Since two distinct plaquettes share at most one link,
the four sides are covered by four distinct plaquettes
$q_i\in X\setminus\{p\}$, $\ell_i\in q_i$, so $|X|\ge5$. Suppose
$|X|=5$. The side $f_1$ of $q_1$ opposite $\ell_1$ is a $\mu$-link
displaced from $\ell_1$ by $\pm e_\lambda$; it lies at $x_\nu=-1$ if
$\lambda=\nu$ (the sign is fixed by $q_1\ne p$), and at $x_\nu=0$ with a
nonzero $\lambda$-coordinate otherwise. A $\mu$-link of $q_2$ or $q_4$
requires the plaquette to lie in the $(\mu,\nu)$ plane through $\ell_2$
or $\ell_4$, where all $\mu$-links have $x_\nu\in\{0,1\}$ and zero
$\lambda$-coordinate; every vertex of $q_3\ne p$ has $x_\nu\in\{1,2\}$;
and the $\mu$-links of $p$ are $\ell_1,\ell_3$. So $f_1$ lies in $q_1$
alone, a contradiction. On a torus, sides of at least $4$ keep the
coordinates $-1,0,1,2$ distinct.

*Incompatible polymers.* A polymer $\gamma'$ incompatible with $\gamma$
contains one of the at most $4|\gamma|\times6=24|\gamma|$ plaquettes
through a link of $\gamma$, so the number of such $\gamma'$ of size $n$
is at most $24|\gamma|(20e)^{n-1}$, with $n\ge6$.

*Criterion.* Kotecký and Preiss (Commun. Math. Phys. 103 (1986) 491;
metadata level): if $a\ge0$ satisfies
$\sum_{\gamma'\not\sim\gamma}|w(\gamma')|e^{a(\gamma')}\le a(\gamma)$ for
every $\gamma$, with $\gamma'=\gamma$ included, then the cluster
expansion of $\log Z$ converges absolutely and the clusters $X$
containing a polymer incompatible with $\gamma$ obey
$\sum_{X\not\sim\gamma}|\Phi^T(X)|\prod_{\gamma'\in X}|w(\gamma')|\le a(\gamma)$.
With $a(\gamma)=|\gamma|$ and $|w(\gamma')|\le\rho^{|\gamma'|}$ the
condition follows from
$$\frac{24}{20e}\sum_{n\ge6}\big(20e^2\rho\big)^n\ \le\ 1
\qquad\Longleftarrow\qquad x\equiv20e^2\rho\le0.84 ,$$
since $24/(20e)=0.4415$ and $0.4415\,x^6/(1-x)$ is increasing, equal to
$0.969$ at $x=0.84$. So the expansion converges, uniformly in the
volume, for
$$\rho\ \le\ \rho_*=\frac{0.84}{20e^2}=5.684\times10^{-3}=\frac1{175.93},$$
which for the rigorous $\rho=e^{6/g^2}-1$ of $SU(3)$ reads
$g^2\ge6/\log(1+\rho_*)=1058.6$.

## 3. Decay of correlations and the gap

*Decay weights.* Applying the criterion to the weights
$|w(\gamma)|e^{d(\gamma)}$, whose clusters carry the same coefficients
$\Phi^T$, gives: if
$$\sum_{\gamma'\not\sim\gamma}|w(\gamma')|e^{a(\gamma')+d(\gamma')}\le a(\gamma)\ \text{for every }\gamma,
\quad\text{then}\quad
\sum_{X\not\sim\gamma}|\Phi^T(X)|\prod_{\gamma'\in X}|w(\gamma')|\,e^{d(X)}\le a(\gamma),$$
with $d(X)=\sum_{\gamma'\in X}d(\gamma')$. With $a(\gamma)=|\gamma|$ and
$d(\gamma)=\delta|\gamma|$ the count of §2 goes through whenever
$xe^\delta\le0.84$, that is for
$$\delta\ \le\ \delta_*=\log\frac{0.84}{20e^2\rho}=\log\frac{1}{175.93\,\rho}.$$

*Observables as decorations.* Let $A$ and $B$ be bounded gauge-invariant
functions of the spatial links of the time slices $0$ and $T\ge1$, with
supports $S_A$, $S_B$, and set
$$Z(\lambda,\mu)=\int(1+\lambda A)(1+\mu B)\prod_p(1+\phi_p)\,dU,\qquad
\langle A;B\rangle=\partial_\lambda\partial_\mu\log Z\big|_{\lambda=\mu=0}.$$
Expanding as in §1, $A$ and $B$ join the polymers that share a link
with their supports. Besides the polymers $\gamma$ there are decorated
polymers $(A,\gamma)$, $(B,\gamma)$ and $(AB,\gamma)$, with $\gamma$
possibly empty or disconnected but $S_A\cup\gamma$ (and so on)
link-connected, weights such as $\lambda\int A\prod_{p\in\gamma}\phi_p\,dU$,
and incompatibility again meaning a shared link. A link of $\gamma$
outside the supports still integrates to zero unless $\gamma$ covers it
twice, and $|\lambda\int A\prod \phi_p|\le|\lambda|\,\|A\|_\infty\rho^{|\gamma|}$.
Give a decorated polymer $a=|\gamma|+|S_A|/4+1$ (with $|S_A|+|S_B|$ for
$(AB,\gamma)$) and $d=\delta|\gamma|$. At $xe^\delta\le0.84$ the
undecorated polymers incompatible with an undecorated centre $\gamma$
contribute at most $0.969\,|\gamma|$ to its sum, by §2, and those
incompatible with a decorated centre at most
$0.969\,(|S_A|/4+|\gamma|)$, counting the $6|S_A|$ extra plaquettes
through the support. The decorated polymers contribute at most the
total $D$ of $|w|e^{a+d}$ over all of them. $D$ is finite, because their
plaquette sets are unions of connected sets touching a support, counted
by §2 with ratio $20e\cdot\rho e^{1+\delta}=xe^\delta\le0.84<1$, and $D$
is proportional to $|\lambda|$ or $|\mu|$. Take $|\lambda|\le r_A$ and
$|\mu|\le r_B$ small enough, depending on $A$ and $B$, that $D\le0.18$.
Undecorated polymers of nonzero weight have $|\gamma|\ge6$, so
$0.969\,|\gamma|+0.18\le|\gamma|$, and the criterion holds for the
enlarged gas with the same $\delta$. Every cluster that
depends on both $\lambda$ and $\mu$ is incompatible with the polymer
$(A,\emptyset)$, so the conclusion of the criterion and Cauchy's
estimate give
$$|\langle A;B\rangle|\ \le\ \frac{|S_A|/4+1}{r_Ar_B}\,e^{-\delta L_{AB}},$$
with $L_{AB}$ the least value of $\sum_{\gamma\in X}|\gamma|$ over such
clusters $X$ of polymers of nonzero weight.

*Size of a connecting cluster: $L_{AB}\ge4T$.* For $0\le t<T$ call the
temporal plaquettes between times $t$ and $t+1$ slab $t$. The objects
of such a cluster (its plaquettes and the two supports) are connected
through shared links, so they contain a chain from $S_A$ to $S_B$ in
which consecutive objects share a link, hence a vertex. Every object
other than a plaquette of slab $t$ has all its vertices at times
$\le t$ or all at times $\ge t+1$, so the chain contains a plaquette
of slab $t$, belonging to some polymer $\pi$ of the cluster.
The temporal links of slab $t$ lie outside $S_A\cup S_B$, so each one
that $\pi$ uses lies in at least two plaquettes of $\pi$, all in slab
$t$. Project slab $t$ to the spatial lattice: its plaquettes go to
distinct spatial links and its temporal links to sites. The plaquettes
of $\pi$ in slab $t$ become a finite graph in which every occurring site
has degree at least two, which therefore contains a cycle, and a cycle
of the cubic lattice, or of a spatial torus with sides of at least $4$,
has at least four links. Each of the $T$ slabs thus holds at least four
plaquettes of the cluster, whatever the number of polymers in the chain
and whether or not they carry $A$ or $B$. With periodic time of period
$L_t$ the same argument on both arcs gives $4\min(T,L_t-T)$.

Hence $|\langle A;B\rangle|\le C_{A,B}\,e^{-4\delta_*T}$, and
$$m\,a\ \ge\ 4\delta_*\ =\ 4\log\frac{1}{175.93\,\rho}\ \ge\ 4\log\frac{1}{176\rho}.$$

**Transfer.** The Wilson action is link-reflection positive, so the
transfer matrix $\mathcal T$ is self-adjoint and positive (Lüscher,
Commun. Math. Phys. 54 (1977) 283; Osterwalder and Seiler, Ann. Phys.
110 (1978) 440; metadata level), and $H_W=-(\hbar c/a)\log\mathcal T$
with $\mathcal T$ normalized to top eigenvalue $1$ on gauge-invariant
vectors. On a spatial torus that eigenvalue is simple, with eigenvector
$\Omega>0$, by Jentzsch's theorem
([conditional theorem](mass-gap-conditional-theorem.md) §3, item 3,
which runs the same argument). For bounded gauge-invariant $B$ on one
time slice and $\psi=(B-\langle\Omega,B\Omega\rangle)\Omega$,
$\langle\psi,\mathcal T^n\psi\rangle$ is the $L_t\to\infty$ limit of
$\langle B^*;\theta_nB\rangle_{L_t}$, so it is at most
$C_Be^{-4\delta_*n}$ for all $n$. This forces the spectral measure of
$\psi$ to vanish above $e^{-4\delta_*}$. Because $\Omega>0$, these
$\psi$ are dense in $\Omega^\perp$, and on every spatial torus with
sides of at least $4$
$$\Delta_W\ =\ -\frac{\hbar c}{a}\log\big\|\mathcal T|_{\Omega^\perp}\big\|\ \ge\ \hbar c\,m\ \ge\ \frac{\hbar c}{a}\,4\log\frac{1}{176\rho},$$
uniformly in the volume.

**Numbers for $SU(3)$.**

| per-plaquette activity | status | threshold | gap bound, units $\hbar c/a$ |
| --- | --- | --- | --- |
| sup norm, all representations, $\rho=e^{6/g^2}-1$ | rigorous (§§1--3) | $g^2\ge1059$ (exactly $1058.6$) | $4\log[1/(176(e^{6/g^2}-1))]$, about $4\log(g^2/1056)$ |
| leading fundamental coefficient, $\rho=1/g^2$ | leading-activity figure, unproved for general polymers | $g^2\ge176$ | $4\log(g^2/176)$ |

At $g^2=1059$, $176(e^{6/g^2}-1)=0.999997<1$, so the first gap bound
is positive from the threshold on, and it grows as $4\log(g^2/1056)$.
The rigorous $\rho$ exceeds the coefficient $1/g^2$ by $2d_f=6$: a
factor $2$ for the fundamental and its conjugate, and $d_f$ from
$\sup|\chi_f|$. It exceeds the tube activity $u\simeq1/(3g^2)$ by
$2d_f^2=18$. On an orientable fundamental surface the weight is
$2d_f^{\chi}u^{|S|}$, with one global orientation choice, so both
factors are costs of the sup norm on large surfaces. Recovering them
would require bounding the link integrals of branched and multiply
covered polymers by their Euler-characteristic value, which is not done
here.

*Room.* Three constants are unoptimized: the factor $18$ above; the
animal entropy $20e$, where the search count is crude for plaquettes;
and the weight $a(\gamma)=|\gamma|$. With $a(\gamma)=|\gamma|/10$ the
condition becomes $0.4415\,v^6/(1-v)\le0.1$ for
$v=20e\rho e^{\delta+0.1}$, which allows $20e\rho e^{\delta}$ up to
$0.59$ in place of $0.84/e=0.31$, nearly halving the thresholds in
$g^2$. This is not carried through.

## 4. Relation to the Kogut--Susskind statement

$H_W$ and $H_{\rm KS}$ are different regularizations of the same
continuum Hamiltonian. At strong coupling their gaps differ in kind:
$H_{\rm KS}$ has an electric term of order $g^2\hbar c/a$ and the flux
loop around one plaquette costs $(8/3)g^2\hbar c/a$ for $SU(3)$; $H_W$
has both electric and magnetic content in $-\log\mathcal T$, and to
leading order a plaquette excitation propagates as a tube of four
plaquettes per time step, with energy about
$(\hbar c/a)(-4\log u)\simeq(\hbar c/a)\,4\log(3g^2)$ (a leading-order
estimate). The rigorous bound of §3 has the same form
with $u$ replaced by $176\rho$. The Jaffe--Witten statement asks for the
continuum theory and is indifferent to the regularization, so either
Hamiltonian serves for T2. The one with an explicit volume-uniform
threshold is $H_W$: the Kogut--Susskind explicit threshold was withdrawn
on 2026-10-02 ([KS note](kogut-susskind-strong-coupling-explicit.md)),
which keeps Yarotsky's existential threshold. The anisotropic limit
$a_t\to0$ that turns $\mathcal T$ into $e^{-a_tH_{\rm KS}/\hbar c}$ sends
the temporal plaquette activity to one, outside the expansion, which is
why the Kogut--Susskind threshold needs a genuinely Hamiltonian
expansion and why Yarotsky's time discretization pays what it pays.

## 5. Consequence for STATE

The rigorous strong-coupling edge of this route is $g^2\ge1059$: for the
Wilson transfer matrix and $SU(3)$ the theory is gapped uniformly in
the volume (spatial tori with sides of at least $4$), with
$\Delta_W\ge(\hbar c/a)\,4\log[1/(176(e^{6/g^2}-1))]$. The figure $176$
is the leading-activity reading only. For the same operator the
Dobrushin note's $g^2>444$ is the lower rigorous edge, and this note's
rate is the larger one for $g^2\gtrsim1.4\times10^3$. The unoptimized
constants are the sup-norm factor $18$, the animal entropy $20e$ and the
weight $a(\gamma)$. On the weak side no step is proved with explicit
constants; the necessary window of
[the operator-inequality note](large-field-operator-inequality.md) is
nonempty only for $1/g^2\gtrsim10^2$ (crude constants). The
intermediate region, from $g^2\sim10^{-2}$ to the rigorous strong edge
($444$ by Dobrushin, $1059$ here), is where the gap forms. LLM.md row T2
and trap 17, and [the position note](mass-gap-position.md), should quote
$1059$ for this route where they quote $1056$ or $176$.
