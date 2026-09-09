# Fixed force ceiling: small bound circles and an excitation floor

One fixed smooth confining potential with a globally bounded force admits
stable circular orbits with positive angular actions tending to zero.
A lower bound on circular speed, together with the force ceiling, instead
gives a positive action bound. This identifies the missing excitation premise
in A16's fixed-force follow-up. A17, C058–C059; written proof and B31 review.

## 1. Fixed Hamiltonian and exact circles

Fix $m,c,K,b>0$ and use Cartesian configuration space $\mathbb R^2$ with

$$
H(q,p)=\sqrt{m^2c^4+c^2|p|^2}+V(|q|),\qquad
V(r)=Kb^2\left(\sqrt{1+r^2/b^2}-1\right).
$$

The potential is smooth even at the origin, tends to infinity, and has
inward force magnitude
$f(r)=Kr/\sqrt{1+r^2/b^2}<Kb$. Thus $Kb\le F_{\max}$ gives a prescribed
global force ceiling without changing the potential across the orbit family.
Finite energy bounds both position and momentum, giving complete trajectories.
Particle velocities are strictly below $c$; this external-potential model
specifies no propagating mediator.

For each radius $R>0$, set $s=Rf(R)$ and

$$
\gamma_R=\frac{s/(mc^2)+\sqrt{[s/(mc^2)]^2+4}}2,
\quad v_R=c\sqrt{1-\gamma_R^{-2}},\quad
P_R=m\gamma_Rv_R,\quad \ell_R=RP_R.
$$

Circular force balance is $P_Rv_R/R=f(R)$, equivalent to
$mc^2(\gamma_R-\gamma_R^{-1})=s$. The positive solution above therefore
gives an exact complete circle with $\omega_R=v_R/R$.
The normalized canonical orbit integral is $\ell_R$ in action units.
Uniform circular phase gives A15's $\mathcal A_{\rm cov}=\ell_R$.

At fixed $\ell=\ell_R$, the radial effective energy is
$U_\ell(r)=\sqrt{m^2c^4+c^2\ell^2/r^2}+V(r)$.
Differentiation at the circle gives

$$
U_\ell''(R)=f'(R)+(3-v_R^2/c^2)\frac{f(R)}R>0.
$$

Indeed the kinetic contribution is
$P_R^2/(m\gamma_R^3R^2)+2P_Rv_R/R^2$; use force balance and
$\gamma_R^{-2}=1-v_R^2/c^2$. Here
$f'(R)=K(1+R^2/b^2)^{-3/2}>0$.
The circle is a strict radial minimum and is stable against sufficiently small
radial perturbations at fixed angular momentum. This is the stability notion
used here, rather than asymptotic attraction of the Hamiltonian flow.

## 2. The small-orbit limit keeps every upper ceiling

As $R\downarrow0$ at fixed $m,c,K,b$,

$$
s=KR^2+O(R^4),\quad
v_R\sim\sqrt{K/m}\,R,\quad
\ell_R\sim\sqrt{mK}\,R^2,\quad
\omega_R\longrightarrow\sqrt{K/m}.
$$

These follow by expanding $\gamma_R=1+s/(2mc^2)+O(s^2)$.
Kinetic energy above rest is $mc^2(\gamma_R-1)\sim KR^2/2$ and
$V(R)\sim KR^2/2$, hence $H-mc^2\sim KR^2$.
Force and coordinate acceleration satisfy
$f(R)\sim KR$ and $v_R^2/R\sim KR/m$, both tending to zero.
Any strictly positive prescribed speed and acceleration upper bounds hold
on all sufficiently small members, alongside the global force ceiling.
The period tends to $2\pi\sqrt{m/K}$: rapid cycling is unnecessary.

Every circle is nonstationary, regular and bound, with positive energy above
the minimum and positive covariance action. Their infimum is nevertheless
zero in this single fixed Hamiltonian. The limiting state is its smooth
central equilibrium. Quantitative excitation restrictions, rather than merely
positivity of excitation, would exclude this family.

## 3. A positive conditional bound

For any relativistic circular orbit under inward force $0<f(R)\le F_{\max}$,
force balance gives the exact identity

$$
\ell=RP=\frac{P^2v}{f(R)}.
$$

If an independently specified speed floor $v\ge v_*>0$, $v_*<c$, is imposed,
then the increasing function $m^2v^3/(1-v^2/c^2)$ yields

$$
\ell\ge\frac{m^2v_*^3}{F_{\max}(1-v_*^2/c^2)}>0.
$$

The dimensions are action. This is a lower bound on circular orbital action,
and on A15's estimator under uniform phase. The speed floor is a lower kinetic
excitation premise; the ceiling alone gives Section 2's zero-infimum family.
The bound is parameter-dependent and does not establish a universal value or
physical-time attraction. For Newtonian circular motion the same calculation
uses $P=mv$ and gives $m^2v_*^3/F_{\max}$.

## 4. Next selection question

A18 should test the positive bound beyond circles, using total turning of
a closed regular trajectory and the force ceiling. Its source audit should
check the relevant total-curvature theorem before importing it.

The useful positive mechanism combines an upper force scale with a lower
excitation scale. The next task should identify a physical source for persistent
excitation in a closed mechanical model, with its energy allocation and any
attraction claim explicit. Reuse A07's prescribed-endpoint turn cost and A02's
prepared reservoir as comparison mechanisms. Another arbitrary upper ceiling
would leave the small-circle family intact.
