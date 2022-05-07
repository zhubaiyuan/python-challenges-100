import pytest


@pytest.mark.parametrize("n, expected",
                         [(6, True), (28, True),
                          (496, True), (8128, True)])
def test_is_perfect_number(n, expected):
    from challenges.c003_perfect_numbers import is_perfect_number, is_perfect_number_v2
    assert is_perfect_number(n) == expected
    assert is_perfect_number_v2(n) == expected


@pytest.mark.parametrize("n, expected", [(50, [6, 28]),
                                         (1000, [6, 28, 496]),
                                         (10000, [6, 28, 496, 8128])])
def test_calc_perfect_numbers(n, expected):
    from challenges.c003_perfect_numbers import calc_perfect_numbers, calc_perfect_numbers_v2
    assert calc_perfect_numbers(n) == expected
    assert calc_perfect_numbers_v2(n) == expected
