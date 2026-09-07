"""Exact finite checks for the repeated elastic collision model."""
from pathlib import Path
import json
import sympy as sp


def main():
    m, M, nu, s2, t, eps = sp.symbols("m M nu s2 t eps", positive=True)
    v, w = sp.symbols("v w", real=True)
    S0 = sp.symbols("S0", nonnegative=True)
    a = (m-M)/(m+M)
    b = 2*M/(m+M)
    vp, wp = a*v+b*w, 2*m*v/(m+M)-a*w
    gamma, beta = nu*(1-a), nu*(1-a**2)
    Seq = M*s2/m
    H = (m+M)*s2/nu
    St = Seq+(S0-Seq)*sp.exp(-beta*t)
    At = 2*m*St/gamma
    checks = {
        "momentum": m*vp+M*wp-m*v-M*w,
        "kinetic_energy": m*vp**2+M*wp**2-m*v**2-M*w**2,
        "convex_weights": a+b-1,
        "stationary_variance": b**2*s2/(1-a**2)-Seq,
        "variance_fixed_point": a**2*Seq+b**2*s2-Seq,
        "correlation_rate": gamma-2*nu*M/(m+M),
        "variance_rate": beta-4*nu*m*M/(m+M)**2,
        "plateau": 2*m*Seq/gamma-H,
        "variance_ode": sp.diff(St,t)+beta*(St-Seq),
        "action_ode": sp.diff(At,t)+beta*(At-H),
        "initial_variance": St.subs(t,0)-S0,
        "rest_preparation": At.subs(S0,0)-H*(1-sp.exp(-beta*t)),
        "bath_scaling": H.subs(s2,eps**2*s2)-eps**2*H,
        "equal_mass_plateau": H.subs(m,M)-2*M*s2/nu,
    }
    g, d, r = sp.symbols("g d r", positive=True)
    window = sp.integrate(1-sp.exp(-g*(d-r)), (r,0,d))
    checks["stationary_window"] = window/d-(1-(1-sp.exp(-g*d))/(g*d))
    for name, residual in checks.items():
        if sp.simplify(residual) != 0:
            raise AssertionError(f"{name}: {residual}")
    report = {
        "scope": "Finite identities; contraction and limiting arguments are written in the paper",
        "assumptions": "m >= M > 0; positive collision rate and bath variance; centered independent bath",
        "checks": {name:"passed" for name in checks},
        "analytic_review_required": ["invariant-law existence and uniqueness", "bounded-speed collision stream",
                                     "conditional covariance", "finite-window and long-duration limits"],
    }
    target = Path(__file__).resolve().parents[1]/"out"/"collision-action-checks.json"
    target.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__ == "__main__":
    main()
