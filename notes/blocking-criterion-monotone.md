# Blocking and Schur bounds: the surface-to-gap obstruction

A block criterion based on the norm of straddling plaquettes divided by
an intra-block gap has a surface cost. For $M^3$-site blocks of a
three-dimensional spatial lattice the counted sufficient bound is
$$\beta_{\rm block}=\frac{24M^2N}{g^2\delta(g;M)},\qquad
\Delta_M=\frac{\hbar c}{a}\delta(g;M).$$
Its strong-coupling asymptotic exceeds the direct criterion by
$3M^2/8$, and a small-volume zero-mode model gives $M^3$ scaling. These
are regime-dependent comparisons, not a proof of monotonicity at every
coupling. The inequality $\beta_{\rm block}(M)\ge\beta_{\rm block}(1)$
follows if $\delta(g;M)\le M^2\delta(g;1)$; a separate upper bound on
$\delta(g;M)$ does not establish this comparison. The original
all-coupling claim is withdrawn. No uniform physical mass gap or
continuum construction follows.

## 1. Blocking, norms and the Schur issue

Partition a periodic lattice of $N_s=MK$ sites per side into $K^3$
blocks, assign links by midpoint and write
$$H=\sum_\alpha H_\alpha+\sum_{p\ {\rm straddling}}w_p,\qquad
H_\alpha=\frac{\hbar cg^2}{2a}\sum_{\ell\in\alpha}(-\Delta_\ell)
+\sum_{p\subset\alpha}w_p.$$
The earlier calculation used $6M^2$ straddling plaquettes per block;
face-crossing counting may require a factor of two unless terms are
half-attributed. The displayed numerical criterion is conditional on
that assignment. For each plaquette,
$\|w_p\|\le4N\hbar c/(ag^2)$. Edge counting and interaction assignment
must be fixed before applying a particular polymer theorem. The block
Hamiltonians have finite-volume ground states and gap $\Delta_M>0$.
A product projection $P$ onto block low-energy subspaces gives a
compression $A=PHP$; a Schur reduction additionally requires a lower
bound on the complement $D=\bar PH\bar P$, including the straddling
interactions. Such a bound does not follow merely from the uncoupled
block gap.

If $B=PH\bar P$ and a complementary resolvent bound is supplied, a
naive per-block estimate is
$$\frac{\|B\|^2}{\Delta_M}\lesssim
36M^4\frac{\hbar c}{a}\frac{16N^2}{g^4\delta(g;M)}.$$
This measures a large boundary contribution as well as level-dependent
variation. The relative Schur lemmas in
[the Feshbach note](weak-coupling-feshbach-reduction.md) show why a common
energy shift can cancel from a gap estimate, while its energy dependence
and residual variation still need control. A proposed bound
$$\|R(E)\|\le C\sum_{p\ {\rm straddling}}
\frac{\|w_p\|^2}{\Delta_M}$$
would replace the naive $M^4$ counting by $M^2$, but is a hypothesis:
polymer connectedness by itself does not prove this particular Schur
operator inequality or its volume-uniform constants. The earlier
one-step threshold and induction based on that unproved inference are
withdrawn.

## 2. Direct block criterion and its limitations

Normalize a block Hamiltonian by its gap,
$h_\alpha=(H_\alpha-E_0^\alpha)/\Delta_M$, and bound the normalized
inter-block perturbation by $\beta_{\rm block}$ above if that count and
assignment hold. Yarotsky's
bounded-perturbation theorem gives a sufficient criterion of the form
$\beta_{\rm block}\le\beta_*$, subject to its product-space, unique
block-ground-state, finite-range and interaction-assignment hypotheses.
Its polymer proof (Commun. Math. Phys. 261 (2006), §2, passage-level
reading) has connected excited-region weights; it can be applied only
after those hypotheses are checked, and it is not the asserted Schur
variation estimate. See the group-specific application and its scope in
[strong coupling](strong-coupling-uniform-gap.md).

At strong coupling, in a block containing an elementary loop and in the
gauge-invariant sector, the electric excitation is a fundamental
plaquette loop with energy $2C_2(R_{\min})g^2\hbar c/a$. For fixed block
geometry as $g\to\infty$ this gives
$$\beta_{\rm block}\sim\frac{12M^2N}{C_2g^4},\qquad
\frac{\beta_{\rm block}}{\beta_{\rm direct}}\sim\frac{3M^2}{8},\qquad
\beta_{\rm direct}=\frac{32N}{C_2g^4}.$$
Thus the displayed sufficient estimates compare unfavourably at $M=2$
in that asymptotic regime; they are bounds, not exact optimal thresholds.
Boundary conditions and the sector of the block operator matter.

For $SU(3)$, $C_2=4/3$ gives
$$\beta_{\rm block}=\frac{72M^2}{g^2\delta(g;M)},\qquad
\beta_{\rm direct}=\frac{72}{g^4}.$$
The same asymptotic ratio is $3M^2/8$, formally $3/2$ at $M=2$.
These constants retain the stated half-attribution and block-geometry
conditions; they do not establish an all-coupling comparison.

For a periodic small-volume zero-mode model, the conditional asymptotic
$\Delta_M\sim\delta_1g^{2/3}\hbar c/(Ma)$ would give
$$\beta_{\rm block}\sim\frac{24M^3N}{\delta_1g^{8/3}}.$$
It must not be imported without proof into the free-boundary blocks
above or treated as a uniform fixed-cutoff theorem; see
[the Feshbach reduction](weak-coupling-feshbach-reduction.md).
Algebraically the criterion is no better than its $M=1$ analogue if
$\delta(g;M)\le M^2\delta(g;1)$, assuming both are defined with compatible
boundary conventions. This condition has not been established for all
couplings. A one-sided upper bound such as the
[Polyakov variational bound](lattice-gap-upper-bounds.md#spatial-polyakov-loop-trials) cannot supply
the missing lower comparison with $\delta(g;1)$.

## 3. Running coupling and generated interactions

The one-loop count for successive doublings, conditional on the running
law $g_{n+1}^{-2}=g_n^{-2}-2b_0\log2$ with
$b_0=11N/(48\pi^2)$, is
$$n\simeq\frac{g_{\rm UV}^{-2}-g_{\rm thr}^{-2}}{2b_0\log2}.$$
For $SU(2)$, $2b_0\log2=11\log2/(12\pi^2)\approx0.064$; the
illustrative inputs $g_{\rm UV}^2=1/2$ and $g_{\rm thr}^2\approx20$
yield about thirty doublings. This perturbative extrapolation is not a
certified arrival at a strong-coupling domain. The number increases
with the ultraviolet cutoff along an asymptotically free trajectory.
A projection generates longer-range and other interactions, and a
coupling label alone does not prove an iterated effective-action or gap
estimate. An RG construction must control those generated terms and
observable matching at each scale.

## 4. Consequence for STATE

Keep the boundary count, conditional comparison, asymptotic strong-coupling
calibration and Schur distinction. Neither a general no-improvement
theorem nor a connected-Schur estimate is established. Control of the
blocked action and gap through the weak-to-intermediate regime remains
open; the physical energy unit is $\hbar c/a$ and the volume and
continuum limits are separate obligations.
