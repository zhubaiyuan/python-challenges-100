import pytest


def inputs_and_expected():
    return [([1, 1, 2, 3, 4, 1, 2, 3], [1, 2, 3, 4]),
            ([7, 5, 3, 5, 1], [7, 5, 3, 1]),
            ([1, 1, 1, 1], [1])]


@pytest.mark.parametrize("inputs, expected",
                         inputs_and_expected())
def test_remove_duplicates(inputs, expected):
    from challenges.c047_remove_duplicates import remove_list_duplicates, remove_list_duplicates_v2
    assert expected == remove_list_duplicates(inputs)
    assert expected == remove_list_duplicates_v2(inputs)
