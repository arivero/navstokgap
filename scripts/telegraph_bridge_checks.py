"""Exact finite checks for the density-disintegrated telegraph return bridge."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sp


def main():
    a, T, u, rate = sp.symbols("a T u rate", positive=True)
    checks = {}
    for k in range(5):
        density = sp.factorial(2*k+1)*a**k*(T-a)**k / (
            sp.factorial(k)**2*T**(2*k+1))
        checks[f"beta_normalization_{k}"] = sp.integrate(density, (a, 0, T))-1
        poisson = sp.exp(-rate*T)*(rate*T)**(2*k+1)/sp.factorial(2*k+1)
        target = sp.exp(-rate*T)*rate**(2*k+1)*(T/2)**(2*k) / (
            2*u*sp.factorial(k)**2)
        checks[f"return_density_{k}"] = poisson*density.subs(a, T/2)/(2*u)-target
    z = sp.symbols("z", positive=True)
    series = sum((z/2)**(2*k)/sp.factorial(k)**2 for k in range(6))
    weighted = sum((2*k+1)*(z/2)**(2*k)/sp.factorial(k)**2 for k in range(6))
    checks["count_series_derivative"] = weighted-series-z*sp.diff(series, z)
    checks["one_switch_density"] = sp.exp(-rate*T)*rate/(2*u)-(
        sp.exp(-rate*T)*rate*T/T/(2*u))
    for name, value in checks.items():
        assert sp.simplify(value) == 0, (name, value)

    # m=u=T=1. Each tuple interleaves positive and negative durations,
    # with each sign total exactly 1/2. All computations use rational numbers.
    paths = [(Q(1,2), Q(1,2)),
             (Q(1,6), Q(1,3), Q(1,3), Q(1,6)),
             (Q(1,8), Q(1,6), Q(1,8), Q(1,6), Q(1,4), Q(1,6))]
    cases = 0
    for durations in paths:
        assert sum(durations[::2]) == sum(durations[1::2]) == Q(1,2)
        switches = [sum(durations[:j]) for j in range(1, len(durations))]

        def position(t):
            start, x = Q(0), Q(0)
            for j, length in enumerate(durations):
                x += (-1)**j*min(length, max(Q(0), t-start))
                start += length
            return x

        assert position(Q(1)) == 0
        for n in range(1, 16):
            coarse = [Q(j,n) for j in range(n+1)]
            fine = sorted(set(coarse + [Q(1,7), Q(3,8), Q(5,6)]))

            def action(cuts):
                return sum((position(b)-position(a))**2/(2*(b-a))
                           for a,b in zip(cuts, cuts[1:]))

            sc, sf = action(coarse), action(fine)
            assert 0 <= sc <= sf <= Q(1,2)
            assert Q(1,2)-sc <= Q(len(switches), 2*n)
            assert action(sorted(set(coarse+switches))) == Q(1,2)
            retained = {t: position(t) for t in fine if t in coarse}
            assert retained == {t: position(t) for t in coarse}
            cases += 1
    # On the one-switch component, symmetric endpoint-window offsets put
    # the switch on either side of the midpoint. Exact equality uses post-jump -1.
    offsets = [Q(-1,100), Q(1,100)]
    velocities = [1 if Q(1,2) < (1+x)/2 else -1 for x in offsets]
    assert sorted(velocities) == [-1, 1]
    exact_switch = Q(1,2)
    assert (1 if Q(1,2) < exact_switch else -1) == -1
    report = {"scope": "Finite algebra and rational path examples; general proofs in the maintained note",
              "symbolic_checks": {name: "passed" for name in checks},
              "rational_partition_cases": cases,
              "velocity_window_and_exact_convention": "passed"}
    output = Path(__file__).resolve().parents[1]/"out"/"telegraph-bridge-checks.json"
    output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
