def append_text(path, text):
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n" + text + "\n")

text = r"""
## 4.4 Criteria for Critical Points. Stability {#sec-4-4}

We continue our discussion of homogeneous linear systems with constant coefficients
$$
\mathbf{y}' = \mathbf{A}\mathbf{y}
$$ {#eq-4-52}
Let us review where we are. From Sec. 4.3 we have:
$$
\begin{aligned}
y'_1 &= a_{11} y_1 + a_{12} y_2 \\
y'_2 &= a_{21} y_1 + a_{22} y_2
\end{aligned}
$$
From the examples in the last section, we have seen that we can obtain an overview of families of solution curves if we represent them parametrically as $\mathbf{y}(t) = [y_1(t)\ \ y_2(t)]^T$ and graph them as curves in the $y_1 y_2$-plane, called the phase plane. Such a curve is called a trajectory of (@eq-4-52), and their totality is known as the phase portrait of (@eq-4-52).

Now we have seen that solutions are of the form $\mathbf{y}(t) = \mathbf{x} e^{\lambda t}$. Substitution into (@eq-4-52) gives $\lambda \mathbf{x} e^{\lambda t} = \mathbf{Ax} e^{\lambda t}$. Dropping the common factor $e^{\lambda t}$, we have
$$
\mathbf{Ax} = \lambda \mathbf{x}
$$ {#eq-4-53}
Hence $\mathbf{y}(t) = \mathbf{x} e^{\lambda t}$ is a (nonzero) solution of (@eq-4-52) if $\lambda$ is an eigenvalue of $\mathbf{A}$ and $\mathbf{x}$ a corresponding eigenvector.

Our examples in the last section show that the general form of the phase portrait is determined to a large extent by the type of critical point of the system (@eq-4-52) defined as a point at which $dy_2/dy_1$ becomes undetermined, $0/0$; here [see (@eq-4-45) in Sec. 4.3]:
$$
\frac{dy_2}{dy_1} = \frac{y'_2}{y'_1} = \frac{a_{21}y_1 + a_{22}y_2}{a_{11}y_1 + a_{12}y_2}
$$ {#eq-4-54}
We also recall from Sec. 4.3 that there are various types of critical points.

What is now new, is that we shall see how these types of critical points are related to the eigenvalues. The latter are solutions $\lambda_1$ and $\lambda_2$ of the characteristic equation
$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} a_{11} - \lambda & a_{12} \\ a_{21} & a_{22} - \lambda \end{vmatrix} = \lambda^2 - (a_{11} + a_{22})\lambda + \det \mathbf{A} = 0
$$
which we write as
$$
\lambda^2 - p\lambda + q = 0
$$ {#eq-4-55}
This is a quadratic equation with coefficients $p$, $q$ and discriminant $\Delta$ given by
$$
p = a_{11} + a_{22}, \quad q = \det \mathbf{A} = a_{11}a_{22} - a_{12}a_{21}, \quad \Delta = p^2 - 4q
$$ {#eq-4-56}
From algebra we know that the solutions of this equation are
$$
\lambda_1 = \frac{1}{2}(p + \sqrt{\Delta}), \quad \lambda_2 = \frac{1}{2}(p - \sqrt{\Delta})
$$ {#eq-4-57}
Furthermore, the product representation of the equation gives
$$
\lambda^2 - p\lambda + q = (\lambda - \lambda_1)(\lambda - \lambda_2) = \lambda^2 - (\lambda_1 + \lambda_2)\lambda + \lambda_1\lambda_2
$$
Hence $p$ is the sum and $q$ the product of the eigenvalues. Also $\lambda_1 - \lambda_2 = \sqrt{\Delta}$ from (@eq-4-57). Together,
$$
p = \lambda_1 + \lambda_2, \quad q = \lambda_1\lambda_2, \quad \Delta = (\lambda_1 - \lambda_2)^2
$$ {#eq-4-58}
This gives the criteria in Table 4.1 for classifying critical points. A derivation will be indicated later in this section.

### Table 4.1: Eigenvalue Criteria for Critical Points
| Name | Real/Complex | Mathematical Conditions |
| --- | --- | --- |
| (a) Node | Real, same sign | $q > 0, \ \Delta \ge 0$ |
| (b) Saddle point | Real, opposite signs | $q < 0$ |
| (c) Center | Pure imaginary | $p = 0, \ q > 0$ |
| (d) Spiral point | Complex, not pure imaginary | $p \neq 0, \ \Delta < 0$ |

### Stability

Critical points may also be classified in terms of their stability. Stability concepts are basic in engineering and other applications. They are suggested by physics, where stability means, roughly speaking, that a small change (a small disturbance) of a physical system at some instant changes the behavior of the system only slightly at all future times $t$. For critical points, the following concepts are appropriate.

**DEFINITIONS: Stable, Unstable, Stable and Attractive**

A critical point $P_0$ of (@eq-4-52) is called **stable**^2^ if, roughly, all trajectories of (@eq-4-52) that at some instant are close to $P_0$ remain close to $P_0$ at all future times; precisely: if for every disk $D_\epsilon$ of radius $\epsilon > 0$ with center $P_0$ there is a disk $D_\delta$ of radius $\delta > 0$ with center $P_0$ such that every trajectory of (@eq-4-52) that has a point $P_1$ (corresponding to $t = t_1$, say) in $D_\delta$ has all its points $P(t)$ corresponding to $t > t_1$ in $D_\epsilon$. See @fig-4-90.

$P_0$ is called **unstable** if $P_0$ is not stable.

$P_0$ is called **stable and attractive** (or **asymptotically stable**) if $P_0$ is stable and every trajectory that has a point in $D_\delta$ approaches $P_0$ as $t \to \infty$. See @fig-4-91.

> ^2^ In the sense of the Russian mathematician ALEXANDER MICHAILOVICH LYAPUNOV (1857–1918), whose work was fundamental in stability theory for ODEs. This is perhaps the most appropriate definition of stability (and the only we shall use), but there are others, too.

Classification criteria for critical points in terms of stability are given in Table 4.2. Both tables are summarized in the stability chart in @fig-4-92. In this chart region of instability is dark blue.

![Fig. 90: Stable critical point $P_0$ of (1) (The trajectory initiating at $P_1$ stays in the disk of radius $\epsilon$.)](../images/chapter4/fig-4-90.png){#fig-4-90}

![Fig. 91: Stable and attractive critical point $P_0$ of (1)](../images/chapter4/fig-4-91.png){#fig-4-91}

### Table 4.2: Stability Criteria for Critical Points
| Type of Stability | Conditions on eigenvalues | Conditions on $p$ and $q$ |
| --- | --- | --- |
| (a) Stable and attractive | Real negative or complex with negative real part | $q > 0, \ p < 0$ |
| (b) Stable | Pure imaginary or stable and attractive | $q > 0, \ p \le 0$ |
| (c) Unstable | Positive real eigenvalues or positive real part | $q < 0$ or $p > 0$ |

![Fig. 92: Stability chart of the system (1) with $p, q, \Delta$ defined in (5)](../images/chapter4/fig-4-92.png){#fig-4-92}

We indicate how the criteria in Tables 4.1 and 4.2 are obtained. If $q = \lambda_1\lambda_2 > 0$, both of the eigenvalues are positive or both are negative or complex conjugates. If also $p = \lambda_1 + \lambda_2 < 0$, both are negative or have a negative real part. Hence $P_0$ is stable and attractive. The reasoning for the other two lines in Table 4.2 is similar.

If $\Delta < 0$, the eigenvalues are complex conjugates, say, $\lambda_1 = \alpha + i\beta$ and $\lambda_2 = \alpha - i\beta$. If also $p = \lambda_1 + \lambda_2 = 2\alpha < 0$, this gives a spiral point that is stable and attractive. If $p = 2\alpha > 0$, this gives an unstable spiral point.

If $p = 0$, then $\lambda_2 = -\lambda_1$ and $q = -\lambda_1^2$. If also $q > 0$, then $\lambda_1^2 < 0$, so that $\lambda_1$, and thus $\lambda_2$, must be pure imaginary. This gives periodic solutions, their trajectories being closed curves around $P_0$, which is a center.

### EXAMPLE 1 Application of the Criteria in Tables 4.1 and 4.2

In Example 1, Sec. 4.3, we have $\mathbf{y}' = \begin{bmatrix} -3 & 1 \\ 1 & -3 \end{bmatrix} \mathbf{y}$. Here $p = -6, \ q = 8, \ \Delta = 4$. By Table 4.1(a) we have a node, which is stable and attractive by Table 4.2(a). $\blacksquare$

### EXAMPLE 2 Free Motions of a Mass on a Spring

What kind of critical point does $my'' + cy' + ky = 0$ in Sec. 2.4 have?

**Solution.** Division by $m$ gives $y'' + \frac{c}{m}y' + \frac{k}{m}y = 0$. To get a system, set $y_1 = y, \ y_2 = y'$ (see Sec. 4.1). Then $y'_1 = y_2, \ y'_2 = -\frac{k}{m}y_1 - \frac{c}{m}y_2$. Hence
$$
\mathbf{y}' = \begin{bmatrix} 0 & 1 \\ -k/m & -c/m \end{bmatrix} \mathbf{y}
$$
The characteristic equation is $\lambda^2 + \frac{c}{m}\lambda + \frac{k}{m} = 0$. We see that
$$
p = -\frac{c}{m}, \quad q = \frac{k}{m}, \quad \Delta = \left(\frac{c}{m}\right)^2 - 4\frac{k}{m}
$$
From this and Tables 4.1 and 4.2 we obtain the following results. Note that in the last three cases the discriminant plays an essential role.

- **No damping.** $c = 0, \ p = 0, \ q > 0$, a center.
- **Underdamping.** $c^2 < 4mk, \ p < 0, \ q > 0, \ \Delta < 0$, a stable and attractive spiral point.
- **Critical damping.** $c^2 = 4mk, \ p < 0, \ q > 0, \ \Delta = 0$, a stable and attractive node.
- **Overdamping.** $c^2 > 4mk, \ p < 0, \ q > 0, \ \Delta > 0$, a stable and attractive node. $\blacksquare$

## PROBLEM SET 4.4 {#sec-4-4-problems}

### 1–10 TYPE AND STABILITY OF CRITICAL POINT
Determine the type and stability of the critical point. Then find a real general solution and sketch or graph some of the trajectories in the phase plane. Show the details of your work.
1. $\begin{aligned} y'_1 &= y_1 \\ y'_2 &= 2y_2 \end{aligned}$
2. $\begin{aligned} y'_1 &= -4y_1 \\ y'_2 &= -3y_2 \end{aligned}$
3. $\begin{aligned} y'_1 &= y_2 \\ y'_2 &= 2y_2 \end{aligned}$
4. $\begin{aligned} y'_1 &= 2y_1 + y_2 \\ y'_2 &= 5y_1 - 2y_2 \end{aligned}$
5. $\begin{aligned} y'_1 &= -6y_1 - y_2 \\ y'_2 &= -9y_1 - 6y_2 \end{aligned}$
6. $\begin{aligned} y'_1 &= y_1 + 2y_2 \\ y'_2 &= 2y_1 + y_2 \end{aligned}$
7. $\begin{aligned} y'_1 &= -2y_1 + 2y_2 \\ y'_2 &= -2y_1 - 2y_2 \end{aligned}$
8. $\begin{aligned} y'_1 &= -y_1 + 4y_2 \\ y'_2 &= 3y_1 - 2y_2 \end{aligned}$
9. $\begin{aligned} y'_1 &= y_2 \\ y'_2 &= -9y_1 \end{aligned}$
10. $\begin{aligned} y'_1 &= 4y_1 + y_2 \\ y'_2 &= 4y_1 + 4y_2 \end{aligned}$

### 11–18 TRAJECTORIES OF SYSTEMS AND SECOND-ORDER ODEs. CRITICAL POINTS
11. **Damped oscillations.** Solve $y'' + 2y' + 2y = 0$. What kind of curves are the trajectories?
12. **Harmonic oscillations.** Solve $y'' + 9y = 0$. Find the trajectories. Sketch or graph some of them.
13. **Types of critical points.** Discuss the critical points in Examples 2–5 of Sec. 4.3 by using Tables 4.1 and 4.2.
14. **Transformation of parameter.** What happens to the critical point in Example 1 if you introduce $\tau = -t$ as a new independent variable?
15. **Perturbation of center.** What happens in Example 4 of Sec. 4.3 if you change $\mathbf{A}$ to $\mathbf{A} + 0.1\mathbf{I}$, where $\mathbf{I}$ is the unit matrix?
16. **Perturbation of center.** If a system has a center as its critical point, what happens if you replace the matrix $\mathbf{A}$ by $\tilde{\mathbf{A}} = \mathbf{A} + k\mathbf{I}$ with any real number $k \neq 0$ (representing measurement errors in the diagonal entries)?
17. **Perturbation.** The system in Example 4 in Sec. 4.3 has a center as its critical point. Replace each $a_{jk}$ in Example 4, Sec. 4.3, by $a_{jk} + b$. Find values of $b$ such that you get (a) a saddle point, (b) a stable and attractive node, (c) a stable and attractive spiral, (d) an unstable spiral, (e) an unstable node.
18. **CAS EXPERIMENT. Phase Portraits.** Graph phase portraits for the systems in Prob. 17 with the values of $b$ suggested in the answer. Try to illustrate how the phase portrait changes "continuously" under a continuous change of $b$.
19. **WRITING PROBLEM. Stability.** Stability concepts are basic in physics and engineering. Write a two-part report of 3 pages each (A) on general applications in which stability plays a role (be as precise as you can), and (B) on material related to stability in this section. Use your own formulations and examples; do not copy.
20. **Stability chart.** Locate the critical points of the systems (10)–(14) in Sec. 4.3 and of Probs. 1, 3, 5 in this problem set on the stability chart.
"""

append_text(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\chapters\ch4.qmd", text)
