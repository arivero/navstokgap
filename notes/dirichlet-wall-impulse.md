# Quantum wall dynamics: boundary choice, reflected packets and impulse

**Result, 2026-10-27.** For the specified incident Gaussian and free Dirichlet
half-line dynamics below, the nonnegative
boundary-force measures converge weakly on the whole time axis:
$$
 \frac{\hbar^2}{2m}\,|\partial_q\psi_{\hbar,D}(0,t)|^2\,dt
 \;\Longrightarrow\;2|p_0|\,\delta_{t_*},
 \qquad t_*=-\frac{mq_0}{p_0}>0.\tag{1}
$$
This includes the impact layer excluded from a uniform off-impact
momentum-current estimate. In fact, on the $\sqrt\hbar$ time scale the
force has an explicit Gaussian profile and the momentum current tends
to an error-function transition.

For the corresponding **Neumann** half-line packet, the derivative in
(1) vanishes identically. The complete boundary stress has another
term; it has the same limiting impulse and the same leading
impact-layer profile. The particle's classical bounce therefore does
not determine whether the quantum wave satisfies Dirichlet or Neumann
boundary conditions. General Robin conditions are discussed through
their scattering phases; no wavepacket limit is claimed here for
arbitrary Robin parameters.

The boundary contribution to Ehrenfest's theorem is established
literature: see [De Vincenzo (2013)](https://www.scielo.org.mx/scielo.php?pid=S1870-35422013000200001&script=sci_arttext),
equations (38)--(39) for a wall on the opposite half-line (passage
read), and [Albrecht et al. (2023)](https://arxiv.org/abs/2206.07531)
(abstract) on boundary momentum and bouncing packets. A particularly
close precedent is [Belloni--Doncheski--Robinett (2004)](https://arxiv.org/pdf/quant-ph/0408182),
equations (8)--(11), (16)--(19): they normalize the same odd-image
Gaussian on the opposite half-line and analyze its near-collision
position and force (relevant passages read). The computation below
gives a particular weak impulse measure and compares the Neumann stress;
it does not claim priority for the reflected Gaussian or wall forces.

## Classical impact and quantum boundary data

Take the half-line $q\ge0$ and a free particle starting at $q_0>0$ with
$p_0<0$. For an ideal **elastic** wall, the prescribed impact law is
$p(t_*+)=-p(t_* -)$ at $t_*=-mq_0/p_0$. The motion is
$$q(t)=|q_0+p_0t/m|,\qquad
 p(t)=p_0\operatorname{sgn}(q_0+p_0t/m)\quad(t\ne t_*).$$
Position is continuous; momentum has a jump. A smooth-force equation with a finite
smooth force does not describe that jump. Nonpenetration alone does not
select the elastic law: a restitution coefficient or another contact
rule would be additional data.

For a smooth wall in several dimensions, the elastic specular rule
reverses the normal component and retains the tangential component:
$v_+=v_--2(v_-\cdot n)n$. This requires a specified unit normal and a
well-defined collision. Corners, grazing contacts and an accumulation
of impacts require separate analysis; one should not infer their
uniqueness merely from the local smooth-force theorem.

A mathematically defined quantum impenetrable wall can be represented by
the Dirichlet Laplacian
$$H_{\hbar,D}=-\frac{\hbar^2}{2m}\frac{d^2}{dq^2},
\qquad D(H_{\hbar,D})=H^2(0,\infty)\cap H^1_0(0,\infty).$$
It is self-adjoint and gives a unitary group. Its Euclidean kernel is
$$
 K_D(T;x,y)=k_{\hbar,T}(x-y)-k_{\hbar,T}(x+y),
 \quad
 k_{\hbar,T}(r)=\sqrt{\frac m{2\pi\hbar T}}
             e^{-mr^2/(2\hbar T)},\quad x,y>0.
$$
This is the method of images: the Euclidean reference process is
Brownian motion killed at the boundary. The quantum real-time wall
reflects, but killed Euclidean paths should not themselves be read as
real-time bouncing trajectories. The reflected-packet estimate below proves a quantitative
coherent-packet position limit through the bounce.

A subtle domain issue is important: the symmetric differential operator
$-i\hbar\,d/dq$ on the half-line with Dirichlet boundary has unequal
deficiency indices and no self-adjoint extension on $L^2(0,\infty)$.
The Dirichlet Hamiltonian is nevertheless self-adjoint. A current or a
quadratic-form expectation involving $-i\hbar d/dq$ can be studied, but
it should not be presented as the expectation of a self-adjoint
half-line momentum operator. See
[Al-Hashimi and Wiese, arXiv:2103.01715](https://arxiv.org/abs/2103.01715)
(abstract) for the boundary momentum problem.

## 1. The packet and its boundary value

Fix $m,\omega,q_0>0$ and $p_0<0$, with $v=p_0/m$. On the full line
take the normalized coherent state
$$
 g_{\hbar,0}(q)=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}
  \exp\!\left[-\frac{m\omega(q-q_0)^2}{2\hbar}
       +\frac{i p_0(q-q_0)}{\hbar}\right].
$$
Let $g_{\hbar,t}=e^{-itP^2/(2m\hbar)}g_{\hbar,0}$,
$a(t)=q_0+vt$, $A(t)=1+\omega^2t^2$, and
$$
 \gamma_\hbar=\langle g_{\hbar,0},Rg_{\hbar,0}\rangle
 =\exp\!\left[-\frac{m\omega q_0^2+p_0^2/(m\omega)}{\hbar}\right],
 \qquad (Rg)(q)=g(-q).\tag{2}
$$
The odd and even extensions restrict to the normalized half-line states
$$
 \psi_{\hbar,D}(q,t)
   =\frac{g_{\hbar,t}(q)-g_{\hbar,t}(-q)}{\sqrt{1-\gamma_\hbar}},
 \qquad
 \psi_{\hbar,N}(q,t)
   =\frac{g_{\hbar,t}(q)+g_{\hbar,t}(-q)}{\sqrt{1+\gamma_\hbar}},
 \quad q>0.\tag{3}
$$
They solve the free Schrödinger equation with Dirichlet and Neumann
conditions, respectively. Their regularity and decay justify the
boundary calculations below.

The free Gaussian formula gives
$$
 |g_{\hbar,t}(0)|^2
 =\sqrt{\frac{m\omega}{\pi\hbar A(t)}}
    \exp\!\left[-\frac{m\omega a(t)^2}{\hbar A(t)}\right],\qquad
 \hbar\,\frac{g'_{\hbar,t}(0)}{g_{\hbar,t}(0)}
 =D(t):=\frac{m\omega q_0+i p_0}{1+i\omega t}.\tag{4}
$$
The simplification in $D$ follows from $a=q_0+p_0t/m$; $g_{\hbar,t}(0)$
is never zero. Define $B=(m\omega q_0)^2+p_0^2$.
Since $\psi'_{\hbar,D}(0,t)=2g'_{\hbar,t}(0)/\sqrt{1-\gamma_\hbar}$,
the boundary-force density is exactly
$$
 F_{\hbar,D}(t)
 =\frac{2B}{m(1-\gamma_\hbar)A(t)}
    \sqrt{\frac{m\omega}{\pi\hbar A(t)}}
    \exp\!\left[-\frac{m\omega a(t)^2}{\hbar A(t)}\right].\tag{5}
$$

### Position through impact and current away from impact

Write $a(t)=q_0+p_0t/m$, and let $g_{\hbar,t}$ be the freely evolved
Gaussian. Its position variance is
$$\sigma_q(t)^2=\frac{\hbar}{2m\omega}(1+\omega^2t^2).\tag{P21}$$
Because $||x|-|a||\le|x-a|$ and reflection commutes with the free
evolution,
$$
 \left|\langle Q\rangle_{\psi_\hbar(t)}-|a(t)|\right|
 \le\sqrt{\frac{2}{1-\gamma_\hbar}}\,\sigma_q(t).\tag{P22}
$$
Indeed the half-line position expectation equals the full-line
expectation of $|X|$ in the normalized full-line odd state $\phi_\hbar=(g_\hbar-Rg_\hbar)/\sqrt{2(1-\gamma_\hbar)}$; apply the triangle inequality
to the two Gaussian terms. Thus position converges uniformly on every
bounded time interval, **including the impact time**, to the elastic
classical folded trajectory.

Away from the impact, the corresponding probability-current momentum
also converges to the incoming or reflected value. More precisely, if
$|a(t)|\ge\eta>0$, with
$\sigma_p=\sqrt{\hbar m\omega/2}$,
$$
 \left|\int_0^\infty\overline{\psi_\hbar}
             (-i\hbar\partial_q)\psi_\hbar\,dq
       -p_0\operatorname{sgn}a(t)\right|
 \le\sqrt{\frac2{1-\gamma_\hbar}}
      \left(\sigma_p+\frac{2|p_0|\sigma_q(t)}{\eta}\right).\tag{P23}
$$
For the proof, the half-line integral is the full-line expectation of
$\operatorname{sgn}(X)P$ in the normalized full-line odd state $\phi_\hbar=(g_\hbar-Rg_\hbar)/\sqrt{2(1-\gamma_\hbar)}$. On the Gaussian,
$\|(\operatorname{sgn}X\,P-\operatorname{sgn}a\,p_0)g_t\|$ is at most
$\sigma_p+2|p_0|\mathbb P(aX<0)^{1/2}$; Chebyshev bounds the last
probability by $\sigma_q(t)^2/a(t)^2$. The reflected Gaussian obeys
the same estimate. For each fixed $T,\eta>0$ independent of $\hbar$,
(P23) proves uniform convergence over $|t|\le T$ with $|a(t)|\ge\eta$.
It gives no uniform bound in an $\hbar$-dependent impact layer
$|a(t)|\sim\sqrt\hbar$ or momentum value at $t_*$. The expression in
(P23) is a real current form on this domain, not an expectation of a
self-adjoint half-line momentum.

Position converges uniformly through impact; current cannot converge uniformly to a discontinuous momentum jump. The next calculation resolves that layer in the weak measure topology.

## 2. The pulse and the limiting impulse

Put $A_*=A(t_*)$ and
$$\Lambda=|v|\sqrt{\frac{m\omega}{A_*}}>0.\tag{6}$$
Because $m\omega q_0=-p_0\omega t_*$, one has $B=p_0^2A_*$.
At every fixed $s\in\mathbb R$, (5) gives
$$
 \sqrt\hbar\,F_{\hbar,D}(t_*+\sqrt\hbar\,s)
 \longrightarrow
 \frac{2p_0^2}{m}\sqrt{\frac{m\omega}{\pi A_*}}\,
          e^{-\Lambda^2s^2}.\tag{7}
$$
The integral of the right side is $2|p_0|$.

This pointwise calculation proves (1) with the following tail control.
For any fixed $\delta>0$,
$$
 c_\delta:=\inf_{|t-t_*|\ge\delta}\frac{m\omega a(t)^2}{A(t)}>0:
$$
the expression is continuous, has only the one zero $t_*$, and tends
to $mv^2/\omega>0$ at both infinities. Equation (5) bounds the total
force outside this neighbourhood by
$C_\delta\hbar^{-1/2}e^{-c_\delta/\hbar}$, since $A(t)^{-3/2}$ is
integrable. Inside the neighbourhood, after $t=t_*+\sqrt\hbar s$,
the profiles have a common integrable Gaussian majorant. Dominated
convergence proves convergence against every bounded continuous test
function and gives the total mass $2|p_0|$. This is weak convergence
of measures, not total-variation convergence to an atom.

The real current-momentum form is
$$J_\hbar(t)=\hbar\operatorname{Im}
 \int_0^\infty\overline{\psi_\hbar}\,\partial_q\psi_\hbar\,dq.\tag{8}$$
The differential operator $-i\hbar\partial_q$ on a half-line is not a
self-adjoint momentum operator; (8) is a real current form. For a
sufficiently regular free half-line wave,
$$
 \frac{dJ_\hbar}{dt}
 =\frac{\hbar^2}{2m}\left(
     |\psi_\hbar'(0,t)|^2
    -\operatorname{Re}[\overline{\psi_\hbar(0,t)}
                                  \psi_\hbar''(0,t)]\right).\tag{9}
$$
To see this, differentiate (8), insert
$\partial_t\psi=i\hbar\psi''/(2m)$, and integrate by parts. For
Dirichlet the second term vanishes, so $dJ_{\hbar,D}/dt=F_{\hbar,D}$.
Using the off-impact current estimate above together with (7),
$$
 J_{\hbar,D}(t_*+\sqrt\hbar\,s)
 \longrightarrow |p_0|\,\operatorname{erf}(\Lambda s).\tag{10}
$$
The incoming value is $p_0=-|p_0|$, the outgoing value is $|p_0|$,
and their difference is the mass in (1). The transition is continuous
for each $\hbar>0$ and becomes discontinuous only in the limit.

## 3. Neumann and Robin boundary information

For $\psi_{\hbar,N}'(0,t)=0$, the expression in (1) is identically
zero. Equation (9), rather than the Dirichlet-only term, is the
appropriate boundary stress. Since
$$
 \frac{g_{\hbar,t}''(0)}{g_{\hbar,t}(0)}
 =\frac{D(t)^2}{\hbar^2}
   -\frac{m\omega}{\hbar(1+i\omega t)},
$$
it is explicitly
$$
 F_{\hbar,N}(t)=\frac{2|g_{\hbar,t}(0)|^2}{m(1+\gamma_\hbar)}
 \left[-\operatorname{Re}D(t)^2+\frac{\hbar m\omega}{A(t)}\right].
 \tag{11}
$$
This density need not be pointwise nonnegative. At the impact,
$D(t_*)=ip_0$, and therefore the rescaled Neumann density has the
same limit (7). Moreover
$$
 |F_{\hbar,N}(t)|
 \le\frac{2|g_{\hbar,t}(0)|^2}{m(1+\gamma_\hbar)}
      \left[\frac{B}{A(t)}+\frac{\hbar m\omega}{A(t)}\right],
$$
so the same argument after (7) controls the total variation outside
every impact neighbourhood. Consequently the finite signed measures
$F_{\hbar,N}(t)dt$ converge weakly to the same
$2|p_0|\delta_{t_*}$. Their impact-layer current has the same limit
as (10). The even-reflection argument also gives the same folded
classical position $|a(t)|$. Thus the limiting position and impulse
do not recover the Dirichlet/Neumann reflection phase.

All self-adjoint realizations of the free half-line Laplacian use
Dirichlet or a real Robin condition
$\psi'(0)=\kappa\psi(0)$, including Neumann at $\kappa=0$. For an
incoming stationary wave $e^{-ikq}+r_\kappa(k)e^{ikq}$,
$$
 r_\kappa(k)=\frac{ik+\kappa}{ik-\kappa},\qquad
 |r_\kappa(k)|=1,\quad
 r_0=1,\quad r_D=-1.\tag{12}
$$
At fixed real $\kappa$ and fixed nonzero physical momentum,
$k=|p|/\hbar\to\infty$ and $r_\kappa(k)\to1$. This is a stationary
scattering comparison, not a proof of the impulse limit for every
Robin packet. For $\kappa<0$ there is additionally a bound state
$\sqrt{-2\kappa}e^{\kappa q}$ of energy
$-\hbar^2\kappa^2/(2m)$, showing another quantum distinction that the
free incoming bounce does not encode.

## 4. Consequence for STATE

For a specified coherent packet, the Dirichlet force is a positive
boundary measure converging to Newton's impulsive momentum jump; the
full Neumann boundary stress has the same limit. A classical bounce
does not identify the boundary condition or reflection phase. This
constructs neither a general boundary-groupoid theorem nor a
positive-action-necessity result.
