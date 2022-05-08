import pytest


def inputs_and_expected():
    return [([1, 4, 7, 12, 20], [10, 15, 17, 33], [1, 4, 7, 10, 12, 15, 17, 20, 33]),
            ([2, 3, 5, 7], [11, 13, 17], [2, 3, 5, 7, 11, 13, 17]),
            ([2, 3, 5, 7, 11], [7, 11, 13, 17], [2, 3, 5, 7, 7, 11, 11, 13, 17]),
            ([1, 2, 3], [], [1, 2, 3])]


@pytest.mark.parametrize("values1, values2, expected",
                         inputs_and_expected())
def test_merge(values1, values2, expected):
    from challenges.c055_list_merge import list_merge, list_merge_v2, list_merge_v3, list_merge_v4
    result = list_merge(values1, values2)
    assert expected == result
    result2 = list_merge_v2(values1, values2)
    assert expected == result2
    result3 = list_merge_v3(values1, values2)
    assert expected == result3
    result4 = list_merge_v4(values1, values2)
    assert expected == result4
