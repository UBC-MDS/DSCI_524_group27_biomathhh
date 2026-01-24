import math

def exponential_growth(initial_value, growth_rate, time):
    """
    Calculate exponential growth over a specified time period.

    This function computes the value after exponential growth using the formula:

        N(t) = N0 * exp(r * t)

    Parameters
    ----------
    initial_value : float
        The starting value at time t = 0. Must be positive.
    growth_rate : float
        The continuous growth rate (decimal, not percentage).
        Positive values indicate growth; negative values indicate decay.
    time : float
        The time period over which growth occurs. Must be non-negative.

    Returns
    -------
    float
        The calculated value after exponential growth.

    Raises
    ------
    TypeError
        If any input is not numeric.
    ValueError
        If any input is NaN, infinite, or violates constraints.
    OverflowError
        If the calculation results in overflow.

    Examples
    --------
    >>> from biomathhh.exponential_growth import exponential_growth
    >>> exponential_growth(50, 0.1, 0)
    50.0
    >>> round(exponential_growth(100, 0.05, 10), 6)
    164.872127
    >>> round(exponential_growth(1000, -0.03, 5), 6)
    860.707976
    """

    # checking for data types
    if not isinstance(initial_value, (int, float)):
        raise TypeError(f"initial_value must be a number, got {type(initial_value).__name__}")
    
    if not isinstance(growth_rate, (int, float)):
        raise TypeError(f"growth_rate must be a number, got {type(growth_rate).__name__}")
    
    if not isinstance(time, (int, float)):
        raise TypeError(f"time must be a number, got {type(time).__name__}")
    
    # checking for non NAN and finite values
    if math.isnan(initial_value) or math.isinf(initial_value):
        raise ValueError("initial_value must be a finite number")
    
    if math.isnan(growth_rate) or math.isinf(growth_rate):
        raise ValueError("growth_rate must be a finite number")
    
    if math.isnan(time) or math.isinf(time):
        raise ValueError("time must be a finite number")
    
    #check constraints
    if initial_value <= 0:
        raise ValueError(f"initial_value must be positive")
    
    if time < 0:
        raise ValueError(f"time must be non-negative")
    
    try:
        final_value = initial_value * math.exp(growth_rate * time)
        
        if math.isinf(final_value):
                raise OverflowError("Result is infinite, calculation overflow occurred")
        
    except OverflowError:
        raise OverflowError(f"Exponential calculation resulted in overflow")

    return final_value