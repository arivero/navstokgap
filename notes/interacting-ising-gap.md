# A uniform relaxation gap with nearest-neighbour interactions

For a periodic zero-field Ising heat-bath chain with per-site refresh rate
$a>0$ and dimensionless ferromagnetic coupling $b\ge0$, the full relaxation
gap is exactly $a[1-\tanh(2b)]$ for every $N\ge3$. This replaces G02's
independence premise by a quantitative interaction contraction. Bounded $b$
and a positive per-site clock floor give a size-independent bound; finite
interaction range alone does not control joint size/coupling limits.

## 1. Model, law, clock and access

On $\Omega_N=\{-1,1\}^N$ with cyclic indices and $N\ge3$, let

$$
\pi_{N,b}(\sigma)=Z_{N,b}^{-1}
 \exp\left(b\sum_{i=1}^N\sigma_i\sigma_{i+1}\right),
\qquad b=\beta J\ge0.
$$

Here $J$ is an energy and $\beta$ an inverse energy; $b$ is dimensionless.
Every site has an independent rate-$a$ Poisson refresh clock. Upon a ring,
replace its sign by the conditional Gibbs sign, whose plus probability is

$$
p_i(\sigma)=\frac{1+\tanh[b(\sigma_{i-1}+\sigma_{i+1})]}2
=\frac12+\frac{\theta}{4}(\sigma_{i-1}+\sigma_{i+1}),
\qquad \theta=\tanh(2b).
$$

The generator on all functions on $\Omega_N$ is
$Q_N=a\sum_i(E_i-I)$, where $E_i$ conditions on all sites except $i$.
Refreshes may leave the sign unchanged. The actual flip rate is
$a[1-\theta\sigma_i(\sigma_{i-1}+\sigma_{i+1})/2]/2$.
The conditional-expectation identity makes each $E_i$ an orthogonal
projection in $L^2(\pi_{N,b})$, hence $Q_N$ is self-adjoint and reversible.
For finite $b$, all conditional probabilities are strictly between zero and
one, so single-spin flips connect all states and the chain is irreducible.
Its full centered-space gap has inverse-time units. The time is an auxiliary
stochastic evolution clock, specified independently of the invariant law.

Fix a velocity calibration $u>0$, independent of $N,b$, and observe
$v_i=u\sigma_i$. Spin-flip symmetry centers these observables; each has
variance $u^2$ and two readout levels separated by $2u$. The full vector
identifies the configuration. Its linear span need not cover all centered
functions: the proof below controls the full spectrum through the dynamics.

## 2. All-size lower bound by a written coupling proof

Couple two copies with the same site clocks and the same uniform random
number at every refresh. Let $D_i$ indicate disagreement at site $i$ and
$D=\sum_iD_i$ be Hamming distance. The refresh disagreement probability is
$|p_i(\sigma)-p_i(\eta)|$, bounded by
$\theta(D_{i-1}+D_{i+1})/2$. Thus the coupled generator satisfies

$$
\mathcal L D\le-aD+\frac{a\theta}{2}\sum_i(D_{i-1}+D_{i+1})
=-a(1-\theta)D.
$$

The finite-state evolution and Gronwall's inequality give
$\mathbb E D_t\le e^{-rt}D_0$, $r=a(1-\theta)>0$.
For the Hamming Lipschitz seminorm of any real function $f$,

$$
|P_tf(\sigma)-P_tf(\eta)|
\le \operatorname{Lip}(f)e^{-rt}d(\sigma,\eta),
\qquad \operatorname{Lip}(P_tf)\le e^{-rt}\operatorname{Lip}(f).
$$

Every nonconstant real eigenfunction of $-Q_N$ with eigenvalue $\lambda$
has positive finite seminorm, and $P_tf=e^{-\lambda t}f$.
Cancellation yields $e^{-\lambda t}\le e^{-rt}$ for every $t>0$,
so $\lambda\ge r$. Reversibility supplies a real eigenbasis. This proves
the lower bound for every centered mode, including functions invisible to
the linear span of the local observables. No dimension-dependent prefactor
enters the spectral estimate.

## 3. A matching eigenmode and susceptibility (C124)

For $M=\sum_i\sigma_i$, conditional expectation gives

$$
Q_N\sigma_i=-a\sigma_i+\frac{a\theta}{2}(\sigma_{i-1}+\sigma_{i+1}),
\qquad Q_N M=-a(1-\theta)M.
$$

$M$ is centered and nonzero in $L^2(\pi_{N,b})$, since every configuration
has positive probability. The upper bound from this eigenfunction matches
§2, proving

$$
\boxed{\operatorname{gap}(-Q_N)=a[1-\tanh(2b)]\quad(N\ge3).}
$$

For the bounded mean velocity $V=uM/N$, $|V|\le u$ and

$$
\chi(V)=\frac{\operatorname{Var}_{\pi}(V)}{a[1-\tanh(2b)]},
\qquad \frac{\chi(V)}{\operatorname{Var}_{\pi}(V)}
=\frac1{\operatorname{gap}(-Q_N)}.
$$

The variance is positive for every finite member but is not asserted to
have a uniform lower bound in $N$. A fixed mass $m>0$ gives the action-valued
plateau $H(V)=2m\chi(V)$, as in C019/C041. The normalized response has time
units and detects the slow mode without an extensive full-frame sum.

## 4. Premises retained and closing limits

At fixed finite $b$, the exact gap stays positive as $N\to\infty$; this
statement concerns the sequence of finite-volume gaps. More generally,
$a_N\ge a_0>0$ and $0\le b_N\le B<\infty$ imply
$\operatorname{gap}(-Q_N)\ge a_0[1-\tanh(2B)]$.
At $b=0$ the refresh chain flips with rate $a/2$, recovering C046's gap $a$.

Finite range and fixed calibration persist if $b_N\to\infty$ with $a$
fixed, but the exact gap tends to zero. For example $b_N=(\log N)/4$ gives
$\tanh(2b_N)=(N-1)/(N+1)$ and gap $2a/(N+1)$. This varies interaction
strength as well as size; it is not a fixed-coupling thermodynamic closure.
Alternatively dividing $Q_N$ by $N$ fixes the total refresh rate at $a$
and gives gap $a[1-\tanh(2b)]/N$ even at fixed $b$.

The sufficient replacement for independence in this family is a uniform
margin in the neighbour-influence sum, together with the per-site clock
floor. A prescribed invariant Gibbs law alone selects neither clock.
For a supplied action constant $K>0$, the operator $K(-Q_N)$ has energy
gap $Ka[1-\tanh(2b)]$. This does not identify the sampling operator with a
physical quantum Hamiltonian or select $K$. An infinite-volume operator
construction and a continuum or quantum-field transfer remain separate tasks.

## 5. Evidence and strategic consequence

The proof is a finite-state written contraction argument plus an explicit
magnetization eigenfunction. The Ising dynamics and relaxation mechanism are
classical prior literature; no novelty is asserted. The [B68 audit](../references/batches/B68.md) records model/method matches
and the [written proof review](../reviews/ising-gap-B68.md). Glauber formula
images remain unverified after the publisher access failure; the exact
full-spectrum equality is accepted on the self-contained proof, with no
imported source theorem required.

G03's first milestone ends here: independence is unnecessary for a uniform
finite-volume gap in this interacting family, while finite range without
coupling and clock control is insufficient. Q01 is the selected next main
track. Further Ising variants are parked until they discharge a named
physical-operator or uniform-limit dependency.
