import pytest


@pytest.mark.parametrize("n, expected",
                         [(1, [[1]]),
                          (2, [[1], [1, 1]]),
                          (3, [[1], [1, 1], [1, 2, 1]]),
                          (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])])
def test_pascal(n, expected):
    from challenges.c051_pascals_triangle import pascal
    result = pascal(n)
    assert expected == result
