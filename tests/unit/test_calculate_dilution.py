import pytest

from biomathhh.dilution import calculate_dilution


def test_calculate_dilution_basic():
    # C1*V1 = C2*V2 -> 5*1 = C2*5 -> C2=1
    assert calculate_dilution(5.0, 1.0, 5.0) == 1.0


def test_calculate_dilution_stock_equals_final_volume():
    # no dilution when V1 == V2
    assert calculate_dilution(2.5, 10.0, 10.0) == 2.5


def test_calculate_dilution_small_numbers():
    result = calculate_dilution(1.0, 0.1, 0.2)  # 1*0.1/0.2 = 0.5
    assert result == pytest.approx(0.5)


def test_calculate_dilution_raises_when_non_positive():
    with pytest.raises(ValueError, match="positive"):
        calculate_dilution(0.0, 1.0, 5.0)

    with pytest.raises(ValueError, match="positive"):
        calculate_dilution(5.0, -1.0, 5.0)

    with pytest.raises(ValueError, match="positive"):
        calculate_dilution(5.0, 1.0, 0.0)


def test_calculate_dilution_raises_when_stock_volume_gt_final_volume():
    with pytest.raises(ValueError, match="stock_volume.*final_volume"):
        calculate_dilution(5.0, 6.0, 5.0)


def test_calculate_dilution_raises_when_not_numeric():
    with pytest.raises(TypeError):
        calculate_dilution("5", 1.0, 5.0)

    with pytest.raises(TypeError):
        calculate_dilution(5.0, "1", 5.0)

    with pytest.raises(TypeError):
        calculate_dilution(5.0, 1.0, None)
        
        
def test_calculate_dilution_accepts_int_inputs():
    # inteegers should be accepted and still compute correctly
    assert calculate_dilution(5, 2, 10) == 1.0


def test_calculate_dilution_invariant_to_scaling_of_volumes():
    # Ifyou scale both volumes by the same factor, concentration should not change at all
    c_small = calculate_dilution(8.0, 1.0, 4.0)   # 8*(1/4)=2
    c_scaled = calculate_dilution(8.0, 10.0, 40.0)  # same ratio (10/40)=1/4  ##also 2
    assert c_small == pytest.approx(c_scaled)
    assert c_small == pytest.approx(2.0)

