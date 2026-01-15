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
