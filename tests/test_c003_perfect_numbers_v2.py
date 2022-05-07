import unittest
from parameterized import parameterized


class PerfectNumbersTest(unittest.TestCase):
    @parameterized.expand(
        [(6, True),
         (28, True),
         (496, True),
         (8128, True)])
    def test_is_perfect_number(self, n, expected):
        from challenges.c003_perfect_numbers import is_perfect_number, is_perfect_number_v2
        result = is_perfect_number(n)
        self.assertEqual(expected, result)
        result2 = is_perfect_number_v2(n)
        self.assertEqual(expected, result2)

    @parameterized.expand(
        [(50, [6, 28]),
         (1000, [6, 28, 496]),
         (10000, [6, 28, 496, 8128])])
    def test_calc_perfect_numbers(self, n, expected):
        from challenges.c003_perfect_numbers import calc_perfect_numbers, calc_perfect_numbers_v2
        result = calc_perfect_numbers(n)
        self.assertEqual(expected, result)
        result2 = calc_perfect_numbers_v2(n)
        self.assertEqual(expected, result2)


if __name__ == '__main__':
    unittest.main()
