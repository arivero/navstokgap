"""Reproduce bounded algebra/measurement checks; not a formal proof certificate."""

from pathlib import Path
import json
import math

import sympy as s


def success_probability(phi, copies):
    """Optimal equal-prior success for the paper's independent pure-state copies."""
    if isinstance(copies, bool) or not isinstance(copies, int) or copies < 1:
        raise ValueError("copies must be a positive integer")
    cosine = min(1.0, abs(math.cos(phi / 2)))
    if cosine == 0:
        return 1.0
    distance_squared = -math.expm1(2 * copies * math.log(cosine))
    return 0.5 * (1 + math.sqrt(max(0.0, distance_squared)))


def action_threshold(probability, copies, hbar=1.0):
    """First-lobe threshold; input hbar is assumed, never inferred."""
    if isinstance(copies, bool) or not isinstance(copies, int) or copies < 1:
        raise ValueError("copies must be a positive integer")
    if not (0.5 < probability <= 1) or not math.isfinite(hbar) or hbar <= 0:
        raise ValueError("require 1/2 < probability <= 1 and finite hbar > 0")
    if probability == 1:
        return math.pi * hbar
    # acos(exp(x)) = 2 asin(sqrt((1-exp(x))/2)), evaluated stably near x=0.
    x = math.log(4 * probability * (1 - probability)) / (2 * copies)
    return 4 * hbar * math.asin(math.sqrt(-math.expm1(x) / 2))


def main():
    t, a = s.symbols("t a", real=True)
    m, T, F, omega, hbar = s.symbols("m T F omega hbar", positive=True)
    k, tau = s.symbols("k tau", real=True)
    n = s.symbols("n", integer=True, positive=True)
    eta = a * t * (T - t)
    y = F * t**2 / (2 * m)

    def action(q):
        return s.integrate(m * s.diff(q, t)**2 / 2 + F * q, (t, 0, T))

    mode = s.sin(n * s.pi * t / T)
    multiplier = s.exp(-s.I * hbar * tau * k**2 / (2 * m))
    r = s.symbols("r", nonnegative=True)
    # The two-state density difference restricted to its span, with overlap r.
    difference = s.Matrix([[1-r**2, -r*s.sqrt(1-r**2)],
                           [-r*s.sqrt(1-r**2), -(1-r**2)]])
    checks = {
        "fixed_endpoints": eta.subs(t, 0) + eta.subs(t, T),
        "action_variation": action(y + eta) - action(y) - m*a**2*T**3/6,
        "small_amplitude_limit": s.limit(m*a**2*T**3/6, a, 0),
        "oscillator_mode": -m*s.diff(mode, t, 2) - m*omega**2*mode
        - m*((n*s.pi/T)**2 - omega**2)*mode,
        "kernel_first_derivative": s.diff(multiplier, tau).subs(tau, 0)
        - (s.I*hbar/(2*m))*(-k**2),
        "density_trace": s.trace(difference),
        "density_square": s.trace(difference**2) - 2*(1-r**2),
        "relativistic_leading_action": s.integrate(m*s.diff(eta,t)**2/2, (t,0,T))
        - m*a**2*T**3/6,
    }
    for name, residual in checks.items():
        if s.simplify(residual) != 0:
            raise AssertionError(f"{name}: {residual}")

    numerical = {}
    for copies in (1, 2, 10, 100, 10000):
        for p in (0.6, 0.75, 0.95, 1.0):
            threshold = action_threshold(p, copies)
            actual = success_probability(threshold, copies)
            if not math.isclose(actual, p, abs_tol=2e-11):
                raise AssertionError((copies, p, threshold, actual))
        numerical[str(copies)] = action_threshold(0.75, copies)
    if not math.isclose(action_threshold(0.75, 1), math.pi/3, abs_tol=1e-14):
        raise AssertionError("one-copy threshold")
    if not all(success_probability(2*math.pi, N) == 0.5 for N in (1, 10, 100)):
        raise AssertionError("phase periodicity")
    if not all(action_threshold(1, N) == math.pi for N in (1, 10, 100)):
        raise AssertionError("perfect discrimination is exceptional")
    if not all(x > y for x,y in zip(list(numerical.values()), list(numerical.values())[1:])):
        raise AssertionError("finite-accuracy thresholds must decrease in this example")
    for invalid in (0, -1, 1.5, True):
        try:
            action_threshold(0.75, invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid copy count accepted")

    report = {
        "scope": "symbolic identities and finite numerical cross-checks, not formal certificates",
        "assumptions": "m,T,F,hbar > 0; matched endpoints; ideal quantum two-arm pure states; N independent copies",
        "symbolic_checks": {name: "passed" for name in checks},
        "numerical_checks": "threshold inversion, phase periodicity, perfect-discrimination endpoint, invalid copy counts",
        "threshold_over_hbar_at_p_0_75": numerical,
        "perfect_discrimination_threshold_over_hbar": math.pi,
    }
    output = Path(__file__).resolve().parents[1] / "out" / "action-gap-checks.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
