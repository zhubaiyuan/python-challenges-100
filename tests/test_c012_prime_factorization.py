import pytest


def value_and_prime_factors():
    return [(8, [2, 2, 2]),
            (14, [2, 7]),
            (42, [2, 3, 7]),
            (1155, [3, 5, 7, 11]),
            (2222, [2, 11, 101])]


@pytest.mark.parametrize("value, primefactors", value_and_prime_factors())
def test_calc_prime_factors(value, primefactors):
    from challenges.c012_prime_factorization import calc_prime_factors, calc_prime_factors_v2
    assert calc_prime_factors(value) == primefactors
    assert calc_prime_factors_v2(value) == primefactors
