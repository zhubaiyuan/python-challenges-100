import unittest
from parameterized import parameterized


class BasicArithmeticTest(unittest.TestCase):
    @parameterized.expand(
        [(6, 7, 0),
         (3, 4, 6),
         (5, 5, 5)])
    def test_calc(self, m, n, expected):
        from challenges.c001_basic_arithmetic import calc, calc_v2
        result = calc(m, n)
        self.assertEqual(expected, result)
        result2 = calc_v2(m, n)
        self.assertEqual(expected, result2)

    @parameterized.expand(
        [(3, {"sum": 2, "count": 1}),
         (8, {"sum": 19, "count": 4}),
         (15, {"sum": 63, "count": 8})])
    def test_calc_sum_and_count_all_numbers_div_by_2_or_7(self, n, expected):
        from challenges.c001_basic_arithmetic import calc_sum_and_count_all_numbers_div_by_2_or_7_v2
        result = calc_sum_and_count_all_numbers_div_by_2_or_7_v2(n)
        self.assertEqual(expected, result)

    @parameterized.expand(
        [(1, False),
         (2, True),
         (3, False),
         (4, True)])
    def test_is_even(self, n, expected):
        from challenges.c001_basic_arithmetic import is_even
        result = is_even(n)
        self.assertEqual(expected, result)

    @parameterized.expand(
        [(1, True),
         (2, False),
         (3, True),
         (4, False)])
    def test_is_odd(self, n, expected):
        from challenges.c001_basic_arithmetic import is_odd
        result = is_odd(n)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
