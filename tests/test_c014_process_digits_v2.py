import unittest
from parameterized import parameterized


class ProcessDigitsTest(unittest.TestCase):
    @parameterized.expand(
        [(1234, 4),
         (1234567, 7)])
    def test_count_digits(self, number, expected):
        from challenges.c014_process_digits import count_digits, count_digits_v2, count_digits_v3
        result = count_digits(number)
        self.assertEqual(result, expected)
        result2 = count_digits_v2(number)
        self.assertEqual(result2, expected)
        result3 = count_digits_v3(number)
        self.assertEqual(result3, expected)

    @parameterized.expand(
        [(1234, 10),
         (1234567, 28)])
    def test_calc_sum_of_digits(self, number, expected):
        from challenges.c014_process_digits import calc_sum_of_digits, calc_sum_of_digits_v2, calc_sum_of_digits_v3
        result = calc_sum_of_digits(number)
        self.assertEqual(result, expected)
        result2 = calc_sum_of_digits_v2(number)
        self.assertEqual(result2, expected)
        result3 = calc_sum_of_digits_v3(number)
        self.assertEqual(result3, expected)

    def test_calc_digits_wrong_input(self):
        from challenges.c014_process_digits import count_digits
        with self.assertRaises(Exception) as excinfo:
            count_digits(-1)
        self.assertTrue("value must be >= 0" in str(excinfo.exception))

    def test_calc_digits_v2_wrong_input(self):
        from challenges.c014_process_digits import count_digits_v2
        with self.assertRaises(Exception) as excinfo:
            count_digits_v2(-1)
        self.assertTrue("value must be >= 0" in str(excinfo.exception))

    def test_calc_digits_v3_wrong_input(self):
        from challenges.c014_process_digits import count_digits_v3
        with self.assertRaises(Exception) as excinfo:
            count_digits_v3(-1)
        self.assertTrue("value must be >= 0" in str(excinfo.exception))

    def test_calc_sum_of_digits_wrong_input(self):
        from challenges.c014_process_digits import calc_sum_of_digits
        with self.assertRaises(Exception) as excinfo:
            calc_sum_of_digits(-1)
        self.assertTrue("value must be >= 0" in str(excinfo.exception))

    def test_calc_sum_of_digits_v2_wrong_input(self):
        from challenges.c014_process_digits import calc_sum_of_digits_v2
        with self.assertRaises(Exception) as excinfo:
            calc_sum_of_digits_v2(-1)
        self.assertTrue("value must be >= 0" in str(excinfo.exception))

    def test_calc_sum_of_digits_v3_wrong_input(self):
        from challenges.c014_process_digits import calc_sum_of_digits_v3
        with self.assertRaises(Exception) as excinfo:
            calc_sum_of_digits_v3(-1)
        self.assertTrue("value must be >= 0" in str(excinfo.exception))


if __name__ == '__main__':
    unittest.main()
