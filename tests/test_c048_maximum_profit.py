import pytest


def prices_and_expected():
    return [([0, 10, 20, 30, 40, 50, 60, 70], 70),
            ([70, 60, 50, 40, 30, 20, 10], 0),
            ([], 0)]


@pytest.mark.parametrize("prices, expected",
                         prices_and_expected())
def test_max_revenue(prices, expected):
    from challenges.c048_maximum_profit import max_revenue, max_revenue_v2
    result = max_revenue(prices)
    assert expected == result
    result2 = max_revenue_v2(prices)
    assert expected == result2
