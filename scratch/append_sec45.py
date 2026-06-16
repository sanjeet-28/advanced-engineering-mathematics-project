def append_text(path, text):
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n" + text + "\n")

text = r"""
## 4.5 Qualitative Methods for Nonlinear Systems {#sec-4-5}

Qualitative methods are methods of obtaining qualitative information on solutions without actually solving a system. These methods are particularly valuable for systems whose solution by analytic methods is difficult or impossible. This is the case for many practically important nonlinear systems
$$
\mathbf{y}' = \mathbf{f}(\mathbf{y}), \quad \text{thus} \quad \begin{aligned} y'_1 &= f_1(y_1, y_2) \\ y'_2 &= f_2(y_1, y_2) \end{aligned}
$$ {#eq-4-59}
In this section we extend phase plane methods, as just discussed, from linear systems to nonlinear systems (@eq-4-59). We assume that (@eq-4-59) is **autonomous**, that is, the independent variable $t$ does not occur explicitly. (All examples in the last section are autonomous.)

We shall again exhibit entire families of solutions. This is an advantage over numeric methods, which give only one (approximate) solution at a time.

Concepts needed from the last section are the **phase plane** (the $y_1 y_2$-plane), **trajectories** (solution curves of (@eq-4-59) in the phase plane), the **phase portrait** of (@eq-4-59) (the totality of these trajectories), and **critical points** of (@eq-4-59) (points $(y_1, y_2)$ at which both $f_1$ and $f_2$ are zero).

Now (@eq-4-59) may have several critical points. Our approach shall be to discuss one critical point after another. If a critical point is not at the origin, then, for technical convenience, we shall move this point to the origin before analyzing the point. More formally, if $P_0$ is a critical point with $(P_0: (a, b))$ not at the origin $(0, 0)$, then we apply the translation
$$
\tilde{y}_1 = y_1 - a, \quad \tilde{y}_2 = y_2 - b
$$
which moves $P_0$ to $(0, 0)$ as desired. Thus we can assume $P_0$ to be the origin $(0, 0)$, and for simplicity we continue to write $(y_1, y_2)$ (instead of $(\tilde{y}_1, \tilde{y}_2)$). We also assume that $P_0$ is **isolated**, that is, it is the only critical point of (@eq-4-59) within a (sufficiently small) disk with center at the origin. If (@eq-4-59) has only finitely many critical points, that is automatically true. (Explain!)

### Linearization of Nonlinear Systems

How can we determine the kind and stability property of a critical point $P_0: (0, 0)$ of (@eq-4-59)? In most cases this can be done by **linearization** of (@eq-4-59) near $P_0$, writing (@eq-4-59) as $\mathbf{y}' = \mathbf{f}(\mathbf{y}) = \mathbf{Ay} + \mathbf{h}(\mathbf{y})$ and dropping $\mathbf{h}$, as follows.

Since $P_0$ is critical, $f_1(0, 0) = 0$, $f_2(0, 0) = 0$, so that $f_1$ and $f_2$ have no constant terms and we can write
$$
\mathbf{y}' = \mathbf{Ay} + \mathbf{h}(\mathbf{y}), \quad \text{thus} \quad \begin{aligned} y'_1 &= a_{11}y_1 + a_{12}y_2 + h_1(y_1, y_2) \\ y'_2 &= a_{21}y_1 + a_{22}y_2 + h_2(y_1, y_2) \end{aligned}
$$ {#eq-4-60}
$\mathbf{A}$ is constant (independent of $t$) since (@eq-4-59) is autonomous. One can prove the following (proof in Ref. [A7], pp. 375–388, listed in App. 1).

**THEOREM 1 Linearization**
If $f_1$ and $f_2$ in (@eq-4-59) are continuous and have continuous partial derivatives in a neighborhood of the critical point $P_0: (0, 0)$, and if $\det \mathbf{A} \neq 0$ in (@eq-4-60), then the kind and stability of the critical point of (@eq-4-59) are the same as those of the linearized system
$$
\mathbf{y}' = \mathbf{Ay}, \quad \text{thus} \quad \begin{aligned} y'_1 &= a_{11}y_1 + a_{12}y_2 \\ y'_2 &= a_{21}y_1 + a_{22}y_2 \end{aligned}
$$ {#eq-4-61}
**Exceptions** occur if $\mathbf{A}$ has equal or pure imaginary eigenvalues; then (@eq-4-59) may have the same kind of critical point as (@eq-4-61) or a spiral point.

### EXAMPLE 1 Free Undamped Pendulum. Linearization

@fig-4-93a shows a pendulum consisting of a body of mass $m$ (the bob) and a rod of length $L$. Determine the locations and types of the critical points. Assume that the mass of the rod and air resistance are negligible.

**Solution.**

**Step 1. Setting up the mathematical model.** Let $u$ denote the angular displacement, measured counterclockwise from the equilibrium position. The weight of the bob is $mg$ ($g$ the acceleration of gravity). It causes a restoring force $-mg \sin u$ tangent to the curve of motion (circular arc) of the bob. By Newton's second law, at each instant this force is balanced by the force of acceleration $mL\ddot{u}$; hence the resultant of these two forces is zero, and we obtain as the mathematical model
$$
mL\ddot{u} + mg \sin u = 0
$$
Dividing this by $mL$, we have
$$
\ddot{u} + k \sin u = 0, \quad k = \frac{g}{L}
$$ {#eq-4-62}
When $u$ is very small, we can approximate $\sin u$ rather accurately by $u$ and obtain the approximate solution $u \approx A \cos \sqrt{k}\,t + B \sin \sqrt{k}\,t$, but the exact solution for any $u$ is not an elementary function.

**Step 2. Critical points. Linearization.** To obtain a system of ODEs, we set $u = y_1, \dot{u} = y_2$. Then from (@eq-4-62) we obtain a nonlinear system (@eq-4-59) of the form
$$
\begin{aligned}
y'_1 &= f_1(y_1, y_2) = y_2 \\
y'_2 &= f_2(y_1, y_2) = -k \sin y_1
\end{aligned}
$$ {#eq-4-62star}
The right sides are both zero when $y_2 = 0$ and $\sin y_1 = 0$. This gives infinitely many critical points $(n\pi, 0)$, where $n = 0, \pm 1, \pm 2, \dots$. We consider $(0, 0)$. Since the Maclaurin series is
$$
\sin y_1 = y_1 - \frac{1}{6}y_1^3 + \dots \approx y_1
$$
the linearized system at $(0, 0)$ is
$$
y'_1 = y_2, \quad y'_2 = -ky_1, \quad \text{thus} \quad \mathbf{y}' = \mathbf{Ay} = \begin{bmatrix} 0 & 1 \\ -k & 0 \end{bmatrix} \mathbf{y}
$$
To apply our criteria in Sec. 4.4 we calculate $p = a_{11} + a_{22} = 0$ and $q = \det \mathbf{A} = k = g/L > 0$, and $\Delta = p^2 - 4q = -4k < 0$. From this and Table 4.1(c) in Sec. 4.4 we conclude that $(0, 0)$ is a center, which is always stable. Since $\sin y_1$ is periodic with period $2\pi$, the critical points $(0, 0), (\pm 2\pi, 0), (\pm 4\pi, 0), \dots$ are all centers.

**Step 3. Critical points $(\pm \pi, 0), (\pm 3\pi, 0), \dots$. Linearization.** We now consider the critical point $(\pi, 0)$, setting $u - \pi = y_1$ and linearizing:
$$
\sin u = \sin(y_1 + \pi) = -\sin y_1 \approx -y_1
$$
$(u - \pi)' = \dot{u} = y_2$. This gives the new linearized system at $(\pi, 0)$:
$$
y'_1 = y_2, \quad y'_2 = ky_1, \quad \text{thus} \quad \mathbf{y}' = \mathbf{Ay} = \begin{bmatrix} 0 & 1 \\ k & 0 \end{bmatrix} \mathbf{y}
$$
We see that $p = 0, q = -k < 0$, and $\Delta = 4k > 0$. Hence, by Table 4.1(b), this gives a saddle point, which is always unstable. Because of periodicity, the critical points $(\pm\pi, 0), (\pm 3\pi, 0), \dots$ are all saddle points.

These results agree with the impression we get from @fig-4-93b. $\blacksquare$

![Fig. 93: Example 1. (a) Pendulum. (b) Solution curves $y_2(y_1)$ of (4) in the phase plane](../images/chapter4/fig-4-93.png){#fig-4-93}

### EXAMPLE 2 Linearization of the Damped Pendulum Equation

To gain further experience in investigating critical points, as another practically important case, let us see how Example 1 changes when we add a damping term (damping proportional to the angular velocity) to equation (@eq-4-62), so that it becomes
$$
\ddot{u} + c\dot{u} + k \sin u = 0
$$ {#eq-4-63}
where $c \geq 0$ and $k > 0$ (which includes our previous case of no damping, $c = 0$). Setting $u = y_1, \dot{u} = y_2$ as before, we obtain the nonlinear system (use $\ddot{u} = y'_2$)
$$
\begin{aligned}
y'_1 &= y_2 \\
y'_2 &= -k\sin y_1 - cy_2
\end{aligned}
$$
We see that the critical points have the same locations as before, namely $(0, 0), (\pm\pi, 0), (\pm 2\pi, 0), \dots$. We consider $(0, 0)$. Linearizing as in Example 1, we get the linearized system at $(0, 0)$:
$$
y'_1 = y_2, \quad y'_2 = -ky_1 - cy_2, \quad \text{thus} \quad \mathbf{y}' = \mathbf{Ay} = \begin{bmatrix} 0 & 1 \\ -k & -c \end{bmatrix} \mathbf{y}
$$ {#eq-4-64}
This is identical with the system in Example 2 of Sec. 4.4, except for the (positive!) factor $m$ (and except for the physical meaning of $y_1$). Hence for $c = 0$ (no damping) we have a center (see @fig-4-93b), for small damping we have a spiral point (see @fig-4-94), and so on.

We now consider the critical point $(\pi, 0)$. We set $u - \pi = y_1$ and linearize:
$$
\sin u = \sin(y_1 + \pi) = -\sin y_1 \approx -y_1
$$
$(u - \pi)' = \dot{u} = y_2$. This gives the new linearized system at $(\pi, 0)$:
$$
y'_1 = y_2, \quad y'_2 = ky_1 - cy_2, \quad \text{thus} \quad \mathbf{y}' = \mathbf{Ay} = \begin{bmatrix} 0 & 1 \\ k & -c \end{bmatrix} \mathbf{y}
$$ {#eq-4-65}
For our criteria in Sec. 4.4 we calculate $p = a_{11} + a_{22} = -c$ and $q = \det \mathbf{A} = -k$ and $\Delta = p^2 - 4q = c^2 + 4k$.

This gives the following results for the critical point at $(\pi, 0)$:

- **No damping.** $c = 0, \ p = 0, \ q = -k < 0, \ \Delta > 0$, a saddle point. See @fig-4-93b.
- **Damping.** $c > 0, \ p = -c < 0, \ q = -k < 0, \ \Delta > 0$, a saddle point. See @fig-4-94.

Since $\sin y_1$ is periodic with period $2\pi$, the critical points $(0, 0), (\pm 2\pi, 0), \dots$ are of the same type as $(0, 0)$, and the critical points $(\pm\pi, 0), (\pm 3\pi, 0), \dots$ are of the same type as $(\pi, 0)$, so that our task is finished.

@fig-4-94 shows the trajectories in the case of damping. What we see agrees with our physical intuition. Indeed, damping means loss of energy. Hence instead of the closed trajectories of periodic solutions in @fig-4-93b we now have trajectories spiraling around one of the critical points $(0, 0), (\pm 2\pi, 0), \dots$. Even the wavy trajectories corresponding to whirly motions eventually spiral around one of these points. Furthermore, there are no more trajectories that connect critical points (as there were in the undamped case for the saddle points). $\blacksquare$

![Fig. 94: Trajectories in the phase plane for the damped pendulum in Example 2](../images/chapter4/fig-4-94.png){#fig-4-94}

### Lotka–Volterra Population Model

### EXAMPLE 3 Predator–Prey Population Model^3^

This model concerns two species, say, rabbits and foxes, and the foxes prey on the rabbits.

**Step 1. Setting up the model.** We assume the following.

1. Rabbits have unlimited food supply. Hence, if there were no foxes, their number $y_1(t)$ would grow exponentially, $y'_1 = ay_1$.
2. Actually, $y'_1$ is decreased because of the kill by foxes, say, at a rate proportional to $y_1 y_2$, where $y_2(t)$ is the number of foxes. Hence $y'_1 = ay_1 - by_1 y_2$, where $a > 0$ and $b > 0$.
3. If there were no rabbits, then $y_2(t)$ would exponentially decrease to zero, $y'_2 = -ly_2$. However, $y'_2$ is increased by a rate proportional to the number of encounters between predator and prey; together we have $y'_2 = -ly_2 + ky_1 y_2$, where $k > 0$ and $l > 0$.

This gives the (nonlinear!) **Lotka–Volterra system**
$$
\begin{aligned}
y'_1 &= f_1(y_1, y_2) = ay_1 - by_1 y_2 \\
y'_2 &= f_2(y_1, y_2) = ky_1 y_2 - ly_2
\end{aligned}
$$ {#eq-4-66}

> ^3^ Introduced by ALFRED J. LOTKA (1880–1949), American biophysicist, and VITO VOLTERRA (1860–1940), Italian mathematician, the initiator of functional analysis.

**Step 2. Critical point $(0, 0)$. Linearization.** We see from (@eq-4-66) that the critical points are the solutions of
$$
f_1(y_1, y_2) = y_1(a - by_2) = 0, \quad f_2(y_1, y_2) = y_2(ky_1 - l) = 0
$$ {#eq-4-66star}
The solutions are $(y_1, y_2) = (0, 0)$ and $(l/k,\ a/b)$. We consider $(0, 0)$. Dropping $by_1 y_2$ and $ky_1 y_2$ from (@eq-4-66) gives the linearized system
$$
\mathbf{y}' = \begin{bmatrix} a & 0 \\ 0 & -l \end{bmatrix} \mathbf{y}
$$
Its eigenvalues are $\lambda_1 = a > 0$ and $\lambda_2 = -l < 0$. They have opposite signs, so that we get a saddle point.

**Step 3. Critical point $(l/k, a/b)$. Linearization.** We set $y_1 = \tilde{y}_1 + l/k$, $y_2 = \tilde{y}_2 + a/b$. Then the critical point $(l/k, a/b)$ corresponds to $(\tilde{y}_1, \tilde{y}_2) = (0, 0)$. Since $y'_1 = \tilde{y}'_1, y'_2 = \tilde{y}'_2$, we obtain from (@eq-4-66) [factorized as in (@eq-4-66star)]
$$
\begin{aligned}
\tilde{y}'_1 &= a\tilde{y}_1 + \frac{l}{k}\left(a - b\left(\tilde{y}_2 + \frac{a}{b}\right)\right) = -\frac{bl}{k}\tilde{y}_2 - b\tilde{y}_1\tilde{y}_2 \\
\tilde{y}'_2 &= ak\tilde{y}_1 + \left(k\tilde{y}_1 - l + \frac{ak}{b}\right)\tilde{y}_2 \cdot\frac{k}{a}\tilde{y}_1
\end{aligned}
$$
Dropping the two nonlinear terms $k\tilde{y}_1\tilde{y}_2$ and $b\tilde{y}_1\tilde{y}_2$, we have the linearized system
$$
\begin{aligned}
\tilde{y}'_1 &= -\frac{bl}{k}\tilde{y}_2 \\
\tilde{y}'_2 &= \frac{ak}{b}\tilde{y}_1
\end{aligned}
$$ {#eq-4-66doublestar}
The left side of (a) times the right side of (b) must equal the right side of (a) times the left side of (b):
$$
-\frac{bl}{k}\tilde{y}_2\tilde{y}'_2 = \frac{ak}{b}\tilde{y}_1\tilde{y}'_1
$$
By integration,
$$
\frac{ak}{b}\tilde{y}_1^2 + \frac{bl}{k}\tilde{y}_2^2 = \text{const}
$$
This is a family of ellipses, so that the critical point of the linearized system (@eq-4-66doublestar) is a center (@fig-4-95). It can be shown, by a complicated analysis, that the nonlinear system (@eq-4-66) also has a center (rather than a spiral point) at $(l/k, a/b)$ surrounded by closed trajectories (not ellipses).

We see that the predators and prey have a cyclic variation about the critical point. Let us move counterclockwise around the ellipse, beginning at the right vertex, where the rabbits have a maximum number. Foxes are sharply increasing in number until they reach a maximum at the upper vertex, and the number of rabbits is then sharply decreasing until it reaches a minimum at the left vertex, and so on. Cyclic variations of this kind have been observed in nature, for example, for lynx and snowshoe hare near the Hudson Bay, with a cycle of about 10 years.

For models of more complicated situations and a systematic discussion, see C. W. Clark, *Mathematical Bioeconomics: The Mathematics of Conservation*, 3rd ed. Hoboken, NJ, Wiley, 2010. $\blacksquare$

![Fig. 95: Ecological equilibrium point and trajectory of the linearized Lotka–Volterra system (7**)](../images/chapter4/fig-4-95.png){#fig-4-95}

### Transformation to a First-Order Equation in the Phase Plane

Another phase plane method is based on the idea of transforming a second-order autonomous ODE (an ODE in which $t$ does not occur explicitly)
$$
F\!\left(y, y', y''\right) = 0
$$ {#eq-4-67}
to first order by taking $y_1 = y$ as the independent variable, setting $y' = y_2$ and transforming $y'' = \ddot{y}$ by the chain rule,
$$
y'' = \ddot{y} = \frac{d^2 y}{dt^2} = \frac{dy'}{dt} = \frac{dy_2}{dt} = \frac{dy_2}{dy_1} \cdot \frac{dy_1}{dt} = \frac{dy_2}{dy_1} \cdot y_2
$$
Then the ODE (@eq-4-67) becomes of first order,
$$
F\!\left(y_1, y_2, \frac{dy_2}{dy_1} y_2\right) = 0
$$ {#eq-4-68}
and can sometimes be solved or treated by direction fields. We illustrate this for the equation in Example 1 and shall gain much more insight into the behavior of solutions.

### EXAMPLE 4 An ODE (8) for the Free Undamped Pendulum

If in (@eq-4-62) we set $y = y_1$ (the angular velocity) and use $\ddot{u} = \frac{dy_2}{dy_1} y_2$, we get $y_2\frac{dy_2}{dy_1} = -k\sin y_1$.

Separation of variables gives $y_2 \, dy_2 = -k\sin y_1 \, dy_1$. By integration,
$$
\frac{1}{2}y_2^2 = k\cos y_1 + C \quad (C \text{ constant})
$$ {#eq-4-69}
Multiplying this by $mL^2$, we get
$$
\frac{1}{2}m(Ly_2)^2 - mL^2 k \cos y_1 = mL^2 C
$$
We see that these three terms are energies. Indeed, $y_2$ is the angular velocity, so that $Ly_2$ is the velocity and the first term is the kinetic energy. The second term (including the minus sign) is the potential energy of the pendulum, and $mL^2 C$ is its total energy, which is constant, as expected from the law of conservation of energy, because there is no damping (no loss of energy). The type of motion depends on the total energy, hence on $C$, as follows.

@fig-4-93b shows trajectories for various values of $C$. These graphs continue periodically with period $2\pi$ to the left and to the right. We see that some of them are ellipse-like and closed, others are wavy, and there are two trajectories (passing through the saddle points $(\pm\pi, 0), (\pm 3\pi, 0), \dots$) that separate those two types of trajectories. From (@eq-4-69) we see that the smallest possible $C$ is $-k$; then $y_2 = 0$ and $\cos y_1 = 1$, so that the pendulum is at rest. The pendulum will change its direction of motion if there are points at which $y_2 = y'_1 = \dot{u} = 0$. Then by (@eq-4-69), $k\cos y_1 + C = 0$. If $|C| < k$, then $\cos y_1 = -C/k$ and $-1 < -C/k < 1$. Hence if $-k < C < k$, then the pendulum reverses its direction for an angle $y_1 = \pm \arccos(-C/k)$, and for these values of $C$ with $|C| < k$ the pendulum oscillates. This corresponds to the closed trajectories in the figure. However, if $C > k$, then $k\cos y_1 + C = 0$ is impossible and the pendulum makes a whirly motion that appears as a wavy trajectory in the $y_1 y_2$-plane. Finally, the value $C = k$ corresponds to the two "separating trajectories" in @fig-4-93b connecting the saddle points. $\blacksquare$

The phase plane method of deriving a single first-order equation (@eq-4-68) may be of practical interest not only when (@eq-4-68) can be solved (as in Example 4) but also when a solution is not possible and we have to utilize direction fields (Sec. 1.2). We illustrate this with a very famous example:

### EXAMPLE 5 Self-Sustained Oscillations. Van der Pol Equation

There are physical systems such that for small oscillations, energy is fed into the system, whereas for large oscillations, energy is taken from the system. In other words, large oscillations will be damped, whereas for small oscillations there is "negative damping" (feeding of energy into the system). For physical reasons we expect such a system to approach a periodic behavior, which will thus appear as a closed trajectory in the phase plane, called a **limit cycle**. A differential equation describing such vibrations is the famous **van der Pol equation**^4^
$$
\ddot{u} - \mu(1 - u^2)\dot{u} + u = 0 \quad (\mu > 0, \ \text{constant})
$$ {#eq-4-70}
It first occurred in the study of electrical circuits containing vacuum tubes. For $\mu = 0$ this becomes $\ddot{u} + u = 0$ and we obtain harmonic oscillations. Let $\mu > 0$. The damping term has the factor $(1 - u^2)$. This is negative for small oscillations, when $|u| < 1$, so that we have "negative damping," is zero for $|u| = 1$ (no damping), and is positive if $|u| > 1$ (positive damping, loss of energy). If $\mu$ is small, we expect a limit cycle that is almost a circle because then our equation differs but little from $\ddot{u} + u = 0$. If $\mu$ is large, the limit cycle will probably look different.

Setting $y = y_1, y' = y_2$ and using $y'' = \frac{dy_2}{dy_1}y_2$ as in (@eq-4-68), we have from (@eq-4-70)
$$
\frac{dy_2}{dy_1} y_2 - \mu(1 - y_1^2)y_2 + y_1 = 0
$$ {#eq-4-71}
The isoclines in the $y_1 y_2$-plane (the phase plane) are the curves $dy_2/dy_1 = K = \text{const}$, that is,
$$
\frac{dy_2}{dy_1} y_2 - \mu(1 - y_1^2)y_2 + y_1 = 0 \quad \Rightarrow \quad Ky_2 - \mu(1-y_1^2)y_2 + y_1 = 0
$$
Solving algebraically for $y_2$, we see that the isoclines are given by
$$
y_2 = \frac{y_1}{\mu(1 - y_1^2) - K} \quad (\text{Figs. 96, 97})
$$

@fig-4-96 shows some isoclines when $\mu$ is small, $\mu = 0.1$, the limit cycle (almost a circle), and two (blue) trajectories approaching it, one from the outside and the other from the inside, of which only the initial portion, a small spiral, is shown. Due to this approach by trajectories, a limit cycle differs conceptually from a closed curve (a trajectory) surrounding a center, which is not approached by trajectories. For larger $\mu$ the limit cycle no longer resembles a circle, and the trajectories approach it more rapidly than for smaller $\mu$. @fig-4-97 illustrates this for $\mu = 1$. $\blacksquare$

> ^4^ BALTHASAR VAN DER POL (1889–1959), Dutch physicist and engineer.

![Fig. 96: Direction field for the van der Pol equation with $\mu = 0.1$ in the phase plane, showing also the limit cycle and two trajectories. See also Fig. 8 in Sec. 1.2](../images/chapter4/fig-4-96.png){#fig-4-96}

![Fig. 97: Direction field for the van der Pol equation with $\mu = 1$ in the phase plane, showing also the limit cycle and two trajectories approaching it](../images/chapter4/fig-4-97.png){#fig-4-97}

## PROBLEM SET 4.5 {#sec-4-5-problems}

1. **Pendulum.** To what state (position, speed, direction of motion) do the four points of intersection of a closed trajectory with the axes in @fig-4-93b correspond? The point of intersection of a wavy curve with the $y_1$-axis?
2. **Limit cycle.** What is the essential difference between a limit cycle and a closed trajectory surrounding a center?
3. **CAS EXPERIMENT. Deformation of Limit Cycle.** Convert the van der Pol equation to a system. Graph the limit cycle and some approaching trajectories for $\mu = 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0$. Try to observe how the limit cycle changes its form continuously if you vary $\mu$ continuously. Describe in words how the limit cycle is deformed with growing $\mu$.

### 4–8 CRITICAL POINTS. LINEARIZATION
Find the location and type of all critical points by linearization. Show the details of your work.
4. $\begin{aligned} y'_1 &= y_2 \\ y'_2 &= 4y_1 - y_1^2 \end{aligned}$
5. $\begin{aligned} y'_1 &= y_2 \\ y'_2 &= y_2 \end{aligned}$
6. $\begin{aligned} y'_1 &= -y_1 + y_2 - y_2^2 \\ y'_2 &= -y_1 - y_2 \end{aligned}$
7. $\begin{aligned} y'_1 &= y_2 \\ y'_2 &= -y_1 - y_1^2 \end{aligned}$
8. $\begin{aligned} y'_1 &= y_2 - y_2^2 \\ y'_2 &= y_1 - y_1^2 \end{aligned}$

### 9–13 CRITICAL POINTS OF ODEs
Find the location and type of all critical points by first converting the ODE to a system and then linearizing it.
9. $y'' + 9y - y^3 = 0$
10. $y'' - 9y + y^3 = 0$
11. $y'' + y - y^3 = 0$
12. $y'' + \cos y = 0$
13. $y'' + \sin y = 0$

14. **TEAM PROJECT. Self-sustained oscillations.**
(a) **Van der Pol equation.** Determine the type of the critical point at $(0, 0)$ when $\mu > 0, \ \mu = 0, \ \mu < 0$.
(b) **Rayleigh equation.**^5^ Show that the Rayleigh equation
$$
\ddot{Y} - \mu\!\left(1 - \tfrac{1}{3}\dot{Y}^2\right)\dot{Y} + Y = 0 \quad (\mu > 0)
$$
also describes self-sustained oscillations and that by differentiating it and setting $y = \dot{Y}$ one obtains the van der Pol equation.
(c) **Duffing equation.** The Duffing equation is
$$
\ddot{y} + \omega_0^2 y + by^3 = 0
$$
where usually $|b|$ is small, thus characterizing a small deviation of the restoring force from linearity. $b > 0$ and $b < 0$ are called the cases of a hard spring and a soft spring, respectively. Find the equation of the trajectories in the phase plane. (Note that for all $b > 0$ these curves are closed.)

> ^5^ LORD RAYLEIGH (JOHN WILLIAM STRUTT) (1842–1919), English physicist and mathematician, professor at Cambridge and London, known by his important contributions to the theory of waves, elasticity theory, hydrodynamics, and various other branches of applied mathematics and theoretical physics. In 1904 he was awarded the Nobel Prize in physics.

15. **Trajectories.** Write the ODE $y'' - 4y + y^3 = 0$ as a system, solve it for $y_2$ as a function of $y_1$, and sketch or graph some of the trajectories in the phase plane.

![Fig. 98: Trajectories in Problem 15](../images/chapter4/fig-4-98.png){#fig-4-98}
"""

append_text(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\chapters\ch4.qmd", text)
