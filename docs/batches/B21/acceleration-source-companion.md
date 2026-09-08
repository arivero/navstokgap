# B21 acceleration and bounded-turn source companion

> Audit date: 2026-09-08. Role: bounded librarian audit for A07.
> Search coverage: two web searches (optimal control with bounded acceleration;
> sharp Lipschitz/Poincare variance). No source was counted from a search
> snippet. At most two primary sources were selected; four pages maximum was
> not exceeded.

## Result and source status

The proposed B21 statement is an elementary, sharp specialization of bounded
double-integrator control, rather than a new optimal-control theorem. The
literature route establishes the surrounding control problem and standard
Lipschitz/Poincare tools, but I found no primary source matching the exact
opposite-velocity, speed-capped kinetic-cost formula. Thus the formula should
be accepted as a project derivation, with literature status “elementary
specialization; exact prior-art match not found in bounded search.”

### Selected sources

1. D. Liberzon, *Calculus of Variations and Optimal Control Theory: A
   Concise Introduction*, Princeton University Press (2012), chapters 4–5
   (control constraints, reachable sets and minimum-time/optimal-control
   constructions). Publisher metadata:
   https://press.princeton.edu/books/hardcover/9780691151878/calculus-of-variations-and-optimal-control-theory
   Reading level: metadata only; no pages were treated as verified. This is a
   primary author source for the general control framework, not for the exact
   B21 cost.
2. Acosta and Durán, “An optimal Poincaré inequality in (L^1) for
   convex domains,” *Proceedings of the American Mathematical Society* 132
   (2004), 195–202, DOI 10.1090/S0002-9939-03-07141-5.
   https://www.ams.org/journals/proc/2004-132-01/S0002-9939-03-07141-5/
   Worker-reported metadata/abstract lead. Coordinator's AMS open failed;
   the record remains unverified at primary-source level in this audit.
   It supplies no theorem or constant used by C043–C044.

The second search also returned general Gaussian Poincare material, which was
not selected as a source because it concerns Gaussian measure rather than a
uniform time interval. No PDF equation was visually checked; consequently no
source claim below is labelled passage-level.

## Mathematical audit of the supplied result

Let (v=dot X), (v(0)=u), (v(T)=-u), (|v|le u), and
(|v'|le a) a.e., with (m,u,a>0). The endpoint Lipschitz envelopes imply

\[
 v(t)\ge u-at\quad\text{and}\quad v(t)\le -u+a(T-t)
\]

in the respective endpoint neighborhoods (equivalently, the required drops
of (2u) and the speed cap force two turn ramps). Feasibility requires

\[
 T\ge 2u/a.
\]

When feasible, the least-cost path is

\[
 v_*(t)=
 \begin{cases}u-at,&0\le t\le u/a,\\
 0,&u/a\le t\le T-u/a,\\
 -a(t-(T-u/a)),&T-u/a\le t\le T,
 \end{cases}
\]

and the disjoint endpoint envelopes give

\[
 S_*={m\over2}\int_0^T v_*^2dt={mu^3\over3a}.
\]

The bound is attained, hence is a minimum and not merely an infimum. At
(T>2u/a), smooth zero-mean bumps supported in the idle interval produce
positive excess kinetic cost tending to zero, so this endpoint-conditioned
minimum is not a universal positive action scale.

At fixed force ceiling (F_{\max}=ma), the value is
\[
 S_*={m^2u^3\over3F_{\max}}.
\]
For fixed (m,a,T), (u\downarrow0) closes the lower bound. A speed ceiling
alone permits the zero path and supplies no positive bound.

For a partition (π), with cell averages ̅v, the polygon kinetic action obeys
\[
 S_\pi={m\over2}\sum_i {(ΔX_i)^2\overΔt_i},\qquad
0\le S-S_\pi={m\over2}\sum_i\int_i(v-\bar v)^2dt
\le {ma^2\over24}\sum_iΔt_i^3
\le {ma^2T\over24}|\pi|^2.
\]
The middle constant is the sharp interval Lipschitz-variance constant
(∫(f-̅f)^2 ≤ L²h³/12), applied cellwise; equality requires affine
velocity on each cell. This is a polygon approximation estimate, not a
full-force Lagrangian action or quantum gap.

## Physical test and next use

Coordinator review corrected the terminal envelope's inequality direction and
the partition symbol. On 2026-09-08 the coordinator additionally searched once
and read the opening problem statement of
[Liberzon §4.4.1](https://liberzon.csl.illinois.edu/teaching/cvoc/node85.html),
online edition footer dated 2010-12-20. It specifies bounded acceleration and
minimum time, with running cost one. Equations are image-backed in this HTML;
their alt text was read, with no image-level formula verification. This supports
the control-framework comparison only. The kinetic-cost and pair-variance
proofs are independently given in the maintained project note. No source PDF
was downloaded; the exact cost remains unmatched in this bounded search.

The endpoint speed lower bound together with a force/acceleration ceiling
supplies a mechanical scale; a speed upper bound by itself does not. Keep the
result conditional on prescribed endpoint velocities and do not promote it to
universality or to a quantum action parameter. The prior-art audit is bounded
and should be revisited only if A07 needs a page-level optimal-control match.
