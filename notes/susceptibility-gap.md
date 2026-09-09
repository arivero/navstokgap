# When an action plateau controls a spectral gap

A complete collection of observables with bounded total susceptibility gives
a lower relaxation-gap bound. A single positive velocity plateau instead
gives an upper bound, and can miss an arbitrarily slow internal mode.
We prove both statements for finite reversible dynamics and specify the
energy normalization needed for the Dirac comparison.

## 1. Operator, observable and units

Let $Q$ generate an irreducible continuous-time Markov chain on a finite set
of $n\ge2$ states, with stationary probabilities $\pi_i>0$ and detailed
balance $\pi_iQ_{ij}=\pi_jQ_{ji}$. The generator acts on functions, with row
sums zero. On $L^2(\pi)$ use
$\langle f,g\rangle_\pi=\sum_i\pi_i\overline{f_i}g_i$.
The centered space $\mathcal H_0=\{f:\langle1,f\rangle_\pi=0\}$ has
dimension $n-1$. All domains are the entire indicated finite-dimensional space.

Set $A=-Q|_{\mathcal H_0}$. It is positive self-adjoint with eigenvalues
$0<\gamma_1\le\cdots\le\gamma_{n-1}$. The full relaxation gap is
$\gamma_1$, in inverse-time units. For a real centered observable $v$ with
velocity units, define

$$
\chi(v)=\langle v,A^{-1}v\rangle_\pi
=\int_0^\infty\langle v,e^{tQ}v\rangle_\pi\,dt,
\qquad H(v)=2m\chi(v),\quad m>0.
$$

$\chi$ has units length squared per time, and $H$ has action units. This
is C019's long-observation plateau for the integrated velocity. The
Green–Kubo/Poisson representation is matched to Pavliotis in
[B20](../references/batches/B20.md); the finite-dimensional consequences
below are derived explicitly. Time here is the chain's evolution parameter.

## 2. One observable: the product and its direction (C041)

Write $v=\sum_j a_je_j$ in an orthonormal eigenbasis of $A$, and
$\sigma_v^2=\|v\|_\pi^2>0$. Then

$$
H(v)=2m\sum_j\frac{|a_j|^2}{\gamma_j},\qquad
H(v)\gamma_1\le2m\sigma_v^2\le H(v)\gamma_{n-1}.
$$

**Proof.** Integrate each exponential in
$\langle v,e^{tQ}v\rangle_\pi=\sum_j|a_j|^2e^{-\gamma_jt}$ and use
$\sum_j|a_j|^2=\sigma_v^2$. The left inequality gives
$\gamma_1\le2m\sigma_v^2/H(v)$: an upper gap bound.
The normalized integral time
$\tau_v=\chi(v)/\sigma_v^2$ is a weighted average of $1/\gamma_j$;
in particular $\tau_v\le1/\gamma_1$.

For the two-state chain $Q=\lambda(\sigma_x-I)$ and $v=u(1,-1)$,
$\pi=(1/2,1/2)$, with $u,\lambda>0$, the centered space is one-dimensional.
Therefore

$$
\gamma_1=2\lambda,\qquad H(v)=\frac{mu^2}{\lambda},\qquad
H(v)\gamma_1=2mu^2.
$$

Here $\sigma_x$ exchanges the two signs. This equality identifies the source
of the two-state product: every centered mode is visible to velocity.

## 3. Fixed plateau with a closing full gap (C041)

Take two independent signs $s,r\in\{-1,1\}$ with rates $\lambda>0$ and
$\epsilon>0$, respectively, and define velocity $v(s,r)=us$, with fixed
$0<u<c$. The four-state generator is

$$
Q_{\lambda,\epsilon}=\lambda(\sigma_x-I)\otimes I
+I\otimes\epsilon(\sigma_x-I).
$$

The uniform measure is stationary and reversible. The functions
$1,s,r,sr$ form an orthonormal eigenbasis with eigenvalues of $-Q$
equal to $0,2\lambda,2\epsilon,2(\lambda+\epsilon)$.
Velocity overlaps only the $s$ mode. Thus

$$
H(v)=\frac{mu^2}{\lambda},\qquad
\gamma_1=2\min(\lambda,\epsilon)\longrightarrow0
\quad\hbox{as }\epsilon\downarrow0.
$$

Every positive-$\epsilon$ member is irreducible, with the same bounded speed
and the same positive plateau. At the limiting parameter the label becomes
conserved. The velocity path law itself is unchanged throughout the family.
The missing information is the label's relaxation: finite-rate assumptions
for each member give positivity member by member, while a uniform lower gap
requires additional control over the family.

## 4. A sufficient condition: complete observability (C042)

Choose centered velocity-unit observables $f_1,\ldots,f_r$ and suppose
that, for every $g\in\mathcal H_0$,

$$
\sum_{a=1}^r|\langle f_a,g\rangle_\pi|^2
\ge\alpha\|g\|_\pi^2,\qquad\alpha>0.
$$

This *frame bound* means that the collection detects every centered mode;
$\alpha$ has velocity-squared units. Put
$S=\sum_a\chi(f_a)$. Then

$$
\boxed{\gamma_1\ge\frac{\alpha}{S}.}
$$

If $H(f_a)\le B_a$, it follows that
$\gamma_1\ge2m\alpha/\sum_aB_a$.

**Proof.** Set $b_j=\sum_a|\langle e_j,f_a\rangle_\pi|^2$.
The frame hypothesis gives $b_j\ge\alpha$ for every unit eigenvector. Hence

$$
S=\sum_j\frac{b_j}{\gamma_j}\ge\frac{\alpha}{\gamma_1}.
$$

Multiplication by $\gamma_1/S$ proves the result. Equivalently, the frame
operator $F=\sum_a|f_a\rangle\langle f_a|$ satisfies $F\ge\alpha I$ and
$S=\operatorname{Tr}(A^{-1}F)$.

For a family, uniform $\alpha\ge\alpha_0>0$ and $S\le S_0<\infty$
give the uniform bound $\gamma_1\ge\alpha_0/S_0$. When masses vary, the
action-valued version must control $\sum_aB_a/(2m)$, rather than merely
$\sum_aB_a$. The frame can have full rank only if $r\ge n-1$.
These requirements expose the cost of carrying the estimate to larger systems.

The exact all-observable formulation is

$$
\sup_{f\in\mathcal H_0\setminus\{0\}}
\frac{\chi(f)}{\|f\|_\pi^2}=\|A^{-1}\|=\frac1{\gamma_1}.
$$

The spectral expansion proves the upper bound, and a slowest eigenvector
attains equality. It is the inverse-operator version of a Poincaré bound.

In the four-state example choose $f_1=us$, $f_2=ur$, $f_3=usr$. They give
$F=u^2I$ on $\mathcal H_0$, and

$$
S=u^2\left[\frac1{2\lambda}+\frac1{2\epsilon}
+\frac1{2(\lambda+\epsilon)}\right].
$$

The complete collection detects the approaching gap closure through
$\chi(f_2)\to\infty$. Each observable stays bounded in magnitude by $u$.
Thus speed control and susceptibility control address different premises.

## 5. Energy normalization and the companion field problem

On full $L^2(\pi)$ define $\mathcal E=K(-Q)$ with a supplied action unit
$K>0$. Constants form its unique zero-energy ground space; its excitation
gap is $\Delta_{\mathcal E}=K\gamma_1$. In the two-state model, setting
$K=H(v)$ gives

$$
\Delta_{\mathcal E}=2mu^2.
$$

The numerical substitution $u=c$ matches C039's Dirac rest-branch separation
$2mc^2$. The two operators have different state spaces and spectral meanings:
$\mathcal E$ is a nonnegative finite-state relaxation operator, while the
Dirac operator has positive and negative single-particle branches. A quantum
field vacuum gap additionally requires its physical Hilbert space and the
continuum/infinite-volume construction.

For the companion programme, C042 supplies a candidate form of estimate:
observable coverage bounded below, inverse-generator response bounded above.
Transferring it requires identifying the physical generator and proving that
both bounds survive the relevant limits. An algorithmic sampling chain's
relaxation time is a distinct object from physical Euclidean time evolution.

## 6. Weak access and distinct velocities (C045)

In §3's four-state model take dimensionless $0<\delta\le1$ and observables
$f_1=us$, $f_2=u\delta r$, $f_3=u\delta sr$. In the centered orthonormal
basis $(s,r,sr)$ their frame and total response are

$$
F_\delta=u^2\operatorname{diag}(1,\delta^2,\delta^2),\quad
\alpha_\delta=u^2\delta^2,\quad
S_\delta=u^2\left[\frac1{2\lambda}+\frac{\delta^2}{2\epsilon}
+\frac{\delta^2}{2(\lambda+\epsilon)}\right].
$$

Set $\epsilon=\lambda\delta^2$, keeping $m,u,\lambda$ fixed. Then
$S_\delta=(u^2/\lambda)[1+\delta^2/(2(1+\delta^2))]$ stays bounded,
while both $\alpha_\delta$ and the actual gap $2\lambda\delta^2$ tend to
zero. This follows by diagonal substitution; full rank at each parameter
is weaker than uniform calibrated coverage.

The same mechanism survives an injective physical velocity map. For
$0<\delta\le1/4$ set

$$
v_\delta(s,r)=\frac{u}{\sqrt2}(s+\delta r),\qquad
\epsilon=\lambda\delta^2.
$$

Its four values are distinct and satisfy
$|v_\delta|\le5u/(4\sqrt2)<u<c$. The stationary mean is zero and

$$
\chi(v_\delta)=\frac{u^2}{2}\left[\frac1{2\lambda}
+\frac{\delta^2}{2\epsilon}\right]=\frac{u^2}{2\lambda},\qquad
H(v_\delta)=\frac{mu^2}{\lambda},\qquad
\gamma_1=2\lambda\delta^2\longrightarrow0.
$$

Thus the velocity itself labels all four states and defines a four-state
Markov chain, with a fixed positive plateau throughout the family. To recover
the observable $ur$ from velocity, any readout $g_\delta$ satisfying
$g_\delta(v_\delta(s,r))=ur$ needs Lipschitz constant at least
$\sqrt2/\delta$: compare the two states with the same $s$ and opposite $r$.
Their input separation is $\sqrt2u\delta$ and output separation is $2u$.
Exact state identification therefore has a diverging sensitivity requirement.
If this calibrated readout is available, its susceptibility is
$\chi(ur)=u^2/(2\epsilon)$ and detects the closing gap.

This is a parameter-family limit, distinct from observation time or mesh
refinement. Every positive-$\delta$ model has a positive gap; a uniform gap
requires a uniform premise on rates or observable response and access.

## 7. Independent composition supplies mixed-mode control (C046)

Let $Q_i$ be finite irreducible reversible generators on $n_i\ge2$ states,
with gaps $\gamma_i$, stationary measures $\pi_i$ and centered spaces
$\mathcal H_{0,i}$. With independent dynamics and unchanged constituent
clocks, $Q=Q_1\otimes I+I\otimes Q_2$. The centered product space is

$$
(\mathcal H_{0,1}\otimes1)\ \oplus\
(1\otimes\mathcal H_{0,2})\ \oplus\
(\mathcal H_{0,1}\otimes\mathcal H_{0,2}).
$$

Tensoring orthonormal eigenbases shows that $-Q$ has all sums of factor
eigenvalues, including zero. The first two sectors have smallest eigenvalues
$\gamma_1,\gamma_2$; the mixed sector has minimum $\gamma_1+\gamma_2$.
Consequently

$$
\gamma_{\rm prod}=\min(\gamma_1,\gamma_2)
\ge\min\left(\frac{\alpha_1}{S_1},\frac{\alpha_2}{S_2}\right)
$$

when each factor has §4's frame bound $\alpha_i$ and total susceptibility
$S_i$. Lifted local observables have unchanged susceptibilities, since the
other factor's constant function has norm one and eigenvalue zero.
They miss the entire mixed sector of dimension $(n_1-1)(n_2-1)$, so their
product frame has zero minimum eigenvalue. Independence supplies the missing
spectral information. A full product frame is therefore sufficient, but local
frames plus the product-generator premise already yield the displayed bound.

For masses $m_i$, write $S_i=\sum_a H_i(f_{ia})/(2m_i)$; uniform mass-family
bounds must retain these denominators. For $N$ identical two-state factors
with flip rate $\lambda$ per factor, the gap is $2\lambda$ for every $N$.
Dividing the generator by $N$ to fix the total flip rate instead gives
$2\lambda/N$. The clock choice is part of the theorem.

The tensor-eigenbasis construction is standard product-chain theory:
Levin–Peres, with contributions by Wilmer, §12.4, Lemma 12.12 and
Corollary 12.13, use weighted discrete random scan. Our additive continuous
generator and local-frame consequence are derived above; [B22](../references/batches/B22.md)
records the precise normalization and source review.

## 8. Next mechanical test and reproduction

G02 identifies two sufficient routes: uniformly calibrated full coverage, or
local coverage with independent-factor dynamics controlling mixed modes.
The next mechanical step specifies a conservative receiver and derives its
correlation and measurement scales. Interactions require a fresh estimate;
the independence premise must be replaced by a proved dynamical bound.
A09 retains preparation independence and coherent-action scale selection.

The written proofs are the mathematical verification route. Earlier scripts
are historical artifacts under the repository's hard verification rule. The
[B20 companion](../docs/batches/B20/susceptibility-source-companion.md)
records the Green–Kubo source match and the bounded prior-art coverage.
C041 is a spectral/product-chain consequence of C019; C042 is an elementary
finite-dimensional observability criterion, with no novelty claim.
