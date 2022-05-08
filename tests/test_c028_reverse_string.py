import pytest


@pytest.mark.parametrize("input, expected",
                         [("ABCD", "DCBA"),
                          ("OTTO", "OTTO"),
                          ("PETER", "RETEP")])
def test_reverse(input, expected):
    from challenges.c028_reverse_string import reverse, reverse_v2, reverse_v3
    assert reverse(input) == expected
    assert reverse_v2(input) == expected
    assert reverse_v3(input) == expected
