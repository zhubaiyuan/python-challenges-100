import pytest


@pytest.mark.parametrize("values1, values2, expected",
                         [([1, 2, 3], [4, 5, 6], [5, 7, 9]),
                          ([9, 2, 7], [1, 3, 5], [1, 0, 6, 2])])
def test_list_add(values1, values2, expected):
    from challenges.c054_addition_of_digits import list_add, list_add_v2, list_add_v3, list_add_v4
    result = list_add(values1, values2)
    assert expected == result
    result2 = list_add_v2(values1, values2)
    assert expected == result2
    result3 = list_add_v3(values1, values2)
    assert expected == result3
    result4 = list_add_v4(values1, values2)
    assert expected == result4


@pytest.mark.parametrize("values1, values2, expected",
                         [([3, 2, 1], [6, 5, 4], [9, 7, 5]),
                          ([7, 2, 9], [5, 3, 1], [2, 6, 0, 1])])
def test_list_add_inverse(values1, values2, expected):
    from challenges.c054_addition_of_digits import list_add_inverse
    result = list_add_inverse(values1, values2)
    assert expected == result
