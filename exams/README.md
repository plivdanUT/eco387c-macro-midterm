# Macro I (ECO387C) midterm prep, Fall 2026

Exam format as known on 2026-10-06: closed book, no notes. Everything boxed in
the study packet has to be known cold.

## Files here

- `practice-packet.tex` / `.pdf`: the study packet. It goes through the class
  material in lecture order. Each part has a setup, then numbered derivation
  steps with every line of algebra, then 21 worked problems with full
  solutions.
- `practice-packet-checks.py` / `-checks.txt`: checks every number in the
  packet (closed forms, brute-force equilibria, a Bellman residual, Tauchen
  and Rouwenhorst matrices, a Working Monte Carlo). Rerun it before changing
  any number.
- `mock-midterm.tex` / `.pdf`: a mock exam, 4 questions of 25 points, each
  split into lettered parts. It is 13 pages, with answer space after every
  part (about 1.5 cm per point) and each question on a new page. `\needspace`
  keeps each prompt on the same page as its space. The solutions are a separate
  document, `mock-midterm-solutions.tex` / `.pdf` (15 pp.). They are written as
  a student's exam answers, with every step of work shown and no tutoring
  commentary.
  - Q1: PSet 6 extended to $\gamma = 2$ with asymmetric persistence
  - Q2: an anticipated income rise in the two-type endowment economy
    (Lecture 2, textbook Sec. 5.2.1)
  - Q3: the growth model by dynamic programming (textbook Examples 4.1 and
    4.6-4.8, Blackwell)
  - Q4: consumption (textbook Sec. 9.3.2-9.3.3: Hall, AR(1) income MPC,
    borrowing constraint, prudence)

  Numbers are checked in `mock-midterm-checks.py`. The draft textbook has no
  end-of-chapter exercises, so its numbered examples stand in.
- `mock-midterm-q1-writeup.tex` / `.pdf` (5 pp.): mock Question 1 written up
  in the same form as `assignments/pset-06-solutions`:
  - an Acknowledgment paragraph, then one section per part
  - lean displays, the example worked through, and the iid case
  - one TikZ figure of $\beta R$ against the stay probability for
    $\gamma = 1, 2$
  - Azzimonti cites (Sec. 7.1.2 p. 193, 7.5 p. 217, 7.6 pp. 218-219) and a
    Sources list
- `cheat-sheet.tex` / `.pdf` / `-print.pdf`: a memorization sheet, two sides
  when printed (`make-cheat-sheet.py` tiles it). You can't bring it into the
  exam. It is for drilling the night before.

Source material lives one level up:
- `lectures/lecture-0N_*.pdf`: handwritten lecture notes. Each has a `.md`
  transcription with page markers, and the page numbers below refer to them.
- `discussions/discussion-0N.pdf`: TA handouts (Kim and Yan).
- `assignments/pset-0N.pdf`: the problem sets, each with its own
  `-solutions.pdf`.
- `textbooks/Azzimonti-et-al-2024-Macro-Textbook.pdf`: section numbers below.

## Topic map

| # | Topic | Lecture | Discussion | PSet | Textbook | Packet |
|---|---|---|---|---|---|---|
| 1 | What macro is, history, Lucas critique | L1 pp. 1-7 | | | Ch. 1 | Part 1 |
| 2 | National accounts, identities, S = I, CPI biases | | D1 | | Sec. 2.1 | Part 2, WP 1-2 |
| 3 | Nominal to real budget, Fisher equation, why the budget binds | L2 pp. 1-2 | D2 Sec. 1.1 | | Sec. 5.3.1 | 3.2-3.3 |
| 4 | Household problem, CE definition, KKT conditions (1)-(9) | L2 pp. 3-5 | D2 Sec. 2.1 | PS2 Q1 | Sec. 5.2.1, 5.3.1 | 3.5-3.6 |
| 5 | Euler equation, TVC, intertemporal budget | L2 p. 5 | D2 Sec. 1.2 | PS2 Q1 | Sec. 4.2 | 3.6-3.7 |
| 6 | Equilibrium rate $1+r_t = Y_{t+1}/(\beta Y_t)$, allocations | L2 p. 6 | D2 Secs. 2.3-2.4 | PS2 Q1, PS3 Q2 | Sec. 5.2.1 | 3.8-3.9, WP 3-4 |
| 7 | Infinite horizon: Ponzi scheme, NPG, TVC implies NPG | L2 pp. 6-7 | | PS3 Q2 | Sec. 4.3.1 | 4.1-4.2 |
| 8 | Uncertainty: stochastic Euler, bond pricing with identical agents | L2 pp. 7-9 | | PS2 Q2, PS6 | Sec. 7.4-7.6 | 4.3-4.4, WP 5-6 |
| 9 | Log-linearization (3 methods, 6 rules) | | D3 Sec. 1 | PS3 Q3 | Sec. 7.3.4 | 5.1-5.3, WP 7 |
| 10 | Working's time-averaging problem | | D3 Sec. 2 | | | 5.4, WP 8 |
| 11 | Problem 1 vs Problem 2, sequence Euler, growth-planner example | L3 pp. 1-3 | D4 Sec. 2 | | Sec. 4.1, 4.3 | 6.1 |
| 12 | Bellman equation derivation, policy function, properties of V | L3 pp. 3-5 | D4 Sec. 2 | PS4, PS5 | Sec. 4.4.1-4.4.3 | 6.2-6.3 |
| 13 | Metric, contraction, Banach, Blackwell (and verifying it) | L3 pp. 5-9 | D4 Sec. 5 | PS4 bonus | Sec. 4.4.4 | 6.4 |
| 14 | Functional Euler equation by FOC plus envelope | L3 pp. 9-10 | D4 Sec. 2 | PS3 Q1, PS6 Q4 | Sec. 4.4.5 | 6.5, WP 9 |
| 15 | Guess and verify (log, $\delta=1$), VFI by hand analytically | | D4 Secs. 3-4 | PS3 Q1, PS4 Q1 | Ex. 4.7 | WP 10-12 |
| 16 | Stochastic consumption-saving: Bellman, envelope, Euler | L3 pp. 10-12 | D5 Sec. 1 | PS4 Q2, PS6 | Sec. 7.6 | WP 13 |
| 17 | VFI on a grid, the algorithm | | D5 Secs. 2-3 | PS4, PS5 | Sec. 4.4.4 | 7.1, WP 14 |
| 18 | Tauchen and Rouwenhorst | | D6 Sec. 2 | | Sec. 7.1.3 | 7.2, WP 15-16 |
| 19 | Stochastic growth VFI, deterministic steady state | | D6 Sec. 3 | | Sec. 7.3 | WP 9 |
| 20 | PIH, consumption smoothing, CRRA and IES | L4 pp. 1-3 | | | Sec. 9.3.1-9.3.2 | 8.1-8.2 |
| 21 | MPC: transitory about $r$, permanent equal to 1 | L4 pp. 3-5 | | | Sec. 9.3.2 | 8.3, WP 17 |
| 22 | RE errors, Hall random walk, tests (Shea, JPS 2006) | L4 pp. 5-9 | | | Sec. 9.3.2 | 8.4, WP 21 |
| 23 | Precautionary saving, prudence, Jensen picture | L4 pp. 9-11 | | | Sec. 9.3.4 | 8.5, WP 19 |
| 24 | Borrowing limits (ad hoc vs natural), KKT, MPC = 1, self-insurance | L4 pp. 11-14 | | | Sec. 9.3.3, 9.3.5 | 8.6, WP 18, 20 |

WP = worked problem in the packet.

The textbook column gives section numbers from the table of contents only.
The page-level cites in the pset solutions are the verified ones.

## Checklist

Tick each item off once you can do it from a blank page.

### Endowment economy
- [ ] Take the nominal budget to the real one and state the Fisher equation
- [ ] Argue why the budget constraint binds
- [ ] State the competitive equilibrium definition in full (taking prices as given, goods clearing, bonds clearing)
- [ ] Write the Lagrangian, derive FOCs (1)-(3), list KKT (4)-(9), and conclude $b_T = 0$
- [ ] Derive the intertemporal budget by telescoping
- [ ] Derive $1+r_t = Y_{t+1}/(\beta Y_t)$ from goods clearing plus the Euler equation
- [ ] Solve the two-period economy (Discussion 2) for $c_1$, $c_2$, $b$, $q$
- [ ] Solve the alternating economy with $n^A \ne n^B$
- [ ] Explain the Ponzi scheme, state NPG, and show TVC implies NPG with equality
- [ ] Derive the stochastic Euler equation and price the bond with identical agents (PSet 6)

### Log-linearization
- [ ] Use all three methods on Cobb-Douglas
- [ ] Derive the six rules, especially the share weights for sums
- [ ] Log-linearize the resource constraint, capital accumulation and the Euler equation
- [ ] Get Working's $\rho_1 = 1/6$ and show the skipped lag is uncorrelated

### Dynamic programming
- [ ] Go from Problem 1 to Problem 2, write the sequence Euler equation and TVC
- [ ] Do the growth model as Problem 2, with $\Gamma(k)$, $F_1$, $F_2$
- [ ] Derive the Bellman equation from the value function
- [ ] State the definitions: metric, sup norm, contraction, Banach, Blackwell
- [ ] Verify monotonicity and discounting for the Bellman operator
- [ ] Derive the VFI error bound $\beta^n d(V_0, V)$, and know the unbounded-$F$ caveat
- [ ] Derive the functional Euler equation by FOC plus envelope
- [ ] Guess and verify $E + F\ln k$, including the constant $E$
- [ ] Do VFI analytically from $V_0 = 0$ ($b_{n+1} = \alpha(1+\beta b_n)$)
- [ ] Solve cake eating with CRRA ($\theta = \beta^{1/\gamma}$)
- [ ] Do the stochastic consumption-saving Euler equation from the Bellman equation
- [ ] Do two VFI iterations on a 3-point grid by hand
- [ ] Compute a 3-state Tauchen row given $\Phi$ values
- [ ] Build Rouwenhorst $P_3$ and check its moments

### Consumption
- [ ] Derive the CRRA Euler equation in growth rates and the IES as an elasticity
- [ ] Derive the PIH consumption function and both MPCs
- [ ] Prove the three properties of RE errors
- [ ] Derive Hall's random walk via a first-order Taylor expansion, and know the test regression
- [ ] Describe the evidence: Shea, Johnson-Parker-Souleles, Kaplan-Violante
- [ ] Derive the precautionary-saving formula by second-order Taylor, and know quadratic vs CRRA
- [ ] Explain the Jensen picture
- [ ] Derive the natural borrowing limit
- [ ] Derive the constrained Euler equation via KKT, MPC = 1, and the supermartingale argument

## Things that look like typos in the lecture notes

These are flagged in the transcriptions. The packet uses the corrected form.

- L2 p. 2: the constraint-binding digression mixes dollars and goods. Divide by $p$.
- L2 p. 4: the present-value Lagrangian has $\beta$ where $\beta^t$ is meant.
- L2 p. 8: the objective under uncertainty should read $\sum_j \beta^j$.
- L3 p. 2: $i_t \le y_t + c_t$ should be $y_t - c_t$.
- L4 p. 4: $y^c_t$ inside the sum should be $y^c_{t+j}$.
- L4 p. 7: $\eta_t$ should be $\eta_{t+1}$.
- L4 p. 11: the natural-limit sum index ($k$ vs $j$).
- L4 p. 12: Case 1 condition should read $a_{t+1} > \underline a$.
