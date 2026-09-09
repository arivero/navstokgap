# B32 source companion: closed-orbit action bound

## Result and coverage

Milnor's primary paper gives the required total-curvature input: for any
closed curve in Euclidean (H^n) (the paper's (n>1) convention),

\[
 K(C)\ge 2\pi .
\]

The result is not restricted to simple curves, so self-intersections are in
scope. For a (C^2), regular, arclength-parametrized curve the paper's
introduction identifies total curvature with absolute turning of the tangent;
the theorem is therefore applicable to the draft's (C^2) unit tangent. The
source does not establish a relativistic force/action bound, nor the smooth
potential equality construction: those remain derived consequences of the
draft's hypotheses.

## Primary source

J. W. Milnor, “On the Total Curvature of Knots,” *Annals of Mathematics*,
Second Series 52(2) (September 1950), pp. 248–257, pp. 248 and 254 of the
printed article. Open scan: https://people.reed.edu/~ormsbyk/milnor-total-curvature.pdf
(stable JSTOR URL recorded on scan: http://www.jstor.org/stable/1969467).
Downloaded audit copy: `.build/b32/milnor-total-curvature.pdf`; SHA-256
`db75ff2d20da489355e9a4ed541198ef23d3e50bdf7b4dcf68f6c9938deecd54`.

Reading level: passage, limited to two article pages. On p. 248 (PDF page 2), Milnor
reports Fenchel's (2\pi) theorem in three dimensions and Borsuk's extension
to n-dimensional space, and says the generalized definition applies to any
closed curve. On p. 254 (PDF page 8), Theorem 3.4 states for “any closed curve”
that (K(C)\ge2\pi), with equality exactly for convex curves. The page's
proof proceeds through inscribed polygons; hence no simplicity assumption is
introduced. The source uses Euclidean (H^n), not spacetime or an arbitrary
metric, and its equality characterization is stronger than needed here.

## Audit of A18 results

* **Total-turning estimate.** Proof status: derived, conditional on a (C^2)
  regular periodic curve in Euclidean (\mathbb R^d), (d\ge2), and on the
  stated momentum regularity. Literature status: established input, directly
  matched by Milnor pp. 248, 254; source covers the dimension scope (n>1).
  The draft should define (K(C)=\int|\dot n|dt) (or cite the arclength
  identification) before invoking the polygonal theorem. Endpoint tangent
  matching follows from the periodic (C^2) map.
* **Force/speed-floor action bound.** Proof status: derived consequence, not a
  source theorem. The orthogonal decomposition
  ( |\dot p|^2=\dot P^2+P^2|\dot n|^2 ) and
  (T\ge P_*K/F_{\max}), followed by (P(v)v\ge P_*v_*), are valid provided
  (p=P(v)n), (P) is monotone, and (p) is absolutely continuously
  differentiable. Literature status: no prior-art match established under the
  bounded two-query audit; do not label this novel beyond that coverage.
* **Smooth-potential circle sharpness.** Proof status: derived model
  construction. The radial cutoff potential is smooth at the origin because it
  is constant there, has global force ceiling, and realizes circular balance at
  (r=R_*). Literature status: not a source match in Milnor; B31's circular
  mechanics source does not audit this cutoff construction. Equality is over
  the admissible model class, not every fixed potential.

## Search and limits

One discovery query was used (Milnor total-curvature PDF); no second query was
needed. Only the one primary source above was read, on the two specified pages.
This is a bounded prior-art audit, not a comprehensive novelty search.

## Proposed next idea

Coordinator visually verified printed pp. 248 and 254, correcting the PDF
offsets for its cover sheet. The source's initial polygon convention is
$n\ge1$; A18 uses $d\ge2$ for regular closed curves. Its smooth-curve
identification and Theorem 3.4 support that domain. The mechanical inequalities
and cutoff-potential construction were separately reviewed in writing.

A19 can replace the pointwise speed floor by a peak-excitation premise (for
example a fixed peak momentum or kinetic excursion) only as a proposal: force
ceilings control turning time, but an excursion alone may be concentrated near
turning points and need not lower-bound \(\int P(v)v\,dt\). The missing test is
an explicit duration/measure condition linking peak excitation to nonzero-speed
occupation; its physical origin and universality remain open.
