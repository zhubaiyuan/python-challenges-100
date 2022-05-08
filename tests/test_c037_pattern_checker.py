import pytest


@pytest.mark.parametrize("pattern, input, expected",
                         [("x", "", False),
                          ("", "x", False),
                          ("xyyx", "tim mike mike tim", True),
                          ("xyyx", "time mike tom tim", False),
                          ("xyxx", "tim mike mike tim", False),
                          ("xxxx", "tim tim tim tim", True)])
def test_matches_pattern_special_cases(pattern, input, expected):
    from challenges.c037_pattern_checker import matches_pattern
    assert matches_pattern(pattern, input) == expected
