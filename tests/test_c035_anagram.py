import pytest


@pytest.mark.parametrize("str1, str2, expected",
                         [("Otto", "Toto", True),
                          ("Mary", "Army", True),
                          ("Ananas", "Bananas", False)])
def test_is_anagram(str1, str2, expected):
    from challenges.c035_anagram import is_anagram, is_anagram_v2
    assert is_anagram(str1, str2) == expected
    assert is_anagram_v2(str1, str2) == expected
