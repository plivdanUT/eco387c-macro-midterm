# Lecture 2: An Endowment Economy

ECO387C PhD Macro I, UT Austin. Handwritten notes dated Wednesday, August 26, 2026.

<!-- page 1 -->

## An endowment economy

### 1) Environment

- discrete time $t = 0, 1, 2, \ldots, T$ ($T$ circled, annotated "odd number")
- one good, perishable

**Households**

two types $e \in \{A, B\}$, get endowments $y_t^e$

| $e \backslash T$ | 0 | 1 | 2 | 3 | 4 | ... | $T$ |
|---|---|---|---|---|---|---|---|
| $A$ | 1 | 0 | 1 | 0 | 1 | ... | 0 |
| $B$ | 0 | 1 | 0 | 1 | 0 | ... | 1 |

- $n^A$ type $A$ HHs, $n^B$ type $B$ HH ("masses of agents")

**Preferences**

$$U_t = \sum_{t=0}^{T} \beta^t u(c_t^e)$$

($u(\cdot)$ annotated "flow utility", $c_t^e$ annotated "consumption", $\beta$ annotated "discount factor $\beta \in (0,1)$")

$$u(c) = \ln(c)$$
$$c_t^e \geq 0 \quad \forall t$$

[Graph: $u$ on vertical axis, $c$ on horizontal. Concave log curve, rising steeply from $-\infty$ near zero, crossing the horizontal axis at $c = 1$.]

$u' > 0$

- households can borrow or save $s_t^e$ ($> 0$: save, $< 0$: borrow)

face prices $p_t > 0$

time 0

$$\underbrace{p_0 c_0^e}_{\$\text{ cons.}} + \underbrace{s_0^e}_{\text{savings}} \leq \underbrace{p_0 y_0^e}_{\$\text{ income}}$$

(the $\leq$ is circled in red)

time $t > 0$

$$p_t c_t^e + s_t^e \leq \underbrace{p_t y_t^e}_{\text{income}} + s_{t-1}^e (1 + i_{t-1})$$

($i_{t-1}$ annotated "nominal interest rate")

<!-- page 2 -->

**Digression:**

Suppose inequality was strict "$<$" for some $\tilde{t}$ at solution $*$

$$p_t c_t^{e,*} + s_t^{e,*} < p_t y_t^e + s_{t-1}^{e,*}(1 + i_{t-1})$$

$$U_t^* = \sum_{t=0}^{\infty} \beta^t u(c_t^{e,*})$$

$$U_t^{**} = \sum_{\substack{t=0 \\ t \neq \tilde t}}^{\infty} \beta^t u(c_t^{e,*}) + \beta^{\tilde t} u(c_{\tilde t}^{e,**}) > U_t^* \quad \text{(contradiction)}$$

where

$$c_{\tilde t}^{e,**} = p_{\tilde t} y_{\tilde t}^e + s_{\tilde t-1}^{e,*}(1 + i_{\tilde t-1}) - s_{\tilde t}^{e,*} > c_{\tilde t}^{e*}$$

[possible typo: the right-hand side is in dollars, so presumably it should be divided by $p_{\tilde t}$. Also the sums run to $\infty$ although the horizon is $T$.]
---

**No Ponzi Game condition**

$$s_T^i \geq 0$$

"the HH cannot die in debt"

[Side box: $T \to \infty$]

$$\lim_{T \to \infty} \frac{1}{\prod_{t=0}^{T-1}(1 + i_t)} s_T \geq 0$$

---

$t = 0$

$$c_0^e + b_0^e \leq y_0^e \quad \text{where } b_0^e = \frac{s_0^e}{p_0}$$

($[s_0^e] = \$$, $[p_0] = \$/\text{basket}$, $[b_0^e] = \text{baskets}$)

$t > 0$

$$c_t^e + b_t^e \leq (1 + i_{t-1}) \cdot \frac{p_{t-1}}{p_t} \cdot b_{t-1}^e + y_t^e$$

$$c_t^e + b_t^e \leq y_t^e + b_{t-1}^e (1 + r_{t-1})$$

$$\pi_t = \frac{p_t - p_{t-1}}{p_{t-1}}$$

$$1 + \pi_t = \frac{p_t}{p_{t-1}}$$

$$\frac{1 + i_t}{1 + \pi_{t+1}} = 1 + r_t$$

"Fisher equation"

$$i_t = r_t + \pi_{t+1}$$

---

**Household problem:**

Taking interest rates $\{r_t\}_{t=0}^{T-1}$ as given, households solve the following problem:

<!-- page 3 -->

$$\max_{\{c_t^e, b_t^e\}_{t=0}^{T}} \sum_{t=0}^{T} \beta^t \ln(c_t^e)$$

$$c_t^e + b_t^e \leq y_t^e + (1 + r_{t-1}) b_{t-1}^e$$

with $b_{-1}^e = 0$

and $b_T^e \geq 0$

$(c_t^e \geq 0)$

[Colored side box: $\max \sum \beta^t \ln(c_t)$ s.t. budget cons. + nPg cond + $r(b_t)$ with "$+1$" written under it [illegible]]

---

**Equilibrium:**

A competitive equilibrium in this economy is a set of prices $\{r_t\}_{t=0}^{T-1}$ and a set of allocations $\{c_t^A, c_t^B, b_t^A, b_t^B\}_{t=0}^{T}$ such that

1) Taking $\{r_t\}_{t=0}^{T-1}$ as given (red annotation: "specifies market structure"), the allocations $\{c_t^A, c_t^B, b_t^A, b_t^B\}$ solve the HHs' optimization problems.

2) The goods market clears for $t = 0, \ldots, T$

$$\underbrace{n^A c_t^A + n^B c_t^B}_{\text{demand}} = \underbrace{n^A y_t^A + n^B y_t^B}_{\text{supply}}$$

(side note: $Y = C + \cancel{I} + \cancel{G} + \cancel{NX}$; below, a struck-through scribble "$\sum c$ '$\leq$' $p$(demand - supply) $\leq 0$", with $\sum Y$ under the supply side)

and the market for assets clears

$$n^A b_t^A + n^B b_t^B = 0$$

---

**Model Solution**

Solving the HHs' problem

$$\max_{\{c_t^e, b_t^e\}_{t=0}^{T}} \sum_{t=0}^{T} \beta^t \ln(c_t^e)$$

s.t.

$$y_t^e + (1 + r_{t-1}) b_{t-1}^e - c_t^e - b_t^e \geq 0$$
$$b_T^e \geq 0$$

$$\beta = \frac{1}{1 + \rho}$$

($\beta$: discount factor, $\rho$: discount rate, rate of time preference)

$$[\lambda] = \frac{\text{utils}}{\text{goods}}$$

<!-- page 4 -->

**Current-value Lagrangian**

$$\mathcal{L}^e = \sum_{t=0}^{T} \beta^t \left[ \ln c_t^e + \lambda_t^e \left( y_t^e + (1 + r_{t-1}) b_{t-1}^e - c_t^e - b_t^e \right) \right] + \mu_T^e b_T^e$$

$$\lambda_t^{e,PV} = \beta^t \lambda_t^e$$

$$\mathcal{L}^{PV} = \sum_{t=0}^{T} \beta \ln c_t^e + \sum_{t=0}^{T} \lambda_t^{e,PV} \left( \ldots \right) + \mu_T^e b_T^e$$

[possible typo: $\beta$ in the first sum of $\mathcal{L}^{PV}$ presumably should be $\beta^t$]

**F.O.N.C.**

$$\frac{\partial \mathcal{L}^e}{\partial c_t^e} = 0 \iff \beta^t \left( \frac{1}{c_t^e} - \lambda_t^e \right) = 0$$

$$\boxed{\frac{1}{c_t^e} = \lambda_t^e} \qquad e = A, B, \quad t = 0, 1, \ldots, T \qquad (1)$$

$$\frac{\partial \mathcal{L}^e}{\partial b_t^e} = 0 \overset{t < T}{\iff} -\beta^t \lambda_t^e + \beta^{t+1} \lambda_{t+1}^e (1 + r_t) = 0$$

$$\boxed{\lambda_t^e = \beta (1 + r_t) \lambda_{t+1}^e} \qquad t = 0, 1, \ldots, T-1 \qquad (2)$$

$t = T$:

$$\mu_T^e - \lambda_T^e \beta^T = 0$$

$$\boxed{\mu_T^e = \beta^T \lambda_T^e} \qquad (3)$$

1. constraints hold

$$y_t^e + (1 + r_{t-1}) b_{t-1}^e - c_t^e - b_t^e \geq 0 \quad \forall t = 0, \ldots, T \qquad (4)$$
$$b_T^e \geq 0 \qquad (5)$$

2. complementary slackness

$$\lambda_t^e \left( y_t^e + (1 + r_{t-1}) b_{t-1}^e - c_t^e - b_t^e \right) = 0 \qquad (6)$$
$$\mu_T^e b_T^e = 0 \qquad (7)$$

3. non-negativity

$$\lambda_t^e \geq 0 \quad t = 0, \ldots, T \qquad (8)$$

<!-- page 5 -->

$$\mu_T^e \geq 0 \qquad (9)$$

---

$c_t > 0 \Rightarrow \lambda_t > 0 \Rightarrow$ (8) satisfied, (4) holds with

flow / per-period budget constraint:

$$\boxed{c_t^e + b_t^e = y_t^e + (1 + r_{t-1}) b_{t-1}^e} \qquad (*)$$

(6) holds

$$\Rightarrow \mu_T^e = \beta^T \lambda_T^e > 0 \Rightarrow \text{(9) satisfied} \overset{(7)}{\Rightarrow} \boxed{b_T^e = 0} \Rightarrow \text{(5) satisfied}$$

Euler equation

$$\boxed{\frac{1}{c_t^e} = \beta (1 + r_t) \cdot \frac{1}{c_{t+1}^e}} \qquad (**)$$

$$b_{-1}^A = b_{-1}^B = 0$$
$$b_T^A = b_T^B = 0 \quad \text{transversality condition (TVC)}$$

---

boils down to 2 equations $(*)$, $(**)$ and two boundary conditions $b_{-1}^e = 0$, $b_T^e = 0$

$\to$ Solution consumption fn. $c_t = f(\{y_t, r_t\}_{t=0}^{T})$

---

**The intertemporal budget constraint**

$$b_t^e = y_t^e - c_t^e + b_{t-1}(1 + r_{t-1})$$

$$\underbrace{\sum_{t=0}^{T} \frac{1}{\prod_{\tau=0}^{t-1}(1 + r_\tau)} c_t}_{\text{life-time consumption}} = \underbrace{\sum_{t=0}^{T} \frac{1}{\prod_{\tau=0}^{t-1}(1 + r_\tau)} y_t}_{\text{life-time income}}$$

(the $=$ is circled)

---

**Some properties of the equilibrium**

from $(**)$: $c_{t+1}^e = \beta (1 + r_t) c_t^e$

<!-- page 6 -->

$$n^A y_t^A + n^B y_t^B = n^A c_t^A + n^B c_t^B$$
$$= n^A \frac{c_{t+1}^A}{\beta(1 + r_t)} + n^B \frac{c_{t+1}^B}{\beta(1 + r_t)}$$
$$= \frac{1}{\beta(1 + r_t)} \left( n^A c_{t+1}^A + n^B c_{t+1}^B \right)$$
$$= \frac{1}{\beta(1 + r_t)} \left( n^A y_{t+1}^A + n^B y_{t+1}^B \right)$$

$$1 + r_t = \frac{1}{\beta} \frac{n^A y_{t+1}^A + n^B y_{t+1}^B}{n^A y_t^A + n^B y_t^B}$$

$$1 + r_t = \begin{cases} \dfrac{1}{\beta} \dfrac{n^B}{n^A} & \text{if } t \text{ even} \\[2ex] \dfrac{1}{\beta} \dfrac{n^A}{n^B} & \text{if } t \text{ odd} \end{cases}$$

[Graph: $1 + r$ on vertical axis, $t$ on horizontal. A zigzag that oscillates up and down every period at a constant level above the axis.]

---

## Extensions

**Infinite horizon economies**

$T \to \infty$

Consider the following borrowing scheme:

- $t = 0$: borrow $b_0 = -x$, $x > 0$
- $t = 1$: borrow $b_1 = -x(1 + r_0)$
- $t = 2$: borrow $b_2 = -x(1 + r_0)(1 + r_1)$

<!-- page 7 -->

- $t = T$: borrow $b^T = -x \prod_{\tau=0}^{T-1}(1 + r_\tau)$

[Side box: this scheme violates the nPg condition!]

no Ponzi-game condition:

$$\lim_{T \to \infty} \frac{b_T}{\prod_{\tau=0}^{T-1}(1 + r_\tau)} \geq 0$$

---

**The corresponding TVC**

$$\lim_{T \to \infty} \beta^T \lambda_T b_T = 0$$

(colored annotation: $\beta^T \lambda_T$ "could replace with PV multiplier")

"at infinity (1) the present (2) value of asset holdings (3) is zero (4)" (numbered red markers link: (1) $\lim_{T \to \infty}$, (2) $\beta^T$, (3) $\lambda_T$, (4) $b_T = 0$)

Use (2):

$$\lambda_t = \frac{1}{\beta(1 + r_{t-1})} \lambda_{t-1}$$
$$= \ldots$$
$$= \frac{1}{\beta^t \prod_{\tau=0}^{t-1}(1 + r_\tau)} \lambda_0$$

$$\Rightarrow \lim_{T \to \infty} \beta^T \frac{1}{\beta^T \prod_{\tau=0}^{T-1}(1 + r_\tau)} \lambda_0 b_T = 0 \quad \Big) : \lambda_0$$

$\Rightarrow$ no Ponzi-game condition follows with "="

---

**Uncertainty**

$$y_t = \bar{y} + \varepsilon_t \qquad \varepsilon_t \overset{iid}{\sim} G(\varepsilon_t)$$
$$E[\varepsilon_t] = 0 \quad \forall t$$

HH becomes

<!-- page 8 -->

$$\max_{\{c_{t+j}, b_{t+j}\}_{t=0}^{\infty}} E_t \sum_{j=0}^{\infty} \beta^t \ln(c_{t+j})$$

[possible typo: the index set should be $j=0$ and the discount factor $\beta^j$, as in the Lagrangian below]

s.t.

(i) $$c_{t+j} + b_{t+j} \leq y_{t+j} + b_{t+j-1}(1 + r_{t+j-1})$$

(ii) nPg condition

and $(1 + r_{t-1}) b_{t-1} = 0$

$$\mathcal{L} = E_t \sum_{j=0}^{\infty} \beta^j \Big( \ln c_{t+j} + \lambda_{t+j} \big( y_{t+j} + (1 + r_{t+j-1}) b_{t+j-1} - c_{t+j} - b_{t+j} \big) \Big)$$

($\lambda_{t+j}$ annotated "current-value multiplier")

$$\frac{\partial \mathcal{L}}{\partial c_t} = 0 \iff E_t \left[ \frac{1}{c_t} - \lambda_t \right] = 0$$

$$E_t[\cdot] = E\left[ \cdot \mid \{y_{t-j}, r_{t-j}, b_{t-1-j}\}_{j=0,\ldots,t} \right]$$

$$\frac{1}{c_t} = \lambda_t$$

[Side note: TVC $\lim_{T \to \infty} \beta^T \lambda_T b_T = 0$; PV version $\lim_{T \to \infty} \lambda_T^{PV} b_T = 0$]

$$\frac{\partial \mathcal{L}}{\partial b_t} = 0 \qquad E_t\left[ \beta(1 + r_t) \lambda_{t+1} - \lambda_t \right] = 0$$

$$\Rightarrow \lambda_t = \beta(1 + r_t) E_t[\lambda_{t+1}]$$

($r_t$ underlined in red)

$$\frac{1}{c_t} = \beta(1 + r_t) E_t\left[ \frac{1}{c_{t+1}} \right]$$

<!-- page 9 -->

$$E_t\left[ \frac{1}{c_{t+1}} \right] = \int \frac{1}{c_{t+1}} g(\varepsilon_{t+1}) \, d\varepsilon_{t+1}$$
