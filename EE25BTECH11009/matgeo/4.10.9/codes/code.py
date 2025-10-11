import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load shared library
lib = ctypes.CDLL('./func.so')

# Prepare output array
out = (ctypes.c_double * 4)()

# Call C function
lib.find_plane(out)

# Extract results
n = np.array([out[0], out[1], out[2]])
d = out[3]

print("Normal vector (from C):", n)
print("Constant term (from C):", d)

# Multiply by 19 to get integer coefficients for clarity
n_int = 19 * n
d_int = 19 * d

print(f"\nSimplified plane: {n_int[0]:.0f}x + {n_int[1]:.0f}y + {n_int[2]:.0f}z + {d_int:.0f} = 0")

# Prepare grid for plotting
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# Plane equation: n·r + d = 0 => Z = (-d - n_x X - n_y Y)/n_z
Z = (-d_int - n_int[0]*X - n_int[1]*Y) / n_int[2]

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot required plane
ax.plot_surface(X, Y, Z, alpha=0.6, color='skyblue', label='Required Plane')

# Plot perpendicular plane (P3)
Z3 = (-8 - 5*X - 3*Y)/(-6)
ax.plot_surface(X, Y, Z3, alpha=0.3, color='orange')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plane through line of intersection ⟂ (5,3,-6) plane')
plt.savefig("../figs/Figure_2.png")
plt.show()

