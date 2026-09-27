# The tangent groupoid, its zoom, and whole trajectories

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
   introduced in 2003 as the "elementary school" groupoid. Refinement
   consistency is a morphism property on it: classically
   $\min_y[S(x,y,r)+S(y,z,u-r)]=S(x,z,u)$, satisfied by Hamilton's principal
   function, the exact discrete Lagrangian of discrete mechanics, and for
   Galileo's constant force by the corrected action $\ell_h$ of the
   [refinement note](refinement-composition-and-limit.md), eq. (2)
   (Proposition 1); quantum mechanically the convolution law
   $K(u+v)=K(u)*K(v)$. The first is the $\hbar\to0$ tropical shadow of the
   second (Maslov dequantization).
3. **Along a quantum trajectory the ultimate velocity fails.** Quantum
   paths have Hausdorff dimension two: $\langle\Delta x^2\rangle\sim\hbar\tau/M$ over a step
   $\tau$, so $\Delta x/\tau$ diverges like $\tau^{-1/2}$. The tangent groupoid's
   $\varepsilon\to0$ fibre, where $(y-x)/\varepsilon\to v$, is reached by ballistic
   scaling; quantum trajectories need the diffusive scaling $\Delta x^2\propto\tau$,
   the user's 1998 remark that the path groupoid relates to Connes's only
   after $(x,y,\varepsilon)\mapsto(x,y,\varepsilon^2)$, and his 2003 remark on the $\sqrt t$
   of Itô's calculus. Newton's *velocitas ultima* is the ballistic
   boundary fibre, which quantum paths do not reach.

The constructions are established; the identifications are readings,
and Proposition 1 is elementary. The note gives the atlas's Newton row a
geometric home: one step is an arrow of the tangent groupoid, a
trajectory is a factorization in the time-graded groupoid, the zoom is
the renormalization, and the principal symbol is what survives.

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

**Proposition 1.** (a) A function $S(x,y,u)$ satisfies
$\min_y[S(x,y,r)+S(y,z,u-r)]=S(x,z,u)$ for all $0<r<u$ exactly when it is
a morphism of the time-graded groupoid into the $(\min,+)$ semiring. For
Galileo's constant force $F$ on a mass $M$ this holds for
$$S(x,y,u)=\frac{M(y-x)^2}{2u}+\frac{Fu}2(x+y)-\frac{F^2u^3}{24M},$$
the corrected action $\ell_u$ of the refinement note, eq. (2), which is the
action along the true path. (b) A kernel $K(x,y,u)$ satisfies
$\int K(x,y,r)K(y,z,u-r)\,dy=K(x,z,u)$ exactly when it is a morphism into the
convolution algebra; the constant-force propagator $U_u$ of the
refinement note, eq. (3), does.

*Proof.* (a) and (b) restate the morphism property. The displayed $S$ is
the classical action of the path $q(s)=x+(y-x)s/u+\frac F{2M}s(s-u)$,
which is the refinement note's $\ell_u$; its composition law is eq. (2)
there, and $U_u$'s is eq. (3). $\square$

The displayed $S$ is the exact discrete Lagrangian of discrete mechanics
([Marsden and West 2001](https://doi.org/10.1017/S096249290100006X),
metadata), and discrete Lagrangian mechanics on groupoids is
[Weinstein's (1996)](https://doi.org/10.1090/fic/007/10) (metadata). The
kick--drift--kick cell $S_h=K_{Fh/2}D_hK_{Fh/2}$ of the refinement note is
the variational (Störmer--Verlet) integrator of the trapezoidal discrete
Lagrangian $L_h$, and the cubic counterterm turns $L_h$ into the exact one.
The two laws of Proposition 1 are related by Maslov dequantization: in
Euclidean form, $-\hbar\log\int e^{-S/\hbar}\to\min S$ as $\hbar\to0$
([Litvinov 2005](https://doi.org/10.1090/conm/377/06982), metadata). So
refinement consistency of a whole trajectory is the morphism property,
tropical in classical mechanics and convolutional in quantum mechanics.

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

The atlas's Newton row gains a geometric home: one step is an arrow of
the tangent groupoid, a trajectory is a factorization in the
time-graded groupoid, refinement consistency is the morphism property
of Proposition 1, the zoom action is the renormalization, and the
principal symbol is what survives $\varepsilon\to0$. A natural next question for
the gauge atlas is the corresponding groupoid of the lattice: the
holonomy groupoid for two dimensions, where series moves are
compositions, and a higher (double) groupoid for the parallel moves of
three and four dimensions.
