import pytest


@pytest.mark.parametrize("input, expected",
                         [("A", "A"),
                          ("ABC", "CBA"),
                          ("abcdefghi", "ihgfedcba")])
def test_reverse_string(input, expected):
    from challenges.c016_reverse_string import reverse_string
    assert reverse_string(input) == expected
