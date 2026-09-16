# The large-field action lower bound is immediate in the natural variable, and the constant field saturates it

The bound asked for at the end of
[the entropy note](large-field-entropy-count.md) holds with the optimal
constant, once the large-field condition is written in the variable the
action already measures. Define the region as
$$K_\eta=\Big\{A:\ \frac1{\ell^4}\int_{\rm block}\big|G_t(x)\big|^2d^4x\ \ge\ \Big(\frac{\eta}{\ell^2}\Big)^2\Big\},
\qquad \sqrt{8t}=\ell,$$
with $G_t$ the field strength at flow time $t$. Then
$$\inf_{K_\eta}\frac{S_E}{\hbar}\ \ge\ \frac{\eta^2}{4g^2},$$
by two steps only: the gradient flow decreases the Euclidean action, so
$S_E[A]\ge S_E[\text{flowed }A]$, and the flowed action is at least its
restriction to the block, which the constraint bounds below. The bound
is **uniform in the block size, in the lattice spacing, in the volume
and in the gauge group** in the normalization used here, and it is
**saturated**: a field of magnitude $\eta/\ell^2$ supported on the block
attains it, so the constant $1/4$ is optimal. The Nielsen--Olesen
instability is no obstruction, because every deformation that lowers the
action also lowers the flowed block average and therefore leaves
$K_\eta$: the constant field is a saddle of the unconstrained action and
a minimizer of the constrained one. Together with
[the entropy count](large-field-entropy-count.md) this closes the
large-field corner as an estimate problem: cost $\eta^2/(4g^2)$, count
$\eta^2/(8\pi^2)$, net exponent
$-\frac{\eta^2}{4g^2}\big(1-Cg^2/2\pi^2\big)$. Constants explicit;
nothing promoted.

## 1. The constraint in the right variable

The Euclidean action is the $L^2$ norm of the field strength,
$$\frac{S_E}{\hbar}=\frac1{4g^2}\int\big|F^a_{\mu\nu}(x)\big|^2d^4x ,$$
so the natural measure of "how large the field is in a block" is the
same quantity restricted to the block, and the natural smoothing is the
gradient flow at the radius of the block. Take $\sqrt{8t}=\ell$ and
$$\mathcal F_\ell(A)=\frac1{\ell^4}\int_{\rm block}\big|G_t(x)\big|^2d^4x,
\qquad K_\eta=\Big\{A:\ \mathcal F_\ell(A)\ge\eta^2/\ell^4\Big\}.$$
This is gauge invariant, because $|G_t|^2$ is, and it is the quantity
that the truncation estimate of
[the Jacobian note](flow-jacobian-truncation-error.md) is sensitive to,
up to replacing a supremum by a block average.

## 2. The bound

**Proposition 1.** For every $\ell>0$, every lattice spacing $a<\ell$ and
every volume,
$$\inf_{A\in K_\eta}\ \frac{S_E[A]}{\hbar}\ \ge\ \frac{\eta^2}{4g^2}.$$

*Proof.* Two steps.

*(i) The flow decreases the action.* Along the gradient flow
$\partial_sB=-D^*G$ one has
$\frac{d}{ds}S_E(B_s)=-\|D^*G\|_2^2\le0$
([comparison note](comparison-and-bridges.md) §4; Lüscher,
arXiv:1006.4518v3, after equation (1.4), passage level), so
$S_E[A]=S_E[B_0]\ge S_E[B_t]=\frac{\hbar}{4g^2}\int|G_t|^2d^4x$.

*(ii) Positivity outside the block.* The integrand is nonnegative, so
$$\frac1{4g^2}\int\big|G_t\big|^2\ \ge\ \frac1{4g^2}\int_{\rm block}\big|G_t\big|^2
\ \ge\ \frac1{4g^2}\,\ell^4\cdot\frac{\eta^2}{\ell^4}=\frac{\eta^2}{4g^2},$$
the middle inequality being the definition of $K_\eta$. $\square$

No property of the gauge group beyond the normalization of the trace
enters, and no property of the lattice beyond $a<\ell$, which is needed
only so that the flow at radius $\ell$ is meaningful.

**Proposition 2 (sharpness).** The constant $1/4$ cannot be improved. A
configuration whose field strength equals $\eta/\ell^2$ on the block and
vanishes outside has $S_E/\hbar=\eta^2/(4g^2)$ and lies in $K_\eta$ up
to the smoothing at the boundary of the block, which contributes a
relative correction of order $a/\ell$.

## 3. Why the instability does not obstruct the bound

[The instability note](flow-instability-large-field.md) shows that a
constant chromomagnetic field is a saddle of the unconstrained action,
with $\mathcal N(\eta)=\eta^2/(8\pi^2)$ descent directions. Each of those
directions lowers $S_E$, and by step (i) of Proposition 1 it therefore
lowers $\int|G_t|^2$ as well, so it lowers $\mathcal F_\ell$ and moves the
configuration out of $K_\eta$. The two statements are consistent and say
different things:

- *unconstrained*: the constant field is not a local minimum, and the
  flow runs away from it at rate $2\|G\|$;
- *constrained*: on $K_\eta$ the constant field attains the infimum,
  because every descent direction violates the constraint.

The instability therefore affects the **treatment** of the region, which
must expand around an inhomogeneous configuration if one insists on
staying inside $K_\eta$ while following the flow, and not the **cost**
of the region, which Proposition 1 fixes.

## 4. The corner, assembled

Collecting the three statements about a large-field region of strength
$\eta$ at scale $\ell$:

| quantity | value | source |
| --- | --- | --- |
| minimal action cost | $\eta^2/(4g^2)$, sharp | Propositions 1--2 here |
| unstable directions | $\eta^2/(8\pi^2)$ | [entropy note](large-field-entropy-count.md) §2 |
| flow-truncation error inside | $e^{2\eta}$, sharp | [instability note](flow-instability-large-field.md) |
| net weight | $\exp\big[-\frac{\eta^2}{4g^2}\big(1-\frac{Cg^2}{2\pi^2}\big)\big]$ | combining the first two |

All four are independent of $\ell$ and of the lattice spacing, which is
the scale invariance that makes an induction over scales possible at
all. The first three are proved or sharp; the fourth needs the standard
conditional argument comparing the constrained partition function with
the full one, in which the entropy of the block is exactly the count in
the second row.

**What is closed.** The large-field region is no longer an unquantified
obstacle. Its cost, its entropy and the failure mode of the flow inside
it are all explicit, scale-invariant, and consistent with each other.

**What is not.** How the effective Hamiltonian is defined inside the
region. Proposition 1 bounds the weight of the region; it does not say
what replaces the flow-and-truncate step there, and the constructive
answer, an expansion around the constrained minimizer with its
$\eta^2/(8\pi^2)$ soft directions treated separately, is a construction
rather than an estimate.

## 5. Consequence for STATE

The lower bound asked for is proved with the optimal constant and
uniformly in every parameter, by flow monotonicity and positivity, once
the constraint is written as a block average of the flowed action
density. The large-field corner is closed at the level of estimates. The
remaining content of the decimation step is the construction inside the
region, which is the same constructive problem the programme has
reached from three directions now: after the small-field truncation is
controlled, the large-field regions are rare and expensive but must
still be given an effective description.
