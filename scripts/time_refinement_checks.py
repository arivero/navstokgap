"""Exact checks for the free Gaussian refinement experiment."""

from pathlib import Path
import json

import sympy as sp


def main():
    s, t, m, kappa = sp.symbols("s t m kappa", positive=True)
    x, y, z, k = sp.symbols("x y z k", real=True)
    mean = (t*x + s*z)/(s+t)
    variance = kappa*s*t/(m*(s+t))
    fine_prefactor = m/(2*sp.pi*kappa*sp.sqrt(s*t))
    coarse_prefactor = sp.sqrt(m/(2*sp.pi*kappa*(s+t)))
    gaussian_integral = sp.sqrt(2*sp.pi*variance)
    checks = {
        "square_completion": (y-x)**2/s + (z-y)**2/t
        - (z-x)**2/(s+t) - (s+t)*(y-mean)**2/(s*t),
        "blocking_normalization": fine_prefactor*gaussian_integral - coarse_prefactor,
        "bridge_mean": mean - (x + s*(z-x)/(s+t)),
        "bridge_variance_from_hessian": 1/(m/kappa*(1/s+1/t)) - variance,
        "bridge_concentration_limit": sp.limit(variance, kappa, 0, dir="+"),
        "heat_fourier_composition": sp.exp(-kappa*s*k**2/(2*m))
        * sp.exp(-kappa*t*k**2/(2*m)) - sp.exp(-kappa*(s+t)*k**2/(2*m)),
        "unitary_fourier_composition": sp.exp(-sp.I*kappa*s*k**2/(2*m))
        * sp.exp(-sp.I*kappa*t*k**2/(2*m)) - sp.exp(-sp.I*kappa*(s+t)*k**2/(2*m)),
    }
    for name, residual in checks.items():
        if sp.simplify(residual) != 0:
            raise AssertionError(f"{name}: {residual}")
    report = {
        "scope": "Exact algebra checks; analytic proofs are in papers/time-refinement.tex",
        "assumptions": "s,t,m,kappa > 0; real positions; free line",
        "checks": {name: "passed" for name in checks},
    }
    output = Path(__file__).resolve().parents[1] / "out" / "time-refinement-checks.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
