import math

def exponential_growth(initial_value, growth_rate, time):
    """
    Calculate exponential growth over a specified time period.
    
    This function computes the value after exponential growth using the formula:
    final_value = initial_value * e^(growth_rate * time)
    
    Parameters:
    -----------
        initial_value (float): The starting value at time t=0.
            Must be a positive number.

        growth_rate (float): The continuous growth rate (as a decimal, not percentage).
            Positive values indicate growth, negative values indicate decay.

        time (float): The time period over which growth occurs. Must be non-negative.
            The units should match the units of the growth_rate.
    
    Returns:
    --------
        float: The calculated value after exponential growth over the specified time period.
    
    
    Examples:
        >>> exponential_growth(100, 0.05, 10)
        164.87212707001282
        
        >>> exponential_growth(1000, -0.03, 5)
        860.7079764250578
        
        >>> exponential_growth(50, 0.1, 0)
        50.0
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
    
    # check for overflow
    if math.isinf(final_value):
        raise OverflowError("Result is infinite, overflow error")

    final_value = initial_value * math.exp(growth_rate * time)

    return final_value