# Consumption

*ECO387C Macro I, lecture 4 (handwritten notes dated Wednesday, September 16, 2026)*

<!-- page 1 -->

## The Permanent Income Hypothesis under rational expectations

$$\max_{\{c_t,\,a_{t+1}\}_{t=0}^{\infty}} \sum_{t=0}^{\infty} \beta^t u(c_t) \qquad u' \geq 0, \quad u'' < 0$$

$$c_t + \frac{a_{t+1}}{1+r_t} = y_t + a_t$$

NPG condition
$$\lim_{T\to\infty} \frac{a_{T+1}}{\prod_{\tau=0}^{T-1}(1+r_\tau)} \geq 0$$

$a_0$ given

FOCs give Euler equation
$$u'(c_t) = \beta(1+r_t)\,u'(c_{t+1}) \qquad \forall t$$

also have ITBC
$$\underbrace{\sum_{j=0}^{\infty} \frac{1}{\prod_{k=0}^{j-1}(1+r_{t+k})}\,c_{t+j}}_{\text{life-time consumption}} = \underbrace{\underbrace{\sum_{j=0}^{\infty} \frac{1}{\prod_{k=0}^{j-1}(1+r_{t+k})}\,y_{t+j}}_{\text{life-time income}} + a_t}_{\text{life-time wealth}}$$

---

## Euler equation, consumption smoothing, and intertemporal substitution

Assume $\beta(1+r_t) = 1$
$$\Rightarrow \quad u'(c_t) = u'(c_{t+1}) \quad \overset{u''<0}{\Longrightarrow} \quad c_t = c_{t+1} \qquad \text{consumption smoothing}$$

[Graph: concave $u$ plotted against $c$, with a chord between two points on the curve.]

<!-- page 2 -->

[Graph: lower panel, $u'$ against $c$ with $0$ marked on the vertical axis, a downward-sloping $u'$ curve plus a red U-shaped curve and red dashed vertical line at their intersection.]

---

Consider constant relative risk aversion
$$u(c) = \frac{c^{1-\frac{1}{\sigma}}}{1-\frac{1}{\sigma}} \qquad \sigma > 0$$

$\sigma$: intertemporal elasticity of substitution

$\frac{1}{\sigma}$: coefficient of relative risk aversion
$$\frac{1}{\sigma} := -\frac{u''(c)\,c}{u'(c)}$$
$$u'(c) = c^{-\frac{1}{\sigma}}$$

EE $\Rightarrow$
$$c_t^{-\frac{1}{\sigma}} = \beta(1+r_t)\,c_{t+1}^{-\frac{1}{\sigma}}$$
$$\frac{c_{t+1}}{c_t} = \left[\beta(1+r_t)\right]^{\sigma}$$

- $\beta(1+r_t) = 1 \;\Rightarrow\; \dfrac{c_{t+1}}{c_t} = 1$
- $\beta(1+r_t) > 1 \;\Rightarrow\; \dfrac{c_{t+1}}{c_t} > 1$ (highlighted)
- $\beta(1+r_t) < 1 \;\Rightarrow\; \dfrac{c_{t+1}}{c_t} < 1$

$$\beta = \frac{1}{1+\rho} \qquad \beta: \text{discount factor}, \quad \rho: \text{rate of time preference}$$

$$\frac{1+r_t}{1+\rho} > 1$$

<!-- page 3 -->

$$\Leftrightarrow\; r_t > \rho$$

EE $\Rightarrow$
$$\ln \frac{c_{t+1}}{c_t} = \sigma \cdot \underbrace{\ln(1+r_t)} + \sigma \ln \beta$$

$$\frac{\partial \ln \frac{c_{t+1}}{c_t}}{\partial \ln(1+r_t)} = \sigma$$

def. of IES $\to$ intertemporal elasticity of substitution (note with arrow: nondurable, perishable goods)

Estimates: $\sigma \in [0.1,\, 0.5]$

$$\Delta \frac{c_{t+1}-c_t}{c_t} = \sigma \cdot \Delta r_t \qquad \Delta \ln(1+r_t) \approx \Delta r_t$$

[Graph: $\ln(1+r_t)$ against $1+r_t$, concave log curve crossing zero with a nearly coincident straight line through the crossing point.]

---

## The marginal propensity to consume in the PIH model

$$\text{mpc} := \frac{\partial c_t}{\partial y_t} \qquad \text{notice: not logs}$$

$R = 1+r = \text{const}$

ITBC:
$$\sum_{j=0}^{\infty} \frac{1}{R^j}\,c_{t+j} = a_t + \sum_{j=0}^{\infty} \frac{1}{R^j}\,y_{t+j}$$

EE: (arrow to $c_{t+j}$ in the ITBC)

<!-- page 4 -->

$$c_{t+j} = (R\beta)^{\sigma} c_{t+j-1} = \left((R\beta)^{\sigma}\right)^{j} c_t$$

$$\Rightarrow\quad c_t = \left(1 - R^{-1}(R\beta)^{\sigma}\right)\left[a_t + \sum_{j=0}^{\infty} \frac{1}{R^j}\,y_{t+j}\right]$$

consider $j = 0$
$$\text{mpc} = \frac{\partial c_t}{\partial y_t} = 1 - R^{-1}(R\beta)^{\sigma} \;\overset{R\beta \approx 1}{\approx}\; 1 - \frac{1}{R} = \frac{1+r}{1+r} - \frac{1}{1+r} \approx r$$

(side note: $R\beta = 1$, $\frac{1+r}{1+\rho} = 1$, $r = \rho$)

in the PIH model, the mpc is small! $\approx 0.03$

---

One subtlety

$$y_t = y^P + y_t^c \qquad y_t^c = y_t - y^P$$

$y^P$: "permanent or average income", $y_t^c$: current income

$$c_t = \left(1 - R^{-1}(R\beta)^{\sigma}\right)\left(a_t + \sum_{j=0}^{\infty} \frac{1}{R^j}\left(y^P + y_t^c\right)\right)$$
[possible typo: $y_t^c$ inside the sum should be $y_{t+j}^c$]
$$= \left(1 - R^{-1}(R\beta)^{\sigma}\right)\left(a_t + y^P \frac{1}{1-R^{-1}} + \sum_{j=0}^{\infty} \frac{1}{R^j}\,y_t^c\right)$$

$$\text{mpc} = \frac{\partial c_t}{\partial a_t} \qquad \frac{1}{1-R^{-1}} = \frac{1}{1-(1+r)^{-1}} = \frac{1+r}{r}$$

$$\frac{\partial c_t}{\partial y^P} = \Big(1 - R^{-1}\underbrace{(R\beta)^{\sigma}}_{\approx 1}\Big)\frac{1+r}{r}$$

<!-- page 5 -->

$$= \frac{1}{r}(1+r-1) = 1$$

Summary:
$$\frac{\partial c_t}{\partial y_t} = \frac{\partial c_t}{\partial y_t^c} \approx \rho \qquad \text{for transitory change in } y$$
[symbol written like $\rho$, possibly $r$]
$$\frac{\partial c_t}{\partial y^P} \approx 1 \qquad \text{for permanent change in } y$$

The MPC depends on the **persistence** of the income change.

Friedman 1957 book, *Theory of the consumption function*.
$$\frac{c_t}{y_t} = \phi \;\Rightarrow\; c_t = \phi y_t \;\Rightarrow\; \frac{\partial c_t}{\partial y_t} = \phi$$

---

## The random walk hypothesis and Rational Expectations errors

consider
$$\max_{\{c_t,\,a_{t+1}\}_{t=0}^{\infty}} E_0 \sum_{t=0}^{\infty} \beta^t u(c_t)$$
s.t.
$$c_t + \frac{a_{t+1}}{1+r} = y_t + a_t$$
$$\lim_{T\to\infty} \frac{a_{T+1}}{\prod_{\tau=0}^{T}(1+r_\tau)} \geq 0$$

<!-- page 6 -->

$a_0$ given
$$\Rightarrow\quad u'(c_t) = \beta(1+r_t)\,E_t\left[u'(c_{t+1})\right]$$

Hall (1978) showed the consumption approximately follows a random walk.

**Digression: Random Walk and RE errors**

$s_t$: generic variable
$$s_{t+1} = s_t + \varepsilon_{t+1}$$

$\varepsilon_t$ is white noise: $E[\varepsilon_t] = 0$, $E[\varepsilon_t^2] = \sigma_\varepsilon^2$, $E[\varepsilon_t \varepsilon_\tau] = 0$ for $t \neq \tau$

Consider $E_t[s_{t+1}] = E[s_{t+1} \mid I_t]$, $\quad I_t = \{c_{t-j}, y_{t-j}, a_{t-j}\}_{j=0}^{\infty}$

RE error:
$$\varepsilon_{t+1} := s_{t+1} - E_t[s_{t+1}]$$

(1) $E_t[\varepsilon_{t+1}] = 0$
$$E_t\left[s_{t+1} - E_t[s_{t+1}]\right] = E_t[s_{t+1}] - E_t[s_{t+1}] = 0$$

take $x_\tau$, $\tau \leq t$, i.e. $x_\tau \in I_t$

(2) $E_t[x_\tau \varepsilon_{t+1}] = x_\tau E_t[\varepsilon_{t+1}] = 0 \qquad \leftarrow$ in data often not true

<!-- page 7 -->

(3)
$$\varepsilon_{t+1} = \alpha + \beta x_t + u_{t+1}$$
$$\beta = \frac{\operatorname{cov}(\varepsilon_{t+1}, x_t)}{V[x_t]} = \frac{E[\varepsilon_{t+1} x]}{V[x_t]} = \frac{E\big[\overbrace{E_t[\varepsilon_{t+1} x_t]}^{(2)\;=\;0}\big]}{V[x_t]} = 0$$

---

**Random Walk hypothesis**
$$u'(c_{t+1}) = E_t\left[u'(c_{t+1})\right] + \varepsilon_{t+1} \qquad (\varepsilon_{t+1}: \text{def of RE error})$$

EE $\Rightarrow$
$$u'(c_t) = \beta(1+r)\,u'(c_{t+1}) - \beta(1+r)\,\varepsilon_{t+1}$$

$\beta(1+r) \approx 1 \Rightarrow$
$$u'(c_{t+1}) \approx u'(c_t) + \varepsilon_{t+1}$$

MU approx follows a random walk.

Take a first order approx (Taylor) of MU around $c$, steady state level consumption
$$u'(c_t) = u'(c) + u''(c)\cdot(c_t - c)$$
$$= u'(c) + u''(c)\cdot c\left(\frac{c_t - c}{c}\right)$$
$$= u'(c) + u''(c)\,c\,(\ln c_t - \ln c)$$

$$\Rightarrow\quad \ln c_{t+1} = \ln c_t + \eta_{t+1}$$
where
$$\eta_t := \frac{1}{c\,u''(c)}\,\varepsilon_{t+1}$$
[possible typo: left side should be $\eta_{t+1}$]

<!-- page 8 -->

$$E_t[\ln c_{t+1}] = \ln c_t$$

Hall tests this prediction
$$\ln c_{t+1} = \ln c_t + \gamma x_t + \eta_{t+1}$$
$$H_0: \gamma = 0 \qquad x_t: \text{past income, stock prices, etc.}$$

---

## Statistical Tests of the PIH

Shea 1995: Union contracts. Predictable wage change causes consumption change ↯ PIH

Hsieh $\approx$ 1999, Kueng (2016)

Johnson, Parker, Souleles (2006): study Economic Growth and Tax Relief Reconciliation Act of 2001

tax rebates $\approx$ 300-600 \$, randomized receipt time

$$c_{i,t} - c_{i,t-1} = \underbrace{\beta \underset{\uparrow\,\text{rebate}}{R_{i,t}}}_{\approx 0 \text{ under PIH}} + \text{controls}_{i,t} + u_{i,t}$$
(written above: $+\,\gamma R_{i,t-1}$)

Kaplan-Violante 2014

<!-- page 9 -->

$$\text{CRRA} \to \quad \beta \approx \rho \;\text{ for transitory income change}$$
$$\beta = 0 \;\text{ for anticipated income changes}$$
$$\hat\beta \approx 0.2\text{-}0.3 \quad \text{↯ PIH}$$

---

## Extensions of the PIH model

### 1) Precautionary savings

EE with $\beta(1+r) = 1$
$$u'(c_t) = E_t\left[u'(c_{t+1})\right]$$

2nd order Taylor exp. around $c_t$
$$u'(c_{t+1}) = u'(c_t) + u''(c_t)\cdot(c_{t+1}-c_t) + \frac{u'''(c_t)}{2}(c_{t+1}-c_t)^2$$

$$E_t\left[\frac{c_{t+1}-c_t}{c_t}\right] = -\underbrace{\frac{u'''(c_t)\,c_t}{2u''(c_t)}}_{u''<0}\;\underbrace{E_t\left[\left(\frac{c_{t+1}-c_t}{c_t}\right)^2\right]}_{\geq 0}$$

Sign determined by $u'''(c_t)$ (prudence motive). $-\frac{u'''(c)c}{u''(c)}$: coefficient of relative prudence (Kimball 1990).

Assume $u''' > 0$. Then
$$E_t\left[\frac{c_{t+1}-c_t}{c_t}\right] > 0$$

This is known as precautionary savings.

<!-- page 10 -->

Quadratic utility
$$u(c_t) = b_1 c_t - \tfrac{1}{2} b_2 c_t^2$$
$$u' = b_1 - b_2 c_t, \qquad u'' = -b_2, \qquad u''' = 0 \;\Rightarrow\; \text{no prudence}$$

CRRA
$$u(c_t) = \frac{c_t^{1-\frac{1}{\sigma}}}{1-\frac{1}{\sigma}}, \qquad u' = c_t^{-\frac{1}{\sigma}}, \qquad u'' = -\frac{1}{\sigma}c_t^{-\frac{1}{\sigma}-1}$$
$$u''' = \frac{1}{\sigma}\left(\frac{1}{\sigma}+1\right)c_t^{-\frac{1}{\sigma}-2} > 0 \;\Rightarrow\; \text{prudence}$$

Illustration
$$u'(c_t) = E_t\left[u'(c_{t+1})\right]$$

[Graph: convex decreasing $u'(c_{t+1})$ against $c_{t+1}$ ($u'>0$, $u''<0$, $u'''>0$). Two outcomes $c_{t+1}^L = c_t - \delta$ and $c_{t+1}^H = c_t + \delta$ around $c_t = E_t[c_{t+1}]$ (with $\beta(1+r)=1$). The chord midpoint $E_t[u'(c_{t+1})]$ lies above $u'(E_t[c_{t+1}])$ on the curve, with $u'(c_{t+1}^L)$ and $u'(c_{t+1}^H)$ marked on the vertical axis.]

Jensen's inequality ($u''' > 0$): $E_t[u'(c_{t+1})] > u'(E_t[c_{t+1}])$

$$u'(c_t) = E_t\left[u'(c_{t+1})\right] > u'\left(E_t[c_{t+1}]\right) \qquad \Big|\,(u')^{-1}, \; u''<0$$
$$\Rightarrow\quad c_t < E_t[c_{t+1}]$$

[Graph: small inset of decreasing $u'$ against $c$ with $u'(c_t) > u'(E_t[c_{t+1}])$ mapping to $c_t < E_t[c_{t+1}]$ on the horizontal axis.]

<!-- page 11 -->

---

**Risk aversion vs. Prudence**

linear utility $u = c \Rightarrow E[u] = E[c]$

quadratic utility $u = ac - bc^2 \Rightarrow$
$$E[u] = aE[c] - bE[c^2] = a\left(pc_L + (1-p)c_H\right) - b\left[pc_L^2 + (1-p)c_H^2\right]$$

### 2) Borrowing Constraint

$$a_{t+1} \geq \underline{a} \qquad \underline{a} \leq 0$$

(i) ad-hoc

(ii) natural borrowing limit ($\forall\, c_t = 0$)
$$a_{t+1} + \sum_{j=0}^{\infty} \frac{1}{\prod_{k=0}^{j-1}(1+r_{t+1+k})}\,y_{t+1+j} = \sum_{j=0}^{\infty} \frac{1}{\prod_{k=0}^{j-1}(1+r_{t+1+k})}\,c_{t+1+j} \geq 0$$

$$a_{t+1} \geq -\sum_{j=0}^{\infty} \frac{1}{\prod_{k=0}^{j-1}(1+r_{t+1+k})}\,y_{t+1+k}$$
[possible typo: $y_{t+1+k}$ should be $y_{t+1+j}$; summation index is also written $i=0$]

$r$ const, $y_{\min}$
$$a_{t+1} \geq -y_{\min}\sum_{i=0}^{\infty}\left(\frac{1}{1+r}\right)^i = -\frac{1+r}{r}\,y_{\min}$$

<!-- page 12 -->

---

$$\max_{\{c_t,\,a_{t+1}\}_{t=0}^{\infty}} E_0 \sum_{t=0}^{\infty} \beta^t u(c_t)$$
s.t.
$$c_t + \frac{a_{t+1}}{1+r} = y_t + a_t$$
$$a_{t+1} \geq \underline{a} \qquad \leftarrow$$
$$\lim_{T\to\infty} \frac{a_{T+1}}{\prod_{\tau=0}^{T}(1+r_\tau)} \geq 0$$

$$\mathcal{L} = E_0 \sum_{t=0}^{\infty} \beta^t \left(u(c_t) + \lambda_t\left(y_t + a_t - c_t - \frac{a_{t+1}}{1+r}\right) + \mu_t\left(a_{t+1} - \underline{a}\right)\right)$$

FOC:
$$u'(c_t) = \lambda_t$$
$$\beta E_t[\lambda_{t+1}] - \lambda_t \frac{1}{1+r} + \mu_t = 0$$

Rearrange:
$$u'(c_t) = \beta(1+r)E_t\left[u'(c_{t+1})\right] + \mu_t(1+r)$$

complementary slackness
$$\mu_t\left(a_{t+1} - \underline{a}\right) = 0, \qquad \mu_t \geq 0$$

Case 1: $a_{t+1} > \underline{a}$, $\mu_t = 0$ (written as $c_{t+1} > \underline{a}$) [possible typo: $c_{t+1}$ should be $a_{t+1}$]
$$u'(c_t) = \beta(1+r)E_t\left[u'(c_{t+1})\right]$$

<!-- page 13 -->

Case 2: constrained $a_{t+1} = \underline{a} \Rightarrow \mu_t \geq 0$
$$u'(c_t) = \beta(1+r)E_t\left[u'(c_{t+1})\right] + (1+r)\mu_t \qquad \leftarrow$$
$$> \beta(1+r)E_t\left[u'(c_{t+1})\right]$$

$$c_t + \frac{a_{t+1}}{1+r} = y_t + a_t, \qquad a_{t+1} = \underline{a}$$
$$c_t = y_t + a_t - \frac{\underline{a}}{1+r}$$

$$\text{mpc} = \frac{\partial c_t}{\partial y_t} = 1 \qquad \textbf{HANK}$$

---

Borrowing constraints induce a saving motive

$\beta(1+r) = 1$
$$u'(c_t) \geq E_t\left[u'(c_{t+1})\right] \qquad \forall t$$

Supermartingale

under conditions the supermartingale convergence thm. applies:
$$u'(c_t) \xrightarrow{a.s.} u'(c) \qquad P\left(\lim_{t\to\infty} u'(c_t) = u'(c)\right) = 1$$
$$a_{t+1} \xrightarrow{a.s.} a$$

<!-- page 14 -->

$c$, $a$ grow to infinity

This is called **self-insurance**.

Sometimes (to distinguish from precautionary savings) use quadratic utility
$$b_1 - b_2 c_t \geq E_t\left[b_1 - b_2 c_{t+1}\right]$$
$$\Rightarrow\quad c_t \leq E_t[c_{t+1}]$$
