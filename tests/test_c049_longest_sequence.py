import pytest


@pytest.mark.parametrize("values, expected",
                         [([7, 2, 7, 1, 2, 5, 7, 1], [1, 2, 5, 7]),
                          ([7, 2, 7, 1, 2, 3, 8, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
                          ([1, 1, 2, 2, 2, 3, 3, 3, 3],
                           [1, 1, 2, 2, 2, 3, 3, 3, 3]),
                          ([], [])])
def test_find_longest_growing_sequence(values, expected):
    from challenges.c049_longest_sequence import find_longest_growing_sequence, find_longest_growing_sequence_v2, find_longest_growing_sequence_v3
    result = find_longest_growing_sequence(values)
    assert expected == result
    result2 = find_longest_growing_sequence_v2(values)
    assert expected == result2
    # result3 = find_longest_growing_sequence_v3(values)
    # assert expected == result3
