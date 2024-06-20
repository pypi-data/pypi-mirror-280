"""
Cylinder: Qsca vs Index
=======================

This example demonstrates how to compute and visualize the scattering efficiency (Qsca) as a function of refractive index for cylindrical scatterers using PyMieSim, considering multiple wavelengths.
"""

# %%
# Importing the package dependencies: numpy, PyMieSim
import numpy as np
from PyMieSim.experiment.scatterer import Cylinder
from PyMieSim.experiment.source import Gaussian
from PyMieSim.experiment import Setup
from PyMieSim.experiment import measure

# %%
# Defining the source
source = Gaussian(
    wavelength=[500e-9, 1000e-9, 1500e-9],  # Array of wavelengths: 500 nm, 1000 nm, 1500 nm
    polarization=30,  # Polarization angle in degrees
    optical_power=1e-3,  # 1 milliwatt
    NA=0.2  # Numerical Aperture
)

# %%
# Defining the scatterer distribution
scatterer = Cylinder(
    diameter=800e-9,  # Fixed diameter of 800 nm
    index=np.linspace(1.3, 1.9, 1500),  # Refractive index ranging from 1.3 to 1.9
    medium_index=1,  # Refractive index of the surrounding medium
    source=source
)

# %%
# Setting up the experiment
experiment = Setup(
    scatterer=scatterer,
    source=source
)

# %%
# Measuring the scattering efficiency (Qsca)
data = experiment.get(measure.Qsca)

# %%
# Plotting the results
# Visualizing how the Qsca varies with the refractive index of the cylinder.
figure = data.plot(
    x=scatterer.index,  # Refractive index as the x-axis
    y_scale='linear'  # Linear scale for the y-axis
)

# %%
# Displaying the plot
_ = figure.show()
