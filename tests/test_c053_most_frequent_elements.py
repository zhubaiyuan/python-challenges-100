import pytest


@pytest.mark.parametrize("values, expected",
                         [([1, 2, 3, 4, 4, 4, 3, 3, 2, 4], {1: 1, 2: 2, 3: 3, 4: 4}),
                          ([1, 1, 1, 2, 2, 2, 3, 3, 3], {1: 3, 2: 3, 3: 3})])
def test_value_count(values, expected):
    from challenges.c053_most_frequent_elements import value_count, value_count_v2
    result = value_count(values)
    assert expected == result
    result2 = value_count_v2(values)
    assert expected == result2


@pytest.mark.parametrize("dictonary, expected",
                         [({1: 1, 2: 2, 3: 3, 4: 4}, {4: 4, 3: 3, 2: 2, 1: 1})])
def test_sort_dict_by_value(dictonary, expected):
    from challenges.c053_most_frequent_elements import sort_dict_by_value
    result = sort_dict_by_value(dictonary)
    assert expected == result
