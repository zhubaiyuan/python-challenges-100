import unittest
from parameterized import parameterized


class PrimeNumberPairsTest(unittest.TestCase):
    @parameterized.expand(
        [(2, {3: 5, 5: 7, 11: 13, 17: 19, 29: 31, 41: 43}),
         (4, {3: 7, 7: 11, 13: 17, 19: 23, 37: 41, 43: 47}),
         (6, {5: 11, 7: 13, 11: 17, 13: 19, 17: 23, 23: 29, 31: 37, 37: 43, 41: 47, 47: 53})])
    def test_calc_pairs(self, n, expected):
        from challenges.c005_prime_number_pairs_v3 import calc_pairs
        max_value = 50
        result = calc_pairs(max_value, n)
        self.assertEqual(expected, result)
