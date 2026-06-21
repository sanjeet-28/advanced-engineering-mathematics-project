# -*- coding: utf-8 -*-

import os

ch11_path = r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\chapters\ch11.qmd"

content = r"""---
title: "CHAPTER 11: Fourier Analysis"
---

This chapter on Fourier analysis covers three broad areas: Fourier series in Secs. 11.1–11.4, more general orthonormal series called Sturm–Liouville expansions in Secs. 11.5 and 11.6, and Fourier integrals and transforms in Secs. 11.7–11.9.

The central starting point of Fourier analysis is Fourier series. They are infinite series designed to represent general periodic functions in terms of simple ones, namely, cosines and sines. This trigonometric system is orthogonal, allowing the computation of the coefficients of the Fourier series by use of the well-known Euler formulas, as shown in Sec. 11.1. Fourier series are very important to the engineer and physicist because they allow the solution of ODEs in connection with forced oscillations (Sec. 11.3) and the approximation of periodic functions (Sec. 11.4). Moreover, applications of Fourier analysis to PDEs are given in Chap. 12. Fourier series are, in a certain sense, more universal than the familiar Taylor series in calculus because many discontinuous periodic functions that come up in applications can be developed in Fourier series but do not have Taylor series expansions.

The underlying idea of the Fourier series can be extended in two important ways. We can replace the trigonometric system by other families of orthogonal functions, e.g., Bessel functions and obtain the Sturm–Liouville expansions. Note that related Secs. 11.5 and 11.6 used to be part of Chap. 5 but, for greater readability and logical coherence, are now part of Chap. 11. The second expansion is applying Fourier series to nonperiodic phenomena and obtaining Fourier integrals and Fourier transforms. Both extensions have important applications to solving PDEs as will be shown in Chap. 12.

In a digital age, the discrete Fourier transform plays an important role. Signals, such as voice or music, are sampled and analyzed for frequencies. An important algorithm, in this context, is the fast Fourier transform. This is discussed in Sec. 11.9.

Note that the two extensions of Fourier series are independent of each other and may be studied in the order suggested in this chapter or by studying Fourier integrals and transforms first and then Sturm–Liouville expansions.

**Prerequisite:** Elementary integral calculus (needed for Fourier coefficients).
**Sections that may be omitted in a shorter course:** 11.4–11.9.
**References and Answers to Problems:** App. 1 Part C, App. 2.

## 11.1 Fourier Series {#sec-11-1}

Fourier series are infinite series that represent periodic functions in terms of cosines and sines. As such, Fourier series are of greatest importance to the engineer and applied mathematician. To define Fourier series, we first need some background material.

A function $f(x)$ is called a **periodic function** if $f(x)$ is defined for all real $x$, except possibly at some points, and if there is some positive number $p$, called a **period** of $f(x)$, such that
$$
f(x + p) = f(x)
$$ {#eq-11-1}
for all $x$.

(The function $f(x) = \tan x$ is a periodic function that is not defined for all real $x$ but undefined for some points (more precisely, countably many points), that is $x \neq \pm\pi/2, \pm3\pi/2, \dots$.)

The graph of a periodic function has the characteristic that it can be obtained by periodic repetition of its graph in any interval of length $p$ (@fig-11-258).

![Fig. 258: Periodic function of period $p$](../images/chapter11/fig-11-258.png){#fig-11-258}

The smallest positive period is often called the **fundamental period**. (See Probs. 2–4.)

Familiar periodic functions are the cosine, sine, tangent, and cotangent. Examples of functions that are not periodic are $x, x^2, x^3, e^x, \cosh x$, and $\ln x$, to mention just a few.

If $f(x)$ has period $p$, it also has the period $2p$ because (@eq-11-1) implies $f(x + 2p) = f([x + p] + p) = f(x + p) = f(x)$, etc.; thus for any integer $n = 1, 2, 3, \dots$,
$$
f(x + np) = f(x)
$$ {#eq-11-2}
for all $x$.

Furthermore if $f(x)$ and $g(x)$ have period $p$, then $af(x) + bg(x)$ with any constants $a$ and $b$ also has the period $p$.

Our problem in the first few sections of this chapter will be the representation of various functions $f(x)$ of period $2\pi$ in terms of the simple functions
$$
1, \quad \cos x, \quad \sin x, \quad \cos 2x, \quad \sin 2x, \quad \dots, \quad \cos nx, \quad \sin nx, \quad \dots
$$ {#eq-11-3}
All these functions have the period $2\pi$. They form the so-called **trigonometric system**. @fig-11-259 shows the first few of them (except for the constant 1, which is periodic with any period).

![Fig. 259: Cosine and sine functions having the period $2\pi$ (the first few members of the trigonometric system (3), except for the constant 1)](../images/chapter11/fig-11-259.png){#fig-11-259}

The series to be obtained will be a **trigonometric series**, that is, a series of the form
$$
a_0 + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx) = a_0 + a_1 \cos x + b_1 \sin x + a_2 \cos 2x + b_2 \sin 2x + \dots
$$ {#eq-11-4}
where $a_0, a_1, b_1, a_2, b_2, \dots$ are constants, called the **coefficients** of the series. We see that each term has the period $2\pi$. Hence if the coefficients are such that the series converges, its sum will be a function of period $2\pi$.

Expressions such as (@eq-11-4) will occur frequently in Fourier analysis. To compare the expression on the right with that on the left, simply write the terms in the summation. Convergence of one side implies convergence of the other and the sums will be the same.

Now suppose that $f(x)$ is a given function of period $2\pi$ and is such that it can be represented by a series (@eq-11-4), that is, (@eq-11-4) converges and, moreover, has the sum $f(x)$. Then, using the equality sign, we write
$$
f(x) = a_0 + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)
$$ {#eq-11-5}
and call (@eq-11-5) the **Fourier series** of $f(x)$. We shall prove that in this case the coefficients of (@eq-11-5) are the so-called **Fourier coefficients** of $f(x)$, given by the **Euler formulas**
$$
a_0 = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) \, dx
$$ {#eq-11-6-0}
$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos nx \, dx, \quad n = 1, 2, \dots
$$ {#eq-11-6-a}
$$
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin nx \, dx, \quad n = 1, 2, \dots
$$ {#eq-11-6-b}

The name "Fourier series" is sometimes also used in the exceptional case that (@eq-11-5) with coefficients (@eq-11-6-0)–(@eq-11-6-b) does not converge or does not have the sum $f(x)$—this may happen but is merely of theoretical interest. (For Euler see footnote 4 in Sec. 2.5.)

### A Basic Example
Before we derive the Euler formulas (@eq-11-6-0)–(@eq-11-6-b), let us consider how (@eq-11-5) and (@eq-11-6-0)–(@eq-11-6-b) are applied in this important basic example. Be fully alert, as the way we approach and solve this example will be the technique you will use for other functions. Note that the integration is a little bit different from what you are familiar with in calculus because of the $n$. Do not just routinely use your software but try to get a good understanding and make observations: How are continuous functions (cosines and sines) able to represent a given discontinuous function? How does the quality of the approximation increase if you take more and more terms of the series? Why are the approximating functions, called the partial sums of the series, in this example always zero at $0$ and $\pi$? Why is the factor $1/n$ (obtained in the integration) important?

### EXAMPLE 1 Periodic Rectangular Wave (Fig. 260) {#ex-11-1}
Find the Fourier coefficients of the periodic function $f(x)$ in @fig-11-260. The formula is
$$
f(x) = \begin{cases} -k & \text{if } -\pi < x < 0 \\ k & \text{if } 0 < x < \pi \end{cases} \quad \text{and} \quad f(x + 2\pi) = f(x)
$$ {#eq-11-7}
Functions of this kind occur as external forces acting on mechanical systems, electromotive forces in electric circuits, etc. (The value of $f(x)$ at a single point does not affect the integral; hence we can leave $f(x)$ undefined at $x = -\pi, 0$, and $\pi$.)

![Fig. 260: Given function $f(x)$ (Periodic rectangular wave)](../images/chapter11/fig-11-260.png){#fig-11-260}

**Solution.**
From (@eq-11-6-0) we obtain $a_0 = 0$. This can also be seen without integration, since the area under the curve of $f(x)$ between $-\pi$ and $\pi$ (taken with a minus sign where $f(x)$ is negative) is zero.

From (@eq-11-6-a) we obtain the coefficients $a_1, a_2, \dots$ of the cosine terms. Since $f(x)$ is given by two expressions, the integrals from $-\pi$ to $\pi$ split into two integrals:
$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos nx \, dx = \frac{1}{\pi} \left[ \int_{-\pi}^{0} (-k) \cos nx \, dx + \int_{0}^{\pi} k \cos nx \, dx \right] = \frac{1}{\pi} \left[ \left. -k \frac{\sin nx}{n} \right|_{-\pi}^{0} + \left. k \frac{\sin nx}{n} \right|_{0}^{\pi} \right] = 0
$$
because $\sin nx = 0$ at $x = -\pi, 0$, and $\pi$ for all $n = 1, 2, \dots$. We see that all these cosine coefficients are zero. That is, the Fourier series of (@eq-11-7) has no cosine terms, just sine terms, it is a Fourier sine series with coefficients obtained from (@eq-11-6-b);
$$
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin nx \, dx = \frac{1}{\pi} \left[ \int_{-\pi}^{0} (-k) \sin nx \, dx + \int_{0}^{\pi} k \sin nx \, dx \right] = \frac{1}{\pi} \left[ \left. k \frac{\cos nx}{n} \right|_{-\pi}^{0} - \left. k \frac{\cos nx}{n} \right|_{0}^{\pi} \right]
$$
Since $\cos(-\alpha) = \cos \alpha$ and $\cos 0 = 1$, this yields
$$
b_n = \frac{k}{n\pi} [ \cos 0 - \cos(-n\pi) - \cos n\pi + \cos 0 ] = \frac{2k}{n\pi} (1 - \cos n\pi)
$$
Now, $\cos \pi = -1, \cos 2\pi = 1, \cos 3\pi = -1, \dots$; in general,
$$
\cos n\pi = \begin{cases} -1 & \text{for odd } n \\ 1 & \text{for even } n \end{cases}
$$
and thus
$$
1 - \cos n\pi = \begin{cases} 2 & \text{for odd } n \\ 0 & \text{for even } n \end{cases}
$$
Hence the Fourier coefficients $b_n$ of our function are
$$
b_1 = \frac{4k}{\pi}, \quad b_2 = 0, \quad b_3 = \frac{4k}{3\pi}, \quad b_4 = 0, \quad b_5 = \frac{4k}{5\pi}, \quad \dots
$$
Since the $a_n$ are zero, the Fourier series of $f(x)$ is
$$
f(x) = \frac{4k}{\pi} \left( \sin x + \frac{1}{3} \sin 3x + \frac{1}{5} \sin 5x + \dots \right)
$$ {#eq-11-8}

The partial sums are
$$
S_1 = \frac{4k}{\pi} \sin x, \quad S_2 = \frac{4k}{\pi} \left( \sin x + \frac{1}{3} \sin 3x \right), \quad S_3 = \frac{4k}{\pi} \left( \sin x + \frac{1}{3} \sin 3x + \frac{1}{5} \sin 5x \right), \quad \dots
$$
Their graphs in @fig-11-261 seem to indicate that the series is convergent and has the sum $f(x)$, the given function.

![Fig. 261: First three partial sums of the corresponding Fourier series](../images/chapter11/fig-11-261.png){#fig-11-261}

We notice that at $x = 0$ and $x = \pi$, the points of discontinuity of $f(x)$, all partial sums have the value zero, the arithmetic mean of the limits $-k$ and $k$ of our function, at these points. This is typical.

Furthermore, assuming that $f(x)$ is the sum of the series and setting $x = \pi/2$, we have
$$
f(\pi/2) = k = \frac{4k}{\pi} \left( 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots \right)
$$
Thus
$$
1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots = \frac{\pi}{4}
$$
This is a famous result obtained by Leibniz in 1673 from geometric considerations. It illustrates that the values of various series with constant terms can be obtained by evaluating Fourier series at specific points. $\blacksquare$

### Derivation of the Euler Formulas (6)
The key to the Euler formulas (@eq-11-6-0)–(@eq-11-6-b) is the orthogonality of (@eq-11-3), a concept of basic importance, as follows. Here we generalize the concept of inner product (Sec. 9.3) to functions.

**THEOREM 1 Orthogonality of the Trigonometric System (3)**
The trigonometric system (@eq-11-3) is orthogonal on the interval $[-\pi, \pi]$ (hence also on $[0, 2\pi]$ or any other interval of length $2\pi$ because of periodicity); that is, the integral of the product of any two functions in (@eq-11-3) over that interval is 0, so that for any integers $n$ and $m$,
$$
\int_{-\pi}^{\pi} \cos nx \cos mx \, dx = 0 \quad (n \neq m)
$$ {#eq-11-9-a}
$$
\int_{-\pi}^{\pi} \sin nx \sin mx \, dx = 0 \quad (n \neq m)
$$ {#eq-11-9-b}
$$
\int_{-\pi}^{\pi} \sin nx \cos mx \, dx = 0 \quad (\text{for all } n \text{ and } m)
$$ {#eq-11-9-c}

**PROOF**
This follows simply by transforming the integrands trigonometrically from products into sums. In (@eq-11-9-a) and (@eq-11-9-b), by (11) in App. A3.1,
$$
\cos nx \cos mx = \frac{1}{2} \cos(n + m)x + \frac{1}{2} \cos(n - m)x
$$
$$
\sin nx \sin mx = \frac{1}{2} \cos(n - m)x - \frac{1}{2} \cos(n + m)x
$$
Since $m \neq n$ (integer!), the integrals on the right are all 0. Similarly, in (@eq-11-9-c), for all integer $m$ and $n$ (without exception; do you see why?)
$$
\sin nx \cos mx = \frac{1}{2} \sin(n + m)x + \frac{1}{2} \sin(n - m)x
$$
giving 0 upon integration. $\square$

### Application of Theorem 1 to the Fourier Series (5)
We prove (@eq-11-6-0). Integrating on both sides of (@eq-11-5) from $-\pi$ to $\pi$, we get
$$
\int_{-\pi}^{\pi} f(x) \, dx = \int_{-\pi}^{\pi} \left[ a_0 + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx) \right] \, dx
$$
We now assume that termwise integration is allowed. (We shall say in the proof of Theorem 2 when this is true.) Then we obtain
$$
\int_{-\pi}^{\pi} f(x) \, dx = a_0 \int_{-\pi}^{\pi} dx + \sum_{n=1}^{\infty} \left[ a_n \int_{-\pi}^{\pi} \cos nx \, dx + b_n \int_{-\pi}^{\pi} \sin nx \, dx \right]
$$
The first term on the right equals $2\pi a_0$. Integration shows that all the other integrals are 0. Hence division by $2\pi$ gives (@eq-11-6-0).

We prove (@eq-11-6-a). Multiplying (@eq-11-5) on both sides by $\cos mx$ with any fixed positive integer $m$ and integrating from $-\pi$ to $\pi$, we have
$$
\int_{-\pi}^{\pi} f(x) \cos mx \, dx = \int_{-\pi}^{\pi} \left[ a_0 + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx) \right] \cos mx \, dx
$$ {#eq-11-10}
We now integrate term by term. Then on the right we obtain an integral of $a_0 \cos mx$, which is 0; an integral of $a_n \cos nx \cos mx$, which is $\pi a_m$ for $n = m$ and 0 for $n \neq m$ by (@eq-11-9-a); and an integral of $b_n \sin nx \cos mx$, which is 0 for all $n$ and $m$ by (@eq-11-9-c). Hence the right side of (@eq-11-10) equals $a_m \pi$. Division by $\pi$ gives (@eq-11-6-a) (with $m$ instead of $n$).

We finally prove (@eq-11-6-b). Multiplying (@eq-11-5) on both sides by $\sin mx$ with any fixed positive integer $m$ and integrating from $-\pi$ to $\pi$, we get
$$
\int_{-\pi}^{\pi} f(x) \sin mx \, dx = \int_{-\pi}^{\pi} \left[ a_0 + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx) \right] \sin mx \, dx
$$ {#eq-11-11}
Integrating term by term, we obtain on the right an integral of $a_0 \sin mx$, which is 0; an integral of $a_n \cos nx \sin mx$, which is 0 by (@eq-11-9-c); and an integral of $b_n \sin nx \sin mx$, which is $b_m \pi$ if $n = m$ and 0 if $n \neq m$, by (@eq-11-9-b). This implies (@eq-11-6-b) (with $n$ denoted by $m$). This completes the proof of the Euler formulas (@eq-11-6-0)–(@eq-11-6-b) for the Fourier coefficients.

### Convergence and Sum of a Fourier Series
The class of functions that can be represented by Fourier series is surprisingly large and general. Sufficient conditions valid in most applications are as follows.

**THEOREM 2 Representation by a Fourier Series**
Let $f(x)$ be periodic with period $2\pi$ and piecewise continuous (see Sec. 6.1) in the interval $[-\pi, \pi]$. Furthermore, let $f(x)$ have a left-hand derivative and a right-hand derivative at each point of that interval. Then the Fourier series (@eq-11-5) of $f(x)$ [with coefficients (@eq-11-6-0)–(@eq-11-6-b)] converges. Its sum is $f(x)$, except at points $x_0$ where $f(x)$ is discontinuous. There the sum of the series is the average of the left- and right-hand limits of $f(x)$ at $x_0$.

> **Footnote 2:** The left-hand limit of $f(x)$ at $x_0$ is defined as the limit of $f(x)$ as $x$ approaches $x_0$ from the left and is commonly denoted by $f(x_0 - 0)$. Thus
> $$
> f(x_0 - 0) = \lim_{h \to 0^+} f(x_0 - h)
> $$
> as $h \to 0$ through positive values. The right-hand limit is denoted by $f(x_0 + 0)$ and
> $$
> f(x_0 + 0) = \lim_{h \to 0^+} f(x_0 + h)
> $$
> as $h \to 0$ through positive values. The left- and right-hand derivatives of $f(x)$ at $x_0$ are defined as the limits of
> $$
> \frac{f(x_0 - h) - f(x_0 - 0)}{-h} \quad \text{and} \quad \frac{f(x_0 + h) - f(x_0 + 0)}{h}
> $$
> respectively, as $h \to 0$ through positive values. Of course if $f(x)$ is continuous at $x_0$, the last term in both numerators is simply $f(x_0)$.

![Fig. 262: Left- and right-hand limits $f(1 - 0) = 1$, $f(1 + 0) = 1/2$ of the function $f(x) = x^2$ if $x < 1$ and $x/2$ if $x \ge 1$](../images/chapter11/fig-11-262.png){#fig-11-262}

**PROOF**
We prove convergence, but only for a continuous function $f(x)$ having continuous first and second derivatives. And we do not prove that the sum of the series is $f(x)$ because these proofs are much more advanced; see, for instance, Ref. [C12] listed in App. 1.

Integrating (@eq-11-6-a) by parts, we obtain
$$
a_n = \frac{1}{n\pi} \left. f(x) \sin nx \right|_{-\pi}^{\pi} - \frac{1}{n\pi} \int_{-\pi}^{\pi} f'(x) \sin nx \, dx
$$
The first term on the right is zero. Another integration by parts gives
$$
a_n = \frac{1}{n^2\pi} \left. f'(x) \cos nx \right|_{-\pi}^{\pi} - \frac{1}{n^2\pi} \int_{-\pi}^{\pi} f''(x) \cos nx \, dx
$$
The first term on the right is zero because of the periodicity and continuity of $f'(x)$. Since $f''(x)$ is continuous in the interval of integration, we have $|f''(x)| < M$ for an appropriate constant $M$. Furthermore, $|\cos nx| \le 1$. It follows that
$$
|a_n| = \frac{1}{n^2\pi} \left| \int_{-\pi}^{\pi} f''(x) \cos nx \, dx \right| \le \frac{1}{n^2\pi} \int_{-\pi}^{\pi} M \, dx = \frac{2M}{n^2}
$$
Similarly, $|b_n| \le \frac{2M}{n^2}$ for all $n$. Hence the absolute value of each term of the Fourier series of $f(x)$ is at most equal to the corresponding term of the series
$$
|a_0| + 2M \left( 1 + \frac{1}{2^2} + \frac{1}{3^2} + \dots \right)
$$
which is convergent. Hence that Fourier series converges and the proof is complete. $\square$

(Readers already familiar with uniform convergence will see that, by the Weierstrass test in Sec. 15.5, under our present assumptions the Fourier series converges uniformly, and our derivation of (6) by integrating term by term is then justified by Theorem 3 of Sec. 15.5.)

### EXAMPLE 2 Convergence at a Jump as Indicated in Theorem 2 {#ex-11-2}
The rectangular wave in Example 1 has a jump at $x = 0$. Its left-hand limit there is $-k$ and its right-hand limit is $k$ (@fig-11-261). Hence the average of these limits is 0. The Fourier series (@eq-11-8) of the wave does indeed converge to this value when $x = 0$ because then all its terms are 0. Similarly for the other jumps. This is in agreement with Theorem 2. $\blacksquare$

**Summary.** A Fourier series of a given function $f(x)$ of period $2\pi$ is a series of the form (@eq-11-5) with coefficients given by the Euler formulas (@eq-11-6-0)–(@eq-11-6-b). Theorem 2 gives conditions that are sufficient for this series to converge and at each $x$ to have the value $f(x)$, except at discontinuities of $f(x)$, where the series equals the arithmetic mean of the left-hand and right-hand limits of $f(x)$ at that point.

## PROBLEM SET 11.1 {#sec-11-1-problems}

### 1–5 PERIOD, FUNDAMENTAL PERIOD
The fundamental period is the smallest positive period. Find it for:
1. $\cos x, \sin x, \cos 2x, \sin 2x, \cos \pi x, \sin \pi x, \cos 2\pi x, \sin 2\pi x$
2. $\cos nx, \sin nx, \cos \frac{2\pi n x}{k}, \sin \frac{2\pi n x}{k}$
3. If $f(x)$ and $g(x)$ have period $p$, show that $h(x) = af(x) + bg(x)$ ($a, b$ constant) has the period $p$. Thus all functions of period $p$ form a vector space.
4. **Change of scale.** If $f(x)$ has period $p$, show that $f(ax)$, $a \neq 0$, and $f(x/b)$, $b \neq 0$, are periodic functions of $x$ of periods $p/a$ and $bp$, respectively. Give examples.
5. Show that $f(x) = \text{const}$ is periodic with any period but has no fundamental period.

### 6–10 GRAPHS OF $2\pi$-PERIODIC FUNCTIONS
Sketch or graph $f(x)$ which for $-\pi < x < \pi$ is given as follows:
6. $f(x) = |x|$
7. $f(x) = |\sin x|, \quad f(x) = \sin |x|$
8. $f(x) = e^{-|x|}, \quad f(x) = |e^{-x}|$
9. $f(x) = \begin{cases} x & \text{if } -\pi < x < 0 \\ \pi - x & \text{if } 0 < x < \pi \end{cases}$
10. $f(x) = \begin{cases} -\cos^2 x & \text{if } -\pi < x < 0 \\ \cos^2 x & \text{if } 0 < x < \pi \end{cases}$

11. **Calculus review.** Review integration techniques for integrals as they are likely to arise from the Euler formulas, for instance, definite integrals of $e^{-2x} \cos nx$, $x \cos nx$, $x^2 \sin nx$, etc.

### 12–21 FOURIER SERIES
Find the Fourier series of the given function $f(x)$, which is assumed to have the period $2\pi$. Show the details of your work. Sketch or graph the partial sums up to that including $S_5$ (or $S_3$ if the terms are zero).
12. $f(x)$ in Prob. 6
13. $f(x)$ in Prob. 9
14. $f(x) = x^2 \quad (-\pi < x < \pi)$
15. $f(x) = x^2 \quad (0 < x < 2\pi)$
16. $f(x) = \begin{cases} 0 & \text{if } -\pi < x < 0 \\ x & \text{if } 0 < x < \pi \end{cases}$
17. $f(x) = \begin{cases} 0 & \text{if } -\pi < x < 0 \\ \pi & \text{if } 0 < x < \pi \end{cases}$
18. $f(x) = \begin{cases} -k & \text{if } -\pi < x < 0 \\ k & \text{if } 0 < x < \pi \end{cases}$ (Wait, isn't this Example 1?)
19. $f(x) = \begin{cases} 0 & \text{if } -\pi < x < -\pi/2 \\ 1 & \text{if } -\pi/2 < x < \pi/2 \\ 0 & \text{if } \pi/2 < x < \pi \end{cases}$
20. $f(x) = \begin{cases} 0 & \text{if } -\pi < x < 0 \\ 1 & \text{if } 0 < x < \pi/2 \\ 0 & \text{if } \pi/2 < x < \pi \end{cases}$
21. $f(x) = \begin{cases} -1 & \text{if } -\pi < x < -\pi/2 \\ 1 & \text{if } -\pi/2 < x < \pi/2 \\ -1 & \text{if } \pi/2 < x < \pi \end{cases}$

22. **CAS EXPERIMENT. Graphing.** Write a program for graphing partial sums of the following series. Guess from the graph what $f(x)$ the series may represent. Confirm or disprove your guess by using the Euler formulas.
    (a) $2 \left( \sin x - \frac{1}{2} \sin 2x + \frac{1}{3} \sin 3x - \frac{1}{4} \sin 4x + \dots \right)$
    (b) $\frac{1}{2} - \frac{4}{\pi^2} \left( \cos x + \frac{1}{9} \cos 3x + \frac{1}{25} \cos 5x + \dots \right)$
    (c) $\frac{2}{3}\pi^2 - 4 \left( \cos x - \frac{1}{4} \cos 2x + \frac{1}{9} \cos 3x - \frac{1}{16} \cos 4x + \dots \right)$
23. **Discontinuities.** Verify the last statement in Theorem 2 for the discontinuities of $f(x)$ in Prob. 21.
24. **CAS EXPERIMENT. Orthogonality.** Integrate and graph the integral of the product $\cos mx \cos nx$ (with various integer $m$ and $n$ of your choice) from $-a$ to $a$ as a function of $a$ and conclude orthogonality of $\cos mx$ and $\cos nx$ ($m \neq n$) for $a = \pi$ from the graph. For what $m$ and $n$ will you get orthogonality for $a = \pi/2$? $a = \pi/3$, $a = \pi/4$? Other $a$? Extend the experiment to $\sin mx \sin nx$ and $\cos mx \sin nx$.
25. **CAS EXPERIMENT. Order of Fourier Coefficients.** The order seems to be $1/n$ if $f$ is discontinuous, and $1/n^2$ if $f$ is continuous but $f' = df/dx$ is discontinuous, $1/n^3$ if $f$ and $f'$ are continuous but $f''$ is discontinuous, etc. Try to verify this for examples. Try to prove it by integrating the Euler formulas by parts. What is the practical significance of this?
"""

with open(ch11_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Section 11.1 written successfully!")
