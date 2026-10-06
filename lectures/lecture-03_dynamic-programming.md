# Dynamic Programming

*ECO387C Macro I, UT Austin. Handwritten lecture notes, Wednesday, September 2, 2026. Transcribed page by page.*

<!-- page 1 -->

## Dynamic Programming

**Readings:**

- Azzimonti et al. (2024, ch. 4.4.)
- Ljungqvist + Sargent (2018, ch. 2.2, 3, 4)
- Stokey, Lucas, Prescott (1989, ch. 4) [ch. 4 highlighted]

### The problem

**Problem 1**

$$\max_{\{y_t, x_{t+1}\}_{t=0}^{\infty}} \sum_{t=0}^{\infty} \beta^t \hat{F}(y_t)$$

subject to

$$x_{t+1} = h(x_t, y_t)$$
$$x_{t+1} \in \Gamma(x_t)$$

- $\hat{F}$: instantaneous (flow) objective
- $y_t$: control variables
- $x_t$: state variables
- $h$: transition equation
- $\Gamma$: feasible set
- $\beta$: discount factor

Suppose $\Gamma(x_t) = [\underline{x}, \gamma(x_t)]$

solve $x_{t+1} = h(x_t, y_t)$ for $y_t$, so $y_t = \hat{h}(x_t, x_{t+1})$

$$F(x_t, x_{t+1}) = \hat{F}\big(\hat{h}(x_t, x_{t+1})\big)$$

**Problem 2:**

$$\max_{\{x_{t+1} \in \Gamma(x_t)\}_{t=0}^{\infty}} \sum_{t=0}^{\infty} \beta^t F(x_t, x_{t+1})$$

<!-- page 2 -->

[arrow pointing up at the Problem 2 objective:] as in Problem 1

difference: transition eq. has been incorporated into the objective

Suppose $F$ is differentiable in both arguments

**Assume interior solution** [highlighted]

$$F_2(x_t, x_{t+1}) + \beta F_1(x_{t+1}, x_{t+2}) = 0$$

$$F_1 = \frac{\partial F}{\partial x_t} \qquad F_2 = \frac{\partial F}{\partial x_{t+1}}$$

Transversality condition

$$\lim_{T \to \infty} \beta^T F_1(x_T, x_{T+1}) \cdot x_T = 0$$

$$\left[\frac{\partial F}{\partial x_t}\right] = \frac{\text{utils}}{\text{units } x_T}$$

---

**Example: Neoclassical Growth Model (Planning Problem)**

$$\max_{\{c_t, k_{t+1}\}_{t=0}^{\infty}} \sum_{t=0}^{\infty} \beta^t u(c_t)$$

s.t.

$$k_{t+1} = k_t(1-\delta) + i_t \qquad \checkmark$$ [annotation on $\delta$: depreciation rate]
$$y_t \ge c_t + i_t \qquad \checkmark \qquad i_t \le y_t + c_t$$ [possible typo: $i_t \le y_t - c_t$]
$$y_t \le f(k_t) \qquad \checkmark \longleftarrow \text{production function } y_t = A_t k_t^{\alpha} \text{ [crossed-out term, likely } n_t^{1-\alpha}\text{]}$$
$$c_t \ge 0 \quad \text{[highlighted]}$$
$$k_{t+1} \ge 0$$
$$k_0 \text{ given}$$

[boxed:]

$$k_{t+1} + c_t \le k_t(1-\delta) + f(k_t)$$

if $u' > 0$: [the $\le$ becomes] $=$

$$k_{t+1} = k_t(1-\delta) + f(k_t) - c_t = h(k_t, c_t)$$

for upper bound on $k_{t+1}$: $c_t = 0$

here | generic
:--|:--
$k$ | $x$
$c$ | $y$

$$k_{t+1} \ge 0$$
$$k_{t+1} \le k_t(1-\delta) + f(k_t)$$
$$\Gamma(k_t) = [0, k_t(1-\delta) + f(k_t)]$$

<!-- page 3 -->

$$\Gamma(k_t) = [0, k_t(1-\delta) + f(k_t)]$$

**Problem 1**

$$\max_{\{c_t, k_{t+1}\}_{t=0}^{\infty}} \sum_{t=0}^{\infty} \beta^t u(c_t)$$
$$k_{t+1} = k_t(1-\delta) + f(k_t) - c_t$$
$$k_{t+1} \in [0, k_t(1-\delta) + f(k_t)]$$

**Problem 2**

$$c_t = k_t(1-\delta) + f(k_t) - k_{t+1}$$

[boxed, highlighted:]

$$\max_{\{k_{t+1}\}_{t=0}^{\infty} \in [0,\, k_t(1-\delta) + f(k_t)]} \sum_{t=0}^{\infty} \beta^t u\big(k_t(1-\delta) + f(k_t) - k_{t+1}\big)$$
$$k_0 \text{ given}$$

---

## Dynamic Programming

Define value function as

$$V(x_0) = \max_{\{x_{t+1} \in \Gamma(x_t)\}_{t=0}^{\infty}} \sum_{t=0}^{\infty} \beta^t F(x_t, x_{t+1})$$

$$V(x_0) \overset{(1)}{=} \max_{\{x_{t+1} \in \Gamma(x_t)\}_{t=0}^{\infty}} \left\{ F(x_0, x_1) + \beta \sum_{t=1}^{\infty} \beta^{t-1} F(x_t, x_{t+1}) \right\}$$

$$\overset{\text{assumptions}}{=} \max_{x_1 \in \Gamma(x_0)} \left\{ F(x_0, x_1) + \beta \max_{\{x_{t+1} \in \Gamma(x_t)\}_{t=1}^{\infty}} \left[ \sum_{t=1}^{\infty} \beta^{t-1} F(x_t, x_{t+1}) \right] \right\}$$

$$= \max_{x_1 \in \Gamma(x_0)} \left\{ F(x_0, x_1) + \beta \max_{\{x_{t+2} \in \Gamma(x_{t+1})\}_{t=0}^{\infty}} \left[ \sum_{t=0}^{\infty} \beta^{t} F(x_{t+1}, x_{t+2}) \right] \right\}$$

[the inner max is underlined in yellow, the re-indexed $t=0$ and $\beta^t$ underlined in red]

$$= \max_{x_1 \in \Gamma(x_0)} \left\{ F(x_0, x_1) + \beta V(x_1) \right\}$$

[arrow to $V(x_1)$:] only a function of $x_1$

<!-- page 4 -->

**Features:**

- we can maximize "in steps"
- Sequence problem involves choosing $\{x_1, x_2, \ldots\}$
- Recursive problem: choose $x_1$ given $V(x_1)$
- Equivalence between sequence and recursive problems: "Principle of Optimality"
- both problems have advantages

**Notational change:** replace $x_t$ by $x$, $x_{t+1}$ by $x'$

**Bellman Equation**

$$V(x) = \max_{x' \in \Gamma(x)} \left\{ F(x, x') + \beta V(x') \right\}$$

- $x$: state
- $V$: value function

[boxed:] **functional equation**

unknown is the value function $V: X \to \mathbb{R}$

$V$ only depends on $x$

**Policy Function:**

$x' = g(x)$, also only a function of $x$

$$g(x) = \arg\max_{x' \in \Gamma(x)} \left\{ F(x, x') + \beta V(x') \right\}$$

$$V(x) = F(x, g(x)) + \beta V(g(x))$$

---

**The Neoclassical Growth Model**

State: $k$

$$V(k) = \max_{k' \in [0,\, (1-\delta)k + f(k)]} \left\{ u\big((1-\delta)k + f(k) - k'\big) + \beta V(k') \right\}$$

<!-- page 5 -->

### Properties of the value function

1) the value function is often unique
2) the value function is often approached by iterations
3) If (i) $F$ is strictly increasing in its first argument, (ii) $\Gamma$ is monotone ($x \le \tilde{x}$ implies $\Gamma(x) \subseteq \Gamma(\tilde{x})$), then $V$ is strictly increasing
4) If (i) $F$ is jointly strictly concave in its two arguments, (ii) $\Gamma$ is convex ($x' \in \Gamma(x)$ and $\tilde{x}' \in \Gamma(\tilde{x})$, then $\forall \theta \in (0,1)$: $\theta x' + (1-\theta)\tilde{x}' \in \Gamma(\theta x + (1-\theta)\tilde{x})$), then $V$ is strictly concave and the policy function is unique

   [small sketch in margin next to item 4: an increasing concave curve]
5) The value function is sometimes differentiable and can be used to obtain the Euler equation
6) The policy function is sometimes increasing

---

### The Bellman Operator as a contraction

**The Bellman Operator**

$\Theta$: space of continuous, real-valued functions defined on $X \subseteq \mathbb{R}^n$, $X$ closed and bounded interval

$f \in \Theta$: $f: X \to \mathbb{R}$

Define Bellman operator $T: \Theta \to \Theta$

$$T(f(x)) = \max_{x' \in \Gamma(x)} \left\{ F(x, x') + \beta f(x') \right\} \qquad (*)$$

**Some Definitions**

<!-- page 6 -->

**Def. 1: (Metric)**

Let $M$ be a set. The function $d: M \times M \to \mathbb{R}$ is a metric if it satisfies for all $x, y, z \in M$:

1. $d(x,y) = 0$ if and only if $x = y$
2. (Symmetry) $d(x,y) = d(y,x)$
3. (Triangle inequality) $d(x,z) \le d(x,y) + d(y,z)$

The pair $(M, d)$ is called a metric space

**Sup-norm:**

$$d(f,g) = \sup_{s \in S} |f(s) - g(s)| \quad \text{for any } f, g \in \Theta$$

the sup-norm is a metric

Metric space $(\Theta, d)$

**Definition 2: (Contraction Mapping)**

Let $(\Theta, d)$ be a metric space. The mapping $T: \Theta \to \Theta$ is a contraction on $\Theta$ if there exists **modulus** $\beta \in [0,1)$ such that

$$d(T(f), T(g)) \le \beta\, d(f,g)$$

**Two Results**

**Prop 1: (Banach's fixed-point theorem)**

Let $(\Theta, d)$ be a non-empty, complete metric space with contraction mapping $T: \Theta \to \Theta$ with **modulus** $\beta$. Then

1) $T$ has a unique fixed point $f^*$, i.e. $T(f^*) = f^*$
2) for any $f_0 \in \Theta$: $d(T(f_0), f^*) \le \beta\, d(f_0, f^*)$

<!-- page 7 -->

**Prop 2: (Blackwell's sufficient conditions for a contraction)**

Let $T: \Theta \to \Theta$ be an operator, satisfying

i) monotonicity: If $f, g \in \Theta$ with $f(s) \le g(s)\ \forall s$, then $T(f(s)) \le T(g(s))\ \forall s$

ii) discounting: There exists $\beta \in [0,1)$ such that $\forall f \in \Theta$ and for all constant functions $k$

$$T(f(s) + k) \le T(f(s)) + \beta k$$

Then $T$ is a contraction with modulus $\beta$

---

**Verifying Blackwell's sufficient conditions**

*Monotonicity:* Take $f, g \in \Theta$ with $f(x) \le g(x)\ \forall x$

$$T(f(x)) \overset{\text{def}(*)}{=} \max_{x' \in \Gamma(x)} \left\{ F(x,x') + \beta f(x') \right\}$$
$$\le \max_{x' \in \Gamma(x)} \left\{ F(x,x') + \beta g(x') \right\}$$
$$\overset{\text{def}(*)}{=} T(g(x)) \qquad \checkmark$$

*Discounting:* Take $f \in \Theta$, $k \in \Theta$, $k$ constant

$$T(f(x) + k) \overset{\text{def}(*)}{=} \max_{x' \in \Gamma(x)} \left\{ F(x,x') + \beta\big(f(x') + k\big) \right\}$$
$$= \max_{x' \in \Gamma(x)} \left\{ F(x,x') + \beta f(x') + \beta k \right\}$$ [arrow pulling $\beta k$ out of the max]
$$= T(f(x)) + \beta k$$
$$\checkmark \text{ for } \beta < 1$$

Hence: The Bellman operator is a contraction

**Note:** Set of bounded and real-valued functions

<!-- page 8 -->

**Note:** Set of bounded and real-valued functions is complete, so $(\Theta, d)$ is a complete metric space

$\Rightarrow$ Banach's fixed point theorem applies

1) The Bellman operator $T$ has a unique fixed point: $T(V) = V$

   Hence, we can write:

$$V(x) = \max_{x' \in \Gamma(x)} \left\{ F(x,x') + \beta V(x') \right\}$$

2) Value function iteration

   $\to$ the fixed point is approached by iterations

   initial guess $V_0$, then $d(T(V_0), V) \le \beta\, d(V_0, V)$

Hence:

$$d\big(T^n(V_0), V\big) \le \beta\, d\big(T^{n-1}(V_0), V\big) \le \ldots \le \beta^n d(V_0, V)$$

$$\lim_{n \to \infty} T^n(V_0) = V$$

**Algorithm:**

1) Set $V_0$ to initial guess, e.g. $V_0(x) = 0\ \forall x$
2) Iterate for $n = 0, 1, \ldots$ using the following recursion:

$$V_{n+1}(x) = \max_{x' \in \Gamma(x)} \left\{ F(x,x') + \beta V_n(x') \right\}$$

**Remark:**

<!-- page 9 -->

**Remark:** oftentimes $F$ is not bounded in economic applications, e.g. $f(k) = k^{\alpha}$ on $[0, \infty)$. This implies that the set $\Theta$ on which the Bellman Operator is defined also contains unbounded functions. Then $(\Theta, d)$ is not generally complete and hence Banach's fixed point theorem may not apply...

---

[flow diagram of three boxes connected by downward arrows: "Blackwell's sufficient conditions" (annotated "monotonicity, discounting") $\to$ "Banach's fixed point theorem" $\to$ "$V$ unique, VFI possible"]

---

### Obtaining the Euler Equation

$$V(x) = \max_{x' \in \Gamma(x)} \left\{ F(x,x') + \beta V(x') \right\}$$

Assume differentiability, interior solution

$$F_2(x, x') + \beta V'(x') = 0 \qquad (*)$$

policy $x' = g(x)$ solves this equation

<!-- page 10 -->

$$F_2(x, g(x)) + \beta V'(g(x)) = 0$$

$$V(x) = F(x, g(x)) + \beta V(g(x))$$

[curved arrow linking these back to $(*)$ on the previous page]

$$V'(x) = F_1(x, g(x)) + F_2(x, g(x))\, g'(x) + \beta V'(g(x)) \cdot g'(x)$$
$$= F_1(x, g(x)) + \underbrace{\big(F_2 + \beta V'\big)}_{=0\ (*)} g'(x)$$

Shift 1 period ahead

$$V'(x') = F_1\big(g(x), g(g(x))\big)$$
$$= F_1\big(x', g(x')\big)$$

**Functional Euler equation**

$$F_2(x, g(x)) + \beta F_1\big(g(x), g(g(x))\big) = 0$$

compare this to our Euler equation from the sequence problem

$$F_2(x_t, x_{t+1}) + \beta F_1(x_{t+1}, x_{t+2}) = 0$$

---

### Example: A stochastic consumption-saving problem

HH:

$$\max_{\{c_t, a_{t+1}\}_{t=0}^{\infty}} E_0 \sum_{t=0}^{\infty} \beta^t u(c_t)$$

s.t.

$$c_t + \frac{a_{t+1}}{1+r} = y_t + a_t$$

Assumption: $r$ is constant

<!-- page 11 -->

[boxed, highlighted:] $a_{t+1} = s_t(1+r)$

uncertainty about $y_t$ $\qquad$ + nPg condition [read as "no-Ponzi-game"; handwriting looks like "uPg"]

$y_t$ follows a 2-state Markov process

- $y_l$ low: $P(y_l \mid y_l)$, $\quad P(y_h \mid y_l) = 1 - P(y_l \mid y_l)$
- $y_h$ high: $P(y_h \mid y_h)$, $\quad P(y_l \mid y_h) = 1 - P(y_h \mid y_h)$

---

1) State variables: $a, y$

2) Bellman eq.

$$V(a, y) = \max_{a'} \left\{ u\left(a + y - \frac{a'}{1+r}\right) + \beta E\big[V(a', y') \mid y\big] \right\}$$

$$E\big[V(a', y') \mid y\big] = P(y_h \mid y) \cdot V(a', y_h) + P(y_l \mid y) \cdot V(a', y_l)$$

FOC

$$0 = u'(c) \cdot \left(-\frac{1}{1+r}\right) + \beta E\left[ \frac{\partial V(a', y')}{\partial a'} \,\Big|\, y \right]$$

[the term $\partial V(a',y')/\partial a'$ is boxed and highlighted]

Suppose $a' = g(a, y)$ policy fn.

$$V(a, y) = u\left(a + y - \frac{g(a,y)}{1+r}\right) + \beta E\big[V(g(a,y), y') \mid y\big]$$

<!-- page 12 -->

$$V(a, y) = u\left(a + y - \frac{g(a,y)}{1+r}\right) + \beta E\big[V(g(a,y), y') \mid y\big]$$

$$\frac{\partial V(a,y)}{\partial a} = u'(c) - \frac{1}{1+r} u'(c) \frac{\partial g(a,y)}{\partial a} + \beta E\left[ \frac{\partial V(g(a,y), y')}{\partial a'} \cdot \frac{\partial g(a,y)}{\partial a} \,\Big|\, y \right]$$

$$= u'(c) + \underbrace{\left[ -\frac{u'(c)}{1+r} + \beta E\left[ \frac{\partial V(g(a,y), y')}{\partial a'} \,\Big|\, y \right] \right]}_{=0 \text{ by FOC}} \frac{\partial g(a,y)}{\partial a}$$

$$= u'(c)$$

$$\frac{\partial V(a', y')}{\partial a'} = u'(c')$$

$\Rightarrow$ Euler equation

$$u'(c) = \beta(1+r) E\big[u'(c') \mid y\big]$$

$$c = a + y - \frac{a'}{1+r}$$
$$= a + y - \frac{g(a,y)}{1+r} =: h(a, y)$$

$$E\big[u'(c') \mid y\big] = E\big[u'(h(a', y')) \mid y\big]$$
$$= \sum_{y' \in \{y_l, y_h\}} P(y' \mid y)\, u'\big(h(a', y')\big)$$
