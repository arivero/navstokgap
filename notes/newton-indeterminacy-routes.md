# Newton indeterminacy routes: the physical premise a record floor needs

**Result, 2026-09-27 (GPT-6 Astra).** The strongest completed route is a
conditional classical disturbance theorem: if every admissible mark and
its recording apparatus obey a uniform bound on the statistical speed
of Hamiltonian translations, with action constant $h_*$, then the
Galileo comparison satisfies

$$\boxed{\frac s8\sum_j\sup\Delta D_j+\frac J2\sum_j\sup\Delta X_j
\ge h_*\arcsin(1-2\epsilon).} \tag{1}$$

Here $s=F\tau^2/(2m)$, $J=F\tau$, and $\Delta$ is standard deviation
in the interpolating ensembles specified below. This is the classical
analogue of the Planck paper's Theorem 6, with its constants unchanged.
For Gaussian ensembles and affine canonical instruments, a covariance
restriction of minimum symplectic eigenvalue $\zeta$ supplies the needed
statistical-speed bound with **$h_*=2\zeta$**. A background-driven Gaussian
oscillator with mean energy $\zeta\omega$ has precisely that covariance
scale. Maintaining the restriction through all recordings, including
readouts of earlier apparatus, is the additional premise.

The two proposed physical candidates leave that premise open. A hidden
Lorentz-invariant background fixes a spectral shape and can supply a
stationary covariance, while records can infer its effects indirectly.
Newton's inflexion observations supply geometry and colour dependence;
even an exact law $\theta b=C\Lambda$ admits deterministic canonical
kicks. The missing physical assertion is therefore explicit: prove the
statistical-speed estimate (7) for an admissible class of records closed
under composition, and identify $2\zeta=\gamma h_{\rm rad}$ with a fixed
pure number $\gamma>0$. Theorem U in the
[unit note](necessity-unit-and-indeterminacy.md) defines $h_{\rm rad}$ from
thermal radiation. Neither candidate presently fixes $\gamma$ or
establishes the all-instrument estimate.

The new results below are written derivations within stated models.
Source claims carry their reading levels; the historical observations
supply no fitted or invented data. The scope remains Newton's inertial
line versus falling parabola and the records used to distinguish them.

## 1. What the corrected two-pointer theorem requires

Theorem I in the [unit note](necessity-unit-and-indeterminacy.md) permits
Hamiltonian dynamics, the specified independent rectangular preparations,
Bayesian coordinate records, and access to two pulses with a stored
first reading. The second pulse determines the momentum that caused the
first recoil. A physical floor can exclude the first preparation, the
second pulse, or preservation of the first reading while its conjugate
is examined. Abstract Liouville dynamics and Bayesian reasoning alone
leave those instrument questions open.

Three quantities must be kept distinct: the unconditional disturbance
spread, uncertainty in that disturbance conditional on the completed
record, and concentration of the body's posterior. Equation (1) charges
the first quantity in particular interpolating states. The construction
of a small posterior tests preservation of a proposed epistemic
restriction. A proof connecting these questions is supplied in §4,
rather than inferred from the dimensions of a posterior ceiling.

## 2. Random classical background: what can be derived

**Source boundary.** [Marshall 1963, Random electrodynamics](https://doi.org/10.1098/rspa.1963.0220)
(publisher abstract via Crossref) starts from stationary classical
oscillator distributions matching quantum ground states and calculates
a radiation field that sustains them. [Boyer 1975](https://doi.org/10.1103/PhysRevD.11.790)
(publisher abstract) assumes a Lorentz-invariant random electromagnetic
boundary field and sets its scale by $\hbar$. These statements supply
models and a normalization choice. They leave a universal bound on
conditional records to a further argument.

Write the mean energy per angular-frequency mode of a homogeneous,
isotropic Gaussian zero-point field as

$$\mathcal E_0(\omega)=\zeta\omega,\qquad
u_0(\omega)=\frac{\zeta\omega^3}{\pi^2c^3},\qquad \zeta\ge0, \tag{2}$$

where $u_0(\omega)\,d\omega$ is its energy density including two
polarizations. The Lorentz-invariant spectral family permits every
normalization $\zeta$, including zero. The conventional choice is
$\zeta=\hbar/2=h_P/(4\pi)$. Its integral over all frequencies diverges;
a stationary oscillator calculation therefore needs specified response,
radiation damping and a controlled approximation or regulator. A
frequency cutoff in a laboratory frame itself adds a preferred frame.
The finite thermal spectrum in Theorem U and this zero-point spectrum
have different integrability assumptions.

**Proposition 1 (stationary oscillator, explicit conditional model).**
Suppose a linear oscillator of mass $m$ and frequency $\omega$ has the
centered Gaussian stationary law with mean energy $\zeta\omega$,
$\zeta>0$, and phase-rotation invariance. Then

$$\Sigma_0=\begin{pmatrix}\zeta/(m\omega)&0\\0&\zeta m\omega\end{pmatrix},
\quad \sqrt{\det\Sigma_0}=\zeta,\quad
\|\rho_0\|_\infty=\frac1{2\pi\zeta}. \tag{3}$$

*Proof.* Rotation invariance in the scaled coordinates
$(\sqrt{m\omega}\,q,p/\sqrt{m\omega})$ makes the covariance scalar.
The mean of $p^2/(2m)+m\omega^2q^2/2$ is then $\omega$ times that
scalar, fixing it to $\zeta$. Gaussian normalization gives the last
identity. $\square$

An explicit bath approximation producing (3) is the linear stochastic
equation, for damping $\gamma_d>0$ and standard Wiener noise $W_t$,

$$dq=(p/m)\,dt,\qquad
dp=(-m\omega^2q-\gamma_d p)\,dt+\sqrt{2\gamma_d m\omega\zeta}\,dW_t.$$

At stationarity the three second-moment equations give successively
$E(qp)=0$, $E(p^2)=m^2\omega^2E(q^2)$, and
$2\gamma_d E(p^2)=2\gamma_d m\omega\zeta$. The stable linear dynamics with
Gaussian noise has the Gaussian invariant law (3). Its noise strength
is supplied here. Deriving this resonant bath approximation from (2),
and preserving its restrictions during measurements, remain physical
obligations. The model gives a stationary prior density ceiling with
constant $2\pi\zeta$.

**Proposition 2 (indirect observations).** Even if records have no direct
access to the background, a prior with covariance (3) need not retain
its ceiling after observing the body. In canonical scaled coordinates,
let $Z\sim N(0,\zeta I_2)$ and let a permitted observation be
$Y=Z+N$, with independent $N\sim N(0,v I_2)$, $v>0$. Then

$$\operatorname{Cov}(Z\mid Y)=\frac{\zeta v}{\zeta+v}I_2,\qquad
\|\rho(\cdot\mid Y)\|_\infty=
\frac{\zeta+v}{2\pi\zeta v}\longrightarrow\infty\quad(v\downarrow0). \tag{4}$$

*Proof.* Completing the square in
$\exp[-|z|^2/(2\zeta)-|y-z|^2/(2v)]$ gives (4).
The measured variable is the body; no field coordinate is recorded.
$\square$

This tests the proposed clause about background access. Realizing $Y$
by a physical instrument is the question that a floor must answer.
The two-pointer mechanism shows why a prior-only ceiling supplies no
answer. If all such observations are forbidden, their exclusion must
come from the admissible couplings, readout noise or disturbance law.
Initial correlations with a field alone do not establish the exclusion.

**A sufficient stronger premise.** Suppose at the *time whose state is
being inferred*, after conditioning on the entire available record $R$,
the body is $Z=Z'+\Xi$, where $\Xi\sim N(0,\Sigma_*)$ is independent of
$(Z',R)$ and $\sqrt{\det\Sigma_*}=\zeta>0$. Then

$$\rho(z\mid R)\le\frac1{2\pi\zeta},\qquad
\operatorname{Cov}(Z\mid R)\succeq\Sigma_*. \tag{5}$$

The first inequality follows by convolving a probability measure with
the Gaussian kernel; the second follows by adding covariances when they
exist. Thus $\Delta q\Delta p\ge\zeta$. The premise demands a residual
innovation independent even of *indirect* records. A record of $Z$
after the innovation generally destroys that independence. A diffusion
with covariance $2D\Delta t$ has
$\sqrt{\det(2D\Delta t)}=2\Delta t\sqrt{\det D}$ for one canonical pair,
which goes to zero with the unobserved interval. A universal positive
$\zeta$ therefore needs an additional time-independent restriction.
Moreover, fresh noise applied after a completed record broadens the
present body without concealing what the record already learned about
its past. Equation (5) alone does not yield (1).

## 3. Newton's inflexion: what the observations warrant

The local [Opticks companion](../docs/classics/Newton_Opticks_1730_fits_and_queries.md)
holds fits and queries; **Book III, Part I, Observations 1--11 are absent
from its local excerpt**. The 1730 fourth-edition text was checked online
in [Gutenberg, Book III, pp. 318--337](https://www.gutenberg.org/files/33504/33504-h/33504-h.htm)
(reading level: passage, Obs. 1--11). It gives shadow and fringe widths,
knife separations and screen distances. Observation 8 says that moving
the second knife changes the bending at the first. Observation 9 relates
fringe intersections to screen distance; Observation 11 compares colours.
The local source addition needed for historical publication is an
edition-labelled transcription of these observations and their tables,
checked against the 1730 pages and diagrams, with a companion and checksum.
No data have been silently added to the held excerpt.

The earlier [1718 second edition, Newton Project NATP00051](https://www.newtonproject.ox.ac.uk/view/texts/diplomatic/NATP00051)
(reading level: passage, Obs. 8--11, pp. 305--312) corroborates the
second-knife dependence. Newton writes in Observation 8:

> the other Knife increases the bent.

That commits him to dependence on the apparatus geometry. The same
passage says the fringe rays' distances from a knife stay unchanged
while the angles increase as the knives approach. A single function
$\theta(b,\mathrm{colour})$ would need additional geometry variables or
an isolated-edge limiting prescription. The editions also differ in the
Observation 9 table: the third screen distance is $8\frac25$ inches in
the 1718 transcription and $8\frac35$ in Gutenberg's 1730 transcription.
A scan comparison would be required before treating either entry as a
precise fitting datum; no numerical fit is used here.

**Inference from the source.** A fringe position on a screen describes
an ensemble intensity feature. Recovering an individual incoming impact
parameter $b$ and outgoing angle $\theta$ needs a ray-assignment model,
source geometry and a propagation law. Establishing
$\theta b=C\Lambda$ per colour would additionally require matching the
inflexion apparatus to an independently calibrated fit interval
$\Lambda$. The cited observations do not supply that identification or
an irreducible distribution of unrecorded kicks.

**Proposition 3 (even the proposed law permits a determinate kick).**
Grant an isolated-edge, paraxial corpuscle law $\theta b=C\Lambda$ with
fixed longitudinal momentum $p_\parallel$ and set
$K=Cp_\parallel\Lambda$. On $b>0$ the transverse canonical map

$$b'=b,\qquad p_b'=p_b+K/b \tag{6}$$

has $\theta\simeq\Delta p_b/p_\parallel=C\Lambda/b$ and preserves
$db\wedge dp_b$.

*Proof.* The integrated impulsive potential is
$V(b)=-K\log(b/b_0)$ for an arbitrary reference length $b_0$.
Hamilton's impulse equation gives $\Delta p_b=-V'(b)=K/b$, and
$db'\wedge dp_b'=db\wedge(dp_b-Kb^{-2}db)=db\wedge dp_b$.
$\square$

If a record localizes $b$ to an interval of width $d$ in $b\ge b_{\min}>0$,
the kick's conditional support width is at most $Kd/b_{\min}^2$ for
$K>0$, which tends to zero as $d\downarrow0$. Momentum conservation can
assign the opposite kick to the edge without making it unknown. Thus
this bending law would change a corpuscle's trajectory while allowing
Bayesian inference. It would leave Theorem I's instrument question open.
The extra physical premise must make a complementary part of the
interaction persistently inaccessible to every permitted subsequent
record.

## 4. A constructive replacement: a statistical-speed theorem

This section isolates a quantitative hypothesis that actually implies
the desired disturbance bound. It also identifies a restricted Gaussian
class for which the hypothesis has a written proof.

For probability densities define the classical statistical angle

$$B(\rho,\sigma)=\arccos\int\sqrt{\rho\sigma}\,dz.$$

The square roots are unit vectors in $L^2$. Along a smooth Hamiltonian
path generated by an action-valued function $A$, the speed is
$\frac12\|\{A,\log\rho\}\|_{L^2(\rho)}$. Markov kernels contract this
angle, and Cauchy--Schwarz gives
$\mathrm{TV}(\rho,\sigma)\le\sin B(\rho,\sigma)$.

**Premise F (statistical speed controlled by disturbance).** On every
joint body--apparatus state used in the translation/hybrid paths of a
protocol, the relevant generators obey

$$\frac12\|\{A,\log\rho\}\|_{L^2(\rho)}
\le\frac{\Delta_\rho A}{h_*},\qquad h_*>0. \tag{7}$$

The state class is closed under the required translations, preparation
of additional apparatus, and retained-record composition. Smoothness,
integration by parts and finite second moments are assumed where used.
For adaptive protocols (7) must hold uniformly over the conditional
states and settings that the proof encounters. Only generators from the
protocol's hybrid paths are required.

**Theorem F (classical conditional form of Planck Theorem 6).** Suppose
body motion between marks is Newtonian free motion or constant-force
motion; marks, including any readout back-action on retained apparatus,
have canonical dilations $M_j$; their records are Markov readouts of
apparatus coordinates. Suppose this instrument class satisfies Premise F
and the decision error is at most $\epsilon<1/2$ for every allowed pair
of initial body states under the two hypotheses. Define
$D_j=p\circ M_j-p$ and $X_j=q\circ M_j-q$. Then (1) holds.

*Proof.* Choose a line $a+bt$ and offset
$c(t)=Ft^2/(2m)-a-bt$. Translate the free initial state by
$(c(0),mc'(0))$ to obtain the forced initial state. Between marks the
offset is $(c(t),mc'(t))$. As in the
[disturbance note](record-costs-disturbance.md), compare successive
hybrids which remove this offset immediately before or after mark $j$.
Their difference is the canonical commutator
$T(-w_j)M_jT(w_j)M_j^{-1}$, $w_j=(c_j,mc_j')$.

Interpolating $w_j\mapsto u w_j$, $0\le u\le1$, gives a Hamiltonian
generator which, after pulling back through the canonical maps, is
$A_j=c_jD_j-mc_j'X_j$ up to sign. The Poisson bracket, probability
integral and variance are invariant under the same change of canonical
coordinates. By (7) the angle of this path is at most
$h_*^{-1}\sup\Delta A_j$. Readout and all later common processing
contract the angle. The triangle inequality over hybrids therefore gives

$$B(P_{\rm I},P_{\rm F})\le
\frac1{h_*}\sum_j\sup\Delta(c_jD_j-mc_j'X_j).$$

For a test with equal-prior error at most $\epsilon$,
$\mathrm{TV}(P_{\rm I},P_{\rm F})\ge1-2\epsilon$, so the left side is at
least $\arcsin(1-2\epsilon)$. The minimax line is
$a+bt=F(\tau t-\tau^2/8)/(2m)$; it gives
$|c_j|\le s/8$ and $m|c_j'|\le J/2$. The variance triangle inequality
proves (1). Conditional suprema extend the same hybrid argument to
adaptive readouts. $\square$

Theorem F uses a classical statistical angle throughout. Its proof
states the extra premise required to replace the quantum generator
bound; it does not infer that premise from a density ceiling.

### The Gaussian realization and its exact constant

Let $z$ comprise $n$ canonical pairs, with Poisson matrix $\Omega$ and
Gaussian covariance $\Sigma>0$. Impose the covariance restriction

$$\Sigma+i\zeta\Omega\succeq0 \qquad(\zeta>0), \tag{8}$$

equivalently, all symplectic eigenvalues of $\Sigma$ are at least $\zeta$.
For one pair this is $\det\Sigma\ge\zeta^2$. Gaussianity is an additional
assumption beyond any covariance or density bound.

**Lemma G.** Under (8), every affine generator $A=a^{\sf T}z+a_0$
satisfies (7) with $h_*=2\zeta$.

*Proof.* Direct differentiation of the Gaussian density gives

$$\|\{A,\log\rho\}\|_{L^2(\rho)}^2
=a^{\sf T}\Omega\Sigma^{-1}\Omega^{\sf T}a.$$

A real symplectic change of basis puts $\Sigma$ into blocks $\nu_j I_2$.
There $\Omega\Sigma^{-1}\Omega^{\sf T}$ has blocks $\nu_j^{-1}I_2$ and
$\nu_j\ge\zeta$ implies
$\Omega\Sigma^{-1}\Omega^{\sf T}\preceq\Sigma/\zeta^2$.
Consequently half the displayed norm is at most
$\sqrt{a^{\sf T}\Sigma a}/(2\zeta)=\Delta A/(2\zeta)$.
For one pair at $\det\Sigma=\zeta^2$ equality holds for every affine $A$.
$\square$

Affine canonical instruments have affine $D_j,X_j$, hence affine hybrid
generators. If all entering and retained conditional Gaussian ensembles
satisfy (8), Theorem F follows with $h_*=2\zeta$. This is a concrete
restricted instrument theorem. The condition must cover pointers that
will be reused and the physical memory of earlier readings. An ideal
passive reading of a retained pointer coordinate followed by an equally
sharp reading of its conjugate violates that closure. That is the precise
point at which the Theorem I protocol becomes inadmissible.

[Bartlett, Rudolph and Spekkens 2012](https://arxiv.org/abs/1111.5057)
(author abstract) give a related established realization by imposing a
covariance uncertainty condition and maximum entropy, and deriving
allowed Gaussian preparations, transformations and measurements. Lemma G
makes the needed constant and the link to this record problem explicit.
Identifying $\zeta=\gamma h_{\rm rad}/2$ would turn (1) into the requested
$\gamma h_{\rm rad}$ floor. Choosing $\zeta=h_P/(4\pi)$ gives
$h_*=h_P/(2\pi)$. Both identifications are additional physical inputs.

### The boundary of this route

Even a Gaussian posterior satisfying (8) cannot satisfy (7) for all
nonlinear generators. For independent centered Gaussian $q,p$ with
variances $\sigma_q^2,\sigma_p^2$, take the bounded action generator
$A=A_0\sin(kq)$. Direct differentiation and the Gaussian Fourier integral give

$$\Delta A^2=\frac{A_0^2}{2}(1-e^{-2k^2\sigma_q^2}),\qquad
\|\{A,\log\rho\}\|^2=
\frac{A_0^2k^2}{2\sigma_p^2}(1+e^{-2k^2\sigma_q^2}). \tag{9}$$

Thus the statistical speed grows without bound relative to $\Delta A$
as $k\to\infty$, even though the Gaussian covariance is unchanged.
A floor valid for every instrument needs control of these fine-scale
couplings, or a different dynamical/state framework supplying an
all-generator bound. A stationary Gaussian bath and the exclusion of
direct bath records alone provide neither control.

## 5. Consequence for STATE

The live Newton obligation is the physical justification of Premise F,
or a comparably strong restriction on the composition of recordings,
with $h_*=\gamma h_{\rm rad}$ and a fixed $\gamma>0$. The Gaussian
instrument class gives an exact conditional theorem with $h_*=2\zeta$;
SED supplies a candidate covariance mechanism but leaves record closure
and scale matching open. Newton's checked inflexion passages motivate
apparatus-dependent bending and leave a deterministic canonical
countermodel. A further source hunt or a fringe fit alone would leave
this operational obligation unchanged.
