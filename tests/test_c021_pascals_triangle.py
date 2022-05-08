import pytest


@pytest.mark.parametrize("n, expected",
                         [(1, [1]),
                          (2, [1, 1]),
                          (3, [1, 2, 1]),
                          (4, [1, 3, 3, 1]),
                          (5, [1, 4, 6, 4, 1]),
                          (6, [1, 5, 10, 10, 5, 1]),
                          (7, [1, 6, 15, 20, 15, 6, 1])])
def test_calc_pascal_with_action(n, expected):
    from challenges.c021_pascals_triangle import print_pascal_v2
    assert print_pascal_v2(n, None) == expected
