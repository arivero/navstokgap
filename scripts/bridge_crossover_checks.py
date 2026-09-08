"""Exact finite beta/count checks and numerical evaluation of the crossover."""
from pathlib import Path
import json
import sympy as s
import mpmath as mp


def main():
    q,z,T,u,rate,m = s.symbols("q z T u rate m", positive=True)
    checks = {}

    def record(name,residual):
        assert s.simplify(residual) == 0, (name,residual)
        checks[name] = "passed"

    for k in range(1,6):
        norm = s.factorial(2*k-1)/(2**(2*k-1)*s.factorial(k-1)**2)
        density = norm*(1+q)*(1-q*q)**(k-1)
        record(f"density_normalization_{k}", s.integrate(density,(q,-1,1))-1)
        record(f"midpoint_mean_{k}", s.integrate(q*density,(q,-1,1))-s.Rational(1,2*k+1))
        record(f"midpoint_second_moment_{k}", s.integrate(q*q*density,(q,-1,1))-s.Rational(1,2*k+1))
        sk = sum(1/(s.factorial(j)*s.factorial(j-1)*s.factorial(k-j)**2)
                 for j in range(1,k+1))
        record(f"count_sum_{k}", sk-k*s.factorial(2*k)/(2*s.factorial(k)**4))
        a,b = T*(1+q)/4,T*(1-q)/4
        joint = s.exp(-rate*T)*rate**(2*k+1)*a**k*b**(k-1)*sk/(2*u*u)
        endpoint = s.exp(-rate*T)*rate**(2*k+1)*(T/2)**(2*k)/(2*u*s.factorial(k)**2)
        record(f"density_jacobian_{k}", joint/endpoint*(u*T/2)-density)

    i0 = sum((z/2)**(2*k)/s.factorial(k)**2 for k in range(5))
    integral = s.integrate(i0,z)
    ratio = integral/(z*i0)
    record("weighted_moment_series", sum((z/2)**(2*k)/(s.factorial(k)**2*(2*k+1))
                                         for k in range(5))-integral/z)
    g = z*ratio*(1-ratio)
    record("cubic_onset", s.series(g,z,0,5).removeO()-z**3/6)
    K = s.symbols("K", positive=True)
    record("crossover_boundary", (m*u*u*T).subs(T,K/(m*u*u))-K)
    record("reference_rate_window", (K/(m*u*u)).subs(K,m*u*u/rate)-1/rate)

    mp.mp.dps = 40
    rows = []
    for value in ("0.25","0.5","1","2","4","8","32"):
        zz = mp.mpf(value)
        rz = mp.quad(lambda x: mp.besseli(0,x),[0,zz])/(zz*mp.besseli(0,zz))
        # Independent evaluation through the positive count-weight sum.
        weighted = mp.nsum(lambda k: (zz/2)**(2*k)/(mp.factorial(k)**2*(2*k+1)),[0,mp.inf])
        assert abs(rz-weighted/mp.besseli(0,zz)) < mp.mpf("1e-30")
        gg = zz*rz*(1-rz)
        assert 0 < gg <= zz/4
        rows.append({"z":float(zz),"R":float(rz),"kappa_over_plateau":float(gg),
                     "second_moment_action_over_plateau":float(zz*rz/2)})
    report = {"scope":"Finite identities and quadrature cross-checks; general proofs in notes/bridge-crossover.md",
              "exact_checks":checks,"quadrature_vs_count_series":rows}
    target = Path(__file__).resolve().parents[1]/"out"/"bridge-crossover-checks.json"
    target.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__ == "__main__":
    main()
