# The bridge midpoint on a compact group at any cut: windings and the centre

**After refereeing (GPT-6 Astra, 2026-09-28).** A1 and A1': ACCEPT the
single- and several-cut identities, with REFINE for metric identifications,
regularity and the extended-character iteration spelled out below. A2:
ACCEPT both reductions; correct the SU(2) theorem number and the bridge
orientation. A3--A4: ACCEPT the centre criterion, torsion, phases and
norms; REFINE the focal-point and relative-exponent qualifications. A5:
ACCEPT the numerical threshold; REFINE its application and the screening
discussion. The image expansion carries signed polynomial amplitudes;
the probability-mixture and topological-winding readings for simply
connected groups are REJECTED. The thin-vortex placement remains a
semiclassical interpretation of exact central phases. All checks used
written derivations.

**Result, 2026-09-28 (Claude; refereed with corrections above).** Let $G$
be a compact connected simply connected Lie group with a bi-invariant
metric, let $t>0$, and take
the heat-kernel bridge of total heat time $t$ from $e$ to $g=e^{iX}$, cut
at fraction $s\in(0,1)$, so that the first piece has heat time $st$. For
every irreducible representation $\lambda$ the midpoint expectation of its
character is an exact finite sum, over the weights $\kappa$ of $\lambda$, of
image sums over the coroot lattice $Q^\vee$ (Theorem 1):

$$\begin{aligned}
E\,\chi_\lambda(m)
&=D_t(X)^{-1}\sum_\kappa m_\lambda(\kappa)
e^{-ts(1-s)|\kappa|^2/2}e^{is\langle\kappa,X\rangle}I_{(1-s)\kappa}(X),\\
I_c(X)&=\sum_{H\in Q^\vee}e^{2\pi i\langle c,H\rangle}
\pi\!\Bigl(\tfrac it(X-2\pi H)-c\Bigr)G_H,\\
D_t(X)&=I_0(X),\qquad G_H=e^{-|X-2\pi H|^2/(2t)}.
\end{aligned}\tag{1}$$

with $m_\lambda(\kappa)$ the weight multiplicities and
$\pi(v)=\prod_{\alpha>0}\langle v,\alpha\rangle/\langle\rho,\alpha\rangle$ the Weyl dimension
polynomial.

- **Corollary 2 (reductions).** For $U(1)$, (1) is the winding mixture of
  [Corollary 5$_s$](series-parallel-gauge-refinement.md)(a). For $SU(2)$ at
  $s=\frac12$ it is Theorems 1 and 2 of the
  [$SU(2)$ midpoint note](su2-midpoint-exact.md), image terms included.
- **Corollary 3 (the centre).** The phase $e^{2\pi i(1-s)\langle\kappa,H\rangle}$ of an image is
  the same for all weights of every representation iff $(1-s)H\in P^\vee$,
  the coweight lattice, and it is then the central character of $\lambda$ at
  $z_H=e^{2\pi i(1-s)H}$. At $s=p/q$ in lowest terms these central images reach
  exactly the $q$-torsion of the centre: $\mathbb Z_{\gcd(q,N)}$ for $SU(N)$.
- **Corollary 4 ($SU(3)$).** At $s=\frac13$ the central images are $H\in3P^\vee$;
  the smallest are the two Weyl triples of $\pm(1,1,-2)$, of relative weight
  $e^{-24\pi^2/t}$ at $X=0$ before polynomial prefactors and the regular limit,
  and they carry $\omega^2$ and $\omega$ on the fundamental
  ($\omega=e^{2\pi i/3}$), the conjugates on the antifundamental and $1$ on the
  adjoint. At $s=\frac12$ every image with a nontrivial phase has a
  weight-dependent one: a halving reaches only the identity in the centre.

For $SU(2)$ at $s=\frac12$ the phase is $(-1)^w$ for half-integer spin and $1$
for integer spin. This is Dirac's belt trick, $\pi_1(SO(3))=\mathbb Z_2$
([Newman 1942](https://doi.org/10.1112/jlms/s1-17.3.173), metadata),
appearing algebraically in the exact midpoint law: the Cartan image
label $w$ shifts a torus geodesic by $4\pi w$, and its midpoint by
$2\pi w$, which spinor characters detect. Since $\pi_1(SU(2))=0$, these
labels describe relative torus geodesics, rather than homotopy sectors of
paths in the group. The spatial belt trick is a comparison through
$SU(2)\to SO(3)$. In specific monopole backgrounds, internal and spatial
rotations also meet in "spin from isospin"
([Jackiw and Rebbi 1976](https://doi.org/10.1103/PhysRevLett.36.1116);
[Hasenfratz and 't Hooft 1976](https://doi.org/10.1103/PhysRevLett.36.1119);
metadata). For $SU(3)$ the same mechanism
carries the triality, and only cuts at thirds (or at denominators
divisible by $3$) produce it.

The ingredients are character orthogonality, the Brauer--Klimyk rule and
Poisson summation, as in the $SU(2)$ note; the denominator of (1) is the
classical image formula for the heat kernel on a compact group
([Fegan 1983](https://doi.org/10.4310/jdg/1214438176), metadata). The
same unfolding and coroot Poisson summation give the heat trace at the
identity and its exponential Seeley--DeWitt structure, $a_k=(R/6)^k/k!$, in the
author's earlier project
([physres1, Remark D9.1o$''$](https://github.com/arivero/physres1/blob/9e31f51/paper/main.md),
2026-02, read); at $X\to0$ the $H=0$ term of the denominator of (1) gives
$k_t(e)\propto t^{-\dim G/2}e^{t|\rho|^2/2}$, the same structure ($R/6=|\rho|^2$ in this metric;
for $SU(2)$, radius 2, $R/6=\frac14$). This describes the local asymptotic
sector; nonzero images give exponentially small corrections at the
identity. With generator $\Delta/2$, the coefficients in powers of $t$
are $(R/12)^k/k!$; $(R/6)^k/k!$ uses heat time for $\Delta$.
No novelty is claimed for the method.

## 1. Conventions

The group metric is that of the
[series/parallel note](series-parallel-gauge-refinement.md) §1:
$-\Delta_G\chi_\lambda=C_2(\lambda)\chi_\lambda$ with $C_2(\lambda)=|\lambda+\rho|^2-|\rho|^2$ in the inner product on
weights dual to the metric on the Cartan algebra $\mathfrak t$. For $SU(N)$
roots have $|\alpha|^2=1$ and coroots $\alpha^\vee=2\alpha/|\alpha|^2$ have $|\alpha^\vee|^2=4$, which is
the metric $|Y|^2=2\,{\rm tr}\,Y^2$ on $\mathfrak t$; then $C_2(j)=j(j+1)$ for $SU(2)$ and
$C_2(\mathbf 3)=\frac43$ for $SU(3)$. Torus elements are $e^{iX}$, $X\in\mathfrak t$; the
pairing of the weight lattice $P$ with the coroot lattice $Q^\vee$ is
integral, $P$ and $Q^\vee$ are dual lattices, and $e^{iX}=e$ iff $X\in2\pi Q^\vee$ ($G$
simply connected). The coweight lattice $P^\vee$ is dual to the root lattice
$Q$, and $P^\vee/Q^\vee\cong Z(G)$ through $Y\mapsto e^{2\pi iY}$. For $SU(2)$, $|X|=\theta$ is the
rotation angle of the $SU(2)$ note, and $X-2\pi w\alpha^\vee$ has length $|\theta-4\pi w|$.

Here $iX/t$ in the argument of $\pi$ means $iX^\flat/t$, using the
metric to identify $\mathfrak t$ with $\mathfrak t^*$. In diagonal
$SU(N)$ coordinates, covectors $a$ have norm $|a|^2=\frac12\sum a_i^2$,
Cartan vectors $H$ have norm $|H|^2=2\sum H_i^2$, and their pairing is
$\sum a_iH_i$. Thus a root $e_i-e_j$ has squared norm 1, its coroot is
the diagonal vector with entries $1,-1$, of squared norm 4, and
$X^\flat=2X$. Pairings between two Cartan vectors below use $2\sum X_iH_i$.

Heat kernel $k_t=\sum_\lambda d_\lambda e^{-tC_2(\lambda)/2}\chi_\lambda$. The bridge midpoint $m$ has
Haar density

$$k_{st}(m)\,k_{(1-s)t}(m^{-1}g)/k_t(g).$$

the bridge law (4) of the series/parallel note becomes this one under
$y=P_em^{-1}$, $g=P_eQ_e$ (with the two heat times assigned as there),
and Corollary 2$_s$ there gives the cut faces heat
times $st$ and $(1-s)t$.

Weyl: $A_v(X)=\sum_{w\in W}\varepsilon(w)e^{i\langle wv,X\rangle}$, $\chi_\lambda=A_{\lambda+\rho}/A_\rho$, $d_\lambda=\pi(\lambda+\rho)$.
Extend $\chi_\nu:=A_{\nu+\rho}/A_\rho$ to every $\nu\in P$: it is zero or $\pm$ an irreducible
character, and $C_2(\nu):=|\nu+\rho|^2-|\rho|^2$ is invariant under the shifted Weyl
action, so it is the Casimir of that character.

*Brauer--Klimyk rule.* $\chi_\lambda\chi_\mu=\sum_\kappa m_\lambda(\kappa)\chi_{\mu+\kappa}$ for dominant $\mu$.
Indeed $\chi_\lambda A_{\mu+\rho}=\sum_\kappa m_\lambda(\kappa)e^{i\langle\kappa,X\rangle}\sum_w\varepsilon(w)e^{i\langle w(\mu+\rho),X\rangle}$, and
replacing $\kappa$ by $w\kappa$, which leaves $m_\lambda$ invariant, gives
$\sum_\kappa m_\lambda(\kappa)A_{\mu+\kappa+\rho}$.

## 2. Theorem 1 and its proof

**Theorem 1 (A1: ACCEPT, conventions refined).** For $A_\rho(X)\ne0$,
(1) holds; on the affine Weyl walls it means the continuous limit of
the complete quotient. Individual image ratios can be singular there.

*Proof.* (i) *Characters.* Expanding both heat kernels gives

$$\begin{aligned}
k_t(g)E\chi_\lambda(m)
&=\sum_{\mu,\nu}d_\mu d_\nu
e^{-stC_2(\mu)/2-(1-s)tC_2(\nu)/2}\\
&\quad\times\int\chi_\lambda(m)\chi_\mu(m)\chi_\nu(m^{-1}g)\,dm.
\end{aligned}$$

The Brauer--Klimyk rule and
$\int\chi_a(m)\chi_b(m^{-1}g)dm=\delta_{ab}\chi_a(g)/d_a$ give

$$k_t(g)\,E\chi_\lambda(m)=\sum_{\mu\ {\rm dominant}}d_\mu\sum_\kappa m_\lambda(\kappa)\,
e^{-stC_2(\mu)/2-(1-s)tC_2(\mu+\kappa)/2}\,\chi_{\mu+\kappa}(g).$$

(ii) *Unfolding.* Multiply by $A_\rho(X)$ and put $v=\mu+\rho$, which runs over
the strictly dominant weights. The summand becomes
$\pi(v)\,m_\lambda(\kappa)\,e^{-\frac t2[s|v|^2+(1-s)|v+\kappa|^2-|\rho|^2]}A_{v+\kappa}(X)$. Expand
$A_{v+\kappa}$ and substitute $v\mapsto w^{-1}v$, $\kappa\mapsto w^{-1}\kappa$: $\varepsilon(w)\pi(w^{-1}v)=\pi(v)$, and
$m_\lambda$ and the norms are Weyl invariant. Each regular weight is the image
of exactly one strictly dominant weight, and $\pi$ vanishes on the walls, so

$$A_\rho(X)k_t(g)E\chi_\lambda(m)=e^{t|\rho|^2/2}\sum_\kappa m_\lambda(\kappa)
\sum_{v\in P}\pi(v)\,e^{-\frac t2[s|v|^2+(1-s)|v+\kappa|^2]}e^{i\langle v+\kappa,X\rangle}.$$

More explicitly, set $v'=wv$, $\kappa'=w\kappa$ in each Weyl term.
Then $\varepsilon(w)\pi(v)=\pi(v')$. Strictly dominant integral weights
are precisely $\rho+P_+$, since their simple-coroot coordinates are
positive integers. The disjoint open chambers therefore exhaust the
regular part of $P$ exactly once, with no factor $|W|$. The wall terms
added to this unfolded sum vanish through $\pi(v')$, even when
$v'+\kappa'$ lies off a wall.

(iii) *Square.* $s|v|^2+(1-s)|v+\kappa|^2=|v+(1-s)\kappa|^2+s(1-s)|\kappa|^2$.

(iv) *Poisson summation* over $P$, whose dual lattice is $Q^\vee$:
$\sum_{v\in P}f(v)={\rm vol}(\mathfrak t^*/P)^{-1}\sum_{H\in Q^\vee}\hat f(H)$ with
$\hat f(H)=\int f(y)e^{-2\pi i\langle y,H\rangle}dy$. With $y=u-(1-s)\kappa$ one has
$\langle y+\kappa,X\rangle=\langle u,X\rangle+s\langle\kappa,X\rangle$ and $\langle y,H\rangle=\langle u,H\rangle-(1-s)\langle\kappa,H\rangle$, so

$$\hat f(H)=e^{is\langle\kappa,X\rangle}e^{2\pi i(1-s)\langle\kappa,H\rangle}\int\pi(u-(1-s)\kappa)\,
e^{-t|u|^2/2}e^{i\langle u,Z\rangle}du,\qquad Z=X-2\pi H.$$

(v) *The Gaussian integral.* $\pi$ is harmonic: $\Delta\pi$ is Weyl-antisymmetric
of lower degree, and every Weyl-antisymmetric polynomial is divisible by
$\pi$. Its derivatives are harmonic too. For a harmonic homogeneous $h$ of
degree $d$, Hobson's formula $h(\partial)F(|Z|^2)=2^dh(Z)F^{(d)}(|Z|^2)$ gives
$h(-i\partial_Z)e^{-|Z|^2/(2t)}=h(iZ/t)\,e^{-|Z|^2/(2t)}$. Taylor-expanding $\pi(u-c)$ in $c$
into harmonic pieces and summing back,

$$\int\pi(u-c)\,e^{-t|u|^2/2+i\langle u,Z\rangle}du=\Bigl(\frac{2\pi}t\Bigr)^{n/2}
\pi\Bigl(\frac{iZ}t-c\Bigr)e^{-|Z|^2/(2t)},\qquad n=\dim\mathfrak t.$$

(vi) The trivial representation ($\kappa=0$ only) gives the denominator.
The constants $e^{t|\rho|^2/2}$, ${\rm vol}(\mathfrak t^*/P)^{-1}$ and $(2\pi/t)^{n/2}$ cancel. All
sums converge absolutely. $\square$

**Theorem 1$'$ (several cuts; A1': ACCEPT).** Cut the same bridge at
$0<s_1<\dots<s_n<1$, with layer values $m_1,\dots,m_n$, and take irreducible
representations $\lambda_1,\dots,\lambda_n$. With $\boldsymbol\kappa=(\kappa_1,\dots,\kappa_n)$ running over weights of
$\lambda_1,\dots,\lambda_n$, $A(\boldsymbol\kappa)=\sum_j(1-s_j)\kappa_j$ and the bridge covariance form
$Q(\boldsymbol\kappa)=\sum_{i,j}\min(s_i,s_j)\,(1-\max(s_i,s_j))\langle\kappa_i,\kappa_j\rangle$,

$$\begin{aligned}
E\prod_j\chi_{\lambda_j}(m_j)
&=D_t(X)^{-1}\sum_{\boldsymbol\kappa}\prod_jm_{\lambda_j}(\kappa_j)\\
&\quad\times e^{-tQ(\boldsymbol\kappa)/2}
e^{i\langle\sum_js_j\kappa_j,X\rangle}I_{A(\boldsymbol\kappa)}(X).
\end{aligned}\tag{1$'$}$$

*Proof.* Integrate $m_1,\dots,m_n$ in turn. Each step applies the
Brauer--Klimyk rule, which holds with the extended characters $\chi_\nu$ for
every $\nu\in P$ (its proof uses only the Weyl invariance of the weight
multiset), and orthogonality; this gives
$k_t(g)E\prod\chi_{\lambda_j}(m_j)=\sum_\mu d_\mu\sum_{\boldsymbol\kappa}\prod m(\kappa_j)
e^{-\frac t2[s_1C_2(\mu)+\sum_j(s_{j+1}-s_j)C_2(\mu+\kappa_1+\dots+\kappa_j)]}\chi_{\mu+\sum\kappa_j}(g)$, $s_{n+1}=1$.
The unfolding of step (ii) holds because the multiset of tuples $\boldsymbol\kappa$ is
invariant under the simultaneous Weyl action. Completing the square,
$s_1|v|^2+\sum_j(s_{j+1}-s_j)|v+\kappa_1+\dots+\kappa_j|^2=|v+A|^2+Q$, where $Q$ is the covariance
of the standard Brownian bridge at the times $s_j$, paired with the $\kappa_j$.
Steps (iv)--(vi) are unchanged with $(1-s)\kappa$ replaced by $A$ and $s\kappa$ by
$\sum_js_j\kappa_j$. $\square$

The iteration can be justified without dividing by dimensions of
extended characters. Heat convolution sends every extended $\chi_\nu$
to $e^{-uC_2(\nu)/2}\chi_\nu$; a wall character stays zero. Multiplication
by the next character obeys Brauer--Klimyk even on a wall, where its
signed terms cancel. Heat convolution preserves that zero sum because
terms representing the same signed irreducible have the same Casimir.
This proves the iterated formula before unfolding. For the square,
put $B(u)=\sum_{s_j\le u}\kappa_j$. Then
$\int_0^1B(u)du=A$ and
$\int_0^1|B(u)|^2du-|A|^2
=\sum_{i,j}[1-\max(s_i,s_j)-(1-s_i)(1-s_j)]
\langle\kappa_i,\kappa_j\rangle=Q$. This also fixes every cross-term
and sign in (1$'$).

The polynomial ratio for a single image is
$\pi(\frac it Z-(1-s)\kappa)/\pi(\frac itZ)=\prod_{\alpha>0}\bigl(1+i(1-s)t\langle\kappa,\alpha\rangle/\langle Z,\alpha\rangle\bigr)$, the
curvature correction; for $SU(2)$ at $s=\frac12$ it is the factor
$1+ikt/(2\theta)$ behind the $-\frac t{2\theta}k\sin\frac{k\theta}2$ term of the $SU(2)$ note.

## 3. Reductions (Corollary 2; A2: ACCEPT with orientation and numbering corrections)

*$U(1)$.* The abelian calculation uses $P=Q^\vee=\mathbb Z$,
$\pi\equiv1$, $\rho=0$, $\langle n,H\rangle=nH$, $X=\theta$:

$$E\,e^{inm}=e^{-ts(1-s)n^2/2}
\frac{\sum_He^{in(s\theta+2\pi(1-s)H)}G_H}{\sum_HG_H}.$$

This is the characteristic
function of the mixture over the winding $H$, with weights $\propto e^{-(\theta-2\pi H)^2/(2t)}$,
of wrapped Gaussians of variance $s(1-s)t$ centred at $s\theta+2\pi(1-s)H$. This is
Corollary 5$_s$(a) of the series/parallel note.

To match that note literally, use $y=P_e-m$, $\theta=\phi_e=P_e+Q_e$
and $H=-W$. Transforming back gives
$m=P_e-s\phi_e+2\pi sH\equiv\bar m_e+2\pi(1-s)W$ modulo $2\pi$,
and the image weight is $e^{-(\phi_e+2\pi W)^2/(2t_e)}$.

*$SU(2)$, $s=\frac12$.* The weights of spin $J$ are $\kappa=k\alpha$, $k=-J,\dots,J$, with
$|\kappa|^2=k^2$, $\langle\kappa,X\rangle=k\theta$, $\langle\kappa,w\alpha^\vee\rangle=2kw$, and $\pi(v)=2\langle v,\alpha\rangle$. The
phase is $e^{2\pi ikw}$: $(-1)^w$ for half-integer $J$ and $1$ for integer $J$. With
$\Xi_{(\sigma)},\Theta_{(\sigma)}$ as in the $SU(2)$ note, the numerator of (1) is
$\sum_ke^{-tk^2/8}e^{ik\theta/2}\bigl[\frac it\Xi_{(\sigma)}-\frac k2\Theta_{(\sigma)}\bigr]$ and the denominator is $\frac it\Xi_+$.
These numerator and denominator expressions have both been divided by
the common factor 2 from $\pi$. Symmetrizing in $k$ gives Theorem 2 of that note, and $J=\frac12$ gives its
Theorem 1, $e^{-t/32}[2\cos\frac\theta4\,\Xi_--\frac t2\sin\frac\theta4\,\Theta_-]/\Xi_+$.
Its Theorem 3(a) then follows using the additional spin-$\frac12$
matrix symmetry established there:
$E D^{1/2}(m)=\lambda D^{1/2}(m_*)$ and
$\lambda=E\chi_{1/2}(m)/(2\cos(\theta/4))$ for $0<\theta<2\pi$.
The cube statement in Theorem 3 also uses independence of its four
bridges. Thus every image agrees, while the character identity alone
supplies no higher-spin diagonal entries.

## 4. The centre (Corollary 3; A3: ACCEPT, geometric scope refined)

*Proof.* Two weights of one representation differ by an element of the
root lattice $Q$, so $e^{2\pi i(1-s)\langle\kappa,H\rangle}$ is independent of $\kappa$ for every $\lambda$ iff
$\langle\beta,(1-s)H\rangle\in\mathbb Z$ for all $\beta\in Q$, i.e. iff $(1-s)H\in Q^*=P^\vee$. Then
$e^{2\pi i(1-s)\langle\kappa,H\rangle}=e^{2\pi i\langle\lambda,(1-s)H\rangle}$ is the scalar by which the central element
$z_H=e^{2\pi i(1-s)H}$ acts in $\lambda$. For $s=p/q$ in lowest terms, $(1-s)=(q-p)/q$ with
$\gcd(q-p,q)=1$, and $(q-p)H/q\in P^\vee$ iff $H/q\in P^\vee$ (Bézout, since
$H\in Q^\vee\subset P^\vee$). So the central images are $H\in qP^\vee\cap Q^\vee$, and the elements
reached are $e^{2\pi i(q-p)Y}$ with $Y\in P^\vee\cap q^{-1}Q^\vee$: the $q$-torsion of
$P^\vee/Q^\vee\cong Z(G)$, on which multiplication by $q-p$ is an automorphism. For
$SU(N)$, $Z(G)=\mathbb Z_N$ and its $q$-torsion is $\mathbb Z_{\gcd(q,N)}$. $\square$

For the necessity of the criterion, the adjoint representation of each
simple factor contains zero and every root; constancy of its phases
forces the root pairings to be integral. For the Bézout step, choose
integers $a,b$ with $a(q-p)+bq=1$ and write
$H/q=a(q-p)H/q+bH\in P^\vee$. These give both directions explicitly.

Consequences. Dyadic refinement ($q=2^n$) reaches the $2$-primary part of
the centre: all of it for $SU(2)$ at the first halving, $\pm1$ at a halving
and $\mathbb Z_4$ at quarters for $SU(4)$, nothing for $SU(3)$ or any odd $N$. The
image classes of a halving, among the groups $SU(N)$, are all central only for $SU(2)$, where
$\frac12Q^\vee=P^\vee$.

Geometrically the nonidentity central elements in these examples are
conjugate cut points of $e$: the shortest
geodesics from $e$ to $e^{2\pi iY}$ ($Y\in P^\vee$ of minimal norm in its class) form
the adjoint orbit of $Y$, a sphere $S^2$ for $-1\in SU(2)$ and a $\mathbb{CP}^2$ for
$\omega\cdot1\in SU(3)$, because conjugation fixes both endpoints.
The stabilizers are $U(1)\subset SU(2)$ and $S(U(2)\times U(1))\subset SU(3)$.
The identity has the unique constant minimizing geodesic. The word
focal refers here to the degeneracy of the exponential map at the
nontrivial central endpoints.

## 5. $SU(3)$ (Corollary 4; A4: ACCEPT, image-size qualification refined)

Use $\mathfrak t=\{H\in\mathbb R^3:\sum H_i=0\}$, $Q^\vee=\mathfrak t\cap\mathbb Z^3$, $|H|^2=2\sum H_i^2$. The weights of $\mathbf3$
are $\kappa_i=e_i-\frac13(1,1,1)$, so $\langle\kappa_i,H\rangle=H_i$: the image $H$ carries the phase
$e^{2\pi i(1-s)H_i}$ on the $i$-th weight.

- $s=\frac13$: the phases $e^{4\pi iH_i/3}$ agree iff $H_1\equiv H_2\equiv H_3\pmod3$, i.e.
  $H\in3P^\vee$. For $(1,1,-2)$ and its Weyl images all $H_i\equiv1$ and the phase is
  $e^{4\pi i/3}=\omega^2$; for $(-1,-1,2)$ and its images it is $\omega$. The
  antifundamental gets the conjugates; the adjoint, with weights $e_i-e_j$,
  gets $e^{4\pi i(H_i-H_j)/3}=1$. These images have $|H|^2=12$, so
  $G_H/G_0=e^{-24\pi^2/t+2\pi\langle X,H\rangle/t}$. The root images, such as $(1,-1,0)$ with
  $|H|^2=4$ and $G_H/G_0\approx e^{-8\pi^2/t}$, give the fundamental the phases $\omega^2,\omega,1$:
  weight-dependent.
- $s=\frac12$: the phases $e^{\pi iH_i}$ agree iff all $H_i$ have the same parity;
  with $\sum H_i=0$ they are then all even, $H\in2Q^\vee$, and the phase is $1$.

An $SU(3)$ halving produces identity phases on $2Q^\vee$ and
weight-dependent phases otherwise. For a root image $(1,-1,0)$ at
halving, the fundamental and antifundamental have phases $(-1,-1,1)$;
the adjoint has phases $(-1)^{H_i-H_j}$ on its six roots and 1 on its
two zero weights. At trisection the antifundamental phases are the
conjugates of the fundamental ones, and the adjoint root phases are
$e^{4\pi i(H_i-H_j)/3}$, with two additional 1's. This confirms both
cuts on $\mathbf3,\overline{\mathbf3},\mathbf8$.

The norms follow directly: $2(1+1+4)=12$ for $(1,1,-2)$ and
$2(1+1)=4$ for $(1,-1,0)$. The exact exponential ratio for any image is
$G_H/G_0=\exp[-(2\pi^2|H|^2-2\pi\langle X,H\rangle)/t]$.
Consequently the difference $16\pi^2$ between the two displayed
exponents is their value at $X=0$; at general $X$ it includes the
linear endpoint terms and the polynomial amplitudes. At singular $X$
one must first combine the images and take the regular limit.

*Remark (a trisection as three fusing vortices; semiclassical placement).*
A trisection inserts two layers, at $s=\frac13$ and $\frac23$; the marginal law of
each is (1). For a central image $H=3Y$, $Y\in P^\vee$, $z=e^{2\pi iY}$, the image path
$e^{iu(X-2\pi H)}$ passes the two layers at $e^{iX/3}z^{-1}$ and $e^{2iX/3}z^{-2}$, so each
of the three sub-segments carries the increment $e^{iX/3}z^{-1}$: every
sub-face of the cut face gains the same central flux $z^{-1}$ relative to
the direct path, and the three fuse to $z^{-3}=1$. The $SU(2)$ halving is the
two-piece case, where each half-face gains $-1$ and the two fuse to $1$,
Dirac's belt. For $SU(3)$ these increments admit a thin-centre-flux
interpretation on the three sub-faces, fusing to the identity. The
trialities also add to zero for three quarks; selecting a colour singlet
additionally requires an invariant tensor. Theorem 1$'$ makes the
placement exact at the level of character moments: for $s_1=\frac13$, $s_2=\frac23$ and
a central image $H=3Y$ the phase is $e^{2\pi i(2\langle\kappa_1,Y\rangle+\langle\kappa_2,Y\rangle)}=\zeta_{\lambda_1}(z)^2\zeta_{\lambda_2}(z)$ with
$\zeta_\lambda(z)=e^{2\pi i\langle\lambda,Y\rangle}$ the central character, which is the phase of the
layers $z^{-1}$ and $z^{-2}$ since $\zeta^3=1$. Joint moments of class functions do not
determine the full joint law of the two layers, whose relative
orientation remains to be described.
The central phase in this remark is ACCEPT (A1'). Identifying an image
with a physical vortex configuration or a positive path sector requires
additional measure information: the amplitudes in (1) and (1$'$)
include signed Weyl polynomials. In particular $G_H$ alone gives no
probability for such a vortex.

### 5b. Fundamental trisection with its first image shells (Round 5B B1)

For $t>0$, write $X=\operatorname{diag}(x_1,x_2,x_3)$ with
$\sum x_i=0$ and initially $A_\rho(X)\ne0$. Put $u=t/3$,
$z_{ij}=z_i-z_j$, and $\Delta(Z)=z_{12}z_{13}z_{23}$. The three
polynomial prefactors are

$$\begin{aligned}
P_1(Z)&=z_{23}(z_{12}+iu)(z_{13}+iu),\\
P_2(Z)&=z_{13}(z_{12}-iu)(z_{23}+iu),\\
P_3(Z)&=z_{12}(z_{13}-iu)(z_{23}-iu).
\end{aligned}\tag{2}$$

Thus $P_i(Z)=\Delta(Z+iu\kappa_i)$, with the coordinates of
$\kappa_i$ regarded here as ordinary triples. The shifts of differences
are what matters; no metric identification is implicit in (2).
Define the two explicitly weighted polynomials

$$\begin{aligned}
F_X(Z)&=\sum_{i=1}^3 e^{ix_i/3}P_i(Z),\\
F_X^{ab}(Z)&=\omega^2e^{ix_a/3}P_a(Z)
+\omega e^{ix_b/3}P_b(Z)+e^{ix_c/3}P_c(Z),
\end{aligned}$$

where $a\ne b$ and $c$ is the remaining index. Let
$R_{ab}=e_a-e_b$ and $C_a=(1,1,1)-3e_a$. The six $R_{ab}$ are the
leading root images and the two triples $\{C_a\}$, $\{-C_a\}$ are
the leading nonzero central images. Formula (1) becomes the exact identity

$$E\chi_{\mathbf3}(m)=e^{-t/27}
\frac{\mathcal N_0+\mathcal N_R+\mathcal N_C+\mathcal R_N}
{\mathcal D_0+\mathcal D_R+\mathcal D_C+\mathcal R_D},
\qquad s=\frac13,\tag{3}$$

with the following terms displayed without a small-$t$ expansion:

$$\begin{aligned}
\mathcal N_0&=F_X(X),&\mathcal D_0&=\Delta(X),\\
\mathcal N_R&=e^{-8\pi^2/t}\sum_{a\ne b}
e^{4\pi(x_a-x_b)/t}F_X^{ab}(X-2\pi R_{ab}),\\
\mathcal D_R&=e^{-8\pi^2/t}\sum_{a\ne b}
e^{4\pi(x_a-x_b)/t}\Delta(X-2\pi R_{ab}),\\
\mathcal N_C&=e^{-24\pi^2/t}\sum_{a=1}^3
\Bigl[\omega^2e^{-12\pi x_a/t}F_X(X-2\pi C_a)\\
&\hspace{43mm}+\omega e^{12\pi x_a/t}F_X(X+2\pi C_a)\Bigr],\\
\mathcal D_C&=e^{-24\pi^2/t}\sum_{a=1}^3
\Bigl[e^{-12\pi x_a/t}\Delta(X-2\pi C_a)\\
&\hspace{43mm}+e^{12\pi x_a/t}\Delta(X+2\pi C_a)\Bigr].
\end{aligned}\tag{4}$$

For precision the remainders are exact sums. With
$\mathcal T=Q^\vee\setminus(\{0\}\cup\{R_{ab}\}\cup\{\pm C_a\})$,
$Z_H=X-2\pi H$ and
$r_H=\exp[-2\pi^2|H|^2/t+4\pi\sum_i x_iH_i/t]$,

$$\begin{aligned}
\mathcal R_N&=\sum_{H\in\mathcal T}r_H
\sum_i e^{ix_i/3}\omega^{2H_i}P_i(Z_H),\\
\mathcal R_D&=\sum_{H\in\mathcal T}r_H\Delta(Z_H).
\end{aligned}\tag{5}$$

*Written derivation.* In the dual metric $|\kappa_i|^2=1/3$, giving
$ts(1-s)|\kappa_i|^2/2=t/27$. For a covector $v$,
$\pi(v)=\frac12(v_1-v_2)(v_1-v_3)(v_2-v_3)$, so

$$\pi(iZ^\flat/t-2\kappa_i/3)=(-4i/t^3)P_i(Z),
\qquad \pi(iZ^\flat/t)=(-4i/t^3)\Delta(Z).$$

Cancel $(-4i/t^3)G_0$ from numerator and denominator of (1).
For $R_{ab}$, the three phases are $\omega^2,\omega,1$; for $C_a$
they are all $\omega^2$ and for $-C_a$ all $\omega$. Also
$\sum_i x_i(C_a)_i=-3x_a$. These substitutions prove (3)--(5).
In particular the exact zero-image sector is

$$e^{-t/27}\sum_i e^{ix_i/3}
\prod_{j\ne i}\left(1+\frac{it}{3(x_i-x_j)}\right).\tag{6}$$

The full expression extends continuously across affine walls. The
remainders start at $|H|^2=16$, hence at Gaussian exponent $32\pi^2$
at $X=0$: ordering an integral zero-sum triple shows the only nonzero
norms below 16 are 4 and 12, represented by the two displayed shells.
At a general endpoint the linear terms in $r_H$ remain essential.
Discarding (5) is a formal image truncation until a normalized bound
on the chosen endpoint set has been proved. In particular the
polynomial zeros at $X=0$ require the complete regular limit.

## 6. What the result says, and what it leaves open

**A5: ACCEPT the threshold; REFINE the inference from it.** The result
is an exact statement about one bridge, the building block of the
parallel insertion, for every compact simply connected group, every
representation and every cut fraction. It concerns characters only: the
diagonal entries of the midpoint matrix $E\,D^\lambda(m)$ differ from the weight
terms of (1), since Theorem 4 of the $SU(2)$ note gives the spin-1 entries
an additional Gaussian tail, so atlas cell 1 is unaffected. In the refinement it fixes which
relative Cartan images of a single step have central phases. The
exponents at the identity, $8\pi^2$ (roots) and $24\pi^2$ (central
$SU(3)$ trisection images), exceed the formal per-volume threshold of
the [zero-spacing note](zero-spacing-any-action.md). Indeed, with
$t=g_{\rm lat}^2$ and one-loop running
$t^{-1}=2b_0\log(1/(a\Lambda))$, $b_0=11/(16\pi^2)$, a per-cell
bound $Ct^{-r}e^{-c/t}$ would sum in a fixed four-volume to
$O((\log(1/a))^r a^{2b_0c-4})$. A strict positive power requires
$c>2/b_0=32\pi^2/11$; the two displayed exponents give powers
$2b_0c=11$ and $33$. Logarithmic corrections matter at equality.
The bridge formula supplies neither that normalized per-cell bound
uniformly in boundary data nor its stability under repeated blocking.
The endpoint term $2\pi\langle X,H\rangle/t$, affine-wall limits and
polynomial prefactors must be controlled first. Character moments also
leave the relative orientations needed by $\Psi$ undetermined.

Centre-valued link configurations exist on any lattice whatever
the blocking, and thick centre vortices
([Mack and Petkova 1979](https://doi.org/10.1016/0003-4916(79)90346-4);
['t Hooft 1978](https://doi.org/10.1016/0550-3213(78)90153-0); metadata)
are a question about many steps. In 't Hooft's language (2026-09-29,
from memory, references Crossref-verified): multiplying one mid-edge by a
central element inserts his disorder operator on the dual set of that
edge's faces, so the open question of whether refinement ties to centre
vortices asks whether image terms at a cut $p/q$ generate such insertions;
on a finite torus his twisted boundary conditions and electric and
magnetic flux sectors
(['t Hooft 1979](https://doi.org/10.1016/0550-3213(79)90595-9); metadata)
organize the cycle holonomies whose small-angle part is the non-based
cycle phase of round 12 in the
[small-field note](su2-midplane-small-field.md) §10; and the fractional
topological charge $1/N mod 1$ of twisted configurations
(['t Hooft 1981](https://doi.org/10.1007/BF01208900); metadata; value
recalled) is $rac13$ for $SU(3)$, the group whose centre only trisections
reach. Pure $SU(3)$ has exact centre symmetry
and no dynamical fundamental matter to screen its triality charges;
whether that symmetry is broken depends on the regime.
[Fradkin and Shenker (1979)](https://doi.org/10.1103/PhysRevD.19.3682)
(abstract, checked 2026-09-28) establish an analytic connection between
confinement and Higgs regions for fundamental lattice Higgs matter.
[Osterwalder and Seiler (1978)](https://doi.org/10.1016/0003-4916(78)90039-8)
(metadata) supplies related gauge-field background. Applying Higgs
complementarity directly to fermionic QCD would exceed these statements.
Dynamical fundamental quarks can screen triality and explicitly break
the corresponding centre symmetry; the algebraic phases of (1) remain
properties of the pure heat-kernel bridge. These distinctions belong
in the [joint-paper comparison](three-continuum-limits.md).
Whether a triadic refinement, $b=3$,
organizes the $SU(3)$ large-field terms better than dyadic refinement is
open; factor-2 decimation with the $\mathbb Z_2$ factor kept explicit goes back to
[Tomboulis (1981)](https://doi.org/10.1103/PhysRevD.23.2371) (metadata).

**Blocking and centre prior art (Round 5B B2, bounded search,
2026-09-28).** The following DOI/title pairs were verified through
Crossref; the reading labels specify the evidence used.

- [Gupta, Guralnik, Patel, Warnock and Zemach (1984), *Monte Carlo
  Renormalization Group for SU(3) Lattice Gauge Theory*](https://doi.org/10.1103/PhysRevLett.53.1721)
  (abstract): SU(3) MCRG estimates both the beta function and the
  generated effective action. This supplies direct SU(3) precedent for
  the blocking programme, with no centre-based choice of factor claimed
  in the abstract read here.
- [Bhattacharya, Gupta and Lee (2000), *Fixed-point pure gauge action
  using $b=\sqrt3$ RGT*](https://doi.org/10.1016/S0920-5632(00)00465-5)
  ([passage, §1, eqs. (1)--(4)](https://arxiv.org/pdf/hep-lat/9910046)):
  the block basis uses cube body diagonals, and two successive
  transformations satisfy $T_2T_1=3I$. This is a concrete net factor-3
  construction through two rotated $\sqrt3$ steps. Its stated motivations
  concern geometry, locality and degrees of freedom. The coordinate
  twists of its intermediate lattice are specified by eq. (2); those
  coordinate identifications alone supply no $\mathbb Z_3$ vortex twist.
- [Tomboulis (2007), *Deriving confinement via RG decimations*](https://doi.org/10.22323/1.042.0336)
  ([passage, §§2--4 and conclusion](https://arxiv.org/pdf/0710.1894)):
  potential-moving decimations with scale factor $b$ are applied to
  partition functions with and without external centre flux. The
  explicit group is SU(2); SU(3) is proposed as an extension in the
  conclusion. This supplies a centre-flux observable and a decimation
  strategy to compare with $\Psi$. Its confinement claim is recorded as
  the author's proposal, with no proof of that claim imported here.
- [Kovács--Tomboulis (1999), *SU(3) string tension and the presence of
  vortices*](https://doi.org/10.1016/S0920-5632(99)85139-1)
  ([abstract](https://arxiv.org/abs/hep-lat/9808046)): simulations report
  that centre fluctuations reproduce the heavy-quark potential and
  persist under smoothing. This concerns thick centre vortices; the
  abstract supplies no preferred blocking factor.

The search covered SU(3) Migdal--Kadanoff with $b=3$, MCRG with
$b=3$ or $\sqrt3$, and centre-vortex free energies under decimation.
Within the passages checked, an explicit SU(3) $b=3$ Migdal--Kadanoff
calculation tied to triality, or a $\mathbb Z_3$ vortex-free-energy
decimation justified by the centre order, was not located. This is a
bounded search outcome. The positive finding is the established
$\sqrt3$ geometry and its net factor 3, alongside the external-flux
decimation strategy.

**Relation to Corollary 3 (inference).** Equal subdivision into $b$
pieces gives first cut $s=1/b$ and hence central image phases in
$Z(G)[b]$. A general lattice RG transformation also integrates
transverse variables and can use rotated blocks, so its length factor
alone does not specify this bridge cut. Testing a centre advantage
requires an actual map retaining the joint layers and comparing
normalized twisted and untwisted observables. Equations (3)--(5)
provide explicit character inputs for that test; their image exponents
alone leave the estimate open.

## 7. Consequence for STATE

Atlas §1b: the bullet on which part of the centre a cut reaches now rests
on Corollary 3 of an exact formula, (1), which also carries the $SU(2)$
belt-trick phase and the $SU(3)$ triality at thirds. The Round 5B Part A
referee is complete, with verdicts and corrections above. The exact
trisection formula for the fundamental of $SU(3)$ is now displayed in
§5b, including polynomial prefactors and exact residual sums (Part B,
written derivation, no independent referee yet). The bounded prior-art
search in §6 locates factor-$\sqrt3$ and net factor-3 blocking; the
centre-adapted normalized refinement estimate remains the next question.
