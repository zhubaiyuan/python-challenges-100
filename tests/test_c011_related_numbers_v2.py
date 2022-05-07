import unittest
from parameterized import parameterized


class RalatedNumbersTest(unittest.TestCase):
    @parameterized.expand(
        [(250, {220: 284}),
         (300, {220: 284, 284: 220}),
         (2_000, {220: 284, 284: 220, 1_184: 1_210, 1_210: 1_184})])
    def test_calc_friends(self, max_exclusive, friends):
        from challenges.c011_related_numbers import calc_friends
        result = calc_friends(max_exclusive)
        self.assertEqual(result, friends)


if __name__ == '__main__':
    unittest.main()
