# Question 7: Make a plot of the curve which is defined by:
# x = 2*cos(\theta) + cos(2*\theta); y = 2*sin(\theta) - sin(2*\theta)
# where 0 <= \theta <= 2*pi. Take a set of values of \theta between 0 and 2*pi, 
# calculate x and y for each from the equations above, and then, plot y as a function of x.

import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 points between 0 and 2*pi
theta = np.linspace(0, 2 * np.pi, 1000)

# Parametric equations
x = 2 * np.cos(theta) + np.cos(2 * theta)
y = 2 * np.sin(theta) - np.sin(2 * theta)

# Plotting
plt.figure(figsize=(6, 6))
plt.plot(x, y, label='Parametric Curve', color='purple')
plt.title(r'Plot of $y$ as a function of $x$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.axis('equal')
plt.show()