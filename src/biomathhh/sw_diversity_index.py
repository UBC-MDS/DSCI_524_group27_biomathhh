import numpy as np 

def sw_diversity_index(arr):
    """
    Calculate the Shannon Wiener diversity index (H') for a community.

    The Shannon Wiener index quantifies species diversity by accounting
    for both species richness and evenness. It is defined as:

        H' = -SUM(p_i * ln(p_i))

    where p_i is the proportion of individuals belonging to species i.

    Parameters
    ----------
    arr : array-like
        A one-dimensional array of non-negative values representing
        species counts.

    Returns
    -------
    float
        The Shannon Wiener diversity index. Returns 0.0 if only one
        species is present or if the input is empty.

    Notes
    -----
    - Zero counts are ignored in the calculation.
    - The natural log (ln) is used.
    - Higher values indicate greater diversity.

    Examples
    --------
    >>> sw_diversity_index([50, 30, 20])
    1.0297

    >>> sw_diversity_index([1])
    0.0
    """

    arr = np.array(arr)

    # Check for non-numeric types
    if not np.issubdtype(arr.dtype, np.number):
        raise TypeError("All elements must be numeric")

    # Check for negative values
    if np.any(arr < 0):
        raise ValueError("All counts must be non-negative")

    # Remove zeros
    arr = arr[arr > 0]

    # If array is empty or has only one species return 0.0
    if len(arr) <= 1:
        return 0.0

    # Calculate proportions (p_i in docstring)
    proportions = arr / arr.sum()

    # Calculate Shannon-Wiener index
    H = -np.sum(proportions * np.log(proportions))

    return float(H)
