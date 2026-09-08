"""Exact checks for notes/cut-paradox-two-faces.md (I003, test 1)."""
from pathlib import Path
import json
import sympy as sp


def main():
    checks = {}

    def record(name, residual):
        assert sp.simplify(residual) == 0, (name, residual)
        checks[name] = "passed"

    u, T, lam, k, w0, m, c, hbar, r, h, z, d = sp.symbols(
        "u T lambda k omega0 m c hbar r h z delta", positive=True)
    n = sp.symbols("n", positive=True, integer=True)
    x, y, beta, b = sp.symbols("x y beta b", real=True)

    # 1. C032 variance step: n Var(mu_{T/n}) <= n u^2 (T/n)^2 = u^2 T^2 / n -> 0
    record("c032_variance_bound", n*u**2*(T/n)**2 - u**2*T**2/n)
    record("c032_bound_vanishes", sp.limit(u**2*T**2/n, n, sp.oo))

    # 2. Linear dispersion: |Im omega| = |beta| |Im k|, saturating the light-cone bound at |beta| = u
    omega_lin = beta*(x + sp.I*y) + b
    record("linear_dispersion_imaginary_part", sp.im(omega_lin) - beta*y)

    # 3. Quadratic dispersion violates linear growth of Im omega
    omega_quad = (x + sp.I*y)**2
    ratio = sp.simplify(sp.im(omega_quad)/y)          # = 2x, unbounded in x
    assert sp.limit(ratio, x, sp.oo) == sp.oo
    checks["quadratic_dispersion_unbounded"] = "passed"

    # 4. Klein-Gordon dispersion: branch points at k = ± i omega0/u; Compton value at u=c, omega0=mc^2/hbar
    kk = sp.symbols("kk")
    roots = sp.solve(sp.Eq(u**2*kk**2 + w0**2, 0), kk)
    assert set(roots) == {sp.I*w0/u, -sp.I*w0/u}
    checks["kg_branch_points"] = "passed"
    record("kg_branch_point_compton", (w0/u).subs({u: c, w0: m*c**2/hbar}) - m*c/hbar)

    # 5. Telegraph transform is even in s = sqrt(lambda^2 - u^2 k^2), hence entire in k
    s = sp.symbols("s")
    tele = sp.exp(-lam*T)*(sp.cosh(s*T) + (lam/s)*sp.sinh(s*T))
    record("telegraph_transform_even_in_s", sp.simplify(tele - tele.subs(s, -s)))

    # 6. Continuation lambda -> i omega0 turns s into i sqrt(u^2 k^2 + omega0^2)
    s_cont = sp.sqrt((sp.I*w0)**2 - u**2*k**2)
    record("continuation_gives_kg_frequency", sp.simplify(s_cont**2 + (u**2*k**2 + w0**2)))

    # 7. Cone sections: adjacent sections differ at first order; cylinder does not
    A = sp.pi*r**2*(1 - z/h)**2
    record("cone_section_derivative", sp.diff(A, z) + 2*sp.pi*r**2*(1 - z/h)/h)
    record("cone_first_order_difference",
           sp.series(A.subs(z, z + d) - A, d, 0, 2).removeO() - sp.diff(A, z)*d)
    record("cylinder_sections_constant", sp.diff(sp.pi*r**2, z))

    # 8. Harmonic-polynomial instance: linear harmonic function vanishing on the axis is beta*y
    hlin = sp.symbols("alpha")*x + beta*y + sp.symbols("gamma")
    record("linear_harmonic_laplacian", sp.diff(hlin, x, 2) + sp.diff(hlin, y, 2))
    hquad = x**2 - y**2
    record("quadratic_harmonic_laplacian", sp.diff(hquad, x, 2) + sp.diff(hquad, y, 2))
    assert sp.limit(hquad.subs(y, 0)/x, x, sp.oo) == sp.oo   # violates |h| <= A|z| + B
    checks["quadratic_harmonic_violates_linear_growth"] = "passed"

    # 9. The C033 atom: one switch at T/2 puts the arrow at uT/2 with left velocity +u and right velocity -u
    Tt = sp.symbols("T", positive=True)
    pos_left = u*(Tt/2)
    pos_right = u*(Tt/2) - u*(Tt/2 - Tt/2)
    record("atom_position", pos_left - u*Tt/2)
    record("atom_position_right_continuous", pos_right - u*Tt/2)

    report = {"scope": "Finite algebra for notes/cut-paradox-two-faces.md; the proposition's proof is in the note",
              "checks": checks}
    out = Path(__file__).resolve().parents[1]/"out"/"cut-paradox-checks.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
