import pytest


def input_and_expected():
    return [(2, [2]),
            (3, [2, 3]),
            (10, [2, 3, 5, 7]),
            (15, [2, 3, 5, 7, 11, 13]),
            (20, [2, 3, 5, 7, 11, 13, 17, 19]),
            (25, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
            (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])]


@pytest.mark.parametrize("n, expected",
                         input_and_expected())
def test_calc_primes_up_to(n, expected):
    from challenges.c004_prime_numbers import calc_primes_up_to, calc_primes_up_to_v2
    assert calc_primes_up_to(n) == expected
    assert calc_primes_up_to_v2(n) == expected


@pytest.mark.parametrize("n, expected",
                         [(2, True),
                          (3, True),
                          (4, False),
                          (5, True),
                          (6, False),
                          (7, True)])
def test_is_prime(n, expected):
    from challenges.c004_prime_numbers import is_prime
    assert is_prime(n) == expected
