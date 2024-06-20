"""
Module: getBreathingRate

This module provides a function for calculating the breathing rate and interbreath interval
based on input lists of inhale and exhale onsets, along with the sample rate.

Functions:
- breathing_rate(inhaleonsets: List[float], exhaleonsets: List[float], sample_rate: float) -> Tuple[float, float]:
    Calculates the breathing rate and interbreath interval based on the provided inhale and exhale onsets and the sample rate.
"""

def breathing_rate(inhaleonsets, exhaleonsets, sample_rate):
    """
    Calculate breathing rate and interbreath interval.

    Args:
        inhaleonsets (List[float]): A list of inhale onset times (in seconds).
        exhaleonsets (List[float]): A list of exhale onset times (in seconds).
        sample_rate (float): The sample rate (in Hz) of the data.

    Returns:
        Tuple[float, float]: A tuple containing two values:
        - The calculated breathing rate (in breaths per minute).
        - The calculated interbreath interval (in seconds per breath).

    This function calculates the breathing rate and interbreath interval based on the provided lists
    of inhale and exhale onset times and the sample rate.

    Usage:
    1. Import this function from the module.
    2. Call the function with the appropriate arguments.

    Example:
    ```python
    from breathmetrics_function.getBreathingRate import breathing_rate

    inhale_onsets = [1.0, 3.5, 6.0, 8.5]
    exhale_onsets = [2.5, 5.0, 7.5, 10.0]
    sample_rate = 100.0  # Sample rate in Hz

    breathing_rate, interbreath_interval = breathing_rate(inhale_onsets, exhale_onsets, sample_rate)
    print(f"Breathing Rate: {breathing_rate} breaths per minute")
    print(f"Interbreath Interval: {interbreath_interval} seconds per breath")
    ```
    """
    temp =0
    length = 0
    inhale_interval=0
    exhale_interval=0
    for i in range(1,len(inhaleonsets)):
        between = (inhaleonsets[i] - inhaleonsets[i-1])/sample_rate
        inhale_interval += (inhaleonsets[i] - exhaleonsets[i])/sample_rate
        exhale_interval += (exhaleonsets[i] - inhaleonsets[i-1])/sample_rate
        temp += between
        length += 1
    interbreath_interval = round(temp/length,3)
    inhale_interbreath_interval = round(inhale_interval/length,3)
    exhale_interbreath_interval = round(exhale_interval/length,3)
    breath_rate = round(60/interbreath_interval,3)
    return breath_rate, inhale_interbreath_interval,  exhale_interbreath_interval, interbreath_interval


