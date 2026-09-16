# The Agmon bound controls the global excess only: the local large-field estimate does not follow

Carrying out the distance estimate of
[the Agmon note](agmon-ground-state-suppression.md) §2 with constants
changes its meaning. The rigorous chain is
$$d(U)\ \ge\ \sqrt{\frac{B'}{A'}}\int_0^{f_0}\frac{\sqrt f\,df}{\|\nabla V\|_\infty}
=\frac{2}{3}\,\frac{2}{g^2}\,\frac{f_0^{3/2}}{\|\nabla V\|_\infty},
\qquad f_0=V(U)-\bar v,$$
obtained from $|df|\le\|\nabla V\|_\infty|d\gamma|$ along any path to the
allowed region, and the gradient norm of the magnetic energy over the
whole configuration space is
$$\|\nabla V\|_\infty\ \le\ 2\sqrt{2N|\mathcal E|},$$
**extensive in the volume**. For an excess $w$ per plaquette spread over
the lattice this gives an extensive exponent,
$$\big|\Omega\big|^2\ \lesssim\ \exp\Big[-\frac{2\sqrt2}{3}\,\frac{w^{3/2}}{g^2\sqrt N}\,|\mathcal P|\Big],$$
with the same rate per plaquette as the earlier estimate when $w=O(N)$.
For an excess carried by $n$ plaquettes in a **fixed region** of a large
lattice the same chain gives $d\gtrsim n^{3/2}N/(g^2\sqrt{|\mathcal P|})$,
which tends to zero as the volume grows: the argument controls the total
magnetic energy and says nothing about a local region. The reason is
structural rather than technical. The forbidden region of the Agmon
method is defined by the **total** potential exceeding the **total**
energy, and in an extensive system a local excess never makes the total
exceed its extensive mean. So [the Agmon note](agmon-ground-state-suppression.md)
proves a thermodynamic large-deviation bound, and the local large-field
estimate that the renormalization step needs does not follow from it.
The gap between the two is the same one the Euclidean formulation closes
for free, because there the weight $e^{-S_w}$ factorizes over plaquettes.
Constants explicit; this note corrects the previous one; nothing
promoted.

## 1. The rigorous distance bound

Let $\bar v=e_0/B'$ and $f=V-\bar v$, so the allowed region is
$\{f\le0\}$ and the Agmon metric is $\sqrt{(B'/A')f}\,|dU|$ on $\{f>0\}$.

**Proposition 1.** For every $U$ with $f_0=f(U)>0$,
$$d(U)\ \ge\ \frac{2}{3}\sqrt{\frac{B'}{A'}}\;\frac{f_0^{3/2}}{\|\nabla V\|_\infty}
=\frac{4}{3g^2}\;\frac{f_0^{3/2}}{\|\nabla V\|_\infty}.$$

*Proof.* Let $\gamma$ be any path from $U$ to $\{f\le0\}$, parametrized
by arclength. Along it $|f'(s)|\le|\nabla V(\gamma(s))|\le\|\nabla V\|_\infty$,
so
$$\int_\gamma\sqrt{\tfrac{B'}{A'}f}\;ds
\ \ge\ \sqrt{\tfrac{B'}{A'}}\int_\gamma\sqrt{f}\;\frac{|f'|\,ds}{\|\nabla V\|_\infty}
\ \ge\ \frac{\sqrt{B'/A'}}{\|\nabla V\|_\infty}\int_0^{f_0}\sqrt f\,df
=\frac{2}{3}\frac{\sqrt{B'/A'}}{\|\nabla V\|_\infty}f_0^{3/2},$$
using that $f$ runs from $f_0$ to $0$. Take the infimum over $\gamma$ and
insert $\sqrt{B'/A'}=2/g^2$. $\square$

**Lemma 2.** $\|\nabla V\|_\infty\le2\sqrt{2N|\mathcal E|}$ for $SU(N)$
in the normalization of
[the obligations map](mass-gap-obligations-lattice.md).

*Proof.* For one link, $|\nabla_\ell V|\le\sum_{p\ni\ell}|\nabla_\ell\operatorname{Re}\operatorname{tr}U_p|$,
and the completeness relation of
[the upper-bound note](lattice-gap-upper-bounds.md) Corollary 2 gives
$|\nabla_\ell\operatorname{Re}\operatorname{tr}U_p|\le\sqrt{N/2}$; each link
lies in four plaquettes, so $|\nabla_\ell V|\le4\sqrt{N/2}=2\sqrt{2N}$.
Summing the squares over the $|\mathcal E|$ links gives
$\|\nabla V\|^2\le8N|\mathcal E|$. $\square$

## 2. What follows, and what does not

*Global excess.* With $f_0=w|\mathcal P|$ and $|\mathcal E|=|\mathcal P|$
in three dimensions,
$$d\ \ge\ \frac{4}{3g^2}\,\frac{(w|\mathcal P|)^{3/2}}{2\sqrt{2N|\mathcal P|}}
=\frac{\sqrt2}{3}\,\frac{w^{3/2}}{g^2\sqrt N}\,|\mathcal P| ,$$
extensive, and the Agmon estimate of
[the Agmon note](agmon-ground-state-suppression.md) Corollary 2 gives
$$\int_{\{V-\bar v\ge w|\mathcal P|\}}\Omega^2\,d\mu
\ \le\ C\exp\Big[-\frac{2\sqrt2(1-\delta)}{3}\,\frac{w^{3/2}}{g^2\sqrt N}\,|\mathcal P|\Big].$$
At $w=O(N)$ the rate per plaquette is of order $N/g^2$, as the previous
note stated.

*Local excess.* If instead the excess $nv$ sits on $n$ plaquettes of a
fixed region while the rest of the lattice is at its mean, then
$f_0=nv$ and
$$d\ \ge\ \frac{4}{3g^2}\,\frac{(nv)^{3/2}}{2\sqrt{2N|\mathcal P|}}
\ \sim\ \frac{n^{3/2}N}{g^2\sqrt{|\mathcal P|}}\ \xrightarrow[\ |\mathcal P|\to\infty\ ]{}\ 0 .$$
The bound degrades with the volume and gives nothing in the
thermodynamic limit.

## 3. Why the local statement fails structurally

The Agmon method measures tunnelling into the region where the **total**
potential exceeds the **total** energy. In an extensive system
$\bar v=e_0/B'$ is extensive, of order $N|\mathcal P|$, so a local excess
of $n$ plaquettes leaves $V$ far below $\bar v$ whenever the rest of the
lattice sits at or below its mean. Such a configuration is classically
allowed, the Agmon weight vanishes on it, and no decay is asserted.

A localized version would need a weight $\rho$ supported near the region,
subject to $A'|\nabla\rho|^2\le B'V-e_0$ **pointwise**, and that
inequality fails for exactly the same reason: its right side is a global
quantity that a local excess does not control. Repairing it requires a
local energy balance, that is, a statement that the ground-state energy
density is locally attained, which is a form of the very locality one is
trying to prove.

## 4. Consequence for the route

*What survives.* A thermodynamic large-deviation bound on the total
magnetic energy in the ground state, with the coupling dependence
$1/g^2$ and an extensive rate. It is a genuine property of the
Kogut--Susskind ground state and it is proved with explicit constants
above.

*What was claimed too strongly.* [The Agmon note](agmon-ground-state-suppression.md)
read the same estimate as a suppression of a **local** large-field
region, which is what the renormalization step needs, and that reading
does not follow. Its Sections 3 and 4 should be read with "global excess"
in place of "$n$ excited plaquettes", and its comparison with the
Euclidean Wilson weight holds only for the global statement. The
Euclidean weight $e^{-S_w}$ factorizes over plaquettes and therefore
gives the local statement immediately, which is the structural advantage
the Hamiltonian formulation lacks and which
[the typical-field note](typical-field-strength-window.md) had already
identified.

*What would close it.* Either a local energy-balance estimate for the
Kogut--Susskind ground state, or a proof that the ground-state measure
is dominated by a product-form weight,
$\Omega^2\le Ce^{-\lambda V}$ with $\lambda>0$, which is a statement of
exactly the kind the strong-coupling expansion produces and which is open
at intermediate coupling. The second is the sharper target: it is a
single inequality, it implies the local estimate by factorization, and at
$g=\infty$ it holds with $\lambda=0$.

## 5. Consequence for STATE

The Agmon route yields the global large-deviation bound and stops there.
The local estimate, which is what the decimation step requires, needs a
pointwise domination of the ground state by a Gibbs weight,
$\Omega^2\le Ce^{-\lambda V}$ with $\lambda>0$ uniform in the volume.
That is now the single sharpest open question in this line, it is
elementary to state, and the strong-coupling case should be provable by
perturbation theory around $\Omega\equiv1$.
