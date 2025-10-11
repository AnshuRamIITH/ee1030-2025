# bisector_plot.py
import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the compiled C shared library
lib = ctypes.CDLL("./func.so")

# Define argument types for the C function
lib.compute_bisector.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # P array
    ctypes.POINTER(ctypes.c_double),  # Q array
    ctypes.POINTER(ctypes.c_double)   # results array
]

# --- Input Points ---
P = np.array([1.0, 4.0])    # Point P(x1, y1)
Q = np.array([-4.0, 3.0])   # Point Q(x2, y2)

# Prepare result array for [a, b, c, slope, intercept]
results = (ctypes.c_double * 5)()

# Convert numpy arrays to ctypes arrays
P_c = (ctypes.c_double * 2)(*P)
Q_c = (ctypes.c_double * 2)(*Q)

# Call the C function
lib.compute_bisector(P_c, Q_c, results)

# Extract computed values
a, b, c, slope, y_intercept = [results[i] for i in range(5)]

# --- Display Results ---
print("\n🧮 Equation of the Perpendicular Bisector:")
print(f"General form: ({a:.2f})x + ({b:.2f})y = {c:.2f}")
if abs(slope) < 1e8:
    print(f"Slope-intercept form: y = {slope:.2f}x + {y_intercept:.2f}")
else:
    print("Vertical line (undefined slope)")

# --- Compute midpoint for plotting ---
M = (P + Q) / 2

# --- Generate data for plotting ---
x_vals = np.linspace(-6, 6, 100)
if abs(slope) < 1e8:
    y_vals = slope * x_vals + y_intercept
else:
    x_vals = np.ones(100) * (-c / a)
    y_vals = np.linspace(-6, 6, 100)

# --- Plot setup ---
plt.figure(figsize=(7, 6))
plt.plot(x_vals, y_vals, 'g-', lw=2, label='Perpendicular Bisector')
plt.plot([P[0], Q[0]], [P[1], Q[1]], 'b--', lw=2, label='Line PQ')

# Mark points
plt.scatter(*P, color='red', s=60, label='P(1,4)')
plt.scatter(*Q, color='blue', s=60, label='Q(-4,3)')
plt.scatter(*M, color='purple', s=60, label='Midpoint M')

# Axis & labels
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Perpendicular Bisector using C + Python (k = -4)")
plt.legend()
plt.grid(True)
plt.show()

