# Newton's vanishing areas and the proposed action scale

2026-09-05. The actual project is now Newtonian trajectories and a possible
action-scale restriction. The earlier Millennium comparison is background.
The user's proposal is investigated here as a heuristic; a positive action gap
is not assumed as a conclusion.

## 1. What was read

We downloaded [the Motte/Chittenden 1846 text](../docs/Newton_Principia_Motte1846.md)
and read Definitions I–VIII and Scholium, the Laws with corollaries and Scholium,
Book I Section I, and Section II Propositions I–II. A
[Motte 1729 excerpt edited by Wilkins](../docs/Newton_Principia_BookI_SectionI_Motte1729_Wilkins2002.md)
supplies readable formulae for Section I. These are later English witnesses, not
a study of the original 1687 Latin or of all historical commentary.

The closest passages are quite specific:

| Passage (1846 printed page) | Content relevant here |
| --- | --- |
| Definitions II, IV, VII–VIII (73–77) | Momentum and impressed force; accelerative versus motive force |
| Definition Scholium (77–82) | Distinguishes mathematical time and space from sensible measures |
| Laws, Corollaries V–VI (89) | Common uniform translation and equal parallel accelerations preserve relative motions |
| Laws, Scholium (89–90) | Explicit projectile parallelogram and parabolic path; attributes the result to Galileo |
| Lemmas I–III (95–96) | Limits and convergence of inscribed/circumscribed figures |
| Lemma X (99–100) | Initial force-generated displacement is quadratic in time |
| Lemma XI, Corollaries 4–5 (101) | Tangent triangles and curved segments scale cubically; segment is one third of the triangle |
| Section I closing Scholium (102–103) | Vanishing magnitudes mean limits, not smallest indivisible magnitudes |
| Proposition I (103–105) | Equal swept areas for a polygon under central impulses, then a curve limit |
| Proposition II (105–106) | Converse relating area law to direction of resultant force |

Newton writes in the closing Scholium that he means “evanescent divisible
quantities”; he explicitly denies a smallest determinate magnitude in these
geometric constructions. This supports a continuity interpretation. It supplies
no historical assertion about Planck's constant. Nor is his example of an
“ultimate velocity” in that Scholium a universal speed limit: it is a limiting
velocity at an event.

The source HTML contains modern image descriptions; these were not treated as
Newton's prose. Some equations are images; the Wilkins PDF was used where HTML
extraction omitted them. Selected historical figures were visually inspected:
[projectile](../docs/images/i_090a.jpg), [central polygon](../docs/images/i_104.jpg).

## 2. Make the proposed area unambiguous

Take a particle of mass $m>0$, a constant force $F>0$ in the positive $y$
direction, $V(y)=-Fy$, and initial data

$$
x(0)=y(0)=0,\qquad \dot x(0)=v_0>0,\qquad \dot y(0)=0.
$$

For an interval $\varepsilon>0$ the exact classical solution is

$$
x(t)=v_0t,\qquad y(t)=\frac{F}{2m}t^2.
$$

The particle deflects along the force and loses potential energy. It does not
initially rise against it when its initial velocity is perpendicular to it.
Reversing the vertical convention reverses the relevant signs, not the magnitudes.
Define the energy transfer by

$$
\delta E:=K(\varepsilon)-K(0)
=-\bigl[V(\varepsilon)-V(0)\bigr]
=F\Delta y=\frac{F^2\varepsilon^2}{2m}.
$$

Total mechanical energy is constant; $\delta E$ is not its change or a quantum
standard deviation. The proportionality constant in $\Delta y=K_{\rm conv}\delta E$
is $K_{\rm conv}=1/F$, which has dimensions of inverse force.

Let $A=(0,0)$, $B=(v_0\varepsilon,0)$ be the inertial endpoint and
$D=(v_0\varepsilon,F\varepsilon^2/(2m))$ the actual endpoint. The triangle $ABD$ has

$$
\mathcal A_\triangle=\frac12\Delta x\Delta y
=\frac{v_0F}{4m}\varepsilon^3
=\frac{v_0}{2F}\,\varepsilon\delta E.
$$

This confirms the proposed proportionality, with an explicit factor and energy
definition. It is an area in configuration space. Multiplication by $F/v_0$
converts its units to action; it is not already a canonical phase-space area.

For $y(x)=Fx^2/(2mv_0^2)$ the other two areas are

$$
\mathcal A_{\rm tangent,curve}=\int_0^{v_0\varepsilon}y(x)\,dx
=\frac23\mathcal A_\triangle,\qquad
\mathcal A_{\rm chord,curve}=\frac13\mathcal A_\triangle
=\frac{v_0F\varepsilon^3}{12m}.
$$

These are the ratios in Lemma XI, Corollary 5, exact for this parabola. The tangent
triangle is cubic in $\varepsilon$, rather than quadratic, because the initial
vertical velocity is zero. About a later point, the deflection from its local
tangent is still quadratic; its absolute vertical displacement need not be.

![Areas for the constant-force launch](../out/constant-force-areas.svg)

## 3. A stronger bridge: an actual action difference

The same-endpoint straight chord is an admissible comparison path in a variational
calculation, although not a solution under the constant force. On
$0\leq t\leq\varepsilon$, set

$$
y_{\rm cl}(t)=\frac{F}{2m}t^2,\qquad
y_{\rm ch}(t)=\frac{F\varepsilon}{2m}t,\qquad x(t)=v_0t.
$$

Compare both with the same Lagrangian

$$
S[x,y]=\int_0^\varepsilon
\left[\frac m2(\dot x^2+\dot y^2)+Fy\right]dt.
$$

For $y=y_{\rm cl}+\eta$, with $\eta(0)=\eta(\varepsilon)=0$, integration by parts
cancels the linear variation because $m\ddot y_{\rm cl}=F$. Consequently

$$
S[y_{\rm cl}+\eta]-S[y_{\rm cl}]
=\frac m2\int_0^\varepsilon\dot\eta^2\,dt.
$$

Here $\eta=F t(\varepsilon-t)/(2m)$ for the chord. Therefore

$$
\boxed{\Delta S_{\rm ch,cl}
=\frac{F^2\varepsilon^3}{24m}
=\frac{F}{2v_0}\mathcal A_{\rm chord,curve}
=\frac{\varepsilon\delta E}{12}.}
$$

This is a genuine action difference, not solely dimensional analysis. Its numerical
factor differs from the converted tangent-triangle area. For this pair of paths,
an identical total time derivative added to the Lagrangian cancels in the action
difference because endpoints agree.

But nothing discretises the neighbouring paths: choosing
$\eta=\alpha t(\varepsilon-t)$ gives

$$
\Delta S(\alpha)=\frac{m\alpha^2\varepsilon^3}{6}\longrightarrow0
\quad\text{as }\alpha\to0.
$$

Thus there is no positive lower bound on nonzero action differences in this
classical path family. A restriction could still be proposed for physical
distinguishability or allowed states; it would require an additional definition
and premise. This calculation does not prejudge those alternatives.

## 4. What Newton's limit does and does not assert

Proposition I proves equality of finite swept triangles already at the polygonal
stage, using central impulses. As the mesh shrinks, individual swept areas vanish
but their sum over a fixed time need not vanish. They are not the small error
lenses between a chord and a curved arc.

For the constant-force parabola, dividing a fixed duration $T$ into $N$ equal
intervals gives $N$ chord lenses, each of area $v_0F(T/N)^3/(12m)$. Their sum is

$$
\mathcal A_{\rm error,total}=\frac{v_0FT^3}{12mN^2}\to0.
$$

This is an exact polygonal approximation statement. A constant parallel force is
not a central force towards a fixed finite point, so its trajectory cannot simply
be substituted into Proposition I's area-law hypothesis. Its direct Newtonian
anchors are the projectile Scholium and Lemmas X–XI.

The opening geometry is not a modern global existence theorem for all force laws.
For constant force the displayed solution exists globally. Singular central forces
need separate collision and continuation analysis. None of these facts identifies
the mesh limit $\varepsilon\to0$ with $\hbar\to0$.

## 5. Path phases, uncertainty and the surviving question

The [Feynman chapter](../docs/Feynman_LeastAction_II19.md) supplies the quantum
interpretation through phases $e^{iS/\hbar}$. Equal phase occurs when an action
**difference** is $nh$, since $h=2\pi\hbar$. It does not select all paths with
absolute action $nh$, impose a smallest action difference, or guarantee that two
terms dominate the full integral. Classical stationarity concerns neighbourhoods
of paths and their phase cancellation.

For our specific chord comparison,

$$
\Delta\varphi=\frac{\Delta S_{\rm ch,cl}}{\hbar}
=\frac{F^2\varepsilon^3}{24m\hbar}.
$$

At fixed $\hbar>0$, $\varepsilon\to0$ makes these two phases closer. Requiring
order-one relative phase would define a comparison scale

$$
\varepsilon_{\rm phase}\sim\left(\frac{24m\hbar}{F^2}\right)^{1/3}.
$$

This is a scale for this chosen pair of paths, not a minimum time or a proved
action gap. In particular the integration-mesh limit of a continuum quantum
formulation is distinct from its semiclassical limit. Introducing $\hbar$ through
the phase rule is new physical input relative to Newton's laws.

Energy-time uncertainty needs another distinction. If $B$ is an observable without
explicit time dependence, the usual quantum commutator variance inequality and
Heisenberg evolution imply

$$
\sigma_H\sigma_B\geq\tfrac12|\langle[H,B]\rangle|,
\qquad
\tau_B:=\frac{\sigma_B}{|d\langle B\rangle/dt|},
\qquad \sigma_H\tau_B\geq\frac\hbar2,
$$

when domains and variances are appropriate and the denominator is nonzero.
This derivation uses a state energy spread and an observable-change timescale.
Neither is automatically the deterministic work $\delta E$ and chosen mesh
$\varepsilon$ above. Likewise a wavepacket uncertainty area concerns a distribution
in conjugate variables, not a geometric area swept by one orbit.

The spatial area also changes under a horizontal Galilean boost. In the frame
moving at $v_0$, horizontal launch velocity and the plotted spatial area vanish.
The action difference above stays finite and unchanged: both paths share the
same horizontal motion, whose action contribution cancels. The formula dividing
by $v_0$ is therefore a conversion for $v_0\neq0$, not a universal area invariant.

Adding a speed cap alone also supplies no positive minimum interval: for
$v_0<c$, the constant-force solution stays below $c$ whenever
$0<\varepsilon<(m/F)\sqrt{c^2-v_0^2}$. Arbitrarily small intervals remain possible.
This is only a consistency check on a finite Newtonian segment, not a relativistic
force model or a theory of finite-speed force propagation.

The promising question is consequently whether an independently justified quantum
notion of distinguishability can be related to this exact geometric action
difference. That is more precise than asserting a universal minimum triangle,
and it leaves open how action bounds and discrete spectra might arise under
additional state, boundary or periodicity conditions.

## 6. Historical status and reproducibility

An admissible modern interpretation is that Newton's geometry permits arbitrarily
fine classical trajectories and does not encode a quantum action scale. Calling
this an implicit $h\to0$ axiom is a retrospective hypothesis, not an assertion
found in the passages read. We have not surveyed enough historical scholarship
to claim that nobody has made or noticed such an interpretation.

The exact polynomial identities and the diagram are reproduced with
`python3 scripts/constant_force_geometry.py`. The
[check output](../out/constant-force-checks.json) records the assumptions and
verified identities. These checks verify the calculation, not the quantum
interpretation or an existence theorem beyond constant force.
