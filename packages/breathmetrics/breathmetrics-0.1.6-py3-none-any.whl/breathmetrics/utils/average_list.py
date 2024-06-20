"""
Module: average_list

This module provides a function for calculating the average of a list after removing outliers.

Dependencies:
- utils.delete_outliers.delete_outliers (custom utility function for removing outliers from a list)

"""

from .delete_outliers import delete_outliers


def average(lst):
    """
    Calculate the average of a list after removing outliers.

    Args:
        lst (List[float]): A list of numerical values.

    Returns:
        float: The calculated average.

    This function calculates the average of a list after removing outliers using the 'delete_outliers' function.

    Usage:
    1. Import this function from the module.
    2. Call the function with a list of numerical values as an argument.

    Example:
    ```python
    from utils.average_list import average

    values = [12.5, 13.2, 11.8, 100.0, 12.7, 12.9, 11.5]
    avg = average(values)
    ```
    """
    sumofall = 0
    lst = delete_outliers(lst)
    for i in range(len(lst)):
        sumofall += lst[i]
    nooflist = len(lst)
    average = round((sumofall / nooflist), 2)
    return average
