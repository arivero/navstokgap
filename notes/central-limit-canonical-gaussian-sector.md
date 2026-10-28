# Canonical averaging and the Gaussian sector of Newton preparations

**Result, 2026-10-27; conditional construction.** Independent copies,
canonical mixing, forgetting unused copies and either weak or
$W_2$-closure do force Gaussian preparations: every admissible
finite-covariance state has an
admissible Gaussian with the same mean and covariance. If, in addition,
the hypotheses of the existing
[cusp preparation theorem](newton-cusp-preparation-floor.md) hold, the
one-pair Gaussian sector is exactly
$$
 \mathcal G_{\kappa_*}
 =\{\mathcal N(\mu,\Sigma):\ \det\Sigma\ge\kappa_*^2\},
 \qquad \kappa_*>0. \tag{1}
$$
The infimum $\kappa_*$ of covariance actions is attained by a Gaussian.
Every Gaussian above the floor can be built from two independently
prepared squeezed copies of a floor state and a canonical mixer.

These conclusions are conditional on the preparation and copying
premises stated below. The mathematical Gaussian covariance condition
is the same shape as a quantum uncertainty condition, but its
identification with $\hbar/2$ is **not** proved. The existing
bounded-density cusp model fails even the two-copy mixer test. An
entropy-floor class below realizes actual nonlinear cusp transport and
the mixer rules with $W_2$-closure, but it is not weakly closed.
Without cusp compatibility, copy/mixing closure allows a zero-floor
Gaussian theory. The subsequent [Gaussian-meter counterexample](gaussian-meter-entropy-floor.md)
shows that selective records do not preserve the entropy-floor witness,
even with a minimum-action Gaussian pointer and a single finite-resolution
position record.

The central limit theorem and Gaussian symplectic covariance are
standard. In quantum optics, the known Cushen--Hudson central limit
has precisely an $n$-splitter interpretation; see
[Becker--Datta--Lami--Rouzé](https://arxiv.org/abs/1912.06129)
(abstract and introduction). The present calculation is a classical
probability argument, not that quantum theorem. The restricted
Liouville/Gaussian comparison is also established in
[Bartlett--Rudolph--Spekkens](https://arxiv.org/abs/1111.5057)
(abstract). The purpose here is to resolve the conditional preparation
question posed in [STATE](../research/STATE.md), without claiming
literature priority.

## 1. The premises and the action units

A one-pair preparation is a probability measure on $(q,p)\in\mathbb R^2$.
Let $\mathcal S_1$ be nonempty and contain at least one state with finite
covariance. Assume:

1. **Affine canonical covariance.** Every affine symplectic image of a
   member of $\mathcal S_1$ belongs to $\mathcal S_1$.
2. **A closure rule.** Either every probability-valued weak limit of
   members belongs to $\mathcal S_1$, or every $W_2$ limit in the
   finite-second-moment space $\mathcal P_2$ of members of
   $\mathcal S_1\cap\mathcal P_2$ belongs to $\mathcal S_1$. The
   second condition is weaker: $W_2$ convergence implies weak
   convergence, but not conversely.
3. **Independent copies and canonical mixing.** For every finite
   collection of admissible one-pair states, independent product
   preparation, a joint canonical transformation of the form described
   below, and forgetting all but one output pair produce a member of
   $\mathcal S_1$. In particular this holds for arbitrarily many
   identical copies and for the two-copy $50{:}50$ mixer.

No selective measurement or conditioning is included in item 3. The
unretained output pairs may be kept as a full record before taking the
marginal; the joint transformation is invertible.

Choose fixed units $L_0,P_0>0$ and let
$$x=q/L_0,\quad y=p/P_0,\quad S_0=L_0P_0.\tag{2}$$
Write $z=(x,y)$, $C=\operatorname{Cov}(z)$, and
$\Omega=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$. A real $2\times2$ map in
the calibrated coordinates is canonical when its determinant is one.
The physical covariance action is
$$\kappa(\mu)=\sqrt{\det\operatorname{Cov}(q,p)}
             =S_0\sqrt{\det C}.\tag{3}$$
Translations and determinant-one maps do not change $\kappa$.

## 2. A central limit implemented by canonical transformations

Let $\mu\in\mathcal S_1$ have mean $m$ and finite covariance $C$.
Prepare $n$ independent copies $Z_i=(x_i,y_i)$ with this law. Choose a
real orthogonal matrix $O_n$ whose first row is
$(1,\ldots,1)/\sqrt n$ and transform
$$x'=O_n x,\qquad y'=O_n y.\tag{4}$$
This is canonical: it preserves the symplectic form because $O_nO_n^T=I$.
The first output pair is
$$Z'_1=\frac1{\sqrt n}\sum_{j=1}^n Z_j.\tag{5}$$
Translate this pair by $(1-\sqrt n)m$, and forget the others. By the
premises its law belongs to $\mathcal S_1$. Its characteristic function
is
$$
 \left[e^{-ik\cdot m/\sqrt n}\,
       \widehat\mu(k/\sqrt n)\right]^n e^{ik\cdot m}.\tag{6}
$$
Finite covariance gives the expansion
$e^{-ik\cdot m/\sqrt n}\widehat\mu(k/\sqrt n)
 =1-\frac1{2n}k^TCk+o(n^{-1})$. Thus (6) tends to
$\exp(ik\cdot m-\frac12k^TCk)$. Lévy's continuity theorem and weak
closure show
$$\boxed{\mathcal N(m,C)\in\mathcal S_1.}\tag{7}$$
This includes a degenerate Gaussian if $C$ is singular. The output
means and covariance are independent of $n$, so the second moments also
converge to those of the Gaussian. Thus the convergence holds in
$W_2$ as well: $W_2$ metrizes weak convergence plus convergence of
second moments; see
[Raginsky--Sason, Lemma 3.4.3](https://webee.technion.ac.il/people/sason/Raginsky_Sason.pdf)
(statement read). Either closure rule therefore admits (7). The
covariance is the covariance of the original state: the theorem
creates a Gaussian sector, not an action scale.

The normalization in (5) is essential. If instead one forms the
arithmetic averages $\bar x=n^{-1}\sum x_i$ and
$\bar y=n^{-1}\sum y_i$, then
$\{\bar x,\bar y\}=1/n$ in normalized canonical brackets. The
canonically conjugate variable to $\bar x$ is
$\sum_i y_i$, not $\bar y$. For independent identical copies their
variances scale as $1/n$ and $n$, respectively, so their covariance
action is not reduced merely by renaming both averages as a canonical
pair.

## 3. A floor state and every Gaussian above it

Define
$$
 \kappa_*=\inf_{\mu\in\mathcal S_1,\ \operatorname{Cov}\mu<\infty}
          \sqrt{\det\operatorname{Cov}(q,p)}.\tag{8}
$$
Suppose **in addition** that $\kappa_*>0$. Let
$\zeta_*=\kappa_*/S_0$. For every sequence $\mu_j$ with covariance
actions decreasing to $\kappa_*$, (7) makes its corresponding Gaussians
admissible. Their calibrated covariances $C_j$ are positive definite.
The canonical matrix
$$A_j=(\det C_j)^{1/4}C_j^{-1/2},\qquad \det A_j=1,\tag{9}$$
takes $C_j$ to $\sqrt{\det C_j}\,I$. Translate the means to zero.
The resulting admissible Gaussian laws converge both weakly and in
$W_2$ to
$$G_*=\mathcal N(0,\zeta_* I).\tag{10}$$
Either closure rule admits $G_*$, which attains the floor.

Now squeeze two **independent** copies of $G_*$ in opposite directions:
$$
 C_1=\zeta_*\begin{pmatrix}e^{2r}&0\\0&e^{-2r}\end{pmatrix},
 \qquad
 C_2=\zeta_*\begin{pmatrix}e^{-2r}&0\\0&e^{2r}\end{pmatrix}.
 \tag{11}
$$
Each squeeze is symplectic. Mix the two copies canonically by
$$
 (x_+,y_+)=\frac{(x_1,y_1)+(x_2,y_2)}{\sqrt2},\quad
 (x_-,y_-)=\frac{(x_1,y_1)-(x_2,y_2)}{\sqrt2},\tag{12}
$$
and keep the plus pair. Its covariance is
$$C_+=\frac{C_1+C_2}{2}=\zeta_*\cosh(2r)\,I.\tag{13}$$
Every isotropic covariance $\nu I$, $\nu\ge\zeta_*$, is obtained by a
choice of $r$. If $C>0$ and $\sqrt{\det C}=\nu$, then
$C=\nu BB^T$ for
$B=C^{1/2}/\sqrt\nu$ with $\det B=1$. A further canonical transformation
and translation therefore produce every Gaussian with
$\det C\ge\zeta_*^2$. Conversely no finite-covariance admissible state
can have a smaller determinant by (8). Consequently
$$
 \{\hbox{Gaussian laws in }\mathcal S_1\}
 =\{\mathcal N(m,C):\det C\ge\zeta_*^2\}. \tag{14}
$$

The copy and mixer assumptions do real work in (11)--(13): canonical
squeezing alone preserves determinant and would only produce the
boundary $\det C=\zeta_*^2$. This gives the full Gaussian sector without
assuming closure under arbitrary additive noise. It does not show that
all non-Gaussian states above the same floor are admissible.

## 4. What the cusp adds, and what remains unproved

The earlier cusp theorem supplies $\kappa_*>0$ if, in addition to
affine canonical covariance and weak closure, preparation evolution is
reversible and agrees with both incoming trajectories at its specified
non-Lipschitz merger. Its proof also works under the weaker $W_2$
closure. Indeed, if $\kappa_*=0$, the centered, canonically squeezed
states constructed in equations (9)--(11) of the cusp note have second
moments tending to zero, so their $W_2$ distance to $\delta_0$ tends to
zero. Closure admits $\delta_0$, and the existing merger argument
contradicts reversibility. Substitution in §3 proves (1), and strengthens
that theorem's previous conclusion in this **enlarged premise set**:
the positive infimum is attained and the whole one-pair Gaussian
sector is known.

This does not prove that the premises are jointly physically realized.
Indeed the earlier bounded-density classical cusp model
$\mathcal S_M=\{0\le f\le M,\ \int f=1\}$ **fails** the two-copy
premise. Let $E$ be a centrally symmetric disk of canonical area $1/M$
and let $f=M1_E$. For two independent copies, the retained
$z_+=(z_1+z_2)/\sqrt2$ has continuous density
$$f_+(z)=2(f*f)(\sqrt2z),\qquad
 f_+(0)=2\int f(w)f(-w)\,dw=2M.\tag{14a}$$
It exceeds $M$ on a neighbourhood of zero. Thus an explicit
cusp-compatible witness for the earlier theorem is not a witness for
the stronger premise set here. Its disk has the earlier sharp action
$1/(4\pi M)$, unchanged by this identical-copy averaging, so the
failure is the pointwise density ceiling, not a change in covariance.

The earlier cusp premise, literally stated, constrains Newtonian
evolution only **if point preparations are admitted**. A positive-floor
Gaussian family admits no points, so identity evolution on that family
satisfies the point-compatibility clause vacuously while also satisfying
the copying assumptions. The abstract combined assumptions are
therefore consistent, but that example does not transport nonpoint
states by Newton's cusp flow. Section 6 gives a class with actual cusp
transport and the copy rules under $W_2$-closure; its ordinary weak
closure fails. A nonlinear cusp flow does not generally preserve Gaussian shape; the
theorem does not assume that it does. Under the literal earlier
premises the cusp argument supplies positivity; the central limit and
mixing supply the Gaussian sector. Identifying the resulting
$\kappa_*$ with the real-time quantum phase constant remains a further
physical question.

This loss of Gaussian shape can be seen directly. For an initial
centered product Gaussian with variances $\sigma_q^2,\sigma_p^2$,
and a Newton force $F(q)=-V'(q)$, the Liouville equation gives, at
almost every point,
$$
 \left.\partial_t\log\rho_t(q,p)\right|_{t=0}
 =\frac{qp}{m\sigma_q^2}+\frac{pF(q)}{\sigma_p^2}.\tag{14b}
$$
For the non-affine cusp force this is not a quadratic polynomial in
$(q,p)$, while the tangent to a differentiable Gaussian family has
quadratic logarithmic derivative. Thus Gaussian preparations alone
are not invariant under the actual cusp transport.

For comparison, the
[statistical-speed theorem](newton-indeterminacy-routes.md) obtains its
affine-generator bound on a restricted Gaussian sector with supplied
$h_*=2\zeta$. Equation (14) gives that Gaussian covariance family under
the additional cusp and copying assumptions, with
$\zeta=\kappa_*$ in physical action units. It does not supply the
recorded-instrument closure required by that theorem, nor does it
extend the affine-generator estimate to every nonlinear generator.

## 5. Two closure tests

**Zero branch.** For every $\zeta\ge0$ and every number $n$ of canonical
pairs, let $\mathcal G_\zeta^{(n)}$ be all Gaussian probability measures
whose covariance satisfies
$$\Sigma+i\zeta\Omega_n\succeq0,\qquad
 \Omega_n=\Omega\oplus\cdots\oplus\Omega.\tag{15}$$
These are classical probability measures, including degenerate ones
when $\zeta=0$. Here $\Sigma$ and $\zeta$ refer to the calibrated
coordinates of (2); the physical covariance action is $S_0\zeta$.
Independent products give block-diagonal covariance;
affine symplectic transformations preserve (15); and a marginal is a
principal submatrix, so it also satisfies (15). Probability-valued
weak limits remain Gaussian: tightness bounds the means and covariance
matrices of a Gaussian sequence, and subsequential parameter limits
preserve (15). Thus all the operations of §§1--2 are available for
every $\zeta\ge0$. In particular $\zeta=0$ includes point measures and
has no positive floor. This family does not establish compatibility
with the cusp flow, and it does not show that copying selects any
particular positive value.
The zero-floor example is not a classification of every possible
zero-floor class: all Dirac measures alone also satisfy the stated
copying and weak-closure rules without containing nondegenerate
Gaussians.

**Selective records.** For $\zeta>0$, take the classical Gaussian
$G_*=\mathcal N(0,\zeta I)$. An ideal, non-disturbing exact
$q$-measurement yields a conditional state supported on a fixed
$q$-line, with zero covariance determinant. It is outside
$\mathcal G_\zeta^{(1)}$. Forgetting unused canonical output pairs is
therefore much weaker than closure under arbitrary selective records.
An instrument preserving a positive floor must restrict the record,
introduce appropriate back-action, or impose another physical rule.

**A covariance floor alone is not weakly closed.** With $\zeta>0$,
$$
 \mu_n=(1-1/n)\delta_0+(1/n)\,\mathcal N(0,n\zeta I)
 \;\Longrightarrow\;\delta_0,\qquad
 \operatorname{Cov}(\mu_n)=\zeta I.\tag{16}
$$
A vanishing fraction of mass can carry all of the variance. Thus
bounding the covariance determinant for each member does not by itself
make the class weakly closed; even uniformly bounded second moments do
not give the uniform integrability needed for covariance convergence.
The Gaussian class in the zero-branch test has extra structure.

## 6. An entropy floor with actual cusp transport

There is a classical realization of the combined preparation, copy and
actual cusp-transport rules if the closure rule is $W_2$ rather than
unrestricted weak closure. In the calibrated coordinates of (2), fix
any **supplied** $\zeta>0$ and consider
$$
 \mathcal E_\zeta
 =\left\{\rho(z)\,dz\in\mathcal P_2(\mathbb R^2):
 h(\rho):=-\int\rho\log\rho\,dz\ge\log(2\pi e\zeta)\right\}.\tag{17}
$$
The entropy threshold uses dimensionless coordinates. A finite second
moment bounds differential entropy from above; the displayed lower
bound makes it finite. The Gaussian $\mathcal N(0,\zeta I)$ belongs,
so the class is nonempty. Affine canonical transformations preserve
area and hence entropy and membership in $\mathcal P_2$.

For the bounded cusp force of the
[earlier theorem](newton-cusp-preparation-floor.md), the point flow is
an invertible, area-preserving group outside an invariant null set.
It transports every density in (17), preserving its entropy; the
bounded force and finite time also preserve its second moment. Coupling
the transported state to the same initial point and using dominated
convergence gives continuity in $W_2$ with time. This is actual
Liouville transport of the nonpoint states, not the vacuous identity
evolution discussed in §4.

For independent $Z_i\sim\rho_i\in\mathcal E_\zeta$ and real coefficients
$a_i$ with $\sum_i a_i^2=1$, the two-dimensional entropy power
inequality gives
$$
 N\!\left(\sum_i a_iZ_i\right)
 \ge\sum_i a_i^2 N(Z_i)\ge\zeta,\qquad
 N(Z):=\frac{e^{h(Z)}}{2\pi e}.\tag{18}
$$
See [Toscani, §6](https://mate.unipv.it/toscani/publi/Convolution.pdf)
(entropy-power inequality statement read). In particular the output
of every copy-index orthogonal mixer and marginal in §2 remains in
$\mathcal E_\zeta$. This establishes those mixers; arbitrary
nonlinear joint canonical maps are not asserted.

The class is $W_2$-closed. Let $g(z)=(2\pi)^{-1}e^{-|z|^2/2}$.
For any absolutely continuous $\mu=\rho dz$,
$$
 D(\mu\Vert g\,dz)
 =-h(\rho)+\log(2\pi)+\frac12\int |z|^2\,d\mu(z).\tag{19}
$$
If $\mu_n\in\mathcal E_\zeta$ tends to $\mu$ in $W_2$, their second
moments converge and relative entropy is weakly lower semicontinuous.
The right side of (19) is uniformly bounded, so $\mu$ is absolutely
continuous and (19) gives $h(\mu)\ge\log(2\pi e\zeta)$.
The Gaussian maximum-entropy inequality then gives
$$
 \sqrt{\det\operatorname{Cov}(Z)}
 \ge \frac{e^{h(Z)}}{2\pi e}\ge\zeta.\tag{20}
$$
Its Gaussian sector is exactly $\det C\ge\zeta^2$, and its physical
floor is $S_0\zeta$.

Ordinary weak closure is stronger and fails here. Put
$$
 \mu_n=(1-1/n)\mathcal N(0,\zeta e^{-2n}I)
       +(1/n)\mathcal N(0,\zeta e^{2n^2}I).\tag{21}
$$
Entropy concavity gives $h(\mu_n)\ge\log(2\pi e\zeta)+2$.
Nevertheless $\mu_n$ converges weakly to $\delta_0$, which is not in
$\mathcal E_\zeta$; the second moments diverge, so this is not a
$W_2$-convergent sequence. The entropy floor, like the earlier density
ceiling, is an explicitly supplied classical preparation constraint.
It does not identify the floor with quantum $\hbar/2$. The subsequent
[Gaussian-meter counterexample](gaussian-meter-entropy-floor.md) proves
that this class fails selective closure under a single specified
minimum-action Gaussian pointer; its postselected states can have
arbitrarily small covariance action. Gaussian input states pass the same
test. The counterexample uses increasingly large preparation apertures.

## 7. Consequence for STATE

The proposed central-limit step is settled under explicit copy/mixer,
discard and either weak- or $W_2$-closure premises. Together with the
earlier point-trajectory compatibility hypotheses, it gives an attained
positive covariance floor and exactly the one-pair Gaussian sector
above it. The entropy model realizes actual nonlinear cusp transport
and the specified mixers under $W_2$ closure, while demonstrating
that ordinary weak closure is a separate, stronger condition. The
supplied entropy floor does not derive $\hbar$ or independent action
necessity; its selective record closure fails as specified above.
