import pytest
import numpy as np

from biomathhh.sw_diversity_index import sw_diversity_index


def test_sw_diversity_index_returns_float_for_valid_input():
    """Returns a float for a valid list/array of non-negative counts."""
    result = sw_diversity_index([10, 20, 30])
    assert isinstance(result, float)


def test_sw_diversity_index_empty_input_returns_zero():
    """Returns 0.0 for an empty input (no community -> no diversity)."""
    assert sw_diversity_index([]) == 0.0


def test_sw_diversity_index_single_species_returns_zero():
    """Returns 0.0 when only one species is present (no diversity)."""
    assert sw_diversity_index([7]) == 0.0


def test_sw_diversity_index_all_zeros_returns_zero():
    """Returns 0.0 when all counts are zero (no observed individuals)."""
    assert sw_diversity_index([0, 0, 0]) == 0.0


def test_sw_diversity_index_negative_values_raise_value_error():
    """Raises ValueError if any count is negative (invalid abundance)."""
    with pytest.raises(ValueError):
        sw_diversity_index([10, -5, 20])


def test_sw_diversity_index_non_numeric_input_raises_type_error():
    """Raises TypeError if counts include non-numeric values."""
    with pytest.raises(TypeError):
        sw_diversity_index([10, "a", 20])


def test_sw_diversity_index_known_value():
    """Matches a known Shannon-Wiener index value for a reference community."""
    result = sw_diversity_index([50, 30, 20])
    assert result == pytest.approx(1.0297, abs=1e-4)


def test_sw_diversity_index_invariant_to_scaling_of_counts():
    """
    Shannon index depends on proportions, not absolute totals.
    Scaling all counts by the same factor should not change the result.
    """
    h1 = sw_diversity_index([5, 3, 2])
    h2 = sw_diversity_index([50, 30, 20])  # scaled by 10
    assert h1 == pytest.approx(h2)


def test_sw_diversity_index_accepts_numpy_array_input():
    """Accepts numpy arrays as input (common in scientific workflows)."""
    arr = np.array([10, 20, 30])
    result = sw_diversity_index(arr)
    assert isinstance(result, float)
