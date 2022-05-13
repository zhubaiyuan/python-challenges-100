import pytest

from challenges.c095_binary_search import binary_search, binary_search_v2, binary_search_v3


@pytest.mark.parametrize("sorted_values, search_for, expected",
                         [([1, 2, 3, 4, 5, 7, 8, 9], 5, True),
                          ([1, 2, 3, 4, 5, 7, 8, 9], 6, False)])
def test_binary_search(sorted_values, search_for, expected):
    assert binary_search(sorted_values, search_for) == expected
    assert binary_search_v2(sorted_values, search_for) == expected


@pytest.mark.parametrize("sorted_values, search_for, expected",
                         [([1, 2, 3, 4, 5, 7, 8, 9], 5, 4),
                          ([1, 2, 3, 4, 5, 7, 8, 9], 6, -1)])
def test_binary_search_iterative(sorted_values, search_for, expected):
    assert binary_search_v3(sorted_values, search_for) == expected
