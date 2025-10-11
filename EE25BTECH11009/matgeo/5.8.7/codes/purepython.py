import numpy as np
import matplotlib.pyplot as plt

A = np.array([[3, -1],
              [4, -2]])
b = np.array([40, 50])

try:
    solution = np.linalg.solve(A, b)
    x_sol, y_sol = solution
    print(f"The system has a unique solution:")
    print(f"x = {x_sol}")
    print(f"y = {y_sol}")
    x_vals = np.linspace(x_sol - 40, x_sol + 40, 400)
    y1 = (3 * x_vals - 40)
    y2 = (2 * x_vals - 25)
    plt.figure(figsize=(8, 8))
    plt.plot(x_vals, y1, label=r'$3x - y = 40$')
    plt.plot(x_vals, y2, label=r'$4x - 2y = 50$')
    plt.plot(x_sol, y_sol, 'ro', label=f'Intersection ({x_sol}, {y_sol})')
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("System of Equations with a Unique Solution")
    plt.legend()
    plt.grid(True)
    plt.savefig("../figs/Figure_2.png")
    plt.show()

except np.linalg.LinAlgError:
    print("The system does not have a unique solution.")

