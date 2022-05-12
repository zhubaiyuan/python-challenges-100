import pytest

from challenges.c078_all_palindrome_substrings import all_palindrome_parts, all_palindrome_parts_v2, all_palindrome_parts_v3, longest_palindrome_part


def input_and_expected():
    return [
        ("BCDEDCB", {"BCDEDCB", "CDEDC", "DED"}),
        ("ABALOTTOLL", {"ABA", "LL", "LOTTOL", "OTTO", "TT"}),
        ("racecar", {"aceca", "cec", "racecar"})]


@pytest.mark.parametrize("input, expected",
                         input_and_expected())
def test_all_palindrome_parts_recs(input, expected):
    result = all_palindrome_parts(input)
    assert result == expected
    result2 = all_palindrome_parts_v2(input)
    assert result2 == expected
    result3 = all_palindrome_parts_v3(input)
    assert result3 == expected


@pytest.mark.parametrize("input, expected",
                         [("ABALOTTOLL", "LOTTOL"),
                          ("dreh_malam_herd", "dreh_malam_herd"),
                          ("abc_XYZYX_def", "_XYZYX_")])
def test_longest_palindrome(input, expected):
    longest = longest_palindrome_part(input)
    assert longest == expected
