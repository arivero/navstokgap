"""Finite algebra checks for the classical action-field paper."""

from pathlib import Path
import json

import sympy as sp


def main():
    m, u, lam, t, s, gamma, a, rate = sp.symbols(
        "m u lam t s gamma a rate", positive=True
    )
    kernel = 1-(1-sp.exp(-gamma*t))/(gamma*t)
    h = m*u**2/lam*(1-(1-sp.exp(-2*lam*t))/(2*lam*t))
    variance = u**2/lam*(t-(1-sp.exp(-2*lam*t))/(2*lam))
    checks = {
        "correlation_integral": sp.integrate((1-s/t)*sp.exp(-gamma*s), (s, 0, t))
        - kernel/gamma,
        "telegraph_correlation_integral": 2*m*sp.integrate(
            (1-s/t)*u**2*sp.exp(-2*lam*s), (s, 0, t))-h,
        "variance_normalization": m*variance/t-h,
        "short_duration_coefficient": sp.limit(h/t, t, 0, dir="+")-m*u**2,
        "long_duration_plateau": sp.limit(h, t, sp.oo)-m*u**2/lam,
        "variance_initial_value": sp.limit(variance, t, 0, dir="+"),
        "variance_initial_slope": sp.limit(sp.diff(variance, t), t, 0, dir="+"),
        "telegraph_second_moment_equation": sp.diff(variance, t, 2)
        + 2*lam*sp.diff(variance, t)-2*u**2,
        "monotonicity_derivative": sp.diff(kernel, t)
        - (1-(1+gamma*t)*sp.exp(-gamma*t))/(gamma*t**2),
        "diffusive_scaling_limit": sp.limit(h.subs(u**2, a*lam), lam, sp.oo)-m*a,
        "microscopic_first_limit": sp.limit(h.subs(u**2, a*lam), t, 0, dir="+"),
        "rate_rescaling_plateau": (m*u**2/(rate*lam))-(m*u**2/lam)/rate,
    }
    Q = sp.Matrix([[-lam, lam], [lam, -lam]])
    v = sp.Matrix([u, -u])
    phi = v/(2*lam)
    checks["two_state_poisson_equation"] = sum(x**2 for x in (-Q*phi-v))
    checks["two_state_plateau"] = m*(v.dot(phi))-m*u**2/lam
    # A nonuniform-rate symmetric chain tests the weighted inverse construction.
    Q3 = lam*sp.Matrix([[-3, 1, 2], [1, -4, 3], [2, 3, -5]])
    v3 = sp.Matrix([-u, 0, u])
    P = sp.ones(3)/3
    phi3 = (-Q3+lam*P).inv()*v3
    checks["three_state_poisson_equation"] = sum(x**2 for x in (-Q3*phi3-v3))
    checks["three_state_centering"] = sum(phi3)
    for name, residual in checks.items():
        if sp.simplify(residual) != 0:
            raise AssertionError(f"{name}: {residual}")
    report = {
        "scope": "Exact finite identities; probability and positivity proofs are in the paper",
        "assumptions": "positive m,u,lambda,durations; stationary centered velocities",
        "checks": {name: "passed" for name in checks},
        "three_state_plateau": str(sp.simplify(2*m*v3.dot(phi3)/3)),
        "analytic_review_required": [
            "bounded-speed increment inequality",
            "Fubini and dominated convergence for covariance integrals",
            "finite reversible generator spectrum and strict positivity",
            "parameter-dependent bounds and interpretation of the two limits",
        ],
    }
    output = Path(__file__).resolve().parents[1]/"out"/"classical-action-field-checks.json"
    output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
