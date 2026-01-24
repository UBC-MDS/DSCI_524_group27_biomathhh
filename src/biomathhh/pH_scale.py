import numpy as np
import numbers

def calculate_pH(hydronium_concentration): 
    """
    Calculate pH scale for a given hydronium concentration.
    
    This function computes pH value using the formula:
    pH = -log(hydronium concentration)
    
    Parameters:
    -----------
	hydronium_concentration: float
		The concentration of hydronium. Must be a positive number.
    
    Returns:
    --------
	float
		The calculated pH value.

	Raises
    ------
    TypeError
        If any input is not numeric.
    ValueError
        If any input is not positive.
    
    Examples:
	--------
    >>> from biomathhh.pH_scale import calculate_pH
	>>> calculate_pH(1e-7)
	7.0
	>>> calculate_pH(6.31e-8)
	7.2

    """
    if not isinstance(hydronium_concentration, numbers.Number): 
        raise TypeError(f"hydronium_concentration must be a number, got {type(hydronium_concentration).__name__}. ")
        
    if(hydronium_concentration<=0): 
        raise ValueError('hydronium_concentration has to be positive. ')
    
    return -np.log10(hydronium_concentration)