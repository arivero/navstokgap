"""Finite-state identities and observability bounds supporting G01 proofs."""
from pathlib import Path
import json
import sympy as s


def main():
    lam, eps, u, m = s.symbols("lam eps u m", positive=True)
    X, I = s.Matrix([[0, 1], [1, 0]]), s.eye(2)
    Q = lam*s.kronecker_product(X-I, I)+eps*s.kronecker_product(I, X-I)
    basis = s.Matrix([[1, 1, 1, 1], [1, 1, -1, -1],
                      [1, -1, 1, -1], [1, -1, -1, 1]]).T
    rates = s.diag(0, 2*lam, 2*eps, 2*(lam+eps))
    centered = basis[:, 1:]
    inv = s.diag(1/(2*lam), 1/(2*eps), 1/(2*(lam+eps)))
    projector = s.eye(4)-s.ones(4)/4
    full_inverse = centered*inv*centered.T/4
    velocity = u*basis[:, 1]
    H = (2*m*velocity.T*full_inverse*velocity/4)[0]
    frame = u*u*centered*centered.T/4
    total = u*u*s.trace(inv)
    residuals = {
        "row_sums": Q*s.ones(4, 1),
        "detailed_balance": Q-Q.T,
        "orthonormal_basis": basis.T*basis/4-s.eye(4),
        "four_eigenmodes": -Q*basis-basis*rates,
        "centered_inverse": -Q*full_inverse-projector,
        "unchanged_velocity_plateau": H-m*u*u/lam,
        "two_state_product": (m*u*u/lam)*(2*lam)-2*m*u*u,
        "full_observable_frame": frame-u*u*projector,
        "frame_trace_identity": s.trace(full_inverse*frame)-total,
        "positive_hidden_rate_gap_limit": s.limit(2*eps, eps, 0),
        "fixed_plateau_hidden_limit": s.limit(H, eps, 0)-m*u*u/lam,
    }
    for name, residual in residuals.items():
        values = list(residual) if isinstance(residual, s.MatrixBase) else [residual]
        assert all(s.simplify(v) == 0 for v in values), name

    examples = []
    for lv, ev in ((1, 1), (3, 1), (1, 3), (2, s.Rational(1, 10)),
                   (2, s.Rational(1, 1000))):
        substitutions = {lam: lv, eps: ev, u: 1, m: 1}
        gap = 2*min(lv, ev)
        susceptibility = total.subs(substitutions)
        lower = 1/susceptibility
        plateau = H.subs(substitutions)
        assert 0 < lower <= gap <= 2/plateau
        examples.append({"lambda": str(lv), "epsilon": str(ev),
                         "gap": str(gap), "frame_lower_bound": str(lower),
                         "velocity_plateau": str(plateau)})
    # Nonuniform stationary law: reversibility uses weighted, not Euclidean, adjoint.
    q = s.Matrix([[-2, 2, 0], [1, -3, 2], [0, 1, -1]])
    weight = s.diag(s.Rational(1, 7), s.Rational(2, 7), s.Rational(4, 7))
    assert weight*q == q.T*weight
    f = s.Matrix([2, -1, 0])
    one = s.ones(3, 1)
    pirow = one.T*weight
    poisson = (-q+one*pirow).inv()*f
    chi = (f.T*weight*poisson)[0]
    assert pirow*f == s.zeros(1, 1)
    assert -q*poisson == f and pirow*poisson == s.zeros(1, 1)
    assert chi > 0
    report = {"scope": "Exact finite checks; general bounds proved in notes/susceptibility-gap.md",
              "identities": {name: "passed" for name in residuals},
              "gap_bound_examples": examples,
              "nonuniform_reversible_checks": 4,
              "nonuniform_susceptibility": str(chi)}
    target = Path(__file__).resolve().parents[1]/"out"/"susceptibility-gap-checks.json"
    target.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
