import pytest


@pytest.mark.parametrize("value, expected",
                         [(5, "101"),
                          (7, "111"),
                          (22, "10110"),
                          (42, "101010"),
                          (256, "100000000")])
def test_to_binary(value, expected):
    from challenges.c019_conversions import to_binary, from_binary
    assert to_binary(value) == expected
    assert from_binary(expected) == value


@pytest.mark.parametrize("value, expected",
                         [(42, "52"),
                          (7, "7"),
                          (8, "10")])
def test_to_octal(value, expected):
    from challenges.c019_conversions import to_octal, from_octal
    assert to_octal(value) == expected
    assert from_octal(expected) == value


@pytest.mark.parametrize("value, expected",
                         [(77, "4D"),
                          (15, "F"),
                          (16, "10")])
def test_to_hex(value, expected):
    from challenges.c019_conversions import to_hex, from_hex
    assert to_hex(value) == expected
    assert from_hex(expected) == value
