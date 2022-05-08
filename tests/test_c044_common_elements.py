import pytest


def inputs_and_expected():
    return [([1, 2, 4, 7, 8], [2, 3, 7, 9], {2, 7}),
            ([1, 2, 7, 4, 7, 8], [7, 7, 3, 2, 9], {2, 7}),
            ([2, 4, 6, 8], [1, 3, 5, 7, 9], set())]


@pytest.mark.parametrize("values1, values2, expected",
                         inputs_and_expected())
def test_find_common(values1, values2, expected):
    from challenges.c044_common_elements import find_common, find_common_v2, find_common_v3, find_common_v4
    assert expected == find_common(values1, values2)
    assert expected == find_common_v2(values1, values2)
    assert expected == find_common_v3(values1, values2)
    assert expected == find_common_v4(values1, values2)
