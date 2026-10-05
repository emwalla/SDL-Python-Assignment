
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import argparse

"""

Reads the optical spectrum from spectrum.txt (given file), fits a polynomial to the background and a Gaussian to the spectrum.

Then plots the full spectrum, the spectrum with the polynomial (x^2 order)
overlaid, and the spectrum with the polynomial and Gaussian overlaid.

Prints best fit parameters for fitted curves and uncertainties.

"""

def parsearguments(): # Parsing argument: argument = file name
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type = str, help = "The file with wavelength and flux data")
    return parser.parse_args()

def polynomial(x, a, b, c): # Second order polynomial to fit continuum
    return (a * x**2 + x * b + c)

def gaussian(x, A, mu, sigma, a, b, c): # Where c0 = ax^2 + bx + c
    topfrac = (x - mu)**2
    bottomfrac = 2 * sigma**2
    frac = (- topfrac / bottomfrac)

    return (a * x**2 + b * x + c) + A * np.exp(frac)

def classic_plot(): # Things that I'll be repeating for each plot
    plt.xlabel('Wavelength (Å)') # From spectrum.txt
    plt.ylabel('Flux (ADU)')
    plt.show()

args = parsearguments()
wavelengths = []
fluxes = []

# Opening the file
with open(args.file, 'r') as file:
    for line in range(27): # Skipping first several lines of comments / info (code not extensible I fear)
        next(file)
    for line in file:
        line = line.strip()
        wavelength, flux = line.split(',')
        wavelengths.append((float(wavelength)))
        fluxes.append((float(flux)))

# Plot of the full spectrum
plt.plot(wavelengths, fluxes)
plt.title('Full Spectrum')
classic_plot()

# Finding the indexes where the peak appears to begin and end
def find_index(wave_val):
    for i, value in enumerate(wavelengths):
        if value > wave_val:
            return i
            break

index1 = find_index(6680) # Peak begins approx
index2 = find_index(6695) # Peak ends approx


# Polynomial fit excludes range of the peak to fit the polynomial to the continuum
popt_p, pcov_p = curve_fit(polynomial, wavelengths[:index1] + wavelengths[index2:], fluxes[:index1] + fluxes[index2:], 
                           p0=[0, -11, 30000], bounds=[(-1000, -1000, -1000), (1e9, 1e9, 1e9)])

# Plot of the full spectrum with polynomial overlaid
plt.plot(wavelengths, fluxes)
plt.plot(wavelengths, polynomial(np.asarray(wavelengths), popt_p[0], popt_p[1], popt_p[2]))
plt.title('Full Spectrum with Polynomial Overlaid')
plt.legend(['Spectrum', 'Continuum Polynomial'])
classic_plot()
uncertainties_p = np.sqrt(np.diag(pcov_p))

# Print statements about polynomial
print(f'Fitted curve: {popt_p[0]:.4f} * x^2 + {popt_p[1]:.4f} * x + {popt_p[2]:.4f}')
print(f'Uncertanties: a: {uncertainties_p[0]:.5f}, b: {uncertainties_p[1]:.5f}, c: {uncertainties_p[2]:.5f}')

#Gaussian fit
popt_g, pcov_g = curve_fit(gaussian, wavelengths, fluxes, p0=[90, 6685, 1, 0, 0, 0])

# Plot of the full spectrum with polynomial and Gaussian overlaid
plt.plot(wavelengths, fluxes)
plt.plot(wavelengths, polynomial(np.asarray(wavelengths), popt_p[0], popt_p[1], popt_p[2]))
plt.plot(wavelengths, gaussian(np.asarray(wavelengths), popt_g[0], popt_g[1], popt_g[2], popt_g[3], popt_g[4], popt_g[5]), 'r')
plt.title('Full Spectrum with Polynomial and Gaussian Overlaid')
plt.legend(['Spectrum', 'Continuum Polynomial', 'Gaussian'])
classic_plot()
uncertainties_g = np.sqrt(np.diag(pcov_g)) # Uncertainties

# Print statements about Gaussian
print(f'Amplitude: {popt_g[0]:.2f} +/- {uncertainties_g[0]:.2f} ADU')
print(f'Central Wavelength: {popt_g[1]:.2f} +/- {uncertainties_g[1]:.2f} Å') # Position at center of peak
print(f'Variance: {popt_g[2]:.2f} Å ^ 2 = {popt_g[2] ** 2:.2f} Å^2')
print(f'FWHM: {popt_g[2]:.2f} Å * 2.355 = {popt_g[2] * 2.355:.2f} Å')
print(f'sigma uncertainty: +/- {uncertainties_g[2]:.2f} Å')
print(f'Baseline: x^2 * {popt_g[3]:.4f} + x * {popt_g[4]:.4f} + {popt_g[5]:.4f}')
print(f'Baseline uncertainties: a: {uncertainties_g[3]:.5f}, b: {uncertainties_g[4]:.5f}, c: {uncertainties_g[5]:.5f}')
