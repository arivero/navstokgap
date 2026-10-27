# A wall impulse from a quantum boundary stress

**Result, 2026-10-27.** For the incident Gaussian and the free Dirichlet
half-line dynamics of the
[Newton--Dimock guide](newton-dimock-balaban-guide.md), the nonnegative
boundary-force measures converge weakly on the whole time axis:
$$
 \frac{\hbar^2}{2m}\,|\partial_q\psi_{\hbar,D}(0,t)|^2\,dt
 \;\Longrightarrow\;2|p_0|\,\delta_{t_*},
 \qquad t_*=-\frac{mq_0}{p_0}>0.\tag{1}
$$
This includes the impact layer omitted from the guide's off-impact
momentum-current bound. In fact, on the $\sqrt\hbar$ time scale the
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
Using the off-impact current limit from the guide together with (7),
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
