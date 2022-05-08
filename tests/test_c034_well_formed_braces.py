import pytest


@pytest.mark.parametrize("input, expected",
                         [("(())", True),
                          ("()()", True),
                          ("(()))((())", False),
                          ("(()", False),
                          (")()", False)])
def test_check_braces(input, expected):
    from challenges.c034_well_formed_braces import check_braces
    assert check_braces(input) == expected
