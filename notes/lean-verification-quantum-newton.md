# Quantum-to-Newton results: literature and Lean verification targets

**Result and verification specification, 2026-10-27.** The recent
0+1 construction yields several precise propositions worth formal
checking, but their being new to this repository is not evidence of
publication priority. The strongest distinctive candidates are the
specified $C^{1,1}$ product/packet package and its sharp-rate example,
the explicitly rescaled wall stresses, and the Gaussian preparation
test at a bounded $C^1$ cusp. Each has substantial close prior art.
The universal constructive-lifting conjecture and an independent
positive-action necessity theorem remain **open**.

The targets below are exact mathematical specifications, **not Lean
declarations that have been compiled**. Their written proofs are in
the linked notes and are unrefereed; the $C^{1,1}$ lift received the
internal Sol check recorded there. The targets state real quantifiers
and boundary/domain conventions so a later Lean development can
translate them without strengthening conclusions silently. A
conditional theorem whose hypotheses include the conclusion, a
placeholder quantum theory, or an unchecked imported axiom does not
verify the corresponding concrete target.

## 1. What is already in the literature

| Repository proposition | Closest checked precedent | Proper status |
| --- | --- | --- |
| Coherent packets follow classical flow; smooth-observable semiclassics | [Hepp (1974)](https://doi.org/10.1007/BF01646348), abstract and theorem statements in the maintained note | Established mechanism, not a new proof of classical mechanics as such. |
| Uniform observable time-splitting estimates | [Borns--Weil--Fang, Theorem 2 and §3.2](https://arxiv.org/pdf/2208.07957) (passages read); [Fang--Qu, Theorem 1](https://arxiv.org/html/2507.02783v1) (statement read) | Prior uniform-in-$\hbar$ observable estimates. The former uses smooth bounded symbol classes; the latter treats periodic, spatially discretized polynomial observables and higher-order splittings. Neither passage alone establishes the exact $C^{1,1}$, arbitrary-partition, coherent-packet package below. |
| Reflected Gaussian and wall impulse | [Belloni--Doncheski--Robinett (2004), equations (8)--(11), (16)--(19)](https://arxiv.org/pdf/quant-ph/0408182) (passages read); [De Vincenzo (2013), equations (38)--(39)](https://www.scielo.org.mx/scielo.php?pid=S1870-35422013000200001&script=sci_arttext) (passage read) | The odd-image Gaussian and collision-force analysis already exist. The particular measure limit, scaled profile and Neumann comparison in Target D are precise specializations whose exact priority remains unverified. |
| Preparation-dependent singular-flow selection | [Athanassoulis--Paul, Theorem 2.1 and Lemma 5.3](https://arxiv.org/pdf/1011.1651) (statements and relevant passages read) include cutoff $-|x|^{1+\theta}$, including $\theta=1/2$; [Chabu, Theorem 1.12 and §3](https://arxiv.org/pdf/1608.03716) (statements and passages read) gives identical incoming and different outgoing limits for $-|x|$. | Neither selection failure nor this power-law cusp is new as such. Target E specifies pure Gaussian preparations, a common incoming trajectory and their explicit mixtures for the bounded $C^1$ cusp. In Chabu's theorem the two profiles may also be chosen equal, so equality of initial position densities is not by itself a new general phenomenon. Exact coverage of Target E by prior results has not been settled. |
| Tangent groupoid, its continuous field and strict quantization | [Cariñena et al. (1998/99)](https://arxiv.org/abs/math/9802102), including Rivero, and [Landsman--Ramazan (2000)](https://arxiv.org/abs/math-ph/0001005) (abstracts and groupoid passages read) | Established background; Target B is a particular state-level estimate on that field, not the invention of the groupoid or of strict quantization. |
| Normalized Euclidean tower | Brownian-bridge/Feynman--Kac and martingale constructions; [Dimock I](https://arxiv.org/abs/1108.1335) and [II](https://arxiv.org/abs/1212.5562) (selected sections in the guide) | Target G packages standard ingredients in a 0+1 illustration. Dimock's papers treat three-dimensional scalar $\phi^4$, not this quantum-mechanical theorem or a four-dimensional gauge construction. |
| Relativistic one-particle limit | [Carmona--Masters--Simon](https://doi.org/10.1016/0022-1236(90)90049-Q) and [Hiroshima--Ichinose--Lőrinczi](https://arxiv.org/abs/1109.5829) (abstracts read) | Known relativistic Schrödinger and subordinate-process framework. Target F is a particular joint estimate; no literature priority has been established. |

The table is a bounded search, not an exhaustive novelty determination.
The primary proofs and their retained limitations remain in the
[Lipschitz lift](lipschitz-certificate-quantum-lift.md),
[smooth construction](quantum-blocks-construct-newton.md),
[groupoid note](groupoid-quantum-newton-states.md),
[wall note](dirichlet-wall-impulse.md),
[cusp note](cusp-quantum-preparation-selection.md), and
[relativistic note](relativistic-dispersion-blocks.md).

## 2. Common definitions for Targets A--C

Use $\hbar>0$, $m,\omega>0$, $\mathcal H=L^2(\mathbb R,dq)$,
$Qf(q)=qf(q)$, $P_\hbar=-i\hbar\partial_q$, and
$N_\hbar=1+Q^2+P_\hbar^2$ as the closure of the oscillator operator
on Schwartz space, with $D(N_\hbar)=H^2(\mathbb R)\cap D(Q^2)$. Put
$$
 \|(q,p)\|_\omega=|q|+|p|/(m\omega),\quad
 K_s=e^{-isV(Q)/\hbar},\quad
 D_s=e^{-isP_\hbar^2/(2m\hbar)},\quad S_s=D_sK_s.
$$
For a finite positive partition $\pi=(0=t_0<\cdots<t_n=T)$, write
$s_j=t_{j+1}-t_j$, $|\pi|=\max_j s_j$, and
$S_{\hbar,\pi}(t_j)=S_{s_{j-1}}\cdots S_{s_0}$, with the empty
product at $j=0$. The initial normalized Gaussian is
$$
 g_\hbar(q)=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}
 \exp\!\left[-\frac{m\omega(q-q_0)^2}{2\hbar}
             +\frac{ip_0(q-q_0)}{\hbar}\right]. \tag{1}
$$
The classical kick--drift vertices, starting at
$z_0=(q_0,p_0)$, obey
$$p^{\rm cl}_{j+1}=p^{\rm cl}_j-s_jV'(q^{\rm cl}_j),\qquad
q^{\rm cl}_{j+1}=q^{\rm cl}_j+s_jp^{\rm cl}_{j+1}/m. \tag{2}$$
When used below, $z_{\hbar,\pi}(t)$ is the piecewise-linear
interpolation of the **quantum means at the vertices**; it is not
asserted to be the expectation of a physical intermediate state.

For the Weyl targets, use the Fourier convention
$$
 \widehat b(\xi,\eta)=\int_{\mathbb R^2}
       e^{-i(\xi q+\eta p)}b(q,p)\,dq\,dp,\quad
 \operatorname{Op}^W_\hbar(b)=\frac1{(2\pi)^2}
       \int\widehat b(\xi,\eta)e^{i(\xi Q+\eta P_\hbar)}d\xi d\eta.
 \tag{3}
$$
This fixes the signs and factors needed by a formalization.

## 3. Target A: Lipschitz certificate, quantum product, and packet

**Quantifiers and assumptions.** Let $V\in C^1(\mathbb R;\mathbb R)$
and $L\ge0$ satisfy $|V'(x)-V'(y)|\le L|x-y|$ for every $x,y$.
There is no lower bound assumption on $V$. For every $m,\omega,\hbar>0$,
$T>0$ and $z_0\in\mathbb R^2$, the following are to be proved.

1. The operator
   $H_\hbar=P_\hbar^2/(2m)+V(Q)$ with initial domain
   $\mathcal S(\mathbb R)$ is essentially self-adjoint. Its closure
   generates $U_\hbar(t)=e^{-it\overline H_\hbar/\hbar}$, and this
   group preserves $D(N_\hbar)$ and is strongly continuous there in
   the $N_\hbar$ graph norm. On Schwartz space
   $[Q,P_\hbar]=i\hbar I$; for all $u,v\in\mathbb R$ the bounded
   Weyl operators satisfy
   $e^{iuQ}e^{ivP_\hbar}=e^{-i\hbar uv}e^{ivP_\hbar}e^{iuQ}$.
2. There exists $0<C_{\hbar,T}<\infty$, depending on the supplied model
   and fixed $\hbar,T$, such that **every** positive partition satisfies
   $$
    \|S_{\hbar,\pi}(T)f-U_\hbar(T)f\|_2
      \le C_{\hbar,T}|\pi|\,\|N_\hbar f\|_2
      \quad(f\in D(N_\hbar)). \tag{A1}
   $$
   Consequently the product converges strongly on all of $\mathcal H$
   as $|\pi|\downarrow0$ at each fixed $\hbar$. For a general
   $\psi\in\mathcal H$ one precise modulus is the infimum over
   $f\in D(N_\hbar)$ of
   $2\|\psi-f\|_2+C_{\hbar,T}\delta\|N_\hbar f\|_2$.
   The constant in (A1) is **not** asserted uniform in $\hbar$.
3. Let $z_j^\hbar=(\langle Q\rangle_j,\langle P_\hbar\rangle_j)$
   in the state $S_{\hbar,\pi}(t_j)g_\hbar$, and let
   $W_j=\operatorname{sd}_jQ+\operatorname{sd}_jP_\hbar/(m\omega)$.
   Set $C=\sqrt{2/(m\omega)}$ and
   $\beta=\omega+L/(m\omega)$. Then for every vertex,
   $$
    W_j\le C\sqrt\hbar\,e^{\beta t_j},\qquad
    \|z_j^\hbar-z_j^{\rm cl}\|_\omega
      \le \frac{LC}{m\omega}\,t_j e^{\beta t_j}\sqrt\hbar. \tag{A2}
   $$
   The classical Lipschitz flow $\Phi_t(z_0)$ exists uniquely, and
   there is a finite classical constant $R_T^{\rm cl}$ such that
   $\sup_{0\le t\le T}\|z_\pi^{\rm cl}(t)-\Phi_t(z_0)\|_\omega
   \le R_T^{\rm cl}|\pi|$. Hence the vertices converge to the flow for
   **every** joint limit $\hbar,|\pi|\downarrow0$.

For the conjecture's bounded instance, the input is the *global*
action/force and the classical polygon certificate. (A1) is proved from
that model data plus the operator toolkit; it is not a consequence of
the numerical error constant of a single orbit. Formalizing (A1) while
assuming its self-adjointness or graph bounds should be reported as a
conditional sublemma, not as the whole lift.

## 4. Target B: the smooth $O(\hbar+|\pi|)$ state estimate

Assume in addition that $V\ge0$, $V\in C^\infty$ and all its
derivatives of order at least two are bounded. Fix $h_0,T>0$.
Let $0<\hbar\le h_0$ and let $\pi$ be any positive partition of
$[0,T]$. In the notation above, write
$$
 \begin{gathered}
 a=\max\!\left(\omega,\frac L{m\omega}\right),\qquad
 G_T=(e^{aT}-1)/a,\\
 b_0=\frac{|V'(0)|+LC\sqrt{h_0}e^{\beta T}}{m\omega},\quad
 R_T=e^{\beta T}(\|z_0\|_\omega+Tb_0),\\
 F_T=|V'(0)|+L(R_T+C\sqrt{h_0}e^{\beta T}),\quad
 C_\delta=(F_T+LR_T)/m,\quad
 C_h=\frac{\|V'''\|_\infty C^2e^{2\beta T}}{2m\omega}.
 \end{gathered} \tag{B0}
$$
The specification is
$$
 \sup_{0\le t\le T}\|z_{\hbar,\pi}(t)-\Phi_t(z_0)\|_\omega
 \le G_T(C_\delta|\pi|+C_h\hbar). \tag{B1}
$$
The centering step responsible for the better rate is the separate
lemma
$$
 |\langle V'(Q)\rangle-V'(\langle Q\rangle)|
 \le \tfrac12\|V'''\|_\infty\operatorname{Var}(Q). \tag{B2}
$$
It requires a normalized state in the needed second-moment domain.
The first derivative term cancels; the width itself remains
$O(\sqrt\hbar)$.

For every $b\in C_c^\infty(\mathbb R^2)$ set
$$
 I_b=(2\pi)^{-2}\!\int|\widehat b|(|\xi|+m\omega|\eta|),\quad
 J_b=\frac1{2(2\pi)^2}\!\int|\widehat b|
                         (|\xi|+m\omega|\eta|)^2. \tag{B3}
$$
At every partition vertex the desired **concrete** result is
$$
 \left|\langle g_\hbar,S_{\hbar,\pi}(t_j)^*
       \operatorname{Op}^W_\hbar(b)S_{\hbar,\pi}(t_j)g_\hbar\rangle
       -b(\Phi_{t_j}(z_0))\right|
 \le J_b C^2e^{2\beta T}\hbar+
      I_bG_T(C_\delta|\pi|+C_h\hbar). \tag{B4}
$$
It follows for any joint schedule $\hbar,|\pi|\to0$. An additional
continuous-field corollary takes $\hbar=\epsilon S_*$, $S_*>0$, and
extends the limit to continuous sections of the established tangent
groupoid field: for every continuous section $A$, every family of
partitions with $\epsilon,|\pi_\epsilon|\to0$, and vertices
$t_{j(\epsilon)}\to t\in[0,T]$, the corresponding vector-state value
on $A(\epsilon)$ converges to $A(0)(\Phi_t(z_0))$. This corollary
requires the continuous-field theorem and the identification of (3)
with the chosen quantization section; (B4) alone does not construct
that $C^*$-field.

## 5. Target C: sharpness of the square-root rate

Set $m=\omega=1$, $V(q)=q|q|/2$, $q_0=p_0=0$, and let $g_\hbar$
be (1). This potential is $C^{1,1}$ and **unbounded below**.
The classical trajectory is identically $(0,0)$. Define
$$f(t)=\langle U_1(t)g_1,P_1U_1(t)g_1\rangle.$$
Prove, for every $\hbar>0$ and real $t$,
$$
 \langle U_\hbar(t)g_\hbar,P_\hbar U_\hbar(t)g_\hbar\rangle
    =\sqrt\hbar\,f(t),\qquad f'(0)=-1/\sqrt\pi. \tag{C1}
$$
In particular, there exists $t_0>0$ such that for all
$0<t\le t_0$ and every $\hbar>0$, the absolute momentum error is at
least $t\sqrt\hbar/(2\sqrt\pi)$. This refutes a uniform $O(\hbar)$
mean bound over the full class in Target A. It does not by itself
establish sharpness under an additional lower-bound assumption on $V$.

## 6. Target D: Dirichlet and Neumann wall stresses

Let $m,\omega,q_0>0$, $p_0<0$, $v=p_0/m$,
$t_*=-q_0/v$, $A(t)=1+\omega^2t^2$, and
$\Lambda=|v|\sqrt{m\omega/A(t_*)}$. Let $g_{\hbar,t}$ be the
free whole-line evolution of (1), and let $R$ reflect $q\mapsto-q$.
Put
$$
 \gamma_\hbar=e^{-[m\omega q_0^2+p_0^2/(m\omega)]/\hbar},\quad
 \psi_{\hbar,D/N}(q,t)=
 \frac{g_{\hbar,t}(q)\mp g_{\hbar,t}(-q)}
      {\sqrt{1\mp\gamma_\hbar}}\quad(q>0). \tag{D0}
$$
The upper sign is Dirichlet, the lower Neumann. Define the real
half-line current form and full boundary stress
$$
 J_\hbar(t)=\hbar\operatorname{Im}\!\int_0^\infty
                 \overline\psi\,\partial_q\psi\,dq,\quad
 F_\hbar(t)=\frac{\hbar^2}{2m}
  \left(|\psi'(0,t)|^2-
        \operatorname{Re}[\overline{\psi(0,t)}\psi''(0,t)]\right).
 \tag{D1}
$$
For both indicated wave families, prove $J_\hbar'=F_\hbar$ and,
for every bounded continuous $\varphi:\mathbb R\to\mathbb R$,
$$
 \lim_{\hbar\downarrow0}\int_{\mathbb R}\varphi(t)F_{\hbar,D/N}(t)\,dt
    =2|p_0|\varphi(t_*). \tag{D2}
$$
The Neumann measures are finite **signed** measures; their
Dirichlet-only derivative term vanishes. At each fixed $s\in\mathbb R$
also prove
$$
 \lim_{\hbar\downarrow0}\sqrt\hbar\,
 F_{\hbar,D/N}(t_*+\sqrt\hbar\,s)
 =\frac{2p_0^2}{m}\sqrt{\frac{m\omega}{\pi A(t_*)}}
   e^{-\Lambda^2s^2},\quad
 J_{\hbar,D/N}(t_*+\sqrt\hbar\,s)\to
 |p_0|\operatorname{erf}(\Lambda s). \tag{D3}
$$
This is weak convergence of measures, not convergence in total
variation to the delta. $J_\hbar$ is a current form: the half-line
operator $-i\hbar\partial_q$ is not being asserted self-adjoint.
No general Robin packet limit is part of this target.

## 7. Target E: two preparations and mixtures at a $C^1$ cusp

In units $m=1$, fix $R>0$ and a smooth even cutoff $\chi$ equal to
one on $[-R,R]$ and zero outside $[-2R,2R]$. Set
$$V(q)=-\tfrac23|q|^{3/2}\chi(q),\quad F=-V',\quad
 H_\hbar=-\tfrac{\hbar^2}{2}\partial_q^2+V(Q),\quad
 F_*=\|F\|_\infty.$$
Choose $T>0$ such that $F_*T^2/2<R/4$. Choose $C_0>0$ with
$|F(x)|\le C_0\sqrt{|x|}$ for all $x$, and a fixed $K>0$ such that
$K^2>\max\{16\sqrt2C_0,16/3\}$.
For $0<\hbar<e^{-1}$ put $a_\hbar=1/\log(1/\hbar)$ and
$$
 g_{\hbar,k}(q)=(\pi\hbar)^{-1/4}
 \exp\!\left[-\frac{(q-a_\hbar)^2}{2\hbar}
             -\frac{ik a_\hbar^{3/4}(q-a_\hbar)}{\hbar}\right],
 \quad k\in\{0,K\}. \tag{E0}
$$
These two states have exactly the same initial position density.
Let $\psi_{\hbar,k}(t)=e^{-itH_\hbar/\hbar}g_{\hbar,k}$ and set
$$
 z_+(t)=(t^4/144,t^3/36),\qquad
 z_\times(t)=
 \begin{cases}z_+(t),&t\le0,\\-z_+(t),&t\ge0.\end{cases} \tag{E1}
$$
The target is uniform on $[-T,T]$:
$$
 (\langle Q\rangle_{\hbar,0},\langle P_\hbar\rangle_{\hbar,0})\to z_+,
 \quad
 (\langle Q\rangle_{\hbar,K},\langle P_\hbar\rangle_{\hbar,K})\to z_\times,
 \quad
 \operatorname{sd}Q_{\hbar,k}+\operatorname{sd}P_{\hbar,k}\to0.
 \tag{E2}
$$
For every $\lambda\in[0,1]$ and $\theta\in\mathbb R$, normalize
$\sqrt\lambda\,g_{\hbar,0}
 +e^{i\theta}\sqrt{1-\lambda}\,g_{\hbar,K}$.
For every $b\in C_c^\infty(\mathbb R^2)$, its evolved Weyl expectation
must converge uniformly on $[-T,T]$ to
$$\lambda b(z_+(t))+(1-\lambda)b(z_\times(t)). \tag{E3}$$
Thus both limiting incoming histories agree for $t\le0$ and can have
different outgoing measures. The target neither asserts finite-$\hbar$
Wigner positivity nor classifies waiting-time branches.

## 8. Target F: a relativistic joint limit

Let $V\in C^\infty(\mathbb R;\mathbb R)$ be bounded below with all
derivatives of order at least two bounded, $m,c_0,h_0,T>0$, and
$z_0\in\mathbb R^2$. For $c\ge c_0$, define
$$T_c(p)=\sqrt{m^2c^4+c^2p^2}-mc^2,\quad
 S_{\hbar,c,s}=e^{-isT_c(P_\hbar)/\hbar}e^{-isV(Q)/\hbar}. \tag{F0}$$
For the coherent packet (1), its piecewise-linear interpolated means,
and the nonrelativistic Newton flow $\Phi_t(z_0)$, prove that there
exists $C_T<\infty$, independent of $\hbar,c,\pi$, such that
$$
 \sup_{0\le t\le T}
 \|z_{\hbar,\pi,c}(t)-\Phi_t(z_0)\|_\omega
 \le C_T(\hbar+|\pi|+c^{-2}) \tag{F1}
$$
for all $0<\hbar\le h_0$, $c\ge c_0$ and positive partitions of
$[0,T]$. At fixed $\hbar$, the self-adjoint
$T_c(P_\hbar)+V(Q)$ converges in strong resolvent sense to
$P_\hbar^2/(2m)+V(Q)$ as $c\to\infty$, and its unitary groups
converge strongly, uniformly on compact time intervals.

The separate free wall target uses the *spectral* Dirichlet
Hamiltonian $T_c(\sqrt{-\hbar^2\Delta_D})$, not the generally
different killed nonlocal process. For the odd packet (D0), its
position expectation satisfies, for $|t|\le T$,
$$
 \left|\langle Q\rangle^D_{\hbar,c}(t)-
           |q_0+p_0t/m|\right|
 \le\sqrt{\frac2{1-\gamma_\hbar}}
  \left[\sqrt{\frac{\hbar}{2m\omega}}+
        \frac Tm\sqrt{\frac{\hbar m\omega}{2}}\right]
       +\frac{T|p_0|^3}{2m^3c^2}. \tag{F2}
$$
The positive-energy one-particle operator in an external potential is
not a construction of a Lorentz-covariant interacting field theory.

## 9. Target G: an exact normalized Euclidean tower

Let $V:\mathbb R\to[0,\infty)$ be continuous, $m,\hbar,T>0$, and
$x,y\in\mathbb R$. Let $\mathbb P_0$ be the Brownian bridge of
variance parameter $\hbar/m$ from $x$ to $y$ on $[0,T]$. Define
$$
 W=\int_0^TV(B_t)\,dt,\quad
 Z=\mathbb E_0e^{-W/\hbar},\quad
 \rho=Z^{-1}e^{-W/\hbar},\quad
 \rho_n=\mathbb E_0[\rho\mid\mathcal F_n], \tag{G0}
$$
where $\mathcal F_n$ is generated by dyadic evaluations of $B$.
The target is $Z>0$ and, almost surely,
$$
 \mathbb E_0\rho_n=1,\quad 0<\rho_n\le Z^{-1},\quad
 \rho_n=\mathbb E_0[\rho_{n+1}\mid\mathcal F_n],\quad
 \rho_n\to\rho\ \text{a.s. and in }L^1(\mathbb P_0). \tag{G1}
$$
For arbitrary positive partitions with mesh tending to zero, the
normalized densities obtained from the trapezoidal sums of $V(B_t)$
also converge to $\rho$ in $L^1(\mathbb P_0)$; their polygonal
pushforwards converge weakly on $C([0,T])$. The pushforward measures
are not claimed to converge in total variation. The $\rho_n$ are
conditional expectations of the continuum density; they are not
identified with the original bare finite-lattice density.

## 10. The bridge to newtonlean

The inspected newtonlean master commit is
[8138e944](https://github.com/arivero/newtonlean/commit/8138e9449b4f961c4adbebcb6090acc0d2fd5aaf).
Its toolchain is Lean 4.34.1 core/Std only, with no mathlib.
The current session did not compile it. Its
[FiniteEstimates.cell](https://github.com/arivero/newtonlean/blob/8138e9449b4f961c4adbebcb6090acc0d2fd5aaf/BarrowLib/Polygon/FiniteEstimates.lean)
uses **drift then kick**:
$$\operatorname{DK}_s(q,v)=(q+sv,\ v+sa(q+sv)), \tag{H0}$$
whereas (2), after $v=p/m$ and $a=-V'/m$, is **kick then drift**:
$$\operatorname{KD}_s(q,v)=(q+s[v+sa(q)],\ v+sa(q)). \tag{H1}$$
Equality of the two cells is false. The following finite rational
lemma is an exact interface target, requiring no quantum foundations.

**Target H.** Let $a:\mathbb Q\to\mathbb Q$ be
$\Lambda$-Lipschitz, with $\Lambda\in\mathbb Q_{\ge0}$. Let
$s_0,\ldots,s_{n-1}\in\mathbb Q_{\ge0}$, $\tau\in\mathbb Q_{>0}$,
and put $\|(q,v)\|_\tau=|q|+\tau|v|$.
Iterate KD and DK from the same rational state. Suppose the DK states
$(\bar q_j,\bar v_j)$ satisfy $|a(\bar q_j)|\le A$ and
$|\bar v_j|\le B$ for $j<n$, with $A,B\in\mathbb Q_{\ge0}$. Then
$$
 \|z_n^{KD}-z_n^{DK}\|_\tau
 \le(A+\tau\Lambda B)
 \sum_{j=0}^{n-1}s_j^2
  \prod_{k=j+1}^{n-1}(1+s_k/\tau)(1+\tau\Lambda s_k). \tag{H2}
$$
Indeed one cell differs by at most
$(A+\tau\Lambda B)s_j^2$, and KD amplifies a previous discrepancy by
at most $(1+s_j/\tau)(1+\tau\Lambda s_j)$. The empty product is one.
The analogous statement for real data with $\sum_js_j=T$ implies
$$\|z_n^{KD}-z_n^{DK}\|_\tau
 \le(A+\tau\Lambda B)T|\pi|e^{(1/\tau+\tau\Lambda)T}. \tag{H3}$$
The rational statement is intended as a finite algebraic lemma; (H3)
also uses real exponential bounds and is a separate completion step.

The existing
[GeneralForcePolygonCurve.polygonMap_uniform_convergence](https://github.com/arivero/newtonlean/blob/8138e9449b4f961c4adbebcb6090acc0d2fd5aaf/ModernLib/Polygon/GeneralForcePolygonCurve.lean)
constructs a uniformly convergent position polygon on its own binary
time and Cauchy-quotient representations, under a regional
CentralOracle, force-sampling, confinement and short-window
conditions. It is not already the general one-dimensional global
$C^{1,1}$ result in Target A: arbitrary partitions, external real-time
identification and general noncentral forces remain separate.
To connect the models one must additionally instantiate a compatible
sample oracle, identify completed coordinates and velocities with
real $q,p/m$, prove that (H2)'s bounds hold, and show the two limits
agree. The axis-embedded harmonic oscillator is a suitable special
case; general $V$ need not define an inward central force.

The
[Reverse/Classical/ClassicalTrajectory.lean](https://github.com/arivero/newtonlean/blob/8138e9449b4f961c4adbebcb6090acc0d2fd5aaf/Reverse/Classical/ClassicalTrajectory.lean)
interfaces assume localized trajectories, free dynamics, the
momentum--velocity relation and additive impulses; the
[QuantumTheory](https://github.com/arivero/newtonlean/blob/8138e9449b4f961c4adbebcb6090acc0d2fd5aaf/Reverse/Parent/QuantumKKFamily.lean)
carrier has no Hilbert-space or operator structure. Targets A--F
could provide evidence for restricted, explicitly embedded versions of
some of these interfaces. They do not automatically discharge the
interfaces for arbitrary composite bodies or prove a quantum gravity
parent. Historical Newton propositions keep their given-trajectory
premise; none of these modern targets is a historical premise.

For context only, current mathlib documentation has
[Picard--Lindelöf](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/ODE/ExistUnique.html),
[Schwartz Fourier analysis](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/SchwartzSpace/Fourier.html),
and [Brownian-motion definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/BrownianMotion/Basic.html).
Those pages are not a claim that this project has, or may import, the
needed version or all operator-theoretic results. Under the present
core-only rule, a full quantum development must construct its analytic
foundations or remain explicitly conditional; a dependency expansion
requires separate user direction. In either route, check the actual
compiled theorem types and axiom dependencies at the pinned toolchain.

## 11. Ordering at finite mesh and in the joint limit

**Result, written derivation, 2026-10-28; no priority claim.** The
ordering difference has three distinct levels: the two finite maps
are different; either order, even mixed cell by cell, reaches the
same *specified* quantum Hamiltonian when the mesh goes to zero at
fixed $\hbar$; yet their quantum vectors need not approach the same
ray along every joint $\hbar$, mesh limit. The common classical
limit of the two schemes was already established in the
[ODE lesson](balaban-ode-lesson.md), including mixed orders.

### 11.1 Fixed action and finite products

For each $\hbar>0$, use the quantum operators of §2. With
$V\in C^{1,1}$ and $V'$ globally Lipschitz, allow **either**
$D_sK_s$ or $K_sD_s$ in each cell. For every fixed $\hbar,T>0$ there
is a finite $C_{\hbar,T}$ such that every such mixed product obeys
$$
 \|S_{\hbar,\pi}^{\rm mixed}(T)f-U_\hbar(T)f\|_2
 \le C_{\hbar,T}|\pi|\,\|N_\hbar f\|_2,\quad f\in D(N_\hbar). \tag{I1}
$$
The proof swaps the kinetic and potential factors in the
[lift](lipschitz-certificate-quantum-lift.md), equations (11a)--(13).
The commutator changes sign but not norm; the same graph-growth
exponents bound both orders. Apply either local bound on each cell and
telescope along the exact orbit. Density and unitarity extend strong
convergence to all $L^2$ states. Neither (I1) nor its constant asserts
uniformity as $\hbar\to0$.

At finite $s$ the products generally differ. For a smooth subquadratic
$V$ and $f\in\mathcal S$, their second-order strong expansion is
$$
 (D_sK_s-K_sD_s)f
 =-\frac{s^2}{\hbar^2}[T_\hbar,V(Q)]f+o(s^2)
 =\frac{is^2}{2m\hbar}
       \big(P_\hbar V'(Q)+V'(Q)P_\hbar\big)f+o(s^2). \tag{I1a}
$$
The remainder is for a fixed $\hbar$ and vector; no operator-norm
Baker--Campbell--Hausdorff expansion for these unbounded operators is
asserted.

For the coherent Gaussian (1), the spread and comparison estimates
(A2) also hold with the corresponding mixed classical polygon. In a
drift-first cell, apply the kick after the drift: the force deviation
is bounded by $L$ times the position spread *after* that drift, at most
$(1+s\omega)W_j$. This gives the same upper recurrence as in the lift:
$$
 \begin{aligned}
 W_{j+1}&\le(1+s_j\omega)
          \left(1+\frac{s_jL}{m\omega}\right)W_j,\\
 e_{j+1}&\le(1+s_j\omega)
          \left(1+\frac{s_jL}{m\omega}\right)e_j+
          \frac{s_jL}{m\omega}(1+s_j\omega)W_j.
 \end{aligned} \tag{I2}
$$
Here $e_j$ is the weighted distance between quantum means and the
classical vertices using the **same** cell orders. Thus the bounds
(A2) are valid for every mixed order. The ODE lesson gives the
independent $O(|\pi|)$ classical polygon error. Both time-order
schemes therefore recover the same classical means and smooth Weyl
observable values for every joint $\hbar,|\pi|\to0$.

For a uniform step $s$ the finite classical maps are conjugate:
$$\operatorname{DK}_s
 =K_s^{\rm cl}\operatorname{KD}_s(K_s^{\rm cl})^{-1},\qquad
 (\operatorname{DK}_s)^n
 =K_s^{\rm cl}(\operatorname{KD}_s)^n(K_s^{\rm cl})^{-1}. \tag{I3}
$$
Exactly the same algebra holds for the quantum unitaries:
$(K_sD_s)^n=K_s(D_sK_s)^nK_s^{-1}$. This is not equality on the
same initial state: the conjugacy changes the endpoint
identification. It gives no single conjugator for general unequal
steps. The two first-order symplectic Euler choices and their
adjoint relation are established in the
[variational-integrator literature](https://escholarship.org/uc/item/9wm0q93j)
(symplectic Euler example read).

### 11.2 Exact distinguishability under a constant force

Fix $m,\omega,T>0$, $F\ne0$, $q_0,p_0\in\mathbb R$ and
$V(q)=Fq$. On $\mathcal H=L^2(\mathbb R)$, start both products from
the same Gaussian (1). For any positive partition write
$$
 A_\pi=\sum_js_j^2,\quad
 \Delta q_\pi=\frac{F}{m}A_\pi,\quad
 C_\pi=\frac{F^2}{2m}\sum_js_j^2(2T-t_j-t_{j+1}). \tag{I4}
$$
Let $\psi_{KD}$ use kick first in every cell and $\psi_{DK}$ use
drift first in every cell. With the $\hbar$-scaled momentum transform
$\widehat\psi(p)=(2\pi\hbar)^{-1/2}\int e^{-ipq/\hbar}\psi(q)dq$,
the **exact** relation is
$$
 \widehat\psi_{DK}(p)
 =e^{-i(C_\pi+\Delta q_\pi p)/\hbar}
   \widehat\psi_{KD}(p). \tag{I5}
$$
Consequently
$$
 \left|\langle\psi_{KD},\psi_{DK}\rangle\right|
 =\exp\!\left[-\frac{\omega F^2}{4m\hbar}A_\pi^2\right],\quad
 \inf_{\theta\in\mathbb R}
   \|\psi_{KD}-e^{i\theta}\psi_{DK}\|_2^2
 =2\!\left(1-e^{-\omega F^2A_\pi^2/(4m\hbar)}\right). \tag{I6}
$$
Indeed, in momentum space a kick sends $\widehat\psi(p)$ to
$\widehat\psi(p+Fs)$ and a drift multiplies it by
$e^{-isp^2/(2m\hbar)}$. At cell $j$, the drift momentum in the
kick-first product is $p+F(T-t_{j+1})$ and in the drift-first product
it is $p+F(T-t_j)$. Subtracting the accumulated quadratic phases gives
(I5). Both final momentum densities are Gaussian with variance
$\hbar m\omega/2$; their characteristic function gives (I6).

For the uniform partition $s=T/n$, take $\hbar_n=\kappa s^2$
with any fixed $\kappa>0$. Then $A_\pi=Ts$ and
$$
 \inf_\theta\|\psi_{KD}-e^{i\theta}\psi_{DK}\|_2^2
 =2\!\left(1-e^{-\omega F^2T^2/(4m\kappa)}\right)>0
 \quad\text{for every }n. \tag{I7}
$$
Nevertheless, both momentum means are $p_0-FT$; their position means
are $q_{\rm cl}(T)\mp F A_\pi/(2m)$, and their position and momentum
standard deviations are $O(\sqrt\hbar)$ on $[0,T]$. Thus both
families converge to the **same** classical point for every joint
schedule, while their rays can remain separated, or even become
orthogonal when $A_\pi^2/\hbar\to\infty$.

The distinction between semiclassically uniform observable accuracy and
wavefunction accuracy is itself established; see
[Fang--Qu](https://doi.org/10.1137/25M1777098) (abstract read). The
calculation here compares the two specified first-order products
directly and gives their exact overlap.

For $F\ne0$, (I6) says ray distance tends to zero exactly when
$A_\pi/\sqrt\hbar\to0$. A ray test ignores the scalar factor in (I5):
convergence of rays does not by itself control relative phase or
interference. At fixed $\hbar$, $A_\pi\le T|\pi|\to0$, and the phase
in (I5) also vanishes on the relevant state. This is a real
finite-resolution ordering effect, not a different fixed-action
continuum Hamiltonian. It complements the
[polygon phase note](cut-measure-newton.md#weyl-lifting-and-polygon-phases), which treats different
histories with matching classical endpoints and a residual scalar
phase. The present endpoints differ at finite mesh. No literature
priority is claimed for (I5)--(I7).

### 11.3 Operator ordering is a further question

The previous result assumes the **same** operator
$H_\hbar=P_\hbar^2/(2m)+V(Q)$. It does not settle factor-ordering
ambiguities when a classical Hamiltonian contains mixed functions of
position and momentum. For a concrete target, take
$f(q)=2+\cos q$, and on Schwartz space define
$$
 H_\hbar^{(1)}=\frac1{2m}P_\hbar f(Q)P_\hbar,\qquad
 H_\hbar^{(2)}
 =\frac1{4m}\big(f(Q)P_\hbar^2+P_\hbar^2f(Q)\big). \tag{I8}
$$
Both are symmetric and have the same classical symbol
$f(q)p^2/(2m)$, but the exact operator identity on Schwartz space is
$$
 H_\hbar^{(1)}-H_\hbar^{(2)}
 =\frac{\hbar^2}{4m}f''(Q)
 =-\frac{\hbar^2}{4m}\cos Q. \tag{I9}
$$
The first operator has its standard nonnegative uniformly elliptic
self-adjoint realization on $H^2(\mathbb R)$; the second is its
bounded self-adjoint perturbation by $+\hbar^2\cos Q/(4m)$. For any
Schwartz initial state the difference of their initial momentum
derivatives is $-\hbar^2\langle\sin Q\rangle/(4m)$, which need not
vanish. Thus a common classical symbol alone does not determine a
unique finite-$\hbar$ dynamics. In more general path integrals,
time-slicing and factor ordering can interact: see
[Dewey (1990)](https://doi.org/10.1103/PhysRevA.42.32) and
[Bastianelli--Schalm--van Nieuwenhuizen (1998)](https://doi.org/10.1103/PhysRevD.58.044002)
(abstracts read). No general uniqueness of the quantum lift follows.

Targets (I1)--(I9) are written proof/verification targets, not compiled
Lean theorems. Formalizing (I5)--(I7) also requires the scaled Fourier
transform, Gaussian normalization and characteristic function, and
the phase-space/ray norm conventions to be defined rather than
assumed as the conclusion.

## 12. Consequence for STATE

These targets distinguish standard inputs, repository-specific
statements and unknown publication priority. They expose a finite
classical comparison that can be attempted under newtonlean's present
rules, and the substantial analytic foundations needed for an
end-to-end quantum verification. The constant-force calculation
separates fixed-action slice independence from joint-limit
distinguishability and from operator-ordering ambiguity. The universal
lifting conjecture, positive-action necessity and the four-dimensional
gauge construction remain open.
