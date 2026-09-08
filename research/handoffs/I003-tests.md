# I003: tests 1–3 drafted

- **Task:** push idea I003 as deep as possible, as asked by the user on
  2026-09-08.
- **Role/model/effort:** interactive Claude Fable 5.1 session; no subagents.
- **Date:** 2026-09-08.
- **Outputs:** `notes/cut-paradox-two-faces.md` (test 1, scalar rigidity) and
  `notes/i003-double-limit-rigidity.md` (general rigidity theorem, one-scale
  corollary, double limit, verdict on remarks 2 and 3, prior-art list), with
  `scripts/cut_paradox_checks.py` and `scripts/i003_double_limit_checks.py`
  in `make check`; I003 status lines; one TASKS row and one STATE pointer.

## Results

1. Any translation-invariant contraction semigroup on $L^2(\mathbb R;\mathbb C^n)$
   with light-cone-supported kernels has symbol $G_0+ikG_1$ with the numerical
   radius of $G_1$ at most $u$: unitary groups are the Dirac class of C039,
   positivity-preserving semigroups are the velocity-jump class of C019.
   Proof by Paley–Wiener–Schwartz, Bernstein's inequality and Duhamel's formula.
2. The evolution has a crossover if and only if $[G_1,G_0]\ne0$; for two
   velocity states the crossover time is $2u/\|[\cdot,\cdot]\|$, giving $1/\lambda$
   and $1/\omega_0$, and the action constants $mu^2/\lambda$ and $mc^2/\omega_0$.
3. The resolution-dependent window coefficient has no joint limit; the
   diffusive parabola manufactures a spurious coefficient, the ballistic
   diagonal gives zero, and the ordered limit gives the plateau above $\Delta_*$.
4. Remark 3 holds inside the class; remark 2 holds as positivity iff
   noncommutativity and as a minimum window given $K$ and $u$; a minimum $K$
   needs C035–C036.

## Checks and limits

Twenty-one checks in the new script pass. The theorem's measure-theoretic
steps (semigroup measurability at fixed $k$, the principal logarithm) are
sketched and need an adversarial review; the theorem may be standard and the
prior-art audit should search for finite-propagation characterizations of
translation-invariant semigroups. No claim IDs assigned.

## Next bounded task

Review of the theorem, the prior-art audit (D'Ariano–Perinotti 2014,
Bisio–D'Ariano–Tosini 2015, Feynman–Hibbs §7-3, Abbott–Wise 1981, Boas 1954,
Hörmander 7.3.1), and the composition of two affine systems as the A08 test
inside the class.
