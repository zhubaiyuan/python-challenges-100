import pytest


@pytest.mark.parametrize("input, expected",
                         [("bananas", "bans"),
                          ("lalalamama", "lam"),
                          ("MICHAEL", "MICHAEL")])
def test_remove_duplicates(input, expected):
    from challenges.c031_remove_duplicate_letters import remove_duplicates
    assert remove_duplicates(input) == expected
