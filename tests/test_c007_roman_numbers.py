import pytest
import csv


def arabic_to_roman_number_map():
    return [(1, "I"), (2, "II"), (3, "III"), (4, "IV"),
            (5, "V"), (7, "VII"), (9, "IX"), (17, "XVII"),
            (40, "XL"), (90, "XC"), (400, "CD"), (444, "CDXLIV"),
            (500, "D"), (900, "CM"), (1000, "M"), (1666, "MDCLXVI"),
            (1971, "MCMLXXI"), (2018, "MMXVIII"), (2019, "MMXIX"),
            (2020, "MMXX"), (3000, "MMM")]


@pytest.mark.parametrize("expected, roman_number",
                         arabic_to_roman_number_map())
def test_from_roman_number(roman_number, expected):
    from challenges.c007_roman_numbers import from_roman_number, from_roman_number_v1
    assert from_roman_number(roman_number) == expected
    assert from_roman_number_v1(roman_number) == expected


@pytest.mark.parametrize("roman_number, expected",
                         arabic_to_roman_number_map())
def test_to_roman_number(roman_number, expected):
    from challenges.c007_roman_numbers import to_roman_number, to_roman_number_v1
    assert to_roman_number(roman_number) == expected
    assert to_roman_number_v1(roman_number) == expected


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


@pytest.mark.parametrize("expected, roman_number",
                         arabic_to_roman_number_map_v1())
def test_from_roman_number(roman_number, expected):
    from challenges.c007_roman_numbers import from_roman_number, from_roman_number_v1
    assert from_roman_number(roman_number) == expected
    assert from_roman_number_v1(roman_number) == expected


@pytest.mark.parametrize("roman_number, expected",
                         arabic_to_roman_number_map_v1())
def test_to_roman_number(roman_number, expected):
    from challenges.c007_roman_numbers import to_roman_number, to_roman_number_v1
    assert to_roman_number(roman_number) == expected
    assert to_roman_number_v1(roman_number) == expected
