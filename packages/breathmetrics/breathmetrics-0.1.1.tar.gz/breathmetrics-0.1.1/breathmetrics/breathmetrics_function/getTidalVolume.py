"""
Module: getTidalVolume

This module provides functions for calculating tidal volume from processed capnostream data,
from detected inhale and exhale onsets, and visualizing the detection results.

Dependencies:
- numpy (imported as np)
- pandas (imported as pd)
- matplotlib.pyplot (imported as plt)
- utils.flatten_list.flatten_list (custom utility function for flattening lists)
- utils.average_list.average (custom utility function for calculating averages)

"""


import numpy as np

from utils.flatten_list import flatten_list
from utils.average_list import average

def get_tidal_volume(yhat, exhaleonsets, sample_rate, interbreath_interval, index):
    """
    Calculate tidal volume from processed capnostream data and detect inhale/exhale onsets.

    Args:
        path (str): The file path for saving detailed tidal volume samples.
        xaxis (List[float]): The corresponding time axis.
        yhat (List[float]): A list of processed capnostream data values.
        exhaleonsets (List[int]): A list of exhale onset indices.
        sample_rate (float): The sample rate (in Hz) of the data.
        interbreath_interval (float): The interbreath interval (in seconds).
        index (int): The index sheet of the saved excel file sample.

    Returns:
        float: The calculated tidal volume.

    This function calculates tidal volume from the provided processed capnostream data and exhale onsets. It also saves
    detailed tidal volume samples to an Excel file and returns the calculated tidal volume.

    Usage:
    1. Import this function from the module.
    2. Call the function with the appropriate arguments.

    Example:
    ```python
    from breathmetrics_function.getTidalVolume import get_tidal_volume

    tidal_volume = get_tidal_volume("path/to/save/samples.xlsx", xaxis, yhat, exhaleonsets, sample_rate, interbreath_interval, 1)
    ```
    """
    y = flatten_list(yhat)
    detrend_constant = 10
    mercury_density = 13.6
    tidalvolume = 0
    exhalelist = exhaleonsets
    tidalvolumes = list()
    detailed_tidal_volumes = []
    actual_y_values = []
    for i in range(len(exhalelist)-1):
        yt = y[exhalelist[i]:exhalelist[i+1]]
        res = [(abs(y[exhalelist[i]]) + X)*detrend_constant for X in yt]
        actual_y_values.append(res)
        tidalvolume = round((np.trapz(res, dx=1)*mercury_density)/(sample_rate*interbreath_interval),2)
        detailed_tidal_volumes.append([exhalelist[i],exhalelist[i+1], tidalvolume])
        tidalvolumes.append(tidalvolume)
    tidalvolumes.sort()
    volume = average(tidalvolumes)
    return volume

