from exponential_growth import exponential_growth as exp
import math
""" All tests for the exponential growth function will go here."""


def test_time_zero():
    """ Tests that function returns original value given time zero"""
    assert exp.exponential_growth(1000, 0.5, 0) == 1000.0

def test_growth_zero():
    """ Tests that function returns original value given zero growth rate"""
    assert exp.exponential_growth(500, 0, 100) == 500.0

def test_large_value():
    """ Tests that function handles large values without overflow"""
    assert exp.exponential_growth(10, 0.01, 1000) == 10 * math.exp(0.01 * 1000) 

def test_precision():
    """ Tests that function can handle small values with precision"""
    assert exp.exponential_growth(0.0001, 0.05, 10) == 0.0001 * math.exp(0.5)

def test_strong_decay():
    """ Tests that function can calculate values approaching zero"""
    assert exp.exponential_growth(1000, -0.5, 20) == 1000 * math.exp(-10)