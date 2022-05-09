import pytest
import numpy as np

from challenges.c060_palindrome import is_palindrome, is_palindrome_v2, is_palindrome_v3, is_palindrome_v4


def values_and_expected():
    return [(["Ein", "Test", " -- ", "Test", "Ein"], True),
            (["Max", "Mike", "Mike", "Max"], True),
            (["Tim", "Tom", "Mike", "Max"], False)]


@pytest.mark.parametrize("values, expected", values_and_expected())
def test_is_palindrome(values, expected):
    result = is_palindrome(values)
    assert result == expected
    result2 = is_palindrome_v2(values)
    assert result2 == expected
    result3 = is_palindrome_v3(values)
    assert result3 == expected
    result4 = is_palindrome_v4(values)
    assert result4 == expected


@pytest.mark.parametrize("values, expected",
                         [(np.array(["Ein", "Test", " -- ", "Test", "Ein"]), True),
                          (np.array(["Max", "Mike", "Mike", "Max"]), True),
                          (np.array(["Tim", "Tom", "Mike", "Max"]), False)])
def test_is_palindrome_using_np(values, expected):
    result = is_palindrome(values)
    assert result == expected
    result2 = is_palindrome_v2(values)
    assert result2 == expected
    result3 = is_palindrome_v3(values)
    assert result3 == expected
    result4 = is_palindrome_v4(values)
    assert result4.any() == expected
