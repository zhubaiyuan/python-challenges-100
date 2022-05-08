import pytest


@pytest.mark.parametrize("input, expected",
                         [("+123", 123),
                          ("-123", -123),
                          ("123", 123),
                          ("7271", 7271)])
def test_str_to_number(input, expected):
    from challenges.c040_conversion_str_to_number import str_to_number, str_to_number_v2
    assert str_to_number(input) == expected
    assert str_to_number_v2(input) == expected


def test_str_to_number_invalid_input_chars():
    from challenges.c040_conversion_str_to_number import str_to_number_v2
    with pytest.raises(ValueError) as excinfo:
        str_to_number_v2("ABC")
    assert "contains not only digits" in str(excinfo.value)


def test_str_to_number_invalid_input_chars():
    from challenges.c040_conversion_str_to_number import str_to_number_v3
    with pytest.raises(ValueError) as excinfo:
        str_to_number_v3("ABC")
    assert "contains not only digits" in str(excinfo.value)


@pytest.mark.parametrize("input, expected",
                         [("+123", 123),
                          ("-123", -123),
                          ("123", 123),
                          ("7271", 7271),
                          ("+0o77", 63),
                          ("-0o77", -63),
                          ("0o77", 63),
                          ("+0o123", 83),
                          ("-0o123", -83),
                          ("0o123", 83)])
def test_str_to_number_v3(input, expected):
    from challenges.c040_conversion_str_to_number import str_to_number_v3
    assert str_to_number_v3(input) == expected


def test_str_to_number_invalid_input_large_digit():
    from challenges.c040_conversion_str_to_number import str_to_number_v3
    with pytest.raises(ValueError) as excinfo:
        str_to_number_v3("0o128")
    assert str(excinfo.value).find("found digit >= 8") != -1
