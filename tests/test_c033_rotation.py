import pytest


@pytest.mark.parametrize("str1, str2, expected",
                         [("ABCD", "ABC", True),
                          ("ABCDEF", "EFAB", True),
                          ("BCDE", "EC", False),
                          ("Challenge", "GECH", True)])
def test_contains_rotation(str1, str2, expected):
    from challenges.c033_rotation import contains_rotation
    assert contains_rotation(str1, str2) == expected
