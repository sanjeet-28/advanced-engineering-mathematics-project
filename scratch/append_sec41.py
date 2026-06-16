def append_text(path, text):
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n" + text + "\n")

text = r"""
## 4.1 Systems of ODEs as Models in Engineering Applications {#sec-4-1}

We show how systems of ODEs are of practical importance as follows. We first illustrate how systems of ODEs can serve as models in various applications. Then we show how a higher order ODE (with the highest derivative standing alone on one side) can be reduced to a first-order system.

### EXAMPLE 1 Mixing Problem Involving Two Tanks

A mixing problem involving a single tank is modeled by a single ODE, and you may first review the corresponding Example 3 in Sec. 1.3 because the principle of modeling will be the same for two tanks. The model will be a system of two first-order ODEs.

![Fig. 78: Fertilizer content in Tanks $T_1$ (lower curve) and $T_2$ (upper curve)](../images/chapter4/fig-4-78.png){#fig-4-78}

Tanks $T_1$ and $T_2$ in @fig-4-78 contain initially 100 gal of water each. In $T_1$ the water is pure, whereas 150 lb of fertilizer are dissolved in $T_2$. By circulating liquid at a rate of 2 gal/min and stirring (to keep the mixture uniform) the amounts of fertilizer $y_1(t)$ in $T_1$ and $y_2(t)$ in $T_2$ change with time $t$. How long should we let the liquid circulate so that $T_1$ will contain at least half as much fertilizer as there will be left in $T_2$?

**Solution.**

**Step 1. Setting up the model.** As for a single tank, the time rate of change of $y_1(t)$ equals inflow minus outflow. Similarly for tank $T_2$. From @fig-4-78 we see that:
$$
\begin{aligned}
\text{Tank } T_1: \quad y'_1 &= \text{Inflow/min} - \text{Outflow/min} = 2 \frac{y_2}{100} - 2 \frac{y_1}{100} \\
\text{Tank } T_2: \quad y'_2 &= \text{Inflow/min} - \text{Outflow/min} = 2 \frac{y_1}{100} - 2 \frac{y_2}{100}
\end{aligned}
$$
Hence the mathematical model of our mixture problem is the system of first-order ODEs
$$
\begin{aligned}
\text{Tank } T_1: \quad y'_1 &= -0.02y_1 + 0.02y_2 \\
\text{Tank } T_2: \quad y'_2 &= 0.02y_1 - 0.02y_2
\end{aligned}
$$ {#eq-4-18}
As a vector equation with column vector $\mathbf{y} = \begin{bmatrix} y_1 \\ y_2 \end{bmatrix}$ and matrix $\mathbf{A}$ this becomes
$$
\mathbf{y}' = \mathbf{Ay}, \quad \text{where} \quad \mathbf{A} = \begin{bmatrix} -0.02 & 0.02 \\ 0.02 & -0.02 \end{bmatrix}
$$

**Step 2. General solution.** As for a single equation, we try an exponential function of $t$,
$$
\mathbf{y} = \mathbf{x} e^{\lambda t}, \quad \text{then} \quad \mathbf{y}' = \lambda \mathbf{x} e^{\lambda t} = \mathbf{Ax} e^{\lambda t}
$$
Dividing the last equation by $e^{\lambda t}$ and interchanging the left and right sides, we obtain
$$
\mathbf{Ax} = \lambda \mathbf{x}
$$
We need nontrivial solutions (solutions that are not identically zero). Hence we have to look for eigenvalues and eigenvectors of $\mathbf{A}$. The eigenvalues are the solutions of the characteristic equation
$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} -0.02 - \lambda & 0.02 \\ 0.02 & -0.02 - \lambda \end{vmatrix} = (-0.02 - \lambda)^2 - 0.02^2 = \lambda(\lambda + 0.04) = 0
$$ {#eq-4-19}
We see that $\lambda_1 = 0$ (which can very well happen—don't get mixed up—it is eigenvectors that must not be zero) and $\lambda_2 = -0.04$. Eigenvectors are obtained from $(\mathbf{A} - \lambda\mathbf{I})\mathbf{x} = \mathbf{0}$ as in Sec. 4.0 with $\lambda = \lambda_1$ and $\lambda = \lambda_2$. For our present $\mathbf{A}$ this gives (we need only the first equation in the system):
$$
\begin{aligned}
\text{For } \lambda_1 = 0: \quad -0.02x_1 + 0.02x_2 = 0 &\implies x_1 = x_2 \\
\text{For } \lambda_2 = -0.04: \quad (-0.02 + 0.04)x_1 + 0.02x_2 = 0 &\implies x_1 = -x_2
\end{aligned}
$$
respectively. Hence $x_1 = x_2$ and $x_1 = -x_2$, respectively, and we can take $\mathbf{x}^{(1)} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ and $\mathbf{x}^{(2)} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$. This gives two eigenvectors corresponding to $\lambda_1$ and $\lambda_2$, respectively.

From $\mathbf{y} = \mathbf{x} e^{\lambda t}$ and the superposition principle (which continues to hold for systems of homogeneous linear ODEs) we thus obtain a solution
$$
\mathbf{y}(t) = c_1 \mathbf{x}^{(1)} e^{\lambda_1 t} + c_2 \mathbf{x}^{(2)} e^{\lambda_2 t} = c_1 \begin{bmatrix} 1 \\ 1 \end{bmatrix} + c_2 \begin{bmatrix} 1 \\ -1 \end{bmatrix} e^{-0.04t}
$$ {#eq-4-20}
where $c_1$ and $c_2$ are arbitrary constants. Later we shall call this a general solution.

**Step 3. Use of initial conditions.** The initial conditions are $y_1(0) = 0$ (no fertilizer in tank $T_1$) and $y_2(0) = 150$. From this and (@eq-4-20) with $t = 0$ we obtain
$$
\mathbf{y}(0) = c_1 \begin{bmatrix} 1 \\ 1 \end{bmatrix} + c_2 \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} c_1 + c_2 \\ c_1 - c_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 150 \end{bmatrix}
$$
In components this is
$$
\begin{aligned}
c_1 + c_2 &= 0 \\
c_1 - c_2 &= 150
\end{aligned}
$$
The solution is $c_1 = 75, c_2 = -75$. This gives the answer
$$
\mathbf{y}(t) = 75 \begin{bmatrix} 1 \\ 1 \end{bmatrix} - 75 \begin{bmatrix} 1 \\ -1 \end{bmatrix} e^{-0.04t}
$$
In components,
$$
\begin{aligned}
y_1(t) &= 75 - 75e^{-0.04t} \quad \text{(Tank } T_1\text{, lower curve)} \\
y_2(t) &= 75 + 75e^{-0.04t} \quad \text{(Tank } T_2\text{, upper curve)}
\end{aligned}
$$
Figure 78 shows the exponential increase of $y_1$ and the exponential decrease of $y_2$ to the common limit 75 lb. Did you expect this for physical reasons? Can you physically explain why the curves look "symmetric"? Would the limit change if initially $T_1$ contained 100 lb of fertilizer and $T_2$ contained 50 lb?

**Step 4. Answer.** $T_1$ contains half the fertilizer amount of $T_2$ if it contains $1/3$ of the total amount, that is, 50 lb. Thus
$$
y_1(t) = 75 - 75e^{-0.04t} = 50 \implies e^{-0.04t} = \frac{1}{3} \implies t = \frac{\ln 3}{0.04} \approx 27.5 \text{ min}
$$
Hence the fluid should circulate for at least about half an hour. $\blacksquare$

### EXAMPLE 2 Electrical Network

Find the currents $I_1(t)$ and $I_2(t)$ in the network in @fig-4-79. Assume all currents and charges to be zero at $t = 0$, the instant when the switch is closed.

**Solution.**

![Fig. 79: Electrical network in Example 2](../images/chapter4/fig-4-79.png){#fig-4-79}

**Step 1. Setting up the mathematical model.** The model of this network is obtained from Kirchhoff's Voltage Law, as in Sec. 2.9 (where we considered single circuits). Let $I_1(t)$ and $I_2(t)$ be the currents in the left and right loops, respectively. In the left loop, the voltage drops are over the inductor $L I'_1 = I'_1$ [V] and over the resistor $R_1(I_1 - I_2) = 4(I_1 - I_2)$ [V], the difference because $I_1$ and $I_2$ flow through the resistor in opposite directions. By Kirchhoff's Voltage Law the sum of these drops equals the voltage of the battery; that is, $I'_1 + 4(I_1 - I_2) = 12$, hence
$$
I'_1 = -4I_1 + 4I_2 + 12
$$ {#eq-4-21}
In the right loop, the voltage drops are $R_2 I_2 = 6I_2$ [V] and $R_1(I_2 - I_1) = 4(I_2 - I_1)$ [V] over the resistors and $\frac{1}{C}\int I_2 \, dt = 4\int I_2 \, dt$ [V] over the capacitor, and their sum is zero,
$$
6I_2 + 4(I_2 - I_1) + 4\int I_2 \, dt = 0
$$
or
$$
10I_2 - 4I_1 + 4\int I_2 \, dt = 0
$$
Division by 10 and differentiation gives $I'_2 - 0.4I'_1 + 0.4I_2 = 0$.

To simplify the solution process, we first get rid of $I'_1$, which by (@eq-4-21) equals $-4I_1 + 4I_2 + 12$. Substitution into the present ODE gives
$$
I'_2 - 0.4(-4I_1 + 4I_2 + 12) + 0.4I_2 = 0
$$
and by simplification
$$
I'_2 = -1.6I_1 + 1.2I_2 + 4.8
$$ {#eq-4-22}
In matrix form, (@eq-4-21) and (@eq-4-22) is (we write $\mathbf{J}$ since $\mathbf{I}$ is the unit matrix)
$$
\mathbf{J}' = \mathbf{AJ} + \mathbf{g}, \quad \text{where} \quad \mathbf{J} = \begin{bmatrix} I_1 \\ I_2 \end{bmatrix}, \quad \mathbf{A} = \begin{bmatrix} -4.0 & 4.0 \\ -1.6 & 1.2 \end{bmatrix}, \quad \mathbf{g} = \begin{bmatrix} 12.0 \\ 4.8 \end{bmatrix}
$$ {#eq-4-23}

**Step 2. Solving (@eq-4-23).** Because of the vector $\mathbf{g}$ this is a nonhomogeneous system, and we try to proceed as for a single ODE, solving first the homogeneous system $\mathbf{J}' = \mathbf{AJ}$ (thus $\mathbf{g} = \mathbf{0}$) by substituting $\mathbf{J} = \mathbf{x} e^{\lambda t}$. This gives
$$
\mathbf{J}' = \lambda \mathbf{x} e^{\lambda t} = \mathbf{Ax} e^{\lambda t}, \quad \text{hence} \quad \mathbf{Ax} = \lambda \mathbf{x}
$$
Hence, to obtain a nontrivial solution, we again need the eigenvalues and eigenvectors. For the present matrix $\mathbf{A}$ they are derived in Example 1 in Sec. 4.0:
$$
\lambda_1 = -2, \quad \mathbf{x}^{(1)} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}; \quad \lambda_2 = -0.8, \quad \mathbf{x}^{(2)} = \begin{bmatrix} 1 \\ 0.8 \end{bmatrix}
$$
Hence a general solution of the homogeneous system is
$$
\mathbf{J}_h = c_1 \mathbf{x}^{(1)} e^{-2t} + c_2 \mathbf{x}^{(2)} e^{-0.8t}
$$
For a particular solution of the nonhomogeneous system (@eq-4-23), since $\mathbf{g}$ is constant, we try a constant column vector $\mathbf{J}_p = \mathbf{a}$ with components $a_1, a_2$. Then $\mathbf{J}'_p = \mathbf{0}$, and substitution into (@eq-4-23) gives $\mathbf{Aa} + \mathbf{g} = \mathbf{0}$; in components,
$$
\begin{aligned}
-4.0a_1 + 4.0a_2 + 12.0 &= 0 \\
-1.6a_1 + 1.2a_2 + 4.8 &= 0
\end{aligned}
$$
The solution is $a_1 = 3, a_2 = 0$; thus $\mathbf{a} = \begin{bmatrix} 3 \\ 0 \end{bmatrix}$. Hence
$$
\mathbf{J} = \mathbf{J}_h + \mathbf{J}_p = c_1 \mathbf{x}^{(1)} e^{-2t} + c_2 \mathbf{x}^{(2)} e^{-0.8t} + \mathbf{a}
$$
in components,
$$
\begin{aligned}
I_1(t) &= 2c_1e^{-2t} + c_2e^{-0.8t} + 3 \\
I_2(t) &= c_1e^{-2t} + 0.8c_2e^{-0.8t}
\end{aligned}
$$ {#eq-4-24}

The initial conditions give
$$
\begin{aligned}
I_1(0) &= 2c_1 + c_2 + 3 = 0 \\
I_2(0) &= c_1 + 0.8c_2 = 0
\end{aligned}
$$
Hence $c_1 = -4$ and $c_2 = 5$. As the solution of our problem we thus obtain
$$
\mathbf{J} = -4\mathbf{x}^{(1)}e^{-2t} + 5\mathbf{x}^{(2)}e^{-0.8t} + \mathbf{a}
$$
In components (cf. @fig-4-80),
$$
\begin{aligned}
I_1(t) &= -8e^{-2t} + 5e^{-0.8t} + 3 \\
I_2(t) &= -4e^{-2t} + 4e^{-0.8t}
\end{aligned}
$$ {#eq-4-25}

Now comes an important idea, on which we shall elaborate further, beginning in Sec. 4.3. @fig-4-80a shows $I_1(t)$ and $I_2(t)$ as two separate curves. @fig-4-80b shows these two currents as a single curve in the $I_1I_2$-plane. This is a parametric representation with time $t$ as the parameter. It is often important to know in which sense such a curve is traced. This can be indicated by an arrow in the sense of increasing $t$, as is shown.

The $I_1I_2$-plane is called the **phase plane** of our system (@eq-4-23), and the curve in @fig-4-80b is called a **trajectory**. We shall see that such "phase plane representations" are far more important than graphs as in @fig-4-80a because they will give a much better qualitative overall impression of the general behavior of whole families of solutions, not merely of one solution as in the present case. $\blacksquare$

![Fig. 80: Currents in Example 2](../images/chapter4/fig-4-80.png){#fig-4-80}

**Remark.** In both examples, by growing the dimension of the problem (from one tank to two tanks or one circuit to two circuits) we also increased the number of ODEs (from one ODE to two ODEs). This "growth" in the problem being reflected by an "increase" in the mathematical model is attractive and affirms the quality of our mathematical modeling and theory.

### Conversion of an $n$th-Order ODE to a System

We show that an $n$th-order ODE of the general form (@eq-4-26) (see Theorem 1) can be converted to a system of $n$ first-order ODEs. This is practically and theoretically important—practically because it permits the study and solution of single ODEs by methods for systems, and theoretically because it opens a way of including the theory of higher order ODEs into that of first-order systems. This conversion is another reason for the importance of systems, in addition to their use as models in various basic applications. The idea of the conversion is simple and straightforward, as follows.

**THEOREM 1 Conversion of an ODE**

An $n$th-order ODE
$$
y^{(n)} = F(t, y, y', \dots, y^{(n-1)})
$$ {#eq-4-26}
can be converted to a system of $n$ first-order ODEs by setting
$$
y_1 = y, \quad y_2 = y', \quad y_3 = y'', \quad \dots, \quad y_n = y^{(n-1)}
$$ {#eq-4-27}
This system is of the form
$$
\begin{aligned}
y'_1 &= y_2 \\
y'_2 &= y_3 \\
&\ \ \vdots \\
y'_{n-1} &= y_n \\
y'_n &= F(t, y_1, y_2, \dots, y_n)
\end{aligned}
$$ {#eq-4-28}

**PROOF.** The first $n-1$ of these $n$ ODEs follow immediately from (@eq-4-27) by differentiation: $y'_1 = y' = y_2$, $y'_2 = y'' = y_3$, etc. Also, $y'_n = y^{(n)}$ by (@eq-4-27), so that the last equation in (@eq-4-28) results from the given ODE (@eq-4-26). $\blacksquare$

### EXAMPLE 3 Mass on a Spring

To gain confidence in the conversion method, let us apply it to an old friend of ours, modeling the free motions of a mass on a spring (see Sec. 2.4)
$$
my'' + cy' + ky = 0 \quad \text{or} \quad y'' = -\frac{c}{m}y' - \frac{k}{m}y
$$
For this ODE (@eq-4-26) the system (@eq-4-28) is linear and homogeneous,
$$
\begin{aligned}
y'_1 &= y_2 \\
y'_2 &= -\frac{k}{m}y_1 - \frac{c}{m}y_2
\end{aligned}
$$
Setting $\mathbf{y} = \begin{bmatrix} y_1 \\ y_2 \end{bmatrix}$, we get in matrix form
$$
\mathbf{y}' = \mathbf{Ay} = \begin{bmatrix} 0 & 1 \\ -k/m & -c/m \end{bmatrix} \mathbf{y}
$$ {#eq-4-29}
The characteristic equation is
$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} -\lambda & 1 \\ -k/m & -c/m - \lambda \end{vmatrix} = \lambda^2 + \frac{c}{m}\lambda + \frac{k}{m} = 0
$$
It agrees with that in Sec. 2.4. For an illustrative computation, let $m = 1$, $c = 2$, and $k = 0.75$. Then
$$
\lambda^2 + 2\lambda + 0.75 = (\lambda + 0.5)(\lambda + 1.5) = 0
$$
This gives the eigenvalues $\lambda_1 = -0.5$ and $\lambda_2 = -1.5$. Eigenvectors follow from the first equation in $(\mathbf{A} - \lambda\mathbf{I})\mathbf{x} = \mathbf{0}$, which is $(-\lambda)x_1 + x_2 = 0$. For $\lambda = \lambda_1 = -0.5$ this gives $0.5x_1 + x_2 = 0$, say, $\mathbf{x}^{(1)} = \begin{bmatrix} 2 \\ -1 \end{bmatrix}$. For $\lambda = \lambda_2 = -1.5$ it gives $1.5x_1 + x_2 = 0$, say, $\mathbf{x}^{(2)} = \begin{bmatrix} 1 \\ -1.5 \end{bmatrix}$. These eigenvectors give
$$
\mathbf{y} = c_1 \begin{bmatrix} 2 \\ -1 \end{bmatrix} e^{-0.5t} + c_2 \begin{bmatrix} 1 \\ -1.5 \end{bmatrix} e^{-1.5t}
$$
This vector solution has the first component
$$
y = y_1 = 2c_1e^{-0.5t} + c_2e^{-1.5t}
$$
which is the expected solution. The second component is its derivative
$$
y_2 = y'_1 = y' = -c_1e^{-0.5t} - 1.5c_2e^{-1.5t}
$$ $\blacksquare$

## PROBLEM SET 4.1 {#sec-4-1-problems}

### 1–6 MIXING PROBLEMS
1. Find out, without calculation, whether doubling the flow rate in Example 1 has the same effect as halving the tank sizes. (Give a reason.)
2. What happens in Example 1 if we replace $T_1$ by a tank containing 200 gal of water and 150 lb of fertilizer dissolved in it?
3. Derive the eigenvectors in Example 1 without consulting this book.
4. In Example 1 find a "general solution" for any ratio $a = \text{(flow rate)}/\text{(tank size)}$, tank sizes being equal. Comment on the result.
5. If you extend Example 1 by a tank $T_3$ of the same size as the others and connected to $T_1$ and $T_2$ by two tubes with flow rates as between $T_1$ and $T_2$, what system of ODEs will you get?
6. Find a "general solution" of the system in Prob. 5.

### 7–9 ELECTRICAL NETWORK
In Example 2 find the currents:
7. If the initial currents are 0 A and $-3$ A (minus meaning that $I_2$ flows against the direction of the arrow).
8. If the capacitance is changed to $C = 5/27$ F. (General solution only.)
9. If the initial currents in Example 2 are 28 A and 14 A.

### 10–13 CONVERSION TO SYSTEMS
Find a general solution of the given ODE (a) by first converting it to a system, (b) as given. Show the details of your work.
10. $y'' + 3y' + 2y = 0$
11. $4y'' - 15y' - 4y = 0$
12. $y''' + 2y'' - y' - 2y = 0$
13. $y'' + 2y' - 24y = 0$

### 14 TEAM PROJECT. Two Masses on Springs.
(a) Set up the model for the (undamped) system in @fig-4-81.
(b) Solve the system of ODEs obtained. *Hint.* Try $\mathbf{y} = \mathbf{x} e^{vt}$ and set $v^2 = \lambda$. Proceed as in Example 1 or 2.
(c) Describe the influence of initial conditions on the possible kind of motions.

![Fig. 81: Mechanical system in Team Project](../images/chapter4/fig-4-81.png){#fig-4-81}

### 15 CAS EXPERIMENT. Electrical Network.
(a) In Example 2 choose a sequence of values of $C$ that increases beyond bound, and compare the corresponding sequences of eigenvalues of $\mathbf{A}$. What limits of these sequences do your numeric values (approximately) suggest?
(b) Find these limits analytically.
(c) Explain your result physically.
(d) Below what value (approximately) must you decrease $C$ to get vibrations?
"""

append_text(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\chapters\ch4.qmd", text)
