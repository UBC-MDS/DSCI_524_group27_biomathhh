import pytest

from biomathhh.pH_scale import calculate_pH


def test_calculate_pH_raises_type_error_for_non_numeric_input():
    """Raises TypeError when input is not a numeric hydrogen ion concentration."""
    with pytest.raises(TypeError):
        calculate_pH("non-numeric input")


def test_calculate_pH_raises_value_error_for_non_positive_input():
    """Raises ValueError when input concentration is zero or negative."""
    with pytest.raises(ValueError):
        calculate_pH(-8)


def test_calculate_pH_neutral_solution():
    """Correctly computes pH for a neutral solution ([H+] = 1e-7)."""
    # Arrange / Act
    result = calculate_pH(1e-7)

    # Assert
    assert result == pytest.approx(7.0)


def test_calculate_pH_weakly_basic_solution():
    """Correctly computes pH for a weakly basic solution within tolerance."""
    # Arrange: expected pH ≈ 7.2
    result = calculate_pH(6.31e-8)

    # Assert
    assert result == pytest.approx(7.2, rel=0.01)


def test_calculate_pH_high_hydrogen_concentration():
    """Computes pH for a relatively high hydrogen ion concentration."""
    # Arrange / Act: expected pH ≈ 0.301
    result = calculate_pH(0.5)

    # Assert
    assert result == pytest.approx(0.301, rel=0.01)


def test_calculate_pH_acidic_solution():
    """Correctly computes pH for an acidic solution."""
    # Arrange / Act: expected pH ≈ 3.1
    result = calculate_pH(0.0008)

    # Assert
    assert result == pytest.approx(3.1, rel=0.01)
