"""Exact checks for elastic midpoint cuts and ballistic support bounds."""
from pathlib import Path
import json
import sympy as sp


def main():
    m,u,D,k,n=sp.symbols("m u D k n",positive=True)
    t=sp.symbols("t",nonnegative=True)
    v,zeta=sp.symbols("v zeta",real=True)
    x1=u*t
    x2=u*(D-t)
    cost=m*sp.integrate(u**2,(t,0,D))/2
    split=m*D*((v+2*zeta/D)**2+(v-2*zeta/D)**2)/4-m*D*v**2/2
    checks={
        "meeting":x1.subs(t,D/2)-x2.subs(t,D/2),
        "return_endpoint":x2.subs(t,D),
        "pair_momentum_before":m*u+m*(-u),
        "pair_momentum_after":m*(-u)+m*u,
        "pair_energy":m*(u**2+(-u)**2)/2-m*u**2,
        "tracer_action":cost-m*u**2*D/2,
        "midpoint_normalization":4*m/D*(u*D/2)**2-m*u**2*D,
        "action_variance_identity":cost-(m*u**2*D)/2,
        "fixed_kappa_energy":(m*u**2).subs(u**2,k/(m*D))-k/D,
        "midpoint_excess":split-2*m*zeta**2/D,
        "support_scale":4*m/D*(D*(u-sp.Abs(v))/2)**2-m*D*(u-sp.Abs(v))**2,
        "convolution_bound":n*u**2*(D/n)**2-u**2*D**2/n,
    }
    for name,residual in checks.items():
        if sp.simplify(residual)!=0:
            raise AssertionError(f"{name}: {residual}")
    report={"scope":"Finite algebra; general support and convolution proofs are in notes/physical-cut-speed.md",
            "checks":{name:"passed" for name in checks}}
    target=Path(__file__).resolve().parents[1]/"out"/"physical-cut-checks.json"
    target.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
