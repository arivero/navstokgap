# Four-dimensional parallel insertions: one-loop shifts and the logarithm

**Result, 2026-09-28 (formal calculation and precise obstruction).** One
directional cut in four dimensions has the six coupling shifts (4) and
(10) below, as explicit, convergent Brillouin-zone integrals. They extend
the refereed $SU(2)$ mid-plane calculation to three coupled transverse
planes, arbitrary positive anisotropy and cut fraction $s$. The bridge
mass makes every one-step integral regular at zero momentum.

The universal logarithm belongs to the matched, four-dimensional
background-field determinant. Its coefficient is analytically

$$2b_0=\frac{11N}{24\pi^2},\qquad
 g_0^{-2}(2a)-g_0^{-2}(a)=-\frac{11N}{24\pi^2}\log2+O(g_0^2)
\tag{1}$$

**when the endpoints use the same coupling scheme.** For a full blocking
step between different action shapes, the right side additionally
contains $c_{\rm in}-c_{\rm out}$, equation (15). Returning the six heat
times and the anisotropy to their initial values leaves that difference
undetermined. The exact pushforward generates interactions already at
tree level; carrying them through the next elimination is essential.
Consequently four applications of the unperturbed one-step coefficients
alone do not establish (1). The missing task is the finite matching of
the generated action, or construction of a stationary action family
under rescaled blocking. Numerical evaluation of one lattice integral
would leave this obstruction in place.

**Status and inputs.** Theorem 1 concerns coefficients of a formal,
zero-image, bulk Laplace expansion. Its matrix and integral identities
are written derivations; uniform remainder estimates remain open.
Theorem 2 is a conditional one-loop matching theorem, with the continuum
logarithm derived analytically. Neither theorem establishes a continuum
measure or a physical mass gap. Inputs read here: the
[series/parallel note](series-parallel-gauge-refinement.md), Proposition 1,
heat-time table, Hypothesis P($\alpha$), including its size clause, and
§5; the [mid-plane calculation](su2-midplane-order-t.md), including N2,
N3 and the winding qualification; the
[midpoint formulas](su2-midpoint-exact.md), Theorems 1--4; and the
[zero-spacing note](zero-spacing-any-action.md), perturbative column and
finite $\Lambda$ matching (full-read: these sections). The new
three-dimensional determinant has received no independent referee review.

## 1. Normalization and a positive mid-space Hessian

Set $t=g^2=\hbar g_{\rm cl}^2$ and

$$\tau_{\mu\nu}=\frac{a_\mu a_\nu}
 {\prod_{\rho\ne\mu,\nu}a_\rho},\qquad
 t_{\mu\nu}=t\tau_{\mu\nu}.$$

Cut direction 1 at $s\in(0,1)$. With the trapezoid dual-length weights
of atlas §1b, every old and new transverse face has heat time
$2t\tau_{jk}$, $j,k\in\{2,3,4\}$. The cut faces have times
$st\tau_{1j}$ and $(1-s)t\tau_{1j}$. This prescription extends to $D=4$
because only the dual length in direction 1 changes. It describes one
cut of a uniform anisotropic lattice.

Write $m_e=m_{*e}e^{\xi_e}$ in the mid-vertex gauge, put
$\sigma=s(1-s)$, and use dimensionless momenta
$k\in\mathcal B_3=[-\pi,\pi]^3$ with measure $d^3k/(2\pi)^3$.
Define the three-by-three curl symbol and positive diagonal matrices by

$$\begin{gathered}
 (C\xi)_{jk}=(1-e^{ik_k})\xi_j+(e^{ik_j}-1)\xi_k,\quad j<k,\\
 M_{jj}=M_j=\frac1{\sigma\tau_{1j}},\qquad
 W_{jk,jk}=W_{jk}=\frac1{2\tau_{jk}},\\
 H_0(k)=M+C(k)^*WC(k),\qquad G(k)=H_0(k)^{-1}.
\end{gathered}\tag{2}$$

The exponent at zero coarse field is $\langle\xi,H_0\xi\rangle/(2t)$,
so the covariance is $tG$. There is an identity in colour space. For
fixed positive ratios,

$$M_{\min}I\le H_0(k)\le(M_{\max}+12W_{\max})I.\tag{3}$$

Indeed $C^*C$ has eigenvalues $0,Q,Q$, where
$Q=\sum_{j=2}^4(2-2\cos k_j)\le12$. In particular $H_0(0)=M$.
For isotropic midpoint cutting, $H_0=4I+C^*C/2$ and
$4I\le H_0\le10I$. The three-dimensional conditional theory has a
bridge mass in lattice units, even as $t\downarrow0$.

We extract the coefficient of $|X_{\mu\nu}|^2$ in the bulk local
amplitude $A_2$ of the normalized defect $\mathcal D$. If that
coefficient is $A_{\mu\nu}$ per coarse plaquette, write

$$\Delta(t_{\mu\nu}^{-1})=2A_{\mu\nu}+O(t),\qquad
 \delta_t^{\mu\nu}=2t\tau_{\mu\nu}A_{\mu\nu}+O(t^2).$$

Thus the shift is $O(t)$ **relative** to the inverse heat time; its
absolute leading value is $O(1)$. In continuum units the inverse
coupling shift for this plane is $2\tau_{\mu\nu}A_{\mu\nu}$, since
$a_\mu^2a_\nu^2/\prod_\rho a_\rho=\tau_{\mu\nu}$. All statements about
$O(t)$ below refer to formal loop order at fixed heat-time ratios.

## 2. N2: the three cut-plane shifts

**Theorem 1(a).** In the formal bulk expansion, for $SU(N)$ with
$C_A=C_2(\mathrm{adj})=N$ and the metric of the input notes,

$$\boxed{\begin{aligned}
 A_{1j}&=\frac{C_A\sigma}{24}
 \int_{\mathcal B_3}[1-M_jG_{jj}(k)],\\
 \delta_t^{1j}&=\frac{C_A\sigma\,t\tau_{1j}}{12}
 \int_{\mathcal B_3}[1-M_jG_{jj}(k)]+O(t^2),\quad j=2,3,4.
\end{aligned}}\tag{4}$$

The leading coefficients are strictly positive for positive transverse
weights. At isotropy and $s=1/2$ this becomes

$$\delta_t^{1j}=\frac{C_A t}{48}
 \int_{\mathcal B_3}\frac{\sum_{k\ne j}(2-2\cos k_k)}{8+Q}
 +O(t^2).\tag{5}$$

*Proof.* Use a constant commuting cut flux $X_{1j}=X$, all other cut
fluxes zero, and choose the geodesically interpolated mid-connection
flat. The classical defect vanishes on this test. Put

$$Q_Z=\frac{\operatorname{ad}Z}{2}\coth\frac{\operatorname{ad}Z}{2}.
$$

The bridge Hessian, divided by its value at $X=0$, is

$$\begin{aligned}
 h_{s,X}&=(1-s)Q_{sX}+sQ_{(1-s)X}\\
 &=I+\frac{\sigma}{12}(\operatorname{ad}X)^2+O(|X|^4).
\end{aligned}$$

This follows by taking the Hessians of the two squared distances,
weighted by $1/(s\tau_{1j})$ and $1/((1-s)\tau_{1j})$. Normalization
subtracts the determinant of the unconstrained bridge. Hence the
quadratic amplitude is

$$\frac{\sigma}{24}\int_{\mathcal B_3}
 (M_jG_{jj}-1)\operatorname{tr}_{\rm adj}(\operatorname{ad}X)^2
 =\frac{C_A\sigma|X|^2}{24}\int_{\mathcal B_3}(1-M_jG_{jj}).$$

The matrix $M^{1/2}GM^{1/2}$ lies between zero and $I$, with a strict
diagonal inequality on a set of positive momentum measure.
For (5), invert $4I+C^*C/2$ to get
$G=\frac14[I-C^*C/(8+Q)]$. $\square$

Suppressing direction 4 and taking $C_A=2$ gives exactly the cut
coefficient $t\int q/R\,/24$ of the D=3 note. The full colour trace,
rather than an isotropic average of the bridge covariance, fixes this
normalization.

## 3. N3: an explicit integral for each transverse plane

Take identical adjacent layers with a covariantly constant Abelian
flux $X_{jk}=BT_3$ in one transverse plane and zero flux in the other
two. Here $|T_3|=1$ for $SU(2)$; $j,k,h$ are the three distinct transverse
directions. The interpolated field is an exact stationary point.
For equal endpoints, the two zero-image heat-kernel amplitudes cancel
the Haar Jacobian, at every $s$:

$$k_{st_e}(e^\xi)k_{(1-s)t_e}(e^{-\xi})\,dm
 \ \propto\ e^{-|\xi|^2/(2\sigma t_e)}\,d\xi.$$

Thus the bridges contribute only $M$ to this determinant. The remaining
mid-face amplitude is $-B^2/24$ per $(jk)$ face for $SU(2)$.

Here is a fully specified matrix-integral expression retaining all
three edge components. It avoids a scalar Schur reduction of the third
component and leaves the lattice integral unevaluated. Put

$$p=k_j,\quad z=k_k,\quad w=k_h,\quad q(v)=2-2\cos v,\qquad
 d_B=\frac{B/2}{\sin(B/2)},\quad h_B=d_B\cos(B/2).$$

Use magnetic Weyl symbols, with $[z,p]=iB$. The Hermitian matrix
$K^{jk}_B$, supported on rows and columns $j,k$, has entries

$$\begin{aligned}
 (K^{jk}_B)_{jj}&=2h_B-2d_B\cos(z+B/2),\\
 (K^{jk}_B)_{kk}&=2h_B-2d_B\cos(p-B/2),\\
 (K^{jk}_B)_{jk}&=d_B\{(e^{-iB/2}-e^{-iz})e^{ip}
                       +e^{-i(z+B/2)}-e^{iB/2}\},\\
 (K^{jk}_B)_{kj}&=\overline{(K^{jk}_B)_{jk}}.
\end{aligned}\tag{6}$$

The other two plane matrices have the following nonzero entries,
with their reverse entries given by complex conjugation:

$$\begin{array}{lll}
 (K^{jh})_{jj}=q(w),& (K^{jh})_{hh}=q(p),&
 (K^{jh})_{jh}=(1-e^{-iw})(e^{ip}-1),\\
 (K^{kh})_{kk}=q(w),& (K^{kh})_{hh}=q(z),&
 (K^{kh})_{kh}=(1-e^{-iw})(e^{iz}-1).
\end{array}\tag{7}$$

Define

$$\begin{gathered}
 H_B=M+W_{jk}K^{jk}_B+W_{jh}K^{jh}+W_{kh}K^{kh}
       =H_0+BH_1+B^2H_2+O(B^3),\\
 H_1=\left.\partial_BH_B\right|_0,\qquad
 H_2=\left.\tfrac12\partial_B^2H_B\right|_0.
\end{gathered}$$

The derivatives here act on the explicit symbols (6)--(7). To include
the orbital contribution, use the ordered matrix products

$$\begin{aligned}
 \{A,B\}&=A_zB_p-A_pB_z,\\
 \mathcal Q(A,B)&=A_{zz}B_{pp}-2A_{zp}B_{zp}+A_{pp}B_{zz}.
\end{aligned}$$

For a real spectral parameter $v\ge0$ set

$$\begin{aligned}
 R_0&=(H_0+vI)^{-1},\\
 R_1&=-R_0\left(H_1R_0+\frac i2\{H_0,R_0\}\right),\\
 R_2&=-R_0\left(H_2R_0+H_1R_1
 +\frac i2\{H_0,R_1\}+\frac i2\{H_1,R_0\}
 -\frac18\mathcal Q(H_0,R_0)\right),\\
 \mathcal I_{jk}(M,W)&=-\operatorname{Re}\int_{[-\pi,\pi]^3}
 \frac{d^3k}{(2\pi)^3}\int_0^\infty\operatorname{tr}_3 R_2(k,v)\,dv.
\end{aligned}\tag{8}$$

Equations (6)--(8) are an explicit Brillouin-zone integral with an elementary resolvent
parameter. They require only inverses and derivatives of specified
three-by-three matrices. Bound (3) guarantees convergence at $v=0$;
$R_2=O(v^{-2})$ guarantees convergence at infinity.

*Derivation.* The squared-distance plaquette Hessian, for transported
oriented edge fluctuations $\eta_i$ and background logarithm $Y$, is

$$L^{(2)}=\frac12\left\langle\sum_i\eta_i,Q_Y\sum_i\eta_i\right\rangle
 +\frac12\sum_{i<l}\langle Y,[\eta_i,\eta_l]\rangle,
 \qquad L=\tfrac12|\log m_{\partial g}|^2.\tag{9}$$

In the gauge $U_j=U_h=1$, $U_k(x)=e^{Bx_jT_3}$, the $(jk)$ operator
is equation (11) of the mid-plane note. A term $f(z)E_j$ has Weyl
symbol $f(z-B/2)e^{ip}$, giving (6). The zero-flux $(jh)$ and $(kh)$
plaquettes have the covariant curls
$(1-e^{iw})\xi_j+(E_j-1)\xi_h$ and
$(1-e^{iw})\xi_k+(e^{iz}-1)\xi_h$, which give (7).
This retains the shared $h$-edge, the radial term $Q_Y$, and the ordered
commutator in (9).

Expanding $(H_B+v)\star(R_0+BR_1+B^2R_2)=I$ with
$A\star B=AB+(iB/2)\{A,B\}-(B^2/8)\mathcal Q(A,B)+O(B^3)$ gives (8).
The logarithm identity
$\log H=\int_0^\infty[(1+v)^{-1}I-(H+v)^{-1}]\,dv$
then proves that $\mathcal I_{jk}$ is the $B^2$ coefficient of the
charged determinant per site. Two charged real colours contribute
$\tfrac12\operatorname{Tr}_{\mathbb R}\log H
=\operatorname{Tr}_{\mathbb C}\log H$. The neutral colour is constant.
This is a bulk magnetic expansion, taken before imposing quantized
flux on a finite torus.

**Theorem 1(b).** The other three plane shifts are

$$\boxed{\begin{aligned}
 A_{jk}&=-\frac{C_A}{48}+\frac{C_A}{2}\mathcal I_{jk}(M,W),\\
 \delta_t^{jk}&=C_A t\tau_{jk}
 \left(-\frac1{24}+\mathcal I_{jk}(M,W)\right)+O(t^2).
\end{aligned}}\tag{10}$$

For $SU(2)$, the Jacobian contribution is $-1/24$ in $A_{jk}$ and the
determinant contribution is exactly (8). For $SU(N)$ the root planes
have charges $\alpha(T)$, with
$\sum_{\alpha>0}\alpha(T)^2=C_A|T|^2/2$; this multiplies the unit-charge
determinant by $C_A/2$. Also
$\log j(X)=\operatorname{tr}(\operatorname{ad}X)^2/24+O(|X|^4)$,
so the heat-kernel amplitude contributes $\tfrac12\log j(X)
=-C_A|X|^2/48$. The old-face heat-kernel ratio cancels its Jacobian.
Together these give (10). $\square$

As a dimensional reduction check, set $W_{jh}=W_{kh}=0$. The third
component becomes a constant determinant; with $M_j=M_k=4$ and
$W_{jk}=1/2$, (8) is the $B^2$ coefficient of $\log\det(8+K)$ of the
D=3 note. Its scalar reduction is exactly that note's integral (2),
including the Weyl-product correction. Simply adding three independent
copies of that two-dimensional integral would discard the shared
fluctuations in (7).

## 4. The infrared and the size clause

For every fixed positive anisotropy and $s\in(0,1)$, (3) makes the
integrands in (4) and (8) analytic near $k=0$. Their integral over a
ball $|k|<\varepsilon$ is $O(\varepsilon^3)$. The cut integrand even
vanishes at $k=0$. Thus the elementary mid-space propagator supplies
**zero coefficient of an infrared logarithmic divergence**. A finite
value containing $\log2$ could still arise from integration over the
whole Brillouin zone; its presence would require a matching argument
before identifying it with the beta function.

The finite-torus issue of P($\alpha$) survives in $D=4$. At isotropy and
$s=1/2$, take equal flat $SU(2)$ layers with adjoint twists
$\theta_j$ and $V_3=\prod_jN_j$. Since the charged determinant has two
transverse eigenvalues, its one-loop winding term is

$$\begin{aligned}
 \Omega_N(\theta)&=2\sum_k\log
 \frac{14-2\sum_{j=2}^4\cos(k_j+\theta_j/N_j)}
      {14-2\sum_{j=2}^4\cos k_j},\\
 0\le\Omega_N(\theta)&\le\frac{7V_3}{n_*}
           \left(\frac37\right)^{n_*},\qquad n_*=\min_jN_j.
\end{aligned}\tag{11}$$

The closed-walk expansion of $\log(14-\mathsf A_\theta)$ proves the
bound: at most $6^n$ walks of length $n$, winding requires $n\ge n_*$,
and $1-\cos(w\cdot\theta)\le2$. The leading factor 2 counts the
transverse eigenvalues. At fixed $N$ this term persists as $t\to0$.
The size clause $n_*\ge c_0/t$ gives density at most
$(7t/c_0)e^{-c_0\log(7/3)/t}$. It controls this winding contribution;
it leaves the bulk bridge mass intact. Positive bounded anisotropies
have analogous exponential decay with ratio-dependent constants.

Theorem 1 uses bulk coefficients, or a volume limit eliminating these
winding terms. Extending it to a normalized small-field estimate needs
the saddle, connected-kernel, heat-kernel-image and remainder controls
specified in §7 of the mid-plane note. P($\alpha$)'s size clause alone
supplies none of those missing bounds. Moreover a bound with $\alpha<1$
can absorb an $O(t)$ relative coupling change, so the inequality alone
cannot determine the one-loop coefficient.

## 5. Four halvings: what actually composes

Let $\mathcal L_r$ have its first $r$ directions halved, starting with
spacing $2a$ in every direction. Then $\mathcal L_4$ has spacing $a$,
and the unperturbed heat-time ratios are

$$\begin{array}{c|rrrrrr}
r&\tau_{12}&\tau_{13}&\tau_{14}&\tau_{23}&\tau_{24}&\tau_{34}\\\hline
0&1&1&1&1&1&1\\
1&1/2&1/2&1/2&2&2&2\\
2&1/4&1&1&1&1&4\\
3&1/2&1/2&2&1/2&2&2\\
4&1&1&1&1&1&1
\end{array}$$

Equations (4) and (10), relabeling direction 1 as direction $r$, give
the unperturbed defect from $\mathcal L_r$ to $\mathcal L_{r-1}$ using
row $r-1$. The coarsening integration proceeds in reverse order,
$r=4,3,2,1$. Denote the reference heat-kernel law on $\mathcal L_r$ by
$\mu_r$, its unperturbed defect by $\mathcal D_r$, and the accumulated
additional action by $\mathcal R_r$. Up to vacuum constants, exact
conditional integration says

$$\boxed{\mathcal R_{r-1}(U)=\mathcal D_r(U)
 -\log E_{\mu_r}\!\left[e^{-\mathcal R_r}\mid p_rU_r=U\right],
 \qquad\mathcal R_4=0.}\tag{12}$$

The conditional law here includes all mid-face weights. Proposition 1
specifies it through the bridge integral. Already $\mathcal D_4$ has
the nonzero Gaussian defect, its nonabelian classical completion and
its one-loop amplitude. Their conditional average in the next step
changes both the saddle and its Hessian. On smooth fields the Gaussian
defect starts at dimension six, but internal momenta in (8) range over
the whole Brillouin zone: that smooth-field suppression gives no
permission to discard it in a one-loop contraction.

At quadratic fluctuation order, exact composition has the familiar
Schur-complement identity

$$\det\begin{pmatrix}A&B\\ B^*&D\end{pmatrix}
 =\det D\,\det(A-BD^{-1}B^*).\tag{13}$$

It is the **successively updated** determinants that telescope.
Replacing each Schur complement by a new nearest-plaquette heat-kernel
Hessian changes the finite coupling matching. The four pristine
$\Psi$ integrals locate the generated terms; (12) governs their
composition. This is the precise qualification needed for the proposed
four-factor calculation in §5 of the series/parallel note.

## 6. Conditional matching theorem and the universal coefficient

**Theorem 2 (formal one-loop matching).** Suppose a gauge-covariant
blocking calculation retains the full generated action as in (12).
Assume its perturbative actions have local kernels with controlled
small-momentum expansions, the continuum Yang--Mills kinetic
normalization, no additional massless modes, and background Ward
identities. Assume that, after a common infrared regulator is inserted,
the one-loop determinants match the continuum operators

$$\Delta_{1,\mu\nu}=-D^2\delta_{\mu\nu}-2\operatorname{ad}F_{\mu\nu},
 \qquad \Delta_0=-D^2,\qquad
 \Gamma_1=\tfrac12\log\det\Delta_1-\log\det\Delta_0,
\tag{14}$$

up to infrared-integrable lattice differences and finite local
$F^2$ matching terms. The scalar determinant is the ghost determinant
in this background gauge. Its counterpart in a gauge-fixed bridge
calculation must be accounted for by the measure and gauge reduction.
Assume also that the coupling is extracted using this same background
normalization at the two endpoints.

Let $\ell=(\prod_\mu a_\mu)^{1/4}$, let
$\zeta_\mu=a_\mu/\ell$ specify the anisotropy, and let $\mathcal K$
specify all remaining dimensionless action kernels. Define the finite
matching coefficient $c$ by

$$u_R(\mu)=u(\ell)+2b_0\log(\ell\mu)
              +c(\zeta,\mathcal K)+O(t),\qquad u=g^{-2}.$$

Then one isotropic coarsening gives

$$\boxed{u_{\rm out}(2a)-u_{\rm in}(a)
 =-2b_0\log2+c(\zeta_{\rm in},\mathcal K_{\rm in})
                 -c(\zeta_{\rm out},\mathcal K_{\rm out})+O(t),
 \quad b_0=\frac{11N}{48\pi^2}.}\tag{15}$$

If the dimensionless action family returns to itself through one-loop
matching accuracy, or if its finite matching terms are subtracted in
defining the coupling, (15) gives (1).

*Analytical coefficient.* Write $F^2=\sum_{a,\mu,\nu}(F^a_{\mu\nu})^2$,
with both orders of $\mu,\nu$ included, so the classical action is
$u\int F^2/4$. The flat-space heat coefficient is

$$a_4(\Delta)=\frac1{(4\pi)^2}\int
 \operatorname{tr}\left(\tfrac12E^2+\tfrac1{12}\Omega_{\mu\nu}\Omega_{\mu\nu}\right).$$

For (14), the traces are $4C_AF^2$ for the vector $E^2$,
$-4C_AF^2$ for its $\Omega^2$, and $-C_AF^2$ for the ghost $\Omega^2$.
Consequently

$$\tfrac12a_4(\Delta_1)-a_4(\Delta_0)
 =\frac{C_A}{16\pi^2}\left(\frac56+\frac1{12}\right)\int F^2
 =\frac{11C_A}{192\pi^2}\int F^2.$$

The proper-time shell $a^2<\rho<(2a)^2$ gives
$\Gamma_{1,\rm shell}=-(11C_A/192\pi^2)\log4\int F^2$.
Multiplication by 4 to extract $u$ proves
$\Delta u=-11C_A\log2/(24\pi^2)$. This normalization calculation uses
[Vassilevich, §4.2.1, equations (4.28)--(4.34)](https://arxiv.org/pdf/hep-th/0306138)
(passage; DOI [10.1016/j.physrep.2003.09.002](https://doi.org/10.1016/j.physrep.2003.09.002),
metadata checked). It is the established one-loop coefficient.

*Telescoping.* Each reverse directional step multiplies $\ell$ by
$2^{1/4}$, and its universal scalar part is $-(2b_0/4)\log2$ in this
choice of scale. Its finite part is $c_{\rm before}-c_{\rm after}$.
Summing the four steps cancels the three intermediate matching terms
and gives (15). Plane-dependent anisotropy counterterms obey the same
endpoint cancellation in a fixed background convention. Splitting
$c$ into a reference anisotropy function and an action-dependent
remainder is a scheme choice. The anisotropy function cancels because
$\zeta_{\rm in}=\zeta_{\rm out}$; the remaining endpoint difference
requires $\mathcal K$ as well. Equation (12) changes $\mathcal K$ even
when the table returns to row 0. $\square$

For the pristine heat-kernel family, matching two isotropic bare
regularizations along a line of fixed renormalized coupling has the
same endpoint $c$ and gives (1). Identifying the coupling obtained by
projecting a single blocked density onto its plaquette term with that
bare-family coupling requires the finite conversion in (15). This is
the same distinction behind the finite $\Lambda$ ratios in the
zero-spacing note: if $u_B=u_A+d+O(t)$ at the same scale, then
$\Lambda_B/\Lambda_A=e^{-d/(2b_0)}$ at one loop.

## 7. The integral carrying the logarithm, and general cuts

The infrared singularity can be isolated without numerical quadrature.
With $\widehat k^2=\sum_{\mu=1}^4(2-2\cos k_\mu)$, use the reference
integral

$$J(a\mu)=\int_{[-\pi,\pi]^4}\frac{d^4k}{(2\pi)^4}
 \frac1{(\widehat k^2+(a\mu)^2)^2}
 =\frac1{8\pi^2}\log\frac1{a\mu}+j_{\rm lat}+o(1).
\tag{16}$$

To see its residue, split at $a\mu\ll\varepsilon\ll1$. In the inner
ball $\widehat k^2=k^2+O(k^4)$; the correction is integrable. The
spherical measure is $2\pi^2r^3dr/(2\pi)^4$, giving
$\log(\varepsilon/(a\mu))/(8\pi^2)$. The outer region has a finite
limit. Equivalently, integrating one continuum momentum first gives

$$\int_{\mathbb R}\frac{dk_1}{2\pi}\frac1{(k_1^2+r^2)^2}
 =\frac1{4r^3},\qquad
 \int_{\mu a<|k_\perp|<\varepsilon}
 \frac{d^3k_\perp}{(2\pi)^3}\frac1{4|k_\perp|^3}
 =\frac1{8\pi^2}\log\frac\varepsilon{a\mu}.\tag{17}$$

This is the three-dimensional propagator integral whose infrared end
carries the logarithm **after matching to the full massless
four-dimensional determinant**. The conditional propagator $G$ of (2)
has a different infrared end, proved regular in §4. Successive Schur
complements and the retained-field determinant must reconstruct the
massless expression before (17) applies. Thus assigning the logarithm
to the infrared end of each elementary massive $\Psi$ sum would miss
the required reassembly.

Under Theorem 2's hypotheses, the singular contribution to the inverse
coupling is $-(11C_A/3)J$, as fixed by (14). Therefore

$$-\frac{11C_A}{3}[J(a\mu)-J(2a\mu)]
 \longrightarrow-\frac{11C_A}{24\pi^2}\log2.\tag{18}$$

Changing a local regularization with the same continuum kinetic
operator changes $j_{\rm lat}$ and the finite tensor integrals, while
the residue in (16) stays fixed. In the inner ball the difference is
integrable; in the outer region it contributes only to $c$. The
scheme-independent object is this logarithmic residue. The finite
values of (8) depend on $M,W$ and $s$. Evaluating them numerically would
compute one-step finite shifts, and would still require (12) and the
endpoint matching to establish a universal isotropic step. The
lattice background-field method and its symmetry requirements are
established in
[Lüscher and Weisz (1995)](https://arxiv.org/abs/hep-lat/9504006)
(abstract; their renormalization result supplies context, with transfer
to this blocking retained as an explicit hypothesis).

**General fractions.** Equations (2), (4) and (8)--(10) already give the
one-step answer for every fixed $s\in(0,1)$. In (8) the fraction enters
only through $M_j=1/(\sigma\tau_{1j})$; the explicit N2 prefactor is
$\sigma/24$. The coefficients are invariant under $s\leftrightarrow1-s$
and their finite values generally depend on $s$. The three-dimensional
Jacobian term in (10) also remains present as $s$ approaches an endpoint.

A cut produces both lengths $sa_1$ and $(1-s)a_1$. Repeating such cuts
creates a nonuniform lattice, so the resulting global scale change
needs a specified schedule and matching convention. A factor
$\log(1/s)$ alone would describe following just one daughter; it omits
the other daughter and its dual-volume weights. For shape-regular
schedules whose successive effective actions satisfy Theorem 2 and
whose endpoint schemes agree, the coefficient per logarithm of the
physical scale is $2b_0$, independent of cut positions. Finite matching
terms and winding estimates can depend on the schedule. Uniform
control for fractions tending to 0 or 1 and for arbitrary nonuniform
meshes remains an additional obligation.

## 8. Consequence for STATE

Atlas cell 4 gains formal anisotropic one-step integrals and a precise
composition obstruction, with a conditional analytic recovery of
$2b_0$. The next bounded four-dimensional task is to retain the
Gaussian Schur complement and its nonabelian background completion
through (12), then determine the finite endpoint matching in (15).
This targets a concrete determinant identity; the D=3 normalized
estimate and the separate infrared mass-gap obligation remain open.
