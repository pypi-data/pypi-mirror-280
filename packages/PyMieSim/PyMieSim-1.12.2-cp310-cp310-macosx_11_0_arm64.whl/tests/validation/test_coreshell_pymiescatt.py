#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import numpy

from PyMieSim.experiment.scatterer import CoreShell
from PyMieSim.experiment.source import Gaussian
from PyMieSim.experiment import Setup
from PyMieSim.experiment import measure

import PyMieScatt as ps
PyMieScatt_measures = {
    'Qext': 0,
    'Qsca': 1,
    'Qabs': 2,
    'g': 3,
    'Qpr': 4,
    'Qback': 5,
    'Qratio': 6
}


def get_PyMieSim_data(source, core_index, shell_index, core_diameters, shell_width, measure_string: str):
    scatterer = CoreShell(
        core_diameter=core_diameters,
        shell_width=shell_width,
        core_index=core_index,
        shell_index=shell_index,
        medium_index=1.,
        source=source
    )

    experiment = Setup(
        scatterer=scatterer,
        source=source,
        detector=None
    )

    data = experiment.get(getattr(measure, measure_string), export_as_numpy=True)

    return data.squeeze()


def get_PyMieScatt_data(source, core_index, shell_index, core_diameters, shell_width, measure_string: str):
    PyMieScatt_data = []
    for core_diameter in core_diameters:
        efficiencies = ps.MieQCoreShell(
            mCore=core_index,
            mShell=shell_index,
            wavelength=source.wavelength[0],
            dCore=core_diameter,
            dShell=core_diameter + shell_width
        )

        measure_idx = PyMieScatt_measures.get(measure_string)
        data = efficiencies[measure_idx]
        PyMieScatt_data.append(float(data))

    return numpy.asarray(PyMieScatt_data).squeeze()


def get_comparison(wavelength, core_index, shell_index, core_diameters, shell_width, measure_string: str):
    source = Gaussian(
        wavelength=wavelength,
        polarization=0,
        optical_power=1e-3,
        NA=0.2
    )

    PyMieScatt_data = get_PyMieScatt_data(
        source=source,
        core_index=core_index,
        shell_index=shell_index,
        core_diameters=core_diameters,
        shell_width=shell_width,
        measure_string=measure_string
    )

    PyMieSim_data = get_PyMieSim_data(
        source=source,
        core_index=core_index,
        shell_index=shell_index,
        core_diameters=core_diameters,
        shell_width=shell_width,
        measure_string=measure_string
    )

    return PyMieSim_data, PyMieScatt_data


@pytest.mark.parametrize('measure_string', ['Qext', 'Qsca', 'Qabs', 'g', 'Qpr'])
def test_comparison(measure_string: str):
    PyMieSim_data, PyMieScatt_data = get_comparison(
        wavelength=632e-9,
        core_index=1.4 + 0.3j,
        shell_index=1.3,
        core_diameters=numpy.geomspace(10e-9, 6000e-9, 800),
        shell_width=600e-9,
        measure_string=measure_string
    )

    discrepency = numpy.isclose(PyMieSim_data, PyMieScatt_data, atol=0, rtol=1e-4)

    if not discrepency.astype(int).mean() > 0.5:
        raise ValueError('Error: mismatch on PyMieScatt calculation occuring')


if __name__ == "__main__":
    pytest.main()

# -
