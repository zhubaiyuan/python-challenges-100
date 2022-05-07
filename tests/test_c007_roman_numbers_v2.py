import unittest
import csv
from parameterized import parameterized


class RomanNumbersTest(unittest.TestCase):
    def arabic_to_roman_number_map():
        return [(1, "I"), (2, "II"), (3, "III"), (4, "IV"),
                (5, "V"), (7, "VII"), (9, "IX"), (17, "XVII"),
                (40, "XL"), (90, "XC"), (400, "CD"), (444, "CDXLIV"),
                (500, "D"), (900, "CM"), (1000, "M"), (1666, "MDCLXVI"),
                (1971, "MCMLXXI"), (2018, "MMXVIII"), (2019, "MMXIX"),
                (2020, "MMXX"), (3000, "MMM")]

    @parameterized.expand(arabic_to_roman_number_map())
    def test_from_roman_number(self, expected, roman_number):
        from challenges.c007_roman_numbers import from_roman_number, from_roman_number_v1
        result = from_roman_number(roman_number)
        self.assertEqual(expected, result)
        result1 = from_roman_number_v1(roman_number)
        self.assertEqual(expected, result1)

    @parameterized.expand(arabic_to_roman_number_map())
    def test_to_roman_number(self, roman_number, expected):
        from challenges.c007_roman_numbers import to_roman_number, to_roman_number_v1
        result = to_roman_number(roman_number)
        self.assertEqual(expected, result)
        result1 = to_roman_number_v1(roman_number)
        self.assertEqual(expected, result1)

    def arabic_to_roman_number_map_v1():
        result = []
        with open('arabicroman.csv', 'rt') as file:
            data = csv.reader(file)
            skip_first = True
            for row in data:
                if not skip_first:
                    result.append((int(row[0].strip()), row[1].strip()))
                skip_first = False
        return result

    @parameterized.expand(arabic_to_roman_number_map_v1())
    def test_from_roman_number(self, expected, roman_number):
        from challenges.c007_roman_numbers import from_roman_number, from_roman_number_v1
        result = from_roman_number(roman_number)
        self.assertEqual(expected, result)
        result1 = from_roman_number_v1(roman_number)
        self.assertEqual(expected, result1)

    @parameterized.expand(arabic_to_roman_number_map_v1())
    def test_to_roman_number(self, roman_number, expected):
        from challenges.c007_roman_numbers import to_roman_number, to_roman_number_v1
        result = to_roman_number(roman_number)
        self.assertEqual(expected, result)
        result1 = to_roman_number_v1(roman_number)
        self.assertEqual(expected, result1)


if __name__ == '__main__':
    unittest.main()
