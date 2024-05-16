import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def logistic_map(r, x):
    """The logistic map equation."""
    return r * x * (1 - x)

# Parameters
n_iterations_max = 50   # Maximum number of iterations
last_iterations = 5      # Number of iterations to plot for each r
r_values = np.linspace(2.5, 4, 500)  # Range of r values

# Initialize 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(2.5, 4)
ax.set_ylim(0, 1)
ax.set_zlim(0, n_iterations_max)
ax.set_xlabel('$r$')
ax.set_ylabel('$x_{n}$')
ax.set_zlabel('Iteration (n)')
ax.set_title('3D Bifurcation Diagram')

# Plot
scatter = ax.scatter([], [], [], c='k', s=1, marker='.', alpha=0.2)

# Calculate data for all iterations
x_data = []
y_data = []
z_data = []

def graph_iter(n_iterations):
    global x_data, y_data, z_data

    # Iterate over r values
    for r in r_values:
        x = 0.5  # Initial condition
        for i in range(n_iterations):
            x = logistic_map(r, x)

            # Store last iterations
            if i >= (n_iterations - last_iterations):
                x_data.append(r)
                y_data.append(x)
                z_data.append(i)

    # Update plot
    scatter._offsets3d = (x_data, y_data, z_data)

for n in range(1, n_iterations_max+1):
    graph_iter(n)

plt.show()
