"""Exact finite checks accompanying the proofs in regulator-limits.tex."""

from pathlib import Path
import json

import sympy as sp


def main():
    m, kappa, tau, b, T, v, eps, kappa_r, m_r = sp.symbols(
        "m kappa tau b T v eps kappa_r m_r", positive=True
    )
    checks = {}
    # Arbitrary rational partitions, so every residual is exact, not a tolerance.
    for steps in ([2, 3], [1, 4, 2], [2, 1, 3, 5], [1, 3, 2, 7, 4]):
        times = [sp.Integer(0)]
        for step in steps:
            times.append(times[-1] + sp.Rational(step, 7))
        widths = [times[j+1] - times[j] for j in range(len(steps))]
        d = len(steps)-1
        A = sp.zeros(d)
        for j in range(d):
            A[j, j] = m*(1/widths[j] + 1/widths[j+1])
            if j+1 < d:
                A[j, j+1] = A[j+1, j] = -m/widths[j+1]
        green = sp.Matrix(d, d, lambda i, j:
                          (min(times[i+1], times[j+1])
                           - times[i+1]*times[j+1]/times[-1])/m)
        checks[f"determinant_d{d}"] = A.det() - m**d*times[-1]/sp.prod(widths)
        checks[f"green_inverse_d{d}"] = sum(
            x**2 for x in (A*green-sp.eye(d))
        )
        fine = sp.prod(sp.sqrt(m/(2*sp.pi*kappa*w)) for w in widths)
        integral = (2*sp.pi*kappa)**(sp.Rational(d, 2))/sp.sqrt(A.det())
        coarse = sp.sqrt(m/(2*sp.pi*kappa*times[-1]))
        checks[f"kernel_normalization_d{d}"] = fine*integral-coarse

    N = sp.symbols("N", positive=True, integer=True)
    d = N-1
    checks["defect_mean_limit"] = sp.limit(d*b*T/(2*N), N, sp.oo)-b*T/2
    checks["defect_variance_limit"] = sp.limit(d*(b*T/N)**2/2, N, sp.oo)
    # Verify the whitened moments from one normal coordinate.
    z = sp.symbols("z", real=True)
    normal = sp.exp(-z**2/2)/sp.sqrt(2*sp.pi)
    checks["normal_second_moment"] = sp.integrate(z**2*normal, (z, -sp.oo, sp.oo))-1
    checks["normal_fourth_moment"] = sp.integrate(z**4*normal, (z, -sp.oo, sp.oo))-3
    u = sp.symbols("u", real=True)
    for n in (1, 2, 5):
        velocity = v*sp.cos(2*sp.pi*n*u/T)
        checks[f"speed_example_cross_n{n}"] = sp.integrate(velocity, (u, 0, T))
        checks[f"speed_example_action_n{n}"] = (
            m*sp.integrate(velocity**2, (u, 0, T))/2-m*v**2*T/4
        )
    mass_bare = eps*m_r/kappa_r
    checks["bare_phase_coefficient"] = mass_bare/eps-m_r/kappa_r
    checks["bare_normalizer"] = (
        sp.sqrt(mass_bare/(2*sp.pi*eps*tau))
        - sp.sqrt(m_r/(2*sp.pi*kappa_r*tau))
    )
    for name, residual in checks.items():
        if sp.simplify(residual) != 0:
            raise AssertionError(f"{name}: {residual}")
    report = {
        "scope": "Exact finite algebra and moments; analytic limit proofs are in the paper",
        "assumptions": "positive parameters; fixed endpoints; free quadratic action",
        "checks": {name: "passed" for name in checks},
        "analytic_review_required": [
            "general partition determinant induction and Green inverse",
            "common Brownian bridge coupling and L2 action limit",
            "Schwartz stationary phase and gradient-delta normalization",
        ],
    }
    output = Path(__file__).resolve().parents[1] / "out" / "regulator-limit-checks.json"
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
