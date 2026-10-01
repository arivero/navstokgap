# Continuous-time Kogut--Susskind expansion: corrected overlap bounds and an open explicit uniform threshold

**Correction (2026-10-02):** The former volume-uniform physical-gap claim
$\Delta_{\rm KS}\ge\frac43g^2\hbar c/a$ for $g^2\ge388$ is **withdrawn
as a conclusion of this note**. The adjacent count roots the first
plaquette at the test link and misses histories reaching that link
later. The proposed general-tree count does not bound the required
marked overlap integrals, and incorrectly excludes repeated plaquettes.
The shift measure must include every excitation interval; its endpoint
term costs up to $4n$, not $n$. The claimed true-vacuum correlation bound
was also not established. Sections 2--4 correct these steps and label
the remaining numerical estimates. The earlier identification of T2's
constant with $4(1-\theta)$, its volume-uniform limit $4$, and relative
error $O(g^{-4})$ is withdrawn here. The existing existential
strong-coupling theorem is unaffected.

Later-note scope pointer: [mass-gap-openings](mass-gap-openings.md) §1 replaces the all-coupling requirement by the weak scaling-region requirement; its §2, Opening 1 curvature comparison concerns Wilson Euclidean measures and does not repair this Hamiltonian expansion.

The results established here are the electric-history norm bound, the
corrected overlap estimate conditional on a factorizing history gas,
and a finite-volume physical-gap bound. For $SU(3)$ on a periodic cubic
spatial lattice with $N_s\ge4$, writing $P=|\mathcal P|=3N_s^3$,
$$\Delta^{\rm phys}_{a,L}\ \ge\ \left(\frac83g^2-\frac{12P}{g^2}\right)\frac{\hbar c}{a},
\qquad L=N_sa.$$
In particular $g^4\ge9P$ gives $\Delta^{\rm phys}_{a,L}\ge\frac43g^2\hbar c/a$.
This bound is extensive and supplies **no volume-uniform threshold**.
At each fixed volume the physical electric-loop gap is recovered as
$g\to\infty$. The continuous-time construction below is a candidate
route to uniformity, not a completed gap theorem. The older numerical
thresholds are retained with their corrected status in §4; no continuum
limit is taken.

## 1. The expansion and the finite-volume result

Units $\hbar c/a=1$. Work on the gauge-invariant subspace of
$L^2(SU(3)^{\mathcal E})$. Write $H=H_E-W+C$ with
$$H_E=\frac{g^2}{2}\sum_\ell(-\Delta_\ell),\qquad
W=\frac1{g^2}\sum_pw_p,\qquad
w_p=\operatorname{tr}U_p+\operatorname{tr}U_p^\dagger,\qquad C=\frac{6P}{g^2}.$$
Thus the magnetic potential is $(2/g^2)\sum_p(3-\operatorname{Re}\operatorname{tr}U_p)$.
In a Peter--Weyl basis, including matrix indices and invariant vertex
intertwiners, the electric eigenvalue is
$$E(\sigma)=\frac{g^2}{2}\sum_\ell C_2(r_\ell)
\ge\varepsilon|S(\sigma)|,\qquad \varepsilon=\frac{2g^2}{3},$$
where $S(\sigma)$ consists of nontrivial link representations and $4/3$
is the least nonzero $SU(3)$ Casimir. Also $\|w_p\|\le6$.

**Correction (2026-10-02), topology and sector:** Gauss's law excludes
a vertex incident to exactly one excited link. Nonabelian invariant
networks can branch, so describing every support as a union of flux
loops was too strong. A nonempty finite graph with minimum degree at
least two contains a cycle. For the cubic lattice with $N_s\ge4$,
its shortest cycle has four edges; hence $|S|\ge4$. Short periodic
lattices require a separate treatment: winding cycles at $N_s=2,3$
can be shorter. The four-link bound concerns the **physical sector**;
the electric gap on the unrestricted Hilbert space is $\varepsilon$.

The constant function $\Omega_0$ is the unique electric vacuum.
The plaquette character $\operatorname{tr}U_p$ is gauge invariant,
nonzero, orthogonal to $\Omega_0$, and an eigenvector with energy
$4\varepsilon$. Therefore the physical electric gap is exactly
$4\varepsilon$. Since $\|W\|\le6P/g^2$, the min--max principle bounds
the shifts of the lowest two eigenvalues of $H_E-W$ by $6P/g^2$ each.
Consequently
$$4\varepsilon-\frac{12P}{g^2}\ \le\ \Delta^{\rm phys}_{a,L}\frac{a}{\hbar c}
\ \le\ 4\varepsilon+\frac{12P}{g^2}.$$
The scalar $C$ cancels from the gap. This proves the lead's bound and
$\Delta^{\rm phys}_{a,L}/(g^2\hbar c/a)\to8/3$ at fixed $N_s$.
A nonpositive lower bound is simply uninformative. Finite-volume
compactness and positivity improvement supply the unique physical
true ground state as proved in [T1](mass-gap-obligations-lattice.md) §2
(repository proof read); this assertion alone is not uniform in volume.

After removing $C$, Duhamel's formula is
$$e^{-t(H_E-W)}=\sum_{n\ge0}\int_{0<\tau_1<\cdots<\tau_n<t}
e^{-(t-\tau_n)H_E}W e^{-(\tau_n-\tau_{n-1})H_E}\cdots W e^{-\tau_1H_E}\,d\tau_1\cdots d\tau_n.$$
**Correction (2026-10-02):** These operator summands and the resolved
history amplitudes are not asserted to be positive. The interaction
$w_p$ takes both signs; the bounds use absolute values.

Insert $1=\sum_SP_S$ between factors, where $P_S$ projects onto the
exact excited link set. These projections factor over links and commute
with gauge transformations. For a vacuum-to-vacuum history let
$S_0=S_n=\emptyset$, $x_k=\tau_{k+1}-\tau_k$ for $1\le k<n$, and
$$A(\gamma)=\sum_{k=1}^{n-1}|S_k|x_k.$$
The history amplitude satisfies
$$|w(\gamma)|\le\left(\frac6{g^2}\right)^n e^{-\varepsilon A(\gamma)}.$$
Outside the plaquette links $S_k$ cannot change, and
$\operatorname{links}(p_k)\subseteq S_{k-1}\cup S_k$: multiplication on
a trivial link produces a fundamental or antifundamental excitation.
There are at most $16$ possible next excited sets per insertion.
An irreducible history with no intervening vacuum has $|S_k|\ge4$.

The intended polymer support consists of the excited link intervals,
with insertion vertices recording which plaquette couples their ends.
Independent histories on disjoint link factors have factorizing
amplitudes; summing their chronological interleavings gives the product
of their internal ordered integrals. A complete polymer construction
must specify components and endpoint compatibility consistently with
these insertion vertices. The hard-core representation
$$Z(t)=\langle\Omega_0,e^{-t(H_E-W)}\Omega_0\rangle
=\sum_{\{\gamma_i\}\ {m compatible}}\prod_iw(\gamma_i)$$
is the proposed organization. The finite-volume bound above does not
require it. For §§2--3 assume such an organization with the history
majorant, $|S_k|\ge4$ inside each polymer, and changes only on the four
links of each insertion; the missing general count remains necessary
even under these assumptions.

## 2. The corrected convergence criterion

For an established hard-core polymer gas on a measure space, a
sufficient Kotecký--Preiss condition is
$$\int_{\gamma'\not\sim\gamma}|w(\gamma')|e^{a(\gamma')}\,d\gamma'\le a(\gamma).$$
The measure-space statement follows from Poghosyan--Ueltschi,
[§2, Assumptions 1--2 and Theorem 2.1](https://arxiv.org/pdf/0811.4281)
(passage read): hard-core interactions have stability function zero.
For finite volume and time one also needs the integrability assumption
of that theorem. Uniform local bounds, when proved, control the
corresponding rooted cluster sums. This abstract criterion does not
itself identify a Hamiltonian spectral gap.

Set
$$a(\gamma)=n(\gamma)+\lambda A(\gamma),\qquad
\delta=\varepsilon-\lambda>0,\qquad h=\frac{6e}{g^2}.$$
The tilted majorant at fixed shape and internal times is
$b(\gamma)=h^n\exp(-\delta\sum_k|S_k|x_k)$.
Let $r_\ell(\gamma)$ count maximal excitation intervals of link $\ell$,
and $T_\ell(\gamma)$ be their total length. Then
$$\sum_\ell T_\ell=A(\gamma),\qquad \sum_\ell r_\ell\le4n(\gamma),$$
because each interval begins at an insertion and an insertion touches
four links.

**Correction (2026-10-02), shift measure:** For one interval of length
$x'_k$ on link $\ell$ in $\gamma'$, the allowed translations overlapping
$\gamma$ have measure at most
$$T_\ell(\gamma)+r_\ell(\gamma)x'_k.$$
Indeed, an interval of length $L_i$ in $\gamma$ gives a translation
interval of length $L_i+x'_k$; take the union bound over all $r_\ell$
intervals. The former $T_\ell+x'_k$ expression omitted this multiplicity.

Define the majorant over **all** connected shapes reaching a test link,
without requiring their first plaquette to contain it:
$$Q_\lambda=\sup_{\ell_0}\sum_{\substack{\text{shapes}\ \exists k:\ell_0\in S_k}}
(n-1)h^n\prod_{k=1}^{n-1}\frac1{\delta|S_k|}.$$
It bounds the same integral summed over marked intervals $k$ containing
$\ell_0$. Its length-marked version is at most $Q_\lambda/(4\delta)$,
since, term by term,
$$\int_0^\infty e^{-\delta|S|x}\,dx=\frac1{\delta|S|},\qquad
\int_0^\infty x e^{-\delta|S|x}\,dx
=\frac1{(\delta|S|)^2}\le\frac1{4\delta}\frac1{\delta|S|}.$$
The chronological internal-time domain has been enlarged to the full
positive orthant. Summing the overlap union bound over links gives
$$\int_{\gamma'\not\sim\gamma}|w(\gamma')|e^{a(\gamma')}\,d\gamma'
\le Q_\lambda A(\gamma)+\frac{Q_\lambda}{4\delta}\sum_\ell r_\ell(\gamma)
\le Q_\lambda A(\gamma)+\frac{Q_\lambda}{\delta}n(\gamma).$$
Thus the corrected sufficient conditions are
$$Q_\lambda\le\lambda,\qquad Q_\lambda\le\delta.$$
The former second condition $Q_\lambda\le4\delta$ lost a factor four.
These are conditional sufficient inequalities, not a proof that the
actual $Q_\lambda$ is finite or small.

## 3. What the shape counts actually establish

**Adjacent growth with the first plaquette anchored.** Fix a link
$\ell_0$ and restrict to histories whose first plaquette contains it
and whose later insertions touch the current excited set. There are
four initial plaquettes; $S_1$ is forced. Each later insertion has at
most $4|S_{k-1}|$ plaquette choices and $16$ support choices. The
preceding interval integral cancels $|S_{k-1}|$, giving
$$u=\frac{64h}{\delta}=\frac{384e}{g^2\delta}.$$
For this restricted class the weighted sum with multiplier $n-1$,
denoted $B_\lambda$ rather than $Q_\lambda$, obeys
$$B_\lambda\le4h\sum_{m\ge1}mu^m
=\frac{24e}{g^2}\frac{u}{(1-u)^2},\qquad u<1.$$
This is a valid overcount of the restricted class.

**Correction (2026-10-02), missing roots:** Even within adjacent growth,
a polymer can start away from $\ell_0$ and reach it later. Thus
$B_\lambda$ does not bound $Q_\lambda$. Rooting at the first insertion
that touches $\ell_0$ requires controlling both the earlier and later
history. No such estimate is supplied here. Even a gas restricted to
adjacent growth still needs this additional root estimate for KP.

**General shapes and the proposed tree count.** A later insertion can
start a disjoint piece that is subsequently bridged. Join consecutive
insertions touching each link during a maximal excitation interval.
For a connected insertion graph and any spanning tree $T$, distinct
edges assigned to a link cover nonoverlapping subintervals, so
$$\sum_{e\in T}|\tau_{i(e)}-\tau_{j(e)}|\le A(\gamma),\qquad
e^{-\delta A(\gamma)}\le\prod_{e\in T}e^{-\delta|\tau_{i(e)}-\tau_{j(e)}|}.$$
This energy inequality is valid with a specified link assignment.
Each insertion has at most eight predecessor/successor link slots.
It does not establish the originally quoted complete tree majorant.

**Correction (2026-10-02), general count withdrawn:** The old expression
$$u_{\rm gen}=32\cdot3\cdot16\,\frac{h}{\delta}
=\frac{9216e}{g^2\delta}=24u$$
was presented as rigorous. A child insertion may use the **same**
plaquette as its parent: creating and then annihilating a single
plaquette loop is already an example. A fixed parent link therefore
allows four plaquettes, not three. More substantially, the rooted
link/interval multiplicities and time-length marks in §2 were not
counted. A tree edge need not be a consecutive *global* time gap, so
replacing every chronological denominator by a tree-edge integral
$1/\delta$ does not justify the length-marked bound. The assertion
that the overlap criterion follows with $Q\le\delta$ under this tree
count is withdrawn. Changing three to four alone would give $32u$
in this formal expression, but is not a repair of the missing proof.
A usable general estimate must bound both the interval-marked integral
and its length-marked counterpart, or give another proved overlap
majorant. Neither $24u$ nor $32u$ is a certified general counting factor.

## 4. Numerical estimates and the spectral implication

Write $\lambda=\varepsilon(1-\theta)$, $\delta=\varepsilon\theta$,
$0<\theta<1$. The exact restricted factor is
$$u=\frac{576e}{\theta g^4}.$$
For $u\le1/2$, the proved restricted bound is
$B_\lambda\le96e\,u/g^2$. Requiring this bound to be at most both
$\lambda$ and $\delta$ is implied by
$$g^4\ge\frac{1152e}{\theta},\qquad
g^8\ge\frac{82944e^2}{\theta\min(\theta,1-\theta)}.$$
The old $3132/\theta$ is a rounded upper approximation to
$1152e/\theta$, and $6.13\times10^5$ approximates $82944e^2$.
The second condition is not universally weaker as $\theta\to1$.
These inequalities control $B_\lambda$ only. They do not certify KP
or a gap.

| $\theta$ | former adjacent threshold $g^2$ | sufficient integer $g^2$ for the displayed restricted inequalities | candidate decay rate $4\lambda$ (unproved for $H$) |
| --- | --- | --- | --- |
| $1/2$ | $79$ | $80$ | $\frac43g^2$ |
| $1/4$ | $112$ | $112$ | $2g^2$ |
| $1/10$ | $177$ | $177$ | $2.4g^2$ |

**Correction (2026-10-02), constants and table status:** $79^2=6241$
is below $2304e$, so $79$ was rounded down even for the restricted
sufficient condition. The old formal general factor is exactly
$$24u=\frac{13824e}{\theta g^4},\qquad 13824e\simeq37578.17,$$
not $37584$. Its half-factor condition alone is
$g^4\ge27648e/\theta$. The following records the old table and the
correct rounding of that **formal condition alone**, not thresholds
for the actual general gas or Hamiltonian:

| $\theta$ | former “rigorous” threshold $g^2$ (withdrawn) | integer satisfying $24u\le1/2$ only |
| --- | --- | --- |
| $1/2$ | $388$ | $388$ |
| $1/4$ | $548$ | $549$ |
| $1/10$ | $867$ | $867$ |

The old accompanying $g^8\ge1.47\times10^7/[\theta(1-\theta)]$
was likewise a formal algebraic estimate from the unproved count;
it is not retained as a convergence condition. Neither table is a
physical-gap table. Rates in its last column would be in units
$\hbar c/a$ if independently established.

**True-vacuum spectral lemma (finite volume).** Let $\psi_0$ be the
normalized true ground state, $E_0$ its energy, and $A$ a bounded
gauge-invariant multiplication observable. Put
$f_A=(A-\langle\psi_0,A\psi_0\rangle)\psi_0$. Suppose for every such
observable (including ones supported on the whole finite lattice)
$$0\le\langle f_A,e^{-t(H-E_0)}f_A\rangle\le C_Ae^{-mt},\qquad t\ge0.$$
Then $\Delta^{\rm phys}_{a,L}\ge m\hbar c/a$ in the present dimensionless
time convention.

*Proof.* The spectral measure $\mu_A$ of $f_A$ is positive. If it had
positive mass on $[0,m-\eta]$ for some $\eta>0$, its Laplace transform
would be at least $\mu_A([0,m-\eta])e^{-(m-\eta)t}$, contradicting the
assumed bound. Thus every $f_A$ has zero spectral weight below $m$.
These vectors are dense in the physical ground-state complement:
$\psi_0>0$ almost everywhere, and any physical $f$ can be approximated
by $A_M\psi_0$ with
$A_M=(f/\psi_0)\mathbf1_{\{|f/\psi_0|\le M\}}$, which is bounded and
gauge invariant. Centering gives the asserted density. Boundedness of
spectral projections extends their vanishing to that complement.
This proves the lemma. In infinite volume the same implication needs
the specified vacuum GNS representation and a dense observable domain.

**Correction (2026-10-02), missing correlation estimate:** The lemma's
hypothesis has not been established by this expansion. Correlations
with external $\Omega_0$ are not automatically true-vacuum correlations.
For each finite volume one can obtain the latter by placing observables
in the interior of a long time slab, dividing by $Z(2T+t)$, and sending
$T\to\infty$. Explicitly, for $A$ centered in the true vacuum,
$$\frac{\langle\Omega_0,e^{-TH}A^*e^{-tH}Ae^{-TH}\Omega_0\rangle}
{\langle\Omega_0,e^{-(2T+t)H}\Omega_0\rangle}
\longrightarrow\langle\psi_0,A^*e^{-t(H-E_0)}A\psi_0\rangle.$$
This follows from the rank-one ground-state spectral projection and
$\langle\psi_0,\Omega_0\rangle>0$; it gives no quantitative decay rate.
A polymer proof must control the normalized, connected insertion
expansion uniformly in the boundary distance $T$ and volume. Also,
the four-link energy bound for individual physical histories does not
by itself prove that the union of every correlation cluster has area
at least $4t$. The required spanning-cluster estimate and observable
prefactors must be proved. Consequently $m=4\lambda$ remains a candidate
rate, and no volume-uniform $\gamma\to4$ or ratio $18/\gamma=4.5$ follows
here. Only the fixed-volume limit in §1 is proved.

## 5. What remains of the time-discretized comparison

**Correction (2026-10-02):** “Yarotsky's theorem gives a threshold
$10^{101}$” and “this beats it by giving $10^2$” were too strong.
Yarotsky's theorem provides an existential smallness threshold, not
that number; the latter is the repository's crude proof-extraction
estimate in [strong-coupling-threshold-explicit](strong-coupling-threshold-explicit.md)
§§1--2 (repository derivation read). Its assumptions are reproduced
below so the comparison is checkable, but the estimate is **heuristic**,
not a certified sufficient threshold of this note.

Normalize by $\varepsilon=2g^2/3$. Group the three plaquette potentials
based at one site: their total norm is at most $54/g^4$. If one assumes
a space-time support entropy $c^n$ with $c=80e$, a per-support-site
activity bound $\rho^n$, and the sufficient condition
$\sum_{n\ge1}(ce\rho)^n\le1$, then $\rho\le1/(2ec)=1/(160e^2)$.
Assume further the site activity estimates
$$\rho_J=e^{-t_0},\qquad
\rho_I=2e\,t_0\beta\,e^{64t_0}.$$
The $64$ comes from the proposed shadow-volume estimate
$|\Lambda_0|^2$ with $\Lambda_0=\{0,1\}^3$, $|\Lambda_0|=8$.
The insertion prefactor follows by minimizing
$2\alpha e^{t_0\beta/\alpha}$ over $\alpha>0$, at $\alpha=t_0\beta$.
Thus $t_0\ge\log(160)+2$ controls $\rho_J$, and choosing $t_0=7.1$
would require
$$\beta\le\frac{e^{-454.4}}{160e^2\,2e\cdot7.1},\qquad
\log\beta\lesssim-465,\qquad
\log g_0^2=\tfrac12(\log54-\log\beta)\simeq234.5.$$
This is roughly $10^{102}$; the former $10^{101}$ quotation was only
an order-of-magnitude description. The extraction still needs a proved
conversion of the full configuration weights and their multiplicities
into the assumed support-site activity bound; it is not a quantitative
application of Yarotsky's theorem proved here. In particular $e^{64t_0}$
is the cost in this assumed shadow estimate, not an unavoidable cost
of every time-discretized method.

The established result used instead is the local-perturbation theorem
as applied in [strong-coupling-uniform-gap](strong-coupling-uniform-gap.md)
§§1--2 (repository hypothesis check read; Yarotsky's Theorem 1 at the
passage level recorded there): for sufficiently small $54/g^4$ there
is a positive volume-uniform gap, with unspecified constants. Retaining
exact link decay in continuous time is a plausible way to improve
constants, but the counts and boundary estimates missing above prevent
any proved numerical improvement in this note.

## 6. Consequence for STATE

This note no longer supplies an explicit volume-uniform KS threshold
$g^2\ge388$, the adjacent value $79$, or a uniform gap coefficient
approaching $8/3$. Its proved outputs are the fixed-volume bound of §1,
the conditional overlap criterion of §2, and the restricted count of
§3. The numerical tables are restricted or formal estimates, with
their status stated at each use. T2 remains supported by the separate
existential strong-coupling theorem. Any catalog or downstream use of
this note's old uniform thresholds, including the target-box tolerances,
needs to inherit this correction. An explicit continuous-time uniform
threshold requires a complete marked general-history count and a
normalized true-vacuum correlation bound. This correction changes no
other note, no STATE file, and makes no weak-coupling or continuum claim.
