"""Checks every number in mock-midterm.tex.
Run: ~/envs/econ/Scripts/python.exe mock-midterm-checks.py > mock-midterm-checks.txt
"""
import numpy as np

hr = lambda s: print("\n=== " + s)

hr("Q1 Markov endowment, CRRA gamma=2")
b, ph, pl, g = 0.95, 0.8, 0.6, 2.0
up = lambda c: c ** (-g)
Rh = up(2) / (b * (ph * up(2) + (1 - ph) * up(1)))
Rl = up(1) / (b * (pl * up(1) + (1 - pl) * up(2)))
print("Rh", Rh, "formula", 1 / (b * (4 - 3 * ph)))
print("Rl", Rl, "formula", 4 / (b * (1 + 3 * pl)))
print("1/beta", 1 / b)
Rh1 = 1 / (b * (2 - ph)); Rl1 = 1 / (b * (pl + (1 - pl) / 2))
print("log case Rh", Rh1, "Rl", Rl1)
# iid: ph = 1 - pl
ph2, pl2 = 0.4, 0.6
Eu = ph2 * up(2) + (1 - ph2) * up(1)
print("iid ph=0.4: Rh", up(2) / (b * Eu), "Rl", up(1) / (b * Eu), "ratio Rl/Rh", up(1) / up(2))

hr("Q2 anticipated rise, beta=0.9, brute force over long horizon")
beta = 0.9
T = 400
t = np.arange(T)
yA = np.ones(T); yB = np.where(t == 0, 1.0, 2.0)
Y = yA + yB
p = beta ** t * Y[0] / Y
for name, y in (("A", yA), ("B", yB)):
    W = p @ y
    c0 = (1 - beta) * W
    c = beta ** t * c0 / p
    print(name, "W", W, "c0", c0, "c1", c[1], "c5", c[5])
cA0 = 1 - beta / 3; cB0 = 1 + beta / 3
print("closed forms cA0", cA0, "cB0", cB0, "cA1", 1.5 * cA0, "cB1", 1.5 * cB0)
R = np.r_[Y[1:] / (beta * Y[:-1])]
print("1+r_0", R[0], "1+r_1", R[1])
# bonds for A
bA = []; bprev = 0.0
cA = beta ** t * cA0 / p
for s in range(6):
    Rprev = R[s - 1] if s > 0 else 0.0
    bnow = yA[s] + Rprev * bprev - cA[s]
    bA.append(bnow); bprev = bnow
print("bA", np.round(bA, 6), "beta/3", beta / 3, "beta/2", beta / 2)

hr("Q3 growth model alpha=0.3 beta=0.95 A=1")
a, beta, A = 0.3, 0.95, 1.0
s = a * beta
kss = (s * A) ** (1 / (1 - a))
print("s", s, "kss", kss, "css", A * kss ** a - kss, "yss", A * kss ** a)
print("iteration-2 saving rate", a * beta / (1 + a * beta))
print("half-life periods", np.log(0.5) / np.log(a))
k0 = kss / 2
print("k0 = kss/2: khat0", np.log(k0 / kss), "khat1", a * np.log(k0 / kss),
      "exact k1", s * A * k0 ** a, "-> khat1 exact", np.log(s * A * k0 ** a / kss))

hr("Q4 consumption, r=0.04")
r = 0.04
for rho in (0.0, 0.9, 1.0):
    print(f"rho={rho}: dc/eps = r/(1+r-rho) =", r / (1 + r - rho))
ybar, yt, at = 1.0, 0.5, 0.0
cu = r / (1 + r) * (at + yt) + ybar / (1 + r)
print("unconstrained c", cu, "cash on hand", at + yt, "implied a'", (1 + r) * (at + yt - cu))
print("natural limit ymin=0.5", -(1 + r) / r * 0.5)
