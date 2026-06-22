# Question 5: Write a program for calculating the wavelengths of emission lines in the 
# spectrum of the hydrogen atom, based on the Rydberg formula:
# 1/\lambda = R * (1/m^2 - 1/n^2)
# The value of R = 1.097 x 10^-2 m^-1 (Note: Adjusted to 1.097e7 for physical accuracy)

def calculate_wavelength(m, n):
    if n <= m:
        return "Error: 'n' must be greater than 'm'."
    
    R = 1.097e7  # Rydberg constant in m^-1
    inv_lambda = R * ((1 / m**2) - (1 / n**2))
    lambda_val = 1 / inv_lambda
    return lambda_val

# Example for the Balmer Series (m=2, n=3)
m = int(input("Enter inner orbit (m): "))
n = int(input("Enter outer orbit (n): "))

wavelength = calculate_wavelength(m, n)
if isinstance(wavelength, str):
    print(wavelength)
else:
    print(f"The wavelength is: {wavelength:.3e} meters ({wavelength * 1e9:.2f} nm)")