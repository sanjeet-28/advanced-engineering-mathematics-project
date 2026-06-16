def append_text(path, text):
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n" + text + "\n")

text = r"""
## 4.2 Basic Theory of Systems of ODEs. Wronskian {#sec-4-2}

In this section we discuss some basic concepts and facts about systems of ODEs that are quite similar to those for single ODEs.

The first-order systems in the last section were special cases of the more general system
$$
\begin{aligned}
y'_1 &= f_1(t, y_1, \dots, y_n) \\
y'_2 &= f_2(t, y_1, \dots, y_n) \\
&\ \ \vdots \\
y'_n &= f_n(t, y_1, \dots, y_n)
\end{aligned}
$$
We can write this system as a vector equation by introducing the column vectors $\mathbf{y} = [y_1\ \ \dots\ \ y_n]^T$ and $\mathbf{f} = [f_1\ \ \dots\ \ f_n]^T$ (where $T$ means transposition and saves us the space that would be needed for writing $\mathbf{y}$ and $\mathbf{f}$ as columns). This gives
$$
\mathbf{y}' = \mathbf{f}(t, \mathbf{y})
$$ {#eq-4-30}
This system (@eq-4-30) includes almost all cases of practical interest. For $n = 1$ it becomes $y'_1 = f_1(t, y_1)$ or, simply, $y' = f(t, y)$, well known to us from Chap. 1.

A **solution** of (@eq-4-30) on some interval $a < t < b$ is a set of $n$ differentiable functions $y_1 = h_1(t), \dots, y_n = h_n(t)$ on that interval that satisfy (@eq-4-30) throughout this interval. In vector form, introducing the "solution vector" $\mathbf{h} = [h_1\ \ \dots\ \ h_n]^T$ (a column vector!) we can write $\mathbf{y} = \mathbf{h}(t)$.

An **initial value problem** for (@eq-4-30) consists of (@eq-4-30) and $n$ given initial conditions
$$
y_1(t_0) = K_1, \quad y_2(t_0) = K_2, \quad \dots, \quad y_n(t_0) = K_n
$$
in vector form, $\mathbf{y}(t_0) = \mathbf{K}$, where $t_0$ is a specified value of $t$ in the interval considered and the components of $\mathbf{K} = [K_1\ \ \dots\ \ K_n]^T$ are given numbers. Sufficient conditions for the existence and uniqueness of a solution of an initial value problem (@eq-4-30), (@eq-4-31) are stated in the following theorem, which extends the theorems in Sec. 1.7 for a single equation. (For a proof, see Ref. [A7].)

**THEOREM 1 Existence and Uniqueness Theorem**
Let $f_1, \dots, f_n$ in (@eq-4-30) be continuous functions having continuous partial derivatives $\partial f_1/\partial y_1, \dots, \partial f_1/\partial y_n, \dots, \partial f_n/\partial y_n$ in some domain $R$ of $t y_1 y_2 \dots y_n$-space containing the point $(t_0, K_1, \dots, K_n)$. Then (@eq-4-30) has a solution on some interval $t_0 - \alpha < t < t_0 + \alpha$ satisfying the initial conditions, and this solution is unique.

### Linear Systems

Extending the notion of a linear ODE, we call (@eq-4-30) a **linear system** if it is linear in $y_1, \dots, y_n$, that is, if it can be written
$$
\begin{aligned}
y'_1 &= a_{11}(t)y_1 + \dots + a_{1n}(t)y_n + g_1(t) \\
&\ \ \vdots \\
y'_n &= a_{n1}(t)y_1 + \dots + a_{nn}(t)y_n + g_n(t)
\end{aligned}
$$
As a vector equation this becomes
$$
\mathbf{y}' = \mathbf{A}(t)\mathbf{y} + \mathbf{g}(t)
$$ {#eq-4-32}
where
$$
\mathbf{A} = \begin{bmatrix} a_{11} & \dots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{n1} & \dots & a_{nn} \end{bmatrix}, \quad \mathbf{y} = \begin{bmatrix} y_1 \\ \vdots \\ y_n \end{bmatrix}, \quad \mathbf{g} = \begin{bmatrix} g_1 \\ \vdots \\ g_n \end{bmatrix}
$$
This system is called **homogeneous** if $\mathbf{g}(t) = \mathbf{0}$, so that it is
$$
\mathbf{y}' = \mathbf{A}(t)\mathbf{y}
$$ {#eq-4-33}
If $\mathbf{g}(t) \neq \mathbf{0}$, then (@eq-4-32) is called **nonhomogeneous**. For example, the systems in Examples 1 and 3 of Sec. 4.1 are homogeneous. The system in Example 2 of that section is nonhomogeneous.

For a linear system (@eq-4-32) we have $\partial f_j/\partial y_k = a_{jk}(t)$ in Theorem 1. Hence for a linear system we simply obtain the following.

**THEOREM 2 Existence and Uniqueness in the Linear Case**
Let the $a_{jk}$'s and $g_j$'s in (@eq-4-32) be continuous functions of $t$ on an open interval $a < t < b$ containing the point $t_0$. Then (@eq-4-32) has a solution $\mathbf{y}(t)$ on this interval satisfying the initial conditions, and this solution is unique.

As for a single homogeneous linear ODE we have:

**THEOREM 3 Superposition Principle or Linearity Principle**
If $\mathbf{y}^{(1)}$ and $\mathbf{y}^{(2)}$ are solutions of the homogeneous linear system (@eq-4-33) on some interval, so is any linear combination $\mathbf{y} = c_1 \mathbf{y}^{(1)} + c_2 \mathbf{y}^{(2)}$.

**PROOF.** Differentiating and using (@eq-4-33), we obtain
$$
\mathbf{y}' = [c_1 \mathbf{y}^{(1)} + c_2 \mathbf{y}^{(2)}]' = c_1 \mathbf{y}^{(1)\prime} + c_2 \mathbf{y}^{(2)\prime} = c_1 \mathbf{A}\mathbf{y}^{(1)} + c_2 \mathbf{A}\mathbf{y}^{(2)} = \mathbf{A}(c_1 \mathbf{y}^{(1)} + c_2 \mathbf{y}^{(2)}) = \mathbf{A}\mathbf{y}
$$ $\blacksquare$

### Basis. General Solution. Wronskian

The general theory of linear systems of ODEs is quite similar to that of a single linear ODE in Secs. 2.6 and 2.7. To see this, we explain the most basic concepts and facts. For proofs we refer to more advanced texts, such as [A7].

By a **basis** or a **fundamental system** of solutions of the homogeneous system (@eq-4-33) on some interval $J$ we mean a linearly independent set of $n$ solutions of (@eq-4-33) on that interval. (We write $J$ because we need $I$ to denote the unit matrix.) We call a corresponding linear combination
$$
\mathbf{y} = c_1 \mathbf{y}^{(1)} + \dots + c_n \mathbf{y}^{(n)} \quad (c_1, \dots, c_n \text{ arbitrary})
$$ {#eq-4-34}
a **general solution** of (@eq-4-33) on $J$. It can be shown that if the $a_{jk}(t)$ in (@eq-4-33) are continuous on $J$, then (@eq-4-33) has a basis of solutions on $J$, hence a general solution, which includes every solution of (@eq-4-33) on $J$.

We can write $n$ solutions $\mathbf{y}^{(1)}, \dots, \mathbf{y}^{(n)}$ of (@eq-4-33) on some interval $J$ as columns of an $n \times n$ matrix
$$
\mathbf{Y} = \begin{bmatrix} \mathbf{y}^{(1)} & \dots & \mathbf{y}^{(n)} \end{bmatrix}
$$ {#eq-4-35}
The determinant of $\mathbf{Y}$ is called the **Wronskian** of $\mathbf{y}^{(1)}, \dots, \mathbf{y}^{(n)}$, written
$$
W(\mathbf{y}^{(1)}, \dots, \mathbf{y}^{(n)}) = \begin{vmatrix}
y_1^{(1)} & y_1^{(2)} & \dots & y_1^{(n)} \\
y_2^{(1)} & y_2^{(2)} & \dots & y_2^{(n)} \\
\vdots & \vdots & \ddots & \vdots \\
y_n^{(1)} & y_n^{(2)} & \dots & y_n^{(n)}
\end{vmatrix}
$$ {#eq-4-36}
The columns are these solutions, each in terms of components. These solutions form a basis on $J$ if and only if $W$ is not zero at any $t_1$ in this interval. $W$ is either identically zero or nowhere zero in $J$. (This is similar to Secs. 2.6 and 3.1.)

If the solutions in (@eq-4-34) form a basis (a fundamental system), then (@eq-4-35) is often called a **fundamental matrix**. Introducing a column vector $\mathbf{c} = [c_1\ \ \dots\ \ c_n]^T$, we can now write (@eq-4-34) simply as
$$
\mathbf{y} = \mathbf{Y}\mathbf{c}
$$ {#eq-4-37}
Furthermore, we can relate (@eq-4-36) to Sec. 2.6, as follows. If $y$ and $z$ are solutions of a second-order homogeneous linear ODE, their Wronskian is
$$
W(y, z) = \begin{vmatrix} y & z \\ y' & z' \end{vmatrix}
$$
To write this ODE as a system, we have to set $y = y_1, y' = y'_1 = y_2$, and similarly for $z$ (see Sec. 4.1). But then $W(y, z)$ becomes (@eq-4-36), except for notation.
"""

append_text(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\chapters\ch4.qmd", text)
