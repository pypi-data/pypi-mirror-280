"""
Module: delete_outliers

This module provides a function for removing outliers from a list of numerical values.

Dependencies:
- numpy as np

"""

import numpy as np

def delete_outliers(lst: list):
    """
    Remove outliers from a list of numerical values.

    Args:
        lst (List[float]): A list of numerical values.

    Returns:
        List[float]: A list with outliers removed.

    This function removes outliers from the provided list using the IQR (Interquartile Range) method.

    Usage:
    1. Import this function from the module.
    2. Call the function with a list of numerical values as an argument.

    Example:
    ```python
    from delete_outliers import delete_outliers

    values = [12.5, 13.2, 11.8, 100.0, 12.7, 12.9, 11.5]
    cleaned_values = delete_outliers(values)
    ```
    """
    lst.sort()
    Q1 = np.percentile(lst, 25, interpolation='midpoint')
    Q3 = np.percentile(lst, 75, interpolation='midpoint')

    IQR = Q3 - Q1

    upper = (lst >= (Q3 + 1.5 * IQR))
    upper = list(upper)

    lower = lst <= (Q1 - 1.5 * IQR)
    lower = list(lower)

    temp = []
    clean = []
    for i in range(len(lst)):
        if upper[i] is True:
            temp.append(i)
        if lower[i] is True:
            temp.append(i)
    for i in range(len(lst)):
        if i not in temp:
            clean.append(lst[i])
    # print(clean)
    return clean