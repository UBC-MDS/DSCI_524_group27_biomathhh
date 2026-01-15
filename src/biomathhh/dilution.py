def calculate_dilution(
    stock_concentration,
    stock_volume,
    final_volume
):
    """
    Calculate the final concentration of a solution after dilution.

    This function applies the standard dilution equation used in
    biological laboratory settings to calculate the
    resulting concentration after a stock solution is diluted.

    The calculation is based on the formula:
        C1 * V1 = C2 * V2

    where:
    - C1 is the stock/Initial  concentration
    - V1 is the volume of stock solution used
    - V2 is the final total volume after dilution
    - C2 is the final concentration (returned by this function)

    Parameters
    ----------
    stock_concentration : float
        the concentration of the original stock solution.
        Must be a positive number.

    stock_volume : float
       the volume of the stock solution used for dilution.
        Must be a positive number and less than or equal to final_volume.

    final_volume : float
        the total volume of the solution after dilution.
        Must be a positive number greater than or equal to stock_volume.

    Returns
    -------
    float
        The final concentration of the diluted solution.

    Raises
    ------
    ValueError
        If any input is not positive, or if stock_volume is greater
        than final_volume.

    Examples
    --------
    >>> calculate_dilution(stock_concentration=5.0, stock_volume=1.0, final_volume=5.0)
    1.0
    """
def calculate_dilution(stock_concentration, stock_volume, final_volume):
    """
    calculate the final concentration of a solution after dilution.
    ...
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

