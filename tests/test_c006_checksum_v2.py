import unittest
from parameterized import parameterized


class Ex06_CalcChecksum_Test(unittest.TestCase):
    @parameterized.expand(
        [("11111", 5),
         ("22222", 0),
         ("111111", 1),
         ("12345678", 4),
         ("87654321", 0)])
    def test_calc_checksum(self, n, expected):
        from challenges.c006_checksum import calc_checksum
        result = calc_checksum(n)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
