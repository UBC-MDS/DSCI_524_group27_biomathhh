"""
Unit tests for biomathhh.exponential_growth.exponential_growth.

Model:
    N(t) = N0 * exp(r * t)

Where:
- N0 is the initial value
- r is the growth rate (can be negative for decay)
- t is time

These tests verify:
- identity behavior at t = 0
- identity behavior at r = 0
- correct computation for large t (no overflow in typical ranges)
- precision for small initial values
- strong decay case (r < 0)
"""

import math
import pytest

from biomathhh.exponential_growth import exponential_growth


def test_exponential_growth_time_zero_returns_initial_value():
    """If time is zero, the result should equal the initial value (exp(0)=1)."""
    # Arrange
    n0, r, t = 1000.0, 0.5, 0.0

    # Act
    result = exponential_growth(n0, r, t)

    # Assert
    assert result == pytest.approx(1000.0)


def test_exponential_growth_zero_rate_returns_initial_value():
    """If growth rate is zero, the result should equal the initial value for any time."""
    n0, r, t = 500.0, 0.0, 100.0
    result = exponential_growth(n0, r, t)
    assert result == pytest.approx(500.0)


def test_exponential_growth_matches_math_exp_for_large_time():
    """Matches the analytical formula for a large (but reasonable) time value."""
    n0, r, t = 10.0, 0.01, 1000.0
    expected = n0 * math.exp(r * t)
    result = exponential_growth(n0, r, t)
    assert result == pytest.approx(expected)


def test_exponential_growth_small_initial_value_precision():
    """Handles small starting values without losing correctness."""
    n0, r, t = 1e-4, 0.05, 10.0
    expected = n0 * math.exp(r * t)  # exp(0.5)
    result = exponential_growth(n0, r, t)
    assert result == pytest.approx(expected)


def test_exponential_growth_strong_decay():
    """Negative growth rate should produce decay toward zero."""
    n0, r, t = 1000.0, -0.5, 20.0
    expected = n0 * math.exp(r * t)  # exp(-10)
    result = exponential_growth(n0, r, t)
    assert result == pytest.approx(expected)
