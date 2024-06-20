"""
Module: cleaningExhaleOnsets

This module provides a function for cleaning exhale onsets based on inhale onsets.

"""

def cleaningex(inhaleonsets: list, exhaleonsets: list):
    """
    Clean exhale onsets based on inhale onsets.

    Args:
        inhaleonsets (list): A list of inhale onset indices.
        exhaleonsets (list): A list of exhale onset indices.

    Returns:
        Tuple[list, list]: A tuple containing two lists:
        - Cleaned inhale onset indices.
        - Cleaned exhale onset indices.

    This function cleans exhale onsets based on the provided inhale onsets. It ensures that
    inhale and exhale onsets are aligned properly.

    Usage:
    1. Import this function from the module.
    2. Call the function with the appropriate arguments.

    Example:
    ```python
    from preprocessing.cleaningExhaleOnsets import cleaningex

    inhale_onsets = [1, 3, 5, 7, 9]
    exhale_onsets = [2, 4, 6, 8, 10]

    cleaned_inhale_onsets, cleaned_exhale_onsets = cleaningex(inhale_onsets, exhale_onsets)
    ```
    """
    i = 0
    j = 0
    exhale = list()
    while (i < len(inhaleonsets) - 1) and (j < len(exhaleonsets)):
        if inhaleonsets[i] > exhaleonsets[j]:
            #print(exhaleonsets[j])
            j += 1
        else:
            exhale.append(exhaleonsets[j])
            j += 1
            i += 1
    exhaleonsets.clear()
    exhaleonsets = exhale
    x = len(inhaleonsets) if len(inhaleonsets) >= len(exhaleonsets) else len(
        exhaleonsets)
    return inhaleonsets[:x], exhaleonsets[:x]