"""Five exact coefficient checks; general proofs in the composition note."""
from pathlib import Path
import json
import sympy as s


def main():
    a,b,D,k1,k2,B,v,rate = s.symbols("a b D k1 k2 B v rate", positive=True)
    M, mu = a+b, a*b/(a+b)
    variances = s.diag(k1*D/a, k2*D/b)
    transform = s.Matrix([[a/M, b/M], [1, -1]])
    cov = transform*variances*transform.T
    cm, rel = M*cov[0,0]/D, mu*cov[1,1]/D
    bath = lambda mass: (mass+B)*v**2/rate
    residuals = {
        "centre_coefficient": cm-(a*k1+b*k2)/M,
        "relative_coefficient": rel-(b*k1+a*k2)/M,
        "sum_rule": cm+rel-k1-k2,
        "cross_covariance": cov[0,1]-D*(k1-k2)/M,
        "bath_discrepancy": bath(M)-(a*bath(a)+b*bath(b))/M-2*a*b*v**2/(rate*M),
    }
    for name,residual in residuals.items():
        assert s.simplify(residual) == 0, (name,residual)
    report = {"scope": "Five finite algebra checks; not a formal certificate of the general theorems",
              "checks": {name: "passed" for name in residuals}}
    target = Path(__file__).resolve().parents[1]/"out"/"composition-checks.json"
    target.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
