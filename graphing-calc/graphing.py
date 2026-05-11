"""FCC Graphing Calculator using NumPy + matplotlib + sympy."""
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def plot_function(expr_str, x_min=-10, x_max=10):
    x = sp.symbols("x")
    expr = sp.sympify(expr_str)
    f = sp.lambdify(x, expr, "numpy")
    xs = np.linspace(x_min, x_max, 400)
    plt.plot(xs, f(xs))
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True)
    plt.title(f"y = {expr_str}")
    plt.savefig("plot.png")
    plt.close()


def solve_eq(expr_str):
    x = sp.symbols("x")
    return sp.solve(sp.sympify(expr_str), x)


def derivative(expr_str):
    x = sp.symbols("x")
    return sp.diff(sp.sympify(expr_str), x)


def integral(expr_str):
    x = sp.symbols("x")
    return sp.integrate(sp.sympify(expr_str), x)
