import unittest
from parameterized import parameterized


class PrimeNumbersTest(unittest.TestCase):
    @parameterized.expand(
        [(10, [2, 3, 5, 7]),
         (15, [2, 3, 5, 7, 11, 13]),
         (20, [2, 3, 5, 7, 11, 13, 17, 19]),
         (25, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
         (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])])
    def test_calc_primes_up_to(self, n, expected):
        from challenges.c004_prime_numbers import calc_primes_up_to, calc_primes_up_to_v2
        result = calc_primes_up_to(n)
        self.assertEqual(expected, result)
        result2 = calc_primes_up_to_v2(n)
        self.assertEqual(expected, result2)

    @parameterized.expand(
        [(2, True),
         (3, True),
         (4, False),
         (5, True),
         (6, False),
         (7, True)])
    def test_is_prime(self, n, expected):
        from challenges.c004_prime_numbers import is_prime
        result = is_prime(n)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
