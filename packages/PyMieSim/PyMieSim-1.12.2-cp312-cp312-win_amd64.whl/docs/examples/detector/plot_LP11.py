"""
LP11 Mode Detector
==================

This example demonstrates the initialization and visualization of an LP11 Mode detector using PyMieSim.
"""

# %%
# Importing the package: PyMieSim
from PyMieSim.single.detector import CoherentMode

# %%
# Initializing the detector
detector = CoherentMode(
    mode_number="LP11",  # Specifying LP11 mode
    sampling=300,  # Number of sampling points
    NA=0.3,  # Numerical Aperture
    gamma_offset=0,  # Gamma offset
    phi_offset=30,  # Phi offset in degrees
)

# %%
# Plotting the detector
figure = detector.plot()

# %%
# Displaying the plot
_ = figure.show()
