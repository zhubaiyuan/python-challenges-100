import pytest


def input_and_expected():
    return [("Otto", False),
            ("Adrian", False),
            ("Micha", True),
            ("ABCDEFG", True)]


@pytest.mark.parametrize("input, expected", input_and_expected())
def test_check_no_duplicate_chars(input, expected):
    from challenges.c030_no_duplicate_chars import check_no_duplicate_chars, check_no_duplicate_chars_v2
    assert check_no_duplicate_chars(input) == expected
    assert check_no_duplicate_chars_v2(input) == expected
