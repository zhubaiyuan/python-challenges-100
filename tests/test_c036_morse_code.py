import pytest


@pytest.mark.parametrize("input, expected",
                         [("SOS", ". . .   - - -   . . ."),
                          ("TWEET", "-   . - -   .   .   -"),
                          ("OST", "- - -   . . .   -"),
                          ("WEST", ". - -   .   . . .   -")])
def test_to_morse_code(input, expected):
    from challenges.c036_morse_code import to_morse_code, to_morse_code_v2, to_morse_code_v3
    assert to_morse_code(input) == expected
    assert to_morse_code_v2(input) == expected
    assert to_morse_code_v3(input) == expected
