# Proof review and promotion decision for G07/G08

2026-09-16. Coordinator (Claude Fable 5.1) written review at the user's
direction to decide promotion on merits. Sequential, no subagents, no
numerical verification. Literature status uses [B78](../references/batches/B78.md)
and [B79](../references/batches/B79.md).

## Decision

Promoted: C131 (floor/unit theorem for any observable), C132 (gap and
action unit are dimensionally equivalent for a dimensionful classical
coupling and inequivalent at $d=4$), C133 (Yang--Mills quantum-mechanical
gap with explicit constants, scaling and gapless limits). Each is an
elementary or established result whose proof is complete in the notes and
whose literature match is exact; the project-specific content is the
explicit constants, the hypotheses and the classification, and no novelty
is asserted.

Kept exploratory: G07 Propositions 7, 11, 12, 13 (finite-volume origin,
two-dimensional circle, delta and inverse-square potentials), whose
sources were read at abstract or metadata level and whose derivations are
standard but were not independently re-derived here; G07 Section 7.3 and
G08 Remarks 3--4, which are a labelled conjecture and semiclassical
estimates; G08 Theorem 2, whose content is one inequality and whose value
is interpretive (it is cited inside C133's evidence rather than promoted).

## 1. Theorem 1 of G07 (C131)

Hypotheses: dimensional homogeneity of the relations defining the attained
set, and universality (the floor is a function of the fixed constants
alone). The proof is the unit-change argument: with
$\gamma(\lambda^{d_1}c_1,\dots)=\lambda^{d_X}\gamma(c)$, a $\lambda$ fixing
all $c_i$ but not the unit of $X$ exists exactly when $d_X$ is outside the
span, giving $\gamma\in\{0,\infty\}$; inside the span $\gamma/\Pi$ is unit
invariant, hence a function of the dimensionless combinations. Checked
line by line; it is Buckingham's $\Pi$ theorem applied to the floor. The
universality hypothesis is a modelling assumption and is stated in the
claim. Corollary 2 (similarity forces zero) follows because the
transformation maps attained values onto all of $(0,\infty)\cdot X$.

## 2. Propositions 4 and 5 of G08 (C132)

Solved the linear systems by hand. Mechanics: $a\,d_m+b\,d_g+c\,d_E=d_A$
with $d_m=(1,0,0)$, $d_g=(\tfrac12,-1,-1)$, $d_E=(1,2,-2)$, $d_A=(1,2,-1)$:
length $-b+2c=2$, time $-b-2c=-1$ give $c=\tfrac34$, $b=-\tfrac12$; mass
$a-\tfrac14+\tfrac34=1$ gives $a=\tfrac12$. Yang--Mills $d=3$,
$d_{1/g^2}=(1,3,-1)$, $d_c=(0,1,-1)$: mass $a+c'=1$, length
$3a+b+2c'=2$, time $-a-b-2c'=-1$; length plus time gives $a=\tfrac12$,
then $c'=\tfrac12$, $b=-\tfrac12$. $d=2$, $d_{1/g^2}=(1,4,-1)$: sum gives
$3a=1$, $c'=\tfrac23$, $b=-\tfrac23$. $d=4$: mass forces $b=1$, length
forces $a=0$, time reads $-2=-1$. All entries of the table are confirmed;
the dimension of $1/g^2$ follows from $[A]=L^{-1}$ and
$S=g^{-2}\int\operatorname{tr}F^2d^dx$ of action dimension.

## 3. Theorems 5 and 6 of G07 (C133)

Oscillator bound: the completed square
$\int|\phi'+\alpha y\phi|^2=\int|\phi'|^2+\alpha^2\int y^2|\phi|^2-\alpha\int|\phi|^2$
uses $2\alpha\operatorname{Re}\int y\bar\phi\phi'=\alpha\int y\,(|\phi|^2)'=-\alpha\int|\phi|^2$,
valid on $C_0^\infty$; the bound $\sqrt{\mu\nu}$ follows with
$\alpha=\sqrt{\nu/\mu}$. With $\mu=\hbar^2/2m$, $\nu=g^2x^2/2$ this is
$\hbar g|x|/(2\sqrt m)$. Slicing by Fubini and adding the two slices gives
$2q_H\ge q_K$; the extension from the core to the form domain and the
min-max comparison $\mu_n(H)\ge\tfrac12\mu_n(K)$ are standard and are
argued in the note. Compact resolvent of $K$: the form-ball argument
(mass outside radius $R$ at most $(\gamma R)^{-1}$, Rellich--Kondrachov
inside) is complete. Simplicity of the ground state rests on the
Feynman--Kac positivity-improving argument and Reed--Simon IV XIII.44,
whose number is corroborated only through citing passages; the
statement itself is textbook and the claim records this dependence.
Dilation: $\hbar^2/(m\ell^2)=g^2\ell^4$ gives $\ell^6=\hbar^2/(mg^2)$ and
$\varepsilon=\hbar^{4/3}g^{2/3}m^{-2/3}$; the mass, length and time
exponents $(\tfrac43+\tfrac13-\tfrac23,\ \tfrac83-\tfrac23,\ -\tfrac43-\tfrac23)=(1,2,-2)$
are an energy. Limits: at $g=0$ the Fourier transform gives spectrum
$[0,\infty)$; the classical valley motion is an explicit solution.

SU(2) bookkeeping re-derived: for fixed $\vec x_i\ne0$,
$|\vec x_i\times\vec x_j|^2=|\vec x_i|^2|\vec x_{j\perp}|^2$; two
transverse oscillator directions each contribute $\hbar g|\vec x_i|/(2\sqrt m)$.
Summing the pair inequalities over ordered pairs with weight $w$ gives
$w(D-1)\sum_jT_j+2w\sum_{i<j}V_{ij}\ge w(D-1)(\hbar g/\sqrt m)\sum_i|\vec x_i|$;
with $w=1/(2(D-1))$ the remainders $(1-w(D-1))\sum T_j=\tfrac12\sum T_j$
and $(1-2w)\sum V_{ij}$, $2w=1/(D-1)\le1$, are nonnegative, so
$H\ge\tfrac12[-\frac{\hbar^2}{2m}\Delta+\frac{\hbar g}{\sqrt m}\sum_i|\vec x_i|]$.
The $SO(3)$ reduction and the invariance of the positive ground state are
correct as written. $D=1$ has no pair and is free.

Literature: Simon 1983 (passage level) contains the scalar theorem with the
same first proof and, in Corollary 4, the Lie-algebra model for at least
two matrices via Fefferman--Phong; the explicit constants, the SU(2)
convex-combination constants $c_D=\tfrac12$, $\kappa_D=1$ and the limit
statements are the project's exposition. Exact match, no novelty.

## 4. What the promoted claims do not say

C131--C133 establish no positive action floor and no Yang--Mills mass
gap. C133's gap is a finite-dimensional quantum-mechanical statement with
$\hbar$ supplied; C132 is dimensional analysis; C131 is the $\Pi$ theorem.
Their use in the programme is as gates and as the solved comparison case.
