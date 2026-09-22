# State

Updated 2026-09-22. Read this page and the note it points to; AGENTS.md
governs. The previous long version, with the full $SU(3)$ queue and the
source-by-source classics log, is in git at commit 6bc52cb.

## Goal

User direction, 2026-09-17: **establish the Planck gap with Newton-age
arguments and their modern equivalents**, in one paper valid for
foundations of physics and for history and philosophy of science. The
comparison is Galileo's inertial line against the falling parabola, whose
area Newton takes to zero in Lemmas X and XI. User direction, 2026-09-22:
put the effort on the modern leg; the classics serve mostly as
inspiration, and the formal and textual work on the *Principia* lives in
the sibling repository `newtonlean`. Constructive steps take precedence
over no-go results.

## In hand

[The paper draft](../notes/planck-gap-paper.md) is the synthesis; the
proofs are in four notes.

- **Classical floor.** Every protocol of Gaussian marks with uncorrelated error
  and recoil and $\delta_j\Delta_j\ge\kappa$ needs
  $\tau\Delta E\ge48z_{1-\epsilon}^2\kappa$, sharp (constant from the
  Poincaré inequality, since invariance under $v_0$ pins $T$ at both ends)
  ([mark-cost note](../notes/mark-cost-and-statistical-floor.md),
  Theorem B; worst-case form in the
  [derivation note](../notes/planck-gap-derivation.md)).
- **Mark cost.** A momentum-transfer mark has conjugate error and recoil,
  so $\kappa\ge\hbar/2$ (Theorem A). A correlation $\rho$ between them
  multiplies the floor by $\sqrt{(1-\rho)/(1+\rho)}$ (Theorem C), and
  three marks attain that dependence (Proposition D).
- **Unmarked preparations.** At aperture $(L,P)$,
  $F\tau L+\frac{F\tau^2}{2m}P\ge(1-2\epsilon)\hbar$ for every adaptive
  protocol ([probabilistic note](../notes/planck-gap-probabilistic.md),
  Theorem 2): impulse against position aperture plus sagitta against
  momentum aperture. The floor is $(1-2\epsilon)^2\hbar^2/(4LP)$ at the
  balanced aperture $L=\tau P/2m$.
- **The junction.** M3 is Robertson's inequality for Newton's corpuscle,
  with the interval of fits as one factor
  ([mark-floor note](../notes/newton-mark-floor.md)), plus the clause
  that the undetermined impulse is unrelated to the mark's error.
- **Classics.** Paper §7 and the [arrow-and-sling note](../notes/arrow-not-sling.md);
  companions in `docs/classics/`.

**Correction, 2026-09-22.** Both quantum floors needed a bound on the
shape of an uncertainty ellipse, since each falls to zero under squeezing
at fixed area. An exported ChatGPT review found the aperture case; the
correlated-mark case was found here. Both are restated as theorems with
the shape parameter explicit.

## Next, modern leg first

1. **Done, 2026-09-22: the squeeze-immune core.**
   [The polygon-lift note](../notes/polygon-lift-phase.md): Newton's
   inscribed polygon and the parabola coincide classically at every
   vertex, and quantum mechanically differ by the pure phase
   $\theta_N=F^2\sum_j\tau_j^3/(24m\hbar)=(F/2v\hbar)\sum_jS_j$, with
   $S_j$ the parabolic segments. Each inserted vertex lowers it by the
   inscribed triangle over $\hbar$, in Archimedes' proportions; the
   reversed ordering carries the complement,
   $\Phi_N+4\theta_N=\tau\Delta E/3\hbar$ for every partition. Newton-age
   form, §5: *Opticks* II.iii Props. X and XVII make $\Lambda p$ a
   refraction invariant, so the fits count along a path is the Maupertuis
   action in units of $\Lambda p$, and it separates the polygon from the
   curve by $(F/v)\sum_jA_j/(2\Lambda p)$ fits. The paper carries
   it as Theorem 6 (§4) with the refraction invariant in §§5--6.
2. **Done, 2026-09-22: general force law and one functional.** Theorem 2
   is sharp with constant $48$ (Poincaré, since $T(0)=T(\tau)=0$). For any
   force history, with $\mathcal K_\tau$ the kinetic action of the motion
   relative to its chord, the polygon phase is $\sum_j\mathcal K_{\tau_j}/\hbar$
   and the sharp mark bound is $d^2\le\mathcal K_\tau/\kappa$; at
   $\kappa=\hbar/2$ the best recorded deflection is twice the chord phase
   (polygon-lift note §6, paper Theorem 7). Open on this line: the
   aperture form for a general force, and correlated marks in Theorem 7.
3. **Done, 2026-09-22: mixed conditional states.** The probabilistic
   Theorem 2 holds for every instrument, any Kraus rank and any apparatus
   memory, by purification.
4. **Theorem A beyond the momentum-transfer class**, in the order the
   user set on 2026-09-22: option 3 first, then 1, then 2. **Option 3
   done:** [the recoil note](../notes/record-costs-recoil.md). Grid probes
   with $\rho=0$ break the Gaussian floor (Proposition G); for every probe
   state, $s\sum_j\Delta_j\ge8(1-2\epsilon)\hbar$ (Theorem R, paper
   Theorem 8), within a constant of squeezed protocols at every squeezing.
   **Option 1 done:** [the additive-noise note](../notes/additive-noise-marks.md).
   Body-independent noise forces $[\hat N,\hat D]=-i\hbar$; with the
   position undisturbed the mark is a von Neumann mark on a canonical pair
   of the apparatus; Theorem R holds for the whole class. **Next, option 2:** Ozawa's relation for body-dependent
   instruments, where the body's own spreads enter.

History, lower priority: the Section I Scholium, where Newton cites
Euclid X against least magnitudes, as the first entry of the Book I
scholion; §9's reading and edition obligations.

## Paused

$SU(3)$ mass gap: [the position note](../notes/mass-gap-position.md) and
[the conditional theorem](../notes/mass-gap-conditional-theorem.md) hold
the map; a proof consists of hypotheses H1 and H2 there.

## Constraints

No numerical or symbolic verification scripts. Build one note at a time
with `make paper NOTE=<slug>`. No multi-agent workflows. Commit and push
after each result.
