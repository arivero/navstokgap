# One blocking step: the obstruction is the variation, not the size, of the inter-block coupling

Partition the lattice into blocks of $M^3$ sites and let $P$ project onto
the tensor product of the low-energy subspaces of the blocks. The
transfer lemma then reduces the gap of the whole system to the gap of the
blocked Hamiltonian $PHP$ minus the Schur error of the straddling
plaquettes. Counting gives, per block, $6M^2$ straddling plaquettes of
norm $\|w_p\|\le4N\hbar c/(ag^2)$ each, against an intra-block gap
$\Delta_M=(\hbar c/a)\delta(g;M)$, so the naive operator-norm estimate
gives a Schur error of order
$$\frac{\|B\|^2}{\Delta_M}\ \sim\ 36M^4\,\frac{\|w\|^2}{\Delta_M}
=36M^4\,\frac{\hbar c}{a}\,\frac{16N^2}{g^4\,\delta(g;M)},$$
which exceeds the gap it is meant to preserve by a factor of order
$M^4N^2/(g^4\delta^2)$. Lemma 1$'$ of
[the Schur note](schur-error-ultraviolet.md) shows where that estimate
is wasteful: a part of the Schur term proportional to the identity shifts
all levels equally and costs nothing, and the boundary energy is exactly
of that kind. What the induction needs is the **variation** of the Schur
term over the low-energy subspace, for which a connected estimate
replaces $\|B\|^2=\big(\sum_p\|w_p\|\big)^2$ by $\sum_p\|w_p\|^2$ and so
replaces $M^4$ by $M^2$. Under that replacement one blocking step closes
when
$$\frac{\|w\|}{\Delta_M}\ \lesssim\ \frac1{M\sqrt6}\qquad\text{i.e.}\qquad
g^4\ \gtrsim\ \frac{8\sqrt6\,MN}{\gamma\,C_2(R_{\min})},$$
a fixed threshold at fixed block factor. Since the effective coupling
grows toward the infrared, the threshold, once reached, is satisfied at
every later step, so the induction closes from that scale onward. The
number of doublings needed to reach it from the cutoff is
$$n\ \simeq\ \frac{1}{2b_0\log2}\Big(\frac1{g_{\rm UV}^2}-\frac1{g_{\rm thr}^2}\Big),
\qquad b_0=\frac{11N}{48\pi^2},$$
finite and of the order of tens for realistic couplings. The whole
difficulty of the mass gap is therefore concentrated in a **finite
number of blocking steps in the intermediate coupling regime**, each of
which generates couplings beyond the Kogut--Susskind form that must be
carried along. Constants explicit; the connected estimate is stated as
the required input and is not proved here; nothing promoted.

## 1. The block decomposition and its counting

Fix a block factor $M\ge2$ and partition the periodic lattice of
$N_s^3$ sites, $N_s=MK$, into $K^3$ blocks of $M^3$ sites. Assign each
link to the block containing its midpoint, so the links are partitioned.
A plaquette is *interior* when all four of its links lie in one block and
*straddling* otherwise. Write
$$H=\sum_{\alpha}H_\alpha+\sum_{p\ \rm straddling}w_p,\qquad
H_\alpha=\frac{\hbar cg^2}{2a}\sum_{\ell\in\alpha}(-\Delta_\ell)
+\sum_{p\subset\alpha}w_p .$$

**Counting.** Each block has six faces of $M^2$ plaquettes, so
$$\#\{\text{straddling plaquettes touching one block}\}=6M^2,
\qquad \|w_p\|\le\frac{4N\hbar c}{a\,g^2},$$
with $N$ replaced by $\dim_{\rm f}$ for a general compact group, as in
[the Lieb--Robinson note](lieb-robinson-kogut-susskind.md) §1. Each
$H_\alpha$ is a Kogut--Susskind Hamiltonian on a block with free
boundary, so T1 applies to it: discrete spectrum, unique positive ground
state $\Omega_\alpha$, gap $\Delta_M=(\hbar c/a)\delta(g;M)$.

Let $\Pi_\alpha$ project onto the spectral subspace of $H_\alpha$ below a
cutoff $E_c$ chosen in the gap region, and
$$P=\bigotimes_\alpha\Pi_\alpha,\qquad A=PHP,\qquad D=\bar PH\bar P\ge\textstyle\sum_\alpha E_0^\alpha+E_c .$$
The compression $A$ is the blocked Hamiltonian: a Hamiltonian on the
product of block low-energy spaces, whose gap the induction must track.

## 2. Why the naive estimate fails

The coupling operator is $B=PH\bar P$, bounded by the sum of the
straddling terms touching the blocks involved,
$$\|B\|\ \le\ \sum_{p\ \rm straddling}\|w_p\|\ \sim\ 6M^2\cdot\frac{4N\hbar c}{a g^2}
\quad\text{per block},$$
and the transfer lemma of [the Feshbach note](weak-coupling-feshbach-reduction.md)
charges $\|B\|^2/(E_c)$ against the gap. With $E_c\sim\Delta_M$,
$$\frac{\|B\|^2}{\Delta_M}\Big/\Delta_M
\ \sim\ 36M^4\Big(\frac{\|w\|}{\Delta_M}\Big)^2
=36M^4\Big(\frac{8N}{\gamma C_2\,g^4}\Big)^2,$$
using $\Delta_M\ge\gamma(g^2/2)C_2\hbar c/a$ from
[the T2 note](strong-coupling-uniform-gap.md) at strong coupling. The
ratio exceeds one unless $g^4\gtrsim M^2N$, and at weak coupling it is
enormous. Taken at face value, real-space blocking is useless.

## 3. What the estimate is actually measuring

The quantity $\|B\|^2/\Delta_M$ is dominated by the **boundary energy**:
the second-order effect of the straddling plaquettes lowers the ground
state of the coupled system by an amount proportional to the total
boundary area, which is extensive in $M^2$ per block and has nothing to
do with the gap. Lemma 1$'$ of
[the Schur note](schur-error-ultraviolet.md) isolates that contribution:
if
$$S(E)=B(D-E)^{-1}B^*=\eta_0(E)\,\mathbb 1+R(E),\qquad
0\le R(E)\le\epsilon\,(A-a_0)+\eta_1,$$
then the constant $\eta_0$ drops out of the gap entirely and only
$\epsilon$, $\eta_1$ and the slope $\eta_0'$ enter. The boundary energy
is the constant; what survives is the dependence of the boundary energy
on **which** low-energy state of the blocks the system occupies.

**The required input.** For each straddling plaquette separately,
$w_p(D-E)^{-1}w_p$ has norm at most $\|w_p\|^2/E_c$, and its variation
across $\operatorname{ran}P$ is at most twice that. Cross terms between
two straddling plaquettes $p\neq p'$ contribute to the constant when
they are far apart and to the variation only through connected
configurations. A connected estimate of the form
$$\big\|R(E)\big\|\ \le\ C\sum_{p\ \rm straddling}\frac{\|w_p\|^2}{E_c}
\qquad\text{in place of}\qquad
\frac{\big(\sum_p\|w_p\|\big)^2}{E_c}$$
therefore replaces $M^4$ by $M^2$. This is exactly what a cluster
expansion supplies at strong coupling, and it is the one analytic input
the blocking step needs. It is stated here as a hypothesis.

## 4. The one-step inequality under that input

**Proposition (conditional).** Assume the connected estimate of Section
3 with constant $C$, and take $E_c=\Delta_M$. Then the transfer lemma
gives
$$\operatorname{gap}(H)\ \ge\ \operatorname{gap}(A)\Big(1-\epsilon\Big)-\eta_1,
\qquad \epsilon,\ \frac{\eta_1}{\Delta_M}\ \le\ 6CM^2\Big(\frac{\|w\|}{\Delta_M}\Big)^2,$$
so one blocking step preserves a positive gap whenever
$$\frac{\|w\|}{\Delta_M}\ \le\ \frac1{M\sqrt{6C}},
\qquad\text{that is}\qquad
g^4\ \ge\ \frac{8\sqrt{6C}\;M\,N}{\gamma\,C_2(R_{\min})} .$$

The threshold depends on the block factor $M$ and on the group, and on
no other scale: it is a **fixed** coupling threshold once $M$ is fixed,
say $M=2$.

## 5. The induction, and where the finite difficulty sits

Under blocking, the effective coupling of an asymptotically free theory
grows toward the infrared. If the blocked Hamiltonian $A$ were again of
Kogut--Susskind form with a coupling $g_{n+1}>g_n$, then the threshold of
Section 4, once satisfied at some step, would be satisfied at every later
step, and the induction would give a gap at all larger scales, uniform in
the volume. Two obligations remain.

*Reaching the threshold.* At the cutoff the coupling is small. With the
one-loop running written for a doubling of scale,
$$\frac1{g_{n+1}^2}=\frac1{g_n^2}-2b_0\log2,\qquad b_0=\frac{11N}{48\pi^2},$$
the number of doublings from $g_{\rm UV}$ to $g_{\rm thr}$ is
$$n\simeq\frac{1}{2b_0\log2}\Big(\frac1{g_{\rm UV}^2}-\frac1{g_{\rm thr}^2}\Big),$$
finite and logarithmic in the ratio of scales. For $SU(2)$,
$2b_0\log2=\tfrac{11}{12\pi^2}\log2\approx0.064$, so a bare coupling
$g_{\rm UV}^2=1/2$ takes of the order of thirty doublings, a scale ratio
of about $10^9$, to reach a threshold at $g_{\rm thr}^2\approx20$. The
mass gap therefore requires control of a **finite, explicitly bounded
number of blocking steps**, all of them in the intermediate regime where
neither the perturbative expansion of
[the Feshbach note](weak-coupling-feshbach-reduction.md) nor the
cluster estimate of Section 3 applies.

*Staying in the family.* The blocked Hamiltonian $A$ is a Hamiltonian on
the product of block low-energy spaces, and it contains, besides a
nearest-block plaquette term, every operator generated by the
compression: longer-range terms, terms of higher order in the block
observables, and terms without a Kogut--Susskind counterpart. Carrying a
controlled family of such Hamiltonians through the steps is the
constructive renormalization-group problem that Balaban's programme
solves on the Euclidean side in finite volume with an ultraviolet
cutoff, and which remains open beyond that.

## 6. What this step establishes

The blocking route survives the first objection: the enormous
inter-block coupling enters the gap only through its variation, and the
boundary energy, which is what makes $\|B\|$ large, is free by Lemma
1$'$. The route then needs one analytic input, a connected estimate for
the Schur variation, and one structural input, a stable family of
effective Hamiltonians. The first is a cluster expansion and is
available at strong coupling; the second is the open problem. The
quantitative shape of the difficulty is now explicit: a fixed coupling
threshold $g_{\rm thr}^4\simeq8\sqrt{6C}MN/(\gamma C_2)$, and a finite
number of steps, logarithmic in the scale ratio, to reach it.

## 7. Consequence for STATE

Step 2 of the foreseen route is written out with its constants. The two
inputs it needs are named and separated: a connected (cluster) estimate
for the variation of the Schur term, which would make the one-step
inequality unconditional at strong coupling, and a stable family of
blocked Hamiltonians, which is the constructive renormalization-group
problem. The next tractable item is the first of these at strong
coupling, where Yarotsky's expansion already produces connected
estimates of the required kind and may be readable as such directly.
