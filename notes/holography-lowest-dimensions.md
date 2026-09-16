# Holography in the lowest dimensions: at $d=0$ it is the wave-function identity, at $d=1$ it is the Schwarzian

A $d$-dimensional boundary theory is supposed to be dual to gravity in
$d+1$ dimensions. For the two lowest cases the content is very different.
For a **zero-dimensional boundary**, the bulk is one-dimensional, where
there is no curvature and general covariance reduces to reparametrization
of a worldline, so the bulk is the first-quantized particle, classified by its number
of endpoints: one point gives the ground-state wave function, two give
the propagator, none gives the partition function, and more than two
give the Feynman graphs of the target-space theory. The duality at two
points is the exact identity
$$|\Omega(x)|^2\,dx\ =\ \text{the }\tau=0\text{ marginal of the one-dimensional Euclidean path integral},$$
the Feynman--Kac form of the ground state; the segment read as a state
on its two endpoints is the thermofield double at $\beta=2T$, and the gap
is the rate at which the two ends disentangle as the bulk lengthens. That is, in one dimension lower,
the identity used in
[the transfer note](ground-state-measure-transfer.md) for Yang--Mills,
where $|\Omega(U)|^2d\mu$ is the time-slice marginal of the
four-dimensional Wilson measure; the emergent dimension is Euclidean
time. For a **one-dimensional boundary**, quantum mechanics, the bulk is
two-dimensional dilaton gravity on nearly-$AdS_2$, the
Jackiw--Teitelboim theory, and its dual is the Sachdev--Ye--Kitaev
model. Pure two-dimensional gravity has no equations of motion, exact
$AdS_2$ with finite energy fragments, and the surviving dynamics is a
single boundary mode, the reparametrization of boundary time with the
Schwarzian action $S=-C\int d\tau\,\{f,\tau\}$. This mode gives the
near-extremal black hole entropy, saturates the chaos bound with
Lyapunov exponent $\lambda_L=2\pi k_BT/\hbar$, and has a **gapless**
density of states $\rho(E)\propto\sinh\big(2\pi\sqrt{2CE}\big)$ with a
square-root edge. The naive counting fails at $d=0$ because the radial
direction of anti-de Sitter space is the renormalization scale and a
zero-dimensional theory has no renormalization group; for a
zero-dimensional scalar integral the bulk is a bare graph, and for a
matrix integral the indices thicken the graph into a surface, which is
how the double-scaled matrix integrals acquire a two-dimensional bulk. Constants
explicit; references at metadata level; nothing promoted.

## 1. What gravity has to work with in low dimensions

In $D$ spacetime dimensions a massless graviton carries $D(D-3)/2$
polarizations: two in $D=4$, none in $D=3$. In $D=2$ the Einstein tensor
vanishes identically and $\sqrt g\,R$ is the Euler density, so the
Einstein--Hilbert action is a topological number and pure gravity has
no field equations; a dilaton $\phi$ must be added to obtain any
dynamics (Teitelboim, Phys. Lett. B 126 (1983) 41; Jackiw, Nucl. Phys.
B 252 (1985) 343). In $D=1$ there is no curvature at all: a
one-manifold is flat, and the metric is a single function, the einbein
$e(\tau)$, with reparametrization as the only gauge symmetry.

So in both low cases the bulk has no local gravitational degrees of
freedom, and all the physics sits at the boundary or in the topology.

## 2. Zero-dimensional boundary, one-dimensional bulk

The bulk theory is the relativistic particle,
$$S=\frac12\int d\tau\Big[\frac{1}{e}\,\dot x^2+e\,m^2c^2\Big],$$
whose constraint is the mass shell $p^2=m^2c^2$ and whose only
"gravitational" content is the invariance under $\tau\to f(\tau)$. A
connected one-manifold with boundary is a segment or a half-line, a
connected one-manifold without boundary is a circle, and a connected
one-dimensional space with more than two ends is a graph with junctions.
The boundary is a finite set of points, and **the number of points
decides what the bulk computes.**

| bulk one-manifold | boundary points | the bulk path integral equals |
| --- | --- | --- |
| half-line $[0,\infty)$ | $1$ | the ground-state wave function $\Omega(x)$ |
| segment $[0,T]$ | $2$ | the propagator $K_T(x,y)=\langle x|e^{-TH/\hbar}|y\rangle$ |
| circle of length $\beta$ | $0$ | the partition function $\operatorname{Tr}e^{-\beta H/\hbar}$ |
| $k$ disjoint segments | $2k$ | the product of $k$ propagators |
| graph with $k$ ends | $k$ | a Feynman diagram of the target-space theory |

**One point: the wave function.** Fix one end at $x$ and let the other
run to infinity with any boundary state $\chi$ of nonzero overlap with
$\Omega$; then
$$\lim_{T\to\infty}e^{TE_0/\hbar}\langle x|e^{-TH/\hbar}|\chi\rangle
=\Omega(x)\,\langle\Omega,\chi\rangle ,$$
so a single boundary point carries the ground-state wave function, and
the half-line is its Euclidean history. This is the no-boundary
prescription of Hartle and Hawking (Phys. Rev. D 28 (1983) 2960) in its
one-dimensional form: the wave function is the path integral over
half-geometries ending on the boundary.

**Two points: the propagator, and the gap.** With both ends fixed the
bulk computes $K_T(x,y)$, and the spectral decomposition gives
$$K_T(x,y)=e^{-TE_0/\hbar}\,\Omega(x)\Omega(y)\Big[1+O\big(e^{-T\Delta/\hbar}\big)\Big],
\qquad \Delta=E_1-E_0 .$$
The leading term is the product of two half-lines, one per boundary
point; **the gap is the decay rate, in the bulk length, of the connected
part**. In the language of ensembles, a connected bulk joining two
boundary components is a wormhole, and the statement that its
contribution factorizes up to $e^{-T\Delta/\hbar}$ says that in one
dimension the wormhole's failure to factorize is exactly the gap. For
every bounded $F$, Feynman--Kac then gives
$$\langle\Omega,F\Omega\rangle=\lim_{T\to\infty}
\frac{\int\mathcal Dx\ F(x(0))\ e^{-S_E[x]/\hbar}}{\int\mathcal Dx\ e^{-S_E[x]/\hbar}},
\qquad
\frac{S_E}{\hbar}=\frac1\hbar\int_{-T}^{T}d\tau\Big[\frac m2\dot x^2+W(x)\Big],$$
so $|\Omega|^2dx$ is the $\tau=0$ marginal of the segment's measure. That
is Proposition 1 of
[the transfer note](ground-state-measure-transfer.md), one dimension
lower: there the segment is the Euclidean slab $[-T,T]\times\mathbb T^3$,
its two "points" are the two time slices, and the Yang--Mills gap is the
decay of the connected slice-to-slice correlator with $T$. In both
cases the reason to move to the bulk is the same: the bulk weight
$e^{-S_E/\hbar}$ factorizes over time steps and separates configurations
locally, while the boundary eigenvalue equation
$-\frac{\hbar^2}{2m}\Omega''+(W-E_0)\Omega=0$ compares the potential
with the total energy. The Agmon estimate of
[the Agmon note](agmon-ground-state-suppression.md) is the boundary-side
statement; the Feynman--Kac marginal is the bulk-side one.

**Cutting the segment.** Inserting a time point $\tau\in(0,T)$ and
integrating over the position there,
$$K_T(x,y)=\int dz\ K_{T-\tau}(x,z)\,K_\tau(z,y),$$
is the semigroup property $e^{-TH/\hbar}=e^{-(T-\tau)H/\hbar}e^{-\tau H/\hbar}$
with the resolution of the identity $\int dz\,|z\rangle\langle z|$ at the
cut. The amplitude is unchanged, so a cut decomposes the wormhole into
two shorter ones glued along the cut, and inserts nothing. Iterating the
cuts at spacing $a_t$ is the transfer-matrix form
$e^{-TH/\hbar}=\mathcal T^{T/a_t}$, and the cut at $\tau=0$ of a slab
$[-T,T]$ is exactly how [the transfer note](ground-state-measure-transfer.md)
exhibits $|\Omega|^2$ as a marginal.

What the segment is, read as a state rather than as an amplitude, is
sharper. Regard $K_T(x,y)$ as the wave function of a state on the two
boundary points, an element of $\mathcal H\otimes\mathcal H$. Its
Schmidt decomposition is the spectral one,
$$K_T=\sum_ne^{-TE_n/\hbar}\ \psi_n\otimes\overline{\psi_n},$$
which is the thermofield double at inverse temperature $\beta=2T$. The
two ends are entangled with Schmidt weights $p_n\propto e^{-2TE_n/\hbar}$,
so the entanglement entropy between them equals the thermal entropy at
$\beta=2T$ and decays, for large $T$, as
$$S_{\rm ent}(T)\ \simeq\ d_1\Big(\frac{2T\Delta}{\hbar}+\log\frac1{d_1}\Big)e^{-2T\Delta/\hbar},$$
with $d_1$ the degeneracy of the first excited level. **The gap is the
rate at which the two ends of the segment disentangle as the bulk
lengthens.** Factorization of the wormhole at large $T$ and
disentanglement of the thermofield double are the same statement. For
the Yang--Mills slab of
[the transfer note](ground-state-measure-transfer.md), the wave
functional $\Psi(U_{-T},U_T)=\langle U_T|e^{-2TH/\hbar}|U_{-T}\rangle$ of
the two boundary slices is the thermofield double of the lattice
Hamiltonian at $\beta=2T$, and the gap is the disentanglement rate of the
two slices.

The ensemble wormholes of Section 3, a cylinder joining two circles,
have no one-dimensional counterpart: a connected one-manifold with two
boundary components is a segment, whose components are points. Their
one-dimensional shadow is the segment, which needs no ensemble.

**No points: the spectrum.** The circle has empty boundary and computes
$\operatorname{Tr}e^{-\beta H/\hbar}=\sum_ne^{-\beta E_n/\hbar}$, which
at large $\beta$ reads $e^{-\beta E_0/\hbar}(1+e^{-\beta\Delta/\hbar}+\dots)$.
A bulk with no boundary at all still knows the gap, through its length.

**More than two points: graphs and Feynman diagrams.** Disjoint
segments factorize. A connected bulk with $k>2$ ends is a graph, and
pure one-dimensional gravity supplies no rule at the junctions; the
junction rule is extra data, and once it is given the sum over graphs
with edge lengths integrated is the Schwinger proper-time form of the
Feynman expansion (Schwinger, Phys. Rev. 82 (1951) 664): each edge is a
segment computing a propagator, each junction is a vertex of the
target-space theory, and the einbein moduli are the Schwinger
parameters. The "boundary theory" is then the field theory on the
target space of the particle, in as many dimensions as the target has.

**The zero-dimensional field theory proper.** Take the target space to
be a point. The propagator is a number, the edges have no moduli, and
the bulk is a bare graph: the Feynman expansion of an ordinary integral
$\int d\phi\,e^{-V(\phi)/\hbar}$ is a sum over graphs weighted by
symmetry factors and couplings, with no geometry left on the edges.
This is the exact content of "holography for a zero-dimensional
theory": **the bulk of a zero-dimensional scalar or vector integral is a
one-dimensional graph with no metric.** When the variable is an $N\times N$
matrix, each graph acquires an index structure that thickens it into a
ribbon graph, that is, a two-dimensional surface with a genus expansion
in $1/N$ ('t Hooft, Nucl. Phys. B 72 (1974) 461), and that is the
mechanism by which the double-scaled matrix integrals of Section 3
acquire a two-dimensional bulk. The extra dimension comes from the
matrix indices, and the count "bulk = boundary + 1" is restored by the
thickening rather than by any property of the point.

## 3. One-dimensional boundary, two-dimensional bulk

Here the duality has content. The bulk is Jackiw--Teitelboim gravity,
$$\frac{S}{\hbar}=-\frac{1}{16\pi G}\Big[\int d^2x\sqrt g\,\phi\Big(R+\frac{2}{L^2}\Big)
+2\int_\partial\sqrt h\,\phi_b\,K\Big],$$
in which the dilaton fixes $R=-2/L^2$ and the geometry is $AdS_2$
exactly. Exact $AdS_2$ cannot support finite-energy excitations: the
backreaction of any finite energy destroys the asymptotics (Maldacena,
Michelson and Strominger, JHEP 1999 (02) 011), so the correspondence is
formulated on *nearly*-$AdS_2$, where the dilaton grows toward the
boundary and breaks the conformal symmetry (Almheiri and Polchinski,
JHEP 2015 (11) 014; Maldacena, Stanford and Yang, PTEP 2016, 12C104).

**The Schwarzian mode.** With the bulk geometry rigid, the only
dynamical variable is the shape of the boundary curve, a
reparametrization $f(\tau)$ of boundary time, and the action reduces to
$$\frac{S}{\hbar}=-C\int d\tau\ \{f,\tau\},\qquad
\{f,\tau\}=\frac{f'''}{f'}-\frac32\Big(\frac{f''}{f'}\Big)^2 ,$$
with $C\propto\phi_b/G$. Its consequences: the near-extremal black hole
entropy $S=S_0+2\pi^2C/\beta\,(\cdot k_B)$ to leading order in $1/\beta$;
the out-of-time-order correlator growing at the maximal rate
$\lambda_L=2\pi k_BT/\hbar$; and the density of states
$$\rho(E)\ \propto\ \sinh\Big(2\pi\sqrt{2CE}\Big),$$
which vanishes at $E=0$ like $\sqrt E$ and has no gap.

**The boundary dual.** The Sachdev--Ye--Kitaev model, $N$ Majorana
fermions with random all-to-all $q$-body couplings (Sachdev and Ye,
Phys. Rev. Lett. 70 (1993) 3339; Kitaev, KITP talks 2015; Maldacena and
Stanford, Phys. Rev. D 94 (2016) 106002), has at large $N$ and low
energy exactly the Schwarzian as its effective action, the same
entropy, the same maximal chaos, and the same gapless spectrum. The
matching is at the level of the low-energy effective theory rather than
of a single microscopic theory: the SYK couplings are drawn from an
ensemble, and the bulk sum over topologies is the dual of the ensemble
average (Saad, Shenker and Stanford, arXiv:1903.11115, which shows that
JT gravity summed over all genera is a double-scaled matrix integral).

## 4. Why the naive counting fails at $d=0$

The radial coordinate of $AdS_{d+1}$ is the renormalization scale of the
boundary theory; an emergent dimension needs a continuum of scales to
emerge from. A zero-dimensional theory is a finite-dimensional integral
and has no renormalization group, so the $d=0\to D=1$ reading of the
counting has nothing to build the dimension out of, and Section 2 is
the whole of what it contains: Euclidean time as the emergent direction,
and the Feynman--Kac identity as the dictionary. The dualities with
zero-dimensional boundaries that do carry content, the double-scaled
matrix integrals of Section 3, have **two-dimensional** bulks. Their
extra dimension comes from the matrix indices thickening each graph
into a ribbon graph, with the eigenvalue density playing the role of a
continuum of scales and the genus expansion supplying the sum over
topologies; the boundary object is an ensemble of theories rather than
one.

## 5. Bearing on this programme

Three points.

1. The $d=0$ identity of Section 2 is the tool that
   [the transfer note](ground-state-measure-transfer.md) uses in $3+1$
   dimensions. In both cases the reason to move to the bulk is the same:
   the bulk weight factorizes and yields local estimates, the boundary
   eigenvalue equation carries the extensive energy and does not.
2. The $d=1$ example is a scale generated entirely by a boundary mode,
   and it is gapless. A Schwarzian-type mechanism therefore produces a
   scale without producing a gap, which is the opposite of what the
   Yang--Mills problem needs and a useful reminder that the two are
   distinct.
3. The holographic setting in which a gap does appear is a bulk whose
   infrared end caps off: Witten's confining geometry, in which the
   Euclidean time circle shrinks smoothly to zero size and the bulk
   spectrum acquires a discrete tower with a gap set by the size of the
   cap (Witten, Adv. Theor. Math. Phys. 2 (1998) 505). That construction
   lives at large $N$ and strong 't Hooft coupling, so it gives a
   picture of how a gap arises in a different regime from the
   weak-coupling one this programme works in, and no theorem about
   $SU(3)$.

## 6. Consequence for STATE

Recorded for orientation. The $d=0$ case is the Feynman--Kac identity
that the programme already uses; the $d=1$ case is the
Schwarzian/SYK system, gapless with $\rho(E)\propto\sinh(2\pi\sqrt{2CE})$;
the holographic mechanism for a gap is a capped-off infrared geometry at
large $N$. Nothing in the main line changes.
