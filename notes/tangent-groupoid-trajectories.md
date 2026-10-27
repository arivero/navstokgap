# The tangent groupoid, its zoom, and whole trajectories

**Correction, 2026-10-27.** The earlier numbered summary below and
corresponding passages are historical and their broad identifications
are withdrawn. The groupoid zoom is a geometric rescaling; identifying
it with integration of fluctuations or with a running physical action
constant requires additional arguments. A real-time Hamilton principal
function composes by stationary elimination on an appropriate branch,
not by an unconditional global minimum. The separate claim that
minimization is an ordinary groupoid-morphism property was also false:
§3 replaces it by a min-plus kernel semigroup and gives a counterexample.
Euclidean Brownian scaling is
not a probability law for real-time Feynman paths, and an unqualified
claim that quantum paths have Hausdorff dimension two is not justified.
The precise state-level construction, the different scales and a Gaussian
scaling test are given in the later
[tangent-groupoid formulation](groupoid-quantum-newton-states.md).
The constant-force calculation remains a separately scoped example.

**Result, 2026-09-27 (user's question: what Connes's tangent groupoid
adds, beyond the user's 1998 and 2003 readings, and whether it extends
to a whole trajectory).** Three statements.

1. **The zoom is the renormalization.** Debord and Skandalis's action of
   $\mathbb R_+^*$ on the tangent groupoid, $(x,y,\varepsilon)\mapsto(x,y,\lambda^{-1}\varepsilon)$ and
   $(x,v,0)\mapsto(x,\lambda v,0)$, is the dilation family of the
   [fifth-postulate note](principia-fifth-postulate.md) (§4, Theorem D) and
   the control transformation $h\mapsto\mu h$ of the user's 1998 note. By
   van Erp and Yuncken, pseudodifferential operators are exactly the
   distributions on the tangent groupoid that are homogeneous under the
   zoom up to smoothing terms; their restriction to $\varepsilon=0$ is the
   principal symbol. What survives the passage $\varepsilon\to0$ is therefore the
   principal symbol, a function of place and velocity together.
2. **Trajectories live on a time-graded groupoid.** The tangent groupoid
   composes chords at one fixed $\varepsilon$, and at $\varepsilon=0$ it composes only
   vectors at one point. Refining a trajectory into more pieces is an
   operation on the groupoid $(x,y,u)\circ(y,z,v)=(x,z,u+v)$ that the user
   introduced in 2003 as the "elementary school" groupoid. When a
   classical action actually minimizes, its endpoint kernels satisfy
   $\inf_y[S_r(x,y)+S_v(y,z)]=S_{r+v}(x,z)$, a semigroup law under
   min-plus convolution. This holds for Galileo's constant force in
   Proposition 1 below; general real-time principal actions require
   stationary elimination on a specified branch. Quantum kernels
   compose by integration, interpreted as operator composition when
   necessary. A Euclidean small-$\hbar$ Laplace limit can relate the
   two kernel laws under additional hypotheses.
3. **Along a quantum trajectory the ultimate velocity fails.** Quantum
   paths have Hausdorff dimension two: $\langle\Delta x^2\rangle\sim\hbar\tau/M$ over a step
   $\tau$, so $\Delta x/\tau$ diverges like $\tau^{-1/2}$. The tangent groupoid's
   $\varepsilon\to0$ fibre, where $(y-x)/\varepsilon\to v$, is reached by ballistic
   scaling; quantum trajectories need the diffusive scaling $\Delta x^2\propto\tau$,
   the user's 1998 remark that the path groupoid relates to Connes's only
   after $(x,y,\varepsilon)\mapsto(x,y,\varepsilon^2)$, and his 2003 remark on the $\sqrt t$
   of Itô's calculus. Newton's *velocitas ultima* is the ballistic
   boundary fibre, which quantum paths do not reach.

The geometric constructions are established; the broader identifications
are historical readings subject to the correction above. Proposition 1
is the separately scoped constant-force kernel calculation.

## 1. Connes's construction

For a manifold $M$, the tangent groupoid is
$\mathbb G_M=(M\times M\times(0,1])\cup(TM\times\{0\})$, with the pair-groupoid
law at each $\varepsilon>0$, the fibrewise vector addition
$(x,X)\circ(x,Y)=(x,X+Y)$ at $\varepsilon=0$, and the topology in which
$(x_n,y_n,\varepsilon_n)\to(x,v,0)$ iff $x_n\to x$ and $(y_n-x_n)/\varepsilon_n\to v$ (in a
chart). Its $C^*$-algebra is a continuous field whose fibre at $\varepsilon>0$ is
the compact operators on $L^2(M)$ and at $\varepsilon=0$ is $C_0(T^*M)$ by Fourier
transform; Connes used the deformation to prove the index theorem
(A. Connes, *Noncommutative Geometry*, Academic Press 1994, §II.5,
metadata), and the construction generalizes the Moyal rule
([Cariñena, Clemente-Gallardo, Follana, Gracia-Bondía, Rivero and Várilly 1999](https://doi.org/10.1016/S0393-0440(98)00028-X),
abstract; [Landsman 2002, arXiv:math-ph/0208004](https://arxiv.org/abs/math-ph/0208004),
abstract). The $\varepsilon=0$ fibre is where a chord has become a velocity at a
place: Newton's *velocitas ultima*, "certain and definite", with place
and velocity commuting. The fibre at $\varepsilon>0$ is noncommutative.

## 2. The zoom action and what survives

[Debord and Skandalis (2014)](https://doi.org/10.1016/j.aim.2014.02.012)
(metadata) define the action of $\mathbb R_+^*$ on the adiabatic (tangent)
groupoid displayed in the summary and identify the crossed product with
an ideal of pseudodifferential operators;
[van Erp and Yuncken (2019)](https://doi.org/10.1515/crelle-2017-0035)
(metadata) characterize pseudodifferential operators as the
distributions on the tangent groupoid, properly supported and
transversal, that are homogeneous under the zoom modulo smooth ones.
Three identifications follow (readings):

- the zoom on the $\varepsilon=0$ fibre, $v\mapsto\lambda v$, is dual on $T^*M$ to the
  scaling that carries the Moyal product with constant $\hbar$ to the one
  with constant $\lambda^{\pm2}\hbar$ (fifth-postulate note, §4);
- the user's 1998 "dressed series", invariant under $h\mapsto\mu h$
  ([arXiv:quant-ph/9803035](https://arxiv.org/abs/quant-ph/9803035),
  eq. (10)), is a zoom-invariance condition, and his Ehrenfest remark
  (eq. (11)) is the statement that the equations of motion are
  zoom-invariant (Theorem A of the fifth-postulate note);
- the principal symbol, the $\varepsilon=0$ restriction of a zoom-homogeneous
  distribution, is the classical datum that survives the limit. The
  atlas's question "what survives refinement" has here a precise answer
  for one step.

## 3. Whole trajectories: the time-graded groupoid

The user's 2003 note
([Rivero, "Flashes of noncommutativity", arXiv:math/0302285](https://arxiv.org/abs/math/0302285),
full read) introduces the groupoid over configuration space with arrows
$(x,y,u)$, $u$ an elapsed time, and law $(x,y,u)\circ(y,z,v)=(x,z,u+v)$. Its
convolution algebra has product
$(AB)(x,z,t)=\int\!\!\int A(x,y,r)\,B(y,z,t-r)\,dy\,dr$; Fourier transformation
in $t$ gives, with $\varepsilon\sim1/\hat t$, the product of the $\varepsilon>0$ part of the
tangent groupoid, so the latter's algebra sits inside the former's
(the 2003 note's second flash). Refining a trajectory is factoring an
arrow $(x,z,u)$ through intermediate points and times, which is Newton's
insertion of $t_{2.6}$.

For endpoint functions define min-plus convolution by
$$
 (A\otimes B)(x,z):=\inf_y\{A(x,y)+B(y,z)\}.
$$
It eliminates the intermediate endpoint; it does not add the action
on each individual composable pair of arrows.

**Proposition 1.** For $M>0$, constant force $F$, and $u>0$, set
$$S_u(x,y)=\frac{M(y-x)^2}{2u}+\frac{Fu}2(x+y)-\frac{F^2u^3}{24M}.$$
Then $(S_u)_{u>0}$ is a semigroup of kernels under min-plus convolution:
$S_r\otimes S_v=S_{r+v}$ for $r,v>0$. This is the corrected action
$\ell_u$ of [the refinement note](refinement-composition-and-limit.md),
equation (2). The corresponding constant-force unitary propagators
satisfy $U_{r+v}=U_rU_v$; their kernels compose by integration over
the intermediate position, in the oscillatory/distributional sense
where the real-time integrals are not absolutely convergent.

*Proof.* The sum $S_r(x,y)+S_v(y,z)$ is a strictly convex quadratic in
$y$ with unique minimizer
$$y_*=\frac{vx+rz}{r+v}-\frac{Frv}{2M}.$$
Substitution gives $S_{r+v}(x,z)$. Equivalently, $y_*$ is the value
at time $r$ of the action-minimizing constant-force path joining $x$
to $z$. The unitary law follows from the self-adjoint Hamiltonian;
its kernel statement is operator composition. $\square$

The min-plus law is not an ordinary groupoid morphism. For free motion
with $M=1$, $S_1(0,1)+S_1(1,0)=1$, whereas $S_2(0,0)=0$.
The equality holds only after minimizing over the intermediate point
($y=0$ in this example).

The displayed $S$ is the exact discrete Lagrangian of discrete mechanics
([Marsden and West 2001](https://doi.org/10.1017/S096249290100006X),
metadata), and discrete Lagrangian mechanics on groupoids is
[Weinstein's (1996)](https://doi.org/10.1090/fic/007/10) (metadata). The
kick--drift--kick cell $S_h=K_{Fh/2}D_hK_{Fh/2}$ of the refinement note is
the variational (Störmer--Verlet) integrator of the trapezoidal discrete
Lagrangian $L_h$, and the cubic counterterm turns $L_h$ into the exact one.
The laws of Proposition 1 can be related through a Euclidean Laplace
limit: under coercivity and regularity conditions,
$-\hbar\log\int e^{-S/\hbar}dy\to\inf_y S$ as $\hbar\to0$
([Litvinov 2005](https://doi.org/10.1090/conm/377/06982), metadata).
This does not turn an oscillatory real-time integral into a probability
integral, nor make every stationary real-time branch a global minimum.

## 4. Quantum trajectories miss the ultimate velocity

In a path integral the typical increment over a step $\tau$ has
$\langle\Delta x^2\rangle\sim\hbar\tau/M$, so the paths have Hausdorff dimension two
([Abbott and Wise 1981](https://doi.org/10.1119/1.12657), metadata), and
the difference quotient $\Delta x/\tau\sim(\hbar/M\tau)^{1/2}$ diverges. The tangent
groupoid reaches its $\varepsilon=0$ fibre along ballistic sequences,
$(y-x)/\varepsilon\to v$. Quantum trajectories approach along diffusive ones,
$\Delta x^2\propto\tau$: the user's 1998 remark that Connes's groupoid relates to the
groupoid of paths only after the rescaling $(x,y,\varepsilon)\mapsto(x,y,\varepsilon^2)$, and
his 2003 remark on the $\sqrt t$ of Itô's calculus, are this fact. The
dimensionless ratio $M\,\Delta x^2/(\hbar\tau)$ is the action per step in units of
$\hbar$: ballistic refinement sends it to zero (the classical limit,
Newton's ultimate velocity), diffusive refinement holds it fixed (the
[dimension ladder](dimension-ladder.md): refining makes each Newtonian
cell quantum). The failure of joint determinacy of the
fifth-postulate note is, along a trajectory, the failure of the
ballistic limit.

## 5. Consequence for STATE

The tangent groupoid organizes geometric deformation, and trajectories
can be factored in a time-graded arrow space. For the constant-force
example, refinement gives a min-plus kernel semigroup classically and
operator composition quantum mechanically; neither is an ordinary
additive morphism of individual arrows. Identifying the geometric zoom
with a particular RG integration remains a separate task. See the
[later state formulation](groupoid-quantum-newton-states.md) for the
controlled quantum/classical comparison.
