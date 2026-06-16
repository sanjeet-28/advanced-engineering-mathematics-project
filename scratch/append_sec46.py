def append_text(path, text):
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n" + text + "\n")

text = r"""
## 4.6 Nonhomogeneous Linear Systems {#sec-4-6}

We continue with systems of ODEs, now turning from homogeneous to **nonhomogeneous linear systems**
$$
\mathbf{y}' = \mathbf{A}(t)\mathbf{y} + \mathbf{g}(t)
$$ {#eq-4-72}
where $\mathbf{A}(t)$ is an $n \times n$ matrix and $\mathbf{g}(t) \not\equiv \mathbf{0}$ is a given vector function (a vector with $n$ components). **Solutions** are vector functions $\mathbf{y}(t)$ satisfying (@eq-4-72) on some interval $J$.

The corresponding **homogeneous system** is $\mathbf{y}' = \mathbf{A}(t)\mathbf{y}$.

**THEOREM 1 General Solution**

If the homogeneous system corresponding to (@eq-4-72) has a fundamental matrix $\mathbf{\Phi}(t)$ on an open interval $J$ and $\mathbf{y}^{(p)}(t)$ is any particular solution of (@eq-4-72) on $J$, then every solution of (@eq-4-72) on $J$ is of the form
$$
\mathbf{y}(t) = \mathbf{\Phi}(t)\mathbf{c} + \mathbf{y}^{(p)}(t)
$$ {#eq-4-73}
where $\mathbf{c}$ is an arbitrary constant vector.

**Proof.** Let $\tilde{\mathbf{y}}$ be any solution of (@eq-4-72) on $J$. Then $\tilde{\mathbf{y}} - \mathbf{y}^{(p)}$ is a solution of the homogeneous system because
$$
(\tilde{\mathbf{y}} - \mathbf{y}^{(p)})' = \tilde{\mathbf{y}}' - \mathbf{y}^{(p)\prime} = (\mathbf{A}\tilde{\mathbf{y}} + \mathbf{g}) - (\mathbf{A}\mathbf{y}^{(p)} + \mathbf{g}) = \mathbf{A}(\tilde{\mathbf{y}} - \mathbf{y}^{(p)})
$$
Since $\mathbf{\Phi}(t)$ is a fundamental matrix, by Theorem 2 of Sec. 4.1, $\tilde{\mathbf{y}} - \mathbf{y}^{(p)} = \mathbf{\Phi}(t)\mathbf{c}$ for some constant vector $\mathbf{c}$, so that $\tilde{\mathbf{y}} = \mathbf{\Phi}(t)\mathbf{c} + \mathbf{y}^{(p)}$. This proves the theorem. $\square$

### Method of Undetermined Coefficients

In the case of constant $\mathbf{A}$ and a "simple" $\mathbf{g}(t)$, a particular solution can be found by the **method of undetermined coefficients**. In this method, one chooses for $\mathbf{y}^{(p)}$ a form similar to $\mathbf{g}$, substitutes into the system, and equates coefficients of like terms on both sides. This is completely analogous to the scalar case discussed in Sec. 2.7.

### EXAMPLE 1 Method of Undetermined Coefficients

Find a solution of
$$
\mathbf{y}' = \mathbf{A}\mathbf{y} + \mathbf{g}
$$
where $\mathbf{A} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ and $\mathbf{g} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}e^{2t}$.

**Solution.** We try $\mathbf{y}^{(p)} = \mathbf{u}e^{2t}$, where $\mathbf{u}$ is a constant vector. Substituting,
$$
2\mathbf{u}e^{2t} = \mathbf{A}\mathbf{u}e^{2t} + \mathbf{g}e^{2t}
$$
$$
(2\mathbf{I} - \mathbf{A})\mathbf{u} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}
$$
$$
\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}\mathbf{u} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}
$$
This gives $2u_1 - u_2 = -1$ and $-u_1 + 2u_2 = 2$. Adding the equations, $u_1 + u_2 = 1$. Subtracting, $3u_1 - 3u_2 = -3$, i.e., $u_1 - u_2 = -1$. Thus $u_1 = 0, u_2 = 1$. Therefore $\mathbf{y}^{(p)} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}e^{2t}$. $\blacksquare$

### Variation of Parameters

A general method for solving (@eq-4-72) on an interval $J$ is **variation of parameters**, analogous to that in Sec. 2.10. Here we have a fundamental matrix $\mathbf{\Phi}(t)$ of $\mathbf{y}' = \mathbf{A}\mathbf{y}$ and we replace the constant vector $\mathbf{c}$ in $\mathbf{\Phi}(t)\mathbf{c}$ by a variable vector $\mathbf{u}(t)$, obtaining a particular solution of (@eq-4-72) in the form
$$
\mathbf{y}^{(p)} = \mathbf{\Phi}(t)\mathbf{u}(t)
$$ {#eq-4-74}
We substitute into (@eq-4-72):
$$
\mathbf{y}^{(p)\prime} = \mathbf{\Phi}'\mathbf{u} + \mathbf{\Phi}\mathbf{u}' = \mathbf{A}\mathbf{\Phi}\mathbf{u} + \mathbf{g}
$$
Since $\mathbf{\Phi}$ is a fundamental matrix of $\mathbf{y}' = \mathbf{A}\mathbf{y}$, we have $\mathbf{\Phi}' = \mathbf{A}\mathbf{\Phi}$, so that $\mathbf{\Phi}'\mathbf{u} = \mathbf{A}\mathbf{\Phi}\mathbf{u}$, and the last equation reduces to
$$
\mathbf{\Phi}\mathbf{u}' = \mathbf{g}
$$
Since $\mathbf{\Phi}$ is a fundamental matrix, $\det\mathbf{\Phi} \neq 0$, so that $\mathbf{\Phi}^{-1}$ exists, and
$$
\mathbf{u}' = \mathbf{\Phi}^{-1}\mathbf{g}, \quad \text{thus} \quad \mathbf{u} = \int \mathbf{\Phi}^{-1}(t)\mathbf{g}(t)\, dt
$$
Substituting this into (@eq-4-74), we obtain

$$
\boxed{\mathbf{y}^{(p)} = \mathbf{\Phi}(t)\int \mathbf{\Phi}^{-1}(t)\mathbf{g}(t)\, dt}
$$ {#eq-4-75}

This is the formula for variation of parameters for systems.

### EXAMPLE 2 Variation of Parameters

Solve the system
$$
\mathbf{y}' = \mathbf{A}\mathbf{y} + \mathbf{g}, \quad \mathbf{A} = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}, \quad \mathbf{g} = \begin{bmatrix} e^{2t} \\ 0 \end{bmatrix}
$$

**Solution.** **Step 1. Homogeneous system.** The characteristic equation of $\mathbf{A}$ is $(\lambda - 2)^2 = 0$, giving the double eigenvalue $\lambda = 2$.

An eigenvector of $\mathbf{A}$ is $\mathbf{x}_1 = [1 \;\; 0]^T$. A generalized eigenvector: solve $(\mathbf{A} - 2\mathbf{I})\mathbf{x}_2 = \mathbf{x}_1$, getting $\mathbf{x}_2 = [0 \;\; 1]^T$. So
$$
\mathbf{y}^{(1)} = e^{2t}\begin{bmatrix}1\\0\end{bmatrix}, \quad \mathbf{y}^{(2)} = e^{2t}\!\left(\begin{bmatrix}0\\1\end{bmatrix} + t\begin{bmatrix}1\\0\end{bmatrix}\right) = e^{2t}\begin{bmatrix}t\\1\end{bmatrix}
$$
The fundamental matrix is
$$
\mathbf{\Phi} = e^{2t}\begin{bmatrix}1 & t\\0 & 1\end{bmatrix}
$$
**Step 2. Particular solution.** We compute $\mathbf{\Phi}^{-1}$. Since $\det\mathbf{\Phi} = e^{4t}$,
$$
\mathbf{\Phi}^{-1} = \frac{1}{e^{4t}} \cdot e^{2t}\begin{bmatrix}1 & -t\\0 & 1\end{bmatrix} = e^{-2t}\begin{bmatrix}1 & -t\\0 & 1\end{bmatrix}
$$
Then
$$
\mathbf{\Phi}^{-1}\mathbf{g} = e^{-2t}\begin{bmatrix}1 & -t\\0 & 1\end{bmatrix}\begin{bmatrix}e^{2t}\\0\end{bmatrix} = \begin{bmatrix}1\\0\end{bmatrix}
$$
Integrating, $\mathbf{u} = \begin{bmatrix}t\\0\end{bmatrix}$. Then by (@eq-4-75),
$$
\mathbf{y}^{(p)} = \mathbf{\Phi}\mathbf{u} = e^{2t}\begin{bmatrix}1&t\\0&1\end{bmatrix}\begin{bmatrix}t\\0\end{bmatrix} = e^{2t}\begin{bmatrix}t\\0\end{bmatrix}
$$
**Step 3. General solution.** From (@eq-4-73),
$$
\mathbf{y} = \mathbf{\Phi}\mathbf{c} + \mathbf{y}^{(p)} = e^{2t}\begin{bmatrix}1&t\\0&1\end{bmatrix}\begin{bmatrix}c_1\\c_2\end{bmatrix} + e^{2t}\begin{bmatrix}t\\0\end{bmatrix} = e^{2t}\begin{bmatrix}c_1 + c_2 t + t\\c_2\end{bmatrix}
$$
Thus $y_1 = (c_1 + t + c_2 t)e^{2t}$ and $y_2 = c_2 e^{2t}$. $\blacksquare$

### EXAMPLE 3 Forced Oscillations

Solve the system
$$
\mathbf{y}' = \begin{bmatrix}0&1\\-1&0\end{bmatrix}\mathbf{y} + \begin{bmatrix}0\\\cos t\end{bmatrix}
$$ {#eq-4-76}
**Solution.** The coefficient matrix $\mathbf{A} = \begin{bmatrix}0&1\\-1&0\end{bmatrix}$ has the characteristic equation $\lambda^2 + 1 = 0$, so $\lambda_{1,2} = \pm i$. The fundamental matrix is
$$
\mathbf{\Phi}(t) = \begin{bmatrix}\cos t & \sin t \\ -\sin t & \cos t\end{bmatrix}
$$
To apply (@eq-4-75), we need $\mathbf{\Phi}^{-1}$. We compute $\det \mathbf{\Phi} = \cos^2 t + \sin^2 t = 1$. By the standard formula,
$$
\mathbf{\Phi}^{-1} = \begin{bmatrix}\cos t & -\sin t \\ \sin t & \cos t\end{bmatrix}
$$
Then
$$
\mathbf{\Phi}^{-1}\mathbf{g} = \begin{bmatrix}\cos t & -\sin t \\ \sin t & \cos t\end{bmatrix}\begin{bmatrix}0\\\cos t\end{bmatrix} = \begin{bmatrix}-\sin t\cos t\\\cos^2 t\end{bmatrix} = \begin{bmatrix}-\tfrac{1}{2}\sin 2t\\ \tfrac{1}{2}(1+\cos 2t)\end{bmatrix}
$$
Integrating component-wise,
$$
\mathbf{u}(t) = \begin{bmatrix}\tfrac{1}{4}\cos 2t\\ \tfrac{1}{2}t + \tfrac{1}{4}\sin 2t\end{bmatrix}
$$
Applying (@eq-4-75):
$$
\mathbf{y}^{(p)} = \mathbf{\Phi}\mathbf{u} = \begin{bmatrix}\cos t & \sin t\\-\sin t & \cos t\end{bmatrix}\begin{bmatrix}\tfrac{1}{4}\cos 2t\\ \tfrac{1}{2}t + \tfrac{1}{4}\sin 2t\end{bmatrix}
$$
Expanding (using $\cos t\cos 2t + \sin t\sin 2t = \cos t$ and $-\sin t\cos 2t + \cos t \sin 2t = \sin t$):
$$
y_1^{(p)} = \tfrac{1}{4}\cos t + \tfrac{1}{2}t\sin t, \quad y_2^{(p)} = -\tfrac{1}{4}\sin t + \tfrac{1}{2}t\cos t + \tfrac{1}{2}\sin t = \tfrac{1}{2}t\cos t + \tfrac{1}{4}\sin t
$$
The general solution of (@eq-4-76) is
$$
\begin{aligned}
y_1 &= (c_1 + \tfrac{1}{4})\cos t + (c_2 + \tfrac{1}{2}t)\sin t \\
y_2 &= -(c_1 + \tfrac{1}{4})\sin t + (c_2 + \tfrac{1}{2}t)\cos t + \tfrac{1}{2}\sin t
\end{aligned}
$$
The terms with $t\sin t$ and $t\cos t$ represent **resonance**, analogous to the scalar case. $\blacksquare$

## PROBLEM SET 4.6 {#sec-4-6-problems}

### 1–8 UNDETERMINED COEFFICIENTS
Find a particular solution. Show all your work.
1. $y'_1 = y_1 + y_2 + 2e^t, \quad y'_2 = y_1 + y_2 + 2t$
2. $y'_1 = y_2 + e^{-t}, \quad y'_2 = -y_1 + t$
3. $y'_1 = y_2 + t^2, \quad y'_2 = y_1 - 1$
4. $y'_1 = 3y_1 - 2y_2 + e^t, \quad y'_2 = 4y_1 - y_2 - e^t$
5. $y'_1 = y_2 + \cos 2t, \quad y'_2 = -y_1 + \sin 2t$
6. $y'_1 = 2y_2 + 8e^t, \quad y'_2 = 2y_1 + 8e^t$
7. $y'_1 = y_2 + 1, \quad y'_2 = y_1 + t^2$
8. $y'_1 = y_2 + e^{2t}, \quad y'_2 = y_1 + e^{2t}$

### 9–16 VARIATION OF PARAMETERS
Solve the IVP using variation of parameters. Show all details.
9. $\mathbf{y}' = \begin{bmatrix}0&1\\-1&0\end{bmatrix}\mathbf{y} + \begin{bmatrix}0\\e^t\end{bmatrix}, \quad \mathbf{y}(0) = \begin{bmatrix}1\\0\end{bmatrix}$
10. $\mathbf{y}' = \begin{bmatrix}1&1\\0&1\end{bmatrix}\mathbf{y} + \begin{bmatrix}e^t\\t\end{bmatrix}$
11. $\mathbf{y}' = \begin{bmatrix}2&-5\\1&-2\end{bmatrix}\mathbf{y} + \begin{bmatrix}\cos t\\\sin t\end{bmatrix}$
12. $\mathbf{y}' = \begin{bmatrix}0&1\\-4&0\end{bmatrix}\mathbf{y} + \begin{bmatrix}0\\\sin 2t\end{bmatrix}, \quad \mathbf{y}(0) = \begin{bmatrix}0\\0\end{bmatrix}$
13. $\mathbf{y}' = \begin{bmatrix}1&0\\1&1\end{bmatrix}\mathbf{y} + \begin{bmatrix}e^t\\e^t\end{bmatrix}$
14. $\mathbf{y}' = \begin{bmatrix}0&1\\-1&0\end{bmatrix}\mathbf{y} + \begin{bmatrix}0\\\csc t\end{bmatrix}$
15. $\mathbf{y}' = \begin{bmatrix}0&1\\-1&0\end{bmatrix}\mathbf{y} + \begin{bmatrix}0\\\sec t\end{bmatrix}$
16. $\mathbf{y}' = \begin{bmatrix}1&1\\-1&1\end{bmatrix}\mathbf{y} + \begin{bmatrix}e^t\cos t\\e^t \sin t\end{bmatrix}$

17. **Electrical network.** Find the general solution of
$$
\mathbf{I}' = \mathbf{A}\mathbf{I} + \mathbf{g}(t)
$$
where $\mathbf{A} = \begin{bmatrix}-2 & 2 \\ 2 & -2\end{bmatrix}$ and $\mathbf{g}(t) = \begin{bmatrix}6\sin t\\ 0\end{bmatrix}$.

18. **Nonhomogeneous system.** Find the general solution of
$$
\mathbf{y}' = \begin{bmatrix}0 & 1 \\ -2 & -3\end{bmatrix}\mathbf{y} + \begin{bmatrix}e^t \\ -e^t\end{bmatrix}
$$

19. **Undetermined coefficients.** Verify that if $\mathbf{g}(t) = \mathbf{g}_1\cos\omega t + \mathbf{g}_2\sin\omega t$ and the matrix $\mathbf{A}$ has no eigenvalue $\pm i\omega$, then a particular solution of $\mathbf{y}' = \mathbf{A}\mathbf{y} + \mathbf{g}(t)$ has the form $\mathbf{y}^{(p)} = \mathbf{a}\cos\omega t + \mathbf{b}\sin\omega t$.

20. **IVP.** Solve the initial value problem
$$
\mathbf{y}' = \begin{bmatrix}1 & -1 \\ 1 & 1\end{bmatrix}\mathbf{y} + \begin{bmatrix}e^t \\ 0\end{bmatrix}, \quad \mathbf{y}(0) = \begin{bmatrix}0 \\ 2\end{bmatrix}
$$

## Chapter 4 Summary {#sec-ch4-summary}

**Systems of ODEs** can be written in vector form $\mathbf{y}' = \mathbf{f}(t, \mathbf{y})$. This chapter concentrated on **linear first-order systems**
$$
\mathbf{y}' = \mathbf{A}(t)\mathbf{y} + \mathbf{g}(t)
$$
where **$\mathbf{A}$** is an $n\times n$ matrix and $\mathbf{g}$ is a vector. When **$\mathbf{g} = \mathbf{0}$** we have a **homogeneous system**.

**Sec. 4.1** developed the general theory for such systems, extending what was done for scalar second-order ODEs in Chap. 2. Key results:

- An IVP for a first-order system has a unique solution under continuity conditions.
- $n$ solutions $\mathbf{y}^{(1)}, \dots, \mathbf{y}^{(n)}$ are a **basis** (fundamental system) iff the **Wronskian** $W[\mathbf{y}^{(1)}, \dots, \mathbf{y}^{(n)}] = \det[\mathbf{y}^{(1)} \cdots \mathbf{y}^{(n)}] \neq 0$.
- The $n\times n$ matrix $\mathbf{\Phi} = [\mathbf{y}^{(1)} \cdots \mathbf{y}^{(n)}]$ is a **fundamental matrix**.
- The **general solution** is $\mathbf{y} = \mathbf{\Phi}(t)\mathbf{c}$ where $\mathbf{c}$ is an arbitrary constant vector.

**Sec. 4.2** concerned systems with **constant coefficients** $\mathbf{A}$. Solutions are of the form $\mathbf{y} = \mathbf{x}e^{\lambda t}$ where $\lambda$ and $\mathbf{x}$ are **eigenvalues** and **eigenvectors** of $\mathbf{A}$. Case studies:

- $\mathbf{A}$ has $n$ distinct eigenvalues: form the general solution directly from $n$ independent eigensolutions.
- **Complex eigenvalues** $\lambda_{1,2} = \alpha \pm i\beta$: take real and imaginary parts of $\mathbf{x}e^{\lambda_1 t}$.
- **Repeated eigenvalues**: use eigenvectors and **generalized eigenvectors**; solutions include polynomial-times-exponential terms.

**Sec. 4.3** introduced **matrix exponential functions** $e^{\mathbf{A}t}$. The solution of $\mathbf{y}' = \mathbf{A}\mathbf{y}, \, \mathbf{y}(0) = \mathbf{y}_0$ is $\mathbf{y}(t) = e^{\mathbf{A}t}\mathbf{y}_0$. Methods for computing $e^{\mathbf{A}t}$ include the diagonalization method and the Cayley–Hamilton approach.

**Sec. 4.4** developed a **qualitative (geometric) theory** for $2 \times 2$ constant-coefficient systems, linking the type and stability of **critical points** to the eigenvalues of $\mathbf{A}$:

| Critical Point Type | Eigenvalues | Stability |
|---|---|---|
| Proper/improper node | Both real, same sign | Stable if negative, unstable if positive |
| Saddle point | Real, opposite signs | Always unstable |
| Center | Purely imaginary | Stable (not asymptotically) |
| Spiral point | Complex, $\text{Re}(\lambda) \neq 0$ | Asymptotically stable if $\text{Re}(\lambda) < 0$ |

**Sec. 4.5** extended qualitative methods to **nonlinear systems** via **linearization**: near an isolated critical point $P_0$, the nonlinear system behaves like its linearized counterpart (the **Jacobian system**), except possibly when eigenvalues are purely imaginary or equal. Prominent examples:

- **Undamped and damped pendulum**: centers (undamped) and stable spirals (damped) at equilibrium $(0,0)$; saddle points at $(\pm\pi, 0)$.
- **Lotka–Volterra predator–prey model**: saddle at origin, center-type oscillation at the interior critical point.
- **Van der Pol equation**: existence of a **limit cycle** (self-sustained oscillation) for $\mu > 0$.

**Sec. 4.6** treated **nonhomogeneous systems** $\mathbf{y}' = \mathbf{A}\mathbf{y} + \mathbf{g}(t)$:

- General solution: $\mathbf{y} = \mathbf{\Phi}(t)\mathbf{c} + \mathbf{y}^{(p)}$.
- Particular solution methods:
  - **Undetermined coefficients**: guess a form for $\mathbf{y}^{(p)}$ matching $\mathbf{g}$, substitute, solve for coefficients.
  - **Variation of parameters**: $\mathbf{y}^{(p)} = \mathbf{\Phi}(t)\int\mathbf{\Phi}^{-1}(t)\mathbf{g}(t)\,dt$.

## Review Questions and Problems for Chapter 4 {#sec-ch4-review}

### SHORT ANSWERS (Fill in the blanks or answer briefly)

1. State the form of the general solution of a homogeneous first-order linear system.
2. What is the Wronskian of $n$ solutions $\mathbf{y}^{(1)}, \dots, \mathbf{y}^{(n)}$ of a linear system?
3. Under what conditions do $n$ solutions of an $n$-dimensional homogeneous linear system form a basis?
4. What kind of critical point corresponds to purely imaginary eigenvalues? Is it stable?
5. What is a limit cycle? How does it differ from a center?
6. State the variation of parameters formula for systems.

### 7–12 SYSTEMS AND PHASE PORTRAITS

Find the general solution and, in the case of Problems 11–12, solve the IVP. Sketch or describe the phase portrait in the $y_1 y_2$-plane.

7. $y'_1 = 3y_1 + y_2, \quad y'_2 = y_1 + 3y_2$
8. $y'_1 = y_2, \quad y'_2 = -4y_1$
9. $y'_1 = -y_1 + y_2, \quad y'_2 = -y_1 - y_2$
10. $y'_1 = 4y_1 - y_2, \quad y'_2 = y_1 + 2y_2$
11. $y'_1 = y_1 - y_2, \quad y'_2 = y_1 + y_2; \quad \mathbf{y}(0) = [2 \;\; 0]^T$
12. $y'_1 = 3y_1 - 4y_2, \quad y'_2 = 2y_1 - 3y_2; \quad \mathbf{y}(0) = [3 \;\; 2]^T$

### 13–16 NONHOMOGENEOUS SYSTEMS

Solve the system.
13. $y'_1 = 3y_1 + y_2 + e^{3t}, \quad y'_2 = y_1 + 3y_2$
14. $y'_1 = y_1 - y_2 + \cos t, \quad y'_2 = y_1 + y_2 + \sin t$
15. $y'_1 = y_2, \quad y'_2 = -y_1 + \sec t$
16. $y'_1 = -y_2 + \csc t, \quad y'_2 = y_1$

### 17–20 NONLINEAR SYSTEMS AND CRITICAL POINTS

Find and classify all critical points.
17. $y'_1 = y_2 - y_1^2, \quad y'_2 = y_1$
18. $y'_1 = y_2, \quad y'_2 = -\sin y_1 - y_2$
19. $y'_1 = y_1(1 - y_1 - y_2), \quad y'_2 = y_2(2 - y_1 - 3y_2)$ (competing species model)
20. $y'_1 = y_2, \quad y'_2 = y_1 - y_1^3$
"""

append_text(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\chapters\ch4.qmd", text)
