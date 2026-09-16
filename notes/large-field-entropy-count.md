# The large-field region costs more action than it has unstable directions, by the factor $2\pi^2/g^2$

The question left by
[the instability note](flow-instability-large-field.md) has a
quantitative answer, and it is favourable. The expansion inside a
large-field region is **not divergent**: the configuration space is
compact, so the action attains a minimum on the closed constraint set,
and at that minimizer the Hessian is nonnegative on the tangent cone, so
the Gaussian order is well defined. What the Nielsen--Olesen instability
says is that the obvious candidate for the minimizer, a constant
chromomagnetic field, is a saddle rather than a minimum. The
quantitative question is then whether the unstable directions are too
numerous for the Boltzmann suppression to beat, and they are not. In a
constant background of magnitude $gB=\eta/\ell^2$ on a four-dimensional
block of side $\ell$, the count is
$$\#\{\text{unstable modes}\}
=\underbrace{\frac{gB\,\ell^2}{2\pi}}_{\text{Landau degeneracy}}\times
\underbrace{\frac{gB\,\ell^2}{4\pi}}_{k_3^2+k_4^2<gB}
=\frac{(gB)^2\ell^4}{8\pi^2}=\frac{\eta^2}{8\pi^2},$$
**independent of $\ell$ and of the lattice spacing**, exactly like the
action cost $S_E/\hbar\simeq\eta^2/(4g^2)$ of
[the transfer note](ground-state-measure-transfer.md) §3. Their ratio is
$$\frac{\text{action cost}}{\text{unstable-mode count}}
=\frac{\eta^2/(4g^2)}{\eta^2/(8\pi^2)}=\frac{2\pi^2}{g^2},$$
uniform in $\eta$, in $\ell$ and in the cutoff, and large at weak
coupling. So the suppression of a large-field region beats its entropy
by a factor $2\pi^2/g^2$ per unstable direction, and the sum over
large-field regions converges for $g^2<2\pi^2\simeq19.7$. The difficulty
in the large-field region is therefore **not entropic**: it is the
identification of the constrained minimizer, which the instability says
is inhomogeneous. Constants explicit; the mode count is the standard one
for a constant background and is a model estimate for the general case,
labelled as such; nothing promoted.

## 1. The expansion is not divergent

**Proposition 1.** Let $K\subset G^{\mathcal E}$ be closed and nonempty,
for instance the set where a block-averaged field strength exceeds a
threshold. Then $S_E$ attains its minimum on $K$, and at any minimizer
$U_*$ the second variation of $S_E$ is nonnegative on the tangent cone
of $K$ at $U_*$.

*Proof.* $G^{\mathcal E}$ is compact and $S_E$ continuous, so the
minimum is attained; the second-order necessary condition for a
constrained minimum gives nonnegativity of the Hessian on the tangent
cone. $\square$

So the Gaussian integral around the constrained minimum is well defined
and the expansion is not divergent at that order. The content of the
Nielsen--Olesen instability is different: the constant chromomagnetic
field satisfies $D^*G=0$, hence is stationary for the unconstrained
action, and has a negative Hessian direction, so it is **not** the
minimizer of $S_E$ on $K$. The true minimizer is inhomogeneous, and
identifying it is the work.

## 2. Counting the unstable directions

Take a constant chromomagnetic background of magnitude $B$ in the
$(1,2)$ plane and colour direction $T^3$, on a four-dimensional block of
side $\ell$. The charged gluon modes have frequencies
$$\omega^2=k_3^2+k_4^2+(2n+1)\,gB\mp2gB,$$
Landau levels in the $(1,2)$ plane and free motion in $(3,4)$, with the
spin term supplied by the curvature operator of
[the instability note](flow-instability-large-field.md) §1. The
unstable modes are $n=0$ with aligned spin and $k_3^2+k_4^2<gB$.

*Landau degeneracy.* The number of states per unit area in a level is
$gB/(2\pi)$, so over the block face of area $\ell^2$ it is
$gB\ell^2/(2\pi)$.

*Longitudinal count.* The admissible $(k_3,k_4)$ fill a disc of radius
$\sqrt{gB}$, and the density of modes in a box of side $\ell$ is
$(\ell/2\pi)^2$, giving $\pi gB\,\ell^2/(4\pi^2)=gB\ell^2/(4\pi)$.

*Total.* Multiplying, and using $gB=\eta/\ell^2$,
$$\mathcal N(\eta)=\frac{(gB)^2\ell^4}{8\pi^2}=\frac{\eta^2}{8\pi^2}.$$
The count depends on $\eta$ alone: a large-field region of given
strength carries the same number of unstable directions at every scale,
matching the scale-invariance of its action cost.

## 3. Cost against count

From [the transfer note](ground-state-measure-transfer.md) §3, the same
region costs
$$\frac{S_E}{\hbar}\simeq\frac{1}{4g^2}\Big(\frac\eta{\ell^2}\Big)^2\ell^4=\frac{\eta^2}{4g^2},$$
so

**Proposition 2.** For a large-field region of strength $\eta$ at any
scale,
$$\frac{S_E/\hbar}{\mathcal N(\eta)}=\frac{2\pi^2}{g^2},$$
independent of $\eta$, of the block size and of the lattice spacing.

The interpretation is the usual competition between energy and entropy.
Each unstable direction can be thought of as contributing at most a
bounded factor to the sum over configurations in the region, so the
region's weight is at most
$$e^{-\eta^2/(4g^2)}\,e^{C\mathcal N(\eta)}
=\exp\Big[-\frac{\eta^2}{4g^2}\Big(1-\frac{Cg^2}{2\pi^2}\Big)\Big],$$
negative in the exponent whenever $g^2<2\pi^2/C$. With $C$ of order one
this is $g^2\lesssim20$, which covers the whole weak-coupling regime in
which the renormalization steps of
[the position note](mass-gap-position.md) §6 are taken.

## 4. What this settles and what it leaves

*Settles.* The large-field region is not excluded by an entropy problem.
The number of dangerous directions grows only as fast as the action
cost, and the ratio is a fixed number times $1/g^2$. In particular the
sum over large-field regions, with the measure bound
$e^{-c\eta^2/g^2}$ of
[the transfer note](ground-state-measure-transfer.md), converges at weak
coupling even after allowing a bounded factor per unstable mode. The
answer to the question of
[the instability note](flow-instability-large-field.md) §5 is therefore
"merely slow", and the slowness is quantified: a factor $g^2/(2\pi^2)$
of the exponent is spent on the unstable directions.

*Leaves.* The identification of the constrained minimizer. The
instability says the constant field is not it, and the physical
expectation is an inhomogeneous configuration, the flux-tube or
"spaghetti" arrangement into which a constant chromomagnetic field
decays. Expanding around it requires knowing it, or at least a lower
bound on $S_E$ over the constraint set better than the constant-field
value, and that is the remaining constructive content in this corner.

*A check available in principle.* Proposition 2 predicts that the
weight of a large-field region is $\exp[-\eta^2(1-O(g^2))/(4g^2)]$ with
the correction linear in $g^2$ and independent of the scale. That is a
statement about the Euclidean measure that a lattice computation could
test, though this repository performs none.

## 5. Consequence for STATE

The entropy question is answered with an explicit ratio $2\pi^2/g^2$,
uniform in the strength of the region and in the scale, so the
large-field sum converges at weak coupling and the expansion is slow
rather than divergent. What remains in this corner is the constrained
minimizer, which the Nielsen--Olesen instability shows is inhomogeneous.
The next question, and the one that would close the corner, is a lower
bound on the Euclidean action over the constraint set that improves on
the constant-field value $\eta^2/(4g^2)$ by a factor bounded away from
zero, uniformly in the scale.
