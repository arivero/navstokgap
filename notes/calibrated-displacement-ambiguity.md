# One calibrated displacement still leaves full receiver ambiguity

A known nonzero incoming probe displacement breaks R26's sign involution but
still permits distinct receiver states with exactly the same ten final
apparatus coordinates and the same two initial energies. A Borsuk–Ulam
argument produces actual equal-record pairs on a compact preparation sphere.
The resulting positive risk concerns the full receiver state in fixed component
units; it does not establish a positive canonical x–P error product.

R27, 2026-09-12. Retain [R25](full-apparatus-preparation-ambiguity.md)'s smooth
finite-duration apparatus, receiver energy E>0, positive clock speed, fixed
masses, pulse supports and cutoff margins. Require initial H_s=E,
H_app=H_0=M_c v_0^2/2, and q_1=c with c nonzero and |c|/L_1<b/4.
Here L_1 is the fixed position unit and b is the dimensionless apparatus
box half-width about R25's nominal preparation. Choose b sufficiently small
for its uniform flow bounds. Every point satisfying these constraints inside
the box is admitted. All ten final apparatus coordinates at known T are
observed exactly. Source coverage and proof review are recorded in
[B58](../references/batches/B58.md) and [the review](../reviews/calibrated-displacement-B58.md).

## 1. A nonempty preparation chart with eleven free coordinates

The apparatus energy is purely kinetic before the pulses. Set q_1=c and solve
its positive clock-momentum branch exactly:

$$p_s=\sqrt{2M_c\left(H_0-\sum_{j=1}^4\frac{\pi_j^2}{2M_j}\right)}. \tag{1}$$

The remaining apparatus coordinates q_2,q_3,q_4,pi_1,...,pi_4,s are eight
independent local coordinates near zero probe phase and s=s_0. At their
centre, (1) gives p_s=M_c v_0. Continuity supplies a fixed neighbourhood
with positive radicand and every apparatus coordinate inside half the box.
This is interior relative to the two imposed apparatus constraints.

For the receiver use three independent coordinates x,P,Q near zero, solving
its energy for the upper y branch:

$$y=\frac gd x+
\sqrt{\frac{2E-k_xx^2-P^2/\mu-Q^2/\nu}{d}},
\qquad k_x=a-g^2/d>0. \tag{2}$$

Equations (1)–(2) give a smooth injective chart Psi from an open neighbourhood
of zero in R^11 into the admissible initial states. Scale each of its eleven
free coordinates by its fixed physical component unit (and centre s at s_0).
Choose r>0 such that the closed parameter ball of radius r lies in this
neighbourhood with strict energy radicands and the b/2 apparatus margin.
The radius r depends on E,H_0,b,c and the component units, but not on lambda.
Initial pulses are absent throughout this chart. Reduce the common positive
coupling upper bound to retain R25's trajectory margins.

## 2. A topological theorem yields exact common records

Write G_lambda(z,eta) for the complete final apparatus record, in its ten
fixed component units. On the parameter sphere |u|_2=r, define

$$f_\lambda(u)=G_\lambda(\Psi(u))\in\mathbb R^{10}. \tag{3}$$

This is a continuous map S^10 to R^10. The Borsuk–Ulam theorem gives some
u_lambda on that sphere with

$$f_\lambda(u_\lambda)=f_\lambda(-u_\lambda). \tag{4}$$

The two initial states are distinct because Psi is injective. Both have
exactly q_1=c, H_s=E and H_app=H_0 by construction, and positive box margins.
The equality in (4) is exact, not an infinitesimal kernel or a dimension count.
Antipodes here are chart parameters: they do not reverse the physical receiver
or the calibrated displacement. No Hamiltonian sign symmetry is used.

## 3. The receiver states differ by a uniform amount

The equal-record pair cannot differ only in apparatus preparation. In fixed
Euclidean component norms, precondition G_lambda by the invertible free shear
S and put F_lambda=S^{-1}G_lambda. R25's smooth-flow argument, with constants
chosen in these norms on the same convex receiver ball and apparatus box, gives

$$\|D_\eta F_\lambda-I\|\le C\lambda\le\tfrac12,
\qquad \|D_zF_\lambda\|\le L\lambda. \tag{5}$$

For two states with equal G_lambda, integrate the first derivative along
the apparatus segment at fixed receiver state, and the second along the
receiver segment at fixed apparatus state. This yields

$$\tfrac12\|\eta_+-\eta_-\|_2
\le L\lambda\|z_+-z_-\|_2. \tag{6}$$

The segments are used only to estimate the unconstrained smooth map on its
convex domain; they need not stay on the two energy shells or calibration
surface. In particular, equal receiver states would force equal apparatus
states, contradicting injectivity of the chart.

There is also a quantitative bound. The eleven chart coordinates are an
orthogonal coordinate projection of the fourteen dimensionless initial
coordinates, up to constant centring. Consequently

$$2r=\|u_\lambda-(-u_\lambda)\|_2
\le\sqrt{\|z_+-z_-\|_2^2+\|\eta_+-\eta_-\|_2^2},$$

and (6) gives

$$\|z_+-z_-\|_2\ge
\frac{2r}{\sqrt{1+4L^2\lambda^2}}. \tag{7}$$

For deterministic estimation of all four initial receiver coordinates, let
R_z be the infimum over estimators of the worst-case Euclidean error in these
fixed component units on the constrained preparation class. The triangle
inequality at the common record proves

$$R_z\ge\frac{r}{\sqrt{1+4L^2\lambda^2}}>0. \tag{8}$$

The constants and r are fixed as lambda decreases. Thus liminf R_z>=r in
this weak-coupling limit. This dimensionless full-state risk need not be in
x or P: the unresolved difference may lie in the internal coordinates y,Q.
It gives neither an action-valued lower bound nor a universal scale.

## 4. What calibration changes and the next test

The involution of R26 sends q_1=c to -c and leaves the admitted class when
c is nonzero. Equations (1)–(8) replace it by a topological obstruction to
full receiver recovery. They use a fixed positive preparation neighbourhood,
exact initial energies and exact final records; they require no pulse-rank
assumption. Borsuk–Ulam is the established imported theorem; the constrained
chart and quantitative receiver bound are consequences for this apparatus.

Next R28: determine whether an equal-record pair under this same calibrated
two-energy preparation can be forced to differ in both x and P. Seek an
actual canonical pair with margins or prove canonical recovery despite hidden
internal coordinates. The full-state norm bound alone settles neither.
