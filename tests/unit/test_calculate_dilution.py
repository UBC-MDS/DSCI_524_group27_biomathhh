import pytest

from biomathhh.dilution import calculate_dilution


def test_calculate_dilution_basic():
    """Computes final concentration using the dilution equation C2 = (C1 * V1) / V2."""
    # Arrange: choose simple numbers with an exact result
    c1 = 5.0
    stock_volume = 1.0
    final_volume = 5.0

    # Act
    result = calculate_dilution(c1, stock_volume, final_volume)

    # Assert: 5 * 1 / 5 = 1
    assert result == pytest.approx(1.0)


def test_calculate_dilution_stock_equals_final_volume():
    """Returns the original concentration when stock_volume == final_volume (no dilution)."""
    # Arrange
    c1 = 2.5
    stock_volume = 10.0
    final_volume = 10.0

    # Act
    result = calculate_dilution(c1, stock_volume, final_volume)

    # Assert: ratio is 1, so concentration stays the same
    assert result == pytest.approx(2.5)


def test_calculate_dilution_small_numbers():
    """Handles small floating-point volumes correctly (uses approx for float comparison)."""
    # Arrange / Act: 1.0 * 0.1 / 0.2 = 0.5
    result = calculate_dilution(1.0, 0.1, 0.2)

    # Assert
    assert result == pytest.approx(0.5)


def test_calculate_dilution_raises_when_non_positive():
    """Raises ValueError when any input is non-positive (must be strictly > 0)."""
    # C1 must be positive
    with pytest.raises(ValueError, match="positive"):
        calculate_dilution(0.0, 1.0, 5.0)

    # stock_volume must be positive
    with pytest.raises(ValueError, match="positive"):
        calculate_dilution(5.0, -1.0, 5.0)

    # final_volume must be positive
    with pytest.raises(ValueError, match="positive"):
        calculate_dilution(5.0, 1.0, 0.0)


def test_calculate_dilution_raises_when_stock_volume_gt_final_volume():
    """Raises ValueError if stock_volume exceeds final_volume (physically impossible setup)."""
    with pytest.raises(ValueError, match="stock_volume.*final_volume"):
        calculate_dilution(5.0, 6.0, 5.0)


def test_calculate_dilution_raises_when_not_numeric():
    """Raises TypeError when inputs are not numeric types (int/float)."""
    with pytest.raises(TypeError):
        calculate_dilution("5", 1.0, 5.0)

    with pytest.raises(TypeError):
        calculate_dilution(5.0, "1", 5.0)

    with pytest.raises(TypeError):
        calculate_dilution(5.0, 1.0, None)


def test_calculate_dilution_accepts_int_inputs():
    """Accepts integer inputs and returns the correct numeric result."""
    # Arrange / Act: 5 * 2 / 10 = 1
    result = calculate_dilution(5, 2, 10)

    # Assert
    assert result == pytest.approx(1.0)


def test_calculate_dilution_invariant_to_scaling_of_volumes():
    """Result is invariant if both volumes are scaled by the same factor (depends only on V1/V2)."""
    # Arrange: same ratio (V1/V2) in both calls
    c_small = calculate_dilution(8.0, 1.0, 4.0)      # 8*(1/4) = 2
    c_scaled = calculate_dilution(8.0, 10.0, 40.0)   # 8*(10/40) = 2

    # Assert: both results match each other and the expected value
    assert c_small == pytest.approx(c_scaled)
    assert c_small == pytest.approx(2.0)
