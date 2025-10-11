import numpy as np
import matplotlib.pyplot as plt

# Given points
P = np.array([1, 4])
k = -4     # Correct answer
Q = np.array([k, 3])

# Midpoint of PQ
M = (P + Q) / 2

# Direction vector of PQ
PQ = Q - P

# Normal vector to bisector (same as direction of PQ)
n = PQ

# Equation of bisector: n·(x - M) = 0  → a*x + b*y = c
a, b = n
c = a*M[0] + b*M[1]

# Find slope and y-intercept
if b != 0:
    m_bisector = -a/b
    y_intercept = c/b
else:
    m_bisector = None  # vertical line case

print(f"Equation of perpendicular bisector:")
print(f"({a})x + ({b})y = {c:.2f}")
if m_bisector is not None:
    print(f"y = {m_bisector:.2f}x + {y_intercept:.2f}")

# Generate x values for plotting
x_vals = np.linspace(-6, 6, 100)
y_vals = m_bisector * x_vals + y_intercept

# Plot setup
plt.figure(figsize=(7, 6))
plt.plot(x_vals, y_vals, 'g-', lw=2, label='Perpendicular Bisector')
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'b--', lw=2, label='Line PQ')

# Mark points
plt.scatter(*P, color='red', s=60, label='P(1,4)')
plt.scatter(*Q, color='blue', s=60, label='Q(-4,3)')
plt.scatter(*M, color='purple', s=60, label='Midpoint M')

# Axis setup
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Perpendicular Bisector (k = -4)")
plt.legend()
plt.grid(True)
plt.show()

