import numpy as np
import matplotlib.pyplot as plt

# Defining the function f(x) = e^x + x^2 - 4
def f(x):
    return np.exp(x) + x**2 - 4

# Generate x values from -3 to 1
x = np.linspace(-3, 1, 400)
y = f(x)

# Plotting the function f(x)
plt.plot(x, y, label='$f(x) = e^x + x^2 - 4$', color='b')

# Highlight the root
root_x = -1.963624  # The root we found using Newton's method
root_y = f(root_x)
plt.plot(root_x, root_y, 'ro', label=f'Root at x = {root_x:.6f}')

# Add horizontal line at y=0 (x-axis)
plt.axhline(0, color='black', linewidth=0.5)

# Add vertical line at the root
plt.axvline(root_x, color='gray', linestyle='--', linewidth=1)

# Add labels and title
plt.title('Plot of the Function $f(x) = e^x + x^2 - 4$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
