# Four-dimensional composition: exact Gaussian blocking and one-loop matching

**After refereeing (Claude, 2026-09-28; Fable frozen).** Theorems 1--4
ACCEPT. Theorem 2 was rederived by hand: at $K=(\kappa,0,0,0)$ only $m_2=0$
survives, $|s_b(k_1)|^2|d_1(k_1)|^2=|e^{i\kappa}-1|^2$, $P_{12,12}=|d_1|^2/q^2$ with $q^2\le12$,
and the $b^3$ aliases give (1); (8) follows from $|s_b(K_2/b)|\ge2b/\pi$ and
$q^2\le16$. Theorem 4 was checked in full: the telescoping of (17) and
$\sum_{k<n}t_k\le\alpha^{-1}\log(1+\alpha n/U)$; $2b_0=11/(8\pi^2)$ for $SU(3)$. Theorems 1 and 3
were checked at the level of their statements: the directional update
(3) composes to the sixteen-alias sum of G1, and the second-order
expansion of ${\rm Tr}\log H(\epsilon)$ and its trace-norm and Hilbert--Schmidt bounds
are standard. The sharp-blocking growth confirms the caution of G1 with
constants.

**Result, 2026-09-28 (GPT-6 Astra, round 6; written derivations).** The four directional Gaussian defects compose exactly
to the sixteen-alias kernel (5), preserving the constant-flux action
coefficient at every intermediate step. For sharp product blocking,
after $n$ isotropic steps the flux covariance satisfies

$$\frac{C_{2^n}(\kappa,0,0,0)_{12,12}}t
 \ge \frac{2^n}{12}|e^{i\kappa}-1|^2,
 \qquad 0<|\kappa|\le\pi. \tag{1}$$

Thus the proposed finite, nondegenerate Gaussian fixed point encounters
an explicit ultraviolet obstruction for these sharp observables. The
small-momentum coefficient stays $t$ at every finite depth; the two
limits fail to commute. The spatial averaging in the cited perfect
gauge action changes this conclusion's hypotheses.

At one loop, Theorem 3 proves continuity of the background determinant
in a norm on its **background Hessian jets**, with explicit bounds.
Tree-level normalization alone leaves these jets uncontrolled. Theorem 4
gives the average rate $-11\log2/(8\pi^2)$ for $SU(3)$ under sublinear
endpoint matching and a sublinear accumulated remainder. The missing
estimate is a uniform bound on the continuum-subtracted contraction of
the generated cubic and quartic vertices, including its infrared
limit. Even the stronger kernel-convergence route is obstructed by (1)
for the prescribed sharp map. Bounded matching itself remains open.

**Inputs and scope.** [G1](gaussian-blocking-coupling.md) was refereed
first, with dated refinements in that note. We use the
[series/parallel note](series-parallel-gauge-refinement.md), Prop. 2 and
Cor. 2$_s$; [round 4](four-dimensional-parallel-log.md), §§5--8,
especially (12), (15) and the many-steps remark; and the finite
$\Lambda$ matching in the [zero-spacing note](zero-spacing-any-action.md)
(full-read: these sections). Gaussian claims below are exact finite
lattice algebra and bulk momentum estimates. Interacting matching is
formal perturbation theory with its further hypotheses stated.
Continuum construction and a physical spectral gap remain separate
obligations. Throughout $t=g^2=\hbar g_{\rm cl}^2$ and
$b_0=11N/(48\pi^2)$ for pure $SU(N)$.

## 1. The directional defect with three transverse planes

Fix a cut direction $r$ and write $\Phi_\ell$ for the column of the
three transverse face fluxes. Let $C_\perp(k)$ be the transverse curl
from three edges to these three faces,
$(C_\perp\xi)_{jk}=d_j\xi_k-d_k\xi_j$, $d_j=e^{ik_j}-1$.
Use the geometric coarse heat times and put

$$\begin{gathered}
 T=\operatorname{diag}_{j<k,\ j,k\ne r}(t_{jk}),\quad
 E=\operatorname{diag}_{j\ne r}(t_{rj}),\quad \sigma=s(1-s),\\
 V_s=\sigma C_\perp E C_\perp^*,\quad R_s=2T+V_s,\quad
 \bar\Phi_\ell=(1-s)\Phi_\ell+s\Phi_{\ell+1}.
\end{gathered}$$

All matrices are per colour. For positive heat times $R_s\ge2T>0$,
even though the curl has a kernel. The Gaussian bridge has covariance
$\sigma E$; convolution of its face curl with the mid-face weight
replaces $2T$ by $R_s$. Subtracting the reference coarse action gives,
up to a flux-independent determinant,

$$\begin{aligned}
 \mathcal D_r
 &=\sum_{\ell,k}\left[
 \tfrac12\bar\Phi_\ell^*R_s^{-1}\bar\Phi_\ell
       -\tfrac14\Phi_\ell^*T^{-1}\Phi_\ell\right]\\
 &=-\tfrac12\sum_{\ell,k}\Phi_\ell^*
       [(2T)^{-1}-R_s^{-1}]\Phi_\ell
   -\tfrac\sigma2\sum_{\ell,k}(\Phi_{\ell+1}-\Phi_\ell)^*
       R_s^{-1}(\Phi_{\ell+1}-\Phi_\ell)\le0.
\end{aligned}\tag{2}$$

The weighted parallelogram identity and periodicity prove the second
line, without commuting $T$ and $V_s$. For a single transverse plane
this is precisely Prop. 2 / Cor. 2$_s$. At constant flux, $V_s(0)=0$
and $\Phi_{\ell+1}=\Phi_\ell$, so (2) vanishes exactly.

Equation (2) gives each *reference* defect. The next elimination uses
the whole effective quadratic form. This is implemented below by
successive Schur complements, the Gaussian specialization of round
4's (12).

## 2. The composed momentum kernel

Use a periodic lattice whose side lengths are divisible by the total
block factor; remove gauge and flat-link modes. Work at nonzero
momentum on the exact flux subspace. Bulk limits below are taken first
at each fixed block depth. With orthonormal oriented face components,
define

$$\begin{gathered}
 (d_1(k)A)_{\mu\nu}=d_\mu A_\nu-d_\nu A_\mu,
 \quad q(k)^2=\sum_\mu|d_\mu|^2,\\
 P(k)=\frac{d_1(k)d_1(k)^*}{q(k)^2},\qquad C_1(k)=tP(k).
\end{gathered}$$

The nonzero singular values of $d_1$ are $q$, proving the projector
formula. In particular $P_{\mu\nu,\mu\nu}=(|d_\mu|^2+|d_\nu|^2)/q^2$.

**Theorem 1 (four Schur complements, exact).** Let $\mathcal T_r$ act
on the current covariance by

$$\begin{aligned}
 (\mathcal T_r C)(K)&=\tfrac12\sum_{\epsilon=0}^1
 F_r(k^{\epsilon})C(k^{\epsilon})F_r(k^{\epsilon})^*,\\
 k^{\epsilon}_r&=K_r/2+\pi\epsilon,\quad k^{\epsilon}_j=K_j\ (j\ne r),\\
 (F_r)_{\mu\nu,\mu\nu}(k)&=
 \begin{cases}1+e^{ik_r},&r\in\{\mu,\nu\},\\1,&r\notin\{\mu,\nu\}.
 \end{cases}
\end{aligned}\tag{3}$$

At every stage the precision is the inverse covariance on its exact
range. Equivalently, after writing the gauge-reduced action in retained
variables $x$ and eliminated variables $y$, its update is

$$Q_{\rm next}=Q_{xx}-Q_{xy}Q_{yy}^{-1}Q_{yx}. \tag{4}$$

After all four directions, in any order,

$$\boxed{\begin{gathered}
 C_2(K)=\frac t{16}\sum_{\nu\in\{0,1\}^4}
 F(k_\nu)P(k_\nu)F(k_\nu)^*,\quad k_\nu=K/2+\pi\nu,\\
 F_{\mu\nu,\mu\nu}(k)=(1+e^{ik_\mu})(1+e^{ik_\nu}),\qquad
 Q_2(K)=\left.C_2(K)\right|_{\operatorname{im}d_1(K)}^{-1}.
\end{gathered}} \tag{5}$$

Here the alias multi-index in the sum is separate from face indices.
If $Q_2$ is extended by zero off the exact range, the effective action
is $\tfrac12\sum_K\Phi(K)^*Q_2(K)\Phi(K)$, and the coarse link Hessian
is $d_1(K)^*Q_2(K)d_1(K)$. Formula (5) is an explicit lattice-momentum
expression for the nested complements (4), retaining every generated
quadratic interaction.

*Proof.* The factor $1/2$ in (3) is the squared unitary Fourier
normalization for decimation in one direction. Stokes supplies its
face factor. Gaussian pushforward gives $BCB^*$; completing the square
gives (4). The finite gauge-reduced integrals satisfy Fubini. Multiplying
the directional factors and the four normalizations yields (5).
All intermediate conditional precisions are positive on the integrated
subspaces. $\square$

**Constant-flux preservation at every intermediate step.** Adjoin a
harmonic background $F_{\mu\nu}$, or use twisted affine boundary data,
with its Maxwell action. On a lattice with side lengths $a_\mu$ the
constant flux is $\Phi_{\mu\nu}=a_\mu a_\nu F_{\mu\nu}$ and
$t_{\mu\nu}=t a_\mu^2a_\nu^2/\prod_\rho a_\rho$. Consequently

$$\frac12\sum_{x,\mu<\nu}\frac{|\Phi_{\mu\nu}|^2}{t_{\mu\nu}}
 =\frac{V_{\rm phys}}{2t}\sum_{\mu<\nu}|F_{\mu\nu}|^2. \tag{6}$$

Constant fine flux is orthogonal in this action to every periodic
exact fluctuation: the sum of a curl is zero. Blocking fixes its
harmonic component. It is therefore the constrained minimizer for
constant coarse data at every intermediate elimination, including
those starting with a generated action. This proves (6) survives each
of the four steps. For nonzero momenta, G1 gives the corresponding
isotropic limit $C_2(K)=t[P_{\rm cont}(\hat K)+O(K^2)]$ in centred
phases. Periodic exact forms alone have zero harmonic flux; (6)
specifies the extension used to speak of a constant-flux coefficient.

## 3. Iteration: an explicit sharp-blocking obstruction

After $n$ steps let $b=2^n$ and define

$$\begin{gathered}
 s_b(z)=\sum_{j=0}^{b-1}e^{ijz},\quad
 F_b(k)_{\mu\nu,\mu\nu}=s_b(k_\mu)s_b(k_\nu),\\
 k_m=(K+2\pi m)/b,\quad m\in\{0,\ldots,b-1\}^4,\\
 C_b(K)=t b^{-4}\sum_m F_b(k_m)P(k_m)F_b(k_m)^*,\qquad
 Q_b=(C_b|_{\operatorname{im}d_1(K)})^{-1}. \tag{7}
\end{gathered}$$

Composition of sums along links proves (7) directly. Each finite $b$
has the same leading small-momentum coefficient $t$, by G1.

**Theorem 2 (growth with explicit constants).** The covariance (7)
satisfies (1). More generally, for $K\in(-\pi,\pi]^4$ with $K_1\ne0$,

$$C_b(K)_{12,12}/t\ \ge\ \frac{b}{4\pi^2}|e^{iK_1}-1|^2. \tag{8}$$

It therefore diverges on sets of positive momentum measure and in
every $L^p$ operator norm, $1\le p\le\infty$. No finite covariance
limit exists in these norms. On the axis of (1),
$\|Q_b(K)\|\le12/[tb|e^{i\kappa}-1|^2]$, so uniform convergence to a
nondegenerate precision also fails.

*Proof.* At $K=(\kappa,0,0,0)$ only $m_2=0$ survives in the 12
diagonal. Since $s_b(0)=b$ and
$|s_b(k_1)|^2|d_1(k_1)|^2=|e^{i\kappa}-1|^2$,

$$C_b(K)_{12,12}/t
 =b^{-2}|e^{i\kappa}-1|^2
 \sum_{m_1,m_3,m_4}\frac1{q(k_m)^2}
 \ge b|e^{i\kappa}-1|^2/12.$$

Here $q^2\le12$, since $k_2=0$. Off-diagonal entries among 12, 13,
14 vanish: shared support forces the other two transverse momenta to
zero, and their projector cross entry then vanishes. By transverse
symmetry these three diagonal entries agree. They span the exact
subspace on this axis, giving the precision bound.

For (8), keep just the $b^3$ aliases with $m_2=0$ in the positive
diagonal sum. Use $P_{12,12}\ge |d_1|^2/q^2$, $q^2\le16$, and

$$|s_b(K_2/b)|
 =\frac{|\sin(K_2/2)|}{|\sin(K_2/(2b))|}\ge\frac{2b}{\pi},$$

with its continuous value at $K_2=0$. Cancellation of $|d_1|^2$ gives
$b^{-4}b^3|e^{iK_1}-1|^2(4b^2/\pi^2)/16$, which is (8).
For example on $\pi/2\le K_1\le\pi$, the bound is
$tb/(2\pi^2)$; this set has normalized Brillouin measure $1/4$.
Thus $\|C_b\|_{L^p}\ge tb(1/4)^{1/p}/(2\pi^2)$, with exponent zero
for $p=\infty$. $\square$

This calculation identifies the ultraviolet boundary fluctuations of
a sharp plaquette surface. It also shows why G1's remainder constants
cannot be uniform in $b$. Taking $K\to0$ first keeps the Maxwell
coefficient; taking $b\to\infty$ at fixed nonzero axial $K$ sends the
precision to zero. A topology which controls a finite nondegenerate
propagator and its inverse cannot supply the proposed fixed point.
Possible degenerate precision limits alone would be insufficient for
one-loop determinant continuity.

**Relation to the cited fixed points.** Bell--Wilson's
[finite-lattice Gaussian RG](https://doi.org/10.1103/PhysRevB.11.3431)
(metadata and abstract checked) supplies the general framework.
Bietenholz--Wiese's [§3, equations (3.1)--(3.6)](https://arxiv.org/pdf/hep-lat/9510026)
(passage; DOI [verified](https://doi.org/10.1016/0550-3213(95)00678-8))
averages the continuum gauge field over adjoining hypercubes, with
form factor $\Pi_\mu(p)=(\widehat p_\mu/p_\mu)\prod_\rho
(\widehat p_\rho/p_\rho)$. Their delta constraint fixes this spatial
average exactly. Sending the constraint's Gaussian width to zero
retains the transverse averaging. Our link product samples a sharp
line, and (7) has no such transverse factors. The distinction explains
why that delta limit supplies no convergence theorem for (7).

## 4. A one-loop continuity theorem with the necessary norm

Let $\mathcal K_n$ denote the full dimensionless action shape, including
vertices and any one-loop local terms, and $\zeta_n$ its anisotropy.
At isotropic endpoints $\zeta_n=1$. Fix the common background scheme of
round 4. In that scheme, the weakest scalar boundedness requirement is
$\sup_n|c(\zeta_n,\mathcal K_n)|<\infty$; compactness of all action
parameters is stronger than necessary. For the average rate even this
can be relaxed to sublinear endpoint differences (Theorem 4).

Here is a useful sufficient condition directly on the determinant.
Introduce a common infrared regulator and finite volume, remove zero
modes consistently, and normalize a smooth external background
$\epsilon\mathcal B$ so its classical action per volume is
$u\epsilon^2/2$. All background differentiation below is at fixed
regulator, boundary prescription and lattice. Write the positive
vector and ghost Hessians as

$$H_{j,n}(\epsilon)=H_{j,n}+\epsilon V_{j,n}
                  +\epsilon^2 W_{j,n}+O(\epsilon^3),\quad j=1,0.$$

These are full operators, allowing momentum transfer by the
background. Define their relative jets

$$A_{j,n}=H_{j,n}^{-1/2}V_{j,n}H_{j,n}^{-1/2},\qquad
 E_{j,n}=H_{j,n}^{-1/2}W_{j,n}H_{j,n}^{-1/2}. \tag{9}$$

Use trace per lattice volume $\tau$. Set
$\|X\|_{1,\tau}=\tau|X|$ and
$\|X\|_{2,\tau}^2=\tau(X^*X)$; these include colour and vector indices.
Let $m_n$ contain the measure, constraint Jacobian and explicitly
supplied local contributions in this normalization.

**Theorem 3 (regulated background determinant).** Its inverse-coupling
coefficient is

$$c_n^{\rm reg}=\tau\left(E_{1,n}-\tfrac12A_{1,n}^2
                       -2E_{0,n}+A_{0,n}^2\right)+m_n. \tag{10}$$

If uniformly in $n$, $\|E_{j,n}\|_{1,\tau}\le M_{E,j}$,
$\|A_{j,n}\|_{2,\tau}\le M_{A,j}$ and $|m_n|\le M_m$, then

$$|c_n^{\rm reg}|\le M_{E,1}+\tfrac12M_{A,1}^2
                      +2M_{E,0}+M_{A,0}^2+M_m. \tag{11}$$

Convergence of $E_j$ in trace norm, $A_j$ in this Hilbert--Schmidt
norm, and $m_n$ implies convergence of $c_n^{\rm reg}$. Explicitly,
for two shapes $n,l$,

$$\begin{aligned}
 |c_n^{\rm reg}-c_l^{\rm reg}|\le{}&
 \|E_{1,n}-E_{1,l}\|_{1,\tau}
 +\tfrac12(\|A_{1,n}\|_{2,\tau}+\|A_{1,l}\|_{2,\tau})
          \|A_{1,n}-A_{1,l}\|_{2,\tau}\\
 &+2\|E_{0,n}-E_{0,l}\|_{1,\tau}
 +(\|A_{0,n}\|_{2,\tau}+\|A_{0,l}\|_{2,\tau})
          \|A_{0,n}-A_{0,l}\|_{2,\tau}+|m_n-m_l|.
\end{aligned}\tag{12}$$

*Proof.* Expand $\operatorname{Tr}\log H(\epsilon)$: its
$\epsilon^2$ coefficient is
$\operatorname{Tr}(H^{-1}W-\tfrac12H^{-1}VH^{-1}V)$.
Use $\Gamma_1=\tfrac12\log\det H_1-\log\det H_0$ and multiply by
2 to extract the coefficient of $u\epsilon^2/2$. Cyclicity proves
(10). Trace Hölder and
$|\tau(A^2-B^2)|\le(\|A\|_{2,\tau}+\|B\|_{2,\tau})
\|A-B\|_{2,\tau}$ prove (11)--(12). $\square$

For example, a family of background quadratic operators with
$H_j\ge\gamma I$, $\|V_j\|\le v_j$, $\|W_j\|\le w_j$, and
$d_j$ components per site obeys (11) with
$M_{E,j}=d_jw_j/\gamma$ and
$M_{A,j}=\sqrt{d_j}v_j/\gamma$. In four dimensions
$d_1=4(N^2-1)$ and $d_0=N^2-1$ (32 and 8 for $SU(3)$).
Operator-norm convergence of these three jets with the same positive
$\gamma$ proves convergence at fixed regulator. This is an actual
continuity theorem for a specified Gaussian-plus-background family.
The positive bridge mass in a single pristine elimination provides
such fixed-step control. Maintaining it and the jet bounds after
arbitrarily many generated eliminations is a further requirement.

**Removing regulators and extracting $F^2$.** In the massless problem
the individual terms in (11) can diverge with the regulator. Let
$\mathcal J_n(k;\rho)$ be the combined vector, ghost and measure
integrand for the $F^2$ coefficient, with the same continuum infrared
subtraction at every $n$. Here $\rho$ collectively denotes the
infrared and external-momentum regulators; the bulk limit is already
taken. Assume the background Ward identities and the extraction of
this integrand, including the external-momentum derivatives, are
valid. Write

$$c_n=c_{\rm ref}+\lim_{\rho\to0}
       \int_{\mathcal B_4}\mathcal J_n(k;\rho)\,
                         \frac{d^4k}{(2\pi)^4}. \tag{13}$$

The concrete sufficient boundedness condition is

$$\sup_{n,\rho}\int|\mathcal J_n(k;\rho)|\,
             \frac{d^4k}{(2\pi)^4}\le M, \tag{14}$$

together with existence of each limit in (13). It gives
$|c_n|\le |c_{\rm ref}|+M$. A common integrable envelope, pointwise
regulator limits and convergence of $\mathcal J_n$ to a limit
uniformly in $\rho$ in $L^1$ imply $c_n\to c_*$ by dominated
convergence. Condition (14) permits cancellations within the combined
integrand and is weaker than bounding every unrenormalized jet norm.
Bounded scalar integrals can also occur without (14); we claim (14)
as a sufficient analytic criterion, not a necessary one.

At the background level, Schur complements give an additional exact
finite-depth identity:

$$\Gamma_1[H]=\Gamma_1[H_{yy}]
                    +\Gamma_1[H/H_{yy}], \tag{15}$$

separately for vectors and ghosts with their stated weights, and with
any measure terms retained. Differentiate this determinant identity
twice before removing regulators. All four updated Hessians compose
exactly. Equation (15) controls bookkeeping through Gaussian
background elimination; it supplies no depth-uniform estimate for
(14). Sharp blocking's Theorem 2 obstructs an argument based just on
convergence to a uniformly invertible zero-background kernel.

## 5. The generated vertices that still need control

In (9), $V$ contains the vertex with two quantum legs and one external
background leg; $W$ contains two quantum and two background legs.
Thus (10) contains the cubic bubble and quartic tadpole, as well as
the ghost and measure terms. For a spatially varying background the
products in (10) are operator products. Their momentum expansion
includes the orbital terms that a pointwise matrix determinant would
miss.

At one loop higher tree vertices cannot enter the term with two
external legs: the loop and leg counts force either two cubic vertices
or one quartic vertex. Generated one-loop two-leg terms must be
carried explicitly in $m_n$. A sufficient missing estimate is control
of (9) in the norms of Theorem 3 after the common subtraction, or
directly (14), **uniform in depth and volume and through the
external-momentum/infrared limits**. This includes bounds for the
external derivatives selecting $F^2$, the ghost vertices and the
background dependence of the blocking constraint. Ward identities
fix the allowed leading structure; the finite integrals need this
additional quantitative estimate.

The freedom left by the quadratic kernel is concrete. In local
near-identity plaquette coordinates $X_p=\log U_p$, the gauge-invariant
term $\eta\sum_p|X_p|^4$ has zero quadratic and cubic part at the
trivial field. Around $X=\epsilon B+f$, its quadratic fluctuation part
at order $\epsilon^2$ is

$$\eta\epsilon^2\bigl(2|B|^2|f|^2+4\langle B,f\rangle^2\bigr). \tag{16}$$

For $\eta>0$ this gives a positive nonzero Gaussian tadpole. One can
vary $\eta$ while preserving the zero-field quadratic kernel exactly.
Smooth gauge-invariant continuations away from the identity have the
same Taylor coefficients. This demonstrates why kernel convergence,
even if supplied by a different blocking, needs a controlled
background completion before it implies continuity of $c$. Equation
(16) describes allowed action shapes; it makes no claim that this
particular $\eta_n$ is generated along our trajectory.

Theorem 2 likewise establishes neither boundedness nor growth of
$c_n$: vector/ghost/vertex cancellations could still control (14)
despite a divergent sharp-flux covariance. Estimating that combined
quantity, or modifying the observables to a spatially averaged
blocking and proving its vertex estimates, are the two concrete next
routes.

## 6. Average running and finite scale matching

**Theorem 4 (conditional average, with remainder).** Consider $n$
isotropic coarsenings, retaining the full generated actions. Assume
round 4's background-matching hypotheses at each step, including no
extra massless modes and the common definition of the coupling. Put
$c_k=c(\zeta_k,\mathcal K_k)$ and assume

$$u_{k+1}-u_k=-2b_0\log2+c_k-c_{k+1}+r_k,
 \qquad |r_k|\le A t_k \tag{17}$$

with a common finite $A$. Then

$$\left|\frac{u_n-u_0}{n}+2b_0\log2\right|
 \le\frac{|c_0-c_n|}{n}+\frac A n\sum_{k<n}t_k. \tag{18}$$

In particular, $|c_0-c_n|=o(n)$ and $\sum_{k<n}t_k=o(n)$ imply the
universal average. Bounded $|c_k|\le C$ gives $2C/n$ for the first
term; boundedness is sufficient and strictly stronger than sublinear
growth. Formal one-loop truncation sets $r_k=0$.

For an explicit weak-coupling remainder bound, assume a family of
trajectories with increasingly fine initial lattices and

$$t_k\le\frac1{U+\alpha(n-k)},\qquad
 U>0,\quad\alpha>0,\quad 0\le k<n, \tag{19}$$

where $U,\alpha,A$ are independent of $n$. Then

$$\sum_{k<n}t_k\le\frac1\alpha\log(1+\alpha n/U),\qquad
 \left|\frac{u_n-u_0}{n}+2b_0\log2\right|
 \le\frac{2C}{n}+\frac A{\alpha n}\log(1+\alpha n/U). \tag{20}$$

*Proof.* Sum (17); all intermediate $c_k$ cancel. For (20), bound the
decreasing sum $\sum_{j=1}^n(U+\alpha j)^{-1}$ by its integral from
0 to $n$. $\square$

For $SU(3)$, $2b_0=11/(8\pi^2)$, so the average is
$-11\log2/(8\pi^2)$. At leading matched one-loop order the expected
value of $\alpha$ is $2b_0\log2$; (19) is an explicit extra hypothesis
for controlling the remainders. An infinite coarsening from a fixed
initial coupling eventually leaves weak coupling. The limit in (20)
uses trajectories with increasingly weak initial coupling and a weak
final endpoint, as in the many-steps remark. If the initial shapes
also vary, the requirement is the endpoint difference in (18), rather
than a statement about $c_n$ alone. No running approximation is used
to prove the bound that is supposed to justify it.

Finally, $u_B=u_A+d$ at the same scale gives
$\Lambda_B/\Lambda_A=e^{-d/(2b_0)}$ at one loop. For
$u_{\rm matched}=u+c_n$, this reads
$\Lambda_{\rm matched}/\Lambda_{\rm bare,n}=e^{-c_n/(2b_0)}$.
Thus a bounded matching family has finite scale ratios in
$[e^{-C/(2b_0)},e^{C/(2b_0)}]$. This is the action-shape version of the
finite $\Lambda$ matching in the zero-spacing note. Defining the
matched coupling absorbs the endpoint terms by definition; identifying
the bare blocked coupling's average still requires (18).

## 7. Round 10: the first generated vertices (formal, unrefereed)

**One pristine isotropic midpoint step, GPT-6 Astra, 2026-09-28.**
The following are coefficients of the zero-image expansion in $t$;
the bounds concern those coefficients, uniformly in spatial volume.
Use dimensionless links, periods at least three, and the mid-vertex
gauge of [Proposition 1](series-parallel-gauge-refinement.md) (passage).
Write the transported bridge endpoints as $e^{a_e},e^{b_e}$ and the
mid-link as $e^{y_e}$. The dimensionless classical action for $-\log\Psi$
is the stationary value in $y$ of

$$\begin{aligned}
s(x,y)={}&\sum_e\bigl(|\log(e^{-a_e}e^{y_e})|^2+
 |\log(e^{-y_e}e^{b_e})|^2-\tfrac12|\log(e^{-a_e}e^{b_e})|^2\bigr)
 &+\tfrac14\sum_p|\log\prod_{e\in\partial p}e^{\epsilon_{pe}y_e}|^2,
 \qquad x=(a,b).
\end{aligned}\tag{21}$$

The contribution to the action is $s_*/t$. Old transverse weights and
the coarse electric action are added separately to obtain the full
blocked action. For original coarse links, substitute the paths
$e^a=P$, $e^b=Q^{-1}$ from Proposition 1 before taking coefficients;
this also retains the background dependence of the constraint.

Here is an explicit finite-word prescription for every lattice kernel.
For an ordered word with signed letters $z_1,\ldots,z_m$, $m\le4$, set

$$\begin{gathered}
 E_r=\sum_{n_1+\cdots+n_m=r}\frac{z_1^{n_1}\cdots z_m^{n_m}}{n_1!\cdots n_m!},\quad
 F_1=E_1,\quad F_2=E_2-\tfrac12E_1^2,\\
 F_3=E_3-\tfrac12(E_1E_2+E_2E_1)+\tfrac13E_1^3,\\
 p_2=|F_1|^2,\quad p_3=2\langle F_1,F_2\rangle,\quad
 p_4=|F_2|^2+2\langle F_1,F_3\rangle. \tag{22}
\end{gathered}$$

Use the invariant metric $|X|^2=-2\operatorname{tr}X^2$ on $\mathfrak{su}(N)$.
In each term of (21) replace the squared logarithm by $p_r$, with its
displayed weight, obtaining $s_r$. Define the symmetric kernels
$Q=\partial^2s_2$, $T=\partial^3s_3$, $U=\partial^4s_4$ at zero.
Thus (22), signed face incidences and finite sums specify all colour
and position indices, without an implicit interacting expectation.
Put $H=Q_{yy}=4I+C^*C/2$, $G=H^{-1}$, $B=Q_{yx}$ and
$Lx=(x,-GBx)$; in endpoint coordinates $Bx=-2(a+b)$.
The generated kernels are

$$\begin{aligned}
 (\Gamma_3)_{ijk}&=\sum_{ABC}T_{ABC}L_{Ai}L_{Bj}L_{Ck},\\
 Z_{e,ij}&=\sum_{AB}T_{eAB}L_{Ai}L_{Bj},\\
 (\Gamma_4)_{ijkl}&=\sum_{ABCD}U_{ABCD}L_{Ai}L_{Bj}L_{Ck}L_{Dl}
 -\sum_{ef}G_{ef}(Z_{e,ij}Z_{f,kl}+Z_{e,ik}Z_{f,jl}+Z_{e,il}Z_{f,jk}).
\end{aligned}\tag{23}$$

Here repeated mid-edge indices include the colour pairing. The vertices
are $\Gamma_3[x^3]/6$ and $\Gamma_4[x^4]/24$; their background Hessian
jets are $V=\Gamma_3[\mathcal B,\cdot,\cdot]$ and
$W=\Gamma_4[\mathcal B,\mathcal B,\cdot,\cdot]/2$.
Indeed $y=-GBx-GZ[x,x]/2+O(x^3)$; substituting into $s_2+s_3+s_4$
gives the exchange contribution $-\langle Z[x,x],GZ[x,x]\rangle/8$.

**Explicit size and decay.** Let $d$ be distance between edges in the
graph joining edges of a common spatial face, attaching endpoint
variables to their corresponding mid-edge. Since $4I\le H\le10I$,
the Neumann series about $7I$ gives
$\|G_{ef}\|\le(3/7)^{d(e,f)}/4$. This is the three-dimensional version
of [Lemma 1](su2-midplane-small-field.md) (passage). Put

$$\alpha=\tfrac12\log(7/3),\quad q=\sqrt{3/7},\quad
 g=48\frac{1+4q+q^2}{(1-q)^4},\quad
 K=2^{40}(1+N)^4e^{6\alpha},\quad l=1+gK. \tag{24}$$

Use the anchored kernel norm: fix any one argument, sum the operator
norm over all other edge arguments, with weight $e^{\alpha\mathsf T}$,
where $\mathsf T$ is the shortest connecting tree length. The same
definition for matrices includes both row and column sums. Then

$$\|G\|_\alpha\le g,\quad \|B\|_\alpha,\|T\|_\alpha,\|U\|_\alpha\le K,
 \quad \|\Gamma_3\|_\alpha\le Kl^3=:v_3,\quad
 \|\Gamma_4\|_\alpha\le(K+3K^2g)l^4=:v_4. \tag{25}$$

For the first bound, a radius-$n$ edge ball has at most $3(4n+3)^3$
members; sum $\frac34\sum_n(4n+3)^3q^n\le g$. For the local bounds,
the absolute word-coefficient sums in (22) are at most $8^r$ for
$r\le3$; multiplication, the derivative factor $4!$, the weights
in (21), and at most 24 incident words are covered by $K$. The same
constant covers the length-three endpoint paths after substitution.
Tree lengths are subadditive when kernels are joined, proving (25)
from (23). In particular each kernel is bounded by $v_r e^{-\alpha\mathsf T}$.
These are deliberately loose constants; $t^{-1}$ restores action units.

**After refereeing §7 (Claude, 2026-09-28).** Formal statements
ACCEPT. Checked: the Neumann bound $\|G_{ef}\|\le\frac14(3/7)^{d}$ from $4I\le H\le10I$
($C^*C\le12$ in the three-dimensional mid-space); the identity (28) as the
Schur-complement factorization $\log\det\mathcal H=\log\det D+\log\det(\mathcal H/D)$, which
confines the one-step subtracted change to the eliminated block; the
cancellation of the common massless $F^2$ logarithm in (28); and the
arithmetic of (30), $D_*=3(16+448+8192+49152)=173424$. The constants in
(24)--(31) are deliberately loose and finite; §7.2 is a fair conditional
statement. Checked at the level of structure, with the Schur-test bounds
(27) taken on trust.

### 7.1. Part (2): one-loop contraction after common subtraction (formal)

The contraction uses the **full** blocked tree action: add the old-face
and electric terms to (23), including cross bubbles with their cubic
vertices. Use the same gauge reduction, background and physical units
on both sides of the cut. The following bounds concern one pristine
step; all coefficients are bulk, zero-image perturbative coefficients.

First take a bounded background $\mathcal B$, with
$b=\sup_e|\mathcal B_e|$, and set $z=L\mathcal B$,
$h=-GT_y[z,z]/2$. At its conditional saddle the eliminated Hessian is

$$D(\epsilon)=H+\epsilon V_D+\epsilon^2W_D+O(\epsilon^3),\qquad
 V_D=T_{yy}[z],\quad W_D=\tfrac12U_{yy}[z,z]+T_{yyy}[h]. \tag{26}$$

The anchored bounds (25) and the Schur test give, with $d=3(N^2-1)$,

$$\begin{gathered}
 v=Kl b,\qquad w=\tfrac12(K+gK^2)l^2b^2,\\
 \|D^{-1/2}V_DD^{-1/2}\|_{2,\tau}\le\sqrt d\,v/4,\qquad
 \|D^{-1/2}W_DD^{-1/2}\|_{1,\tau}\le d w/4,\\
 |\tau(E_D-A_D^2/2)|\le d(w/4+v^2/32). \tag{27}
\end{gathered}$$

Here $D=H$ at zero background and $\tau$ is per mid-space site
(one mid-space per slab). These are precisely Theorem 3's norms,
uniform in volume and in an added nonnegative mass regulator.
The saddle term $T_{yyy}[h]$ retains the exchange term in (23).

For clarity about the subtraction, let $\mathcal H$ be the pristine
Hessian in retained/eliminated coordinates, evaluated on this saddle,
and $S=\mathcal H/D$ the full blocked tree Hessian. Differentiation of
the stationary action gives $S$ exactly, including its cubic/quartic
jets. With $\mathcal C(H)=\tau(E_H-A_H^2/2)$, determinant factorization
at fixed regulator gives

$$\mathcal C(S)-\mathcal C(\mathcal H)=-\mathcal C(D). \tag{28}$$

In the mid-vertex gauge the eliminated gauge volume has already been
removed. A background-gauge implementation must include its ghost and
constraint determinants in (28); their net contribution is the same
reduced integral. Local heat-kernel and Haar amplitudes are kept in
$m$, as in (10). Subtract the **same** continuum determinant from both
massless sides of (28), before taking their difference. Thus (27)
bounds the determinant part of the subtracted one-step change. The
retained massless $A_S,E_S$ can separately have divergent norms;
(28) controls their combined contraction and subtraction. Isolated
diagrams built only from $\Gamma_3,\Gamma_4$ have no such assertion.

To extract $F^2$ with explicit constants, use the constant commuting
flux tests of [the one-step note, Theorem 1](four-dimensional-parallel-log.md)
(full-read: §§1--5). They are stationary interpolated backgrounds, so
(28) applies without a background field redefinition. Its magnetic
symbol includes the orbital terms needed for this extraction; (27)
alone, with a bounded potential, would leave that issue unresolved.
Here is an explicit bound on that note's integral $\mathcal I_{jk}$.
In its (6)--(8), at $M=4I,W=I/2$, put $a_*=64$, $r=(4+v)^{-1}$.
The absolute trigonometric coefficient row sums bound $H_1,H_2$,
the first two momentum derivatives of $H_0$, and the first momentum
derivatives of $H_1$ by $a_*$. The inverse derivative identities give

$$\begin{aligned}
 \|\partial R_0\|&\le a_*r^2,&
 \|\partial^2R_0\|&\le a_*r^2+2a_*^2r^3,\\
 \|R_1\|&\le a_*r^2+a_*^2r^3,&
 \|\partial R_1\|&\le a_*r^2+4a_*^2r^3+3a_*^3r^4,\\
 \|R_2\|&\le a_*r^2+\tfrac72a_*^2r^3+6a_*^3r^4+3a_*^4r^5.
\end{aligned} \tag{29}$$

Each $\partial$ is either magnetic momentum derivative; mixed second
derivatives obey the same bound. For example the two Poisson products
cancel the factor $1/2$ in an absolute bound, while the four second
derivative products give $4/8$ in the last term of (8).
Integrating (29), using $|\operatorname{tr}_3R_2|\le3\|R_2\|$, gives

$$|\mathcal I_{jk}|\le D_*:=3\left(
 \frac{a_*}{4}+\frac{7a_*^2}{64}+\frac{a_*^3}{32}
 +\frac{3a_*^4}{1024}\right). \tag{30}$$

For a unit flux in any one plane the full normalized conditional
one-loop coefficient $d_{\mu\nu}=2A_{\mu\nu}$ therefore satisfies

$$|d_{1j}|\le N/48,\qquad
 |d_{jk}|\le N(1/24+D_*)=:D_N. \tag{31}$$

These constants include the bridge normalization and the transverse
heat-kernel amplitude $-N/24$ in the inverse coupling. In a common
scheme at the same physical scale, (28), with these local terms,
says $c_{\rm blocked}^{\rm tree}=c_{\rm pristine}-d_{\mu\nu}$ for
the selected plane coefficient. Thus its finite matching change is
bounded by $D_N$ ($3(1/24+D_*)$ for $SU(3)$); in an arbitrary fixed
scheme $|c_{\rm blocked}^{\rm tree}|\le|c_{\rm pristine}|+D_N$.
One may fix the common finite subtraction by $c_{\rm pristine}=0$.
The pristine continuum-subtracted coefficient and Ward extraction
are understood in the formal matching scheme of the one-step note.
Keeping the generated one-loop local term adds $d_{\mu\nu}$ back,
as required by exact integration. Changing the physical matching scale
also adds the universal logarithm; (31) uses equal scales throughout.

**Infrared term.** The common massless $F^2$ logarithm has coefficient
$2b_0=11N/(24\pi^2)$; it cancels in (28). The surviving transverse
bridge density at $k=0$ is
$-N/24-N\operatorname{Re}\int_0^\infty\operatorname{tr}_3R_2(0,v)\,dv$.
It controls the leading small-ball contribution, bounded by
$D_N\varepsilon^3/(6\pi^2)$ for $|k|<\varepsilon\le1$.
The cut density vanishes quadratically and contributes at most
$N\varepsilon^5/(2304\pi^2)$, since $Q\le|k|^2$ and $8+Q\ge8$.
Equation (29) supplies domination through the infrared limit, including
the orbital response. This proves finite one-step matching within the
stated formal scheme; depth-uniform (14) remains the next estimate.

### 7.2. Part (3): the uniform iteration requirement (conditional)

To iterate [recursion (12)](four-dimensional-parallel-log.md) uniformly,
each **updated** action, in rescaled lattice units, must have a conditional
Hessian $D_n\ge\gamma I$ and anchored bounds (25) with common positive
$\gamma,\alpha$ and finite $g,K,l$, including the constraint's background
jets; anisotropies must remain bounded above and away from zero. Ghosts,
Jacobians and generated one-loop local terms must be carried in the same
Ward-compatible scheme. These hypotheses give bounds of the form
(27)--(31) with common constants. Uniform endpoint matching requires (14) for the
full retained, continuum-subtracted integrand, with regulator limits
justified, for example, by a common integrable envelope after the $F^2$
derivatives. Bounded individual bridge contributions allow accumulation
of order $n$; their scale-adjusted partial sums need separate control
(sublinear control suffices for Theorem 4). Proving these bounds for the
generated trajectory, and the interacting remainder bound (17), remains
open; Theorem 2 excludes inferring them from a nondegenerate sharp
Gaussian fixed point.

## 8. Consequence for STATE

Cell 4 has explicit one-step vertices and a finite commonly subtracted
one-loop matching change with constants (Round 10, formal, unrefereed).
The iteration hypotheses are explicit in §7.2; proving them, especially
(14), and controlling interacting remainders remain open.
