import pytest

from challenges.c017_list_sum import sum_lambda, sum_rec_v2


@pytest.mark.parametrize("values, expected",
                         [([1], 1),
                          ([1, 2, 3], 6),
                          ([1, 2, 3, -7], -1)])
def test_sum_rec(values, expected):
    from challenges.c017_list_sum import sum_rec, sum_rec_v2, sum_lambda
    assert sum_rec(values) == expected
    assert sum_rec_v2(values) == expected
    assert sum_lambda(values) == expected
