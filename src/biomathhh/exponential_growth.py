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
    final_value = initial_value * math.exp(growth_rate * time)

    return final_value