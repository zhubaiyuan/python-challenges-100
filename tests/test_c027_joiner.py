import pytest


@pytest.mark.parametrize("values, delimiter, expected",
                         [(["hello", "world", "message"], " +++ ", "hello +++ world +++ message"),
                          (["Micha", "Zürich"], " likes ", "Micha likes Zürich")])
def test_join(values, delimiter, expected):
    from challenges.c027_joiner import join, join_v2
    assert join(values, delimiter) == expected
    assert join_v2(values, delimiter) == expected
