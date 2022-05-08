import pytest


@pytest.mark.parametrize("value, expected",
                         [(2, True),
                          (3, False),
                          (4, True),
                          (10, False),
                          (16, True)])
def test_is_power_of2(value, expected):
    from challenges.c020_exponential_function import is_power_of_2, is_power_of_2_v2
    assert is_power_of_2(value) == expected
    assert is_power_of_2_v2(value) == expected


@pytest.mark.parametrize("number, exponent, expected",
                         [(2, 2, 4),
                          (4, 2, 16),
                          (16, 2, 256),
                          (4, 4, 256),
                          (2, 8, 256),
                          (3, 3, 27)])
def test_power_of(number, exponent, expected):
    from challenges.c020_exponential_function import power_of, power_of_v2, power_of_v3
    assert power_of(number, exponent) == expected
    assert power_of_v2(number, exponent) == expected
    assert power_of_v3(number, exponent) == expected
