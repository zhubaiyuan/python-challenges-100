import pytest


@pytest.mark.parametrize("value, expected",
                         [("10101", True),
                          ("222", False),
                          ("12345", False)])
def test_is_binary_number(value, expected):
    from challenges.c026_number_conversions import is_binary_number, is_binary_number_v2, is_binary_number_v3, is_binary_number_v4
    assert is_binary_number(value) == expected
    assert is_binary_number_v2(value) == expected
    assert is_binary_number_v3(value) == expected
    assert is_binary_number_v4(value) == expected


@pytest.mark.parametrize("value, expected",
                         [("111", 7),
                          ("1010", 10),
                          ("1111", 15),
                          ("10000", 16)])
def test_binary_to_decimal(value, expected):
    from challenges.c026_number_conversions import binary_to_decimal
    assert binary_to_decimal(value) == expected


@pytest.mark.parametrize("value, expected",
                         [("7", 7),
                          ("A", 10),
                          ("F", 15),
                          ("10", 16)])
def test_hex_to_decimal(value, expected):
    from challenges.c026_number_conversions import hex_to_decimal
    assert hex_to_decimal(value) == expected
