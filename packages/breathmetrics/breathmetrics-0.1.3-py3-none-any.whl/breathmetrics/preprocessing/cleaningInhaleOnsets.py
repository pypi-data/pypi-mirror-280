"""
Module: cleaningInhaleOnsets

This module provides a function for cleaning inhale onsets based on exhale onsets.

"""

def cleaningin(inhaleonsets: list, exhaleonsets: list):
    """
    Clean inhale onsets based on exhale onsets.

    Args:
        inhaleonsets (list): A list of inhale onset indices.
        exhaleonsets (list): A list of exhale onset indices.

    Returns:
        Tuple[list, list]: A tuple containing two lists:
        - Cleaned inhale onset indices.
        - Cleaned exhale onset indices.

    This function cleans inhale onsets based on the provided exhale onsets. It ensures that
    inhale and exhale onsets are aligned properly.

    Usage:
    1. Import this function from the module.
    2. Call the function with the appropriate arguments.

    Example:
    ```python
    from preprocessing.cleaningInhaleOnsets import cleaningin

    inhale_onsets = [1, 3, 5, 7, 9]
    exhale_onsets = [2, 4, 6, 8, 10]

    cleaned_inhale_onsets, cleaned_exhale_onsets = cleaningin(inhale_onsets, exhale_onsets)
    ```
    """
    i = 1
    j = 0
    inhale = list()
    inhale.append(inhaleonsets[0])
    while (i < len(inhaleonsets)) and (j < len(exhaleonsets)):
        if exhaleonsets[j] < inhaleonsets[i]:
            inhale.append(inhaleonsets[i])
            i += 1
            j += 1
        else:
            i += 1
    inhaleonsets.clear()
    inhaleonsets = inhale
    x = len(inhaleonsets) if len(inhaleonsets) >= len(exhaleonsets) else len(
        exhaleonsets)
    return inhaleonsets[:x], exhaleonsets[:x]