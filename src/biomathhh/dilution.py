def calculate_dilution(stock_concentration, stock_volume, final_volume):
    """
    Calculate the final concentration of a solution after dilution.

    This function applies the standard laboratory dilution equation:

        C1 * V1 = C2 * V2

    Parameters
    ----------
    stock_concentration : float
        Concentration of the original stock solution. Must be positive.
    stock_volume : float
        Volume of stock solution used. Must be positive and less than or equal to final_volume.
    final_volume : float
        Final total volume after dilution. Must be positive.

    Returns
    -------
    float
        Final concentration of the diluted solution.

    Raises
    ------
    TypeError
        If any input is not numeric.
    ValueError
        If any input is non-positive or stock_volume > final_volume.

    Examples
    --------
    >>> from biomathhh.dilution import calculate_dilution
    >>> calculate_dilution(5.0, 1.0, 5.0)
    1.0
    >>> calculate_dilution(8.0, 10.0, 40.0)
    2.0
    """
    for name, value in {
        "stock_concentration": stock_concentration,
        "stock_volume": stock_volume,
        "final_volume": final_volume,
    }.items():
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number (int or float).")

    if stock_concentration <= 0 or stock_volume <= 0 or final_volume <= 0:
        raise ValueError("All inputs must be positive numbers.")

    if stock_volume > final_volume:
        raise ValueError("stock_volume must be less than or equal to final_volume.")

    return (stock_concentration * stock_volume) / final_volume
