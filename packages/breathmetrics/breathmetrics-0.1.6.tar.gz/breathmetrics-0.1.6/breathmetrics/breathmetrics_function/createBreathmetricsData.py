"""
Module: createBreathmetricsData

This module contains functions for processing and visualizing capnostream data from a CSV file.
It performs data preprocessing steps such as flattening, smoothing and detrending the data to generate breathmetrics.

Dependencies:
- pandas (imported as pd)
- numpy (imported as np)
- matplotlib.pyplot (imported as plt)
- scipy.signal (imported as signal)
- scipy.signal.savgol_filter (imported as savgol_filter)
- utils.flatten_list.flatten_list (custom utility function for flattening lists)

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import savgol_filter

from ..utils.flatten_list import flatten_list


def create_breathmterics_data(raw_y: str, minutes: int):
    """
    Create breathmetrics data from capnostream data by removing junk values.

    Args:
        dir (str): The path to the CSV file containing capnostream data.
        minutes (int): The number of minutes recorded by the data.

    Returns:
        Tuple[List[float], List[float]]: A tuple containing two lists:
        - The processed breathmetrics data.
        - The corresponding time axis.

    This function reads capnostream data from a CSV file, processes it to calculate
    breathmetrics parameters, and returns the processed data and corresponding time axis.

    Usage:
    1. Import this function from the module.
    2. Call the function with the file directory ('dir') and the number of minutes of data as arguments.

    Example:
    ```python
    from breathmetrics_function.createBreathmetricsData import create_breathmterics_data

    data, time_axis = create_breathmetrics_data("data.csv", minutes=10)
    ```
    """
    y = flatten_list(raw_y)
    x = []
    xaxis = []
    for i in range(len(y) - 1):
        x.append(list(np.linspace(y[i], y[i + 1], 20)))
    y = flatten_list(x)
    sample_rate = len(y) / (minutes * 60)
    for i in range(len(y)):
        xaxis.append(i / sample_rate)
    recorded_y = y
    yhat = signal.detrend(savgol_filter(y, 45, 3)) * 100
    x = []
    detrend_constant = 10
    for i in range(0, len(yhat), 5000):
        x.append(flatten_list(signal.detrend(yhat[i : i + 5000] / detrend_constant)))
    yhat = signal.detrend(flatten_list(x))

    return recorded_y, yhat, xaxis, sample_rate
