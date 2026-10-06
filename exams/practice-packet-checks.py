"""Numerical checks for every number quoted in practice-packet.tex.
Run: ~/envs/econ/Scripts/python.exe practice-packet-checks.py > practice-packet-checks.txt
"""
import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq

np.set_printoptions(precision=4, suppress=True)
hr = lambda s: print("\n=== " + s)

hr("1. NIPA three approaches")
ore, steel, autos = 100, 250, 500
wages = [60, 100, 150]
va = [ore, steel - ore, autos - steel]
profits = [va[i] - wages[i] for i in range(3)]
print("value added", va, "sum", sum(va))
print("profits", profits, "income sum", sum(wages) + sum(profits))
print("expenditure C=400 + inventory 100 =", 400 + 100)

hr("2. Two-period endowment economy, yA=(3,1), yB=(1,1), beta=0.9")
b = 0.9
yA, yB = (3, 1), (1, 1)
Y1, Y2 = yA[0] + yB[0], yA[1] + yB[1]
q = b * Y1 / Y2
c1 = lambda y: (y[0] + q * y[1]) / (1 + b)
c2 = lambda y: b * (y[0] + q * y[1]) / (q * (1 + b))
bb = lambda y: y[0] - c1(y)
print("q", q, "1+r", 1 / q)
for n, y in (("A", yA), ("B", yB)):
    print(n, "c1", c1(y), "c2", c2(y), "b", bb(y), "check c2", y[1] + bb(y) / q)
print("clear t1", c1(yA) + c1(yB), "t2", c2(yA) + c2(yB), "bonds", bb(yA) + bb(yB))

hr("3. T-period alternating economy: brute-force Arrow-Debreu check")
def solve_alt(nA, nB, beta, T):
    t = np.arange(T + 1)
    yA = (t % 2 == 0).astype(float)
    yB = 1 - yA
    n = nB / nA
    qt = np.where(t % 2 == 0, beta ** t, beta ** t / n)
    # log utility: c_t = beta^t / (lambda q_t), lambda from IBC
    cA = beta ** t / qt * (qt @ yA) / beta ** t.sum() if False else None
    S = (beta ** t).sum()
    cA = beta ** t / qt * (qt @ yA) / S
    cB = beta ** t / qt * (qt @ yB) / S
    return t, cA, cB, nA * cA + nB * cB - (nA * yA + nB * yB), qt
for nA, nB in ((1, 1), (1, 2)):
    t, cA, cB, ex, qt = solve_alt(nA, nB, 0.9, 7)
    print(f"nA={nA} nB={nB}: cA", cA, "cB", cB, "excess", np.abs(ex).max())
    print("  1+r_t", qt[:-1] / qt[1:])
beta = 0.9; n = 2
print("formula cA_even", 1 / (1 + beta), "cA_odd", n / (1 + beta),
      "cB_even", beta / (n * (1 + beta)), "cB_odd", beta / (1 + beta))

hr("4. Stochastic endowment: R(y) = u'(y)/(beta E[u'(y')|y])")
beta, p = 0.96, 0.9
Rh = 1 / (beta * (2 - p)) ; Rl = 2 / (beta * (1 + p))
print("Markov log yh=2 yl=1: Rh", Rh, "Rl", Rl, "1/beta", 1 / beta)
print("check Rh", (1 / 2) / (beta * (p / 2 + (1 - p) / 1)))
Eu = 0.5 * (1 / 1) + 0.5 * (1 / 2)
print("iid 1/2: R(2)", 0.5 / (beta * Eu), "=2/(3b)", 2 / (3 * beta), "R(1)", 1 / (beta * Eu), "=4/(3b)", 4 / (3 * beta))

hr("5. Log-linearization: finite-difference check of the resource constraint")
C, I = 0.8, 0.2
Y = C + I
eps = 1e-4
Ch, Ih = 0.01, -0.02
exact = np.log((C * np.exp(Ch) + I * np.exp(Ih)) / Y)
print("exact", exact, "approx", C / Y * Ch + I / Y * Ih)

hr("6. Working time averaging, Monte Carlo")
rng = np.random.default_rng(387)
e = rng.standard_normal(2_000_000)
c = np.cumsum(e)
x = (c[1:] + c[:-1]) / 2
xs = x[::2]
u = np.diff(xs)
print("Var u", u.var(), "(theory 1.5)  corr lag1", np.corrcoef(u[1:], u[:-1])[0, 1], "(theory 1/6)")
print("u_{t+1} vs u_{t-3} (two observations apart)", np.corrcoef(u[2:], u[:-2])[0, 1], "(theory 0)")

hr("7. Growth model closed form and analytic VFI, alpha=0.3 beta=0.6")
a, beta = 0.3, 0.6
F = a / (1 - a * beta)
E = (np.log(1 - a * beta) + a * beta / (1 - a * beta) * np.log(a * beta)) / (1 - beta)
print("F", F, "E", E, "policy k'=", a * beta, "k^a")
k = np.linspace(0.05, 0.5, 7)
V = E + F * np.log(k)
grid = np.linspace(1e-6, 1, 200001)
resid = []
for ki in k:
    cc = ki ** a - grid
    ok = cc > 0
    rhs = np.log(cc[ok]) + beta * (E + F * np.log(grid[ok]))
    resid.append(rhs.max())
print("Bellman residual", np.abs(np.array(resid) - V).max())
bn = 0.0
for nn in range(1, 6):
    s = beta * bn / (1 + beta * bn)
    bn = a * (1 + beta * bn)
    print(f"iter {nn}: savings rate used {s:.5f}, b_{nn} = {bn:.5f}")
print("limit b", F, "limit savings rate", a * beta)
kss = (a * beta) ** (1 / (1 - a))
print("steady state k (delta=1)", kss)

hr("8. Grid VFI by hand, grid {0.1,0.2,0.3}, alpha=0.3, beta=0.6")
G = np.array([0.1, 0.2, 0.3])
Vn = np.zeros(3)
for it in (1, 2):
    M = np.log(G[:, None] ** a - G[None, :]) + beta * Vn[None, :]
    print(f"iteration {it}: RHS matrix (row k, col k')\n", M.round(4))
    Vn = M.max(1); g = G[M.argmax(1)]
    print("  V =", Vn.round(4), " g =", g)
print("k^a", (G ** a).round(4))
print("logs:", {f"{kk:.1f}->{kp:.1f}": round(float(np.log(kk**a-kp)), 4) for kk in G for kp in G})

hr("9. Cake eating CRRA gamma=2 beta=0.95")
gam, beta = 2.0, 0.95
th = beta ** (1 / gam)
print("theta", th, "consumption share 1-theta", 1 - th)

hr("10. Tauchen N=3, rho=0.9, sigma=0.1, m=1, zbar=0")
rho, sig, m = 0.9, 0.1, 1.0
sz = sig / np.sqrt(1 - rho ** 2)
z = np.array([-m * sz, 0, m * sz]); w = z[1] - z[0]
P = np.zeros((3, 3))
for j in range(3):
    mu = rho * z[j]
    P[j, 0] = norm.cdf((z[0] + w / 2 - mu) / sig)
    P[j, 2] = 1 - norm.cdf((z[2] - w / 2 - mu) / sig)
    P[j, 1] = 1 - P[j, 0] - P[j, 2]
print("sigma_z", sz, "grid", z, "w", w)
for j in range(3):
    mu = rho * z[j]
    print(f" row {j+1}: cut args lo {(z[0]+w/2-mu)/sig:.4f}, hi {(z[2]-w/2-mu)/sig:.4f}")
print(P.round(4))
pi = np.linalg.matrix_power(P.T, 500)[:, 0]
print("stationary", pi.round(4), "sd", np.sqrt(pi @ z ** 2), "vs", sz)
print("implied autocorr", (pi * z) @ (P @ z) / (pi @ z ** 2))

hr("11. Rouwenhorst N=3 rho=0.9 sigma=0.1")
pp = (1 + rho) / 2
def rouw(n, p, q):
    Pm = np.array([[p, 1 - p], [1 - q, q]])
    for k in range(3, n + 1):
        Z = np.zeros((k, k))
        Z[:-1, :-1] += p * Pm; Z[:-1, 1:] += (1 - p) * Pm
        Z[1:, :-1] += (1 - q) * Pm; Z[1:, 1:] += q * Pm
        Z[1:-1] /= 2
        Pm = Z
    return Pm
P3 = rouw(3, pp, pp)
v = np.sqrt(2) * sz
zr = np.array([-v, 0, v])
print("p", pp, "v", v); print(P3.round(4))
pi = np.linalg.matrix_power(P3.T, 2000)[:, 0]
print("stationary", pi.round(4), "var", pi @ zr ** 2, "vs sz^2", sz ** 2)
print("E[z'|z=v]", P3[2] @ zr, "= rho v", rho * v)

hr("12. Consumption: MPCs and limits")
r = 0.04; R = 1 + r
print("beta R=1 transitory mpc exact r/(1+r)", r / R)
beta, s = 0.95, 0.5
print("beta=0.95 r=0.04 sigma=0.5: mpc", 1 - (R * beta) ** s / R)
print("permanent: (1-1/R)*R/r", (1 - 1 / R) * R / r)
print("natural limit ymin=0.5:", -R / r * 0.5)
print("relative prudence log", 1 + 1 / 1.0, "approx growth with sd 5%:", (1 + 1) / 2 * 0.05 ** 2)
# exact two-point check for log, beta R = 1: u'(c_t) = E u'(c_t(1+g)), g = +-0.05
gt = brentq(lambda mu: 1 - 0.5 * (1 / (1 + mu + 0.05) + 1 / (1 + mu - 0.05)), -0.01, 0.01)
print("exact mean growth needed, log, +-5%:", gt)
print("borrowing-constrained: c1=1 c2=3 mu =", 1 - 1 / 3)
