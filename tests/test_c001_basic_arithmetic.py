import pytest


@pytest.mark.parametrize("m, n, expected",
                         [(6, 7, 0),
                          (3, 4, 6),
                          (5, 5, 5)])
def test_calc(m, n, expected):
    from challenges.c001_basic_arithmetic import calc, calc_v2
    assert calc(m, n) == expected
    assert calc_v2(m, n) == expected


@pytest.mark.parametrize("n, expected",
                         [(3, {"sum": 2, "count": 1}),
                          (8, {"sum": 19, "count": 4}),
                          (15, {"sum": 63, "count": 8})])
def test_calc_sum_and_count_all_numbers_div_by_2_or_7(n, expected):
    from challenges.c001_basic_arithmetic import calc_sum_and_count_all_numbers_div_by_2_or_7_v2
    assert calc_sum_and_count_all_numbers_div_by_2_or_7_v2(n) == expected


@pytest.mark.parametrize("n, expected",
                         [(1, False),
                          (2, True),
                          (3, False),
                          (4, True)])
def test_is_even(n, expected):
    from challenges.c001_basic_arithmetic import is_even
    assert is_even(n) == expected


@pytest.mark.parametrize("n, expected",
                         [(1, True),
                          (2, False),
                          (3, True),
                          (4, False)])
def test_is_odd(n, expected):
    from challenges.c001_basic_arithmetic import is_odd
    assert is_odd(n) == expected
