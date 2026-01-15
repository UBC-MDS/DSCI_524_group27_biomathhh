import pytest
import numpy as np

from src.biomathhh.sw_diversity_index import sw_diversity_index


def test_returns_float():
    """
    Test that valid numeric arrays return a float
    """
    result = sw_diversity_index([10, 20, 30])
    assert isinstance(result, float)


def test_empty_array():
    """
    Test that an empty array returns 0.0
    """
    assert sw_diversity_index([]) == 0.0


def test_empty_array():
    """
    Test that a single-species array returns 0.0
    """
    assert sw_diversity_index([7]) == 0.0


def test_empty_array():
    """
    Test that arrays containing zeros are handled correctly
    """
    assert sw_diversity_index([0,0,0]) == 0.0


def test_negative_values_raise_error():
    """
    Test that negative values raise an error
    """
    with pytest.raises(ValueError):
        sw_diversity_index([10, -5, 20])


def test_non_numeric_input_raises_error():
    """
    Docstring for test_non_numeric_input_raises_error
    Test that non-numeric inputs raise an error
    """
    with pytest.raises(TypeError):
        sw_diversity_index([10, "a", 20])


def test_known_input():
    """
    Test that known inputs return expected Shannon index values
    """
    result = sw_diversity_index([50, 30, 20])
    assert abs(result - 1.0297) < 1e-4








