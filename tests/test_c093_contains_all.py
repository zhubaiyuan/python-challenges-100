import pytest

from challenges.c093_contains_all import contains_all, contains_all_v2


@pytest.mark.parametrize("values, search_values, expected",
                         [([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [7, 2], True),
                          ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 11], False)])
def test_contains_all(values, search_values, expected):
    assert contains_all(values, search_values) == expected
    assert contains_all_v2(values, search_values) == expected
