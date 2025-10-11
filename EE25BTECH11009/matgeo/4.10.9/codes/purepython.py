

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# ------------------------------------------------------------
# Step 1: Define the given data
# ------------------------------------------------------------
# Plane 1 : r·(1,2,3) = 4
# Plane 2 : r·(2,1,-1) = -5
# Plane 3 : r·(5,3,-6) = -8 (perpendicular plane)

n1 = np.array([1, 2, 3])      # Normal to Plane 1
n2 = np.array([2, 1, -1])     # Normal to Plane 2
n3 = np.array([5, 3, -6])     # Normal to perpendicular plane
c1 = 4
c2 = -5
c3 = -8

# ------------------------------------------------------------
# Step 2: Equation of required plane
# ------------------------------------------------------------
# Required plane passes through line of intersection of Plane 1 & Plane 2
# and is perpendicular to Plane 3
# So, its normal n = n1 + λ*n2
# Condition for perpendicularity: n · n3 = 0

# Solve for λ
lambda_val = -np.dot(n1, n3) / np.dot(n2, n3)

# Normal and constant term for the required plane
n = n1 + lambda_val * n2
c = c1 + lambda_val * c2

# Multiply through by 19 to clear fractions (optional)
n = n * 19
c = c * 19

print("λ =", round(lambda_val, 3))
print("Normal vector of required plane =", n)
print(f"Equation of required plane: {n[0]:.0f}x + {n[1]:.0f}y + {n[2]:.0f}z = {c:.0f}")

# ------------------------------------------------------------
# Step 3: Plot the planes
# ------------------------------------------------------------
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)

# Plane 1: z = (4 - x - 2y)/3
Z1 = (c1 - n1[0]*X - n1[1]*Y) / n1[2]

# Plane 2: z = (-5 - 2x - y)/(-1) = 2x + y + 5
Z2 = (c2 - n2[0]*X - n2[1]*Y) / n2[2]

# Required Plane: 33x + 45y + 50z = 41 → z = (41 - 33x - 45y)/50
Z = (c - n[0]*X - n[1]*Y) / n[2]

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot all three planes
ax.plot_surface(X, Y, Z1, color='cyan', alpha=0.5)
ax.plot_surface(X, Y, Z2, color='orange', alpha=0.5)
ax.plot_surface(X, Y, Z, color='green', alpha=0.6)

# ------------------------------------------------------------
# Step 4: Plot the line of intersection of Plane 1 and Plane 2
# ------------------------------------------------------------
# The direction of the line is along cross(n1, n2)
d = np.cross(n1, n2)

# To find a point on the line, solve both plane equations together
# n1·r = c1, n2·r = c2
A = np.vstack((n1, n2, d))
b = np.array([c1, c2, 0])
r0 = np.linalg.solve(A, b)  # point on line

# Generate line points
t = np.linspace(-3, 3, 50)
line_points = r0[:, None] + d[:, None] * t
ax.plot(line_points[0], line_points[1], line_points[2], color='k', linewidth=3)

# ------------------------------------------------------------
# Step 5: Add labels and legend
# ------------------------------------------------------------
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Plane Intersection and Required Plane")
ax.view_init(elev=20, azim=40)

# Custom legend
legend_elements = [
    Patch(facecolor='cyan', edgecolor='k', label='Plane 1'),
    Patch(facecolor='orange', edgecolor='k', label='Plane 2'),
    Patch(facecolor='green', edgecolor='k', label='Required Plane'),
    Line2D([0], [0], color='k', lw=3, label='Line of Intersection')
]
ax.legend(handles=legend_elements)

plt.tight_layout()
plt.show()

