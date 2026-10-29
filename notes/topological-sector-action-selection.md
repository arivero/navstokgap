# Topology, size stabilization and action normalization

A fixed nonzero topological sector can have a positive classical energy floor
while admitting arbitrarily small size-based action. Quadratic/quartic gradient
competition can stabilize size, but then its coefficient $b/c$ already has
action units; the common stiffness normalization remains free. Neither model
has a vacuum frequency gap or derives a quantum phase rule. The two explicit
families below test different hypotheses: actual two-dimensional static
solutions, and a three-dimensional trial family with a preferred radius.

The sector bounds, sigma/Skyrme ingredients and Derrick scaling have established
prior art. These are written conditional constructions with the source reading
levels stated below; historical checks were internal. No full field-minimizer
or global evolution theorem is inferred from a one-parameter scale minimum.

## A sector energy floor with actual solutions at every radius

Take $n(t,x)\in S^2$, $x\in\mathbb R^2$, with stiffness $\rho>0$ in
energy units, speed $c>0$ and physical Lorentzian action

$$S[n]=\frac\rho2\int dt\,d^2x
 [c^{-2}|\partial_tn|^2-|\nabla n|^2],\qquad
H=\frac\rho2\int[c^{-2}|\partial_tn|^2+|\nabla n|^2]d^2x.$$

The canonical momentum density is $\pi=\rho\partial_tn/c^2$.
Require finite energy and a smooth one-point compactification with
$n(\infty)=e_3$. Degree

$$Q=\frac1{4\pi}\int n\cdot(\partial_1n\times\partial_2n)d^2x\in\mathbb Z$$

is conserved during smooth evolutions preserving this boundary condition.
Restrict to $|Q|=1$; the model does not explain exclusion of $Q=0$.
For $a=\partial_1n$, $b=\partial_2n$, $q=n\cdot(a\times b)$,

$$|a\pm n\times b|^2=|a|^2+|b|^2\mp2q$$

proves $H\ge E\ge4\pi\rho|Q|$. For each $R>0$ the explicit field

$$n_R(x)=\frac{(2Rx_1,2Rx_2,r^2-R^2)}{r^2+R^2},\qquad r=|x|,$$

has unit norm and boundary $e_3$, and direct differentiation gives

$$|\nabla n_R|^2=\frac{8R^2}{(r^2+R^2)^2},\qquad
q_R=-\frac{4R^2}{(r^2+R^2)^2}.$$

Using $d^2x=2\pi r\,dr$ and
$\int_0^\infty r(r^2+R^2)^{-2}dr=1/(2R^2)$ gives $Q=-1$ and
$E=4\pi\rho$. Reflection reverses degree. Saturating the sector minimum
makes each a stationary solution, not just a variational trial. Its enclosed
energy is

$$E_R(r)=4\pi\rho\frac{r^2}{r^2+R^2},$$

so $R$ is its half-energy radius. As $R\downarrow0$, every member stays
smooth in the sector, while the limit is singular at the origin and its
energy measure tends weakly to $4\pi\rho\delta_0$. Gradients do not
converge strongly to the vacuum in $L^2$. Excluding the singular endpoint
does not exclude this family of preparations; no dynamical collapse or
finite-inertia dilation mode is claimed.

## Which action and which time are tested?

For the specified crossing duration $\tau_R=R/c$, a static solution has

$$\mathcal A_R=|S[n_R;0,R/c]|=E[n_R]R/c=4\pi\rho R/c\longrightarrow0.$$

This is an energy-times-crossing-time observable, not a period of oscillation
or every possible action functional. At fixed external duration $T$ the same
solutions instead have $|S|\ge4\pi\rho T$, including that supplied clock.
Their canonical motion cost $\int\pi\cdot\partial_tn$ is identically zero.
Under spacetime dilation $n_\lambda(t,x)=n(t/\lambda,x/\lambda)$ with
scaled duration, $S[n_\lambda]=\lambda S[n]$, degree and the field equation
being preserved at fixed $\rho,c$. Those constants alone supply no action
unit. A radius floor $R\ge\ell$ would add
$\mathcal A_R\ge4\pi\rho\ell/c$ within this family, using a new length.

Near the vacuum, $n=(u_1,u_2,\sqrt{1-|u|^2})$ gives
$\partial_t^2u=c^2\Delta u$, $\omega(k)=c|k|$. On
$L^2(\mathbb R^2;\mathbb R^2)$, the squared-frequency operator
$-c^2\Delta$ with domain $H^2$ has spectrum $[0,\infty)$.
Normalized packets $u_L=L^{-1}f(x/L)$ have Rayleigh quotient
$c^2L^{-2}\|\nabla f\|_2^2/\|f\|_2^2\to0$.
A periodic box with constant rotations removed has first frequency
$2\pi c/L$, which closes with volume. Within the degree-one sector,
translations $n_R(x-a)$ give square-integrable zero tangents of the static
second variation. No positive internal gap after quotienting them is asserted.
Sector energy, classical frequency and quantum Hamiltonian spectrum differ.

## A stabilized three-dimensional trial family

Now use $n:\mathbb R^3\to S^3\subset\mathbb R^4$, approaching a fixed
point at infinity, with degree $N$, and static energy

$$E[n]=\int\left[a\sum_i|\partial_in|^2+
 b\sum_{i<j}(|\partial_in|^2|\partial_jn|^2
 -(\partial_in\cdot\partial_jn)^2)\right]d^3x.$$

Here $a>0$ has units energy/length, $b>0$ energy times length. Specify
physical time by the conservative completion

$$L=\int\left[\frac a{c^2}|\dot n|^2+
 \frac b{c^2}\sum_i(|\dot n|^2|\partial_in|^2
 -(\dot n\cdot\partial_in)^2)\right]d^3x-E[n].$$

Its velocity quadratic form is positive; this is the quadratic/quartic
Lorentz completion with $x^0=ct$. Smooth solutions are assumed where they
exist; no global nonlinear well-posedness or hard-speed theorem for arbitrary
backgrounds is supplied.

If $\lambda_i$ are the singular values of $dn$, pairing
$a\lambda_i^2$ with $b\lambda_j^2\lambda_k^2$ gives static density at
least $6\sqrt{ab}\lambda_1\lambda_2\lambda_3$. The absolute Jacobian
integral bounds absolute degree and $\operatorname{vol}S^3=2\pi^2$, so

$$E\ge12\pi^2\sqrt{ab}|N|.$$

For $y=x/R$, $r=|y|$, the inverse stereographic trial profile is

$$n_R(x)=\frac{(2y_1,2y_2,2y_3,r^2-1)}{1+r^2},\quad |N|=1.$$

Its three dimensionless singular values are $2/(1+r^2)$, giving

$$A=48\pi\int_0^\infty\frac{r^2dr}{(1+r^2)^2}=12\pi^2,\qquad
B=192\pi\int_0^\infty\frac{r^2dr}{(1+r^2)^4}=6\pi^2.$$

The substitution $r=\tan u$ proves both integrals. Scaling then gives

$$E(R)=aAR+bB/R,\quad R_* =\sqrt{b/(2a)},\quad
E(R_*)=12\sqrt2\pi^2\sqrt{ab}.$$

The scale minimum is unique with second derivative $2bB/R^3>0$;
both shrinking and expansion cost energy. Shape variations are outside
this calculation. In particular $n_{R_*}$ is not asserted to solve the
static Euler–Lagrange equation.

## The remaining common normalization

For an off-shell static trial field over $T_R=R/c$, the diagnostic action is

$$\mathcal A_R=E(R)R/c=(aAR^2+bB)/c.$$

Its infimum within this family is $6\pi^2b/c$, and at the energy-optimal
radius it is $12\pi^2b/c$. The coefficient $b/c$ already has action units.
Rescaling $x=\ell y$, $t=\ell s/c$, $\ell=\sqrt{b/a}$, gives the **full**
action, including kinetic terms,

$$S=(b/c)\widetilde S[n].$$

Replacing $(a,b)$ by $(\eta a,\eta b)$, $\eta>0$, leaves the length,
classical field equations, degree and vacuum speed unchanged, while energy
and action scale by $\eta$. This varies physical stiffnesses; it does not
deny a bound with both coefficients fixed. No degenerate $\eta=0$ model is
needed for the zero-infimum countertest. At quadratic order around a vacuum,

$$L^{(2)}=a\int[c^{-2}|\dot\pi|^2-|\nabla\pi|^2]d^3x,\qquad
\Omega(k)=c|k|.$$

The quartic term has no quadratic vacuum contribution. Stabilizing a
nonzero-degree radius therefore leaves vacuum waves gapless and does not
select that sector or an absolute action normalization.

## Source evidence and consequence for STATE

Ody–Ryder [1994](https://arxiv.org/abs/hep-th/9402137v1), §2, pp. 4–7,
equations (2.1)–(2.26), was read for the static degree, square completion
and arbitrary-scale ingredients. This is a static source match; it does
not supply the Lorentzian kinetic term or crossing-time prescription.
The Lorentzian time law,
half-energy crossing diagnostic and spectrum comparison are the specified
model tests here. The generalized Skyrme-bound
[2014 source](https://arxiv.org/abs/1311.2939) was read at abstract level
only; no full-text formula match is claimed. The coefficients, trial integrals
and normalization above have written derivations.

Topology supplies a conditional sector-energy floor; gradient competition
can supply size at fixed coefficients. Neither determines physical $\hbar$,
quantum states/instruments or a universal positive action. The separate
[reciprocal-coupling test](rotation-composition-universality.md#reciprocal-mechanical-calibration) asks what
interaction fixes about relative normalizations.
