# SU(3) in four dimensions: every constant of this programme, evaluated

With the goal narrowed to $SU(3)$, each bound proved in these notes
becomes a number. The group data are
$$N=3,\quad \dim G=8,\quad
C_2(R_{\rm f})=\frac{N^2-1}{2N}=\frac43,\quad
C_2(\text{adj})=N=3,\quad
Z(G)=\mathbb Z_3,$$
in the normalization $\operatorname{tr}T^aT^b=\tfrac12\delta^{ab}$, and
the one- and two-loop coefficients are
$$b_0=\frac{11N}{48\pi^2}=\frac{11}{16\pi^2}=0.06966,\qquad
\frac{b_1}{2b_0^2}=\frac{51}{121}=0.4215 .$$
The consequences, collected: the strong-coupling criterion of
[the T2 note](strong-coupling-uniform-gap.md) reads $54/g^4\le\beta_*$;
the gap it gives is $\Delta_{a,L}\ge\tfrac23\gamma g^2\,\hbar c/a$; the
unperturbed flux-loop gap is $\tfrac83g^2\hbar c/a$; the Lieb--Robinson
velocity is $v\le96e\,c/g^2\simeq261\,c/g^2$; the exact identities are
$\Delta V=\tfrac{16}3(3|\mathcal P|-V)$ and $|\nabla V|^2\le48V$; the
number of renormalization doublings from a bare coupling
$g_{\rm UV}^2=1/2$ to a strong-coupling threshold is
$$n\simeq\frac{1}{2b_0\log2}\Big(\frac1{g_{\rm UV}^2}-\frac1{g_{\rm thr}^2}\Big)\le\frac{2}{0.0966}\simeq21,$$
fewer than the thirty of $SU(2)$ because the coupling runs faster; and
the flowed upper bound $4.26\,\hbar c/\sqrt{8t}$ is unchanged, because
in the free limit the eight gluon species multiply numerator and
denominator equally. Two features of $SU(3)$ that $SU(2)$ lacks are
recorded in Section 4: the defining representation is complex, so
$\operatorname{tr}U_p$ is complex and the plaquette term keeps only its
real part, and the centre is $\mathbb Z_3$, so a periodic box carries
$27$ electric-flux sectors instead of $8$. Constants explicit; nothing
promoted.

## 1. Group data

| quantity | value | where used |
| --- | --- | --- |
| $N$ | $3$ | everywhere |
| $\dim G$ | $8$ | free-limit species count |
| $C_2(R_{\rm f})$ | $4/3$ | flux-loop energy, T2 gap |
| $C_2(\text{adj})$ | $3$ | Jacobian curvature factor |
| centre | $\mathbb Z_3$ | flux sectors, valley minima |
| $\operatorname{tr}(1)$ in $R_{\rm f}$ | $3$ | plaquette norm $\|w_p\|\le4N\hbar c/(ag^2)=12\hbar c/(ag^2)$ |
| $b_0$ | $11/(16\pi^2)=0.06966$ | running, step count |
| $b_1/(2b_0^2)$ | $51/121=0.4215$ | the power in $a\Lambda_{\rm lat}$ |

The lattice $\Lambda$ parameter of
[the obligations map](mass-gap-obligations-lattice.md) §5 is therefore
$$a\Lambda_{\rm lat}(g)=\big(b_0g^2\big)^{-51/121}\,e^{-1/(2b_0g^2)}\big[1+O(g^2)\big],
\qquad \frac1{2b_0}=\frac{8\pi^2}{11}=7.180 .$$

## 2. The proved bounds, evaluated

**T1.** Unchanged in form: unique positive physical ground state and
$\delta(g;N_s,SU(3))>0$ at every finite lattice and coupling.

**T2** ([T2 note](strong-coupling-uniform-gap.md)). The perturbation
parameter is
$$\beta=\frac{48N^2}{g^4(N^2-1)}=\frac{48\cdot9}{8\,g^4}=\frac{54}{g^4},$$
so the criterion $\beta\le\beta_*(3,\{0,1\}^3)$ becomes
$$g\ \ge\ g_0=\Big(\frac{54}{\beta_*}\Big)^{1/4},$$
and the gap is
$$\Delta_{a,L}\ \ge\ \gamma\,\frac{g^2}{2}\,\frac43\,\frac{\hbar c}{a}
=\frac{2\gamma}{3}\,g^2\,\frac{\hbar c}{a}.$$
The unperturbed physical excitation, a single plaquette flux loop in the
fundamental, costs
$2C_2g^2\hbar c/a=\tfrac83g^2\hbar c/a$.

**Feynman--Bijl, strong coupling**
([upper-bound note](lattice-gap-upper-bounds.md) Corollary 3). At
$g=\infty$ the Haar variance is
$\operatorname{Var}(\operatorname{Re}\operatorname{tr}U_p)=\tfrac12$ for
$N\ge3$, so the two-sided statement reads
$$\frac{2\gamma}{3}g^2\,\frac{\hbar c}{a}\ \le\ \Delta^{\rm phys}_{a,L}\ \le\ 12\,g^2\,\frac{\hbar c}{a}$$
for $g$ beyond both thresholds, a ratio of $18/\gamma$ between the two
sides.

**Lieb--Robinson** ([note](lieb-robinson-kogut-susskind.md)). Four
plaquettes per link and $\|w_p\|\le12\hbar c/(ag^2)$ give
$J\le48\hbar c/(ag^2)$ and
$$v=\frac{2eaJ}{\hbar}\ \le\ \frac{96\,e\,c}{g^2}\ \simeq\ \frac{261\,c}{g^2},$$
so the lattice light cone exceeds $c$ for $g^2<261$, that is throughout
any regime of interest, and the strong-coupling correlation length is
$\xi\le C'\,a\,/(\gamma g^4)\cdot\tfrac94$.

**Exact identities** ([note](magnetic-energy-identities.md)). With
$C_2=4/3$ and $N=3$,
$$\Delta V=\frac{16}{3}\big(3|\mathcal P|-V\big),\qquad
|\nabla V|^2\le16NV=48\,V,$$
and the ground-state sum rule of that note holds with
$2C_2=8/3$.

**Blocking** ([criterion note](blocking-criterion-monotone.md)). The
block criterion is $\beta_{\rm block}=72M^2/(g^2\delta(g;M))$ and the
direct one is $\beta_{\rm direct}=24/g^4$, so the ratio at strong
coupling is $3M^2/8$ as before, blocking losing by $3/2$ already at
$M=2$.

**Small volume** ([G07](low-dimensional-mass-gap.md) Proposition 7). The
constant-mode sector has $D=3$ and gauge group $SU(3)$, so the matrix
model runs over $\vec x_i\in\mathbb R^8$ with the structure constants of
$SU(3)$ in place of the cross product; the gap keeps the form
$\delta_1^{(3)}g^{2/3}\hbar c/L$ with a pure number $\delta_1^{(3)}$
specific to the group.

## 3. The step count

With $2b_0\log2=2(0.06966)(0.6931)=0.09657$, the number of
renormalization doublings needed to run from a bare coupling to a
strong-coupling threshold is
$$n=\frac{1}{0.09657}\Big(\frac1{g_{\rm UV}^2}-\frac1{g_{\rm thr}^2}\Big).$$

| $g_{\rm UV}^2$ | $n$ to $1/g_{\rm thr}^2\to0$ | scale ratio $2^n$ |
| --- | --- | --- |
| $1$ | $10.4$ | $1.4\times10^{3}$ |
| $1/2$ | $20.7$ | $1.7\times10^{6}$ |
| $1/4$ | $41.4$ | $2.9\times10^{12}$ |

For $SU(2)$ the same table reads $15.5$, $31.1$, $62.1$, since
$b_0$ is smaller by $2/3$. **The $SU(3)$ problem needs about a third
fewer steps than $SU(2)$** at the same bare coupling, which is the only
quantitative respect in which the physical case is easier.

## 4. Two features specific to $SU(3)$

**The defining representation is complex.** For $SU(2)$,
$\operatorname{tr}U_p$ is real, and the plaquette term is the full trace;
for $SU(3)$ it is complex and the Wilson term keeps
$\operatorname{Re}\operatorname{tr}U_p$. Consequences: the bound
$\int(\operatorname{tr}U)^2dU=0$ used in
[the upper-bound note](lattice-gap-upper-bounds.md) Corollary 3 holds
for $N\ge3$ and gives Haar variance $\tfrac12$ rather than $1$; and
charge conjugation is a nontrivial symmetry, so the spectrum splits into
$C$-even and $C$-odd sectors, and the glueball channel relevant to the
gap is $C$-even.

**The centre is $\mathbb Z_3$.** The valley minima of
[the valley note](torus-valley-potential.md) §4 lie at holonomies that
are central, so there are three per direction and $27$ electric-flux
sectors on a three-torus, against $8$ for $SU(2)$. The tunnelling
barrier between them is the same $O(\hbar c/L)$, and the sector
structure is what the small-volume spectrum organizes itself by.

## 5. What does not change

The structural results are group-independent and stand as written:

- the seven closed routes of [the position note](mass-gap-position.md) §3,
  each closed by an argument that uses no property of the group beyond
  compactness and non-abelianness;
- the moment hierarchy and the reduction of $m<\infty$ to one flowed
  correlator, where the free-limit value $4.26\,\hbar c/\sqrt{8t}$ is
  unchanged because the $\dim G=8$ species multiply the susceptibility
  and the gradient term equally;
- the equivalence of T2$'$ with the absence of a zero-temperature phase
  transition;
- the three places where the non-abelian structure is isolated, all of
  which are statements about the commutator and hold for $SU(3)$ with
  the $SU(3)$ structure constants.

## 6. Consequence for STATE

Specializing to $SU(3)$ fixes every constant and shortens the step count
to about twenty-one doublings from $g_{\rm UV}^2=1/2$. It changes no
structural conclusion, and the open obligations are those of
[the position note](mass-gap-position.md) §5. The next work should be
carried out with these numbers in place, and any new bound should be
reported in them.
