import pytest
from biomathhh.pH_scale import calculate_pH
    
def test_non_numeric_input_error():
    """
    Test whether non-numeric input raises an error
    """
    with pytest.raises(TypeError):
        calculate_pH('non-numeric input')
        
def test_non_positive_input_error():
    """
    Test whether non-positive input raises an error
    """
    with pytest.raises(ValueError):
        calculate_pH(-8)
        
def test_case1(): 
    assert calculate_pH(1e-7)==7.0
    
def test_case2(): 
    assert abs(calculate_pH(6.31e-8)-7.2)/7.2<0.01