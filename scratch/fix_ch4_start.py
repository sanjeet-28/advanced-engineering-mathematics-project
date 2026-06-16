def fix_start(path):
    correct_start = r"""---
title: "CHAPTER 04: Systems of ODEs. Phase Plane. Qualitative Methods"
---

Tying in with Chap. 3, we present another method of solving higher order ODEs in Sec. 4.1. This converts any $n$th-order ODE into a system of $n$ first-order ODEs. We also show some applications. Moreover, in the same section we solve systems of first-order ODEs that occur directly in applications, that is, not derived from an $n$th-order ODE but dictated by the application such as two tanks in mixing problems and two circuits in electrical networks. (The elementary aspects of vectors and matrices needed in this chapter are reviewed in Sec. 4.0 and are probably familiar to most students.)

In Sec. 4.3 we introduce a totally different way of looking at systems of ODEs. The method consists of examining the general behavior of whole families of solutions of ODEs in the phase plane, and aptly is called the phase plane method. It gives information on the stability of solutions. (Stability of a physical system is desirable and means roughly that a small change at some instant causes only a small change in the behavior of the system at later times.) This approach to systems of ODEs is a qualitative method because it depends only on the nature of the ODEs and does not require the actual solutions. This can be very useful because it is often difficult or even impossible to solve systems of ODEs. In contrast, the approach of actually solving a system is known as a quantitative method.

The phase plane method has many applications in control theory, circuit theory, population dynamics and so on. Its use in linear systems is discussed in Secs. 4.3, 4.4, and 4.6 and its even more important use in nonlinear systems is discussed in Sec. 4.5 with applications to the pendulum equation and the Lotka–Volterra population model. The chapter closes with a discussion of nonhomogeneous linear systems of ODEs.

**NOTATION.** We continue to denote unknown functions by $y$; thus, $y_1(t), y_2(t)$, analogous to Chaps. 1–3. (Note that some authors use $x$ for functions, when dealing with systems of ODEs, e.g., $x_1(t), x_2(t)$.)

**Prerequisite:** Chap. 2.

**References and Answers to Problems:** App. 1 Part A, and App. 2.

## 4.0 For Reference: Basics of Matrices and Vectors {#sec-4-0}

For clarity and simplicity of notation, we use matrices and vectors in our discussion of linear systems of ODEs. We need only a few elementary facts (and not the bulk of the material of Chaps. 7 and 8). Most students will very likely be already familiar with these facts. Thus this section is for reference only. Begin with Sec. 4.1 and consult Sec. 4.0 as needed.

Most of our linear systems will consist of two linear ODEs in two unknown functions $y_1(t), y_2(t)$,
$$
\begin{aligned}
y'_1 &= a_{11}y_1 + a_{12}y_2 \\
y'_2 &= a_{21}y_1 + a_{22}y_2
\end{aligned}
\quad \text{for example,} \quad
\begin{aligned}
y'_1 &= -5y_1 + 2y_2 \\
y'_2 &= -13y_1 + \frac{1}{2}y_2
\end{aligned}
$$ {#eq-4-1}
(perhaps with additional given functions $g_1(t), g_2(t)$ on the right in the two ODEs).

Similarly, a linear system of $n$ first-order ODEs in $n$ unknown functions $y_1(t), \dots, y_n(t)$ is of the form
$$
\begin{aligned}
y'_1 &= a_{11}y_1 + a_{12}y_2 + \dots + a_{1n}y_n \\
y'_2 &= a_{21}y_1 + a_{22}y_2 + \dots + a_{2n}y_n \\
&\ \ \dots \\
y'_n &= a_{n1}y_1 + a_{n2}y_2 + \dots + a_{nn}y_n
\end{aligned}
$$ {#eq-4-2}
(perhaps with an additional given function on the right in each ODE).

### Some Definitions and Terms

**Matrices.** In (@eq-4-1) the (constant or variable) coefficients form a $2 \times 2$ matrix $\mathbf{A}$, that is, an array
$$
\mathbf{A} = [a_{jk}] = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}, \quad \text{for example,} \quad \mathbf{A} = \begin{bmatrix} -5 & 2 \\ -13 & \frac{1}{2} \end{bmatrix}
$$ {#eq-4-3}
Similarly, the coefficients in (@eq-4-2) form an $n \times n$ matrix
$$
\mathbf{A} = [a_{jk}] = \begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\dots & \dots & \ddots & \dots \\
a_{n1} & a_{n2} & \dots & a_{nn}
\end{bmatrix}
$$ {#eq-4-4}
The $a_{jk}$ are called **entries**, the horizontal lines **rows**, and the vertical lines **columns**. Thus, in (@eq-4-3) the first row is $[a_{11}\ \ a_{12}]$, the second row is $[a_{21}\ \ a_{22}]$, and the first and second columns are
$$
\begin{bmatrix} a_{11} \\ a_{21} \end{bmatrix} \quad \text{and} \quad \begin{bmatrix} a_{12} \\ a_{22} \end{bmatrix}
$$
In the "double subscript notation" for entries, the first subscript denotes the row and the second the column in which the entry stands. Similarly in (@eq-4-4). The **main diagonal** is the diagonal $a_{11}, a_{22}, \dots, a_{nn}$ in (@eq-4-4), hence $a_{11}, a_{22}$ in (@eq-4-3).

We shall need only square matrices, that is, matrices with the same number of rows and columns, as in (@eq-4-3) and (@eq-4-4).

**Vectors.** A **column vector** $\mathbf{x}$ with $n$ components is of the form
$$
\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ \dots \\ x_n \end{bmatrix}, \quad \text{thus if } n = 2, \quad \mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
$$
Similarly, a **row vector** $\mathbf{v}$ is of the form
$$
\mathbf{v} = [v_1 \ \ \dots \ \ v_n], \quad \text{thus if } n = 2, \quad \mathbf{v} = [v_1 \ \ v_2]
$$

### Calculations with Matrices and Vectors

**Equality.** Two $n \times n$ matrices are equal if and only if corresponding entries are equal. Thus for $n = 2$, let
$$
\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} \quad \text{and} \quad \mathbf{B} = \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix}
$$
Then $\mathbf{A} = \mathbf{B}$ if and only if
$$
a_{11} = b_{11}, \quad a_{12} = b_{12}, \quad a_{21} = b_{21}, \quad a_{22} = b_{22}
$$
Two column vectors (or two row vectors) are equal if and only if they both have $n$ components and corresponding components are equal. Thus, let
$$
\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} \quad \text{and} \quad \mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
$$
Then $\mathbf{v} = \mathbf{x}$ if and only if $v_1 = x_1$, $v_2 = x_2$.

**Addition** is performed by adding corresponding entries (or components); here, matrices must both be $n \times n$, and vectors must both have the same number of components. Thus for $n = 2$,
$$
\mathbf{A} + \mathbf{B} = \begin{bmatrix} a_{11} + b_{11} & a_{12} + b_{12} \\ a_{21} + b_{21} & a_{22} + b_{22} \end{bmatrix}, \quad \mathbf{v} + \mathbf{x} = \begin{bmatrix} v_1 + x_1 \\ v_2 + x_2 \end{bmatrix}
$$ {#eq-4-5}

**Scalar multiplication** (multiplication by a number $c$) is performed by multiplying each entry (or component) by $c$. For example, if
$$
\mathbf{A} = \begin{bmatrix} 9 & 3 \\ -2 & 0 \end{bmatrix}, \quad \text{then} \quad -7\mathbf{A} = \begin{bmatrix} -63 & -21 \\ 14 & 0 \end{bmatrix}
$$
If $\mathbf{v} = \begin{bmatrix} 0.4 \\ -13 \end{bmatrix}$, then $10\mathbf{v} = \begin{bmatrix} 4 \\ -130 \end{bmatrix}$.

**Matrix Multiplication.** The product $\mathbf{C} = \mathbf{AB}$ (in this order) of two $n \times n$ matrices $\mathbf{A} = [a_{jk}]$ and $\mathbf{B} = [b_{jk}]$ is the $n \times n$ matrix with entries
$$
c_{jk} = \sum_{m=1}^n a_{jm} b_{mk}, \quad j = 1, \dots, n; \ k = 1, \dots, n
$$ {#eq-4-6}
that is, multiply each entry in the $j$th row of $\mathbf{A}$ by the corresponding entry in the $k$th column of $\mathbf{B}$ and then add these $n$ products. One says briefly that this is a "multiplication of rows into columns." For example,
$$
\begin{bmatrix} 9 & 3 \\ -2 & 0 \end{bmatrix} \begin{bmatrix} 1 & -4 \\ 2 & 5 \end{bmatrix} = \begin{bmatrix} 9 \cdot 1 + 3 \cdot 2 & 9 \cdot (-4) + 3 \cdot 5 \\ -2 \cdot 1 + 0 \cdot 2 & -2 \cdot (-4) + 0 \cdot 5 \end{bmatrix} = \begin{bmatrix} 15 & -21 \\ -2 & 8 \end{bmatrix}
$$
**CAUTION!** Matrix multiplication is not commutative, in general. In our example,
$$
\begin{bmatrix} 1 & -4 \\ 2 & 5 \end{bmatrix} \begin{bmatrix} 9 & 3 \\ -2 & 0 \end{bmatrix} = \begin{bmatrix} 1 \cdot 9 + (-4) \cdot (-2) & 1 \cdot 3 + (-4) \cdot 0 \\ 2 \cdot 9 + 5 \cdot (-2) & 2 \cdot 3 + 5 \cdot 0 \end{bmatrix} = \begin{bmatrix} 17 & 3 \\ 8 & 6 \end{bmatrix}
$$
Multiplication of an $n \times n$ matrix $\mathbf{A}$ by a vector $\mathbf{x}$ with $n$ components is defined by the same rule: $\mathbf{v} = \mathbf{Ax}$ is the vector with the $n$ components
$$
v_j = \sum_{m=1}^n a_{jm} x_m, \quad j = 1, \dots, n
$$
For example,
$$
\begin{bmatrix} 12 & 7 \\ -8 & 3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 12x_1 + 7x_2 \\ -8x_1 + 3x_2 \end{bmatrix}
$$

### Systems of ODEs as Vector Equations

**Differentiation.** The derivative of a matrix (or vector) with variable entries (or components) is obtained by differentiating each entry (or component). Thus, if
$$
\mathbf{y}(t) = \begin{bmatrix} y_1(t) \\ y_2(t) \end{bmatrix} = \begin{bmatrix} e^{-2t} \\ \sin t \end{bmatrix}, \quad \text{then} \quad \mathbf{y}'(t) = \begin{bmatrix} y'_1(t) \\ y'_2(t) \end{bmatrix} = \begin{bmatrix} -2e^{-2t} \\ \cos t \end{bmatrix}
$$
Using matrix multiplication and differentiation, we can now write (@eq-4-1) as
$$
\mathbf{y}' = \mathbf{Ay}
$$ {#eq-4-7}
Similarly for (@eq-4-2) by means of an $n \times n$ matrix $\mathbf{A}$ and a column vector $\mathbf{y}$ with $n$ components, namely, $\mathbf{y}' = \mathbf{Ay}$. The vector equation (@eq-4-7) is equivalent to two equations for the components, and these are precisely the two ODEs in (@eq-4-1).

### Some Further Operations and Terms

**Transposition** is the operation of writing columns as rows and conversely and is indicated by $^T$. Thus the transpose of the $2 \times 2$ matrix
$$
\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} = \begin{bmatrix} -5 & 2 \\ -13 & \frac{1}{2} \end{bmatrix}
$$
is
$$
\mathbf{A}^T = \begin{bmatrix} a_{11} & a_{21} \\ a_{12} & a_{22} \end{bmatrix} = \begin{bmatrix} -5 & -13 \\ 2 & \frac{1}{2} \end{bmatrix}
$$
The transpose of a column vector, say, $\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$, is a row vector, $\mathbf{v}^T = [v_1\ \ v_2]$, and conversely.

**Inverse of a Matrix.** The $n \times n$ unit matrix $\mathbf{I}$ is the $n \times n$ matrix with main diagonal $1, 1, \dots, 1$ and all other entries zero. If, for a given $n \times n$ matrix $\mathbf{A}$, there is an $n \times n$ matrix $\mathbf{B}$ such that $\mathbf{AB} = \mathbf{BA} = \mathbf{I}$, then $\mathbf{A}$ is called **nonsingular** and $\mathbf{B}$ is called the **inverse** of $\mathbf{A}$ and is denoted by $\mathbf{A}^{-1}$; thus
$$
\mathbf{AA}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}
$$ {#eq-4-8}
The inverse exists if the determinant $\det \mathbf{A}$ of $\mathbf{A}$ is not zero.

If $\mathbf{A}$ has no inverse, it is called **singular**. For $n = 2$,
$$
\mathbf{A}^{-1} = \frac{1}{\det \mathbf{A}} \begin{bmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{bmatrix}
$$ {#eq-4-9}
where the determinant of $\mathbf{A}$ is
$$
\det \mathbf{A} = \begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix} = a_{11}a_{22} - a_{12}a_{21}
$$ {#eq-4-10}
(For general $n$, see Sec. 7.7, but this will not be needed in this chapter.)

**Linear Independence.** $r$ given vectors $\mathbf{v}^{(1)}, \dots, \mathbf{v}^{(r)}$ with $n$ components are called a **linearly independent set** or, more briefly, **linearly independent**, if
$$
c_1 \mathbf{v}^{(1)} + \dots + c_r \mathbf{v}^{(r)} = \mathbf{0}
$$ {#eq-4-11}
implies that all scalars $c_1, \dots, c_r$ must be zero; here, $\mathbf{0}$ denotes the zero vector, whose $n$ components are all zero. If (@eq-4-11) also holds for scalars not all zero (so that at least one of these scalars is not zero), then these vectors are called a **linearly dependent set** or, briefly, **linearly dependent**, because then at least one of them can be expressed as a linear combination of the others; that is, if, for instance, $c_1 \neq 0$ in (@eq-4-11), then we can obtain
$$
\mathbf{v}^{(1)} = -\frac{1}{c_1} \left( c_2 \mathbf{v}^{(2)} + \dots + c_r \mathbf{v}^{(r)} \right)
$$

### Eigenvalues, Eigenvectors

Eigenvalues and eigenvectors will be very important in this chapter (and, as a matter of fact, throughout mathematics).

Let $\mathbf{A} = [a_{jk}]$ be an $n \times n$ matrix. Consider the equation
$$
\mathbf{Ax} = \lambda \mathbf{x}
$$ {#eq-4-12}
where $\lambda$ is a scalar (a real or complex number) to be determined and $\mathbf{x}$ is a vector to be determined. Now, for every $\lambda$, a solution is $\mathbf{x} = \mathbf{0}$. A scalar $\lambda$ such that (@eq-4-12) holds for some vector $\mathbf{x} \neq \mathbf{0}$ is called an **eigenvalue** of $\mathbf{A}$, and this vector $\mathbf{x}$ is called an **eigenvector** of $\mathbf{A}$ corresponding to this eigenvalue $\lambda$.

We can write (@eq-4-12) as $\mathbf{Ax} - \lambda \mathbf{x} = \mathbf{0}$ or
$$
(\mathbf{A} - \lambda \mathbf{I})\mathbf{x} = \mathbf{0}
$$ {#eq-4-13}
These are $n$ linear algebraic equations in the $n$ unknowns $x_1, \dots, x_n$ (the components of $\mathbf{x}$). For these equations to have a solution $\mathbf{x} \neq \mathbf{0}$, the determinant of the coefficient matrix $\mathbf{A} - \lambda \mathbf{I}$ must be zero. This is proved as a basic fact in linear algebra (Theorem 4 in Sec. 7.7). In this chapter we need this only for $n = 2$. Then (@eq-4-13) is
$$
(\mathbf{A} - \lambda \mathbf{I})\mathbf{x} = \mathbf{0}
$$ {#eq-4-14}
in components,
$$
\begin{aligned}
(a_{11} - \lambda)x_1 + a_{12}x_2 &= 0 \\
a_{21}x_1 + (a_{22} - \lambda)x_2 &= 0
\end{aligned}
$$ {#eq-4-14star}
Now $\mathbf{A} - \lambda \mathbf{I}$ is singular if and only if its determinant $\det(\mathbf{A} - \lambda \mathbf{I})$, called the **characteristic determinant** of $\mathbf{A}$ (also for general $n$), is zero. This gives
$$
\det(\mathbf{A} - \lambda \mathbf{I}) = \begin{vmatrix} a_{11} - \lambda & a_{12} \\ a_{21} & a_{22} - \lambda \end{vmatrix} = (a_{11} - \lambda)(a_{22} - \lambda) - a_{12}a_{21} = \lambda^2 - (a_{11} + a_{22})\lambda + a_{11}a_{22} - a_{12}a_{21} = 0
$$ {#eq-4-15}
This quadratic equation in $\lambda$ is called the **characteristic equation** of $\mathbf{A}$. Its solutions are the eigenvalues $\lambda_1$ and $\lambda_2$ of $\mathbf{A}$. First determine these. Then use (@eq-4-14star) with $\lambda = \lambda_1$ to determine an eigenvector $\mathbf{x}^{(1)}$ of $\mathbf{A}$ corresponding to $\lambda_1$. Finally use (@eq-4-14star) with $\lambda = \lambda_2$ to find an eigenvector $\mathbf{x}^{(2)}$ of $\mathbf{A}$ corresponding to $\lambda_2$. Note that if $\mathbf{x}$ is an eigenvector of $\mathbf{A}$, so is $k\mathbf{x}$ with any $k \neq 0$.

### EXAMPLE 1 Eigenvalue Problem

Find the eigenvalues and eigenvectors of the matrix
$$
\mathbf{A} = \begin{bmatrix} -4.0 & 4.0 \\ -1.6 & 1.2 \end{bmatrix}
$$ {#eq-4-16}

**Solution.** The characteristic equation is the quadratic equation
$$
\det(\mathbf{A} - \lambda \mathbf{I}) = \begin{vmatrix} -4.0 - \lambda & 4.0 \\ -1.6 & 1.2 - \lambda \end{vmatrix} = \lambda^2 + 2.8\lambda + 1.6 = 0
$$
It has the solutions $\lambda_1 = -2$ and $\lambda_2 = -0.8$. These are the eigenvalues of $\mathbf{A}$.

Eigenvectors are obtained from (@eq-4-14star). For $\lambda = \lambda_1 = -2$ we have from (@eq-4-14star)
$$
\begin{aligned}
(-4.0 + 2.0)x_1 + 4.0x_2 &= 0 \\
-1.6x_1 + (1.2 + 2.0)x_2 &= 0
\end{aligned}
$$
A solution of the first equation is $x_1 = 2, x_2 = 1$. This also satisfies the second equation. (Why?) Hence an eigenvector of $\mathbf{A}$ corresponding to $\lambda_1 = -2$ is
$$
\mathbf{x}^{(1)} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}
$$ {#eq-4-17}
Similarly,
$$
\mathbf{x}^{(2)} = \begin{bmatrix} 1 \\ 0.8 \end{bmatrix}
$$
is an eigenvector of $\mathbf{A}$ corresponding to $\lambda_2 = -0.8$, as obtained from (@eq-4-14star) with $\lambda = \lambda_2 = -0.8$. Verify this. $\blacksquare$

"""
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # We find where Section 4.1 starts. Section 4.1 line is:
    # ## 4.1 Systems of ODEs as Models in Engineering Applications {#sec-4-1}
    idx = -1
    for i, line in enumerate(lines):
        if "## 4.1 Systems of ODEs as Models" in line:
            idx = i
            break
            
    if idx == -1:
        print("Error: Could not find Section 4.1 line in file.")
        return
        
    remaining_content = "".join(lines[idx:])
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(correct_start + "\n" + remaining_content)
        
    print(f"Successfully fixed Section 4.0 in {path}")

if __name__ == "__main__":
    fix_start(r"c:\Users\sanje\OneDrive\Desktop\anew\advanced-engineering-mathematics-project\chapters\ch4.qmd")
