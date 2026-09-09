# B31 source companion: fixed-force small circles

Coordinator verified metadata and the readable mathematical HTML of
[v1, Sections II–III](https://arxiv.org/html/physics/0407049v1), specifically
Eqs. (2), (23)–(25). Source line numbers below are worker-view locations,
not stable anchors. With signed source force $F=-f$ and $\alpha_0=1/\gamma$,
its stability sign agrees with the note's directly differentiated radial
energy. No PDF formula was transcribed or new source original archived.

## Audit result

The bounded audit supports the note's relativistic circular-orbit and radial-
stability setup, but does not directly match the proposed globally bounded
smooth confining potential or its zero-infimum conclusion. The source read is
one primary research article, in two named HTML sections only:

- J. M. Aguirregabiria, A. Hernández and M. Rivas, “Circular Orbits under
  Central Forces in Special Relativity,” arXiv:physics/0407049,
  https://arxiv.org/abs/physics/0407049. Section II, “Circular orbits and
  angular momentum,” lines 14–32, gives the relativistic balance equation
  (F(r_0)=-m\gamma v^2/r_0), and its equivalent velocity/angular-momentum
  formulas (Eqs. (2)–(5)); it explicitly states one circular orbit for each
  radius with attractive force. Section III, “Stability of circular orbits,”
  lines 83–120, linearizes (r=r_0+\epsilon), obtains
  \(\ddot\epsilon+\Lambda\epsilon=0\), and gives the force-derivative
  criterion (Eqs. (21)–(25)). Evidence level: passage.

Search coverage was limited to two discovery queries (relativistic circular
force balance; relativistic effective-potential stability). Search results were
leads only. No exhaustive prior-art claim is made; novelty is unassessed.

## Relation to the note

The article's Eq. (2) implies (P v/R=f(R)) with (P=m\gamma v). Writing
\(s=Rf(R)\), this is
\[
mc^2(\gamma-\gamma^{-1})=s,
\qquad
\gamma=\frac{s/(mc^2)+\sqrt{(s/(mc^2))^2+4}}2,
\]
so the note's gamma formula is an elementary algebraic consequence of the
source balance law. Consequently (v=c\sqrt{1-\gamma^{-2}}) and
\(\ell=RP\) are also correctly normalized in action units.

For the note's fixed-ℓ radial energy,
\[
U_\ell(r)=\sqrt{m^2c^4+c^2\ell^2/r^2}+V(r),
\]
direct differentiation gives at a circular solution
\[
U_\ell''(R)=f'(R)+(3-v_R^2/c^2)f(R)/R.
\]
For (f(R)=KR(1+R^2/b^2)^{-1/2}), both terms are positive, since
\(f'(R)=K(1+R^2/b^2)^{-3/2}>0). This is a written elementary consequence,
not a formula directly stated in the source. It agrees with the source's
linear stability method after converting its signed force (F=-f).

The small-radius estimates are likewise derived consequences:
\(f(R)=KR+O(R^3)), (s=KR^2+O(R^4)),
\(v_R=\sqrt{K/m}\,R+O(R^3)), and
\(\ell_R=\sqrt{mK}\,R^2+O(R^4)). Thus the fixed Hamiltonian has positive
actions with infimum zero, despite a global force ceiling. The source does
not address this confining potential, force-ceiling class, or preparation
quantifiers.

The conditional lower bound is valid independently: from balance,
\(\ell=P^2v/f\), and (f\le F_{\max}). Since
\(P^2v=m^2v^3/(1-v^2/c^2)) increases for (0<v<c), a separately imposed
floor (v\ge v_*>0) yields
\[
\ell\ge \frac{m^2v_*^3}{F_{\max}(1-v_*^2/c^2)}>0.
\]
This is a conditional bound, not a universal action calibration.

## Proof issues to preserve

“Stable” means a strict radial minimum / linear oscillatory stability at fixed
angular momentum, not asymptotic attraction. The zero-infimum family approaches
the central equilibrium and remains nonstationary for every (R>0). A speed
floor is an independent excitation premise; positivity of energy alone does not
exclude arbitrarily small circles. The external potential supplies no mediator
or physical mechanism selecting that floor.
