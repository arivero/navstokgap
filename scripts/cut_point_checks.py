"""Exact checks for arbitrary cut points and Gaussian refinement consistency."""
from pathlib import Path
import json
import sympy as sp


def main():
    m,F,a,b,t,T,k,d,s=sp.symbols("m F a b t T k d s",positive=True)
    x,y,z=sp.symbols("x y z",real=True)
    eta=F*t*(a-t)/(2*m)
    mean=(b*x+a*z)/(a+b)
    cost=m*((y-x)**2/a+(z-y)**2/b-(z-x)**2/(a+b))/2
    checks={
        "interval_action":sp.integrate(m*sp.diff(eta,t)**2/2,(t,0,a))-F**2*a**3/(24*m),
        "split_cubic":(a+b)**3-a**3-b**3-3*a*b*(a+b),
        "equal_partition":d*(T/d)**3-T**3/d**2,
        "split_kinetic":cost-m*(a+b)*(y-mean)**2/(2*a*b),
        "conditional_extra_mean":m*(a+b)/(2*a*b)*k*a*b/(m*(a+b))-k/2,
        "estimator_mean":2/d*(d*k/2)-k,
        "estimator_variance":(2/d)**2*(d*k**2/2)-2*k**2/d,
        "retained_variance":s-s**2/T-s*(T-s)/T,
    }
    # Schur complement eliminates a newly inserted node from free precision.
    A=m*sp.Matrix([[1/a+1/b,-1/b],[-1/b,1/b+1/T]])
    checks["schur_complement"]=A[1,1]-A[1,0]*A[0,1]/A[0,0]-m*(1/(a+b)+1/T)
    for name,residual in checks.items():
        if sp.simplify(residual)!=0:
            raise AssertionError(f"{name}: {residual}")
    report={"scope":"Finite identities; general limit and consistency proofs in notes/cut-point-consistency.md",
            "checks":{name:"passed" for name in checks}}
    target=Path(__file__).resolve().parents[1]/"out"/"cut-point-checks.json"
    target.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
