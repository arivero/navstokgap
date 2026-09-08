# Exact midpoint crossover for a finite-speed return bridge

The velocity-resolved return bridge has an explicit midpoint variance:

$$\frac{\kappa_{\rm mid}(T)}{H_*}=g(z)=zR(z)[1-R(z)],\qquad
R(z)=\frac{\int_0^z I_0(s)\,ds}{zI_0(z)},\qquad z=\lambda T.$$

It has cubic onset $g(z)=z^3/6+O(z^5)$ and converges to one as $z\to\infty$.
Thus the conditioned observable reaches the same long-window plateau as the
stationary increment observable, through a different crossover function.

## 1. Preparation and units

Fix $m>0$, $0<u<c$, $\lambda>0$ and $T>0$. Use the C033 bridge from
$(X_0,V_0)=(0,+u)$ to $(X_T,V_T)=(0,-u)$, with its explicit density
disintegration and right-continuous velocity convention. Put
$Y=X_{T/2}$, $Q=2Y/(uT)$ and $N_T=2K+1$. Its count weights are

$$w_k=\frac{(z/2)^{2k}}{(k!)^2I_0(z)},\qquad k=0,1,\ldots.$$

Here $I_0(z)=\sum_{k\ge0}(z/2)^{2k}/(k!)^2$.
The action-valued observables are
$\kappa_{\rm mid}=4m\operatorname{Var}(Y)/T$ and
$A_2=2m\mathbb E[Y^2]/T$, while $H_*=mu^2/\lambda$ is the C020
stationary long-window plateau. All expectations below use this bridge;
cut refinement keeps this preparation fixed and does not vary $T$.

## 2. A beta law at fixed switch count

For $k=0$, $Q=1$ deterministically. For every integer $k\ge1$,

$$\boxed{\frac{Q+1}{2}\,\bigg|\,K=k\ \sim\operatorname{Beta}(k+1,k).}$$

Equivalently its density on $-1<q<1$ is

$$f_k(q)=\frac{(2k-1)!}{2^{2k-1}[(k-1)!]^2}
                  (1+q)(1-q^2)^{k-1}.$$

**Proof.** For a telegraph segment of duration $t$, displacement $x$ and
initial velocity $+u$, let $a=(t+x/u)/2$, $b=(t-x/u)/2$. Uniform Poisson
spacings, grouped into positive and negative durations, give joint
position/count densities in the interior $|x|<ut$:

$$d_{2j+1}(x,t)=\frac{e^{-\lambda t}\lambda^{2j+1}}{2u(j!)^2}a^jb^j
\quad(j\ge0),$$
$$d_{2j}(x,t)=\frac{e^{-\lambda t}\lambda^{2j}}{2u\,j!(j-1)!}a^jb^{j-1}
\quad(j\ge1).$$

The zero-count law is an atom at $ut$, handled separately. For initial
velocity $-u$, reverse the displacement sign. These formulas follow from
Dirichlet spacings with respectively $(j+1,j+1)$ and $(j+1,j)$ groups;
the position Jacobian is $1/(2u)$.

Split the return path at $t=T/2$ and take an interior midpoint $y$.
The two possible midpoint velocity sectors have even/odd and odd/even
counts. With $a=T(1+q)/4$, $b=T(1-q)/4$, each sector contributes
$a^kb^{k-1}$ times a factorial sum. Their combined joint density in
midpoint $y$ and terminal position zero is

$$\frac{e^{-\lambda T}\lambda^{2k+1}}{2u^2}a^kb^{k-1}S_k,
\qquad S_k=\sum_{j=1}^k\frac1{j!(j-1)![(k-j)!]^2}
             =\frac{k(2k)!}{2(k!)^4}.$$

For the last equality write each term as
$j\binom{k}{j}^2/(k!)^2$, use symmetry $j\leftrightarrow k-j$ and
Vandermonde's identity $\sum_j\binom{k}{j}^2=\binom{2k}{k}$.
Divide by C033's terminal position/count density
$e^{-\lambda T}\lambda^{2k+1}(T/2)^{2k}/[2u(k!)^2]$ and multiply by
$dy/dq=uT/2$. This yields $f_k$. It integrates to one, so at $k\ge1$
the interior formula exhausts the conditional mass. At $k=0$ retain the
deterministic midpoint atom; its mixture mass is $1/I_0(z)$.

## 3. Exact moments and limits

Beta integration gives, also including the $k=0$ atom,

$$\mathbb E[Q\mid K=k]=\mathbb E[Q^2\mid K=k]=\frac1{2k+1}.$$

Summing the absolutely convergent series and integrating $I_0$ term by term
therefore gives $\mathbb E Q=\mathbb E Q^2=R(z)$. Consequently

$$\mathbb E Y=\frac{uT}{2}R(z),\qquad
\operatorname{Var}(Y)=\frac{u^2T^2}{4}R(z)[1-R(z)],$$
$$\kappa_{\rm mid}=H_*g(z),\qquad A_2=\frac{H_*}{2}zR(z).$$

For $z>0$, $0<R(z)<1$, hence $g(z)>0$. The exact identity also improves
the generic midpoint bound to $g(z)\le z/4$. The Taylor series gives
$R(z)=1-z^2/6+O(z^4)$ and thus the cubic onset in the opening result.

For the large-window limit use the integral representation
$I_0(z)=\pi^{-1}\int_0^\pi e^{z\cos\theta}d\theta$,
[DLMF 10.32.1](https://dlmf.nist.gov/10.32.E1).
The normalized exponential weight concentrates at $\theta=0$: for any
$0<\delta<\pi$, the weight of $[\delta,\pi]$ is at most
$(2\pi/\delta)e^{-z(\cos(\delta/2)-\cos\delta)}$.
Differentiation under the integral then gives $I_0'(z)/I_0(z)\to1$.
Both $I_0(z)$ and $\int_0^zI_0(s)ds$ diverge, so l'Hopital's rule yields

$$zR(z)=\frac{\int_0^zI_0(s)ds}{I_0(z)}\longrightarrow1,
\qquad R(z)\longrightarrow0,\qquad g(z)\longrightarrow1.$$

At fixed $m,u,\lambda$, this proves

$$\kappa_{\rm mid}(T)\to H_*,\qquad A_2(T)\to H_*/2,
\qquad \mathbb E Y\to\frac{u}{2\lambda}\quad(T\to\infty).$$

The normalized mean $\mathbb E Q$ vanishes; the unscaled midpoint mean
retains a boundary bias. P02's sampler anticipated the plateau and cubic
onset. This proof supplies the full curve and corrects its provisional
statement that the unscaled midpoint mean tends to zero. Monotonicity of
$g$ is a separate question; the endpoint limits do not assume it.

## 4. Crossover windows and mass universality

For either C018's increment coefficient or C031's return-midpoint coefficient,
a prescribed value $K_*>0$ under a speed ceiling $u$ can be realized only if

$$T\ge T_*:=\frac{K_*}{mu^2}.$$

This follows by dividing $K_*\le mu^2T$ by the positive factor $mu^2$.
For the present bridge the sharper $g\le z/4$ gives
$\kappa_{\rm mid}\le mu^2T/4$. These are necessary bounds on the
observable, not sufficient conditions for any prescribed distribution.

A consequence for C035 is immediate. Suppose masses extend arbitrarily close
to zero, the speed ceiling $u$ and finite window $T$ are common, and the
increment or midpoint coefficient is the same $K_*\ge0$ for every mass.
Then $K_*\le mu^2T$ for all those masses forces $K_*=0$.
A positive mass-universal plateau is compatible with finite speed through
mass-dependent crossover windows, rather than a common finite window valid
for arbitrarily small masses.

For a telegraph family with shared plateau $H_*$ and common speed $u$,
$\lambda_m=mu^2/H_*$ and $T_{*,m}=1/\lambda_m$ when $K_*=H_*$.
The exact midpoint curve is $H_*g(mu^2T/H_*)$. Its dependence on $mT$
exhibits the nonuniformity of the large-window limit across small masses.
The stationary increment instead uses
$H_*[1-(1-e^{-2\lambda_mT})/(2\lambda_mT)]$.

At the additional formal identifications $H_*=\hbar$ and $u=c$, the scales
are $T_{*,m}=\hbar/(mc^2)$ and $uT_{*,m}=\hbar/(mc)$, the reduced
Compton time and length. The bounded-speed inequalities extend to $u=c$;
the identification with a quantum phase scale belongs to the next dynamics
test. This calculation concerns classical probability and specified windows.

## 5. Research handoff

A09a supplies the exact conditioned crossover and the common-window test.
A09b retains the direct checkerboard source reading, complex-amplitude
recurrence and quantum normalization. B17 records the per-result source audit;
Cinque's occupation-time formulas provide the telegraph source chain, while
the beta midpoint specialization and action normalization are derived here.
The existing C033 path law remains unchanged. Keep physical time, observation
duration and the cut mesh separate when applying these results to the target.
