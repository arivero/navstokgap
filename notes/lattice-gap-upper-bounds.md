# Upper bounds on the lattice gap: the Feynman--Bijl inequality, the abelian structure factor and the non-abelian dressing obstruction

The single-mode (Feynman--Bijl) inequality bounds the gap of the
Kogut--Susskind Hamiltonian above by ground-state expectation values, and
three consequences follow with explicit constants. (i) For any real
gauge-invariant function $O$ of the links,
$\Delta^{\rm phys}_{a,L}\le\frac{\hbar cg^2}{2a}\sum_\ell\langle|\nabla_\ell O|^2\rangle/\operatorname{Var}O$;
for a plaquette this is $\Delta\le\hbar cg^2N/(a\operatorname{Var}\operatorname{Re}\operatorname{tr}U_p)$,
which together with the strong-coupling lower bound shows that for large
$g$ the gap is of order $g^2\hbar c/a$ on both sides. (ii) For compact
$U(1)$ the operator $O=\sum_\ell\varphi_\ell E_\ell$ is gauge invariant
without dressing, and the uncertainty principle turns the inequality into
$$\Delta\ \le\ \frac{2\hbar c}{a\,g^2}\;\frac{\hat S(k)}{\langle\cos\theta_p\rangle},
\qquad\hat S(k)=\frac{\langle\Theta_k^2\rangle}{\sum_p|(d\varphi_k)_p|^2},\quad
\Theta_k=\sum_p(d\varphi_k)_p\sin\theta_p,$$
for every lattice momentum $k$: the abelian gap is bounded by the
zero-momentum limit of the plaquette-sine structure factor, so a Coulomb
phase, where $\hat S(k)\to0$, is gapless, and T2$'$ fails for $U(1)$
exactly through this channel. (iii) For a non-abelian group no operator
linear in the electric field with c-number coefficients commutes with
Gauss's law (proved), so the same trial excitation must be dressed with a
Wilson line, and the dressing contributes to the double commutator an
electric term of order $g^2\hbar c/a$ per unit length that does not
vanish as the wavelength grows: the channel through which the abelian gap
closes is blocked by gauge invariance, which is the exact place where the
non-abelian conjecture T2$'$ parts from the abelian theorem. The
plaquette bound diverges in the continuum limit because plaquette
fluctuations are ultraviolet dominated, so the finiteness half
$m<\infty$ of the conjecture needs smeared operators, and the next
target is the same inequality for Wilson-flowed observables with a
flow-Jacobian bound uniform in $a$. Nothing here is promoted.

## 1. The inequality

Let $H$ be self-adjoint and bounded below with simple ground state
$\psi_0$ and next eigenvalue $E_1$, and let $O$ be symmetric with
$\psi_0\in D(O)$, $O\psi_0\in D(H)$ and $\langle\psi_0,O\psi_0\rangle=0$.
Then $O\psi_0\perp\psi_0$, so by the min-max principle
$$E_1-E_0\ \le\ \frac{\langle O\psi_0,(H-E_0)O\psi_0\rangle}{\|O\psi_0\|^2}
=\frac{\tfrac12\langle\psi_0,[O,[H,O]]\psi_0\rangle}{\langle\psi_0,O^2\psi_0\rangle},$$
using $[O,[H,O]]=2OHO-O^2H-HO^2$ and $(H-E_0)\psi_0=0$. If $O$ commutes
with the Gauss generators, $O\psi_0$ lies in the physical sector and the
same bound holds for $\Delta^{\rm phys}$. (Feynman, Phys. Rev. 94 (1954)
262, metadata; the argument is the two lines above.)

## 2. Functions of the links, and the strong-coupling order

Take $H=\frac{\hbar c}{a}[\frac{g^2}{2}\sum_\ell(-\Delta_\ell)+\frac2{g^2}\sum_p(N-\operatorname{Re}\operatorname{tr}U_p)]$
as in [the obligations map](mass-gap-obligations-lattice.md) §1 and a
real function $O=f(U)$ with $\langle f\rangle=0$. Then $[V,f]=0$, and
for the Laplacian $\Delta_\ell=\sum_aX_a^2$ in the left-invariant fields
$X_a$ of link $\ell$,
$$[f,[-\Delta_\ell,f]]=2\sum_a(X_af)^2=:2|\nabla_\ell f|^2,$$
because $[\Delta,f]h=(\Delta f)h+2\sum_a(X_af)(X_ah)$ and the second
commutator with $f$ removes the $(\Delta f)$ terms and leaves
$-2\sum_a(X_af)^2h$. Hence

**Proposition 1.** For every real gauge-invariant $f(U)$ with
$\langle f\rangle_0=0$,
$$\Delta^{\rm phys}_{a,L}\ \le\ \frac{\hbar cg^2}{2a}\;
\frac{\sum_\ell\langle|\nabla_\ell f|^2\rangle_0}{\langle f^2\rangle_0}.$$

**Corollary 2 (plaquette).** With $f=\operatorname{Re}\operatorname{tr}U_p-\langle\operatorname{Re}\operatorname{tr}U_p\rangle_0$:
for a link $\ell$ of $p$, $X_a\operatorname{tr}U_p=\operatorname{tr}(T^aM)$
up to a phase, with $M$ a cyclic rearrangement of $U_p$, so by the
$SU(N)$ completeness relation
$\sum_a\operatorname{tr}(T^aM)\operatorname{tr}(T^aM^\dagger)=\tfrac12[\operatorname{tr}MM^\dagger-\tfrac1N|\operatorname{tr}M|^2]\le\tfrac N2$,
and $|\nabla_\ell\operatorname{Re}\operatorname{tr}U_p|^2\le|\nabla_\ell\operatorname{tr}U_p|^2\le N/2$. Four links give
$\sum_\ell|\nabla_\ell f|^2\le2N$ and
$$\Delta^{\rm phys}_{a,L}\ \le\ \frac{\hbar c\,g^2N}{a\,\operatorname{Var}_0(\operatorname{Re}\operatorname{tr}U_p)} .$$

**Corollary 3 (two-sided strong-coupling order).** At $g=\infty$ the
ground state is the Haar measure and
$\operatorname{Var}(\operatorname{Re}\operatorname{tr}U_p)=\tfrac12\langle|\operatorname{tr}U|^2\rangle+\tfrac12\operatorname{Re}\langle(\operatorname{tr}U)^2\rangle$
equals $1$ for $SU(2)$ and $\tfrac12$ for $SU(N\ge3)$, by Peter--Weyl
orthogonality of the fundamental character and the vanishing of
$\int(\operatorname{tr}U)^2dU$ for $N\ge3$. The ground-state expectation of
a local function is continuous in $g^{-4}$ at $g=\infty$ uniformly in
the volume (Yarotsky's Theorem 1, conclusion 4, analyticity of $\omega(A)$
in the perturbation parameter; the finite-volume statement is analytic
perturbation theory of a simple isolated eigenvalue), so there is
$g_1(N)$ with $\operatorname{Var}_0\ge\tfrac14$ for $g\ge g_1$. Combined
with [the strong-coupling note](strong-coupling-uniform-gap.md),
$$\gamma\,\frac{g^2}{2}\,\frac{N^2-1}{2N}\,\frac{\hbar c}{a}\ \le\ \Delta^{\rm phys}_{a,L}\ \le\ 4N\,g^2\,\frac{\hbar c}{a}
\qquad(g\ge\max(g_0,g_1)),$$
uniformly in the lattice size. The strong-coupling gap is $g^2\hbar c/a$
times a number bounded on both sides.

**Why the plaquette says nothing about the continuum.** As $a\to0$ along
the scaling curve the links approach the identity and
$\operatorname{Var}(\operatorname{Re}\operatorname{tr}U_p)\to0$ (the plaquette
angle fluctuates on the scale $g$, and its square on the scale $g^4$),
so the right side of Corollary 2 grows without bound. The plaquette is an
ultraviolet observable whose excitation costs an energy of order
$\hbar c/a$; the finiteness half $m<\infty$ of the conjecture requires an
operator whose ratio $\sum_\ell\langle|\nabla_\ell O|^2\rangle/\operatorname{Var}O$
stays of order $a/\ell$ for a physical length $\ell$. Section 5 states
that target.

## 3. The abelian theory: the gap is bounded by a structure factor

For compact $U(1)$ write $U_\ell=e^{i\theta_\ell}$, $E_\ell=-i\partial/\partial\theta_\ell$,
$\theta_p=\sum_{\ell\in\partial p}\epsilon_{p\ell}\theta_\ell$, and
$$H=\frac{\hbar c}{a}\Big[\frac{g^2}{2}\sum_\ell E_\ell^2+\frac1{g^2}\sum_p(1-\cos\theta_p)\Big]$$
(other conventions rescale $g^2$). Gauss's law generators
$G_x=\sum_{\ell\ni x}\pm E_\ell$ commute with every $E_\ell$, so

**Lemma 4.** $O_\varphi=\sum_\ell\varphi_\ell E_\ell$ with real
$\varphi$ is gauge invariant, and $\langle O_\varphi\rangle_0=0$.

*Proof.* The $E_\ell$ commute among themselves. Charge conjugation
$\theta\mapsto-\theta$ is a unitary symmetry of $H$ under which the
unique ground state is invariant and $E_\ell\mapsto-E_\ell$. $\square$

With $[E_\ell,h(\theta)]=-i\partial_\ell h$ and the lattice curl
$(d\varphi)_p=\sum_{\ell\in\partial p}\epsilon_{p\ell}\varphi_\ell$:
$[O_\varphi,\cos\theta_p]=i(d\varphi)_p\sin\theta_p$,
$[O_\varphi,\sin\theta_p]=-i(d\varphi)_p\cos\theta_p$, hence
$$[O_\varphi,[H,O_\varphi]]=\frac{\hbar c}{ag^2}\sum_p(d\varphi)_p^2\cos\theta_p,$$
and Section 1 gives
$$\Delta^{\rm phys}\le\frac{\hbar c}{2ag^2}\,\frac{\sum_p(d\varphi)_p^2\,c_0}{\langle O_\varphi^2\rangle_0},
\qquad c_0=\langle\cos\theta_p\rangle_0,$$
where $c_0$ is independent of $p$ by translation invariance of the unique
ground state. To bound $\langle O_\varphi^2\rangle$ below use the
uncertainty relation with the gauge-invariant
$\Theta=\sum_p\psi_p\sin\theta_p$: $\langle O^2\rangle\langle\Theta^2\rangle\ge\tfrac14|\langle[O,\Theta]\rangle|^2$
with $\langle[O_\varphi,\Theta]\rangle=-ic_0\sum_p\psi_p(d\varphi)_p$.
Choosing $\psi=d\varphi$:

**Theorem 5.** If $c_0>0$, then for every real $\varphi$ on the links,
$$\Delta^{\rm phys}_{a,L}\ \le\ \frac{2\hbar c}{a\,g^2\,c_0}\;
\frac{\langle\Theta_\varphi^2\rangle_0}{\sum_p(d\varphi)_p^2},
\qquad\Theta_\varphi=\sum_p(d\varphi)_p\sin\theta_p .$$
For a plane wave $\varphi_\ell=\cos(k\cdot x_\ell)\,u_{i(\ell)}$ the
ratio is the structure factor $\hat S(k)$ of the plaquette sine at
momentum $k$, and $\Delta^{\rm phys}\le2\hbar c\,\hat S(k)/(ag^2c_0)$
for every $k\ne0$ allowed by the box.

*Proof.* Insert the uncertainty bound into the previous display:
$\langle O^2\rangle\ge c_0^2(\sum_p(d\varphi)_p^2)^2/(4\langle\Theta^2\rangle)$. $\square$

**Reading.** In a Coulomb phase $\sin\theta_p$ is a curl of a nearly
Gaussian field and $\hat S(k)\to0$ as $k\to0$; the theorem then forces
$\Delta\to0$ with the box, which is the gaplessness Guth and
Fröhlich--Spencer prove at weak coupling (abstract, B78), obtained here as
a consequence of two ground-state quantities, $c_0$ and $\hat S$. In a
confining phase $\hat S(0)>0$ and the bound is finite, consistent with
the strong-coupling gap. The theorem does not decide which phase occurs;
it shows that the abelian question T2$'$ is equivalent, at the level of
upper bounds, to the behaviour of one correlation function at zero
momentum.

## 4. The non-abelian obstruction

**Proposition 6.** Let $G$ be non-abelian and
$O=\sum_\ell\sum_a\varphi^a_\ell E^a_\ell$ with c-number coefficients.
If $O$ commutes with all Gauss generators, then $\varphi=0$.

*Proof.* Write $E^a_\ell=L^a_\ell$ for the left generators of link
$\ell$, which satisfy $[L^b_\ell,L^a_\ell]=if^{bac}L^c_\ell$, and let
$R^b_\ell$ be the right generators, which commute with all $L^a_\ell$.
The Gauss generator at $x$ is $G^b_x=\sum_{s(\ell)=x}L^b_\ell+\sum_{t(\ell)=x}R^b_\ell$
up to the sign convention. Then
$[G^b_x,O]=i\sum_{s(\ell)=x}f^{bac}\varphi^a_\ell L^c_\ell$, with no
contribution from the entering links. The $L^c_\ell$ are linearly
independent operators, so $[G^b_x,O]=0$ for all $b,x$ forces
$f^{bac}\varphi^a_\ell=0$ for all $b,c$ and every link, that is
$[\varphi_\ell,T^b]=0$ for all $b$: $\varphi_\ell$ lies in the centre of
the Lie algebra, which is trivial for a semisimple $G$. $\square$

The trial excitation of Theorem 5 therefore does not exist in the
non-abelian theory. A gauge-invariant operator linear in $E$ must carry
a Wilson line, $O=\sum_\ell\varphi_\ell\operatorname{tr}(E_\ell W_{C_\ell})$
with $C_\ell$ a closed path through $\ell$, and then $[K,O]\ne0$: the
double commutator acquires the term
$\frac{\hbar cg^2}{2a}\sum_{\ell'\in C}\langle|\nabla_{\ell'}O|^2\rangle$
of Section 2, of order $g^2\hbar c/a$ per link of $C$, which does not
decrease when $\varphi$ becomes a long-wavelength mode. The Feynman--Bijl
bound then reads
$$\Delta^{\rm phys}\le\frac{\text{magnetic term}\ (\propto g^{-2}\hat S\text{-like})+\text{string term}\ (\propto g^2|C|)}{\langle O^2\rangle},$$
and no choice of $\varphi$ removes the second numerator. This is the
precise sense in which gauge invariance blocks, for non-abelian groups,
the channel through which the abelian gap closes: the excitation that
would be a photon must be attached to a string whose electric energy is
set by the cutoff-scale coupling. It is an obstruction to proving
gaplessness, and it is consistent with T2$'$; it proves nothing in the
direction of a lower bound.

## 5. The finiteness half and the flowed-operator target

Jaffe--Witten require $m<\infty$. On the lattice every bound above is
finite, and the continuum question is whether some gauge-invariant
observable has $\frac{\hbar cg^2}{2a}\sum_\ell\langle|\nabla_\ell O|^2\rangle/\operatorname{Var}O$
bounded as $a\to0$ along the scaling curve. Plaquettes fail (Section 2).
Wilson-flowed observables (Lüscher's flow, [local companion](../docs/Luscher_WilsonFlow_1006.4518v3.md),
equations (1.1)--(2.4) at passage level) are smooth functions of the
links smeared over the physical radius $\sqrt{8t}$; for them
$\nabla_\ell O_t$ is the flow Jacobian, and the target statement is

> **T$_{\rm fin}$.** For the flowed energy density $O_t=t^2\operatorname{tr}F_t^2$
> at fixed physical flow time $t$, $\sum_\ell\langle|\nabla_\ell O_t|^2\rangle$
> is $O(a^3t^{-3/2})$ times a number uniform in $a$, so that
> $\Delta\le C(t)\,\hbar c/\sqrt{8t}$ in the continuum limit.

The ingredient to prove is a diamagnetic-type bound on the linearized
flow, which is a covariant heat equation with a curvature term; the
covariant heat kernel obeys the scalar Gaussian bound by Kato's
inequality, and the curvature term must be controlled by the flow's own
a-priori estimates. This is the next theorem-sized target on the upper
side; it delivers the finiteness half of the conjecture in the
finite-volume continuum theory once existence is available, and its
proof would be the first continuum-uniform spectral statement in this
programme.

## 6. Consequence for STATE

The upper side of the lattice route is organized: Proposition 1 is the
tool, Corollary 3 fixes the strong-coupling gap to order $g^2\hbar c/a$
on both sides, Theorem 5 reduces the abelian T2$'$ to a structure factor,
and Proposition 6 with the string term is where the non-abelian theory
escapes that reduction. Two targets follow: T$_{\rm fin}$ via flowed
observables (upper side, continuum), and, on the lower side, the
weak-coupling lattice bound of STATE step 3 whose obstruction is now
sharper: any lower-bound argument must use gauge invariance in the way
Proposition 6 shows the upper bound is forced to.
