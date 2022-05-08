import sys

import pytest


@pytest.mark.parametrize("values, expected",
                         [([7, 2, 1, 9, 7, 1], 1),
                          ([1, 2, 3, -7], -7),
                          ([11, 2, 33, 44, 55, 6, 7], 2),
                          ([], sys.maxsize)])
def test_min_rec(values, expected):
    from challenges.c018_list_min import min_rec
    assert min_rec(values) == expected
