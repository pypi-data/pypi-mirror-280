"""
Module: getInhaleExhaleonsets

This module provides functions for detecting inhale and exhale onsets in processed capnostream data and visualizing the detected onsets.

Dependencies:
- matplotlib.pyplot (imported as plt)
- preprocessing.cleaningInhaleOnsets.cleaningin (custom utility function for cleaning inhale onsets)
- preprocessing.cleaningExhaleOnsets.cleaningex (custom utility function for cleaning exhale onsets)

"""

import matplotlib.pyplot as plt

from utils.flatten_list import flatten_list

from preprocessing.cleaningInhaleOnsets import cleaningin
from preprocessing.cleaningExhaleOnsets import cleaningex

def onsets_detection(start,end, sensor, yhat, xaxis, sample_rate):
    """
    Detect inhale and exhale onsets in processed capnostream data.

    Args:
        yhat (List[float]): A list of processed capnostream values.
        xaxis (List[float]): The corresponding time axis.
        sample_rate (float): The sample rate (in Hz) of the data.

    Returns:
        Tuple[List[float], List[float]]: A tuple containing two lists:
        - List of detected inhale onsets (in indices).
        - List of detected exhale onsets (in indices).

    This function detects inhale and exhale onsets in the processed capnostream data and
    returns their indices.

    Usage:
    1. Import this function from the module.
    2. Call the function with the appropriate arguments.

    Example:
    ```python
    from breathmetrics_function.getInhaleExhaleonsets import onsets_detection

    inhale_onsets, exhale_onsets = onsets_detection(yhat, xaxis, sample_rate)
    ```
    """
    # plt.clf()
    for i in range(len(yhat)):
        yhat[i] = round(yhat[i],1)
    inhaleonsets = []
    exhaleonsets = []
    for i in range(len(yhat)-1):
        if (yhat[i] == 0 and yhat[i]<yhat[i+1]):
            inhaleonsets.append(i)
        if (yhat[i] == 0 and yhat[i]>yhat[i+1]):
            exhaleonsets.append(i)
    for i in range(10):
        inhaleonsets,exhaleonsets = cleaningex(inhaleonsets,exhaleonsets)
        inhaleonsets,exhaleonsets = cleaningin(inhaleonsets,exhaleonsets)
    # inhaleonsets_min = [i / sample_rate for i in inhaleonsets]
    # exhaleonsets_min = [i / sample_rate for i in exhaleonsets]
    # plt.plot(xaxis, yhat*10, 'g')
    # plt.plot(inhaleonsets_min, yhat[inhaleonsets]*10, 'x:r')
    # plt.plot(exhaleonsets_min, yhat[exhaleonsets]*10, 'x:b')
    # plt.xlabel('Time in sec')
    # plt.ylabel('Baseline temperature in degree celcius')
    # plt.title(f"Normalized Data With Baseline Onsets Detection - {sensor} - Duration - {start}mins to  - {end}mins")
    # plt.grid(True)
    # plt.show()

    y = flatten_list(yhat)
    # detrend_constant = 10

    inhalelist = list()
    exhalelist = list()
    for i in range(len(exhaleonsets)-1):
        t = list(range(exhaleonsets[i],exhaleonsets[i+1]))
        min = 0
        max = 0
        exid = 0
        inid = 0
        for i in t:
            if y[i]<min:
                min = y[i]
                exid = i
            if y[i]>max:
                max = y[i]
                inid = i
        exhalelist.append(exid)
        inhalelist.append(inid)

    # plt.clf()
    # inhalelist_min = [i / sample_rate for i in inhalelist]
    # exhalelist_min = [i / sample_rate for i in exhalelist]
    # plt.plot(xaxis, yhat*detrend_constant, 'g')
    # plt.plot(inhalelist_min, yhat[inhalelist]*detrend_constant, 'x:r')
    # plt.plot(exhalelist_min, yhat[exhalelist]*detrend_constant, 'x:b')
    # plt.xlabel('Time in sec')
    # plt.ylabel('Normalized Temperature')
    # plt.title(f"InhaleOnsets & ExhaleOnsets Detection - {sensor} - Duration - {start}mins to  - {end}mins")
    # plt.grid(True)
    # plt.show()

    return inhalelist, exhalelist