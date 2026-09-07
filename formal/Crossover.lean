-- Draft F01 target, written 2026-09-08. UNCOMPILED: no Lean toolchain was
-- available on the authoring machine. Acceptance follows formal/README.md.
--
-- Finite speed versus a window-independent action coefficient.
-- If the increment variance over a window Δ equals κΔ/m and paths have speed
-- at most u, then κΔ/m ≤ u²Δ², hence Δ ≥ κ/(m u²). At κ = ħ and u = c this
-- window is the reduced Compton time. See notes/composition-crossover-gap-checks.md.
import Mathlib

theorem crossover_window
    (κ m u Δ : ℝ) (hm : 0 < m) (hu : 0 < u) (hΔ : 0 < Δ)
    (hvar : κ * Δ / m ≤ u ^ 2 * Δ ^ 2) :
    κ / (m * u ^ 2) ≤ Δ := by
  have hmu : 0 < m * u ^ 2 := by positivity
  rw [div_le_iff hmu]
  have h1 : κ * Δ ≤ m * (u ^ 2 * Δ ^ 2) := by
    have := (div_le_iff hm).mp hvar
    linarith
  nlinarith [h1, hΔ]

-- Below the crossover, any coefficient obeying h ≤ m u² Δ is at most the
-- fraction Δ/Δ* of a prescribed window-independent value κ (C018/C031 form).
theorem coefficient_fraction
    (κ m u Δ h : ℝ) (hm : 0 < m) (hu : 0 < u) (hΔ : 0 < Δ) (hκ : 0 < κ)
    (hbound : h ≤ m * u ^ 2 * Δ) :
    h / κ ≤ Δ / (κ / (m * u ^ 2)) := by
  have hmu : 0 < m * u ^ 2 := by positivity
  rw [div_div_eq_mul_div]
  have : h / κ ≤ m * u ^ 2 * Δ / κ :=
    div_le_div_of_nonneg_right hbound hκ.le
  calc h / κ ≤ m * u ^ 2 * Δ / κ := this
    _ = Δ * (m * u ^ 2) / κ := by ring
