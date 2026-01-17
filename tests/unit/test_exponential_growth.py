import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from biomathhh.exponential_growth import exponential_growth 

import math
""" All tests for the exponential growth function will go here."""


def test_time_zero():
    """ Tests that function returns original value given time zero"""
    assert exponential_growth(1000, 0.5, 0) == 1000.0
    print("test_time_zero passed")

def test_growth_zero():
    """ Tests that function returns original value given zero growth rate"""
    assert exponential_growth(500, 0, 100) == 500.0
    print("test_growth_zero passed")

def test_large_value():
    """ Tests that function handles large values without overflow"""
    assert exponential_growth(10, 0.01, 1000) == 10 * math.exp(0.01 * 1000)
    print("test_large_value passed")

def test_precision():
    """ Tests that function can handle small values with precision"""
    assert exponential_growth(0.0001, 0.05, 10) == 0.0001 * math.exp(0.5)
    print("test_precision passed")

def test_strong_decay():
    """ Tests that function can calculate values approaching zero"""
    assert exponential_growth(1000, -0.5, 20) == 1000 * math.exp(-10)
    print("test_strong_decay passed")



if __name__ == "__main__":
    print("Running exponential growth tests...\n")
    
    try:
        test_time_zero()
        test_growth_zero()
        test_large_value()
        test_precision()
        test_strong_decay()
        print("\n All tests passed!")

    except AssertionError as error:
        print(f"\n Test failed: {error}")