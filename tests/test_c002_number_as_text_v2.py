import unittest
from parameterized import parameterized


class NumberAsTextTest(unittest.TestCase):
    @parameterized.expand(
        [(7, "SEVEN"),
         (42, "FOUR TWO"),
         (7271, "SEVEN TWO SEVEN ONE"),
         (24680, "TWO FOUR SIX EIGHT ZERO"),
         (13579, "ONE THREE FIVE SEVEN NINE")])
    def test_number_as_text(self, n, expected):
        from challenges.c002_number_as_text import number_as_text, number_as_text_v2, number_as_text_v3
        result = number_as_text(n)
        self.assertEqual(expected, result)
        result2 = number_as_text_v2(n)
        self.assertEqual(expected, result2)
        result3 = number_as_text_v3(n)
        self.assertEqual(expected, result3)


if __name__ == '__main__':
    unittest.main()
