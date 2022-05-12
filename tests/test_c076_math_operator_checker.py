import pytest

from challenges.c076_math_operator_checker import all_combinations_with_value, find_all_combinations
from challenges.c076_math_operator_checker_v2 import all_combinations_with_value_v2, find_all_combinations_v2


@pytest.mark.parametrize("digits,  expected",
                         [([1, 2, 3],
                           {"12-3": 9,
                            "123": 123,
                            "1+2+3": 6,
                            "1+2-3": 0,
                            "1-2+3": 2,
                            "1-23": -22,
                            "1-2-3": -4,
                            "1+23": 24,
                            "12+3": 15})])
def test_all_combinations(digits, expected):
    result = find_all_combinations(digits)
    assert result == expected
    result2 = find_all_combinations_v2(digits)
    assert result2 == expected


@pytest.mark.parametrize("digits, value, expected",
                         [([1, 2, 3, 4, 5, 6, 7, 8, 9], 100,
                           {"1+23-4+5+6+78-9",
                            "12+3+4+5-6-7+89",
                            "123-45-67+89",
                            "123+4-5+67-89",
                            "123-4-5-6-7+8-9",
                            "123+45-67+8-9",
                            "1+2+3-4+5+6+78+9",
                            "12+3-4+5+67+8+9",
                            "1+23-4+56+7+8+9",
                            "1+2+34-5+67-8+9",
                            "12-3-4+5-6+7+89"})])
def test_all_combinations_with_value(digits, value, expected):
    result = all_combinations_with_value(digits, value)
    assert result == expected
    result2 = all_combinations_with_value_v2(digits, value)
    assert result2 == expected
