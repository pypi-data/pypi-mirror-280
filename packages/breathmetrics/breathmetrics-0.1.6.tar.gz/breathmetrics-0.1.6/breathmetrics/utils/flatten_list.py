"""
Module: flatten_list

This module provides a function for flattening a nested list into a flat list.

"""

def flatten_list(_2d_list):
    """
    Flatten a nested list into a flat list.

    Args:
        _2d_list (list): A nested list containing elements.

    Returns:
        list: A flat list containing all the elements.

    This function takes a nested list and flattens it into a single flat list.

    Usage:
    1. Import this function from the module.
    2. Call the function with a nested list as an argument.

    Example:
    ```python
    from flatten_list import flatten_list

    nested_list = [[1, 2], [3, 4, 5], [6]]
    flat_list = flatten_list(nested_list)
    ```
    """
    flat_list = []
    for element in _2d_list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list