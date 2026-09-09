# Bound motion: transport variance and a canonical action estimator

A phase-uniform circular orbit has vanishing short- and long-window transport
response, while twice its projected canonical covariance area equals its
orbital action at every time. This supplies an action estimator for bound
mechanics and separates conservation of a prepared scale from its selection.
A15, 2026-09-09; C054–C055, written proof and sequential B29 source review.

## 1. One orbit, one preparation

Take any circular solution of the planar external-potential Hamiltonian
$H=\sqrt{m^2c^4+c^2|p|^2}+V(|q|)$ with radius $R>0$, momentum magnitude
$P>0$ and positive angular frequency $\omega$. Put

$$
q(t)=R(\cos\theta,\sin\theta),\quad
p(t)=P(-\sin\theta,\cos\theta),\quad
\theta=\omega t+\Phi,\quad \Phi\sim\operatorname{Unif}[0,2\pi).
$$

Hamilton's velocity law gives $P=\gamma mR\omega$, where
$\gamma=(1-R^2\omega^2/c^2)^{-1/2}$. The normalized orbital action is
$\ell=(2\pi)^{-1}\oint p\cdot dq=RP$.
Use the canonical Cartesian projection $x=q_1$, $p_x=p_1$; the physical
coordinate is bounded and the preparation is invariant. For the singular
Kepler circles C052 gives $\ell>k/c$; C053 supplies softened circles with
arbitrarily small positive $\ell$. Newtonian circles obey the same formulas
with $P=mR\omega$ and $\gamma=1$.

## 2. What a finite observation window measures

Let $z=\omega\Delta>0$. Uniform-phase trigonometric averaging gives
$\mathbb E[x(t)x(t+\Delta)]=(R^2/2)\cos z$. Consequently

$$
\mathsf h_x(\Delta)
=\frac{m}{\Delta}\operatorname{Var}(x(t+\Delta)-x(t))
=\frac{mR^2}{\Delta}(1-\cos z)
=\frac{\ell}{\gamma}\frac{1-\cos z}{z}.
$$

At a known initial position $x\in(-R,R)$, the two velocity signs have equal
conditional weights. Their next positions are
$x\cos z\pm\sqrt{R^2-x^2}\sin z$. This specifies the conditional version,
with the continuous degenerate extension at the endpoints, and gives

$$
\operatorname{Var}(x(t+\Delta)\mid x(t)=x)
=(R^2-x^2)\sin^2z.
$$

Its phase-averaged action coefficient is
$\overline{\mathsf h}_{\rm cond}=\ell\sin^2z/(2\gamma z)$.
Conditioning on the full canonical state makes the future deterministic.
The conditional variance here measures the unobserved direction at a cut.

Both coefficients vanish as $\Delta\downarrow0$ and as $\Delta\to\infty$.
There is no parametrically broad positive plateau of orbital-action size in
this one-frequency family. Indeed $1-\cos z\le\min(z^2/2,2)$, so
$\mathsf h_x\ge\eta\ell$ for fixed $\eta>0$ requires

$$2\gamma\eta\le z\le\frac{2}{\gamma\eta}.$$

Every interval satisfying this lower bound therefore has endpoint ratio at
most $1/(\gamma^2\eta^2)$. The statement keeps the positive fraction $\eta$
fixed; a broad intermediate plateau in another model requires additional
time scales and a separate estimate.

## 3. A canonical covariance area

For $Z=(x,p_x)$ define the centered covariance matrix $\Sigma$ and

$$
\mathcal A_{\rm cov}=2\sqrt{\det\Sigma}.
$$

Uniform phase yields $\operatorname{Var}x=R^2/2$,
$\operatorname{Var}p_x=P^2/2$ and $\operatorname{Cov}(x,p_x)=0$.
Thus $\mathcal A_{\rm cov}=RP=\ell$, with units of action.
The factor two is chosen for this uniform orbit: the projected ellipse
encloses area $\pi RP$, half the full planar canonical orbit integral.

For a linear canonical change $Z'=SZ+b$, $\Sigma'=S\Sigma S^T$ and
$\det S=1$, hence $\mathcal A_{\rm cov}$ is unchanged. This invariance is
for the selected canonical plane and affine symplectic maps; arbitrary
nonlinear canonical transformations need a different argument.
The determinant is the familiar rms-emittance construction; B29 audits that
literature connection and the normalization.

On this fixed circular family the projected evolution itself is linear:

$$
S_t=\begin{pmatrix}
\cos\omega t & (R/P)\sin\omega t\\
-(P/R)\sin\omega t & \cos\omega t
\end{pmatrix},\qquad \det S_t=1.
$$

It preserves the determinant even for a nonuniform initial phase law. A
point-phase preparation has determinant zero despite orbital action $\ell>0$.
Uniform phase is sufficient for the equality with $\ell$; other phase laws
with the same first and second moments also give equality. The point-phase
example shows the dependence on preparation.
Hamiltonian phase rotation preserves the prepared estimator instead of
attracting all preparations to a common value.

## 4. Selection consequence and next test

For the uniform singular-Kepler circular family,
$\inf\mathcal A_{\rm cov}=k/c$ by C052. For a fixed softened core it is zero
by C053. The covariance estimator transfers the known admissibility threshold
to an operational ensemble quantity, keeping its singular-core and preparation
premises visible. It gives a constant-in-time classical action observable;
the remaining selection problem is a physical mechanism fixing its value and
its preparation across systems.

A16 should test scale-changing transformations of this canonical estimator,
including their effect on the external coupling and preparation. A future
receiver extension of A15 would need two separated time scales before an
intermediate-window plateau is proposed. The [B29 audit](../references/batches/B29.md)
and coordinator review complete this single-orbit test.
