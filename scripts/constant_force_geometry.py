"""Exact checks and an exportable figure for the perpendicular-launch note.

Run from any directory: python3 scripts/constant_force_geometry.py
Dependencies used in this run: SymPy 1.14.0, Matplotlib 3.10.9.
"""

from pathlib import Path
import json

import sympy as s
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    m, F, v, T = s.symbols("m F v T", positive=True)
    t, alpha = s.symbols("t alpha", real=True)
    x = v * t
    y = F * t**2 / (2 * m)
    chord = F * T * t / (2 * m)
    dK = F**2 * T**2 / (2 * m)
    triangle = v * T * y.subs(t, T) / 2
    lens = s.integrate(v * (chord - y), (t, 0, T))

    def action(path):
        return s.integrate(m * (v**2 + s.diff(path, t)**2) / 2 + F * path, (t, 0, T))

    deltaS = s.simplify(action(chord) - action(y))
    varied = s.simplify(action(y + alpha * t * (T - t)) - action(y))
    checks = {
        "newton_equation": m * s.diff(y, t, 2) - F,
        "energy_conservation": s.diff(m * (v**2 + s.diff(y, t)**2) / 2 - F * y, t),
        "triangle_conversion": triangle - v * T * dK / (2 * F),
        "lens_ratio": lens - triangle / 3,
        "action_area_conversion": deltaS - F * lens / (2 * v),
        "action_difference": deltaS - F**2 * T**3 / (24 * m),
        "arbitrary_variation": varied - m * alpha**2 * T**3 / 6,
    }
    for name, residual in checks.items():
        if s.simplify(residual) != 0:
            raise AssertionError(f"{name}: {residual}")

    output = Path(__file__).resolve().parents[1] / "out"
    output.mkdir(exist_ok=True)
    report = {
        "assumptions": "m,F,v,T > 0; V=-F*y; endpoints fixed; no quantum postulate",
        "checks": {name: "passed" for name in checks},
        "triangle": str(triangle),
        "chord_curve_area": str(lens),
        "chord_minus_classical_action": str(deltaS),
        "arbitrary_variation_action": str(varied),
    }
    (output / "constant-force-checks.json").write_text(json.dumps(report, indent=2) + "\n")

    # Dimensionless axes X=x/(v*T), Y=y/(F*T**2/(2*m)).
    z = [i / 300 for i in range(301)]
    parabola = [q*q for q in z]
    fig, ax = plt.subplots(figsize=(7.4, 4.8), layout="constrained")
    ax.fill_between(z, 0, parabola, color="#dceaf6", label="Tangent–curve area = 2/3 triangle")
    ax.fill_between(z, parabola, z, color="#f5d39c", label="Chord–curve area = 1/3 triangle")
    ax.plot(z, parabola, color="#165d93", lw=2.5, label="Constant-force trajectory")
    ax.plot(z, z, color="#9c5a10", lw=1.7, label="Same-endpoint straight chord")
    ax.plot([0, 1, 1], [0, 0, 1], "k--", lw=1)
    ax.annotate("Launch", (0, 0), xytext=(0.04, -0.11))
    ax.annotate("Endpoint", (1, 1), xytext=(0.76, 1.06))
    ax.set(xlabel="Horizontal displacement / (v₀ T)", ylabel="Deflection / (F T² / 2m)",
           xlim=(-0.03, 1.05), ylim=(-0.17, 1.17), title="One interval: three distinct geometric areas")
    ax.legend(loc="upper left", fontsize=8.5)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(output / "constant-force-areas.svg")
    fig.savefig(output / "constant-force-areas.png", dpi=160)
    plt.close(fig)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
