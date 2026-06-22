# Question 1: The height of a satellite above the earth should be h = ((G*M_E*T^2)/(4*pi^2))^(1/3) - R_E
# where, G = 6.673 x 10^-11 Nm^2/kg^2 is the universal gravitational constant. 
# M_E = 5.98 x 10^24 kg, mass of the earth, R_E = 6.37 x 10^6 m, radius of the earth.
# A geosynchronous orbit (GEO) is a prograde, low inclination orbit about Earth having a period
# of 23 hours 56 minutes 4 seconds. A spacecraft in geosynchronous orbit appears to remain above
# Earth at a constant longitude, although it may seem to wander north and south. 
# Estimate the height of a Geosynchronous satellite.

import math

# Constants
G = 6.673e-11      # Universal gravitational constant (N m^2/kg^2)
M_E = 5.98e24      # Mass of the Earth (kg)
R_E = 6.37e6       # Radius of the Earth (m)

# Time period T converted to seconds: 23h 56m 4s
T = (23 * 3600) + (56 * 60) + 4 

# Kepler's Third Law rearranged for height h
h = ((G * M_E * (T**2)) / (4 * (math.pi**2)))**(1/3) - R_E

print(f"The height of the Geosynchronous satellite is: {h / 1000:.2f} km")