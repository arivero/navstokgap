# An unknown clock hides an exact fixed-energy receiver phase

For an admissible fixed pulse design, eight exact final pointer coordinates
and known incoming probe momenta leave a smooth family of receiver states on
one exact energy shell when the initial clock data are hidden. Both initial
canonical coordinates vary along this family. Consequently their worst-case
reconstruction-error product is positive at fixed clock preparation width.

R20, 2026-09-11. Use [R19](full-pointer-recovery.md)'s apparatus and common
compact cutoff margins, with incoming probe momenta fixed and revealed at
zero. The observation time T and Hamiltonian are known. Initial probe
positions and clock position/momentum range independently over small positive
boxes; the receiver ranges over H_s=E>0. The family constructed below lies
inside this Cartesian support. This is a design-existence result and a
preparation-dependent reconstruction bound. Literature status is in
[B51](../references/batches/B51.md).

## 1. Reduce identical records to one energy equation

Write the clock data as c=(s,v), with p_s=M_c v and v>0. Let M generate the
free receiver flow Phi_t, H_s(z)=z^T Gz/2 with G positive definite, and

$$A_{s,v}=K\int_0^T f_j(s+vt)e_x\Phi_t\,dt\quad\hbox{(row j)}.$$

R19's scaled eight-record map extends smoothly to lambda=0:

$$F_{\lambda,c}(z,q)=(-A_cz,q)+O_{C^1}(\lambda). \tag{1}$$

The extension and estimate hold also for clock derivatives: divide the
integrated momentum equation by lambda before taking the limit, then use
smooth finite-time flow dependence on all initial data. All pulses remain
interior for clocks in the chosen box. Fix nominal c_0=(s_0,v_0), an interior
probe position q_*=0, and a shell point z_* to be selected below. Set
Y_lambda=F_{lambda,c_0}(z_*,0).

Since the derivative in (z,q) at lambda=0 is diag(-A_c,I), the parameter
implicit-function theorem gives a smooth local solution

$$F_{\lambda,c}(z_\lambda(c),q_\lambda(c))=Y_\lambda,$$
$$z_0(c)=A_c^{-1}A_{c_0}z_*,\qquad q_0(c)=0. \tag{2}$$

Neighbourhoods can be chosen uniformly for sufficiently small lambda,
including zero. This follows by a contraction with the fixed invertible
derivative on a small product neighbourhood. At positive fixed lambda these
are identical unscaled final records as well. The remaining physical
constraint is the scalar equation

$$e_\lambda(c):=H_s(z_\lambda(c))-E=0. \tag{3}$$

Thus clock dimension counting is replaced by a specific shell equation.

## 2. Clock offset changes receiver phase at zero coupling

Interior pulse support permits integration by parts, giving the exact identity

$$\partial_s A_{s,v}=-A_{s,v}M/v.$$

Equation (2) therefore gives at c_0

$$\partial_s z_0=Mz_*/v_0,\qquad \partial_s e_0=0. \tag{4}$$

The last equality uses G M+M^T G=0: free receiver motion preserves its
quadratic energy. A change of clock offset is, to leading order, a change
of receiver phase. A transverse clock-speed derivative will keep this
phase freedom on the exact interacting energy shell.

## 3. A fixed pulse design with transverse speed response

Choose four distinct positive dimensionless numbers a_j and a nonnegative
smooth bump phi of positive integral, supported in (-1,1). Fix eta>0 small
enough that the intervals a_j+eta(-1,1) are positive and disjoint. For a
positive design time epsilon set

$$f_j(s)=\phi\left(\frac{s-s_0-v_0\epsilon a_j}
                                  {v_0\epsilon\eta}\right).$$

For small epsilon all pulses finish before T. With r=v_0/v and t=r epsilon u,

$$A_{s_0,v,j}=K r\epsilon\int\phi((u-a_j)/\eta)
                         e_x\exp(Mr\epsilon u)\,du.$$

The first four Taylor rows e_x M^n, n=0,1,2,3, are independent by R06.
The moment matrix W_{jn}=integral phi((u-a_j)/eta)u^n/n! du is invertible
for small fixed eta: its row-normalized limit is the Vandermonde matrix
a_j^n/n!. Expanding the determinant by multilinearity, the first nonzero
power uses distinct n=0,1,2,3. Hence, uniformly with one v derivative near v_0,

$$\det A_{s_0,v}=D(r\epsilon)^{10}(1+O(\epsilon)),\qquad D\ne0. \tag{5}$$

The exponent is four integration factors plus 0+1+2+3. Analyticity of the
matrix exponential gives the differentiated remainder after factoring the
first nonzero coefficient. Fix epsilon sufficiently small once and for all.
Then A is invertible and, putting B=-A^{-1}partial_v A at c_0,

$$\operatorname{tr}B=-\partial_v\log|\det A|
                     =10/v_0+O(\epsilon)>0. \tag{6}$$

This design limit is used only to prove existence. Pulse widths, masses and
all derivative bounds subsequently stay fixed; reducing lambda_0 meets the
apparatus force ceilings and cutoff margins.

Let S_B=(GB+B^T G)/2. Its G-normalized trace is tr(B)>0, so it has a
positive quadratic direction. Choose z_* on H_s=E with z_*^T S_B z_*>0.
This is an open subset of the shell. Within it choose also
P_*^{state} nonzero and -a x_*+g y_* nonzero: the excluded hyperplanes have
empty relative interior. These conditions imply

$$\partial_v e_0=z_*^T GBz_*>0,\quad
(Mz_*)_x=P_*^{state}/\mu\ne0,\quad
(Mz_*)_P=-a x_*+g y_*\ne0. \tag{7}$$

The symbol P_*^{state} here is the chosen state's momentum, distinct from
the fixed momentum unit P_* used in risk bounds.

## 4. Exact interacting shell family and preparation margins

By (7) and smooth dependence, partial_v e_lambda remains positive near
(s_0,v_0) for all sufficiently small lambda. Since e_lambda(c_0)=0, solve
(3) as v=v_lambda(s), with v_lambda(s_0)=v_0. Equations (4) and (7) give

$$v'_\lambda(s_0)=O(\lambda),\qquad
\frac{d}{ds}z_\lambda(s,v_\lambda(s))\bigg|_{s_0}
       =Mz_*/v_0+O(\lambda). \tag{8}$$

Both canonical components therefore have nonzero derivatives. Choose a fixed
small offset interval |s-s_0|<=sigma within the implicit-function domains.
Continuity, first in s and then in lambda, gives physical constants k_x,k_P>0
such that along the whole interval the two derivatives retain their signs
and have magnitudes at least k_x,k_P. The constants have units respectively
one and momentum/length, since s is a length coordinate.

At lambda=0 equation (4) holds along the family at fixed v_0, so that
v_0(s)=v_0 and q_0(c)=0. Uniform smoothness gives
v_lambda(s)-v_0=O(lambda |s-s_0|) and
q_lambda(s,v_lambda(s))=O(lambda |s-s_0|). Choose sigma smaller than half
the physical clock-position half-width. For fixed positive clock-momentum
and probe-position half-widths, reduce lambda_0 if necessary to leave at
least half their margins. Receiver energy is exactly E throughout. Known
incoming probe momenta and all eight final records agree exactly. The
apparatus upper resource bounds persist on the inherited compact domain.

## 5. A phase uncertainty gives a canonical risk product

The endpoints s_0-sigma and s_0+sigma have canonical separations at least
2 k_x sigma and 2 k_P sigma and one common record. Every deterministic
estimator consequently has worst-case initial-coordinate errors

$$\epsilon_x\ge k_x\sigma,\qquad
\epsilon_P\ge k_P\sigma,\qquad
\mathcal H_{\rm rec}\ge k_x k_P\sigma^2>0. \tag{9}$$

The product has action units. This curve need not enclose positive canonical
area; positive coordinate-risk products and positive phase-space area are
different assertions. Equation (9) survives sufficiently small positive
coupling with one fixed sufficiently small sigma and fixed preparation
widths. It closes as the admitted clock-offset interval contracts. The
known-clock result R19 recovers zero exact-record risk by removing precisely
this preparation freedom.

Next R21: reveal only the initial clock position, leaving its momentum
unknown. The transverse derivative (7) suggests local recovery after imposing
the receiver energy shell. Test uniform local uniqueness and record stability,
and separate them from recovery on the entire shell.
