import pytest


@pytest.mark.parametrize("input, expected",
                         [("Otto", True),
                          ("ABCBX", False),
                          ("ABCXcba", True)])
def test_is_palindrome(input, expected):
    from challenges.c029_palindrome import is_palindrome, is_palindrome_v2, is_palindrome_v3, is_palindrome_v4
    assert is_palindrome(input) == expected
    assert is_palindrome_v2(input) == expected
    assert is_palindrome_v3(input) == expected
    assert is_palindrome_v4(input) == expected


@pytest.mark.parametrize("input, expected",
                         [("Dreh mal am Herd.", True),
                          ("Das ist kein Palindrom!", False)])
def test_is_palindrome_ignore(input, expected):
    from challenges.c029_palindrome import is_palindrome_ignore, is_palindrome_ignore_v2
    ignore_spaces_and_punctuation = True
    assert is_palindrome_ignore(
        input, ignore_spaces_and_punctuation) == expected
    assert is_palindrome_ignore_v2(
        input, ignore_spaces_and_punctuation) == expected
