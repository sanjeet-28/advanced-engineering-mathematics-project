def append_text(path, text):
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n" + text + "\n")

text = r"""
## 4.3 Constant-Coefficient Systems. Phase Plane Method {#sec-4-3}

Continuing, we now assume that our homogeneous linear system
$$
\mathbf{y}' = \mathbf{A}\mathbf{y}
$$ {#eq-4-38}
under discussion has constant coefficients, so that the $n \times n$ matrix $\mathbf{A} = [a_{jk}]$ has entries not depending on $t$. We want to solve (@eq-4-38). Now a single ODE $y' = ky$ has the solution $y = C e^{kt}$. So let us try
$$
\mathbf{y} = \mathbf{x} e^{\lambda t}
$$ {#eq-4-39}
Substitution into (@eq-4-38) gives $\lambda \mathbf{x} e^{\lambda t} = \mathbf{Ax} e^{\lambda t}$. Dividing by $e^{\lambda t}$, we obtain the eigenvalue problem
$$
\mathbf{A}\mathbf{x} = \lambda \mathbf{x}
$$ {#eq-4-40}
Thus the nontrivial solutions of (@eq-4-38) (solutions that are not zero vectors) are of the form (@eq-4-39), where $\lambda$ is an eigenvalue of $\mathbf{A}$ and $\mathbf{x}$ is a corresponding eigenvector.

We assume that $\mathbf{A}$ has a linearly independent set of $n$ eigenvectors. This holds in most applications, in particular if $\mathbf{A}$ is symmetric or skew-symmetric ($\mathbf{A}^T = -\mathbf{A}$) or has $n$ different eigenvalues.

Let those eigenvectors be $\mathbf{x}^{(1)}, \dots, \mathbf{x}^{(n)}$ and let them correspond to eigenvalues $\lambda_1, \dots, \lambda_n$ (which may be all different, or some—or even all—may be equal). Then the corresponding solutions (@eq-4-39) are
$$
\mathbf{y}^{(1)} = \mathbf{x}^{(1)} e^{\lambda_1 t}, \quad \dots, \quad \mathbf{y}^{(n)} = \mathbf{x}^{(n)} e^{\lambda_n t}
$$ {#eq-4-41}
Their Wronskian $W = W(\mathbf{y}^{(1)}, \dots, \mathbf{y}^{(n)})$ is given by
$$
W = \begin{vmatrix}
x_1^{(1)} e^{\lambda_1 t} & \dots & x_1^{(n)} e^{\lambda_n t} \\
x_2^{(1)} e^{\lambda_1 t} & \dots & x_2^{(n)} e^{\lambda_n t} \\
\vdots & \ddots & \vdots \\
x_n^{(1)} e^{\lambda_1 t} & \dots & x_n^{(n)} e^{\lambda_n t}
\end{vmatrix} = e^{(\lambda_1 + \dots + \lambda_n)t} \begin{vmatrix}
x_1^{(1)} & \dots & x_1^{(n)} \\
x_2^{(1)} & \dots & x_2^{(n)} \\
\vdots & \ddots & \vdots \\
x_n^{(1)} & \dots & x_n^{(n)}
\end{vmatrix}
$$
On the right, the exponential function is never zero, and the determinant is not zero either because its columns are the $n$ linearly independent eigenvectors. This proves the following theorem, whose assumption is true if the matrix $\mathbf{A}$ is symmetric or skew-symmetric, or if the $n$ eigenvalues of $\mathbf{A}$ are all different.

**THEOREM 1 General Solution**
If the constant matrix $\mathbf{A}$ in the system (@eq-4-38) has a linearly independent set of $n$ eigenvectors, then the corresponding solutions in (@eq-4-41) form a basis of solutions of (@eq-4-38), and the corresponding general solution is
$$
\mathbf{y} = c_1 \mathbf{x}^{(1)} e^{\lambda_1 t} + \dots + c_n \mathbf{x}^{(n)} e^{\lambda_n t}
$$ {#eq-4-42}

### How to Graph Solutions in the Phase Plane

We shall now concentrate on systems (@eq-4-38) with constant coefficients consisting of two ODEs
$$
\mathbf{y}' = \mathbf{A}\mathbf{y}; \quad \text{in components,} \quad \begin{aligned} y'_1 &= a_{11} y_1 + a_{12} y_2 \\ y'_2 &= a_{21} y_1 + a_{22} y_2 \end{aligned}
$$
Of course, we can graph solutions of this system,
$$
\mathbf{y}(t) = \begin{bmatrix} y_1(t) \\ y_2(t) \end{bmatrix}
$$
as two curves over the $t$-axis, one for each component of $\mathbf{y}(t)$. (@fig-4-80a in Sec. 4.1 shows an example.) But we can also graph them as a single curve in the $y_1 y_2$-plane. This is a parametric representation (parametric equation) with parameter $t$. (See @fig-4-80b for an example. Many more follow. Parametric equations also occur in calculus.) Such a curve is called a **trajectory** (or sometimes an orbit or path) of the system. The $y_1 y_2$-plane is called the **phase plane**.^1^ If we fill the phase plane with trajectories, we obtain the so-called **phase portrait** of the system.

Studies of solutions in the phase plane have become quite important, along with advances in computer graphics, because a phase portrait gives a good general qualitative impression of the entire family of solutions. Consider the following example, in which we develop such a phase portrait.

> ^1^ A name that comes from physics, where it is the $y$-$(mv)$-plane, used to plot a motion in terms of position $y$ and velocity $y' = v$ ($m = \text{mass}$); but the name is now used quite generally for the $y_1 y_2$-plane. The use of the phase plane is a qualitative method, a method of obtaining general qualitative information on solutions without actually solving an ODE or a system. This method was created by HENRI POINCARÉ (1854–1912), a great French mathematician, whose work was also fundamental in complex analysis, divergent series, topology, and astronomy.

### EXAMPLE 1 Trajectories in the Phase Plane (Phase Portrait)

Find and graph solutions of the system
$$
\mathbf{y}' = \mathbf{A}\mathbf{y} = \begin{bmatrix} -3 & 1 \\ 1 & -3 \end{bmatrix} \mathbf{y}, \quad \text{thus} \quad \begin{aligned} y'_1 &= -3y_1 + y_2 \\ y'_2 &= y_1 - 3y_2 \end{aligned}
$$ {#eq-4-43}

**Solution.** By substituting $\mathbf{y} = \mathbf{x} e^{\lambda t}$ and $\mathbf{y}' = \lambda \mathbf{x} e^{\lambda t}$ and dropping the exponential function we get $\mathbf{Ax} = \lambda \mathbf{x}$. The characteristic equation is
$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} -3 - \lambda & 1 \\ 1 & -3 - \lambda \end{vmatrix} = \lambda^2 + 6\lambda + 8 = 0
$$
This gives the eigenvalues $\lambda_1 = -2$ and $\lambda_2 = -4$. Eigenvectors are then obtained from $(\mathbf{A} - \lambda\mathbf{I})\mathbf{x} = \mathbf{0}$.

For $\lambda_1 = -2$ this is $-x_1 + x_2 = 0$. Hence we can take $\mathbf{x}^{(1)} = [1\ \ 1]^T$.

For $\lambda_2 = -4$ this becomes $x_1 + x_2 = 0$, and an eigenvector is $\mathbf{x}^{(2)} = [1\ \ -1]^T$. This gives the general solution
$$
\mathbf{y} = \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = c_1 \mathbf{y}^{(1)} + c_2 \mathbf{y}^{(2)} = c_1 \begin{bmatrix} 1 \\ 1 \end{bmatrix} e^{-2t} + c_2 \begin{bmatrix} 1 \\ -1 \end{bmatrix} e^{-4t}
$$ {#eq-4-44}
@fig-4-82 shows a phase portrait of some of the trajectories (to which more trajectories could be added if so desired). The two straight trajectories correspond to $c_2 = 0$ and $c_1 = 0$, and the others to other choices of $c_1, c_2$.

The method of the phase plane is particularly valuable in the frequent cases when solving an ODE or a system is inconvenient or impossible. $\blacksquare$

### Critical Points of the System

The point $\mathbf{y} = \mathbf{0}$ in @fig-4-82 seems to be a common point of all trajectories, and we want to explore the reason for this remarkable observation. The answer will follow by calculus. Indeed, from our system we obtain
$$
\frac{dy_2}{dy_1} = \frac{y'_2}{y'_1} = \frac{a_{21}y_1 + a_{22}y_2}{a_{11}y_1 + a_{12}y_2}
$$ {#eq-4-45}
This associates with every point $P : (y_1, y_2)$ a unique tangent direction $dy_2/dy_1$ of the trajectory passing through $P$, except for the point $P_0 : (0,0)$, where the right side of (@eq-4-45) becomes $0/0$. This point $P_0$, at which $dy_2/dy_1$ becomes undetermined, is called a **critical point** of the system.

### Five Types of Critical Points

There are five types of critical points depending on the geometric shape of the trajectories near them. They are called **improper nodes**, **proper nodes**, **saddle points**, **centers**, and **spiral points**. We define and illustrate them in Examples 1–5.

### EXAMPLE 1 (Continued) Improper Node

An **improper node** is a critical point at which all the trajectories, except for two of them, have the same limiting direction of the tangent at the critical point. The two exceptional trajectories also have a limiting direction of the tangent at $P_0$ which, however, is different.

The system (@eq-4-43) has an improper node at $0$, as its phase portrait @fig-4-82 shows. The common limiting direction at $0$ is that of the eigenvector $\mathbf{x}^{(1)} = [1\ \ 1]^T$ because $e^{-4t}$ goes to zero faster than $e^{-2t}$ as $t$ increases. The two exceptional limiting tangent directions are those of $\mathbf{x}^{(2)} = [1\ \ -1]^T$ and $-\mathbf{x}^{(2)} = [-1\ \ 1]^T$. $\blacksquare$

![Fig. 82: Trajectories of the system (8) (Improper node)](../images/chapter4/fig-4-82.png){#fig-4-82}

### EXAMPLE 2 Proper Node

A **proper node** is a critical point at which every trajectory has a definite limiting direction and for any given direction $d$ at $P_0$ there is a trajectory having $d$ as its limiting direction.

The system
$$
\mathbf{y}' = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \mathbf{y}, \quad \text{thus} \quad \begin{aligned} y'_1 &= y_1 \\ y'_2 &= y_2 \end{aligned}
$$ {#eq-4-46}
has a proper node at the origin (see @fig-4-83). Indeed, the matrix is the unit matrix. Its characteristic equation has the double root $\lambda = 1$. Any $\mathbf{x} \neq \mathbf{0}$ is an eigenvector, and we can take $\mathbf{x}^{(1)} = [1\ \ 0]^T$ and $\mathbf{x}^{(2)} = [0\ \ 1]^T$. Hence a general solution is
$$
\mathbf{y} = c_1 \begin{bmatrix} 1 \\ 0 \end{bmatrix} e^t + c_2 \begin{bmatrix} 0 \\ 1 \end{bmatrix} e^t \quad \text{or} \quad \begin{aligned} y_1 &= c_1 e^t \\ y_2 &= c_2 e^t \end{aligned} \quad \text{or} \quad c_1 y_2 = c_2 y_1
$$ $\blacksquare$

![Fig. 83: Trajectories of the system (10) (Proper node)](../images/chapter4/fig-4-83.png){#fig-4-83}

### EXAMPLE 3 Saddle Point

A **saddle point** is a critical point at which there are two incoming trajectories, two outgoing trajectories, and all the other trajectories in a neighborhood of $P_0$ bypass $P_0$.

The system
$$
\mathbf{y}' = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \mathbf{y}, \quad \text{thus} \quad \begin{aligned} y'_1 &= y_1 \\ y'_2 &= -y_2 \end{aligned}
$$ {#eq-4-47}
has a saddle point at the origin. Its characteristic equation has the roots $\lambda_1 = 1$ and $\lambda_2 = -1$. For $\lambda_1 = 1$ an eigenvector is $\mathbf{x}^{(1)} = [1\ \ 0]^T$. For $\lambda_2 = -1$ an eigenvector is $\mathbf{x}^{(2)} = [0\ \ 1]^T$. Hence a general solution is
$$
\mathbf{y} = c_1 \begin{bmatrix} 1 \\ 0 \end{bmatrix} e^t + c_2 \begin{bmatrix} 0 \\ 1 \end{bmatrix} e^{-t} \quad \text{or} \quad \begin{aligned} y_1 &= c_1 e^t \\ y_2 &= c_2 e^{-t} \end{aligned} \quad \text{or} \quad y_1 y_2 = \text{const}
$$
This is a family of hyperbolas (and the coordinate axes); see @fig-4-84. $\blacksquare$

![Fig. 84: Trajectories of the system (11) (Saddle point)](../images/chapter4/fig-4-84.png){#fig-4-84}

### EXAMPLE 4 Center

A **center** is a critical point that is enclosed by infinitely many closed trajectories.

The system
$$
\mathbf{y}' = \begin{bmatrix} 0 & 1 \\ -4 & 0 \end{bmatrix} \mathbf{y}, \quad \text{thus} \quad \begin{aligned} y'_1 &= y_2 \\ y'_2 &= -4y_1 \end{aligned}
$$ {#eq-4-48}
has a center at the origin. The characteristic equation gives the eigenvalues $\lambda = \pm 2i$. For $\lambda_1 = 2i$ an eigenvector follows from the first equation of $(\mathbf{A} - \lambda\mathbf{I})\mathbf{x} = \mathbf{0}$, say, $\mathbf{x}^{(1)} = [1\ \ 2i]^T$. For $\lambda_2 = -2i$ that equation gives, say, $\mathbf{x}^{(2)} = [1\ \ -2i]^T$. Hence a complex general solution is
$$
\mathbf{y} = c_1 \begin{bmatrix} 1 \\ 2i \end{bmatrix} e^{2it} + c_2 \begin{bmatrix} 1 \\ -2i \end{bmatrix} e^{-2it}, \quad \text{thus} \quad \begin{aligned} y_1 &= c_1 e^{2it} + c_2 e^{-2it} \\ y_2 &= 2i c_1 e^{2it} - 2i c_2 e^{-2it} \end{aligned}
$$
A real solution is obtained by the Euler formula or directly from the system by a trick. Namely, the left side of (a) times the right side of (b) is $-4y_1 y'_1$. This must equal the left side of (b) times the right side of (a). Thus, $-4y_1 y'_1 = y_2 y'_2$. By integration, $2y_1^2 + \frac{1}{2}y_2^2 = \text{const}$. This is a family of ellipses (see @fig-4-85) enclosing the center at the origin. $\blacksquare$

![Fig. 85: Trajectories of the system (12) (Center)](../images/chapter4/fig-4-85.png){#fig-4-85}

### EXAMPLE 5 Spiral Point

A **spiral point** is a critical point about which the trajectories spiral, approaching $P_0$ as $t \to \infty$ (or tracing these spirals in the opposite sense, away from $P_0$).

The system
$$
\mathbf{y}' = \begin{bmatrix} -1 & 1 \\ -1 & -1 \end{bmatrix} \mathbf{y}, \quad \text{thus} \quad \begin{aligned} y'_1 &= -y_1 + y_2 \\ y'_2 &= -y_1 - y_2 \end{aligned}
$$ {#eq-4-49}
has a spiral point at the origin, as we shall see. The characteristic equation is $\lambda^2 + 2\lambda + 2 = 0$. It gives the eigenvalues $\lambda_1 = -1 + i$ and $\lambda_2 = -1 - i$. Corresponding eigenvectors are obtained from $(\mathbf{A} - \lambda\mathbf{I})\mathbf{x} = \mathbf{0}$. For $\lambda_1 = -1 + i$ this becomes $-ix_1 + x_2 = 0$ and we can take $\mathbf{x}^{(1)} = [1\ \ i]^T$ as an eigenvector. Similarly, an eigenvector corresponding to $\lambda_2 = -1 - i$ is $\mathbf{x}^{(2)} = [1\ \ -i]^T$. This gives the complex general solution
$$
\mathbf{y} = c_1 \begin{bmatrix} 1 \\ i \end{bmatrix} e^{(-1+i)t} + c_2 \begin{bmatrix} 1 \\ -i \end{bmatrix} e^{(-1-i)t}
$$
The next step would be the transformation of this complex solution to a real general solution by the Euler formula. But, as in the last example, we just wanted to see what eigenvalues to expect in the case of a spiral point. Accordingly, we start again from the beginning and instead of that rather lengthy systematic calculation we use a shortcut. We multiply the first equation in (@eq-4-49) by $y_1$, the second by $y_2$, and add, obtaining
$$
y_1 y'_1 + y_2 y'_2 = -(y_1^2 + y_2^2)
$$
We now introduce polar coordinates $r, \theta$, where $r^2 = y_1^2 + y_2^2$. Differentiating this with respect to $t$ gives $2r r' = 2y_1 y'_1 + 2y_2 y'_2$. Hence the previous equation can be written
$$
r r' = -r^2, \quad \text{Thus,} \quad r' = -r, \quad \frac{dr}{r} = -dt, \quad \ln |r| = -t + c^*, \quad r = c e^{-t}
$$
For each real $c$ this is a spiral, as claimed (see @fig-4-86). $\blacksquare$

![Fig. 86: Trajectories of the system (13) (Spiral point)](../images/chapter4/fig-4-86.png){#fig-4-86}

### EXAMPLE 6 No Basis of Eigenvectors Available. Degenerate Node

This cannot happen if $\mathbf{A}$ in (@eq-4-38) is symmetric ($a_{kj} = a_{jk}$, as in Examples 1–3) or skew-symmetric ($a_{kj} = -a_{jk}$ thus $a_{jj} = 0$). And it does not happen in many other cases (see Examples 4 and 5). Hence it suffices to explain the method to be used by an example.

Find and graph a general solution of
$$
\mathbf{y}' = \mathbf{A}\mathbf{y} = \begin{bmatrix} 4 & 1 \\ -1 & 2 \end{bmatrix} \mathbf{y}
$$ {#eq-4-50}

**Solution.** $\mathbf{A}$ is not symmetric! Its characteristic equation is
$$
\det(\mathbf{A} - \lambda\mathbf{I}) = \begin{vmatrix} 4 - \lambda & 1 \\ -1 & 2 - \lambda \end{vmatrix} = \lambda^2 - 6\lambda + 9 = (\lambda - 3)^2 = 0
$$
It has a double root $\lambda = 3$. Hence eigenvectors are obtained from $(\mathbf{A} - 3\mathbf{I})\mathbf{x} = \mathbf{0}$, thus from
$$
(4 - 3)x_1 + x_2 = x_1 + x_2 = 0
$$
say, $\mathbf{x} = [1\ \ -1]^T$ and nonzero multiples of it (which do not help). The method now is to substitute
$$
\mathbf{y}^{(2)} = \mathbf{x} t e^{\lambda t} + \mathbf{u} e^{\lambda t}
$$
with constant $\mathbf{u} = [u_1\ \ u_2]^T$ into (@eq-4-50). (The $\mathbf{x}te^{\lambda t}$-term alone, the analog of what we did in Sec. 2.2 in the case of a double root, would not be enough. Try it.) This gives
$$
\mathbf{y}^{(2)\prime} = \mathbf{x} e^{\lambda t} + \lambda \mathbf{x} t e^{\lambda t} + \lambda \mathbf{u} e^{\lambda t} = \mathbf{A}\mathbf{y}^{(2)} = \mathbf{A}\mathbf{x} t e^{\lambda t} + \mathbf{A}\mathbf{u} e^{\lambda t}
$$
On the right, $\mathbf{A}\mathbf{x} = \lambda \mathbf{x}$. Hence the $t e^{\lambda t}$-terms cancel, and then division by $e^{\lambda t}$ gives
$$
\mathbf{x} + \lambda \mathbf{u} = \mathbf{A}\mathbf{u}, \quad \text{thus} \quad (\mathbf{A} - \lambda \mathbf{I})\mathbf{u} = \mathbf{x}
$$
Here $\lambda = 3$ and $\mathbf{x} = [1\ \ -1]^T$, so that
$$
(\mathbf{A} - 3\mathbf{I})\mathbf{u} = \begin{bmatrix} 4 - 3 & 1 \\ -1 & 2 - 3 \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ -1 & -1 \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$
thus
$$
\begin{aligned}
u_1 + u_2 &= 1 \\
-u_1 - u_2 &= -1
\end{aligned}
$$
A solution is $u_1 = 0, u_2 = 1$, so that $\mathbf{u} = [0\ \ 1]^T$. A solution, linearly independent of $\mathbf{y}^{(1)}$, is $\mathbf{y}^{(2)} = \left(\mathbf{x} t + \mathbf{u}\right) e^{3t}$. This yields the answer (cf. @fig-4-87):
$$
\mathbf{y} = c_1 \mathbf{y}^{(1)} + c_2 \mathbf{y}^{(2)} = c_1 \begin{bmatrix} 1 \\ -1 \end{bmatrix} e^{3t} + c_2 \left( \begin{bmatrix} 1 \\ -1 \end{bmatrix} t + \begin{bmatrix} 0 \\ 1 \end{bmatrix} \right) e^{3t}
$$ {#eq-4-51}
The critical point at the origin is often called a **degenerate node**. $c_1 \mathbf{y}^{(1)}$ gives the heavy straight line, with $c_1 > 0$ the lower part and $c_1 < 0$ the upper part of it. $c_2 \mathbf{y}^{(2)}$ gives the right part of the heavy curve from $0$ through the second, first, and—finally—fourth quadrants. $-c_2 \mathbf{y}^{(2)}$ gives the other part of that curve. $\blacksquare$

![Fig. 87: Degenerate node in Example 6](../images/chapter4/fig-4-87.png){#fig-4-87}

We mention that for a system (@eq-4-38) with three or more equations and a triple eigenvalue $\lambda$ with only one linearly independent eigenvector, one will get two solutions, as just discussed, and a third linearly independent one from
$$
\mathbf{y}^{(3)} = \left( \frac{1}{2} \mathbf{x} t^2 + \mathbf{u} t + \mathbf{v} \right) e^{\lambda t}
$$
with $\mathbf{v}$ from $\mathbf{u} + \lambda \mathbf{v} = \mathbf{A}\mathbf{v}$.

## PROBLEM SET 4.3 {#sec-4-3-problems}

### 1–9 GENERAL SOLUTION
Find a real general solution of the following systems. Show the details.
1. $\begin{aligned} y'_1 &= y_1 + 2y_2 \\ y'_2 &= \frac{1}{2}y_1 + y_2 \end{aligned}$
2. $\begin{aligned} y'_1 &= 6y_1 + 9y_2 \\ y'_2 &= y_1 + 6y_2 \end{aligned}$
3. $\begin{aligned} y'_1 &= y_1 + y_2 \\ y'_2 &= y_1 - y_2 \end{aligned}$
4. $\begin{aligned} y'_1 &= -8y_1 - 2y_2 \\ y'_2 &= 2y_1 - 4y_2 \end{aligned}$
5. $\begin{aligned} y'_1 &= 2y_1 - 2y_2 \\ y'_2 &= 2y_1 + 2y_2 \end{aligned}$
6. $\begin{aligned} y'_1 &= -10y_1 + y_2 - 14y_3 \\ y'_2 &= -4y_1 - 14y_2 - 2y_3 \\ y'_3 &= 10y_1 - 10y_2 - 4y_3 \end{aligned}$
7. $\begin{aligned} y'_1 &= -y_1 + y_3 \\ y'_2 &= 8y_1 - y_2 \\ y'_3 &= -y_2 \end{aligned}$
8. $\begin{aligned} y'_1 &= 2y_1 + 5y_2 \\ y'_2 &= 5y_1 + 12.5y_2 \end{aligned}$
9. $\begin{aligned} y'_1 &= y_1 + 10y_2 \\ y'_2 &= -y_1 - y_2 \end{aligned}$

### 10–15 INITIAL VALUE PROBLEMS
Solve the following initial value problems.
10. $\begin{aligned} y'_1 &= y_2 \\ y'_2 &= y_1 \end{aligned}, \quad y_1(0) = 0, \ y_2(0) = 2$
11. $\begin{aligned} y'_1 &= y_1 + 3y_2 \\ y'_2 &= \frac{1}{3}y_1 + y_2 \end{aligned}, \quad y_1(0) = 12, \ y_2(0) = 2$
12. $\begin{aligned} y'_1 &= 2y_1 + 5y_2 \\ y'_2 &= -\frac{1}{2}y_1 - \frac{3}{2}y_2 \end{aligned}, \quad y_1(0) = -12, \ y_2(0) = 0$
13. $\begin{aligned} y'_1 &= 2y_1 + 2y_2 \\ y'_2 &= 5y_1 - y_2 \end{aligned}, \quad y_1(0) = 0, \ y_2(0) = 7$
14. $\begin{aligned} y'_1 &= -y_1 - y_2 \\ y'_2 &= y_1 - y_2 \end{aligned}, \quad y_1(0) = 1, \ y_2(0) = 0$
15. $\begin{aligned} y'_1 &= 3y_1 + 2y_2 \\ y'_2 &= 2y_1 + 3y_2 \end{aligned}, \quad y_1(0) = 0.5, \ y_2(0) = -0.5$

### 16–17 CONVERSION
Find a general solution by conversion to a single ODE.
16. The system in Prob. 8.
17. The system in Example 5 of the text.

### 18 MIXING PROBLEM
Each of the two tanks in @fig-4-88 contains 200 gal of water, in which initially 100 lb (Tank $T_1$) and 200 lb (Tank $T_2$) of fertilizer are dissolved. The inflow, circulation, and outflow are shown in @fig-4-88. The mixture is kept uniform by stirring. Find the fertilizer contents $y_1(t)$ in $T_1$ and $y_2(t)$ in $T_2$.

![Fig. 88: Tanks in Problem 18](../images/chapter4/fig-4-88.png){#fig-4-88}

### 19 ELECTRICAL NETWORK
Show that a model for the currents $I_1(t)$ and $I_2(t)$ in @fig-4-89 is
$$
\frac{1}{C}\int I_1 \, dt + R(I_1 - I_2) = 0, \quad L I'_2 + R(I_2 - I_1) = 0
$$
Find a general solution, assuming that $R = 3\ \Omega$, $L = 4$ H, $C = 1/12$ F.

![Fig. 89: Network in Problem 19](../images/chapter4/fig-4-89.png){#fig-4-89}

### 20 CAS PROJECT. Phase Portraits.
Graph some of the figures in this section, in particular @fig-4-87 on the degenerate node, in which the vector $\mathbf{y}^{(2)}$ depends on $t$. In each figure highlight a trajectory that satisfies an initial condition of your choice.
"""

append_text(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\chapters\ch4.qmd", text)
