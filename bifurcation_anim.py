import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def logistic_map(r, x):
    """The logistic map equation."""
    return r * x * (1 - x)

# Parameters
n_iterations_max = 50   # Maximum number of iterations to animate
last_iterations = 5      # Number of iterations to plot for each r
r_values = np.linspace(2.5, 4, 500)  # Range of r values

# Initialize plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(2.5, 4)
ax.set_ylim(0, 1)
ax.set_xlabel('$r$')
ax.set_ylabel('$x_{n}$')
ax.set_title('Bifurcation Diagram (Animated)')
line, = ax.plot([], [], ',k', alpha=0.2)  # Plot points

# Data storage
x_data = []

# Animation function
def animate(n_iterations):
    global x_data  # Access global x_data

    # Iterate over r values
    for r in r_values:
        x = 0.5  # Initial condition
        for i in range(n_iterations):
            x = logistic_map(r, x)
        
        # Store last iterations
        if i >= (n_iterations - last_iterations):
            x_data.append((r, x))

    # Update plot
    line.set_data(*zip(*x_data))
    return line,

# Create animation
ani = FuncAnimation(
    fig, animate, frames=range(1, n_iterations_max + 1), interval=100, blit=True, repeat=False
)

# Save as GIF
writer = PillowWriter(fps=10)
ani.save('bifurcation_animation.gif', writer=writer)