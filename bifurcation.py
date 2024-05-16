import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    """The logistic map equation."""
    return r * x * (1 - x)

def find_r(data):
    return data[0]

def find_x(data):
    return data[1]

# Parameters
n = 200   # Number of iterations
r_values = np.linspace(2.5, 4, 10000)  # Range of r values

# Initialize plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(2.5, 4)
ax.set_ylim(0, 1)
ax.set_xlabel('$r$')
ax.set_ylabel('$x_{n}$')
ax.set_title('Bifurcation Diagram of the Logistic Map')

x_data = []

# Iterate over r values
for r in r_values:
    x = 0.5  # Initial condition
    for i in range(n):
        x = logistic_map(r, x)
        x_data.append((r, x))

# Organize data
x = list(map(find_x, x_data))
r = list(map(find_r, x_data))

ax.plot(r, x, ',k', alpha=0.2)  # Plot points
plt.show()