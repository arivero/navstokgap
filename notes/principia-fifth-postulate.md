# A fifth postulate for the Principia: joint determinacy of place and motion

**Result, 2026-09-27; revised the same day after an adversarial Fable
review.** The user's goal: identify the statement of the *Principia* whose
change gives mechanics with $h>0$, as the parallel postulate does for
curved geometry. The proposed statement is **joint determinacy**: every
body admits states in which its place and its quantity of motion are
given together, sharply, at one instant. Newton asserts it in the
scholium closing Book I, Section I, as his reply to the objection that a
vanishing ratio is not ultimate before the quantities vanish and is
nothing once they have: the ultimate velocity is "the very velocity with
which the body reaches its last place", a limit "certain and definite"
(§1). A place belongs to an instant and a motion to an interval; the
classical debate from Zeno's arrow onward keeps them apart, and Newton's
ultimate velocity joins them.

Joint determinacy can be denied in two ways: in the algebra of
observables (they cease to commute) or in the states (a restriction on
which states are admissible). For the algebraic denial the analogy with
Euclid's fifth postulate holds in the following precise, partial sense.

1. **Independence (Theorem A).** For every real $\hbar$, the Moyal product
   $*_\hbar$ satisfies Newton's second law as an identity of observables
   (Heisenberg form), and for Newton's integrable cases (inertia, uniform
   gravity, the force proportional to distance of Book I, Proposition X)
   every observable evolves by the classical flow. Relative to these
   Heisenberg-form axioms, commutativity is undecided.
2. **One constant (Theorem B, Gutt's theorem in this setting).** Every
   associative product on the polynomial observables that deforms the
   commutative one, respects complex conjugation, and is covariant under
   the affine symplectic group (premise (H2), stated and justified in §4)
   is a Moyal product with one real constant $\hbar$, of the units of
   action. The state route adds one constant too (Theorem B$'$): a
   covariant, noise-closed restriction on the Gaussian states is
   $\sqrt{\det\Sigma}\ge\zeta$, with $\zeta=\hbar/2$ in quantum mechanics.
3. **The floor (Theorem C).** For $\hbar\ne0$, every state obeys
   $\Delta q\,\Delta p\ge|\hbar|/2$, and every recorded comparison of the
   inertial line with the constant-force parabola, whose enclosed area
   Newton takes to zero in Lemmas X and XI, obeys the floor of the
   [Planck paper](planck-gap-paper.md), Theorem 6, with $|\hbar|$ in place
   of $\hbar$. For $\hbar=0$ with all states admissible, point states give
   zero undetermined disturbance, so there is no floor.
3b. **Complementarity (Theorem E).** For $\hbar\ne0$, no state confines place and
   momentum to windows of half-widths $a$, $b$ with probabilities at least
   $1-\epsilon$ unless $\lambda_0(ab/|\hbar|)\ge(1-2\epsilon)^2$ (Landau--Pollak--Slepian):
   a non-Gaussian floor on the area $ab$. Bohr's Como statement of
   complementarity names the classical "union" of space-time co-ordination
   and causality that this denies (§6b).
4. **Similarity (Theorem D).** The action-rescaling map
   $(q,p)\mapsto(\lambda q,\lambda p)$ preserves the product $*_\hbar$ only for
   $\hbar=0$; up to isomorphism there are two products, commutative and
   Moyal. This is the mechanical counterpart of Wallis's form of the
   fifth postulate (similar figures of every size) and of the absolute
   length of Lambert and Gauss, in the sense made precise in §6.

**Where the analogy stops.** The state route reaches the same floor
without noncommutativity: GPT-6 Astra's
[routes note](newton-indeterminacy-routes.md) proves the same floor in a
commutative theory with a Gaussian covariance restriction, with
$h_*=2\zeta$. So "floor if and only if $\hbar\ne0$" holds only with the
state-completeness premise of Theorem C(c). Noncommutativity is the
unique *algebraic* denial of joint determinacy under (H1)--(H3); it is
one of two denials. And (H2) is a premise about the observables,
Weyl or Groenewold covariance, which the *Principia* does not supply.

The thesis that the constant enters as a consistency condition, and the
classical origin of the complex exponential, are in the user's
[1998 note](https://arxiv.org/abs/quant-ph/9803035); §7 reads Theorems
A--D against it and against Connes's tangent groupoid, whose $\varepsilon=0$
boundary is Newton's ultimate velocity.

The mathematics is established. Moyal's product
([Moyal 1949](https://doi.org/10.1017/S0305004100000487), metadata);
Groenewold's reduction of its bracket to the Poisson bracket for
quadratic functions
([Groenewold 1946, *Physica* 12, 405](https://doi.org/10.1016/S0031-8914(46)80059-4),
metadata) and van Hove's no-go for quantizing all observables
([van Hove 1951](https://doi.org/10.3406/barb.1951.70660), metadata);
Vey's deformations of the Poisson bracket
([Vey 1975](https://doi.org/10.1007/BF02565761), metadata); the
deformation-quantization programme
([Bayen, Flato, Fronsdal, Lichnerowicz and Sternheimer 1978, I](https://doi.org/10.1016/0003-4916(78)90224-5),
metadata), whose authors framed quantization as a deformation in the
spirit of the passage to non-Euclidean and relativistic physics
([Flato 1982](https://doi.org/10.1007/BF01596202);
[Sternheimer 1998](https://doi.org/10.1063/1.57093); metadata). The
uniqueness in Theorem B is Gutt's theorem: the Moyal product is the
unique $Sp(2n,\mathbb R)\ltimes\mathbb R^{2n}$-invariant and covariant star
product (S. Gutt, *Mém. Acad. Roy. Belg. Cl. Sci.* 44:6, 1983, as cited in
[Duval, El Gradechi and Ovsienko 2004](https://doi.org/10.1007/s00220-003-0973-7),
passage); the associativity step is Fletcher's
([Fletcher 1990](https://doi.org/10.1016/0370-2693(90)90300-U), metadata);
equivalence classes of invariant products are parametrized by
[Bertelson, Bieliavsky and Gutt (1998)](https://doi.org/10.1023/A:1007598606137)
(metadata). Robertson's inequality is
[Robertson 1929](https://doi.org/10.1103/PhysRev.34.163) (metadata). The
contribution here is the identification of Newton's *velocitas ultima* as
the statement concerned, and the reading of Theorems A--D against the
parallel postulate, with the limits just stated.

## 1. The textual anchor

A place is predicated of an instant; a quantity of motion, of an
interval. The distinction is the substance of Zeno's arrow and of
Aristotle's thesis that nothing moves in the now (*Physics* VI; cited by
book only, the Greek is not held in this repository). Newton addresses
it in the second paragraph of the scholium closing Book I, Section I
(1687 text, held in the
[Latin companion](../docs/classics/Newton_Principia_1687_BookI_SectI_scholia_la_wikisource.md),
added 2026-09-27 at the user's prompting):

> Objectio est, quod quantitatum evanescentium nulla sit ultima
> proportio; quippe quæ, antequam evanuerunt, non est ultima, ubi
> evanuerunt, nulla est. Sed & eodem argumento æque contendi posset
> nullam esse corporis ad certum locum pergentis velocitatem ultimam.
> [...] Per velocitatem ultimam intelligi eam, qua corpus movetur neq;
> antequam attingit locum ultimum & motus cessat, neq; postea, sed tunc
> cum attingit, id est illam ipsam velocitatem quacum corpus attingit
> locum ultimum & quacum motus cessat. [...] Extat limes quem velocitas
> in fine motus attingere potest, non autem transgredi. Hæc est velocitas
> ultima. [...] Cumq; hic limes sit certus & definitus, Problema est vere
> Geometricum eundem determinare.

"The objection is that vanishing quantities have no ultimate proportion,
since before they vanish it is not ultimate and when they have vanished
it is none. By the same argument one could claim that a body reaching a
given place has no ultimate velocity [...]. By the ultimate velocity is
meant that with which the body moves neither before it reaches its last
place and the motion ceases, nor after, but when it reaches it, that is,
the very velocity with which the body reaches its last place [...]. There
is a limit which the velocity at the end of the motion can reach and not
pass. This is the ultimate velocity. [...] And since this limit is
certain and definite, determining it is a truly geometrical problem."

A velocity, a ratio over an interval, is here assigned as a certain and
definite quantity to the instant of arrival at a place. The third
paragraph adds that the compared quantities are "semper diminuendas sine
limite", always to be diminished without limit. The scholium defends the
lemmas of Section I; Newton applies those lemmas to the sagitta of Lemma X
and the polygon of Proposition I, and the Scholium to the Definitions
defines motion as "translatio corporis de loco [...] in locum" (location
only; the Latin of that scholium is not held here). For a geometrical
ratio the thesis is a theorem about limits and holds in every model
below. For a *recorded* comparison, where the place is read at an
instant and the motion inferred over an interval, it becomes the claim
that states exist in which both are sharp. That claim is joint
determinacy. What remains interpretive is the extension from the
geometrical thesis to records, which Newton did not distinguish.

**Earlier authors on the arrow and uncertainty.** Bohm's *Quantum Theory*
(Prentice-Hall, 1951, ch. 8, pp. 145--148) discusses Zeno's arrow while
contrasting classical definite position and velocity with the quantum
description (passage as reported from a transcription by the GPT-6 Astra
bibliography search of 2026-09-27; not checked here). Landsberg,
*Seeking Ultimates* (IOP, 2nd ed., 2000, p. 124) connects velocity over an
interval, uncertain position and the arrow (passage as reported).
[Vaidman (2008)](https://doi.org/10.1038/451137a) links the arrow's
momentum and localization to Heisenberg's relation before turning to the
quantum Zeno effect (passage as reported; DOI verified).
[Goyal (2026)](https://doi.org/10.1007/s10701-026-00922-0), §VI.1, ties
the arrow to Bohr's complementarity of coordination and causality
(passage as reported; DOI verified). Wagstaff (*Philosophy Now* 45, 2004)
argues that exact position and exact momentum cannot be represented at
once, since one needs an instant and the other an interval (passage).
[Lynds (2003)](https://doi.org/10.1023/A:1025361725408) proposes an
indeterminacy that enables motion and distinguishes it explicitly from
the indeterminacy of $h$ (passage as reported). The philosophical debate
on instantaneous velocity is
[Arntzenius (2000)](https://doi.org/10.5840/monist20008328) and
[Smith (2003)](https://doi.org/10.1016/S1355-2198(03)00007-8) (abstracts).
The quantum Zeno effect of Misra and Sudarshan is a different phenomenon.
No author found connects Newton's *velocitas ultima* to uncertainty; the
statement reports the reach of the search.

## 2. The family of products

Observables of one degree of freedom (the transverse coordinate of
Galileo's comparison) are polynomials in $q$ and $p$ with complex
coefficients. Write $\mu(f\otimes g)=fg$ and

$$P=\partial_q\otimes\partial_p-\partial_p\otimes\partial_q,\qquad
f*_\hbar g=\mu\circ\exp\Bigl(\frac{i\hbar}2P\Bigr)(f\otimes g),$$

a finite sum on polynomials. For $\hbar=0$ it is the commutative product;
$q*_\hbar p-p*_\hbar q=i\hbar$. The Moyal bracket is
$\{f,g\}_\hbar=(f*_\hbar g-g*_\hbar f)/(i\hbar)=\frac2\hbar\,
\mu\circ\sin(\frac\hbar2P)(f\otimes g)$, with $\{f,g\}_0$ the Poisson bracket.

## 3. Theorem A: independence from the Laws in Heisenberg form

**Theorem A.** Let $H=p^2/(2M)+V(q)$ with $V$ a polynomial and $M>0$.
For every real $\hbar$:

(a) $\{q,H\}_\hbar=p/M$ and $\{p,H\}_\hbar=-V'(q)$: the Heisenberg
equations are Newton's second law, $M\ddot q=-V'(q)$, as an identity of
observables;

(b) if $\deg V\le2$ (inertia $V=0$, uniform gravity $V=-Fq$, the force
proportional to distance of Book I, Proposition X, $V=kq^2/2$), then
$\{f,H\}_\hbar=\{f,H\}_0$ for every $f$: every observable evolves by the
classical flow $\varphi_t$, and each $\varphi_t$ is an automorphism of $*_\hbar$.

*Proof.* The bracket $\{f,g\}_\hbar$ is the Poisson bracket plus terms
$\hbar^{2j}\,\mu\,P^{2j+1}(f\otimes g)$, $j\ge1$, each of which puts at
least three derivatives on each factor; they vanish if one factor has
degree at most two. This gives (a) because $q$ and $p$ have degree one,
and (b) because $H$ has degree two. The flow of a quadratic Hamiltonian
is an affine symplectic map, under which $*_\hbar$ is covariant:
translations commute with the constant-coefficient operator $P$, and a
linear map of determinant one leaves $P$ invariant. $\square$

The independence is relative to axioms stated in Heisenberg form: the
Laws as identities of observables and the classical evolution of
Newton's integrable cases. Both the commutative product and every Moyal
product satisfy them.

## 4. Theorem B: one action constant, under covariance

Consider products $f*g=\mu\circ B(f\otimes g)$ on $\mathbb C[q,p]$ with $B$ a
bilinear map. On polynomials every bilinear map can be written as a
formal bidifferential operator
$B=\sum c_{\alpha\beta}(q,p)\,\partial^\alpha\otimes\partial^\beta$, so this is no
restriction. Assume:

- (H1) $*$ is associative with unit 1, and $c_{00}=1$;
- (H2) $*$ is covariant under the affine symplectic group: for every
  translation and every linear map $A$ of determinant one,
  $(f\circ A)*(g\circ A)=(f*g)\circ A$;
- (H3) $\overline{f*g}=\bar g*\bar f$.

**What (H2) says, and what it does not follow from.** By Theorem A(b),
the flows of Newton's integrable cases are affine symplectic maps: free
flight is a shear, uniform gravity adds translations, and the harmonic
flow is a rotation in suitable units; shears and rotations generate the
group of linear maps of determinant one. (H2) requires that these flows
act by automorphisms of the product, that is, that quadratic observables
evolve classically in the deformed theory as well. The Laws alone do not
impose it. The product
$f*g=\mu\circ\exp(\frac{i\hbar}2P+\sigma\,\partial_q\otimes\partial_q)(f\otimes g)$,
$\sigma\in\mathbb R$, is associative and unital, satisfies (H3), is covariant
under translations and shears, and satisfies Theorem A(a) verbatim; it
fails only under the harmonic rotation, where the product $q\,p$ drifts by
a term proportional to $\sigma k$ (reviewer's counterexample). So (H2) is a
premise of Weyl or Groenewold covariance, physically natural (the
kinematics of composing observables is the same along Newton's
integrable motions) and outside the *Principia*.

**Theorem B.** Under (H1)--(H3), $*=*_\hbar$ for a unique real $\hbar$, of
the units of action.

*Proof.* Translation covariance makes the coefficients $c_{\alpha\beta}$
constant. Then $B$ is a formal power series in the components of two
vectors $u=\partial^{(1)}$, $v=\partial^{(2)}$, invariant under the simultaneous
action of the determinant-one linear maps; by the first fundamental
theorem of invariant theory for $SL(2)$, it is a function of
$\det(u,v)=P$ alone: $B=F(P)$, $F(0)=1$. For three factors put $x=P_{12}$,
$y=P_{13}$, $z=P_{23}$; the three $2\times2$ minors of a $2\times3$ matrix are
algebraically independent, and associativity reads
$F(x)F(y+z)=F(z)F(x+y)$ as formal series. At $z=0$ this is
$F(x)F(y)=F(x+y)$, so $F(x)=e^{\kappa x}$ (Fletcher's step). Exchanging the
factors reverses $P$ and conjugation leaves it real, so (H3) gives
$\bar\kappa=-\kappa$: $\kappa=i\hbar/2$ with $\hbar$ real. $P$ carries the reciprocal
units of $q\,p$. $\square$

**The state route also adds exactly one constant.** The second denial
of joint determinacy keeps the commutative algebra and restricts the
states. For Newton's quadratic cases the natural class is the Gaussian
states, which quadratic flows preserve (§7 explains why the quadratic
case is exact). A Gaussian state of one degree of freedom has mean
$m\in\mathbb R^2$ and covariance $\Sigma>0$; write $\nu(\Sigma)=\sqrt{\det\Sigma}$, which has
the units of action.

**Theorem B$'$.** Let $\mathcal G$ be a nonempty set of nondegenerate Gaussian states
that is (i) invariant under the affine symplectic group, the flows of
Newton's integrable cases (as in (H2)), and (ii) closed under adding
independent Gaussian noise, $\Sigma\mapsto\Sigma+K$ with $K\ge0$, which is what
forgetting or coarse-graining a record does. Then there is a unique
$\zeta\ge0$ with $\{\nu(\Sigma):\Sigma\in\mathcal G\}=[\zeta,\infty)$ or $(\zeta,\infty)$: the
admissible Gaussian states are exactly those with $\sqrt{\det\Sigma}\ge\zeta$ (up
to the endpoint). The constant $\zeta$ has the units of action; $\zeta=0$ is
joint determinacy (states arbitrarily close to point states), and
$\zeta>0$ is the state-route denial of GPT-6 Astra's
[routes note](newton-indeterminacy-routes.md), whose Theorem F gives the
floor with $h_*=2\zeta$.

*Proof.* By Williamson's theorem in one degree of freedom, every
$\Sigma>0$ is $S(\nu I)S^{\sf T}$ with $S$ of determinant one and $\nu=\nu(\Sigma)$;
translations move the mean. So the affine symplectic group acts
transitively on the Gaussian states with a given $\nu$, and by (i) $\mathcal G$ is
a union of such levels, fixed by a set $N\subset(0,\infty)$ of allowed $\nu$. By
(ii), if $\nu\in N$ then $\Sigma+\kappa I\in\mathcal G$ for all $\kappa\ge0$, and
$\nu(\Sigma+\kappa I)$ increases continuously from $\nu$ to $\infty$; so $N$ is an
interval unbounded above. Set $\zeta=\inf N$. $\square$

In quantum mechanics the Gaussian states obey the Robertson--Schrödinger
bound $\det\Sigma\ge\hbar^2/4$, so $\zeta=\hbar/2$ there, and Astra's $h_*=2\zeta$ equals
$\hbar$. The two routes of denial each add exactly one action constant,
the algebraic one $\hbar$ (Theorem B) and the Gaussian-state one $\zeta$
(Theorem B$'$). They coincide in quantum mechanics, and no further
premise here makes them coincide in general.

**Two products up to isomorphism.** The dilation
$D_\lambda(q,p)=(\lambda q,\lambda p)$ satisfies
$P((f\circ D_\lambda)\otimes(g\circ D_\lambda))=\lambda^2(P(f\otimes g))\circ D_\lambda$,
so $f\mapsto f\circ D_\lambda$ is an isomorphism from $*_{\lambda^2\hbar}$ to $*_\hbar$, and
$(q,p)\mapsto(q,-p)$ carries $*_\hbar$ to $*_{-\hbar}$. All products with $\hbar\ne0$
are isomorphic, and distinct from the commutative one. Geometry has
three constant-curvature classes; this algebraic family has two.

## 5. Theorem C: the floor on the recorded comparison

A state is a linear functional $\omega$ with $\omega(1)=1$ and
$\omega(\bar f*_\hbar f)\ge0$; it is regular if its GNS representation
integrates to Weyl operators.

**Theorem C.** (a) For $\hbar\ne0$ every state satisfies
$\Delta q\,\Delta p\ge|\hbar|/2$.

(b) For $\hbar\ne0$, consider the comparison of the inertial line with the
constant-force parabola over a cell of duration $\tau$, with fall
$s=F\tau^2/(2M)$ and impulse $J=F\tau$ (the Planck paper's convention), made
by any instrument coupled unitarily to the body, with regular joint
states, deciding between the two hypotheses for every initial state
with error probability at most $\epsilon<\frac12$. Then the undetermined
impulses $\hat D_j$ and displacements $\hat X_j$, with spreads taken as
suprema over the interpolating states of the Planck paper, satisfy

$$\frac s8\sum_j\Delta(\hat D_j)+\frac J2\sum_j\Delta(\hat X_j)\ \ge\
|\hbar|\arcsin(1-2\epsilon)>0 .$$

(c) For $\hbar=0$, if every probability measure on phase space is an
admissible state of body and pointers (state completeness), there is no
floor: a pointer prepared at $p_y=0$ and coupled by $g\,q\,p_y$ reads $q$
with delivered impulse $D=0$ and displacement $X=0$.

*Proof.* (a) Cauchy--Schwarz for the positive form
$(f,g)\mapsto\omega(\bar f*_\hbar g)$ applied to $q-\omega(q)$ and $p-\omega(p)$,
with $q*_\hbar p-p*_\hbar q=i\hbar$ (Robertson). (b) By the Stone--von Neumann
theorem a regular representation is a multiple of the Schrödinger
representation with constant $\hbar$; the multiplicity space is absorbed
into the apparatus. Theorem 6 of the Planck paper is proved from the
Weyl relations and Mandelstam--Tamm in the Bures angle, which is
independent of the representation, under exactly these quantifiers; for
$\hbar<0$ apply the reflection $(q,p)\mapsto(q,-p)$. (c) The coupling moves the
pointer by $gq$ and kicks the body by $-gp_y=0$. $\square$

The floor bounds the part of the comparison that Newton's scholium says
is to be diminished without limit: the recorded fall and impulse. Part
(c) shows that the floor needs either noncommutativity or a restriction
of states; Astra's routes note realizes the second in a commutative
theory with the same constants.

## 6. Theorem D: similarity

**Theorem D.** For $\lambda\ne\pm1$, $D_\lambda$ is an automorphism of the
associative product $*_\hbar$ if and only if $\hbar=0$.

*Proof.* $D_\lambda$ carries $*_{\lambda^2\hbar}$ to $*_\hbar$, and $*_{\lambda^2\hbar}=*_\hbar$ iff
$\lambda^2\hbar=\hbar$. $\square$

The statement concerns the product, the structure that records see.
$D_\lambda$ also multiplies the Poisson bracket by $\lambda^2$, so it is not an
automorphism of the classical Poisson algebra either; for the dynamics
it is a similarity that rescales actions, in both theories. The honest
form of the analogy is therefore the one stated in the
[dimensional note](action-unit-dimensional-selection.md), Theorem B:
similar records at every scale exist exactly when no absolute action is
available. Wallis replaced Euclid's fifth postulate by the existence of
similar figures of different size; Lambert and Gauss saw that its
negation brings an absolute length. Theorem D is the counterpart for the
product of observables, with $\hbar$ as the absolute action.

## 6b. Complementarity: the negated postulate in Bohr's words and in exact form

Bohr's founding statement of complementarity names Newton's joint
determinacy as the thing given up. In the Como lecture
([Bohr 1928, *Nature* 121, 580](https://doi.org/10.1038/121580a0), p. 580;
the sentence checked as quoted in
[Busch and Shilladay 2006, arXiv:quant-ph/0609048](https://arxiv.org/abs/quant-ph/0609048),
§2.2.1):

> The very nature of the quantum theory thus forces us to regard the
> space-time co-ordination and the claim of causality, the union of which
> characterizes the classical theories, as complementary but exclusive
> features of the description, symbolizing the idealization of
> observation and definition respectively.

Space-time co-ordination is the place at an instant; the claim of
causality is the quantity of motion governed by the Laws and conserved
by the third. Their union is the *velocitas ultima* of §1, and Bohr's pair
"observation and definition" is the distinction of §1 between the
recorded comparison and the geometrical thesis. So the negated fifth
postulate has a name, and its author stated it as a negation of the
classical union.

It also has an exact, non-Gaussian form. Write $P_a$ for the spectral
projection of $q-q_0$ on $[-a,a]$ and $Q_b$ for that of $p-p_0$ on $[-b,b]$.

**Theorem E (complementarity).** Let $\hbar\ne0$ and $c=ab/|\hbar|$. For every
state, the probabilities $\alpha^2=\langle P_a\rangle$ and $\beta^2=\langle Q_b\rangle$
satisfy

$$\arccos\alpha+\arccos\beta\ \ge\ \arccos\sqrt{\lambda_0(c)},$$

where $\lambda_0(c)<1$ is the largest eigenvalue of the time- and
band-limiting operator of Slepian and Pollak, increasing in $c$, with
$\lambda_0(c)\simeq2c/\pi$ for small $c$. In particular, a state (a posterior
after records) that confines the place to a window of half-width $a$ and
the momentum to one of half-width $b$, each with probability at least
$1-\epsilon$, $\epsilon<\frac12$, obeys

$$\lambda_0\Bigl(\frac{ab}{|\hbar|}\Bigr)\ \ge\ (1-2\epsilon)^2,
\qquad\text{so}\qquad ab\ \ge\ |\hbar|\,c_*(\epsilon),\quad
c_*(\epsilon)=\lambda_0^{-1}\bigl((1-2\epsilon)^2\bigr)>0 .$$

For $\epsilon\to0$ no state reaches it at all: a nonzero wavefunction and
its Fourier transform cannot both vanish outside sets of finite measure.
For $\hbar=0$ with all states admissible, point states give $\alpha=\beta=1$ for
every $a,b>0$, and there is no bound.

*Proof.* In the Schrödinger representation $p=-i\hbar\,d/dq$, so confining
$p$ to $[-b,b]$ is band-limiting the wavefunction to spatial frequencies
$|\nu|\le b/(2\pi|\hbar|)$. With the interval length $2a$, the Slepian parameter
$c=\pi WT$ equals $\pi\cdot\frac b{2\pi|\hbar|}\cdot2a=ab/|\hbar|$ (equivalently $c=\Omega T/2$
with the angular band $\Omega=b/|\hbar|$); the shifts $q_0,p_0$ are removed by
a translation and a boost. With $D=P_a$, $B=Q_b$ one has
$\|DB\|=\sqrt{\lambda_0(c)}$
([Slepian and Pollak 1961](https://doi.org/10.1002/j.1538-7305.1961.tb03976.x)).
For a pure state $f$: if $\alpha\beta=0$ the left side is at least
$\pi/2>\arccos\sqrt{\lambda_0}$. Otherwise put $g=Df/\alpha$, $h=Bf/\beta$; then
${\rm Re}\langle f,g\rangle=\alpha$, ${\rm Re}\langle f,h\rangle=\beta$ and
$|\langle g,h\rangle|=|\langle Df,DB\,Bf\rangle|/(\alpha\beta)\le\sqrt{\lambda_0}$. The angle
$d(x,y)=\arccos{\rm Re}\langle x,y\rangle$ is the geodesic distance on the unit sphere
of the underlying real Hilbert space, so
$\arccos\sqrt{\lambda_0}\le d(g,h)\le d(g,f)+d(f,h)=\arccos\alpha+\arccos\beta$
(proof supplied by the reviewer).
[Landau and Pollak (1961)](https://doi.org/10.1002/j.1538-7305.1961.tb03977.x)
(passage, as read by the reviewer in the archive.org scan) show that the
inequality is sharp and characterize the attainable pairs in four cases;
it binds only when $\alpha^2,\beta^2\ge\lambda_0$ and holds everywhere as a necessary
condition, which is all that is used here. Mixed states: in the
coordinates $u=\alpha^2+\beta^2-1$, $v=\alpha^2-\beta^2$ the boundary is an arc of the
ellipse $(u/\cos\theta_0)^2+(v/\sin\theta_0)^2=1$, $\theta_0=\arccos\sqrt{\lambda_0}$, centred
at $(\frac12,\frac12)$, inscribed in the unit square and tangent to its sides at
$(\lambda_0,1)$ and $(1,\lambda_0)$, where the arc ends. The allowed set is the
square with that one corner rounded off, a convex set, and
$(\langle P_a\rangle,\langle Q_b\rangle)$ is linear in the state. With $\alpha,\beta\ge\sqrt{1-\epsilon}$,
$\arccos\sqrt{1-\epsilon}=\arcsin\sqrt\epsilon$ and $\cos(2\arcsin\sqrt\epsilon)=1-2\epsilon$ give
the second display ($\epsilon\le\frac12$ keeps the angles in the monotone range).
For interval windows $\epsilon=0$ is excluded because $\lambda_0(c)<1$; for general
sets of finite measure it is the theorem of
[Amrein and Berthier (1977)](https://doi.org/10.1016/0022-1236(77)90056-8)
and [Benedicks (1985)](https://doi.org/10.1016/0022-247X(85)90140-4)
(metadata). For $\hbar=0$ the state $\delta_{(q_0,p_0)}$ lies in every window.
$\square$

Theorem E complements Theorem C. Theorem C bounds the disturbance that a
record leaves; Theorem E bounds the concentration of the body's state
that records can produce, which is the quantity Theorem I of the
[unit-and-indeterminacy note](necessity-unit-and-indeterminacy.md) shows
can be made arbitrarily small classically. It uses no Gaussian
assumption, and it depends on the windows only through the product of
half-widths $ab$ in units of $\hbar$, the action scale of the comparison
Newton takes to zero (the windows' area is $4ab$). It shares with the
Planck paper's floor only the total-variation input $(1-2\epsilon)$; for small
$\epsilon$, Slepian's asymptotics give $c_*(\epsilon)\approx\frac12\ln(1/\epsilon)$ (reviewer's
recollection), a few units of $\hbar$ at practical error levels. (Check,
2026-09-27: the large-$c$ formula $1-\lambda_0(c)\simeq4\sqrt{\pi c}\,e^{-2c}$ of
[Slepian 1965](https://doi.org/10.1002/sapm196544199) and Fuchs 1964, recalled,
printed passage not yet located, turns $\lambda_0\ge(1-2\epsilon)^2\simeq1-4\epsilon$ into
$2c-\frac12\ln c-\frac12\ln\pi\ge\ln(1/\epsilon)$, so
$c_*(\epsilon)=\frac12\ln(1/\epsilon)+\frac14\ln\ln(1/\epsilon)+O(1)$; the leading term
agrees with the reviewer.) It holds for every
$\hbar\ne0$; the state route of the routes note must reproduce it separately.

## 7. The same structure in Rivero 1998: the classical Dirac measure and its constant

The thesis that the path-integral constant is a consistency condition
was stated by the user in 1998
([Rivero, "A short derivation of Feynman formula", arXiv:quant-ph/9803035](https://arxiv.org/abs/quant-ph/9803035),
full read). Its abstract: "The complex exponential weighting of Feynman
formalism is seen to happen at the classical level. (Finiteness of)
Feynman path integral formula is suspected then to appear as a
consistency condition for the existence of certain Dirac measures over
functional spaces." Theorems A--D fit it point by point.

- **The complex exponential is classical.** The Dirac measure
  concentrated on the critical points of $f$, which is the principle of
  virtual work, is given the representation
  $\langle\delta(f')|g\rangle=\lim_{\varepsilon\to0}\iint
  e^{i(f(y)-f(x))/\varepsilon}g(x)\,dx\,dy/\varepsilon$ (its eqs. (1)--(2)). The
  "halved" functional $\varepsilon^{-1/2}\int e^{if/\varepsilon}O\,dx$ recovers it by
  modulus squared, $g=|O|^2$, when $f$ has a single critical point
  (eqs. (3)--(4); the paper proposes eq. (2) as asymptotically equivalent
  to eq. (1), with the normalization of the Dirac measure absorbing a
  factor $2\pi$). The classical variational
  problem already carries an amplitude whose square is the record.
- **Theorem A is its Ehrenfest remark.** The paper's control
  transformation $\tau_\mu\delta^h=\delta^{\mu h}$ (eq. (10)) leaves the mean of the
  Euler--Lagrange expression invariant in a formal manipulation (the
  paper's word), "RG invariance in this context
  relates to Ehrenfest theorem" (eq. (11)): the equations of motion hold
  for every value of the constant. Theorem A(a) is the operator form.
- **The dilation family.** The map $h\mapsto\mu h$ is the isomorphism
  $*_{\lambda^2\hbar}\to*_\hbar$ of §4: every nonzero value of the constant gives an
  equivalent theory, and only the value $0$ is distinguished.
- **Why Gaussian integrals are exact here.** For a quadratic $f$, the
  halved functional gives the classical value of every linear observable
  for every $\varepsilon$, because the odd moments of $e^{ia(x-x_*)^2/\varepsilon}$ about
  $x_*$ vanish. The Gaussian integrals that run through this programme's
  notes (the elimination law of the refinement note, heat kernels,
  Gaussian marks, Astra's Gaussian restriction) are exact because
  Galileo's comparison and Newton's other integrable cases are quadratic;
  this is Theorem A(b) in the language of the Dirac measure. For general
  forces the object is the oscillatory measure.
- **Where a fixed constant enters.** On paths, the regularized measure has
  two parameters, the action resolution $\varepsilon$ of the Dirac measure and the
  time step $\varepsilon'$ of the partition (eq. (5)). Newton's classical
  mechanics takes $\varepsilon\to0$ at each partition (the classical elimination,
  Proposition 2 of the [refinement note](refinement-composition-and-limit.md))
  and then refines; the path integral of eqs. (7)--(8) holds the action
  resolution at a fixed $h$ while the partition is refined. (The paper
  also writes $\varepsilon=h\varepsilon'$ after eq. (5), where the resolution itself goes to
  zero; the reading here follows eq. (7).) For Newton's
  quadratic cases both orders converge (the refinement note's
  Proposition 2 and Theorem 3), which is the independence of Theorem A.
  The 1998 conjecture that finiteness forces the joint limit concerns the
  general, non-quadratic case, and it remains open.
- **The tangent groupoid and the ultimate velocity.** The paper proposes
  Connes's tangent groupoid as the frame
  ([Rivero 1997, arXiv:dg-ga/9710026](https://arxiv.org/abs/dg-ga/9710026),
  abstract;
  [Cariñena, Clemente-Gallardo, Follana, Gracia-Bondía, Rivero and Várilly 1999](https://doi.org/10.1016/S0393-0440(98)00028-X),
  abstract: the construction "generalizes the standard Moyal rule"). In
  that groupoid a pair of points $(x,y)$ at scale $\varepsilon>0$ is a chord, and
  the smooth structure glues it at $\varepsilon=0$ to the tangent vector
  $\lim(y-x)/\varepsilon$. The $\varepsilon=0$ boundary is Newton's *velocitas ultima*, the
  "certain and definite" limit of §1; functions there are functions of
  place and velocity together, a commutative algebra, while at $\varepsilon>0$ the
  groupoid convolution of kernels is noncommutative. Joint determinacy
  holds on the boundary fibre, and the deformation of Theorem B is the
  passage to the interior with $\varepsilon$ playing the part of $\hbar$. This is a
  reading of the cited constructions; on the Moyal side the boundary
  algebra is functions on $T^*M$, Fourier dual to $TM$.

## 8. What remains, and consequence for STATE

Theorems A--D are proved for one degree of freedom; several degrees
follow with $Sp(2n)$, whose invariants of two vectors are again generated
by the symplectic pairing. The analogy with the parallel postulate holds
for the algebraic route under (H1)--(H3): independence from the
Heisenberg-form axioms, a unique deformation with one constant, and a
floor. It is partial in two ways stated above: (H2) is an added premise,
and the state route gives the same floor without noncommutativity. The
identification with Newton rests on his *velocitas ultima*, with the step
from geometry to records interpretive.

For STATE item 2 this places the necessity question precisely. Theorem U
supplies the value of the unit from radiation thermodynamics; Theorem I
and the routes note say what must be denied; this note shows that the
algebraic denial is a single step with a single constant, and that
Newton asserted, in the ultimate velocity, the joint determinacy it
denies.
