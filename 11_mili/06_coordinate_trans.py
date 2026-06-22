# Question 6: The coordinate of a point in the cartesian coordinate system is given by (x, y) 
# and that in the polar coordinate system is given by (r, \theta). Write a user-defined 
# function to transform coordinates from one system to another.

import math

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)  # Returns angle in radians
    return r, theta

def polar_to_cartesian(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

# Example Usage
x, y = 3, 4
r, theta = cartesian_to_polar(x, y)
print(f"Cartesian ({x}, {y}) -> Polar: r = {r:.2f}, theta = {math.degrees(theta):.2f}°")