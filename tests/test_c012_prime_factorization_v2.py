import unittest
from parameterized import parameterized


def value_and_prime_factors():
    return [(8, [2, 2, 2]),
            (14, [2, 7]),
            (42, [2, 3, 7]),
            (1155, [3, 5, 7, 11]),
            (2222, [2, 11, 101])]


class PrimeFactorizationTest(unittest.TestCase):
    @parameterized.expand(value_and_prime_factors())
    def test_calc_prime_factors(self, value, primefactors):
        from challenges.c012_prime_factorization import calc_prime_factors, calc_prime_factors_v2
        result = calc_prime_factors(value)
        self.assertEqual(result, primefactors)
        result1 = calc_prime_factors_v2(value)
        self.assertEqual(result1, primefactors)


if __name__ == '__main__':
    unittest.main()
