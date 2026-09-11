# Positive preparation width hides receiver states from exact records

The R06 apparatus has a common exact four-momentum record for a two-dimensional
patch of distinct receiver states on its fixed-energy shell. Unknown incoming
probe momenta compensate the receiver changes. For every sufficiently small
fixed coupling lambda>0 and preparation half-width b>0, this gives positive
worst-case position and momentum reconstruction errors. Their product has
action units and a lower bound supplied by the preparation box.

R17, 2026-09-11. The information consists of four final probe momenta only.
The Hamiltonian, receiver energy and preparation support are known; individual
incoming apparatus coordinates are unknown. All receiver/apparatus pairs in
the Cartesian product of the shell and box are admissible. These are
deterministic support risks, not average errors under a density. Additional
records, correlations restricting that product, or other apparatus designs
require a new information-fibre test. Literature status is recorded in B48.

## 1. A uniform compensation estimate

Use [R06](autonomous-finite-readout.md)'s Hamiltonian and
[R16](fixed-coupling-calibration.md)'s component units and record map. Set the
clock and probe positions to their nominal initial values and vary only the
four incoming probe momenta u, measured in the same momentum units as their
final records. This is an admissible slice of the full ten-coordinate box.
Write G_lambda(z,u) for this restricted map, and F_lambda(z)=G_lambda(z,0).
All norms in this section are component sup norms and induced operator norms.

There are positive b_0, lambda_0, L, independent of b and lambda, such that
on a fixed convex receiver neighbourhood and ||u||<=b_0,

$$\|D_uG_\lambda-I\|\le\tfrac12,\qquad
\|D_zF_\lambda\|\le L\lambda,
\quad 0\le\lambda\le\lambda_0.$$

At lambda=0, the probes are free and G_0(z,u)=u. Smooth finite-time flow
dependence on the compact initial-data class makes D_uG uniformly close to
I for small coupling. The second estimate follows from R16's uniform C1
expansion F_lambda=-lambda A z+O(lambda^3). A common compact trajectory
neighbourhood and fixed cutoff/pulse margins follow from the R06 energy and
continuation bounds after reducing b_0 and lambda_0. This proof needs no
assumption that back-reaction vanishes at the chosen positive coupling.

Fix z_* on the shell, Y_*=F_lambda(z_*), and 0<b<=b_0. For any shell state w
satisfying

$$\|w-z_*\|\le \frac{b}{4L\lambda},$$

consider T_w(u)=u-G_lambda(w,u)+Y_* on ||u||<=b/2. The derivative bound makes
T_w a contraction with constant at most 1/2, and

$$\|T_w(0)\|\le L\lambda\|w-z_*\|\le b/4,
\qquad \|T_w(u)\|\le b/4+\|u\|/2\le b/2.$$

The contraction theorem gives a unique solution in this ball,

$$G_\lambda(w,u(w))=Y_*,\qquad
\|u(w)\|\le2L\lambda\|w-z_*\|\le b/2.$$

This is a quantitative implicit-function construction with a b/2 preparation
margin. It establishes exact equality of nonlinear records, including clock
reaction. Injectivity of the nominal map F_lambda is compatible with this
ambiguity because the incoming u changes.

## 2. A common-record patch on the energy shell

Use physical canonical coordinates z=(x,P,y,Q) and R06's

$$H_s=\frac{P^2}{2\mu}+\frac{Q^2}{2\nu}
       +\frac a2x^2-gxy+\frac d2y^2=E>0.$$

Here a,d,mu,nu>0 and ad-g^2>0. At z_*=(0,0,sqrt(2E/d),0), a shell chart is

$$w(x,P)=\left(x,P,\frac gd x+
 \sqrt{\frac{2E-(a-g^2/d)x^2-P^2/\mu}{d}},0\right).$$

Completing the square in the potential verifies H_s(w)=E exactly. Choose
fixed length and momentum units L_*,P_* and a dimensionless r_0>0 so that
the square |x|<=L_*r_0, |P|<=P_*r_0 lies strictly inside the positive
radicand domain and the receiver neighbourhood. Smoothness on this square
provides C_0>0 with

$$\|w(x,P)-z_*\|\le C_0
 \max(|x|/L_*,|P|/P_*).$$

Set

$$r=\min\left(r_0,\frac{b}{4LC_0\lambda}\right)>0.$$

Every point of the square |x|<=L_*r, |P|<=P_*r therefore has an admissible
incoming momentum u(w), with ||u(w)||<=b/2, yielding the same exact Y_*.
Both the initial receiver energy and all fixed apparatus design parameters
are preserved. No fixed total energy equality for the entire apparatus was
assumed in R06; its uniform upper energy bound still holds.

## 3. Reconstruction risks and canonical projected area

For any deterministic estimator of initial canonical position and momentum
from the four records, define

$$\epsilon_x=\sup_{z\in S,\,\|a\|\le b}
 |\widehat x(G_\lambda(z,a))-x|,\qquad
\epsilon_P=\sup_{z\in S,\,\|a\|\le b}
 |\widehat P(G_\lambda(z,a))-P|.$$

At Y_*, the estimator has one answer while compatible x and P each span a
centred interval of the stated half-width. The triangle inequality between
the two endpoints proves, for every estimator,

$$\boxed{\epsilon_x\ge L_*r,\quad
\epsilon_P\ge P_*r,\quad
\mathcal H_{\rm rec}=\epsilon_x\epsilon_P\ge L_*P_*r^2.}$$

The projection of that common-record compatible receiver fibre onto the
(x,P) plane contains the whole square, so its ordinary canonical projected
area is at least 4L_*P_*r^2. This is projected area, not a volume of the
three-dimensional energy shell or a symplectic area assigned to that shell.
Both products have units ML^2/T, with no 2 pi normalization. The result is
an explicit positive lower bound; optimal constants and the full fibre are
not calculated.

At fixed lambda the bound scales as b^2 for small b, consistently with R16's
O_fixedlambda(b^2) upper bound on the reconstruction product. At fixed b,
weakening coupling does not remove this ambiguity: the displayed lower bound
saturates at L_*P_*r_0^2. Positivity is conditional on the fixed-width product
support and the specified record access. The quantity here is a reconstruction
error product. No lower bound for R06's accuracy-disturbance product follows
without a separate disturbance argument.

## 4. Next test: access to the incoming momenta

R18 should reveal the four initial probe momenta as extra records while
retaining positive unknown initial probe-position widths. Test the derivative
of final momenta with respect to those positions and its rank at small
coupling. Determine whether position preparation can still compensate a shell
patch, or whether the augmented records recover the receiver. This identifies
which apparatus variables must be calibrated before proposing a preparation
principle that selects an action scale.

C090–C091 are accepted by [written review](../reviews/fixed-preparation-B48.md).
The [B48 audit](../references/batches/B48.md) records established contraction
and indistinguishable-observation methods and bounded literature coverage.
