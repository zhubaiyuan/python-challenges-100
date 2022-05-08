import pytest

from challenges.c050_well_formed_braces import CheckResult


@pytest.mark.parametrize("values, expected",
                         [("()", True),
                          ("()[]{}", True),
                          ("[((()[]{}))]", True),
                          ("(()", False),
                          ("((})", False),
                          ("(()}", False),
                          (")()(", False),
                          ("()((", False),
                          ("()A(", False)])
def test_check_parentheses(values, expected):
    from challenges.c050_well_formed_braces import check_parentheses
    result = check_parentheses(values)
    assert expected == result


@pytest.mark.parametrize("values",
                         [("()"),
                          ("()[]{}"),
                          ("[((()[]{}))]")])
def test_check_parentheses_v2(values):
    from challenges.c050_well_formed_braces import check_parentheses_v2
    result = check_parentheses_v2(values)
    assert CheckResult.OK == result


@pytest.mark.parametrize("values, expected",
                         [("(()", CheckResult.ODD_LENGTH),
                          ("((})", CheckResult.MISMATCHING_PARENTHESIS),
                          ("(()}", CheckResult.MISMATCHING_PARENTHESIS),
                          (")()(", CheckResult.CLOSING_BEFORE_OPENING),
                          ("()((", CheckResult.REMAINING_OPENING),
                          ("()A(", CheckResult.INVALID_CHAR)])
def test_check_parentheses_v2_errors(values, expected):
    from challenges.c050_well_formed_braces import check_parentheses_v2
    result = check_parentheses_v2(values)
    assert expected == result
