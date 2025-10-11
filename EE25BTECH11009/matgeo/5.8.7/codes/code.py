import numpy as np
import matplotlib.pyplot as plt

# Coefficient matrix and constants
A = np.array([[3, -1],
              [4, -2]])
b = np.array([40, 50])

try:
    # Solve the linear system
    solution = np.linalg.solve(A, b)
    x_sol, y_sol = solution

    print("The system has a unique solution:")
    print(f"x = {x_sol}")
    print(f"y = {y_sol}")
    print(f"Total questions = {x_sol + y_sol}")

    # Plotting
    x_vals = np.linspace(x_sol - 20, x_sol + 20, 400)
    y1 = 3 * x_vals - 40           # from 3x - y = 40 → y = 3x - 40
    y2 = 2 * x_vals - 25           # from 4x - 2y = 50 → y = 2x - 25

    plt.figure(figsize=(8, 8))
    plt.plot(x_vals, y1, label=r'$3x - y = 40$')
    plt.plot(x_vals, y2, label=r'$4x - 2y = 50$')
    plt.plot(x_sol, y_sol, 'ro', label=f'Intersection ({x_sol:.2f}, {y_sol:.2f})')

    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.xlabel("x (Right Answers)")
    plt.ylabel("y (Wrong Answers)")
    plt.title("System of Equations with a Unique Solution")
    plt.legend()
    plt.grid(True)
    plt.savefig("/home/anshu-ram/Desktop/local-repositry/EE25BTECH11009/matgeo/5_8_7/figs/Figure_1.png")
    plt.show()

except np.linalg.LinAlgError:
    print("The system does not have a unique solution.")

