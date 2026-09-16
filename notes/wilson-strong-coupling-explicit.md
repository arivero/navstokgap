# An explicit strong-coupling gap for the Wilson transfer matrix: $SU(3)$ is gapped for $g^2\ge176$, with $\Delta\ge(\hbar c/a)\,4\log(g^2/176)$

The threshold that Yarotsky's theorem supplies for the Kogut--Susskind
Hamiltonian is $g_0^2\sim10^{101}$
([threshold note](strong-coupling-threshold-explicit.md)). The same
statement for the other standard lattice Hamiltonian, the logarithm of
the Wilson transfer matrix, has an explicit and usable threshold,
because the Euclidean character expansion is a polymer gas of closed
plaquette surfaces with no time discretization to pay for. With
the plaquette activity $\rho$ of the fundamental representation, which
is $1/g^2$ for $SU(3)$ to leading order, the Kotecký--Preiss criterion
holds for
$$20e^2\rho\ \le\ 0.84,\qquad\text{that is}\qquad \rho\le5.7\times10^{-3},$$
and the truncated correlations of local observables then decay with
rate at least $4\log(1/(176\rho))$ per lattice unit, because the
smallest closed surface joining two distant plaquettes is a tube with
four plaquettes per unit length. Through the transfer matrix
$\mathcal T=e^{-aH_W/\hbar c}$, self-adjoint and positive by link
reflection positivity, the decay rate is a lower bound on the gap of
$H_W$ on the cyclic subspace of local observables, so for $SU(3)$
$$\Delta_W\ \ge\ \frac{\hbar c}{a}\,4\log\frac{g^2}{176}\qquad(g^2\ge176),$$
uniformly in the volume. The fully crude version, which bounds the sum
over all representations by $2N\beta_W=36/g^2$ instead of using the
fundamental alone, gives the same form with $6340$ in place of $176$.
The entropy constant $20e$ for plaquette animals is the only place with
room, and a careful count would lower $176$ to about $10^2$. The gap of
$H_W$ grows like $\log g^2$ where that of $H_{\rm KS}$ grows like $g^2$,
the two Hamiltonians being different regularizations that agree only in
the continuum limit. Constants explicit; nothing promoted.

## 1. The polymer gas

Write the Wilson weight of a plaquette in characters,
$$e^{\frac{\beta_W}{N}\operatorname{Re}\operatorname{tr}U_p}
=c_0(\beta_W)\Big[1+\sum_{r\ne0}d_r\frac{c_r}{c_0}\chi_r(U_p)\Big],
\qquad c_r=\frac1{d_r}\int e^{\frac{\beta_W}{N}\operatorname{Re}\operatorname{tr}U}\,\overline{\chi_r(U)}\,dU ,$$
with $\beta_W=2N/g^2$. Expanding the product over plaquettes and
integrating over links, a set of plaquettes with nontrivial
representations contributes only if the representations at every link
fuse to the trivial one, so every link is covered by at least two
plaquettes of the set: the surviving sets are **closed surfaces**, the
smallest being the six faces of a cube. On a closed surface carrying the
fundamental on every plaquette, the link integrals
$\int\chi_f(U_1g)\chi_f(g^{-1}U_2)dg=\chi_f(U_1U_2)/d_f$ and the vertex
closures combine to $d_f^{\chi(P)}(c_f/c_0)^{|P|}$ with $\chi(P)$ the
Euler characteristic, so the activity per plaquette along a tube, where
the vertex and link factors balance, is
$$\rho\ =\ d_f\,\frac{c_f}{c_0}\ =\ \frac{\beta_W}{2N}\big(1+O(\beta_W)\big)=\frac1{g^2}\big(1+O(g^{-2})\big)\qquad(SU(N)),$$
the textbook strong-coupling parameter. The polymers of the gas are the
connected closed surfaces, two polymers being incompatible when they
share a link, and $Z=c_0^{|\mathcal P|}\sum_{\text{compatible}}\prod w(\gamma)$.

**All representations.** The level of $r$ is the least $n(r)$ with
$r\subset(f\oplus\bar f)^{\otimes n}$, and
$|\operatorname{Re}\operatorname{tr}U|\le N$, $|\chi_r|\le d_r$ give
$d_r|c_r|/c_0\le d_r\beta_W^{n(r)}e^{2\beta_W}/n(r)!$, while
$\sum_{n(r)=n}d_r\le(2N)^n$. Hence
$$\sum_{r\ne0}d_r\frac{|c_r|}{c_0}\ \le\ e^{2\beta_W}\big(e^{2N\beta_W}-1\big)\ \simeq\ 2N\beta_W=\frac{4N^2}{g^2}=\frac{36}{g^2}\quad(SU(3)),$$
a bound $36$ times worse than the leading activity. Everything below is
stated for a per-plaquette activity $\rho$; the two readings differ only
in what $\rho$ is.

## 2. Convergence: the Kotecký--Preiss criterion with numbers

*Adjacency.* In four dimensions a link lies in six plaquettes, so a
plaquette shares a link with $4\times5=20$ others, and the number of
connected sets of $n$ plaquettes containing a given one is at most
$(20e)^{n-1}$.

*Incompatible polymers.* A polymer $\gamma'$ incompatible with $\gamma$
shares a link with it; $\gamma$ has at most $4|\gamma|$ links, each in
six plaquettes, so the number of $\gamma'$ of size $n$ is at most
$24|\gamma|(20e)^{n-1}$, and $n\ge6$.

*Criterion.* With $a(\gamma)=|\gamma|$ and $|w(\gamma')|\le\rho^{|\gamma'|}$,
the Kotecký--Preiss condition
$\sum_{\gamma'\not\sim\gamma}|w(\gamma')|e^{a(\gamma')}\le a(\gamma)$
follows from
$$\frac{24}{20e}\sum_{n\ge6}\big(20e^2\rho\big)^n\ \le\ 1
\qquad\Longleftarrow\qquad x\equiv20e^2\rho\le0.84 ,$$
since $0.4415\,x^6/(1-x)\le1$ there. So the expansion converges,
uniformly in the volume, for
$$\rho\ \le\ \frac{0.84}{20e^2}=5.7\times10^{-3}.$$

## 3. Decay of correlations and the gap

Running the criterion with $a(\gamma)=(1+\delta)|\gamma|$ instead, it
holds as long as $xe^{\delta}\le0.84$, that is for
$\delta\le\log(0.84/x)=\log(1/(176\rho))$, and then the cluster sums
carry a factor $e^{-\delta|X|}$. A cluster connecting two plaquettes at
distance $T$ contains a closed connected surface through both, whose
size is at least that of a tube, $4T$ plaquettes, so the truncated
two-point function of any two local observables at separation $T$ is
bounded by $C\,e^{-4\delta T}$:
$$m\,a\ \ge\ 4\log\frac{1}{176\rho}.$$

**Transfer.** The Wilson action is link-reflection positive, so the
transfer matrix $\mathcal T$ is self-adjoint and positive (Lüscher,
Commun. Math. Phys. 54 (1977) 283; Osterwalder and Seiler, Ann. Phys.
110 (1978) 440; metadata level), and $H_W=-(\hbar c/a)\log\mathcal T$.
For a local observable $A$ orthogonal to the vacuum,
$\langle A,\mathcal T^nA\rangle\le C_Ae^{-man}$ for all $n$ forces the
spectral measure of $A$ to vanish above $e^{-ma}$, so on the cyclic
subspace generated by local observables, which is the whole space of
the reconstructed theory,
$$\Delta_W\ \ge\ \hbar c\,m\ \ge\ \frac{\hbar c}{a}\,4\log\frac{1}{176\rho}.$$

**Numbers for $SU(3)$.**

| reading of $\rho$ | threshold $\rho\le5.7\times10^{-3}$ | gap |
| --- | --- | --- |
| leading, $\rho=1/g^2$ | $g^2\ge176$ | $\Delta_W\ge(\hbar c/a)\,4\log(g^2/176)$ |
| all representations, $\rho=36/g^2$ | $g^2\ge6340$ | $\Delta_W\ge(\hbar c/a)\,4\log(g^2/6340)$ |

The first line uses the leading term of $c_f/c_0$ and drops the higher
representations, which contribute at relative order $\beta_W$; making it
rigorous costs a factor $(1+O(1/g^2))$ in $\rho$, not the factor $36$.
The second line is rigorous as written.

## 4. Relation to the Kogut--Susskind statement

$H_W$ and $H_{\rm KS}$ are different regularizations of the same
continuum Hamiltonian. At strong coupling their gaps differ in kind:
$H_{\rm KS}$ has an electric term of order $g^2\hbar c/a$ and the flux
loop costs $(8/3)g^2\hbar c/a$ for $SU(3)$; $H_W$ has both electric and
magnetic content in $-\log\mathcal T$, and the flux loop costs
$4\log(g^2/\cdot)\,\hbar c/a$, the logarithm of the tube activity. The
Jaffe--Witten statement asks for the continuum theory and is indifferent
to the regularization, so either Hamiltonian serves for T2, and the one
with the explicit threshold is $H_W$. The anisotropic limit $a_t\to0$
that turns $\mathcal T$ into $e^{-a_tH_{\rm KS}/\hbar}$ sends the temporal
plaquette activity to one, outside the expansion, which is why the
Kogut--Susskind threshold needs a genuinely Hamiltonian expansion and
why Yarotsky's time discretization pays what it pays.

## 5. Consequence for STATE

The strong-coupling boundary of the intermediate region is now a
number: for the Wilson transfer matrix and $SU(3)$, the theory is gapped
uniformly in the volume for $g^2\ge176$ (leading activity) or
$g^2\ge6340$ (fully crude), with the gap explicit. The only constant
with room is the plaquette-animal entropy $20e$. On the weak side the
boundary is $1/g^2\gtrsim10^2$ with the crude window of
[the operator-inequality note](large-field-operator-inequality.md), and
the intermediate region between $g^2\sim10^{-2}$ and $g^2\sim2\times10^2$
is where the gap forms.
